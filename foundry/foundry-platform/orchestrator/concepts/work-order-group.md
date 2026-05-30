# Work Order Group

A Work Order Group is a mechanism for atomically creating multiple parallel Work Orders and tracking their collective completion as a single workflow event.

## What it is

Some workflow stages require parallel work across multiple Workspaces. For example, when a Product Intent enters the `specified` stage, both Development and QA Preparation should start simultaneously. A Work Order Group bundles these Work Orders together so the workflow can wait for all of them to complete before transitioning.

Work Order Groups provide:

- **Atomic creation** — All WOs in the group are created in a single Jira batch request. Either all succeed or none are created.
- **Collective tracking** — The Orchestrator tracks completion of each WO in the group and fires `work-order-group-completed` only when all have finished.
- **Partial failure handling** — If some WOs complete and others fail, the group reaches a `partial` status that handlers can address.

Groups are identified by a `group-label` that correlates creation with completion events. The label appears in the `foundry-wo-group` Jira attribute on each member WO.

Individual WOs within a group still fire their own `work-order-completed` events. The group completion event is an additional aggregate signal.

## Where it lives

| Component | Location |
|-----------|----------|
| **Group creation** | Action Executor (`create-work-order-group` action) |
| **Group membership** | Postgres `wo_groups` table |
| **Member WOs** | Jira (with `foundry-wo-group` attribute) |
| **Completion tracking** | Orchestrator completion handler |

## Group lifecycle

```
┌──────────────────────────────────────────────────────────────────┐
│  Workflow action: create-work-order-group                         │
│                                                                   │
│  group-label: dev-and-qa-prep                                    │
│  work-orders:                                                     │
│    - wo-label: dev-wo, workspace: development, scenario: impl    │
│    - wo-label: qa-prep-wo, workspace: qa, scenario: test-prep    │
└──────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────────┐
│  Jira: batch create                                               │
│                                                                   │
│  WO-567 (dev-wo)       → assigned to Developer                   │
│  WO-568 (qa-prep-wo)   → assigned to QA Engineer                 │
└──────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────────┐
│  Parallel execution                                               │
│                                                                   │
│  Developer works on WO-567    QA Engineer works on WO-568        │
│           │                              │                        │
│           ▼                              ▼                        │
│  work-order-completed (dev-wo)   work-order-completed (qa-prep)  │
└──────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌──────────────────────────────────────────────────────────────────┐
│  Group completion (when both WOs finish)                          │
│                                                                   │
│  Event: work-order-group-completed                                │
│  Params: { group-label: dev-and-qa-prep, status: completed }     │
└──────────────────────────────────────────────────────────────────┘
```

## Group completion status

| Status | Meaning |
|--------|---------|
| `completed` | All WOs in the group finished successfully |
| `partial` | Some WOs completed, some failed or were cancelled |
| `failed` | All WOs in the group failed |

Workflow handlers can match on group completion status to implement different paths for success vs. partial failure.

## Example workflow usage

```yaml
stages:
  - name: specified
    on-enter:
      - action: create-work-order-group
        params:
          group-label: dev-and-qa-prep
          work-orders:
            - wo-label: dev-wo
              workspace: development
              scenario: implement-product-specification
            - wo-label: qa-prep-wo
              workspace: qa
              scenario: prepare-test-suite-for-product-specification
    handlers:
      - when:
          event: work-order-group-completed
          params:
            group-label: dev-and-qa-prep
            status: completed
        then:
          - action: invoke-governance-scenario
            params:
              scenario: test-plan-review
          - action: transition-orchestration-item
            params:
              to: in-qa
```

## Related concepts

- [Action Executor](action-executor.md) — Executes `create-work-order-group`
- [Workflow Engine](workflow-engine.md) — Matches `work-order-group-completed` events
- [Work Order](../../concepts/work-order.md) — Individual members of the group
- [Task](../../concepts/task.md) — Work within each group member WO

## Further reading

- [../user-guide/product-intent-journey.md](../user-guide/product-intent-journey.md) — See Phase 5 for group example
- [../platform-developer-guide/requirements.md](../platform-developer-guide/requirements.md) — Group requirements (ORC-FR-0017 through ORC-FR-0022)
