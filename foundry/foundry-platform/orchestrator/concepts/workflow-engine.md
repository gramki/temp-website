# Workflow Engine

The Workflow Engine is the event-driven processor that evaluates OI Workflow definitions, matches incoming events to handlers, and orchestrates the execution of workflow actions.

## What it is

The Workflow Engine is the core of the Orchestrator. It implements an event-driven loop that processes orchestration item lifecycle events:

1. **Event arrives** — Work Repository adapter webhooks or Atropos HTTP callbacks deliver events (item created, WO completed, governance verdict, etc.)
2. **Workflow loaded** — The engine resolves the effective workflow from the Work Catalog hierarchy (User → Workbench → Workshop → Foundry → Platform)
3. **Handlers matched** — Each handler in the current stage is evaluated against the incoming event
4. **Actions executed** — Matched handlers invoke the Action Executor to run their `then` actions sequentially

The engine maintains stage state for each orchestration item. An item's current stage determines which handlers are eligible to match. When a transition action executes, the item moves to a new stage and its `on-enter` actions run.

Workflow definitions are declarative YAML stored in the Work Catalog. The engine interprets these definitions at runtime — coordination logic is configuration, not code. This enables Workbench-level customization without platform engineering involvement.

## Where it lives

| Component | Location |
|-----------|----------|
| **Workflow Engine** | Orchestrator service |
| **Workflow Definitions** | Work Catalog (`work-catalog/{track}/{oi-type}/workflow.yaml`) |
| **Stage State** | Postgres `workflow_stages` table |
| **Transition History** | Postgres `transition_history` table |

## Event types processed

| Event | Source | Typical trigger |
|-------|--------|-----------------|
| `orchestration-item-created` | Jira webhook | New PI, Discovery Case, etc. created |
| `work-order-completed` | WO Runtime via MQ | Work Order finished |
| `work-order-group-completed` | Internal | All WOs in a group finished |
| `user-task-completed` | Jira webhook | Human completed a manual task |
| `work-order-timeout` | Timeout checker job | WO exceeded its timeout |
| `governance-completed` | Governance module | Governance scenario returned verdict |
| `release-intent-milestone-reached` | Internal | Release Intent milestone set |

## Handler matching rules

A handler matches when:

1. Its `event` field matches the incoming event type
2. All parameters in its `params` clause match the event payload
3. The handler is defined in the orchestration item's *current stage*

Multiple handlers can match the same event. All matching handlers execute.

## Resolution hierarchy

Workflow definitions are resolved from the Work Catalog with closest-wins semantics:

```
User Catalog (if activated)
    └── Workbench Catalog
        └── Workshop Catalog
            └── Foundry Catalog
                └── Platform Default
```

A user with an activated personal catalog can test workflow modifications in their sessions without affecting team workflows.

## Related concepts

- [Action Executor](action-executor.md) — Runs the `then` actions from matched handlers
- [Dead Letter Queue](dead-letter-queue.md) — Where failed actions go
- [Gate Enforcement](gate-enforcement.md) — How governance integrates with transitions
- [Work Order](../../concepts/work-order.md) — Created by workflow actions
- [Scenario](../../concepts/scenario.md) — Referenced in `create-work-order` actions
- [Work Catalog](../../concepts/work-catalog.md) — Where workflows are stored

## Further reading

- [../user-guide/orchestration-item-workflow.md](../user-guide/orchestration-item-workflow.md) — How the Orchestrator consumes OI Workflows
- [../../work-catalogues/user-guide/authoring-oi-workflows.md](../../work-catalogues/user-guide/authoring-oi-workflows.md) — Workflow authoring guide
- [../../management/platform-developer-guide/work-catalog-management/oi-workflow-schema.md](../../management/platform-developer-guide/work-catalog-management/oi-workflow-schema.md) — YAML schema reference
- [../platform-developer-guide/requirements.md](../platform-developer-guide/requirements.md) — Implementation requirements
