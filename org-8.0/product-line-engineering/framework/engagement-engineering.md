# Engagement Engineering: PLE Framing

## Purpose

**Engagement Engineering** is the PLE layer that delivers **Customer Products**. Squads are composed per Engagement to configure Product Line platforms, build extensions and integrations, and deliver the integrated solution. They do not own the core platforms; Product Line Squads do. They own the **derived product** — the Customer Product — for that Engagement.

For the complete squad model, role structure, and delivery methodology, see the [Engagement Operating Model Guide](../../engagement/README.md).

---

## Relationship to Product Line Squads

This is the core interface between PLE and Engagement Engineering:

- **Assigning people:** Squads are staffed by assigning Product Line Engineers (and others) from Product Line Squads. Duration and return are governed by the [rotation model](../processes/rotation-model.md). Product Line Squad leads reserve the right to decline or delay if platform capacity is at risk.
- **Using platforms:** Engagement Engineering configures and extends platforms; it does not fork or own platform code. Ownership of core assets stays with Product Line Squads.
- **Contributing back:** When the Engagement needs a platform capability that doesn't exist, the EA prioritizes the contribution, the squad consults Product Line Maintainers, implements per DoD and standards, and submits a PR (inner source). EA prioritizes; ELs execute; Product Line Maintainers review. See [Inner Source Guidelines](../governance/inner-source-guidelines.md).

---

## PLE-Relevant Success Metrics

These metrics measure how well Engagement Engineering leverages and contributes to the product line:

| Metric | Purpose |
|--------|---------|
| **Reuse** | Proportion of solution built from core assets and archetypes vs. net-new custom |
| **Inner source contribution** | Quality and usefulness of PRs merged back to Product Line platforms |
| **Handover quality** | Smooth transition to run team or customer; documentation and knowledge capture |

Engagement Engineering success is measured at the Engagement and Customer Product level; Product Line Squads are measured on platform health and reuse. For the full Engagement metrics (delivery velocity, customer satisfaction, assembly quality), see [Metrics and Feedback](../../engagement/metrics-and-feedback.md).

---

## References

- [Engagement Operating Model Guide](../../engagement/README.md) — Squad model, roles, lifecycle, verification
- [PLE Overview](ple-overview.md) — PLE and Engagement Operating Model relationship
- [Product Line Engineering](product-line-squads.md) — Product Line Squads and assignment
- [Solution Archetypes](solution-archetypes.md) — Archetype framework
- [Inner Source Guidelines](../governance/inner-source-guidelines.md) — PR flow, DoD, Maintainer model
- [Rotation Model](../processes/rotation-model.md) — Return guarantees
