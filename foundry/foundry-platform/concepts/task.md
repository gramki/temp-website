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

Tasks have two primary types based on who executes them:

| Type | Executor | Surfaced In |
|------|----------|-------------|
| **Agent Task** | Employed Agent with Skills | Agent process in Session |
| **Human Task** | Human practitioner | Web console, IDE panel |

The distinction matters for tooling and workflow:

- **Agent Tasks** are picked up by spawned agents within a [Workspace Session](workspace-session.md). The agent has context, skills, and a delegation token.
- **Human Tasks** are surfaced in the Foundry Web App and IDE for humans to claim and complete. These might be review tasks, approval tasks, or tasks requiring judgment beyond agent capability.

Tasks maintain state through a lifecycle:

| State | Meaning |
|-------|---------|
| `pending` | Created but not started |
| `blocked` | Waiting on dependency |
| `in_progress` | Being worked on |
| `completed` | Successfully finished |
| `failed` | Execution failed |
| `cancelled` | Explicitly cancelled |

Tasks are stored in Jira as the system of record. Root Tasks are Stories under the Work Order Epic; Sub-Tasks are Jira Sub-tasks. This enables consistent tracking, reporting, and integration with existing workflows.

## Where it lives in Foundry

| Module | Responsibility |
|--------|----------------|
| **WO Runtime** | Creates task tree, manages dependencies, tracks state |
| **Jira (MCP)** | System of record for Task storage |
| **Agent Fabric** | Provides Skills that agents use to complete Tasks |
| **IDE** | Surfaces Human Tasks in Work Orders panel |
| **Web App** | Shows Human Tasks in Work console |

WO Runtime's Task Manager is the central component:

```
Scenario Definition → Task Tree Creation → Dependency Resolution → Agent Spawning/Human Surfacing → Completion Tracking → WO Completion
```

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Task](../../ace/concepts.md#scenarios-and-tasks) | Task tree in Jira via WO Runtime |
| Human–Agent Team | Both types execute Tasks within same Workspace |
| Task completion | Updates Work Repository; notifies Orchestrator |

From ACE: "Tasks are the unit of work completed by the Human–Agent Team."

UPIM's Work Model defines abstract work entities (Epic, Story, Task, Bug). The Foundry Platform maps these to Jira issue types, with WO Runtime managing the execution lifecycle.

## Related concepts

- [Scenario](scenario.md) — What creates Tasks when it executes
- [Work Order](work-order.md) — The container for a Task tree
- [Workspace Session](workspace-session.md) — Where Tasks execute
- [Agent Model](agent-model.md) — Who executes Agent Tasks
- [Delegation](delegation.md) — Authority that agents have to complete Tasks

## Further reading

- [../work-order-runtime/README.md](../work-order-runtime/README.md) — Task Manager and lifecycle
- [../work-order-runtime/platform-developer-guide/requirements.md](../work-order-runtime/platform-developer-guide/requirements.md) — Task management requirements
- [../../ace/concepts.md#scenarios-and-tasks](../../ace/concepts.md#scenarios-and-tasks) — ACE definition
- [../../ace/repositories.md#work-repository](../../ace/repositories.md#work-repository) — Work Repository structure
