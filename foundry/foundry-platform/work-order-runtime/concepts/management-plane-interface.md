# Management Plane Interface

> The protocol by which WO Runtime, as an in-session worker, communicates with Workspace Session Management on the Foundry management plane.

## What it is

WO Runtime runs inside a session pod provisioned by [Workspace Session Infrastructure](../../workspace-session-infrastructure/README.md). It does **not** create sessions — Session Management decides lifecycle; Session Infrastructure provisions the pod; WO Runtime boots and **acknowledges liveness** so the session can become Active.

The management plane interface is WO Runtime's **upward-facing contract** with Session Management. It is distinct from the user/local interface (IDE plugin API, `foundry workspace` CLI) that serves builders inside the session.

## Interface operations

| Operation | Direction | When |
|-----------|-----------|------|
| **Liveness acknowledgment** | WO Runtime → Session Management | On boot, within 30s of container start |
| **Heartbeat** | WO Runtime → Session Management | Every 15s while session is Active |
| **Stop/drain command** | Session Management → WO Runtime | Piggybacked on heartbeat response, or explicit command |
| **Shutdown acknowledgment** | WO Runtime → Session Management | After draining tasks on stop |
| **Health endpoint** | K8s → WO Runtime | `/health` for readiness/liveness probes |

### Liveness acknowledgment

On boot, WO Runtime sends:

```yaml
POST /api/v1/sessions/{session-id}/ack
request:
  wo_runtime_version: string
  pod_ip: string
  api_port: 9090
```

Session Management transitions the session to **Active** only after receiving this ack (and after Session Infrastructure has reported pod-ready).

### Heartbeat

Every 15 seconds, WO Runtime reports session-local metrics:

```yaml
POST /api/v1/sessions/{session-id}/heartbeat
request:
  active_wos: int
  active_agents: int
  cpu_usage_pct: float
  memory_usage_pct: float
response:
  command: null | "stop" | "drain"
```

Session Management may piggyback **stop** or **drain** commands on the heartbeat response. WO Runtime must honor these promptly.

### Shutdown

When draining completes (or timeout expires), WO Runtime sends:

```yaml
POST /api/v1/sessions/{session-id}/shutdown
request:
  reason: "user-requested" | "admin-forced" | "idle-timeout" | "max-lifetime" | "drain-complete"
  pending_tasks: int
```

## Dual role

WO Runtime serves two masters:

1. **Management plane** — liveness, heartbeats, shutdown ack (this interface)
2. **Session user** — task execution, agent spawning, IDE/CLI (local interface)

## Related concepts

- [WO Runtime Daemon](wo-runtime-daemon.md) — process that implements both interfaces
- [Workspace Session](../../concepts/workspace-session.md) — platform concept
- [Session Lifecycle](../../workspace-session-management/concepts/session-lifecycle.md) — state machine WO Runtime participates in

## Further reading

- [../platform-developer-guide/requirements.md](../platform-developer-guide/requirements.md) — WOR-FR-0030 through WOR-FR-0033
- [../../workspace-session-management/platform-developer-guide/interface-contracts.md](../../workspace-session-management/platform-developer-guide/interface-contracts.md) — full API schemas
