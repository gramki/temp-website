---
name: Role Doc Restructure
overview: Restructure all 11 role coaching documents from the current 4-section format to the new 8-section format (Empowerment, Assignment, Ambition, Commitments, Collaboration, Management, Accountability, Objectives in Perspective), with SLA-based Commitments covering Quality/Predictability/Velocity/Fitment/Cost dimensions and contractual connection, and a retained Further Learning section.
todos:
  - id: template
    content: Update ROLE-TEMPLATE.md with new 8-section structure (Empowerment, Assignment, Ambition, Commitments, Collaboration, Management, Accountability, Objectives in Perspective) plus Further Learning
    status: completed
  - id: client-partner
    content: Restructure client-partner.md — Empowerment (client-facing decisions, cannot override AVA), Assignment (ERC assigns, per-client scope), Ambition (first 90 days + what great looks like), Commitments (Fitment, Cost, Predictability — Tier 1 contractual), Collaboration (EO, CPA, EPM, AM tensions), Management (AM functional axis), Accountability (ERC escalation, CP↔EO disputes), Objectives in Perspective, Further Learning
    status: completed
  - id: cpa
    content: Restructure cpa.md — Empowerment (governance prep, stakeholder tracking, commercial tracking), Assignment (ERC ensures CPA with CP, per-client scope), Ambition (first 90 days + progression toward CP), Commitments (Predictability, Cost — Tier 3 roll-up), Collaboration (CP, EPMs, ERC tensions), Management (CP execution axis, AM or Program functional), Accountability (escalation through CP), Objectives in Perspective, Further Learning
    status: completed
  - id: eo
    content: Restructure engagement-owner.md — Empowerment (final Engagement escalation, may override AVA as governance event), Assignment (ERC assigns, per-Engagement, heritage matching), Ambition (first 90 days + what great looks like), Commitments (all 5 dimensions — Tier 1 contractual), Collaboration (CP, EPM, EA, AVA, ERC tensions), Management (functional axis varies by heritage), Accountability (ERC escalation, governance events), Objectives in Perspective, Further Learning
    status: completed
  - id: epm
    content: Restructure epm.md — Empowerment (customer-facing delivery communication, commercial alignment, first cross-role escalation point), Assignment (ERC assigns, per-Engagement), Ambition (first 90 days + what great looks like), Commitments (Predictability, Velocity, Cost — Tier 1 contractual), Collaboration (EO, CP, EA, AVA, ELs, EPO, SRE, Scrum Masters, AM tensions), Management (Delivery functional axis), Accountability (escalation model, mediation role), Objectives in Perspective, Further Learning
    status: completed
  - id: ea
    content: Restructure ea.md — retain Architecture vs Technical Architecture preamble. Empowerment (engineering quality standards, mandatory review, inner source priority, architecture decisions), Assignment (ERC assigns, per-Engagement, from Architecture or Engineering function), Ambition (first 90 days + what great looks like), Commitments (Quality, Fitment, Cost — Tier 2 mechanism), Collaboration (AVA, ELs, EPM, PL Maintainers, EPO tensions), Management (Architecture or Engineering functional axis), Accountability (PAC escalation, inner source accountability), Objectives in Perspective, Further Learning
    status: completed
  - id: ava
    content: Restructure ava.md — retain AVA Leads Verification Squad preamble. Empowerment (release-block authority, certification, Verification Squad direction), Assignment (ERC assigns, per-Engagement, from Architecture or Engineering), Ambition (first 90 days + what great looks like), Commitments (Quality, Fitment — Tier 2 mechanism), Collaboration (EA, EPM, ELs, SRE Lead tensions), Management (Architecture or Engineering functional axis), Accountability (governance events when EO overrides, certification accountability), Objectives in Perspective, Further Learning
    status: completed
  - id: epo
    content: Restructure epo.md — Empowerment (requirements authority, customer discovery, training/enablement), Assignment (EO assigns at Stage 2, per-Engagement), Ambition (first 90 days + what great looks like), Commitments (Fitment, Velocity — Tier 3 roll-up), Collaboration (EA, Squad PMs, EPM, CP tensions), Management (Product functional axis), Accountability (escalation through EPM), Objectives in Perspective, Further Learning
    status: completed
  - id: sre-lead
    content: Restructure sre-lead.md — Empowerment (operational readiness sign-off, release mechanics authority), Assignment (EO assigns at Stage 2, per-Engagement, from SRE/Ops), Ambition (first 90 days + what great looks like), Commitments (Quality, Predictability, Fitment — Tier 2 mechanism), Collaboration (AVA, EA, EPM, ELs tensions), Management (SRE/Ops functional axis), Accountability (operational readiness accountability, go-live readiness), Objectives in Perspective, Further Learning
    status: completed
  - id: el
    content: Restructure engineering-lead.md — Empowerment (squad delivery decisions, technical decisions within squad), Assignment (EO assigns at Stage 2, per-squad), Ambition (first 90 days + what great looks like), Commitments (Quality, Predictability, Velocity — Tier 3 roll-up), Collaboration (EPM, EA, AVA, Squad PM, Scrum Master tensions), Management (Engineering functional axis), Accountability (EL prevails over EPM, escalation through EA/EO), Objectives in Perspective, Further Learning
    status: completed
  - id: squad-pm
    content: Restructure squad-pm.md — Empowerment (backlog ownership, prioritisation within squad), Assignment (EO assigns at Stage 2, per-squad), Ambition (first 90 days + what great looks like), Commitments (Predictability, Velocity, Fitment — Tier 3 roll-up), Collaboration (EPO, EL, Scrum Master, EA/AVA tensions), Management (Product functional axis), Accountability (escalation through EL/EPM), Objectives in Perspective, Further Learning
    status: completed
  - id: scrum-master
    content: Restructure scrum-master.md — Empowerment (process facilitation, ceremony ownership, impediment escalation), Assignment (PPM staffs at Stage 3, 1-3 squads), Ambition (first 90 days + what great looks like), Commitments (Predictability, Velocity — Tier 3 roll-up), Collaboration (EL, Squad PM, EPM, multi-squad tensions), Management (Program/Delivery functional axis), Accountability (escalation through EPM), Objectives in Perspective, Further Learning
    status: completed
  - id: readme-update
    content: Update career-guides/README.md to reflect the new 8-section structure in the Guide Contents and Role Coaching descriptions
    status: completed
isProject: false
---

# Role Coaching Document Restructure

## Current State

All 11 role coaching documents in `[org-8.0/engagement/career-guides/roles/](org-8.0/engagement/career-guides/roles/)` follow a 4-section structure:

1. **Success in the Role** (First 90 Days, What Good Looks Like, Key Relationships, Performance Input)
2. **Expected Interactions, Tensions, and How to Navigate**
3. **Escalation: Dos and Don'ts**
4. **Further Learning** (Internal + External references)

## Target State

Each document will be restructured into **an Introduction plus 8 sections plus Further Learning**:

**Introduction** — Brief, self-contained role description (3-5 lines) covering: Purpose (one sentence), Scope (per-client / per-Engagement / per-squad), Position in the execution-axis hierarchy, Functional track. Drawn from `[roles.md](org-8.0/engagement/roles.md)`. Appears immediately after the header and nav links. Makes the document nearly self-sufficient — a reader should not need to leave the doc to understand what the role is. For EA and AVA, their conceptual preambles ("Architecture vs. Technical Architecture" and "The AVA Leads the Verification Squad") follow the Introduction, before section 1.

1. **Empowerment** — What authority this role carries, what decisions it can make, what mechanisms it owns.
2. **Assignment** — How the role is assigned (ERC / EO / PPM), at which formation stage, scope (per-client / per-Engagement / per-squad).
3. **Ambition** — What "great" looks like. Career trajectory. First 90 days entry point. The aspiration, not just the baseline.
4. **Commitments** — SLA-based delivery commitments across applicable dimensions (Quality, Predictability, Velocity, Fitment, Cost). Contractual connection tiered by role (Direct / Mechanism / Roll-up). Connects to the [accountability framework](org-8.0/people-and-culture/accountability.md).
5. **Collaboration** — Key relationships table + interaction tensions with navigation guidance. Consolidated from current sections 1 and 2.
6. **Management** — Dual-axis reporting. Who the role reports to on each axis. How performance input flows. What to document and when to request feedback.
7. **Accountability** — Escalation model. Dos and Don'ts. What happens when commitments are missed. Governance events. References the [accountability framework](org-8.0/people-and-culture/accountability.md) distinction between outcome-based and commitment-based accountability.
8. **Objectives in Perspective** — How this role's objectives fit within the broader Engagement, client, and organisational context. What the role should care about beyond its immediate scope.

**Further Learning** — Retained as a closing section with internal and external references. All existing curated links preserved.

**Role-specific preambles** — EA retains "Architecture vs. Technical Architecture"; AVA retains "The AVA Leads the Verification Squad." These appear after the Introduction and before section 1.

## Commitments Dimension Mapping

Each role's Commitments section covers only the dimensions it is directly accountable for:

- **EO:** Quality, Predictability, Velocity, Fitment, Cost (all five). Tier 1 — direct contractual.
- **Client Partner:** Fitment, Cost, Predictability. Tier 1 — direct contractual.
- **EPM:** Predictability, Velocity, Cost. Tier 1 — direct contractual (delivery-commercial sync, Engagement Success).
- **EA:** Quality, Fitment, Cost. Tier 2 — contractual mechanism (architecture determines scope).
- **AVA:** Quality, Fitment. Tier 2 — contractual mechanism (certification as evidence).
- **SRE Lead:** Quality, Predictability, Fitment. Tier 2 — contractual mechanism (operational readiness as precondition).
- **EPO:** Fitment, Velocity. Tier 3 — roll-up (requirements reflect contract scope).
- **EL:** Quality, Predictability, Velocity. Tier 3 — roll-up.
- **Squad PM:** Predictability, Velocity, Fitment. Tier 3 — roll-up.
- **Scrum Master:** Predictability, Velocity. Tier 3 — roll-up.
- **CPA:** Predictability, Cost. Tier 3 — roll-up (commercial alignment tracking).

## Content Migration

Existing content migrates as follows (no content is lost):


| Current section                 | Target section(s)                                                         |
| ------------------------------- | ------------------------------------------------------------------------- |
| First 90 Days                   | **Ambition** (entry point) + **Assignment** (formation context)           |
| What Good Looks Like            | **Ambition** (elevated) + **Commitments** (measurable SLAs)               |
| Key Relationships table         | **Collaboration**                                                         |
| Performance Input and Dual Axis | **Management**                                                            |
| Expected Interactions, Tensions | **Collaboration** (tensions and navigation)                               |
| Escalation: Dos and Don'ts      | **Accountability**                                                        |
| Further Learning                | **Further Learning** (unchanged)                                          |
| Authority (from roles.md)       | **Empowerment** (new, drawn from [roles.md](org-8.0/engagement/roles.md)) |


**New content to write per role:**

- **Introduction:** Synthesised from `roles.md` purpose, scope, position, and function.
- **Empowerment:** Synthesised from `roles.md` authority definitions and existing coaching content.
- **Commitments:** New section — SLAs per dimension with contractual connection.
- **Objectives in Perspective:** New section — broader context for the role's purpose.
- **Assignment:** Partially new — drawn from `engagement-formation.md` and `roles.md`.

## Execution Order

1. Update `[ROLE-TEMPLATE.md](org-8.0/engagement/career-guides/ROLE-TEMPLATE.md)` with the new 8-section structure.
2. Restructure each role document (order follows the execution-axis hierarchy):
  - Client Partner
  - CPA
  - EO
  - EPM
  - EA
  - AVA
  - EPO
  - SRE Lead
  - EL
  - Squad PM
  - Scrum Master
3. Update `[career-guides/README.md](org-8.0/engagement/career-guides/README.md)` to reflect the new section structure in the "Guide Contents" table.

## Key Constraints

- Every section must reference at least one concrete construct from the operating model (per existing publishing checklist).
- Commitments section uses SLAs as primary language, with contractual terms connected at the appropriate tier.
- Commitments section references the [accountability framework](org-8.0/people-and-culture/accountability.md) to connect outcome-based vs. commitment-based accountability.
- No platitudes. No generic advice. All content grounded in the Engagement Operating Model.
- All existing external reference links preserved verbatim.
- EA preamble ("Architecture vs. Technical Architecture") and AVA preamble ("The AVA Leads the Verification Squad") retained after the Introduction, before section 1.
- Each document opens with a brief Introduction (Purpose, Scope, Position, Function) making it nearly self-sufficient.

