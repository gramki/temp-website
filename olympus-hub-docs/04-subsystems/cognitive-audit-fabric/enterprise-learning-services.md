# Enterprise Learning Services

> **Status**: 🟡 Draft — Conceptual design complete; implementation deferred  
> **Last Updated**: 2026-01-07  
> **Related**: [CAF README](./README.md) | [Semantic Memory Store](./semantic-memory-store/README.md) | [ETSL](../../../pontus/etsl/)

---

## Overview

**Enterprise Learning Services** is a CAF component responsible for **promoting memory across the ESPP hierarchy** — from Episodic to Semantic/Procedural/Preference, and from Semantic to ETSL when authorized.

### Core Mission

> *"Turn experience into institutional memory and knowledge — deliberately, with governance."*

Enterprise Learning Services orchestrates the full learning lifecycle:
- **Episodic → Semantic**: Patterns from cases become hypotheses and beliefs
- **Episodic → Procedural**: Successful action sequences become learned procedures
- **Episodic → Preference**: Observed preferences become preference records
- **Semantic → ETSL**: Validated hypotheses become authoritative knowledge

---

## Key Responsibilities

| Responsibility | Description |
|----------------|-------------|
| **Cross-Memory Promotion** | Orchestrate Episodic → Semantic/Procedural/Preference workflows |
| **Knowledge Promotion** | Coordinate Semantic → ETSL workflows |
| **Pattern Detection** | Identify promotable patterns in episodic traces |
| **Evidence Packaging** | Compile evidence packages for governance review |
| **Governance Checkpoints** | Enforce approval gates before promotion |
| **Conflict Detection** | Identify when learned patterns conflict with existing memory/knowledge |
| **Rollback Support** | Enable reversal of promotions when beliefs are disproven |

---

## Promotion Hierarchy

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        EPISODIC MEMORY                                   │
│                    (Event-based, case-bound)                             │
│                                                                          │
│  CaseRecord → DecisionRecord → OutcomeRecord → OverrideRecord           │
│            → EvidenceBundle → ContextSnapshot → HandoffContext          │
│            → IncidentTimeline                                           │
│                                                                          │
└─────────────────────────────────────┬───────────────────────────────────┘
                                      │
          ┌───────────────────────────┼───────────────────────────┐
          │                           │                           │
          ▼                           ▼                           ▼
┌──────────────────┐      ┌──────────────────┐      ┌──────────────────┐
│ SEMANTIC MEMORY  │      │PROCEDURAL MEMORY │      │PREFERENCE MEMORY │
│                  │      │                  │      │                  │
│ Patterns from    │      │ Successful       │      │ Observed user/   │
│ cases become     │      │ action sequences │      │ agent preferences│
│ hypotheses       │      │ become skills    │      │ become settings  │
│                  │      │                  │      │                  │
│ • Hypothesis     │      │ • LearnedSkill   │      │ • Preference     │
│ • Pattern        │      │ • Procedure      │      │ • Behavior       │
│ • EntityBelief   │      │ • ActionSequence │      │ • Setting        │
│ • Relationship   │      │                  │      │                  │
│ • Constraint     │      │                  │      │                  │
│ • Finding        │      │                  │      │                  │
└────────┬─────────┘      └──────────────────┘      └──────────────────┘
         │
         │ Validated + Governed
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

## Promotion Flows

### Flow 1: Episodic → Semantic

**Pattern detection from case outcomes**

```
Episodic:
  Multiple OutcomeRecords showing same result
  + Multiple DecisionRecords with similar rationale
  + OverrideRecords with consistent justification
                    │
                    ▼
Enterprise Learning Services:
  1. Detect recurring pattern across cases
  2. Extract commonalities (conditions, outcomes)
  3. Calculate confidence from evidence
  4. Generate HypothesisRecord or PatternSummary
                    │
                    ▼
Semantic Memory:
  HypothesisRecord (pattern pending validation)
  PatternSummary (descriptive correlation)
  LearnedConstraint (advisory guideline)
```

### Flow 2: Episodic → Procedural

**Skill extraction from successful action sequences**

```
Episodic:
  DecisionRecords + ContextSnapshots showing:
  - Consistent action sequences
  - Successful outcomes
  - Across multiple similar cases
                    │
                    ▼
Enterprise Learning Services:
  1. Identify repeating action sequences
  2. Extract preconditions and postconditions
  3. Measure success rate
  4. Generate LearnedSkill or Procedure
                    │
                    ▼
Procedural Memory:
  LearnedSkill (reusable capability)
  Procedure (step-by-step guidance)
  ActionSequence (successful pattern)
```

### Flow 3: Episodic → Preference

**Preference extraction from behavioral patterns**

```
Episodic:
  DecisionRecords + ContextSnapshots showing:
  - User/agent choices when alternatives exist
  - Consistent selections over time
  - Context-dependent preferences
                    │
                    ▼
Enterprise Learning Services:
  1. Identify choice patterns
  2. Extract preference dimensions
  3. Determine context sensitivity
  4. Generate Preference or Behavior record
                    │
                    ▼
Preference Memory:
  Preference (learned preference)
  Behavior (observed behavior pattern)
  Setting (inferred setting)
```

### Flow 4: Semantic → ETSL

**Knowledge promotion through governance**

```
Semantic Memory:
  HypothesisRecord with:
  - High confidence (e.g., > 0.85)
  - Sufficient evidence (e.g., 20+ episodes)
  - Stable over time (e.g., 30+ days)
  - Clear scope
                    │
                    ▼
Enterprise Learning Services:
  1. Identify promotion candidates
  2. Compile evidence package
  3. Submit to governance channel
  4. Track approval workflow
                    │
                    ▼
Governance:
  - Review evidence
  - Assess risk
  - Approve/reject/defer
                    │
                    ▼ (if approved)
ETSL:
  Asserted Fact / Rule / Constraint
  - Authority-qualified
  - Temporally valid
  - Versioned
```

---

## Promotion Types

### Episodic → Semantic

| Source Pattern | Target Record | Trigger Condition |
|----------------|--------------|-------------------|
| Recurring outcomes across cases | HypothesisRecord | N+ cases with similar outcome |
| Repeated decision rationale | PatternSummary | Consistent reasoning pattern |
| Override justifications | LearnedConstraint | Repeated policy gap signals |
| Entity behavior signals | EntityBelief | Consistent entity attributes |
| Cross-entity interactions | RelationshipBelief | Repeated relationship signals |

### Episodic → Procedural

| Source Pattern | Target Record | Trigger Condition |
|----------------|--------------|-------------------|
| Successful action sequences | LearnedSkill | High success rate across cases |
| Step-by-step resolution paths | Procedure | Repeatable workflow detected |
| Tool invocation patterns | ActionSequence | Consistent tool use patterns |

### Episodic → Preference

| Source Pattern | Target Record | Trigger Condition |
|----------------|--------------|-------------------|
| User choice consistency | UserPreference | Stable selections over time |
| Agent decision patterns | AgentBehavior | Repeated agent choices |
| Configuration selections | InferredSetting | Consistent config patterns |

### Semantic → ETSL (Knowledge Promotion)

| Source (Semantic) | Target (ETSL) | Governance Gate |
|------------------|---------------|-----------------|
| HypothesisRecord | Fact / Rule | Domain governance review |
| PatternSummary | Derived Fact | Data steward approval |
| LearnedConstraint | Business Rule | Policy committee |
| EntityBelief | Entity Attribute | MDM governance |
| RelationshipBelief | Relationship | Entity governance |

---

## Promotion Criteria (Configurable)

### Episodic → Semantic / Procedural / Preference

| Criterion | Description | Default |
|-----------|-------------|---------|
| **Min Occurrences** | Minimum pattern repetitions | 5 |
| **Min Consistency** | Pattern consistency ratio | 0.80 |
| **Min Timespan** | Pattern must span this period | 14 days |
| **Min Success Rate** | For procedural promotions | 0.90 |
| **Scope Clarity** | Explicit scope required | Yes |

### Semantic → ETSL

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
# ============================================================
# EPISODIC → SEMANTIC / PROCEDURAL / PREFERENCE
# ============================================================

# Detect promotable patterns in episodic memory
GET /learning/episodic-patterns
  ?workbench_id=...
  &target_memory=semantic|procedural|preference
  &min_occurrences=5
  &status=candidate

# Get pattern details with supporting episodes
GET /learning/episodic-patterns/{pattern_id}

# Promote episodic pattern to target memory
POST /learning/episodic-patterns/{pattern_id}/promote
  {
    target_memory: "semantic",      # or procedural, preference
    target_record_type: "hypothesis",
    initial_confidence: 0.75,
    scope: { workbench_id: "..." }
  }

# ============================================================
# SEMANTIC → ETSL (Knowledge Promotion)
# ============================================================

# List promotion candidates (high-confidence semantic records)
GET /learning/knowledge-candidates
  ?workbench_id=...
  &min_confidence=0.85
  &status=ready_for_review

# Get evidence package for governance
GET /learning/knowledge-candidates/{record_id}/evidence-package

# Submit for governance review
POST /learning/knowledge-candidates/{record_id}/submit
  {
    governance_channel: "policy-committee",
    notes: "Strong evidence, recommend promotion"
  }

# Promote to ETSL (after governance approval)
POST /learning/knowledge-candidates/{record_id}/promote
  {
    target_type: "etsl_rule",
    effective_from: "2026-02-01",
    authority: "fraud-ops-governance"
  }

# ============================================================
# PROMOTION MANAGEMENT
# ============================================================

# List all promotions
GET /learning/promotions
  ?workbench_id=...
  &source_memory=episodic|semantic
  &target=semantic|procedural|preference|etsl
  &status=active|deprecated

# Rollback a promotion
POST /learning/promotions/{promotion_id}/rollback
  {
    reason: "Contradicting evidence discovered",
    evidence: [...]
  }

# Deprecate due to new evidence
POST /learning/promotions/{promotion_id}/deprecate
  {
    reason: "Pattern no longer holds",
    effective_from: "2026-03-01"
  }
```

---

## Design Scope & Maturity

### What This Document Covers

| Aspect | Status |
|--------|--------|
| Promotion hierarchy (Episodic → ESPP → ETSL) | ✅ Defined |
| Promotion flows (all 4 paths) | ✅ Defined |
| Promotion types and trigger conditions | ✅ Defined |
| Configurable promotion criteria | ✅ Defined |
| ETSL assertion translation | ✅ Defined |
| Conflict resolution strategies | ✅ Defined |
| API sketch (endpoints) | ✅ Defined |
| Procedural Memory record schemas | ✅ Defined (see [procedural-memory-store/](./procedural-memory-store/)) |
| Preference Memory record schemas | ✅ Defined (see [preference-memory-store/](./preference-memory-store/)) |

### What This Document Does NOT Cover (Intentionally Deferred)

The following aspects are **intentionally not specified** at this stage:

| Aspect | Reason for Deferral |
|--------|---------------------|
| **Pattern detection algorithms** | Requires operational experience to understand what patterns emerge in practice |
| **Automated promotion workflows** | Premature automation; initial cycles should be human-supervised |
| **Machine learning for pattern recognition** | Over-engineering before adoption; start with manual curation |
| **Governance workflow automation** | Governance processes vary by organization; define after adoption |
| **Conflict detection algorithms** | Need real-world conflict examples before designing algorithms |
| **Rollback automation** | Edge cases unknown; manual rollback sufficient initially |
| **Monitoring/alerting thresholds** | Baselines unknown until operational |

### Initial Operating Model: Manual Promotion

> **Design Principle**: Enterprise Learning Services is envisaged as a **manual, human-supervised process** in early Hub adoption cycles. Automation should be introduced incrementally as patterns become clear and governance matures.

**Phase 1 (Initial Adoption):**
- Analysts manually identify patterns in episodic memory
- Promotion candidates flagged via UI or reports
- Governance review via existing approval workflows
- ETSL promotion via manual assertion authoring

**Phase 2 (Maturity):**
- Pattern detection surfaced as suggestions (human confirms)
- Semi-automated evidence packaging
- Integrated governance workflow

**Phase 3 (Full Automation — Future):**
- Automated pattern detection with confidence thresholds
- Auto-promotion for low-risk patterns
- Continuous monitoring and anomaly detection

### Why No Premature Engineering

| Risk | Mitigation |
|------|------------|
| **Building for unknown patterns** | Wait until episodic memory accumulates real data |
| **Over-automating governance** | Let organizations define their approval processes first |
| **Optimizing before understanding** | Manual processes reveal what's actually worth automating |
| **Coupling to specific algorithms** | Keep flexibility for different approaches per domain |

---

## Related Documents

### CAF Components
- [CAF README](./README.md) — Cognitive Audit Fabric overview
- [Episodic Memory Store](./episodic-memory-store/README.md) — Event-based, case-bound memory
- [Semantic Memory Store](./semantic-memory-store/README.md) — Learned beliefs and patterns
- Procedural Memory Store *(stub pending)* — Learned skills and procedures  
- Preference Memory Store *(stub pending)* — Observed preferences and behaviors

### Key Record Types
- [Hypothesis Records](./semantic-memory-store/hypothesis-records.md) — Primary knowledge promotion candidates
- [Decision Records](./episodic-memory-store/decision-records.md) — Source for pattern detection
- [Outcome Records](./episodic-memory-store/outcome-records.md) — Source for learning feedback

### Target Systems
- [ETSL Overview](../../../pontus/etsl/) — Enterprise Temporal Semantic Layer
- [Enterprise Knowledge](../../../olympus-seer-docs/agentic-ai-concepts/enterprise-knowledge/README.md) — Asserted truths

