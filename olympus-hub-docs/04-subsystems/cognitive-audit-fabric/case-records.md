# Case Records

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-07  
> **Memory Type**: Episodic Memory  
> **Related**: [Record Relationships](./record-relationships.md) | [Memory Store Contract](./memory-store-contract.md)

---

## Overview

A **Case Record** is the root anchor for all episodic memory within a case. It establishes the case context, tracks lifecycle state, and provides the binding point for all related records (decisions, evidence, outcomes, etc.).

Every CAF record references a `case_id`—the Case Record is what that ID resolves to.

---

## Schema

```yaml
# ─────────────────────────────────────────────────────────────────
# Identity
# ─────────────────────────────────────────────────────────────────
case_id: uuid                           # Primary identifier (= hub request_id when Hub-originated)
case_type: string                       # e.g., "fraud_investigation", "loan_application", "dispute_resolution"
external_reference: string              # Optional: external system case/ticket ID

# ─────────────────────────────────────────────────────────────────
# Lifecycle
# ─────────────────────────────────────────────────────────────────
status: enum                            # open | in_progress | pending_review | escalated | resolved | closed
created_at: datetime                    # When case was opened
updated_at: datetime                    # Last modification
closed_at: datetime                     # When case was closed (if applicable)

# ─────────────────────────────────────────────────────────────────
# Description
# ─────────────────────────────────────────────────────────────────
title: string                           # Brief case title
summary: string                         # Human-readable description
summary_content_type:
  mime: string                          # "text/plain" or "text/markdown"
  format: string                        # text

# ─────────────────────────────────────────────────────────────────
# Actors
# ─────────────────────────────────────────────────────────────────
actors: array
actors_content_type:
  mime: "application/vnd.olympus.caf.case-actors.v1+json"
  schema: olympus.caf.case-actors
  schema_version: "1.0.0"

# Actor schema:
# - actor_id: uuid
# - actor_type: agent | human | system
# - role: string (e.g., "primary_analyst", "reviewer", "approver")
# - joined_at: datetime
# - left_at: datetime (optional)

# ─────────────────────────────────────────────────────────────────
# Subject (What/Who the case is about)
# ─────────────────────────────────────────────────────────────────
subject: object
subject_content_type:
  mime: string                          # e.g., "application/vnd.olympus.caf.case-subject.v1+json"
  schema: string
  schema_version: string

# Subject varies by case_type:
# - Fraud: { customer_id, account_id, transaction_ids }
# - Loan: { application_id, applicant_id }
# - Dispute: { dispute_id, parties: [...] }

# ─────────────────────────────────────────────────────────────────
# Resolution (when case is resolved/closed)
# ─────────────────────────────────────────────────────────────────
resolution: object
resolution_content_type:
  mime: "application/vnd.olympus.caf.case-resolution.v1+json"
  schema: olympus.caf.case-resolution
  schema_version: "1.0.0"

# Resolution schema:
# - outcome: string (e.g., "approved", "denied", "fraud_confirmed", "false_positive")
# - resolved_by: actor
# - resolved_at: datetime
# - resolution_notes: string
# - final_decision_id: uuid (reference to the closing DecisionRecord)

# ─────────────────────────────────────────────────────────────────
# Metrics
# ─────────────────────────────────────────────────────────────────
metrics: object
  total_decisions: integer              # Count of decisions made
  total_handoffs: integer               # Count of handoffs
  time_to_resolution_ms: integer        # Duration from open to resolved
  escalation_count: integer             # Number of escalations

# ─────────────────────────────────────────────────────────────────
# Hub Context (Optional)
# ─────────────────────────────────────────────────────────────────
hub_metadata:
  tenant_id: uuid
  subscription_id: uuid
  workbench_id: uuid
  scenario_id: uuid
  request_id: uuid                      # Same as case_id for Hub-originated cases
  parent_request_id: uuid               # For nested/sub-cases

# ─────────────────────────────────────────────────────────────────
# Tags & Classification
# ─────────────────────────────────────────────────────────────────
tags: array[string]                     # Free-form tags for filtering
priority: enum                          # low | medium | high | critical
sensitivity: enum                       # public | internal | confidential | restricted
```

---

## Status Lifecycle

```
┌─────────┐     ┌─────────────┐     ┌────────────────┐
│  open   │────▶│ in_progress │────▶│ pending_review │
└─────────┘     └─────────────┘     └────────────────┘
                      │                      │
                      │                      │
                      ▼                      ▼
               ┌───────────┐          ┌──────────┐
               │ escalated │─────────▶│ resolved │
               └───────────┘          └──────────┘
                                            │
                                            ▼
                                      ┌────────┐
                                      │ closed │
                                      └────────┘
```

| Status | Description |
|--------|-------------|
| `open` | Case created, not yet started |
| `in_progress` | Actively being worked |
| `pending_review` | Awaiting human review/approval |
| `escalated` | Elevated to higher authority |
| `resolved` | Decision made, outcome determined |
| `closed` | Case finalized, no further action |

---

## Relationship to Other Records

The Case Record is the **root** of the episodic memory graph:

```
                    ┌──────────────┐
                    │  CaseRecord  │
                    │   (anchor)   │
                    └──────┬───────┘
                           │
       ┌───────────────────┼───────────────────┐
       │                   │                   │
       ▼                   ▼                   ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ DecisionRec  │   │ HandoffCtx   │   │IncidentTime  │
└──────┬───────┘   └──────────────┘   └──────────────┘
       │
       ├─────────────────────┐
       │                     │
       ▼                     ▼
┌──────────────┐      ┌──────────────┐
│EvidenceBundle│      │ OutcomeRec   │
└──────┬───────┘      └──────────────┘
       │
       ▼
┌──────────────┐
│ContextSnap   │
└──────────────┘
```

### Traversal from Case

| To Find | Query |
|---------|-------|
| All decisions | `decision_records WHERE case_id = X` |
| All outcomes | `outcome_records WHERE case_id = X` |
| All actors | `case.actors` + `handoff_context.from_actor, to_actor` |
| Timeline | All records `WHERE case_id = X ORDER BY timestamp` |
| Final outcome | `case.resolution.final_decision_id` → DecisionRecord |

---

## Case Record vs Request

| Aspect | Case Record | Hub Request |
|--------|-------------|-------------|
| **Scope** | Business case (may span requests) | Single Hub workflow execution |
| **Lifecycle** | Days to months | Minutes to hours |
| **Binding** | All episodic memory | Hub workflow state |
| **ID** | `case_id` | `request_id` |

For Hub-originated cases, `case_id == request_id` initially. But a case may continue across multiple requests (e.g., customer returns, escalation re-opened).

---

## Examples

### Fraud Investigation Case

```json
{
  "case_id": "550e8400-e29b-41d4-a716-446655440000",
  "case_type": "fraud_investigation",
  "external_reference": "FRAUD-2026-00142",
  
  "status": "resolved",
  "created_at": "2026-01-07T10:00:00Z",
  "updated_at": "2026-01-07T14:30:00Z",
  "closed_at": "2026-01-07T14:35:00Z",
  
  "title": "Suspicious ACH transfer - Account 4521",
  "summary": "Automated fraud detection flagged unusual ACH transfer pattern. Investigation confirmed false positive after customer verification.",
  
  "actors": [
    {
      "actor_id": "agent-fraud-resolution",
      "actor_type": "agent",
      "role": "primary_analyst",
      "joined_at": "2026-01-07T10:00:05Z"
    },
    {
      "actor_id": "user-jane-analyst",
      "actor_type": "human",
      "role": "reviewer",
      "joined_at": "2026-01-07T11:30:00Z"
    }
  ],
  
  "subject": {
    "customer_id": "cust-789",
    "account_id": "acct-4521",
    "transaction_ids": ["txn-abc", "txn-def"],
    "flagged_amount": 15000.00,
    "flagged_reason": "velocity_anomaly"
  },
  
  "resolution": {
    "outcome": "false_positive",
    "resolved_by": {
      "actor_id": "user-jane-analyst",
      "actor_type": "human"
    },
    "resolved_at": "2026-01-07T14:30:00Z",
    "resolution_notes": "Customer verified via step-up authentication. Pattern explained by authorized recurring transfer.",
    "final_decision_id": "dec-xyz-123"
  },
  
  "metrics": {
    "total_decisions": 3,
    "total_handoffs": 1,
    "time_to_resolution_ms": 16200000,
    "escalation_count": 0
  },
  
  "hub_metadata": {
    "tenant_id": "tenant-acme-bank",
    "workbench_id": "fraud-ops",
    "request_id": "550e8400-e29b-41d4-a716-446655440000"
  },
  
  "tags": ["ach", "velocity", "false-positive"],
  "priority": "high",
  "sensitivity": "confidential"
}
```

---

## Related Documents

- [Record Relationships](./record-relationships.md) — How records link together
- [Decision Records](./decision-records.md) — Decision record schema
- [Memory Store Contract](./memory-store-contract.md) — Store registration and retrieval
- [CAF Store REST API](./caf-store-rest-api.md) — Write API specification

