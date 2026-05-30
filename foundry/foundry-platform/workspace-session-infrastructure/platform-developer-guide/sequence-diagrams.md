# Sequence Diagrams

End-to-end time-ordered flows for platform developers implementing Session Infrastructure, Session Management, WO Runtime, or Orchestrator participants.

## Session creation flow

Orchestrator requests a session; Session Management delegates provisioning to Session Infrastructure; WO Runtime acks liveness to activate the session.

```mermaid
sequenceDiagram
    participant ORC as Orchestrator
    participant WSM as Session Management
    participant WSI as Session Infrastructure
    participant K8S as Kubernetes
    participant WOR as WO Runtime

    ORC->>WSM: POST /sessions/create (user, workspace-type, workbench)
    WSM->>WSM: Create session record (state: Created)
    WSM->>WSI: POST /sessions/provision (session-id, foundry-id, ...)
    WSM->>WSM: Transition state: Starting
    WSI->>K8S: Create PVC, Pod, Service
    K8S-->>WSI: Pod scheduled
    K8S-->>K8S: Init containers run (workspace-merge, admin-overlay)
    K8S-->>K8S: Main container starts (Code Server + WO Runtime via supervisord)
    K8S-->>WSI: Readiness probe passes (WO Runtime /health)
    WSI-->>WSM: Event: pod-ready (session-url)
    WSM->>WSM: Store session URL
    WOR->>WSM: POST /sessions/{id}/ack (liveness acknowledgment)
    WSM->>WSM: Transition state: Active
    WSM-->>ORC: Event: session-activated (session-id, session-url)
    ORC->>ORC: Assign WO (write to Work repo)
    WOR->>WOR: Discover WO via polling/event
```

**Key timing constraints:**
- WSI-NFR-0001: Readiness probe passes within 90s of provision request
- WSI-NFR-0002: Session URL accessible within 10s of pod readiness
- WO Runtime sends liveness ack within 30s of container start (WOR-FR-0030)

---

## Session stop flow

Admin or policy triggers stop; WO Runtime drains; Session Infrastructure deletes pod and retains PVC.

```mermaid
sequenceDiagram
    participant Admin as Foundry Admin
    participant WSM as Session Management
    participant WOR as WO Runtime
    participant WSI as Session Infrastructure
    participant K8S as Kubernetes

    Admin->>WSM: POST /sessions/{id}/stop
    WSM->>WSM: Transition state: Stopping
    WSM->>WOR: Stop command (drain active tasks)
    WOR->>WOR: Drain: finish current task, block new tasks
    WOR-->>WSM: Shutdown acknowledgment
    WSM->>WSI: DELETE /sessions/{id}/pod
    WSI->>K8S: Delete Pod (PVC retained)
    K8S-->>WSI: Pod terminated
    WSI-->>WSM: Event: pod-terminated
    WSM->>WSM: Transition state: Stopped
    WSM-->>Admin: Event: session-stopped
```

**Grace period:** 30s preStop hook (WSI-NFR-0004). If drain exceeds grace period, WOR reports pending tasks in shutdown ack.

---

## Pod crash recovery flow

Kubernetes restarts the pod; WO Runtime re-acks; Session Management decides whether to remain Active or transition to Unhealthy/Stopped.

```mermaid
sequenceDiagram
    participant K8S as Kubernetes
    participant WSI as Session Infrastructure
    participant WSM as Session Management
    participant WOR as WO Runtime

    K8S->>K8S: Pod crashes (OOM, process exit, etc.)
    K8S->>K8S: Restart pod (restartPolicy: Always)
    K8S-->>WSI: Pod restarting event
    WSI-->>WSM: Event: pod-restarting (session-id)
    Note over WSM: Liveness timeout clock running (60s)
    K8S->>K8S: Init containers re-run
    K8S->>K8S: Main container starts
    WOR->>WSM: POST /sessions/{id}/ack (re-acknowledgment)
    WSM->>WSM: Reset liveness timer; remain Active
    Note over WSM: If ack does NOT arrive within 60s:
    WSM->>WSM: Transition: Active → Unhealthy
    WSM->>WSI: Query pod status via K8s API
    alt Pod running but WO Runtime unhealthy
        WSI-->>WSM: Pod exists, container running
        WSM->>WSM: Wait additional 30s for ack
    else Pod gone or CrashLoopBackOff
        WSI-->>WSM: Pod failed
        WSM->>WSM: Transition: Unhealthy → Stopped
    end
```

**PVC behavior:** Crash restart rebinds the same PVC. Init containers re-apply merge and overlay layers.

---

## Related documentation

- [interface-contracts.md](interface-contracts.md) — Event and API schemas referenced in flows
- [failure-modes.md](failure-modes.md) — Recovery strategies per failure type
- [pod-lifecycle.md](pod-lifecycle.md) — Probes and graceful shutdown details
- [../../workspace-session-management/platform-developer-guide/session-state-machine.md](../../workspace-session-management/platform-developer-guide/session-state-machine.md) — Session state transitions
