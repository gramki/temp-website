# Learned Skill

> **Status**: 🟡 Draft  
> **Record Type**: `learned_skill`  
> **Memory Class**: Procedural  
> **Related**: [Procedural Memory README](./README.md) | [Procedures](./procedures.md)

---

## Overview

A **Learned Skill** represents a **capability that an agent (or role) has developed** through successful task execution. It's a higher-level abstraction that groups related procedures, action sequences, and tool usage patterns.

> *"Skills are what agents learn to do well — the synthesized capability from repeated successful experience."*

### Key Characteristics

| Aspect | Description |
|--------|-------------|
| **Learned** | Derived from episodic observation, not authored |
| **Measurable** | Success rate tracked from outcomes |
| **Scoped** | Agent-specific, role-scoped, or broader |
| **Evolvable** | Improves with more evidence |
| **Advisory** | Guides behavior, doesn't mandate it |

---

## Schema

```yaml
# Learned Skill Record
skill_id: uuid                    # Primary key

# Skill Identity
name: string                      # Human-readable name
description: string               # What this skill enables
category: string                  # Skill category (investigation, communication, analysis, etc.)

# Scope
scope:
  level: enum                     # agent | role | workbench | enterprise
  agent_id: uuid                  # If agent-specific
  role: string                    # If role-scoped
  workbench_id: uuid              # If workbench-scoped or broader

# Capability Definition
capability:
  task_types: [string]            # Task types this skill applies to
  preconditions: [string]         # When this skill is applicable
  expected_outcomes: [string]     # What successful application looks like

# Performance Metrics
metrics:
  success_rate: float             # 0.0 - 1.0
  application_count: integer      # Times skill has been applied
  last_success: datetime          # Most recent successful application
  avg_duration: duration          # Average time to apply skill

# Confidence & Evidence
confidence: float                 # 0.0 - 1.0
evidence:
  episode_count: integer          # Number of supporting episodes
  episode_refs: [uuid]            # Sample episode IDs (case_ids)
  first_observed: datetime        # When pattern first detected
  last_observed: datetime         # Most recent supporting episode

# Lifecycle
status: enum                      # candidate | active | validated | deprecated | archived
created_at: datetime
updated_at: datetime
validated_at: datetime            # When moved to validated status
deprecated_at: datetime           # If deprecated

# Relationships
implements: [uuid]                # Procedure IDs that implement this skill
patterns: [uuid]                  # ActionSequence IDs demonstrating skill
tool_patterns: [uuid]             # ToolUsagePattern IDs for this skill

# Promotion
promotion_target:                 # If being considered for Knowledge promotion
  status: enum                    # none | candidate | submitted | approved | rejected
  target_sop_id: uuid             # Target SOP if promoted
  governance_ticket: string       # Governance tracking

# Hub Context
hub_metadata:
  tenant_id: uuid
  subscription_id: uuid
  workbench_id: uuid              # Primary domain anchor
```

---

## Example

```yaml
skill_id: "a1b2c3d4-5678-90ab-cdef-111213141516"

name: "First-Party Fraud Pattern Recognition"
description: "Ability to identify indicators of first-party fraud in transaction disputes"
category: "investigation"

scope:
  level: role
  role: "senior_fraud_investigator"
  workbench_id: "wb-fraud-ops-001"

capability:
  task_types:
    - "fraud_case_investigation"
    - "dispute_analysis"
  preconditions:
    - "Case involves customer-initiated dispute"
    - "Transaction history available"
  expected_outcomes:
    - "Fraud pattern identified or ruled out"
    - "Evidence compiled for decision"

metrics:
  success_rate: 0.89
  application_count: 247
  last_success: "2026-01-06T14:30:00Z"
  avg_duration: "PT15M"  # 15 minutes average

confidence: 0.87
evidence:
  episode_count: 247
  episode_refs:
    - "case-001"
    - "case-045"
    - "case-089"
  first_observed: "2025-09-15T10:00:00Z"
  last_observed: "2026-01-06T14:30:00Z"

status: validated
created_at: "2025-09-20T08:00:00Z"
updated_at: "2026-01-06T15:00:00Z"
validated_at: "2025-11-01T09:00:00Z"

implements:
  - "proc-fraud-pattern-check-001"
  - "proc-fraud-evidence-compile-002"
patterns:
  - "seq-fraud-investigation-001"
tool_patterns:
  - "tp-transaction-analysis-001"

promotion_target:
  status: candidate
  target_sop_id: null
  governance_ticket: "GOV-2026-0042"

hub_metadata:
  tenant_id: "tenant-acme-bank"
  subscription_id: "sub-fraud-premium"
  workbench_id: "wb-fraud-ops-001"
```

---

## Traversal

### From Skill
```
skill_id
  └── implements[] ────► Procedure records
  └── patterns[] ──────► ActionSequence records
  └── tool_patterns[] ─► ToolUsagePattern records
  └── evidence.episode_refs[] ─► CaseRecord (episodic)
```

### To Skill
```
Procedure.skill_id ────────────► LearnedSkill
ActionSequence.skill_id ───────► LearnedSkill
ToolUsagePattern.skill_id ─────► LearnedSkill
```

---

## Lifecycle States

| State | Description |
|-------|-------------|
| `candidate` | Newly detected pattern, under observation |
| `active` | In use, being tracked for success/failure |
| `validated` | Proven effective across many applications |
| `deprecated` | No longer recommended (superseded or ineffective) |
| `archived` | Retained for history, not active |

---

## Related Records

- [Procedures](./procedures.md) — Step-by-step implementations of skills
- [Action Sequences](./action-sequences.md) — Specific patterns demonstrating the skill
- [Tool Usage Patterns](./tool-usage-patterns.md) — Tool combinations for the skill
- [Enterprise Learning Services](../enterprise-learning-services.md) — Creates and promotes skills

