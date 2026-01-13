# Validation Console

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Desk:** [Agent Design Desk](./README.md)  
> **Primary Persona:** [Cognitive Systems Architect (CSA)](../../../personas-and-needs/roles.md#2-cognitive-systems-architect-csa)

---

## Purpose

The Validation Console enables the **Cognitive Systems Architect (CSA)** ([role definition](../../../personas-and-needs/roles.md#2-cognitive-systems-architect-csa)) to review AE implementations against designs, validate pattern compliance, and sign off on production readiness from a design perspective.

---

## Sections

### Design Review Queue

Pending implementations awaiting CSA review.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ DESIGN REVIEW QUEUE                                          [4 Pending]    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ Agent                │ Version │ Design      │ Submitted   │ Priority     │
│ ───────────────────────────────────────────────────────────────────────────│
│ expense-approver     │ v2.0.0  │ expense-v2  │ 2 days ago  │ 🔴 High       │
│ customer-service     │ v1.5.0  │ cs-suggest  │ 3 days ago  │ 🟡 Medium     │
│ data-enricher        │ v2.2.0  │ enricher-v2 │ 5 days ago  │ 🟢 Low        │
│ order-validator      │ v1.3.0  │ order-v1    │ 1 week ago  │ 🟢 Low        │
│                                                                             │
│ [Review Selected] [Bulk Actions]                                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Diff View

Side-by-side comparison of design spec vs. implementation.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ DESIGN VS IMPLEMENTATION: expense-approver v2.0.0                           │
├────────────────────────────────────┬────────────────────────────────────────┤
│ DESIGN SPEC                        │ IMPLEMENTATION                         │
├────────────────────────────────────┼────────────────────────────────────────┤
│                                    │                                        │
│ Pattern: ReAct                     │ Pattern: ReAct ✅                      │
│ Max Iterations: 5                  │ Max Iterations: 5 ✅                   │
│ Timeout: 30s                       │ Timeout: 30s ✅                        │
│ Confidence Threshold: 0.85         │ Confidence Threshold: 0.80 ⚠️          │
│                                    │                                        │
│ Escalation: amount > $500          │ Escalation: amount > $500 ✅           │
│ Escalation Target: human           │ Escalation Target: human ✅            │
│                                    │                                        │
│ Required Tools:                    │ Implemented Tools:                     │
│ • expense_parser                   │ • expense_parser ✅                    │
│ • policy_lookup                    │ • policy_lookup ✅                     │
│ • budget_check                     │ • budget_check ✅                      │
│                                    │ • receipt_ocr (new) ⚠️                 │
│                                    │                                        │
│ Trace Events:                      │ Trace Events:                          │
│ • task.started                     │ • task.started ✅                      │
│ • reasoning.step                   │ • reasoning.step ✅                    │
│ • decision.made                    │ • decision.made ✅                     │
│                                    │                                        │
├────────────────────────────────────┴────────────────────────────────────────┤
│ ⚠️ 2 Deviations Found:                                                      │
│ 1. Confidence threshold differs (0.85 vs 0.80)                              │
│ 2. Additional tool (receipt_ocr) not in design                              │
│                                                                             │
│ [Request Changes] [Approve with Notes] [Approve]                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Validation Checklist

Structured checklist for comprehensive review.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ VALIDATION CHECKLIST: expense-approver v2.0.0                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ PATTERN COMPLIANCE                                                          │
│ ☑ Implementation uses correct pattern (ReAct)                               │
│ ☑ Steps execute in correct sequence                                         │
│ ☑ Iteration bounds enforced                                                 │
│ ⬜ Timeout behavior matches design                                          │
│                                                                             │
│ COGNITIVE BOUNDARIES                                                        │
│ ☑ Agent stays within defined scope                                          │
│ ☑ Only allowed decisions are made                                           │
│ ☑ Tool access matches design                                                │
│                                                                             │
│ FAILURE SEMANTICS                                                           │
│ ☑ Failures classified correctly                                             │
│ ☑ Escalation triggers match design                                          │
│ ⬜ Recovery behavior validated                                              │
│                                                                             │
│ OBSERVABILITY                                                               │
│ ☑ Required trace events emitted                                             │
│ ☑ Decision rationale captured                                               │
│ ☑ Confidence scores included                                                │
│                                                                             │
│ Progress: 10/12 items complete                                              │
│                                                                             │
│ [Save Progress] [Complete Review]                                           │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Sign-Off

Formal approval or change request.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ VALIDATION DECISION                                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ Agent: expense-approver v2.0.0                                              │
│ Reviewer: Alex T. (CSA)                                                     │
│ Date: 2026-01-13                                                            │
│                                                                             │
│ Decision: ○ Approve  ○ Approve with Notes  ● Request Changes                │
│                                                                             │
│ Required Changes:                                                           │
│ ┌─────────────────────────────────────────────────────────────────────────┐│
│ │ 1. Confidence threshold must match design (0.85, not 0.80)              ││
│ │ 2. receipt_ocr tool requires design update before implementation        ││
│ │                                                                         ││
│ │ Please update implementation or submit design change request.           ││
│ └─────────────────────────────────────────────────────────────────────────┘│
│                                                                             │
│ [Submit Decision]                                                           │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Features

- **Side-by-side design/implementation comparison**
- **Automated constraint checking**
- **Review history and audit trail**
- **Integration with AE Release Console**

---

## OPDA Contribution

| OPDA | Console Contribution |
|------|---------------------|
| **Observable** | Implementation visibility for validation |
| **Predictable** | Design compliance ensures predictability |
| **Directable** | Change requests guide implementation |
| **Authority Enforceable** | CSA sign-off as authority gate |

---

*Status: 🟡 Draft — Specification complete, implementation TBD*
