# Feedback Promotion

> **Status:** 🟡 Draft

---

## Overview

**Promotion** is the act of sending feedback from a source workbench (STAGING, PROD) to a development workbench. Promoters are personas operating in non-development workbenches who identify issues or opportunities during their work.

---

## Promotion Flow

```
Source Workbench                 Feedback Services              Development WB
      │                                │                              │
      ├─── Promote Feedback ──────────▶│                              │
      │    (type, content, lineage)    │                              │
      │                                │                              │
      │                                ├─── Validate ─────────────────│
      │                                │    • Source workbench exists │
      │                                │    • Dev WB configured       │
      │                                │    • Promoter authorized     │
      │                                │                              │
      │                                ├─── Create Entity ───────────▶│
      │                                │    • In dev WB namespace     │
      │                                │    • Status: pending         │
      │                                │                              │
      │                                ├─── Notify APO ──────────────▶│
      │                                │    "New feedback received"   │
      │                                │                              │
      │◀── Confirmation ───────────────┤                              │
      │    (feedback_id, status)       │                              │
      │                                │                              │
```

---

## Workbench Configuration

### Source Workbench (Production)

```yaml
apiVersion: hub.olympus.io/v1
kind: Workbench
metadata:
  name: dispute-ops-prod-apac
spec:
  dev_lifecycle_stage: PROD
  
  feedback:
    # Target development workbench
    development_workbench_ref: dispute-ops-dev
    
    # Enable/disable feedback promotion
    enabled: true
    
    # Optional: restrict promoters
    allowed_promoters:
      - role: agent
      - role: supervisor
      - role: auditor
    
    # Optional: require approval
    require_supervisor_approval: false
```

### Development Workbench (Target)

```yaml
apiVersion: hub.olympus.io/v1
kind: Workbench
metadata:
  name: dispute-ops-dev
spec:
  dev_lifecycle_stage: DEV
  
  feedback:
    # Accept feedback from linked workbenches
    accept_feedback: true
    
    # APO for inbox
    inbox_owner: apo@acme.com
    
    # Notification settings
    notifications:
      on_new_feedback:
        - user: apo@acme.com
        - group: dev-team
```

---

## Promoter Authorization

| Promoter Role | Can Promote | Types Allowed |
|---------------|-------------|---------------|
| Agent | From Agent Desk | Bug, Observation |
| Supervisor | From Supervisor Desk | Bug, Issue, Observation, Suggestion |
| Auditor | From Auditor Desk | Observation, Learning |
| Developer (staging) | From Dev Desk | Bug |
| APO (production) | From APO Desk | All types |

---

## Promotion Interface

### Agent Desk Example

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  PROMOTE FEEDBACK                                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Type: [Problem ▼]        Subtype: [Bug ▼]        Severity: [High ▼]        │
│                                                                              │
│  Title:                                                                      │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │ Escalation not triggering for priority disputes                       │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│  Description:                                                               │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │ When a dispute is marked as priority, the escalation should          │  │
│  │ trigger at the 2-hour mark but is not firing. I've seen this in      │  │
│  │ REQ-1234 and REQ-5678.                                                │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│  Related Entities (auto-populated):                                         │
│  ☑ Current Request: REQ-1234                                               │
│  ☑ Current Task: TASK-5678                                                 │
│  ☑ Scenario: standard-dispute                                              │
│                                                                              │
│  Attachments:                                                               │
│  [+ Add Screenshot]  [+ Add File]                                           │
│                                                                              │
│  Target: dispute-ops-dev (Development Workbench)                            │
│                                                                              │
│  [Cancel]                                              [Promote Feedback]   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Lineage Auto-Population

When promoting from a task context:

| Field | Source |
|-------|--------|
| `source_workbench_id` | Current workbench |
| `source_workbench_stage` | Current stage |
| `promoted_by` | Current user |
| `promoted_from_desk` | Current desk |
| `related_entities.requests` | Current request (if in task context) |
| `related_entities.tasks` | Current task (if in task context) |
| `related_entities.scenarios` | Current scenario |

---

## Validation Rules

| Rule | Error Message |
|------|---------------|
| Source WB has `feedback.enabled: true` | "Feedback promotion is disabled for this workbench" |
| Source WB has `development_workbench_ref` | "No development workbench configured" |
| Development WB exists | "Development workbench not found" |
| Development WB has `accept_feedback: true` | "Development workbench not accepting feedback" |
| Promoter role in `allowed_promoters` | "You are not authorized to promote feedback" |
| Title is not empty | "Title is required" |
| Description is not empty | "Description is required" |

---

## Post-Promotion

After successful promotion:

1. **Confirmation** — Promoter sees confirmation with feedback ID
2. **Tracking** — Feedback appears in "My Promoted Feedback" list
3. **Notification** — APO receives notification in development workbench
4. **Status Updates** — Promoter receives updates when status changes

---

## APIs

### REST Channels

**Agent/Supervisor/Auditor Channels:**

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/feedback` | Promote new feedback |
| `POST` | `/problems` | Promote new problem |
| `GET` | `/feedback/promoted` | List promoted feedback |
| `GET` | `/feedback/promoted/{id}` | Get promoted feedback status |

### MCP Channels

| Tool | Description |
|------|-------------|
| `promote_feedback` | Promote feedback/suggestion |
| `promote_problem` | Promote bug/issue/limitation |
| `list_promoted_feedback` | List my promoted items |
| `get_feedback_status` | Check status of promoted item |

---

## Related Documentation

- [Feedback Entities](./feedback-entities.md) — Entity schemas
- [Feedback Inbox](./feedback-inbox.md) — APO review process
- [Agent Desk](../../06-ux-architecture/tenant-domain/agent-desk.md)
- [Supervisor Desk](../../06-ux-architecture/tenant-domain/supervisor-desk.md)

