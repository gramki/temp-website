# Request-Scoped Delegation: Context Summary

> **Purpose**: Condensed reference for documentation updates across all phases  
> **Authoritative Source**: [`request-scoped-delegation.md`](../../olympus-seer-docs/seer-design/implementation-concepts/request-scoped-delegation.md)  
> **Design Decisions**: [`0WIP-seer-request-scoped-authority-delegation.md`](./0WIP-seer-request-scoped-authority-delegation.md)

---

## 1. Terminology Glossary

| Term | Definition |
|------|------------|
| **Delegation Template** | Cipher artifact defining a package of delegatable authority; tenant-scoped, human-readable, policy-bearing |
| **Delegation Certificate** | User's signed consent to delegate authority per a template; can specify delegate by identity, role, or group |
| **Delegation Access Token** | Request-scoped JWT enabling agent to act as user; bound to single agent SPIFFE ID |
| **Authority Request** | REQUEST_UPDATE sub-type requesting delegation from Channel |
| **Authority Grant** | REQUEST_UPDATE sub-type delivering token after consent |
| **Chaining** | Agent delegating received authority to another agent (requires certificate permission) |
| **Cascading** | Authority request propagating up request hierarchy to parent |
| **Business User** | End-user (customer, external employee) — not an enterprise operator |
| **Enterprise Identity** | Internal operator identity (bank employee, internal staff) in Cipher IAM |
| **Deferred Delegation** | Employment mode where agent receives no authority at deployment; gets it per-request |

---

## 2. OAuth 2.0 Mapping

| OAuth 2.0 Concept | Request-Scoped Delegation Equivalent |
|-------------------|--------------------------------------|
| **Client** | Employed Agent (identified by SPIFFE ID) |
| **Client Credentials** | Agent's deployment credentials (from EmploymentSpec) |
| **Resource Owner** | Business User (delegator) |
| **Authorization Server** | Cipher IAM Extensions |
| **Scope** | Delegation Template |
| **Authorization Grant** | Delegation Certificate |
| **Access Token** | Delegation Access Token |
| **Resource Server** | Tool Gateway, External APIs |

---

## 3. Critical Invariants

| Invariant | Rule |
|-----------|------|
| **Policy Composition** | All policies must ALLOW (AND/intersection logic): Training Spec + Employment Spec + Delegation Template |
| **Token Binding** | One token per agent; bound to specific SPIFFE ID |
| **Signal Provider vs Channel** | Only Channels can delegate; Signal Providers just forward signals |
| **Template → Certificate → Token** | Hierarchy is always in this order; never reversed |
| **Chaining Control** | Only if certificate explicitly allows `chainingAllowed: true` |
| **Denial/Timeout Default** | Agent continues with degraded capability (can override) |

---

## 4. Delegation Flows

| Flow | Trigger | Description |
|------|---------|-------------|
| **Proactive** | User initiates before scenario | User grants consent via Channel before agent starts work |
| **Reactive** | Agent requests during execution | Agent posts AUTHORITY_REQUEST; Channel prompts user or auto-fulfills |
| **Implicit** | Channel fulfills from certificates | Channel finds matching certificate; no user prompt needed |
| **Cascading** | Child request needs authority | Request walks up hierarchy; parent Channel handles consent |

---

## 5. YAML Schema Snippets

### Delegation Template CRD
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
  constraints:
    maxDuration: "24h"
    chainingAllowed: false
  policies:
    - name: "business-hours-only"
      rego: |
        package delegation
        allow { input.time.hour >= 9; input.time.hour < 17 }
```

### EmploymentSpec Delegation Section
```yaml
spec:
  delegation:
    mode: "deferred"  # vs "user", "role", "bot"
    requestScopedDelegation:
      enabled: true
      allowedTemplates:
        - "personal-finance-assistant"
        - "view-investments"
      chainingPolicy: "template-controlled"
```

### TrainingSpec Delegation Requirements
```yaml
spec:
  delegationRequirements:
    templates:
      - name: "personal-finance-assistant"
        required: true
      - name: "view-investments"
        required: false
    onDelegationUnavailable: "degrade"  # or "fail"
```

### Message Envelope: environment.auth.delegations
```yaml
environment:
  auth:
    identity:
      spiffeId: "spiffe://seer/agents/my-agent"
      delegationMode: "deferred"
    delegations:
      - token: "eyJ..."
        template: "personal-finance-assistant"
        delegator: "user-67890"
        expiresAt: "2026-01-17T22:00:00Z"
```

---

## 6. Confirmed Design Decisions

### From Q&A (Core Patterns)

| Decision | Confirmation |
|----------|--------------|
| Authority Request as REQUEST_UPDATE sub-type | ✅ Follows REMIND pattern |
| Authority Grant delivered as REQUEST_UPDATE | ✅ Token in both payload and environment |
| Channels are observer modules | ✅ Receive all REQUEST_UPDATEs |
| Token in `environment.auth.delegations` | ✅ Signal Exchange refreshes on each update |
| Cascading via Request Hierarchy | ✅ Follows lifecycle cascade pattern |
| Cross-workbench cascading is best-effort async | ✅ Same as lifecycle cascade |
| Implicit fulfillment via existing certificates | ✅ Check certificates first, then prompt |
| Agent cannot query own certificates | ✅ Unless that privilege is delegated |

### C2-Level Architectural Decisions

| Decision | Detail |
|----------|--------|
| **Template Selection Ownership** | Developer/architect responsibility; not automatic |
| **Policy Composition** | All policies must ALLOW (AND logic) |
| **Chaining Flow** | Agent-initiated via SDK; Channel uses Certificates only |
| **Business User Profiles** | Cipher maintains profiles with imported + added claims |
| **Token per Agent** | Each token bound to single agent SPIFFE ID |
| **Denial/Timeout Behavior** | Default is degraded capability continuation |

---

## 7. Component Responsibilities

| Component | Delegation Responsibilities |
|-----------|----------------------------|
| **Channel** | Orchestrate consent flow, request Certificate/Token from Cipher, attach to Request, handle AUTHORITY_REQUEST |
| **Cipher IAM Extensions** | Manage Templates, issue Certificates, issue Tokens, validate credentials, maintain business user profiles |
| **Request Lifecycle Manager** | Store delegation context per Request, provide API for token lookup |
| **Signal Exchange** | Route AUTHORITY_REQUEST/GRANTED updates, refresh `environment.auth.delegations` |
| **Seer Sidecar** | Pre-guardrail delegation check, post AUTHORITY_REQUEST, token injection |
| **Agent Ingress Gateway** | Forward delegation token to agent, token validation |
| **Tool Gateway** | Validate delegation token on tool calls, enforce template policies |
| **Agent SDK** | Provide `request_authority()`, `get_delegation_token()`, `delegate_to_child()` APIs |

---

## 8. Signal Provider vs Channel Distinction

| Aspect | Signal Provider (I/O Gateway) | Channel |
|--------|-------------------------------|---------|
| **Purpose** | Signal ingestion (events, files, API calls) | User interaction interface |
| **Direction** | Primarily inbound; may send responses | Fully bidirectional |
| **User Presence** | No user context; machine-to-machine | User is present and can interact |
| **Delegation Role** | **Cannot delegate** | **Can facilitate delegation** |
| **Examples** | Atropos, Dia, Kale, Cronus | Web Console, MS Teams, MCP, REST API |

**Key Reason**: Signal Providers have no user identity context. Channels interact with authenticated users who can grant or deny delegation.

---

## 9. Sequence Diagram References

| Flow | Comprehensive Doc Section |
|------|--------------------------|
| Proactive Delegation | Section 4.2 |
| Reactive Delegation (Authority Request) | Section 4.3 |
| Implicit Fulfillment | Section 4.4 |
| Cascading via Request Hierarchy | Section 4.5 |
| Policy Composition | Section 6 |
| SDK Usage | Section 8 |

---

## 10. Two Identity Domains

| Domain | Who Delegates | When Configured | Duration | Use Case |
|--------|---------------|-----------------|----------|----------|
| **Enterprise** (User/Role/Bot) | Internal operators | Employment time | Agent lifetime | Internal operations |
| **Business User** (Request-Scoped) | End-users | Request time | Request/session | Represent user |

These are **orthogonal** — an agent may have both simultaneously.
