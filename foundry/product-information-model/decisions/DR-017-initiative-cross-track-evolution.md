# DR-017: Initiative Evolves to Cross-Track Coordination Construct with Lever Mix and Embedded Targets

**Status:** Accepted
**Date:** 2026-02-16

## Context

Initiative was originally defined as "a strategic program to advance one or more Objectives" — primarily a mechanism for grouping Signals for discovery investment. Its relationships pointed to Objectives (upstream), Signals (associated), and Customer Release Intents (downstream). This framing was product-centric: Initiative → Discovery → Product Intent → PSD → Build.

The Dimension 2 restructure (DR-015) and the recognition that not all Win Outcomes are advanced by product capabilities alone (DR-016) revealed that Initiatives drive work across all four tracks. A "LATAM Enterprise Market Entry" Initiative requires product development (Build Track), GTM execution (Win Track), sales enablement (Win Track), CS programs (Win Track), and potentially infrastructure provisioning (Run Track) and organizational changes (Operating Model).

## Decision

Evolve Initiative from a Discovery-focused "program of Signals" to a **cross-track coordination construct** with three new capabilities:

1. **Lever Mix** — weighted allocation of effort across levers from the Business Model's Lever Portfolio (e.g., Product 40%, GTM 25%, Sales Enablement 20%, CS 15%)
2. **Embedded Targets** — time-bound, quantitative measures of success per Win Outcome, like Key Results in an OKR (e.g., "Q3: 85% activation rate", "Q3: CAC below $25K")
3. **Cross-track work alignment** — Win Track planning, enablement, engagement, and review entities all reference the Initiative they advance

Objectives remain lever-agnostic. The lever mix is an Initiative-level concern.

## Rationale

- **Initiatives already targeted Win Outcomes** — adding lever mix and targets makes the "how" and "how much" explicit alongside the "what"
- **OKR pattern** — embedding targets follows the widely-understood OKR model (Objective → Key Results) without introducing a new entity
- **Resource allocation visibility** — a lever mix makes cross-track investment visible: "this Initiative needs 60% Win Track investment, not just engineering"
- **Eliminated Adoption Goal** — targets embedded in Initiatives rendered the standalone Adoption Goal entity redundant
- **Objectives stay clean** — lever-agnosticism at the Objective level preserves the strategy → execution separation

## Consequences

### Positive
- Initiative is the single coordination construct across all tracks
- Resource allocation across levers is explicit and plannable
- Targets are contextual (embedded in the Initiative that drives toward them)
- Win Reviews assess Initiative target progress, closing the feedback loop
- Eliminates standalone Adoption Goal entity and its naming problems

### Negative
- Initiative entity is significantly more complex
- Lever mix weights are approximate, not precise resource plans — organizations must understand they're directional guidance, not budgets
- Cross-track scope means Initiative touches more organizational boundaries, requiring broader stakeholder involvement in Initiative Scoping Tasks
