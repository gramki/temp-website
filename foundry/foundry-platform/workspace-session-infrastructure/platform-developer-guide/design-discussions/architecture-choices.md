# Architecture Choices

Design decisions for Workspace Session Infrastructure. Each section documents options considered, the decision taken, and rationale.

> **Status:** Decisions marked **DECIDED** are normative for implementation. Options not selected remain documented as escape paths.

---

## 1. Coder vs raw Kubernetes pods

Do we run Coder (workspace provider, template registry, dashboard) or deploy Code Server directly in pods managed by Session Infrastructure?

| Aspect | Coder | Raw Code Server in Pod |
|--------|-------|------------------------|
| Session resume (stop/start) | Built-in; Coder manages workspace state | Must build: delete pod, retain PVC, re-create pod on resume |
| Template registry | Coder templates (Terraform-based) | K8s manifests managed by Session Infrastructure directly |
| Dashboard / admin UI | Coder dashboard for session visibility | Must build in Foundry Web App or rely on Session Management API |
| Dotfiles sync | Built-in per-user | Must implement separately |
| Networking | Coder's built-in proxy (wildcard app routing) | Standard K8s Ingress (full control) |
| Licensing | Open-source (AGPLv3); enterprise features require license | No licensing concern |
| Abstraction layer | Adds layer between Session Infrastructure and K8s | Direct K8s control; no intermediary |
| Multi-cluster | Coder supports multiple provisioners | Must build multi-cluster routing |
| Customization | Constrained by Coder's template model | Full control over pod spec, init containers, volumes |

### **DECIDED: Coder as thin provisioner**

Use Coder's workspace provisioner pointing at the Foundry-admin-provided K8s cluster. Session Infrastructure owns **template definitions** (Kubernetes provider directly, not Terraform templates). Session Management is the **source of truth** for session state — not Coder's internal state. WO Runtime acks to Session Management; Coder's agent is not Foundry's WO Runtime.

**Rationale:** Stop/start/resume and wildcard proxy routing come for free. Avoids rebuilding session resume and URL routing. Foundry retains control of lifecycle decisions and pod spec ownership.

**Escape path:** Replace Coder API calls with direct K8s calls. Pod spec, volumes, and networking are owned by Session Infrastructure either way.

→ [coder-on-kubernetes.md](../coder-on-kubernetes.md)

---

## 2. Single container vs sidecar architecture

Does WO Runtime run as a sidecar container alongside Code Server, or as a process within the same container?

| Aspect | Single Container | Sidecar |
|--------|-----------------|---------|
| Filesystem sharing | Trivial (same filesystem) | Requires shared volume mount |
| Independent restart | WO Runtime crash = supervisor restart; Code Server unaffected | WO Runtime crash restarts only sidecar |
| Resource accounting | Single resource limit for both | Independent CPU/memory limits |
| Health probes | One probe covers WO Runtime readiness | Independent probes per container |
| Logging | Shared stdout; must demux | Separate log streams |
| Deployment coupling | Same image contains both | Can version/update independently |
| Complexity | Simpler pod spec | Standard sidecar pattern |

### **DECIDED: Single container with process supervision**

Code Server, WO Runtime, and Raw Agent processes run in one container managed by supervisord. WO Runtime and agents need direct access to the same workspace files; shared filesystem is the natural model. Supervisord handles independent process restarts (`autorestart=true`) without killing Code Server.

**Rationale:** Simpler pod spec and networking. One container, one set of resource limits, one image. Process-level crashes handled by supervisor; container-level OOM handled by K8s pod restart with PVC intact.

**Future option:** cgroups at process level within the container if finer-grained resource isolation is needed.

→ [pod-lifecycle.md](../pod-lifecycle.md) — Pod spec and supervisord layout

---

## 3. Ingress-per-session vs wildcard subdomain

| Aspect | Wildcard Subdomain | Path-based Routing |
|--------|-------------------|-------------------|
| URL format | `{session-id}.sessions.foundry.example.com` | `sessions.foundry.example.com/{session-id}/` |
| DNS | Wildcard A record | Single A record |
| TLS | Wildcard cert (one covers all) | Single cert for one domain |
| WebSocket | Clean (host-based routing) | Requires path-stripping; Code Server base-path config |
| Code Server compatibility | Works out of the box | Requires `--base-path`; extensions break |
| Ingress resource count | One per session (without Coder) | One shared Ingress |
| Coder compatibility | Coder's wildcard routing uses this pattern | Coder does not support path-based routing |

### **DECIDED: Wildcard subdomain via Coder proxy**

Session URLs follow `{session-id}.sessions.{ingress-domain}`. One wildcard DNS record and one wildcard certificate. Coder proxy routes by workspace name — **zero per-session Ingress objects**.

**Rationale:** Code Server and Coder assume host-based routing. Path-based routing breaks extensions that construct absolute URLs. Coder proxy eliminates the "thousands of Ingress objects" concern.

**Escape path:** Single wildcard Ingress with ExternalDNS + service discovery if Coder is removed.

→ [networking.md](../networking.md)

---

## 4. Session Management: standalone service vs Management subsystem

| Aspect | Standalone Service | Management Subsystem |
|--------|-------------------|---------------------|
| Scaling driver | Heartbeats: 15s × N sessions | Coupled to Management config-read load |
| Failure isolation | Session Mgmt crash does not affect Validation, WCM | Shared fate with all Management subsystems |
| Event throughput | High-frequency heartbeats + state events | Mixes with low-frequency config events |
| Latency | Heartbeat + query must be fast (200ms) | Management less latency-sensitive |
| Data relationships | FK references by ID only | Natural join; same DB with FKs |
| Operational surface | +1 service to deploy | No additional deployment |

### **DECIDED: Standalone service, shared database, no FK constraints**

Session Management deploys as a separate container with its own schema in the same PostgreSQL instance. References Foundry/Workbench/User by ID — no foreign key constraints to Management tables. Deploy in the same K8s namespace as Management.

**Rationale:** Heartbeat throughput (~67/s per 1000 sessions) and failure isolation. A bug in liveness timeout logic should not take down Validation or WCM. Easy to extract to its own database later.

*Note: This decision applies to Session Management, documented here for cross-module context.*

→ [../../workspace-session-management/platform-developer-guide/design-discussions/standalone-vs-subsystem.md](../../workspace-session-management/platform-developer-guide/design-discussions/standalone-vs-subsystem.md)

---

## 5. Image variant strategy

One image per workspace type (6 images) vs universal image with activation?

| Aspect | 6 Type-specific Images | Universal Image + Activation |
|--------|------------------------|------------------------------|
| Image size | Smaller per-type | Larger (union of all tools) |
| Build pipeline | 6 parallel builds | 1 build |
| Content overlap | ~95% shared | Naturally deduplicated |
| Workspace-type differences | Language runtimes, test frameworks, signing tools | Activation via env var + init script |

### **DECIDED: Single base image + workspace-type activation at session start**

Six workspace types share ~95% content. Differences (language runtimes for Dev, test frameworks for QA, signing tools for Release) are applied as an activation layer at session start via init container or devcontainer features. Foundry admin Layer 3 overlay handles per-workspace customization using the same mechanism.

**Rationale:** Simple build pipeline. Activation caches baked into the image keep startup fast without network fetch. Type-specific tooling remains available without maintaining six separate image build pipelines.

→ [container-image-spec.md](../container-image-spec.md)
→ [../../concepts/platform-base-image.md](../../concepts/platform-base-image.md)

---

## Decision summary

| # | Question | Decision |
|---|----------|----------|
| 1 | Coder vs raw K8s | **Coder as thin provisioner** |
| 2 | Single container vs sidecar | **Single container + supervisord** |
| 3 | URL routing | **Wildcard subdomain via Coder proxy** |
| 4 | Session Management deployment | **Standalone service** (cross-module) |
| 5 | Image strategy | **Single base image + activation** |

## Related documentation

- [../README.md](../README.md) — Module README with decision summary
- [../../README.md](../../README.md) — Platform-wide design decisions
