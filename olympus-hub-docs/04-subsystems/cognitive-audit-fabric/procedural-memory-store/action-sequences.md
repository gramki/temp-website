# Action Sequence

> **Status**: 🟡 Draft  
> **Record Type**: `action_sequence`  
> **Memory Class**: Procedural  
> **Related**: [Procedural Memory README](./README.md) | [Procedures](./procedures.md)

---

## Overview

An **Action Sequence** is a **specific pattern of actions** that has been observed to succeed in accomplishing a task. It's more concrete than a Procedure — capturing the actual sequence of tool invocations and decisions as they occurred.

> *"Action Sequences are the 'replay templates' — specific successful patterns that can be followed or adapted."*

### Key Characteristics

| Aspect | Description |
|--------|-------------|
| **Concrete** | Actual tool calls with parameters |
| **Ordered** | Strict sequence with timing |
| **Observed** | Derived from actual case execution |
| **Replayable** | Can serve as a template |
| **Contextual** | Tied to specific case conditions |

---

## Schema

```yaml
# Action Sequence Record
sequence_id: uuid                 # Primary key

# Sequence Identity
name: string                      # Descriptive name
description: string               # What this sequence accomplishes

# Relationships
skill_id: uuid                    # Parent skill (optional)
procedure_id: uuid                # Procedure this exemplifies (optional)

# Context
context:
  task_type: string               # Task type where observed
  case_type: string               # Case type where observed
  conditions: [string]            # Conditions present when successful

# Action Steps (in order)
actions:
  - action_id: string             # Unique within sequence
    order: integer                # Execution order
    action_type: enum             # tool_call | decision | wait | handoff
    
    # Tool call details
    tool:
      tool_id: uuid
      tool_name: string
      parameters: object          # Actual parameters used
      
    # Timing
    timestamp_offset: duration    # Relative to sequence start
    duration: duration            # How long action took
    
    # Outcome
    outcome:
      status: enum                # success | partial | failed
      result_summary: string

# Overall Metrics
metrics:
  success_rate: float             # When this sequence is followed
  observation_count: integer      # Times this exact pattern seen
  avg_total_duration: duration
  last_observed: datetime

# Source Evidence
evidence:
  source_episodes: [uuid]         # Case IDs where observed
  first_observed: datetime
  canonical_episode: uuid         # Best example case

# Lifecycle
status: enum                      # observed | validated | template | deprecated
created_at: datetime
updated_at: datetime

# Hub Context
hub_metadata:
  tenant_id: uuid
  subscription_id: uuid
  workbench_id: uuid
```

---

## Example

```yaml
sequence_id: "seq-fraud-investigation-001"

name: "Quick Fraud Pattern Check Sequence"
description: "Efficient sequence for identifying first-party fraud patterns"

skill_id: "a1b2c3d4-5678-90ab-cdef-111213141516"
procedure_id: "proc-fraud-pattern-check-001"

context:
  task_type: "fraud_case_investigation"
  case_type: "dispute"
  conditions:
    - "Customer-initiated dispute"
    - "Initial fraud score between 0.3 and 0.6"
    - "Account age > 1 year"

actions:
  - action_id: "act-1"
    order: 1
    action_type: tool_call
    tool:
      tool_id: "tool-txn-history-001"
      tool_name: "get_transaction_history"
      parameters:
        account_id: "{context.account_id}"
        days: 90
        include_pending: true
    timestamp_offset: "PT0S"
    duration: "PT2.5S"
    outcome:
      status: success
      result_summary: "Retrieved 342 transactions"

  - action_id: "act-2"
    order: 2
    action_type: tool_call
    tool:
      tool_id: "tool-pattern-analyzer-001"
      tool_name: "analyze_transaction_patterns"
      parameters:
        transaction_data: "{act-1.result}"
        pattern_types: ["velocity", "merchant_category"]
    timestamp_offset: "PT3S"
    duration: "PT7S"
    outcome:
      status: success
      result_summary: "Pattern score: 0.72, velocity anomaly detected"

  - action_id: "act-3"
    order: 3
    action_type: decision
    tool:
      tool_id: null
      tool_name: null
      parameters:
        decision: "escalate_for_review"
        rationale: "Pattern score above threshold, velocity anomaly present"
    timestamp_offset: "PT10S"
    duration: "PT30S"
    outcome:
      status: success
      result_summary: "Escalated to senior investigator"

  - action_id: "act-4"
    order: 4
    action_type: tool_call
    tool:
      tool_id: "tool-evidence-compiler-001"
      tool_name: "compile_evidence_bundle"
      parameters:
        case_id: "{context.case_id}"
        include: ["transactions", "patterns", "customer_history"]
    timestamp_offset: "PT45S"
    duration: "PT4M"
    outcome:
      status: success
      result_summary: "Evidence bundle created with 12 items"

metrics:
  success_rate: 0.91
  observation_count: 47
  avg_total_duration: "PT5M30S"
  last_observed: "2026-01-05T16:20:00Z"

evidence:
  source_episodes:
    - "case-042"
    - "case-067"
    - "case-089"
  first_observed: "2025-11-01T10:00:00Z"
  canonical_episode: "case-067"

status: template
created_at: "2025-11-05T09:00:00Z"
updated_at: "2026-01-05T17:00:00Z"

hub_metadata:
  tenant_id: "tenant-acme-bank"
  subscription_id: "sub-fraud-premium"
  workbench_id: "wb-fraud-ops-001"
```

---

## Traversal

### From Action Sequence
```
sequence_id
  └── skill_id ────────► LearnedSkill
  └── procedure_id ────► Procedure
  └── actions[].tool.tool_id ──► Tool Registry
  └── evidence.source_episodes[] ─► CaseRecord (episodic)
```

### To Action Sequence
```
LearnedSkill.patterns[] ──────► ActionSequence
Procedure (conceptual link) ──► ActionSequence
```

---

## Use Cases

| Use Case | Description |
|----------|-------------|
| **Template for agents** | New agents can follow validated sequences |
| **Training examples** | Used to train new agent models |
| **Debugging** | Compare actual execution to known-good sequences |
| **Optimization** | Identify which sequences are most efficient |
| **Procedure extraction** | Multiple similar sequences → abstracted Procedure |

---

## Status States

| State | Description |
|-------|-------------|
| `observed` | Pattern detected, under observation |
| `validated` | Confirmed successful across multiple cases |
| `template` | Recommended as a template for similar tasks |
| `deprecated` | No longer recommended (e.g., tools changed) |

---

## Related Records

- [Learned Skills](./learned-skills.md) — Parent skill
- [Procedures](./procedures.md) — Abstract procedure this exemplifies
- [Tool Usage Patterns](./tool-usage-patterns.md) — Tool combinations extracted from sequences

