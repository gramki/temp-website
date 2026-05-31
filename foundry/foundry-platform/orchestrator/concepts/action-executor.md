# Action Executor

The Action Executor is the component that executes workflow actions — creating Work Orders, transitioning orchestration items, invoking governance, and sending notifications.

## What it is

When the Workflow Engine matches a handler, it passes the handler's `then` clause to the Action Executor. The Action Executor runs these actions **sequentially**, passing context from one action to the next. If any action fails, subsequent actions do not execute and the item enters the Dead Letter Queue.

The Action Executor is the bridge between declarative workflow definitions and concrete system operations. It translates high-level actions like `create-work-order` into Work Repository adapter calls, database updates, and Atropos event publications.

Each action type has specific validation rules and side effects:

- `create-work-order` validates that the referenced Scenario exists with `scope: workspace-ingress` before creating the Jira issue
- `invoke-governance-scenario` creates a governance WO and waits for the verdict before allowing subsequent actions
- `transition-orchestration-item` updates both Postgres state and Jira status, then executes the target stage's `on-enter` actions

## Where it lives

| Component | Location |
|-----------|----------|
| **Action Executor** | Orchestrator service |
| **Action Results** | Postgres `work_orders`, `transition_history` tables |
| **External Effects** | Jira (REST API), Atropos |

## Supported actions

| Action | Purpose | External effects |
|--------|---------|------------------|
| `create-work-order` | Create a Work Order for a Scenario in a Workspace | Creates Jira issue, publishes to Atropos for WO Runtime |
| `create-work-order-group` | Create multiple parallel WOs atomically | Batch Jira creation, group tracking in Postgres |
| `create-orchestration-item` | Create OI on target track (cross-track handoff) | Work Repository create, traceability link, start workflow |
| `create-user-task` | Create a manual task for a human | Creates Jira issue (User Task type) |
| `transition-orchestration-item` | Move OI to a new stage | Updates Postgres, Jira; executes `on-enter` |
| `invoke-governance-scenario` | Call governance and await verdict | Creates governance WO, waits for completion |
| `notify` | Send a notification | Email, Slack, or other configured channel |

## Action execution flow

```
Handler matched
    │
    ├── For each action in handler.then:
    │       │
    │       ├── Validate action parameters
    │       ├── Execute action (Jira call, Atropos publish, etc.)
    │       ├── Persist results to Postgres
    │       └── Update context with action outputs
    │
    └── On failure → DLQ
```

## Action parameters

### `create-work-order`

| Parameter | Required | Description |
|-----------|----------|-------------|
| `wo-label` | Yes | Correlation label for completion events |
| `workspace` | Yes | Target Workspace type |
| `scenario` | Yes | Scenario to execute |
| `assignee` | No | Assignment selector (`auto`, `role:X`, `workbench-queue`) |

### `create-work-order-group`

| Parameter | Required | Description |
|-----------|----------|-------------|
| `group-label` | Yes | Correlation label for group completion |
| `work-orders` | Yes | Array of WO definitions (each with `wo-label`, `workspace`, `scenario`) |

### `create-orchestration-item`

Common envelope for cross-track handoff. OI-specific seed fields are defined in track workflow docs.

| Parameter | Required | Description |
|-----------|----------|-------------|
| `track` | Yes | Target track (`discovery`, `build`, `run`, `governance`) |
| `orchestrationItem` | Yes | Target OI kind (e.g. `product-intent`) |
| `title` | Yes | Title for the new OI |
| `seedFrom` | No | Parent entity refs (`workRepoKey`, `entityRefs`) |

See [orchestrator-rules.md](../../../foundry-work-plan/phase-1/orchestrator-rules.md#create-orchestration-item-cross-track-handoff).

### `invoke-governance-scenario`

| Parameter | Required | Description |
|-----------|----------|-------------|
| `scenario` | Yes | Governance Scenario to invoke |
| `on-reject` | No | `hard-block` (default) or `soft-block` |

## Related concepts

- [Workflow Engine](workflow-engine.md) — Invokes Action Executor when handlers match
- [Work Order Group](work-order-group.md) — Created via `create-work-order-group`
- [Gate Enforcement](gate-enforcement.md) — Handles `invoke-governance-scenario` verdicts
- [Dead Letter Queue](dead-letter-queue.md) — Receives failed actions
- [Work Order](../../concepts/work-order.md) — Created by `create-work-order`
- [Scenario](../../concepts/scenario.md) — Referenced in WO creation

## Further reading

- [../platform-developer-guide/requirements.md](../platform-developer-guide/requirements.md) — Action implementation requirements (ORC-FR-*)
- [../user-guide/orchestration-item-workflow.md](../user-guide/orchestration-item-workflow.md) — Runtime execution model
- [../../management/platform-developer-guide/work-catalog-management/oi-workflow-schema.md](../../management/platform-developer-guide/work-catalog-management/oi-workflow-schema.md) — Action YAML schema
