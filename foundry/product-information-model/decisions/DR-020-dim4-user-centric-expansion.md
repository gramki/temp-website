# DR-020: User Experience Expansion — JTBD, UX Channel, and Touchpoint Deprecation

**Status:** Accepted
**Date:** 2026-02-15

## Context

User Experience (User-Centric) was the thinnest dimension in the UPIM — three stub entities (User Persona, User Journey, Touchpoint) with `_To be refined._` fields. The dimension lacked:
- A structural link between what users need (intent) and what the product provides (Structural)
- A model for how users access the product (channels with modality and service model characteristics)
- Clear guidance on what is Definition Model-level vs. work artifact-level granularity
- Cross-dimensional connections to Customer Value (buyer justification) and Structural (product structure)

The Discovery process produces User Experience entities — they are hypothesized, validated, and formalized through Research Tasks, Deliberations, Prototypes, and Modeling Tasks.

## Decision

### D1: Introduce Job (JTBD) as a standalone entity

Job captures the user-level "job to be done" — what the User Persona needs to accomplish. Standalone (not a field on Persona) because: Jobs are reusable across Personas, Jobs bridge User Experience → Structural → Customer Value, and Jobs give User Journeys their structural purpose.

### D2: Introduce UX Channel as a typed entity

UX Channel is the access mechanism, typed by two orthogonal axes:
- **Interaction Modality** (by technology): Web, Mobile, Chat, Voice, Email, CLI
- **Engagement Mode** (by service model): Self-serve, Assisted, Managed

Each UX Channel is implemented by exactly one Human-Interactive Module (Structural). Channel investment is a PDR-level decision.

### D3: Deprecate Touchpoint from the Definition Model

Touchpoints (specific UI elements) are implementation-level artifacts that change with every sprint. They belong in Build Track work artifacts (PSDs, prototypes, design specifications). The Definition Model captures down to User Journey; screen-level detail lives in work artifacts.

### D4: Expand User Persona with JTBD linkage

User Persona gains: Jobs (JTBD), Technical Proficiency, Frequency of Use, Customer Segment scoping, and explicit Pain (Customer Value) relationship.

### D5: Expand User Journey with cross-channel references

User Journey gains: Job reference (what it accomplishes), Channel reference (where it's experienced), Value Stream traversal (how it maps to product structure), Journey Equivalence (same Job, different Channel), and Journey Continuity (sequential handoff across Channels).

### D6: Establish Job → Structural dual mapping

Job → Value Stream is the primary structural mapping (end-to-end flow). Job → Capability is a direct mapping for simpler, capability-scoped jobs. Both are many-to-many. A Value Stream may serve multiple Jobs across different Personas.

### D7: Experience attributes as guidance, not structured fields

Features within Human-Interactive Modules are encouraged to specify experience attributes (simplicity, ease, delight, control, speed, discoverability, error tolerance) as guidance in the HI Module feature template. Not mandatory structured fields — lightweight hints that seed experiential thinking.

## Rationale

- **Job as bridge entity** resolves the structural gap between "what users need" (User Experience) and "what the product can do" (Structural), while connecting to "why the buyer pays" (Customer Value).
- **UX Channel with two axes** provides a complete, orthogonal classification. The Modality axis captures technology constraints; the Engagement Mode axis captures service model. Their intersection produces distinct UX and HI Module requirements.
- **Touchpoint deprecation** keeps the Definition Model at a sustainable granularity level. The model captures structural truth that persists across releases; UI elements don't qualify.
- **Cross-channel journey references** solve multi-channel continuity without complex flow modeling. Two simple reference types (equivalence, continuity) are sufficient.

## Consequences

**Positive:**
- User Experience now has cross-dimensional links to Customer Value (Persona → Pain, Job → Business Outcome), Structural (Job → Value Stream/Capability, Channel → HI Module), and Strategy (Channel → PDR)
- User research findings have structured entities to populate — Jobs, Personas, Journeys
- Channel portfolio decisions are governed entities with lifecycle
- The entity count is manageable: 4 entities (Persona, Job, Channel, Journey) vs. the original 3 stubs

**Negative:**
- Job is a new entity concept that teams may initially conflate with User Story (Build Track) or Business Outcome (Customer Value) — clear documentation distinguishes them
- UX Channel creates a naming overlap with marketing "channels" — the UPIM term is specifically about product access mechanisms
- Touchpoint deprecation means existing references to Touchpoints in PSDs or design docs need to be understood as work artifacts, not Definition Model entities

**Migration:**
- `dim4-touchpoint.md` is deprecated with a notice pointing to the Work Execution Framework
- Existing PSD templates that reference "Touchpoints" continue to work — Touchpoints are valid work artifacts, just not Definition Model entities
