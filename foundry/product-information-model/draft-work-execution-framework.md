# Work Execution Framework

The Work Model defines **what work exists** — entity types, state transitions, and relationships. But it is intentionally light on three execution dimensions that stakeholders need to structure, assess, and navigate their work:

1. **Artifacts** — what structured outputs does this work produce?
2. **Definition of Done** — when is this work complete, and what quality gates must it pass?
3. **Guidance** — what playbooks, guidelines, and decision frameworks help navigate this work from initiation to completion?

This framework establishes the systematic approach for capturing these dimensions across all five tracks. The framework is part of the Work Model (not the Operating Model), because artifacts and completion criteria are properties of the work itself — they are information model concerns, not organizational design concerns.

> **Boundary with Operating Model:** Artifacts and Definition of Done describe *what the work produces* and *when it's done*. Playbooks and guidelines describe *how to do the work well*. The former belongs here (Work Model). The latter is a reference from here to the Operating Model, where team practices, tooling, and execution methodology live. This framework captures the *structure* of guidance (what a playbook should cover) but not the *content* (that is Operating Model territory, developed per-team).

---

## 1. Artifact Taxonomy

Every work entity in the Work Model produces one or more structured outputs. These artifacts fall into five categories:

| Artifact Category | What It Contains | Examples |
|---|---|---|
| **Decision Artifact** | A recorded decision with context, rationale, and consequences. Captures *why* a choice was made. | PDR, Win/Loss Analysis finding, Prioritization rationale |
| **Evidence Artifact** | Data, findings, or observations that inform decisions. Captures *what was learned*. | Research findings, Experiment results, Feedback, Case pattern analysis |
| **Specification Artifact** | A detailed description of what should be built, changed, or delivered. Captures *what to do*. | PSD, Release plan, Deployment runbook, GTM launch plan, Onboarding plan |
| **Delivery Artifact** | A versioned, quality-gated output that moves toward or reaches a customer. Captures *what was built*. | System Version, Module Version, Product Version, Module Package Version, Product Package Version, Deployment (record), Enablement asset, Campaign asset |
| **Assessment Artifact** | A structured evaluation of results against targets or criteria. Captures *how it went*. | Post-Incident Report, QBR summary, Post-implementation review, Target progress update |

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

Not all artifacts pass through every state. A System Version goes `Building → Released` (its own lifecycle). A Module Version goes `Integrating → Verified`. Feedback goes `Captured → Reviewed → Promoted/Archived`. The pattern provides a common vocabulary, not a mandatory sequence.

### Transitional vs. Terminal Artifacts

| Type | Behavior | Examples |
|---|---|---|
| **Transitional** | Born in one track, consumed by another. The artifact's primary value is in *crossing a boundary*. | Feedback (Win → Discovery), PSD (Discovery → Build), Deployment runbook (Build → Run) |
| **Terminal** | Consumed within the same track or by external systems. The artifact's primary value is *within its context*. | Module Version (integration verification), Enablement asset (Win internal), Post-Incident Report (Run internal — consumed by planning and Definition Model) |

---

## 1b. Artifact Type Catalog

The five artifact categories above (Decision, Evidence, Specification, Delivery, Assessment) are top-level classifications. Within each category, specific **named artifact types** exist per track — each with a description and **assessment criteria** that define what a good instance of that artifact looks like.

Assessment criteria serve two purposes: (1) they define quality expectations for artifact producers, and (2) they provide the evaluation basis for Evolve Reviews (Track 5) when assessing artifact quality across tracks.

> **Scope note:** Assessment criteria below are initial/skeletal. They will be refined iteratively as each track is detailed through the Work Execution Framework phasing plan. Track 5 (Evolve) owns the work of refining these criteria over time.

### Decision Artifacts

| Type | Track | Description | Assessment Criteria |
|---|---|---|---|
| PDR (Product Decision Record) | Discovery | Recorded product decision with context, rationale, consequences, and stakeholder acknowledgment | Alternatives considered and documented; consequences stated (positive and negative); all affected dimensions identified; stakeholders acknowledged |
| ADR (Architecture Decision Record) | Discovery, Build | Recorded technical/architectural decision with context, decision, consequences (Dim 5 entity). May be triggered by PDR or independent. | Context describes forces at play; decision is specific and actionable; consequences include both positive and negative; affected Systems identified; quality attributes addressed stated |
| ODR (Operations Decision Record) | Discovery, Run | Recorded operational/infrastructure decision with context, decision, consequences (Dim 7 entity). May be triggered by PDR, ADR, or independent. Scope: cloud provider/services, deployment strategy, data governance/archival, DR/BCP, compliance zones, capacity, cost optimization. | Context describes operational forces; decision is specific and actionable; consequences include both positive and negative; affected Environments and Systems identified; category classified; quality attributes addressed stated |
| Prioritization Rationale | Discovery | Ranked signal list with scoring methodology and association decisions | Scoring criteria transparent and consistently applied; all active Signals considered; association decisions justified against Initiative alignment |
| Change Record | Run | Recorded production change with approval chain and verification | Approval chain complete; rollback plan documented; verification results recorded; compliance window respected |
| Win/Loss Analysis Finding | Win | Post-deal decision analysis identifying contributing factors | Both win and loss factors identified; product vs. non-product attribution explicit; actionable patterns extracted; competitive intelligence captured |
| Evolve Definition Change Record | Evolve | Recorded change to Work Model or Operating Model definition with rationale | Change rationale references findings or improvement objectives; affected tracks identified; backward compatibility considered |

### Evidence Artifacts

| Type | Track | Description | Assessment Criteria |
|---|---|---|---|
| Exploration Findings | Discovery | Context, root causes, affected segments, and patterns from Signal investigation | Multiple root causes considered; affected segments identified; patterns linked to adjacent Signals; Ideas are hypothesis-framed |
| Research Findings | Discovery | Data, interview summaries, and analysis for/against a hypothesis | Research question clearly stated; methodology appropriate; evidence directly addresses hypothesis; bias acknowledged |
| Experiment Results | Discovery | Hypothesis, method, measurements, and pass/fail assessment | Pass/fail criteria defined before execution; sample size and duration justified; measurements reproducible; conclusions follow from data |
| Prototype/Spike Findings | Discovery | Feasibility or desirability evidence from throwaway artifacts | Assumption tested is explicit; findings distinguish feasibility from desirability; limitations of prototype acknowledged |
| Proposal/SOW | Win | Pre-sales proposal or statement of work for a prospect | Scope aligned to prospect's stated needs; pricing consistent with Pricing Tier (Dim 2); technical feasibility confirmed; timeline realistic |
| POC Results | Win | Proof-of-concept evaluation summary | Success criteria defined upfront; results measured against criteria; technical and business evaluation separated; next steps clear |
| Monitoring Alert/Report | All | Threshold breach notification or periodic health dashboard | Alert condition clearly defined; data source identified; false positive rate acceptable; escalation path specified |
| Evolve Findings | Evolve | Structured observations from process effectiveness, artifact quality, or guidance adequacy reviews | Finding type classified; severity justified with evidence; affected track(s) identified; recommendation actionable |

### Specification Artifacts

| Type | Track | Description | Assessment Criteria |
|---|---|---|---|
| Objective Definition | Discovery | Strategic objective for a planning horizon (Dim 1 entity update) | Measurable; time-bound; aligned to Strategic Theme; achievable within planning horizon |
| Initiative Definition | Discovery | Initiative scope with lever mix, targets, and Signal associations (Dim 1 entity update) | Lever mix totals 100%; embedded targets are measurable; associated Signals identified; cross-track implications stated |
| PSD (Product Specification Document) | Discovery | Engineering specification for module changes | Cross-dimensional review completed; acceptance criteria testable; affected modules identified; Dim 6 contract implications addressed (if applicable) |
| Definition Model Entity Update | Discovery | Evolution of entities in Dims 2–9 via Modeling Task | Entity fields complete; relationships bidirectionally consistent; examples provided; FAQ updated if design decision involved |
| Release Plan | Build | Scope, timeline, milestones, team allocation, risk assessment | All included PSDs/Initiatives listed; milestone criteria defined; risks identified with mitigations; team capacity validated |
| Milestone Definition | Build | Checkpoint criteria with entry/exit gates | Entry and exit criteria testable; dependencies identified; verification steps defined |
| Iteration Plan | Build | Story/task assignments and capacity allocation | Capacity validated against team availability; stories sized; dependencies sequenced |
| Deployment Runbook | Run | Environments, rollout strategy, rollback plan, verification steps | All target environments listed; rollback procedure tested; verification steps automated where possible; compliance windows noted |
| Capacity Forecast | Run | Projected load, scaling requirements, infrastructure plan | Load projections based on Customer Release scope; scaling triggers defined; cost implications stated |
| Market Delivery Plan | Win | Segment sequencing, readiness criteria, coordination checklist | Segment sequencing justified; readiness criteria testable; coordination with Build/Run Track confirmed |
| GTM Launch Plan | Win | Messaging, deliverables list, stakeholder enablement checklist | Messaging aligned to Customer Promise (Dim 3); all enablement assets identified; launch timeline synchronized with deployment |
| Enablement Program Plan | Win | Asset inventory, training schedule, competitive program scope | Asset gaps identified; training schedule realistic; competitive positioning current |
| CS Program Plan | Win | Onboarding playbook scope, retention program design, QBR cadence | Segment coverage complete; health score model defined; expansion triggers identified |
| Engagement Priority List | Win | Prospect/customer/segment ranking, sequencing, resource allocation | Ranking criteria transparent; resource allocation feasible; Initiative alignment stated |
| Evolution Cycle Plan | Evolve | Scope, objectives, timeline, and participants for an evolution cycle | Scope specific (named tracks/entities/artifacts); objectives measurable; participants confirmed; timeline realistic |
| Entity/Artifact Definition | Evolve | New or updated work entity definition, artifact type definition, or DoD criteria | Fields complete; statuses defined; relationships bidirectional; assessment criteria stated (for artifacts); examples provided |
| Guidance Structure Template | Evolve | Playbook or ceremony definition structure for Operating Model | All guidance sections covered; decision points identified; quality considerations specific; common pitfalls evidence-based |

### Delivery Artifacts

| Type | Track | Description | Assessment Criteria |
|---|---|---|---|
| Working Software Increment | Build | Code changes with acceptance test results (Story output) | Acceptance criteria met; unit tests pass; code reviewed; for HI Modules: UI touchpoint implementation verified |
| Epic Completion | Build | Completed capability with all Stories delivered (Module-scoped) | All Stories accepted; acceptance criteria met end-to-end |
| Bug Fix | Build | Root cause analysis, fix verification, regression test results | Root cause identified; fix verified; regression tests added; no new defects introduced; provenance documented |
| System Version | Build | Versioned, quality-gated artifact of a System (Dim 5) — atomic deployment unit. Build+Run shared vocabulary. Gate Profile: Standard (all gates) or Emergency (peer review + security scan + smoke tests; regression + benchmarks deferred — DR-031). | Standard: all quality gates passed. Emergency: non-negotiable gates passed; deferred gates tracked via originating Bug's Deferred Gate Obligation field; version follows semver; release notes complete |
| Module Version | Build | Composite system: integration-verified composition of System Versions for a Module (Dim 8) — integrated deployment unit + integration verification. Build+Run+Product shared vocabulary. | Integration contracts validated; integration test suite passes; all constituent System Versions released; binding configuration defined |
| Product Version | Build | Highest-order composite system: certified composition of Module Versions (BOM) — complete deployment unit + certification. Ubiquitous language across all teams and customers. | Declared BOM compatible; Resolved BOM tested together; end-to-end tests pass; compliance/security certification complete |
| Module Package Version | Run | Environment-independent composition: Module Version + operator-facing System Versions + operational wiring — integrated deployment artifact | Module Version verified; all operational System Versions released; operational wiring validated; environment-independent |
| Product Package Version | Run | Environment-independent highest-order deployable: Product Version + Module Package Versions + cross-module operational wiring — complete deployment artifact | Product Version certified; all Module Package Versions ready; cross-module operational wiring validated; environment-independent |
| SDD (System Deployment Descriptor) | Run | Environment-specific deployment specification for a System Version — resource config, runtime artifact references | System Version referenced; target environment specified; resource configuration validated; runtime artifacts identified |
| MDD (Module Deployment Descriptor) | Run | Environment-specific deployment specification for a Module Package Version — composes SDDs, Module-level config, deployment scripts | Module Package Version referenced; all SDDs composed; scripts tested; environment config validated; change management reviewed |
| PDD (Product Deployment Descriptor) | Run | Environment-specific deployment specification for a Product Package Version — composes MDDs, cross-module config, deployment ordering | Product Package Version referenced; all MDDs composed; deployment ordering defined; product-level scripts validated |
| Deployment Record | Run | Which descriptor (SDD/MDD/PDD version) was applied, to which environment, when, verification results | Environment and descriptor version recorded; verification results documented; rollback status confirmed |
| Tenant Provisioning Record | Run | What tenant was provisioned, in which environment, for which customer, with what purpose and configuration | Customer and segment identified; tenant purpose documented; isolation level verified; SLO tier assigned; initial health check passed |
| Maintenance Record | Run | What maintenance was done, verification results | Work completed as specified; verification results recorded; no service impact (or impact documented) |
| GTM Enablement Asset | Win | Marketing collateral, positioning docs, campaign assets | Messaging consistent with Customer Promise (Dim 3); segment-appropriate; reviewed by Product Marketing |
| Sales Enablement Asset | Win | Battlecards, demo environments, ROI calculators, playbooks | Competitive positioning current; demo data realistic; ROI model validated; training materials reviewed |
| CS Enablement Asset | Win | Onboarding playbooks, health score models, QBR templates, education assets | Segment-specific; health score thresholds validated; education content accurate and current |
| Partner Enablement Asset | Win | Partner demo environments, co-marketing kits, partner training | Partner-appropriate (not internal jargon); certification criteria clear; co-marketing approved |

### Assessment Artifacts

| Type | Track | Description | Assessment Criteria |
|---|---|---|---|
| Post-Incident Report | Run | Timeline reconstruction, final root cause analysis, contributing factors, quantified impact, corrective actions with owners and deadlines, lessons learned. Produced by Post-Incident Review. | Root cause identified (not just symptoms); contributing factors are systemic (not individual blame); impact quantified (tenants, duration, revenue, SLA breach); corrective actions assigned with owners and deadlines; prevention measures systemic; communication effectiveness assessed |
| Incident Record | Run | Observation record of service degradation: severity, detection source, affected systems/modules/environments/tenants, customer impact, SLA breach, response/resolution times, correlation fields | Severity classified (SEV-0..4); affected scope identified; SLA breach determination explicit; response/resolution times measured; parent/related/caused-by correlation completed where applicable |
| Customer Communication Record | Run | Chronological record of incident communications: channels, audience, content summaries, resolution summary (external), follow-up commitments | Communication timely relative to incident progression; channels appropriate for audience; resolution summary accurate and customer-appropriate; all committed follow-ups tracked |
| Go-live Checklist Completion | Win | Integration verification, configuration validation, handoff summary | All checklist items verified; integration tests passed; customer sign-off obtained |
| Health Intervention Record | Win | Customer health assessment, intervention actions, outcome | Health signals documented; intervention timely; outcome measured; follow-up scheduled if unresolved |
| Renewal/Churn Record | Win | Renewal outcome or churn analysis | Renewal terms documented; churn root causes identified (if churned); product vs. non-product attribution explicit |
| Campaign/Event Results | Win | Reach, engagement metrics, conversion outcomes | Metrics against targets; segment reach measured; conversion funnel documented; lessons captured |
| Partner Outcome Record | Win | Partner onboarding outcome, co-sell results, pipeline contribution | Onboarding milestones tracked; pipeline contribution quantified; partnership health assessed |
| Revenue Operations Record | Win | Billing/collections status, renewal processing, revenue recognition | Invoice accuracy verified; collections status current; revenue recognition compliant |
| Win Case Resolution Record | Win | Issue description, resolution steps, time-to-resolution, CSAT | Resolution complete; root cause documented (for Complaints); time-to-resolution within SLA; CSAT captured |
| Feedback | Win | Qualitative observations and pattern analyses from Win Reviews | Observation specific and evidence-based; patterns supported by data; promotion decision justified |
| Target Progress Update | Win | Quantitative assessment against Initiative embedded targets | Metrics current; variance explained; forecast updated; Business KPI and Customer Value Metric status included |
| QBR Summary | Win | Quarterly business review assessment | Win Outcome progress assessed; Customer Promise fulfillment reviewed; next-quarter priorities identified |
| Evolve Review Report | Evolve | Process effectiveness, artifact quality, or guidance adequacy assessment | Scope stated; evidence cited; findings classified by type and severity; recommendations actionable |

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
| **Deliberation** | PDR — Product Decision Record; ADR — Architecture Decision Record (when scope is technical/architectural); ODR — Operations Decision Record (when scope is operational/infrastructure) | Decision | Transitional (→ Build, Run, Definition Model) | **Entity files exist** (`dim1-pdr.md`, `dim5-adr.md`, `dim7-odr.md`) |
| **Research Task** | Research findings — evidence for/against a hypothesis, data, interview summaries | Evidence | Terminal (informs Deliberation) | _To be detailed._ |
| **Experiment** | Experiment results — hypothesis, method, measurements, pass/fail assessment | Evidence | Terminal (informs Deliberation) | _To be detailed._ |
| **Prototype / Spike** | Prototype artifact or spike findings — what was learned about feasibility or desirability | Evidence + Delivery | Terminal (informs Deliberation) | _To be detailed._ |
| **Specification Task** | PSD — Product Specification Document (includes UI journey specifications and touchpoint detail for HI Modules) | Specification | Transitional (→ Build Track) | **Entity file exists** (`dim1-psd.md`) |
| **Modeling Task** | Definition Model entity updates (Dims 2–9, including Dim 5 systems, components, dependencies, interaction flows, and Dim 6 personas, modules, operations, contracts) | Specification | Transitional (→ Definition Model) | Captured via entity files |
| **Signal Monitoring** | Alert/trigger (when threshold breached), pipeline report/dashboard | Evidence + Assessment | Terminal (triggers Prioritization, Deliberation) | **Entity file exists** (`track1-signal-monitoring.md`) |

### Track 2: Build Track

| Work Entity | Artifact(s) Produced | Category | Transitional? | Current State |
|---|---|---|---|---|
| **Release Planning Task** | Release plan — scope, timeline, milestones, team allocation, risk assessment; Epic and Integration Epic identification | Specification | Terminal (internal planning) | **Entity file exists** (`track2-release-planning-task.md`) |
| **Milestone Planning Task** | Milestone definition — checkpoint criteria, entry/exit gates, cross-Epic dependency gating, integration verification gates | Specification | Terminal (internal planning) | **Entity file exists** (`track2-milestone-planning-task.md`) |
| **Iteration Planning Task** | Iteration plan — Story/Integration Story/Technical Task assignments, capacity allocation | Specification | Terminal (internal planning) | **Entity file exists** (`track2-iteration-planning-task.md`) |
| **Epic** | Completed Epic — acceptance criteria met, all Stories delivered (Module-scoped, Dim 8) | Delivery | Terminal | **Entity file exists** (`track2-epic.md`) |
| **Story** | Working software increment, acceptance test results; for HI Modules includes UI touchpoint implementation (Module-scoped, Dim 8) | Delivery | Terminal | **Entity file exists** (`track2-story.md`) |
| **Technical Task** | Code changes, test results, technical documentation updates (System/Component-scoped, Dim 5). Serves Build Track Stories and Integration Stories. | Delivery | Terminal | **Entity file exists** (`track2-technical-task.md`) |
| **Bug** | Bug fix — root cause analysis, fix verification, regression test results. Provenance: Build / Run / Win | Delivery + Evidence | Terminal | **Entity file exists** (`track2-bug.md`) |
| **Integration Epic** | Verified cross-System integration; integration contracts; contributes to Module Version verification | Delivery | Terminal | **Entity file exists** (`track2-integration-epic.md`) |
| **Integration Story** | Integration contracts (API schemas, event schemas), integration test suites | Delivery + Evidence | Terminal | **Entity file exists** (`track2-integration-story.md`) |
| **Design Deliberation** | ADR(s) — architectural decisions emerging during build work | Decision | Transitional (→ Definition Model, Dim 5) | **Entity file exists** (`track2-design-deliberation.md`) |
| **System Version** | Versioned, quality-gated artifact of a System (Dim 5) — atomic deployment unit | Delivery | Transitional (→ Run Track) | **Entity file exists** (`track2-system-version.md`) |
| **Module Version** | Composite system: integration-verified composition of System Versions for a Module (Dim 8) — integrated deployment unit + integration verification; Build+Run+Product shared vocabulary | Delivery | Transitional (→ Run Track for Module Package Version enrichment) | **Entity file exists** (`track2-module-version.md`) |
| **Product Version** | Highest-order composite system: certified composition of Module Versions (BOM) — complete deployment unit + certification; ubiquitous language across all teams and customers | Delivery | Transitional (→ Run Track for Product Package Version enrichment, → Win Track) | **Entity file exists** (`track2-product-version.md`) |
| **Technical Debt Item** | Documented technical debt — debt category, impact, resolution path | Evidence | Terminal (resolved via Epic or Story) | **Entity file exists** (`track2-technical-debt-item.md`) |
| **Build Monitoring** | Alert/trigger (when threshold breached), quality report/dashboard | Evidence + Assessment | Terminal (triggers Bug, Technical Debt Item, planning) | **Entity file exists** (`track2-build-monitoring.md`) |

### Track 3: Run Track

| Work Entity | Artifact(s) Produced | Category | Transitional? | Current State |
|---|---|---|---|---|
| **Deployment Planning Task** | Deployment descriptors (SDD/MDD/PDD versions) — environment-specific deployment specifications with configuration and scripts. Also produces deployment runbooks. Also may produce Verification Tasks and Maintenance Tasks. Governed by a Deployment Plan. | Specification + Delivery | Terminal (operational) | **Entity file exists** (`track3-deployment-planning-task.md`) |
| **Capacity Planning Task** | Capacity forecast — projected load, scaling requirements, infrastructure plan | Specification | Terminal (operational) | _To be detailed._ |
| **Run Epic** | Completed operational engineering capability — operational System Versions, Module Package Version contribution (Module-scoped) | Delivery | Terminal | **Entity file exists** (`track3-run-epic.md`) |
| **Run Story** | Operational System Version — versioned artifact of an operational System (e.g., probe, reconciler) | Delivery | Terminal | **Entity file exists** (`track3-run-story.md`) |
| **Technical Task (Run Track)** | Code changes, test results, documentation updates for operational Systems (System/Component-scoped, Dim 5). Serves Run Stories. Same entity structure as Build Track Technical Tasks, distinct track ownership. | Delivery | Terminal | **Entity file exists** (`track3-technical-task.md`) |
| **Deployment** | Deployment record (artifact) — which descriptor (SDD/MDD/PDD version) was applied, to which environment, when, by whom. Produced by a Deployment Task. | Delivery | Terminal | **Entity file exists** (`track3-deployment.md`) |
| **Incident (Artifact)** | Incident record — observation of service degradation: severity (SEV-0..4), detection source, affected systems/modules/environments/tenants, customer impact, SLA breach, response/resolution times, correlation (parent/related/caused-by) | Evidence | Terminal (observation record; triggers work entities) | **Entity file exists** (`track3-incident.md`) |
| **Incident Response Task** | Resolution summary, workaround documentation; may produce Bug (Track 2), Signal (Track 1), emergency Change Request (Track 3) | Delivery + Evidence | Transitional (→ Bug, → Signal, → Change Request) | **Entity file exists** (`track3-incident-response-task.md`) |
| **Post-Incident Review** | Post-Incident Report — timeline reconstruction, final RCA, contributing factors, quantified impact, corrective actions with owners. Routes follow-ups to Build (Bug), Run (Run Epic, Maintenance), Discovery (Signal), Evolve (Finding), Definition Model (ODR) | Assessment | Transitional (→ multiple tracks) | **Entity file exists** (`track3-post-incident-review.md`) |
| **Customer Communication Task** | Incident communication record — status updates issued, channels used, audience reached, resolution summary (external), follow-up commitments | Evidence | Terminal | **Entity file exists** (`track3-customer-communication-task.md`) |
| **Change Request** | Change record — what changed, approval chain, verification, rollback status | Decision | Terminal | _To be detailed._ |
| **Maintenance Task** | Maintenance record — what was done, verification results | Delivery | Terminal | _To be detailed._ |
| **Tenant** | Tenant provisioning record — customer, environment, purpose, configuration, SLO tier; Tenant lifecycle events (scale, suspend, decommission) | Delivery | Terminal (operational) | _To be detailed._ |
| **Module Package Version** | Environment-independent composition: Module Version + operator-facing System Versions + operational wiring — integrated deployment artifact | Delivery | Transitional (→ MDD, → Product Package Version) | **Entity file exists** (`track3-module-package-version.md`) |
| **Product Package Version** | Environment-independent highest-order deployable: Product Version + Module Package Versions + cross-module operational wiring — complete deployment artifact | Delivery | Transitional (→ PDD) | **Entity file exists** (`track3-product-package-version.md`) |
| **SDD (System Deployment Descriptor)** | Environment-specific deployment specification for a System Version — resource config, replicas, env vars, runtime artifact references. Composed into MDD. | Delivery | Transitional (→ MDD, → Deployment Task) | **Entity file exists** (`track3-sdd.md`) |
| **MDD (Module Deployment Descriptor)** | Environment-specific deployment specification for a Module Package Version — composes SDDs, Module-level env config, pre-rollout/validation/rollback scripts. A "system" in its own right. | Delivery | Transitional (→ PDD, → Deployment Task) | **Entity file exists** (`track3-mdd.md`) |
| **PDD (Product Deployment Descriptor)** | Environment-specific deployment specification for a Product Package Version — composes MDDs, cross-module env config, deployment ordering, product-level scripts. | Delivery | Transitional (→ Deployment Task) | **Entity file exists** (`track3-pdd.md`) |
| **Deployment Plan** | Deployment Plan scope, risk assessment, produced tasks — deliberation activity for scoping a rollout | Specification | Terminal (operational) | **Entity file exists** (`track3-deployment-plan.md`) |
| **Deployment Task** | Deployment execution record — descriptor applied, environment targeted, deployer, result. Produces Deployment (artifact). | Delivery | Terminal | **Entity file exists** (`track3-deployment-task.md`) |
| **Verification Task** | Post-deployment verification evidence — criteria, type, pass/fail, evidence. Required for Change Request closure. | Assessment | Terminal | **Entity file exists** (`track3-verification-task.md`) |
| **Deployment Drill Task** | Drill results — rehearsal of deployment procedure in non-production environment. Optional predecessor to Deployment Tasks. | Assessment | Terminal | **Entity file exists** (`track3-deployment-drill-task.md`) |
| **(Run-originated ODR)** | Operations Decision Record — operational decisions emerging from Run Deliberations within Run Epics | Decision | Transitional (→ Definition Model, Dim 7) | **Entity file exists** (`dim7-odr.md`) |
| **System Monitoring** | Alert/trigger (when threshold breached), SLA report/dashboard, Tenant health report, Operational Target compliance report. Monitors operational health across all composition levels. | Evidence + Assessment | Terminal (triggers Incident, Change Request, Capacity Planning, Run Epic) | **Entity file exists** (`track3-system-monitoring.md`) |
| **Run Engineering Monitoring** | Alert/trigger (when threshold breached), engineering quality report/dashboard. Monitors Run Track engineering health (operational system CI/CD, Run Epic velocity). | Evidence + Assessment | Terminal (triggers Run Story, Run Epic scope adjustment) | **Entity file exists** (`track3-run-engineering-monitoring.md`) |

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
| **FIR (First Information Report)** | FIR Resolution Record — original report, triage assessment, sub-item references, resolution summary; routed sub-items (Incident, Bug, Signal, Win Case, Maintenance Task) | Evidence + Specification | Transitional (→ Track 2 Bug, → Track 3 Incident, → Dim 1 Signal, → Track 4 Win Case, → Track 3 Maintenance Task) | **Entity file exists** (`track4-fir.md`) |
| **Win Case** | Resolution record — issue description, resolution steps, time-to-resolution, CSAT score. Always originates from an FIR (DR-032). | Assessment | Terminal (patterns → Win Review) | _To be detailed._ |
| **Win Review** | Feedback (qualitative) + Target progress updates (quantitative) | Evidence + Assessment | Transitional (Feedback → Discovery) | **Entity files exist** (`track4-win-review.md`, `track4-feedback.md`) |
| **Win Monitoring** | Alert/trigger (when threshold breached), health/revenue report/dashboard | Evidence + Assessment | Terminal (triggers Win Activity, Win Case escalation, Win Review) | **Entity file exists** (`track4-win-monitoring.md`) |

### Track 5: Evolve Track

| Work Entity | Artifact(s) Produced | Category | Transitional? | Current State |
|---|---|---|---|---|
| **Evolve Planning** | Evolution cycle plan — scope, objectives, timeline, participants | Specification | Terminal (Evolve internal) | **Entity file exists** (`track5-evolve-planning.md`) |
| **Evolve Review** | Evolve Findings — process gaps, artifact quality issues, guidance deficiencies | Evidence + Assessment | Transitional (→ Evolve Definition Task, or → Discovery as Signal) | **Entity file exists** (`track5-evolve-review.md`) |
| **Evolve Definition Task** | Updated entity files, artifact type definitions, DoD criteria, guidance structures, Decision Records | Specification + Decision | Transitional (→ Work Model, Operating Model) | **Entity file exists** (`track5-evolve-definition-task.md`) |
| **Evolve Monitoring** | Alert/trigger (when threshold breached), process health report/dashboard | Evidence + Assessment | Terminal (triggers Evolve Review, Evolve Planning) | **Entity file exists** (`track5-evolve-monitoring.md`) |

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
| **Phase 0 (this document)** | Framework structure, artifact taxonomy, artifact type catalog, cross-track inventory, DoD/Guidance patterns | Framework document; entity template extension; artifact type catalog with assessment criteria |
| **Phase 1: Discovery Track** | Detail artifacts, DoD, and guidance structure for all Discovery Track entities | Updated entity files; Track 1 framework view |
| **Phase 2: Build Track** | Detail artifacts, DoD, and guidance structure for all Build Track entities | Updated entity files; Track 2 framework view |
| **Phase 3: Run Track** | Detail artifacts, DoD, and guidance structure for all Run Track entities | Updated entity files; Track 3 framework view |
| **Phase 4: Win Track** | Detail artifacts, DoD, and guidance structure for all Win Track entities | Updated entity files; Track 4 framework view |
| **Phase 5: Evolve Track** | Detail artifacts, DoD, and guidance structure for all Evolve Track entities | Updated entity files; Track 5 framework view |
| **Phase 6: Cross-track integration** | Verify all cross-track handoffs; validate transitional artifact flows end-to-end | Cross-track artifact flow diagram; handoff contract validation |

Tracks may be detailed in any order. Each phase is self-contained — detailing one track does not require detailing another first (though cross-track handoff validation in Phase 6 requires all five tracks).

---

## 7. Relationship to Other UPIM Documents

| Document | Relationship |
|---|---|
| `draft-work-model.md` | The Work Model defines work entities and their state transitions. This framework adds execution dimensions (artifacts, DoD, guidance) to those entities. |
| `entities/work-model/*.md` | Entity files will be extended with Outputs/Artifacts, Definition of Done, and Guidance Reference sections as each track is detailed. |
| `entities/README.md` | The entity template will be extended to include the new sections. |
| Operating Model (future) | Guidance content (playbooks, procedures) will live in the Operating Model. Entity files will reference them. |

---
