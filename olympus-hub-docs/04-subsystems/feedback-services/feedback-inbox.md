# Feedback Inbox

> **Status:** 🟡 Draft

---

## Overview

The **Feedback Inbox** is the APO's queue of incoming feedback from linked production workbenches. APO reviews, triages, and acts on each item.

---

## Inbox Structure

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  PRODUCTION FEEDBACK INBOX                                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  [Filters]                                                                  │
│  Source: [All ▼]  Type: [All ▼]  Severity: [All ▼]  Status: [Pending ▼]    │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │ 🔴 BUG | HIGH | Escalation not triggering for priority disputes       │  │
│  │    From: dispute-ops-prod-apac | By: supervisor@acme.com             │  │
│  │    Received: 2 hours ago | Status: Pending                           │  │
│  │    Related: REQ-1234, TASK-5678 | Scenario: standard-dispute         │  │
│  ├───────────────────────────────────────────────────────────────────────┤  │
│  │ 🟡 ISSUE | MEDIUM | SLA thresholds too aggressive for EMEA timezone  │  │
│  │    From: dispute-ops-prod-emea | By: supervisor@acme.eu              │  │
│  │    Received: 1 day ago | Status: In Review                           │  │
│  ├───────────────────────────────────────────────────────────────────────┤  │
│  │ 💡 SUGGESTION | LOW | Add document preview in task solver            │  │
│  │    From: dispute-ops-staging | By: agent@acme.com                    │  │
│  │    Received: 3 days ago | Status: Accepted                           │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│  [Accept] [Reject] [Route to PA] [Route to Dev] [Promote to Idea]          │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Inbox Filters

| Filter | Options |
|--------|---------|
| **Source** | All, specific workbench IDs |
| **Type** | All, Problem, Feedback |
| **Subtype** | Bug, Issue, Critical Limitation, Observation, Suggestion, Learning |
| **Severity** | Critical, High, Medium, Low |
| **Status** | Pending, In Review, Accepted, Rejected, Routed, Resolved |
| **Date Range** | Last 7 days, 30 days, 90 days, Custom |

---

## Inbox Sorting

| Sort By | Default |
|---------|---------|
| Severity (Critical first) | ✓ |
| Received date (newest first) | |
| Source workbench | |
| Type | |

---

## APO Actions

### Accept

Mark feedback as valid and to be addressed.

```yaml
action: accept
feedback_id: fb-12345
notes: "Valid bug, adding to sprint backlog"
```

**Effects:**
- Status → `accepted`
- Promoter notified
- Added to backlog (if configured)

### Reject

Mark feedback as invalid or will not address.

```yaml
action: reject
feedback_id: fb-12345
reason: "Duplicate of existing issue"
notes: "See ISSUE-999 for tracking"
```

**Effects:**
- Status → `rejected`
- Promoter notified with reason

### Route to PA

Send to Process Architect for normative review.

```yaml
action: route
feedback_id: fb-12345
route_to: pa@acme.com
route_type: process_architect
notes: "Needs SOP update"
```

**Effects:**
- Status → `routed`
- PA notified
- Promoter notified

### Route to Developer

Send to Developer for technical investigation.

```yaml
action: route
feedback_id: fb-12345
route_to: developer@acme.com
route_type: developer
notes: "Investigate escalation timing logic"
```

**Effects:**
- Status → `routed`
- Developer notified
- Promoter notified

### Promote to Idea

Convert suggestion to Idea for Ideation workflow.

```yaml
action: promote_to_idea
feedback_id: fb-67890
```

**Effects:**
- Status → `accepted` (feedback resolved as promoted)
- New Idea created with lineage
- Promoter notified

---

## Detail View

When APO opens a feedback item:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  FEEDBACK DETAIL                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  🔴 BUG | HIGH                                                              │
│  Escalation not triggering for priority disputes                            │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  DESCRIPTION                                                                │
│  When a dispute is marked as priority, the escalation should trigger at    │
│  the 2-hour mark but is not firing. Noticed in REQ-1234 and REQ-5678.      │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  LINEAGE                                                                    │
│  Source: dispute-ops-prod-apac (PROD)                                       │
│  Promoted by: supervisor@acme.com                                           │
│  Promoted at: 2026-01-09 10:30 UTC                                          │
│  Promoted from: Supervisor Desk                                             │
│                                                                              │
│  Related:                                                                   │
│  • Requests: [REQ-1234] [REQ-5678]                                         │
│  • Tasks: [TASK-123]                                                       │
│  • Scenario: standard-dispute                                               │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  ATTACHMENTS                                                                │
│  [📷 screenshot-1.png]  [📄 log-snippet.txt]                               │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  [Accept] [Reject] [Route to PA] [Route to Dev] [Back to Inbox]            │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Inbox Metrics

APO Dashboard includes inbox metrics:

| Metric | Description |
|--------|-------------|
| **Pending Count** | Items awaiting review |
| **Average Time to Acknowledge** | Pending → In Review |
| **Average Time to Resolve** | Pending → Resolved |
| **By Source** | Distribution by source workbench |
| **By Type** | Distribution by Problem/Feedback type |

---

## APIs

### REST (Creator Channel - APO)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/feedback/inbox` | List inbox items |
| `GET` | `/feedback/inbox/{id}` | Get item details |
| `POST` | `/feedback/inbox/{id}/accept` | Accept item |
| `POST` | `/feedback/inbox/{id}/reject` | Reject item |
| `POST` | `/feedback/inbox/{id}/route` | Route to PA/Dev |
| `POST` | `/feedback/inbox/{id}/promote-to-idea` | Promote to Idea |

### MCP (Creator Channel - APO)

| Tool | Description |
|------|-------------|
| `list_feedback_inbox` | List inbox with filters |
| `get_feedback_details` | Get item details |
| `accept_feedback` | Accept item |
| `reject_feedback` | Reject with reason |
| `route_feedback` | Route to PA or Developer |
| `promote_feedback_to_idea` | Convert to Idea |

---

## Related Documentation

- [Feedback Entities](./feedback-entities.md) — Entity schemas
- [Feedback Promotion](./feedback-promotion.md) — How items arrive
- [Resolution Tracking](./resolution-tracking.md) — Post-acceptance flow
- [Automation Product Desk](../../06-ux-architecture/tenant-domain/automation-product-desk.md)

