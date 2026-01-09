# Agent Behavior

> **Status**: 🟡 Draft  
> **Record Type**: `agent_behavior`  
> **Memory Class**: Preference  
> **Related**: [Preference Memory README](./README.md) | [User Preferences](./user-preferences.md)

---

## Overview

An **Agent Behavior** captures **observed behavioral patterns of an employed agent** — tendencies in how it makes decisions, interacts with users, and handles tasks. These are emergent patterns, not designed behaviors.

> *"Agent Behaviors are what we notice agents tend to do — their 'personality' emerging from experience."*

### Key Characteristics

| Aspect | Description |
|--------|-------------|
| **Emergent** | Develops through operation, not training |
| **Observable** | Detected from patterns in decisions/actions |
| **Agent-specific** | May vary across agents with same training |
| **Trackable** | Monitor for drift or undesirable patterns |
| **Adjustable** | Can inform retraining or guardrails |

---

## Schema

```yaml
# Agent Behavior Record
behavior_id: uuid                 # Primary key

# Subject
subject:
  type: "agent"
  agent_id: uuid                  # Employed agent ID
  agent_type: string              # Agent type/role
  training_spec_id: uuid          # Training baseline

# Behavior Definition
behavior:
  category: enum                  # decision_style | interaction_style | strategy | tendency
  dimension: string               # Specific dimension
  
  behavior_type: enum             # tendency | preference | pattern | habit
  
  # The observed behavior
  description: string             # Human-readable description
  
  # Quantified behavior (if applicable)
  quantified:
    metric: string                # What's measured
    observed_value: float         # Observed value
    baseline_value: float         # Expected/baseline value
    deviation: float              # How much it deviates

# Context
context:
  task_types: [string]
  case_types: [string]
  conditions: [string]            # When this behavior manifests

# Assessment
assessment:
  alignment: enum                 # aligned | neutral | concerning | misaligned
  impact: enum                    # positive | neutral | negative
  notes: string                   # Assessment notes

# Confidence & Evidence
confidence: float
evidence:
  observation_count: integer
  consistency: float
  first_observed: datetime
  last_observed: datetime
  sample_episodes: [uuid]
  
  # Comparative evidence
  compared_to:
    baseline: string              # What it's compared to
    deviation_significance: float # Statistical significance

# Lifecycle
status: enum                      # observed | monitoring | stable | flagged | addressed
created_at: datetime
updated_at: datetime

# Actions taken (if any)
interventions:
  - intervention_type: enum       # guardrail | retrain | config | none
    date: datetime
    details: string
    outcome: string

# Hub Context
hub_metadata:
  tenant_id: uuid
  subscription_id: uuid
  workbench_id: uuid
```

---

## Examples

### Conservative Decision Tendency

```yaml
behavior_id: "behav-agent-001-conservative"

subject:
  type: "agent"
  agent_id: "agent-fraud-investigator-001"
  agent_type: "fraud_investigator"
  training_spec_id: "ts-fraud-inv-v2"

behavior:
  category: decision_style
  dimension: "risk_appetite"
  behavior_type: tendency
  description: "Agent tends to escalate more frequently than peers"
  quantified:
    metric: "escalation_rate"
    observed_value: 0.45          # 45% escalation
    baseline_value: 0.30          # 30% expected
    deviation: 0.15               # 15% higher

context:
  task_types: ["fraud_case_investigation"]
  case_types: ["high_value_dispute"]
  conditions: ["ambiguous_evidence"]

assessment:
  alignment: aligned              # Conservative is okay for fraud
  impact: neutral                 # Not problematic
  notes: "Higher escalation may be appropriate given case complexity"

confidence: 0.82
evidence:
  observation_count: 156
  consistency: 0.78
  first_observed: "2025-11-01T08:00:00Z"
  last_observed: "2026-01-06T14:00:00Z"
  sample_episodes: ["case-045", "case-089"]
  compared_to:
    baseline: "peer_agents_same_training"
    deviation_significance: 0.92

status: monitoring
created_at: "2025-11-15T09:00:00Z"
updated_at: "2026-01-06T15:00:00Z"

interventions: []

hub_metadata:
  tenant_id: "tenant-acme-bank"
  subscription_id: "sub-fraud-premium"
  workbench_id: "wb-fraud-ops-001"
```

### Communication Style Drift

```yaml
behavior_id: "behav-agent-002-verbose"

subject:
  type: "agent"
  agent_id: "agent-fraud-investigator-002"
  agent_type: "fraud_investigator"
  training_spec_id: "ts-fraud-inv-v2"

behavior:
  category: interaction_style
  dimension: "response_length"
  behavior_type: pattern
  description: "Agent responses have become increasingly verbose over time"
  quantified:
    metric: "avg_response_tokens"
    observed_value: 850
    baseline_value: 400
    deviation: 450

context:
  task_types: ["fraud_case_investigation"]
  case_types: ["all"]
  conditions: ["post_deployment_30_days"]

assessment:
  alignment: concerning
  impact: negative
  notes: "Verbose responses slow down user workflow"

confidence: 0.91
evidence:
  observation_count: 234
  consistency: 0.85
  first_observed: "2025-12-01T08:00:00Z"
  last_observed: "2026-01-06T16:00:00Z"
  sample_episodes: ["case-112", "case-145", "case-178"]
  compared_to:
    baseline: "initial_deployment_week"
    deviation_significance: 0.97

status: flagged
created_at: "2025-12-15T09:00:00Z"
updated_at: "2026-01-06T17:00:00Z"

interventions:
  - intervention_type: config
    date: "2026-01-07T10:00:00Z"
    details: "Added max_tokens constraint to system prompt"
    outcome: "pending_evaluation"

hub_metadata:
  tenant_id: "tenant-acme-bank"
  subscription_id: "sub-fraud-premium"
  workbench_id: "wb-fraud-ops-001"
```

---

## Behavior Categories

### Decision Style
| Dimension | Description |
|-----------|-------------|
| `risk_appetite` | Conservative vs. aggressive decisions |
| `certainty_threshold` | How certain before deciding |
| `escalation_tendency` | How often escalates to human |
| `evidence_thoroughness` | How much evidence gathered |

### Interaction Style
| Dimension | Description |
|-----------|-------------|
| `response_length` | Concise vs. verbose |
| `proactivity` | Proactive suggestions vs. reactive |
| `confidence_expression` | How uncertainty is communicated |
| `formality` | Formal vs. casual tone |

### Strategy
| Dimension | Description |
|-----------|-------------|
| `tool_preference` | Which tools used most |
| `approach_pattern` | Breadth-first vs. depth-first |
| `prioritization` | How tasks are ordered |

### Tendency
| Dimension | Description |
|-----------|-------------|
| `drift_direction` | Is behavior changing over time? |
| `context_sensitivity` | Does behavior vary by context? |
| `consistency` | How stable is behavior? |

---

## Assessment Framework

| Alignment | Description | Action |
|-----------|-------------|--------|
| `aligned` | Behavior matches expectations | Monitor |
| `neutral` | Neither good nor bad | Track |
| `concerning` | May need attention | Investigate |
| `misaligned` | Conflicts with requirements | Intervene |

---

## Drift Detection

Agent Behavior records are key for **behavioral drift detection**:

```
Training Baseline ──► Initial Behavior ──► Current Behavior
                           │                      │
                           └──────── DRIFT ───────┘
```

Drift signals:
- Increasing deviation from baseline
- Decreasing consistency
- Pattern changes over time

---

## Traversal

### From Agent Behavior
```
behavior_id
  └── subject.agent_id ──────► Agent Registry (Seer)
  └── subject.training_spec_id ► Training Spec (Seer)
  └── evidence.sample_episodes[] ► CaseRecord (episodic)
```

### To Agent Behavior
```
(Query by agent_id, category, dimension)
(Query by status = flagged for intervention)
```

---

## Related Records

- [User Preferences](./user-preferences.md) — Similar for users
- [Learned Skills](../procedural-memory-store/learned-skills.md) — What agent can do (vs. how it behaves)
- [Evaluation Findings](../semantic-memory-store/evaluation-findings.md) — Formal evaluation results

