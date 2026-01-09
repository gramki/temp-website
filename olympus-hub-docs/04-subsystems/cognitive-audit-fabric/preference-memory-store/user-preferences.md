# User Preference

> **Status**: 🟡 Draft  
> **Record Type**: `user_preference`  
> **Memory Class**: Preference  
> **Related**: [Preference Memory README](./README.md) | [Interaction Patterns](./interaction-patterns.md)

---

## Overview

A **User Preference** captures a **learned preference for a human user** — how they prefer to receive information, make decisions, and interact with the system. These are inferred from observed behavior, not explicitly stated.

> *"User Preferences are what we've learned about how someone likes things done — personalization through observation."*

### Key Characteristics

| Aspect | Description |
|--------|-------------|
| **Inferred** | Derived from observed choices |
| **Personal** | Belongs to a specific user |
| **Contextual** | May vary by situation |
| **Probabilistic** | Confidence-weighted |
| **Evolving** | Updates with new evidence |

---

## Schema

```yaml
# User Preference Record
preference_id: uuid               # Primary key

# Subject
subject:
  type: "user"
  user_id: uuid                   # User this preference belongs to
  user_role: string               # User's role (for role-level defaults)

# Preference Definition
preference:
  category: enum                  # communication | presentation | risk | timing | interaction
  dimension: string               # Specific dimension within category
  
  # The preference itself
  preference_type: enum           # binary | scale | choice | behavior
  
  # For binary preferences (prefers/avoids)
  binary_value:
    prefers: boolean
    
  # For scale preferences (e.g., verbosity 1-10)
  scale_value:
    value: float                  # 0.0 - 1.0 normalized
    scale_name: string            # e.g., "concise ← → verbose"
    
  # For choice preferences (option A vs B)
  choice_value:
    preferred: string
    over: [string]                # Alternatives not preferred
    
  # For behavioral preferences
  behavior_value:
    pattern: string               # Description of preferred behavior
    context: string               # When this applies

# Context (when preference applies)
context:
  task_types: [string]            # Task types where observed
  scenarios: [string]             # Scenario types where observed
  time_of_day: string             # If time-dependent
  workload: string                # If workload-dependent (high/normal/low)

# Confidence & Evidence
confidence: float                 # 0.0 - 1.0
evidence:
  observation_count: integer      # Times this preference observed
  consistency: float              # How consistent (0.0 - 1.0)
  first_observed: datetime
  last_observed: datetime
  sample_episodes: [uuid]         # Sample case_ids showing preference

# Lifecycle
status: enum                      # observed | active | stable | overridden | archived
created_at: datetime
updated_at: datetime

# Override (if user explicitly overrode)
explicit_override:
  overridden: boolean
  override_value: any
  override_date: datetime

# Hub Context
hub_metadata:
  tenant_id: uuid
  subscription_id: uuid
  workbench_id: uuid              # If workbench-specific preference
```

---

## Examples

### Communication Style Preference

```yaml
preference_id: "pref-user-001-comm"

subject:
  type: "user"
  user_id: "user-sarah-analyst-001"
  user_role: "fraud_analyst"

preference:
  category: communication
  dimension: "explanation_verbosity"
  preference_type: scale
  scale_value:
    value: 0.8                    # Prefers verbose
    scale_name: "concise ← → verbose"

context:
  task_types: ["fraud_case_investigation"]
  scenarios: []
  time_of_day: null
  workload: null

confidence: 0.85
evidence:
  observation_count: 47
  consistency: 0.89
  first_observed: "2025-10-01T08:00:00Z"
  last_observed: "2026-01-06T16:00:00Z"
  sample_episodes: ["case-012", "case-045"]

status: stable
created_at: "2025-10-05T09:00:00Z"
updated_at: "2026-01-06T17:00:00Z"

explicit_override:
  overridden: false

hub_metadata:
  tenant_id: "tenant-acme-bank"
  subscription_id: "sub-fraud-premium"
  workbench_id: "wb-fraud-ops-001"
```

### Risk Tolerance Preference

```yaml
preference_id: "pref-user-001-risk"

subject:
  type: "user"
  user_id: "user-sarah-analyst-001"
  user_role: "fraud_analyst"

preference:
  category: risk
  dimension: "decision_autonomy"
  preference_type: choice
  choice_value:
    preferred: "review_recommendations"
    over: ["auto_approve", "auto_escalate"]

context:
  task_types: ["fraud_case_investigation"]
  scenarios: ["high_value_dispute"]
  time_of_day: null
  workload: "high"                # When busy, prefers review

confidence: 0.78
evidence:
  observation_count: 23
  consistency: 0.82
  first_observed: "2025-11-01T08:00:00Z"
  last_observed: "2026-01-05T14:00:00Z"
  sample_episodes: ["case-089", "case-102"]

status: active
created_at: "2025-11-05T09:00:00Z"
updated_at: "2026-01-05T15:00:00Z"

explicit_override:
  overridden: false

hub_metadata:
  tenant_id: "tenant-acme-bank"
  subscription_id: "sub-fraud-premium"
  workbench_id: "wb-fraud-ops-001"
```

---

## Preference Categories

### Communication
| Dimension | Description | Scale/Choices |
|-----------|-------------|---------------|
| `explanation_verbosity` | Detail level | concise ↔ verbose |
| `tone_formality` | Communication tone | casual ↔ formal |
| `update_frequency` | How often to notify | batch ↔ real-time |
| `channel_preference` | Preferred channel | email, slack, in-app |

### Presentation
| Dimension | Description | Scale/Choices |
|-----------|-------------|---------------|
| `data_format` | How to show data | table, chart, prose |
| `summary_first` | Summary before details | yes/no |
| `include_confidence` | Show confidence scores | yes/no |
| `highlight_anomalies` | Emphasize unusual items | yes/no |

### Risk
| Dimension | Description | Scale/Choices |
|-----------|-------------|---------------|
| `decision_autonomy` | How much to delegate | auto, review, manual |
| `escalation_threshold` | When to escalate | early ↔ late |
| `confirmation_preference` | Confirm before action | always, high-impact, never |

### Timing
| Dimension | Description | Scale/Choices |
|-----------|-------------|---------------|
| `response_priority` | Speed vs. thoroughness | quick ↔ thorough |
| `batch_processing` | Group similar tasks | yes/no |
| `focus_time_respect` | Avoid interruptions | yes/no |

---

## Traversal

### From User Preference
```
preference_id
  └── subject.user_id ─────► User directory
  └── evidence.sample_episodes[] ─► CaseRecord (episodic)
```

### To User Preference
```
(Query by user_id, category, dimension)
```

---

## Privacy & Control

Users should be able to:

1. **View** their learned preferences
2. **Correct** incorrect preferences
3. **Override** with explicit settings (which take precedence)
4. **Delete** preferences they don't want tracked

---

## Related Records

- [Agent Behaviors](./agent-behaviors.md) — Similar for agents
- [Interaction Patterns](./interaction-patterns.md) — Cross-entity patterns
- [Contextual Preferences](./contextual-preferences.md) — Context-dependent variations

