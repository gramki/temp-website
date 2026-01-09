# Outcome Records

> **Status:** 🔴 Stub — Placeholder for expansion

Outcome Records capture **what happened after a decision was made**—enabling feedback loops, learning, and accuracy measurement. CAF provides the **catalog and schema** for outcome records; the records themselves are stored in **Enterprise Memory**.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Track decision outcomes for learning and measurement |
| **Timing** | Written when outcome is known (may be delayed from decision) |
| **Linkage** | Always linked to originating DecisionRecord |
| **Storage** | Enterprise Memory (via Memory Services) |
| **CAF Role** | Catalog, schema, outcome-to-decision linking |

---

## Why Outcome Records Matter

Without outcome records:
- Cannot measure decision accuracy
- Cannot learn which decisions led to good/bad outcomes
- Cannot improve decision models over time
- Cannot identify systematic decision errors

---

## Outcome Record Schema

```yaml
outcome_record:
  # Identity & Integrity
  id: uuid                         # Unique identifier (UUID v4)
  content_hash: string             # sha256:<hex> — hash of record content (immutability verification)
  timestamp: datetime
  case_id: uuid                    # Universal binding ID (UUID v4, = hub request_id when Hub-originated)
  
  # Hub Metadata (optional - populated when captured within Hub context)
  hub_metadata:
    tenant_id: string              # Tenant identifier
    subscription_id: string        # Subscription within tenant
    workbench_id: string           # Workbench where outcome was recorded
    scenario_id: string            # Scenario governing original decision
    request_id: string             # Hub Request this outcome relates to
    parent_request_id: string      # Parent request if nested (optional)
  
  # Linkage
  decision_record_id: uuid         # → DecisionRecord this outcome measures
  entity_type: string              # Same as decision
  entity_id: uuid                  # Same as decision
  
  # Outcome Details
  outcome_type: enum               # success | failure | partial | pending | unknown
  outcome_description: text        # Human-readable outcome description
  
  # Measurement
  expected_outcome: object         # What the decision predicted would happen
  expected_outcome_content_type:
    mime: string                   # e.g., "application/vnd.olympus.caf.outcome-expectation.v1+json"
    schema: string
    schema_version: string
  actual_outcome: object           # What actually happened
  actual_outcome_content_type:
    mime: string                   # Same schema as expected_outcome for comparison
    schema: string
    schema_version: string
  variance: object                 # Difference between expected and actual
  variance_content_type:
    mime: string                   # e.g., "application/vnd.olympus.caf.outcome-variance.v1+json"
    schema: string
    schema_version: string
  
  # Timing
  time_to_outcome: duration        # Time from decision to outcome
  outcome_detection_method: enum   # manual | automated | system_event
  
  # Attribution
  contributing_factors: array      # Factors that influenced the outcome
  contributing_factors_content_type:
    mime: string                   # e.g., "application/vnd.olympus.caf.contributing-factor.v1+json"
    schema: string
    schema_version: string
  external_factors: array          # Factors outside the decision's control
  external_factors_content_type:
    mime: string
    schema: string
    schema_version: string
  
  # Classification
  outcome_category: string         # Domain-specific categorization
  severity: enum                   # For failures: critical | high | medium | low
  
  # Learning
  lessons_learned: text            # Optional learnings captured
  recommended_changes: array       # Suggested policy/procedure changes
  
  # Metadata
  recorded_by: string              # Who/what recorded the outcome
  recorded_by_type: enum           # human | system | agent
  tags: array
  linked_records: array
```

---

## Outcome Types

| Type | Description | Example |
|------|-------------|---------|
| **Success** | Decision achieved desired result | Fraud correctly identified |
| **Failure** | Decision did not achieve desired result | False positive, missed fraud |
| **Partial** | Some goals achieved, others not | Fraud caught but customer friction |
| **Pending** | Outcome not yet determinable | Decision made, awaiting result |
| **Unknown** | Outcome cannot be determined | Data unavailable |

---

## Capture Triggers

Outcome records are captured:

| Trigger | Description |
|---------|-------------|
| **Case Closure** | Case reaches terminal state |
| **Time-Based** | Outcome window expires |
| **Event-Based** | System event indicates outcome |
| **Manual Entry** | Human records outcome |
| **Feedback Loop** | Customer/user provides feedback |

---

## Outcome Windows

| Decision Type | Typical Window | Example |
|---------------|----------------|---------|
| **Fraud Alert** | 30-90 days | Chargeback window |
| **Loan Approval** | 6-12 months | Default window |
| **Case Routing** | Hours-Days | Resolution time |
| **Risk Classification** | Ongoing | Continuous validation |

---

## Learning Integration

Outcome records feed into:

| Consumer | Use Case |
|----------|----------|
| **Model Training** | Labeled examples for ML |
| **Policy Review** | Evidence for policy changes |
| **Agent Improvement** | Feedback for agent tuning |
| **Analytics** | Decision quality dashboards |

---

## Related Documentation

- [CAF Overview](../README.md)
- [Episodic Memory Store](./README.md)
- [Decision Records](./decision-records.md)
- [Enterprise Memory](../../memory-services/enterprise-memory/README.md)

---

*TODO: Detailed design — outcome detection automation, variance calculation, learning pipeline integration*

