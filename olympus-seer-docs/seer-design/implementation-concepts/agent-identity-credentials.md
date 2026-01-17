# Agent Identity & Credentials

> **Status**: 🟡 Draft — Concept  
> **Last Updated**: 2026-01-13

## Overview

Agent Identity & Credentials extends Hub Cipher IAM to support **agent-specific identity and authority management**. It provides the IAM foundation for agent identity, authority delegation, and policy enforcement.

**Key Characteristics:**
- Extensions to Hub Cipher IAM (not replacement)
- Supports Raw, Trained, and Employed Agent identity types
- Authority delegation with human accountability
- Per-PEP policy enforcement

---

## Architecture

Cipher IAM Extensions extends Hub Cipher IAM:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 CIPHER IAM EXTENSIONS ARCHITECTURE                          │
│                                                                              │
│   Seer Components → Cipher IAM Extensions → Hub Cipher IAM (Core)          │
│                                                                              │
│   • Agent Profile API                                                       │
│   • Authority Delegation                                                    │
│   • Policy Enforcement                                                       │
│   • Credential Management                                                   │
│                                                                              │
│   Extends:                                                                   │
│   • Identity Management                                                      │
│   • SPIFFE Integration                                                       │
│   • OPA Policy Engine                                                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Principles

- **Extensions to Hub Cipher IAM** — Extends Hub Cipher IAM, not replaces
- **Agent Profile Types** — Raw, Trained, and Employed Agent profiles
- **Authority Delegation Model** — User delegation, role delegation, bot mode
- **Policies Per PEP** — Policies are per Policy Enforcement Point (not global)
- **SPIFFE Integration** — Leverages SPIFFE for deployment identity (OAuth Client equivalent)
- **Two-Layer Identity Model** — Deployment Identity (SPIFFE) + Agent Persona (Scenario-derived)

---

## Two-Layer Identity Model

Employed Agents have **two distinct identities** that serve different purposes:

### 1. Deployment Identity (SPIFFE ID)

The **Deployment Identity** is the infrastructure-level identity of the running agent pod. It is equivalent to an **OAuth Client** — it proves "this request is coming from this specific agent deployment."

| Aspect | Description |
|--------|-------------|
| **What it is** | Cryptographic identity of the deployed Employed Agent instance |
| **Format** | `spiffe://hub.olympus.io/seer/tenant/{tenant_id}/workbench/{workbench_id}/agent/{agent_id}` |
| **Provisioned by** | SPIRE Agent during pod startup |
| **Purpose** | mTLS, service mesh authentication, infrastructure-level authN |
| **Lifetime** | Tied to deployment lifecycle (created on deploy, rotated hourly, revoked on undeploy) |
| **Scope** | Per-deployment instance |
| **OAuth Analogy** | OAuth Client — the technical caller |

**SPIFFE ID is the "client identity"** — it proves "this request is coming from this specific agent deployment."

### 2. Agent Persona

The **Agent Persona** is the business-level identity derived from the Scenario. It represents "who this agent is" in business terms and is carried in the **Delegation Access Token**.

| Aspect | Description |
|--------|-------------|
| **What it is** | Business/persona identity — "who is this agent" in business terms |
| **Source** | Derived from **Scenario** (Scenario provides the agent's human-like personality) |
| **Purpose** | App-to-app interactions, authority delegation, audit attribution |
| **Lifetime** | Tied to Scenario lifecycle (survives redeployments) |
| **Scope** | Per-Scenario (or per-Scenario-binding, sub-personas for Composite Applications) |
| **OAuth Analogy** | OAuth Principal — the business entity on whose behalf actions are taken |
| **Storage** | Cipher IAM (Scenario references it; operator can create non-existent profiles during deployment) |

**Agent Persona is the "principal identity"** — it represents "who is accountable for this action" in business terms.

### Identity Relationship

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

### Delegation Access Token Structure

The Delegation Access Token carries both identities:

```json
{
  "sub": "dispute-resolution-agent@acme.hub.io",  // Agent Persona
  "iss": "cipher.hub.olympus.io",
  "client_id": "spiffe://acme.hub.io/seer/agent/acme/fraud-analyst-pod-001",  // Deployment Identity
  "delegated_by": "dispute-scenario-profile",  // Scenario Identity Profile or Business User
  "scopes": ["disputes:read", "disputes:resolve"],
  "exp": "2026-01-17T22:00:00Z"
}
```

### Key Insights

1. **One Deployment, Multiple Personas**: A single deployment can serve multiple Agent Personas via different Delegation Access Tokens per request.

2. **One Persona, Multiple Deployments**: A single Agent Persona can have multiple deployments (multiple pods for scaling).

3. **Composite Applications**: Each agent in a Composite Application gets its own **sub-persona** (e.g., `dispute-analyst-agent`, `dispute-reviewer-agent`), all deriving from the same base Agent Persona.

> **See**: [ADR-0129: Agent Identity Model](../../../olympus-hub-docs/decision-logs/0129-agent-identity-model.md) for the complete architectural decision.

---

## Agent Profile Types

### Raw Agent Profile

| Aspect | Description |
|--------|-------------|
| **Tag** | `raw-agent` |
| **Capabilities** | Base capabilities, no delegation |
| **Credentials** | No runtime credentials (not yet employed) |
| **Purpose** | Declares supported models, tools, and capabilities |

### Trained Agent Profile

| Aspect | Description |
|--------|-------------|
| **Tag** | `trained-agent` |
| **Capabilities** | Trained capabilities, potential delegation constraints |
| **Credentials** | No runtime credentials (not yet employed) |
| **Purpose** | Inherits from Raw Agent, adds allowed models |

### Employed Agent Profile

| Aspect | Description |
|--------|-------------|
| **Tag** | `employed-agent` |
| **Capabilities** | Full identity with delegation chain and policies |
| **Credentials** | Full credential set (SPIFFE deployment identity, virtual key, zone-vault reference) |
| **Identity Layers** | Contains both Deployment Identity (SPIFFE) and Agent Persona (Scenario-derived) |
| **Purpose** | Runtime identity with authority and accountability |

---

## Authority Delegation Model

Three delegation models:

| Model | Description |
|-------|-------------|
| **User Delegation** | Agent acts on behalf of a specific user |
| **Role Delegation** | Agent inherits from a role |
| **Bot Mode** | Agent has base identity only, no delegation |

---

## Credential Management

Credential lifecycle for Employed Agents:

| Credential Type | Provisioned By | Purpose | Rotation |
|-----------------|----------------|---------|----------|
| **SPIFFE Certificate** | SPIRE Agent | mTLS identity, service mesh auth | Automatic (hourly) |
| **Virtual Key** | Seer Operator | Model Gateway access, budget tracking | On employment or rotation request |
| **Zone-Vault Reference** | Seer Operator | Tool credential injection | On demand |

---

## SPIFFE Identity (Deployment Identity)

Employed Agents receive **SPIFFE-based Deployment Identities**:

| Aspect | Description |
|--------|-------------|
| **Format** | `spiffe://hub.olympus.io/seer/tenant/{tenant_id}/workbench/{workbench_id}/agent/{agent_id}` |
| **Purpose** | Cryptographic identity for mTLS and service mesh authentication (infrastructure-level) |
| **OAuth Analogy** | OAuth Client — the technical caller making requests |
| **Rotation** | Automatic rotation (hourly) |
| **Revocation** | Revoked on employment revocation |
| **Scope** | Per-deployment instance (not per-Scenario) |

**Note**: SPIFFE ID is the **Deployment Identity** (infrastructure-level), not the Agent Persona (business-level). The Agent Persona is derived from the Scenario and carried in Delegation Access Tokens.

---

## Policy Enforcement Points (PEPs)

Policies are **per Policy Enforcement Point**:

| Aspect | Description |
|--------|-------------|
| **PEP-Specific** | Policies are per PEP (not global) |
| **Unknown PEPs** | Unknown PEPs are ignored (graceful degradation) |
| **Policy References** | Policies are referenced files (not inline) |
| **PEP Types** | Tool Gateway, Model Gateway, Signal Exchange, Seer Sidecar |

---

## Human Accountability

All Employed Agents have **accountable humans**:

| Aspect | Description |
|--------|-------------|
| **Accountable Human** | Reference to the Supervisor who delegated authority |
| **Audit Trail** | Full audit trail of delegation and accountability |
| **Delegation Chain** | Full delegation chain traceable to humans |

---

## Related

### Cipher IAM Extensions Subsystem
- [Cipher IAM Extensions README](../subsystems/cipher-iam-extensions/README.md) — Subsystem overview
- [Architecture](../subsystems/cipher-iam-extensions/architecture.md) — Hub Cipher IAM relationship, agent identity types
- [Agent Profile API](../subsystems/cipher-iam-extensions/agent-profile-api.md) — API specification, endpoints
- [Authority Delegation](../subsystems/cipher-iam-extensions/authority-delegation.md) — Delegation model, inheritance algorithms
- [Profile Tags](../subsystems/cipher-iam-extensions/profile-tags.md) — Raw/Trained/Employed agent profile tags
- [Credential Management](../subsystems/cipher-iam-extensions/credential-management.md) — Credential issuance, injection, virtual keys
- [Policy Enforcement Points](../subsystems/cipher-iam-extensions/policy-enforcement-points.md) — PEP registration, policy evaluation

### Related Systems
- [Agent Lifecycle](../implementation-concepts/agent-lifecycle.md) — Lifecycle integration
- [Authority Enforcement](../implementation-concepts/authority-enforcement.md) — Enforcement concepts
- [Request-Scoped Authority Delegation](../implementation-concepts/request-scoped-delegation.md) — Delegation model using this identity structure
- [Hub Cipher IAM](../../../olympus-hub-docs/04-subsystems/cipher-iam/README.md) — Core Cipher IAM
- [ADR-0106: Cipher IAM Extensions for Agent Profiles](../../../olympus-hub-docs/decision-logs/0106-seer-cipher-iam-extensions-agent-profiles.md) — Architecture decision
- [ADR-0129: Agent Identity Model](../../../olympus-hub-docs/decision-logs/0129-agent-identity-model.md) — Two-layer identity model decision
- [ADR-0130: Unified Delegation Model](../../../olympus-hub-docs/decision-logs/0130-unified-delegation-model.md) — Scenario-scoped vs request-scoped modes

---

*For detailed implementation, see [Cipher IAM Extensions README](../subsystems/cipher-iam-extensions/README.md).*
