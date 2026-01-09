# Semantic Memory Record Relationships

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-07  
> **Related**: [Semantic Memory Store](./README.md) | [CAF README](../README.md)

---

## Overview

Semantic Memory records form a **knowledge graph** of learned beliefs. Unlike Episodic Memory (which is case-anchored), Semantic Memory is **entity-anchored** and **domain-scoped**.

---

## Relationship Structure

```
                    ┌─────────────────────────────────────────┐
                    │           DOMAIN (Workbench)             │
                    │                                          │
                    │  hub_metadata.workbench_id               │
                    └────────────────────┬────────────────────┘
                                         │
          ┌──────────────────────────────┼──────────────────────────────┐
          │                              │                              │
          ▼                              ▼                              ▼
┌──────────────────┐          ┌──────────────────┐          ┌──────────────────┐
│  EntityBelief    │◀────────▶│ RelationshipBelief│         │  PatternSummary  │
│                  │          │                  │          │                  │
│  subject:        │          │  from_entity     │          │  conditions      │
│   entity_type    │          │  to_entity       │          │  outcomes        │
│   entity_id      │          │  relationship    │          │                  │
└────────┬─────────┘          └──────────────────┘          └────────┬─────────┘
         │                                                           │
         │ evidence_links                              evidence_links│
         │                                                           │
         ▼                                                           ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         EPISODIC MEMORY                                      │
│                                                                              │
│  CaseRecord → DecisionRecord → EvidenceBundle → ContextSnapshot             │
│            → OutcomeRecord → OverrideRecord → HandoffContext                │
│            → IncidentTimeline                                               │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘

┌──────────────────┐          ┌──────────────────┐
│  HypothesisRec   │─────────▶│LearnedConstraint │
│                  │          │                  │
│  (may promote to)│          │  (may promote to)│
│                  │          │                  │
└────────┬─────────┘          └────────┬─────────┘
         │                             │
         │         PROMOTION           │
         ▼                             ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      ENTERPRISE KNOWLEDGE                                    │
│                                                                              │
│  Policies | Rules | Facts | Definitions | Reference Data                    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Relationship Types

### 1. Domain Binding (All Records)

All Semantic Memory records are bound to a **domain** (workbench):

```yaml
hub_metadata:
  tenant_id: uuid
  subscription_id: uuid
  workbench_id: uuid        # Domain anchor
```

Unlike Episodic Memory, there is **no case_id** — beliefs span many cases.

---

### 2. Entity Anchoring

Entity Beliefs and Relationship Beliefs reference **external entities**:

```yaml
# EntityBelief
subject:
  entity_type: customer
  entity_id: uuid           # References external MDM
  entity_source: core-banking

# RelationshipBelief
from_entity:
  entity_type: customer
  entity_id: uuid
to_entity:
  entity_type: customer
  entity_id: uuid
```

Entities are **not owned by CAF** — they're references to systems of record.

---

### 3. Evidence Links (Episodic → Semantic)

All Semantic Memory records link back to supporting episodes:

```yaml
evidence_links:
  - case_id: uuid
    record_type: decision_record | outcome_record | incident_timeline
    record_id: uuid
    relevance: float
    contribution: supports | contradicts
```

This establishes **provenance** — every belief traces to experience.

---

### 4. Derivation Chains

Some beliefs derive from other beliefs:

```yaml
# EntityBelief
source: derived
derived_from:
  - belief_id: uuid
    belief_type: pattern_summary
  - belief_id: uuid
    belief_type: evaluation_finding
```

---

### 5. Promotion Links (Semantic → Knowledge)

When hypotheses are promoted to knowledge:

```yaml
# HypothesisRecord
promotion:
  promoted_at: datetime
  promoted_by: actor
  promotion_target: uuid        # ID in Knowledge system
  promotion_type: fact | rule | constraint | policy
```

---

## Traversal Patterns

| Pattern | Starting Point | Query |
|---------|---------------|-------|
| **Entity portrait** | Entity ID | All beliefs WHERE `subject.entity_id = X` |
| **Entity network** | Entity ID | All relationships WHERE `from_entity = X` OR `to_entity = X` |
| **Domain beliefs** | Workbench ID | All records WHERE `hub_metadata.workbench_id = X` |
| **Evidence backtrack** | Belief ID | Follow `evidence_links` to Episodic records |
| **Derivation chain** | Belief ID | Follow `derived_from` recursively |
| **Promotion history** | Knowledge ID | Hypotheses WHERE `promotion.promotion_target = X` |

---

## Cross-Memory Relationships

### Episodic → Semantic

| Episodic Record | Semantic Record | Relationship |
|-----------------|-----------------|--------------|
| Multiple OutcomeRecords | PatternSummary | "Pattern observed across cases" |
| Multiple DecisionRecords | LearnedConstraint | "Constraint learned from decisions" |
| OverrideRecords | HypothesisRecord | "Override pattern becoming hypothesis" |
| EvaluationRun | EvaluationFinding | "Evaluation produced finding" |

### Semantic → Knowledge (Promotion)

| Semantic Record | Knowledge Target | Governance Gate |
|-----------------|------------------|-----------------|
| HypothesisRecord | Policy Rule | Governance review + approval |
| LearnedConstraint | Business Rule | Risk assessment + approval |
| PatternSummary | Reference Data | Data steward approval |
| EntityBelief | Entity Attribute (MDM) | MDM governance |

---

## Consistency Rules

| Rule | Description |
|------|-------------|
| **Evidence Required** | Every belief must have at least one evidence link |
| **Entity Exists** | Entity references should resolve to valid external IDs |
| **Confidence Bounded** | Confidence must be 0-1 |
| **Decay Applied** | Stale beliefs should have reduced confidence |
| **Promotion Immutable** | Promoted records cannot be modified (only deprecated) |

---

## Index Requirements

| Index | Purpose |
|-------|---------|
| `hub_metadata.workbench_id` | Domain queries |
| `subject.entity_id` (EntityBelief) | Entity portrait |
| `from_entity.entity_id`, `to_entity.entity_id` | Relationship network |
| `status` | Active belief queries |
| `confidence` | High-confidence filter |
| `freshness.last_corroborated` | Staleness detection |
| `evidence_links[].case_id` | Episodic backtrack |

---

## Related Documents

- [Semantic Memory Store](./README.md) — Overview
- [Episodic Memory Relationships](../episodic-memory-store/record-relationships.md) — Case-anchored records
- [CAF README](../README.md) — Control plane overview

