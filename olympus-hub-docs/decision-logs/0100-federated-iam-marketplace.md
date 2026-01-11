# ADR-0100: Federated IAM for Marketplace

## Status

Accepted

## Date

2026-01-11

## Context

Marketplace is a platform-level service accessed by users from multiple tenant IAM domains. Authentication and authorization must work across tenant boundaries while:

- Maintaining tenant identity
- Protecting user PII
- Enabling publisher/subscriber identification
- Supporting audit trails

### Options

1. **Direct tenant IAM** — Marketplace validates tokens from each tenant IAM
2. **Federated IAM** — Tenant IAM domains federate with Marketplace IAM
3. **Separate accounts** — Users create separate Marketplace accounts

### Requirements

- Seamless access from tenant context
- Identity attribution for actions
- Minimal PII in Marketplace domain
- Publisher/subscriber authentication
- Cross-tenant audit capability

## Decision

**Marketplace uses federated IAM.** All Tenant IAM Domains federate with the Marketplace IAM. Requests from tenant users are authenticated and attributed to a federated identity in the Marketplace domain.

### Federation Model

```
Tenant IAM Domain (e.g., acme-bank)
         │
         │ Federation
         ▼
Marketplace IAM Domain
         │
         │ Federated Identity
         ▼
Marketplace Services
```

### Identity Attributes

| Attribute | Source | Purpose |
|-----------|--------|---------|
| Federated identity ID | Marketplace IAM | Unique identifier in Marketplace |
| Tenant domain reference | Tenant IAM | Links to source tenant |
| Desensitized name | Tenant IAM | Display only (no full PII) |
| Roles | Both domains | Authorization |

### PII Protection

- **No PII beyond desensitized name** is taken to create Marketplace profile
- Email, phone, full name not stored in Marketplace domain
- Audit logs use federated identity ID, not PII

### Authentication Flow

1. User accesses Marketplace Console from tenant desk
2. Tenant IAM issues federated token
3. Marketplace IAM validates and creates/updates federated identity
4. Request attributed to federated identity
5. Marketplace services authenticate and authorize

## Alternatives Considered

### Alternative 1: Direct Tenant IAM Validation

Marketplace directly validates tokens from each tenant IAM.

**Pros:**
- Simpler initial setup
- No separate IAM domain

**Cons:**
- Marketplace needs trust relationships with each tenant
- No unified identity in Marketplace
- Complex multi-tenant token validation
- No Marketplace-scoped roles

**Why rejected:** Doesn't scale well; no unified Marketplace identity model.

### Alternative 2: Separate Marketplace Accounts

Users create separate accounts for Marketplace.

**Pros:**
- Clear separation
- Full control over Marketplace identity

**Cons:**
- Poor UX (another account to manage)
- Identity linking complexity
- Duplicate identity management

**Why rejected:** Poor user experience; unnecessary identity duplication.

## Consequences

### Positive

- Seamless SSO from tenant context
- Unified identity model in Marketplace
- PII protection (minimal data in Marketplace)
- Clear audit attribution
- Publisher/subscriber always authenticated

### Negative

- Federation setup required per tenant
- Federated identity management complexity
- Token validation latency

### Neutral

- Marketplace-specific roles can be defined
- Federation configuration managed by Hub Win team

## Implementation Notes

- Federation established when tenant subscription created
- Federated identity created on first Marketplace access
- Desensitized name extracted from tenant profile
- Marketplace IAM uses Cipher IAM infrastructure

## References

- [Security and Compliance](../04-subsystems/marketplace/security-and-compliance.md)
- [Cipher IAM](../04-subsystems/supporting-systems/cipher-iam.md)
- [ADR-0093: Marketplace as Platform Service](./0093-marketplace-platform-service.md)

