# Feedback Entities

> **Status:** 🟡 Draft

---

## Overview

Feedback Services manages two top-level entity types: **Problems** (defects requiring remediation) and **Feedback** (observations for improvement). Each has subtypes with appropriate severity levels.

---

## Entity Hierarchy

```
Feedback Entity
├── Problem
│   ├── Bug
│   ├── Issue
│   └── Critical Limitation
│
└── Feedback
    ├── Observation
    ├── Suggestion
    └── Learning
```

---

## Problem Schema

```yaml
apiVersion: hub.olympus.io/v1
kind: Problem
metadata:
  id: prob-12345
  namespace: acme-bank
spec:
  # Classification
  type: problem
  subtype: bug                   # bug | issue | critical_limitation
  severity: high                 # critical | high | medium | low
  
  # Content
  title: "Escalation not triggering for priority disputes"
  description: |
    When a dispute is marked as priority, the escalation should trigger
    at the 2-hour mark but is not firing. Noticed in multiple requests.
  
  # Attachments (optional)
  attachments:
    - type: screenshot
      url: "s3://..."
    - type: log
      url: "s3://..."
  
  # Lineage
  lineage:
    source_workbench_id: dispute-ops-prod-apac
    source_workbench_stage: PROD
    
    promoted_by: supervisor@acme.com
    promoted_at: "2026-01-09T10:30:00Z"
    promoted_from_desk: supervisor-desk
    
    related_entities:
      requests:
        - req-abc
        - req-def
      tasks:
        - task-123
      scenarios:
        - standard-dispute
    
    caf_records:
      - record_type: EscalationRecord
        record_id: esc-456

  # Target
  development_workbench_id: dispute-ops-dev

status:
  state: pending                 # pending | in_review | accepted | rejected | routed | resolved
  
  updated_at: "2026-01-09T10:30:00Z"
  updated_by: null
  
  # Review (populated by APO)
  review:
    reviewed_by: null
    reviewed_at: null
    decision: null               # accept | reject | route
    notes: null
  
  # Routing (if routed)
  routing:
    routed_to: null              # user_id or role
    routed_at: null
  
  # Resolution (if resolved)
  resolution:
    resolved_by: null
    resolved_at: null
    scenario_version: null
    release_notes: null
    fix_reference: null
```

---

## Feedback Schema

```yaml
apiVersion: hub.olympus.io/v1
kind: Feedback
metadata:
  id: fb-67890
  namespace: acme-bank
spec:
  # Classification
  type: feedback
  subtype: suggestion            # observation | suggestion | learning
  severity: low                  # medium | low
  
  # Content
  title: "Add document preview in task solver"
  description: |
    Agents currently have to download and open documents externally.
    An inline preview would save 2-3 minutes per task.
  
  # Lineage
  lineage:
    source_workbench_id: dispute-ops-prod-apac
    source_workbench_stage: PROD
    
    promoted_by: agent@acme.com
    promoted_at: "2026-01-09T11:00:00Z"
    promoted_from_desk: agent-desk
    
    related_entities:
      requests: []
      tasks: []
      scenarios:
        - standard-dispute

  # Target
  development_workbench_id: dispute-ops-dev

status:
  state: pending
  # ... same as Problem
```

---

## Problem Subtypes

### Bug

Implementation defects that cause incorrect behavior.

| Severity | Criteria | Examples |
|----------|----------|----------|
| **Critical** | System unusable, data loss | Crash, data corruption |
| **High** | Major feature broken | Escalation not firing |
| **Medium** | Feature degraded | Slow performance |
| **Low** | Minor cosmetic | UI alignment issue |

### Issue

Operational constraints or deviations from expected behavior.

| Severity | Criteria | Examples |
|----------|----------|----------|
| **High** | Blocking operations | SLA thresholds too tight |
| **Medium** | Impacting efficiency | Queue configuration suboptimal |
| **Low** | Minor inconvenience | Notification timing off |

### Critical Limitation

Design or capability gaps blocking operations.

| Severity | Criteria | Examples |
|----------|----------|----------|
| **Critical** | Cannot handle required case | Multi-currency not supported |

---

## Feedback Subtypes

### Observation

Behavioral patterns or anomalies noticed during operations.

| Severity | Criteria | Examples |
|----------|----------|----------|
| **Medium** | Pattern affecting outcomes | High reject rate on Fridays |
| **Low** | Interesting but not urgent | Unusual customer behavior |

### Suggestion

Improvement ideas from operational experience.

| Severity | Criteria | Examples |
|----------|----------|----------|
| **Low** | Nice to have | Document preview, keyboard shortcuts |

### Learning

Validated insights worth incorporating into process or automation.

| Severity | Criteria | Examples |
|----------|----------|----------|
| **Medium** | Actionable insight | "Priority disputes need special handling" |
| **Low** | General insight | "Customers prefer SMS notifications" |

---

## Lineage Information

Every feedback item includes immutable lineage:

| Field | Description | Required |
|-------|-------------|----------|
| `source_workbench_id` | Originating workbench | Yes |
| `source_workbench_stage` | DEV, STAGING, PROD | Yes |
| `promoted_by` | User who promoted | Yes |
| `promoted_at` | Promotion timestamp | Yes |
| `promoted_from_desk` | Desk used to promote | Yes |
| `related_entities.requests` | Related request IDs | Optional |
| `related_entities.tasks` | Related task IDs | Optional |
| `related_entities.scenarios` | Related scenario names | Optional |
| `caf_records` | Related CAF record references | Optional |

---

## Related Documentation

- [Feedback Promotion](./feedback-promotion.md) — How entities are promoted
- [Feedback Inbox](./feedback-inbox.md) — APO review process
- [Resolution Tracking](./resolution-tracking.md) — Resolution lifecycle

