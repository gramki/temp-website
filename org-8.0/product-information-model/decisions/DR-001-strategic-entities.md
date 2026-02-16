# DR-001: Add Strategic Entities (Objective, Initiative) to Dimension 1

**Status:** Accepted
**Date:** 2026-02-15
**Related FAQ:** Q11

---

## Context

The original UPIM Dimension 1 (Strategy) contained only Signal entities (Problem, Need, Opportunity), solution entities (Idea, PDR, PSD), and no strategic direction entities. This meant every Signal was an equal candidate for discovery at every point in time — there was no mechanism to prioritize discovery based on business strategy.

The question arose: how should strategic planning be represented in the model? Should there be a separate "Plan Track" in the Work Model, or should strategic entities live in the Definition Model?

## Decision

Add **Objective** and **Initiative** as Definition Model entities in Dimension 1 (Strategy):

- **Objective:** A strategic goal over a defined planning horizon. Answers "where are we going?"
- **Initiative:** A strategic program to advance Objectives. The prioritization vehicle that associates Signals for discovery investment.

Signals (Problem, Need, Opportunity) may exist independently before being associated with an Initiative during a planning cycle. The association is many-to-many.

## Rationale

1. **Objectives and Initiatives describe what the product strategy *is***, not work to be performed. They belong in the Definition Model alongside other "what it is" entities.
2. **Signals need a prioritization context.** Without Initiatives, there is no answer to "why is this Problem being investigated now?" or "which Signals should we focus on this quarter?"
3. **A separate "Plan Track" was rejected** because planning is not a standalone activity — it is inherent to each track. Discovery Track plans what to investigate, Build Track plans what to build, Run Track plans what to deploy, Win Track plans what to launch. Centralizing planning in a fifth track would artificially separate planning from execution.

## Consequences

- **Positive:** Strategy → Initiative → Signals {P/N/O} → Idea → PDR → PSD chain is now complete from business strategy to technical specification.
- **Positive:** Planning work is distributed across tracks, keeping it close to teams that execute.
- **Negative:** Dimension 1 is now the largest dimension with 9 entity types (Objective, Initiative, Customer Release, Problem, Need, Opportunity, Idea, PDR, PSD). May warrant sub-grouping in documentation for readability.
- **New entities required:** Objective Setting Task, Initiative Scoping Task, Prioritization Task (Track 1 planning entities).
