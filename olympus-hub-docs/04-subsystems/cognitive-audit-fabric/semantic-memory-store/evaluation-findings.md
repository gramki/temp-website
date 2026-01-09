# Evaluation Finding Records

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-07  
> **Memory Type**: Semantic Memory  
> **Related**: [CAF README](../README.md) | [Semantic Memory Store](./README.md)

---

## Overview

An **Evaluation Finding** captures **benchmark, test, or evaluation results** — quantified outcomes from systematic analysis. Unlike patterns (observed correlations), findings are results of deliberate experiments or evaluations.

### Key Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Quantified** | Specific metrics with statistical measures |
| **Reproducible** | Methodology documented for replication |
| **Scoped** | Valid under specific conditions |
| **Time-bound** | May expire or require re-evaluation |

---

## Schema

```yaml
# ─────────────────────────────────────────────────────────────────
# Identity
# ─────────────────────────────────────────────────────────────────
finding_id: uuid                        # Primary identifier
finding_type: enum                      # benchmark | ab_test | regression | drift | quality_gate

# ─────────────────────────────────────────────────────────────────
# Description
# ─────────────────────────────────────────────────────────────────
title: string                           # Brief finding title
description: string                     # Full finding description
description_content_type:
  mime: "text/markdown"
  format: text

# ─────────────────────────────────────────────────────────────────
# Population & Scope
# ─────────────────────────────────────────────────────────────────
population: object
population_content_type:
  mime: "application/vnd.olympus.caf.evaluation-population.v1+json"
  schema: olympus.caf.evaluation-population
  schema_version: "1.0.0"

# Population schema:
# - description: string
# - size: integer
# - sampling_method: random | stratified | exhaustive
# - filters: [{attribute, operator, value}]
# - time_window: {start, end}

valid_for: object                       # Scope of applicability
valid_for_content_type:
  mime: "application/vnd.olympus.caf.finding-scope.v1+json"
  schema: olympus.caf.finding-scope
  schema_version: "1.0.0"

# Scope schema:
# - entity_types: [string]
# - segments: [string]
# - scenarios: [string]
# - conditions: [{attribute, operator, value}]

# ─────────────────────────────────────────────────────────────────
# Metric & Result
# ─────────────────────────────────────────────────────────────────
metric: string                          # What was measured
metric_definition: string               # How the metric is defined

result: object
result_content_type:
  mime: "application/vnd.olympus.caf.evaluation-result.v1+json"
  schema: olympus.caf.evaluation-result
  schema_version: "1.0.0"

# Result schema:
# - value: number | object
# - unit: string
# - baseline: number (comparison point)
# - delta: number (change from baseline)
# - delta_percent: float
# - direction: improvement | regression | neutral

# ─────────────────────────────────────────────────────────────────
# Statistical Measures
# ─────────────────────────────────────────────────────────────────
significance: float                     # Statistical significance (p-value inverse or confidence)
confidence_interval:
  lower: float
  upper: float
  level: float                          # e.g., 0.95 for 95% CI

effect_size: float                      # Cohen's d or similar
sample_size: integer
statistical_test: string                # t-test, chi-square, etc.

# ─────────────────────────────────────────────────────────────────
# Methodology
# ─────────────────────────────────────────────────────────────────
methodology: string                     # Description of how evaluation was conducted
methodology_content_type:
  mime: "text/markdown"
  format: text

conditions: object                      # Under what conditions
conditions_content_type:
  mime: "application/vnd.olympus.caf.evaluation-conditions.v1+json"
  schema: olympus.caf.evaluation-conditions
  schema_version: "1.0.0"

# For A/B tests
variants: array                         # Test variants
variants_content_type:
  mime: "application/vnd.olympus.caf.ab-variants.v1+json"
  schema: olympus.caf.ab-variants
  schema_version: "1.0.0"

# Variants schema:
# - variant_id: string
# - description: string
# - allocation: float (% of traffic)
# - result: object

# ─────────────────────────────────────────────────────────────────
# Evidence
# ─────────────────────────────────────────────────────────────────
evidence_links: array                   # Raw data / episodes
evidence_links_content_type:
  mime: "application/vnd.olympus.caf.evidence-refs.v1+json"
  schema: olympus.caf.evidence-refs
  schema_version: "1.0.0"

data_source: string                     # Where data came from
data_snapshot_uri: string               # URI to raw data if preserved

# ─────────────────────────────────────────────────────────────────
# Temporal
# ─────────────────────────────────────────────────────────────────
evaluation_date: datetime               # When evaluation was conducted
data_period:
  start: datetime
  end: datetime

expiry: datetime                        # When to re-evaluate
replication_required: boolean           # Should this be replicated before acting?

# ─────────────────────────────────────────────────────────────────
# Lifecycle
# ─────────────────────────────────────────────────────────────────
status: enum                            # current | superseded | invalidated | pending_replication
superseded_by: finding_id               # If replaced by newer finding
invalidated_reason: string              # If invalidated

# ─────────────────────────────────────────────────────────────────
# Ownership
# ─────────────────────────────────────────────────────────────────
created_by: actor
reviewed_by: actor
created_at: datetime

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

## Finding Types

| Type | Description | Example |
|------|-------------|---------|
| `benchmark` | Performance against established baseline | "Model accuracy: 94.2% (baseline: 91.0%)" |
| `ab_test` | Comparison of variants | "Variant B outperforms A by 12% on resolution time" |
| `regression` | Decline from previous performance | "Precision dropped 8% since last month" |
| `drift` | Distribution shift detected | "Input distribution shifted significantly (KL div: 0.15)" |
| `quality_gate` | Pass/fail on quality criteria | "Agent passed all quality gates for production" |

---

## Examples

### Benchmark Finding

```json
{
  "finding_id": "find-a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "finding_type": "benchmark",
  
  "title": "Fraud Detection Model Q4 2025 Benchmark",
  "description": "Quarterly benchmark of fraud detection model against holdout set.",
  
  "population": {
    "description": "Q4 2025 transactions, stratified sample",
    "size": 50000,
    "sampling_method": "stratified",
    "filters": [
      {"attribute": "transaction_date", "operator": "between", "value": ["2025-10-01", "2025-12-31"]}
    ]
  },
  
  "metric": "precision",
  "metric_definition": "True positives / (True positives + False positives)",
  
  "result": {
    "value": 0.942,
    "unit": "ratio",
    "baseline": 0.910,
    "delta": 0.032,
    "delta_percent": 3.5,
    "direction": "improvement"
  },
  
  "significance": 0.99,
  "confidence_interval": {
    "lower": 0.935,
    "upper": 0.949,
    "level": 0.95
  },
  "effect_size": 0.42,
  "sample_size": 50000,
  "statistical_test": "bootstrap_ci",
  
  "evaluation_date": "2026-01-05T00:00:00Z",
  "data_period": {
    "start": "2025-10-01T00:00:00Z",
    "end": "2025-12-31T23:59:59Z"
  },
  "expiry": "2026-04-01T00:00:00Z",
  
  "status": "current",
  
  "hub_metadata": {
    "tenant_id": "tenant-acme-bank",
    "subscription_id": "sub-retail-banking",
    "workbench_id": "fraud-ops"
  },
  
  "tags": ["model_performance", "quarterly_benchmark", "fraud_detection"],
  "domain_category": "fraud"
}
```

### A/B Test Finding

```json
{
  "finding_id": "find-b2c3d4e5-f6a7-8901-bcde-f23456789012",
  "finding_type": "ab_test",
  
  "title": "Step-Up Auth vs Manual Review for Mid-Risk Cases",
  "description": "A/B test comparing step-up authentication against manual review for cases with fraud score 0.5-0.7",
  
  "metric": "resolution_time_hours",
  
  "variants": [
    {
      "variant_id": "A",
      "description": "Manual review by analyst",
      "allocation": 0.5,
      "result": {"mean": 4.2, "median": 3.8, "p95": 12.0}
    },
    {
      "variant_id": "B",
      "description": "Automated step-up authentication",
      "allocation": 0.5,
      "result": {"mean": 0.8, "median": 0.5, "p95": 2.1}
    }
  ],
  
  "result": {
    "value": -3.4,
    "unit": "hours",
    "baseline": 4.2,
    "delta": -3.4,
    "delta_percent": -81,
    "direction": "improvement"
  },
  
  "significance": 0.999,
  "sample_size": 2400,
  
  "status": "current",
  
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
- [Pattern Summary](./pattern-summary.md)
- [Hypothesis Records](./hypothesis-records.md)

