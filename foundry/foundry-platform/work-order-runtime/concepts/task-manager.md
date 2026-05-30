# Task Manager

The Task Manager is the component that manages task trees, handles dependencies between tasks, and executes the task state machine within a Work Order.

## What it is

When a Work Order is attached to a session, the Task Manager builds its task tree by querying Jira for all tasks under that WO. It then tracks each task's state and dependencies, scheduling tasks for execution when their dependencies are met.

The Task Manager implements:

- **DAG representation** — Tasks form a Directed Acyclic Graph where edges represent dependencies
- **State machine** — Each task moves through states: Blocked → Ready → In-Progress → Completed/Failed/Cancelled
- **Dependency resolution** — A task becomes Ready when all its dependencies reach terminal states
- **Scheduling** — Ready tasks are handed to the Agent Spawner (for agent tasks) or surfaced in the UI (for human tasks)

Work Orders are themselves root tasks. Completion of the root task means completion of the Work Order. Sub-tasks can create further sub-tasks during execution, extending the tree dynamically.

## Where it lives

| Component | Location |
|-----------|----------|
| **Task Manager** | WO Runtime Daemon |
| **Task state** | Local SQLite `tasks` table |
| **Task records** | Jira (system of record) |
| **Tree updates** | Via Jira MCP |

## Task state machine

```
           ┌──────────────────────────────────────────────┐
           │                                              │
           ▼                                              │
       ┌────────┐     dependencies met     ┌────────┐     │
       │Blocked │─────────────────────────►│ Ready  │     │
       └────────┘                          └────────┘     │
           ▲                                    │         │
           │                                    │ start   │
           │                                    ▼         │
           │                              ┌───────────┐   │
           │    dependency added          │In-Progress│   │
           └──────────────────────────────┴───────────┘   │
                                               │          │
                              ┌────────────────┼──────────┤
                              │                │          │
                         success          failure    cancel
                              │                │          │
                              ▼                ▼          │
                        ┌───────────┐   ┌────────┐        │
                        │ Completed │   │ Failed │────────┘
                        └───────────┘   └────────┘
```

## State definitions

| State | Meaning |
|-------|---------|
| **Blocked** | Task has unmet dependencies |
| **Ready** | All dependencies complete; can be executed |
| **In-Progress** | Agent spawned or human picked up the task |
| **Completed** | Successfully finished |
| **Failed** | Execution failed; may be retried or escalated |
| **Cancelled** | Explicitly cancelled by user or system |

## Dependency handling

Dependencies are stored in Jira's `dependencies` custom field as a list of task keys:

```json
{
  "key": "TASK-893",
  "fields": {
    "dependencies": ["TASK-891", "TASK-892"],
    "scenario": "write-tests"
  }
}
```

**Resolution rule:** A task becomes Ready when all dependencies are in terminal state (Completed or Cancelled) and the task itself is not Cancelled.

Dependencies can span:
- **Within WO** — Task B depends on Task A in same Work Order
- **Within Workbench** — Task in WO-567 depends on task in WO-566
- **Cross-user** — Task assigned to Alice depends on task assigned to Bob

## Task tree visualization

```
WO-567: Implement user preferences
├── TASK-890 (Root) ─────────────────────────────────────────
│       │
│       ├─► TASK-891 (Implement API) ────────────────┐
│       │                                            │
│       ├─► TASK-892 (Implement UI) ─────────────────┤
│       │                                            │
│       │                                            ▼
│       │                                     TASK-893 (Tests)
│       │                                            │
│       └─► TASK-894 (Docs) ─────────────────────────┘
│                                 │
│                                 ▼
│                          WO Complete
└─────────────────────────────────────────────────────────────
```

## Task creation by skills

During execution, skills can create sub-tasks via Jira MCP:

```yaml
task_templates:
  implement-component:
    summary: "Implement {component_name}"
    scenario: implement-component
    type: Sub-task
    
  write-tests:
    summary: "Write tests for {component_name}"
    scenario: write-tests
    type: Sub-task
    dependencies_pattern: ["implement-*"]
```

The Task Manager detects newly created tasks during its next poll cycle and adds them to the tree.

## Task tree limits

| Limit | Default | Purpose |
|-------|---------|---------|
| Max depth | 5 levels | Prevent runaway nesting |
| Max tasks per WO | 500 | Prevent runaway creation |
| Max concurrent | 10 | Session resource protection |

These are abuse/accident prevention limits, not conceptual constraints.

## Workspace-local tasks

The Task Manager handles [Workspace-Local Tasks](workspace-local-tasks.md) alongside synced tasks:

- **Creation** — Builder-initiated via IDE; rows written to Local State Store with `sync_scope = 'local'`; no Jira MCP calls.
- **Graph** — Local tasks appear in the full DAG returned to the IDE; dependency edges are enforced in the local store for display and optional scheduling hints.
- **Manual start with unmet dependencies** — When a builder uses Create & Start on a manual Human Task, the Task Manager transitions to In-Progress without requiring dependencies to be terminal (WOR-FR-0043).
- **Agent sessions under Human Tasks** — WO Runtime may record each builder-employed agent session as a local child task for uniform tracking; these are not exported to Jira.

Synced tasks continue to use Jira as system of record; local tasks use the Local State Store only.

## Personal Work

The Task Manager maintains the [Personal Work](../../concepts/personal-work.md) Work Order (`is_personal_work = 1`). Agent sessions associated with Personal Work are attached as local tasks under that WO. Personal Work does not participate in Orchestrator completion reporting.

## Completion criteria

**Task completion:** Agent marks complete via Jira MCP, or human marks complete in UI.

**Work Order completion:** All tasks in the tree reach terminal state. Failed tasks block WO completion unless manually resolved (retry, cancel, or override).

## Related concepts

- [WO Runtime Daemon](wo-runtime-daemon.md) — Hosts the Task Manager
- [Agent Spawner](agent-spawner.md) — Receives ready tasks for agent execution
- [Local State Store](local-state-store.md) — Persists task state
- [Task](../../concepts/task.md) — What the Task Manager schedules
- [Work Order](../../concepts/work-order.md) — The root task

## Further reading

- [../platform-developer-guide/task-execution.md](../platform-developer-guide/task-execution.md) — Detailed task execution spec
- [../platform-developer-guide/requirements.md](../platform-developer-guide/requirements.md) — Task Manager requirements (WOR-FR-0005, WOR-FR-0006)
