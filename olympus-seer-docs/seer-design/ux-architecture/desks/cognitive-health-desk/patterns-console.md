# Patterns Console

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Desk:** [Cognitive Health Desk](./README.md)  
> **Primary Persona:** [Cognitive Operations Specialist (COS)](../../../personas-and-needs/roles.md#6-cognitive-operations-specialist-cos)

---

## Purpose

The Patterns Console enables the **Cognitive Operations Specialist (COS)** ([role definition](../../../personas-and-needs/roles.md#6-cognitive-operations-specialist-cos)) to analyze behavioral patterns, detect drift, and identify reasoning anti-patterns across the agent fleet.

---

## Sections

### Behavioral Trends

Long-term behavioral analysis.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ BEHAVIORAL TRENDS                                           Last 30 Days    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ DECISION DISTRIBUTION: expense-approver                                     │
│ ──────────────────────────────────────────────────────────────────────────  │
│     │                                                                       │
│ 80% │    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄              │
│ 60% │                                                                       │
│ 40% │                                                                       │
│ 20% │    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░               │
│  0% │────────────────────────────────────────────────────────              │
│      Week 1    Week 2    Week 3    Week 4                                   │
│                                                                             │
│     ▄ Approved (72%)  ░ Rejected (15%)  ▒ Escalated (13%)                   │
│                                                                             │
│ TREND ALERTS                                                                │
│ • Escalation rate increased 3% over baseline                                │
│ • Rejection rate stable                                                     │
│ • Approval confidence trending down (0.91 → 0.87)                           │
│                                                                             │
│ [Drill Down] [Compare Agents] [Export]                                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Drift Detection

Monitor for behavioral drift from baselines.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ DRIFT DETECTION                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ BASELINE COMPARISON                                                         │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Agent               │ Metric            │ Baseline │ Current │ Drift       │
│ ───────────────────────────────────────────────────────────────────────────│
│ expense-approver    │ Approval rate     │ 75%      │ 72%     │ -3% ⚠️     │
│ expense-approver    │ Avg confidence    │ 0.89     │ 0.87    │ -2% ✅     │
│ invoice-processor   │ Processing time   │ 2.1s     │ 2.8s    │ +33% 🔴    │
│ customer-service    │ Escalation rate   │ 12%      │ 18%     │ +50% 🔴    │
│ order-validator     │ Rejection rate    │ 8%       │ 15%     │ +88% 🔴    │
│                                                                             │
│ SIGNIFICANT DRIFT ALERT                                                     │
│ ──────────────────────────────────────────────────────────────────────────  │
│ 🔴 order-validator: Rejection rate increased 88% (8% → 15%)                │
│                                                                             │
│ Possible causes:                                                            │
│ • Recent prompt update (v1.3.0, Jan 10)                                     │
│ • Input data quality change                                                 │
│ • Knowledge source update                                                   │
│                                                                             │
│ Recommended actions:                                                        │
│ • Review recent changes                                                     │
│ • Compare trace samples before/after                                        │
│ • Consult with AE on prompt changes                                         │
│                                                                             │
│ [Investigate] [Adjust Baseline] [Configure Alerts]                          │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Anti-Pattern Detection

Identify reasoning anti-patterns.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ ANTI-PATTERN DETECTION                                      Last 7 Days     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ DETECTED ANTI-PATTERNS                                                      │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Pattern              │ Agent              │ Occurrences │ Severity          │
│ ───────────────────────────────────────────────────────────────────────────│
│ Reasoning Loop       │ order-validator-03 │ 12          │ 🔴 High           │
│ Tool Retry Storm     │ invoice-proc-02    │ 8           │ 🟡 Medium         │
│ Context Bloat        │ customer-svc-05    │ 15          │ 🟡 Medium         │
│ Premature Decision   │ data-enricher-01   │ 5           │ 🟢 Low            │
│                                                                             │
│ ANTI-PATTERN DETAIL: Reasoning Loop                                         │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Description: Agent cycles through same reasoning steps without progress     │
│                                                                             │
│ Example (req-2026-0112-loop):                                               │
│ Step 1: Check order details                                                 │
│ Step 2: Validate customer                                                   │
│ Step 3: Check order details (repeat)                                        │
│ Step 4: Validate customer (repeat)                                          │
│ ... (terminated at iteration limit)                                         │
│                                                                             │
│ Root cause: Ambiguous exit condition in validation logic                    │
│                                                                             │
│ [View Examples] [Route to AE] [Create Ticket]                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Comparative Analysis

Compare behavior across agents.

---

## Key Features

- **Long-term behavioral trend analysis**
- **Automated drift detection**
- **Anti-pattern identification**
- **Baseline management**
- **Comparative agent analysis**

---

## OPDA Contribution

| OPDA | Console Contribution |
|------|---------------------|
| **Observable** | Pattern visibility |
| **Predictable** | Drift alerts maintain predictability |
| **Directable** | Route issues to appropriate teams |
| **Authority Enforceable** | N/A (monitoring focus) |

---

*Status: 🟡 Draft — Specification complete, implementation TBD*
