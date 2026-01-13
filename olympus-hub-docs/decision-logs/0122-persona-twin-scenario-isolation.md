# 0122. Persona Twin Scenario Isolation

## Status

Accepted

## Date

2026-01-14

## Context

Persona Twin Scenarios need to be distinguished from Business Scenarios in the UI and APIs. Collaborators' personal workflows should be isolated from organizational operations while still benefiting from the same infrastructure.

### Constraints

- Must use existing Scenario infrastructure
- Must support filtering in UI and APIs
- Must not require separate scenario management systems
- Must support visibility controls for privacy

### Requirements

- Clear distinction between Business and Persona Twin Scenarios
- Filter support in APIs and UI
- Visibility controls (public/private) at scenario level
- Consistent with existing scenario patterns

## Decision

We will use **metadata labels and a category field** to isolate Persona Twin Scenarios from Business Scenarios, with scenario-level visibility controls.

### Key Points

- Persona Twin Scenarios are identified by:
  - `metadata.labels.persona-twin: "true"` — metadata label
  - `metadata.category: "persona-twin"` — explicit category field
- Visibility controls:
  - `metadata.visibility: "public" | "private"` — scenario-level setting
  - Private scenarios visible only to delegator and admins
- API filter support:
  - `?category=business` or `?category=persona-twin`
  - `?visibility=public` or `?visibility=private`
  - `?delegator=user:john@acme.com`
- UI isolation:
  - Separate sections in Workbench Studio (Business Scenarios vs Persona Twins)
  - Default view includes all visible scenarios (filter support sufficient)

## Alternatives Considered

### Alternative 1: Separate Scenario Type

Create a distinct `PersonaTwinScenario` CRD type.

**Pros:**
- Type safety—clearly different from regular scenarios
- Could have different validation rules

**Cons:**
- Duplicates scenario infrastructure
- Requires new operators, triggers, request handling
- Breaks uniform scenario model

**Why rejected:** The scenario lifecycle is identical; only metadata differs. A separate type would duplicate infrastructure unnecessarily.

---

### Alternative 2: Namespace Isolation

Put Persona Twin Scenarios in separate namespaces.

**Pros:**
- Strong isolation at Kubernetes level
- Clear boundaries

**Cons:**
- Namespace proliferation (one per collaborator?)
- Complicates cross-scenario operations
- Breaks workbench-centric model

**Why rejected:** Hub uses workbench-scoped resources, not namespace-scoped. Namespace isolation would break the model.

---

### Alternative 3: Exclude from Default Lists

Make Persona Twin Scenarios invisible by default, require explicit filter to see.

**Pros:**
- Cleaner default views
- Reduces noise

**Cons:**
- Inconsistent with "filter support is sufficient" principle
- May hide scenarios users expect to see
- Complicates discovery

**Why rejected:** Filter support is sufficient. Exclusion by default is confusing and inconsistent.

## Consequences

### Positive

- Reuses existing Scenario infrastructure
- Consistent filter-based isolation pattern
- Visibility controls enable privacy
- UI can show separate sections while using same data model

### Negative

- Additional metadata fields in Scenario schema
- API clients must filter appropriately

### Neutral

- Default behavior includes all visible scenarios
- Admins can always see all scenarios (for governance)

## Implementation Notes

- Add `category` and `visibility` fields to Scenario schema
- Update Workbench Management APIs to support new filters
- Update Workbench Studio UI to show separate sections
- Visibility enforcement at API level (not just UI)

## Related Decisions

- [ADR-0098: Visibility Controls Private Marketplace](./0098-visibility-controls-private-marketplace.md) — Marketplace visibility pattern (similar approach)
- [ADR-0002: Scenario Specification Types](./0002-scenario-specification-types.md) — Scenario specification model

## References

- [Scenario Definitions](../04-subsystems/workbench-management/scenario-definitions.md)
- [Persona Twins Concept](../../olympus-seer-docs/seer-design/implementation-concepts/persona-twins.md)
