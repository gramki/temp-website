# Human Accountability

> **Category:** Platform Foundation  
> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-15

---

## Overview

Human Accountability ensures that every agent action has a responsible human in the accountability chain. It implements the RASCI (Responsible, Accountable, Supporting, Consulted, Informed) framework where **humans are always Accountable** and agents can be **Responsible**. This principle is fundamental to enterprise agent governance, regulatory compliance, and auditability.

---

## Ontology Context

### Relationship to Ontology

Human Accountability implements the **RASCI Accountability** principle from AOSM:

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|-------------|
| **RASCI Accountability** | Accountable human assignment, accountability chain | Humans are Accountable; agents are Responsible |
| **Controlled Autonomy** | Accountable humans set autonomy boundaries | Accountability enables controlled autonomy |
| **Directability** | Accountable humans can override agent actions | Accountability enables directability |
| **Audit Trail** | Complete accountability chain in CAF | Accountability requires auditability |

### Gap This Fills

The AOSM ontology defines RASCI but doesn't specify how to implement human accountability in practice. Human Accountability fills this gap by providing:

1. **Mandatory Accountable Human**: Every Employed Agent must have designated accountable human
2. **Accountability Chain**: Complete chain from agent action to accountable human
3. **Audit Trail**: All actions recorded with accountability context
4. **Override Authority**: Accountable humans can override agent actions
5. **Regulatory Compliance**: Meets requirements for human accountability in regulated industries

---

## Definition

**Human Accountability** is the principle that every agent action must have a responsible human in the accountability chain. In the RASCI framework, agents can be **Responsible** (execute the work), but **Accountable** (bear risk and consequences) must always be a human. Every Employed Agent must have a designated accountable human who is responsible for the agent's actions.

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Per Employed Agent (accountable human specified in EmploymentSpec) |
| **Lifecycle** | Assigned at Employment Spec creation; can be changed; recorded in audit trail |
| **Ownership** | Agent Product Owner (APO) assigns accountable human; Cognitive Operations Steward (COS) manages governance |
| **Multiplicity** | One accountable human per Employed Agent; one human can be accountable for multiple agents |

---

## Rationale

### Why This Design?

**RASCI Framework**:
- **Accountable (A)**: Must be human (bears risk, justifies decisions)
- **Responsible (R)**: Can be agent (executes the work)
- Agents cannot be Accountable (cannot bear legal responsibility, testify to regulators)

**Regulatory Compliance**:
- Regulated industries require human accountability
- Audit trails must identify accountable humans
- Evidence production requires accountability chain

**Governance and Oversight**:
- Accountable humans monitor agent performance
- Accountable humans receive notifications for agent events
- Accountable humans can override agent actions

**Audit Trail**:
- All agent actions recorded with accountability chain
- Complete traceability from action to accountable human
- Required for regulatory compliance

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **No Accountability** | Regulatory requirement; agents cannot be accountable |
| **Optional Accountability** | Mandatory for enterprise governance; optional is insufficient |
| **Role-Based Accountability** | Must be specific human; roles are not sufficient for legal accountability |

### Related ADRs

| ADR | Decision |
|-----|----------|
| *To be added* | *Human accountability architecture decisions* |

---

## Structure

### Key Attributes

```yaml
# Conceptual accountability structure
accountability:
  agent_id: string
  accountable:
    human: string  # user:...
    relationship: string  # manager, owner, supervisor
    assigned_at: timestamp
    assigned_by: string  # user:...
  
  delegation_chain:
    delegator: string  # Optional: user:... or role:...
    accountable: string  # Required: user:...
  
  audit:
    actions_recorded: boolean
    accountability_chain_in_caf: boolean
    override_authority: boolean
```

### States

| State | Description | Transitions |
|-------|-------------|-------------|
| **Assigned** | Accountable human assigned | → Changed |
| **Changed** | Accountable human changed | → Assigned |
| **Active** | Accountable human active | → Inactive (if user deactivated) |

---

## Behavior

### How It Works

#### Accountability Chain Creation

```
1. EmploymentSpec created with delegation.accountable field
2. Accountable human validated (must be user identity, must exist, must be active)
3. Accountability chain established (Agent → Delegator → Accountable)
4. IAM profile created with accountable human reference
5. Audit trail initialized
```

#### Agent Action Accountability

```
1. Agent performs action (decision, tool invocation, etc.)
2. Action logged to CAF with accountability chain
3. Accountability chain includes:
   - Agent ID and SPIFFE ID
   - Delegator (if user/role delegation)
   - Accountable human
   - Action details (request ID, scenario, type)
   - Timestamp and outcome
```

#### Accountable Human Notifications

```
1. Agent event occurs (deployment, authority change, violation, kill switch)
2. Notification sent to accountable human
3. Accountable human can:
   - Review agent activity
   - Override agent actions
   - Escalate issues
   - Request kill switch
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| **EmploymentSpec** | ← | Accountable human specified in delegation.accountable |
| **Cipher IAM Extensions** | → | Accountable human recorded in IAM profile |
| **CAF (Cognitive Audit Fabric)** | → | All actions logged with accountability chain |
| **Agent Directory** | ↔ | Accountable human visible in agent profile |
| **Notification Service** | → | Accountable human receives agent event notifications |
| **Kill Switch** | ← | Accountable human can activate kill switch |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Mandatory** | Every Employed Agent must have accountable human |
| **Must Be Human** | Accountable must be user identity, not role or agent |
| **Must Exist** | Accountable human identity must exist in Cipher IAM |
| **Must Be Active** | Accountable human account must be active |
| **Audit Required** | All agent actions must be logged with accountability chain |
| **Override Authority** | Accountable humans can override agent actions |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Regulatory Compliance** | Meets requirements for human accountability |
| ✅ **Complete Audit Trail** | All actions traceable to accountable human |
| ✅ **Governance** | Accountable humans provide oversight |
| ✅ **Legal Protection** | Humans bear legal responsibility, not agents |
| ✅ **Override Authority** | Accountable humans can control agent behavior |
| ✅ **Notification System** | Accountable humans informed of agent events |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Accountable Human Assignment** | Clear guidelines for assigning accountable humans |
| ⚠️ **Notification Overload** | Configurable notification preferences |
| ⚠️ **Accountability Changes** | Change process with audit trail |
| ⚠️ **Bot Mode Accountability** | Even bot-mode agents require accountable human |

---

## Examples

### Example 1: User Delegation Accountability

**Use Case**: Personal assistant agent with user delegation

```yaml
# EmploymentSpec
spec:
  delegation:
    type: user
    delegator: "user:john.smith@acme.com"
    accountable: "user:jane.manager@acme.com"  # Manager accountable
```

**Accountability Chain**:
```
fraud-analyst-acme-retail (Agent) - Responsible
    ↓ delegated by
user:john.smith@acme.com (Delegator)
    ↓ accountable to
user:jane.manager@acme.com (Accountable Human)
```

**Behavior**: Agent actions logged with full accountability chain. Accountable human (jane.manager) receives notifications and can override.

---

### Example 2: Role Delegation Accountability

**Use Case**: Team-level agent with role delegation

```yaml
spec:
  delegation:
    type: role
    delegator: "role:fraud-analyst"
    accountable: "user:sarah.team-lead@acme.com"  # Team lead accountable
```

**Accountability Chain**:
```
dispute-processor-bot (Agent) - Responsible
    ↓ delegated by
role:fraud-analyst (Delegator Role)
    ↓ accountable to
user:sarah.team-lead@acme.com (Accountable Human)
```

**Behavior**: Agent actions logged with role delegation and accountable human. Team lead receives notifications.

---

### Example 3: Bot Mode Accountability

**Use Case**: Fully automated agent with bot mode

```yaml
spec:
  delegation:
    type: bot
    accountable: "user:ops-manager@acme.com"  # Still required
    # No delegator for bot mode
```

**Accountability Chain**:
```
payment-processor-bot (Agent) - Responsible
    ↓ (no delegator - bot mode)
    ↓ accountable to
user:ops-manager@acme.com (Accountable Human)
```

**Behavior**: Even bot-mode agents require accountable human. Ops manager receives notifications and can override.

---

### Example 4: Accountability in Audit Trail

**Use Case**: Agent action logged with accountability chain

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
    "scenario": "fraud-investigation",
    "decision": "fraud_confirmed"
  },
  
  "outcome": {
    "status": "success"
  }
}
```

**Behavior**: Complete accountability chain recorded in CAF. Regulators can trace action to accountable human.

---

## Implementation Notes

### For Developers

- **Accountable Field**: Always include `delegation.accountable` in EmploymentSpec
- **Validation**: Validate accountable human exists and is active before creating EmploymentSpec
- **Audit Integration**: All agent actions must include accountability chain in CAF logs
- **Notification Integration**: Send notifications to accountable human for agent events

### For Operators

- **Accountable Human Assignment**: Assign appropriate accountable human (typically manager or supervisor)
- **Accountability Changes**: Update EmploymentSpec when accountable human changes; notify both old and new accountable
- **Audit Review**: Review accountability audit trail regularly for compliance
- **Notification Management**: Configure notification preferences for accountable humans

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Delegation Chains](./delegation-chains.md) | Accountability chain includes delegation chain |
| [Agent Lifecycle](./agent-lifecycle.md) | Accountable human assigned at Employment |
| [Kill Switch & Emergency Controls](./kill-switch-emergency-controls.md) | Accountable humans can activate kill switches |
| [Agent Levers](./agent-levers.md) | Accountable humans can operate agent levers |

---

## References

- [Human Accountability](../subsystems/cipher-iam-extensions/human-accountability.md) — Implementation details
- [Agent Profile API](../subsystems/cipher-iam-extensions/agent-profile-api.md) — Accountable human in profile
- [AOSM Meta-Model](../../../aosm-meta-model/agent-oriented-system.md) — RASCI framework
- [Why Seer: Accountability Gap](../../why-seer/part-1-background/02-why-enterprise-agents-different/02-2-accountability-gap.md) — Conceptual foundation
- [CAF Integration](../../../olympus-hub-docs/04-subsystems/caf/README.md) — Audit logging

---

*Human Accountability ensures every agent action has a responsible human in the accountability chain, meeting regulatory requirements and enabling proper governance and oversight.*
