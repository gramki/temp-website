# Work Execution Framework

The Work Model defines **what work exists** — entity types, state transitions, and relationships. But it is intentionally light on three execution dimensions that stakeholders need to structure, assess, and navigate their work:

1. **Artifacts** — what structured outputs does this work produce?
2. **Definition of Done** — when is this work complete, and what quality gates must it pass?
3. **Guidance** — what playbooks, guidelines, and decision frameworks help navigate this work from initiation to completion?

This framework establishes the systematic approach for capturing these dimensions across all four tracks. The framework is part of the Work Model (not the Operating Model), because artifacts and completion criteria are properties of the work itself — they are information model concerns, not organizational design concerns.

> **Boundary with Operating Model:** Artifacts and Definition of Done describe *what the work produces* and *when it's done*. Playbooks and guidelines describe *how to do the work well*. The former belongs here (Work Model). The latter is a reference from here to the Operating Model, where team practices, tooling, and execution methodology live. This framework captures the *structure* of guidance (what a playbook should cover) but not the *content* (that is Operating Model territory, developed per-team).

---

## 1. Artifact Taxonomy

Every work entity in the Work Model produces one or more structured outputs. These artifacts fall into five categories:

| Artifact Category | What It Contains | Examples |
|---|---|---|
| **Decision Artifact** | A recorded decision with context, rationale, and consequences. Captures *why* a choice was made. | PDR, Win/Loss Analysis finding, Prioritization rationale |
| **Evidence Artifact** | Data, findings, or observations that inform decisions. Captures *what was learned*. | Research findings, Experiment results, Feedback, Case pattern analysis |
| **Specification Artifact** | A detailed description of what should be built, changed, or delivered. Captures *what to do*. | PSD, Release plan, Deployment runbook, GTM launch plan, Onboarding plan |
| **Delivery Artifact** | A versioned, quality-gated output that moves toward or reaches a customer. Captures *what was built*. | Module Version, Product Version, Enablement asset, Campaign asset |
| **Assessment Artifact** | A structured evaluation of results against targets or criteria. Captures *how it went*. | Post-mortem, QBR summary, Post-implementation review, Target progress update |

### Artifact Lifecycle Pattern

Artifacts follow a common lifecycle pattern regardless of category:

```
Created → Reviewed → Accepted/Revised → Consumed/Archived
```

- **Created** — the artifact is drafted as an output of work
- **Reviewed** — the artifact is assessed for quality and completeness (by whom depends on the artifact)
- **Accepted** — the artifact meets quality criteria and is available for consumption
- **Revised** — the artifact needs rework before acceptance
- **Consumed** — the artifact is used by downstream work (e.g., PSD consumed by Build Track; Feedback promoted to Signal)
- **Archived** — the artifact is no longer active but retained for reference

Not all artifacts pass through every state. A Module Version goes `Building → Released` (its own lifecycle). Feedback goes `Captured → Reviewed → Promoted/Archived`. The pattern provides a common vocabulary, not a mandatory sequence.

### Transitional vs. Terminal Artifacts

| Type | Behavior | Examples |
|---|---|---|
| **Transitional** | Born in one track, consumed by another. The artifact's primary value is in *crossing a boundary*. | Feedback (Win → Discovery), PSD (Discovery → Build), Deployment runbook (Build → Run) |
| **Terminal** | Consumed within the same track or by external systems. The artifact's primary value is *within its context*. | Module Version (Build output), Enablement asset (Win internal), Post-mortem (Run internal) |

---

## 2. Cross-Track Artifact Inventory

The following inventory identifies key artifacts produced by each track. This is the current known state — individual tracks will be detailed iteratively. Items marked `_To be detailed._` indicate artifacts where the structure, fields, and quality criteria have not yet been specified.

### Track 1: Discovery Track

| Work Entity | Artifact(s) Produced | Category | Transitional? | Current State |
|---|---|---|---|---|
| **Objective Setting Task** | Objective definition (Dim 1 entity update) | Specification | Terminal (Dim 1) | Captured via Dim 1 entity |
| **Initiative Scoping Task** | Initiative definition (Dim 1 entity update) with lever mix and targets | Specification | Terminal (Dim 1) | Captured via Dim 1 entity |
| **Prioritization Task** | Prioritization rationale — ranked signal list with scoring and association decisions | Decision | Terminal | _To be detailed._ |
| **Signal Exploration Task** | Exploration findings — context, root causes, affected segments, patterns; Idea(s) generated | Evidence + Specification | Transitional (→ Ideas) | _To be detailed._ |
| **Deliberation** | PDR — Product Decision Record | Decision | Transitional (→ Build, Definition Model) | **Entity file exists** (`dim1-pdr.md`) |
| **Research Task** | Research findings — evidence for/against a hypothesis, data, interview summaries | Evidence | Terminal (informs Deliberation) | _To be detailed._ |
| **Experiment** | Experiment results — hypothesis, method, measurements, pass/fail assessment | Evidence | Terminal (informs Deliberation) | _To be detailed._ |
| **Prototype / Spike** | Prototype artifact or spike findings — what was learned about feasibility or desirability | Evidence + Delivery | Terminal (informs Deliberation) | _To be detailed._ |
| **Specification Task** | PSD — Product Specification Document (includes UI journey specifications and touchpoint detail for HI Modules) | Specification | Transitional (→ Build Track) | **Entity file exists** (`dim1-psd.md`) |
| **Modeling Task** | Definition Model entity updates (Dims 2–9, including Dim 6 personas, modules, operations, contracts) | Specification | Transitional (→ Definition Model) | Captured via entity files |
| **Signal Monitoring** | Alert/trigger (when threshold breached), pipeline report/dashboard | Evidence + Assessment | Terminal (triggers Prioritization, Deliberation) | **Entity file exists** (`track1-signal-monitoring.md`) |

### Track 2: Build Track

| Work Entity | Artifact(s) Produced | Category | Transitional? | Current State |
|---|---|---|---|---|
| **Release Planning Task** | Release plan — scope, timeline, milestones, team allocation, risk assessment | Specification | Terminal (internal planning) | _To be detailed._ |
| **Milestone Planning Task** | Milestone definition — checkpoint criteria, entry/exit gates | Specification | Terminal (internal planning) | _To be detailed._ |
| **Iteration Planning Task** | Iteration plan — story/task assignments, capacity allocation | Specification | Terminal (internal planning) | _To be detailed._ |
| **Epic** | Completed epic — acceptance criteria met, stories delivered | Delivery | Terminal | _To be detailed._ |
| **User Story** | Working software increment, acceptance test results; for HI Modules includes UI touchpoint implementation (screens, forms, interactions) | Delivery | Terminal | _To be detailed._ |
| **Technical Task** | Code changes, test results, technical documentation updates | Delivery | Terminal | _To be detailed._ |
| **Bug** | Bug fix — root cause analysis, fix verification, regression test results | Delivery + Evidence | Terminal | _To be detailed._ |
| **Module Version** | Versioned, quality-gated module artifact | Delivery | Transitional (→ Run Track) | **Entity file exists** (`track2-module-version.md`) |
| **Product Version** | Verified/certified composition of Module Versions (BOM) | Delivery | Transitional (→ Run Track) | **Entity file exists** (`track2-product-version.md`) |
| **Build Monitoring** | Alert/trigger (when threshold breached), quality report/dashboard | Evidence + Assessment | Terminal (triggers Bug, Maintenance Task, planning) | **Entity file exists** (`track2-build-monitoring.md`) |

### Track 3: Run Track

| Work Entity | Artifact(s) Produced | Category | Transitional? | Current State |
|---|---|---|---|---|
| **Deployment Planning Task** | Deployment runbook — environments, rollout strategy, rollback plan, verification steps | Specification | Terminal (operational) | _To be detailed._ |
| **Capacity Planning Task** | Capacity forecast — projected load, scaling requirements, infrastructure plan | Specification | Terminal (operational) | _To be detailed._ |
| **Deployment** | Deployment record — what was deployed, where, when, verification results | Delivery | Terminal | _To be detailed._ |
| **Incident** | Post-mortem — timeline, root cause, impact assessment, corrective actions, prevention measures | Assessment + Evidence | Transitional (→ Discovery as Signal, if systemic) | _To be detailed._ |
| **Change Request** | Change record — what changed, approval chain, verification, rollback status | Decision | Terminal | _To be detailed._ |
| **Maintenance Task** | Maintenance record — what was done, verification results | Delivery | Terminal | _To be detailed._ |
| **System Monitoring** | Alert/trigger (when threshold breached), SLA report/dashboard | Evidence + Assessment | Terminal (triggers Incident, Change Request, Capacity Planning) | **Entity file exists** (`track3-system-monitoring.md`) |

### Track 4: Win Track

| Work Entity | Artifact(s) Produced | Category | Transitional? | Current State |
|---|---|---|---|---|
| **Customer Release Planning** | Market delivery plan — segment sequencing, readiness criteria, coordination checklist | Specification | Terminal (Win internal) | _To be detailed._ |
| **GTM Planning** | GTM launch plan — messaging, deliverables list, stakeholder enablement checklist | Specification | Terminal (Win internal) | _To be detailed._ |
| **Sales Enablement Planning** | Enablement program plan — asset inventory, training schedule, competitive program scope | Specification | Terminal (Win internal) | _To be detailed._ |
| **Customer Success Planning** | CS program plan — onboarding playbook scope, retention program design, QBR cadence | Specification | Terminal (Win internal) | _To be detailed._ |
| **Engagement Planning** | Engagement priority list — prospect/customer/segment ranking, sequencing, resource allocation | Specification | Terminal (Win internal) | _To be detailed._ |
| **GTM Enablement** | Marketing collateral, positioning docs, campaign assets, pricing tools | Delivery | Terminal (reusable asset) | _To be detailed._ |
| **Sales Enablement Asset** | Battlecards, demo environments, ROI calculators, playbooks, training materials | Delivery | Terminal (reusable asset) | _To be detailed._ |
| **CS Enablement** | Onboarding playbooks, health score models, QBR templates, expansion frameworks, customer education assets | Delivery | Terminal (reusable asset) | _To be detailed._ |
| **Partner Enablement** | Partner demo environments, co-marketing kits, partner training, certification programs | Delivery | Terminal (reusable asset) | _To be detailed._ |
| **Pre-sales Engagement** | Proposal/SOW, POC results, technical evaluation summary | Evidence + Specification | Terminal (CRM-linked) | _To be detailed._ |
| **Implementation / Onboarding** | Go-live checklist completion, integration verification, handoff summary | Assessment | Terminal | _To be detailed._ |
| **Retention Engagement** | Health intervention record, renewal outcome, churn analysis (if churned) | Assessment | Terminal | _To be detailed._ |
| **Expansion Engagement** | Expansion proposal, negotiation outcome, account growth record | Evidence + Specification | Terminal | _To be detailed._ |
| **Segment Engagement** | Campaign/event results — reach, engagement metrics, conversion outcomes; customer training delivery | Assessment | Terminal | _To be detailed._ |
| **Partner Engagement** | Partner onboarding outcome, co-sell results, pipeline contribution | Assessment | Terminal (PRM-linked) | _To be detailed._ |
| **Revenue Operations Engagement** | Billing/collections record, renewal outcome, revenue recognition status | Assessment | Terminal | _To be detailed._ |
| **Win Case** | Resolution record — issue description, resolution steps, time-to-resolution, CSAT score | Assessment | Terminal (patterns → Win Review) | _To be detailed._ |
| **Win Review** | Feedback (qualitative) + Target progress updates (quantitative) | Evidence + Assessment | Transitional (Feedback → Discovery) | **Entity files exist** (`track4-win-review.md`, `track4-feedback.md`) |
| **Win Monitoring** | Alert/trigger (when threshold breached), health/revenue report/dashboard | Evidence + Assessment | Terminal (triggers Win Engagement, Win Case escalation, Win Review) | **Entity file exists** (`track4-win-monitoring.md`) |

---

## 3. Definition of Done (DoD) Pattern

Every work entity has an implicit or explicit "done" condition. Making these explicit serves three purposes:

1. **Quality gate** — prevents premature state transitions (e.g., a PSD marked `Ready` without cross-dimensional review)
2. **Completeness checklist** — ensures all required artifacts are produced
3. **Handoff contract** — downstream consumers know what to expect

### DoD Structure

Each work entity's Definition of Done consists of three components:

| Component | Description | Example (Deliberation) |
|---|---|---|
| **Entry Criteria** | What must be true before this work can start | Ideas/PDRs to evaluate have been identified; relevant stakeholders are available; supporting evidence (Research findings, Experiment results) is assembled |
| **Exit Criteria** | What must be true for this work to be considered complete | Decision recorded as PDR with context, rationale, and consequences; all stakeholders have acknowledged; status transitions applied to evaluated Ideas |
| **Artifact Checklist** | Which artifacts must be produced before "done" | PDR document created; Idea statuses updated; downstream work items identified (PSDs, Modeling Tasks) |

### DoD Granularity

DoD can be defined at two levels:

1. **Entity-level DoD** — applies to all instances of a work entity type (captured in the entity file). This is a Work Model concern.
2. **Instance-level DoD** — applies to a specific work item, extending the entity-level DoD with context-specific criteria. This is an Operating Model concern (teams decide how to extend).

The Work Model captures entity-level DoD. Teams extend it at the instance level through their Operating Model practices.

---

## 4. Guidance Pattern

Guidance helps stakeholders navigate a work entity from initiation to completion. While the *content* of guidance is an Operating Model concern (it varies by team, product, and context), the *structure* of guidance is a Work Model concern — we can define what a playbook for any work type should cover.

### Guidance Structure

Every work entity's guidance follows a common structure:

| Section | What It Covers | Example (Signal Exploration Task) |
|---|---|---|
| **When to initiate** | Triggers and conditions that warrant creating this work item | A Signal has been associated with an active Initiative during Prioritization; the Signal has sufficient initial context to begin exploration |
| **Key activities** | The core activities involved in this work (not a step-by-step procedure, but the essential moves) | Context mapping, stakeholder interviews, root cause analysis, pattern identification, adjacent signal review, idea generation |
| **Decision points** | Forks where the work may branch or terminate | "Is this Signal well-understood enough to generate Ideas, or does it need Research Task evidence first?" |
| **Artifacts to produce** | What outputs are expected (references the artifact inventory) | Exploration findings document, one or more Idea drafts |
| **Quality considerations** | What distinguishes good work from poor work | Exploration considered multiple root causes (not just the first); affected segments are identified; Ideas are hypothesis-framed (not solution-stated) |
| **Common pitfalls** | Known failure modes | Jumping to solutions without understanding the problem space; exploring too broadly without time-boxing; generating a single Idea instead of multiple candidates |
| **Related work** | What typically comes before and after | Before: Prioritization Task (Signal association); After: Research Task, Experiment, or Deliberation (Idea validation) |

### Guidance Location

Guidance content is **referenced** from the work entity file, not embedded in it. The entity file contains a `## Guidance Reference` section that points to the Operating Model location where the playbook lives.

This separation means:
- The Work Model remains stable (what the work *is* doesn't change when a team updates its playbook)
- Different teams or products can have different playbooks for the same work entity
- Playbooks can evolve independently of the information model

---

## 5. Track-Level Framework View

Each track can be viewed through this framework lens — a systematic summary of its work entities, artifacts, DoD gates, and guidance references. This provides a "dashboard" view for each track.

### Track Framework Template

```markdown
## Track N: [Name] — Execution Framework View

### Artifact Summary

| Work Entity | Primary Artifact | Category | Downstream Consumer |
|---|---|---|---|
| ... | ... | ... | ... |

### DoD Summary

| Work Entity | Key Exit Criteria | Artifact Checklist |
|---|---|---|
| ... | ... | ... |

### Guidance Index

| Work Entity | Playbook | Status |
|---|---|---|
| ... | [reference] | Available / In Development / Not Started |

### Cross-Track Handoffs

| From | To | Artifact | Handoff Condition |
|---|---|---|---|
| ... | ... | ... | ... |
```

Track-level framework views will be developed iteratively per track. They may live as sections within `draft-work-model.md` or as separate per-track documents, depending on size.

---

## 6. Iterative Detailing Plan

The framework is designed for incremental development:

| Phase | Scope | What Gets Produced |
|---|---|---|
| **Phase 0 (this document)** | Framework structure, artifact taxonomy, cross-track inventory, DoD/Guidance patterns | Framework document; entity template extension |
| **Phase 1: Discovery Track** | Detail artifacts, DoD, and guidance structure for all Discovery Track entities | Updated entity files; Track 1 framework view |
| **Phase 2: Build Track** | Detail artifacts, DoD, and guidance structure for all Build Track entities | Updated entity files; Track 2 framework view |
| **Phase 3: Run Track** | Detail artifacts, DoD, and guidance structure for all Run Track entities | Updated entity files; Track 3 framework view |
| **Phase 4: Win Track** | Detail artifacts, DoD, and guidance structure for all Win Track entities | Updated entity files; Track 4 framework view |
| **Phase 5: Cross-track integration** | Verify all cross-track handoffs; validate transitional artifact flows end-to-end | Cross-track artifact flow diagram; handoff contract validation |

Tracks may be detailed in any order. Each phase is self-contained — detailing one track does not require detailing another first (though cross-track handoff validation in Phase 5 requires all four tracks).

---

## 7. Relationship to Other UPIM Documents

| Document | Relationship |
|---|---|
| `draft-work-model.md` | The Work Model defines work entities and their state transitions. This framework adds execution dimensions (artifacts, DoD, guidance) to those entities. |
| `entities/work-model/*.md` | Entity files will be extended with Outputs/Artifacts, Definition of Done, and Guidance Reference sections as each track is detailed. |
| `entities/README.md` | The entity template will be extended to include the new sections. |
| Operating Model (future) | Guidance content (playbooks, procedures) will live in the Operating Model. Entity files will reference them. |

---
