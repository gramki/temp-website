# DR-011: Introduce Deliberation as a Discovery Track Entity

**Status:** Accepted
**Date:** 2026-02-15

## Context

The Discovery Track's existing entities — Signal Exploration Task, Research Task, Experiment, and Prototype/Spike — all represent individual or small-team investigation and testing work. They produce outcomes through empirical methods: investigation findings, test results, prototype learnings.

However, many significant product decisions emerge from structured group discussions rather than empirical validation:

- **Product council meetings** where leadership evaluates strategic options and decides direction
- **Architecture review boards** where technical leadership assesses feasibility and approach
- **Cross-functional brainstorms** where diverse expertise generates candidate solutions
- **Customer advisory boards** where key customers provide structured input on priorities

This class of work was invisible in the model. A product council deciding to enter the LATAM market — a decision involving the CPO, CTO, VP Sales, and PM — had no trackable representation. The implicit assumption was that all product decisions must flow through empirical validation (Research → Experiment → PDR), which doesn't match practice.

## Decision

Introduce **Deliberation** as a Discovery Track entity representing collaborative, group-based activities where authorized stakeholders convene to discuss, evaluate, and decide. Deliberation produces outcomes through collective judgment rather than empirical evidence.

Key characteristics:
- **Inherently collaborative** — the only Discovery entity requiring a group
- **Spans both phases** — can be generative (brainstorming Ideas from Signals) or evaluative (deciding Go/Kill/Pivot on Ideas)
- **Produces PDRs directly** — group judgment is a legitimate decision path alongside empirical validation
- **Scoped to consequential outcomes** — routine meetings, status syncs, and ceremonies are NOT Deliberations

## Rationale

- **Reflects practice:** In real product organizations, a significant share of decisions are made through authorized group judgment, not experiments.
- **Distinct from all existing entities:** Deliberation's distinguishing characteristic is *collaborative group judgment* — not investigation (Research), not formal testing (Experiment), not building (Prototype), not divergent solo exploration (Signal Exploration).
- **First-class decision path:** When the product council deliberates and decides, the PDR records their reasoning. The evidence is the group's expertise and discussion, not empirical data. This is legitimate and common.
- **The term "Deliberation"** was chosen over alternatives:
  - "Evaluation" overlaps with what Research and Experiments already do
  - "Brainstorming" covers only the generative mode, not the evaluative mode
  - "Review" is heavily overloaded (code review, sprint review, etc.)
  - "Workshop" implies a specific facilitated format
  - "Deliberation" covers both generative and evaluative modes, implies careful consideration by an authorized group, and is precise without being academic in the UPIM context

## Consequences

### Positive
- Group decision-making work is visible, plannable, and trackable
- Product councils, architecture reviews, and advisory boards have a first-class work entity
- PDRs can now trace to deliberations as well as empirical evidence
- Complete coverage: Discovery now represents individual investigation (Research), individual exploration (Signal Exploration), formal testing (Experiment), building to learn (Prototype), AND group judgment (Deliberation)

### Negative
- One more entity type in the Discovery Track (now eight: planning + Signal Exploration + Deliberation + Research + Experiment + Prototype + Specification + Modeling)
- Risk of over-tracking: teams may be tempted to create Deliberation records for routine meetings. The "consequential outcome" criterion must be enforced.
- Boundary with planning entities (Objective Setting, Initiative Scoping, Prioritization) may occasionally blur — those are also group activities. The distinction is that planning entities produce strategic structure (Objectives, Initiatives), while Deliberation produces Ideas or PDRs.
