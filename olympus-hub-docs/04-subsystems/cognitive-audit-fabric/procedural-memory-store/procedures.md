# Procedure

> **Status**: 🟡 Draft  
> **Record Type**: `procedure`  
> **Memory Class**: Procedural  
> **Related**: [Procedural Memory README](./README.md) | [Learned Skills](./learned-skills.md)

---

## Overview

A **Procedure** is a **learned step-by-step workflow** derived from observing successful case resolutions. Unlike normative SOPs (which are authored and mandatory), procedures are learned patterns that work well.

> *"Procedures capture 'here's how successful agents solved this' — guidance, not mandate."*

### Key Characteristics

| Aspect | Description |
|--------|-------------|
| **Derived** | Extracted from multiple successful case resolutions |
| **Ordered** | Steps have sequence and dependencies |
| **Conditional** | May include decision points and branches |
| **Measurable** | Success tracked per step and overall |
| **Advisory** | Suggested approach, not required |

---

## Schema

```yaml
# Procedure Record
procedure_id: uuid                # Primary key

# Procedure Identity
name: string                      # Human-readable name
description: string               # What this procedure accomplishes
purpose: string                   # When to use this procedure

# Relationship to Skill
skill_id: uuid                    # Parent skill this implements

# Applicability
applies_to:
  task_types: [string]            # Task types where applicable
  case_types: [string]            # Case types where applicable
  preconditions: [string]         # When procedure is appropriate

# Procedure Steps
steps:
  - step_id: string               # Unique within procedure
    order: integer                # Sequence position
    name: string                  # Step name
    description: string           # What to do
    action_type: enum             # tool_invocation | decision | verification | handoff
    
    # If action_type is tool_invocation
    tool_ref:
      tool_id: uuid               # Tool to invoke
      typical_parameters: object  # Common parameter patterns
    
    # Decision points
    decision_criteria: [string]   # If action_type is decision
    branches:                     # Conditional next steps
      - condition: string
        next_step: string
    
    # Expected outcomes
    expected_outcome: string
    success_indicators: [string]
    
    # Metrics for this step
    step_metrics:
      success_rate: float
      avg_duration: duration
      skip_rate: float            # How often step is skipped

# Overall Metrics
metrics:
  success_rate: float             # Overall procedure success
  completion_rate: float          # How often fully completed
  avg_duration: duration          # Average total time
  application_count: integer      # Times procedure applied

# Confidence & Evidence
confidence: float                 # 0.0 - 1.0
evidence:
  episode_count: integer
  episode_refs: [uuid]            # Sample case_ids
  first_observed: datetime
  last_observed: datetime

# Lifecycle
status: enum                      # candidate | active | validated | deprecated
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
procedure_id: "proc-fraud-pattern-check-001"

name: "First-Party Fraud Investigation Procedure"
description: "Step-by-step process for investigating potential first-party fraud"
purpose: "Use when dispute shows first-party fraud indicators"

skill_id: "a1b2c3d4-5678-90ab-cdef-111213141516"

applies_to:
  task_types: ["fraud_case_investigation"]
  case_types: ["dispute", "chargeback"]
  preconditions:
    - "Transaction dispute initiated by customer"
    - "Initial fraud score > 0.3"

steps:
  - step_id: "step-1"
    order: 1
    name: "Retrieve Transaction History"
    description: "Pull 90-day transaction history for the account"
    action_type: tool_invocation
    tool_ref:
      tool_id: "tool-txn-history-001"
      typical_parameters:
        days: 90
        include_pending: true
    expected_outcome: "Transaction list retrieved"
    success_indicators:
      - "200+ transactions available"
      - "No API errors"
    step_metrics:
      success_rate: 0.99
      avg_duration: "PT3S"
      skip_rate: 0.0

  - step_id: "step-2"
    order: 2
    name: "Analyze Transaction Patterns"
    description: "Identify unusual patterns in recent transactions"
    action_type: tool_invocation
    tool_ref:
      tool_id: "tool-pattern-analyzer-001"
      typical_parameters:
        pattern_types: ["velocity", "merchant_category", "amount_deviation"]
    expected_outcome: "Pattern analysis complete"
    success_indicators:
      - "Pattern score generated"
    step_metrics:
      success_rate: 0.97
      avg_duration: "PT8S"
      skip_rate: 0.02

  - step_id: "step-3"
    order: 3
    name: "Evaluate Fraud Indicators"
    description: "Decide if indicators warrant fraud classification"
    action_type: decision
    decision_criteria:
      - "Pattern score > 0.7"
      - "Velocity anomaly detected"
      - "Customer behavior inconsistent"
    branches:
      - condition: "Strong fraud indicators (score > 0.8)"
        next_step: "step-4a"
      - condition: "Moderate indicators (0.5 < score < 0.8)"
        next_step: "step-4b"
      - condition: "Weak indicators (score < 0.5)"
        next_step: "step-5"
    expected_outcome: "Fraud likelihood determined"
    step_metrics:
      success_rate: 0.91
      avg_duration: "PT2M"
      skip_rate: 0.0

  - step_id: "step-4a"
    order: 4
    name: "Compile Fraud Evidence Package"
    description: "Gather all supporting evidence for fraud determination"
    action_type: tool_invocation
    tool_ref:
      tool_id: "tool-evidence-compiler-001"
    expected_outcome: "Evidence bundle created"
    step_metrics:
      success_rate: 0.95
      avg_duration: "PT5M"
      skip_rate: 0.35  # Often skipped if weak indicators

  - step_id: "step-5"
    order: 5
    name: "Document Decision"
    description: "Record final determination with rationale"
    action_type: verification
    expected_outcome: "Decision record created"
    step_metrics:
      success_rate: 0.99
      avg_duration: "PT1M"
      skip_rate: 0.0

metrics:
  success_rate: 0.88
  completion_rate: 0.92
  avg_duration: "PT12M"
  application_count: 189

confidence: 0.85
evidence:
  episode_count: 189
  episode_refs: ["case-042", "case-067", "case-103"]
  first_observed: "2025-10-01T08:00:00Z"
  last_observed: "2026-01-06T11:30:00Z"

status: validated
created_at: "2025-10-05T09:00:00Z"
updated_at: "2026-01-06T12:00:00Z"

hub_metadata:
  tenant_id: "tenant-acme-bank"
  subscription_id: "sub-fraud-premium"
  workbench_id: "wb-fraud-ops-001"
```

---

## Traversal

### From Procedure
```
procedure_id
  └── skill_id ────► LearnedSkill
  └── steps[].tool_ref.tool_id ──► Tool Registry
  └── evidence.episode_refs[] ───► CaseRecord (episodic)
```

### To Procedure
```
LearnedSkill.implements[] ──► Procedure
ActionSequence.procedure_id ► Procedure
```

---

## Relationship to SOPs

| Learned Procedure | Normative SOP |
|-------------------|---------------|
| "Here's how agents have successfully done this" | "Here's how you must do this" |
| Emerged from experience | Authored by experts |
| Success rate tracked | Compliance tracked |
| May become an SOP if validated | Exists from day one |

When a Procedure is proven highly effective and broadly applicable, it can be **promoted to Enterprise Knowledge** as a formal SOP through governance review.

---

## Related Records

- [Learned Skills](./learned-skills.md) — Parent skill this procedure implements
- [Action Sequences](./action-sequences.md) — Specific execution instances
- [Tool Usage Patterns](./tool-usage-patterns.md) — Tool combinations used in steps

