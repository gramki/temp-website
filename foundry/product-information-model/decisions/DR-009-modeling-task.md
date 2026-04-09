# DR-009: Introduce Modeling Task as a Discovery Track Work Entity

**Status:** Accepted
**Date:** 2026-02-15

## Context

The Discovery Track originally produced two types of output:
1. **Idea validation** — Research Tasks, Experiments, and Prototypes validate or kill Ideas
2. **PSDs** — Specification Tasks author engineering specifications

However, discovery work frequently produces knowledge outputs that don't result in engineering specifications. When exploring a new market segment, a Product Manager must define Customer Segments (Dim 3), map Value Streams (Dim 8), document Compliance Posture (Dim 3), design Pricing Tiers (Dim 2), and define User Personas (Dim 4). This work is substantial, valuable, and distinct from PSD authoring — yet it had no representation in the Work Model.

Without an explicit work entity, this knowledge work was invisible to planning systems, untrackable, and often neglected in favor of "more tangible" PSD-oriented work.

## Decision

Introduce **Modeling Task** as a Discovery Track work entity that produces updates to Definition Model entities in any dimension (Dims 2–9).

Modeling Task sits alongside Research Task, Experiment, Prototype/Spike, and Specification Task as a co-equal Discovery Track work entity. It may be triggered by:
- A PDR (decision affecting a dimension)
- Research Task findings (discovery uncovering knowledge gaps)
- Ad-hoc product knowledge maintenance (e.g., Sales identifying a new segment)

The naming "Modeling Task" was chosen over "Definition Task" (too similar to "Specification Task") to emphasize that the work is about *modeling* the product's reality — not specifying engineering changes.

## Rationale

### Why not fold this into Specification Task?

Specification Tasks produce PSDs — engineering specifications scoped to modules. Modeling Tasks produce Definition Model updates — knowledge artifacts that may never result in engineering changes. Conflating them would either:
- Overload PSDs with non-engineering content (segment definitions, compliance posture), or
- Leave knowledge work untracked because "it doesn't produce a PSD"

### Why not fold this into Research Task?

Research Tasks are investigation actions — interviews, competitive analysis, data pulls. They produce *findings*. Modeling Tasks consume those findings and formalize them into Definition Model entities. The relationship is sequential: Research Task → findings → Modeling Task → entity update. They are different types of work with different skills, outputs, and review processes.

### Three output paths from Discovery

| Output Type | Work Entity | What's Produced | Target |
|---|---|---|---|
| Engineering changes | Specification Task | PSD(s) | Build Track (Epic → Story) |
| Knowledge/model changes | **Modeling Task** | Definition Model entity updates (Dims 2–9) | Definition Model |
| Decision records | (any Discovery work) | PDR | Decision archive; justifies PSDs and Modeling Tasks |

## Consequences

### Positive
- Knowledge work is visible, plannable, and trackable in sprint/iteration planning
- Definition Model updates are traceable to the discovery work that produced them
- PMs can justify "we're investing in understanding, not just building"
- Clean separation: Specification Task → engineering output, Modeling Task → knowledge output
- Dims 2–9 are no longer "things that exist" but "things that are actively maintained through explicit work"

### Negative
- One more work entity type in the Discovery Track (now six: Research Task, Experiment, Prototype/Spike, Specification Task, Modeling Task, plus the planning entities)
- Teams must distinguish between Specification Task and Modeling Task scope — a PSD that also introduces a new Capability would need both a Specification Task (for the PSD) and a Modeling Task (for the Capability definition in Dim 8)
- Modeling Tasks may feel "abstract" to teams accustomed to only tracking engineering work
