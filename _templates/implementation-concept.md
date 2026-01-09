# [Concept Name]

> **Category:** [Platform Foundation | Signal Architecture | Application Architecture | Request and Task | UX Architecture | Data Architecture | Configuration Model | Composite Patterns | DevOps and Lifecycle | Integration]

---

## Overview

*One paragraph explaining what this concept is and why it exists in Hub.*

---

## Ontology Context

### Relationship to Ontology

*Explain how this implementation concept relates to the theoretical ontology.*

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| *e.g., Signal* | *e.g., I/O Gateway* | *Implements signal ingress* |

### Gap This Fills

*What specific implementation need does this concept address that the ontology doesn't cover?*

---

## Definition

**[Concept Name]** is *[precise one-sentence definition]*.

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | *Where does this concept exist? (System, Tenant, Subscription, Workbench)* |
| **Lifecycle** | *How is it created, modified, deleted?* |
| **Ownership** | *Which persona owns/manages this?* |
| **Multiplicity** | *How many can exist? Cardinality?* |

---

## Rationale

### Why This Design?

*Explain the reasoning behind the design decisions for this concept.*

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| *Alternative 1* | *Reason* |
| *Alternative 2* | *Reason* |

### Related ADRs

| ADR | Decision |
|-----|----------|
| *[ADR-XXXX](../decision-logs/XXXX-*.md)* | *Brief description* |

---

## Structure

### Key Attributes

```yaml
# Conceptual structure (not necessarily exact CRD)
concept_name:
  attribute_1: type
  attribute_2: type
  nested:
    attribute_3: type
```

### States (if applicable)

| State | Description | Transitions |
|-------|-------------|-------------|
| *State 1* | *Description* | *→ State 2, State 3* |

---

## Behavior

### How It Works

*Step-by-step or flow description of how this concept operates.*

```
1. [Step 1]
2. [Step 2]
3. [Step 3]
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| *Concept A* | *→ / ← / ↔* | *How they interact* |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| *Constraint 1* | *Description* |
| *Constraint 2* | *Description* |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ *Benefit 1* | *Explanation* |
| ✅ *Benefit 2* | *Explanation* |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ *Trade-off 1* | *How it's mitigated* |
| ⚠️ *Trade-off 2* | *How it's mitigated* |

---

## Examples

### Example 1: [Scenario Name]

*Concrete example showing this concept in use.*

```yaml
# Example configuration or usage
```

### Example 2: [Scenario Name]

*Another example if helpful.*

---

## Implementation Notes

### For Developers

*Key points developers should know when working with this concept.*

### For Operators

*Key points operators should know when managing this concept.*

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| *[Related Concept 1](./related-concept-1.md)* | *How related* |
| *[Related Concept 2](./related-concept-2.md)* | *How related* |

---

## References

- [Subsystem Documentation](../04-subsystems/relevant-subsystem/README.md)
- [Related Guide](../10-guides/relevant-guide.md)
- [ADR](../decision-logs/relevant-adr.md)

