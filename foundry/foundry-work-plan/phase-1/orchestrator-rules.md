# Phase 1 Orchestrator Rules

**Status:** Authoritative SSOT for Orchestrator state model, action contracts, retry semantics, workflow versioning, and Release Intent milestone behavior.

Normative implementation requirements: [orchestrator/platform-developer-guide/requirements.md](../../foundry-platform/orchestrator/platform-developer-guide/requirements.md).

---

## State store

Postgres is the **authoritative read/write state store** for workflow execution. This is **not event sourcing** — current state is queried from Postgres tables.

| Table | Purpose |
|-------|---------|
| `orchestration_items` | OI identity, stage, pinned `workflowVersion`, containment IDs |
| `workflow_stages` | Current stage and pending handlers per item |
| `work_orders` | WO tracking with labels and groups |
| `wo_groups` | WO Group membership and completion tracking |
| `transition_history` | Audit log of all state transitions |
| `dlq_items` | Dead Letter Queue for failed actions |

**Emit-on-write:** Every state transition persisted to Postgres MUST also publish a platform event to Atropos per [event-contracts.md](event-contracts.md). Consumers use events for fan-out; Orchestrator reads current state from Postgres.

Jira remains the Work Repository adapter store for work items; Orchestrator reads and writes via the adapter.

---

## Retry policy

### Technical failures — auto-retry

**All workflow actions** (`create-work-order`, `create-orchestration-item`, `transition-orchestration-item`, etc.) MAY be retried automatically when the failure is **technical**:

| Failure class | Examples | Retry |
|---------------|----------|-------|
| Transient API | Jira timeout/5xx, Management API timeout | Exponential backoff |
| Infrastructure | Atropos publish failure, Postgres write failure | Exponential backoff |
| Exhausted retries | Any of the above after budget | DLQ for manual retry |

Jira 4xx (client/configuration error) is not retried — route to DLQ immediately.

### Work-completion semantics — no auto-retry

Failures that reflect **work outcome**, not infrastructure, MUST NOT be auto-retried:

| Situation | Behavior |
|-----------|----------|
| WO completed with `status: failed` | Surface to operator; manual review |
| Partial WO group (`partial` status) | Do not auto-create replacement WOs; manual review |
| Governance rejection (`hard-block` / `soft-block`) | Per gate policy; no automatic re-invocation |
| Incorrect or incomplete WO output | Manual intervention; no automatic WO re-execution |

WO Runtime MAY retry **Atropos delivery** of completion events (technical). Re-running the WO after a completion event is not automatic.

---

## Workflow versioning

When platform or scope-level workflow YAML changes:

1. **Pin at OI creation** — store `workflowVersion` (from workflow `metadata.version`) and resolved catalog source on `orchestration_items`.
2. **In-flight OIs** — continue using the pinned version until the OI reaches a terminal stage.
3. **New OIs** — resolve the current effective workflow from Work Catalog hierarchy (User > Workbench > Workshop > Foundry > Platform).

Old workflow versions remain available in the catalog for in-flight OIs. Removing a version in use by active OIs is forbidden.

See [oi-workflow-schema.md](../../foundry-platform/management/platform-developer-guide/work-catalog-management/oi-workflow-schema.md#workflow-version-pinning).

---

## `create-orchestration-item` (cross-track handoff)

Common action envelope for G10 cross-track handoff. OI-specific seed payloads are defined in track/OI workflow docs — not duplicated here.

```yaml
- action: create-orchestration-item
  params:
    track: build                    # target track: discovery | build | run | governance
    orchestrationItem: product-intent
    title: string                 # required
    seedFrom:                     # parent entity refs
      workRepoKey: DC-89          # optional: Work Repository binding
      entityRefs:                 # optional: Intent Repository / traceability refs
        - kind: discovery-case
          id: DC-89
    # foundryId, workshopId, workbenchId inherited from parent OI unless overridden
```

**Orchestrator responsibilities:**

1. Allocate new OI ID via Management Metadata Service
2. Create Work Item in Work Repository (Jira adapter) on target track
3. Link parent → child in traceability store
4. Pin workflow version for the new OI
5. Start target workflow at `start` stage (or configured entry stage)
6. Emit Atropos event per [event-contracts.md](event-contracts.md)

**Phase 1 trigger:** Discovery Case workflow `user-task-completed` with outcome `proceed-to-build`. See [contract-gates.md](../integration/contract-gates.md) G10 and [golden-path.md](golden-path.md).

---

## Release Intent milestones

Two distinct behaviors — both apply; they do not contradict.

### Manual initiation (Phase 1)

Release Intent milestones such as `product-specification-development-start` are **set manually** by the Program Manager. Phase 1 has **no scheduled/calendar automation** for milestone initiation.

A Product Intent enters `ready-for-specification` via **manual approval** (draft-approval user task), not on a schedule.

### System-derived tracking

The Orchestrator **auto-sets roll-up milestones** on the Release Intent when tagged PIs enter or complete stages (e.g. `development-started` when the first tagged PI enters Development). These are observational aggregates — not scheduled triggers.

When a PM **manually sets** a milestone on a Release Intent, the Orchestrator fires `release-intent-milestone-reached` for each tagged PI in the matching wait stage (e.g. `ready-for-specification` for `product-specification-development-start`).

---

## Read next

- [event-contracts.md](event-contracts.md) — Atropos paths and envelope
- [module-boundaries.md](module-boundaries.md) — cross-module flows
- [integration/contract-gates.md](../integration/contract-gates.md) — G10 handoff gate
- [orchestrator/concepts/dead-letter-queue.md](../../foundry-platform/orchestrator/concepts/dead-letter-queue.md) — DLQ operations
