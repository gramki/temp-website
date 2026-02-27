# Engagement Architect: PLE Responsibilities

## Purpose

The **Engagement Architect (EA)** owns architecture guidance across the entire Engagement. For the complete EA role description — authority, relationships (to EO, EPM, AVA, EPO, ELs), escalation model, and typical challenges — see [Roles](../../engagement/roles.md) in the Engagement Operating Model Guide.

This document covers what the EA does **within the PLE framework**: variability tracking, inner source prioritization, archetype ownership, relationship to Product Line Squads, and PLE-specific assessment and metrics.

---

## PLE-Specific Responsibilities

### Variability Tracking Ownership (Critical)

Engagement Architects **own** variability documentation for their Engagements. This is a **mandatory** part of the role, not optional.

- **Per Engagement** — Document which configuration points were used, which options were chosen, binding time, and how this maps to the customer/Engagement. Use the template in [Variability Management](../framework/variability-management.md).
- **Submit to Council** — Ensure variability documentation is submitted or updated so PAC can perform quarterly variability review and governance.
- **New points or options** — When an Engagement needs a configuration point or option not yet in the model, propose it to PAC; Council approves or rejects. Do not introduce undocumented variability.

### Inner Source Debt and Priority

- Maintains a view of inner source debt across the Engagement — what should be contributed back to the platform vs. kept as Engagement-specific.
- Prioritizes inner source contributions; ELs execute. See [Inner Source Guidelines](../governance/inner-source-guidelines.md).
- Escalates to PAC when a contribution raises broader platform design questions.

### Archetype Ownership

When the EA is assigned as owner of an archetype (e.g. Credit Card Issuer, Lending):

- Maintain blueprint, cookbook, playbook, integration patterns, and variability points.
- Incorporate Engagement feedback — archetype evolution is a key PLE outcome.
- Allocate time for archetype maintenance alongside Engagement work.
- Significant or structural changes may require PAC review.

---

## Relationship to Product Line Squads

- EA does not override Product Line Maintainers on platform code or Product Line Squads on platform roadmap.
- When the Engagement needs a capability that doesn't exist, EA plans the gap closure (inner source contribution or custom component).
- EA's gap analysis during Discover feeds the PPM's capacity coordination with PL Squad leads.

---

## Engagement Portfolio Limits

To avoid EAs being stretched too thin:

- **Concurrent Engagements** — No EA is assigned to more than a defined number of concurrent Engagements (e.g. 2–3). Exact cap is set by ERC and Engineering Leadership.
- **Capacity planning** — ERC manages EA capacity centrally; if no EA is available, Engagement start may be delayed or scope may be reduced.
- **Recognition** — Archetype ownership and variability documentation are part of EA performance and recognition; overload is not acceptable.

---

## EA Assessment Framework

EA effectiveness is assessed on four dimensions:

| Dimension | What It Measures |
|-----------|-----------------|
| **Product Line leverage** | How effectively the EA leveraged existing Product Line capability |
| **Gap anticipation** | How well the EA anticipated gaps early and planned for them |
| **Contribution back** | Quality and volume of inner source contributions and archetype updates |
| **Stakeholder effectiveness** | How effectively the EA worked with EPO, AVA, ELs, EPM, and customers |

---

## PLE Success Metrics

| Metric | Purpose |
|--------|---------|
| **Archetype reuse** | Solution is derived from archetype; custom work is justified and documented |
| **Variability completeness** | All configuration points and options documented; PAC has visibility; no undocumented variability |
| **Archetype evolution** | When owning an archetype: blueprint, cookbook, playbook stay current from Engagement feedback |
| **Knowledge capture** | Decision log and variability documentation complete at transition; archetype update proposals submitted |

---

## References

- [Engagement Operating Model Guide](../../engagement/README.md) — Complete EA role description, authority, relationships
- [Roles](../../engagement/roles.md) — EA role in context of all Engagement roles
- [Solution Archetypes](../framework/solution-archetypes.md) — Archetype concept and ownership
- [Variability Management](../framework/variability-management.md) — Variability documentation (critical for EA)
- [Council Charter](../governance/council-charter.md) — PAC and variability governance
- [Inner Source Guidelines](../governance/inner-source-guidelines.md) — PR flow, DoD, Maintainer model
- [Career Paths](../../engagement/career-paths.md) — EA career progression
