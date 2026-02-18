# DR-016: Win Track Restructure — Six Categories, Initiative-Embedded Targets, Win Review, Win Case

**Status:** Accepted
**Date:** 2026-02-16

## Context

The Win Track had minimal structure: two planning entities (GTM Planning Task, Customer Rollout Planning Task), one execution entity (Implementation/Onboarding), one measurement entity (Adoption Goal), and one observation entity (Feedback). Several gaps were identified:

1. **No enablement tracking.** Building reusable sales assets, CS playbooks, and marketing collateral was invisible.
2. **No pre-sales tracking.** POCs, demos, RFP responses — significant work advancing Acquisition — were not modeled.
3. **No reactive work tracking.** Customer queries, complaints, and escalations were invisible, yet they test Service Commitments and drive Cost-to-Serve.
4. **No structured assessment entity.** Feedback "appeared" without a traceable review event producing it.
5. **Adoption Goal naming was wrong.** "Adoption" is stage-specific; "Goal" conflicts with Objectives.
6. **Targets as standalone entities were unnatural.** Targets are attributes of the coordination construct (Initiative), not independent entities.
7. **Win Track had no connection to levers.** No way to express that a Win Outcome needs GTM work, not product work.

## Decisions

### 1. Restructure Win Track into six categories
Planning (Plan), Enablement (Equip), Engagement (Execute), Win Case (Respond), Win Review (Assess), Feedback (Learn/Artifact).

### 2. Win Planning as parent entity with 5 lever-specific subtypes
Customer Release Planning (Product lever), GTM Planning, Sales Enablement Planning, Customer Success Planning, Engagement Planning. Subsumes and broadens former GTM Planning Task and Customer Rollout Planning Task.

### 3. Win Enablement as parent entity with 3 subtypes
GTM Enablement, Sales Enablement Asset, CS Enablement. One-to-many asset/program creation.

### 4. Win Engagement as parent entity with 5 subtypes
Pre-sales Engagement (account, Acquisition), Implementation/Onboarding (account, Activation — existing, now subtype), Retention Engagement (account, Retention), Expansion Engagement (account, Revenue), Segment Engagement (segment-level, any stage — covers both pre-sale and post-sale).

### 5. Win Case for reactive work
Types: Query, Service Request, Complaint, Escalation. Customer-facing (distinct from Run Track Incident which is system-facing).

### 6. Win Review as structured assessment entity
Parallel to Deliberation in Discovery Track. Produces Feedback (qualitative) and Initiative target progress updates (quantitative).

### 7. Feedback reclassified as transitional artifact
Not a work item. Produced by Win Reviews. May be promoted to Signal or archived.

### 8. Adoption Goal deprecated — targets embedded in Initiatives
Targets are embedded in Initiatives like Key Results in OKRs. Eliminates naming problems ("Adoption" stage-specific, "Goal" conflicts with Objectives) and reflects that targets are attributes of coordination constructs.

### 9. CRM Deal/Opportunity is external
Pre-sales Engagement references CRM entities but UPIM does not model deals/pipeline.

### 10. Win Track operates in continuous flow (kanban)
Work items vary in duration and don't align to sprint boundaries. Planning is periodic but work is continuous.

## Rationale

- **Enablement vs. Engagement** captures the fundamental distinction between building the arsenal (one-to-many) and deploying it (one-to-one or one-to-segment)
- **Win Review → Feedback** parallels **Deliberation → PDR** — structured work producing traceable artifacts
- **Win Case** makes reactive work visible, connecting to Service Commitments (Dim 3) and Cost-to-Serve (Dim 2)
- **Targets in Initiatives** follows the OKR pattern and avoids creating entities that are really just fields
- **Six categories** (Plan, Equip, Execute, Respond, Assess, Learn) provide a complete, non-overlapping taxonomy of Win Track work

## Consequences

### Positive
- Complete Win Track entity landscape covering proactive and reactive work
- Clear connection between Win Track work and Dim 2 entities (Win Outcomes, Win Stakeholders, Business KPIs)
- Initiative becomes the universal coordination construct across all tracks
- Reactive work (Win Case) makes Service Commitment testing and Cost-to-Serve visible
- Win Review provides structured learning mechanism parallel to Discovery Track's Deliberation

### Negative
- Win Track now has significantly more entity types (from 5 to ~15 including subtypes)
- Initiative entity is more complex (lever mix, embedded targets)
- Organizations with simple Win Track needs may find the full taxonomy heavy — subtypes can be adopted incrementally
