# UPIM Entity Catalog

This folder contains **one file per entity** defined in the Unified Product Information Model (UPIM). Each file is the canonical, detailed description of that entity — its definition, purpose, fields, statuses, and relationships.

---

## Directory Structure

```
entities/
├── README.md                  ← This file
├── definition-model/          ← Entities from the 9 Dimensions (what the product IS)
│   ├── dim1-portfolio.md             ← Thin reference entity (not owned by UPIM)
│   ├── dim1-strategic-theme.md        ← Portfolio or Product scope; persistent cross-horizon direction
│   ├── dim1-objective.md              ← Now references Theme + External Constraints
│   ├── dim1-initiative.md             ← Now has External Constraints
│   ├── dim1-customer-release.md
│   ├── dim1-problem.md
│   ├── dim1-need.md
│   ├── dim1-opportunity.md
│   ├── dim1-idea.md
│   ├── dim1-pdr.md
│   ├── dim1-psd.md
│   ├── dim2-business-model.md
│   ├── ...
│   ├── dim3-customer-segment.md
│   ├── dim3-buying-persona.md         ← Roles: Economic, Technical, User, Coach/Champion
│   ├── dim3-business-outcome.md
│   ├── dim3-pain.md                   ← Endured by User Persona (Dim 4), cared about by Buying Persona
│   ├── dim3-customer-promise.md       ← Subtypes: Value Proposition, Service Commitment, Compliance Posture
│   ├── dim3-customer-value-metric.md  ← Subtypes: ROI, Service Level, Compliance
│   ├── dim3-adoption-barrier.md       ← 8 types; may challenge Customer Promises
│   ├── ...
│   ├── dim8-value-stream.md           ← Horizontal composition across modules
│   ├── ...
│   └── psd-templates/
│       ├── README.md
│       ├── psd-human-interactive.md
│       ├── psd-programmatic-interactive.md
│       └── psd-reactive-background.md
└── work-model/                ← Entities from the 4 Tracks (how the product MOVES)
    ├── track1-objective-setting-task.md
    ├── track1-initiative-scoping-task.md
    ├── track1-prioritization-task.md
    ├── track1-signal-exploration-task.md ← Divergent: Signal → Idea(s)
    ├── track1-deliberation.md          ← Collaborative group judgment (Ideas or PDRs)
    ├── track1-research-task.md         ← Convergent: targeted evidence gathering
    ├── track1-experiment.md
    ├── track1-prototype-spike.md
    ├── track1-specification-task.md
    ├── track1-modeling-task.md         ← Produces Definition Model updates (Dims 2–9)
    ├── track2-release-planning-task.md
    ├── track2-milestone-planning-task.md
    ├── track2-iteration-planning-task.md
    ├── track2-epic.md
    ├── track2-user-story.md
    ├── track2-technical-task.md
    ├── track2-bug.md
    ├── track2-module-version.md       ← Build Track output
    ├── track2-product-version.md      ← Build Track output
    ├── track3-deployment-planning-task.md
    ├── track3-capacity-planning-task.md
    ├── track3-deployment.md
    ├── track3-incident.md
    ├── track3-change-request.md
    ├── track3-maintenance-task.md
    ├── track4-gtm-planning-task.md
    ├── track4-customer-rollout-planning-task.md
    ├── track4-implementation-onboarding.md
    ├── track4-adoption-goal.md
    └── track4-feedback.md
```

## Naming Convention

Each file is named: `<prefix>-<entity-name>.md`

- **Definition Model prefix:** `dim<N>-` where N is the dimension number (1–9).
- **Work Model prefix:** `track<N>-` where N is the track number (1–4).
- **Entity name:** Lowercase kebab-case (e.g., `research-task`, `payload-schema`).

## File Template

Every entity file follows this structure:

```markdown
# Entity Name

**Model:** Definition Model | Work Model
**Dimension / Track:** Dimension N: Name | Track N: Name
**Owner:** Role(s) responsible for this entity

## Definition

One-paragraph canonical definition.

## Purpose

Why this entity exists in the model — what gap it fills, what it enables.

## Fields

| Field | Type | Description |
|---|---|---|
| ... | ... | ... |

## Statuses (if applicable)

| Status | Description |
|---|---|
| ... | ... |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Upstream | ... | ... |
| Downstream | ... | ... |

## Example

A concrete example using the reference product (B2B Core Payment Gateway — Cross-Border Payouts).
```

## Maintenance Guidelines

1. **One entity, one file.** Never combine multiple entities into a single file.
2. **Refine incrementally.** Fields and statuses are discovered through discussion. Mark undiscovered sections with `_To be refined._` rather than guessing.
3. **Keep definitions authoritative.** The entity files in this folder are the source of truth. The summary documents (`draft-definition-model.md`, `draft-work-model.md`) should stay consistent with these files but contain less detail.
4. **Capture rationale.** When a design decision affects an entity (e.g., "Customer Release was added to decouple business delivery from artifact versioning"), note it briefly in the Purpose section and reference the relevant FAQ in `draft-modeling-faqs.md`.
5. **Cross-reference, don't duplicate.** Use the Relationships table to link entities. Don't copy another entity's definition into this file.
6. **Track discussions.** When a discussion refines an entity's fields or statuses, update the entity file immediately. The FAQ document captures the *why*; the entity file captures the *what*.

---
