# Solution Archetypes

## What Is a Solution Archetype

A **Solution Archetype** is a reusable pattern for a class of Customer Products. It describes what such a solution typically looks like: which Product Line platforms are used, how they are configured and integrated, and what variability points apply. Archetypes **guide** derivation; they do not rigidly prescribe it. Customer Product Squads use archetypes to accelerate delivery and maintain consistency while allowing customer-specific adaptation.

---

## Current Archetypes

| Archetype | Description | Typical Platforms | Status |
|-----------|-------------|-------------------|--------|
| **Credit Card Issuer** | Solutions for credit card issuance and management | Olympus, Tachyon, Neutrino (optional), Electron (optional) | Draft / Active / Mature (set per org) |
| **Commercial Cards** | Solutions for commercial/expense card programs | Olympus, Tachyon, Electron, Neutrino (optional) | Draft / Active / Mature |
| **Lending** | Solutions for lending (retail, business, or both) | Olympus, Tachyon, Quark (optional), Neutrino (optional) | Draft / Active / Mature |
| **Payments Hub** | Solutions for payment hub / orchestration | Olympus, Tachyon, Quark (optional) | Draft / Active / Mature |

Status (draft, active, mature) is maintained in the [Archetype Catalog](../archetypes/README.md). New archetypes are added as engagement patterns emerge; we avoid premature formalization.

---

## Blueprint, Cookbook, Playbook: Definitions and Role in Engagement Engineering

Archetype artifacts used by Engagement Engineering (solution/product engineering) are defined as follows:

| Artifact | Definition | Role and purpose in Engagement Engineering |
|----------|------------|-------------------------------------|
| **Blueprint** | Reference architecture for the solution class: which Product Line platforms, integration points, key design decisions, and configuration baseline (what to configure). | Primary design reference when deriving a Customer Product. Customer Product Squads use the blueprint to align on scope, platform selection, and configuration approach. |
| **Cookbook** | Step-by-step or how-to guides for common tasks in deriving and operating the solution: e.g. how to configure a given capability, how to integrate with a specific system, how to troubleshoot a known scenario. | Task-oriented implementation and operational guidance. Customer Product Squads use cookbooks to perform specific configuration, integration, or operations tasks without reinventing approach. |
| **Playbook** | Delivery guide: phases, activities, checkpoints, handover criteria for the Engagement. | Guides how to run the Engagement and delivery. Used by EPM, ELs, and Customer Product Squad to align on lifecycle, milestones, and transition. |

These three artifacts (blueprint, cookbook, playbook) are the core of an archetype. Integration patterns and variability points are documented alongside them.

---

## Archetype Components

Each archetype is documented with:

| Component | Description | Owner |
|-----------|-------------|-------|
| **Blueprint** | Reference architecture: platforms, integration points, key design decisions, configuration baseline | Engagement Architects |
| **Cookbook** | How-to guides for common tasks: configuration, integration, operations, troubleshooting | Engagement Architects |
| **Playbook** | Delivery guide: phases, activities, checkpoints, handover criteria | Engagement Architects |
| **Integration Patterns** | Standard integration patterns (e.g. core banking, data lakes) and how they apply | Engagement Architects + Product Line Squads |
| **Variability Points** | Configuration points, options, binding time; linked to [Variability Management](variability-management.md) | Engagement Architects; governed by Council |

Archetypes live in the [archetypes](../archetypes/) directory (or equivalent); each archetype has a folder (e.g. `credit-card-issuer/`) with these components.

---

## Archetype Ownership

**Engagement Architects** (assigned to Engagements by ERC) own archetypes:

- **Engagement Architects** maintain archetypes (blueprint, cookbook, playbook, integration patterns)
- **Archetype owner** may be assigned per archetype (e.g. one EA per archetype) for continuity
- **Council** reviews archetypes (e.g. in Practice Mode) and governs variability; Council does not own day-to-day archetype content

Product Line Squads contribute when archetype changes affect platform capabilities or configuration; Engagement Architects coordinate.

---

## How Archetypes Evolve

- **Engagement feedback** — Customer Product Squads and ELs feed back what worked and what didn’t; Engagement Architects update archetypes
- **Council reviews** — Council (Practice Mode) reviews pattern extraction and archetype updates; approves significant changes or new variability
- **Variability governance** — New configuration points or options that affect an archetype are documented and governed per [Variability Management](variability-management.md)
- **Deprecation** — If an archetype (or part of it) is no longer used or is superseded, Council can deprecate with migration guidance

Archetypes are living artifacts; they improve as more engagements use them and as Council and Engagement Architects incorporate learnings.

---

## When to Create a New Archetype

Create a new archetype when:

- A class of solutions repeats (e.g. 2–3 engagements with similar scope and platform mix)
- Reuse would be high: blueprint, cookbook, and playbook would accelerate delivery
- The pattern is stable enough to document (not one-off or highly experimental)

Avoid creating archetypes too early: if engagement frequency is low or the pattern is still evolving, document learnings in retrospectives and Council notes first; formalize the archetype when the pattern is clear.

Process: Engagement Architects propose the new archetype (scope, components, variability); Council reviews and approves; archetype is added to the catalog and folder structure.

---

## References

- [Engagement Engineering](engagement-engineering.md) — How Customer Product Squads use archetypes
- [Variability Management](variability-management.md) — Variability points and governance
- [Council Charter](../governance/council-charter.md) — Council’s role in archetype and variability
- [Archetype Catalog](../archetypes/README.md) — List of archetypes and how to use them
