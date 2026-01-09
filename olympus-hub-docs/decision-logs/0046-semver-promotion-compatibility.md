# ADR-0046: Semantic Version Compatibility for Promotion

## Status

Accepted

## Date

2026-01-06

## Context

When promoting Scenarios between workbenches, the target workbench must be compatible with the promoted artifacts. A mechanism is needed to validate compatibility and prevent breaking changes from being deployed to incompatible targets.

### Constraints

- Workbench Specifications evolve over time
- Scenarios depend on roles, task types, and other workbench-level constructs
- Promotion should be blocked if breaking changes would occur
- Manual override should not be trivially available

### Requirements

- Clear compatibility rules
- Automated validation during promotion
- Meaningful error messages for incompatibility
- Support for incremental specification evolution

## Decision

Promotion compatibility will be validated using **semantic versioning rules** applied to Workbench Specifications. Target workbenches must have a compatible specification version.

### Compatibility Rules

| Source Version | Target Version | Compatible? |
|----------------|----------------|-------------|
| 1.2.3 | 1.2.3 | ✅ Same version |
| 1.2.3 | 1.2.0 | ✅ Same MAJOR.MINOR |
| 1.2.3 | 1.0.0 | ⚠️ Same MAJOR (may work) |
| 1.2.3 | 2.0.0 | ❌ Breaking change |

### Breaking Changes (Block Promotion)

- Different MAJOR version
- Removed roles referenced by Scenario
- Removed task types used by Scenario
- Incompatible Hub Environment changes

## Alternatives Considered

### Alternative 1: No Compatibility Checking

Allow any promotion, trust developers.

**Pros:**
- Maximum flexibility
- Simpler implementation

**Cons:**
- Runtime failures in target
- Difficult troubleshooting
- No guardrails

**Why rejected:** High risk of production issues.

### Alternative 2: Exact Version Match

Require identical Workbench Specification versions.

**Pros:**
- Maximum safety
- Simple rule

**Cons:**
- Too restrictive
- Blocks valid promotions
- Forces lockstep updates

**Why rejected:** Overly restrictive for practical use.

### Alternative 3: Schema Diff Analysis

Deep analysis of actual schema differences.

**Pros:**
- Most accurate compatibility check
- Allows non-breaking changes across versions

**Cons:**
- Complex implementation
- Performance overhead
- Edge cases difficult to handle

**Why rejected:** Semver provides good balance; schema diff may be added later.

## Consequences

### Positive

- Clear, well-understood compatibility model
- Automated validation prevents broken deployments
- Encourages proper versioning practices
- Enables incremental evolution

### Negative

- Requires discipline in version management
- May block valid promotions in edge cases
- MAJOR version bumps require coordination

### Neutral

- Follows industry-standard semver conventions
- Target workbenches must track their specification version

## References

- [Promotion Model](../04-subsystems/artifact-registry/promotion-model.md)
- [Dev-Lifecycle-Stages](../04-subsystems/artifact-registry/dev-lifecycle-stages.md)


