
## PART II: THE WORK MODEL (THE 4 TRACKS)

While the 9 Dimensions define the *Definition Model* of the product, the 4 Tracks define the *motion*. This is how Maker Roles (PMs, Devs, CS) organize their daily work to mutate the 9 Dimensions. Each track owns its own planning work alongside its core activities.

> **Scope Boundary Note:** The Work Model deliberately describes **what work exists** — entities, artifacts, and state transitions. It does NOT cover:
>
> - **Coordination patterns** — ceremonies, cadences, rituals, decision-making rhythms (e.g., Sprint Planning, Quarterly Business Review, Signal Review ceremonies)
> - **Organizational design** — roles, team structures, skills profiles, training, tools, and resource allocation
> - **Capacity and scheduling** — how much work fits in a period, who does it, velocity tracking
> - **Guidance content** — playbooks, procedures, and templates for executing work (the *structure* of guidance is a Work Model concern; the *content* is an Operating Model concern)
>
> These concerns belong to the **Operating Model** — the third model in the UPIM architecture, sitting above the Work Model. The Operating Model covers both coordination and organizational design as entangled facets of how the org executes. It depends on the Work Model (you must know what work entities exist before you can design ceremonies and roles around them) but is a separate modeling concern. See the PIM Architecture README for the full three-model stack.
>
> **Work Execution Framework:** The Work Model *does* capture three execution dimensions for each work entity: (1) what artifacts it produces, (2) its Definition of Done (entry/exit criteria, artifact checklist), and (3) references to Operating Model guidance. See `draft-work-execution-framework.md` for the framework, artifact taxonomy, and cross-track inventory.

### Track 1: The Discovery Track (Learning)

* **Goal:** Set strategic direction, prioritize Signals for discovery, explore Signals (Problems, Needs, Opportunities) to generate solution hypotheses (Ideas), validate hypotheses through research, experiments, prototypes, and deliberation, and author PSD(s) for validated Ideas.
* **Primary Owner:** Product Manager, UX Researcher, Executive Leadership (for strategic planning).
* **Input:** Strategic Themes and Objectives from business strategy; Signals (Problems, Needs, Opportunities); Ideas requiring validation.
* **Output:** Discovery produces three types of outputs:
  1. **PDR** — captures any significant decision affecting any dimension. A PDR may justify PSDs (engineering changes) AND/OR Definition Model updates (knowledge/model changes).
  2. **PSD(s)** — engineering specifications for module changes (via Specification Task).
  3. **Definition Model updates** — evolution of entities in Dims 2–9 (via Modeling Task). Examples: new Customer Segments, refined Value Propositions, updated Value Streams, new Capabilities.
  Additionally: Objectives, Initiatives, Customer Release definitions (Dimension 1); Idea status changes — either advanced to `Validated` (triggering PSD authoring via PDR) or moved to `Killed`.

* **Planning Entities:**
  * **Objective Setting Task:** Work to define or refine strategic Objectives for a planning horizon. (e.g., "Define H2 2026 product objectives based on board strategy review").
  * **Initiative Scoping Task:** Work to define an Initiative's scope, success criteria, target outcomes, and associate Signals. (e.g., "Scope the LATAM Currency Expansion initiative — target currencies, revenue goal, timeline").
  * **Prioritization Task:** Work to evaluate, score, and rank Signals (Problems, Needs, Opportunities) and associate them with active Initiatives for discovery investment. (e.g., "Quarterly review: rank and associate top 30 Signals to Q3 Initiatives").

* **Signal Exploration Entities:**
  * **Signal Exploration Task:** The structured work of investigating a Signal (Problem, Need, or Opportunity) — understanding its context, scope, root causes, affected segments, and adjacent patterns — and synthesizing one or more candidate Ideas (hypotheses) from that understanding. This is divergent, open-ended work that produces the Signal → Idea transition. (e.g., "Explore Signal: LATAM enterprises report 6-click FX confirmation — understand workflow pain, identify root causes, generate candidate solutions").
  * **Deliberation:** A collaborative, group-based activity where authorized stakeholders convene to discuss, evaluate, and decide. Deliberation produces outcomes through collective judgment — not empirical evidence. Spans both exploration (brainstorming Ideas from Signals) and validation (council deciding Go/Kill/Pivot on an Idea). A Deliberation may directly produce a PDR. (e.g., "Product council deliberation: evaluate three LATAM expansion approaches, decide on preferred strategy", "Cross-functional brainstorm: generate Ideas for batch payout automation from customer Signals").

* **Idea Validation Entities:**
  * **Research Task:** A targeted investigation action — specific data gathering, user interviews, competitive analysis, market sizing, regulatory review — to produce evidence for or against a hypothesis. Research Tasks are focused and convergent: you know what question you're trying to answer. (e.g., "Conduct 5 user interviews on FX rate-lock workflow to validate Idea X", "Pull usage data to quantify batch payout demand").
  * **Experiment:** A formal hypothesis test with explicit pass/fail criteria (e.g., "Fake-door button test for Euro payments — success if >10% click-through").
  * **Prototype / Spike:** A throwaway or low-fidelity artifact built to test a specific assumption around desirability or feasibility (e.g., "Figma mockup of the FX rate-lock confirmation flow", "Technical spike: can we get sub-200ms FX quotes from provider X?").

* **Output Entities:**
  * **Specification Task:** A granular PSD-authoring action — scoping modules, writing acceptance criteria, coordinating feasibility with engineering, decomposing into shippable increments. Represents the substantial work between a validated Idea and a shipped PSD (e.g., "Define webhook payload contract with Platform team", "Write acceptance criteria for FX module").
  * **Modeling Task:** Work to evolve Definition Model entities in any dimension (Dims 2–9) based on discovery findings. Modeling Tasks produce updates to the product's self-description — customer segments, buyer personas, business outcomes, customer promises, value streams, capabilities, data domains, and more. Dim 6 (Ecosystem & Extensibility) modeling includes Developer Personas, Programmatic User Personas, API Modules, API Operations and SLOs, and API Compatibility Contracts. A Modeling Task may be triggered by a PDR (a decision affecting a dimension) or by ongoing product knowledge maintenance. (e.g., "Define LATAM AP Clerk user persona", "Map Cross-Border Payout Processing value stream", "Design LATAM pricing tier structure", "Define Developer Persona", "Design API Module with operations and SLOs", "Model API Compatibility Contract for Payments API v2").

* **Monitoring Entities:**
  * **Signal Monitoring:** Continuous tracking of signal pipeline health, trend analysis across Signals, discovery velocity metrics. Surfaces when signal backlog grows, when themes shift, when discovery capacity is mismatched. Triggers: Prioritization Task re-evaluation, new Signal creation, Deliberation scheduling. (e.g., "Monitor LATAM Initiative signal pipeline — daily scan; alert when backlog > 20 or Signal aged > 60 days").



### Track 2: The Build Track (Construction)

* **Goal:** Plan releases and iterations, take validated PSDs, write high-quality code, and continuously produce Module Versions as stable, quality-gated artifacts.
* **Primary Owner:** Tech Lead, Developers, QA.

* **Planning Entities:**
  * **Release Planning Task:** Work to scope a Customer Release — which PSDs/Initiatives are included, timeline, milestones, team allocation. (e.g., "Plan Customer Release 'LATAM Expansion': scope to LATAM initiative PSDs, target mid-Q3 ship date").
  * **Milestone Planning Task:** Work to define checkpoints within a Customer Release with clear entry/exit criteria. (e.g., "Define 'API Complete' milestone — all cross-border endpoints passing integration tests").
  * **Iteration Planning Task:** Work to assign Epics/Stories to a time-boxed iteration, balance capacity. (e.g., "Sprint 14 planning: allocate FX rate-lock stories, account for team PTO").

* **Build Entities:**
  * **Epic:** A large, committed capability decomposed from a PSD (e.g., "Build Cross-Border API").
  * **User Story:** An Agile requirement delivering specific value (e.g., "As an AP Clerk, I want to lock the FX rate for 24 hours").
  * **Technical Task:** A granular engineering step (e.g., "Write unit test for `calculateConversion()`").
  * **Bug:** Unplanned defect resolution.

* **Build Track Outputs:**
  * **Module Version:** A versioned, quality-gated artifact of a specific module, continuously produced by CI/CD pipelines. Module Versions are *results* of engineering progress, not planned entities — they are routinely and continuously incremented. A Module Version with status `Released` has passed all quality gates and is available for deployment. Composite artifacts (like Product Version) may refer to constituent Module Versions using semver compatibility ranges rather than pinned versions.
    * *Status Lifecycle:* `Building` → `Released` (quality gates passed, available for deployment).
    * *Example:* `payments-service v2.3.3`, `fx-engine v1.8.1`.
  * **Product Version:** A verified, certified composition of compatible Module Versions — the Bill of Materials (BOM) for the product. A Product Version declares compatible version ranges for constituent modules (Declared BOM) and records the specific versions tested together (Resolved BOM). Like Module Versions, Product Versions are results of build and integration work, not planned entities.
    * *Declared BOM:* Compatible version ranges (e.g., `payments-service ^2.3.0`, `fx-engine ~1.8.0`).
    * *Resolved BOM:* Specific versions tested and certified together.
    * *Status Lifecycle:* `Assembling` → `Verified` (integration tests pass) → `Certified` (all quality gates, compliance, security).
    * *Example:* `Product v3.2.0` = {payments-service v2.3.3, fx-engine v1.8.1, merchant-portal v4.1.1}.

* **Monitoring Entities:**
  * **Build Monitoring:** Continuous tracking of build health (CI/CD pipeline), quality metrics (test coverage, defect rates, tech debt), velocity trends. Surfaces when quality degrades, when builds destabilize, when technical debt accumulates. Triggers: Bug creation, Maintenance Task, Release Planning adjustment. (e.g., "Monitor payments-service and fx-engine CI — alert on build failure or integration pass rate < 95%").



### Track 3: The Run Track (Stability & Operations)

* **Goal:** Plan deployments, ensure infrastructure readiness, and maintain SLA/uptime requirements in the Operational Dimension.
* **Primary Owner:** DevOps, Site Reliability Engineers (SRE).

* **Planning Entities:**
  * **Deployment Planning Task:** Work to plan a Module Version deployment — environments, rollout strategy, rollback plan, deployment windows. Deployment is tracked per-environment (a single Module Version may be deployed to staging, production-us, production-eu at different times). (e.g., "Plan payments-service v2.3.3 deployment: canary to 5% → 25% → 100% over 72 hours, PCI audit window avoidance").
  * **Capacity Planning Task:** Work to forecast infrastructure needs based on projected load from upcoming Customer Releases. (e.g., "Forecast FX microservice scaling needs: LATAM launch expected to 3x transaction volume").

* **Operational Entities:**
  * **Incident:** Unplanned service degradation (e.g., "FX API latency spiked to 5000ms").
  * **Change Request:** A scheduled production alteration (e.g., "Migrate Payment DB to larger instance").
  * **Maintenance Task:** Routine preventative work (e.g., "Rotate bank API vault secrets").
  * **Deployment:** The operational act of installing a specific Module Version into a specific environment. Deployments are tracked per-environment — a Module Version is not "deployed" in absolute terms; it is deployed *somewhere*. (e.g., "Deploy payments-service v2.3.3 to production-us").

* **Monitoring Entities:**
  * **System Monitoring:** Continuous tracking of infrastructure health, SLA/uptime metrics, capacity utilization, performance baselines. Surfaces when thresholds are breached, when capacity is strained, when SLAs are at risk. Triggers: Incident creation, Change Request, Capacity Planning adjustment. (e.g., "Monitor production-us API — alert on P95 latency > 300ms or availability < 99.9%").



### Track 4: The Win Track (Value Realization)

* **Goal:** Plan go-to-market and customer engagement, build reusable enablement assets, execute proactive and reactive customer/prospect work across the AAARRR lifecycle (Awareness, Acquisition, Activation, Retention, Revenue, Referral), and ensure the product achieves the Win Outcomes and Business KPIs defined in Dimension 2.
* **Primary Owner:** Customer Success, Product Marketing, Sales, Support.
* **PLG / self-service note:** For segments where the Product lever dominates (self-service onboarding, free trial, in-product expansion), the Win Track's role shifts from human execution to monitoring + exception-based intervention. Win Monitoring becomes the primary activity; human engagement is reserved for stuck or high-value accounts. The same engagement subtypes apply; the Build Track delivers the "Win" experience in-product.
* **Dim 2 Connection:** The Win Track is the operational arm of Dimension 2. Where Dim 2 defines *what winning looks like* (Win Outcomes, Business KPIs, Win Stakeholder roles, Achievement Levers), the Win Track does *the work to achieve it*. Initiatives carry embedded targets (like OKR Key Results) that Win Reviews assess. Feedback surfaces Delivery Frictions and Win Barriers as Signals.
* **Ecosystem & Extensibility (Dim 6):** When the product has deliberate API or extensibility surfaces, the Win Track captures ecosystem-oriented work: developer enablement (API docs, SDK guides, sandbox environments, developer training), developer and partner engagement (API POCs, integration workshops, developer community), API adoption monitoring and SLO compliance tracking, and Win Reviews that assess API adoption, developer satisfaction, and API Compatibility Contract compliance.
* **Operational Model:** The Win Track operates in **continuous flow (kanban)** — work items vary in duration (a POC: weeks; a campaign: months; a QBR: quarterly) and don't align to sprint boundaries. Planning is periodic but work item size is independent of planning cadence.
* **Initiative Alignment:** All Win Track work aligns to Initiatives, which declare a **Lever Mix** (from the Business Model's Lever Portfolio) with relative weights. An Initiative with lever mix Product 40% / GTM 25% / Sales Enablement 20% / CS 15% tells the Win Track what kinds of work it needs to plan, build, and execute.

The Win Track has seven entity categories: **Plan, Equip, Execute, Respond, Assess, Learn, and Monitor.**

#### Win Monitoring (Monitor — continuous vigilance)

Win Monitoring is continuous tracking of customer health (adoption, usage, NPS), revenue metrics (pipeline, NRR, churn signals), competitive intelligence, and Customer Promise fulfillment metrics. It sits between periodic Win Reviews and reactive Win Case / Win Engagement work — surfacing at-risk accounts, expansion opportunities, competitive threats, and promise gaps before they become crises. **Revenue monitoring** is included: tracking revenue metrics and surfacing signals when targets are missed, feeding Win Review and potentially triggering Retention or Expansion Engagement. Triggers: Win Engagement creation, Win Case escalation, Win Review preparation. (e.g., "Monitor LATAM Enterprise accounts — daily health and usage; alert on health drop > 15 points; weekly revenue report: NRR, pipeline, churn risk").

#### Win Planning (Plan — strategic preparation)

Win Planning is a parent entity with lever-specific subtypes. Each subtype plans a different kind of Win Track work, aligned to the lever it activates.

  * **Customer Release Planning:** Work to coordinate the market delivery of a Customer Release — segment sequencing, market readiness assessment, Win Stakeholder preparation, coordination with Build Track's Release Planning. Distinct from Build Track's Release Planning Task (which scopes technical content); Customer Release Planning is concerned with *how the release reaches the market*. (e.g., "Plan LATAM Expansion market delivery: LATAM Enterprise first (Activation Win Outcome: live within 30 days), US Mid-Market 30 days later").
  * **GTM Planning:** Work to prepare launch messaging, pricing communication, partnership execution, marketing campaigns, and channel strategy for a Customer Release or Initiative. (e.g., "Prepare LATAM Expansion launch: sales deck targeting CFO Win Outcome, pricing page for Enterprise Volume Plan, LATAM partner co-marketing").
  * **Sales Enablement Planning:** Work to plan competitive programs, demo environment programs, sales training, and enablement asset creation. (e.g., "Plan Q3 LATAM sales enablement: competitive battlecard vs. CompetitorX, LATAM demo environment, Pre-Sales regulatory training").
  * **Customer Success Planning:** Work to plan onboarding programs, retention programs, expansion programs, advocacy programs, and customer education/certification programs. (e.g., "Plan LATAM CS program: onboarding playbook, health score model for LATAM Enterprise, QBR template, customer advocacy workshop, LATAM API certification program").
  * **Engagement Planning:** Work to plan which prospects, customers, segments, and partners to engage, sequencing, and resource allocation. Includes partner prioritization and sequencing when the product has a channel/partner model. (e.g., "Q3 Pre-sales prioritization: POC for 5 LATAM Enterprise prospects; QBR schedule for 12 at-risk LATAM accounts; LATAM feature webinar series; partner onboarding sequence for 3 LATAM bank partners").

All Win Planning subtypes carry: Initiative(s) advanced, lever(s) activated, Win Outcome(s) targeted, Customer Segment(s), planning cycle reference.

#### Win Enablement (Equip — reusable asset/program creation)

Win Enablement creates reusable assets and programs that Win Stakeholders use across many engagements. Enablement is **one-to-many** — one battlecard serves fifty deals, one onboarding playbook serves all customers in a segment.

  * **GTM Enablement:** Marketing collateral, pricing tools, partner materials, campaign assets, positioning documents. (e.g., "Create LATAM Enterprise competitive positioning deck", "Build partner co-marketing toolkit for LATAM channel").
  * **Sales Enablement Asset:** Competitive battlecards, demo environments, ROI calculators, segment-specific sales playbooks, sales training materials. (e.g., "Build LATAM competitive battlecard vs. CompetitorX", "Create LATAM demo environment with BRL/MXN sandbox data").
  * **CS Enablement:** Onboarding playbooks, health score models, QBR templates, expansion frameworks, advocacy program materials, and customer education assets (training materials, certification curricula, knowledge bases). Advocacy encompasses both referral/case-study and customer education. (e.g., "Create LATAM Enterprise onboarding playbook", "Design health score model for LATAM Enterprise accounts", "LATAM API integration certification program").
  * **Partner Enablement:** Partner demo environments, co-marketing kits, partner training, certification programs, partner playbooks. Equips channel partners (resellers, integrators, referral partners) — distinct from Sales Enablement, which equips internal teams. (e.g., "LATAM bank partner certification program", "LATAM fintech co-marketing kit").

All Win Enablement subtypes carry: lever, AAARRR stage(s) supported, Win Stakeholder(s) who will use the asset, output/deliverable description.
Status lifecycle: `Planned` → `In Progress` → `Available` → `Retired`.

#### Win Engagement (Execute — proactive prospect/customer/segment work)

Win Engagement is the proactive, customer-facing execution work of the Win Track. Engagements operate at two granularities: **account-level** (one-to-one, for specific prospects or customers) and **segment-level** (one-to-segment, for webinars, workshops, campaigns).

  * **Pre-sales Engagement:** Account-level work to advance a specific prospect through Acquisition — POC, custom demo, technical evaluation, RFP response, solution architecture. References CRM Deal/Opportunity (external). (e.g., "Run POC for Prospect X: LATAM Enterprise, SAP integration, 3-week timeline").
  * **Implementation / Onboarding:** Account-level work to integrate a specific customer — configuration, data migration, integration, go-live. Directly affects Activation Win Outcomes and may surface Delivery Frictions. (e.g., "Onboard Customer Y: Connect SAP ERP to Cross-Border API, target go-live within 30 days").
  * **Retention Engagement:** Account-level work to maintain and strengthen a customer relationship — health interventions, QBR preparation, renewal management. (e.g., "Health intervention for Customer Z: usage dropped 40%, schedule executive check-in").
  * **Expansion Engagement:** Account-level work to grow account value — upsell proposals, cross-sell campaigns, account planning. (e.g., "Upsell proposal for Customer W: add batch payout processing, estimated $50K ACV increase").
  * **Segment Engagement:** Segment-level work to engage a group of prospects or customers — awareness campaigns, feature webinars, advocacy workshops, community events, capability enablement sessions, and customer training/certification delivery. Applies to both pre-sale (awareness campaigns) and post-sale (feature adoption webinars, customer workshops, training sessions). Advocacy includes customer education. (e.g., "LATAM Enterprise feature webinar: batch payout processing launch", "LATAM CFO roundtable: cross-border payment optimization", "LATAM API certification training — cohort 3").
  * **Partner Engagement:** Account-level work directed at a specific partner — partner onboarding, co-selling, partner account management, partner pipeline management. References external PRM (Partner Relationship Management) records. Distinct from customer-facing engagement; the "account" is the partner. (e.g., "Onboard Banco Regional as LATAM channel partner — co-marketing, certification, Q3 pipeline target").
  * **Revenue Operations Engagement:** Account-level, customer-facing work to ensure revenue is realized — invoicing/billing communication, collections follow-up, renewal processing, revenue recognition coordination with Finance. Advances Revenue Win Outcomes; distinct from Expansion Engagement (upsell/cross-sell). Billing disputes are Win Case (Complaint). (e.g., "Collections follow-up for Customer W — invoice 60 days overdue; renewal processing for Customer Z — contract renewal Q3").

All Win Engagements carry: AAARRR stage, Customer Segment, Win Outcome(s) advanced, Win Stakeholder(s) performing the work, Initiative alignment.

#### Win Case (Respond — reactive, customer-initiated work)

Win Case captures the reactive, responsive work of Win Teams — queries, requests, complaints, and escalations initiated by customers and prospects. Win Cases are distinct from Run Track entities (Incident, Change Request) which are infrastructure/system-facing. Win Cases are customer-facing.

  * **Win Case types:** `Query` (customer seeking information), `Service Request` (customer asking for an action), `Complaint` (customer expressing dissatisfaction — tests Service Commitments from Dim 3), `Escalation` (issue requiring elevated attention).

Win Cases connect to Dim 2 and Dim 3: Service Commitments (Dim 3) are tested by Win Case response/resolution quality. Cost-to-Serve (Business KPI, Dim 2) is measured against Win Case volume and effort. Win Case patterns reveal Delivery Frictions and Win Barriers. Win Stakeholders (Support Engineers, CS Managers) endure friction in reactive work.

Win Case patterns are assessed during Win Reviews, producing Feedback that may become Signals. Initiative targets like CSAT and first-response time can only be assessed against reactive work quality.

#### Win Review (Assess — structured assessment)

Win Review is a structured assessment activity — the Win Track's equivalent of Deliberation in the Discovery Track. Win Reviews assess both proactive work (engagements, enablement effectiveness) and reactive work (Win Case patterns, support quality) across **two dimensions**: vendor success (Win Outcomes, Dim 2) and customer promise fulfillment (Customer Promises, Dim 3).

  * **Win Review types:** QBR (Quarterly Business Review), Win/Loss Analysis, Post-Implementation Review, Campaign/Program Review, Case Pattern Review, Adoption Review.

Win Review produces two outputs:
1. **Feedback** (qualitative observations, patterns, insights) — an artifact that may be promoted to a Signal when it warrants Discovery investigation. May surface both Win Outcome gaps and Customer Promise failures.
2. **Target progress updates** (quantitative assessment against Initiative embedded targets) — updates the Initiative's target tracking, analogous to updating OKR Key Result progress. May include Customer Value Metric status alongside Business KPI status.

#### Feedback (Learn — transitional artifact)

Feedback is a structured observation record produced by Win Reviews. It is an **artifact**, not a work item — you do a Win Review and *produce* Feedback, just as you do a Deliberation and *produce* a PDR. Feedback captures customer observations, Win Stakeholder observations, and pattern analyses.

Feedback is a **transitional artifact**: born in the Win Track, consumed by the Discovery Track when promoted to a Signal. Not every observation becomes a Signal — Feedback is the raw, structured record; Signal is the qualified, investigation-worthy version. Feedback that doesn't warrant a Signal is archived with rationale.



---

### Cross-Track Relationship: Customer Release Lifecycle

A **Customer Release** (Definition Model, Dimension 1) is a cross-cutting entity whose lifecycle spans multiple tracks:

| Track | Contribution |
|---|---|
| **Discovery Track** | Strategic planning defines Customer Releases as part of Initiative scoping |
| **Build Track** | Release Planning scopes which PSDs/Initiatives are included; build work produces Module Versions and Product Versions |
| **Run Track** | Deployment Planning ensures all required Module Versions are deployed to target environments |
| **Win Track** | Customer Release Planning coordinates market delivery; GTM Planning prepares launch messaging; the Win Track **activates** the Customer Release through engagement, enablement, and reactive support |

A Customer Release becomes `Launched` when all required Module Versions are deployed (Run Track confirms) AND the business activates the release (Win Track executes Customer Release Planning and GTM Planning).

---
