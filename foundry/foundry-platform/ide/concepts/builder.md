# Builder

A Builder is Foundry's term for any human using the IDE in a Workspace Session — to complete Tasks, interact with agents, and produce work artifacts.

## What it is

Foundry uses "Builder" for all human practitioners who work within Workspace Sessions:

- **Developers** writing and reviewing code in Development Workspaces
- **Product Managers** refining specifications in Product Specification Workspaces
- **QA Engineers** executing and approving tests in QA Workspaces
- **UX Designers** creating and validating designs in UX Design Workspaces
- **Release Engineers** managing artifacts in Release Workspaces
- **Governance participants** conducting rituals in Governance Workspaces

The label applies across disciplines because the IDE experience is the same regardless of UPIM role.

Key Builder capabilities in the IDE:

| Capability | Description |
|------------|-------------|
| **Workspace-specific views** | Tailored UI for the active Workspace type |
| **Work Order visibility** | Track assigned WOs, progress, and status |
| **Human Task surfacing** | See tasks awaiting human action |
| **Agent interaction** | Chat with agents, observe terminal output |
| **Context access** | Access product context pre-loaded per Workspace |

Builders own their [Workspace Sessions](../../concepts/workspace-session.md) — each session belongs to one Builder, even when multiple Work Orders attach to that session.

## Where it lives in Foundry

| Module | Responsibility |
|--------|----------------|
| **IDE** | Builder-facing interface; all IDE features target Builders |
| **Session Management** | Lifecycle for Builder-owned sessions |
| **WO Runtime** | Executes Work Orders in Builder sessions; surfaces Human Tasks |
| **Orchestrator** | Assigns Work Orders to Builders |
| **Web App** | Alternative interface for Builders who don't need IDE |
| **Workbench** | Defines Builder roles and permissions |

## Documentation map

```
ide/
├── user-guide/              ← Written for Builders
│   └── workspace-sessions.md
└── platform-developer-guide/ ← Written for platform engineers
    └── extensions.md
```

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| Human–Agent Team | Builder is the human in the team |
| [Workspace](../../ace/concepts.md#workspace) | Builder works within Workspaces via the IDE |
| Practitioner | ACE term; Foundry uses "Builder" for IDE context |

From ACE: "ACE treats each Workspace as having its own IDE context." The Builder is the human who enters that context.

### UPIM alignment

In UPIM's Workforce Repository, Builders are practitioners assigned to Workbenches with specific roles (Developer, Product Manager, etc.). The IDE abstracts over these roles — regardless of UPIM role, everyone using the IDE is a Builder.

## Related concepts

- [Workspace Views](workspace-views.md) — UI tailored per Workspace type for Builders
- [Workspace Session](../../concepts/workspace-session.md) — Builder-owned runtime environment
- [Task](../../concepts/task.md) — What Builders complete (Human Tasks) or observe (Agent Tasks)
- [Delegation](../../concepts/delegation.md) — How Builders authorize agents to act

## Further reading

- [../user-guide/workspace-sessions.md](../user-guide/workspace-sessions.md) — Builder-facing capabilities
- [../README.md](../README.md) — IDE module scope
- [../../concepts/workspace-session.md](../../concepts/workspace-session.md) — Session ownership model
