# ADR-0130: Unified Delegation Model (Scenario-Scoped vs Request-Scoped)

> **Status**: Accepted  
> **Date**: 2026-01-17  
> **Authors**: Architecture Team  
> **Related ADRs**: [ADR-0129: Agent Identity Model](./0129-agent-identity-model.md), [ADR-0127: Request-Scoped Authority Delegation](./0127-request-scoped-authority-delegation.md)

---

## Context

The current documentation presents scenario-scoped and request-scoped delegation as separate mechanisms:

- **Scenario-Scoped Delegation**: Authority derives from Scenario Identity Profile (created at deployment)
- **Request-Scoped Delegation**: Authority derives from Business User consent (created per-request)

However, they share identical semantics:
- Both use Delegation Templates to define delegatable authority
- Both use Delegation Certificates to represent consent
- Both use Delegation Access Tokens for runtime authorization
- Both follow the same token structure (including `client_id`, `sub`, `delegated_by`)

The only difference is **when the Certificate is created** and **who grants the authority**.

---

## Decision

**Unify scenario-scoped and request-scoped delegation as a single mechanism with two modes.**

### Unified Model

Both modes use the same components and semantics:

```
┌─────────────────────────────────────────────────────────────────────┐
│                     DELEGATION TEMPLATE                              │
│  Defines: What authority CAN be delegated                           │
│  Created by: Tenant Admin in Cipher IAM                             │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     DELEGATION CERTIFICATE                            │
│  Represents: Consent to delegate                                    │
│  Created by: Scenario Identity Profile (scenario-scoped) OR         │
│              Business User via Channel (request-scoped)              │
│  Timing: At deployment (scenario-scoped) OR per-request (request-scoped) │
└─────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────┐
│                   DELEGATION ACCESS TOKEN                             │
│  Represents: Request-scoped authority for a specific agent            │
│  Created by: Cipher IAM Extensions                                   │
│  Timing: ALWAYS per-request (from Certificate)                       │
│  Bound to: Single agent (SPIFFE ID), Single request                  │
└─────────────────────────────────────────────────────────────────────┘
```

### Mode Differences

| Aspect | Scenario-Scoped Mode | Request-Scoped Mode |
|--------|---------------------|---------------------|
| **Certificate Source** | Scenario Identity Profile | Business User (via Channel) |
| **Certificate Timing** | Created at deployment | Created per-request (when user grants) |
| **Token Timing** | Per-request (from Certificate) | Per-request (from Certificate) |
| **Token Semantics** | Identical | Identical |
| **Token Structure** | Identical (`client_id`, `sub`, `delegated_by`) | Identical |
| **Employment Spec** | Specifies delegation templates and policies | Specifies delegation templates and policies |
| **Identity Profile** | Not named in Employment Spec (comes from Scenario) | Not named in Employment Spec (comes from request) |

### Key Principle: Hybrid Token Issuance

Both modes use the same pattern:
- **Certificate** created at source time (deployment for scenario-scoped, request for request-scoped)
- **Token** always issued per-request from the Certificate
- Same semantics, different timing of Certificate creation

---

## Rationale

### Why Unify?

1. **Semantic Consistency**: Both modes use identical token structures and delegation flows
2. **Implementation Simplicity**: Single code path for token issuance and validation
3. **Documentation Clarity**: One model to explain, with clear mode distinction
4. **Future Extensibility**: Easy to add new modes (e.g., role-scoped, time-scoped) without new mechanisms

### Why Two Modes?

1. **Different Authority Sources**:
   - Scenario-scoped: Enterprise authority (Scenario Identity Profile)
   - Request-scoped: Business user authority (per-request consent)

2. **Different Use Cases**:
   - Scenario-scoped: Long-lived operational agents with stable authority
   - Request-scoped: Temporary, task-bounded agents with user-granted authority

3. **Different Lifecycles**:
   - Scenario-scoped: Certificate created once at deployment, tokens issued per-request
   - Request-scoped: Certificate created per-request, tokens issued per-request

### Why Not Separate Mechanisms?

**Rejected because**:
- Duplicates code and documentation
- Creates confusion about which to use when
- Makes it harder to support hybrid scenarios (e.g., scenario-scoped agent that also accepts request-scoped delegation)
- Breaks the principle of "same semantics, different source"

---

## Consequences

### Benefits

- **Consistency**: Single model for all delegation scenarios
- **Simplicity**: One set of components (Templates, Certificates, Tokens)
- **Clarity**: Clear mode distinction without mechanism confusion
- **Flexibility**: Easy to support hybrid scenarios or new modes

### Trade-offs

- **Mode Selection**: Must clearly document when to use which mode
- **Certificate Timing**: Different timing may require different implementation paths (but same semantics)

### Implications

| Scenario | Mode | Certificate Source | Certificate Timing |
|----------|------|-------------------|-------------------|
| Operational agent with stable authority | Scenario-scoped | Scenario Identity Profile | At deployment |
| User-initiated task with temporary authority | Request-scoped | Business User | Per-request |
| Agent that can accept both | Both | Scenario Identity Profile OR Business User | Deployment OR per-request |

---

## Implementation Notes

### Employment Spec Structure

Employment Spec specifies delegation templates and policies, not identity profile references:

```yaml
spec:
  # Reference to Scenario (source of Agent Persona)
  scenarioRef:
    name: dispute-resolution
    workbench: acme-disputes
    
  # Delegation configuration (unified model)
  delegation:
    # Mode determines source
    mode: scenario-scoped  # or "request-scoped"
    
    # Templates this employment accepts (same for both modes)
    allowedTemplates:
      - analyze-disputes
      - review-analysis
      - approve-resolution
    
    # Additional policies (same for both modes)
    policies:
      - pep: tool-gateway
        policy: dispute-tool-policy
      - pep: signal-exchange
        policy: dispute-signal-policy
    
    # Chaining policy (same for both modes)
    chainingPolicy: template-controlled  # or "never" or "with-approval"
    
    # Behavior when delegation denied (same for both modes)
    onDelegationDenied: continue-degraded  # or "fail" or "escalate"
```

**Key Points**:
- Employment Spec does NOT name the identity profile (comes from Scenario or request)
- Same structure for both modes
- Mode determines source, not mechanism

### Token Structure (Unified)

Both modes produce identical token structure:

```json
{
  "sub": "dispute-resolution-agent@acme.hub.io",  // Agent Persona
  "iss": "cipher.hub.olympus.io",
  "client_id": "spiffe://acme.hub.io/seer/agent/acme/fraud-analyst-pod-001",  // Deployment Identity
  "delegated_by": "dispute-scenario-profile",  // Scenario Identity Profile (scenario-scoped) OR "user-12345" (request-scoped)
  "certificate_id": "cert-abc123",  // Delegation Certificate ID
  "template": "analyze-disputes",  // Delegation Template
  "scopes": ["disputes:read", "disputes:analyze"],
  "exp": "2026-01-17T22:00:00Z"
}
```

### Certificate Lifecycle

**Scenario-Scoped**:
1. Deployment time: Scenario Identity Profile creates Delegation Certificate
2. Certificate stored, referenced by Employment Spec
3. Per-request: Token issued from Certificate

**Request-Scoped**:
1. Request time: Business User grants consent via Channel
2. Channel requests Delegation Certificate from Cipher
3. Certificate created, stored
4. Per-request: Token issued from Certificate

**Key Insight**: Certificate timing differs, but token issuance is identical.

---

## Alternatives Considered

### Alternative 1: Separate Mechanisms

Keep scenario-scoped and request-scoped as completely separate mechanisms.

**Rejected because**:
- Duplicates code and documentation
- Creates confusion about which to use
- Makes hybrid scenarios difficult
- Breaks semantic consistency

### Alternative 2: Request-Scoped Only

Use only request-scoped delegation, create certificates at deployment for scenario-scoped.

**Rejected because**:
- Loses clarity about authority source (Scenario vs User)
- Makes it harder to distinguish operational vs user-initiated agents
- Breaks the principle of explicit consent timing

### Alternative 3: Scenario-Scoped Only

Use only scenario-scoped delegation, create certificates per-request for request-scoped.

**Rejected because**:
- Loses clarity about temporary vs permanent authority
- Makes it harder to distinguish enterprise vs business user delegation
- Breaks the principle of different authority sources

---

## Related Documentation

- [ADR-0129: Agent Identity Model](./0129-agent-identity-model.md) — Two-layer identity model used by both modes
- [ADR-0127: Request-Scoped Authority Delegation](./0127-request-scoped-authority-delegation.md) — Detailed request-scoped delegation design
- [Agent Identity Ambiguity Resolution](../../scratchpad/0WIP-agent-identity-ambiguity-resolution.md) — Original problem analysis
