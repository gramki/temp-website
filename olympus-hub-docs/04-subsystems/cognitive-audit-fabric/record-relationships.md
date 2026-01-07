# CAF Record Relationships & Traversal

> **Status:** 🟡 Draft — Core relationships defined

This document defines how CAF records relate to each other and the expected traversal patterns for audit, investigation, and analysis.

---

## Overview

CAF records form a **directed graph** with `case_id` as the primary anchor. Every record is reachable from `case_id`, enabling complete case reconstruction.

---

## ID Convention

All CAF record identifiers use **UUID v4** format:

```yaml
id: uuid           # e.g., "550e8400-e29b-41d4-a716-446655440000"
case_id: uuid      # Universal binding anchor
```

| Field | Format | Description |
|-------|--------|-------------|
| `id` | UUID v4 | Unique identifier for this record |
| `case_id` | UUID v4 | Case binding (= `request_id` for Hub-originated) |
| `*_id` references | UUID v4 | All foreign key references |

---

## Record Relationship Graph

```
                                    ┌─────────────────┐
                                    │    case_id      │
                                    │  (anchor UUID)  │
                                    └────────┬────────┘
                                             │
           ┌─────────────────────────────────┼─────────────────────────────────┐
           │                                 │                                 │
           ▼                                 ▼                                 ▼
┌─────────────────────┐        ┌─────────────────────┐        ┌─────────────────────┐
│  ContextSnapshot    │        │   DecisionRecord    │        │  IncidentTimeline   │
│                     │◀───────│                     │        │                     │
│  - id               │        │  - id               │        │  - id               │
│  - case_id ─────────┼────────│  - case_id ─────────┼────────│  - case_id          │
│  - session_id       │        │  - evidence_bundle  │        │  - events[]         │
│  - turn_number      │        │  - context_snapshot │        │                     │
└─────────────────────┘        └──────────┬──────────┘        └─────────────────────┘
                                          │
                    ┌─────────────────────┼─────────────────────┐
                    │                     │                     │
                    ▼                     ▼                     ▼
        ┌───────────────────┐  ┌───────────────────┐  ┌───────────────────┐
        │  EvidenceBundle   │  │   OutcomeRecord   │  │  OverrideRecord   │
        │                   │  │                   │  │                   │
        │  - id             │  │  - id             │  │  - id             │
        │  - case_id        │  │  - case_id        │  │  - case_id        │
        │  - decision_id    │  │  - decision_id    │  │  - orig_decision  │
        │  - context_snap   │  │  - outcome_id     │  │  - evidence_id    │
        └───────────────────┘  └───────────────────┘  └───────────────────┘
                                                               │
                                                               ▼
                                                    ┌───────────────────┐
                                                    │  OutcomeRecord    │
                                                    │  (for override)   │
                                                    └───────────────────┘

        ┌───────────────────┐                      ┌───────────────────┐
        │  HandoffContext   │                      │ HypothesisRecord  │
        │                   │                      │                   │
        │  - id             │                      │  - id             │
        │  - case_id        │                      │  - case_id (opt)  │
        │  - decisions[]    │                      │  - evidence[]     │
        │  - evidence[]     │                      │                   │
        └───────────────────┘                      └───────────────────┘
```

---

## Relationship Definitions

### Primary Relationships

| From | To | Relationship | Cardinality | Field |
|------|-----|--------------|-------------|-------|
| **DecisionRecord** | EvidenceBundle | captures evidence for | 1:1 | `evidence_bundle_id` |
| **DecisionRecord** | ContextSnapshot | made with context | 1:1 | `context_snapshot_id` |
| **EvidenceBundle** | DecisionRecord | documents | 1:1 | `decision_record_id` |
| **EvidenceBundle** | ContextSnapshot | includes | 1:1 | `context_snapshot_id` |
| **OutcomeRecord** | DecisionRecord | measures result of | N:1 | `decision_record_id` |
| **OverrideRecord** | DecisionRecord | overrides | 1:1 | `original_decision_id` |
| **OverrideRecord** | EvidenceBundle | supported by | 1:1 | `evidence_bundle_id` |
| **OverrideRecord** | OutcomeRecord | tracked by | 1:1 | `outcome_record_id` |
| **HandoffContext** | DecisionRecord[] | summarizes | 1:N | `decisions_made[]` |
| **HandoffContext** | EvidenceBundle[] | references | 1:N | `evidence_gathered[]` |
| **IncidentTimeline** | DecisionRecord[] | chronicles | 1:N | `events[].linked_records.decision_record_id` |
| **HypothesisRecord** | * | derived from | 1:N | `supporting_evidence[]`, `counter_evidence[]` |

### Inverse Relationships (Queryable)

| Record | Can Find Via |
|--------|--------------|
| All records for a case | `case_id` |
| Evidence for a decision | `DecisionRecord.evidence_bundle_id` |
| Context for a decision | `DecisionRecord.context_snapshot_id` |
| Outcome of a decision | Query `OutcomeRecord` by `decision_record_id` |
| Override of a decision | Query `OverrideRecord` by `original_decision_id` |
| Decisions in a handoff | `HandoffContext.decisions_made[]` |
| Decisions in an incident | `IncidentTimeline.events[].linked_records` |

---

## Traversal Patterns

### 1. Case Reconstruction (Forward Traversal)

Starting from `case_id`, reconstruct complete case history:

```
case_id
  │
  ├──▶ ContextSnapshots (all turns)
  │      └── by case_id, ordered by timestamp
  │
  ├──▶ DecisionRecords (all decisions)
  │      └── by case_id, ordered by timestamp
  │      │
  │      └──▶ EvidenceBundle (per decision)
  │      └──▶ OutcomeRecord (if available)
  │      └──▶ OverrideRecord (if overridden)
  │
  ├──▶ HandoffContexts (agent transitions)
  │      └── by case_id, ordered by timestamp
  │
  └──▶ IncidentTimelines (if escalated/investigated)
         └── by case_id
```

**Query Pattern:**
```sql
-- All records for a case
SELECT * FROM decision_records WHERE case_id = ?;
SELECT * FROM evidence_bundles WHERE case_id = ?;
SELECT * FROM context_snapshots WHERE case_id = ?;
SELECT * FROM outcome_records WHERE case_id = ?;
SELECT * FROM override_records WHERE case_id = ?;
SELECT * FROM handoff_contexts WHERE case_id = ?;
SELECT * FROM incident_timelines WHERE case_id = ?;
```

### 2. Decision Audit (Depth Traversal)

For a specific decision, retrieve complete audit package:

```
DecisionRecord
  │
  ├──▶ EvidenceBundle
  │      ├── context (session_state, agent_memory, ...)
  │      ├── data (entity_snapshots, documents, ...)
  │      ├── model (prompts, completions, predictions)
  │      └── retrieval (queries, results, rankings)
  │
  ├──▶ ContextSnapshot
  │      └── context_frame (constraints, goal, facts, precedent, ...)
  │
  ├──▶ OutcomeRecord (if exists)
  │      └── expected_outcome, actual_outcome, variance
  │
  └──▶ OverrideRecord (if exists)
         ├── rationale, supporting_evidence
         └── OutcomeRecord (override outcome)
```

**Query Pattern:**
```sql
-- Decision audit package
SELECT * FROM decision_records WHERE id = ?;
SELECT * FROM evidence_bundles WHERE decision_record_id = ?;
SELECT * FROM context_snapshots WHERE id = (SELECT context_snapshot_id FROM decision_records WHERE id = ?);
SELECT * FROM outcome_records WHERE decision_record_id = ?;
SELECT * FROM override_records WHERE original_decision_id = ?;
```

### 3. Outcome Analysis (Backward Traversal)

Starting from an outcome, trace back to understand what led to it:

```
OutcomeRecord
  │
  └──▶ DecisionRecord
         │
         ├──▶ EvidenceBundle (what was known)
         ├──▶ ContextSnapshot (what context was provided)
         └──▶ case_id ──▶ Prior Decisions (decision history)
```

### 4. Pattern Discovery (Cross-Case Traversal)

For hypothesis validation, traverse across cases:

```
HypothesisRecord
  │
  ├──▶ supporting_evidence[]
  │      └── DecisionRecord, OutcomeRecord, OverrideRecord (any type)
  │
  └──▶ counter_evidence[]
         └── Same types, challenging the hypothesis
```

### 5. Session Replay (Temporal Traversal)

Replay an agent session turn-by-turn:

```
session_id
  │
  └──▶ ContextSnapshots (ordered by turn_number)
         │
         ├── Turn 1: context_frame, retrieval_log
         ├── Turn 2: context_frame, retrieval_log
         │     └──▶ DecisionRecord (if decision made)
         ├── Turn 3: ...
         └── Turn N: ...
```

---

## Required Linking Fields per Record

### DecisionRecord
```yaml
# Forward links
evidence_bundle_id: uuid       # → EvidenceBundle
context_snapshot_id: uuid      # → ContextSnapshot

# Traversal anchor
case_id: uuid                  # Case binding

# Inverse links (queryable, not stored)
# - OutcomeRecord.decision_record_id → this
# - OverrideRecord.original_decision_id → this
```

### EvidenceBundle
```yaml
# Forward links
decision_record_id: uuid       # → DecisionRecord (1:1)
context_snapshot_id: uuid      # → ContextSnapshot (embedded or reference)

# Traversal anchor
case_id: uuid
```

### ContextSnapshot
```yaml
# Forward links
linked_records: array          # → EvidenceBundle (if decision turn)

# Session context
session_id: uuid               # Session grouping
turn_number: integer           # Order within session

# Traversal anchor
case_id: uuid
```

### OutcomeRecord
```yaml
# Forward links
decision_record_id: uuid       # → DecisionRecord this outcome measures

# Traversal anchor
case_id: uuid
```

### OverrideRecord
```yaml
# Forward links
original_decision_id: uuid     # → DecisionRecord being overridden
evidence_bundle_id: uuid       # → EvidenceBundle for override
outcome_record_id: uuid        # → OutcomeRecord (populated later)

# Traversal anchor
case_id: uuid
```

### HandoffContext
```yaml
# Forward links (arrays of references)
decisions_made: array[uuid]    # → DecisionRecord[]
evidence_gathered: array[uuid] # → EvidenceBundle[]

# Traversal anchor
case_id: uuid
```

### IncidentTimeline
```yaml
# Forward links (embedded in events)
events[].linked_records:
  decision_record_id: uuid     # → DecisionRecord
  evidence_bundle_id: uuid     # → EvidenceBundle
  request_id: uuid             # → Hub Request
  task_id: uuid                # → Task

# Traversal anchor
case_id: uuid
```

### HypothesisRecord
```yaml
# Forward links (evidence references)
supporting_evidence[].record_id: uuid  # → Any record type
counter_evidence[].record_id: uuid     # → Any record type

# Traversal anchor (optional - hypotheses may span cases)
case_id: uuid                  # Optional
```

---

## Indexing Requirements

For efficient traversal, the following indexes are required:

| Index | Purpose |
|-------|---------|
| `case_id` (all records) | Case reconstruction |
| `decision_record_id` (OutcomeRecord, OverrideRecord) | Decision audit |
| `original_decision_id` (OverrideRecord) | Override lookup |
| `session_id + turn_number` (ContextSnapshot) | Session replay |
| `timestamp` (all records) | Temporal ordering |
| `entity_type + entity_id` (DecisionRecord) | Entity history |

---

## Consistency Rules

| Rule | Description |
|------|-------------|
| **Case ID Propagation** | All records created within a case MUST share the same `case_id` |
| **Decision-Evidence Pairing** | Every DecisionRecord SHOULD have an EvidenceBundle |
| **Context Reference** | DecisionRecord.context_snapshot_id MUST reference a valid ContextSnapshot |
| **Override Chain** | OverrideRecord.original_decision_id MUST reference a valid DecisionRecord |
| **Outcome Linkage** | OutcomeRecord.decision_record_id MUST reference a valid DecisionRecord |
| **UUID Format** | All `*_id` fields MUST be valid UUID v4 |

---

## Related Documentation

- [CAF Overview](./README.md)
- [Decision Records](./decision-records.md)
- [Evidence Bundles](./evidence-bundles.md)
- [Context Snapshots](./context-snapshots.md)

---

*TODO: Add API examples for common traversal queries*

