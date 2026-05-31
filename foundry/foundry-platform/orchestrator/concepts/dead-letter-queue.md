# Dead Letter Queue

The Dead Letter Queue (DLQ) is the queue for failed workflow actions that require manual intervention before the orchestration item can continue.

## What it is

When the Action Executor encounters a failure that exhausts all retries, it places the failed action into the Dead Letter Queue. The DLQ preserves the full context of the failure — the orchestration item, the action that failed, the error message, and the workflow state at the time of failure.

DLQ items are visible in the Orchestration Console. Administrators can:

- **Retry** — Re-execute the failed action (after fixing the underlying issue)
- **Skip** — Move past the failed action with justification (continues to next action)
- **Abort** — Cancel the orchestration item entirely

The DLQ exists because some failures cannot be automatically recovered. **Technical failures** (API timeout, Atropos unavailable, misconfiguration) may be retried from the DLQ after fixing the root cause. **Work-completion failures** (WO completed with `failed` status, partial WO group, governance rejection) require manual review — the Orchestrator does not auto-re-execute WOs for these outcomes.

See [orchestrator-rules.md](../../../foundry-work-plan/phase-1/orchestrator-rules.md#retry-policy).

DLQ items generate alerts to notify administrators. The goal is prompt resolution: an item in the DLQ represents stalled work.

## Where it lives

| Component | Location |
|-----------|----------|
| **DLQ storage** | Postgres `dlq_items` table |
| **Admin interface** | Orchestration Console (Web App) |
| **Alerts** | Configured notification channel |
| **Metrics** | `orchestrator_dlq_depth` gauge |

## DLQ item structure

| Field | Description |
|-------|-------------|
| `id` | Unique DLQ item ID |
| `orchestration_item` | ID of the affected OI |
| `work_order` | ID of the affected WO (if applicable) |
| `action` | The action that failed (with parameters) |
| `error` | Error message and stack trace |
| `context` | Workflow state snapshot at failure |
| `created_at` | When the item entered the DLQ |
| `status` | `pending`, `retrying`, `skipped`, `resolved` |
| `resolved_by` | User who resolved the item |
| `resolution` | How it was resolved (`retry`, `skip`, `abort`) |
| `justification` | Required justification for `skip` or `abort` |

## Failure types that enter DLQ

| Failure | After retries | DLQ action |
|---------|---------------|------------|
| Jira API 4xx (client error) | None (no retry) | Fix configuration, Retry |
| Jira API 5xx (server error) | 5 retries with backoff | Wait for Jira, Retry |
| Atropos publish failure | 5 retries with backoff | Wait for Atropos, Retry |
| Scenario not found | None | Fix Scenario reference, Retry |
| Invalid workflow definition | None | Fix workflow YAML, Retry |
| Governance timeout | Configurable | Review governance WO, Retry or Skip |
| WO completed `status: failed` | N/A (not retried) | Manual review — no auto WO re-execution |
| WO group `partial` | N/A (not retried) | Manual review of failed members |

## Admin workflow

```
1. Alert: "Item entered DLQ: PI-456, action: create-work-order"
   │
   └── Admin investigates error message
           │
           ├── Root cause: Scenario "implment-feature" typo
           │       │
           │       └── Fix: Correct to "implement-feature" in workflow
           │               │
           │               └── DLQ action: Retry
           │
           └── Root cause: Jira project decommissioned
                   │
                   └── Fix: Cannot recover this PI
                           │
                           └── DLQ action: Abort with justification
```

## Metrics and observability

| Metric | Description |
|--------|-------------|
| `orchestrator_dlq_depth` | Current number of pending DLQ items |
| `orchestrator_dlq_items_total` | Total items entered DLQ (by resolution type) |
| `orchestrator_dlq_age_seconds` | Age of oldest pending DLQ item |

High DLQ depth or long item age indicates systemic issues requiring attention.

## Related concepts

- [Action Executor](action-executor.md) — Places failed actions into DLQ
- [Workflow Engine](workflow-engine.md) — Pauses on DLQ items
- [Gate Enforcement](gate-enforcement.md) — Governance failures may enter DLQ

## Further reading

- [../platform-developer-guide/requirements.md](../platform-developer-guide/requirements.md) — DLQ requirements (ORC-FR-0024 through ORC-FR-0026)
- [../user-guide/orchestration-item-workflow.md](../user-guide/orchestration-item-workflow.md) — Troubleshooting DLQ scenarios
