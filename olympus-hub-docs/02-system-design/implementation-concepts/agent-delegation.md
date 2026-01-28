# Agent Delegation

> **Category:** Agent Delegation  
> **Status:** 🟢 Design Complete  
> **Last Updated:** 2026-01-21

---

## Overview

**Agent Delegation** is the mechanism by which agents receive authority to act on behalf of others. Delegation enables agents to perform actions they couldn't perform with their base identity alone, while maintaining traceability and accountability.

Hub and Seer support delegation in **two distinct identity domains**:

| Domain | Delegator | When Configured | Use Case |
|--------|-----------|-----------------|----------|
| **Enterprise Delegation** | Internal operators (employees, roles) | At employment time | Agents acting on behalf of enterprise users |
| **Business User Delegation** | End-users (customers, external employees) | At deployment or per-request | Agents acting on behalf of customers |

These domains are **orthogonal** — an agent may have authority from both simultaneously.

---

## Enterprise Delegation

Enterprise delegation enables agents to inherit authority from **internal operators** — enterprise employees or organizational roles. This is the traditional delegation model for agents operating within the enterprise context.

| Mode | Description | Use Case |
|------|-------------|----------|
| **User Delegation** | Agent acts on behalf of a specific enterprise user | Personal assistant for an employee |
| **Role Delegation** | Agent inherits from an enterprise role | Team-level automation agent |
| **Bot Mode** | Agent has base identity only (no delegation) | Fully automated processing |

**Key Characteristics:**
- Configured at **employment time** via Employment Spec
- Authority flows through **delegation chains** with narrowing-only inheritance
- Requires designated **accountable human** for RASCI compliance
- Real-time synchronization — agent authority shrinks when delegator authority shrinks

> **Authoritative Source:** [Delegation Chains (Seer)](../../../olympus-seer-docs/seer-design/implementation-concepts/delegation-chains.md)

---

## Business User Delegation

Business user delegation enables agents to act on behalf of **end-users** — customers, external employees, or other non-enterprise users who interact with the system. This is critical for customer-facing AI agents.

### The Unified Model

Business user delegation uses a **unified model** with two modes that share identical semantics but differ in when authority is granted:

```
┌─────────────────────────────────────────────────────────────────────┐
│                     DELEGATION TEMPLATE                              │
│  Defines: What authority CAN be delegated                           │
│  Created by: Tenant Admin in Cipher IAM                             │
└─────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     DELEGATION CERTIFICATE                           │
│  Represents: Consent to delegate                                    │
│  Created by: Scenario Identity Profile (scenario-scoped) OR         │
│              Business User via Channel (request-scoped)              │
│  Timing: At deployment (scenario-scoped) OR per-request             │
└─────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────┐
│                   DELEGATION ACCESS TOKEN                            │
│  Represents: Request-scoped authority for a specific agent          │
│  Created by: Cipher IAM Extensions                                   │
│  Timing: ALWAYS per-request (from Certificate)                       │
│  Bound to: Single agent (SPIFFE ID), Single request                  │
└─────────────────────────────────────────────────────────────────────┘
```

> **Source:** [ADR-0130: Unified Delegation Model](../../decision-logs/0130-unified-delegation-model.md)

### Mode Comparison

| Aspect | Scenario-Scoped | Request-Scoped |
|--------|-----------------|----------------|
| **Purpose** | Long-lived operational agents with stable authority | Temporary, task-bounded agents with user-granted authority |
| **Certificate Source** | Scenario Identity Profile | Business User (via Channel) |
| **Certificate Timing** | At deployment | Per-request (when user grants) |
| **Token Timing** | Per-request | Per-request |
| **Token Structure** | Identical | Identical |
| **Applicability** | Operational automation, enterprise processes | Customer-facing assistants, user-initiated tasks |

**Key Principle:** Both modes use **hybrid token issuance**:
- **Certificate** created at source time (deployment for scenario-scoped, request for request-scoped)
- **Token** always issued per-request from the Certificate
- Same token semantics and structure (`client_id`, `sub`, `delegated_by`)

### When to Use Which Mode

| Scenario | Mode | Why |
|----------|------|-----|
| Dispute resolution agent processing cases | Scenario-scoped | Stable authority from enterprise; no per-case user consent needed |
| Personal finance AI paying bills for customer | Request-scoped | Customer must consent per-request; authority is task-bounded |
| Fraud detection agent analyzing transactions | Scenario-scoped | Operational automation with enterprise authority |
| Family banking assistant transferring money | Request-scoped | Parent must authorize each session; temporary authority |
| Agent that handles both enterprise and customer tasks | Both | Can accept scenario-scoped OR request-scoped depending on context |

---

## Contrast: Enterprise vs Business User Delegation

| Aspect | Enterprise Delegation | Business User Delegation |
|--------|----------------------|--------------------------|
| **Delegator** | Internal operator (employee, role) | End-user (customer, external employee) |
| **Identity Domain** | Enterprise IAM | Federated business user identity |
| **Configured When** | Employment time | Deployment (scenario-scoped) or per-request (request-scoped) |
| **Authority Source** | Delegator's IAM roles/groups | Delegation Template + User consent |
| **Inheritance** | Real-time shrinking with delegator | Shrinks with delegator; eventual consistency |
| **Certificate** | Not used (direct IAM inheritance) | Required (represents consent) |
| **Accountability** | Designated accountable human | Layered: business user (action) + enterprise (agent) |
| **Use Case** | Internal operations, employee assistants | Customer-facing agents, external user tasks |

**Notes on Business User Delegation:**

- **Inheritance**: Both models exhibit eventual consistency. If a business user's authority shrinks (e.g., account suspended), the effective authority of their delegation shrinks accordingly.
- **Layered Accountability**: Business user delegation has two accountability layers:
  1. **Action accountability** — The business user (delegator) is accountable for the actions they authorized
  2. **Agent accountability** — The enterprise (via designated accountable human) is accountable for the agent's behavior, since the enterprise provides the agent

**Combining Both Domains:**

An agent may operate with authority from both domains simultaneously:
- **Enterprise delegation** provides base authority for internal operations
- **Business user delegation** adds customer-specific authority for their tasks

Example: A customer service agent with `bot` mode (enterprise delegation) can also accept request-scoped delegation from customers to perform actions on their behalf.

---

## Hub Components Involved

| Component | Role in Delegation |
|-----------|-------------------|
| **Cipher IAM Extensions** | Delegation Templates, Certificates, Tokens, Business User Profiles |
| **Signal Exchange** | Token refresh on REQUEST_UPDATE delivery, AUTHORITY_REQUEST/GRANTED routing |
| **Request Lifecycle Manager** | Delegation context storage per request |
| **Channels** | Consent capture (request-scoped), Authority Request handling |
| **Observer Pattern** | Channels receive REQUEST_UPDATEs as delegation observers |

---

## Token Structure

Both business user delegation modes produce identical token structure:

```json
{
  "sub": "dispute-resolution-agent@acme.hub.io",
  "iss": "cipher.hub.olympus.io",
  "client_id": "spiffe://acme.hub.io/seer/agent/acme/fraud-analyst-pod-001",
  "delegated_by": "dispute-scenario-profile",
  "certificate_id": "cert-abc123",
  "template": "analyze-disputes",
  "scopes": ["disputes:read", "disputes:analyze"],
  "exp": "2026-01-21T22:00:00Z"
}
```

| Field | Description |
|-------|-------------|
| `sub` | Agent Persona (business identity) |
| `client_id` | Deployment Identity (SPIFFE ID) |
| `delegated_by` | Scenario Identity Profile (scenario-scoped) OR Business User ID (request-scoped) |
| `certificate_id` | Delegation Certificate used |
| `template` | Delegation Template defining authority package |
| `scopes` | Specific permissions granted |

---

## Related Documentation

### Mode-Specific Concepts

| Concept | Description |
|---------|-------------|
| [Scenario-Scoped Delegation](./scenario-scoped-delegation.md) | Authority from Scenario Identity Profile at deployment |
| [Request-Scoped Delegation](./request-scoped-delegation.md) | Authority from Business User consent per-request |

### Enterprise Delegation

| Concept | Description |
|---------|-------------|
| [Delegation Chains (Seer)](../../../olympus-seer-docs/seer-design/implementation-concepts/delegation-chains.md) | Enterprise delegation model (User, Role, Bot modes) |

### Supporting Concepts

| Concept | Description |
|---------|-------------|
| [Agent Identity Model](../../decision-logs/0129-agent-identity-model.md) | Two-layer identity (Deployment Identity + Agent Persona) |
| [Channel](./channel.md) | Consent capture and Authority Request handling |
| [Observer Pattern](./observer-pattern.md) | Channels as delegation observers |

### Decision Records

| ADR | Decision |
|-----|----------|
| [ADR-0127](../../decision-logs/0127-request-scoped-authority-delegation.md) | Request-Scoped Authority Delegation |
| [ADR-0129](../../decision-logs/0129-agent-identity-model.md) | Agent Identity Model (Deployment vs Persona) |
| [ADR-0130](../../decision-logs/0130-unified-delegation-model.md) | Unified Delegation Model |

---

*Agent Delegation enables agents to act on behalf of humans — whether enterprise operators or business users — with clear authority, traceability, and accountability.*
