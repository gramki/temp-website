# Request-Scoped Authority Delegation

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-17  
> **Related**: [Delegation Chains](./delegation-chains.md), [Authority Enforcement](./authority-enforcement.md), [Agent Identity & Credentials](./agent-identity-credentials.md)

---

## Executive Summary

Request-Scoped Authority Delegation enables Employed Agents to act on behalf of **business users** with **temporary, task-bounded authority**. The key driver is **temporality** — users want agents to have authority only for the duration of a specific task, not permanently.

**Primary Driver**: Users don't want agents with permanent authority living indefinitely. For example:
- A user asks an agent to pay 10 bills → the agent should lose authority after completing those payments
- During the task, the agent may need to make multiple decisions on behalf of the user
- Once the task is complete, the delegation expires

**Key Insight**: Agents with request-scoped delegation typically:
1. Have **minimal enterprise identity** — usually "bot" mode with limited internal Hub authority
2. Act as an **OAuth client-like identity** — a consistent ID through which they act on behalf of the delegator
3. Remain **explainable and maintainable** — separation of enterprise vs. delegated authority keeps the agent's role clear

These agents combine a stable enterprise identity (for accountability and routing) with temporary, user-granted authority (for task execution).

---

## 1. Problem Statement

### 1.1 The Gap in Existing Delegation

The existing Seer delegation model (User, Role, Bot) operates in the **Enterprise/Operator Identity Domain**:

| Existing Model | Delegator | Example |
|----------------|-----------|---------|
| **User Delegation** | Internal employee | `john.smith@bank.com` (fraud analyst) delegates to agent |
| **Role Delegation** | Internal IAM role | `fraud-analyst` role permissions delegated to agent |
| **Bot Mode** | None (explicit roles) | Agent has `automated-processor` role directly |

These models answer: *"How does an enterprise employee delegate their internal permissions to an agent?"*

### 1.2 What's Missing

Existing delegation models grant **permanent authority** — appropriate for long-lived operational agents but not for **temporary, task-specific** scenarios:

| Scenario | Task | Why Request-Scoped? |
|----------|------|---------------------|
| **Bill Payment Assistant** | Pay 10 scheduled bills | Authority expires after the 10 payments complete; agent shouldn't retain payment authority indefinitely |
| **Expense Approval Bot** | Approve a specific expense claim | Authority granted only for this claim; shouldn't have permanent approval rights |
| **Document Signing Agent** | Sign 3 contracts on user's behalf | Authority scoped to these specific documents; revoked immediately after |
| **Investment Rebalancer** | Execute quarterly rebalance | Temporary authority to trade; user reviews and grants per rebalance cycle |

Request-Scoped Delegation answers: *"How does a user grant an agent temporary authority for a specific task, ensuring that authority expires when the task completes?"*

### 1.3 Design Goals

1. **Temporality**: Authority is bounded by request/session lifecycle, not agent lifetime
2. **Explicit Consent**: User grants authority for specific actions via understandable templates
3. **Minimal Enterprise Footprint**: These agents typically have "bot" enterprise identity with limited internal permissions
4. **Client-Like Identity**: Agent maintains a stable identity (like an OAuth client) for routing and accountability
5. **Explainability**: Clear separation between what the agent can do internally vs. what it can do on behalf of users

---

## 2. Core Concepts

### 2.1 Concept Hierarchy

```
┌─────────────────────────────────────────────────────────────────────┐
│                     DELEGATION TEMPLATE                              │
│  Defines: What authority CAN be delegated                           │
│  Created by: Tenant Admin in Cipher IAM                             │
│  Examples: "view-transactions", "initiate-payments-under-1000"      │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     DELEGATION CERTIFICATE                           │
│  Represents: User's consent to delegate                              │
│  Created by: Business user (via Channel)                             │
│  Contains: Template ref, Delegate pattern, Constraints, Expiry       │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│                   DELEGATION ACCESS TOKEN                            │
│  Represents: Request-scoped authority for a specific agent           │
│  Created by: Cipher IAM Extensions                                   │
│  Bound to: Single agent (SPIFFE ID), Single request                  │
└─────────────────────────────────────────────────────────────────────┘
```

### 2.2 Delegation Template

A **Delegation Template** defines a package of authority that can be delegated. It's designed for cognitive ergonomics — users should understand what they're granting.

```yaml
apiVersion: cipher.zeta.tech/v1
kind: DelegationTemplate
metadata:
  name: personal-finance-assistant
  namespace: retail-banking
spec:
  displayName: "Personal Finance Assistant"
  description: "View accounts, initiate transfers under $500"
  
  permissions:
    - resource: "accounts"
      actions: ["read", "list"]
    - resource: "transfers"
      actions: ["create"]
      constraints:
        maxAmount: 500
        currency: "USD"
  
  constraints:
    maxDuration: "24h"
    chainingAllowed: false
    
  policies:
    - name: "business-hours-only"
      rego: |
        package delegation
        allow { input.time.hour >= 9; input.time.hour < 17 }
```

**Key Properties**:
- **Tenant-scoped**: Templates are defined per tenant
- **Human-readable**: Designed for user consent flows
- **Policy-bearing**: Can include OPA policies that constrain usage
- **Chaining control**: Explicitly allows or denies re-delegation

### 2.3 Delegation Certificate

A **Delegation Certificate** represents a user's consent to delegate authority. It references a template and specifies who can use it.

```yaml
apiVersion: cipher.zeta.tech/v1
kind: DelegationCertificate
metadata:
  id: "cert-12345"
  issuedAt: "2026-01-17T10:00:00Z"
spec:
  delegator:
    type: "business-user"
    id: "user-67890"
    source: "retail-banking-idp"
  
  template:
    name: "personal-finance-assistant"
    namespace: "retail-banking"
  
  delegate:
    pattern: "role"  # or "specific-identity", "group"
    value: "personal-assistant-agent"
  
  constraints:
    expiry: "2026-01-17T22:00:00Z"
    chainingAllowed: false
    sessionScoped: true
  
  revocation:
    mechanism: "cipher-revocation-list"
    checkUrl: "https://cipher.internal/revoke/check"
```

**Key Properties**:
- **Delegator**: The business user granting authority
- **Template Reference**: What authority is being granted
- **Delegate Pattern**: Who can claim this certificate (specific agent, role, group)
- **Constraints**: Time bounds, chaining rules, session scope

### 2.4 Delegation Access Token

A **Delegation Access Token** is the runtime artifact — a request-scoped token that an agent uses to perform actions on behalf of the delegator.

```yaml
# Conceptual structure (actual format is signed JWT or similar)
header:
  alg: "RS256"
  typ: "DAT"  # Delegation Access Token
  
claims:
  iss: "cipher.zeta.tech"
  sub: "bill-payment-assistant@acme.hub.io"  # Agent Persona (business identity)
  client_id: "spiffe://acme.hub.io/seer/agent/acme/bill-payment-pod-001"  # Deployment Identity (SPIFFE)
  delegated_by: "user-67890"  # Resource Owner (Business User for request-scoped, Scenario Profile for scenario-scoped)
  iat: 1737108000
  exp: 1737151200
  
  delegation:
    template: "personal-finance-assistant"
    certificate: "cert-12345"
    requestId: "req-abcdef"
    permissions: [...]
    constraints: [...]
```

**Key Properties**:
- **Two-Layer Identity**: Includes both `client_id` (Deployment Identity/SPIFFE) and `sub` (Agent Persona)
- **Bound to single agent**: `client_id` specifies exactly one agent's SPIFFE ID (deployment)
- **Request-scoped**: Valid only for the specific request
- **Agent Persona as subject**: `sub` is the Agent Persona (Scenario-derived business identity)
- **Delegator tracked**: `delegated_by` identifies who granted authority (Business User or Scenario Profile)
- **Traceable**: Links back to certificate for audit

> **See**: [ADR-0129: Agent Identity Model](../../../olympus-hub-docs/decision-logs/0129-agent-identity-model.md) for the two-layer identity model.

---

## 3. OAuth 2.0 Analogy

Request-Scoped Delegation maps to OAuth 2.0 concepts:

| OAuth 2.0 Concept | Request-Scoped Delegation Equivalent |
|-------------------|--------------------------------------|
| **Client** | Deployment Identity (SPIFFE ID) — OAuth Client equivalent |
| **Client Credentials** | Agent's deployment credentials (SVID from SPIRE) |
| **Principal** | Agent Persona (Scenario-derived business identity) |
| **Resource Owner** | Business User (delegator) |
| **Authorization Server** | Cipher IAM Extensions |
| **Scope** | Delegation Template |
| **Authorization Grant** | Delegation Certificate |
| **Access Token** | Delegation Access Token (includes both `client_id` and `sub`) |
| **Resource Server** | Tool Gateway, External APIs |

### Agent as OAuth Client

The agent's **Deployment Identity (SPIFFE ID)** functions like an **OAuth Client ID**:

```
┌───────────────────────────────────────────────────────────────────┐
│                    TASK-SCOPED AGENT PATTERN                       │
├───────────────────────────────────────────────────────────────────┤
│  Deployment Identity (OAuth "Client")                              │
│  ├── SPIFFE ID: spiffe://seer/agents/bill-payment-assistant       │
│  ├── Purpose: Infrastructure authentication (mTLS, service mesh)  │
│  └── OAuth Analogy: Client ID — proves "this request from this pod"│
├───────────────────────────────────────────────────────────────────┤
│  Agent Persona (OAuth "Principal")                                 │
│  ├── Persona: bill-payment-assistant@acme.hub.io                  │
│  ├── Source: Scenario-derived business identity                    │
│  └── Purpose: Business authorization, audit, accountability       │
├───────────────────────────────────────────────────────────────────┤
│  Request-Scoped Delegation (OAuth "Access Token")                  │
│  ├── client_id: spiffe://.../bill-payment-assistant (Deployment)  │
│  ├── sub: bill-payment-assistant@acme.hub.io (Persona)            │
│  ├── delegated_by: user-12345 (Resource Owner)                    │
│  ├── Template: pay-bills                                          │
│  ├── Scope: Execute payments to approved payees                   │
│  └── Expires: When request completes or after 2 hours             │
└───────────────────────────────────────────────────────────────────┘
```

**Key Insight**: The agent has almost no inherent authority. Its Deployment Identity (SPIFFE ID) is the "OAuth Client" — it identifies the deployment for infrastructure authentication. The Agent Persona (Scenario-derived) represents the business identity. All meaningful authority comes from the user's temporary delegation via the Delegation Access Token.

> **See**: [ADR-0129: Agent Identity Model](../../../olympus-hub-docs/decision-logs/0129-agent-identity-model.md) for the two-layer identity model.

---

## 4. Delegation Flows

### 4.1 Flow Types

| Flow Type | Trigger | When Used |
|-----------|---------|-----------|
| **Proactive** | User initiates delegation before scenario | Mobile app consent screen before starting |
| **Reactive** | Agent requests authority during execution | Agent discovers it needs authority mid-task |
| **Implicit** | Channel fulfills from existing certificates | User has pre-authorized; no prompt needed |

### 4.2 Proactive Delegation Flow

User grants authority before the agent begins work. The Channel obtains both the Certificate and the Token, then includes them in the Request.

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│  User    │     │ Channel  │     │  Cipher  │     │   RLM    │     │  Agent   │
│ (Mobile) │     │  (App)   │     │   IAM    │     │          │     │          │
└────┬─────┘     └────┬─────┘     └────┬─────┘     └────┬─────┘     └────┬─────┘
     │                │                │                │                │
     │ 1. Start task  │                │                │                │
     │───────────────>│                │                │                │
     │                │                │                │                │
     │ 2. Show consent│                │                │                │
     │   (template)   │                │                │                │
     │<───────────────│                │                │                │
     │                │                │                │                │
     │ 3. Grant       │                │                │                │
     │───────────────>│                │                │                │
     │                │                │                │                │
     │                │ 4. Issue       │                │                │
     │                │   Certificate  │                │                │
     │                │───────────────>│                │                │
     │                │                │                │                │
     │                │ 5. Certificate │                │                │
     │                │<───────────────│                │                │
     │                │                │                │                │
     │                │ 6. Request     │                │                │
     │                │   Token        │                │                │
     │                │   (for agent)  │                │                │
     │                │───────────────>│                │                │
     │                │                │                │                │
     │                │ 7. Token       │                │                │
     │                │<───────────────│                │                │
     │                │                │                │                │
     │                │ 8. Create Request               │                │
     │                │   (with Cert + Token)           │                │
     │                │───────────────────────────────>│                │
     │                │                │                │                │
     │                │                │                │ 9. Dispatch    │
     │                │                │                │   (token in    │
     │                │                │                │   env.auth)    │
     │                │                │                │───────────────>│
     │                │                │                │                │
     │                │                │                │                │ 10. Execute
     │                │                │                │                │    with token
```

**Note**: The Channel is responsible for converting the Certificate to a Delegation Access Token before creating the Request. This ensures the agent receives the token immediately upon dispatch, without needing to query for it.

### 4.3 Reactive Delegation Flow (Authority Request)

Agent discovers it needs authority and requests it.

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│  Agent   │     │ Sidecar  │     │   SX     │     │ Channel  │     │  User    │
│          │     │          │     │          │     │  (App)   │     │          │
└────┬─────┘     └────┬─────┘     └────┬─────┘     └────┬─────┘     └────┬─────┘
     │                │                │                │                │
     │ 1. Attempt     │                │                │                │
     │    action      │                │                │                │
     │───────────────>│                │                │                │
     │                │                │                │                │
     │                │ 2. Check:      │                │                │
     │                │    No token    │                │                │
     │                │                │                │                │
     │                │ 3. Post        │                │                │
     │                │   AUTHORITY_   │                │                │
     │                │   REQUEST      │                │                │
     │                │───────────────>│                │                │
     │                │                │                │                │
     │ 4. Suspend     │                │ 5. Notify      │                │
     │    (wait)      │                │    observer    │                │
     │<───────────────│                │───────────────>│                │
     │                │                │                │                │
     │                │                │                │ 6. Show consent│
     │                │                │                │───────────────>│
     │                │                │                │                │
     │                │                │                │ 7. Grant/Deny  │
     │                │                │                │<───────────────│
     │                │                │                │                │
     │                │                │ 8. Post        │                │
     │                │                │   AUTHORITY_   │                │
     │                │                │   GRANTED      │                │
     │                │                │<───────────────│                │
     │                │                │                │                │
     │                │ 9. Token in    │                │                │
     │                │   env.auth.    │                │                │
     │                │   delegations  │                │                │
     │                │<───────────────│                │                │
     │                │                │                │                │
     │ 10. Resume     │                │                │                │
     │    with token  │                │                │                │
     │<───────────────│                │                │                │
```

### 4.4 Implicit Fulfillment Flow

Channel auto-fulfills from existing certificates — no user prompt.

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│  Agent   │     │ Sidecar  │     │   SX     │     │ Channel  │
└────┬─────┘     └────┬─────┘     └────┬─────┘     └────┬─────┘
     │                │                │                │
     │ 1. Post        │                │                │
     │   AUTHORITY_   │                │                │
     │   REQUEST      │                │                │
     │───────────────>│───────────────>│───────────────>│
     │                │                │                │
     │                │                │                │ 2. Check existing
     │                │                │                │    certificates
     │                │                │                │
     │                │                │                │ 3. Certificate found!
     │                │                │                │    (matches template)
     │                │                │                │
     │                │                │ 4. AUTHORITY_  │
     │                │                │    GRANTED     │
     │                │                │    (no prompt) │
     │                │                │<───────────────│
     │                │                │                │
     │ 5. Resume      │                │                │
     │    with token  │                │                │
     │<───────────────│<───────────────│                │
```

### 4.5 Cascading via Request Hierarchy

Child request inherits or cascades authority requests to parent.

```
┌────────────────────────────────────────────────────────────────────┐
│                    REQUEST HIERARCHY                                │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  Parent Request (req-parent)                                 │   │
│  │  └── Delegation Certificate: cert-123                        │   │
│  │      └── Template: personal-finance-assistant                │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              │ creates child                        │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  Child Request (req-child)                                   │   │
│  │  └── Agent B needs authority                                 │   │
│  │      └── AUTHORITY_REQUEST posted                            │   │
│  │          └── If certificate allows chaining:                 │   │
│  │              Token issued to Agent B                         │   │
│  │          └── If not: Cascade to parent for user prompt       │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
└────────────────────────────────────────────────────────────────────┘
```

**Cascading Rules**:
1. Check if current request has applicable certificate
2. If not, check parent request (recursive up hierarchy)
3. If certificate found with `chainingAllowed: true`, issue new token
4. If no certificate found, AUTHORITY_REQUEST cascades to parent's Channel
5. Cross-workbench cascading follows best-effort async pattern

---

## 5. Component Responsibilities

### 5.1 Responsibility Matrix

| Component | Responsibilities |
|-----------|------------------|
| **Channel** | Orchestrate consent flow (present template, capture user approval), request Certificate and Token from Cipher, attach to Request, handle AUTHORITY_REQUEST (prompt user or auto-fulfill) |
| **Cipher IAM Extensions** | Manage Templates, issue Certificates, issue Tokens, validate credentials, maintain business user profiles |
| **Request Lifecycle Manager** | Store delegation context per Request, provide API for delegation lookup |
| **Signal Exchange** | Route AUTHORITY_REQUEST/GRANTED updates, refresh `environment.auth.delegations` on each update |
| **Seer Sidecar** | Pre-guardrail delegation check, post AUTHORITY_REQUEST, inject token into agent context |
| **Agent Ingress Gateway** | Forward delegation token to agent, token validation |
| **Tool Gateway** | Validate delegation token on tool calls, enforce template policies |
| **Agent SDK** | Provide `request_authority()`, `get_delegation_token()`, `delegate_to_child()` APIs |

### 5.2 Token Placement

Delegation tokens are placed in the message envelope:

```yaml
environment:
  auth:
    # Enterprise identity (existing)
    identity:
      spiffeId: "spiffe://seer/agents/my-agent"
      delegationMode: "bot"
    
    # Business user delegations (new)
    delegations:
      - token: "eyJ..."
        template: "personal-finance-assistant"
        delegator: "user-67890"
        expiresAt: "2026-01-17T22:00:00Z"
```

Signal Exchange **refreshes** this section on every REQUEST_UPDATE delivery to ensure revocations are reflected.

### 5.3 Scenario-Scoped Delegation (Alternative Mode)

Request-Scoped Delegation and **Scenario-Scoped Delegation** use the **same unified mechanism** with different modes:

| Aspect | Request-Scoped Mode | Scenario-Scoped Mode |
|--------|---------------------|----------------------|
| **Certificate Source** | Business User (via Channel) | Scenario Identity Profile |
| **Certificate Timing** | Created per-request (when user grants) | Created at deployment |
| **Token Timing** | Per-request (from Certificate) | Per-request (from Certificate) |
| **Token Semantics** | Identical | Identical |
| **Token Structure** | Identical (`client_id`, `sub`, `delegated_by`) | Identical |
| **Use Case** | Temporary, user-initiated tasks | Long-lived operational agents |

**Key Principle**: Both modes use **hybrid token issuance**:
- **Certificate** created at source time (deployment for scenario-scoped, request for request-scoped)
- **Token** always issued per-request from the Certificate
- Same semantics, different timing of Certificate creation

**Example - Scenario-Scoped Delegation**:

```
Deployment Time:
  Scenario Identity Profile → Creates Delegation Certificate
  Certificate stored, referenced by Employment Spec

Per-Request:
  Agent receives Request Update
  Cipher issues Delegation Access Token from Certificate
  Token includes: client_id (SPIFFE), sub (Agent Persona), delegated_by (Scenario Profile)
```

**Employment Spec Configuration**:

```yaml
delegation:
  unified:
    mode: scenario-scoped  # or "request-scoped"
    allowedTemplates:
      - analyze-disputes
      - review-analysis
    # Same structure for both modes
    # Identity profile comes from Scenario (not specified here)
```

> **See**: [ADR-0130: Unified Delegation Model](../../../olympus-hub-docs/decision-logs/0130-unified-delegation-model.md) for the complete unified model.

---

## 6. Policy Composition

When an agent uses delegated authority, **all applicable policies must ALLOW**:

```
┌─────────────────────────────────────────────────────────────────────┐
│                     POLICY EVALUATION                                │
│                                                                      │
│  Training Spec Policies    ───┐                                      │
│                               │                                      │
│  Employment Spec Policies  ───┼───▶  ALL must ALLOW  ───▶  Action   │
│                               │      (Intersection)       Permitted  │
│  Delegation Template Policies─┘                                      │
│                                                                      │
│  If ANY policy DENIES  ───────────────────────────────▶  DENIED     │
└─────────────────────────────────────────────────────────────────────┘
```

This is **narrowing-only inheritance** — delegation can never expand beyond what any layer allows.

---

## 7. Configuration

### 7.1 Training Spec

```yaml
apiVersion: seer.zeta.tech/v1
kind: TrainingSpec
metadata:
  name: personal-assistant
spec:
  # ... existing fields ...
  
  delegationRequirements:
    # Templates this scenario may request
    templates:
      - name: "personal-finance-assistant"
        required: true
      - name: "view-investments"
        required: false
    
    # Behavior when delegation unavailable
    onDelegationUnavailable: "degrade"  # or "fail"
```

### 7.2 Employment Spec

```yaml
apiVersion: seer.zeta.tech/v1
kind: EmploymentSpec
metadata:
  name: my-assistant-prod
spec:
  # ... existing fields ...
  
  delegation:
    mode: "deferred"  # vs existing: "user", "role", "bot"
    
    requestScopedDelegation:
      enabled: true
      allowedTemplates:
        - "personal-finance-assistant"
        - "view-investments"
      chainingPolicy: "template-controlled"  # or "always-deny"
```

---

## 8. Agent SDK Usage

### 8.1 Checking for Delegation

```python
from seer_sdk import delegation

# Check if delegation is available
if delegation.has_token("personal-finance-assistant"):
    # Proceed with delegated action
    result = tools.transfer_funds(amount=100)
else:
    # Request delegation
    delegation.request_authority(
        template="personal-finance-assistant",
        reason="Need to transfer funds as requested"
    )
    # Agent will be resumed when granted
```

### 8.2 Explicit Authority Request

```python
# Proactively request authority
await delegation.request_authority(
    template="personal-finance-assistant",
    reason="You asked me to manage your bills",
    blocking=True  # Wait for response
)

# Check result
if delegation.was_granted("personal-finance-assistant"):
    # Proceed
else:
    # Handle denial gracefully
    respond("I don't have permission to do that. Would you like to grant access?")
```

### 8.3 Chaining to Child Agent

```python
# When spawning a child agent, delegate authority
child_request = hub.create_child_request(
    scenario="payment-processor",
    delegation=delegation.chain_token(
        template="personal-finance-assistant",
        for_agent="payment-processor-agent"
    )
)
```

---

## 9. Security Considerations

### 9.1 Token Binding

- Each token is bound to **exactly one agent** (SPIFFE ID in `aud` claim)
- Tokens cannot be shared between agents
- Token theft is mitigated by agent identity verification at every use

### 9.2 Revocation

- Certificates can be revoked at any time via Cipher
- Signal Exchange checks revocation status on each update delivery
- Revoked tokens are removed from `environment.auth.delegations`
- Agent behavior on revocation: configurable (default: degrade gracefully)

### 9.3 Audit Trail

- All delegation events are logged to Cognitive Audit Fabric
- Token usage is traceable to both delegator and accountable human
- Certificate lineage is preserved for compliance

### 9.4 Human Accountability

Request-Scoped Delegation does **not** remove human accountability:
- Accountable human (from enterprise delegation) remains responsible for agent behavior
- Delegator (business user) consents to agent action but is not accountable for agent design
- Both are informed of actions via audit and notification

---

## 10. Relationship to Existing Concepts

### 10.1 vs. User/Role/Bot Delegation

| Aspect | User/Role/Bot | Request-Scoped |
|--------|---------------|----------------|
| **Primary Purpose** | Permanent operational authority | Temporary task-specific authority |
| **Duration** | Agent lifetime | Request/session (expires with task) |
| **When Configured** | Employment time | Request time |
| **Who Delegates** | Operator/Enterprise | End-user/Business user |
| **Typical Use Case** | Long-running operational agents | Short-lived task agents |

**Key Pattern**: Agents designed for request-scoped delegation typically:
- Use **Bot mode** for enterprise identity — minimal internal permissions
- Act as a **stable client identity** — consistent SPIFFE ID for routing and accountability
- Receive **all meaningful authority** from the delegating user, not from enterprise IAM

This separation keeps agents explainable: the enterprise identity answers "who built and deployed this agent?" while request-scoped delegation answers "on whose behalf is it acting right now?"

### 10.2 OAuth Analogy: Agent as Client

Request-Scoped Delegation follows the OAuth Authorization Code flow pattern:

| OAuth Concept | Request-Scoped Equivalent | Purpose |
|---------------|---------------------------|---------|
| **Client** | Employed Agent (SPIFFE ID) | Stable identity for routing, audit, and accountability |
| **Resource Owner** | Business User | Grants temporary authority |
| **Authorization Grant** | Delegation Certificate | Records user's consent |
| **Access Token** | Delegation Access Token | Short-lived proof of authority |
| **Scope** | Delegation Template | What authority is being granted |

**Why This Analogy Matters**: The agent's enterprise identity (SPIFFE ID) functions like an OAuth Client ID — it provides a consistent, registered identity that users and systems can trust. The agent doesn't have inherent authority; it receives authority from users who choose to delegate to it, just as OAuth clients receive tokens from resource owners.

### 10.3 vs. Hub Request Context

Request-Scoped Delegation extends Hub's existing request context:

- Request already carries: assignee, status, tags, memory references
- Delegation adds: certificates, access tokens, authority requests
- Both follow request hierarchy inheritance patterns

---

## 11. Glossary

| Term | Definition |
|------|------------|
| **Business User** | End-user of the business (customer, partner) who grants temporary authority to an agent |
| **Delegation Template** | Cipher artifact defining a package of delegatable authority; designed for user comprehension |
| **Delegation Certificate** | User's signed consent to delegate authority per a template; stored with request |
| **Delegation Access Token** | Short-lived token enabling agent to act on user's behalf; expires with task |
| **Authority Request** | REQUEST_UPDATE sub-type requesting delegation from Channel |
| **Authority Grant** | REQUEST_UPDATE sub-type delivering token after consent |
| **Chaining** | Agent delegating received authority to another agent (if template allows) |
| **Cascading** | Authority request propagating up request hierarchy to find consent-capable Channel |
| **Task-Scoped Agent** | Agent pattern with minimal enterprise identity, receiving authority per-request from users |
| **Agent as Client** | Conceptual model where agent's SPIFFE ID functions like an OAuth Client ID |

---

## 12. References

### Hub Documentation
- [Request Lifecycle](../../../olympus-hub-docs/04-subsystems/request-management/request-lifecycle.md)
- [Request Hierarchy](../../../olympus-hub-docs/04-subsystems/request-management/request-hierarchy.md)
- [Signal Exchange](../../../olympus-hub-docs/04-subsystems/signal-exchange/README.md)
- [Message Envelope](../../../olympus-hub-docs/04-subsystems/signal-exchange/message-envelope.md)
- [Channels](../../../olympus-hub-docs/02-system-design/implementation-concepts/channel.md)

### Seer Documentation
- [Delegation Chains](./delegation-chains.md)
- [Authority Enforcement](./authority-enforcement.md)
- [Agent Identity & Credentials](./agent-identity-credentials.md)
- [Seer Sidecar](./seer-sidecar.md)
- [Cipher IAM Extensions](../subsystems/cipher-iam-extensions/README.md)

### Design Source
- [Brainstorming Document](../../../olympus-hub-docs/scratchpad/0WIP-seer-request-scoped-authority-delegation.md)
