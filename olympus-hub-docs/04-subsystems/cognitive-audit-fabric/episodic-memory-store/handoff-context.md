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
  # Identity & Integrity
  id: uuid                         # Unique identifier (UUID v4)
  content_hash: string             # sha256:<hex> — hash of record content (immutability verification)
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

Handoff context surfaces in multiple UI components, integrated with Task Management:

### Task Management Integration

When a handoff creates a new task assignment, the handoff context is automatically linked:

```yaml
task_handoff_binding:
  # Task created from handoff
  task:
    task_id: "task-xyz789"
    case_id: "case-12345"
    assigned_to: "user-jane"
    status: "assigned"
    
    # Link to handoff context
    handoff_context_id: "hoff-55555"
    
    # Key fields surfaced in task
    context_summary:
      from_agent: "agent-triage-001"
      handoff_reason: "escalation"
      sla_status: "on_track"
      open_items_count: 3
```

### Agent Desk Integration

The **Agent Desk** displays handoff context when an agent receives a task:

```yaml
agent_desk_handoff_panel:
  # Panel layout
  sections:
    - section: "context_summary"
      title: "What You Need to Know"
      content:
        - current_state.summary
        - current_state.key_facts
        - current_state.working_hypothesis
      
    - section: "work_completed"
      title: "What's Been Done"
      content:
        - actions_taken (collapsible list)
        - decisions_made (linked to decision records)
        - evidence_gathered (linked to evidence bundles)
      
    - section: "open_items"
      title: "What's Needed"
      content:
        - open_items.pending_actions (actionable checklist)
        - open_items.unanswered_questions
        - open_items.blockers (highlighted)
      
    - section: "recommendations"
      title: "Suggested Approach"
      content:
        - recommendations.suggested_next_steps
        - recommendations.areas_of_concern (warning style)
        - recommendations.relevant_precedent (linked)
      
    - section: "sla_status"
      title: "Time Sensitivity"
      content:
        - sla_status.deadline
        - sla_status.time_remaining (countdown)
        - sla_status.sla_risk (color-coded)
```

### Supervisor Desk Integration

Supervisors monitor handoff quality across their team:

```yaml
supervisor_handoff_dashboard:
  # Metrics panel
  metrics:
    - metric: "avg_handoff_quality_score"
      display: "Average Handoff Quality"
      threshold: { warning: 0.7, critical: 0.5 }
    
    - metric: "handoffs_with_missing_fields"
      display: "Incomplete Handoffs"
      drill_down: true
    
    - metric: "handoffs_by_reason"
      display: "Handoff Reasons (Distribution)"
      chart_type: "pie"
  
  # Handoff list
  handoff_list:
    columns:
      - case_id
      - from_agent
      - to_agent
      - handoff_reason
      - handoff_quality_score
      - timestamp
    
    filters:
      - by_team
      - by_reason
      - by_quality_score_range
      - by_date_range
    
    actions:
      - view_handoff_details
      - view_case
      - reassign_task
```

### Case Timeline Integration

Handoffs appear as events in the case timeline:

```yaml
timeline_event:
  event_type: "handoff"
  timestamp: "2026-01-07T10:00:00Z"
  
  # Timeline card content
  card:
    icon: "handoff"
    title: "Escalated to Human Analyst"
    subtitle: "From: agent-triage-001 → To: user-jane"
    
    # Expandable details
    details:
      - label: "Reason"
        value: "escalation"
      - label: "Summary"
        value: "High-value wire transfer flagged as suspicious..."
      - label: "Open Items"
        value: "3 items"
    
    # Actions
    actions:
      - label: "View Full Handoff"
        action: "navigate_to_handoff"
        params: { handoff_id: "hoff-55555" }
```

### Surface Mapping

| Interface | Use | Key Data Displayed |
|-----------|-----|-------------------|
| **Agent Desk** | Context panel when receiving task | Summary, key facts, open items, recommendations, SLA |
| **Supervisor Desk** | Handoff quality monitoring | Quality scores, incomplete handoffs, reason distribution |
| **Case Timeline** | Handoff events visible | Event card with from/to, reason, summary |
| **Analytics** | Handoff patterns and quality | Quality trends, bottleneck identification |
| **Task List** | Quick context indicator | SLA status, open items count, from agent |

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

## Task Assignment Flow

When a handoff occurs, the following flow integrates with Task Management:

```
1. Hub Application creates HandoffContext record
   - Attaches to REQUEST_UPDATE
   - Signal Exchange routes to episodic memory

2. Task Management receives handoff notification
   - Creates or updates Task for receiving agent
   - Links task.handoff_context_id to handoff record

3. Agent Desk queries handoff context
   - Uses memory.get_handoff_context tool
   - Displays context panel with handoff details

4. Agent works on task
   - References handoff context as needed
   - Creates new records (decisions, evidence) linked to same case_id

5. If agent hands off again
   - Creates new HandoffContext record
   - Cycle repeats
```

---

## Quality Scoring Algorithm

Handoff quality is scored based on completeness and actionability:

```yaml
quality_scoring:
  # Required fields (binary)
  required_fields:
    - current_state.summary
    - current_state.status
    - actions_taken
    - handoff_reason
  
  # Quality dimensions (weighted)
  dimensions:
    - dimension: "completeness"
      weight: 0.3
      scoring:
        - field: "current_state.key_facts"
          points: 0.05 per item, max 0.15
        - field: "open_items.pending_actions"
          points: 0.05 per item, max 0.10
        - field: "recommendations.suggested_next_steps"
          points: 0.05 per item, max 0.05
    
    - dimension: "actionability"
      weight: 0.3
      scoring:
        - field: "open_items.pending_actions"
          criteria: "contains actionable verbs"
          points: 0.10
        - field: "recommendations.suggested_next_steps"
          criteria: "contains specific guidance"
          points: 0.10
        - field: "sla_status"
          criteria: "sla_status present and valid"
          points: 0.10
    
    - dimension: "context_richness"
      weight: 0.2
      scoring:
        - field: "evidence_gathered"
          points: 0.05 per item, max 0.10
        - field: "decisions_made"
          points: 0.05 per item, max 0.10
    
    - dimension: "precedent_linkage"
      weight: 0.2
      scoring:
        - field: "recommendations.relevant_precedent"
          points: 0.10 if present with similarity > 0.7
        - field: "recommendations.applicable_sops"
          points: 0.10 if present
  
  # Final score
  final_score:
    formula: "weighted sum of dimension scores"
    range: 0.0 to 1.0
    thresholds:
      excellent: ">= 0.85"
      good: ">= 0.70"
      adequate: ">= 0.50"
      poor: "< 0.50"
```

---

## Related Documentation

- [CAF Overview](../README.md)
- [Episodic Memory Store](./README.md)
- [Decision Records](./decision-records.md)
- [Memory Services](../../memory-services/README.md)
- [Hub Enterprise Memory](../../memory-services/hub-enterprise-memory.md)
- [Memory Access Tools](../../memory-services/memory-access-tools.md)
- [Task Management](../../task-management/README.md)

---

*TODO: Detailed design — handoff completeness validation enforcement, real-time quality feedback, agent training integration*

