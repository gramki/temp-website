# ADR-0048: Physical Copy for Cross-Subscription Promotion

## Status

Accepted

## Date

2026-01-06

## Context

When promoting artifacts to a different subscription (potentially a different tenant), the container artifacts need to be made available in the target subscription's registry. A decision is needed on whether to copy artifacts or use federation/reference mechanisms.

### Constraints

- Cross-tenant promotion must respect security boundaries
- Target subscription must own its artifacts
- Source subscription changes should not affect target
- Audit trail for artifact provenance required
- Network isolation between subscriptions possible

### Requirements

- Artifact availability in target subscription
- Independence from source after promotion
- Clear ownership model
- Security boundary enforcement

## Decision

When promoting to a different subscription, containers are **physically copied** to the target subscription's registry. CRDs are also cloned to the target's Git repository.

### Copy Behavior

| Artifact Type | Cross-Subscription Behavior |
|---------------|----------------------------|
| Container images | Physical copy to target registry |
| CRDs | Clone to target Git repository |
| Credentials | NOT copied (configured per subscription) |
| Environment configs | NOT copied (configured per subscription) |

## Alternatives Considered

### Alternative 1: Registry Federation/Pull-Through

Configure target registry to pull from source.

**Pros:**
- No duplication of storage
- Faster "promotion"
- Single source of truth

**Cons:**
- Source dependency remains
- Source changes affect target
- Network connectivity required
- Security boundary blurred

**Why rejected:** Violates isolation and independence requirements.

### Alternative 2: Reference-Based (No Copy)

Store reference to source location.

**Pros:**
- Minimal storage
- Simple implementation

**Cons:**
- Source deletion breaks target
- Cross-tenant access required
- Version consistency issues

**Why rejected:** Too fragile for production use.

### Alternative 3: Hybrid (Copy with Dedup)

Copy with content-addressable deduplication.

**Pros:**
- Efficient storage
- Independence
- Faster copies

**Cons:**
- Complex implementation
- Shared storage layer required
- Dedup across tenants is problematic

**Why rejected:** Complexity not justified; physical copy is clean.

## Consequences

### Positive

- Complete isolation between subscriptions
- Target owns its artifacts
- Source changes don't affect target
- Clear audit trail with provenance
- No runtime dependencies on source

### Negative

- Storage duplication
- Promotion takes longer (copy time)
- More storage consumption

### Neutral

- Container images are immutable (copy once)
- Storage is typically cheap relative to isolation benefits

## Implementation Notes

- Container copy preserves image digest for verification
- Provenance metadata stored with copied artifacts
- Copy operation is atomic (all or nothing)

## References

- [Container Registry](../04-subsystems/artifact-registry/container-registry.md)
- [Promotion Model](../04-subsystems/artifact-registry/promotion-model.md)

