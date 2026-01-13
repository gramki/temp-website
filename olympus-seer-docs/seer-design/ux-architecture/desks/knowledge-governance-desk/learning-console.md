# Learning Console

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Desk:** [Knowledge Governance Desk](./README.md)  
> **Primary Persona:** [Knowledge & Memory Owner (KMO)](../../../personas-and-needs/roles.md#4-knowledge--memory-owner-kmo)

---

## Purpose

The Learning Console enables the **Knowledge & Memory Owner (KMO)** ([role definition](../../../personas-and-needs/roles.md#4-knowledge--memory-owner-kmo)) to govern enterprise learning, review learning candidates for promotion, and establish promotion criteria.

For detailed context on enterprise learning requirements, see [KMO: Enterprise Learning & Memory Promotion](../../../personas-and-needs/needs/kmo-enterprise-learning.md).

---

## Sections

### Promotion Queue

Learning candidates awaiting KMO review.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ PROMOTION QUEUE                                             [24 Candidates] │
├─────────────────────────────────────────────────────────────────────────────┤
│ Level: [L1→L2 ▼] [L2→L3 ▼]  Agent: [All ▼]  Domain: [All ▼]                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ L1 → L2 PROMOTIONS (Class Memory)                          [12 Candidates]  │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Learning             │ Source Agent     │ Reuse Count │ Score │ Status     │
│ ───────────────────────────────────────────────────────────────────────────│
│ Receipt validation   │ expense-approver │ 45          │ 0.92  │ 🔴 Review   │
│   pattern for meals  │                  │             │       │            │
│ Vendor name          │ invoice-proc     │ 38          │ 0.88  │ 🔴 Review   │
│   normalization      │                  │             │       │            │
│ Per diem lookup      │ travel-agent     │ 28          │ 0.85  │ 🟡 Pending  │
│   optimization       │                  │             │       │            │
│                                                                             │
│ L2 → L3 PROMOTIONS (Enterprise Memory)                     [6 Candidates]   │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Learning             │ Agent Class      │ Usage       │ Score │ Status     │
│ ───────────────────────────────────────────────────────────────────────────│
│ Q4 expense policy    │ finance-agents   │ 250 uses    │ 0.95  │ 🔴 Review   │
│   interpretation     │                  │             │       │            │
│ New vendor onboard   │ procurement      │ 180 uses    │ 0.91  │ 🔴 Review   │
│   process pattern    │                  │             │       │            │
│                                                                             │
│ [Review Selected] [Bulk Approve] [Reject with Feedback]                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Learning Review

Detailed review interface for individual learnings.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ LEARNING REVIEW: Receipt validation pattern for meals                       │
├─────────────────────────────────────────────────────────────────────────────┤
│ Source: expense-approver │ Proposed Level: L2 (Agent Class)                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ LEARNING CONTENT                                                            │
│ ──────────────────────────────────────────────────────────────────────────  │
│ When validating meal receipts:                                              │
│ 1. Check receipt date matches expense claim date ±1 day                     │
│ 2. Verify vendor name contains food-related keywords                        │
│ 3. Confirm total matches claimed amount within $0.10 tolerance              │
│ 4. Flag receipts over $75 for per diem check                                │
│                                                                             │
│ PROVENANCE                                                                  │
│ ──────────────────────────────────────────────────────────────────────────  │
│ • Originated: expense-approver-01 on Nov 15, 2025                           │
│ • Refined: 12 iterations across 3 agent instances                           │
│ • Reuse count: 45 (last 30 days)                                            │
│ • Success rate: 98.2%                                                       │
│                                                                             │
│ PROMOTION CRITERIA                                                          │
│ ──────────────────────────────────────────────────────────────────────────  │
│ ☑ Minimum reuse count (>25)                              ✅ 45 uses         │
│ ☑ Success rate (>95%)                                    ✅ 98.2%           │
│ ☑ Cross-instance validation                              ✅ 3 instances     │
│ ☑ No contradictions with existing knowledge              ✅ Verified        │
│ ⬜ KMO approval                                          🔄 Pending         │
│                                                                             │
│ KMO NOTES                                                                   │
│ ┌─────────────────────────────────────────────────────────────────────────┐│
│ │                                                                         ││
│ │                                                                         ││
│ └─────────────────────────────────────────────────────────────────────────┘│
│                                                                             │
│ [Approve] [Approve with Edits] [Reject] [Request More Data]                 │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Promotion Criteria

Define thresholds for automatic promotion eligibility.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ PROMOTION CRITERIA                                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ L1 → L2 (Instance → Class)                                                  │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Criterion             │ Threshold  │ Required │ Description                 │
│ Minimum Reuse         │ 25         │ Yes      │ Used across tasks           │
│ Success Rate          │ 95%        │ Yes      │ Positive outcomes           │
│ Cross-Instance        │ 2          │ Yes      │ Validated by other agents   │
│ Age                   │ 7 days     │ Yes      │ Minimum age before review   │
│                                                                             │
│ L2 → L3 (Class → Enterprise)                                                │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Criterion             │ Threshold  │ Required │ Description                 │
│ Minimum Usage         │ 100        │ Yes      │ Cross-class usage           │
│ Success Rate          │ 97%        │ Yes      │ Higher bar for enterprise   │
│ Cross-Class           │ 2          │ Yes      │ Used by multiple classes    │
│ No Contradictions     │ 100%       │ Yes      │ Consistent with existing    │
│ KMO Approval          │ Required   │ Yes      │ Human review required       │
│                                                                             │
│ [Edit Criteria] [Preview Candidates] [View History]                         │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Learning Analytics

Metrics on learning effectiveness and promotion rates.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ LEARNING ANALYTICS                                         Last 30 Days     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ PROMOTION FUNNEL                                                            │
│ ──────────────────────────────────────────────────────────────────────────  │
│ L1 Candidates:    450 ████████████████████████████████████████████████████  │
│ L1→L2 Eligible:   120 █████████████                                         │
│ L1→L2 Promoted:    85 █████████                                             │
│ L2→L3 Eligible:    15 ██                                                    │
│ L2→L3 Promoted:     8 █                                                     │
│                                                                             │
│ LEARNING IMPACT                                                             │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Metric                         │ Before Learning │ After Learning │ Change  │
│ Task success rate              │ 87%             │ 94%            │ +7%     │
│ Avg reasoning steps            │ 5.2             │ 3.8            │ -27%    │
│ Human escalation rate          │ 18%             │ 11%            │ -39%    │
│                                                                             │
│ [Detailed Report] [Export] [Trends]                                         │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Features

- **Learning promotion queue with filtering**
- **Detailed review with provenance tracking**
- **Configurable promotion criteria**
- **Learning impact analytics**
- **Bulk actions for efficient review**

---

## OPDA Contribution

| OPDA | Console Contribution |
|------|---------------------|
| **Observable** | Learning provenance visibility |
| **Predictable** | Promotion criteria consistency |
| **Directable** | KMO approval workflow |
| **Authority Enforceable** | Knowledge promotion governance |

---

*Status: 🟡 Draft — Specification complete, implementation TBD*
