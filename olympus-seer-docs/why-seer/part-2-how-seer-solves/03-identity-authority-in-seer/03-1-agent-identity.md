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

### The Two-Layer Identity Model

Seer implements **two-layer identity** for Employed Agents, clearly separating infrastructure concerns from business concerns:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         IDENTITY LAYERS                                     │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  BUSINESS/PERSONA LAYER (Agent Persona)                            │    │
│  │                                                                     │    │
│  │  • Derived from Scenario                                            │    │
│  │  • "Dispute Resolution Agent" — recognizable business persona         │    │
│  │  • Has authority delegated from Scenario's Identity Profile Owner │    │
│  │  • Used for: access tokens, audit, delegation chains              │    │
│  │  • Stored in: Cipher IAM (Scenario references it)                │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                   │                                         │
│                                   │ presents as                             │
│                                   ▼                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  INFRASTRUCTURE LAYER (Deployment Identity)                         │    │
│  │                                                                     │    │
│  │  • SPIFFE ID (OAuth Client equivalent)                             │    │
│  │  • "This pod running in this namespace in this cluster"           │    │
│  │  • Used for: mTLS, service mesh, infrastructure authN              │    │
│  │  • Acts as "client" presenting the Agent Persona                   │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Why Two Layers?

The separation of Deployment Identity from Agent Persona addresses fundamental differences in lifecycle, purpose, and accountability:

**Different Lifecycles**:
- **Deployment Identity**: Tied to pod lifecycle — created on deploy, rotated hourly, revoked on undeploy
- **Agent Persona**: Tied to Scenario lifecycle — survives redeployments, consistent across pod restarts

**Different Purposes**:
- **Deployment Identity (SPIFFE)**: Infrastructure authentication — proves "this request is coming from this specific agent deployment"
- **Agent Persona**: Business authorization — represents "who is accountable for this action" in business terms

**OAuth Client Analogy**:
The two-layer model aligns with standard OAuth 2.0 patterns:
- **Deployment Identity = OAuth Client**: The infrastructure entity (like a browser or mobile app) that makes requests
- **Agent Persona = OAuth Principal**: The business entity (like a user account) on whose behalf actions are taken
- The deployment presents tokens on behalf of the persona, just as an OAuth client presents tokens on behalf of a user

### Identity Layer Details

| Layer | Identity Type | Purpose | OAuth Analogy | Lifecycle |
|-------|---------------|---------|---------------|-----------|
| **Deployment Identity** | SPIFFE-based infrastructure identity | mTLS, service mesh authentication, request routing | OAuth Client — proves "this request from this pod" | Pod lifecycle (hours) |
| **Agent Persona** | Scenario-derived business identity | Business authorization, audit, delegation chains | OAuth Principal — the business entity on whose behalf actions are taken | Scenario lifecycle (months/years) |

**Lifecycle Progression**:
- **Raw Agent**: Infrastructure identity (SPIFFE) declared
- **Trained Agent**: Application identity configured (no runtime credentials)
- **Employed Agent**: Full two-layer identity (Deployment Identity + Agent Persona)

### Token Structure

Delegation Access Tokens include both identities, enabling both infrastructure authentication and business authorization:

```json
{
  "sub": "dispute-resolution-agent@acme.hub.io",  // Agent Persona (business identity)
  "iss": "cipher.hub.olympus.io",
  "client_id": "spiffe://acme.hub.io/seer/agent/acme/fraud-analyst-pod-001",  // Deployment Identity (infrastructure)
  "delegated_by": "dispute-scenario-profile",  // Source of authority
  "scopes": ["disputes:read", "disputes:resolve"],
  "exp": "2026-01-17T22:00:00Z"
}
```

The token structure enables:
- **Infrastructure verification**: `client_id` (SPIFFE) proves the request comes from a verified deployment
- **Business authorization**: `sub` (Agent Persona) identifies the business entity accountable for the action
- **Audit clarity**: Both identities are recorded, but business actions are attributed to the persona

### Identity Flexibility

The two-layer model provides flexibility in deployment and scaling:

**One Deployment, Multiple Personas**:
A single deployment can serve multiple Agent Personas via different Delegation Access Tokens per request. This enables:
- Shared infrastructure for multiple scenarios
- Cost optimization through deployment consolidation
- Different authority per request while using the same infrastructure

**One Persona, Multiple Deployments**:
A single Agent Persona can have multiple deployments (multiple pods for scaling). This enables:
- Horizontal scaling without identity fragmentation
- High availability through multiple deployment instances
- Consistent business identity across all deployment instances

### Identity Use Cases

| Use Case | Identity Used | Notes |
|----------|---------------|-------|
| **mTLS / Service Mesh** | Deployment Identity (SPIFFE) | Infrastructure authentication — proves request from verified pod |
| **Access Tokens** | Agent Persona (`sub`) | Business authorization — identifies accountable business entity |
| **Audit Logs** | Agent Persona | Business accountability — all actions attributed to persona |
| **Delegation Chains** | Agent Persona | Tracks business authority — who delegated to this persona |
| **Request Routing** | Deployment Identity (SPIFFE) | Infrastructure routing — routes to correct pod instance |
| **Composite Applications** | Sub-Personas | Each agent in composite gets distinct sub-persona derived from base persona |

> **See**: [ADR-0129: Agent Identity Model](../../../../../olympus-hub-docs/decision-logs/0129-agent-identity-model.md) for the complete two-layer identity model design decision.

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

- **SPIFFE SVIDs:** Deployment Identity (infrastructure-level) — OAuth Client equivalent
- **Delegation Access Tokens:** Include both `client_id` (SPIFFE) and `sub` (Agent Persona)
- **Signed Credentials:** All credentials are cryptographically signed

Verification is possible at any point in the request chain. The Deployment Identity (SPIFFE) proves infrastructure authenticity, while the Agent Persona (in tokens) proves business authorization.

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
