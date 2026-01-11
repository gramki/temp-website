# ADR-0099: Publisher Registration Approval

## Status

Accepted

## Date

2026-01-11

## Context

Not every Hub tenant should automatically be able to publish packages to the Marketplace. Publishing requires:

- Trust establishment (is the publisher legitimate?)
- Quality expectations (will packages meet standards?)
- Security verification (is the signing certificate valid?)
- Commercial/legal considerations (future)

### Options

1. **Open publishing** — Any tenant can publish immediately
2. **Admin approval** — Tenant admin enables publishing for their subscription
3. **Hub Win approval** — Platform team reviews and approves publishers
4. **Tiered model** — Different approval levels for different publishing scopes

### Requirements

- Quality and trust verification before publishing
- Signing certificate management
- Audit trail for publisher approvals
- Scalable process for growing ecosystem

## Decision

**Publisher registration requires Hub Win (Customer Success) team approval.** Tenant admin initiates registration, submits signing certificate, and Hub Win team reviews and authorizes.

### Registration Flow

```
1. Tenant Admin initiates publisher registration
   └── Submits: Publisher name, contact info, signing certificate

2. Hub Win team receives registration request
   └── Reviews: Business legitimacy, signing certificate validity

3. Hub Win team approves/rejects
   └── If approved: Publisher is registered, can publish packages
   └── If rejected: Tenant notified with reason

4. Signing certificate stored
   └── Associated with publisher for container signing verification
```

### Prerequisites for Publishing

- Publisher registration approved
- Valid signing certificate on file
- At least one workbench in subscription

## Alternatives Considered

### Alternative 1: Open Publishing

Any tenant can publish without approval.

**Pros:**
- Low friction
- Fast ecosystem growth
- Self-service

**Cons:**
- No quality control
- Security risks (malicious packages)
- Trust issues
- Spam/abuse potential

**Why rejected:** Enterprise marketplace requires trust and quality guarantees.

### Alternative 2: Tenant Admin Only

Tenant admin can enable publishing for their subscription.

**Pros:**
- Self-service
- Tenant-level control

**Cons:**
- No platform-level oversight
- No signing certificate validation
- Trust established only at tenant level

**Why rejected:** Platform needs oversight for cross-tenant sharing.

### Alternative 3: Automated Approval

Automatic approval based on criteria (e.g., tenant tier, history).

**Pros:**
- Scalable
- Fast for qualified tenants

**Cons:**
- Complex criteria management
- Edge cases need manual handling
- Initial criteria hard to define

**Why rejected:** Initially manual approval is simpler; automation can be added later.

## Consequences

### Positive

- Trust established before publishing
- Signing certificates validated
- Hub Win maintains quality oversight
- Audit trail for all publishers
- Security baseline enforced

### Negative

- Approval latency (not instant)
- Hub Win team workload
- Barrier to entry for new publishers

### Neutral

- Process can be streamlined over time
- Criteria can evolve
- Automation can be added for trusted categories

## Implementation Notes

- Publisher registration via Marketplace Console or Admin Desk
- Hub Win uses Hub Win Ops Center for approval workflow
- Signing certificate stored securely
- Publisher status visible in subscription settings

## References

- [Publishing Services](../04-subsystems/marketplace/publishing-services.md)
- [Hub Win Ops Center](../06-ux-architecture/publisher-domain/hub-win-ops-center.md)
- [Security and Compliance](../04-subsystems/marketplace/security-and-compliance.md)

