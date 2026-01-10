# 3.5 Cipher IAM Integration

Seer's identity and authority capabilities are built in partnership with Cipher, Olympus's identity and access management system. This section clarifies the division of responsibilities and integration patterns.

## Division of Responsibilities

### What Seer Defines

Seer defines the **agent identity framework**:

| Seer Responsibility | Description |
|---------------------|-------------|
| **Agent Identity Semantics** | What agent identity means (Raw, Trained, Employed layers) |
| **Delegation Model** | How authority flows from humans to agents |
| **Authority Ceilings** | Layered limits and their semantics |
| **Kill Switch Logic** | When and how to revoke authority |
| **Integration Patterns** | How agents authenticate and authorize |

### What Cipher Provides

Cipher provides the **identity infrastructure**:

| Cipher Responsibility | Description |
|----------------------|-------------|
| **Principal Storage** | Registry of all identities (users, services, agents) |
| **Credential Issuance** | Creating and managing tokens, keys, certificates |
| **Policy Evaluation** | OPA-based policy enforcement |
| **PEP Infrastructure** | Policy Enforcement Points across systems |
| **Audit Infrastructure** | Logging all identity operations |

## Agent Registration in Cipher

### Enrollment Process

Agents are enrolled in Cipher at each lifecycle stage:

```
Raw Agent Deployed
    ↓
Register in Cipher with infrastructure identity (SPIFFE)
    ↓
Training Spec Applied
    ↓
Register application identity
    ↓
Employment Spec Applied
    ↓
Register workforce/customer identity
    ↓
Grant delegated authority
```

### Registration Records

Cipher maintains agent records:

```json
{
  "principal": "dispute-analyst-bot@workforce.acme.com",
  "type": "employed_agent",
  "tenant": "acme",
  "training_spec": "dispute-analyst-training:v1.7.0",
  "employment_spec": "dispute-analyst-acme-production:v3.2.0",
  "delegation": {
    "from": "dispute-analyst-role",
    "manager": "sarah.chen@acme.com",
    "authority": ["dispute:*", "refund:request"],
    "ceilings": {
      "maxDecisionValue": 5000
    }
  },
  "status": "active",
  "created": "2026-01-10T14:00:00Z"
}
```

## Authentication Flow

### Agent → System Authentication

When an agent accesses a system:

```
Agent presents credentials (token/SVID)
    ↓
System validates with Cipher
    ↓
Cipher returns:
  - Principal identity
  - Delegation chain
  - Current authority
  - Ceiling limits
    ↓
System applies authorization
```

### Credential Types

| Context | Credential Type |
|---------|-----------------|
| **Within Kubernetes** | SPIFFE SVID |
| **Hub Services** | OAuth Bearer Token |
| **External APIs** | Per-service credentials |
| **Human Interaction** | Session-bound token |

## Authorization Flow

### Policy Enforcement

Every agent action goes through Cipher PEPs:

```
Agent requests: "Approve refund $750 for customer X"
    ↓
PEP extracts:
  - Agent identity
  - Requested action
  - Resource (customer X)
  - Context (amount, time, etc.)
    ↓
PEP queries Cipher:
  - Is agent authorized for action?
  - What are the ceiling limits?
  - Is delegator still authorized?
    ↓
PEP applies OPA policy
    ↓
Allow, Deny, or Route to Approval
```

### Policy Composition

Policies combine multiple sources:

```rego
package seer.authorization

# Final decision combines all sources
allow {
    org_policy_allows
    training_ceiling_allows
    employment_ceiling_allows
    delegator_still_authorized
    not kill_switch_active
}
```

## Delegation Chain Verification

### Real-Time Verification

Cipher verifies delegation chains in real-time:

```
Agent requests action
    ↓
Cipher traces delegation:
  Agent ← Role ← Role Assignment ← IT Admin
    ↓
Cipher verifies each link:
  - Agent: active, not killed
  - Role: still assigned to agent
  - Role Assignment: still valid
  - IT Admin: still authorized
    ↓
If any link broken → Deny
```

### Authority Inheritance

When a delegator's authority changes:

```
Sarah loses "refund:approve" permission
    ↓
Cipher updates delegation graph
    ↓
All agents delegated from Sarah:
  - Immediately lose "refund:approve"
  - No manual intervention needed
```

## Multi-Tenant Support

### Tenant Isolation

Cipher provides tenant isolation for agent identity:

- Agents in one tenant cannot authenticate as another tenant's agent
- Cross-tenant access requires explicit federation
- Tenant-specific policies apply automatically

### Sandbox Support

Within a tenant, Cipher supports sandboxes:

```yaml
# Agent can only access its designated sandbox
agentScope:
  tenant: acme
  sandbox: disputes-production
  accessibleSandboxes:
    - disputes-production
    - disputes-staging  # if needed
```

## Integration Patterns

### SDKs

Cipher provides SDKs for agent integration:

```python
from cipher import CipherClient

# Agent authenticates
cipher = CipherClient.from_environment()
token = cipher.get_agent_token()

# Agent checks authority
if cipher.is_authorized("refund:approve", amount=750):
    process_refund()
else:
    request_approval()
```

### Sidecars

For non-SDK environments, Cipher provides sidecars:

```yaml
# Cipher sidecar in agent pod
containers:
  - name: agent
    # Agent container
  - name: cipher-sidecar
    image: cipher/pep-sidecar
    # Intercepts and authorizes requests
```

---

**References:**
*   `olympus-hub-docs/04-subsystems/supporting-systems/cipher-iam.md`
*   `olympus-seer-docs/seer-design/subsystems/agent-identity-authority.md`
