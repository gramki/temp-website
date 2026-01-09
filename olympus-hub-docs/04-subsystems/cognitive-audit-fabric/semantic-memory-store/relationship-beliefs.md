# Relationship Belief Records

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-07  
> **Memory Type**: Semantic Memory  
> **Related**: [CAF README](../README.md) | [Semantic Memory Store](./README.md)

---

## Overview

A **Relationship Belief** captures a **learned connection between entities** — a probabilistic inference that two entities are related in some way, derived from experience rather than asserted by a system of record.

### Key Distinction from Master Relationships

| Aspect | Master Relationship (Knowledge) | Relationship Belief (Memory) |
|--------|--------------------------------|------------------------------|
| **Source** | Declared in system of record | Inferred from behavior/patterns |
| **Authority** | Authoritative | Probabilistic |
| **Confidence** | 100% (asserted) | 0-1 (learned) |
| **Example** | "Account X belongs to Customer Y" | "Customer A and B are likely related" |

---

## Schema

```yaml
# ─────────────────────────────────────────────────────────────────
# Identity
# ─────────────────────────────────────────────────────────────────
belief_id: uuid                         # Primary identifier
relationship_type: string               # Type of believed relationship

# ─────────────────────────────────────────────────────────────────
# Entities
# ─────────────────────────────────────────────────────────────────
from_entity:
  entity_type: string                   # customer | account | organization
  entity_id: uuid
  entity_source: string                 # System of record

to_entity:
  entity_type: string
  entity_id: uuid
  entity_source: string

directionality: enum                    # directed | bidirectional | unknown

# ─────────────────────────────────────────────────────────────────
# Relationship Details
# ─────────────────────────────────────────────────────────────────
relationship_category: enum             # familial | financial | organizational | behavioral | geographic

# For more specific relationships
relationship_subtype: string            # spouse, parent, authorized_user, business_partner, etc.

# Optional: relationship strength/weight
strength: float                         # 0-1 (for weighted relationships)

# Optional: relationship attributes
attributes: object
attributes_content_type:
  mime: "application/vnd.olympus.caf.relationship-attributes.v1+json"
  schema: olympus.caf.relationship-attributes
  schema_version: "1.0.0"

# Attributes schema (varies by relationship_type):
# - For familial: {inferred_relation: "spouse" | "parent" | "sibling"}
# - For financial: {shared_patterns: [...], transaction_links: [...]}
# - For behavioral: {co_occurrence_score: float, shared_actions: [...]}

# ─────────────────────────────────────────────────────────────────
# Confidence
# ─────────────────────────────────────────────────────────────────
confidence: float                       # 0-1
confidence_method: string               # How computed
confidence_breakdown: object            # Per-signal contributions
confidence_breakdown_content_type:
  mime: "application/vnd.olympus.caf.confidence-breakdown.v1+json"
  schema: olympus.caf.confidence-breakdown
  schema_version: "1.0.0"

# Breakdown schema:
# - [{signal, weight, contribution}]

# ─────────────────────────────────────────────────────────────────
# Inference
# ─────────────────────────────────────────────────────────────────
inference_method: string                # How relationship was inferred
inference_signals: array                # What signals contributed
inference_signals_content_type:
  mime: "application/vnd.olympus.caf.inference-signals.v1+json"
  schema: olympus.caf.inference-signals
  schema_version: "1.0.0"

# Inference signals schema:
# - signal_type: shared_address | shared_device | transaction_pattern | behavioral_correlation
# - signal_value: object
# - signal_strength: float

# ─────────────────────────────────────────────────────────────────
# Evidence
# ─────────────────────────────────────────────────────────────────
evidence_links: array
evidence_links_content_type:
  mime: "application/vnd.olympus.caf.evidence-refs.v1+json"
  schema: olympus.caf.evidence-refs
  schema_version: "1.0.0"

evidence_summary:
  supporting_count: integer
  contradicting_count: integer
  first_observed: datetime
  last_observed: datetime

# ─────────────────────────────────────────────────────────────────
# Freshness & Decay
# ─────────────────────────────────────────────────────────────────
freshness:
  created_at: datetime
  last_corroborated: datetime
  decay_model: string
  half_life: duration

# ─────────────────────────────────────────────────────────────────
# Scope
# ─────────────────────────────────────────────────────────────────
scope: object
scope_content_type:
  mime: "application/vnd.olympus.caf.belief-scope.v1+json"
  schema: olympus.caf.belief-scope
  schema_version: "1.0.0"

# ─────────────────────────────────────────────────────────────────
# Lifecycle
# ─────────────────────────────────────────────────────────────────
status: enum                            # active | weakening | stale | retired | confirmed
confirmed_by: object                    # If confirmed by authoritative source
confirmed_by_content_type:
  mime: "application/vnd.olympus.caf.confirmation.v1+json"
  schema: olympus.caf.confirmation
  schema_version: "1.0.0"

# Confirmation schema:
# - confirmed_at: datetime
# - confirmed_by: actor
# - confirmation_source: system of record
# - promoted_to: master_relationship_id

# ─────────────────────────────────────────────────────────────────
# Ownership
# ─────────────────────────────────────────────────────────────────
created_by: actor
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
risk_implication: enum                  # none | low | medium | high
```

---

## Relationship Categories

| Category | Description | Examples |
|----------|-------------|----------|
| `familial` | Family/household relationships | Spouse, parent, child, sibling |
| `financial` | Money/account relationships | Shared accounts, fund transfers |
| `organizational` | Business relationships | Employer, business partner |
| `behavioral` | Pattern-based connections | Similar behavior, co-occurrence |
| `geographic` | Location-based | Shared address, same region |

---

## Common Inference Signals

| Signal Type | Description | Weight Factor |
|-------------|-------------|---------------|
| `shared_address` | Same physical address | High |
| `shared_device` | Same device fingerprint | Medium-High |
| `shared_phone` | Same phone number | Medium-High |
| `shared_email_domain` | Same email domain (non-generic) | Low |
| `transaction_pattern` | Regular fund transfers between | Medium |
| `behavioral_correlation` | Similar action patterns | Low-Medium |
| `temporal_co_occurrence` | Actions at similar times | Low |
| `network_clustering` | Graph-based clustering | Varies |

---

## Examples

### Familial Relationship Belief

```json
{
  "belief_id": "rel-a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "relationship_type": "likely_family_member",
  
  "from_entity": {
    "entity_type": "customer",
    "entity_id": "cust-123",
    "entity_source": "core-banking"
  },
  "to_entity": {
    "entity_type": "customer",
    "entity_id": "cust-456",
    "entity_source": "core-banking"
  },
  
  "directionality": "bidirectional",
  "relationship_category": "familial",
  "relationship_subtype": "spouse",
  
  "confidence": 0.82,
  "confidence_method": "multi_signal_fusion",
  "confidence_breakdown": [
    {"signal": "shared_address", "weight": 0.4, "contribution": 0.32},
    {"signal": "shared_phone", "weight": 0.3, "contribution": 0.24},
    {"signal": "transaction_pattern", "weight": 0.2, "contribution": 0.16},
    {"signal": "temporal_co_occurrence", "weight": 0.1, "contribution": 0.10}
  ],
  
  "inference_method": "relationship_inference_model_v3",
  "inference_signals": [
    {"signal_type": "shared_address", "signal_value": {"address_id": "addr-789"}, "signal_strength": 0.95},
    {"signal_type": "shared_phone", "signal_value": {"phone_hash": "abc123"}, "signal_strength": 0.90},
    {"signal_type": "transaction_pattern", "signal_value": {"pattern": "regular_transfers"}, "signal_strength": 0.75}
  ],
  
  "evidence_summary": {
    "supporting_count": 24,
    "contradicting_count": 1,
    "first_observed": "2024-06-15T00:00:00Z",
    "last_observed": "2026-01-05T00:00:00Z"
  },
  
  "freshness": {
    "created_at": "2024-06-15T00:00:00Z",
    "last_corroborated": "2026-01-05T00:00:00Z",
    "decay_model": "linear",
    "half_life": "P365D"
  },
  
  "status": "active",
  "risk_implication": "low",
  
  "hub_metadata": {
    "tenant_id": "tenant-acme-bank",
    "subscription_id": "sub-retail-banking",
    "workbench_id": "customer-analytics"
  },
  
  "tags": ["family", "household", "relationship_graph"],
  "domain_category": "customer_intelligence"
}
```

### Financial Relationship Belief (Potential Fraud Ring)

```json
{
  "belief_id": "rel-b2c3d4e5-f6a7-8901-bcde-f23456789012",
  "relationship_type": "potential_fraud_ring_member",
  
  "from_entity": {
    "entity_type": "account",
    "entity_id": "acct-111",
    "entity_source": "core-banking"
  },
  "to_entity": {
    "entity_type": "account",
    "entity_id": "acct-222",
    "entity_source": "core-banking"
  },
  
  "directionality": "bidirectional",
  "relationship_category": "financial",
  "relationship_subtype": "suspicious_fund_flow",
  
  "strength": 0.68,
  "confidence": 0.71,
  
  "attributes": {
    "shared_patterns": ["rapid_fund_movement", "new_account_velocity"],
    "transaction_links": [
      {"from": "acct-111", "to": "acct-222", "count": 12, "total_amount": 45000}
    ],
    "network_position": "bridge_node"
  },
  
  "inference_signals": [
    {"signal_type": "transaction_pattern", "signal_value": {"pattern": "layering"}, "signal_strength": 0.85},
    {"signal_type": "shared_device", "signal_value": {"device_hash": "dev-xyz"}, "signal_strength": 0.72},
    {"signal_type": "network_clustering", "signal_value": {"cluster_id": "cluster-42"}, "signal_strength": 0.65}
  ],
  
  "status": "active",
  "risk_implication": "high",
  
  "hub_metadata": {
    "tenant_id": "tenant-acme-bank",
    "subscription_id": "sub-retail-banking",
    "workbench_id": "fraud-ops"
  },
  
  "tags": ["fraud_ring", "suspicious", "network_analysis"],
  "domain_category": "fraud"
}
```

---

## Related Documents

- [CAF README](../README.md)
- [Semantic Memory Store](./README.md)
- [Entity Beliefs](./entity-beliefs.md)
- [Pattern Summary](./pattern-summary.md)

