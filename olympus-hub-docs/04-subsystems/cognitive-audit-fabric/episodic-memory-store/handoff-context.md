# Handoff Context Records

> **Status:** 🔴 Stub — Placeholder for expansion

Handoff Context Records capture the **state and learnings when work transitions between agents**—human to AI, AI to human, or human to human. CAF provides the **catalog and schema** for handoff records; the records themselves are stored in **Enterprise Memory**.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Enable seamless transitions between agents working on a case |
| **Timing** | Written at handoff time |
| **Linkage** | Linked to Request, Case, and relevant DecisionRecords |
| **Storage** | Enterprise Memory (via Memory Services) |
| **CAF Role** | Catalog, schema, handoff completeness validation |

---

## Why Handoff Context Matters

Without handoff context:
- Receiving agent starts from scratch
- Context is lost in transitions
- Duplicate work and customer friction
- No continuity when agents change

---

## Handoff Context Schema

```yaml
handoff_context:
  # Identity
  id: uuid                         # Unique identifier (UUID v4)
  timestamp: datetime
  case_id: uuid                    # Universal binding ID (UUID v4, = hub request_id when Hub-originated)
  
  # Hub Metadata (optional - populated when handoff within Hub context)
  hub_metadata:
    tenant_id: string              # Tenant identifier
    subscription_id: string        # Subscription within tenant
    workbench_id: string           # Workbench where handoff occurred
    scenario_id: string            # Scenario governing this case
    request_id: string             # Hub Request being handed off
    parent_request_id: string      # Parent request if nested (optional)
  
  # Case/Request Reference
  external_case_id: string         # External case ID if applicable
  entity_type: string              # Type of entity being worked
  entity_id: uuid

  # Handoff Parties
  from_agent: uuid                 # Agent handing off
  from_agent_type: enum            # human | ai_agent
  to_agent: uuid                   # Agent receiving (may be null for queue)
  to_agent_type: enum              # human | ai_agent | queue
  handoff_reason: enum             # escalation | shift_change | skill_mismatch | scheduled | completed_portion
  
  # Current State Summary
  current_state:
    content_type:
      mime: string                 # e.g., "application/vnd.olympus.caf.handoff-state.v1+json"
      schema: string
      schema_version: string
    status: string                 # Current case/request status
    summary: text                  # Human-readable summary
    key_facts: array               # Critical facts established
    key_facts_content_type:
      mime: string
      schema: string
      schema_version: string
    working_hypothesis: text       # Current understanding of situation
    
  # Work Completed
  actions_taken: array             # Actions performed by from_agent
  actions_taken_content_type:
    mime: string                   # e.g., "application/vnd.olympus.caf.action-summary.v1+json"
    schema: string
    schema_version: string
  decisions_made: array[uuid]      # → DecisionRecord[] made during this assignment
  evidence_gathered: array[uuid]   # → EvidenceBundle[] collected
  documents_reviewed: array        # Documents that were reviewed
  documents_reviewed_content_type:
    mime: string                   # e.g., "application/vnd.olympus.caf.document-reference.v1+json"
    schema: string
    schema_version: string
  tools_invoked: array             # Tools that were called
  tools_invoked_content_type:
    mime: string                   # e.g., "application/vnd.olympus.caf.tool-invocation.v1+json"
    schema: string
    schema_version: string
  
  # Open Items
  open_items:
    content_type:
      mime: string                 # e.g., "application/vnd.olympus.caf.open-items.v1+json"
      schema: string
      schema_version: string
    pending_actions: array         # Actions still needed
    awaiting_response: array       # External parties we're waiting on
    unanswered_questions: array    # Questions that need answers
    blockers: array                # Blocking issues
    
  # Guidance for Receiving Agent
  recommendations:
    content_type:
      mime: string                 # e.g., "application/vnd.olympus.caf.handoff-recommendations.v1+json"
      schema: string
      schema_version: string
    suggested_next_steps: array    # What to do next
    areas_of_concern: array        # Things to watch out for
    relevant_precedent: array      # Links to similar cases
    applicable_sops: array         # Relevant procedures
    
  # Context for Understanding
  customer_context:
    content_type:
      mime: string                 # e.g., "application/vnd.olympus.caf.customer-context.v1+json"
      schema: string
      schema_version: string
    sentiment: enum                # positive | neutral | negative | escalated
    communication_notes: text      # How to communicate with this customer
    prior_interactions: array      # Relevant history
    prior_interactions_content_type:
      mime: string
      schema: string
      schema_version: string
    
  # Time Sensitivity
  sla_status:
    deadline: datetime             # When case must be resolved
    time_remaining: duration
    sla_risk: enum                 # on_track | at_risk | breached
    
  # Metadata
  handoff_quality_score: number    # Completeness of handoff (0-1)
  tags: array
  linked_records: array
```

---

## Handoff Types

| Type | From | To | Trigger |
|------|------|-----|---------|
| **Escalation** | AI Agent | Human Agent | Confidence < threshold |
| **Skill Routing** | Agent | Specialist Agent | Skill mismatch |
| **Shift Change** | Human | Human | End of shift |
| **Tier Escalation** | Tier-1 | Tier-2 | Complexity/Authority |
| **Completion Handoff** | AI Agent | Human Agent | AI portion complete |
| **Queue Return** | Agent | Queue | Agent unavailable |

---

## Handoff Reasons

| Reason | Description | Common For |
|--------|-------------|------------|
| **escalation** | Needs higher authority or expertise | AI → Human |
| **shift_change** | Normal work transition | Human → Human |
| **skill_mismatch** | Current agent lacks required skill | Any |
| **scheduled** | Planned handoff point in workflow | Workflow-based |
| **completed_portion** | Agent finished their part | Multi-agent workflows |
| **timeout** | Agent couldn't complete in time | AI → Human |
| **customer_request** | Customer requested different agent | Any → Human |

---

## Handoff Quality Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| **Completeness** | All required fields populated | 100% |
| **Accuracy** | Summary accurately reflects state | Human validation |
| **Actionability** | Next steps are clear | Receiving agent rates |
| **Time Saved** | How much ramp-up time saved | Measured reduction |

---

## UI Integration

Handoff context surfaces in:

| Interface | Use |
|-----------|-----|
| **Agent Desk** | Context panel when receiving task |
| **Supervisor Desk** | Handoff quality monitoring |
| **Case Timeline** | Handoff events visible |
| **Analytics** | Handoff patterns and quality |

---

## Retention

| Record Type | Retention | Notes |
|-------------|-----------|-------|
| **Handoff Context** | 1 year after case close | Or longer if linked to audit records |

---

## Related Documentation

- [CAF Overview](../README.md)
- [Episodic Memory Store](./README.md)
- [Decision Records](./decision-records.md)
- [Hub Enterprise Memory](../memory-services/hub-enterprise-memory.md)
- [Task Management](../task-management/README.md)

---

*TODO: Detailed design — handoff completeness validation, UI components, quality scoring algorithm*

