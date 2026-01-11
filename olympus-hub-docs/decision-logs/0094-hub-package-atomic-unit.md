# ADR-0094: Hub Package as Atomic Publishing Unit

## Status

Accepted

## Date

2026-01-11

## Context

When publishing artifacts to the Marketplace, a decision is needed about the atomic unit of publishing. Options include:

1. **Individual artifacts** — Publish single Scenarios, Tools, Machines, etc.
2. **Hub Package** — Publish a curated collection of related Blueprints
3. **Workbench export** — Publish entire workbench contents

### Constraints

- Artifacts often have interdependencies
- Partial installations could lead to broken deployments
- Publishers want to curate what they share
- Subscribers need complete, working solutions

### Requirements

- Ensure deployable completeness
- Support mixed artifact types
- Enable versioning and updates
- Maintain clear boundaries

## Decision

**Hub Package is the atomic unit of publishing.** A Hub Package is a self-sufficient, cohesive collection of **Blueprints** — definitions/specifications exported for distribution.

### Hub Package Contents

A package can contain Blueprints of these types:
1. **Scenario Blueprints** (includes Trained Agents)
2. **Workbench Blueprints**
3. **Machine Blueprints**
4. **Standalone Tools Blueprints**
5. **Raw Agents Blueprints**
6. **Mixed artifacts** (combination of the above)

### Key Properties

- **Self-sufficient** — Contains all required artifacts (no external dependencies on other packages)
- **Cohesive** — Related artifacts bundled together
- **Versioned** — Follows semantic versioning
- **Signed** — Publisher signature for integrity

### Blueprint Terminology

"Blueprint" distinguishes:
- **Specification** — Normative resource deployed in a workbench
- **Blueprint** — Candidate specification that can be adopted/deployed

## Alternatives Considered

### Alternative 1: Individual Artifact Publishing

Publish each artifact (Scenario, Tool, Machine) separately.

**Pros:**
- Maximum granularity
- Flexibility for subscribers
- Smaller download sizes

**Cons:**
- Complex dependency management
- Risk of incomplete installations
- Version compatibility issues between artifacts
- No clear bundling for related artifacts

**Why rejected:** Dependency management complexity and risk of broken deployments.

### Alternative 2: Workbench Export

Publish entire workbench as a unit.

**Pros:**
- Guaranteed completeness
- Simple model

**Cons:**
- Too coarse-grained
- Includes unrelated artifacts
- Large package sizes
- No curation ability

**Why rejected:** Too inflexible; publishers can't curate what they share.

### Alternative 3: Scenario as Atomic Unit

Align with Promotion Model's atomic unit (Scenario).

**Pros:**
- Consistency with Promotion Model
- Clear boundaries

**Cons:**
- Can't bundle multiple Scenarios
- Can't share Workbench templates
- Limited to Scenario-level sharing

**Why rejected:** Too restrictive; many use cases require multi-Scenario or Workbench-level sharing.

## Consequences

### Positive

- Publishers have full control over package contents
- Self-sufficient packages avoid dependency conflicts
- Clear versioning at package level
- Supports various sharing use cases (Scenario, Workbench, Tools)

### Negative

- Packages may have some redundancy (no cross-package sharing)
- Publishers must carefully curate package contents
- Larger packages than individual artifact publishing

### Neutral

- Package Manifest CRD defines contents
- Associated children automatically included

## Implementation Notes

- Package Manifest CRD created by developer in workbench
- Publishing flow automatically includes associated children
- Deep clone to Marketplace Artifact Repository
- Containers stored individually with deduplication

## References

- [Blueprints and Packages](../04-subsystems/marketplace/blueprints-and-packages.md)
- [ADR-0047: Scenario as Atomic Promotion Unit](./0047-scenario-atomic-promotion-unit.md)

