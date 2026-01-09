# ADR-0047: Scenario as Atomic Promotion Unit

## Status

Accepted

## Date

2026-01-06

## Context

When promoting artifacts between workbenches, a granularity decision is needed: What is the smallest unit that can be promoted? This affects developer workflow, deployment complexity, and consistency guarantees.

### Constraints

- Scenarios have multiple associated artifacts (Hub Applications, triggers, templates, migrations)
- Artifacts have interdependencies
- Partial promotions could lead to inconsistent states
- Developers want flexibility but also simplicity

### Requirements

- Clear promotion boundaries
- Consistency of deployed artifacts
- Predictable deployment behavior
- Manageable promotion workflow

## Decision

**Scenario is the atomic (smallest) unit of promotion.** All artifacts associated with a Scenario are promoted together. Partial Scenario promotion is not supported.

### What Gets Promoted with a Scenario

| Artifact Type | Included |
|---------------|----------|
| Scenario Specifications (Normative, Automation, Deployment) | ✅ |
| Hub Application container(s) | ✅ |
| Trigger definitions | ✅ |
| Notification templates | ✅ |
| Task queue configurations | ✅ |
| Tool bindings | ✅ |
| Migration CRDs | ✅ |

### Promotion Hierarchy

```
Subscription (largest)
  └── Workbench
        └── Scenario (atomic, smallest)
```

## Alternatives Considered

### Alternative 1: Individual Artifact Promotion

Allow promoting individual artifacts (just the container, just triggers).

**Pros:**
- Maximum flexibility
- Faster incremental updates

**Cons:**
- High risk of inconsistent state
- Complex dependency tracking
- Difficult rollback
- Developer confusion

**Why rejected:** Consistency risks outweigh flexibility benefits.

### Alternative 2: Workbench-Only Promotion

Only allow promoting entire workbenches.

**Pros:**
- Simplest model
- Always consistent

**Cons:**
- Too coarse-grained
- Forces unrelated changes together
- Slower iteration

**Why rejected:** Too restrictive for practical development.

### Alternative 3: Developer-Defined Bundles

Let developers define custom promotion bundles.

**Pros:**
- Flexible
- Customizable

**Cons:**
- Complex to configure
- Error-prone
- Inconsistent practices

**Why rejected:** Scenario boundary is natural and sufficient.

## Consequences

### Positive

- Predictable promotion behavior
- Guaranteed consistency within Scenario
- Simpler rollback (revert entire Scenario)
- Clear ownership boundaries

### Negative

- Cannot promote part of a Scenario
- Large Scenarios take longer to promote
- Must update entire Scenario for any change

### Neutral

- Developers must think in Scenario-sized units
- Encourages well-bounded Scenario design

## Implementation Notes

- Workbench promotion promotes all Scenarios + workbench-level resources
- Subscription promotion promotes all Workbenches + subscription-level resources

## References

- [Promotion Model](../04-subsystems/artifact-registry/promotion-model.md)


