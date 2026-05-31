# Task

A Task is the unit of work completed by human-agent teams — the atomic execution step created when a Scenario triggers, with clear ownership, dependencies, and completion criteria.

## What it is

When a [Scenario](scenario.md) executes, it creates one or more Tasks. Tasks form a tree structure with dependencies:

```
Work Order (from Scenario)
└── Root Task
    ├── Sub-Task A
    │   ├── Sub-Task A.1
    │   └── Sub-Task A.2
    └── Sub-Task B
```

Every Task carries contract fields `title` (short label) and `description` (markdown body).

### `agentType` (contract field)

| `agentType` | Executor | Surfaced In |
|-------------|----------|-------------|
| `ai-agent` | Employed Agent with Skills | Agent process in Session |
| `human` | Human practitioner | Web console, IDE panel |

The distinction matters for tooling and workflow:

- **`ai-agent`** tasks are picked up by spawned agents within a [Workspace Session](workspace-session.md). The agent has context, skills, and a delegation token.
- **`human`** tasks are surfaced in the Foundry Web App and IDE for humans to claim and complete.

Tasks maintain state through a lifecycle:

| State | Meaning |
|-------|---------|
| `pending` | Created but not started |
| `blocked` | Waiting on dependency |
| `in_progress` | Being worked on |
| `completed` | Successfully finished |
| `failed` | Execution failed |
| `cancelled` | Explicitly cancelled |

Work Items (Tasks) are stored in the **Work Repository** as the system of record. In Phase 1 the adapter is Jira: root Tasks are Stories under the Work Order Epic; sub-tasks are Jira Sub-tasks. Contract field `workRepoItemKey` holds the adapter item key.

Workspace-local and Personal Work tasks use `syncScope: local` and are not synced to the Work Repository.

## Where it lives in Foundry

| Module | Responsibility |
|--------|----------------|
| **WO Runtime** | Creates task tree, manages dependencies, tracks state |
| **Work Repository** | System of record (`workRepoItemKey`) |
| **Agent Fabric** | Provides Skills that agents use to complete Tasks |
| **IDE** | Surfaces Human Tasks in Work Orders panel |
| **Web App** | Shows Human Tasks in Work console |

API routes: track-based `/workbenches/{workbenchId}/tracks/build/tasks/{taskId}` — see [../../foundry-work-plan/phase-1/api-surface.md](../../foundry-work-plan/phase-1/api-surface.md).

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Task](../../ace/concepts.md#scenarios-and-tasks) | Task tree via WO Runtime + Work Repository |
| Human–Agent Team | Both `agentType` values execute Tasks within same Workspace |
| Task completion | Updates Work Repository; notifies Orchestrator |

## Related concepts

- [Scenario](scenario.md) — What creates Tasks when it executes
- [Work Order](work-order.md) — The container for a Task tree
- [Workspace Session](workspace-session.md) — Where Tasks execute
- [Agent Model](agent-model.md) — Who executes `ai-agent` Tasks
- [Delegation](delegation.md) — Authority that agents have to complete Tasks

## Further reading

- [../../foundry-work-plan/phase-1/repository-contracts.md](../../foundry-work-plan/phase-1/repository-contracts.md) — Task schema and `agentType`
- [../work-order-runtime/README.md](../work-order-runtime/README.md) — Task Manager and lifecycle
- [../work-order-runtime/platform-developer-guide/requirements.md](../work-order-runtime/platform-developer-guide/requirements.md) — Task management requirements
