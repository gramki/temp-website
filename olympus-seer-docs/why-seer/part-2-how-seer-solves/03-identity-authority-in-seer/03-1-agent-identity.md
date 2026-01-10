# 3.1 Agent Identity

Enterprise agents require identity that is distinct from the identity of the users they serve or the services they invoke. Seer provides a comprehensive agent identity framework that makes agents first-class principals with verifiable credentials.

## Why Agents Need Their Own Identity

### Beyond Caller Identity

Traditional systems authenticate users and services. Agents introduce a new entity type that requires its own identity:

| Identity Type | Example | Limitation for Agents |
|---------------|---------|----------------------|
| **User Identity** | alice@acme.com | Agent is not a user |
| **Service Identity** | payments-api | Agent is not a backend service |
| **Workload Identity** | pod-12345 | Too infrastructure-focused |

Agents need identity that captures:
- Who the agent is (not just what container it runs in)
- What authority it has been delegated
- Who is accountable for its actions

### Accountability Requirements

When an agent acts, regulators and auditors ask: *Who authorized this?* Agent identity must provide:
- Clear identification of the acting agent
- Traceable delegation chain to accountable humans
- Verifiable credentials that cannot be forged

## Seer's Agent Identity Model

### Identity Layers

Seer implements identity at multiple layers:

| Layer | Identity Type | Purpose |
|-------|---------------|---------|
| **Raw Agent** | Infrastructure identity (SPIFFE) | Platform-level authentication |
| **Trained Agent** | Application identity | Tenant-level identification |
| **Employed Agent** | Workforce/Customer IAM | Delegation and authority |

### Employed Agent Identity

When an agent is employed, it receives identity in the appropriate IAM domain:

**Workforce IAM (Role Delegation)**
```
Agent acts as: dispute-analyst-bot@workforce.acme.com
Delegation from: Dispute Analyst role
Manager (Accountable): sarah.chen@acme.com
```

**Customer IAM (User Delegation)**
```
Agent acts as: alice-assistant@customers.acme.com
Delegation from: alice@acme.com
Authority: Subset of Alice's permissions
```

### Cryptographically Verifiable

Agent identity is cryptographically verifiable:

- **SPIFFE SVIDs:** Raw agents receive SPIFFE identity
- **OAuth Tokens:** Employed agents receive scoped tokens
- **Signed Credentials:** All credentials are cryptographically signed

Verification is possible at any point in the request chain.

## Identity Lifecycle

### Creation

Agent identity is created as part of employment:

```yaml
# Employment triggers identity creation
apiVersion: seer.olympus.io/v1
kind: EmploymentSpec
metadata:
  name: dispute-analyst-acme
spec:
  identity:
    domain: workforce
    principal: dispute-analyst-bot
    manager: sarah.chen@acme.com
```

### Rotation

Credentials are rotated automatically:

| Credential Type | Rotation Frequency |
|-----------------|-------------------|
| **SPIFFE SVID** | Hours (configurable) |
| **OAuth Tokens** | Hours to days |
| **API Keys** | Days to months |

Rotation is transparent to the agent and its callers.

### Revocation

Revocation is immediate when triggered:

- Kill switch triggers immediate revocation
- Employment termination revokes identity
- Security incidents can trigger emergency revocation

All revocation events are logged to CAF.

## Identity Resolution

### At Request Time

When an agent makes a request, its identity is resolved:

```
Request arrives
    ↓
Extract agent credentials
    ↓
Verify credentials with Cipher
    ↓
Resolve identity to principal
    ↓
Check delegation chain
    ↓
Verify authority for action
```

### Across Systems

Agent identity is consistent across all systems:

- Hub recognizes the agent's identity
- External tools receive verifiable credentials
- Audit records include full identity information

## Identity Governance

### Registration

Agents must be registered in Cipher:

- Raw Agents registered with infrastructure identity
- Trained Agents registered with application identity
- Employed Agents registered with workforce/customer identity

### Groups and Roles

Employed Agents can participate in IAM groups:

```yaml
identity:
  principal: fraud-analyst-bot
  groups:
    - fraud-team
    - tier-1-responders
  roles:
    - fraud-analyst
```

### Audit

All identity operations are audited:

- Identity creation and modification
- Credential rotation
- Delegation changes
- Access attempts (success and failure)

---

**References:**
*   `olympus-seer-docs/seer-design/subsystems/agent-identity-authority.md`
*   `olympus-hub-docs/04-subsystems/supporting-systems/cipher-iam.md`
