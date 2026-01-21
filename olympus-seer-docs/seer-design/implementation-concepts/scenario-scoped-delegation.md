# Scenario-Scoped Delegation

> **Category:** Agent Delegation  
> **Status:** 🟢 Design Complete  
> **Last Updated:** 2026-01-21  
> **Related:** [Request-Scoped Delegation](./request-scoped-delegation.md), [Delegation Chains](./delegation-chains.md), [ADR-0130: Unified Delegation Model](../../../olympus-hub-docs/decision-logs/0130-unified-delegation-model.md)

---

## Overview

**Scenario-Scoped Delegation** enables Employed Agents to act on behalf of a **Scenario Identity Profile** with **stable, enterprise-granted authority**. Authority is established at deployment time and remains valid for the lifetime of the employment.

This is one of two modes in the [Unified Delegation Model](../../../olympus-hub-docs/decision-logs/0130-unified-delegation-model.md) for business user delegation.

---

## Purpose

Scenario-scoped delegation addresses the need for **operational agents with stable authority**:

| Need | How Scenario-Scoped Addresses It |
|------|----------------------------------|
| **Consistent authority** | Certificate created once at deployment; no per-request consent needed |
| **Enterprise processes** | Authority derives from Scenario Identity Profile, not individual users |
| **Operational continuity** | Authority persists across requests; doesn't expire per-task |
| **Audit traceability** | All actions traceable to the Scenario Identity Profile |

**Primary Use Cases:**
- Dispute resolution agents processing cases continuously
- Fraud detection agents monitoring transactions
- Document processing agents handling enterprise workflows
- Any operational automation with stable, enterprise-level authority

---

## Contrast with Other Delegation Types

### vs Request-Scoped Delegation

| Aspect | Scenario-Scoped | Request-Scoped |
|--------|-----------------|----------------|
| **Purpose** | Long-lived operational agents | Temporary, task-bounded agents |
| **Authority Source** | Scenario Identity Profile (enterprise) | Business User consent (customer) |
| **Certificate Timing** | At deployment | Per-request |
| **Authority Duration** | Employment lifetime | Request duration |
| **User Interaction** | None required | Consent capture via Channel |
| **Typical Agent** | Enterprise automation | Customer-facing assistant |

### vs Enterprise Delegation (User/Role/Bot)

| Aspect | Scenario-Scoped | Enterprise Delegation |
|--------|-----------------|----------------------|
| **Identity Domain** | Business User (via Scenario Profile) | Enterprise IAM |
| **Delegator** | Scenario Identity Profile | Enterprise user or role |
| **Mechanism** | Delegation Certificate + Token | Direct IAM inheritance |
| **Real-Time Sync** | No (fixed at deployment) | Yes (shrinks with delegator) |
| **Accountable Human** | Via Scenario | Via Employment Spec |

**Key Insight:** Scenario-scoped delegation uses the **business user delegation mechanism** (Templates, Certificates, Tokens) but with authority granted by the **enterprise** at deployment time rather than by an end-user at request time.

---

## How It Works

### Certificate Lifecycle

```
Deployment Time:
┌─────────────────────────────────────────────────────────────────────┐
│  1. Scenario deployed with Identity Profile                         │
│  2. Operator creates EmploymentSpec referencing Scenario            │
│  3. Operator specifies delegation mode: "scenario-scoped"           │
│  4. Scenario Identity Profile creates Delegation Certificate        │
│  5. Certificate stored, referenced by EmploymentSpec                │
└─────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
Per-Request:
┌─────────────────────────────────────────────────────────────────────┐
│  1. Agent receives REQUEST_UPDATE                                   │
│  2. Signal Exchange fetches Certificate from deployment context     │
│  3. Cipher issues fresh Delegation Access Token from Certificate    │
│  4. Token placed in environment.auth.delegations                    │
│  5. Agent uses token for authorized actions                         │
└─────────────────────────────────────────────────────────────────────┘
```

### Token Issuance

Tokens are **always issued per-request**, even though the certificate is created at deployment:

```
Certificate (Deployment Time)          Token (Per-Request)
┌──────────────────────────┐          ┌──────────────────────────┐
│ certificate_id: cert-123 │ ───────▶ │ certificate_id: cert-123 │
│ template: analyze-disputes│          │ template: analyze-disputes│
│ delegator: scenario-profile│          │ delegated_by: scenario-profile│
│ valid_until: 2027-01-21  │          │ exp: 2026-01-21T23:00:00Z │
│                          │          │ client_id: spiffe://...   │
│                          │          │ sub: agent-persona        │
└──────────────────────────┘          └──────────────────────────┘
```

**Why per-request tokens from deployment-time certificates?**
- Tokens are short-lived for security
- Certificate can be revoked without redeploying
- Same mechanism as request-scoped; only timing differs

---

## Configuration

### Employment Spec

```yaml
apiVersion: seer.zeta.tech/v1
kind: EmploymentSpec
metadata:
  name: dispute-resolver-employment
  namespace: acme-disputes
spec:
  # Reference to Scenario (source of Agent Persona)
  scenarioRef:
    name: dispute-resolution
    workbench: acme-disputes
  
  # Delegation configuration
  delegation:
    # Mode: scenario-scoped or request-scoped
    mode: scenario-scoped
    
    # Templates this employment can use
    allowedTemplates:
      - analyze-disputes
      - review-analysis
      - approve-resolution
    
    # Additional policies (narrowing only)
    policies:
      - pep: tool-gateway
        policy: dispute-tool-policy
      - pep: signal-exchange
        policy: dispute-signal-policy
    
    # Chaining policy
    chainingPolicy: template-controlled
    
    # Behavior when delegation unavailable
    onDelegationUnavailable: fail
```

**Key Points:**
- `mode: scenario-scoped` — authority from Scenario Identity Profile
- `allowedTemplates` — which Delegation Templates can be used
- `policies` — additional narrowing policies (cannot expand beyond template)
- Identity Profile comes from Scenario; not specified in EmploymentSpec

### Scenario Identity Profile

The Scenario defines its Identity Profile, which becomes the delegator:

```yaml
apiVersion: hub.olympus.io/v1
kind: ScenarioNormativeSpec
metadata:
  name: dispute-resolution
spec:
  identity:
    profile: dispute-resolution-profile
    owner: operations-manager@acme.com
    delegationTemplates:
      - analyze-disputes
      - review-analysis
```

---

## Components Involved

### Seer Components

| Component | Role |
|-----------|------|
| **Seer Operator** | Processes EmploymentSpec; provisions IAM resources |
| **Cipher IAM Extensions** | Creates Delegation Certificate at deployment |
| **Seer Sidecar** | Fetches token; injects into agent context |
| **Agent SDK** | Provides `get_delegation_token()` API |

### Hub Components

| Component | Role |
|-----------|------|
| **Signal Exchange** | Refreshes tokens on REQUEST_UPDATE delivery |
| **Request Lifecycle Manager** | Stores deployment delegation context |
| **Scenario Registry** | Provides Identity Profile reference |

---

## Policy Composition

When an agent uses scenario-scoped delegation, **all applicable policies must ALLOW**:

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

This is **narrowing-only** — delegation can never expand authority beyond what any layer allows.

---

## Token Placement

Tokens are placed in the message envelope by Signal Exchange:

```yaml
environment:
  auth:
    identity:
      spiffeId: "spiffe://seer/agents/dispute-resolver"
      delegationMode: "scenario-scoped"
    
    delegations:
      - token: "eyJ..."
        template: "analyze-disputes"
        delegator: "dispute-resolution-profile"
        expiresAt: "2026-01-21T23:00:00Z"
```

Signal Exchange refreshes tokens on every REQUEST_UPDATE delivery to ensure:
- Fresh short-lived tokens
- Certificate revocations are reflected
- Policy changes are applied

---

## Examples

### Example 1: Dispute Resolution Agent

**Scenario:** Agent processes dispute cases with stable enterprise authority.

```yaml
# EmploymentSpec
spec:
  scenarioRef:
    name: dispute-resolution
    workbench: acme-disputes
  delegation:
    mode: scenario-scoped
    allowedTemplates:
      - analyze-disputes
      - approve-refunds
```

**Behavior:**
- Certificate created at deployment from `dispute-resolution` Scenario's Identity Profile
- Agent processes any dispute case with consistent authority
- No user consent required per-case
- All actions attributed to Scenario Identity Profile

### Example 2: Fraud Detection Agent

**Scenario:** Agent monitors transactions with read-only analysis authority.

```yaml
spec:
  scenarioRef:
    name: fraud-detection
    workbench: acme-security
  delegation:
    mode: scenario-scoped
    allowedTemplates:
      - analyze-transactions
    policies:
      - pep: data-gateway
        policy: read-only-transactions
```

**Behavior:**
- Stable authority for transaction analysis
- Policy limits to read-only (cannot modify transactions)
- Continuous operation without per-transaction consent

### Example 3: Hybrid Agent (Both Modes)

**Scenario:** Agent handles both enterprise tasks and customer requests.

```yaml
spec:
  scenarioRef:
    name: customer-service
    workbench: acme-support
  delegation:
    mode: both  # Accept either mode
    allowedTemplates:
      - handle-inquiries      # Scenario-scoped
      - act-on-behalf        # Request-scoped (customer consent)
```

**Behavior:**
- Enterprise tasks use scenario-scoped certificate
- Customer-specific tasks require request-scoped consent
- Same agent, different authority sources depending on context

---

## Related Documentation

| Concept | Relationship |
|---------|--------------|
| [Request-Scoped Delegation](./request-scoped-delegation.md) | Alternative mode for per-request user consent |
| [Delegation Chains](./delegation-chains.md) | Enterprise delegation (User/Role/Bot modes) |
| [Agent Identity & Credentials](./agent-identity-credentials.md) | How identity is created from delegation |
| [Authority Enforcement](./authority-enforcement.md) | How delegation authority is enforced |

| ADR | Decision |
|-----|----------|
| [ADR-0130](../../../olympus-hub-docs/decision-logs/0130-unified-delegation-model.md) | Unified Delegation Model |
| [ADR-0129](../../../olympus-hub-docs/decision-logs/0129-agent-identity-model.md) | Agent Identity Model |

---

*Scenario-scoped delegation enables operational agents to act with stable, enterprise-granted authority — without requiring per-request user consent while maintaining the same token semantics as request-scoped delegation.*
