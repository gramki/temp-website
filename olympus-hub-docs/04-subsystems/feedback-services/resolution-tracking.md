# Resolution Tracking

> **Status:** 🟡 Draft

---

## Overview

**Resolution Tracking** manages the lifecycle from accepted feedback to resolved status, including fix implementation and reflection back to the source workbench.

---

## Resolution Flow

```
Accepted Feedback           Developer/PA              APO
      │                          │                     │
      ├─── Investigate ─────────▶│                     │
      │                          │                     │
      │                          ├─── Implement Fix    │
      │                          │                     │
      │                          ├─── PR Merged ──────▶│
      │                          │                     │
      │                          │                     ├─── Link Fix
      │                          │                     │
      │                          │                     ├─── Mark Resolved
      │                          │                     │
      │◀──────────── Status Reflected ─────────────────┤
      │                                                │
```

---

## Resolution Schema

```yaml
resolution:
  # Basic info
  resolved_by: developer@acme.com
  resolved_at: "2026-01-15T14:00:00Z"
  
  # Fix details
  fix:
    scenario_version: "1.4.0"
    release_notes: "Fixed escalation trigger timing for priority disputes"
    fix_reference: "PR-456"
    commit_hash: "abc123"
  
  # Deployment
  deployment:
    deployed_to:
      - workbench_id: dispute-ops-staging
        deployed_at: "2026-01-15T16:00:00Z"
      - workbench_id: dispute-ops-prod-apac
        deployed_at: "2026-01-16T10:00:00Z"
    target_deployment_date: "2026-01-16"
  
  # Verification
  verification:
    verified_by: supervisor@acme.com
    verified_at: "2026-01-16T14:00:00Z"
    verification_notes: "Tested with priority dispute, escalation fired correctly"
```

---

## Resolution Lifecycle

```
                    ┌──────────────┐
                    │   ACCEPTED   │
                    └──────┬───────┘
                           │
                           │ Developer/PA assigned
                           ▼
                    ┌──────────────┐
                    │ IN_PROGRESS  │
                    └──────┬───────┘
                           │
                           │ Fix ready
                           ▼
                    ┌──────────────┐
                    │ FIX_READY    │
                    └──────┬───────┘
                           │
                           │ APO links fix
                           ▼
                    ┌──────────────┐
                    │  RESOLVED    │
                    └──────┬───────┘
                           │
                           │ Promoter verifies (optional)
                           ▼
                    ┌──────────────┐
                    │  VERIFIED    │
                    └──────────────┘
```

| State | Description | Owner |
|-------|-------------|-------|
| `accepted` | Feedback accepted, awaiting work | APO |
| `in_progress` | Work underway | Developer/PA |
| `fix_ready` | Fix implemented, awaiting linkage | Developer |
| `resolved` | APO linked fix to feedback | APO |
| `verified` | Promoter verified fix works | Promoter (optional) |

---

## Linking a Fix

APO links fix to feedback:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  RESOLVE FEEDBACK                                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Feedback: Escalation not triggering for priority disputes                  │
│  Status: Accepted                                                           │
│                                                                              │
│  ─────────────────────────────────────────────────────────────────────────  │
│                                                                              │
│  Scenario Version: [ 1.4.0                    ▼ ]                           │
│                                                                              │
│  Release Notes:                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │ Fixed escalation trigger timing for priority disputes                 │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│  Fix Reference (PR/Commit): [ PR-456 ]                                      │
│                                                                              │
│  Target Deployment Date: [ 2026-01-16 ]                                     │
│                                                                              │
│  [Cancel]                                              [Mark Resolved]      │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Reflection to Source

When feedback is resolved, status is reflected to source workbench:

### Notification to Promoter

```
Subject: Feedback Resolved: Escalation not triggering for priority disputes

Your feedback has been resolved!

Resolution:
- Fixed in scenario version 1.4.0
- "Fixed escalation trigger timing for priority disputes"
- Deployment scheduled: 2026-01-16

View details: [Link]

---
Original feedback promoted: 2026-01-09
From: dispute-ops-prod-apac
```

### Source Workbench Update

In the promoter's "Promoted Feedback" list:

```
┌───────────────────────────────────────────────────────────────────────┐
│ ✅ Escalation not triggering for priority | RESOLVED                  │
│    Promoted: 1 week ago | Resolved: 2 days ago                       │
│    Fix: v1.4.0 - "Fixed escalation trigger timing"                   │
│    Deployment: 2026-01-16                                            │
│    [View Resolution Details] [Verify Fix]                            │
└───────────────────────────────────────────────────────────────────────┘
```

---

## Verification (Optional)

Promoter can verify the fix works in production:

```yaml
action: verify
feedback_id: fb-12345
verification_notes: "Tested with priority dispute, escalation fired correctly"
```

**Effects:**
- Status → `verified`
- APO and Developer notified
- Feedback fully closed

---

## Bulk Resolution

For related issues fixed by same release:

```yaml
action: bulk_resolve
feedback_ids:
  - fb-12345
  - fb-12346
  - fb-12347
resolution:
  scenario_version: "1.4.0"
  release_notes: "Escalation timing overhaul"
  fix_reference: "PR-456"
```

---

## Resolution Metrics

| Metric | Description |
|--------|-------------|
| **Time to Resolve** | Accepted → Resolved |
| **Resolution Rate** | Accepted items that reach Resolved |
| **Verification Rate** | Resolved items verified by promoter |
| **By Fix Type** | Bug vs Issue vs Limitation |
| **By Source** | Distribution by source workbench |

---

## APIs

### REST (Creator Channel)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/feedback/{id}/resolve` | Mark as resolved |
| `POST` | `/feedback/{id}/verify` | Promoter verifies |
| `POST` | `/feedback/bulk-resolve` | Bulk resolve |
| `GET` | `/feedback/{id}/resolution` | Get resolution details |

### MCP (Creator Channel)

| Tool | Description |
|------|-------------|
| `resolve_feedback` | Link fix and resolve |
| `verify_feedback_resolution` | Promoter verifies |
| `get_resolution_details` | Get resolution info |

---

## Related Documentation

- [Feedback Inbox](./feedback-inbox.md) — APO review process
- [Feedback Promotion](./feedback-promotion.md) — How items arrive
- [Automation Product Desk](../../06-ux-architecture/tenant-domain/automation-product-desk.md)

