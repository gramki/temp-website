# ADR-0129: Agent Identity Model (Deployment vs Persona)

> **Status**: Accepted  
> **Date**: 2026-01-17  
> **Authors**: Architecture Team  
> **Related ADRs**: [ADR-0130: Unified Delegation Model](./0130-unified-delegation-model.md), [ADR-0127: Request-Scoped Authority Delegation](./0127-request-scoped-authority-delegation.md)

---

## Context

The current documentation conflates two distinct identities for Employed Agents:

1. **Deployment Identity (SPIFFE ID)**: Infrastructure-level, identifies the running container/pod
2. **Agent Persona**: Business-level identity derived from Scenario, identifies "who this agent is" in business terms

This conflation creates confusion about:
- What identity is used for what purpose
- Where authority comes from
- How delegation works in different models
- How tokens should be structured

---

## Decision

**Adopt a two-layer identity model that clearly separates Deployment Identity from Agent Persona.**

### Two-Layer Identity Model

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

### Key Principles

1. **SPIFFE ID = OAuth Client**: The deployment identity is equivalent to an OAuth Client — it proves "this request is coming from this specific agent deployment" (infrastructure-level).

2. **Agent Persona = Business Identity**: The persona identity represents "who is accountable for this action" in business terms. It is derived from the Scenario and stored in Cipher IAM.

3. **Token Structure Includes Both**: Delegation Access Tokens include both identities:
   - `client_id`: SPIFFE ID (deployment identity)
   - `sub`: Agent Persona (business identity)
   - `delegated_by`: Source of authority (Scenario Identity Profile or Business User)

4. **One Deployment, Multiple Personas**: A single deployment can serve multiple Agent Personas via different Delegation Access Tokens per request.

5. **One Persona, Multiple Deployments**: A single Agent Persona can have multiple deployments (multiple pods for scaling).

---

## Rationale

### Why Separate These Identities?

1. **Different Lifecycles**: 
   - Deployment Identity is tied to pod lifecycle (created on deploy, rotated hourly, revoked on undeploy)
   - Agent Persona is tied to Scenario lifecycle (survives redeployments)

2. **Different Purposes**:
   - Deployment Identity: Infrastructure authentication (mTLS, service mesh)
   - Agent Persona: Business authorization (access tokens, audit, delegation chains)

3. **OAuth Client Analogy**: 
   - The deployment is the "client" (like a browser or mobile app)
   - The persona is the "principal" (like a user account)
   - The deployment presents tokens on behalf of the persona

4. **Flexibility**: 
   - Same deployment can serve different personas (via different tokens)
   - Same persona can scale across multiple deployments

### Why SPIFFE for Deployment Identity?

- **Cryptographic Verification**: SPIFFE provides cryptographically verifiable identity via X.509 certificates
- **Service Mesh Integration**: Standard for mTLS and service-to-service authentication
- **Automatic Rotation**: SPIRE agent handles certificate rotation
- **Infrastructure Focus**: Clearly identifies the running workload, not the business entity

### Why Scenario-Derived Persona?

- **Business Context**: Scenarios define business operations and roles
- **Consistency**: Same persona across redeployments
- **Accountability**: Clear business identity for audit and compliance
- **Authority Source**: Scenario Identity Profile provides base authority

---

## Consequences

### Benefits

- **Clear Separation**: Infrastructure vs. business identity concerns are separated
- **Flexibility**: Deployments can serve multiple personas; personas can scale across deployments
- **OAuth Alignment**: Aligns with standard OAuth 2.0 patterns (client vs. principal)
- **Audit Clarity**: Business actions are attributed to personas, not infrastructure
- **Security**: Infrastructure identity (SPIFFE) provides strong cryptographic verification

### Trade-offs

- **Complexity**: Two identities to manage instead of one
- **Documentation**: Must clearly explain when to use which identity
- **Token Structure**: Tokens must include both identities

### Implications

| Use Case | Identity Used | Notes |
|----------|---------------|-------|
| mTLS / Service Mesh | Deployment Identity (SPIFFE) | Infrastructure authentication |
| Access Tokens | Agent Persona (`sub`) | Business authorization |
| Audit Logs | Agent Persona | Business accountability |
| Delegation Chains | Agent Persona | Tracks business authority |
| Request Routing | Deployment Identity (SPIFFE) | Infrastructure routing |
| Composite Applications | Sub-Personas | Each agent gets distinct sub-persona |

---

## Alternatives Considered

### Alternative 1: Single Identity (SPIFFE Only)

Use only SPIFFE ID for both infrastructure and business identity.

**Rejected because**:
- SPIFFE ID is tied to deployment lifecycle (changes on redeploy)
- Business identity should survive redeployments
- No clear way to represent "who this agent is" in business terms
- Breaks audit and accountability requirements

### Alternative 2: Single Identity (Persona Only)

Use only Agent Persona, derive SPIFFE from persona.

**Rejected because**:
- SPIFFE requires infrastructure-level attestation (pod identity)
- Persona is business-level concept, shouldn't dictate infrastructure identity
- Service mesh requires SPIFFE for mTLS
- Breaks standard SPIFFE patterns

### Alternative 3: Persona as SPIFFE Path Component

Include persona in SPIFFE ID path (e.g., `spiffe://.../persona/{persona}/deployment/{deployment}`).

**Rejected because**:
- SPIFFE ID should identify the workload, not the business entity
- Mixes concerns (infrastructure + business)
- Still doesn't solve token structure (need both in token)
- Breaks SPIFFE best practices

---

## Implementation Notes

### Token Structure

Delegation Access Tokens must include both identities:

```json
{
  "sub": "dispute-resolution-agent@acme.hub.io",  // Agent Persona
  "iss": "cipher.hub.olympus.io",
  "client_id": "spiffe://acme.hub.io/seer/agent/acme/fraud-analyst-pod-001",  // Deployment Identity
  "delegated_by": "dispute-scenario-profile",  // Scenario Identity Profile (scenario-scoped) or Business User (request-scoped)
  "scopes": ["disputes:read", "disputes:resolve"],
  "exp": "2026-01-17T22:00:00Z"
}
```

### Composite Applications

In Hub Composite Applications, each agent gets its own **sub-persona**:

```
Scenario: dispute-resolution
    │
    ├── Sub-Persona: dispute-analyst-agent
    │       └── Deployment Identity: spiffe://.../analyst-pod-001
    │
    ├── Sub-Persona: dispute-reviewer-agent
    │       └── Deployment Identity: spiffe://.../reviewer-pod-001
    │
    └── Sub-Persona: dispute-approver-agent
            └── Deployment Identity: spiffe://.../approver-pod-001
```

All sub-personas derive from the same base Agent Persona (from Scenario), but each has distinct identity for delegation and audit.

---

## Related Documentation

- [Agent Identity Ambiguity Resolution](../../scratchpad/0WIP-agent-identity-ambiguity-resolution.md) — Original problem analysis
- [Request-Scoped Authority Delegation](../0127-request-scoped-authority-delegation.md) — Delegation model using this identity structure
- [Unified Delegation Model](../0130-unified-delegation-model.md) — How scenario-scoped and request-scoped use same identity model
