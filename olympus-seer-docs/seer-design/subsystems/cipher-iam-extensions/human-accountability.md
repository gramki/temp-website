# Human Accountability

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-12

---

## Overview

Every Employed Agent must have an accountable human who is responsible for the agent's actions. This document describes accountable human assignment, accountability chain, and audit trail requirements.

---

## Accountable Human Requirement

### Mandatory for All Employed Agents

Every Employed Agent **must** have an accountable human:

```yaml
spec:
  delegation:
    accountable: "user:jane.manager@acme.com"  # Required
```

### Validation Rules

| Rule | Description |
|------|-------------|
| **Required** | `accountable` field is mandatory |
| **Must be human** | Must be a user identity, not role or agent |
| **Must exist** | Identity must exist in Cipher IAM |
| **Must be active** | User account must be active |

---

## Accountability Chain

### Chain Structure

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        ACCOUNTABILITY CHAIN                                  │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  AGENT ACTION                                                        │   │
│   │  Transaction analyzed by fraud-analyst-acme-retail                  │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                 │                                            │
│                          performed by                                        │
│                                 ▼                                            │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  EMPLOYED AGENT                                                      │   │
│   │  fraud-analyst-acme-retail                                          │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                 │                                            │
│                          delegated by                                        │
│                                 ▼                                            │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  DELEGATOR (optional)                                                │   │
│   │  user:john.smith@acme.com                                           │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                 │                                            │
│                          accountable to                                      │
│                                 ▼                                            │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  ACCOUNTABLE HUMAN                                                   │   │
│   │  user:jane.manager@acme.com                                         │   │
│   │  (Manager responsible for agent's actions)                          │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Chain Components

| Component | Role | Required |
|-----------|------|----------|
| **Agent** | Performs the action | Yes |
| **Delegator** | Provides authority | No (bot mode) |
| **Accountable** | Responsible human | Yes |

---

## Manager Relationship

### Accountable as Manager

The accountable human is typically the **manager** of the agent:

| Responsibility | Description |
|----------------|-------------|
| **Oversight** | Monitor agent performance and behavior |
| **Approval** | Approve agent deployment and changes |
| **Escalation** | Receive escalations for agent issues |
| **Remediation** | Address agent failures or violations |

### Manager Notifications

The accountable human receives notifications for:

| Event | Notification |
|-------|--------------|
| **Agent Deployed** | Deployment confirmation |
| **Authority Change** | When delegator's authority changes |
| **Policy Violation** | When agent violates policy |
| **Kill Switch** | When agent is killed |
| **Budget Alert** | When budget thresholds are reached |

---

## Audit Trail

### CAF Integration

All agent actions are logged to CAF with accountability chain:

```json
{
  "event": "agent_action",
  "timestamp": "2026-01-12T14:30:00Z",
  
  "agent": {
    "id": "fraud-analyst-acme-retail",
    "spiffeId": "spiffe://acme.hub.io/seer/agent/acme-seer-subscription/fraud-analyst-acme-retail"
  },
  
  "accountability": {
    "delegator": "user:john.smith@acme.com",
    "accountable": "user:jane.manager@acme.com"
  },
  
  "action": {
    "type": "request_completed",
    "requestId": "req-12345",
    "scenario": "fraud-investigation"
  },
  
  "outcome": {
    "status": "success",
    "decision": "fraud_confirmed"
  }
}
```

### Audit Requirements

| Requirement | Implementation |
|-------------|----------------|
| **Agent identification** | SPIFFE ID + agent code |
| **Delegation chain** | Delegator + accountable |
| **Action details** | Request ID, scenario, action type |
| **Timestamp** | ISO 8601 with timezone |
| **Outcome** | Status and decision |

### Audit Retention

| Audit Type | Retention | Storage |
|------------|-----------|---------|
| **Normal operations** | 90 days | CAF |
| **Policy violations** | 7 years | CAF + Archive |
| **Kill switch events** | 7 years | CAF + Archive |

---

## Accountable Human Changes

### When Accountable Changes

If the accountable human needs to change:

1. **Update EmploymentSpec** — Modify `delegation.accountable`
2. **Seer Operator Detects** — Operator watches for changes
3. **Profile Update** — Cipher IAM profile updated
4. **Notification** — Both old and new accountable notified

### Change Audit

```json
{
  "event": "accountability_changed",
  "timestamp": "2026-01-12T15:00:00Z",
  "agent": "fraud-analyst-acme-retail",
  "previous_accountable": "user:jane.manager@acme.com",
  "new_accountable": "user:bob.supervisor@acme.com",
  "changed_by": "user:admin@acme.com",
  "reason": "Manager transfer"
}
```

---

## Bot Mode Accountability

### Accountable Required Even for Bots

Even bot-mode agents require an accountable human:

```yaml
spec:
  delegation:
    type: bot
    accountable: "user:jane.manager@acme.com"  # Still required
    # No delegator for bot mode
```

### Bot Mode Differences

| Aspect | User/Role Delegation | Bot Mode |
|--------|---------------------|----------|
| **Delegator** | Required | None |
| **Accountable** | Required | Required |
| **Authority Source** | Delegator | Explicit assignment |
| **Audit Chain** | Agent → Delegator → Accountable | Agent → Accountable |

---

## Accountability Reporting

### Manager Dashboard

Accountable humans can view their agents:

| View | Content |
|------|---------|
| **Agent List** | All agents they're accountable for |
| **Activity Summary** | Recent actions by their agents |
| **Violation Alerts** | Any policy violations |
| **Budget Status** | Budget usage by agent |

### Compliance Reports

Reports available for compliance:

| Report | Frequency | Content |
|--------|-----------|---------|
| **Agent Activity** | Daily | All actions by accountable's agents |
| **Policy Violations** | Real-time | Any violations |
| **Delegation Audit** | Weekly | Authority changes |

---

## Related Documentation

- [Authority Delegation](./authority-delegation.md) — Delegation model
- [Agent Profile API](./agent-profile-api.md) — Profile management
- [CAF Integration](../../../../olympus-hub-docs/04-subsystems/caf/README.md) — Audit logging

---

*Human Accountability ensures every agent action has a responsible human in the accountability chain.*
