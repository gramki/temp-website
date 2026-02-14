# Solution Archetype Catalog

## Purpose

This directory contains **Solution Archetypes** — reusable patterns for classes of Customer Solutions. Each archetype includes a **blueprint** (reference architecture and configuration baseline), **cookbook** (how-to guides for configuration, integration, operations), **playbook** (delivery guide), integration patterns, and variability points. Win Engineering Teams use archetypes to guide derivation; archetypes are owned by Solution Architecture and evolved via Council and engagement feedback. See [Blueprint, Cookbook, Playbook: definitions and role in Win Engineering](../framework/solution-archetypes.md#blueprint-cookbook-playbook-definitions-and-role-in-win-engineering).

See [Solution Archetypes](../framework/solution-archetypes.md) for the full concept, components, ownership, and evolution.

---

## Current Archetypes

| Archetype | Description | Typical Platforms | Status |
|-----------|-------------|-------------------|--------|
| [Credit Card Issuer](credit-card-issuer/README.md) | Solutions for credit card issuance and management | Olympus, Tachyon, Neutrino (optional), Electron (optional) | Draft |
| [Commercial Cards](commercial-cards/README.md) | Solutions for commercial/expense card programs | Olympus, Tachyon, Electron, Neutrino (optional) | Draft |
| [Lending](lending/README.md) | Solutions for lending (retail, business, or both) | Olympus, Tachyon, Quark (optional), Neutrino (optional) | Draft |
| [Payments Hub](payments-hub/README.md) | Solutions for payment hub / orchestration | Olympus, Tachyon, Quark (optional) | Draft |

**Status:** Draft = under development; Active = in use; Mature = stable and widely used. Update this table as archetypes evolve.

---

## How to Use Archetypes

1. **Scoping** — Solution Architect selects or adapts an archetype for the engagement (see [Engagement Lifecycle](../processes/engagement-lifecycle.md) Phase 1).
2. **Deliver** — Win Engineering Team uses the archetype’s blueprint, cookbook, and playbook to configure platforms, build extensions, and integrate. See [Win Engineering](../framework/win-engineering.md).
3. **Variability** — Solution Architect documents configuration points, options, binding time, and customer usage per [Variability Management](../framework/variability-management.md).
4. **Feedback** — At transition, Solution Architect proposes archetype updates based on engagement learnings; Council reviews in Practice Mode.

---

## How to Propose a New Archetype

1. **Identify the pattern** — A class of solutions has repeated (e.g. 2–3 engagements with similar scope and platform mix); reuse would be high.
2. **Propose** — Solution Architecture proposes the new archetype: scope, components (blueprint, cookbook, playbook), variability points, and owner.
3. **Council review** — Council reviews in Practice or Governance Mode; approves or rejects.
4. **Create** — Solution Architecture creates the archetype folder and initial content (blueprint, cookbook, playbook, integration patterns, variability points).
5. **Catalog** — Add the archetype to this README with status "Draft"; update status as it becomes Active or Mature.

Avoid creating archetypes too early: if engagement frequency is low or the pattern is still evolving, document learnings in retrospectives and Council notes first; formalize the archetype when the pattern is clear.

---

## References

- [Solution Archetypes](../framework/solution-archetypes.md) — Concept, components, ownership, evolution
- [Variability Management](../framework/variability-management.md) — Variability points and governance
- [Council Charter](../governance/council-charter.md) — Council’s role in archetype and variability
- [Engagement Lifecycle](../processes/engagement-lifecycle.md) — How archetypes are used in engagements
