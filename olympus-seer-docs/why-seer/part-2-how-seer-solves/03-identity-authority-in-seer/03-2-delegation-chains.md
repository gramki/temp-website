# 3.2 Delegation Chains

When an agent acts, a fundamental question arises: *Under whose authority?* Seer implements traceable delegation chains that answer this question at any point in an agent's operation.

## What Delegation Chains Capture

A delegation chain records:

1. **Who delegated:** The principal (user, role, or Scenario Identity Profile) that granted authority
2. **To whom:** The Agent Persona receiving authority (not the deployment infrastructure)
3. **What authority:** The specific permissions delegated
4. **When:** The time bounds of the delegation
5. **Under what conditions:** Constraints on the delegation

### Persona-Based Tracking

Delegation chains track **Agent Persona** (business identity), not Deployment Identity (SPIFFE). This ensures:

- **Business Accountability**: Audit logs attribute actions to personas, not infrastructure
- **Consistency Across Deployments**: Same persona maintains same delegation chain regardless of which pod serves the request
- **Survival Through Redeployments**: Delegation chains persist when pods are recreated

The Deployment Identity (SPIFFE) is used for infrastructure authentication (mTLS, service mesh), but delegation chains operate at the business layer, tracking who authorized the Agent Persona to act.

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

Every delegation is recorded with Agent Persona as the recipient:

```json
{
  "event": "delegation_created",
  "delegator": "dispute-scenario-profile",  // Scenario Identity Profile or Business User
  "agent_persona": "dispute-analyst-agent@acme.hub.io",  // Agent Persona (business identity)
  "deployment_identity": "spiffe://acme.hub.io/seer/agent/acme/analyst-pod-001",  // Deployment Identity (for infrastructure context)
  "authority": ["dispute:read", "dispute:resolve", "refund:request"],
  "constraints": {
    "maxValue": 500,
    "scenarios": ["dispute-resolution"]
  },
  "timestamp": "2026-01-10T14:00:00Z",
  "expiry": null
}
```

The audit record includes both identities for complete traceability, but the delegation chain itself tracks the Agent Persona as the business entity receiving authority.

### Chain Verification

At any time, the full delegation chain can be verified:

```
Action: Refund $200 to customer
Actor: dispute-analyst-agent@acme.hub.io (Agent Persona)
Deployment: spiffe://acme.hub.io/seer/agent/acme/analyst-pod-001 (Deployment Identity)
    ↓
Delegated by: dispute-scenario-profile (Scenario Identity Profile)
    ↓
Scenario owned by: Dispute Operations Team
    ↓
Manager (Accountable): Sarah Chen
```

The chain tracks the Agent Persona through the business hierarchy, while the Deployment Identity provides infrastructure context but does not appear in the delegation chain itself.

### Regulatory Response

When regulators ask "who authorized this agent to take this action?", the answer is immediately available:

- The delegation chain is immutable
- All links are cryptographically verifiable
- The accountable human is identified

## Multi-Agent Delegation

When agents delegate to other agents:

### Chain Extension

```
Alice (Business User)
    ↓ delegates to
Orchestrator Agent Persona
    ↓ delegates to
Specialist Agent Persona
```

Each link in the chain tracks Agent Personas, ensuring business accountability throughout the delegation hierarchy.

### Composite Application Sub-Personas

In Hub Composite Applications, each agent in the composite receives its own **sub-persona** derived from the base Agent Persona:

```
Base Agent Persona: dispute-resolution-agent@acme.hub.io
    ↓
Composite Application creates:
    ├── Sub-Persona: dispute-analyst-agent (derived from base)
    ├── Sub-Persona: dispute-reviewer-agent (derived from base)
    └── Sub-Persona: dispute-approver-agent (derived from base)
```

Each sub-persona has its own distinct identity for delegation and audit, but all derive from the same base Agent Persona. This enables:
- **Individual Accountability**: Each agent's actions are attributed to its specific sub-persona
- **Shared Authority Source**: All sub-personas inherit from the same base delegation
- **Audit Clarity**: Composite application actions can be traced to specific sub-personas while maintaining the base persona context

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

---

**References:**
*   `aosm-meta-model/raw-trained-employed-agents.md` — Section 3.3 on delegation
*   `olympus-seer-docs/seer-design/subsystems/authority-enforcement.md`
*   `olympus-hub-docs/decision-logs/0129-agent-identity-model.md` — Two-layer identity model
*   Section 8.1 (Agent Identity) — Identity model context
*   Section 8.6 (Request-Scoped Authority Delegation) — Request-scoped delegation model