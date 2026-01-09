# Production Feedback Loop Journey

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-09

This journey describes how operational feedback flows from production workbenches back to development for incorporation into future releases.

---

## Overview

| Aspect | Description |
|--------|-------------|
| **Purpose** | Enable structured feedback from Run stage to Evolve stage |
| **Scope** | Cross-workbench (production → development) |
| **Primary Personas** | Supervisor, Agent, APO, Process Architect, Developer |
| **ADR** | [ADR-0081: Production Feedback Loop](../../decision-logs/0081-production-feedback-loop.md) |

---

## Journey Context

The **Automation Lifecycle** follows: Design → Build → Deploy → Run → **Evolve**.

This journey covers the **Evolve** stage, where learnings from production inform the next design iteration:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        AUTOMATION LIFECYCLE                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   DESIGN ───▶ BUILD ───▶ DEPLOY ───▶ RUN ───▶ EVOLVE                        │
│     ▲                                           │                            │
│     │                                           │                            │
│     └───────────────────────────────────────────┘                            │
│                  Production Feedback Loop                                    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Personas Involved

| Persona | Role in Journey | Workbench |
|---------|-----------------|-----------|
| **Agent** | Identify and promote bugs, observations | Production |
| **Supervisor** | Identify and promote issues, observations | Production |
| **APO** | Review, triage, and resolve feedback | Development |
| **Process Architect** | Receive routed feedback, update normative specs | Development |
| **Developer** | Receive routed feedback, implement fixes | Development |

---

## Journey Phases

### Phase 1: Issue Identification (Production Workbench)

**Location:** Production Workbench (STAGING, PROD)  
**Actors:** Agent, Supervisor

During normal operations, issues and observations are identified:

```
PRODUCTION WORKBENCH
────────────────────

Agent (completing tasks)              Supervisor (monitoring operations)
       │                                       │
       │ ┌─────────────────────────┐          │ ┌─────────────────────────┐
       │ │ "This workflow failed   │          │ │ "SLA thresholds are    │
       │ │  unexpectedly when..."  │          │ │  too aggressive for... │
       │ └─────────────────────────┘          │ └─────────────────────────┘
       │                                       │
       ▼                                       ▼
  [Local Issue]                          [Local Issue]
```

#### Issue Categories

| Category | Type | Subtype | Example |
|----------|------|---------|---------|
| **Implementation Defect** | Problem | Bug | "Escalation not triggering" |
| **Operational Constraint** | Problem | Issue | "SLA too tight for EMEA timezone" |
| **Capability Gap** | Problem | Critical Limitation | "Cannot handle multi-currency" |
| **Pattern Noticed** | Feedback | Observation | "High reject rate on Fridays" |
| **Improvement Idea** | Feedback | Suggestion | "Add document preview" |

---

### Phase 2: Feedback Promotion (Production Workbench)

**Location:** Production Workbench  
**Actors:** Agent, Supervisor

The persona decides to promote feedback to development:

```
Agent Desk / Supervisor Desk
────────────────────────────

┌─────────────────────────────────────────────────────────────────────────────┐
│  PROMOTE FEEDBACK TO DEVELOPMENT                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Type: [Problem ▼]     Subtype: [Bug ▼]     Severity: [High ▼]              │
│                                                                              │
│  Title: Escalation not triggering for priority disputes                     │
│                                                                              │
│  Description:                                                                │
│  When a dispute is marked as priority, the escalation should trigger at     │
│  the 2-hour mark but is not firing. Noticed in REQ-1234 and REQ-5678.       │
│                                                                              │
│  Related Entities (auto-populated):                                          │
│  ☑ Request: REQ-1234                                                        │
│  ☑ Task: TASK-5678                                                          │
│  ☑ Scenario: standard-dispute                                               │
│                                                                              │
│  Target: dispute-ops-dev (Development Workbench)                            │
│                                                                              │
│  [Cancel]                                              [Promote Feedback]   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### What Happens on Promote

1. Feedback item created with full lineage
2. Status set to `pending`
3. Routed to development workbench inbox
4. Promoter can track status via "My Promoted Feedback"

---

### Phase 3: Inbox Review (Development Workbench)

**Location:** Development Workbench  
**Actor:** APO

The APO reviews incoming feedback in the Production Feedback Inbox:

```
Automation Product Desk → Production Feedback Inbox
───────────────────────────────────────────────────

┌─────────────────────────────────────────────────────────────────────────────┐
│  PRODUCTION FEEDBACK INBOX                                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  [Filter: All Sources ▼] [Type: All ▼] [Severity: All ▼] [Status: Pending ▼]│
│                                                                              │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │ 🔴 BUG | Escalation not triggering for priority disputes              │  │
│  │    From: dispute-ops-prod-apac | By: supervisor@acme.com             │  │
│  │    Severity: High | Status: Pending | 2 hours ago                    │  │
│  ├───────────────────────────────────────────────────────────────────────┤  │
│  │ 🟡 ISSUE | SLA thresholds too aggressive for EMEA timezone           │  │
│  │    From: dispute-ops-prod-emea | By: supervisor@acme.eu              │  │
│  │    Severity: Medium | Status: In Review | 1 day ago                  │  │
│  ├───────────────────────────────────────────────────────────────────────┤  │
│  │ 💡 SUGGESTION | Add document preview in task solver                  │  │
│  │    From: dispute-ops-staging | By: agent@acme.com                    │  │
│  │    Severity: Low | Status: Accepted | 3 days ago                     │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│  [Accept] [Reject] [Route to PA] [Route to Dev] [Link to Backlog]           │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### APO Triage Decisions

| Decision | When to Use | Next Step |
|----------|-------------|-----------|
| **Accept** | Valid issue, will address | Add to backlog, notify promoter |
| **Reject** | Not valid, won't fix, or duplicate | Provide reason, notify promoter |
| **Route to PA** | Requires normative spec change | PA reviews and updates SOPs |
| **Route to Developer** | Requires code fix | Developer investigates |

---

### Phase 4: Resolution (Development Workbench)

**Location:** Development Workbench  
**Actors:** APO, Process Architect, Developer

After investigation and fix:

```
APO                           Developer                    Version Control
 │                                │                              │
 │                                ├── Investigate Bug ──────────▶│
 │                                │                              │
 │                                ├── Implement Fix ────────────▶│
 │                                │                              │
 │                                ├── Create PR ────────────────▶│
 │                                │                              │
 │                                │◀── Merge to v1.4.0 ──────────┤
 │                                │                              │
 │◀── Notify: Fix Ready ─────────┤                              │
 │                                │                              │
 ├── Mark Resolved ──────────────▶                               │
 │    (link to v1.4.0)                                           │
 │                                                                │
```

#### Resolution Record

```json
{
  "resolution": {
    "scenario_version": "1.4.0",
    "release_notes": "Fixed escalation trigger timing for priority disputes",
    "fix_reference": "PR-456",
    "resolved_by": "developer@acme.com",
    "resolved_at": "2026-01-15T14:00:00Z",
    "deployment_date": "2026-01-16"
  }
}
```

---

### Phase 5: Status Reflection (Production Workbench)

**Location:** Production Workbench  
**Actors:** Original Promoter, Supervisor

The resolution is reflected back to the source workbench:

```
Production Workbench → Supervisor Desk → Feedback Console
──────────────────────────────────────────────────────────

PROMOTED TO DEVELOPMENT
───────────────────────

  ┌───────────────────────────────────────────────────────────────────────┐
  │ ✅ Escalation not triggering for priority | RESOLVED                  │
  │    Promoted: 1 week ago | Resolved: 2 days ago                       │
  │    Fix: v1.4.0 - "Fixed escalation trigger timing"                   │
  │    Deployment: 2026-01-16                                            │
  │    [View Resolution Details]                                          │
  └───────────────────────────────────────────────────────────────────────┘
```

#### Notification to Promoter

```
Subject: Feedback Resolved: Escalation not triggering for priority disputes

Your feedback has been resolved!

Resolution:
- Fixed in scenario version 1.4.0
- "Fixed escalation trigger timing for priority disputes"
- Deployment scheduled: 2026-01-16

View details: [Link to feedback item]
```

---

## Journey Diagram (End-to-End)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PRODUCTION FEEDBACK LOOP JOURNEY                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  PRODUCTION WORKBENCH                    DEVELOPMENT WORKBENCH              │
│                                                                              │
│  ┌─────────────────────┐                ┌─────────────────────┐             │
│  │ 1. IDENTIFY         │                │ 3. REVIEW           │             │
│  │    Agent/Supervisor │                │    APO reviews      │             │
│  │    notices issue    │                │    in inbox         │             │
│  └──────────┬──────────┘                └──────────┬──────────┘             │
│             │                                      │                         │
│             ▼                                      ▼                         │
│  ┌─────────────────────┐                ┌─────────────────────┐             │
│  │ 2. PROMOTE          │   ─────────▶   │ 4. TRIAGE           │             │
│  │    Fill details     │   Feedback     │    Accept/Reject/   │             │
│  │    Submit           │   with lineage │    Route            │             │
│  └─────────────────────┘                └──────────┬──────────┘             │
│                                                    │                         │
│                                                    ▼                         │
│                                         ┌─────────────────────┐             │
│                                         │ 5. FIX              │             │
│                                         │    PA/Developer     │             │
│                                         │    implements       │             │
│                                         └──────────┬──────────┘             │
│                                                    │                         │
│                                                    ▼                         │
│  ┌─────────────────────┐                ┌─────────────────────┐             │
│  │ 7. NOTIFICATION     │   ◀─────────   │ 6. RESOLVE          │             │
│  │    Status updated   │   Resolution   │    APO marks done   │             │
│  │    Promoter alerted │   reflected    │    Links to version │             │
│  └─────────────────────┘                └─────────────────────┘             │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Success Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| **Feedback Volume** | Items promoted per week | Healthy signal (not zero) |
| **Time to Acknowledge** | Pending → In Review | < 24 hours |
| **Time to Resolve** | Pending → Resolved (for accepted items) | < 2 weeks (varies by severity) |
| **Resolution Rate** | Accepted items that reach Resolved | > 90% |
| **Rejection Rate** | Items rejected (with valid reason) | < 30% |

---

## Common Patterns

### Pattern 1: Bug → Quick Fix

```
Agent finds bug → Promote → APO accepts → Developer fixes → Resolve
Timeline: 3-5 days
```

### Pattern 2: Issue → Normative Change

```
Supervisor raises issue → Promote → APO routes to PA → PA updates SOP → Resolve
Timeline: 1-2 weeks
```

### Pattern 3: Suggestion → Backlog

```
Agent suggests improvement → Promote → APO accepts → Adds to backlog → Resolve later
Timeline: Weeks to months
```

### Pattern 4: Observation → Enterprise Learning

```
Multiple observations → Pattern detected → Escalate to Enterprise Learning
(Outside scope of this journey, handled by CAF Enterprise Learning Services)
```

---

## Edge Cases

### Duplicate Feedback

If multiple promoters report the same issue:

1. APO links duplicates to the original
2. All promoters notified when resolved
3. Each promoter sees their item as "Resolved (duplicate of fb-xxx)"

### Cross-Workbench Feedback

If issue affects multiple production workbenches:

1. APO may receive from multiple sources
2. Resolution applies to all (single fix)
3. All sources notified on resolution

### Rejected Feedback - Disagreement

If promoter disagrees with rejection:

1. Promoter can re-promote with additional evidence
2. APO reviews again
3. If still rejected, escalate to Administrator

---

## Related Documentation

- [Production Feedback Concept](../../02-system-design/implementation-concepts/production-feedback.md)
- [ADR-0081: Production Feedback Loop](../../decision-logs/0081-production-feedback-loop.md)
- [Automation Lifecycle Journey](./automation-lifecycle.md)
- [Automation Product Desk](../../06-ux-architecture/tenant-domain/automation-product-desk.md)
- [Supervisor Desk](../../06-ux-architecture/tenant-domain/supervisor-desk.md)

