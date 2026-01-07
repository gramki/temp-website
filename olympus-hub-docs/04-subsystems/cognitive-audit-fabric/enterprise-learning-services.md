# Enterprise Learning Services

> **Status**: 🔴 Stub — Placeholder for expansion  
> **Last Updated**: 2026-01-07  
> **Related**: [CAF README](./README.md) | [Semantic Memory Store](./semantic-memory-store/README.md) | [ETSL](../../../pontus/etsl/)

---

## Overview

**Enterprise Learning Services** is a CAF component responsible for **promoting learned memory to authoritative knowledge** — specifically to ETSL (Enterprise Temporal Semantic Layer) when authorized.

### Core Mission

> *"Turn experience into institutional knowledge — deliberately, with governance."*

Enterprise Learning Services bridges the gap between:
- **Semantic Memory** (learned, probabilistic, informative)
- **Enterprise Knowledge** (asserted, governed, normative)

---

## Key Responsibilities

| Responsibility | Description |
|----------------|-------------|
| **Promotion Orchestration** | Coordinate memory → knowledge promotion workflows |
| **ETSL Integration** | Translate promoted beliefs into ETSL assertions |
| **Governance Checkpoints** | Enforce approval gates before promotion |
| **Evidence Packaging** | Compile evidence packages for governance review |
| **Conflict Detection** | Identify when learned patterns conflict with existing knowledge |
| **Rollback Support** | Enable reversal of promotions when beliefs are disproven |

---

## Promotion Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    SEMANTIC MEMORY                                       │
│                                                                          │
│  HypothesisRecord │ PatternSummary │ LearnedConstraint │ EntityBelief   │
│                                                                          │
└─────────────────────────────────────┬───────────────────────────────────┘
                                      │
                                      │ Candidate identified
                                      │ (confidence threshold, evidence count)
                                      ▼
┌─────────────────────────────────────────────────────────────────────────┐
│              ENTERPRISE LEARNING SERVICES                                │
│                                                                          │
│  1. Candidate Detection                                                  │
│     - Monitor beliefs crossing promotion thresholds                      │
│     - Detect patterns with stable, replicated evidence                   │
│                                                                          │
│  2. Evidence Compilation                                                 │
│     - Gather supporting episodes                                         │
│     - Compile counterexamples                                            │
│     - Generate evidence package                                          │
│                                                                          │
│  3. Governance Submission                                                │
│     - Submit to appropriate governance channel                           │
│     - Track approval status                                              │
│                                                                          │
│  4. ETSL Translation                                                     │
│     - Convert approved belief to ETSL assertion                          │
│     - Handle temporal semantics                                          │
│     - Establish authority and scope                                      │
│                                                                          │
│  5. Post-Promotion                                                       │
│     - Update Semantic Memory record status → promoted                    │
│     - Link to ETSL assertion                                             │
│     - Monitor for contradicting evidence                                 │
│                                                                          │
└─────────────────────────────────────┬───────────────────────────────────┘
                                      │
                                      │ Approved + Translated
                                      ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                           ETSL                                           │
│                 (Enterprise Temporal Semantic Layer)                     │
│                                                                          │
│  Asserted Facts │ Rules │ Constraints │ Definitions                     │
│                                                                          │
│  - Authority-qualified                                                   │
│  - Time-aware (temporal validity)                                        │
│  - Versioned                                                             │
│  - Normative (constrains behavior)                                       │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Promotion Types

| Source (Memory) | Target (Knowledge) | Governance Gate |
|-----------------|-------------------|-----------------|
| HypothesisRecord | ETSL Fact / Rule | Domain governance review |
| PatternSummary | ETSL Derived Fact | Data steward approval |
| LearnedConstraint | ETSL Business Rule | Policy committee |
| EntityBelief | ETSL Entity Attribute | MDM governance |
| RelationshipBelief | ETSL Relationship | Entity governance |

---

## Promotion Criteria (Configurable)

| Criterion | Description | Default |
|-----------|-------------|---------|
| **Confidence Threshold** | Minimum confidence for promotion consideration | 0.85 |
| **Evidence Count** | Minimum supporting episodes | 20 |
| **Stability Period** | How long belief must be stable | 30 days |
| **Contradiction Ratio** | Max contradicting/supporting ratio | 0.10 |
| **Scope Clarity** | Explicit scope required | Yes |
| **Owner Assigned** | Review owner must be assigned | Yes |

---

## ETSL Integration

### Assertion Translation

```yaml
# Semantic Memory (Learned)
hypothesis:
  hypothesis_id: hyp-123
  description: "Customers with pattern X have 3x dispute rate"
  confidence: 0.87
  scope: { segment: "retail", product: "checking" }
  
# ETSL Assertion (Promoted)
etsl_assertion:
  assertion_id: ast-456
  statement: "Customers with pattern X have elevated dispute risk"
  authority: "fraud-ops-governance"
  effective_from: "2026-01-15"
  scope: { segment: "retail", product: "checking" }
  provenance:
    source_type: learned_hypothesis
    source_id: hyp-123
    promotion_date: "2026-01-15"
    approved_by: "policy-committee"
```

### Temporal Semantics

ETSL assertions are **time-aware**:
- `effective_from` — When assertion becomes active
- `effective_to` — When assertion expires (if applicable)
- `superseded_by` — If replaced by newer assertion

Enterprise Learning Services ensures proper temporal handling during promotion.

---

## Conflict Resolution

When learned patterns conflict with existing knowledge:

| Scenario | Resolution |
|----------|------------|
| **New belief contradicts existing ETSL fact** | Flag for governance review; do not auto-promote |
| **Multiple beliefs contradict each other** | Present both with evidence for governance decision |
| **Promoted belief later disproven** | Trigger deprecation workflow, notify stakeholders |
| **ETSL fact updated externally** | Deprecate related Semantic Memory beliefs |

---

## API Sketch (Placeholder)

```yaml
# Candidate Detection
GET /learning/candidates
  ?workbench_id=...
  &min_confidence=0.85
  &status=ready_for_review

# Evidence Package
GET /learning/candidates/{hypothesis_id}/evidence-package

# Submit for Governance
POST /learning/candidates/{hypothesis_id}/submit
  {
    governance_channel: "policy-committee",
    notes: "Strong evidence, recommend promotion"
  }

# Promote to ETSL
POST /learning/candidates/{hypothesis_id}/promote
  {
    target_type: "etsl_rule",
    effective_from: "2026-02-01",
    authority: "fraud-ops-governance"
  }

# Rollback Promotion
POST /learning/promotions/{promotion_id}/rollback
  {
    reason: "Contradicting evidence discovered",
    evidence: [...]
  }
```

---

## TODO

| Item | Description | Priority |
|------|-------------|----------|
| Define promotion criteria configuration schema | How tenants/workbenches customize thresholds | P1 |
| Define ETSL assertion translation format | Mapping from Memory to ETSL types | P1 |
| Design governance workflow integration | How promotion requests flow to approval | P1 |
| Define conflict detection algorithms | How to detect knowledge conflicts | P2 |
| Design rollback mechanics | How to safely deprecate promoted assertions | P2 |
| Define monitoring/alerting for promotion anomalies | Track promotion health | P2 |

---

## Related Documents

- [CAF README](./README.md) — Cognitive Audit Fabric overview
- [Semantic Memory Store](./semantic-memory-store/README.md) — Source of learned beliefs
- [Hypothesis Records](./semantic-memory-store/hypothesis-records.md) — Primary promotion candidates
- [ETSL Overview](../../../pontus/etsl/) — Enterprise Temporal Semantic Layer
- [Enterprise Knowledge](../../../olympus-seer-docs/agentic-ai-concepts/enterprise-knowledge/README.md) — Asserted truths

