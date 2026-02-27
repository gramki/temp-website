# Engagement Lifecycle: Product Line Perspective

## Overview

The Engagement lifecycle has five phases: **Initiate → Discover → Build → Transfer → Complete**. For the full phase descriptions, activities, inputs/outputs, decision gates, and role responsibilities, see [Lifecycle](../../engagement/lifecycle.md) in the Engagement Operating Model Guide.

This document describes what **Product Line Squads, Product Line Maintainers, PPM, and PAC** do at each phase — the PLE side of the Engagement lifecycle.

---

## Per-Phase PLE Responsibilities

### Initiate

- **Product Line Squads (as needed):** Provide feasibility assessments for the proposed scope — can the platforms support the customer need? Indicate capacity constraints and inner source expectations early.

### Discover

- **ERC Portfolio Program Manager (PPM):** Consolidates staffing demand across all Engagements and presents a unified demand view to Product Line Squad leads. Prevents ad-hoc requests from individual ELs.
- **Product Line Squad Leads:** Review consolidated demand; check capacity against platform roadmap and existing commitments; commit specific engineers with documented return dates or rotation cadence. Reserve the right to decline or delay if platform capacity is at risk.
- **Rotation planning:** Return expectations (duration, return dates) are documented in the staffing plan. See [Rotation Model](rotation-model.md).

### Build

- **Product Line Maintainers:** Review inner source PRs from Engagement squads for correctness, DoD compliance, and platform standards. Approve, request changes, or accept with tech debt tagging per [Tech Debt Policy](../governance/tech-debt-policy.md).
- **Inner source timing:** EA prioritizes contributions; ELs execute; Product Line Maintainers review. The consult-before-build pattern (step 3 in [Inner Source Guidelines](../governance/inner-source-guidelines.md)) reduces rework. PR review SLAs apply.
- **Inner source decision gate:** PRs must meet DoD or be merged with tech debt tag. Maintainers do not have to accept substandard work.
- **Variability documentation:** EA documents configuration points, options, binding time, and customer usage per [Variability Management](../framework/variability-management.md). This feeds PAC's quarterly variability review.

### Transfer

- **Product Line Squads:** Accept return of assigned engineers per the rotation/return plan. Own ongoing platform maintenance for any inner source work that was merged during Build.
- **PAC:** Pattern extraction — uses Engagement retrospective summaries, decision logs, and archetype update proposals as input to Practice Mode sessions. Governs variability review.
- **Knowledge capture:** EA produces archetype updates and variability documentation finalization. Returning engineers share learnings with Product Line Squads. See [Knowledge Capture](knowledge-capture.md).
- **Tech debt follow-up:** Any inner source PRs merged with tech debt tags have remediation tickets assigned and tracked. Product Line Squads own remediation.

### Complete

- **Inner source repatriation:** Engagement-specific work that proved reusable is contributed back to Product Lines as inner source. This is the final opportunity to extract platform value from the Engagement.
- **Squad release:** Engineers return to Product Line Squads (or move to another Engagement per rotation model). Product Line Squad leads ensure returning engineers have meaningful platform work.

---

## Timeline Expectations

- **Initiate:** Typically 2–4 weeks (depends on complexity and customer alignment).
- **Discover:** Typically 1–2 weeks after scope is agreed (depends on capacity and availability).
- **Build:** Variable; may extend to ~2 years for large or complex Engagements.
- **Transfer:** Typically 2–4 weeks (handover, knowledge capture, team release).
- **Complete:** Typically 1–2 weeks (stabilization, squad release, close-out).

Exact timelines are set per Engagement; the above are guidelines.

---

## References

- [Engagement Operating Model Guide](../../engagement/README.md) — Full lifecycle, roles, and governance
- [Lifecycle](../../engagement/lifecycle.md) — Complete phase descriptions with all role responsibilities
- [Team Composition](team-composition.md) — PL capacity perspective on staffing
- [Rotation Model](rotation-model.md) — Return guarantees and rotation cadence
- [Knowledge Capture](knowledge-capture.md) — How knowledge flows back to platforms and PAC
- [Inner Source Guidelines](../governance/inner-source-guidelines.md) — PR flow, DoD, Maintainer model
- [Tech Debt Policy](../governance/tech-debt-policy.md) — Soft gate, tracking, remediation
- [Variability Management](../framework/variability-management.md) — Configuration documentation
