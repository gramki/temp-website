# Incident Timelines

> **Status:** 🔴 Stub — Placeholder for expansion

Incident Timelines capture the **chronological sequence of events across systems and agents during incidents or complex cases**—enabling forensic analysis, root cause investigation, and postmortem learning. CAF provides the **catalog and schema** for incident timelines; the records themselves are stored in **Enterprise Memory**.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Chronicle events for investigation and learning |
| **Scope** | Cross-system, cross-agent event sequences |
| **Use Cases** | Postmortems, root cause analysis, dispute investigation |
| **Storage** | Enterprise Memory (via Memory Services) |
| **CAF Role** | Catalog, schema, event correlation, timeline assembly |

---

## Why Incident Timelines Matter

Without incident timelines:
- Cannot reconstruct what happened during incidents
- Cannot identify root causes across systems
- Cannot learn from complex failures
- Cannot defend decisions during disputes

---

## Incident Timeline Schema

```yaml
incident_timeline:
  # Identity & Integrity
  id: uuid                         # Unique identifier (UUID v4)
  content_hash: string             # sha256:<hex> — hash of record content (immutability verification)
  created_at: datetime
  case_id: uuid                    # Universal binding ID (UUID v4, = hub request_id when Hub-originated)
  
  # Hub Metadata (optional - populated when incident tracked within Hub context)
  hub_metadata:
    tenant_id: string              # Tenant identifier
    subscription_id: string        # Subscription within tenant
    workbench_id: string           # Workbench managing the incident
    scenario_id: string            # Primary scenario (if applicable)
    request_id: string             # Originating request (if applicable)
    parent_request_id: string      # Parent request if nested (optional)
  
  # Incident Reference
  incident_type: enum              # system_incident | case_investigation | dispute | audit_request
  incident_id: string              # External incident/case ID (may be external system reference)
  title: text                      # Human-readable title
  description: text                # Summary of the incident
  
  # Scope
  scope:
    start_time: datetime           # When timeline starts
    end_time: datetime             # When timeline ends (may be open)
    affected_systems: array        # Systems involved
    affected_entities: array       # Entities affected
    affected_agents: array         # Agents involved
    
  # Events (ordered chronologically)
  events:
    content_type:
      mime: string                 # e.g., "application/vnd.olympus.caf.timeline-event.v1+json"
      schema: string
      schema_version: string
    items:
      - event_id: string
        timestamp: datetime
        event_type: enum           # signal | decision | action | error | external | observation
        source_system: string      # Which system generated this event
        
        # Actor
        actor: string              # Who/what performed the action
        actor_type: enum           # human | ai_agent | system
        
        # Event Details
        summary: text              # Brief description
        details: object            # Full event details
        details_content_type:
          mime: string             # Type varies by event_type and source_system
          schema: string
          schema_version: string
        
        # Links
        linked_records:
          decision_record_id: uuid   # → DecisionRecord
          evidence_bundle_id: uuid   # → EvidenceBundle
          request_id: uuid           # → Hub Request
          task_id: uuid              # → Task
          
        # Classification
        severity: enum             # info | warning | error | critical
        category: string           # Domain-specific event category
        
        # Evidence
        evidence_refs: array       # Links to supporting evidence
      
  # Analysis
  analysis:
    content_type:
      mime: string                 # e.g., "application/vnd.olympus.caf.incident-analysis.v1+json"
      schema: string
      schema_version: string
    root_cause: text               # Identified root cause
    contributing_factors: array    # Factors that contributed
    contributing_factors_content_type:
      mime: string
      schema: string
      schema_version: string
    timeline_gaps: array           # Missing information
    
  # Impact
  impact:
    content_type:
      mime: string                 # e.g., "application/vnd.olympus.caf.incident-impact.v1+json"
      schema: string
      schema_version: string
    business_impact: text          # Business consequences
    customer_impact: text          # Customer consequences
    systems_affected: array        # Systems impacted
    duration: duration             # How long impact lasted
    
  # Resolution
  resolution:
    status: enum                   # open | investigating | resolved | closed
    resolution_summary: text       # How it was resolved
    resolved_at: datetime
    resolved_by: string
    
  # Learnings
  learnings:
    lessons_learned: array         # Key takeaways
    recommended_actions: array     # Improvements suggested
    related_hypotheses: array      # Links to HypothesisRecords
    policy_changes: array          # Policy updates triggered
    
  # Metadata
  created_by: string
  last_updated_by: string
  tags: array
  linked_timelines: array          # Related incidents
```

---

## Event Types

| Type | Description | Example |
|------|-------------|---------|
| **signal** | Signal received by Hub | Fraud alert received |
| **decision** | Decision made | Claim denied |
| **action** | Action taken | Account frozen |
| **error** | Error occurred | API timeout |
| **external** | External system event | Vendor response received |
| **observation** | Human observation | Analyst noted anomaly |
| **escalation** | Escalation event | Escalated to Tier-2 |
| **communication** | Customer/stakeholder communication | Email sent to customer |

---

## Timeline Assembly

Incident timelines are assembled from:

| Source | Event Types |
|--------|-------------|
| **Signal Exchange** | Signals, triggers, requests |
| **Task Management** | Task assignments, completions |
| **Decision Records** | All decisions made |
| **Audit Logs** | System events |
| **Observability** | Errors, latency, failures |
| **Manual Entry** | Human observations |

---

## Use Cases

### 1. Postmortem Analysis
- Reconstruct incident sequence
- Identify root cause
- Document learnings
- Track remediation

### 2. Dispute Investigation
- Show what happened chronologically
- Link decisions to evidence
- Demonstrate due diligence
- Support compliance response

### 3. Root Cause Analysis
- Correlate events across systems
- Identify causal chains
- Spot contributing factors
- Pinpoint failures

### 4. Training & Learning
- Real-world case studies
- Pattern recognition
- Process improvement

---

## Timeline Visualization

```
┌─────────────────────────────────────────────────────────────────┐
│ INCIDENT TIMELINE: CASE-12345                                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ 09:00 ──● Signal: Fraud alert received (risk_score: 0.87)       │
│         │ Source: fraud-detection-vendor                         │
│         │                                                        │
│ 09:01 ──● Decision: Flag for review (AI Agent)                  │
│         │ DecisionRecord: DR-7890                                │
│         │                                                        │
│ 09:15 ──● Action: Account freeze initiated                      │
│         │ Tool: freeze_account                                   │
│         │                                                        │
│ 09:16 ──● Error: Core banking API timeout                       │
│         │ Retry: 3 attempts                                      │
│         │                                                        │
│ 09:20 ──● Escalation: Sent to human analyst                     │
│         │ Reason: System error during action                     │
│         │                                                        │
│ 09:45 ──● Decision: Manual freeze confirmed (Human)             │
│         │ DecisionRecord: DR-7891                                │
│         │                                                        │
│ 10:30 ──● Resolution: Case closed - fraud confirmed             │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## Retention

| Record Type | Retention | Notes |
|-------------|-----------|-------|
| **Incident Timelines** | 7 years | Or longer for regulatory incidents |
| **Associated Events** | Same as timeline | Linked to timeline lifecycle |

---

## Related Documentation

- [CAF Overview](../README.md)
- [Episodic Memory Store](./README.md)
- [Decision Records](./decision-records.md)
- [Evidence Bundles](./evidence-bundles.md)
- [Hub Observability](../../05-infrastructure/olympus-watch.md)

---

*TODO: Detailed design — event correlation algorithms, timeline assembly automation, visualization UI*

