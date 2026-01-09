# Entity Belief Records

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-07  
> **Memory Type**: Semantic Memory  
> **Related**: [CAF README](../README.md) | [Semantic Memory Store](./README.md)

---

## Overview

An **Entity Belief** captures a **learned attribute about an entity** — a probabilistic inference derived from experience, not asserted master data.

### Key Distinction from Entity Master Data

| Aspect | Entity Master Data (Knowledge) | Entity Belief (Memory) |
|--------|-------------------------------|------------------------|
| **Source** | Asserted by authoritative system | Inferred from experience |
| **Authority** | System of record | Learned observation |
| **Confidence** | 100% (declared) | Probabilistic (0-1) |
| **Example** | "Customer X is in Segment A" | "Customer X is likely risk-averse" |

---

## Schema

```yaml
# ─────────────────────────────────────────────────────────────────
# Identity
# ─────────────────────────────────────────────────────────────────
belief_id: uuid                         # Primary identifier
belief_type: enum                       # attribute | classification | propensity | state

# ─────────────────────────────────────────────────────────────────
# Subject (What entity the belief is about)
# ─────────────────────────────────────────────────────────────────
subject:
  entity_type: string                   # customer | account | product | organization
  entity_id: uuid                       # External entity identifier
  entity_source: string                 # System of record for entity

# ─────────────────────────────────────────────────────────────────
# Belief Content
# ─────────────────────────────────────────────────────────────────
attribute: string                       # What property is believed
value: any                              # Believed value
value_type: enum                        # scalar | category | range | distribution
value_content_type:
  mime: string                          # e.g., "application/vnd.olympus.caf.belief-value.v1+json"
  schema: string
  schema_version: string

# For range/distribution values
value_distribution: object              # Optional: probability distribution
value_distribution_content_type:
  mime: "application/vnd.olympus.caf.value-distribution.v1+json"
  schema: olympus.caf.value-distribution
  schema_version: "1.0.0"

# Distribution schema:
# - type: normal | uniform | categorical | custom
# - parameters: {mean, std} | {min, max} | {categories: [{value, probability}]}

# ─────────────────────────────────────────────────────────────────
# Confidence
# ─────────────────────────────────────────────────────────────────
confidence: float                       # 0-1
confidence_method: string               # How computed
confidence_factors: array               # What contributed to confidence
confidence_factors_content_type:
  mime: "application/vnd.olympus.caf.confidence-factors.v1+json"
  schema: olympus.caf.confidence-factors
  schema_version: "1.0.0"

# Confidence factors schema:
# - [{factor, contribution, direction}]

# ─────────────────────────────────────────────────────────────────
# Source & Provenance
# ─────────────────────────────────────────────────────────────────
source: enum                            # learned | inferred | derived | aggregated
inference_method: string                # How belief was formed

# For derived beliefs
derived_from: array                     # Source beliefs
derived_from_content_type:
  mime: "application/vnd.olympus.caf.belief-refs.v1+json"
  schema: olympus.caf.belief-refs
  schema_version: "1.0.0"

# ─────────────────────────────────────────────────────────────────
# Evidence
# ─────────────────────────────────────────────────────────────────
evidence_links: array                   # Supporting episodes
evidence_links_content_type:
  mime: "application/vnd.olympus.caf.evidence-refs.v1+json"
  schema: olympus.caf.evidence-refs
  schema_version: "1.0.0"

contradicting_evidence: array           # Challenging episodes
contradicting_evidence_content_type:
  mime: "application/vnd.olympus.caf.evidence-refs.v1+json"
  schema: olympus.caf.evidence-refs
  schema_version: "1.0.0"

evidence_summary:
  supporting_count: integer
  contradicting_count: integer
  last_supporting: datetime

# ─────────────────────────────────────────────────────────────────
# Freshness & Decay
# ─────────────────────────────────────────────────────────────────
freshness:
  created_at: datetime
  last_corroborated: datetime
  decay_model: string                   # linear | exponential | step
  decay_rate: float
  half_life: duration                   # Time for confidence to halve

# ─────────────────────────────────────────────────────────────────
# Scope & Context
# ─────────────────────────────────────────────────────────────────
scope: object
scope_content_type:
  mime: "application/vnd.olympus.caf.belief-scope.v1+json"
  schema: olympus.caf.belief-scope
  schema_version: "1.0.0"

# Scope schema:
# - context: {conditions under which belief holds}
# - exclusions: [when belief doesn't apply]
# - temporal_validity: {valid_from, valid_to}

# ─────────────────────────────────────────────────────────────────
# Lifecycle
# ─────────────────────────────────────────────────────────────────
status: enum                            # active | weakening | stale | retired | superseded
superseded_by: belief_id                # If replaced
retirement_reason: string               # If retired

# ─────────────────────────────────────────────────────────────────
# Ownership
# ─────────────────────────────────────────────────────────────────
created_by: actor                       # System or user that created
created_at: datetime
updated_at: datetime

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

## Belief Types

| Type | Description | Example |
|------|-------------|---------|
| `attribute` | Learned property value | "Customer likely prefers email contact" |
| `classification` | Inferred category | "Customer is likely in high-value segment" |
| `propensity` | Likelihood of behavior | "Customer is likely to dispute (propensity: 0.65)" |
| `state` | Inferred current state | "Account is likely dormant" |

---

## Examples

### Attribute Belief

```json
{
  "belief_id": "bel-a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "belief_type": "attribute",
  
  "subject": {
    "entity_type": "customer",
    "entity_id": "cust-789",
    "entity_source": "core-banking"
  },
  
  "attribute": "risk_tolerance",
  "value": "risk_averse",
  "value_type": "category",
  
  "confidence": 0.73,
  "confidence_method": "behavioral_inference",
  "confidence_factors": [
    {"factor": "transaction_patterns", "contribution": 0.4, "direction": "positive"},
    {"factor": "product_preferences", "contribution": 0.3, "direction": "positive"},
    {"factor": "short_observation_period", "contribution": -0.1, "direction": "negative"}
  ],
  
  "source": "learned",
  "inference_method": "behavioral_clustering",
  
  "evidence_links": [
    {"case_id": "case-001", "record_type": "decision_record", "relevance": 0.8},
    {"case_id": "case-002", "record_type": "decision_record", "relevance": 0.7}
  ],
  
  "evidence_summary": {
    "supporting_count": 12,
    "contradicting_count": 2,
    "last_supporting": "2026-01-05T00:00:00Z"
  },
  
  "freshness": {
    "created_at": "2025-10-01T00:00:00Z",
    "last_corroborated": "2026-01-05T00:00:00Z",
    "decay_model": "exponential",
    "decay_rate": 0.02,
    "half_life": "P90D"
  },
  
  "status": "active",
  
  "hub_metadata": {
    "tenant_id": "tenant-acme-bank",
    "subscription_id": "sub-retail-banking",
    "workbench_id": "customer-analytics"
  },
  
  "tags": ["risk_profile", "behavioral"],
  "domain_category": "customer_intelligence"
}
```

### Propensity Belief

```json
{
  "belief_id": "bel-b2c3d4e5-f6a7-8901-bcde-f23456789012",
  "belief_type": "propensity",
  
  "subject": {
    "entity_type": "customer",
    "entity_id": "cust-456",
    "entity_source": "core-banking"
  },
  
  "attribute": "dispute_propensity",
  "value": 0.65,
  "value_type": "scalar",
  
  "value_distribution": {
    "type": "normal",
    "parameters": {"mean": 0.65, "std": 0.12}
  },
  
  "confidence": 0.78,
  "source": "derived",
  "inference_method": "propensity_model_v2",
  
  "scope": {
    "context": {"transaction_type": ["ach", "wire"]},
    "exclusions": ["recurring_payments"],
    "temporal_validity": {"valid_from": "2026-01-01T00:00:00Z"}
  },
  
  "status": "active",
  
  "hub_metadata": {
    "tenant_id": "tenant-acme-bank",
    "subscription_id": "sub-retail-banking",
    "workbench_id": "dispute-ops"
  }
}
```

---

## Related Documents

- [CAF README](../README.md)
- [Semantic Memory Store](./README.md)
- [Relationship Beliefs](./relationship-beliefs.md)
- [Pattern Summary](./pattern-summary.md)

