# ADR-0098: Visibility Controls for Private Marketplace

## Status

Accepted

## Date

2026-01-11

## Context

While Marketplace is a platform-level service (ADR-0093), enterprises need mechanisms for private sharing scenarios:

- Large enterprises with multiple related tenants
- Partners who want to share packages exclusively
- Exclusion of specific tenants (e.g., sanctioned organizations)
- Regional availability restrictions

### Options

1. **Separate private marketplace infrastructure**
2. **Visibility controls in package manifest**
3. **Access control lists at tenant level**

### Requirements

- Support private sharing without separate infrastructure
- Publisher controls who can see their packages
- Support both allow and disallow lists
- Support regional restrictions

## Decision

**Visibility controls are specified in the package manifest.** Publishers define allow/disallow lists for tenants and regions directly in their package manifest. No separate private marketplace infrastructure is needed.

### Visibility Control Fields

```yaml
visibility:
  visibility_mode: "restricted"  # public | restricted | private
  
  tenant_allow_list:
    - "tenant-acme-corp"
    - "tenant-acme-subsidiary"
  
  tenant_disallow_list:
    - "tenant-sanctioned-org"
  
  region_allow_list:
    - "us-east-1"
    - "eu-west-1"
  
  region_disallow_list:
    - "cn-north-1"
```

### Visibility Modes

| Mode | Behavior |
|------|----------|
| **public** | Visible to all tenants (subject to disallow lists) |
| **restricted** | Visible only to tenants in allow list |
| **private** | Visible only to specific tenants (requires allow list) |

### List Semantics

- **Tenant allow list** — Only listed tenants can see/subscribe
- **Tenant disallow list** — Listed tenants are blocked
- **Region allow list** — Package available only in listed regions
- **Region disallow list** — Package blocked in listed regions
- Region list values published by Hub Win team

### Privacy

- Tenant lists are **private** to the publisher
- Other tenants cannot see who is on allow/disallow lists
- Region lists reference publicly known region identifiers

## Alternatives Considered

### Alternative 1: Separate Private Marketplace

Create separate Marketplace instances for private sharing.

**Pros:**
- Complete isolation
- Independent management

**Cons:**
- High infrastructure overhead
- Complex cross-marketplace federation
- Duplicate storage and services

**Why rejected:** Visibility controls achieve same goals without infrastructure complexity.

### Alternative 2: Tenant-Level ACLs

Tenant admins configure which packages they can access.

**Pros:**
- Subscriber-controlled
- Centralized management

**Cons:**
- Publisher loses control
- No way to enforce exclusions
- Complex synchronization

**Why rejected:** Publishers need control over who accesses their packages.

## Consequences

### Positive

- No separate infrastructure for private sharing
- Publishers maintain full control
- Flexible allow/disallow semantics
- Regional compliance supported
- Private tenant lists protect business relationships

### Negative

- Visibility enforcement at query time (performance consideration)
- Publishers must manage lists (no delegation)
- No hierarchical/group-based controls

### Neutral

- OpenSearch indexes include visibility metadata
- Catalog services enforce visibility at query time

## Implementation Notes

- Visibility controls validated during publishing
- Region names validated against Hub Win published list
- Tenant IDs validated at query time (tenant may be added/removed)
- Catalog Services filter results based on requesting tenant

## References

- [ADR-0093: Marketplace as Platform Service](./0093-marketplace-platform-service.md)
- [Catalog Services](../04-subsystems/marketplace/catalog-services.md)
- [Publishing Services](../04-subsystems/marketplace/publishing-services.md)

