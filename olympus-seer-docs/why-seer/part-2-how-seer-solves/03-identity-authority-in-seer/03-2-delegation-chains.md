# 3.2 Delegation Chains

When an agent acts, a fundamental question arises: *Under whose authority?* Seer implements traceable delegation chains that answer this question at any point in an agent's operation.

## What Delegation Chains Capture

A delegation chain records:

1. **Who delegated:** The principal (user or role) that granted authority
2. **To whom:** The agent receiving authority
3. **What authority:** The specific permissions delegated
4. **When:** The time bounds of the delegation
5. **Under what conditions:** Constraints on the delegation

## Delegation Models

### User Delegation

An agent acts as a delegate of a specific user:

```
Alice (VP Engineering, has permissions A, B, C, D)
    ↓ delegates
Alice's Assistant (granted A, B only)
```

**Characteristics:**
- Agent authority is subset of delegator's authority
- Identity derived from delegating user
- Authority shrinks if delegator's authority shrinks

### Role Delegation

An agent represents an organizational role:

```
Dispute Analyst Role
    ↓ delegates to
Dispute Analyst Bot
    ↓ managed by
Sarah Chen (Team Lead) — Accountable
```

**Characteristics:**
- Agent has role's permissions
- Must have designated manager (accountable human)
- Participates in IAM groups and role hierarchies

## Authority Inheritance

A critical security property: delegated authority is always a subset of what the delegator is currently authorized to do.

### Real-Time Inheritance

If Alice delegates to an agent and later loses permission B:
- The agent immediately loses access to B
- No manual intervention required
- Authority shrinks in real-time with delegator

### Implementation

Seer implements real-time inheritance through Cipher's Policy Enforcement Points (PEPs):

```
Agent requests action
    ↓
PEP checks agent's delegated authority
    ↓
PEP checks delegator's current authority
    ↓
Effective authority = intersection
    ↓
Allow or deny
```

## Traceability

### Audit Trail

Every delegation is recorded:

```json
{
  "event": "delegation_created",
  "delegator": "sarah.chen@acme.com",
  "agent": "dispute-analyst-bot@workforce.acme.com",
  "authority": ["dispute:read", "dispute:resolve", "refund:request"],
  "constraints": {
    "maxValue": 500,
    "scenarios": ["dispute-resolution"]
  },
  "timestamp": "2026-01-10T14:00:00Z",
  "expiry": null
}
```

### Chain Verification

At any time, the full delegation chain can be verified:

```
Action: Refund $200 to customer
Actor: dispute-analyst-bot
    ↓
Delegated by: Dispute Analyst role
    ↓
Role assigned by: IT Admin
    ↓
Manager (Accountable): Sarah Chen
```

### Regulatory Response

When regulators ask "who authorized this agent to take this action?", the answer is immediately available:

- The delegation chain is immutable
- All links are cryptographically verifiable
- The accountable human is identified

## Multi-Agent Delegation

When agents delegate to other agents:

### Chain Extension

```
Alice
    ↓ delegates to
Orchestrator Agent
    ↓ delegates to
Specialist Agent
```

### Authority Narrowing

Each link in the chain can only narrow authority:
- Orchestrator cannot grant more than Alice gave
- Specialist cannot receive more than Orchestrator has

### Depth Limits

Organizations can configure maximum delegation depth:

```yaml
delegationPolicy:
  maxDepth: 3  # Alice → Agent1 → Agent2 → Agent3
  requiresApproval:
    - depth: 2  # Second-level delegation requires approval
```

## Delegation Governance

### Approval Workflows

High-risk delegations require approval:

```yaml
delegationPolicy:
  requiresApproval:
    - authority: ["payment:execute"]
    - maxValue: "> 10000"
    - role: ["admin", "supervisor"]
```

### Time Bounds

Delegations can be time-limited:

```yaml
delegation:
  expiry: "2026-02-01T00:00:00Z"
  autoRenew: false
```

### Scope Restrictions

Delegations can be scoped to specific contexts:

```yaml
delegation:
  scope:
    workbench: acme-disputes
    scenarios: [dispute-resolution]
    customers: [enterprise-tier]
```

---

**References:**
*   `aosm-meta-model/raw-trained-employed-agents.md` — Section 3.3 on delegation
*   `olympus-seer-docs/seer-design/subsystems/authority-enforcement.md`
