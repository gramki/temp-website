# Interaction Pattern

> **Status**: 🟡 Draft  
> **Record Type**: `interaction_pattern`  
> **Memory Class**: Preference  
> **Related**: [Preference Memory README](./README.md) | [User Preferences](./user-preferences.md)

---

## Overview

An **Interaction Pattern** captures **how two or more entities prefer to interact** — the observed dynamics of user-agent, agent-agent, or user-user interactions. These patterns help optimize collaboration.

> *"Interaction Patterns are the relationship dynamics we've learned — how these parties work best together."*

### Key Characteristics

| Aspect | Description |
|--------|-------------|
| **Relational** | Involves two or more parties |
| **Bilateral** | Preferences of both parties matter |
| **Contextual** | May vary by task or situation |
| **Emergent** | Develops through repeated interaction |
| **Optimizable** | Used to improve collaboration |

---

## Schema

```yaml
# Interaction Pattern Record
pattern_id: uuid                  # Primary key

# Parties
parties:
  - party_type: enum              # user | agent | team
    party_id: uuid
    role_in_interaction: string   # e.g., "requester", "responder", "reviewer"

# Pattern Definition
pattern:
  interaction_type: enum          # request_response | collaboration | handoff | review
  dimension: string               # Specific dimension
  
  description: string             # Human-readable pattern description
  
  # Observed dynamics
  dynamics:
    initiator: uuid               # Who typically initiates
    frequency: string             # How often interaction occurs
    typical_duration: duration    # How long interactions last
    success_rate: float           # How often interactions succeed

# Optimal Conditions
optimal_conditions:
  timing: string                  # When interaction works best
  context: [string]               # Contextual factors
  prerequisites: [string]         # What should be in place

# Anti-patterns (what doesn't work)
anti_patterns:
  - pattern: string
    reason: string
    observed_failure_rate: float

# Confidence & Evidence
confidence: float
evidence:
  observation_count: integer
  consistency: float
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

### User-Agent Preferred Handoff Pattern

```yaml
pattern_id: "ip-user-agent-handoff-001"

parties:
  - party_type: user
    party_id: "user-sarah-analyst-001"
    role_in_interaction: "reviewer"
  - party_type: agent
    party_id: "agent-fraud-investigator-001"
    role_in_interaction: "preparer"

pattern:
  interaction_type: handoff
  dimension: "review_handoff"
  description: "Agent prepares case summary, user reviews and decides"
  dynamics:
    initiator: "agent-fraud-investigator-001"
    frequency: "per_case"
    typical_duration: "PT5M"
    success_rate: 0.92

optimal_conditions:
  timing: "After initial investigation complete"
  context:
    - "High-value case"
    - "Ambiguous evidence"
  prerequisites:
    - "Evidence bundle prepared"
    - "Recommendation drafted"

anti_patterns:
  - pattern: "Agent decides without handoff"
    reason: "User prefers to review high-value decisions"
    observed_failure_rate: 0.65
  - pattern: "Multiple back-and-forth before decision"
    reason: "Frustrates user, prefer single comprehensive handoff"
    observed_failure_rate: 0.40

confidence: 0.87
evidence:
  observation_count: 45
  consistency: 0.91
  first_observed: "2025-10-15T08:00:00Z"
  last_observed: "2026-01-06T15:00:00Z"
  sample_episodes: ["case-023", "case-067"]

status: stable
created_at: "2025-10-20T09:00:00Z"
updated_at: "2026-01-06T16:00:00Z"

hub_metadata:
  tenant_id: "tenant-acme-bank"
  subscription_id: "sub-fraud-premium"
  workbench_id: "wb-fraud-ops-001"
```

### Agent-Agent Collaboration Pattern

```yaml
pattern_id: "ip-agent-agent-collab-001"

parties:
  - party_type: agent
    party_id: "agent-fraud-investigator-001"
    role_in_interaction: "primary_investigator"
  - party_type: agent
    party_id: "agent-transaction-analyzer-001"
    role_in_interaction: "specialist"

pattern:
  interaction_type: collaboration
  dimension: "specialist_consultation"
  description: "Primary investigator consults transaction specialist for complex patterns"
  dynamics:
    initiator: "agent-fraud-investigator-001"
    frequency: "0.3_per_case"  # 30% of cases
    typical_duration: "PT30S"
    success_rate: 0.95

optimal_conditions:
  timing: "Early in investigation"
  context:
    - "Complex transaction patterns"
    - "Multi-merchant fraud suspected"
  prerequisites:
    - "Basic transaction history retrieved"

anti_patterns:
  - pattern: "Consult after decision made"
    reason: "Wastes specialist capacity, doesn't improve outcome"
    observed_failure_rate: 0.50

confidence: 0.79
evidence:
  observation_count: 67
  consistency: 0.83
  first_observed: "2025-11-01T08:00:00Z"
  last_observed: "2026-01-05T11:00:00Z"
  sample_episodes: ["case-056", "case-089", "case-112"]

status: active
created_at: "2025-11-10T09:00:00Z"
updated_at: "2026-01-05T12:00:00Z"

hub_metadata:
  tenant_id: "tenant-acme-bank"
  subscription_id: "sub-fraud-premium"
  workbench_id: "wb-fraud-ops-001"
```

---

## Interaction Types

| Type | Description | Example |
|------|-------------|---------|
| `request_response` | One party asks, other responds | User asks agent for analysis |
| `collaboration` | Joint work on a task | Two agents working on case |
| `handoff` | Transfer of responsibility | Agent hands off to user for decision |
| `review` | One party reviews other's work | User reviews agent recommendation |
| `escalation` | Transfer to higher authority | Agent escalates to supervisor |

---

## Multi-Party Patterns

Some patterns involve more than two parties:

```yaml
parties:
  - party_type: agent
    party_id: "agent-001"
    role_in_interaction: "coordinator"
  - party_type: agent
    party_id: "agent-002"
    role_in_interaction: "specialist_a"
  - party_type: agent
    party_id: "agent-003"
    role_in_interaction: "specialist_b"
  - party_type: user
    party_id: "user-001"
    role_in_interaction: "approver"
```

---

## Traversal

### From Interaction Pattern
```
pattern_id
  └── parties[].party_id ──► User directory / Agent registry
  └── evidence.sample_episodes[] ──► CaseRecord (episodic)
```

### To Interaction Pattern
```
(Query by party_id to find all patterns involving entity)
(Query by interaction_type for pattern types)
```

---

## Use Cases

| Use Case | Description |
|----------|-------------|
| **Workflow optimization** | Design workflows matching observed patterns |
| **Team formation** | Match users and agents with compatible styles |
| **Training** | Train new agents on effective interaction patterns |
| **Conflict detection** | Identify when interaction patterns clash |

---

## Related Records

- [User Preferences](./user-preferences.md) — Individual user preferences
- [Agent Behaviors](./agent-behaviors.md) — Individual agent behaviors
- [Contextual Preferences](./contextual-preferences.md) — Context-dependent variations

