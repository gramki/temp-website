# DR-037: Product Intent as Hybrid Bridge Entity

**Status:** Accepted
**Date:** 2026-05-24

## Context

Earlier UPIM and ACE drafts treated the chain from Discovery to execution as:

```text
Signal -> Idea -> PDR -> PSD -> Build
```

This made the Product Specification Document carry two jobs:

1. the specification contract for engineering; and
2. the execution trigger that communicates "we intend to evolve the product."

ACE already routes Product Intent through Workspaces, but Product Intent was not modeled clearly as a UPIM entity. That created drift: some docs said Release produced Product Intent, some UI docs placed Product Intent after PSD, and some repository docs used "product intent" to refer to all strategy/specification content in PIR.

## Decision

Model **Product Intent** as a hybrid bridge entity in Dimension 1:

- **Definition-bearing:** it records committed product direction, decision provenance, strategic context, and intended outcome.
- **Work-triggering:** it starts downstream product evolution work and has lifecycle state.
- **ACE-routable:** ACE uses Product Intent as the item that moves through Product Specification, UX Design, Development, QA, Release, and Governance.

The canonical chain is:

```text
Signal -> Idea -> PDR / Product Decision -> Product Intent -> PSD(s) -> Epic(s)
```

PSD refines Product Intent. PSD does not create Product Intent.

## Rationale

Product decisions and specifications answer different questions:

- **PDR:** Why did we decide this?
- **Product Intent:** What product evolution are we committing to route through the system?
- **PSD:** How should each affected module change?

Separating these prevents PSDs from becoming overloaded as both the commitment object and the specification contract. It also aligns UPIM with ACE, where Product Intent is the object routed through Workspaces and governed on transitions.

## Consequences

- Add `dim1-product-intent.md` as the canonical Product Intent entity.
- Add Intent Purpose to distinguish Evolution from Discovery Support and other non-delivery Build intents.
- Update Dimension 1 references from `Signal -> Idea -> PDR -> PSD` to `Signal -> Idea -> PDR -> Product Intent -> PSD`.
- Update Discovery Track outputs to include Product Intent.
- Update Product Specification docs to frame PSD as refinement of Product Intent.
- Update ACE docs to distinguish Discovery-originated Product Intent from Release-renewed Product Intent.
- Update PI Console and Product Manager docs so PDR creates or updates Product Intent, and PSD refinement happens under that intent.

## Notes

One PDR may create multiple Product Intents. Product Intent maps to product decisions, not only to Initiatives; decisions may arise from Initiatives, KRAs, SLAs, Customer Promises, compliance obligations, operational targets, or Release learnings.
