# Test Console

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Desk:** [Agent Development Desk](./README.md)  
> **Primary Persona:** [Agent Engineer (AE)](../../../personas-and-needs/roles.md#3-agent-engineer-ae)

---

## Purpose

The Test Console provides a comprehensive testing environment for the **Agent Engineer (AE)** ([role definition](../../../personas-and-needs/roles.md#3-agent-engineer-ae)) to validate agent behavior through behavioral, integration, regression, and stress testing.

---

## Sections

### Test Suites

Manage test suites by type.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ TEST SUITES: invoice-processor                                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ Suite            │ Tests │ Passing │ Failing │ Last Run     │ Actions      │
│ ───────────────────────────────────────────────────────────────────────────│
│ Unit Tests       │ 45    │ 45      │ 0       │ 2 hours ago  │ [Run] [Edit] │
│ Behavioral Tests │ 12    │ 12      │ 0       │ 2 hours ago  │ [Run] [Edit] │
│ Integration Tests│ 10    │ 8       │ 2       │ 2 hours ago  │ [Run] [Edit] │
│ Regression Tests │ 25    │ 25      │ 0       │ 1 day ago    │ [Run] [Edit] │
│ Stress Tests     │ 5     │ 5       │ 0       │ 1 week ago   │ [Run] [Edit] │
│                                                                             │
│ [Run All] [Run Failed] [Create Suite]                                       │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Test Results

View detailed test results with comparison.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ TEST RESULTS: Behavioral Tests                               Run: 2h ago    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ Test                              │ Status │ Expected        │ Actual       │
│ ───────────────────────────────────────────────────────────────────────────│
│ approve_matching_po               │ ✅ Pass │ Approve        │ Approve      │
│ reject_no_po                      │ ✅ Pass │ Reject         │ Reject       │
│ escalate_high_value               │ ✅ Pass │ Escalate       │ Escalate     │
│ escalate_new_vendor               │ ✅ Pass │ Escalate       │ Escalate     │
│ approve_within_authority          │ ✅ Pass │ Approve        │ Approve      │
│ reasoning_steps_bounded           │ ✅ Pass │ ≤5 steps       │ 3 steps      │
│                                                                             │
│ [View Details] [Export] [Rerun Failed]                                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Scenario Replay

Replay production scenarios for debugging.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ SCENARIO REPLAY                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ Request ID: [req-2026-0110-xyz789]                          [Load Scenario] │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ ORIGINAL EXECUTION                │ REPLAY EXECUTION                        │
│ ──────────────────────────────────│──────────────────────────────────────── │
│ Decision: Approve                 │ Decision: Approve                       │
│ Confidence: 0.87                  │ Confidence: 0.88                        │
│ Steps: 4                          │ Steps: 4                                │
│ Duration: 2.3s                    │ Duration: 2.1s                          │
│                                   │                                         │
│ Reasoning:                        │ Reasoning:                              │
│ 1. Extract invoice ($750)         │ 1. Extract invoice ($750) ✅            │
│ 2. Lookup PO (found)              │ 2. Lookup PO (found) ✅                 │
│ 3. Check vendor (approved)        │ 3. Check vendor (approved) ✅           │
│ 4. Decision: Approve              │ 4. Decision: Approve ✅                 │
│                                   │                                         │
│ ✅ Replay matches original execution                                        │
│                                                                             │
│ [Modify Input] [Step Through] [Compare Traces]                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Test Types

| Type | Purpose | When Run |
|------|---------|----------|
| **Unit Tests** | Component correctness | Every commit |
| **Behavioral Tests** | Reasoning validation | Every commit |
| **Integration Tests** | Tool binding validation | Every commit |
| **Regression Tests** | Prompt stability | Every prompt change |
| **Stress Tests** | Bound enforcement | Before release |

---

## Key Features

- **Test suite management**
- **Expected vs. actual comparison**
- **Automated test runs on commit**
- **Coverage reporting**
- **Scenario replay for debugging**

---

## OPDA Contribution

| OPDA | Console Contribution |
|------|---------------------|
| **Observable** | Test results visibility |
| **Predictable** | Behavioral test validation |
| **Directable** | Test-driven development |
| **Authority Enforceable** | Bound testing |

---

*Status: 🟡 Draft — Specification complete, implementation TBD*
