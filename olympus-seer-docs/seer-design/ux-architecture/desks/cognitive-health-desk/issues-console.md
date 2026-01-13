# Issues Console

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Desk:** [Cognitive Health Desk](./README.md)  
> **Primary Persona:** [Cognitive Operations Specialist (COS)](../../../personas-and-needs/roles.md#6-cognitive-operations-specialist-cos)

---

## Purpose

The Issues Console enables the **Cognitive Operations Specialist (COS)** ([role definition](../../../personas-and-needs/roles.md#6-cognitive-operations-specialist-cos)) to manage cognitive quality issues, coordinate with AE/CSA for resolution, and track issue lifecycle.

---

## Sections

### Issue Queue

Active cognitive issues awaiting attention.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ COGNITIVE ISSUE QUEUE                                       [8 Open Issues] │
├─────────────────────────────────────────────────────────────────────────────┤
│ Priority: [All ▼]  Agent: [All ▼]  Type: [All ▼]                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ ID         │ Agent              │ Type           │ Priority │ Status       │
│ ───────────────────────────────────────────────────────────────────────────│
│ COG-2026-23│ order-validator-03 │ Reasoning Loop │ 🔴 P1    │ Investigating│
│ COG-2026-22│ customer-svc-05    │ Hallucination  │ 🔴 P1    │ Assigned AE  │
│ COG-2026-21│ invoice-proc-02    │ Drift          │ 🟡 P2    │ Under Review │
│ COG-2026-20│ expense-apprvr     │ Low Confidence │ 🟡 P2    │ Monitoring   │
│ COG-2026-19│ data-enricher-01   │ Anti-Pattern   │ 🟢 P3    │ Backlog      │
│                                                                             │
│ [Create Issue] [Bulk Assign] [Export]                                       │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Issue Detail

Full issue management view.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ ISSUE: COG-2026-23                                         Priority: 🔴 P1  │
├─────────────────────────────────────────────────────────────────────────────┤
│ Title: Reasoning loop in order-validator-03                                 │
│ Type: Reasoning Loop  │  Agent: order-validator-03  │  Status: Investigating│
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ DESCRIPTION                                                                 │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Agent repeatedly cycles through validation steps without reaching a         │
│ decision. Occurs in approximately 8% of requests with certain product       │
│ combinations. Agent hits iteration limit and task times out.                │
│                                                                             │
│ EVIDENCE                                                                    │
│ ──────────────────────────────────────────────────────────────────────────  │
│ • 12 occurrences in last 24 hours                                           │
│ • Sample traces: req-2026-0112-a, req-2026-0112-b, req-2026-0113-c          │
│ • Common pattern: Orders with product codes starting with "SPEC-"           │
│                                                                             │
│ IMPACT                                                                      │
│ ──────────────────────────────────────────────────────────────────────────  │
│ • 8% of order validation tasks affected                                     │
│ • ~45 failed validations per day                                            │
│ • Customer impact: Delayed order confirmations                              │
│                                                                             │
│ ANALYSIS                                                                    │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Hypothesis: Prompt change in v1.3.0 introduced ambiguous handling for       │
│ special product codes. Agent gets stuck trying to classify them.            │
│                                                                             │
│ ROUTING                                                                     │
│ ──────────────────────────────────────────────────────────────────────────  │
│ ☑ Assigned to COS: Maria L. (initial investigation)                        │
│ 🔄 Routing to AE: Pending (prompt fix required)                            │
│ ⬜ CSA review: Not required                                                 │
│                                                                             │
│ [Add Note] [Route to AE] [Route to CSA] [Resolve]                           │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Cross-Team Coordination

Handoff and collaboration with AE/CSA.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ CROSS-TEAM COORDINATION: COG-2026-22                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ ISSUE: Hallucination in customer-service-05                                 │
│ Status: Assigned to AE                                                      │
│                                                                             │
│ HANDOFF TO AE                                                               │
│ ──────────────────────────────────────────────────────────────────────────  │
│ From: Maria L. (COS)                                                        │
│ To: James K. (AE)                                                           │
│ Date: Jan 13, 2026 10:30                                                    │
│                                                                             │
│ Summary:                                                                    │
│ ┌─────────────────────────────────────────────────────────────────────────┐│
│ │ Agent is fabricating customer account details (premium status, discount ││
│ │ levels) not present in the data sources. Grounding appears to be        ││
│ │ failing on account lookups. Recommend reviewing prompt grounding        ││
│ │ instructions and possibly adding explicit verification step.            ││
│ └─────────────────────────────────────────────────────────────────────────┘│
│                                                                             │
│ Attached evidence:                                                          │
│ • 3 sample traces with hallucinated content                                 │
│ • Confidence analysis (hallucinations at confidence >0.85)                  │
│ • Suggested fix approach                                                    │
│                                                                             │
│ AE RESPONSE                                                                 │
│ ──────────────────────────────────────────────────────────────────────────  │
│ From: James K. (AE)                                                         │
│ Date: Jan 13, 2026 14:15                                                    │
│                                                                             │
│ "Confirmed issue. Root cause is missing grounding check on account lookup   │
│ tool response. Fix in v2.1.1, currently in staging. Will deploy tomorrow."  │
│                                                                             │
│ [Add Comment] [Request Update] [Close Handoff]                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Resolution Tracking

Track issue resolution and verification.

---

## Key Features

- **Cognitive issue queue management**
- **Evidence collection and documentation**
- **Cross-team routing and coordination**
- **Resolution tracking and verification**
- **Issue analytics and trends**

---

## OPDA Contribution

| OPDA | Console Contribution |
|------|---------------------|
| **Observable** | Issue visibility |
| **Predictable** | Issue resolution improves predictability |
| **Directable** | Route issues to appropriate teams |
| **Authority Enforceable** | N/A (coordination focus) |

---

*Status: 🟡 Draft — Specification complete, implementation TBD*
