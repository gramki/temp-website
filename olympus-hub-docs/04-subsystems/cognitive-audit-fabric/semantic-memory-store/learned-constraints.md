# Learned Constraint Records

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-07  
> **Memory Type**: Semantic Memory  
> **Related**: [CAF README](../README.md) | [Semantic Memory Store](./README.md)

---

## Overview

A **Learned Constraint** captures an **advisory guideline derived from experience** — "Avoid X when Y" or "Prefer A over B under conditions C". Unlike policy rules (which are normative), learned constraints are **informative** and **probabilistic**.

### Key Distinction from Policy Rules

| Aspect | Policy Rule (Knowledge) | Learned Constraint (Memory) |
|--------|------------------------|----------------------------|
| **Source** | Asserted by governance | Learned from experience |
| **Authority** | Binding | Advisory |
| **Violation** | Requires override justification | May be ignored with context |
| **Confidence** | Declared (100%) | Probabilistic (0-1) |

---

## Schema

```yaml
# ─────────────────────────────────────────────────────────────────
# Identity
# ─────────────────────────────────────────────────────────────────
constraint_id: uuid                     # Primary identifier
constraint_type: enum                   # avoid | prefer | escalate_when | verify_when | delay_until

# ─────────────────────────────────────────────────────────────────
# Statement
# ─────────────────────────────────────────────────────────────────
statement: string                       # Natural language constraint
statement_content_type:
  mime: "text/plain"
  format: text

structured_form: object                 # Machine-readable condition/action
structured_form_content_type:
  mime: "application/vnd.olympus.caf.constraint-rule.v1+json"
  schema: olympus.caf.constraint-rule
  schema_version: "1.0.0"

# Structured form schema:
# - condition: {attribute, operator, value}[]
# - action: avoid | prefer | escalate | verify | delay
# - alternative: what to do instead

# ─────────────────────────────────────────────────────────────────
# Scope
# ─────────────────────────────────────────────────────────────────
scope: object
scope_content_type:
  mime: "application/vnd.olympus.caf.constraint-scope.v1+json"
  schema: olympus.caf.constraint-scope
  schema_version: "1.0.0"

# Scope schema:
# - applies_to: [entity_type, segment, scenario]
# - exclusions: [explicit exclusions]
# - temporal_bounds: {valid_from, valid_to}

# ─────────────────────────────────────────────────────────────────
# Risk & Impact
# ─────────────────────────────────────────────────────────────────
risk_if_violated: string                # What happens if ignored
risk_level: enum                        # low | medium | high | critical
historical_violation_outcomes: array    # What happened when violated
historical_violation_outcomes_content_type:
  mime: "application/vnd.olympus.caf.violation-outcomes.v1+json"
  schema: olympus.caf.violation-outcomes
  schema_version: "1.0.0"

# Violation outcome schema:
# - case_id: uuid
# - outcome: string
# - severity: low | medium | high
# - timestamp: datetime

# ─────────────────────────────────────────────────────────────────
# Confidence
# ─────────────────────────────────────────────────────────────────
confidence: float                       # 0-1
confidence_method: string               # How computed
confidence_trend: enum                  # increasing | stable | decreasing

# ─────────────────────────────────────────────────────────────────
# Evidence
# ─────────────────────────────────────────────────────────────────
evidence_links: array                   # Supporting episodes
evidence_links_content_type:
  mime: "application/vnd.olympus.caf.evidence-refs.v1+json"
  schema: olympus.caf.evidence-refs
  schema_version: "1.0.0"

evidence_summary:
  supporting_count: integer
  violation_count: integer              # How often violated
  violation_success_rate: float         # % of violations that worked anyway

# ─────────────────────────────────────────────────────────────────
# Lifecycle
# ─────────────────────────────────────────────────────────────────
status: enum                            # active | under_review | suspended | retired
created_at: datetime
updated_at: datetime
review_date: datetime                   # When to re-evaluate

# ─────────────────────────────────────────────────────────────────
# Ownership
# ─────────────────────────────────────────────────────────────────
created_by: actor
review_owner: actor
stakeholders: [actor]

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
domain_category: string
```

---

## Constraint Types

| Type | Description | Example |
|------|-------------|---------|
| `avoid` | Don't do X under conditions | "Avoid auto-approve for customers < 6 months old" |
| `prefer` | Prefer A over B | "Prefer manual review over auto-deny for first-time disputes" |
| `escalate_when` | Escalate under conditions | "Escalate when fraud score > 0.8 AND account age < 30 days" |
| `verify_when` | Add verification step | "Verify identity when transaction > 5x average" |
| `delay_until` | Wait for condition | "Delay final decision until 24h observation window" |

---

## Examples

### Avoid Constraint

```json
{
  "constraint_id": "con-a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "constraint_type": "avoid",
  
  "statement": "Avoid auto-approve for customers with account age under 30 days when transaction exceeds $1,000",
  
  "structured_form": {
    "condition": [
      {"attribute": "account_age_days", "operator": "<", "value": 30},
      {"attribute": "transaction_amount", "operator": ">", "value": 1000}
    ],
    "action": "avoid",
    "target": "auto_approve",
    "alternative": "manual_review"
  },
  
  "scope": {
    "applies_to": ["fraud_detection", "transaction_approval"],
    "exclusions": ["pre_verified_customers", "business_accounts"]
  },
  
  "risk_if_violated": "Higher false negative rate observed (12% vs 3% baseline)",
  "risk_level": "high",
  
  "confidence": 0.85,
  "confidence_method": "outcome_analysis",
  "confidence_trend": "stable",
  
  "evidence_summary": {
    "supporting_count": 234,
    "violation_count": 45,
    "violation_success_rate": 0.38
  },
  
  "status": "active",
  "review_date": "2026-04-01T00:00:00Z",
  
  "hub_metadata": {
    "tenant_id": "tenant-acme-bank",
    "subscription_id": "sub-retail-banking",
    "workbench_id": "fraud-ops"
  },
  
  "tags": ["new_account", "high_value", "auto_approve"],
  "domain_category": "fraud"
}
```

### Escalate When Constraint

```json
{
  "constraint_id": "con-b2c3d4e5-f6a7-8901-bcde-f23456789012",
  "constraint_type": "escalate_when",
  
  "statement": "Escalate to senior analyst when multiple risk indicators combine",
  
  "structured_form": {
    "condition": [
      {"attribute": "fraud_score", "operator": ">", "value": 0.7},
      {"attribute": "account_age_days", "operator": "<", "value": 90},
      {"attribute": "transaction_velocity", "operator": ">", "value": 3.0}
    ],
    "action": "escalate",
    "target": "senior_analyst_queue"
  },
  
  "risk_if_violated": "Junior analyst resolution rate drops to 45% (vs 78% with escalation)",
  "risk_level": "medium",
  
  "confidence": 0.72,
  "status": "active",
  
  "hub_metadata": {
    "tenant_id": "tenant-acme-bank",
    "subscription_id": "sub-retail-banking",
    "workbench_id": "fraud-ops"
  }
}
```

---

## Related Documents

- [CAF README](../README.md)
- [Semantic Memory Store](./README.md)
- [Hypothesis Records](./hypothesis-records.md)
- [Pattern Summary](./pattern-summary.md)

