# Failure Modes

Failure scenarios, detection mechanisms, recovery strategies, and session state impact.

Session Infrastructure detects failures via Kubernetes informers, Coder workspace status, and provision timeouts. All failures are reported to Session Management as events — Session Infrastructure does not transition session state directly.

## Failure matrix

| Failure | Detection | Recovery | Session state impact |
|---------|-----------|----------|---------------------|
| **Pod crashes** | K8s restarts pod; informer emits `pod-restarting` | PVC retained; new pod binds same PVC; WO Runtime re-sends liveness ack | Transparent if ack within liveness timeout; Active → Unhealthy → Stopped if timeout exceeded |
| **Pod evicted (resource pressure)** | Pod phase `Failed`, reason `Evicted`; preStop hook fires | Emit `pod-failed`; Session Management may re-provision on different node | Stopping → may auto-restart per policy |
| **Cluster unreachable** | Provision request times out; K8s API connection failure | Session Management marks creation Failed; retries with backoff | Created → Failed |
| **WO Runtime fails to ack (timeout)** | Session Management liveness timeout (60s) expires | Session Management queries pod status via WSI; may force-restart | Active → Unhealthy → (restart or Stopped) |
| **Network partition (pod ↔ management plane)** | Heartbeat stops at Session Management | Session Management uses K8s API via WSI to verify pod; extends timeout if pod healthy | Depends on K8s-level pod status |
| **Image pull failure** | K8s `ImagePullBackOff` | Emit `pod-failed` with reason; Session Management marks Failed | Created → Starting → Failed |
| **PVC provision failure** | PVC status `Pending` (no storage) | Emit `pod-failed`; admin alerted | Created → Starting → Failed |
| **Node failure (pod running)** | Node `NotReady`; pod evicted or stuck | Pod rescheduled; liveness timeout may fire first | Active → Unhealthy → (rescheduled → Active, or Stopped) |
| **Provision timeout** | 90s elapsed without readiness probe pass | Emit `pod-failed` with reason `ProvisionTimeout` | Starting → Failed |
| **Quota exceeded** | K8s rejects pod create (ResourceQuota) | Emit `pod-failed`; admin must increase quota | Starting → Failed |

---

## Pod crash recovery

When a process exits or the container OOMs, Kubernetes restarts the pod (`restartPolicy: Always`).

```
Pod crash (OOM, process exit)
    │
    ├── K8s restarts pod
    │
    ├── WSI emits session-infrastructure.pod-restarting
    │
    ├── Init containers re-run (workspace-merge, admin-overlay)
    │
    ├── Main container starts (supervisord → code-server, wo-runtime)
    │
    └── WO Runtime sends liveness ack to Session Management
            │
            ├── Ack within 60s → remain Active
            │
            └── No ack within 60s → Unhealthy → query pod → Stopped or wait
```

Supervisord handles individual process crashes without container restart. Container-level OOM kills both Code Server and WO Runtime; K8s restarts the entire pod.

→ [sequence-diagrams.md](sequence-diagrams.md) — Pod crash recovery sequence

---

## Eviction and graceful shutdown

**WSI-NFR-0004:** Eviction triggers graceful shutdown via preStop hook.

```
Eviction or stop request
    │
    ├── K8s sends SIGTERM
    │
    ├── preStop: /opt/foundry/graceful-shutdown.sh
    │   ├── Signal supervisord
    │   ├── WO Runtime drains (coordinated with Session Management stop command)
    │   └── WO Runtime sends shutdown ack
    │
    ├── 30s grace period (terminationGracePeriodSeconds)
    │
    └── SIGKILL if not terminated
            │
            └── WSI emits pod-terminated or pod-failed (Evicted)
```

If WO Runtime cannot drain within grace period, Session Management records pending tasks from shutdown ack.

---

## Cluster unreachable

When the Kubernetes API is unreachable:

| Phase | Behavior |
|-------|----------|
| Provision in flight | Watch timeout → emit `pod-failed` with cluster error |
| New provision request | Return 503; Session Management retries with backoff |
| Existing running pods | WSI informer reconnects; no action unless pod events missed |

Foundry admin is alerted if cluster endpoint fails validation or remains unreachable.

---

## Image and storage failures

### ImagePullBackOff

Usually caused by incorrect registry credentials, missing image tag, or registry outage.

- WSI watches pod events for `Failed` + `ImagePullBackOff`
- Emits `pod-failed` after retry threshold (default: 3 minutes)
- Session Management marks session Failed
- Admin fixes registry config or image tag; Orchestrator may retry creation

### PVC Pending

StorageClass missing, quota exceeded, or cluster storage exhausted.

- WSI watches PVC events for prolonged `Pending` state (> 60s)
- Emits `pod-failed` with reason `StoragePending`
- Session cannot start until storage is available

---

## Network partition

When the pod loses connectivity to Session Management but remains running:

1. Heartbeats stop arriving at Session Management
2. Session Management calls `GET /api/v1/sessions/{id}/pod` via WSI
3. If pod is running and healthy, Session Management extends liveness timeout
4. If pod is gone or CrashLoopBackOff, transition to Stopped

WSI does not implement split-brain resolution — Session Management owns state decisions.

---

## Operational alerts

| Alert | Trigger | Owner |
|-------|---------|-------|
| Cluster unreachable | 3 consecutive provision failures | Foundry admin |
| Quota near limit | > 80% of namespace ResourceQuota | Foundry admin |
| CrashLoopBackOff rate | > 5 pod-failed events in 10 minutes | Platform ops |
| Provision latency | p95 > 90s | Platform ops |
| Storage exhaustion | PVC Pending > 5 minutes | Foundry admin |

---

## Related documentation

- [sequence-diagrams.md](sequence-diagrams.md) — Crash and stop recovery flows
- [interface-contracts.md](interface-contracts.md) — Event schemas
- [pod-lifecycle.md](pod-lifecycle.md) — Probes and graceful shutdown
- [requirements.md](requirements.md) — WSI-NFR-0001, WSI-NFR-0004
