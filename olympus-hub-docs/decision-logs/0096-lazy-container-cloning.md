# ADR-0096: Lazy Container Cloning

## Status

Accepted

## Date

2026-01-11

## Context

Marketplace packages contain both CRDs (specifications) and OCI containers (runtime artifacts). When a package is subscribed to, a decision is needed about when containers are cloned to the subscriber's artifact repository.

### Options

1. **Eager cloning** — Clone all containers at subscription time
2. **Lazy cloning** — Clone containers only when first used in deployment
3. **Reference-based** — Never clone; reference Marketplace containers directly

### Constraints

- Containers can be large (hundreds of MB to GB)
- Not all subscribed packages may be used immediately
- Tenant isolation requires containers in tenant's own registry
- Storage costs are a consideration

### Requirements

- Minimize subscription overhead
- Ensure runtime availability
- Maintain tenant isolation
- Optimize storage usage

## Decision

**Containers are cloned lazily — only when first used in a Scenario Deployment.** At subscription time, only CRDs (BlueprintSpecs) are made available; containers remain in Marketplace Artifact Repository until needed.

### Cloning Trigger

Containers are cloned to tenant's artifact repository when:
- A Scenario Deployment references a container for the first time
- The deployment workflow initiates the clone

### Container Update Behavior

- Containers are updated only when derived resources are updated
- Updates don't impact running pods/containers until rollout
- Subscriber controls when container updates are applied

## Alternatives Considered

### Alternative 1: Eager Cloning

Clone all containers at subscription time.

**Pros:**
- Containers immediately available
- No delay at first deployment
- Simpler deployment flow

**Cons:**
- Large storage overhead for unused containers
- Long subscription times for large packages
- Wasted bandwidth for containers never used

**Why rejected:** Storage and bandwidth overhead for potentially unused containers.

### Alternative 2: Reference-Based (No Cloning)

Reference Marketplace containers directly at runtime.

**Pros:**
- No storage duplication
- Always get latest container

**Cons:**
- Runtime dependency on Marketplace availability
- No tenant isolation
- Security concerns (external registry access)
- No version control (Marketplace changes affect runtime)

**Why rejected:** Violates tenant isolation and creates runtime dependency on Marketplace.

## Consequences

### Positive

- Minimal subscription overhead
- Storage optimized (only used containers cloned)
- Tenant isolation maintained (containers in tenant registry)
- Subscriber controls container versions

### Negative

- First deployment may have slight delay for container clone
- Deployment workflow more complex
- Must handle clone failures at deployment time

### Neutral

- Container clone is one-time per container per tenant
- Subsequent deployments use already-cloned containers

## Implementation Notes

- Subscription creates BlueprintSpecs only (no containers)
- Scenario Deployment checks for container availability
- If container not in tenant registry, clone initiated from Marketplace
- Clone includes signature verification
- Marketplace containers are signed by Marketplace private key

## References

- [Marketplace Artifact Repository](../04-subsystems/marketplace/marketplace-artifact-repository.md)
- [Subscription Services](../04-subsystems/marketplace/subscription-services.md)
- [Artifact Registry](../04-subsystems/artifact-registry/README.md)

