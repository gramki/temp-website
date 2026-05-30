# Architecture Choices

Design decisions for Workspace Session Infrastructure. Each section documents options considered, trade-offs, and the chosen direction.

## 1. Coder vs raw Kubernetes pods

Do we run Coder (workspace provider model, template registry, dashboard) or deploy Code Server directly in pods managed by Session Infrastructure?

| Aspect | Coder | Raw Code Server in Pod |
|--------|-------|------------------------|
| Session resume (stop/start) | Built-in; Coder manages workspace state | Must build: delete pod, retain PVC, re-create pod on resume |
| Template registry | Coder templates (Terraform-based) | K8s manifests managed by Session Infrastructure directly |
| Dashboard / admin UI | Coder dashboard for session visibility | Must build in Foundry Web App or rely on Session Management API |
| Dotfiles sync | Built-in per-user | Must implement separately |
| Networking | Coder's built-in proxy (wildcard app routing) | Standard K8s Ingress (we control fully) |
| Licensing | Open-source (AGPLv3); enterprise features require license | No licensing concern |
| Abstraction layer | Adds a layer between Session Infrastructure and K8s | Direct K8s control; no intermediary |
| Multi-cluster | Coder supports multiple provisioners | Must build multi-cluster routing |
| Customization | Constrained by Coder's template model and lifecycle hooks | Full control over pod spec, init containers, volumes |

### DECISION: Coder as thin provisioner

Use Coder's workspace provisioner pointing at the K8s cluster (Coder's intended deployment model). This gives stop/start/resume, the proxy layer for session URLs, and dotfiles sync for free.

Constraints that keep Foundry in control:
- Session Infrastructure owns **template definitions** (Coder Kubernetes provider directly, not Terraform templates)
- Session Management is the **source of truth** for session state — not Coder's internal state
- WO Runtime still acks to Session Management — Coder's agent is not Foundry's WO Runtime; Coder ensures the container runs

**Escape path:** Replace Coder API calls with direct K8s pod creation. Pod spec and volumes are owned by Session Infrastructure either way.

→ [coder-on-kubernetes.md](../coder-on-kubernetes.md)

---

## 2. Single container vs sidecar architecture

Does WO Runtime run as a sidecar container alongside Code Server, or as a process within the same container?

| Aspect | Single Container | Sidecar |
|--------|-----------------|---------|
| Filesystem sharing | Trivial (same filesystem) | Requires shared volume mount |
| Independent restart | WO Runtime crash = container restart = Code Server restart | WO Runtime crash restarts only sidecar; Code Server unaffected |
| Resource accounting | Single resource limit for both | Independent CPU/memory limits |
| Health probes | One probe must cover both | Independent probes per container |
| Logging | Shared stdout; must demux | Separate log streams |
| Deployment coupling | Same image contains both | Can version/update independently |
| Complexity | Simpler pod spec; process supervision inside (supervisord) | More K8s-native; standard sidecar pattern |

### DECISION: Single container with process supervision

WO Runtime and Code Server run as processes within one container, managed by supervisord.

Rationale:
- Simpler pod spec and networking — no shared volume mounts for filesystem access
- WO Runtime and agents need direct access to the same workspace files
- Process supervision handles WO Runtime restarts independently (`autorestart=true`) without killing Code Server
- One container, one set of resource limits, one image
- Finer-grained isolation available later via cgroups within the container

→ [pod-lifecycle.md](../pod-lifecycle.md) — Pod spec
→ [../concepts/session-pod.md](../../concepts/session-pod.md)

---

## 3. Ingress-per-session vs shared ingress with path routing

| Aspect | Wildcard Subdomain | Path-based Routing |
|--------|-------------------|-------------------|
| URL format | `{session-id}.sessions.foundry.example.com` | `sessions.foundry.example.com/{session-id}/` |
| DNS | Wildcard A record | Single A record |
| TLS | Wildcard cert (one covers all) | Single cert for one domain |
| WebSocket | Clean (host-based routing works natively) | Requires path-stripping; Code Server base-path config |
| Code Server compatibility | Works out of the box (served at root `/`) | Requires `--base-path` flag; some extensions break |
| Ingress resource count | One per session (could be 1000s) | One shared Ingress |
| Coder compatibility | Coder's wildcard app routing uses this pattern | Coder does not support path-based routing |

### DECISION: Wildcard subdomain via Coder proxy

Code Server and Coder assume host-based routing. Path-based routing breaks extensions that construct absolute URLs.

With Coder's built-in proxy: one wildcard cert, one DNS record, Coder routes `{session-id}.sessions.{domain}` to the correct pod — **zero per-session Ingress objects**.

Fallback without Coder: single wildcard Ingress + ExternalDNS service discovery.

→ [networking.md](../networking.md)

---

## 4. Session Management: standalone service vs Management subsystem

| Aspect | Standalone Service | Management Subsystem |
|--------|-------------------|---------------------|
| Scaling driver | Heartbeats: 15s × N sessions = ~67/s per 1000 sessions | Coupled to Management's config-read load |
| Failure isolation | Session Management crash does not affect Validation, WCM | Shared fate with all Management subsystems |
| Event throughput | High-frequency (heartbeats + state events) | Mixes with Management's low-frequency config events |
| Latency | Heartbeat + query must be fast (200ms) | Management is less latency-sensitive |
| Data relationships | FK references to Foundry/Workbench/User (Management tables) | Natural join; same DB |
| Operational surface | +1 service to deploy and monitor | No additional deployment |

### DECISION: Standalone service, shared database, no FK constraints

Session Management is a standalone service (separate container, own scaling, own release cycle) sharing the same PostgreSQL instance but using its own schema/tables.

- References Foundry/Workbench/User by ID — **no foreign key constraints** to Management tables
- Logically coupled by convention, physically decoupled at schema level
- Deploy as separate container in same K8s namespace as Management

This decision affects Session Management (Phase 2), documented here because Session Infrastructure's interface contracts depend on Session Management being independently scalable.

→ [../../workspace-session-management/platform-developer-guide/design-discussions/standalone-vs-subsystem.md](../../workspace-session-management/platform-developer-guide/design-discussions/standalone-vs-subsystem.md) (Phase 2)

---

## 5. Image variant strategy

One image per workspace type (6 images) vs universal image with activation?

| Aspect | 6 Type-specific Images | Universal Image + Activation |
|--------|------------------------|------------------------------|
| Image size | Smaller per-type | Larger (union of all tools) |
| Build pipeline | 6 parallel builds | 1 build |
| Content overlap | ~95% shared | Naturally deduplicated |
| Workspace-type differences | Language runtimes, test frameworks, release tools | Activation via env var at session start |

### DECISION: Single base image + workspace-type activation at session start

Six workspace types share ~95% content. Differences (language runtimes for Dev, test frameworks for QA, signing tools for Release) are applied as an activation layer at session start via init container or activation scripts.

- Keeps build pipeline simple (one release artifact)
- Foundry admin Layer 3 overlay handles per-workspace customization using the same mechanism
- Activation cache pre-staged in image — no runtime network required

→ [container-image-spec.md](../container-image-spec.md)
→ [../../concepts/platform-base-image.md](../../concepts/platform-base-image.md)

---

## Summary

| # | Decision |
|---|----------|
| 1 | **Coder ok** — thin provisioner; Session Management owns lifecycle |
| 2 | **Single container** — supervisord manages Code Server + WO Runtime |
| 3 | **Wildcard ingress ok** — via Coder proxy; no per-session Ingress |
| 4 | **Session Management standalone** — shared DB, no FK (Phase 2 module) |
| 5 | **Single base image + activation** — not six separate images |

## Related documentation

- [../README.md](../README.md) — Module overview
- [requirements.md](../requirements.md) — Requirements derived from these decisions
