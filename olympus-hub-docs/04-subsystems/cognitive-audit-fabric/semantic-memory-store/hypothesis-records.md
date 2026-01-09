# Hypothesis Records

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-07  
> **Memory Type**: Semantic Memory  
> **Related**: [CAF README](../README.md) | [Semantic Memory Store](./README.md)

---

## Overview

A **Hypothesis Record** captures a **learned pattern pending promotion to Enterprise Knowledge**. Hypotheses arise from experience (episodes), accumulate evidence, and may eventually become asserted truth through governance.

### Key Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Probabilistic** | Confidence-scored, not asserted |
| **Evidence-grounded** | Linked to supporting (and contradicting) episodes |
| **Promotable** | Can become Knowledge through governance |
| **Decayable** | Weakens without reinforcement |
| **Domain-scoped** | Bound to workbench context |

---

## Schema

```yaml
# ─────────────────────────────────────────────────────────────────
# Identity
# ─────────────────────────────────────────────────────────────────
hypothesis_id: uuid                     # Primary identifier
pattern_type: string                    # behavioral | outcome | risk | failure_mode | optimization

# ─────────────────────────────────────────────────────────────────
# Statement
# ─────────────────────────────────────────────────────────────────
title: string                           # Brief hypothesis title
description: string                     # Full hypothesis statement
description_content_type:
  mime: "text/markdown"
  format: text

structured_form: object                 # Machine-readable hypothesis
structured_form_content_type:
  mime: "application/vnd.olympus.caf.hypothesis-structure.v1+json"
  schema: olympus.caf.hypothesis-structure
  schema_version: "1.0.0"

# ─────────────────────────────────────────────────────────────────
# Scope
# ─────────────────────────────────────────────────────────────────
scope: object
scope_content_type:
  mime: "application/vnd.olympus.caf.hypothesis-scope.v1+json"
  schema: olympus.caf.hypothesis-scope
  schema_version: "1.0.0"

# Scope schema:
# - applies_to: [entity_type, segment, condition]
# - exclusions: [explicit exclusions]
# - temporal_bounds: {valid_from, valid_to}
# - geographic_bounds: [regions]

# ─────────────────────────────────────────────────────────────────
# Confidence
# ─────────────────────────────────────────────────────────────────
confidence: float                       # 0-1: current confidence level
confidence_method: string               # How confidence was computed
confidence_history: array               # Historical confidence values
confidence_history_content_type:
  mime: "application/vnd.olympus.caf.confidence-history.v1+json"
  schema: olympus.caf.confidence-history
  schema_version: "1.0.0"

# Confidence history schema:
# - [{timestamp, confidence, reason, evidence_delta}]

# ─────────────────────────────────────────────────────────────────
# Evidence
# ─────────────────────────────────────────────────────────────────
evidence_links: array                   # Supporting episodes
evidence_links_content_type:
  mime: "application/vnd.olympus.caf.evidence-refs.v1+json"
  schema: olympus.caf.evidence-refs
  schema_version: "1.0.0"

# Evidence ref schema:
# - case_id: uuid
# - record_type: decision_record | outcome_record | incident_timeline
# - record_id: uuid
# - relevance: float (0-1)
# - contribution: supports | contradicts

counterexamples: array                  # Episodes that challenge this
counterexamples_content_type:
  mime: "application/vnd.olympus.caf.evidence-refs.v1+json"
  schema: olympus.caf.evidence-refs
  schema_version: "1.0.0"

evidence_summary:
  supporting_count: integer
  contradicting_count: integer
  last_supporting: datetime
  last_contradicting: datetime

# ─────────────────────────────────────────────────────────────────
# Freshness & Decay
# ─────────────────────────────────────────────────────────────────
freshness:
  created_at: datetime
  last_corroborated: datetime           # Last supporting evidence
  decay_model: string                   # linear | exponential | step
  decay_rate: float                     # Rate parameter
  next_review_date: datetime            # Scheduled review

# ─────────────────────────────────────────────────────────────────
# Lifecycle
# ─────────────────────────────────────────────────────────────────
status: enum                            # candidate | under_review | validated | promoted | deprecated | retired
status_history: array                   # [{timestamp, from_status, to_status, actor, reason}]

# Promotion tracking
promotion:
  promoted_at: datetime                 # When promoted (if applicable)
  promoted_by: actor
  promotion_target: uuid                # What it became (fact_id, rule_id)
  promotion_type: fact | rule | constraint | policy

# Retirement tracking
retirement:
  retired_at: datetime
  retired_by: actor
  retirement_reason: string             # disproven | superseded | stale | out_of_scope

# ─────────────────────────────────────────────────────────────────
# Ownership
# ─────────────────────────────────────────────────────────────────
created_by: actor
review_owner: actor                     # Who can promote/retire
stakeholders: [actor]                   # Notified on status changes

# ─────────────────────────────────────────────────────────────────
# Domain Context (Hub Metadata)
# ─────────────────────────────────────────────────────────────────
hub_metadata:
  tenant_id: uuid
  subscription_id: uuid
  workbench_id: uuid                    # Domain = Workbench

# ─────────────────────────────────────────────────────────────────
# Tags & Classification
# ─────────────────────────────────────────────────────────────────
tags: array[string]
domain_category: string                 # fraud | credit | compliance | operations
risk_level: enum                        # low | medium | high | critical
```

---

## Status Lifecycle

```
┌───────────┐     ┌──────────────┐     ┌───────────┐
│ candidate │────▶│ under_review │────▶│ validated │
└───────────┘     └──────────────┘     └─────┬─────┘
                                             │
                    ┌────────────────────────┼────────────────────────┐
                    │                        │                        │
                    ▼                        ▼                        ▼
             ┌──────────┐             ┌───────────┐             ┌─────────┐
             │ promoted │             │deprecated │             │ retired │
             └──────────┘             └───────────┘             └─────────┘
```

| Status | Description |
|--------|-------------|
| `candidate` | Newly created, insufficient evidence |
| `under_review` | Sufficient evidence, pending governance review |
| `validated` | Governance-approved but not yet knowledge |
| `promoted` | Became Enterprise Knowledge |
| `deprecated` | Superseded by better hypothesis |
| `retired` | Disproven or out of scope |

---

## Examples

### Fraud Pattern Hypothesis

```json
{
  "hypothesis_id": "hyp-550e8400-e29b-41d4-a716-446655440000",
  "pattern_type": "risk",
  "title": "Velocity + New Account = Higher False Positive Rate",
  "description": "High-velocity transactions on accounts < 30 days old have 3x false positive rate compared to established accounts. Consider adjusted thresholds.",
  
  "scope": {
    "applies_to": ["fraud_detection", "account_age < 30_days"],
    "exclusions": ["business_accounts", "pre_verified_customers"]
  },
  
  "confidence": 0.78,
  "confidence_method": "bayesian_update",
  
  "evidence_links": [
    {"case_id": "case-001", "record_type": "outcome_record", "relevance": 0.9, "contribution": "supports"},
    {"case_id": "case-002", "record_type": "outcome_record", "relevance": 0.85, "contribution": "supports"}
  ],
  "counterexamples": [
    {"case_id": "case-003", "record_type": "outcome_record", "relevance": 0.6, "contribution": "contradicts"}
  ],
  
  "evidence_summary": {
    "supporting_count": 47,
    "contradicting_count": 8,
    "last_supporting": "2026-01-06T14:30:00Z"
  },
  
  "freshness": {
    "created_at": "2025-11-15T10:00:00Z",
    "last_corroborated": "2026-01-06T14:30:00Z",
    "decay_model": "exponential",
    "decay_rate": 0.05,
    "next_review_date": "2026-02-15T00:00:00Z"
  },
  
  "status": "validated",
  "review_owner": {"type": "user", "id": "analyst-jane"},
  
  "hub_metadata": {
    "tenant_id": "tenant-acme-bank",
    "subscription_id": "sub-retail-banking",
    "workbench_id": "fraud-ops"
  },
  
  "tags": ["velocity", "new_account", "false_positive"],
  "domain_category": "fraud",
  "risk_level": "medium"
}
```

---

## Related Documents

- [CAF README](../README.md)
- [Semantic Memory Store](./README.md)
- [Pattern Summary](./pattern-summary.md)
- [Enterprise Knowledge Promotion](../../../../olympus-seer-docs/agentic-ai-concepts/enterprise-memory/semantic-memory.md#promotion-semantic-memory--knowledge)

