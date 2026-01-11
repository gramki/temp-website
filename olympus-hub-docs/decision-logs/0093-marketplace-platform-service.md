# ADR-0093: Marketplace as Platform Service

## Status

Accepted

## Date

2026-01-11

## Context

Hub needs a Marketplace subsystem to allow developers to publish reusable artifacts (Scenarios, Workbenches, Tools, etc.) for other Hub subscribers to discover and deploy. A key architectural decision is whether the Marketplace should operate at:

1. **Platform level** — A single, shared Marketplace instance serving all tenants
2. **Tenant level** — Each tenant has its own private Marketplace
3. **Hybrid** — Platform Marketplace with optional tenant-scoped extensions

### Constraints

- Enterprise customers may need to share artifacts within their organization only
- Some customers may want to exclude certain tenants (e.g., sanctioned organizations)
- Large enterprises may have multiple related tenants that need private sharing
- Platform-level infrastructure is simpler to operate and maintain

### Requirements

- Support public sharing across all tenants
- Support private sharing within enterprise boundaries
- Support exclusion of specific tenants
- Minimize infrastructure complexity

## Decision

**Marketplace is a platform-level service.** A single Marketplace instance serves all tenants. Private/restricted visibility is achieved through **visibility controls** in package manifests, not separate infrastructure.

### Visibility Controls

Publishers can specify in their package manifest:
- **Tenant allow list** — Only specified tenants can see/subscribe to the package
- **Tenant disallow list** — Specified tenants are blocked from seeing the package
- **Region allow/disallow lists** — Control availability by region

This enables:
- **Public packages** — No restrictions, visible to all
- **Private packages** — Allow list contains only related tenants
- **Restricted packages** — Disallow list excludes specific tenants

## Alternatives Considered

### Alternative 1: Tenant-Scoped Marketplaces

Each tenant gets its own Marketplace instance with separate storage and catalog.

**Pros:**
- Complete isolation
- Independent scaling
- Tenant-specific customization

**Cons:**
- High infrastructure overhead
- Cross-tenant sharing requires complex federation
- Duplicate storage for shared packages
- Complex operations

**Why rejected:** Infrastructure overhead outweighs benefits; visibility controls achieve the same goals more efficiently.

### Alternative 2: Hybrid Model

Platform Marketplace plus optional tenant-scoped extensions.

**Pros:**
- Flexibility
- Best of both worlds

**Cons:**
- Complex architecture
- Unclear boundaries
- Dual maintenance burden

**Why rejected:** Visibility controls in platform Marketplace provide sufficient flexibility without complexity.

## Consequences

### Positive

- Single infrastructure to operate
- Simplified architecture
- No duplication of shared packages
- Visibility controls provide fine-grained access control
- Publishers maintain control over who sees their packages

### Negative

- All packages stored in single repository (though visibility-filtered)
- Requires careful visibility enforcement at query time
- No complete physical isolation between tenants

### Neutral

- Publishers must understand visibility control model
- Hub Win team manages region lists

## Implementation Notes

- Visibility controls enforced at query time by Catalog Services
- OpenSearch indexes include visibility metadata for efficient filtering
- Tenant allow/disallow lists are private to the publisher

## References

- [Marketplace Subsystem](../04-subsystems/marketplace/README.md)
- [Catalog Services](../04-subsystems/marketplace/catalog-services.md)

