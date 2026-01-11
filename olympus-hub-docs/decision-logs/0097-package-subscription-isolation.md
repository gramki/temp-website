# ADR-0097: Package Subscription Isolation

## Status

Accepted

## Date

2026-01-11

## Context

When multiple packages are subscribed to within a workbench, a decision is needed about resource sharing between packages.

### Options

1. **Shared resources** — Resources from different packages can reference each other
2. **Isolated resources** — Each package-subscription is isolated; no cross-package references
3. **Explicit sharing** — Packages can declare shared resources

### Constraints

- Dependency conflicts between packages must be avoided
- Update and unsubscription should be clean
- Simple mental model for subscribers

### Requirements

- No dependency conflicts between packages
- Clean unsubscription (no orphaned references)
- Predictable behavior
- Simple resource management

## Decision

**All resources from a package are isolated to that package-subscription scope.** No shared resources between packages. Packages can only reference platform-provided resources.

### Isolation Model

```
Package A (subscribed)
  └── All derived resources from A
      └── Can reference: Platform resources
      └── Cannot reference: Resources from Package B

Package B (subscribed)
  └── All derived resources from B
      └── Can reference: Platform resources
      └── Cannot reference: Resources from Package A
```

### Platform-Provided Resources

Packages CAN reference:
- Platform Machine Definitions (e.g., core banking system connectors)
- Platform Tool Definitions (e.g., standard utilities)
- Other platform-provided resources

Packages CANNOT reference:
- Resources from other packages
- Resources from other workbenches

## Alternatives Considered

### Alternative 1: Shared Resources

Allow resources from different packages to reference each other.

**Pros:**
- Flexibility
- Reduced duplication
- Composability

**Cons:**
- Complex dependency tracking
- Update conflicts between packages
- Difficult unsubscription (cascading effects)
- Version compatibility issues

**Why rejected:** Complexity of dependency management and clean unsubscription.

### Alternative 2: Explicit Sharing Declarations

Packages declare which resources they expose for sharing.

**Pros:**
- Controlled sharing
- Publisher intent explicit

**Cons:**
- Complex model
- Still has dependency issues
- Requires coordination between publishers

**Why rejected:** Still creates cross-package dependencies with associated problems.

## Consequences

### Positive

- No dependency conflicts between packages
- Clean unsubscription (only affects single package)
- Predictable update behavior
- Simple mental model

### Negative

- Potential duplication if multiple packages need similar resources
- No composition of packages
- Larger overall footprint if packages have overlapping functionality

### Neutral

- Each package must be self-sufficient
- Publishers must include all required resources

## Implementation Notes

- Package validation ensures no cross-package references
- Derived resources scoped to package-subscription
- Platform resource references resolved at deployment time
- Unsubscription only affects single package's derived resources

## References

- [Blueprints and Packages](../04-subsystems/marketplace/blueprints-and-packages.md)
- [Subscription Services](../04-subsystems/marketplace/subscription-services.md)
- [ADR-0094: Hub Package as Atomic Publishing Unit](./0094-hub-package-atomic-unit.md)

