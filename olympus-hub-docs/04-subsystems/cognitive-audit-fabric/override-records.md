# Override Records

> **Status:** 🔴 Stub — Placeholder for expansion

Override Records capture **manual overrides of automated or prior decisions**—documenting who overrode, why, and with what authority. CAF provides the **catalog and schema** for override records; the records themselves are stored in **Enterprise Memory**.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Document exceptions and overrides with accountability |
| **Timing** | Written at override time |
| **Linkage** | Always linked to original DecisionRecord being overridden |
| **Storage** | Enterprise Memory (via Memory Services) |
| **CAF Role** | Catalog, schema, authority validation, pattern detection |

---

## Why Override Records Matter

Without override records:
- Cannot track when policies were bypassed
- Cannot identify patterns of overrides (may indicate policy gaps)
- Cannot hold overriders accountable
- Cannot distinguish between override outcomes and original decision outcomes

---

## Override Record Schema

```yaml
override_record:
  # Identity
  id: uuid                         # Unique identifier (UUID v4)
  timestamp: datetime
  case_id: uuid                    # Universal binding ID (UUID v4, = hub request_id when Hub-originated)
  
  # Hub Metadata (optional - populated when override made within Hub context)
  hub_metadata:
    tenant_id: string              # Tenant identifier
    subscription_id: string        # Subscription within tenant
    workbench_id: string           # Workbench where override occurred
    scenario_id: string            # Scenario under which override was made
    request_id: string             # Hub Request this override belongs to
    parent_request_id: string      # Parent request if nested (optional)
  
  # Linkage
  original_decision_id: uuid       # → DecisionRecord being overridden
  original_decision_type: string
  original_decision_value: object  # What was originally decided
  original_decision_value_content_type:
    mime: string                   # Type varies by decision_type
    schema: string
    schema_version: string
  
  # Override Details
  override_action: string          # The new decision/action
  override_type: enum              # reversal | modification | escalation | exception
  
  # Rationale
  rationale: text                  # Why the override was made
  rationale_category: enum         # policy_gap | new_information | error_correction | customer_request | business_exception
  supporting_evidence: array       # Evidence supporting the override
  supporting_evidence_content_type:
    mime: string                   # e.g., "application/vnd.olympus.caf.override-evidence.v1+json"
    schema: string
    schema_version: string
  evidence_bundle_id: uuid         # → EvidenceBundle for override justification
  
  # Authority
  overriding_actor: string         # Who performed the override
  overriding_actor_type: enum      # human (always human for overrides)
  authority_level: string          # What authority level was used
  authority_justification: text    # How authority was verified
  approval_chain: array            # Approvals required and obtained
  approval_chain_content_type:
    mime: string                   # e.g., "application/vnd.olympus.caf.approval-record.v1+json"
    schema: string
    schema_version: string
  
  # Risk Assessment
  risk_assessment: object          # Risk of the override
  risk_assessment_content_type:
    mime: string                   # e.g., "application/vnd.olympus.caf.risk-assessment.v1+json"
    schema: string
    schema_version: string
  risk_accepted_by: string         # Who accepted the risk
  
  # Outcome Tracking
  expected_outcome: object         # What overrider expects to happen
  expected_outcome_content_type:
    mime: string
    schema: string
    schema_version: string
  outcome_record_id: uuid          # → OutcomeRecord (populated when outcome known)
  outcome_validated: boolean       # Whether override led to expected outcome
  
  # Context
  context_at_override: object      # Relevant context when override was made
  context_at_override_content_type:
    mime: string                   # e.g., "application/vnd.olympus.caf.override-context.v1+json"
    schema: string
    schema_version: string
  time_pressure: boolean           # Whether override was made under time pressure
  
  # Metadata
  tags: array
  linked_records: array
  policy_exceptions: array         # Which policies were excepted
```

---

## Override Types

| Type | Description | Example |
|------|-------------|---------|
| **Reversal** | Completely reverse the original decision | Deny → Approve |
| **Modification** | Partially change the decision | Reduce refund amount |
| **Escalation** | Move decision to higher authority | Send to supervisor |
| **Exception** | Grant policy exception | Approve despite policy violation |

---

## Rationale Categories

| Category | Description | Policy Implication |
|----------|-------------|-------------------|
| **Policy Gap** | Policy doesn't cover this situation | May need policy update |
| **New Information** | Information not available at decision time | Process improvement |
| **Error Correction** | Original decision was incorrect | Quality issue |
| **Customer Request** | Customer escalation/appeal | Customer satisfaction |
| **Business Exception** | Business need overrides policy | Risk acceptance |

---

## Authority Requirements

| Override Impact | Authority Level | Approval Required |
|-----------------|-----------------|-------------------|
| **Low** | Same-level operator | Self-approval with rationale |
| **Medium** | Supervisor | Supervisor approval |
| **High** | Manager + Compliance | Dual approval |
| **Critical** | Executive | Executive sign-off |

---

## Pattern Detection

CAF monitors override patterns to identify:

| Pattern | Indicator | Action |
|---------|-----------|--------|
| **High Override Rate** | >X% of decisions overridden | Policy review |
| **Repeat Overrider** | Single user many overrides | Training/coaching |
| **Systematic Override** | Same scenario always overridden | Policy gap |
| **Poor Override Outcomes** | Overrides lead to bad outcomes | Process review |

---

## Retention

| Record Type | Retention Period | Rationale |
|-------------|------------------|-----------|
| **Override Records** | 10 years | Regulatory compliance, audit |
| **Associated Evidence** | 10 years | Support audit trail |

---

## Related Documentation

- [CAF Overview](./README.md)
- [Decision Records](./decision-records.md)
- [Outcome Records](./outcome-records.md)
- [Hub Enterprise Memory](../memory-services/hub-enterprise-memory.md)

---

*TODO: Detailed design — authority validation, pattern detection algorithms, approval workflow integration*

