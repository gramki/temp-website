# Agent Identity Ambiguity Resolution

> **Status**: ✅ **RESOLVED**  
> **Priority**: High — Foundational issue affecting multiple documents  
> **Related**: Hub Agent vs Seer Agent, Request-Scoped Delegation  
> **Last Updated**: 2026-01-17  
> **Resolution**: Two-layer identity model documented in ADR-0129 and ADR-0130

---

## The Problem

The current documentation conflates **two distinct identities**:

1. **Deployment Identity (SPIFFE ID)** — Infrastructure-level, identifies the running container/pod
2. **Agent Identity (Persona)** — Business-level, identifies "who this agent is" to other systems

This conflation creates confusion about:
- What identity is used for what purpose
- Where authority comes from
- How delegation works in different models

---

## The Two Identities

### 1. Deployment Identity (SPIFFE ID)

| Aspect | Description |
|--------|-------------|
| **What it is** | Cryptographic identity of the deployed Employed Agent instance |
| **Format** | `spiffe://hub.olympus.io/seer/tenant/{tenant_id}/workbench/{workbench_id}/agent/{agent_id}` |
| **Provisioned by** | SPIRE Agent during pod startup |
| **Purpose** | mTLS, service mesh authentication, infrastructure-level authN |
| **Lifetime** | Tied to deployment lifecycle (created on deploy, rotated hourly, revoked on undeploy) |
| **Scope** | Per-deployment instance |

**SPIFFE ID is the "client identity"** — it proves "this request is coming from this specific agent deployment."

### 2. Agent Identity (Persona)

| Aspect | Description |
|--------|-------------|
| **What it is** | Business/persona identity — "who is this agent" in business terms |
| **Source** | Derived from **Scenario** (Scenario provides the agent's human-like personality) |
| **Purpose** | App-to-app interactions, authority delegation, audit attribution |
| **Lifetime** | Tied to Scenario lifecycle (survives redeployments) |
| **Scope** | Per-Scenario (or per-Scenario-binding) |

**Agent Identity is the "principal identity"** — it represents "who is accountable for this action" in business terms.

---

## Key Insight: Separation of Concerns

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         IDENTITY LAYERS                                     │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  BUSINESS/PERSONA LAYER (Agent Identity)                            │    │
│  │                                                                     │    │
│  │  • Derived from Scenario                                            │    │
│  │  • "Dispute Resolution Agent" — a recognizable business persona     │    │
│  │  • Has authority delegated from Scenario's Identity Profile Owner   │    │
│  │  • Used for: access tokens, audit, delegation chains                │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                   │                                         │
│                                   │ presents as                             │
│                                   ▼                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  INFRASTRUCTURE LAYER (Deployment Identity)                         │    │
│  │                                                                     │    │
│  │  • SPIFFE ID                                                        │    │
│  │  • "This pod running in this namespace in this cluster"             │    │
│  │  • Used for: mTLS, service mesh, infrastructure authN               │    │
│  │  • Acts as "client" presenting the Agent Identity                   │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Original Notes (Expanded)

### SPIFFE ID = Deployment Identity

- SPIFFE ID is the identity of the **deployment** of the Employed Agent
- It is NOT the agent's business identity
- It should be used as a **"client" identity** for the agent
- Analogous to: "This is the browser/device making the request" (not "This is Alice")

### Scenario = Agent Identity Source

- The Scenario provides the **"Agent" identity** (human-like personality)
- This is different from the deployment identity
- This identity is required to create **access tokens for app-to-app interactions**
- The agent needs to be recognizable as a principal across systems

### Authority Derivation

- Ideally, the Employment Spec should **derive or reference Delegated Authority** from the Scenario's Identity Profile Owner
- The Scenario "owns" the agent persona and its base authority
- Employment Spec configures how that authority is bound to a specific deployment

### Exception: Request-Scoped Delegation

- Only in request-scoped delegation does the Scenario potentially NOT have identity with authority to delegate
- In this case, authority comes from the Business User per-request
- But even then, the agent still has its base identity (just not the delegated authority)

### Composite Applications Consideration

- Delegation specification should be part of EmploymentSpec even for Scenario-scoped delegation
- Reason: A Scenario can have **multiple Employed Agents** (Hub Composite Application)
- Each agent may have different delegation configurations
- The EmploymentSpec is the right place to configure per-agent delegation

---

## Documentation Gaps to Fix

### Current Conflation Patterns

1. **SPIFFE ID described as "agent identity"** — Should clarify it's deployment identity
2. **Authority delegation described at deployment level** — Should clarify it derives from Scenario
3. **Employed Agent Profile conflates both identities** — Should separate them
4. **"Agent Identity" used interchangeably for both** — Need distinct terms

### Terminology to Clarify

| Current Term | Proposed Clarification |
|--------------|------------------------|
| "Agent Identity" (ambiguous) | "Agent Persona" (business) vs "Agent Deployment Identity" (infra) |
| "SPIFFE Identity" | "Deployment Identity (SPIFFE-based)" — make clear it's infra |
| "Agent Profile" | Clarify: contains both persona + deployment identity references |
| "Employed Agent Identity" | Clarify: composite of Scenario-derived persona + deployment SPIFFE |

---

## Confirmed Decisions

### Identity Model

1. **Agent Persona Storage**: Cipher IAM maintains and manages the identity lifecycle. Scenario references it. During deployment, the operator can create non-existent IAM profiles.

2. **Persona-to-Deployment Linking**: The Delegation Access Token is provided to the Employed Agent from the environment (as described in request-scoped-delegation docs). This should be called "Scenario-scoped delegation model" with semantics similar to request-scoped delegation.

3. **One Persona, Multiple Deployments**: Yes — one Agent Persona can have multiple deployments (multiple pods).

4. **One Deployment, Multiple Personas**: Yes. Each request contains the Delegation Access Token that provides the agent's authority and persona in the scope of that request. Although a typical deployment is 1:1 for a scenario, it need not be the only deployment choice. Even if deployment is scenario-scoped, a request-scoped-delegation employment means a deployment is serving multiple Agent Personas.

### Authority Delegation

5. **Scenario Identity Profile Owner**: In scenario-scoped delegation, the tenant admin provides an explicit input or the operator implicitly creates one.

6. **Employment Spec Reference**: Employment Spec merely needs to specify the required delegation templates and any additional access policies. It need not specifically name the identity profile as it will receive from the Scenario. Model it exactly as request-scoped-delegation, just the mode being different (scenario-scoped vs request-scoped).

7. **Scenario Identity Profile Owner Changes**: It will be a new deployment anyway, so no concern.

8. **Interaction with Request-Scoped Delegation**: They are similar and don't conflict.

### Composite Applications

9. **Agent Distinction in Composite**: SPIFFE IDs will be different. Each agent receives a different Delegation Access Token.

10. **Sub-Personas for Composite Applications**: Each agent has its own sub-persona (e.g., `dispute-analyst-agent`, `dispute-reviewer-agent`). Each has a different Delegation Access Token representing different delegation authority. They all derive from the same base Agent Persona associated with the Scenario, but each gets a distinct sub-persona identity.

11. **Delegation Spec Partitioning**: Employment Spec contains the delegation spec per agent.

### Token Issuance Model

12. **Hybrid Token Issuance**: Both scenario-scoped and request-scoped delegation use the same pattern:
    - **Certificate** created at source time (deployment for scenario-scoped, request for request-scoped)
    - **Token** always issued per-request from the Certificate
    - Same semantics, different timing of Certificate creation

### Composite Application Sub-Persona Model

```
Scenario: dispute-resolution
    │
    │ defines base Agent Persona
    ▼
Base Agent Persona: dispute-resolution-agent
    │
    ├── Sub-Persona: dispute-analyst-agent
    │       │
    │       ├── Deployment Identity: spiffe://.../analyst-pod-001
    │       ├── Delegation Template: analyze-disputes
    │       └── Delegation Access Token (per-request)
    │
    ├── Sub-Persona: dispute-reviewer-agent
    │       │
    │       ├── Deployment Identity: spiffe://.../reviewer-pod-001
    │       ├── Delegation Template: review-analysis
    │       └── Delegation Access Token (per-request)
    │
    └── Sub-Persona: dispute-approver-agent
            │
            ├── Deployment Identity: spiffe://.../approver-pod-001
            ├── Delegation Template: approve-resolution
            └── Delegation Access Token (per-request)
```

**Key Points**:
- Each agent in a Composite Application gets its own **sub-persona** (distinct from base persona)
- Each sub-persona has its own **Deployment Identity** (SPIFFE ID)
- Each sub-persona has its own **Delegation Template** (configured in Employment Spec)
- All sub-personas derive from the same **base Agent Persona** (from Scenario)
- Each request includes a **Delegation Access Token** bound to the specific sub-persona

---

## Proposed Resolution

### 1. Introduce Clear Terminology

| Term | Definition |
|------|------------|
| **Agent Persona** | Business identity derived from Scenario; represents "who" the agent is |
| **Deployment Identity** | SPIFFE-based identity of the running agent pod; represents "which instance" |
| **Agent Principal** | The composite identity (Persona + Deployment) used for access control |
| **Scenario Identity Profile** | The IAM profile owned by the Scenario, from which Agent Personas derive |

### 2. Update Identity Model Diagram

```
Scenario
    │
    │ defines
    ▼
Agent Persona (business identity)
    │
    │ is deployed as
    ▼
Employed Agent Instance
    │
    │ has
    ▼
Deployment Identity (SPIFFE)
```

### 3. Update EmploymentSpec Structure

```yaml
spec:
  # Reference to Scenario (source of Agent Persona)
  scenarioRef:
    name: dispute-resolution
    workbench: acme-disputes
    
  # Delegation configuration (per-agent, even in Composite)
  delegation:
    # Where authority comes from
    source:
      type: scenario_identity_profile  # or "request_scoped"
      profileRef: dispute-resolution-agent  # Scenario's Identity Profile
      
    # Ceiling: what can be delegated
    ceiling:
      scopes: [...]
      
  # Deployment identity is auto-provisioned (SPIFFE)
  # Agent persona comes from scenarioRef
```

### 4. Token Structure

Access tokens should include BOTH identities:

```json
{
  "sub": "dispute-resolution-agent@acme.hub.io",  // Agent Persona
  "iss": "cipher.hub.olympus.io",
  "client_id": "spiffe://acme.hub.io/seer/agent/...",  // Deployment Identity
  "delegated_by": "dispute-scenario-profile",  // Scenario Identity Profile
  "scopes": ["disputes:read", "disputes:resolve"],
  "exp": "..."
}
```

---

## Documents Updated

### ADRs Created

- [x] [ADR-0129: Agent Identity Model](../decision-logs/0129-agent-identity-model.md) — Two-layer identity model (Deployment vs Persona)
- [x] [ADR-0130: Unified Delegation Model](../decision-logs/0130-unified-delegation-model.md) — Scenario-scoped vs request-scoped modes

### Seer Design Docs

- [x] `implementation-concepts/agent-lifecycle.md` — Clarified identity layers
- [x] `implementation-concepts/agent-identity-credentials.md` — Added two-layer identity model section
- [x] `subsystems/cipher-iam-extensions/architecture.md` — Updated with identity layers
- [x] `subsystems/cipher-iam-extensions/profile-tags.md` — Added persona vs deployment tags
- [x] `subsystems/cipher-iam-extensions/authority-delegation.md` — Added delegation modes
- [x] `hub-integration/employment-spec-crd.md` — Updated with unified delegation model
- [x] `implementation-concepts/request-scoped-delegation.md` — Added scenario-scoped mode section

### Hub Design Docs

- [x] `02-system-design/agent-model.md` — Added identity layers section
- [x] `02-system-design/implementation-concepts/scenario-as-agent.md` — Added identity model section
- [x] `05-infrastructure/cipher-iam-infrastructure.md` — Added agent identity model section

---

## Impact on Other Work

### Hub Agent vs Seer Agent

- This resolution is foundational — must be clarified before that doc
- Hub Agent identity comes from Scenario (persona)
- Seer Agent identity adds deployment layer (SPIFFE)

### Request-Scoped Delegation

- Already designed with this separation in mind
- Business User grants to Agent Persona (not deployment)
- Delegation Access Token is bound to Agent Persona + Deployment

### Composite Applications

- Each agent in composite has distinct persona (from Scenario or sub-scenario)
- All may share workbench but have different EmploymentSpecs
- Delegation must be per-agent (in EmploymentSpec)

---

## Next Steps

1. [x] Consolidate confirmed decisions (hybrid token, sub-personas)
2. [x] Create ADR-0129: Agent Identity Model (Deployment vs Persona)
3. [x] Create ADR-0130: Unified Delegation Model (scenario/request modes)
4. [x] Update Seer design docs with clear terminology and two-layer identity model
5. [x] Update Hub design docs with identity layers
6. [x] Update request-scoped delegation doc with scenario-scoped mode
7. [x] Update Hub Agent vs Seer Agent doc with refined identity model
8. [x] Finalize scratchpad with ADR references and completion status

## Resolution Status

**Status**: ✅ **RESOLVED**

All documentation has been updated to reflect the two-layer identity model:
- **Deployment Identity (SPIFFE)**: Infrastructure-level, OAuth Client equivalent
- **Agent Persona**: Business-level, Scenario-derived, carried in Delegation Access Tokens

The unified delegation model (scenario-scoped and request-scoped) has been documented as a single mechanism with two modes.

**Key ADRs**:
- [ADR-0129: Agent Identity Model](../decision-logs/0129-agent-identity-model.md)
- [ADR-0130: Unified Delegation Model](../decision-logs/0130-unified-delegation-model.md)
