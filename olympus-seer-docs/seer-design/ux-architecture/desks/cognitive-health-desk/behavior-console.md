# Behavior Console

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Desk:** [Cognitive Health Desk](./README.md)  
> **Primary Persona:** [Cognitive Operations Specialist (COS)](../../../personas-and-needs/roles.md#6-cognitive-operations-specialist-cos)

---

## Purpose

The Behavior Console enables the **Cognitive Operations Specialist (COS)** ([role definition](../../../personas-and-needs/roles.md#6-cognitive-operations-specialist-cos)) to monitor agent reasoning quality, identify behavioral anomalies, and assess cognitive health.

For detailed context on COS needs, see [COS: Cognitive Health & Behavioral Monitoring](../../../personas-and-needs/needs/cos-behavioral-monitoring.md).

---

## Sections

### Reasoning Quality Dashboard

Overview of reasoning health across agents.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ REASONING QUALITY DASHBOARD                               Last 24 Hours     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ OVERALL METRICS                                                             │
│ ┌───────────────────┬───────────────────┬───────────────────┐              │
│ │ Reasoning Success │ Avg Confidence    │ Anomaly Rate      │              │
│ │      94.2%        │      0.87         │      2.1%         │              │
│ │   (target: >90%)  │  (target: >0.80)  │  (target: <5%)    │              │
│ └───────────────────┴───────────────────┴───────────────────┘              │
│                                                                             │
│ BY AGENT CLASS                                                              │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Class                │ Success │ Confidence │ Anomalies │ Status           │
│ ───────────────────────────────────────────────────────────────────────────│
│ expense-approver     │ 96.5%   │ 0.89       │ 1.2%      │ 🟢 Healthy       │
│ invoice-processor    │ 95.2%   │ 0.88       │ 1.8%      │ 🟢 Healthy       │
│ customer-service     │ 91.8%   │ 0.82       │ 4.5%      │ 🟡 Watch         │
│ order-validator      │ 88.5%   │ 0.78       │ 6.2%      │ 🔴 Attention     │
│ data-enricher        │ 97.1%   │ 0.91       │ 0.8%      │ 🟢 Healthy       │
│                                                                             │
│ [View Details] [Configure Thresholds] [Export Report]                       │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Trace Viewer

Deep dive into agent reasoning traces.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ TRACE VIEWER                                                                │
├─────────────────────────────────────────────────────────────────────────────┤
│ Request: [req-2026-0113-abc123]                              [Load Trace]   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ Agent: expense-approver-02  │  Task: Approve expense claim $450             │
│ Duration: 2.3s  │  Steps: 4  │  Result: Approved  │  Confidence: 0.91       │
│                                                                             │
│ REASONING TRACE                                                             │
│ ──────────────────────────────────────────────────────────────────────────  │
│ ┌─────────────────────────────────────────────────────────────────────────┐│
│ │ STEP 1: Parse Request (150ms)                                           ││
│ │ Input: "Expense claim for team lunch - $450"                            ││
│ │ Extracted: {type: "meals", amount: 450, category: "team"}               ││
│ │ Confidence: 0.95                                                        ││
│ └─────────────────────────────────────────────────────────────────────────┘│
│                           │                                                 │
│                           ▼                                                 │
│ ┌─────────────────────────────────────────────────────────────────────────┐│
│ │ STEP 2: Policy Lookup (200ms)                                           ││
│ │ Tool: policy_lookup("meals", "team")                                    ││
│ │ Result: {limit: 500, approval_required: false}                          ││
│ │ Confidence: 0.98                                                        ││
│ └─────────────────────────────────────────────────────────────────────────┘│
│                           │                                                 │
│                           ▼                                                 │
│ ┌─────────────────────────────────────────────────────────────────────────┐│
│ │ STEP 3: Decision (300ms)                                                ││
│ │ Reasoning: "Amount $450 is within $500 limit for team meals.            ││
│ │ No additional approval required per policy."                            ││
│ │ Decision: APPROVE                                                       ││
│ │ Confidence: 0.91                                                        ││
│ └─────────────────────────────────────────────────────────────────────────┘│
│                           │                                                 │
│                           ▼                                                 │
│ ┌─────────────────────────────────────────────────────────────────────────┐│
│ │ STEP 4: Record Decision (50ms)                                          ││
│ │ Tool: record_decision({...})                                            ││
│ │ Result: Decision logged successfully                                    ││
│ └─────────────────────────────────────────────────────────────────────────┘│
│                                                                             │
│ [Previous Step] [Next Step] [Export] [Flag for Review]                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Confidence Distribution

Analyze confidence patterns.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ CONFIDENCE DISTRIBUTION: expense-approver                   Last 7 Days     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ DISTRIBUTION                                                                │
│ ──────────────────────────────────────────────────────────────────────────  │
│        │                                                                    │
│ 0.9-1.0│ ████████████████████████████████████████████████  (62%)           │
│ 0.8-0.9│ ██████████████████████████████  (28%)                             │
│ 0.7-0.8│ ██████  (7%)                                                      │
│ 0.6-0.7│ ██  (2%)                                                          │
│  <0.6  │ █  (1%)                                                           │
│        └───────────────────────────────────────────────────────────────    │
│                                                                             │
│ LOW CONFIDENCE SAMPLES (< 0.7)                                              │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Request         │ Confidence │ Decision       │ Reason                     │
│ req-2026-0112-x │ 0.65       │ Escalated      │ Ambiguous expense category │
│ req-2026-0111-y │ 0.62       │ Escalated      │ Missing receipt            │
│ req-2026-0110-z │ 0.58       │ Escalated      │ Unusual vendor             │
│                                                                             │
│ [View Trend] [Configure Threshold] [Investigate Low Confidence]             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Hallucination Detection

Monitor for hallucination indicators.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ HALLUCINATION INDICATORS                                    Last 24 Hours   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ DETECTED INSTANCES                                                          │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Agent               │ Type               │ Severity │ Time                  │
│ ───────────────────────────────────────────────────────────────────────────│
│ customer-service-05 │ Fabricated fact    │ 🔴 High  │ 2 hours ago          │
│ data-enricher-02    │ Contradictory stmt │ 🟡 Med   │ 6 hours ago          │
│ order-validator-03  │ Unsupported claim  │ 🟡 Med   │ 12 hours ago         │
│                                                                             │
│ HALLUCINATION DETAIL                                                        │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Agent: customer-service-05                                                  │
│ Request: req-2026-0113-hal1                                                │
│                                                                             │
│ Agent stated: "Your account has a premium status with 20% discount"         │
│ Reality: No discount associated with this account                           │
│ Detection: Cross-reference with account data returned no match              │
│                                                                             │
│ Action: [Review Agent] [Retrain] [Adjust Grounding]                         │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Features

- **Reasoning quality metrics dashboard**
- **Interactive trace visualization**
- **Confidence analysis and distribution**
- **Hallucination detection and alerting**
- **Step-by-step reasoning inspection**

---

## OPDA Contribution

| OPDA | Console Contribution |
|------|---------------------|
| **Observable** | Deep reasoning visibility |
| **Predictable** | Quality baselines and thresholds |
| **Directable** | Issue flagging and routing |
| **Authority Enforceable** | N/A (monitoring focus) |

---

*Status: 🟡 Draft — Specification complete, implementation TBD*
