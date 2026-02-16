# DR-014: Three-Model Architecture (Definition, Work, Operating)

**Status:** Accepted
**Date:** 2026-02-15

## Context

The UPIM Work Model deliberately excludes coordination patterns (ceremonies, cadences) and organizational design (roles, team structures, skills, tools). During model development, the question arose: how should these excluded concerns be architecturally represented?

An initial design proposed a **four-model architecture:**

```
Organization Model    — How the org is DESIGNED (roles, teams, skills, tools)
Operating Model       — How the org COORDINATES (ceremonies, cadences, rituals)
Work Model            — What work EXISTS
Definition Model      — What the product IS
```

This required determining the dependency direction between Operating Model and Organization Model. Multiple orderings were explored:

1. **Organization above Operating:** "Design the org to support the coordination patterns" — but coordination choices (e.g., choosing Scrum) shape organizational requirements (e.g., needing a Scrum Master).
2. **Operating above Organization:** "Choose coordination first, then design the org for it" — but organizational realities (e.g., only 3 PMs available) constrain coordination options (e.g., can't run 6 parallel reviews).

Every ordering felt wrong because strict layering implies **one-way dependency**, and the relationship between coordination and organization is **bidirectional**.

## Decision

Consolidate the Operating Model and Organization Model into a **single Operating Model** with two entangled facets: **Coordination** and **Organization**. The UPIM architecture is three models, not four.

```
Operating Model       — How the org EXECUTES (Coordination + Organization)
Work Model            — What work EXISTS
Definition Model      — What the product IS
```

The Operating Model's internal structure (subdivision terminology, entity catalog) is deferred until the modeling work is done. The Definition Model has 9 Dimensions and the Work Model has 4 Tracks — the Operating Model's organizational pattern will earn its name through the same iterative process.

## Rationale

### Why not four models?

Coordination and Organization have a **symbiotic, bidirectional dependency** that defies strict layering:

| Direction | Example |
|---|---|
| Coordination → Organization | "We chose Scrum" → "We need a Scrum Master role" |
| Organization → Coordination | "We only have 3 PMs" → "We can't run 6 parallel Signal Reviews" |

Layers imply that A depends on B but B never depends on A. Since both concerns co-constrain and co-evolve, forcing them into separate layers distorts the relationship. The entanglement is a **feature**, not a problem to be solved by splitting.

### Why a single Operating Model?

In business conversation, "our operating model" naturally encompasses **both** how we're structured and how we coordinate. It was only when the model tried to split them for architectural purity that separate names and an ordering became necessary.

The single Operating Model:
- Acknowledges that coordination and organization are **co-designed** — you don't design one independently of the other
- Avoids a forced layering that doesn't reflect reality
- Uses "Operating Model" as a term that business stakeholders already understand
- Keeps the overall architecture clean: three models with clear one-way dependencies between them

### Why defer the internal structure?

The Definition Model's 9 Dimensions and the Work Model's 4 Tracks earned their names through iterative modeling work. Naming the Operating Model's subdivisions before the content exists would be premature — like naming Dimension 3 "The ROI Dimension" before discovering it's really about the full buying committee, pain, promises, and adoption barriers.

What we know today:
- The Operating Model covers Coordination and Organization
- These are entangled, not layered

What we don't yet know:
- How many entities the Operating Model contains
- Whether a third facet emerges (e.g., Governance? Learning?)
- Whether the internal structure is hierarchical, flat, or something else

## Consequences

### Positive
- Three clean layers with unambiguous one-way dependencies
- No forced ordering between things that are actually peers
- "Operating Model" is intuitive terminology for business stakeholders
- Avoids premature naming of subdivision patterns
- Follows the same principle as the rest of the UPIM: model what you understand, defer what you don't

### Negative
- "Operating Model" is a broad term — when detailed, it may need internal structure to remain navigable
- The deferred internal structure means teams cannot reference specific Operating Model entities yet
- Combining two concerns risks the Operating Model becoming a catch-all for "everything not in Definition or Work"

### Mitigations
- The scope boundary is explicitly defined: coordination + organizational design for product work execution. Not general business operations, not HR, not finance.
- The deferred structure will be resolved when the Operating Model is detailed — the same iterative process that produced Dimensions and Tracks will produce the right pattern.
