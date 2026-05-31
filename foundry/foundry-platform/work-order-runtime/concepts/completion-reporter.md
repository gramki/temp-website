# Completion Reporter

The Completion Reporter is the component that notifies the Orchestrator when Work Orders reach terminal states — completed, failed, or blocked — enabling orchestration workflows to advance.

## What it is

When a Work Order finishes, the Orchestrator needs to know so it can fire the appropriate workflow events and potentially transition the parent orchestration item. The Completion Reporter publishes events to **Atropos** at paths `/{foundry-id}/foundry.wo-runtime.{event-semantic-name}`. Orchestrator subscribes via HTTP callbacks.

The Completion Reporter monitors Work Order state within the session and sends:

- `work-order-completed` — WO finished successfully
- `work-order-failed` — WO failed with no retry available
- `task-blocked` — A task entered recoverable failure (quota, agent disabled, etc.)

Events use the canonical Foundry envelope (see [event-contracts.md](../../../foundry-work-plan/phase-1/event-contracts.md)) with `entityRefs` and `workRepoKey` where applicable.

## Where it lives

| Component | Location |
|-----------|----------|
| **Completion Reporter** | WO Runtime Daemon |
| **Atropos** | Olympus event fabric (HTTP callbacks to Orchestrator) |
| **Orchestrator consumer** | Orchestrator callback endpoint |
| **Local queue** | SQLite (for retry on Atropos delivery failure) |

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
    ├── Update Work Repository (adapter)
    │       │
    │       └── Transition WO to Done | Failed status
    │
    └── Publish to Atropos
            │
            └── Path: /foundry-zeta/foundry.wo-runtime.work-order-completed
                    Envelope: { foundryId, workshopId, workbenchId, correlationId,
                                 entityRefs: [{ entityId: "WO-567", workRepoKey: "…" }],
                                 payload: { status: "completed", … } }
```

## Event types

### `work-order-completed`

Atropos path: `/{foundry-id}/foundry.wo-runtime.work-order-completed`

| Field | Location | Description |
|-------|----------|-------------|
| `entityRefs[].entityId` | envelope | Work Order ID (WO-567) |
| `payload.status` | payload | `completed` or `failed` |
| `entityRefs[].workRepoKey` | envelope | Work Repository item key |
| `payload.outputs` | payload | Artifact URIs, PR links, etc. |
| `correlationId` | envelope | End-to-end trace id |

### `work-order-failed`

Atropos path: `/{foundry-id}/foundry.wo-runtime.work-order-failed`

| Field | Location | Description |
|-------|----------|-------------|
| `payload.failureReason` | payload | Why the WO failed |
| `payload.failedTasks` | payload | List of failed task IDs |

### `task-blocked`

Atropos path: `/{foundry-id}/foundry.wo-runtime.task-blocked`

| Field | Location | Description |
|-------|----------|-------------|
| `payload.blockedReason` | payload | `quota_exhausted`, `agent_disabled`, etc. |

This allows Orchestrator workflows to handle blocked tasks (escalate, reassign, etc.).

## Retry handling

If Atropos delivery is unavailable:

1. Event is queued locally in SQLite
2. Background job retries publication with exponential backoff
3. After max retries, event enters local DLQ
4. Alert sent to session owner and Workbench admin

The local queue ensures no completion notifications are lost even during Atropos outages.

## Atropos paths (Phase 1)

| Path | Content |
|------|---------|
| `/{foundry-id}/foundry.wo-runtime.work-order-completed` | WO terminal success |
| `/{foundry-id}/foundry.wo-runtime.work-order-failed` | WO terminal failure |
| `/{foundry-id}/foundry.wo-runtime.task-blocked` | Recoverable task failure |

Orchestrator registers HTTP callbacks for these paths. See [event-contracts.md](../../../foundry-work-plan/phase-1/event-contracts.md).

## Orchestrator handling

When Orchestrator receives `work-order-completed`:

1. Workflow Engine looks up the OI from `entityRefs` or `payload`
2. Engine matches handlers in the current stage against the event
3. If `foundry-wo-label` and `status` match a handler, actions execute
4. Potential outcomes: transition to next stage, invoke governance, create next WO

## Related concepts

- [WO Runtime Daemon](wo-runtime-daemon.md) — Hosts the Completion Reporter
- [Task Manager](task-manager.md) — Detects WO completion
- [Work Order](../../concepts/work-order.md) — What gets reported complete
- [Orchestration Item](../../concepts/orchestration-item.md) — What advances on completion

## Further reading

- [../platform-developer-guide/requirements.md](../platform-developer-guide/requirements.md) — Completion Reporter requirements (WOR-FR-0009, WOR-FR-0010)
- [../../orchestrator/user-guide/orchestration-item-workflow.md](../../orchestrator/user-guide/orchestration-item-workflow.md) — How Orchestrator handles completion events
- [../../../foundry-work-plan/phase-1/event-contracts.md](../../../foundry-work-plan/phase-1/event-contracts.md) — Authoritative envelope and path spec
