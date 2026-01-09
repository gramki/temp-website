# ADR-0044: Platform-Agnostic Container Registry via Olympus Weave

## Status

Accepted

## Date

2026-01-06

## Context

Hub needs container registry infrastructure to store OCI-compliant artifacts (Hub Application containers, migration DML bundles). The platform must support enterprise-grade registry capabilities while remaining flexible for different deployment scenarios.

### Constraints

- Hub should not be tightly coupled to a specific registry provider
- Enterprise customers may have existing registry infrastructure preferences
- The solution must support subscription-level isolation
- Cross-subscription promotion requires container copying capabilities

### Requirements

- Support for OCI-compliant container storage
- Subscription-scoped snapshot and production registries
- Abstraction from underlying infrastructure details

## Decision

Hub will use **Olympus Weave** as the abstraction layer for container registry infrastructure. Hub documentation and APIs will reference abstract registry concepts without exposing specific provider details.

### Key Points

- One Workbench maps to one Weave Cluster
- Current implementations include ECR and JFrog Artifactory
- Hub abstracts provider-specific URLs and configurations
- Registry capabilities are exposed through Hub's Artifact Registry APIs

## Alternatives Considered

### Alternative 1: Direct ECR Integration

Build directly on Amazon ECR.

**Pros:**
- Simpler initial implementation
- Deep AWS integration

**Cons:**
- Locks Hub to AWS
- Limits deployment options
- Customer choice restricted

**Why rejected:** Reduces platform flexibility and enterprise adoption potential.

### Alternative 2: Multi-Provider Direct Integration

Build direct integrations with multiple registry providers.

**Pros:**
- More control over each integration
- Optimized for each provider

**Cons:**
- High maintenance burden
- Inconsistent feature parity
- Duplicated effort

**Why rejected:** Weave already provides this abstraction.

## Consequences

### Positive

- Platform flexibility across cloud providers
- Enterprise customers can use preferred infrastructure
- Single abstraction layer for all registry operations
- Leverages existing Weave capabilities

### Negative

- Dependency on Olympus Weave
- May not expose all provider-specific features
- Additional abstraction layer

### Neutral

- Hub documentation avoids provider-specific details
- Registry URLs are Hub-managed, not provider-specific

## References

- [Artifact Registry README](../04-subsystems/artifact-registry/README.md)
- [Container Registry](../04-subsystems/artifact-registry/container-registry.md)
- [Olympus Weave Documentation](https://weave.olympus.tech/getting-started/overview/)


