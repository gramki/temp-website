# Contextual Preference

> **Status**: 🟡 Draft  
> **Record Type**: `contextual_preference`  
> **Memory Class**: Preference  
> **Related**: [Preference Memory README](./README.md) | [User Preferences](./user-preferences.md)

---

## Overview

A **Contextual Preference** captures **preferences that vary depending on context** — situations where a user or agent behaves differently based on circumstances like task type, time pressure, case complexity, or other factors.

> *"Contextual Preferences are the 'it depends' — learned nuances about when preferences change."*

### Key Characteristics

| Aspect | Description |
|--------|-------------|
| **Conditional** | Applies only in specific contexts |
| **Nuanced** | Captures exceptions and variations |
| **Learned** | Derived from observing behavior differences |
| **Specific** | More specific than general preferences |
| **Overriding** | Takes precedence over base preferences in matching context |

---

## Schema

```yaml
# Contextual Preference Record
preference_id: uuid               # Primary key

# Subject
subject:
  type: enum                      # user | agent | role
  subject_id: uuid
  subject_role: string

# Base Preference Reference
base_preference:
  preference_id: uuid             # The general preference this modifies
  category: string
  dimension: string

# Context Condition
context:
  # Context factors (any combination)
  task_type: string
  case_type: string
  complexity: enum                # low | medium | high | critical
  time_pressure: enum             # relaxed | normal | urgent | critical
  workload: enum                  # light | normal | heavy | overloaded
  time_of_day: string             # morning | afternoon | evening | night
  day_type: enum                  # weekday | weekend | holiday
  stakeholder_type: string        # Who is involved
  risk_level: enum                # low | medium | high | critical
  
  # Custom context factors
  custom_factors:
    - factor: string
      value: string

# Contextual Preference Value
preference_value:
  type: enum                      # override | modify | suppress
  
  # For override: completely replace base preference
  override_value: any
  
  # For modify: adjust base preference
  modification:
    direction: enum               # increase | decrease
    magnitude: float              # How much to adjust (0.0 - 1.0)
    
  # For suppress: disable base preference
  suppress_reason: string

# Confidence & Evidence
confidence: float
evidence:
  observation_count: integer
  consistency_in_context: float   # How consistent when context matches
  contrast_with_base: float       # How different from base preference
  first_observed: datetime
  last_observed: datetime
  sample_episodes: [uuid]

# Lifecycle
status: enum                      # observed | active | stable | archived
created_at: datetime
updated_at: datetime

# Hub Context
hub_metadata:
  tenant_id: uuid
  subscription_id: uuid
  workbench_id: uuid
```

---

## Examples

### Under Time Pressure: Less Verbose

```yaml
preference_id: "cpref-001-time-pressure"

subject:
  type: "user"
  subject_id: "user-sarah-analyst-001"
  subject_role: "fraud_analyst"

base_preference:
  preference_id: "pref-user-001-comm"
  category: "communication"
  dimension: "explanation_verbosity"
  # Base preference: prefers verbose (0.8 on scale)

context:
  task_type: null                 # Any task
  case_type: null
  complexity: null
  time_pressure: urgent           # When under time pressure
  workload: heavy                 # And high workload
  time_of_day: null
  day_type: null
  stakeholder_type: null
  risk_level: null
  custom_factors: []

preference_value:
  type: modify
  modification:
    direction: decrease
    magnitude: 0.5                # Reduce verbosity preference by 50%
  # Effective preference in context: 0.4 (concise)

confidence: 0.81
evidence:
  observation_count: 18
  consistency_in_context: 0.89
  contrast_with_base: 0.72        # Significantly different behavior
  first_observed: "2025-11-15T08:00:00Z"
  last_observed: "2026-01-05T16:00:00Z"
  sample_episodes: ["case-078", "case-112"]

status: stable
created_at: "2025-11-20T09:00:00Z"
updated_at: "2026-01-05T17:00:00Z"

hub_metadata:
  tenant_id: "tenant-acme-bank"
  subscription_id: "sub-fraud-premium"
  workbench_id: "wb-fraud-ops-001"
```

### High-Risk Cases: More Conservative

```yaml
preference_id: "cpref-002-high-risk"

subject:
  type: "agent"
  subject_id: "agent-fraud-investigator-001"
  subject_role: "fraud_investigator"

base_preference:
  preference_id: "pref-agent-001-autonomy"
  category: "decision_style"
  dimension: "autonomy_level"
  # Base: moderate autonomy

context:
  task_type: "fraud_case_investigation"
  case_type: null
  complexity: null
  time_pressure: null
  workload: null
  time_of_day: null
  day_type: null
  stakeholder_type: null
  risk_level: high                # High-risk cases
  custom_factors:
    - factor: "case_value"
      value: ">10000"             # High-value cases

preference_value:
  type: override
  override_value:
    autonomy: "minimal"
    escalation: "always"
  # In high-risk/high-value context: always escalate

confidence: 0.93
evidence:
  observation_count: 34
  consistency_in_context: 0.97
  contrast_with_base: 0.85
  first_observed: "2025-10-20T08:00:00Z"
  last_observed: "2026-01-06T12:00:00Z"
  sample_episodes: ["case-045", "case-089", "case-134"]

status: stable
created_at: "2025-10-25T09:00:00Z"
updated_at: "2026-01-06T13:00:00Z"

hub_metadata:
  tenant_id: "tenant-acme-bank"
  subscription_id: "sub-fraud-premium"
  workbench_id: "wb-fraud-ops-001"
```

### Weekend: Batch Processing Preference

```yaml
preference_id: "cpref-003-weekend"

subject:
  type: "user"
  subject_id: "user-sarah-analyst-001"
  subject_role: "fraud_analyst"

base_preference:
  preference_id: "pref-user-001-timing"
  category: "timing"
  dimension: "update_frequency"
  # Base: real-time updates

context:
  task_type: null
  case_type: null
  complexity: null
  time_pressure: null
  workload: null
  time_of_day: null
  day_type: weekend               # On weekends
  stakeholder_type: null
  risk_level: null
  custom_factors: []

preference_value:
  type: override
  override_value: "batch"
  # On weekends: batch updates, don't interrupt

confidence: 0.76
evidence:
  observation_count: 12
  consistency_in_context: 0.83
  contrast_with_base: 0.65
  first_observed: "2025-12-07T10:00:00Z"
  last_observed: "2026-01-04T14:00:00Z"
  sample_episodes: ["case-098", "case-145"]

status: active
created_at: "2025-12-10T09:00:00Z"
updated_at: "2026-01-04T15:00:00Z"

hub_metadata:
  tenant_id: "tenant-acme-bank"
  subscription_id: "sub-fraud-premium"
  workbench_id: "wb-fraud-ops-001"
```

---

## Context Factors

| Factor | Values | Description |
|--------|--------|-------------|
| `task_type` | string | Type of task being performed |
| `case_type` | string | Type of case |
| `complexity` | low/medium/high/critical | Task complexity |
| `time_pressure` | relaxed/normal/urgent/critical | Time constraints |
| `workload` | light/normal/heavy/overloaded | Current workload |
| `time_of_day` | morning/afternoon/evening/night | Time of day |
| `day_type` | weekday/weekend/holiday | Type of day |
| `stakeholder_type` | string | Who is involved |
| `risk_level` | low/medium/high/critical | Risk of the situation |

---

## Preference Resolution

When applying preferences:

```
1. Check for matching ContextualPreference
   └── If match: Apply contextual preference
   └── If no match: Fall back to base preference
       └── If no base: Fall back to system default

Priority: ContextualPreference > BasePreference > SystemDefault
```

For multiple matching contextual preferences, apply **most specific context** (most factors matched).

---

## Traversal

### From Contextual Preference
```
preference_id
  └── base_preference.preference_id ──► UserPreference / AgentBehavior
  └── subject.subject_id ─────────────► User / Agent
  └── evidence.sample_episodes[] ─────► CaseRecord (episodic)
```

### To Contextual Preference
```
(Query by subject_id + context factors)
UserPreference/AgentBehavior ──► (query for contextual variations)
```

---

## Use Cases

| Use Case | Description |
|----------|-------------|
| **Adaptive UX** | Adjust interface based on context |
| **Smart defaults** | Pre-fill based on contextual preferences |
| **Agent tuning** | Adjust agent behavior per context |
| **Workflow routing** | Route tasks based on contextual patterns |

---

## Related Records

- [User Preferences](./user-preferences.md) — Base preferences this modifies
- [Agent Behaviors](./agent-behaviors.md) — Base behaviors this modifies
- [Interaction Patterns](./interaction-patterns.md) — Cross-entity patterns

