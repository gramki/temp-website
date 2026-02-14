# Win Engineering

## Purpose

**Win Engineering** is the PLE layer that delivers **Customer Solutions**. Win Engineering Teams are composed per engagement to configure domain platforms, build extensions and integrations, and deliver the integrated solution. They do not own the core platforms; Domain Teams do. They own the **derived product**—the Customer Solution—for that engagement.

---

## Win Engineering Teams

A **Win Engineering Team** is the team assembled to deliver a specific Customer Solution under an engagement. Key points:

- **Composed per engagement** — The team is formed when an engagement is scoped and staffed; it disbands or transitions when the engagement moves to steady-state operations (handover to run team or customer).
- **Duration** — A Win Engineering Team may remain on that Customer Solution for an extended period (e.g. up to ~2 years), not “weeks.” The team is still engagement-bound, not permanent.
- **Composition** — Mix of roles loaned from Domain Teams and Solution Architecture, plus other roles as needed (see [Team Composition](../processes/team-composition.md)).
- **Rotation within engagement** — Individual members may rotate (for knowledge preservation and breadth) while the team continues; the whole team does not have to disband at once.

The broader **Win** organization includes roles that are not all ephemeral (e.g. Engagement Leads, some shared functions). The **Win Engineering Team** for a given engagement is the group dedicated to that Customer Solution for its delivery phase.

---

## What Win Engineering Delivers

A **Customer Solution** is:

- One or more domain platforms (typically Olympus + Tachyon, plus others as needed) **configured** for the customer
- **Integrations** with the customer’s ecosystem (core banking, data lakes, etc.)
- **Extensions** within platform boundaries (e.g. custom business rules, adapters)
- **Customer-specific components** where necessary (documented, and where appropriate handed over or supported per contract)

Win Engineering does **not** own:

- **Studio work** — Customer-exclusive apps, portals, back-office tools (customer IP). Studio is a separate engagement type; it may consume the Customer Solution but is out of PLE scope.
- **Core platform development** — That remains with Domain Teams; Win Engineering contributes via inner source when adding capability.

---

## Relationship to Domain Teams

- **Borrowing people:** Win Engineering Teams are staffed by loaning Domain Engineers (and others) from Domain Teams. Duration and return are governed by the [rotation model](../processes/rotation-model.md).
- **Using platforms:** Win Engineering configures and extends platforms; it does not fork or own platform code. Ownership of core assets stays with Domain Teams.
- **Contributing back:** When the engagement needs a platform capability that doesn’t exist, the Win Engineering Team consults Domain Maintainers, implements per DoD and standards, and submits a PR (inner source). See [Inner Source Guidelines](../governance/inner-source-guidelines.md).

---

## Relationship to Solution Architecture

- **Solution Architects** are loaned from the Solution Architecture team to engagements. They own solution design, archetype selection/adaptation, and [variability documentation](variability-management.md).
- **Archetypes** (e.g. Credit Card Issuer, Lending) provide blueprints, cookbooks, and playbooks. Win Engineering Teams use them to guide—not rigidly dictate—how they build the Customer Solution.

---

## Engagement Lead

Each engagement has an **Engagement Lead** who owns **delivery accountability** for the Customer Solution: scope, timeline, customer liaison, team coordination. The Engagement Lead is not the Solution Architect; the SA owns architecture and variability, the Engagement Lead owns delivery. See [Engagement Lead](../roles/engagement-lead.md).

---

## Success Metrics for Win Engineering

| Metric | Purpose |
|--------|---------|
| **Delivery velocity** | Time from scoping to production (or to key milestones) |
| **Reuse** | Proportion of solution built from core assets and archetypes vs. net-new custom |
| **Inner source contribution** | Quality and usefulness of PRs merged back to domain platforms |
| **Customer satisfaction** | Feedback and outcomes for the Customer Solution |
| **Handover quality** | Smooth transition to run team or customer; documentation and knowledge capture |

Win Engineering success is measured at the engagement and Customer Solution level; Domain Teams are measured on platform health and reuse.

---

## References

- [PLE Overview](ple-overview.md)
- [Domain Engineering](domain-engineering.md)
- [Solution Archetypes](solution-archetypes.md)
- [Engagement Lifecycle](../processes/engagement-lifecycle.md)
- [Team Composition](../processes/team-composition.md)
- [Engagement Lead](../roles/engagement-lead.md)
