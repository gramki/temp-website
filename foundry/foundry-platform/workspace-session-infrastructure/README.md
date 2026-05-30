# Workspace Session Infrastructure

**Module scope:** Kubernetes-based session provisioning — pod lifecycle, container images, networking, Coder integration, multi-tenant isolation.

## What this module does

Workspace Session Infrastructure provisions and manages the Kubernetes runtime for [Workspace Sessions](../concepts/workspace-session.md). When Session Management requests a session, this module spawns a pod on a Foundry-admin-provided cluster, applies workspace content layers, generates an accessible session URL, and reports readiness back to the control plane.

Each session pod runs a single container supervised by a process manager. Inside that container: Coder Code Server (IDE), WO Runtime (execution daemon), Capable Agent binaries, and platform IDE extensions. Init containers apply Workshop/Workbench workspace content and Foundry admin overlays before the main container starts.

Primary beneficiaries are Foundry admins (cluster configuration, image customization) and platform engineers (provisioning implementation). Builders experience the result as a browser-accessible IDE at a deterministic session URL.

## Infrastructure model

Sessions are Kubernetes pods on a cluster endpoint provided by the Foundry admin — the platform does not provision clusters. Each session pod is the unit of isolation, persistence binding, and network routing.

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
│  │  Session Pod (session-{session-id})                                    │  │
│  │  init: workspace-merge │ admin-overlay                                 │  │
│  │  container: code-server + wo-runtime + agents (supervisord)            │  │
│  │  PVC: workspace-data │ emptyDir: merged-content, skill-cache           │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│  Coder proxy → {session-id}.sessions.{ingress-domain}                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Key output:** An accessible session URL returned to Session Management when the pod passes readiness probes.

## Layering model

Workspace content is applied in three layers at different times:

| Layer | When applied | Source | Contents |
|-------|--------------|--------|----------|
| **1 — Platform base image** | Image build time | Platform release pipeline | Coder Code Server, WO Runtime binary, Capable Agent binaries, platform IDE extensions |
| **2 — Workshop/Workbench specifics** | Session start (init container) | Workshop Definition Repo | `.devcontainer/` config, Scenarios, Skills |
| **3 — Foundry admin additions** | Session start (overlay mount) | Foundry Definition Repo | `workspace-infrastructure/<workspace>/` custom tools, extensions, runtimes |

Layer 1 uses a **single base image + workspace-type activation** at session start rather than six separate images. Workspace-type differences (language runtimes, test frameworks, signing tools) are applied via activation scripts or devcontainer features in the init container.

→ [concepts/platform-base-image.md](concepts/platform-base-image.md) — Layer 1 details
→ [concepts/admin-layering.md](concepts/admin-layering.md) — Layer 3 mechanism
→ [concepts/workspace-template.md](concepts/workspace-template.md) — Layer 2 and Coder template composition

## ACE concepts realized

| Concept | How this module realizes it |
|---------|----------------------------|
| [Workspace Session](../concepts/workspace-session.md) | Provisions the K8s pod that is the session runtime |
| [Workspace](../../ace/concepts.md#workspace) | Session pod is the runtime instance of a Workspace type |
| [IDE](../../ace/concepts.md#ide) | Code Server and extensions ship in the platform base image |

See [ACE overview](../../ace/README.md) for the full model.

## What this module does NOT do

| Boundary | Owned by |
|----------|----------|
| Session lifecycle decisions (create, stop, archive) | [Workspace Session Management](../workspace-session-management/) |
| Work Order execution, agent spawning, liveness ack | [Work Order Runtime](../work-order-runtime/) |
| Workspace content schemas (devcontainer, scenarios) | [Management](../management/) — Workshop Definition Repo |
| Kubernetes cluster provisioning | Foundry admin — provides cluster endpoint |
| Work Order routing and session query/creation requests | [Orchestrator](../orchestrator/) → Session Management |

## Key design decisions

- **Coder as thin provisioner.** Coder's Kubernetes workspace provider handles stop/start/resume and wildcard proxy routing. Session Infrastructure owns template definitions; Session Management is the source of truth for session state — not Coder's internal state.
- **Single container with process supervision.** Code Server, WO Runtime, and agent processes run in one container managed by supervisord. Shared filesystem access is trivial; WO Runtime restarts independently without killing Code Server.
- **Wildcard subdomain via Coder proxy.** Session URLs follow `{session-id}.sessions.{ingress-domain}`. One wildcard DNS record and cert; Coder routes by workspace name — no per-session Ingress objects.
- **Single base image + activation layer.** Six workspace types share ~95% of image content. Type-specific tooling is activated at session start via init container, not separate image builds.

→ [platform-developer-guide/design-discussions/architecture-choices.md](platform-developer-guide/design-discussions/architecture-choices.md) — Full decision rationale

## Dependencies

| Dependency | Relationship |
|------------|--------------|
| [Workspace Session Management](../workspace-session-management/) | Sends provision/stop requests; receives pod-ready and pod-failed events |
| [Work Order Runtime](../work-order-runtime/) | Runs inside session pod; exposes `/health` for readiness probes |
| [Management](../management/) | Foundry settings include `workspace_infrastructure` cluster config |
| [IDE](../ide/) | Extensions packaged into platform base image (Layer 1) |
| [Agent Fabric](../agent-fabric/) | Capable Agent binaries included in base image |
| Coder | Workspace provisioner and session URL proxy |

## Key Concepts

### Platform-wide concepts

| Concept | What Session Infrastructure does with it |
|---------|------------------------------------------|
| [Workspace Session](../concepts/workspace-session.md) | Provisions the K8s pod, URL, and storage that constitute a session |
| [Agent Model](../concepts/agent-model.md) | Ships Capable Agent binaries in the base image |
| [Delegation](../concepts/delegation.md) | Session pod network policy allows egress to platform APIs for token exchange |

### Module-specific concepts

| Concept | Definition |
|---------|------------|
| [Platform Base Image](concepts/platform-base-image.md) | Layer 1 container image contents and workspace-type activation |
| [Admin Layering](concepts/admin-layering.md) | Foundry admin overlay from Foundry Definition Repo |
| [Workspace Template](concepts/workspace-template.md) | Coder template and devcontainer merge into pod spec |
| [Session Pod](concepts/session-pod.md) | Kubernetes pod as the unit of session infrastructure |

→ [concepts/README.md](concepts/README.md) — Full module concept index

## Documentation

| Guide | Audience | Index |
|-------|----------|-------|
| [Concepts](concepts/) | Anyone | Module-specific concept definitions |
| [User guide](user-guide/) | Foundry admins, builders | Cluster config, image customization, in-session CLI |
| [Foundry Platform developer guide](platform-developer-guide/) | Platform engineers | K8s specs, requirements, interface contracts |

## Read next

- [platform-developer-guide/requirements.md](platform-developer-guide/requirements.md) — WSI-FR and WSI-NFR specifications
- [platform-developer-guide/sequence-diagrams.md](platform-developer-guide/sequence-diagrams.md) — Creation, stop, and crash recovery flows
- [user-guide/customizing-workspace-images.md](user-guide/customizing-workspace-images.md) — Foundry admin overlay guide
- [../concepts/workspace-session.md](../concepts/workspace-session.md) — Platform-wide Workspace Session definition
