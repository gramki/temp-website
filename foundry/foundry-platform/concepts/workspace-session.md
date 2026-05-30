# Workspace Session

A Workspace Session is an ephemeral development environment — a Coder-based container where humans and agents work together on Tasks, with full IDE access, installed Skills, and repository bindings.

## What it is

Workspace Sessions are the runtime environments where Work Orders actually execute. They provide:

- **Coder-based containers** — Similar to GitHub Codespaces, with consistent tooling
- **IDE access** — VS Code with workspace-specific views and extensions
- **Repository bindings** — Access to relevant Workshop repositories
- **Skill injection** — Skills installed from registries at session start
- **Agent processes** — Employed Agents spawned within the session
- **WO Runtime daemon** — Polls for work, manages Tasks, reports completion

Key characteristics:

| Aspect | Detail |
|--------|--------|
| **Technology** | Coder (ephemeral dev environments) |
| **Template** | Per (Workspace Type, Workbench) — from `.devcontainer/` in Workshop repo |
| **Ownership** | Owned by one person (not shared) |
| **WO relationship** | Multiple Work Orders can attach to one Session |
| **Lifecycle** | User explicitly closes; states: Active, Stopped, Archived |

Sessions are **user-owned** — each session belongs to a single human practitioner. Multiple Work Orders from the same Workbench can be attached to one session, allowing a developer to work on several features simultaneously.

The WO Runtime daemon runs inside each session:

```
┌───────────────────────────────────────────────────────────────────────────┐
│                        Workspace Session (Coder)                          │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐ │
│  │                      WO Runtime Daemon                               │ │
│  │  Jira Poller → Task Manager → Agent Spawner → Completion Reporter   │ │
│  └─────────────────────────────────────────────────────────────────────┘ │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐ │
│  │                    Employed Agent Processes                          │ │
│  │    Agent 1 (Task A)   │   Agent 2 (Task B)   │   Agent N (...)      │ │
│  └─────────────────────────────────────────────────────────────────────┘ │
└───────────────────────────────────────────────────────────────────────────┘
```

Sessions are activated when Work Orders are assigned. Depending on user configuration, assignment can automatically activate a session or wait for manual activation.

## Where it lives in Foundry

| Module | Responsibility |
|--------|----------------|
| **WO Runtime** | Creates sessions, runs daemon, manages lifecycle |
| **Agent Fabric** | Provides Skills installed at session start |
| **IDE** | User interface; Work Orders panel, agent chat tabs |
| **Coder** | Underlying container infrastructure |
| **Orchestrator** | Triggers session activation on WO assignment |

Session templates are defined in Workshop Definition Repositories:

```
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

- [../work-order-runtime/README.md](../work-order-runtime/README.md) — Session management and daemon
- [../work-order-runtime/platform-developer-guide/requirements.md](../work-order-runtime/platform-developer-guide/requirements.md) — Session requirements
- [../ide/README.md](../ide/README.md) — IDE integration
- [../../ace/concepts.md#ide](../../ace/concepts.md#ide) — ACE IDE definition
