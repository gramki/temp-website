# Security Console

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Desk:** [Agent Compliance Desk](./README.md)  
> **Primary Persona:** [Agent Risk & Audit Officer (ARAO)](../../../personas-and-needs/roles.md#7-agent-risk--audit-officer-arao)

---

## Purpose

The Security Console enables the **Agent Risk & Audit Officer (ARAO)** ([role definition](../../../personas-and-needs/roles.md#7-agent-risk--audit-officer-arao)) to manage tool permissions, monitor authority violations, and oversee security boundaries for the agent fleet.

---

## Sections

### Tool Permissions

Manage agent access to tools and APIs.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ TOOL PERMISSIONS                                                            │
├─────────────────────────────────────────────────────────────────────────────┤
│ Agent: [expense-approver ▼]  View: [Granted ▼]  [Search...]                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ GRANTED PERMISSIONS                                                         │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Tool                  │ Type    │ Scope              │ Granted By │ Date   │
│ ───────────────────────────────────────────────────────────────────────────│
│ expense_parser        │ MCP     │ Read               │ System     │ Initial│
│ policy_lookup         │ REST    │ Read               │ Sarah M.   │ Jan 5  │
│ budget_check          │ REST    │ Read               │ Sarah M.   │ Jan 5  │
│ record_decision       │ Hub API │ Write (decisions)  │ System     │ Initial│
│ employee_lookup       │ REST    │ Read (non-PII)     │ James K.   │ Jan 10 │
│                                                                             │
│ DENIED PERMISSIONS                                                          │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Tool                  │ Type    │ Reason                        │ Date     │
│ ───────────────────────────────────────────────────────────────────────────│
│ employee_full_profile │ REST    │ Contains PII                  │ Jan 5    │
│ payment_execute       │ REST    │ Outside agent scope           │ Jan 5    │
│ database_direct       │ Native  │ No direct DB access allowed   │ Initial  │
│                                                                             │
│ [Add Permission] [Revoke Permission] [Audit Trail]                          │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Authority Boundaries

Define and monitor authority boundaries.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ AUTHORITY BOUNDARIES                                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ BOUNDARY DEFINITION: expense-approver                                       │
│ ──────────────────────────────────────────────────────────────────────────  │
│                                                                             │
│ DECISION AUTHORITY                                                          │
│ ┌─────────────────────────────────────────────────────────────────────────┐│
│ │ CAN: Approve expense claims ≤ $500                                      ││
│ │ CAN: Reject expense claims (any amount)                                 ││
│ │ CAN: Request additional information from employee                       ││
│ │ CANNOT: Approve expense claims > $500 (escalate)                        ││
│ │ CANNOT: Override policy rules                                           ││
│ │ CANNOT: Access employee salary/compensation data                        ││
│ └─────────────────────────────────────────────────────────────────────────┘│
│                                                                             │
│ DATA ACCESS                                                                 │
│ ┌─────────────────────────────────────────────────────────────────────────┐│
│ │ CAN: Read expense claim data                                            ││
│ │ CAN: Read expense policy rules                                          ││
│ │ CAN: Read employee name and department                                  ││
│ │ CANNOT: Read employee PII (SSN, bank details)                           ││
│ │ CANNOT: Write to employee records                                       ││
│ └─────────────────────────────────────────────────────────────────────────┘│
│                                                                             │
│ [Edit Boundaries] [Test Boundaries] [Export Policy]                         │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Authority Violations

Monitor and investigate authority violations.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ AUTHORITY VIOLATIONS                                        Last 7 Days     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ SUMMARY                                                                     │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Total attempts: 15  │  Blocked: 15 (100%)  │  Critical: 0                   │
│                                                                             │
│ VIOLATION LOG                                                               │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Time          │ Agent             │ Violation              │ Action        │
│ ───────────────────────────────────────────────────────────────────────────│
│ Jan 13, 14:22 │ expense-apprvr-03 │ Attempted $800 approval│ Blocked       │
│ Jan 13, 11:05 │ customer-svc-02   │ PII access attempt     │ Blocked       │
│ Jan 12, 16:45 │ invoice-proc-01   │ Unauthorized tool call │ Blocked       │
│ Jan 12, 09:30 │ data-enricher-05  │ Write to read-only DB  │ Blocked       │
│ Jan 11, 22:15 │ expense-apprvr-07 │ Attempted $600 approval│ Blocked       │
│                                                                             │
│ VIOLATION DETAIL                                                            │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Agent: expense-apprvr-03                                                    │
│ Request: req-2026-0113-viol1                                               │
│ Violation: Attempted to approve expense claim of $800                       │
│ Authority limit: $500                                                       │
│ Action: Blocked and escalated to human approver                             │
│ OPA Policy: expense_authority_limit                                         │
│                                                                             │
│ [View Trace] [Investigate] [Export Log]                                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Security Events

Monitor security-related events.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ SECURITY EVENTS                                             Last 24 Hours   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ EVENT TYPE SUMMARY                                                          │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Authority violations:    15  ████████████                                   │
│ Tool permission denials: 8   ████████                                       │
│ Unusual access patterns: 2   ██                                             │
│ Prompt injection attempts: 0                                                │
│                                                                             │
│ RECENT EVENTS                                                               │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Time          │ Type                  │ Agent         │ Severity │ Status  │
│ ───────────────────────────────────────────────────────────────────────────│
│ Jan 13, 15:30 │ Unusual access        │ data-enricher │ 🟡 Med   │ Reviewing│
│ Jan 13, 14:22 │ Authority violation   │ expense-appr  │ 🟢 Low   │ Resolved│
│ Jan 13, 11:05 │ Tool denial           │ customer-svc  │ 🟢 Low   │ Resolved│
│ Jan 13, 09:45 │ Unusual access        │ invoice-proc  │ 🟡 Med   │ Reviewing│
│                                                                             │
│ [Configure Alerts] [Export Events] [SIEM Integration]                       │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Features

- **Tool permission management**
- **Authority boundary definitions**
- **Violation monitoring and alerting**
- **Security event logging**
- **Integration with OPA policies**

---

## OPDA Contribution

| OPDA | Console Contribution |
|------|---------------------|
| **Observable** | Security event visibility |
| **Predictable** | Consistent authority enforcement |
| **Directable** | Permission configuration |
| **Authority Enforceable** | Core authority enforcement |

---

*Status: 🟡 Draft — Specification complete, implementation TBD*
