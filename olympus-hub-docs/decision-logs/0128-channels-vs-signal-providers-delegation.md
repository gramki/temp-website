# ADR-0128: Channels vs Signal Providers for Delegation

> **Status**: Proposed  
> **Date**: 2026-01-17  
> **Authors**: Architecture Team  
> **Related ADRs**: [ADR-0127: Request-Scoped Authority Delegation](./0127-request-scoped-authority-delegation.md)

---

## Context

Request-Scoped Authority Delegation requires explicit user consent to grant agents authority to act on their behalf. The Hub platform has two main ingestion patterns:

1. **Signal Providers (I/O Gateways)**: Ingest signals from external systems (Atropos for events, Dia for files, Kale for scheduled triggers)
2. **Channels**: User interaction interfaces (Web Console, MS Teams, MCP, REST API with user context)

We need to decide which component(s) can facilitate delegation.

---

## Decision

**Only Channels can facilitate Request-Scoped Authority Delegation.** Signal Providers cannot delegate.

### Distinction

| Aspect | Signal Provider | Channel |
|--------|----------------|---------|
| **Purpose** | Signal ingestion (events, files, API calls) | User interaction interface |
| **Direction** | Primarily inbound; may send responses | Fully bidirectional |
| **User Presence** | No user context; machine-to-machine | User is present and can interact |
| **Delegation Role** | **Cannot delegate** | **Can facilitate delegation** |
| **Examples** | Atropos, Dia, Kale, Cronus | Web Console, MS Teams, MCP, REST API |

### Rationale

1. **User Identity**: Signal Providers operate without direct user identity context. They handle machine-to-machine communication. Channels, by definition, interact with authenticated users.

2. **Consent Capture**: Delegation requires explicit user consent. Only Channels can present a consent UI (or handle programmatic consent for API Channels).

3. **Reactive Flow**: Channels receive `REQUEST_UPDATE` messages including `AUTHORITY_REQUEST`, enabling them to prompt users for reactive delegation. Signal Providers are fire-and-forget.

4. **Certificate Attachment**: Only Channels can attach Delegation Certificates to initial Hub Requests or send `AUTHORITY_GRANTED` updates.

---

## Consequences

### Benefits

- **Clear separation**: Ingestion (Signal Providers) vs. interaction (Channels) have distinct roles
- **Security**: Delegation is always tied to authenticated user interaction
- **Auditability**: Consent is captured at a known interaction point

### Trade-offs

- **No automated delegation**: Signal-triggered workflows cannot automatically have user delegation
- **Channel dependency**: Request-scoped features require Channel initiation or intervention

### Implications

| Pattern | Supported? | Notes |
|---------|------------|-------|
| User initiates via Channel, agent works with delegation | ✅ | Primary use case |
| Signal triggers work, agent requests delegation mid-flow | ✅ | Channel prompts user via Authority Request |
| Signal triggers work, no user interaction, full automation | ❌ | Use enterprise delegation (Role/Bot mode) instead |
| Proactive delegation before signal-triggered work | ✅ | User pre-authorizes via Channel; certificate stored |

---

## Alternatives Considered

### Alternative 1: Allow Signal Providers to Carry Pre-Authorized Tokens

Signal Providers could include pre-authorized Delegation Access Tokens from external systems.

**Rejected because**:
- External systems issuing Hub tokens breaks security model
- No way to validate external consent
- Token lifecycle management complexity

### Alternative 2: Implicit Delegation from Signal Context

Derive delegation from signal metadata (e.g., if signal includes customer ID, assume delegation).

**Rejected because**:
- No explicit consent
- Violates principle of least privilege
- Regulatory/compliance issues with assumed consent

### Alternative 3: Signal Providers as Minimal Channels

Add consent capabilities to Signal Providers.

**Rejected because**:
- Blurs architectural distinction
- Signal Providers would need bidirectional user interaction
- Essentially makes them Channels anyway

---

## Implementation Notes

### Channel Responsibilities

1. **Proactive Delegation**: Present Delegation Template, capture consent, request Certificate/Token from Cipher
2. **Reactive Delegation**: Receive `AUTHORITY_REQUEST`, prompt user, request Token from Cipher, send `AUTHORITY_GRANTED`
3. **Implicit Fulfillment**: Check existing Certificates before prompting
4. **Observer Registration**: Subscribe to `REQUEST_UPDATE` messages for delegation events

### Signal Provider Behavior

1. **No Delegation Context**: Signal Providers do not attach delegation information
2. **Enterprise Delegation Only**: Signals trigger work under agent's enterprise authority
3. **Delegation via Cascade**: If work needs user delegation, Authority Request cascades to parent Channel

---

## References

- [Channel Implementation Concept](../../02-system-design/implementation-concepts/channel.md)
- [Signal Exchange](../../04-subsystems/signal-exchange/README.md)
- [Request-Scoped Authority Delegation](../../olympus-seer-docs/seer-design/implementation-concepts/request-scoped-delegation.md)
