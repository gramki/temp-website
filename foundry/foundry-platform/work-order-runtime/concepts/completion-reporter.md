# Completion Reporter

The Completion Reporter is the component that notifies the Orchestrator when Work Orders reach terminal states — completed, failed, or blocked — enabling orchestration workflows to advance.

## What it is

When a Work Order finishes, the Orchestrator needs to know so it can fire the appropriate workflow events and potentially transition the parent orchestration item. The Completion Reporter handles this notification by publishing messages to the message queue that the Orchestrator consumes.

The Completion Reporter monitors Work Order state within the session and sends:

- `work-order-completed` — WO finished successfully
- `work-order-failed` — WO failed with no retry available
- `task-blocked` — A task entered recoverable failure (quota, agent disabled, etc.)

These messages contain the WO label, status, and relevant metadata so the Orchestrator's Workflow Engine can match them to handlers.

## Where it lives

| Component | Location |
|-----------|----------|
| **Completion Reporter** | WO Runtime Daemon |
| **Message queue** | Kafka or RabbitMQ (shared infrastructure) |
| **Orchestrator consumer** | Orchestrator service |
| **Local queue** | SQLite (for retry on MQ failure) |

## Completion flow

```
Task Manager detects all tasks complete
    │
    ├── Calculate WO final state
    │       │
    │       ├── All tasks Completed → WO completed
    │       ├── Any task Failed (unrecoverable) → WO failed
    │       └── Any task Blocked (recoverable) → WO blocked
    │
    ├── Update local state
    │       │
    │       └── work_orders.status = 'completed' | 'failed'
    │
    ├── Update Jira
    │       │
    │       └── Transition WO to Done | Failed status
    │
    └── Publish to message queue
            │
            └── Message: work-order-completed
                    {
                      wo_id: "WO-567",
                      wo_label: "dev-wo",
                      status: "completed",
                      orchestration_item: "PI-456",
                      workbench: "product-abc",
                      completed_at: "2026-05-30T10:30:00Z"
                    }
```

## Message types

### `work-order-completed`

Sent when a WO finishes (success or failure):

| Field | Description |
|-------|-------------|
| `wo_id` | Work Order ID (WO-567) |
| `wo_label` | Workflow correlation label (dev-wo) |
| `status` | `completed` or `failed` |
| `orchestration_item` | Parent OI ID (PI-456) |
| `workbench` | Workbench ID |
| `completed_at` | Completion timestamp |

### `work-order-failed`

Sent when a WO fails with no recovery path:

| Field | Description |
|-------|-------------|
| `wo_id` | Work Order ID |
| `wo_label` | Workflow correlation label |
| `failure_reason` | Why the WO failed |
| `failed_tasks` | List of failed task IDs |
| `orchestration_item` | Parent OI ID |

### `task-blocked`

Sent when a task enters recoverable failure:

| Field | Description |
|-------|-------------|
| `task_id` | Task ID (TASK-890) |
| `wo_id` | Parent WO ID |
| `blocked_reason` | `quota_exhausted`, `agent_disabled`, etc. |
| `blocked_at` | When the block occurred |

This allows Orchestrator workflows to handle blocked tasks (escalate, reassign, etc.).

## Retry handling

If the message queue is unavailable:

1. Message is queued locally in SQLite
2. Background job retries publication with exponential backoff
3. After max retries, message enters local DLQ
4. Alert sent to session owner and Workbench admin

The local queue ensures no completion notifications are lost even during MQ outages.

## Message queue topology

| Topic | Content |
|-------|---------|
| `orchestrator.wo-runtime` | All completion messages from WO Runtime |
| `orchestrator.events.{workbench}` | Partitioned by Workbench for scalability |

The Orchestrator consumes these topics and routes messages to the Workflow Engine.

## Orchestrator handling

When Orchestrator receives `work-order-completed`:

1. Workflow Engine looks up the OI by `orchestration_item` ID
2. Engine matches handlers in the current stage against the event
3. If `wo-label` and `status` match a handler, actions execute
4. Potential outcomes: transition to next stage, invoke governance, create next WO

## Related concepts

- [WO Runtime Daemon](wo-runtime-daemon.md) — Hosts the Completion Reporter
- [Task Manager](task-manager.md) — Detects WO completion
- [Work Order](../../concepts/work-order.md) — What gets reported complete
- [Orchestration Item](../../concepts/orchestration-item.md) — What advances on completion

## Further reading

- [../platform-developer-guide/requirements.md](../platform-developer-guide/requirements.md) — Completion Reporter requirements (WOR-FR-0009, WOR-FR-0010)
- [../../orchestrator/user-guide/orchestration-item-workflow.md](../../orchestrator/user-guide/orchestration-item-workflow.md) — How Orchestrator handles completion events
