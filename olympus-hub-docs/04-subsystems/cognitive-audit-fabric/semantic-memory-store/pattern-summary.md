# Pattern Summary Records

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-07  
> **Memory Type**: Semantic Memory  
> **Related**: [CAF README](../README.md) | [Semantic Memory Store](./README.md)

---

## Overview

A **Pattern Summary** captures a **recurring pattern with conditions and outcomes**. Unlike a Hypothesis (which is a claim about causation), a Pattern Summary is a descriptive observation of correlation.

### Key Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Descriptive** | Observes correlation, doesn't claim causation |
| **Conditional** | Specifies when the pattern applies |
| **Quantified** | Includes frequency, significance |
| **Decayable** | Staleness if not recently observed |

---

## Schema

```yaml
# ─────────────────────────────────────────────────────────────────
# Identity
# ─────────────────────────────────────────────────────────────────
pattern_id: uuid                        # Primary identifier
pattern_type: enum                      # behavioral | outcome | anomaly | failure_mode | success

# ─────────────────────────────────────────────────────────────────
# Description
# ─────────────────────────────────────────────────────────────────
title: string                           # Brief pattern title
description: string                     # Full pattern description
description_content_type:
  mime: "text/markdown"
  format: text

# ─────────────────────────────────────────────────────────────────
# Conditions (When pattern applies)
# ─────────────────────────────────────────────────────────────────
conditions: object
conditions_content_type:
  mime: "application/vnd.olympus.caf.pattern-conditions.v1+json"
  schema: olympus.caf.pattern-conditions
  schema_version: "1.0.0"

# Conditions schema:
# - preconditions: [{attribute, operator, value}]
# - context: {segment, entity_type, time_of_day, etc.}
# - triggers: [what activates the pattern]

# ─────────────────────────────────────────────────────────────────
# Observed Outcomes
# ─────────────────────────────────────────────────────────────────
observed_outcomes: array
observed_outcomes_content_type:
  mime: "application/vnd.olympus.caf.pattern-outcomes.v1+json"
  schema: olympus.caf.pattern-outcomes
  schema_version: "1.0.0"

# Outcome schema:
# - outcome: string (what happens)
# - probability: float (0-1)
# - typical_latency: duration (how long after trigger)
# - variance: object (range of outcomes)

# ─────────────────────────────────────────────────────────────────
# Statistics
# ─────────────────────────────────────────────────────────────────
frequency: float                        # How often observed (per time unit)
observation_count: integer              # Total observations
significance: float                     # Statistical significance (p-value inverse)
effect_size: float                      # Magnitude of effect
population_size: integer                # How many entities/cases examined

# ─────────────────────────────────────────────────────────────────
# Caveats & Limitations
# ─────────────────────────────────────────────────────────────────
caveats: array[string]                  # Known limitations
confounders: array[string]              # Potential confounding factors
known_exceptions: array                 # Documented exceptions
known_exceptions_content_type:
  mime: "application/vnd.olympus.caf.evidence-refs.v1+json"
  schema: olympus.caf.evidence-refs
  schema_version: "1.0.0"

# ─────────────────────────────────────────────────────────────────
# Evidence
# ─────────────────────────────────────────────────────────────────
evidence_links: array                   # Supporting episodes
evidence_links_content_type:
  mime: "application/vnd.olympus.caf.evidence-refs.v1+json"
  schema: olympus.caf.evidence-refs
  schema_version: "1.0.0"

# ─────────────────────────────────────────────────────────────────
# Temporal
# ─────────────────────────────────────────────────────────────────
valid_from: datetime                    # When pattern was first observed
last_observed: datetime                 # Most recent observation
observation_window:
  start: datetime
  end: datetime

# ─────────────────────────────────────────────────────────────────
# Freshness & Decay
# ─────────────────────────────────────────────────────────────────
decay_status: enum                      # active | weakening | stale | dormant
freshness:
  last_corroborated: datetime
  decay_model: string
  next_review_date: datetime

# ─────────────────────────────────────────────────────────────────
# Ownership
# ─────────────────────────────────────────────────────────────────
created_by: actor
review_owner: actor
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

## Pattern Types

| Type | Description | Example |
|------|-------------|---------|
| `behavioral` | How actors (agents, users) behave | "Customers who dispute once tend to dispute again within 90 days" |
| `outcome` | What results tend to occur | "Cases escalated on Friday have 20% longer resolution time" |
| `anomaly` | Unusual patterns detected | "Transaction velocity spikes precede 70% of confirmed fraud" |
| `failure_mode` | How things tend to fail | "Timeout errors cluster between 2-4pm EST" |
| `success` | What works well | "Step-up auth resolves 85% of low-confidence fraud alerts" |

---

## Examples

### Behavioral Pattern

```json
{
  "pattern_id": "pat-a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "pattern_type": "behavioral",
  "title": "Repeat Dispute Tendency",
  "description": "Customers who file one dispute have a 45% probability of filing another dispute within 90 days.",
  
  "conditions": {
    "preconditions": [
      {"attribute": "dispute_count", "operator": ">=", "value": 1}
    ],
    "context": {
      "segment": "retail_banking",
      "account_type": ["checking", "savings"]
    }
  },
  
  "observed_outcomes": [
    {
      "outcome": "second_dispute_filed",
      "probability": 0.45,
      "typical_latency": "P45D",
      "variance": {"min": "P7D", "max": "P90D"}
    }
  ],
  
  "frequency": 0.023,
  "observation_count": 1247,
  "significance": 0.99,
  "effect_size": 0.45,
  "population_size": 52000,
  
  "caveats": [
    "Based on 2025 data only",
    "Does not distinguish dispute types"
  ],
  "confounders": ["account_age", "transaction_volume"],
  
  "decay_status": "active",
  "freshness": {
    "last_corroborated": "2026-01-05T00:00:00Z",
    "decay_model": "linear",
    "next_review_date": "2026-04-01T00:00:00Z"
  },
  
  "hub_metadata": {
    "tenant_id": "tenant-acme-bank",
    "subscription_id": "sub-retail-banking",
    "workbench_id": "dispute-ops"
  },
  
  "tags": ["dispute", "repeat_behavior", "customer_risk"],
  "domain_category": "disputes"
}
```

---

## Related Documents

- [CAF README](../README.md)
- [Semantic Memory Store](./README.md)
- [Hypothesis Records](./hypothesis-records.md)
- [Evaluation Findings](./evaluation-findings.md)

