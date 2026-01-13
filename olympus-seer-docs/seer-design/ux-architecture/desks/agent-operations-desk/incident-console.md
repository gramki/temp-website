# Incident Console

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Desk:** [Agent Operations Desk](./README.md)  
> **Primary Persona:** [Agent Reliability Engineer (ARE)](../../../personas-and-needs/roles.md#5-agent-reliability-engineer-are)

---

## Purpose

The Incident Console enables the **Agent Reliability Engineer (ARE)** ([role definition](../../../personas-and-needs/roles.md#5-agent-reliability-engineer-are)) to manage operational incidents, coordinate response, and track resolution for agent-related issues.

---

## Sections

### Active Incidents

Current incidents requiring attention.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ ACTIVE INCIDENTS                                               [3 Active]   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ ID         │ Severity │ Title                    │ Duration │ Assignee     │
│ ───────────────────────────────────────────────────────────────────────────│
│ INC-2026-45│ 🔴 P1    │ order-validator-03 error │ 2h 15m   │ Jane D.      │
│            │          │ rate spike               │          │              │
│ INC-2026-44│ 🟡 P2    │ compliance-check circuit │ 45m      │ Alex T.      │
│            │          │ breaker open             │          │              │
│ INC-2026-43│ 🟡 P2    │ expense-approver SLA     │ 4h 30m   │ Sam W.       │
│            │          │ degradation              │          │              │
│                                                                             │
│ [Create Incident] [View Resolved] [Analytics]                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Incident Detail

Full incident management view.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ INCIDENT: INC-2026-45                                      Severity: 🔴 P1  │
├─────────────────────────────────────────────────────────────────────────────┤
│ Title: order-validator-03 error rate spike                                  │
│ Status: [Investigating ▼]  Assignee: [Jane D. ▼]                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ TIMELINE                                                                    │
│ ──────────────────────────────────────────────────────────────────────────  │
│ 12:30 │ 🔔 Alert triggered: Error rate > 10%                               │
│ 12:35 │ 📋 Incident created automatically                                   │
│ 12:40 │ 👤 Assigned to Jane D.                                              │
│ 12:45 │ 🔍 Investigation started                                            │
│ 13:00 │ 📝 Note: Root cause identified - bad prompt in v1.3.0               │
│ 13:15 │ 🔄 Rollback initiated to v1.2.9                                     │
│ 13:20 │ ⏳ Rollback in progress...                                          │
│                                                                             │
│ IMPACT                                                                      │
│ ──────────────────────────────────────────────────────────────────────────  │
│ • Affected tasks: 145                                                       │
│ • Failed tasks: 23 (15.8%)                                                  │
│ • Customer impact: Medium (order validation delays)                         │
│ • Estimated time to resolve: 30 minutes                                     │
│                                                                             │
│ ACTIONS TAKEN                                                               │
│ ──────────────────────────────────────────────────────────────────────────  │
│ ☑ Agent paused (12:32)                                                      │
│ ☑ Root cause identified (13:00)                                             │
│ 🔄 Rollback in progress (13:15)                                             │
│ ⬜ Verify resolution                                                        │
│ ⬜ Post-incident review                                                     │
│                                                                             │
│ NOTES                                                                       │
│ ┌─────────────────────────────────────────────────────────────────────────┐│
│ │ Root cause: Prompt change in v1.3.0 introduced ambiguous instruction    ││
│ │ that caused agent to reject valid orders with certain product codes.    ││
│ │ Rolling back to v1.2.9 while AE reviews the prompt change.              ││
│ └─────────────────────────────────────────────────────────────────────────┘│
│                                                                             │
│ [Add Note] [Escalate] [Resolve] [Link to Problem]                           │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Post-Incident Review

Structured PIR template.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ POST-INCIDENT REVIEW: INC-2026-42                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ SUMMARY                                                                     │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Incident: invoice-processor timeout cascade                                 │
│ Duration: 3h 45m │ Severity: P1 │ Resolved: Jan 10, 2026                    │
│                                                                             │
│ ROOT CAUSE                                                                  │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Upstream vendor-lookup service latency increased from 200ms to 5s due to    │
│ database maintenance. Agent retry logic amplified the issue, causing        │
│ cascading timeouts across the invoice processing fleet.                     │
│                                                                             │
│ CONTRIBUTING FACTORS                                                        │
│ ──────────────────────────────────────────────────────────────────────────  │
│ • Aggressive retry policy (5 retries, no backoff)                           │
│ • No circuit breaker on vendor-lookup                                       │
│ • Alerting threshold too high (didn't trigger until 10% error rate)         │
│                                                                             │
│ ACTION ITEMS                                                                │
│ ──────────────────────────────────────────────────────────────────────────  │
│ ☑ Add circuit breaker to vendor-lookup (completed Jan 11)                   │
│ ☑ Implement exponential backoff (completed Jan 12)                          │
│ 🔄 Lower alerting threshold to 2% (in progress)                             │
│ ⬜ Add vendor-lookup to dependency monitoring                               │
│                                                                             │
│ [Export PIR] [Create Problem Record] [Schedule Follow-up]                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Features

- **Automated incident creation from alerts**
- **Structured incident management workflow**
- **Timeline tracking with audit trail**
- **Impact assessment**
- **Post-incident review templates**
- **Problem linking for recurring issues**

---

## OPDA Contribution

| OPDA | Console Contribution |
|------|---------------------|
| **Observable** | Incident visibility and tracking |
| **Predictable** | PIR drives preventive actions |
| **Directable** | Incident response coordination |
| **Authority Enforceable** | N/A (operational focus) |

---

*Status: 🟡 Draft — Specification complete, implementation TBD*
