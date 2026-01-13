# 0121. Persona Twin Blueprint Structure

## Status

Accepted

## Date

2026-01-14

## Context

Collaborators in a Workbench need the ability to create personal AI agents (Persona Twins) to delegate their responsibilities. This requires a mechanism for non-developers to create agents without writing Training Specs from scratch.

### Constraints

- Must be accessible to any collaborator, not just developers
- Must reuse existing agent lifecycle infrastructure
- Must provide sensible defaults for common delegation patterns
- Must be consistent with existing blueprint patterns in Hub

### Requirements

- Provide templates for common signal configurations (task assignments, notifications, schedules)
- Include OPA filter suggestions for signal filtering
- Enable customization beyond the template
- Integrate with existing Trained Agent Blueprint system

## Decision

We will implement **Persona Twin Blueprints as extensions to Trained Agent Blueprints**, adding a `personaTwinBlueprint` field with signal suggestions and OPA filter templates.

### Key Points

- Persona Twin Blueprint is a standard `TrainingSpec` CRD with additional metadata
- Not a separate CRD type—reuses existing Training Spec infrastructure
- `personaTwinBlueprint` field contains:
  - `signalSuggestions`: Common signals with default OPA filters
  - `filterSuggestions`: Reusable OPA policies for filtering
  - `scheduleSuggestions`: Common schedule patterns for time triggers
- Blueprints are provided by Hub Platform subscription (available in all workbenches)
- Collaborators select blueprint, customize, then create Training Spec

## Alternatives Considered

### Alternative 1: Separate PersonaTwinBlueprint CRD

Create a dedicated CRD type specifically for Persona Twin Blueprints.

**Pros:**
- Type safety—clearly distinguishes from regular Training Specs
- Could have different validation rules

**Cons:**
- Duplicates Training Spec infrastructure
- Requires new operators, validators, directories
- Inconsistent with existing blueprint patterns

**Why rejected:** Unnecessary complexity. Extending Training Spec with additional metadata achieves the same goal with less overhead.

---

### Alternative 2: Wizard-Only Creation (No Blueprints)

Provide a wizard UI that guides collaborators through creating Training Specs without templates.

**Pros:**
- No new concepts
- Maximum flexibility

**Cons:**
- Slower creation experience
- No reusable patterns
- Every collaborator reinvents the wheel
- No best practices encoded

**Why rejected:** Blueprints encode proven patterns and accelerate creation. Wizard approach doesn't scale.

---

### Alternative 3: Hardcoded Signal Configurations

Build signal configurations into the UI rather than the blueprint.

**Pros:**
- Simpler blueprint structure
- UI can be updated independently

**Cons:**
- No customization of signals at blueprint level
- Different blueprints can't suggest different signals
- Less flexible for different use cases

**Why rejected:** Different use cases require different signal suggestions. Encoding in blueprints enables specialization.

## Consequences

### Positive

- Reuses existing Training Spec infrastructure
- Consistent with existing Hub blueprint patterns
- Enables non-developers to create agents
- Encodes best practices for common delegation patterns
- Extensible—new blueprints can be added without platform changes

### Negative

- Training Spec schema becomes larger with optional fields
- Need to maintain Hub-provided blueprints

### Neutral

- Blueprints are versioned like Training Specs
- Validation must handle optional `personaTwinBlueprint` field

## Implementation Notes

- Add `personaTwinBlueprint` field to Training Spec CRD schema
- Training Spec Manager validates blueprint-specific fields when present
- Trained Agent Directory indexes by `persona-twin` label
- UI provides blueprint selection wizard for collaborators

## Related Decisions

- [ADR-0102: Hub Application Blueprints](./0102-hub-application-blueprints.md) — Blueprint pattern for Hub Applications
- [ADR-0095: BlueprintSpec Transformation](./0095-blueprintspec-transformation.md) — Blueprint transformation patterns

## References

- [Persona Twin Blueprint Concept](../../olympus-seer-docs/seer-design/implementation-concepts/persona-twin-blueprint.md)
- [Persona Twins Concept](../../olympus-seer-docs/seer-design/implementation-concepts/persona-twins.md)
- [Training Spec Manager](../../olympus-seer-docs/seer-design/subsystems/trained-agent-lifecycle-manager/training-spec-manager.md)
