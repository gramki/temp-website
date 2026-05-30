# Workspace Session Infrastructure Requirements

This document specifies detailed implementation requirements for the Workspace Session Infrastructure module.

## Key Concepts

| Concept | Link |
|---------|------|
| Workspace Session | [../../concepts/workspace-session.md](../../concepts/workspace-session.md) |
| Agent Model | [../../concepts/agent-model.md](../../concepts/agent-model.md) |
| Delegation | [../../concepts/delegation.md](../../concepts/delegation.md) |

Module-specific concepts:

| Concept | Link |
|---------|------|
| Platform Base Image | [../concepts/platform-base-image.md](../concepts/platform-base-image.md) |
| Admin Layering | [../concepts/admin-layering.md](../concepts/admin-layering.md) |
| Workspace Template | [../concepts/workspace-template.md](../concepts/workspace-template.md) |
| Session Pod | [../concepts/session-pod.md](../concepts/session-pod.md) |

## ACE alignment

| ACE concept | How this module realizes it |
|-------------|----------------------------|
| **Workspace Session** | Provisions K8s pod, PVC, URL, and storage |
| **Workspace** | Workspace type drives activation and resource defaults |
| **IDE** | Code Server and extensions ship in platform base image |

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     Foundry Management Plane                                 │
│  ┌──────────────────────┐         ┌──────────────────────────────────────┐  │
│  │ Session Management   │────────▶│ Workspace Session Infrastructure     │  │
│  │ (lifecycle control)  │ provision│ (K8s provisioning, URLs, images)    │  │
│  └──────────────────────┘         └──────────────────┬───────────────────┘  │
└──────────────────────────────────────────────────────┼──────────────────────┘
                                                       │
                                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│              Kubernetes Cluster (Foundry-admin-provided)                   │
│  namespace: foundry-{id}-sessions                                            │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │  Session Pod — single container (supervisord)                          │  │
│  │  init: workspace-merge │ admin-overlay                                 │  │
│  │  processes: code-server (8080) + wo-runtime (9090)                     │  │
│  │  PVC: workspace-data │ emptyDir: merged-content, skill-cache           │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│  Coder proxy → {session-id}.sessions.{ingress-domain}                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Functional Requirements

### Session Provisioning

**WSI-FR-0001:** Session Infrastructure SHALL spawn a session pod on the Kubernetes cluster provided by the Foundry admin.

| Aspect | Detail |
|--------|--------|
| Trigger | Provision request from Session Management |
| Cluster source | `workspace_infrastructure.kubernetes` in Foundry settings |
| Output | Pod, Service, PVC in `foundry-{id}-sessions` namespace |
| Provider | Coder Kubernetes workspace provider or direct K8s API |

**WSI-FR-0002:** Session Infrastructure SHALL return an accessible session URL to Session Management within the pod-ready timeout.

| Aspect | Detail |
|--------|--------|
| URL format | `https://{session-id}.sessions.{ingress-domain}` |
| Delivery | Asynchronous event: `session-infrastructure.pod-ready` |
| Timeout | Pod readiness probe must pass (see WSI-NFR-0001) |

### Workspace Layering

**WSI-FR-0003:** Session Infrastructure SHALL apply Foundry admin layers from `workspace-infrastructure/<workspace>/` as an overlay volume at session start.

| Aspect | Detail |
|--------|--------|
| Init container | `admin-overlay` |
| Source | Foundry Definition Repo |
| Mount | `/workspace/.foundry` (read-only) |

**WSI-FR-0004:** Session Infrastructure SHALL apply Workshop/Workbench workspace merge (scenarios, skills, devcontainer config) via init container.

| Aspect | Detail |
|--------|--------|
| Init container | `workspace-merge` |
| Source | Workshop Definition Repo |
| Output | `merged-content` emptyDir volume |

### Image and Workspace Types

**WSI-FR-0005:** Session Infrastructure SHALL support all six workspace types with type-specific activation on a single base image.

| Workspace type | Activation |
|----------------|------------|
| product-specification | Documentation and spec tooling |
| ux-design | Design tool CLIs |
| development | Language runtimes and build tools |
| qa | Test frameworks |
| release | Signing and publishing tools |
| governance | Policy and compliance tools |

### Coder Integration

**WSI-FR-0006:** Session Infrastructure SHALL configure Coder workspace provider to target the Foundry-admin-provided cluster.

| Aspect | Detail |
|--------|--------|
| Template owner | Session Infrastructure |
| State owner | Session Management (not Coder) |
| Proxy | Coder wildcard proxy for session URLs |

### Multi-Tenant Isolation

**WSI-FR-0007:** Session Infrastructure SHALL create a per-Foundry namespace if it does not exist and apply NetworkPolicies and RBAC.

| Aspect | Detail |
|--------|--------|
| Namespace | `foundry-{id}-sessions` |
| NetworkPolicy | Default-deny; allow ingress from Coder proxy only |
| RBAC | ServiceAccount per pod; provisioner identity for create/delete |

### Networking

**WSI-FR-0008:** Session Infrastructure SHALL generate unique, deterministic session URLs following the naming convention `{session-id}.sessions.{ingress-domain}`.

**WSI-FR-0011:** Session Infrastructure SHALL configure TLS termination at ingress/proxy for all session URLs.

| Aspect | Detail |
|--------|--------|
| TLS | Wildcard cert via cert-manager ClusterIssuer |
| WebSocket | Long-lived connections supported (3600s timeout) |

### Storage

**WSI-FR-0009:** Session Infrastructure SHALL provision a PVC for workspace persistence; bind to pod on start, retain on stop.

| Aspect | Detail |
|--------|--------|
| PVC name | `pvc-session-{session-id}` |
| Default size | 20Gi (configurable per Foundry) |
| Access mode | ReadWriteOnce |

**WSI-FR-0010:** Session Infrastructure SHALL reclaim PVC storage on session archive/delete.

| Aspect | Detail |
|--------|--------|
| Archive | Volume snapshot, then PVC delete |
| Delete | Snapshot and PVC both deleted |

### Resource Limits

**WSI-FR-0012:** Session Infrastructure SHALL configure pod resource limits (CPU, memory) per workspace type and Foundry quota.

| Aspect | Detail |
|--------|--------|
| Per-type defaults | See [pod-lifecycle.md](pod-lifecycle.md) |
| Quota enforcement | Namespace ResourceQuota |

---

## Non-Functional Requirements

**WSI-NFR-0001:** Pod ready (passing readiness probe) within 90 seconds of provision request.

| Aspect | Detail |
|--------|--------|
| Probe target | WO Runtime `GET /health:9090` |
| Failure action | Emit `session-infrastructure.pod-failed` |

**WSI-NFR-0002:** Session URL accessible within 10 seconds of pod readiness.

**WSI-NFR-0003:** Cross-Foundry network traffic blocked by NetworkPolicy (zero-trust).

**WSI-NFR-0004:** Pod eviction SHALL trigger graceful shutdown (preStop hook, 30s grace period).

| Aspect | Detail |
|--------|--------|
| Hook | `/opt/foundry/graceful-shutdown.sh` |
| Grace period | `terminationGracePeriodSeconds: 30` |

**WSI-NFR-0005:** Base image size target: under 4GB per workspace type (single image with activation cache).

**WSI-NFR-0006:** PVC storage default: 20GB per session (configurable per Foundry).

**WSI-NFR-0007:** Concurrent sessions per Foundry limited by namespace ResourceQuota.

---

## Related documentation

- [interface-contracts.md](interface-contracts.md) — API and event schemas
- [failure-modes.md](failure-modes.md) — Failure scenarios and recovery
- [sequence-diagrams.md](sequence-diagrams.md) — End-to-end flows
- [foundry-management-integration.md](foundry-management-integration.md) — Foundry settings schema
