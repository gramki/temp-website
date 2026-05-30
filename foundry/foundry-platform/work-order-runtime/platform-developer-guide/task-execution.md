# Task Execution

This document describes how WO Runtime manages task trees, handles dependencies, and executes tasks within a Workspace Session.

## ACE alignment

| ACE concept | How this module realizes it |
|-------------|---------------------------|
| **Task** | Models tasks as DAG with dependencies; manages state machine (Blocked → Ready → In-Progress → Completed/Failed) |
| **Work Order** | Work Order is the root task; completion of root = completion of WO |
| **Scenario** | Each task has a Scenario that determines its Skilled Agent and execution path |
| **Agent** | Agent execution path spawns Employed Agents; Human execution path surfaces tasks in UI |

## Task Tree Model

A Work Order is structured as a task tree:

```
Work Order (Root Task)
├── Task A
│   ├── Task A.1
│   └── Task A.2
├── Task B (depends on A)
└── Task C (depends on A, B)
    ├── Task C.1
    └── Task C.2
```

### Work Order as Root Task

Every Work Order is itself the root task. The root task:

- Has the Work Order's Scenario
- May have a Skilled Agent (if Scenario defines one)
- Completion of root task = completion of Work Order

### Sub-Tasks

Tasks can have sub-tasks:

- Created by skills during execution
- Created manually by session owner
- Inherit context from parent (but may override Scenario)

## Jira as System of Record

All Work Orders and Tasks are stored in Jira:

### Jira Structure

```
Jira Project: PRODUCT-ABC-WO (per Workbench)
│
├── Epic: WO-567 (Work Order)
│   ├── Story: TASK-890 (Root task)
│   │   ├── Sub-task: TASK-891
│   │   ├── Sub-task: TASK-892
│   │   └── Sub-task: TASK-893
│   └── (other tasks...)
│
└── Epic: WO-568 (Another Work Order)
    └── ...
```

### Jira Custom Fields

| Field | Purpose |
|-------|---------|
| `scenario` | Scenario identifier for this task |
| `dependencies` | List of task keys this task depends on |
| `foundry-work-order` | Link to parent Work Order |
| `foundry-track` | Track context |
| `foundry-workspace` | Workspace type |

### Jira MCP Server

WO Runtime accesses Jira through the Jira MCP Server:

```
WO Runtime Daemon
    │
    ├── Query: assigned WOs
    ├── Query: task tree
    ├── Update: task status
    └── Create: new tasks
    │
    ▼
Jira MCP Server
    │
    ▼
Jira API
```

Tools provided by Jira MCP:

| Tool | Purpose |
|------|---------|
| `jira_search` | Query WOs and tasks |
| `jira_get_issue` | Get task details |
| `jira_create_issue` | Create new task |
| `jira_update_issue` | Update task status/fields |
| `jira_transition_issue` | Move task through states |

## Task Dependencies

Tasks form a Directed Acyclic Graph (DAG):

### Dependency Definition

Dependencies are stored in Jira's `dependencies` custom field:

```json
{
  "key": "TASK-893",
  "fields": {
    "dependencies": ["TASK-891", "TASK-892"],
    "scenario": "write-tests"
  }
}
```

### Dependency Resolution

A task becomes Ready when:

```
All dependencies are in terminal state (Completed or Cancelled)
AND
Task is not Cancelled
```

### Cross-Task Dependencies

Dependencies can cross:

- **Within WO** — Task B depends on Task A in same WO
- **Within Workbench** — Task in WO-567 depends on task in WO-566
- **Cross-user** — Task assigned to Alice depends on task assigned to Bob

### Dependency Visualization

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  WO-567: Implement user preferences                                         │
│                                                                              │
│  TASK-890 (Root) ──────────────────────────────────────────────────────────│
│      │                                                                       │
│      ├─► TASK-891 (Implement API) ────────────────────┐                     │
│      │                                                 │                     │
│      ├─► TASK-892 (Implement UI) ─────────────────────┤                     │
│      │                                                 │                     │
│      │                                                 ▼                     │
│      │                                          TASK-893 (Tests)            │
│      │                                                 │                     │
│      └─► TASK-894 (Docs) ─────────────────────────────┘                     │
│                                    │                                         │
│                                    ▼                                         │
│                             WO Complete                                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Task State Machine

Tasks follow a defined state machine:

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

### State Definitions

| State | Description |
|-------|-------------|
| **Blocked** | Has unmet dependencies |
| **Ready** | All dependencies met; can be executed |
| **In-Progress** | Currently being executed (agent or human) |
| **Completed** | Successfully finished |
| **Failed** | Execution failed; may be retried or escalated |
| **Cancelled** | Cancelled by user or system |

### State Transitions

| From | To | Trigger |
|------|-----|---------|
| Blocked | Ready | All dependencies complete |
| Ready | In-Progress | Agent spawned or human picks up |
| In-Progress | Completed | Task successfully finished |
| In-Progress | Failed | Error during execution |
| Any | Cancelled | User cancels |
| Failed | Ready | Retry requested |

## Task Execution

### Execution Flow

For each ready task:

```
1. Check Scenario definition
2. Look for Skilled Agent
   ├── Found → Agent execution path
   └── Not found → Human execution path
```

### Agent Execution Path

```
1. WO Runtime reads Skilled Agent definition
2. WO Runtime selects Capable Agent and Model
3. WO Runtime prepares harness
4. WO Runtime spawns Employed Agent
5. Agent executes skill
6. Agent may create sub-tasks (via Jira MCP)
7. Agent updates task status
8. Agent notifies completion
```

### Human Execution Path

```
1. Task appears in web console work queue
2. Task appears in IDE Work Orders Panel
3. Human picks up task
4. Human works on task (code, design, review, etc.)
5. Human marks task complete
```

## Task Creation by Skills

Skills create sub-tasks using the Jira MCP `create_issue` tool:

### Task Template

Skills define task templates:

```yaml
# In skill definition
task_templates:
  implement-component:
    summary: "Implement {component_name}"
    scenario: implement-component
    type: Sub-task
    
  write-tests:
    summary: "Write tests for {component_name}"
    scenario: write-tests
    type: Sub-task
    dependencies_pattern: ["implement-*"]  # Dynamic dependency
```

### Task Creation Call

```python
# In skill execution
jira_create_issue(
    project="PRODUCT-ABC-WO",
    issue_type="Sub-task",
    parent=current_task_key,
    summary="Implement database migration",
    fields={
        "scenario": "implement-migration",
        "dependencies": ["TASK-891"],
        "description": "Migration details..."
    }
)
```

### Task Creation Rules

- Sub-tasks are created under the current task
- Scenario is specified for Skilled Agent lookup
- Dependencies can reference sibling tasks or external tasks
- WO Runtime tracks all created tasks for the task tree

## Task Tree Limits

Configurable limits prevent runaway task creation:

| Limit | Default | Description |
|-------|---------|-------------|
| **Max depth** | 5 levels | Maximum task tree depth |
| **Max tasks per WO** | 500 | Maximum tasks in one Work Order |
| **Max concurrent** | 10 | Maximum in-progress tasks per session |

These are abuse/accident prevention limits, not conceptual constraints.

## Completion Criteria

### Task Completion

A task is complete when:

- Agent marks it complete, OR
- Human marks it complete in UI

### Work Order Completion

A Work Order is complete when:

- All tasks in the task tree are in terminal state
- Terminal states: Completed, Cancelled
- Failed tasks block completion unless manually resolved

### Partial Completion

If some tasks failed:

```
WO-567
├── TASK-890 ✓ Completed
├── TASK-891 ✓ Completed
├── TASK-892 ✗ Failed
└── TASK-893 (Blocked - depends on 892)

Options:
1. Retry TASK-892
2. Cancel TASK-892 and TASK-893
3. Mark TASK-892 as Completed (manual override)
4. Escalate WO to human review
```

## Read Next

- [agent-spawning.md](agent-spawning.md) — How agents are spawned for tasks
- [ide-integration.md](ide-integration.md) — How tasks appear in the IDE
- [../user-guide/work-order-lifecycle.md](../user-guide/work-order-lifecycle.md) — Full WO lifecycle
- [../agent-fabric/user-guide/skilled-agents.md](..//agent-fabric/user-guide/skilled-agents.md) — Skilled Agent definitions
