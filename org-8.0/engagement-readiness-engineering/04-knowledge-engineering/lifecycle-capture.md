# Lifecycle-Embedded Capture

[← Back to Knowledge Engineering](README.md) | [← Back to ERE](../README.md)

Knowledge artifacts are **required at each phase transition**, not captured post-hoc. This ensures knowledge is captured while context is fresh and before teams move on to new work.

---

## Core Principle

Traditional knowledge capture fails because it happens after the fact — when teams have moved on and context is lost. ERE embeds knowledge capture into the Engagement lifecycle:

- **Required artifacts** at each phase transition
- **AI-assisted drafting** reduces capture burden
- **Gates enforce** completion (progressively)
- **Quality standards** ensure reusability

---

## Phase Transition Requirements

| Phase Transition | Required Knowledge Artifact | Owner |
|------------------|----------------------------|-------|
| **Exploration → Initiate** | Exploration summary, qualification rationale | Exploration Lead |
| **Discover → Build** | Solution architecture, gap analysis, archetype decisions | EA |
| **Build → Transfer** | Variability documentation, inner source contributions | EA + ELs |
| **Transfer → Complete** | Retrospective, lessons learned, pattern candidates | EPM |
| **Complete (exit)** | Case study draft, reusable artifacts tagged | EPM + Knowledge Engineer |

---

## Artifact Details

### Exploration → Initiate

| Artifact | Content | Quality Criteria |
|----------|---------|------------------|
| **Exploration summary** | Customer context, problem statement, proposed approach, key decisions | Complete enough for someone unfamiliar to understand the opportunity |
| **Qualification rationale** | Why go/no-go decision was made; risk factors; assumptions | Traceable to qualification checklist; assumptions documented |

**AI Assistance:** Proposal Agent drafts summary from Exploration artifacts; human reviews.

### Discover → Build

| Artifact | Content | Quality Criteria |
|----------|---------|------------------|
| **Solution architecture** | High-level design, component choices, integration approach | Follows architecture template; reviewable by Architecture Agent |
| **Gap analysis** | Platform gaps, archetype gaps, inner source candidates | Quantified gaps; linked to Product Line backlog |
| **Archetype decisions** | Which archetype(s) apply; deviations and rationale | ADR format; traceable to archetype definitions |

**AI Assistance:** BRD Agent and Architecture Agent propose artifacts; EA validates.

### Build → Transfer

| Artifact | Content | Quality Criteria |
|----------|---------|------------------|
| **Variability documentation** | Customer-specific configurations, customizations, extensions | Indexed by component; searchable for future Engagements |
| **Inner source contributions** | PRs submitted to Product Lines with learning notes | PRs linked; learning notes capture "why" not just "what" |

**AI Assistance:** Pattern Curator Agent identifies generalization candidates; ELs document.

### Transfer → Complete

| Artifact | Content | Quality Criteria |
|----------|---------|------------------|
| **Retrospective** | What worked, what didn't, improvement recommendations | Structured format; actionable insights |
| **Lessons learned** | Key learnings tagged to archetype, domain, and technology | Tagged for discoverability; linked to patterns |
| **Pattern candidates** | Recurring solutions worthy of formal pattern status | Evaluated against pattern criteria; routed to Pattern Library |

**AI Assistance:** Retrospective Agent synthesizes from PI retrospectives; EPM reviews.

### Complete (exit)

| Artifact | Content | Quality Criteria |
|----------|---------|------------------|
| **Case study draft** | Customer narrative, differentiators, outcomes, metrics | Marketing-ready with customer approval path |
| **Reusable artifacts tagged** | Proposals, architectures, patterns marked for reuse | Quality-scored; indexed in knowledge base |

**AI Assistance:** Case Study Generator drafts from Engagement artifacts; Knowledge Engineer + customer approve.

---

## Enforcement Model

Knowledge gates follow the same progressive enforcement model as delivery gates:

| Stage | Behavior |
|-------|----------|
| **Guidance** | Tools remind; completion is optional |
| **Assistance** | Tools flag incomplete artifacts; Engagement can proceed with documented exception |
| **Mandatory Gate** | Engagement cannot proceed without knowledge artifacts complete |

**Current state:** Most knowledge gates operate at Guidance or Assistance level.

**Target state:** As tooling matures and AI assistance improves, knowledge gates become mandatory.

---

## Capture at the Source

Knowledge is captured as a byproduct of work, not as a separate activity:

| Tool | Knowledge Capture |
|------|-------------------|
| **Meeting Suite** | Transcribes decisions, extracts action items, identifies knowledge-worthy discussions |
| **BRD Author** | Prompts "What's generalizable here?" during requirements capture |
| **Governance Prep Suite** | Captures gate review outcomes and exception rationales |
| **Retrospective Synthesizer** | Aggregates learnings across PIs and Engagements |

---

## Quality Gates

Each knowledge artifact passes through quality gates before entering the knowledge base:

| Gate | Criteria |
|------|----------|
| **Completeness** | All required sections present; no placeholders |
| **Reusability score** | Evaluated for applicability beyond this Engagement |
| **Findability** | Properly tagged (archetype, domain, technology, outcome) |
| **Freshness** | Review date set; periodic refresh scheduled |

---

*See also: [Ownership](ownership.md) | [Pattern Curator Agent](pattern-curator.md) | [Gates and Checkpoints](../06-governance-enforcement/gates-checkpoints.md)*
