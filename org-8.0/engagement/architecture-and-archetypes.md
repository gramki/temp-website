# Architecture and Archetypes

[← Back to Guide](README.md)

---

## Archetype-Driven Assembly

Every Engagement begins with an archetype assessment. Archetypes provide reusable patterns for classes of Customer Products:

- **Blueprint** — reference architecture (what to configure)
- **Cookbook** — step-by-step implementation and operational guidance
- **Playbook** — delivery guide (phases, checkpoints, handover criteria)

See [solution-archetypes.md](../product-line-engineering/framework/solution-archetypes.md) for the full archetype framework.

---

## EA's Gap Analysis

The EA performs gap analysis at Discover and maintains it through Build:

- What capability exists in the Product Line vs. what the customer needs
- Where inner source contributions are needed
- Where custom (Engagement-specific) components are required
- Where archetype updates should be proposed

---

## Inner Source Decisions

EA maintains the inner source debt and priority view for the Engagement. ELs execute inner source contributions per EA's prioritization. Product Line Maintainers review and merge (or reject) per [Inner Source Guidelines](../product-line-engineering/governance/inner-source-guidelines.md).

---

## Variability Management

The EA documents variability — how the Engagement's configuration, extensions, and integrations differ from the archetype baseline. This documentation serves two purposes: it enables future Engagements to learn from configuration decisions, and it feeds archetype evolution.

See [variability-management.md](../product-line-engineering/framework/variability-management.md) for the variability management framework.

---

## Security in Architecture

The EA is responsible for ensuring security is addressed in the architecture — cross-component authentication, authorization boundaries, data-in-transit integrity, and compliance with the customer's regulatory environment. Security requirements flow from the EA to squads for implementation and to the AVA for verification (see [Verification and Certification](verification-and-certification.md) for security verification scenarios).

The shared security team under ERC performs VA/PT and security reviews on a periodic or on-demand basis.

---

## Product Line Version Absorption

During Build, Product Line versions evolve. The EA and AVA jointly decide the absorption strategy — how the Engagement handles PL version changes. Three patterns are available:

- **Pin and upgrade** — pin PL versions at Build start; plan explicit upgrade events with re-verification
- **Rolling absorption** — accept PL changes as they come; continuous verification catches issues
- **Windowed absorption** — accept PL changes within defined windows; verify at increment boundaries

The choice depends on architecture complexity, verification cost, and customer risk tolerance. See [Verification and Certification](verification-and-certification.md) for how the absorption strategy affects verification planning.

---

## Verification Strategy

Archetype selection influences the verification strategy: a blueprint-heavy Engagement (mostly configuration) has different verification needs than an extension-heavy one. EA and AVA jointly define the system-under-test boundary and the assembly acceptance criteria based on the architecture and archetype.

See [Verification and Certification](verification-and-certification.md) for the full verification model.

---

## Archetype Evolution

Archetypes are not static. Engagement experience drives their evolution:

- At Transfer, the EA proposes archetype updates based on what worked, what was missing, and what should be generalized
- Proposals are submitted to PAC Practice Mode for review and adoption
- Inner source contributions that prove broadly reusable may trigger new archetype patterns

This feedback loop ensures that each Engagement strengthens the archetype library for future Engagements.

---

## Mandatory Architect Consultation

Architecture-significant changes by squads require EA review before implementation. This is part of each squad's Definition of Done. EA attends relevant squad planning and review ceremonies to maintain context and provide early guidance.

See [Roles and Responsibilities](roles.md#mandatory-architect-consultation) for the full consultation mechanism (covering both EA and AVA).

---

## EA Assessment Framework

EA effectiveness is assessed on four dimensions:

| Dimension | What it measures |
|-----------|-----------------|
| **Product Line leverage** | How effectively the EA leveraged existing Product Line capability |
| **Gap anticipation** | How well the EA anticipated gaps early and planned for them |
| **Contribution back** | Quality and volume of inner source contributions and archetype updates |
| **Stakeholder effectiveness** | How effectively the EA worked with EPO, AVA, ELs, and customers |

---

## References

- [Roles and Responsibilities](roles.md) — EA role description, mandatory architect consultation
- [Solution Archetypes](../product-line-engineering/framework/solution-archetypes.md) — Archetype framework
- [Variability Management](../product-line-engineering/framework/variability-management.md) — Variability documentation practices
- [Inner Source Guidelines](../product-line-engineering/governance/inner-source-guidelines.md) — Inner source contribution process
- [Verification and Certification](verification-and-certification.md) — Verification model, system-under-test boundary, EA-AVA collaboration
- [Governance and Escalation](governance.md) — Escalation model for architectural disputes

---

[← Previous: Squad Model and Staffing](squad-model.md) | [→ Next: Verification and Certification](verification-and-certification.md)
