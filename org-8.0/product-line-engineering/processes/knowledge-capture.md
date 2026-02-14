# Knowledge Capture

## Purpose

Win Engineering Teams are **engagement-bound**: they form for an engagement and disband or transition when the engagement moves to steady state. To avoid losing learning when teams change, we rely on **knowledge capture**—documentation, archetype updates, people rotation, and Council-led pattern extraction. This document describes why it matters, the four mechanisms, checkpoints in the engagement lifecycle, and ownership.

---

## Why Knowledge Capture Matters

- **Teams are not permanent** — When the Win Engineering Team disbands or transitions, the people may return to Domain Teams or move to other engagements. What they learned must be captured in artifacts, not only in their heads.
- **Archetypes improve with use** — Each engagement produces feedback: what worked, what didn’t, what to reuse. That feedback must flow into archetypes (blueprints, cookbooks, playbooks) so the next engagement benefits.
- **Variability must be documented** — Solution Architects document configuration points, options, and customer usage per [Variability Management](../framework/variability-management.md). That is both governance and knowledge.
- **Council needs input** — The Platform Architecture & Practice Council does pattern extraction and best-practice development; it needs structured input from engagements (retrospectives, decision logs, archetype updates).

---

## Four Capture Mechanisms

### 1. Documentation (Engagement Retrospectives, Decision Logs)

- **Retrospective** — At the end of the engagement (or at phase boundaries), the Win Engineering Team holds a retrospective: what worked, what didn’t, what we’d do differently, what should be reused.
- **Decision log** — Significant architectural or design decisions are recorded with context, rationale, and alternatives considered. Solution Architect owns or coordinates.
- **Output** — Retrospective summary and decision log are stored in a designated place (e.g. engagement folder, wiki, repo). Council and Solution Architecture use them for pattern extraction and archetype updates.

### 2. Archetype Updates (Blueprints, Cookbooks, Playbooks)

- **Feedback into archetypes** — Solution Architect (and team) update the relevant solution archetype: blueprint, cookbook, playbook, integration patterns. Updates reflect what was learned (e.g. "add this integration pattern," "clarify this configuration option").
- **Ownership** — Solution Architecture owns archetypes; Solution Architect for the engagement proposes updates. Council may review significant changes in Practice Mode.
- **Output** — Updated archetype docs in the [archetypes](../archetypes/) directory (or equivalent). Variability documentation is updated per [Variability Management](../framework/variability-management.md).

### 3. People Rotation (Carrying Knowledge Back to Domain Teams)

- **Rotation** — When engineers rotate back to Domain Teams (or to another engagement), they carry context: what worked on the engagement, what was hard, what the platform could do better. See [Rotation Model](rotation-model.md).
- **Informal and formal** — Knowledge is shared informally (conversations, demos) and formally (e.g. short write-up or presentation to Domain Team or Council). Domain Team leads encourage sharing when people return.
- **Inner source** — Code and design contributions merged via inner source are themselves knowledge capture; the PR and review thread document the "what" and "why."

### 4. Council Reviews (Monthly Pattern Extraction)

- **Practice Mode** — Council holds monthly Practice Mode sessions: knowledge sharing, case reviews, pattern extraction. Inputs include: retrospective summaries, decision logs, archetype update proposals, and verbal sharing from recent engagements.
- **Pattern extraction** — Council identifies recurring patterns: "Multiple engagements did X; we should add it to archetype Y" or "We keep seeing Z; we need a platform or process change." Follow-up is assigned (e.g. Solution Architecture for archetype, Domain Team for platform).
- **Output** — Council notes, follow-up actions, and updated standards or archetypes. Variability governance (e.g. new configuration points) is handled in Council as needed.

---

## Knowledge Capture Checkpoints in Engagement Lifecycle

| Phase | Checkpoint | Owner | Output |
|-------|------------|-------|--------|
| **Scoping** | Architecture and gap analysis documented | Solution Architect | Solution architecture doc, variability expectations |
| **Deliver** | Significant decisions logged as they occur | Solution Architect | Decision log |
| **Transition** | Retrospective held; decision log finalized | Engagement Lead + Solution Architect | Retrospective summary, decision log |
| **Transition** | Archetype updates proposed and (where agreed) applied | Solution Architect | Updated archetype docs, variability docs |
| **Transition** | Returning engineers share with Domain Teams (or Council) | Domain Team leads | Sharing session or write-up |
| **Ongoing** | Council Practice Mode uses engagement outputs | Council | Pattern extraction, archetype/process follow-up |

---

## Ownership and Accountability

- **Engagement Lead** — Ensures retrospective and handover happen; supports Solution Architect on capture; does not own archetype content.
- **Solution Architect** — Owns decision log, variability documentation, and archetype update proposals; ensures they are completed before or during transition.
- **Domain Team leads** — Encourage and create time for returning engineers to share; consume archetype updates and Council outputs for platform improvement.
- **Council** — Runs Practice Mode; does pattern extraction; assigns follow-up; governs variability and significant archetype changes.

---

## References

- [Engagement Lifecycle](engagement-lifecycle.md) — Phase 4: Transition
- [Solution Archetypes](../framework/solution-archetypes.md) — How archetypes evolve
- [Variability Management](../framework/variability-management.md) — Variability documentation
- [Council Charter](../governance/council-charter.md) — Practice Mode and pattern extraction
- [Rotation Model](rotation-model.md) — People carrying knowledge back
