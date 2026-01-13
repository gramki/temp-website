# Compliance Console

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Desk:** [Agent Compliance Desk](./README.md)  
> **Primary Persona:** [Agent Risk & Audit Officer (ARAO)](../../../personas-and-needs/roles.md#7-agent-risk--audit-officer-arao)

---

## Purpose

The Compliance Console enables the **Agent Risk & Audit Officer (ARAO)** ([role definition](../../../personas-and-needs/roles.md#7-agent-risk--audit-officer-arao)) to monitor policy compliance, manage compliance rules, and generate evidence for audits.

---

## Sections

### Compliance Dashboard

Enterprise-wide compliance overview.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ COMPLIANCE DASHBOARD                                       Last 30 Days     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ OVERALL COMPLIANCE                                                          │
│ ┌───────────────────┬───────────────────┬───────────────────┐              │
│ │    COMPLIANT      │   MINOR ISSUES    │    VIOLATIONS     │              │
│ │       42          │        3          │        0          │              │
│ │     (93%)         │     (7%)          │     (0%)          │              │
│ └───────────────────┴───────────────────┴───────────────────┘              │
│                                                                             │
│ BY POLICY DOMAIN                                                            │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Domain              │ Agents │ Compliant │ Issues │ Status                  │
│ ───────────────────────────────────────────────────────────────────────────│
│ Financial Controls  │ 15     │ 15        │ 0      │ ✅ Full compliance      │
│ Data Privacy        │ 20     │ 18        │ 2      │ ⚠️ Minor issues        │
│ Operational Risk    │ 25     │ 24        │ 1      │ ⚠️ Minor issues        │
│ Regulatory          │ 10     │ 10        │ 0      │ ✅ Full compliance      │
│                                                                             │
│ [View Details] [Export Report] [Schedule Audit]                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Policy Rules

Manage compliance policies.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ POLICY RULES                                                                │
├─────────────────────────────────────────────────────────────────────────────┤
│ Domain: [All ▼]  Status: [Active ▼]  [Search...]                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ Rule ID     │ Name                    │ Domain     │ Applies To │ Status   │
│ ───────────────────────────────────────────────────────────────────────────│
│ POL-FIN-001 │ Approval authority limit│ Financial  │ All        │ ✅ Active │
│ POL-FIN-002 │ Dual approval required  │ Financial  │ expense-*  │ ✅ Active │
│ POL-PRI-001 │ PII masking required    │ Privacy    │ customer-* │ ✅ Active │
│ POL-PRI-002 │ Data retention limits   │ Privacy    │ All        │ ✅ Active │
│ POL-OPS-001 │ Execution time bounds   │ Operational│ All        │ ✅ Active │
│ POL-REG-001 │ Audit trail required    │ Regulatory │ All        │ ✅ Active │
│                                                                             │
│ [Create Rule] [Import Rules] [Export]                                       │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Policy Rule Detail

Configure individual policy rules.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ POLICY RULE: POL-FIN-001                                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ RULE DEFINITION                                                             │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Name: Approval authority limit                                              │
│ Domain: Financial Controls                                                  │
│ Applies to: All financial agents                                            │
│                                                                             │
│ Description:                                                                │
│ Agents cannot approve transactions exceeding their assigned authority       │
│ limit. Transactions exceeding limits must be escalated.                     │
│                                                                             │
│ CONDITION                                                                   │
│ ──────────────────────────────────────────────────────────────────────────  │
│ IF decision.type == "approval"                                              │
│    AND decision.amount > agent.authority_limit                              │
│ THEN DENY with reason "Exceeds authority limit"                             │
│    AND escalate_to "manager"                                                │
│                                                                             │
│ AUTHORITY LIMITS BY AGENT CLASS                                             │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Agent Class          │ Authority Limit │ Escalation Target                  │
│ expense-approver     │ $500            │ finance_manager                    │
│ invoice-processor    │ $5,000          │ finance_director                   │
│ purchase-approver    │ $10,000         │ procurement_head                   │
│                                                                             │
│ ENFORCEMENT                                                                 │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Mode: ● Hard (block) ○ Soft (warn) ○ Monitor only                          │
│ Last updated: Jan 5, 2026 by Sarah M. (ARAO)                                │
│                                                                             │
│ [Edit Rule] [View Violations] [Test Rule] [Disable]                         │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Audit Evidence

Generate compliance evidence for audits.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ AUDIT EVIDENCE GENERATOR                                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ REPORT CONFIGURATION                                                        │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Period: [Jan 1, 2026] to [Jan 31, 2026]                                    │
│ Scope: ☑ All agents ○ Selected agents                                      │
│ Policy domains: ☑ All ○ Selected                                           │
│                                                                             │
│ REPORT CONTENTS                                                             │
│ ──────────────────────────────────────────────────────────────────────────  │
│ ☑ Agent inventory and classifications                                       │
│ ☑ Autonomy levels and change history                                        │
│ ☑ Policy compliance status                                                  │
│ ☑ Decision audit trails (sample)                                            │
│ ☑ Escalation statistics                                                     │
│ ☑ Incident history                                                          │
│ ☑ Control effectiveness metrics                                             │
│                                                                             │
│ FORMAT                                                                      │
│ ──────────────────────────────────────────────────────────────────────────  │
│ ○ PDF Report  ● XLSX Workbook  ○ JSON Data  ○ All formats                  │
│                                                                             │
│ [Preview] [Generate Report] [Schedule Recurring]                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Features

- **Enterprise compliance dashboard**
- **Policy rule management**
- **Compliance monitoring and alerting**
- **Audit evidence generation**
- **Violation tracking and remediation**

---

## OPDA Contribution

| OPDA | Console Contribution |
|------|---------------------|
| **Observable** | Compliance visibility |
| **Predictable** | Policy enforcement |
| **Directable** | Policy configuration |
| **Authority Enforceable** | Compliance governance |

---

*Status: 🟡 Draft — Specification complete, implementation TBD*
