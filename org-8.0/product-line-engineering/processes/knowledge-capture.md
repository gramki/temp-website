# Knowledge Capture

## Purpose

Customer Product Squads are **Engagement-bound**: they form for an Engagement and disband or transition when the Engagement moves to steady state. To avoid losing learning when teams change, we rely on **knowledge capture**—documentation, archetype updates, people rotation, and Council-led pattern extraction. This document describes why it matters, the four mechanisms, checkpoints in the Engagement lifecycle, and ownership.

---

## Why Knowledge Capture Matters

- **Teams are not permanent** — When the Customer Product Squad disbands or transitions, the people may return to Product Line Squads or move to other Engagements. What they learned must be captured in artifacts, not only in their heads.
- **Archetypes improve with use** — Each Engagement produces feedback: what worked, what didn't, what to reuse. That feedback must flow into archetypes (blueprints, cookbooks, playbooks) so the next Engagement benefits.
- **Variability must be documented** — Engagement Architects document configuration points, options, and customer usage per [Variability Management](../framework/variability-management.md). That is both governance and knowledge.
- **Council needs input** — The Platform Architecture Council does pattern extraction and best-practice development; it needs structured input from Engagements (retrospectives, decision logs, archetype updates).

---

## Four Capture Mechanisms

### 1. Documentation (Engagement Retrospectives, Decision Logs)

- **Retrospective** — At the end of the Engagement (or at phase boundaries), the Customer Product Squad holds a retrospective: what worked, what didn't, what we'd do differently, what should be reused.
- **Decision log** — Significant architectural or design decisions are recorded with context, rationale, and alternatives considered. Engagement Architect owns or coordinates.
- **Output** — Retrospective summary and decision log are stored in a designated place (e.g. Engagement folder, wiki, repo). PAC and EA use them for pattern extraction and archetype updates.

### 2. Archetype Updates (Blueprints, Cookbooks, Playbooks)

- **Feedback into archetypes** — Engagement Architect (and team) update the relevant solution archetype: blueprint, cookbook, playbook, integration patterns. Updates reflect what was learned (e.g. "add this integration pattern," "clarify this configuration option").
- **Ownership** — EAs own archetypes; the Engagement Architect for the Engagement proposes updates. PAC may review significant changes in Practice Mode.
- **Output** — Updated archetype docs in the [archetypes](../archetypes/) directory (or equivalent). Variability documentation is updated per [Variability Management](../framework/variability-management.md).

### 3. People Rotation (Carrying Knowledge Back to Product Line Squads)

- **Rotation** — When engineers rotate back to Product Line Squads (or to another Engagement), they carry context: what worked on the Engagement, what was hard, what the platform could do better. See [Rotation Model](rotation-model.md).
- **Informal and formal** — Knowledge is shared informally (conversations, demos) and formally (e.g. short write-up or presentation to Product Line Squad or Council). Product Line Squad leads encourage sharing when people return.
- **Inner source** — Code and design contributions merged via inner source are themselves knowledge capture; the PR and review thread document the "what" and "why."

### 4. Council Reviews (Monthly Pattern Extraction)

- **Practice Mode** — Council holds monthly Practice Mode sessions: knowledge sharing, case reviews, pattern extraction. Inputs include: retrospective summaries, decision logs, archetype update proposals, and verbal sharing from recent Engagements.
- **Pattern extraction** — Council identifies recurring patterns: "Multiple Engagements did X; we should add it to archetype Y" or "We keep seeing Z; we need a platform or process change." Follow-up is assigned (e.g. EA for archetype, Product Line Squad for platform).
- **Output** — Council notes, follow-up actions, and updated standards or archetypes. Variability governance (e.g. new configuration points) is handled in Council as needed.

---

## Knowledge Capture Checkpoints in Engagement Lifecycle

| Phase | Checkpoint | Owner | Output |
|-------|------------|-------|--------|
| **Discover** | Architecture and gap analysis documented | Engagement Architect | Solution architecture doc, variability expectations |
| **Build** | Significant decisions logged as they occur | Engagement Architect | Decision log |
| **Transfer** | Retrospective held; decision log finalized | EPM + Engagement Architect | Retrospective summary, decision log |
| **Transfer** | Archetype updates proposed and (where agreed) applied | Engagement Architect | Updated archetype docs, variability docs |
| **Transfer** | AVA hands over verification module documentation (certification records, environment definitions, test data tooling) | AVA | Verification module handover artifacts |
| **Transfer** | Returning engineers share with Product Line Squads (or Council) | Product Line Squad leads | Sharing session or write-up |
| **Ongoing** | Council Practice Mode uses Engagement outputs | Council | Pattern extraction, archetype/process follow-up |

---

## Ownership and Accountability

- **EPM** — Ensures retrospective and handover happen; drives Engagement Success (adoption, value delivery); supports Engagement Architect on capture; does not own archetype content.
- **Engagement Architect** — Owns decision log, variability documentation, and archetype update proposals; ensures they are completed before or during Transfer.
- **AVA** — Owns verification knowledge capture: certification records, verification module documentation, test environment definitions. Ensures these are completed before Transfer.
- **Product Line Squad leads** — Encourage and create time for returning engineers to share; consume archetype updates and Council outputs for platform improvement.
- **Council** — Runs Practice Mode; does pattern extraction; assigns follow-up; governs variability and significant archetype changes.

---

## References

- [Engagement Operating Model Guide](../../engagement/README.md) — Complete role structure
- [Engagement Lifecycle](engagement-lifecycle.md) — Phase 4: Transfer
- [Solution Archetypes](../framework/solution-archetypes.md) — How archetypes evolve
- [Variability Management](../framework/variability-management.md) — Variability documentation
- [Council Charter](../governance/council-charter.md) — Practice Mode and pattern extraction
- [Rotation Model](rotation-model.md) — People carrying knowledge back
