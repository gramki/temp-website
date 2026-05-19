# PSD Capability Templates

This directory contains **Capability Templates** — PM-facing specification guides used within a Product Specification Document (PSD).

## What Are Capability Templates?

A Capability Template guides the Product Manager in specifying a Capability within a PSD. Templates are selected **per Capability**, not per PSD — a single PSD (scoped to a Module) may contain Capabilities of different types, each specified using the appropriate template.

Three templates are available:

| Template | When to use | PM specifies |
|---|---|---|
| **Experience** | The capability's primary expression is direct human interaction (dashboards, forms, flows, mobile screens) | User persona, user journey, UX channel, interaction model, key screens, accessibility requirements |
| **Integration** | The capability is consumed programmatically (API, event stream, webhook, batch file) | Consumer persona, API intent, contract shape, SLO targets, backward compatibility |
| **Processing** | The capability is realized through background computation (event-triggered, scheduled, async) | Trigger, input data, processing intent, output/side effects, SLA, error handling |

## Authorship Model

PSDs are authored in two phases (DR-035, D8):

**Product Draft phase (PM-authored):**
- PSD header and traceability fields
- Section 1: Structural Impact — Capabilities and Features added/modified/retired
- Per-Capability specifications using these templates
- Section 9: Acceptance Criteria
- Section 10: Epic Decomposition

**Technical Review phase (Architect-authored):**
- Section 5: Technical & Architectural Impact — mapping Capabilities and Features to Systems and Components
- Sections 6, 7, 8: Ecosystem, Operational, Data impact
- The Architect is accountable for ensuring all PM-specified Capabilities are addressed in the technical plan

## Template Files

- [`psd-human-interactive.md`](psd-human-interactive.md) → **Experience Capability Template**
- [`psd-programmatic-interactive.md`](psd-programmatic-interactive.md) → **Integration Capability Template**
- [`psd-reactive-background.md`](psd-reactive-background.md) → **Processing Capability Template**

> **Note:** The legacy file names (`psd-human-interactive.md`, etc.) are preserved for continuity. The template names — Experience, Integration, Processing — are the canonical names used in PSD authoring. The Capability Template field on the Capability entity uses these three values.

## Relationship to Capability Templates (Dim 8)

The `Capability Template` field on the `dim8-capability.md` entity takes one of three values: `Experience` / `Integration` / `Processing`. This field records which template a PM used or would use to specify that Capability. It is informational and does not constrain the Architect's System mapping.

## Relationship to System/Component Archetypes (Dim 5)

Capability Templates are **decoupled from System and Component Archetypes**. A PM selecting an "Experience" template is not prescribing that an HI-style System will realize it. The Architect independently decides which Systems and Components address the Capability. This decoupling is a deliberate design decision (DR-035, D5).
