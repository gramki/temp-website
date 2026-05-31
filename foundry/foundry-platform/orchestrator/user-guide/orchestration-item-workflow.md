# How the Orchestrator Consumes OI Workflows

## Purpose

This guide explains the runtime mechanics of how the Orchestrator processes OI Workflows. After reading this, you will understand the event-driven execution model: how events trigger handler matching, how actions execute, and how Work Orders flow through the system.

## Audience

| Role | When to use this guide |
|------|------------------------|
| Platform Engineers | Debugging workflow execution issues, understanding internal flow |
| Foundry Admins | Troubleshooting why a transition didn't fire or a Work Order wasn't created |
| Workbench Managers | Understanding how their team's Work Orders are created and assigned |

**Not covered here:**
- Authoring workflows → [Authoring OI Workflows](../../work-catalogues/user-guide/authoring-oi-workflows.md)
- YAML schema reference → [OI Workflow Schema](../management/platform-developer-guide/work-catalog-management/oi-workflow-schema.md)

## Execution Model

The Orchestrator executes workflows through an event-driven loop:

```
Event arrives → Workflow Engine loads definition → Handler matching → Action execution → State update
     ↑                                                                                      │
     └───────────────────────── Completion events ─────────────────────────────────────────┘
```

### 1. Event Arrival

Events enter the Orchestrator via Work Repository adapter webhooks or **Atropos HTTP callbacks** (`/{foundry-id}/foundry.*`):

- `orchestration-item-created` — a new Product Intent, Discovery Case, etc. was created
- `work-order-completed` — a Work Order finished (success or failure)
- `work-order-group-completed` — all Work Orders in a group finished
- `user-task-completed` — a human completed a manual task
- `work-order-timeout` — a Work Order exceeded its timeout
- `governance-completed` — a governance scenario returned a verdict

### 2. Workflow Definition Loading

The Workflow Engine resolves the effective workflow from the Work Catalog hierarchy:

```
User Catalog → Workbench → Workshop → Foundry → Platform Default
```

The closest definition wins. A user with an activated personal catalog can test workflow modifications without affecting others.

For resolution details, see [Work Catalog Resolution Algorithm](../management/platform-developer-guide/work-catalog-management/resolution-algorithm.md).

### 3. Handler Matching

The engine evaluates each handler in the current stage against the incoming event:

1. **Event type match** — the handler's `event` field must match the event type
2. **Parameter match** — all parameters in the handler's `params` must match the event payload
3. **Multiple matches** — if multiple handlers match, all execute

Handlers only match within the OI's current stage. A `work-order-completed` event for `dev-wo` won't match a handler in `ready-for-specification` if the OI is in `in-development`.

### 4. Action Execution

Matched handlers execute their `then` actions **sequentially**:

| Action | What happens |
|--------|--------------|
| `create-work-order` | Orchestrator creates a WO in Work Repository, publishes `/{foundry-id}/foundry.orchestrator.work-order-assigned` via Atropos |
| `create-work-order-group` | Creates multiple WOs atomically; tracks collective completion |
| `create-user-task` | Creates a Jira task assigned to a user or queue |
| `transition-orchestration-item` | Moves the OI to a new stage, executes `on-enter` actions |
| `invoke-governance-scenario` | Calls the Governance module and awaits verdict |
| `notify` | Sends a notification via the configured channel |

If any action fails, subsequent actions do not execute. The OI enters the dead-letter queue (DLQ) for manual intervention.

### 5. Work Order Creation Flow

When `create-work-order` executes:

1. Orchestrator validates the referenced `scenario` exists in the effective Work Catalog with `scope: workspace-ingress`
2. Orchestrator creates a WO record in Postgres and a linked Jira issue
3. WO is assigned based on the `assignee` selector (`auto`, `role:`, `workbench-queue`, etc.)
4. WO Runtime receives a message and activates a Workspace Session for the assignee
5. The Scenario executes within the Session

### 6. Completion Loop

When work completes, the loop restarts:

1. WO Runtime marks the WO complete (success/failure/cancelled)
2. Jira webhook notifies Orchestrator of the status change
3. Orchestrator fires `work-order-completed` with the WO label and status
4. Handlers in the current stage evaluate against the event
5. Matched handlers execute, potentially transitioning to a new stage

For Work Order groups, individual completions are tracked. The `work-order-group-completed` event fires only when all WOs in the group have finished.

## Stage Lifecycle

### On-Enter Actions

When an OI transitions to a stage, `on-enter` actions execute before handlers become active. Common uses:

- Create the initial Work Order for that stage
- Send notifications that work is starting
- Set up parallel Work Order groups

### Timeout Handling

Stages with a `timeout` field fire `work-order-timeout` when the duration elapses. The handler can escalate, reassign, or notify — the workflow definition determines the response.

### Manual Transitions

Workbench Managers and Program Managers can manually transition OIs via the Web Console or API. Manual transitions:

- Bypass workflow handlers
- Execute `on-enter` actions of the target stage
- Are logged in `transition_history` for audit

## State Persistence

| Store | What it holds |
|-------|---------------|
| Postgres | Workflow state, WO labels, group completion tracking, transition history |
| Jira | Work items (OIs, WOs, tasks) — the visible artifact for users |

Postgres is the source of truth for workflow execution state. Jira is updated to reflect state changes but is not queried for orchestration decisions.

## Related

### Concepts

- [Orchestration Item](../../concepts/orchestration-item.md) — Track-level coordination token
- [Work Order](../../concepts/work-order.md) — Instantiation of a Scenario for execution
- [Work Catalog](../../concepts/work-catalog.md) — Hierarchical collection of OI Workflows and Scenarios
- [Governance](../../concepts/governance.md) — Policy enforcement at transitions
- [Workflow Engine](../concepts/workflow-engine.md) — Event-driven processor (module-specific)
- [Action Executor](../concepts/action-executor.md) — Executes workflow actions (module-specific)

### Guides

- [Authoring OI Workflows](../../work-catalogues/user-guide/authoring-oi-workflows.md) — how to create and edit workflows
- [OI Workflow Schema](../../management/platform-developer-guide/work-catalog-management/oi-workflow-schema.md) — canonical YAML reference
- [Orchestrator README](../README.md) — module boundaries and architecture
- [Work Order Runtime](../../work-order-runtime/README.md) — how WOs execute after creation

## Troubleshooting

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Handler not firing | Event parameters don't match | Compare event payload to handler `params` |
| WO not created | Scenario not found or wrong scope | Verify scenario exists with `scope: workspace-ingress` |
| Transition blocked | Governance returned `hard-block` rejection | Check governance verdict and required remediation |
| OI stuck in stage | No handler matches the completion event | Verify `wo-label` and `status` match handler criteria |
| OI in DLQ | Action execution failed | Check Orchestrator logs for the specific failure |
