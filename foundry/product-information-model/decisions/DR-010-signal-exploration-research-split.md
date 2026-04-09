# DR-010: Split Research Task into Signal Exploration Task and Research Task

**Status:** Accepted
**Date:** 2026-02-15

## Context

The original "Research Task" entity was used for all investigation work in the Discovery Track — both open-ended Signal exploration (understanding a Problem/Need/Opportunity and generating Ideas) and targeted evidence gathering (validating or invalidating a specific Idea). This conflated two fundamentally different types of work:

- **Exploration** is divergent and generative — "What does this Signal mean? What are the root causes? What could we do about it?" The output is one or more Ideas (hypotheses).
- **Validation** is convergent and evidence-oriented — "Is this Idea viable? What data supports or contradicts it?" The output is evidence that informs a Go/Kill/Pivot decision.

Using a single entity obscured the critical phase transition from Signal to Idea. The exploration work — which includes substantial investigation, pattern recognition, and creative synthesis — was invisible as a distinct planned activity.

## Decision

1. Introduce **Signal Exploration Task** as a new Discovery Track entity for the divergent, open-ended work of investigating Signals and synthesizing Ideas.
2. Narrow **Research Task** to mean targeted, convergent investigation — specific data gathering, interviews, competitive analysis — to answer a known question or test a known hypothesis.

The two entities now represent distinct phases:
- **Signal Exploration Task** → Phase 1 (Signal → Idea)
- **Research Task** → Phase 2 (Idea → Evidence), with secondary use in Phase 1 when specific data is needed during exploration

## Rationale

- **Different mindsets:** Exploration requires creative synthesis; validation requires disciplined evidence gathering.
- **Different outputs:** Exploration produces Ideas; Research produces evidence.
- **Different planning:** Exploration is scoped by Signal ("explore this Pain point"); Research is scoped by question ("answer whether demand for X exceeds Y threshold").
- **Naming consistency:** Signal Exploration Task is input-anchored (processes Signals), following the UPIM pattern where Specification Task processes specifications and Modeling Task models entities.
- **Key heuristic:** If you don't yet have a hypothesis, you need Signal Exploration. If you have a hypothesis and need evidence, you need Research (or Experiment/Prototype).

## Consequences

### Positive
- The Signal → Idea transition is explicit and trackable
- Exploration work (often substantial) is plannable in sprints/iterations
- PMs can communicate "we're exploring this Signal" vs. "we're validating this Idea" — different stakeholder expectations
- Research Task gains precision — it's always about answering a specific question

### Negative
- One more entity type in the Discovery Track
- Teams must decide whether work is "exploration" or "research" — boundary may occasionally be blurry
- Existing Research Tasks in flight may need reclassification
