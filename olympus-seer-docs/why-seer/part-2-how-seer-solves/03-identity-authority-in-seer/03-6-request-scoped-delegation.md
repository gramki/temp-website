# 3.6 Request-Scoped Authority Delegation

Enterprise delegation models (User, Role, Bot) address how internal employees and roles delegate authority to agents. However, business-facing agents must act on behalf of **end-users** — customers, partners, and external employees who are not part of the enterprise's internal IAM. Request-Scoped Authority Delegation enables agents to receive temporary, task-bounded authority from business users within the scope of a specific Hub Request.

## Purpose of This Section

This section explains how Seer enables business users to delegate authority to agents for specific tasks, distinct from the enterprise delegation model covered in Section 3.2. It addresses the fundamental question: *How can a customer grant an agent temporary authority to act on their behalf, ensuring that authority expires when the task completes?*

Request-Scoped Delegation operates in a **second identity domain** alongside enterprise delegation, enabling agents to combine stable enterprise identity (for accountability and routing) with temporary, user-granted authority (for task execution).

## Core Concepts & Definitions

### Two Orthogonal Identity Domains

Seer supports two distinct identity domains for agent delegation:

| Domain | Delegator | Use Case | Duration |
|--------|-----------|----------|----------|
| **Enterprise Delegation** | Internal employees, IAM roles | Long-lived operational agents | Agent lifetime |
| **Request-Scoped Delegation** | Business users (customers, partners) | Temporary, task-specific agents | Request/session lifecycle |

These domains are **orthogonal** — an agent can participate in both simultaneously. For example, an agent may have enterprise identity for internal operations (via Scenario Identity Profile) while also receiving request-scoped authority from a business user for a specific task.

### Core Artifacts

Request-Scoped Delegation introduces three core artifacts:

**Delegation Template**: Defines a package of authority that can be delegated. Designed for cognitive ergonomics — users should understand what they're granting.

```yaml
apiVersion: cipher.zeta.tech/v1
kind: DelegationTemplate
metadata:
  name: personal-finance-assistant
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
```

**Delegation Certificate**: Represents a user's consent to delegate authority. Created when a business user grants authority via a Channel.

```yaml
apiVersion: cipher.zeta.tech/v1
kind: DelegationCertificate
metadata:
  id: "cert-12345"
spec:
  delegator:
    type: "business-user"
    id: "user-67890"
  template:
    name: "personal-finance-assistant"
  delegate:
    pattern: "role"
    value: "personal-assistant-agent"
  constraints:
    expiry: "2026-01-17T22:00:00Z"
```

**Delegation Access Token**: A request-scoped JWT that an agent uses to perform actions on behalf of the delegator. Includes both Deployment Identity (SPIFFE) and Agent Persona.

```json
{
  "sub": "bill-payment-assistant@acme.hub.io",  // Agent Persona
  "client_id": "spiffe://acme.hub.io/seer/agent/acme/bill-payment-pod-001",  // Deployment Identity
  "delegated_by": "user-67890",  // Business User (Resource Owner)
  "template": "personal-finance-assistant",
  "certificate": "cert-12345",
  "scopes": ["accounts:read", "transfers:create"],
  "exp": "2026-01-17T22:00:00Z"
}
```

## Conceptual Models / Frameworks

### OAuth 2.0-Inspired Model

Request-Scoped Delegation maps to OAuth 2.0 concepts, providing a familiar mental model:

| OAuth 2.0 Concept | Request-Scoped Delegation Equivalent | Purpose |
|-------------------|--------------------------------------|---------|
| **Client** | Deployment Identity (SPIFFE ID) | Infrastructure authentication — proves "this request from this pod" |
| **Resource Owner** | Business User | Grants temporary authority |
| **Authorization Server** | Cipher IAM Extensions | Issues Certificates and Tokens |
| **Scope** | Delegation Template | Defines what authority is being granted |
| **Authorization Grant** | Delegation Certificate | Records user's consent |
| **Access Token** | Delegation Access Token | Short-lived proof of authority |

**Key Insight**: The agent's Deployment Identity (SPIFFE ID) functions like an OAuth Client ID — it provides a stable, registered identity that users and systems can trust. The agent doesn't have inherent authority; it receives authority from users who choose to delegate to it, just as OAuth clients receive tokens from resource owners.

### Delegation Flow Types

Request-Scoped Delegation supports four delegation flows:

**1. Proactive Delegation**: User grants authority before the agent begins work. The Channel obtains both the Certificate and the Token, then includes them in the Request.

```
User → Channel → Cipher (Issue Certificate) → Cipher (Issue Token) → Request → Agent
```

**2. Reactive Delegation**: Agent discovers it needs authority and requests it mid-execution via `AUTHORITY_REQUEST` update type. Channel prompts user, then issues Certificate and Token.

```
Agent → Sidecar → Signal Exchange → Channel → User (Prompt) → Channel → Cipher → Token → Agent
```

**3. Implicit Delegation**: Channel auto-fulfills from existing certificates — no user prompt needed. User has pre-authorized; Channel finds matching certificate and issues token.

```
Agent → Sidecar → Signal Exchange → Channel (Check Certificates) → Certificate Found → Token → Agent
```

**4. Cascading Delegation**: Authority requests propagate up the request hierarchy. If a child request needs authority, it can cascade to the parent request's Channel.

```
Child Request → Parent Request → Parent Channel → User → Certificate → Token → Child Agent
```

### Policy Composition Model

When an agent uses delegated authority, **all applicable policies must ALLOW** (AND logic):

```
Training Spec Policies
    ↓
Employment Spec Policies  ────▶  ALL must ALLOW  ────▶  Action Permitted
    ↓
Delegation Template Policies
```

This is **narrowing-only inheritance** — delegation can never expand beyond what any layer allows. If ANY policy DENIES, the action is denied.

## Systemic and Enterprise Considerations

### Channel Dependency

Request-Scoped Delegation **requires Channels** (not Signal Providers) to facilitate delegation:

- **Channels** (Web Portal, Mobile App, MS Teams) can present consent UI and capture user approval
- **Signal Providers** (APIs, Event Streams) cannot interact with users and therefore cannot facilitate delegation

This dependency means that request-scoped delegation is only available for scenarios that are triggered via Channels, not for scenarios triggered by Signal Providers.

### Business User Identity Federation

Request-Scoped Delegation requires business user identity federation:

- Business users must be authenticated via external identity providers (customer IDP, partner IDP)
- Cipher IAM Extensions must maintain business user profiles separate from enterprise IAM
- Identity federation enables consent capture and certificate issuance

### Token Lifecycle Management

Delegation Access Tokens have specific lifecycle characteristics:

- **Short-lived**: Tokens expire with the request or after a configurable duration (typically hours, not days)
- **Request-scoped**: Each token is bound to a specific request ID
- **Agent-bound**: Each token is bound to a specific agent's SPIFFE ID (cannot be shared)
- **Revocable**: Certificates can be revoked at any time, invalidating all derived tokens

Signal Exchange refreshes the `environment.auth.delegations` section on every REQUEST_UPDATE delivery to ensure revocations are reflected immediately.

### Consent Capture and User Experience

Delegation Templates must be designed for user comprehension:

- **Human-readable descriptions**: Users must understand what authority they're granting
- **Clear constraints**: Maximum amounts, time bounds, and scope limitations must be explicit
- **Consent fatigue mitigation**: Templates should be concise and focused, avoiding overly broad authority packages

### Policy Composition Requirements

All applicable policies must ALLOW for an action to proceed:

- **Training Spec Policies**: Guardrails defined at training time
- **Employment Spec Policies**: Constraints defined at employment time
- **Delegation Template Policies**: Constraints defined in the template

If any layer denies, the action is denied. This ensures that delegation cannot bypass enterprise controls.

## Common Misconceptions & Failure Modes

### Misconception 1: Confusing with Enterprise Delegation

**Misconception**: Request-Scoped Delegation is just another way to do enterprise delegation.

**Reality**: These are two orthogonal identity domains. Enterprise delegation grants permanent authority from internal employees/roles. Request-Scoped Delegation grants temporary authority from business users. An agent can participate in both simultaneously.

### Misconception 2: Channels and Signal Providers Are Equivalent

**Misconception**: Any trigger source can facilitate request-scoped delegation.

**Reality**: Only Channels can facilitate delegation because they can interact with users. Signal Providers (APIs, event streams) cannot present consent UI and therefore cannot facilitate delegation. Scenarios triggered by Signal Providers cannot use request-scoped delegation.

### Misconception 3: Tokens Are Long-Lived

**Misconception**: Delegation Access Tokens persist for the agent's lifetime.

**Reality**: Tokens are request-scoped and short-lived. They expire when the request completes or after a configurable duration (typically hours). This ensures authority is temporary and task-bounded.

### Misconception 4: Delegation Bypasses Enterprise Controls

**Misconception**: Request-Scoped Delegation allows agents to bypass enterprise policies.

**Reality**: Policy composition requires ALL policies to ALLOW. Delegation Template policies are evaluated alongside Training Spec and Employment Spec policies. Delegation can only narrow authority, never expand it.

### Failure Mode: Consent Fatigue

**Problem**: Users are overwhelmed by frequent delegation prompts, leading to either denial or blind approval.

**Mitigation**: 
- Design focused, understandable templates
- Support implicit fulfillment from existing certificates
- Use proactive delegation when possible (user grants before task starts)
- Provide clear explanations of what authority is needed and why

## Practical Implications

### When to Use Request-Scoped vs Enterprise Delegation

**Use Request-Scoped Delegation when**:
- Agent acts on behalf of business users (customers, partners)
- Authority should expire when task completes
- User consent is required for each task or session
- Agent has minimal enterprise identity (typically "bot" mode)

**Use Enterprise Delegation when**:
- Agent acts on behalf of internal employees or roles
- Authority should persist for agent lifetime
- Authority is granted at deployment time
- Agent has full enterprise identity (User or Role mode)

### Channel Requirements

Request-Scoped Delegation requires scenarios to be triggered via Channels:

- **Web Portal**: User initiates task, grants consent, agent receives token
- **Mobile App**: User initiates task, grants consent via app UI, agent receives token
- **MS Teams**: User initiates task via bot, grants consent, agent receives token

Scenarios triggered by Signal Providers (APIs, event streams) cannot use request-scoped delegation because there is no user interaction point.

### Reactive Delegation Latency Trade-offs

Reactive delegation (agent requests authority mid-execution) introduces latency:

- **User Prompt**: Agent must wait for user to respond to consent prompt
- **Network Latency**: Round-trip through Channel, Cipher, Signal Exchange
- **User Response Time**: User may take minutes or hours to respond

**Mitigation Strategies**:
- Use proactive delegation when possible (user grants before task starts)
- Support implicit fulfillment (auto-fulfill from existing certificates)
- Design agents to degrade gracefully when delegation unavailable
- Provide clear explanations of why authority is needed

### Hybrid Scenarios

Agents can participate in both identity domains simultaneously:

```yaml
# Agent has enterprise identity for internal operations
enterpriseIdentity:
  mode: "bot"
  role: "automated-processor"
  
# Agent also accepts request-scoped delegation for user tasks
requestScopedDelegation:
  enabled: true
  allowedTemplates:
    - "personal-finance-assistant"
```

This enables agents to:
- Perform internal operations using enterprise identity
- Act on behalf of users using request-scoped delegation
- Maintain clear separation between internal and user-facing authority

## Cross-References

- **Section 3.1 (Agent Identity)**: Two-layer identity model (Deployment Identity vs Agent Persona) used in Delegation Access Tokens
- **Section 3.2 (Delegation Chains)**: Enterprise delegation model, distinct from request-scoped delegation
- **Section 3.5 (Cipher IAM Integration)**: Cipher IAM Extensions provide Delegation Templates, Certificates, and Tokens
- **Section 23 (Collaboration Channels)**: Channels facilitate request-scoped delegation via consent UI
- **Section 22.1 (Hub Composite Applications)**: Composite applications can use request-scoped delegation with sub-personas

---

**References:**
*   `olympus-hub-docs/decision-logs/0127-request-scoped-authority-delegation.md` — Architectural decision record
*   `olympus-seer-docs/seer-design/implementation-concepts/request-scoped-delegation.md` — Complete implementation design
*   `olympus-hub-docs/decision-logs/0130-unified-delegation-model.md` — Unified delegation model (scenario-scoped and request-scoped)
*   [OAuth 2.0 RFC 6749](https://tools.ietf.org/html/rfc6749) — OAuth 2.0 specification
