# Autonomy Console

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Desk:** [Agent Compliance Desk](./README.md)  
> **Primary Persona:** [Agent Risk & Audit Officer (ARAO)](../../../personas-and-needs/roles.md#7-agent-risk--audit-officer-arao)

---

## Purpose

The Autonomy Console enables the **Agent Risk & Audit Officer (ARAO)** ([role definition](../../../personas-and-needs/roles.md#7-agent-risk--audit-officer-arao)) to define, manage, and monitor autonomy levels across the agent fleet, ensuring appropriate human oversight.

For detailed context on ARAO needs, see [ARAO: Audit Readiness & Policy Compliance](../../../personas-and-needs/needs/arao-audit-readiness.md).

---

## Sections

### Autonomy Level Registry

Define and manage autonomy levels.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ AUTONOMY LEVEL REGISTRY                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ Level     │ Name               │ Description               │ Human Role     │
│ ───────────────────────────────────────────────────────────────────────────│
│ L0        │ Manual             │ Human executes, AI advises│ Executor       │
│ L1        │ Assisted           │ AI proposes, human decides│ Decision-maker │
│ L2        │ Supervised         │ AI executes, human reviews│ Reviewer       │
│ L3        │ Bounded Autonomous │ AI autonomous within rules│ Exception only │
│ L4        │ Fully Autonomous   │ AI autonomous, audit only │ Auditor        │
│                                                                             │
│ [View Details] [Edit Definitions] [Export]                                  │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Agent Autonomy Assignments

Current autonomy levels by agent.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ AGENT AUTONOMY ASSIGNMENTS                                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│ Filter: [All Levels ▼]  [All Classes ▼]  [Search...]                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ Agent Class          │ Current │ Requested │ Ceiling │ Status │ Actions    │
│ ───────────────────────────────────────────────────────────────────────────│
│ expense-approver     │ L3      │ —         │ L3      │ ✅ At ceiling │ [Edit]│
│ invoice-processor    │ L2      │ L3        │ L3      │ 📋 Pending    │ [Review]│
│ order-validator      │ L2      │ —         │ L3      │ ✅ Active     │ [Edit]│
│ customer-service     │ L1      │ L2        │ L2      │ 📋 Pending    │ [Review]│
│ data-enricher        │ L3      │ —         │ L4      │ ✅ Active     │ [Edit]│
│ compliance-checker   │ L2      │ —         │ L2      │ ✅ At ceiling │ [Edit]│
│                                                                             │
│ [Bulk Update] [Export Report]                                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Autonomy Change Request

Review and approve autonomy level changes.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ AUTONOMY CHANGE REQUEST: invoice-processor                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│ Requested by: Alex T. (APO)  │  Date: Jan 12, 2026                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ CURRENT STATE                      │ REQUESTED STATE                        │
│ ──────────────────────────────────│────────────────────────────────────────│
│ Level: L2 (Supervised)             │ Level: L3 (Bounded Autonomous)         │
│ Human: Reviews all decisions       │ Human: Exception handling only         │
│ Escalation: >$1000                 │ Escalation: >$5000 or new vendor       │
│                                                                             │
│ JUSTIFICATION                                                               │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Agent has operated at L2 for 6 months with 99.2% accuracy on decisions     │
│ reviewed by humans. Human reviewers are experiencing fatigue and           │
│ rubber-stamping decisions. Upgrade to L3 would reduce review burden while  │
│ maintaining appropriate oversight for high-value and new vendor invoices.  │
│                                                                             │
│ SUPPORTING EVIDENCE                                                         │
│ ──────────────────────────────────────────────────────────────────────────  │
│ ☑ 6+ months at current level                                               │
│ ☑ Accuracy > 99% (actual: 99.2%)                                           │
│ ☑ No critical incidents at current level                                    │
│ ☑ Human reviewer concordance > 98%                                          │
│ ☑ AHS > 0.90 for 90 days (actual: 0.92)                                    │
│                                                                             │
│ RISK ASSESSMENT                                                             │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Risk: Medium                                                                │
│ Mitigation: Maintain escalation rules for high-value and new vendors       │
│ Rollback plan: Immediate downgrade to L2 if error rate exceeds 2%          │
│                                                                             │
│ ARAO DECISION                                                               │
│ ──────────────────────────────────────────────────────────────────────────  │
│ ○ Approve  ○ Approve with conditions  ○ Deny                               │
│                                                                             │
│ Conditions/Notes:                                                           │
│ ┌─────────────────────────────────────────────────────────────────────────┐│
│ │                                                                         ││
│ └─────────────────────────────────────────────────────────────────────────┘│
│                                                                             │
│ [Submit Decision]                                                           │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Escalation Rules

Define when agents must escalate to humans.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ ESCALATION RULES: expense-approver (L3)                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ MANDATORY ESCALATION CONDITIONS                                             │
│ ──────────────────────────────────────────────────────────────────────────  │
│ ☑ Amount exceeds $500                                                       │
│ ☑ New vendor (not in approved vendor list)                                  │
│ ☑ Category requires receipts and receipt missing                            │
│ ☑ Confidence score < 0.85                                                   │
│ ☑ Policy lookup returns ambiguous result                                    │
│                                                                             │
│ ESCALATION TARGETS                                                          │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Condition                  │ Target                 │ SLA                   │
│ Amount > $500              │ Finance Manager        │ 4 hours               │
│ New vendor                 │ Procurement Team       │ 24 hours              │
│ Missing receipt            │ Employee (requestor)   │ 48 hours              │
│ Low confidence             │ Finance Analyst        │ 2 hours               │
│                                                                             │
│ [Add Rule] [Edit Rules] [Test Rules] [History]                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Features

- **Autonomy level definitions and registry**
- **Agent autonomy assignments**
- **Change request workflow with evidence**
- **Escalation rule management**
- **Autonomy compliance monitoring**

---

## OPDA Contribution

| OPDA | Console Contribution |
|------|---------------------|
| **Observable** | Autonomy level visibility |
| **Predictable** | Clear autonomy boundaries |
| **Directable** | Escalation rules |
| **Authority Enforceable** | Autonomy governance |

---

*Status: 🟡 Draft — Specification complete, implementation TBD*
