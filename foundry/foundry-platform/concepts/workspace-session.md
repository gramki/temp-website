# Workspace Session

A Workspace Session is an ephemeral development environment — a Kubernetes pod (Coder workspace) where humans and agents work together on Tasks, with full IDE access, installed Skills, and repository bindings.

## What it is

Workspace Sessions are the runtime environments where Work Orders actually execute. They provide:

- **Kubernetes pods** — Coder workspace on a Foundry-admin-provided cluster
- **IDE access** — VS Code (Code Server) with workspace-specific views and extensions
- **Repository bindings** — Access to relevant Workshop repositories
- **Skill injection** — Skills installed from registries at session start
- **Agent processes** — Employed Agents spawned within the session
- **WO Runtime daemon** — In-session worker; polls for work, manages Tasks, reports completion

Key characteristics:

| Aspect | Detail |
|--------|--------|
| **Technology** | Coder on Kubernetes (single container: Code Server + WO Runtime) |
| **Template** | Per (Workspace Type, Workbench) — from `.devcontainer/` in Workshop repo |
| **Ownership** | Owned by one person (not shared) |
| **WO relationship** | Multiple Work Orders can attach to one Session |
| **Lifecycle** | Managed by Session Management: Created → Starting → Active → Stopping → Stopped → Archived |

Sessions are **user-owned** — each session belongs to a single human practitioner. Multiple Work Orders from the same Workbench can be attached to one session, allowing a developer to work on several features simultaneously.

The WO Runtime daemon runs inside each session pod:

```
┌───────────────────────────────────────────────────────────────────────────┐
│                   Workspace Session Pod (K8s / Coder)                     │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐ │
│  │  workspace container (Code Server + WO Runtime via process supervisor)│ │
│  │  Jira Poller → Task Manager → Agent Spawner → Completion Reporter   │ │
│  └─────────────────────────────────────────────────────────────────────┘ │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐ │
│  │                    Employed Agent Processes                          │ │
│  │    Agent 1 (Task A)   │   Agent 2 (Task B)   │   Agent N (...)      │ │
│  └─────────────────────────────────────────────────────────────────────┘ │
└───────────────────────────────────────────────────────────────────────────┘
```

Sessions become Active when WO Runtime acknowledges liveness to Session Management after the pod is provisioned. Orchestrator queries or creates sessions and assigns Work Orders; WO Runtime discovers assignments independently.

## Where it lives in Foundry

| Module | Responsibility |
|--------|----------------|
| **Session Infrastructure** | K8s provisioning, container images, networking, URL generation |
| **Session Management** | Lifecycle control plane, state tracking, session events |
| **WO Runtime** | In-session worker; liveness ack, task execution, agent spawning |
| **IDE** | User interface within the session; Work Orders panel, agent chat tabs |
| **Orchestrator** | Queries/creates sessions; assigns Work Orders (does not execute) |
| **Agent Fabric** | Provides Skills installed at session start |

Session templates and admin overlays are defined in Foundry and Workshop Definition Repositories:

```
foundry-{id}/
└── workspace-infrastructure/
    └── {workspace-type}/          # Foundry admin Layer 3 overlay

workshop-{id}/
└── workbenches/
    └── {product-code}/
        └── .devcontainer/
            └── {workspace-type}/
                └── devcontainer.json
```

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Workspace](../../ace/concepts.md#workspace) | Session is the runtime instance of a Workspace |
| [IDE](../../ace/concepts.md#ide) | VS Code within the Session container |
| Human–Agent Team | Both work in the same Session environment |
| Repository access | Session has bindings to Workshop repositories |

From ACE: "The IDE is the human's entry surface into a Workspace. ACE treats each Workspace as having its own IDE context."

Sessions operationalize this by providing workspace-specific views, plugins, and repository bindings based on the Workspace type (Development, QA, Release, etc.).

## Related concepts

- [Work Order](work-order.md) — What attaches to and executes in a Session
- [Task](task.md) — What agents and humans complete within a Session
- [Agent Model](agent-model.md) — Employed Agents spawned in Sessions
- [Skill](skill.md) — Installed at session start
- [Delegation](delegation.md) — Authority tokens used by agents in Sessions

## Further reading

- [../workspace-session-infrastructure/README.md](../workspace-session-infrastructure/README.md) — Pod provisioning and images
- [../workspace-session-management/README.md](../workspace-session-management/README.md) — Session lifecycle control plane
- [../work-order-runtime/README.md](../work-order-runtime/README.md) — In-session execution and management-plane agent
- [../ide/README.md](../ide/README.md) — IDE integration
- [../../ace/concepts.md#ide](../../ace/concepts.md#ide) — ACE IDE definition
