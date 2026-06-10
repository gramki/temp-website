# Session Pod

The Session Pod is the Kubernetes pod that is the unit of Workspace Session infrastructure — one pod per active session, with storage, networking, and process supervision bound together.

## What it is

When Session Management requests provisioning, Session Infrastructure creates a pod (via Coder's Kubernetes provider) in the Foundry's session namespace. The pod encapsulates everything needed for an active session except lifecycle state, which Session Management owns.

```
┌─────────────────────────────────────────────────────────────────────────┐
│  Pod: session-{session-id}                                              │
│  namespace: foundry-{foundry-id}-sessions                                 │
│                                                                           │
│  initContainers:                                                          │
│  ┌─────────────────────┐  ┌─────────────────────┐                        │
│  │  workspace-merge    │  │  admin-overlay      │                        │
│  │  (Layer 2)          │  │  (Layer 3)          │                        │
│  └─────────────────────┘  └─────────────────────┘                        │
│                                                                           │
│  containers:                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐ │
│  │  workspace (single container)                                        │ │
│  │  supervisord → code-server (8080)                                    │ │
│  │              → wo-runtime (9090)                                     │ │
│  │              → raw-agent processes (on demand)                       │ │
│  └─────────────────────────────────────────────────────────────────────┘ │
│                                                                           │
│  volumes:                                                                 │
│  workspace-data (PVC) │ merged-content (emptyDir) │ skill-cache (emptyDir)│
└─────────────────────────────────────────────────────────────────────────┘
```

Key characteristics:

| Aspect | Detail |
|--------|--------|
| **Unit of provisioning** | One pod = one session instance |
| **Container model** | Single container with process supervision (not sidecar) |
| **Restart policy** | Always — K8s restarts on crash; PVC rebinds |
| **Readiness** | WO Runtime `/health` on port 9090 |
| **Labels** | `foundry.io/session-id`, `foundry.io/user`, `foundry.io/workspace-type`, `foundry.io/workbench` |

## Resource shape

Default resource limits are configurable per Foundry via `workspace_infrastructure.resource_defaults`:

| Resource | Default request | Default limit |
|----------|-----------------|---------------|
| CPU | 2 | 4 |
| Memory | 4Gi | 8Gi |
| Storage (PVC) | 20Gi | — |

Per-workspace-type overrides and namespace ResourceQuota cap concurrent sessions.

## Lifecycle mapping

Session Management state maps to Kubernetes primitives as follows:

| Session state | Pod | PVC | Ingress/URL |
|---------------|-----|-----|-------------|
| **Starting** | Creating / init running | Binding | Not yet routed |
| **Active** | Running, readiness OK | Bound | Coder proxy active |
| **Stopping** | Terminating (preStop hook) | Retained, unbound | Draining |
| **Stopped** | Deleted | Retained | Unavailable |
| **Archived** | Deleted | Snapshot taken, PVC deleted | Unavailable |
| **Deleted** | — | Snapshot deleted | — |

Stop deletes the pod but retains the PVC. Resume creates a new pod that rebinds the same PVC.

## Process supervision

The single `workspace` container runs supervisord as PID 1:

| Process | Port | Restart policy |
|---------|------|----------------|
| `code-server` | 8080 | autorestart=true |
| `wo-runtime` | 9090 | autorestart=true |
| `raw-agent-*` | — | on-demand, managed by WO Runtime via supervisor API |

A WO Runtime crash restarts only that process — Code Server continues serving the IDE. Container-level OOM kills both; K8s restarts the pod with PVC intact.

## Health and shutdown

| Probe | Target | Purpose |
|-------|--------|---------|
| **readinessProbe** | `http://localhost:9090/health` | Session ready for URL routing |
| **livenessProbe** | `http://localhost:9090/health` | Detect hung WO Runtime |
| **preStop hook** | SIGTERM to supervisord → graceful drain | 30s grace before forced kill (WSI-NFR-0004) |

## Where it lives in Foundry

| Module | Responsibility |
|--------|----------------|
| **Session Infrastructure** | Creates, monitors, deletes pods; manages PVC binding |
| **Session Management** | Decides when to provision/stop; tracks state |
| **Work Order Runtime** | Runs inside pod; provides health endpoint |
| **Coder** | Kubernetes provider creates pod from template |

## Related concepts

- [Platform Base Image](platform-base-image.md) — Container image the pod runs
- [Workspace Template](workspace-template.md) — Init container merge into pod
- [Admin Layering](admin-layering.md) — Admin overlay init container
- [Workspace Session](../../concepts/workspace-session.md) — Platform-wide session definition

## Further reading

- [../platform-developer-guide/pod-lifecycle.md](../platform-developer-guide/pod-lifecycle.md) — Probes, eviction, graceful shutdown
- [../platform-developer-guide/storage.md](../platform-developer-guide/storage.md) — PVC lifecycle
- [../platform-developer-guide/networking.md](../platform-developer-guide/networking.md) — Session URL routing
