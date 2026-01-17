# ADR-0127: Request-Scoped Authority Delegation

> **Status**: Proposed  
> **Date**: 2026-01-17  
> **Authors**: Architecture Team  
> **Related ADRs**: [ADR-0073: Authority Enforcement via OPA](./0073-seer-authority-enforcement-opa.md)

---

## Context

Seer's existing delegation model (User, Role, Bot) operates in the **Enterprise/Operator Identity Domain** — delegating authority from bank employees and internal roles to agents. However, business-facing agents need to act on behalf of **end-users** (customers, external employees) who are not part of the enterprise's internal IAM.

### The Gap

| Scenario | Who Delegates? | Problem |
|----------|----------------|---------|
| Personal Finance AI | Retail banking customer | Customer isn't a bank employee |
| Expense Approval Bot | Company employee (customer's staff) | External employee, not in bank's IAM |
| Family Banking Agent | Parent (customer) | Customer delegating for family |

The existing User/Role/Bot models cannot capture business user consent or provide fine-grained, request-scoped authority for end-user interactions.

---

## Decision

We introduce **Request-Scoped Authority Delegation** as a second identity domain alongside existing enterprise delegation. This enables agents to receive authority from business users within the scope of a specific Hub Request.

### Key Design Elements

1. **Two Orthogonal Identity Domains**:
   - **Enterprise Delegation** (User/Role/Bot): Internal operations
   - **Request-Scoped Delegation**: Business user authority per-request

2. **OAuth 2.0-Inspired Model**:
   | OAuth 2.0 | Request-Scoped Delegation |
   |-----------|---------------------------|
   | Client | Employed Agent |
   | Resource Owner | Business User |
   | Authorization Server | Cipher IAM Extensions |
   | Scope | Delegation Template |
   | Access Token | Delegation Access Token |

3. **Core Artifacts**:
   - **Delegation Template**: Defines delegatable authority packages
   - **Delegation Certificate**: Represents user consent
   - **Delegation Access Token**: Request-scoped JWT for enforcement

4. **Delegation Flows**:
   - **Proactive**: User grants before agent starts
   - **Reactive**: Agent requests mid-execution via `AUTHORITY_REQUEST`
   - **Implicit**: Channel auto-fulfills from existing certificates
   - **Cascading**: Request hierarchy propagation

5. **Policy Composition**: All applicable policies (Training Spec, Employment Spec, Delegation Template) must ALLOW (AND logic).

---

## Consequences

### Benefits

- **End-user delegation**: Customers can delegate to agents acting on their behalf
- **Fine-grained control**: Delegation Templates provide clear, auditable authority packages
- **Request isolation**: Authority is scoped to specific requests, not agent lifetime
- **Composable**: Works alongside existing enterprise delegation
- **Consent capture**: Explicit user consent via Channels

### Trade-offs

- **Increased complexity**: Second identity domain to manage
- **Channel dependency**: Only Channels (not Signal Providers) can facilitate delegation
- **Latency**: Reactive delegation adds user prompt latency
- **Federation**: Business user identity federation required

### Risks

| Risk | Mitigation |
|------|------------|
| Consent fatigue | Clear, concise Delegation Template descriptions |
| Token misuse | Short-lived tokens, SPIFFE binding, PEP enforcement |
| Scope creep | Policy composition requires all policies to ALLOW |

---

## Alternatives Considered

### Alternative 1: Extend Existing User Delegation

Create business user accounts in enterprise IAM and use standard User delegation.

**Rejected because**:
- Conflates enterprise and business user identity domains
- Scaling issues with potentially millions of customer accounts
- Privacy concerns with storing customer data in internal IAM

### Alternative 2: API Key per User

Issue long-lived API keys to customers.

**Rejected because**:
- No consent granularity
- Key management at scale is complex
- No request-scoped expiration

### Alternative 3: Session-Based Delegation

Tie delegation to user's web session only.

**Rejected because**:
- Doesn't support proactive delegation (before session)
- Limits asynchronous agent operations
- Session expiry breaks ongoing work

---

## Implementation

See the comprehensive design: [Request-Scoped Authority Delegation](../../olympus-seer-docs/seer-design/implementation-concepts/request-scoped-delegation.md)

### Key Subsystem Changes

| Subsystem | Changes |
|-----------|---------|
| Cipher IAM Extensions | Delegation Templates, Certificates, Tokens, Business User Profiles |
| Signal Exchange | Token refresh, AUTHORITY_REQUEST/GRANTED routing |
| Request Lifecycle Manager | Delegation context storage and API |
| Seer Sidecar | Delegation service, pre-guardrail check, token injection |
| Agent SDK | `request_authority()`, `get_delegation_token()`, `delegate_to_child()` |
| Channels | Consent UI, Authority Request handling |

---

## References

- [Request-Scoped Delegation Implementation Concept](../../olympus-seer-docs/seer-design/implementation-concepts/request-scoped-delegation.md)
- [OAuth 2.0 RFC 6749](https://tools.ietf.org/html/rfc6749)
- [SPIFFE Specification](https://spiffe.io/docs/latest/spiffe-about/overview/)
