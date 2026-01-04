# Decision Records

> **Status:** 🔴 Stub — Placeholder for expansion

Decision Records capture the **rationale and context of decisions at decision time**—enabling audit, explanation, and institutional learning. CAF provides the **catalog and schema** for decision records; the records themselves are stored in **Enterprise Memory**.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Capture decision rationale for audit and explanation |
| **Timing** | Written at decision time, not retroactively |
| **Scope** | All consequential decisions by agents (human and AI) |
| **Immutability** | Append-only, cannot be modified |
| **Storage** | Enterprise Memory (via Memory Services) |
| **CAF Role** | Catalog, schema, policies, indexing |

---

## Why Decision Records Matter

Without decision records:
- Cannot explain *why* a decision was made
- Cannot reconstruct the context at decision time
- Cannot prove reasonableness to regulators
- Cannot learn from past decisions

---

## Decision Record Schema

```yaml
decision_record:
  # Identity
  id: string
  timestamp: datetime
  tenant_id: string
  
  # Decision Context
  decision_type: string  # e.g., "loan_approval", "fraud_alert", "case_routing"
  entity_type: string    # what entity this decision affects
  entity_id: string
  request_id: string     # originating request
  
  # The Decision
  decision: string       # the actual decision made
  alternatives: array    # alternatives considered
  selected_alternative: string
  
  # Rationale
  factors: array         # factors that influenced the decision
  weights: object        # relative importance of factors
  confidence: number     # confidence level (0-1)
  reasoning: text        # human-readable reasoning
  
  # Evidence
  evidence_bundle_id: string  # link to evidence bundle
  context_snapshot_id: string # link to context at decision time
  
  # Accountability
  actor_type: enum       # human | ai_agent
  actor_id: string       # who/what made the decision
  accountable_party: string # human accountable (always human)
  authority_chain: array # delegation chain if AI
  
  # Metadata
  tags: array
  linked_records: array
```

---

## Decision Types

| Category | Examples |
|----------|----------|
| **Approval/Rejection** | Loan approval, claim approval, access grant |
| **Routing** | Case assignment, escalation, queue routing |
| **Classification** | Fraud classification, risk tier, priority |
| **Action Selection** | Next best action, treatment selection |
| **Exception** | Override, policy exception, manual adjustment |

---

## Capture Points

Decision records are created at:

| Capture Point | Description |
|---------------|-------------|
| **Gateway Decision Points** | BPMN gateways in Rhea |
| **Agent Decisions** | AI agent action selections |
| **Human Decisions** | Task completions with decisions |
| **Automation Decisions** | Rule engine outputs |
| **Exception Grants** | Manual overrides |

---

## CAF's Role

CAF provides the **control plane** for decision records, not the storage:

| CAF Provides | Memory Services Provides |
|--------------|-------------------------|
| Schema definitions | Actual record storage |
| Capture policies (when/what) | Write operations |
| Catalog (metadata, indexes) | Read/query operations |
| Linking rules | Retention execution |
| Query interfaces | Storage tiering |

---

## Immutability & Versioning

| Principle | Implementation |
|-----------|----------------|
| **Append-only** | Records cannot be modified after creation |
| **Supersession** | New decisions can supersede old ones |
| **Linking** | Superseding records link to original |
| **Timestamp** | All records have immutable timestamps |

---

## Query Patterns

| Query | Use Case |
|-------|----------|
| By entity | All decisions about a specific customer/case |
| By decision type | All fraud decisions in a period |
| By actor | All decisions by a specific agent |
| By outcome | Decisions that led to specific outcomes |
| Similar context | Decisions in similar situations (semantic) |

---

## Compliance Mapping

| Regulation | Decision Record Support |
|------------|-------------------------|
| **GDPR Art. 22** | Automated decision explanation |
| **ECOA** | Fair lending decision documentation |
| **SOX** | Financial decision audit trail |
| **BCBS 239** | Risk data governance |

---

## Related Documentation

- [CAF Overview](./README.md)
- [Explanation Service](./explanation-service.md)
- [Evidence Bundles](./evidence-bundles.md)
- [Hub Enterprise Memory](../memory-services/hub-enterprise-memory.md)

---

*TODO: Detailed design — schema validation, capture hooks, storage optimization, search indexing*

