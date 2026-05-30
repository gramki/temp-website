# Coder on Kubernetes

Coder workspace provider configuration, template registration, API integration, and Code Server routing.

## Role of Coder

Session Infrastructure uses **Coder as a thin provisioner** — not as the source of truth for session lifecycle. Coder provides:

| Capability | How Foundry uses it |
|------------|---------------------|
| Kubernetes workspace provider | Creates and manages session pods from templates |
| Stop/start/resume | Pod delete + PVC retain without custom resume logic |
| Wildcard proxy | Routes `{session-id}.sessions.{domain}` to workspace pods |
| Dotfiles sync | Optional per-user workspace personalization |

Session Management owns session state. WO Runtime acks liveness to Session Management — Coder's agent is not Foundry's WO Runtime.

→ [design-discussions/architecture-choices.md](design-discussions/architecture-choices.md) — Coder vs raw K8s decision

## Deployment model

Coder runs as a platform-managed deployment in the management plane namespace (or a dedicated Coder namespace per cluster). Each Foundry-admin-provided cluster registers as a Coder workspace provisioner.

```
Session Infrastructure
    │
    ├── Registers Coder template per workspace type
    │
    ├── On provision: Coder API CreateWorkspace(session-id, template, params)
    │
    └── On stop: Coder API StopWorkspace(session-id)
            │
            ▼
    Coder Kubernetes Provider
            │
            ├── Creates Pod + Service in foundry-{id}-sessions
            │
            └── Registers workspace with Coder proxy for URL routing
```

**WSI-FR-0006:** Coder workspace provider targets the Foundry-admin-provided cluster endpoint from `workspace_infrastructure.kubernetes`.

## Template registration

Session Infrastructure owns template definitions. Templates use Coder's **Kubernetes provider directly** — not Terraform-based templates.

Each template specifies:

| Field | Value |
|-------|-------|
| Template name | `foundry-{workspace-type}` (e.g. `foundry-development`) |
| Provider | Kubernetes |
| Pod spec | From [pod-lifecycle.md](pod-lifecycle.md) — single container, init containers |
| Workspace name | `{session-id}` — matches URL hostname segment |
| Parameters | `foundry_id`, `workbench_id`, `user_id`, `workspace_type` |

Template registration is idempotent — Session Infrastructure upserts templates on platform release or Foundry config change.

```yaml
# Coder template parameter mapping (conceptual)
parameters:
  - name: session_id
    type: string
  - name: foundry_id
    type: string
  - name: workbench_id
    type: string
  - name: workspace_type
    type: string
    valid_values:
      - product-specification
      - ux-design
      - development
      - qa
      - release
      - governance
```

## Coder API integration

Session Infrastructure calls Coder's REST API for provisioning operations:

| Operation | Coder API | Session Infrastructure action |
|-----------|-----------|------------------------------|
| Create workspace | `POST /api/v2/workspaces` | Triggered by provision request from Session Management |
| Stop workspace | `POST /api/v2/workspaces/{id}/stop` | Triggered by pod delete request |
| Get workspace status | `GET /api/v2/workspaces/{id}` | Poll until running or failed |
| Delete workspace | `DELETE /api/v2/workspaces/{id}` | On session delete (after PVC cleanup) |

Coder API credentials are platform-managed. Session Infrastructure authenticates with a service token scoped to workspace creation in registered provisioners.

## Code Server routing

Coder's wildcard proxy maps session URLs to workspace pods:

```
https://{session-id}.sessions.{ingress-domain}
    │
    ▼
Coder ingress (wildcard TLS cert)
    │
    ▼
Coder proxy: resolve workspace name → pod Service
    │
    ▼
svc-session-{session-id}:8080 → code-server
```

No per-session Ingress objects are required. One wildcard DNS record and one wildcard certificate cover all sessions.

→ [networking.md](networking.md) — URL scheme, TLS, WebSocket

## Readiness coordination

Session Infrastructure watches Coder workspace status **and** Kubernetes readiness probes:

1. Coder reports workspace as `running`
2. Pod readiness probe passes (`GET /health:9090` on WO Runtime)
3. Session Infrastructure emits `session-infrastructure.pod-ready` with session URL

The session URL is constructed deterministically — Coder does not generate arbitrary URLs:

```
https://{session-id}.sessions.{ingress_domain}
```

**WSI-FR-0002:** URL returned to Session Management within pod-ready timeout.

## Cluster registration

For each Foundry cluster, Session Infrastructure ensures:

1. Coder Kubernetes provisioner registered with cluster endpoint and credentials
2. Provisioner credentials match or are equivalent to Session Infrastructure's K8s identity
3. Wildcard ingress configured for `*.sessions.{ingress_domain}`
4. Image pull secrets available in session namespace

→ [kubernetes-integration.md](kubernetes-integration.md) — Cluster connectivity and auth

## Escape path

If Coder introduces friction, Session Infrastructure can replace Coder API calls with direct Kubernetes API calls. The pod spec, volumes, and networking design are owned by Session Infrastructure either way — Coder is an execution layer, not a structural dependency.

Direct K8s mode uses per-session Services and optionally the fallback Ingress path documented in [networking.md](networking.md).

## Related documentation

- [kubernetes-integration.md](kubernetes-integration.md) — Cluster auth and Coder registration
- [networking.md](networking.md) — Wildcard proxy and TLS
- [pod-lifecycle.md](pod-lifecycle.md) — Pod spec Coder templates reference
- [requirements.md](requirements.md) — WSI-FR-0002, WSI-FR-0006, WSI-FR-0008
