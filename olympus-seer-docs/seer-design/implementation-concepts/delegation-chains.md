# Delegation Chains

> **Category:** Platform Foundation  
> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-15

---

## Overview

Delegation Chains define how authority flows from humans to agents in Seer. They establish traceable, auditable chains of authority delegation where agents inherit permissions from delegators (users or roles) and operate under the accountability of designated humans. Delegation chains implement the Controlled Autonomy principle by ensuring agents can only act within the authority granted by their delegators.

**Identity Model**: Delegation chains track **Agent Persona** (business identity), not Deployment Identity (SPIFFE). The Deployment Identity is the OAuth Client equivalent used for infrastructure authentication. The Agent Persona is the business identity that receives delegated authority.

**Delegation Modes**: Delegation can be **scenario-scoped** (authority from Scenario Identity Profile) or **request-scoped** (authority from Business User consent). Both use the same unified mechanism with different modes. See [ADR-0130: Unified Delegation Model](../../../olympus-hub-docs/decision-logs/0130-unified-delegation-model.md).

---

## Ontology Context

### Relationship to Ontology

Delegation Chains implement the **Controlled Autonomy** and **RASCI Accountability** principles from AOSM:

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|-------------|
| **Controlled Autonomy** | Authority delegation with narrowing-only principle | Agents operate within delegated authority bounds |
| **RASCI Accountability** | Accountable human assignment, delegation traceability | Humans remain accountable; agents are Responsible |
| **Authority** | Delegation types, inheritance algorithms | Authority flows through delegation chains |
| **Four Components of Autonomy** | Authority component implemented via delegation | Delegation provides the Authority component |
| **Directability** | Authority revocation, delegation constraints | Delegations can be revoked, enabling directability |

### Gap This Fills

The AOSM ontology defines Controlled Autonomy and RASCI but doesn't specify how authority is delegated and inherited in practice. Delegation Chains fill this gap by providing:

1. **Explicit Delegation Model**: Clear specification of who delegates what authority to whom
2. **Real-Time Inheritance**: Agent authority automatically shrinks when delegator authority shrinks
3. **Narrowing-Only Principle**: Each link in the chain can only narrow, never expand authority
4. **Traceability**: Complete audit trail of delegation chain from agent to ultimate authority
5. **Accountability**: Designated accountable humans for each agent

---

## Definition

**Delegation Chains** are traceable sequences of authority delegation from humans (or roles) to **Agent Personas**, where each agent persona inherits a subset of its delegator's authority and operates under the accountability of a designated human. Delegation chains implement narrowing-only inheritance, real-time synchronization, and complete auditability.

**Note**: Delegation chains track **Agent Persona** (business identity), not Deployment Identity (SPIFFE). The Deployment Identity is the OAuth Client equivalent used for infrastructure authentication. The Agent Persona is the business identity that receives delegated authority.

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Per Employed Agent (delegation specified in EmploymentSpec) |
| **Lifecycle** | Created when EmploymentSpec created; updated when delegator authority changes; revoked on kill switch |
| **Ownership** | Agent Product Owner (APO) defines delegation; Cognitive Operations Steward (COS) manages governance |
| **Multiplicity** | One delegation chain per Employed Agent; multiple agents can delegate from same delegator |

---

## Rationale

### Why This Design?

**Three Delegation Types**:
- **User Delegation**: Personal assistant agents acting on behalf of specific users
- **Role Delegation**: Team-level agents representing organizational roles
- **Bot Mode**: Fully automated agents with base identity only

**Real-Time Inheritance**:
- Agent authority automatically shrinks when delegator authority shrinks
- No manual intervention required
- Ensures agents always operate within current delegator authority

**Narrowing-Only Principle**:
- Each link in chain can only narrow, never expand authority
- Prevents authority escalation
- Training Spec ceilings cannot be relaxed in Employment Spec

**Accountability Model**:
- Every agent has designated accountable human
- Accountable human is separate from delegator
- Enables RASCI model (humans Accountable, agents Responsible)

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Static Delegation** | Real-time inheritance ensures security; static delegation is error-prone |
| **Expanding Authority** | Narrowing-only prevents authority escalation; expanding would violate security model |
| **No Accountability** | RASCI requires accountable humans; agents cannot be accountable |

### Related ADRs

| ADR | Decision |
|-----|----------|
| [ADR-0129: Agent Identity Model](../../../olympus-hub-docs/decision-logs/0129-agent-identity-model.md) | Two-layer identity model (Deployment Identity + Agent Persona) |
| [ADR-0130: Unified Delegation Model](../../../olympus-hub-docs/decision-logs/0130-unified-delegation-model.md) | Unified delegation model with scenario-scoped and request-scoped modes |

---

## Structure

### Key Attributes

```yaml
# Conceptual delegation chain structure
delegation_chain:
  agent_id: string
  delegation_type: user | role | bot
  
  # For User/Role Delegation
  delegator:
    identity: string  # user:... or role:...
    roles: string  # "*" or CSV list
    groups: string  # "*" or CSV list
  
  # For All Types
  accountable:
    human: string  # user:...
    relationship: string  # manager, owner, etc.
  
  # Authority Inheritance
  inherited_authority:
    roles: [string]
    groups: [string]
    ceilings:
      value: object
      rate: object
      scope: object
  
  # Constraints
  constraints:
    temporal_bounds:
      start: timestamp
      end: timestamp
    scope_restrictions:
      workbenches: [string]
      scenarios: [string]
  
  # Audit Trail
  audit:
    created_at: timestamp
    created_by: string
    last_updated: timestamp
    chain_verification: object
```

### States

| State | Description | Transitions |
|-------|-------------|-------------|
| **Active** | Delegation active, agent operating | → Revoked, → Suspended |
| **Suspended** | Delegation temporarily suspended | → Active, → Revoked |
| **Revoked** | Delegation revoked (kill switch) | (terminal) |

---

## Behavior

### How It Works

#### Delegation Chain Creation

```
1. EmploymentSpec created with delegation section
2. Delegation type determined (user, role, or bot)
3. Delegator identity resolved (if user/role delegation)
4. Inheritance algorithm executed (roles/groups)
5. Authority ceilings calculated (intersection of delegator + Training Spec)
6. Accountable human assigned
7. IAM profile created with delegated authority
8. Delegation chain recorded in audit trail
```

#### Real-Time Inheritance

```
1. IAM change occurs (delegator roles/groups changed)
2. IAM Observer Service detects change
3. Delegation Chain Sync Service identifies affected agents
4. New authority calculated (intersection of new delegator authority + existing ceilings)
5. Authority narrowed if delegator lost permissions
6. EmploymentSpec CRD updated
7. Agent respawned with new authority
8. Audit trail updated
```

#### Authority Evaluation

```
1. Agent requests action (tool invocation, decision, etc.)
2. Policy Enforcement Point (PEP) evaluates request
3. PEP checks agent's delegated authority
4. PEP checks delegator's current authority
5. Effective authority = intersection(agent authority, delegator authority)
6. PEP checks authority ceilings (Training Spec, Employment Spec)
7. If all checks pass: Allow
8. If any check fails: Deny
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| **Cipher IAM Extensions** | ↔ | Creates IAM profiles, validates delegator authority |
| **IAM Observer Service** | ← | Detects IAM changes, triggers delegation sync |
| **Delegation Chain Sync Service** | → | Syncs authority changes to agents |
| **Seer Operator** | → | Updates EmploymentSpec CRDs on authority changes |
| **Agent Runtime** | → | Respawning agents with updated authority |
| **Policy Enforcement Points** | → | Evaluates delegated authority on requests |
| **Seer Sidecar** | → | Enforces authority ceilings at runtime |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Narrowing-Only** | Each link in chain can only narrow, never expand authority |
| **Real-Time Inheritance** | Agent authority automatically shrinks when delegator authority shrinks |
| **Accountable Human Required** | Every agent must have designated accountable human |
| **Delegator Validation** | Delegator identity must exist and be valid |
| **Authority Intersection** | Effective authority = intersection(agent authority, delegator authority) |
| **Ceiling Immutability** | Training Spec ceilings cannot be relaxed in Employment Spec |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Traceable Authority** | Complete audit trail from agent to ultimate authority |
| ✅ **Real-Time Security** | Authority automatically shrinks with delegator changes |
| ✅ **Prevents Escalation** | Narrowing-only principle prevents authority escalation |
| ✅ **RASCI Compliance** | Accountable humans ensure proper accountability model |
| ✅ **Flexible Delegation** | Three delegation types support different use cases |
| ✅ **Auditable** | All delegations recorded with full context |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Respawning Overhead** | Authority changes are infrequent; respawning ensures security |
| ⚠️ **Delegation Complexity** | Clear documentation and examples for common patterns |
| ⚠️ **Real-Time Sync Latency** | IAM Observer Service provides fast change detection |
| ⚠️ **Accountability Assignment** | Clear guidelines for assigning accountable humans |

---

## Examples

### Example 1: User Delegation

**Use Case**: Personal assistant agent acting on behalf of a user

```yaml
# EmploymentSpec
spec:
  delegation:
    type: user
    delegator: "user:john.smith@acme.com"
    accountable: "user:jane.manager@acme.com"
    roles: "*"  # All of john.smith's roles
    groups: "*" # All of john.smith's groups
```

**Delegation Chain**:
```
fraud-analyst-acme-retail (Agent)
    ↓ delegates from
user:john.smith@acme.com (Delegator)
    Roles: [fraud-reviewer, dispute-handler, case-closer]
    Groups: [disputes-team, fraud-analysts]
    ↓ accountable to
user:jane.manager@acme.com (Accountable Human)
```

**Behavior**: Agent inherits all of `john.smith`'s roles and groups. If `john.smith` loses `fraud-reviewer` role, agent automatically loses that role and respawns.

---

### Example 2: Role Delegation

**Use Case**: Team-level agent representing organizational role

```yaml
spec:
  delegation:
    type: role
    delegator: "role:fraud-analyst"
    accountable: "user:sarah.team-lead@acme.com"
    roles: "*"  # All permissions from role
    groups: "fraud-analysts,disputes-team"
```

**Delegation Chain**:
```
dispute-processor-bot (Agent)
    ↓ delegates from
role:fraud-analyst (Delegator Role)
    Permissions: [review-disputes, approve-refunds, escalate-cases]
    ↓ accountable to
user:sarah.team-lead@acme.com (Accountable Human)
```

**Behavior**: Agent inherits all permissions from `fraud-analyst` role. If role permissions change, agent authority updates automatically.

---

### Example 3: Bot Mode

**Use Case**: Fully automated agent with base identity only

```yaml
spec:
  delegation:
    type: bot
    accountable: "user:ops-manager@acme.com"
    roles: "automated-processor"  # Explicit roles only
    groups: "bots,automated-systems"
```

**Delegation Chain**:
```
payment-processor-bot (Agent)
    ↓ (no delegator - bot mode)
    Base Identity Only
    Roles: [automated-processor]
    Groups: [bots]
    ↓ accountable to
user:ops-manager@acme.com (Accountable Human)
```

**Behavior**: Agent has base identity with explicit roles only. No inheritance from delegator (no delegator exists).

---

### Example 4: Narrowing Authority

**Use Case**: Employment Spec narrows Training Spec authority

**Training Spec**:
```yaml
spec:
  authority:
    ceilings:
      value:
        maxSingleTransaction: 10000
        maxDailyTotal: 50000
```

**Employment Spec** (narrowing):
```yaml
spec:
  delegation:
    type: user
    delegator: "user:john.smith@acme.com"
    roles: "fraud-reviewer"  # Subset of delegator's roles
  authority:
    ceilings:
      value:
        maxSingleTransaction: 5000  # ✅ Narrower than 10000
        maxDailyTotal: 25000       # ✅ Narrower than 50000
```

**Behavior**: Agent inherits only `fraud-reviewer` role (even if delegator has more roles). Transaction limits are narrower than Training Spec (cannot exceed Training Spec limits).

---

## Implementation Notes

### For Developers

- **Inheritance Algorithms**: Use wildcard (`*`) for all roles/groups, or CSV list for subset
- **Authority Calculation**: Effective authority = intersection(agent authority, delegator authority)
- **Real-Time Sync**: IAM Observer Service detects changes; Delegation Chain Sync Service propagates
- **Audit Trail**: All delegation operations recorded with full context (who, what, when, why)

### For Operators

- **Delegation Configuration**: Configure in EmploymentSpec; validate delegator identity exists
- **Accountable Human Assignment**: Assign appropriate accountable human (typically manager)
- **Authority Monitoring**: Monitor delegation chain sync operations; verify authority changes propagate
- **Audit Review**: Review delegation audit trail for compliance

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Scenario-Scoped Delegation](./scenario-scoped-delegation.md) | Business user delegation with deployment-time authority |
| [Request-Scoped Delegation](./request-scoped-delegation.md) | Business user delegation with per-request consent |
| [Agent Identity & Credentials](./agent-identity-credentials.md) | Delegation chains create agent identity |
| [Authority Enforcement](./authority-enforcement.md) | Delegation chains provide authority for enforcement |
| [Agent Runtime](./agent-runtime.md) | Runtime respawns agents on authority changes |
| [Human Accountability](./human-accountability.md) | Delegation chains assign accountable humans |
| [Agent Lifecycle](./agent-lifecycle.md) | Delegation specified in Employment Spec |

---

## References

- [Authority Delegation](../subsystems/cipher-iam-extensions/authority-delegation.md) — Delegation model and inheritance algorithms
- [Delegation Chain Sync Service](../subsystems/agent-lifecycle-manager/delegation-chain-sync-service.md) — Authority change synchronization
- [IAM Observer Service](../subsystems/agent-lifecycle-manager/iam-observer-service.md) — IAM change detection
- [Agent Identity & Credentials](./agent-identity-credentials.md) — Identity creation from delegation
- [Why Seer: Delegation Chains](../../why-seer/part-2-how-seer-solves/03-identity-authority-in-seer/03-2-delegation-chains.md) — Conceptual foundation
- [Cipher IAM Extensions](../subsystems/cipher-iam-extensions/README.md) — IAM infrastructure

---

*Delegation Chains provide traceable, auditable authority flow from humans to agents, ensuring agents operate within Controlled Autonomy boundaries and RASCI accountability requirements.*
