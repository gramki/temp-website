# Tool Usage Pattern

> **Status**: 🟡 Draft  
> **Record Type**: `tool_usage_pattern`  
> **Memory Class**: Procedural  
> **Related**: [Procedural Memory README](./README.md) | [Action Sequences](./action-sequences.md)

---

## Overview

A **Tool Usage Pattern** captures **how tools are effectively used together** — which tools pair well, optimal parameter combinations, and effective sequencing. This helps agents leverage tool synergies.

> *"Tool Usage Patterns encode the 'tribal knowledge' of effective tool combinations."*

### Key Characteristics

| Aspect | Description |
|--------|-------------|
| **Tool-centric** | Focused on tool capabilities and combinations |
| **Learned** | Derived from successful tool invocations |
| **Efficiency-oriented** | Captures what works well together |
| **Parameter-aware** | Includes effective parameter patterns |

---

## Schema

```yaml
# Tool Usage Pattern Record
pattern_id: uuid                  # Primary key

# Pattern Identity
name: string                      # Descriptive name
description: string               # What this pattern enables
category: enum                    # data_retrieval | analysis | action | communication

# Scope
skill_id: uuid                    # Related skill (optional)
task_types: [string]              # Where this pattern applies

# Tool Combination
tools:
  primary_tool:
    tool_id: uuid
    tool_name: string
    role: string                  # What role this tool plays
    
  secondary_tools:                # Tools that complement primary
    - tool_id: uuid
      tool_name: string
      role: string
      relationship: enum          # feeds_into | validates | enriches | fallback
      typical_ordering: enum      # before | after | parallel

# Parameter Patterns
parameter_patterns:
  - tool_id: uuid
    effective_parameters:
      parameter_name: string
      recommended_value: any
      rationale: string
    anti_patterns:                # What NOT to do
      - parameter_name: string
        avoid_value: any
        reason: string

# Sequencing
typical_sequence:
  - step: integer
    tool_id: uuid
    condition: string             # When to use this tool

# Metrics
metrics:
  success_rate: float             # When pattern is followed
  observation_count: integer
  avg_combined_duration: duration
  efficiency_gain: float          # vs. using tools separately

# Evidence
evidence:
  source_sequences: [uuid]        # ActionSequence IDs
  episode_count: integer
  first_observed: datetime
  last_observed: datetime

# Lifecycle
status: enum                      # observed | validated | recommended | deprecated
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
pattern_id: "tp-transaction-analysis-001"

name: "Transaction History + Pattern Analysis Combo"
description: "Effective combination for fraud pattern detection"
category: analysis

skill_id: "a1b2c3d4-5678-90ab-cdef-111213141516"
task_types:
  - "fraud_case_investigation"
  - "dispute_analysis"

tools:
  primary_tool:
    tool_id: "tool-txn-history-001"
    tool_name: "get_transaction_history"
    role: "Data retrieval"
    
  secondary_tools:
    - tool_id: "tool-pattern-analyzer-001"
      tool_name: "analyze_transaction_patterns"
      role: "Pattern detection"
      relationship: feeds_into
      typical_ordering: after
      
    - tool_id: "tool-customer-profile-001"
      tool_name: "get_customer_profile"
      role: "Context enrichment"
      relationship: enriches
      typical_ordering: parallel

parameter_patterns:
  - tool_id: "tool-txn-history-001"
    effective_parameters:
      parameter_name: "days"
      recommended_value: 90
      rationale: "90 days provides enough history for pattern detection without noise"
    anti_patterns:
      - parameter_name: "days"
        avoid_value: 365
        reason: "Too much data, slows analysis without improving accuracy"
        
  - tool_id: "tool-pattern-analyzer-001"
    effective_parameters:
      parameter_name: "pattern_types"
      recommended_value: ["velocity", "merchant_category", "amount_deviation"]
      rationale: "These three patterns catch 90% of first-party fraud"
    anti_patterns:
      - parameter_name: "pattern_types"
        avoid_value: ["all"]
        reason: "Too many false positives, analysis takes too long"

typical_sequence:
  - step: 1
    tool_id: "tool-txn-history-001"
    condition: "Always first - provides data for analysis"
  - step: 2
    tool_id: "tool-customer-profile-001"
    condition: "Parallel or after - enriches context"
  - step: 3
    tool_id: "tool-pattern-analyzer-001"
    condition: "After transaction history retrieved"

metrics:
  success_rate: 0.93
  observation_count: 156
  avg_combined_duration: "PT12S"
  efficiency_gain: 0.35  # 35% faster than using tools in isolation

evidence:
  source_sequences:
    - "seq-fraud-investigation-001"
    - "seq-fraud-investigation-002"
  episode_count: 156
  first_observed: "2025-10-15T08:00:00Z"
  last_observed: "2026-01-06T14:00:00Z"

status: recommended
created_at: "2025-10-20T09:00:00Z"
updated_at: "2026-01-06T15:00:00Z"

hub_metadata:
  tenant_id: "tenant-acme-bank"
  subscription_id: "sub-fraud-premium"
  workbench_id: "wb-fraud-ops-001"
```

---

## Traversal

### From Tool Usage Pattern
```
pattern_id
  └── skill_id ─────────► LearnedSkill
  └── tools.*.tool_id ──► Tool Registry
  └── evidence.source_sequences[] ─► ActionSequence
```

### To Tool Usage Pattern
```
LearnedSkill.tool_patterns[] ──► ToolUsagePattern
```

---

## Pattern Categories

| Category | Description | Example |
|----------|-------------|---------|
| `data_retrieval` | Effective data gathering combinations | Transaction + Customer + Account tools |
| `analysis` | Analysis tool combinations | Pattern analyzer + Risk scorer |
| `action` | Action execution patterns | CMS update + Notification tools |
| `communication` | Communication tool patterns | Email template + Customer lookup |

---

## Anti-Patterns

Tool Usage Patterns can also capture **anti-patterns** — combinations or parameter values that don't work well:

```yaml
anti_patterns:
  - pattern: "Call pattern analyzer before transaction history"
    reason: "No data to analyze"
    observed_failure_rate: 1.0
    
  - pattern: "Use 'all' pattern types"
    reason: "Analysis takes too long, many false positives"
    observed_failure_rate: 0.4
```

---

## Related Records

- [Learned Skills](./learned-skills.md) — Parent skill
- [Action Sequences](./action-sequences.md) — Concrete examples of pattern use
- [Procedures](./procedures.md) — Higher-level workflows using these patterns

