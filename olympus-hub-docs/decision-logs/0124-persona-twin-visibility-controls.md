# 0124. Persona Twin Visibility Controls

## Status

Accepted

## Date

2026-01-14

## Context

Persona Twins represent personal workflows for collaborators. Some collaborators may want their twins to be private—visible only to themselves and administrators. This requires visibility controls at the Scenario level.

### Constraints

- Must be scenario-level, not workbench-level (different twins may have different visibility)
- Must be consistent with existing visibility patterns (e.g., Marketplace)
- Must still allow admin visibility for governance
- Must integrate with existing authorization model

### Requirements

- Private visibility option for Persona Twin Scenarios
- Delegator (creator) always has access to their own twins
- Admins always have access for governance
- Other collaborators cannot see private twins
- API and UI must enforce visibility

## Decision

We will implement **scenario-level visibility controls** with `public` and `private` options, similar to Marketplace visibility patterns.

### Key Points

- `metadata.visibility: "public" | "private"` field on Scenario
- **Private visibility**:
  - Delegator (creator) can always see and manage
  - Workbench admins can always see (for governance)
  - Other collaborators cannot see
- **Public visibility**:
  - All workbench members can see
  - Standard access controls apply
- Similar to Marketplace visibility controls (ADR-0098)
- Enforcement at API level—UI reflects API visibility

## Alternatives Considered

### Alternative 1: Workbench-Level Controls

Set visibility at workbench level—all Persona Twins in a workbench have same visibility.

**Pros:**
- Simpler—one setting per workbench
- Consistent for all twins

**Cons:**
- No flexibility—can't have some private, some public
- Doesn't match per-collaborator ownership
- Over-constrains use cases

**Why rejected:** Different collaborators may have different privacy needs. Per-scenario is more flexible.

---

### Alternative 2: Role-Based Access Only

Use existing RBAC for visibility—no explicit visibility field.

**Pros:**
- Reuses existing RBAC
- No new concepts

**Cons:**
- Complex to configure per-twin visibility
- RBAC designed for action authorization, not visibility
- Overkill for simple public/private distinction

**Why rejected:** Public/private is a simpler model for this use case. RBAC is for action authorization.

---

### Alternative 3: Namespace-Based Isolation

Put private twins in separate namespaces.

**Pros:**
- Strong Kubernetes-level isolation

**Cons:**
- Breaks workbench-scoped model
- Complicates scenario management
- Namespace proliferation

**Why rejected:** Hub uses workbench-scoped resources. Namespace isolation breaks the model.

## Consequences

### Positive

- Simple public/private model
- Consistent with Marketplace visibility pattern
- Preserves admin governance visibility
- Per-scenario flexibility

### Negative

- Additional visibility check in API layer
- UI must handle visibility in display

### Neutral

- Default visibility could be either public or private (implementation choice)
- Visibility can be changed after creation

## Implementation Notes

- Add `visibility` field to Scenario metadata
- Workbench Management APIs filter by visibility based on caller
- Admins bypass visibility filters (for governance)
- Delegator always has access to own scenarios (check `delegator` field)
- UI shows visibility indicator and enforces in display

## Related Decisions

- [ADR-0098: Visibility Controls Private Marketplace](./0098-visibility-controls-private-marketplace.md) — Marketplace visibility pattern
- [ADR-0122: Persona Twin Scenario Isolation](./0122-persona-twin-scenario-isolation.md) — Scenario isolation approach

## References

- [Scenario Definitions](../04-subsystems/workbench-management/scenario-definitions.md)
- [Persona Twins Concept](../../olympus-seer-docs/seer-design/implementation-concepts/persona-twins.md)
