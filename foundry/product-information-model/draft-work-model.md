
## PART II: THE WORK MODEL (THE 5 TRACKS)

> **Deployment/versioning semantics:** DR-036 supersedes DR-026–029 for operational use. Versioning: Component Version → System Version → Product Version. Deployment: System Deployment Specification, Product Deployment Specification.

While the 9 Dimensions define the *Definition Model* of the product, the 5 Tracks define the *motion*. This is how Maker Roles (PMs, Devs, CS, Process Leads) organize their daily work to mutate the 9 Dimensions — and to evolve the Work Model and Operating Model themselves. Each track owns its own planning work alongside its core activities.

> **Scope Boundary Note:** The Work Model deliberately describes **what work exists** — entities, artifacts, and state transitions. It does NOT cover:
>
> - **Coordination patterns** — ceremonies, cadences, rituals, decision-making rhythms (e.g., Sprint Planning, Quarterly Business Review, Signal Review ceremonies)
> - **Organizational design** — roles, team structures, skills profiles, training, tools, and resource allocation
> - **Capacity and scheduling** — how much work fits in a period, who does it, velocity tracking
> - **Guidance content** — playbooks, procedures, and templates for executing work (the *structure* of guidance is a Work Model concern; the *content* is an Operating Model concern)
>
> These concerns belong to the **Operating Model** — the third model in the UPIM architecture, sitting above the Work Model. The Operating Model covers both coordination and organizational design as entangled facets of how the org executes. It depends on the Work Model (you must know what work entities exist before you can design ceremonies and roles around them) but is a separate modeling concern. See the PIM Architecture README for the full three-model stack.
>
> **Work Execution Framework:** The Work Model *does* capture three execution dimensions for each work entity: (1) what artifacts it produces, (2) its Definition of Done (entry/exit criteria, artifact checklist), and (3) references to Operating Model guidance. See `draft-work-execution-framework.md` for the framework, artifact taxonomy, artifact type catalog, and cross-track inventory.
>
> **Self-evolution:** The Work Model explicitly accounts for its own evolution through **Track 5: Evolve**. This is the only track whose outputs directly modify both the Work Model (entity/artifact definitions, DoD criteria) and the Operating Model (guidance content, ceremonies, roles). A model that cannot evolve is dead; Track 5 ensures the model stays alive.

### Track 1: The Discovery Track (Learning)

* **Goal:** Set strategic direction, prioritize Signals for discovery, organize cross-functional Discovery Cases, explore product-relevant questions and Signals, validate hypotheses through research, experiments, prototypes, and deliberation, create Product Intent from Go/Pivot product decisions, request Build evidence when needed, and refine accepted intent through PSD(s).
* **Primary Owner:** Product Management for product alignment; Discovery work may be originated and performed by Product, UX, Engineering, Architecture, QA, Run, Win, Governance, executives, and authorized agents.
* **Input:** Strategic Themes and Objectives from business strategy; optional Signals (Problems, Needs, Opportunities); Ideas requiring validation; cross-functional discovery questions from any function (PM judgment, technical ideas, architecture concerns, operational insights, customer commitments, release learnings) via Discovery Case.
* **Output:** Discovery produces four types of outputs:
  1. **PDR** — captures any significant decision affecting any dimension. A PDR may create Product Intent(s), justify PSDs (engineering changes), and/or trigger Definition Model updates (knowledge/model changes).
  2. **Product Intent** — the hybrid bridge item created or updated by Go/Pivot decisions, carrying committed product direction into ACE Workspace execution.
  3. **PSD(s)** — module-scoped specifications that refine Product Intent through Specification Tasks.
  4. **Definition Model updates** — evolution of entities in Dims 2–9 (via Modeling Task). Examples: new Customer Segments, refined Value Propositions, updated Value Streams, new Capabilities.
  Additionally: Objectives, Initiatives, Customer Release Intent definitions (Dimension 1); Idea status changes — either advanced to `Validated` (triggering PDR/Product Intent) or moved to `Killed`.

* **Orchestration Entities:**
  * **Discovery Case:** Cross-functional orchestration container for a bounded discovery investigation. Coordinates sub-work (Signal Exploration, Deliberation, Research, Experiment, Prototype/Spike, Modeling Task). Signal-optional. May request Build evidence through Discovery Support Product Intent. Closes when investigation is concluded — producing PDR(s), Ideas, Modeling Tasks, Product Intent(s), or routing outcomes. (e.g., "Discovery Case: assess event-sourcing for audit trail — origin: Architecture Concern, no Signal filed")

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
  * **Specification Task:** A granular PSD-authoring action that refines Product Intent — scoping modules, writing acceptance criteria, coordinating feasibility with engineering, decomposing into shippable increments. Represents the substantial work between accepted Product Intent and approved PSD(s); it consumes intent, it does not originate it (e.g., "Define webhook payload contract with Platform team", "Write acceptance criteria for FX module").
  * **Modeling Task:** Work to evolve Definition Model entities in any dimension (Dims 2–9) based on discovery findings. Modeling Tasks produce updates to the product's self-description — customer segments, buyer personas, business outcomes, customer promises, value streams, capabilities, data domains, and more. Dim 5 (Technical & Architectural) modeling includes Systems, Components, Dependencies, Interaction Flows, and Technical Knowledge Base assessments. Dim 6 (Ecosystem & Extensibility) modeling includes Developer Personas, Programmatic User Personas, API Modules, API Operations and SLOs, and API Compatibility Contracts. A Modeling Task may be triggered by a PDR (a decision affecting a dimension) or by ongoing product knowledge maintenance. (e.g., "Define LATAM AP Clerk user persona", "Map Cross-Border Payout Processing value stream", "Design LATAM pricing tier structure", "Define Developer Persona", "Design API Module with operations and SLOs", "Model API Compatibility Contract for Payments API v2", "Document payments-service System with Module mapping and tech stack", "Assess payments-service Technical Knowledge Base").
  * **Note on ADR production:** Deliberation may produce Architecture Decision Records (ADRs, Dim 5) in addition to or instead of PDRs (Dim 1). When the Deliberation scope is a technical/architectural question ("should we adopt event sourcing?"), the output is an ADR. When the scope is a product question that has architectural implications, both a PDR and one or more ADRs may be produced. See DR-024.
  * **Note on ODR production:** Deliberation may also produce Operations Decision Records (ODRs, Dim 7) for strategic infrastructure and operational decisions. When the Deliberation scope is an operational question ("which cloud provider for LATAM?", "what data archival policy?"), the output is an ODR. A single product decision (PDR) may cascade to both ADRs and ODRs: "Go on LATAM" → ADR (architecture for LATAM services) + ODR (LGPD compliance hosting, data residency). See DR-025.

* **Monitoring Entities:**
  * **Signal Monitoring:** Continuous tracking of signal pipeline health, trend analysis across Signals, discovery velocity metrics. Surfaces when signal backlog grows, when themes shift, when discovery capacity is mismatched. Triggers: Prioritization Task re-evaluation, new Signal creation, Deliberation scheduling. (e.g., "Monitor LATAM Initiative signal pipeline — daily scan; alert when backlog > 20 or Signal aged > 60 days").



### Track 2: The Build Track (Construction)

* **Goal:** Plan releases and iterations, take validated PSDs, decompose them into Module-scoped Epics and System-scoped Technical Tasks, and continuously produce Component Versions, System Versions, and Product Versions through a three-tier versioning model (DR-036).
* **Primary Owner:** Tech Lead, Developers, QA.

* **Primary orchestration item:** **Product Intent**. Build Track does not independently orchestrate Epics, PSDs, ADRs, bugs, refactors, or technical tasks as top-level items. Those are subordinate to Product Intent or to another Track's orchestration item.

> **Build boundary:** Product Intent entering Build does not necessarily mean customer-committed delivery. Delivery Product Intents may ship to customers; Discovery Support, Technical Validation, Internal / Enabling, Operational Enablement, and Release Renewal intents may enter Build to produce evidence, internal capability, operational readiness, or follow-up learning.
>
> **Architecture/refactoring rule:** Architecture and refactoring work must fit an existing Product Intent, become Product Intent through Discovery Case and product decision, route to Run/Evolve if operational or process-oriented, or remain local engineering hygiene if small and internal.

> **Work Entities vs. Work Artifacts:** The Build Track distinguishes between *work entities* (work to be done — Epic, Story, Technical Task, Bug, Integration Epic, Integration Story) and *work artifacts* (things produced by work — Component Version, System Version, Product Version, ADR, Technical Debt Item). Work entities are planned, assigned, and tracked through status lifecycles. Work artifacts are *results* — they emerge from completed work.
>
> **Module scope vs. System scope:** Epics and Stories are Module-scoped (Dim 8) — they speak the functional language ("Build FX Rate Locking" for the FX Module). Technical Tasks are System/Component-scoped (Dim 5) — they speak the engineering language ("Implement gRPC endpoint in fx-service"). This reflects reality: PMs and Tech Leads plan in Module terms; developers implement in System terms. The Module-to-System many-to-many mapping means a single Story may spawn Technical Tasks in multiple Systems. See DR-026.

* **Planning Entities:**
  * **Release Planning Task:** Work to scope realization of a Customer Release Intent — which PSDs/Product Intents/Initiatives are included, timeline, milestones, team allocation. Release Planning decomposes PSDs into Epics (one per affected Module) and identifies Integration Epics (cross-System integration work). (e.g., "Plan Customer Release Intent 'LATAM Expansion': scope to LATAM initiative PSDs, target mid-Q3 ship date; identify 5 Epics across 3 Modules, 2 Integration Epics").
  * **Milestone Planning Task:** Work to define checkpoints within realization of a Customer Release Intent with clear entry/exit criteria, cross-Epic dependency gating, and integration verification gates. (e.g., "Define 'API Complete' milestone — all cross-border endpoints passing integration tests; 'Integration Verified' milestone — Payments and FX System Versions Released").
  * **Iteration Planning Task:** Work to assign Stories, Integration Stories, and Technical Tasks to a time-boxed iteration, balance capacity, and identify cross-System dependencies. (e.g., "Sprint 14 planning: allocate FX rate-lock Stories, assign Technical Tasks to fx-service and payments-service developers").

* **Work Entities (work to be done):**
  * **Epic:** A large, committed body of work decomposed from a PSD, scoped to a single Module (Dim 8). A cross-Module PSD results in multiple Epics — one per affected Module. (e.g., "Build Real-Time FX Rate Locking" for the FX Module).
  * **Story:** A unit of work within an Epic, Module-scoped (Dim 8). Not necessarily user-facing — can be functional, technical, or enablement. Implemented by Technical Tasks. (e.g., "Lock FX rate for 24 hours", "Set up Kafka consumer for payment events"). *Renamed from User Story.*
  * **Technical Task:** A granular engineering step scoped to a System (Dim 5) and optionally a Component. The most granular work entity. Build Track Technical Tasks serve Stories and Integration Stories. (e.g., "Implement gRPC GetRate endpoint in fx-service", "Add Kafka consumer in payments-service"). *Technical Task is a per-track concept — the Run Track has its own Technical Tasks serving Run Stories; the Win Track may have Technical Tasks for win engineering automation.*
  * **Bug:** Unplanned defect resolution with **provenance**: `Build` (discovered during development), `Run` (originated from Incident Response Task or Post-Incident Review, Track 3 — links back to Incident artifact), or `Win` (originated from Win Case, Track 4). Run-provenance Bugs may carry a `Workaround` field when the incident was resolved with a temporary fix, serving as the Known Error registry. P0 Bugs (typically Run-provenance from SEV-0/SEV-1 Incidents) signal sprint-boundary bypass and eligibility for the Emergency quality gate profile on the resulting System Version; deferred gates are tracked via the Bug's `Deferred Gate Obligation` field (DR-031). Provenance enables cross-Track traceability.
  * **Integration Epic:** Cross-System integration work, emerging from Release Planning when PSD-derived Epics require their Systems to interoperate. References the PSD-derived Epic(s)/Story(ies) being integrated and validates Interaction Flows (Dim 5). (e.g., "Integrate Payments↔FX Rate Locking Flow").
  * **Integration Story:** A unit of integration work within an Integration Epic. Produces integration contracts (API schemas, event schemas) and integration test suites. (e.g., "Validate gRPC contract: payments-service → fx-service GetRate").
  * **Design Deliberation:** A collaborative technical discussion during build work that produces ADR(s) (Dim 5). Narrower scope than Discovery Track Deliberation — focused on implementation-time architectural questions. (e.g., "gRPC vs REST for fx-service ↔ payments-service" → ADR-031).

* **Work Artifacts (things produced by work):**
  * **Component Version:** A versioned, quality-gated build artifact of a single Component (Dim 5) — container image, Lambda package, etc. Produced continuously by CI/CD. The **atomic build tier** (DR-036). Not independently deployed to production.
    * *Status Lifecycle:* `Building` → `Released`.
    * *Example:* `payments-service v2.3.3`, `fx-engine v1.8.1`.
  * **System Version:** A **sealed, immutable BOM** of Component Versions for a System (Dim 5). The **operational deployment unit** — what SRE deploys as a whole. Component-integration verified within the System boundary. Produced by Build Track (product and operational Systems alike).
    * *Status Lifecycle:* `Assembling` → `Verified` → `Released`.
    * *Example:* `payments-system v3.1.0` = {payments-service v2.3.3, payment-reconciler v1.4.0, payment-notification-worker v1.2.0}.
  * **Product Version:** A certified composition of **System Versions** (flat BOM) for the product. Cross-System integration verification and certification. The **ubiquitous language** across teams and customers.
    * *Status Lifecycle:* `Assembling` → `Verified` → `Certified`.
    * *Example:* `Product v4.0.0` = {payments-system v3.1.0, fx-system v2.0.1, compliance-system v3.2.0, payments-monitoring-system v1.2.0}.
  * **Architecture Decision Record (ADR):** Architectural decisions produced by Design Deliberation during build work. Both Discovery-originated ADRs (from Deliberation) and Build-originated ADRs (from Design Deliberation) produce the same Dim 5 entity. See DR-024.
  * **Technical Debt Item:** A documented instance of accumulated technical debt. When prioritized, resolved via an Epic (if significant) or a Story (if contained). (e.g., "payments-service: synchronous bank calls should be async" → Epic "Async Bank Integration").

* **Monitoring Entities:**
  * **Build Monitoring:** Continuous tracking of build health (CI/CD pipeline), quality metrics (test coverage, defect rates, tech debt), velocity trends. Surfaces when quality degrades, when builds destabilize, when technical debt accumulates. Triggers: Bug creation, Technical Debt Item creation, Release Planning adjustment. (e.g., "Monitor payments-service and fx-service CI — alert on build failure or integration pass rate < 95%").



### Track 3: The Run Track (Stability & Operations)

* **Goal:** Plan deployments, ensure infrastructure readiness, maintain SLA/uptime requirements in the Operational Dimension (Dim 7), manage tenant lifecycle within Deployment Environments, and **engineer operational Systems** (via Build Track) that are versioned and deployed like product Systems.
* **Primary Owner:** DevOps, Site Reliability Engineers (SRE), Platform Engineering.
* **Dim 7 Connection:** The Run Track is the operational arm of Dimension 7. Where Dim 7 defines *what the operational reality needs to be* (Infrastructure Model, Deployment Environments, Operational Targets, Operational Readiness), the Run Track does *the work to maintain and manage it* — deploying System Versions, managing tenants, responding to incidents, and monitoring system health. Operational Pains (Dim 7) surface through Run Track experience and become Signals (Dim 1).

> **Run Track as engineering track (DR-036).** Operational Systems (probes, reconcilers, monitoring agents) are ordinary Dim 5 Systems in the Product Specification. Run Epics/Stories produce Component and System Versions through the **Build Track** pipeline. Run Deliberations produce ODRs (Dim 7), not ADRs (Dim 5). Deployment uses System Deployment Specifications and Product Deployment Specifications — no separate Package layer.

* **Planning Entities:**
  * **Deployment Plan:** A deliberation activity where the Run team scopes a rollout — determining which System or Product deployments advance through Deployment Trains and Stations, identifying verification and maintenance prerequisites, and producing Deployment Planning Tasks. Governed by a Change Request. (e.g., "Deployment Plan: Deploy Product v4.0.0 through PCI Regulated Train — create Product Deployment Specification, verification tasks, drill task").
  * **Deployment Planning Task:** Work to plan a deployment and **produce Deployment Specifications** (System Deployment Specification or Product Deployment Specification) for target environments. Governed by a Deployment Plan. (e.g., "Plan payments-system v3.1.0 deployment to production-latam: produce System Deployment Specification sds-1.2, migration script, validation smoke test, rollback script").
  * **Deployment Drill Task:** An optional rehearsal of a Deployment Plan in a non-production environment. (e.g., "Rehearse Product Deployment Specification pds-1.0 procedure in staging-drill environment").
  * **Capacity Planning Task:** Work to forecast infrastructure needs based on projected load from upcoming Customer Release Intents. (e.g., "Forecast FX microservice scaling needs: LATAM launch expected to 3x transaction volume").

* **Engineering Entities (Run Track as engineering track):**
  * **Run Epic:** A large body of operational engineering work scoped to a single Module (Dim 8). Produces operational System Versions via Build Track. Triggered by Operational Readiness gaps, Post-Incident Reviews, incident patterns, or operational improvement initiatives. (e.g., "Build comprehensive health monitoring for Payments Module").
  * **Run Story:** A unit of operational engineering work within a Run Epic. Describes a functional increment of operational capability. Implemented by Run Track Technical Tasks scoped to operational Systems (Dim 5). (e.g., "Create synthetic payment probe for BRL corridor end-to-end path verification").
  * **Technical Task (Run Track):** A granular engineering step scoped to an operational System (Dim 5). Serves Run Stories. Same entity structure as Build Track Technical Tasks but with distinct track ownership — each engineering track owns its own Technical Tasks.

* **Incident Management Entities:**
  * **Incident (Artifact):** A durable observation record of unplanned service degradation — what happened, not what to do about it. Produced by System Monitoring (alerts), operator observations, or corresponding to Win Case complaints. Severity uses SEV-0 through SEV-4. Carries structured fields for correlation (Parent Incident, Related Incidents), causation (Caused By — linking to a Deployment or Change Request), and SLA tracking (SLA Breach, Response Time, Resolution Time). Incidents inform Run Track planning tasks (Deployment Planning, Capacity Planning, Run Epic scoping) and feed Definition Model assessment (Customer Value Metrics, Operational Targets, Operational Readiness). (e.g., "INC-2026-0847: SEV-1, FX API latency spiked to 5000ms, Production US-East, SLA breach: sub-200ms P95 latency").
  * **Incident Response Task:** The primary work entity for triaging, investigating, and resolving an Incident. DoD is "service restored to SLO-compliant state" — root cause fix is downstream (Bug, Run Epic, Signal). Captures escalation levels, workaround applied, and resolution summary. May produce Bugs (provenance: Run), Signals, and emergency Change Requests. (e.g., "Respond to INC-2026-0847: L2 escalation to FX Team; FX cache rebuilt; latency restored to P95 < 200ms").
  * **Post-Incident Review:** A standalone deliberation entity — structured collaborative assessment after incident resolution. Produces Post-Incident Report (assessment artifact) and routes corrective actions to appropriate tracks: Bugs (Track 2), Run Epics (Track 3), Signals (Track 1), ODRs (Dim 7), Evolve Findings (Track 5). SEV-0, SEV-1, and SEV-2 incidents require PIR; the Operating Model may adjust this threshold. (e.g., "PIR: Database cluster failover — root cause: connection pool reconnect timeout; corrective: Bug for pool logic, Run Epic for AZ failover automation, ODR for multi-AZ requirement").
  * **Customer Communication Task:** Run Track work entity for incident communication — status page updates, affected-tenant notifications, resolution summaries. Runs in parallel with Incident Response Task. Run Track owns incident communication because SRE/DevOps has the technical context; Win Track consumes summarized views. (e.g., "Communicate INC-2026-0849: status page updates at 14:30, 14:45, 15:10, 15:30; tenant notification to all LATAM tenants; RCA committed within 48h").

* **Operational Entities:**
  * **Change Request:** A formal change management envelope governing deployment-related changes, scoped to System Deployment or Product Deployment and a Deployment Train (Dim 7) or Station. Three types: Standard, Emergency-Technical, Emergency-Business. Completed when all Deployment Tasks AND Verification Tasks pass. (e.g., "CR-2026-0142: Standard, Product Deployment, PCI Regulated Train, deploy Product v4.0.0").
  * **Maintenance Task:** Routine preventative work (e.g., "Rotate bank API vault secrets").
  * **Deployment (Artifact):** A durable record that a Deployment Specification was applied to an environment — produced by a Deployment Task. Status lifecycle: `Active` → `Superseded` → `Rolled Back`. (e.g., "payments-system sds-1.2 applied to production-latam at 2026-02-12T14:30:00Z — Status: Active").
  * **Deployment Task:** The work of applying a System Deployment Specification or Product Deployment Specification to an environment. Produces a Deployment record. (e.g., "Apply payments-system System Deployment Specification sds-1.2 to production-latam").
  * **Verification Task:** Post-deployment verification work. Required for Change Request closure. (e.g., "SLA Verification — payments-system sds-1.2 → production-latam: P95 latency < 300ms for 24h").
  * **Tenant:** A logical isolation unit within a Deployment Environment (Dim 7), belonging to a Customer (instance of Customer Segment, Dim 3), with a customer-facing purpose. Tenants are provisioned, configured, monitored, scaled, and eventually decommissioned as Run Track operational work. A single Customer may have multiple Tenants in the same environment (e.g., one for production use, one for UAT). The Deployment Environment defines the infrastructure; the Tenant defines the customer's logical slice within it. (e.g., "Provision Tenant 'itau-prod' in Production LATAM for Banco Itaú — purpose: Production, isolation: dedicated schema, SLO tier: Enterprise").
    * *Tenant Purpose:* `Production` / `UAT` / `Sandbox` / `Trial` / `DR` — the customer-facing purpose, distinct from the environment's vendor purpose.
    * *Status Lifecycle:* `Requested` → `Provisioning` → `Active` → `Suspended` → `Decommissioning` → `Retired`.

* **Work Artifacts (things produced by Run Track work):**
  * **System Deployment Specification:** Environment-specific deployment specification for a sealed **System Version**. Resource sizing, env vars, runtime mappings, scripts. Versioned independently from System Version. (e.g., "payments-system sds-1.2 → production-latam").
  * **Product Deployment Specification:** Environment-specific specification for a certified **Product Version**. Composes System Deployment Specifications; deployment ordering; cross-System scripts. (e.g., "Product Deployment Specification pds-1.0 → production-latam").
  * **Post-Incident Report:** Assessment artifact produced by Post-Incident Review — captures timeline reconstruction, final root cause analysis, contributing factors, quantified impact, corrective actions with owners and deadlines, and lessons learned. The durable knowledge artifact that ensures incident learning is preserved and actionable.
  * **Operations Decision Record (ODR):** Operational decisions that emerge during Run Track work — deployment strategy changes driven by incident patterns, data governance decisions driven by regulatory changes, cloud service selection driven by operational experience, capacity and scaling decisions driven by performance data — are recorded as ODRs (Dim 7). Run-originated ODRs arise from operational experience (Run Deliberations within Run Epics). Both Discovery and Run ODRs produce the same Dim 7 entity. See DR-025.

* **Monitoring Entities:**
  * **System Monitoring:** Continuous tracking of operational health — Systems, deployed Product Versions, Tenant health, cross-System wiring. Triggers: Incident creation, Change Request, Capacity Planning adjustment, Run Epic creation.
  * **Run Engineering Monitoring:** Continuous tracking of Run Track engineering health — CI/CD pipeline health for operational systems, quality metrics, and Run Epic/Run Story velocity trends. The Run Track's counterpart to Build Monitoring (Track 2). Distinct from System Monitoring, which watches operational health of running systems. (e.g., "Monitor payments-healthcheck CI — alert on build failure or test coverage drop below 85%; weekly Run Epic velocity report").



### Track 4: The Win Track (Value Realization)

* **Goal:** Plan go-to-market and customer engagement, build reusable enablement assets, execute proactive and reactive customer/prospect work across the AAARRR lifecycle (Awareness, Acquisition, Activation, Retention, Revenue, Referral), and ensure the product achieves the Win Outcomes and Business KPIs defined in Dimension 2.
* **Primary Owner:** Customer Success, Product Marketing, Sales, Support.
* **PLG / self-service note:** For segments where the Product lever dominates (self-service onboarding, free trial, in-product expansion), the Win Track's role shifts from human execution to monitoring + exception-based intervention. Win Monitoring becomes the primary activity; human engagement is reserved for stuck or high-value accounts. The same engagement subtypes apply; the Build Track delivers the "Win" experience in-product.
* **Dim 2 Connection:** The Win Track is the operational arm of Dimension 2. Where Dim 2 defines *what winning looks like* (Win Outcomes, Business KPIs, Win Stakeholder roles, Achievement Levers), the Win Track does *the work to achieve it*. Initiatives carry embedded targets (like OKR Key Results) that Win Reviews assess. Feedback surfaces Delivery Frictions and Win Barriers as Signals.
* **Ecosystem & Extensibility (Dim 6):** When the product has deliberate API or extensibility surfaces, the Win Track captures ecosystem-oriented work: developer enablement (API docs, SDK guides, sandbox environments, developer training), developer and partner engagement (API POCs, integration workshops, developer community), API adoption monitoring and SLO compliance tracking, and Win Reviews that assess API adoption, developer satisfaction, and API Compatibility Contract compliance.
* **Operational Model:** The Win Track operates in **continuous flow (kanban)** — work items vary in duration (a POC: weeks; a campaign: months; a QBR: quarterly) and don't align to sprint boundaries. Planning is periodic but work item size is independent of planning cadence.
* **Initiative Alignment:** All Win Track work aligns to Initiatives, which declare a **Lever Mix** (from the Business Model's Lever Portfolio) with relative weights. An Initiative with lever mix Product 40% / GTM 25% / Sales Enablement 20% / CS 15% tells the Win Track what kinds of work it needs to plan, build, and execute.

The Win Track has seven entity categories: **Plan, Equip, Execute, Respond, Assess, Learn, and Monitor.** The Respond category begins with the **FIR (First Information Report)** — the universal intake entity that is upstream of all reactive Win Track work.

#### Win Monitoring (Monitor — continuous vigilance)

Win Monitoring is continuous tracking of customer health (adoption, usage, NPS), revenue metrics (pipeline, NRR, churn signals), competitive intelligence, and Customer Promise fulfillment metrics. It sits between periodic Win Reviews and reactive Win Case / Win Activity work — surfacing at-risk accounts, expansion opportunities, competitive threats, and promise gaps before they become crises. **Revenue monitoring** is included: tracking revenue metrics and surfacing signals when targets are missed, feeding Win Review and potentially triggering Retention or Expansion Engagement. Triggers: Win Activity creation, Win Case escalation, Win Review preparation. (e.g., "Monitor LATAM Enterprise accounts — daily health and usage; alert on health drop > 15 points; weekly revenue report: NRR, pipeline, churn risk").

#### Win Planning (Plan — strategic preparation)

Win Planning is a parent entity with lever-specific subtypes. Each subtype plans a different kind of Win Track work, aligned to the lever it activates.

  * **Customer Release Planning:** Work to coordinate the market delivery that realizes a Customer Release Intent — segment sequencing, market readiness assessment, Win Stakeholder preparation, coordination with Build Track's Release Planning. Distinct from Build Track's Release Planning Task (which scopes technical content); Customer Release Planning is concerned with *how the release reaches the market*. (e.g., "Plan LATAM Expansion market delivery: LATAM Enterprise first (Activation Win Outcome: live within 30 days), US Mid-Market 30 days later").
  * **GTM Planning:** Work to prepare launch messaging, pricing communication, partnership execution, marketing campaigns, and channel strategy for a Customer Release Intent or Initiative. (e.g., "Prepare LATAM Expansion launch: sales deck targeting CFO Win Outcome, pricing page for Enterprise Volume Plan, LATAM partner co-marketing").
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

#### Win Activity (Execute — proactive prospect/customer/segment work)

Win Activity is the proactive, customer-facing execution work of the Win Track. Engagements operate at two granularities: **account-level** (one-to-one, for specific prospects or customers) and **segment-level** (one-to-segment, for webinars, workshops, campaigns).

  * **Pre-sales Engagement:** Account-level work to advance a specific prospect through Acquisition — POC, custom demo, technical evaluation, RFP response, solution architecture. References CRM Deal/Opportunity (external). (e.g., "Run POC for Prospect X: LATAM Enterprise, SAP integration, 3-week timeline").
  * **Implementation / Onboarding:** Account-level work to integrate a specific customer — configuration, data migration, integration, go-live. Directly affects Activation Win Outcomes and may surface Delivery Frictions. (e.g., "Onboard Customer Y: Connect SAP ERP to Cross-Border API, target go-live within 30 days").
  * **Retention Engagement:** Account-level work to maintain and strengthen a customer relationship — health interventions, QBR preparation, renewal management. (e.g., "Health intervention for Customer Z: usage dropped 40%, schedule executive check-in").
  * **Expansion Engagement:** Account-level work to grow account value — upsell proposals, cross-sell campaigns, account planning. (e.g., "Upsell proposal for Customer W: add batch payout processing, estimated $50K ACV increase").
  * **Segment Engagement:** Segment-level work to engage a group of prospects or customers — awareness campaigns, feature webinars, advocacy workshops, community events, capability enablement sessions, and customer training/certification delivery. Applies to both pre-sale (awareness campaigns) and post-sale (feature adoption webinars, customer workshops, training sessions). Advocacy includes customer education. (e.g., "LATAM Enterprise feature webinar: batch payout processing launch", "LATAM CFO roundtable: cross-border payment optimization", "LATAM API certification training — cohort 3").
  * **Partner Engagement:** Account-level work directed at a specific partner — partner onboarding, co-selling, partner account management, partner pipeline management. References external PRM (Partner Relationship Management) records. Distinct from customer-facing engagement; the "account" is the partner. (e.g., "Onboard Banco Regional as LATAM channel partner — co-marketing, certification, Q3 pipeline target").
  * **Revenue Operations Engagement:** Account-level, customer-facing work to ensure revenue is realized — invoicing/billing communication, collections follow-up, renewal processing, revenue recognition coordination with Finance. Advances Revenue Win Outcomes; distinct from Expansion Engagement (upsell/cross-sell). Billing disputes are Win Case (Complaint). (e.g., "Collections follow-up for Customer W — invoice 60 days overdue; renewal processing for Customer Z — contract renewal Q3").

All Win Activities carry: AAARRR stage, Customer Segment, Win Outcome(s) advanced, Win Stakeholder(s) performing the work, Initiative alignment.

#### FIR — First Information Report (Respond — universal intake)

FIR is the atomic intake unit for all product-in-operation feedback. Every piece of feedback — whether from an external customer, an SRE detecting a monitoring alert, or a QA engineer observing a regression — enters the system as an FIR. The FIR is triaged (typically by Win team customer support) and routed: the full FIR, or specific sub-parts of it, are dispatched as work items to appropriate tracks.

**Always FIR-first.** Win Cases, Incidents, Bugs, Signals, and Maintenance Tasks that originate from product-in-operation feedback are always sub-items of an FIR. FIRs may also be resolved directly at triage (zero sub-items) for trivial inquiries. Created by any team (Win, Run, Build); Provenance field distinguishes External / Run / Build / Internal. Auto-routing is permitted for monitoring alerts.

Status lifecycle: `Created` → `Triaged` → `In Progress` → `Resolved` → `Closed`. See DR-032.

#### Win Case (Respond — reactive, customer-initiated work)

Win Case captures the reactive, responsive work of Win Teams — queries, requests, complaints, and escalations initiated by customers and prospects. Win Cases are distinct from Run Track entities (Incident, Change Request) which are infrastructure/system-facing. Win Cases are customer-facing. **Every Win Case originates from an FIR** — the universal intake envelope (DR-032).

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



### Track 5: The Evolve Track (Process Evolution)

* **Goal:** Continuously assess, define, and refine the Work Model and Operating Model — work entity definitions, artifact type definitions, DoD criteria, guidance structures, and organizational practices. Ensure the model stays current and effective as the product, organization, and market evolve.
* **Primary Owner:** Process Leads, Product Ops, Engineering Managers.
* **Bridge characteristic:** The Evolve Track is the only track whose outputs directly modify both the Work Model (entity/artifact definitions, DoD criteria, assessment criteria) and the Operating Model (guidance content, ceremony definitions, role descriptions). It is the structural bridge between the two models.
* **Operational Model:** The Evolve Track operates in **periodic review cycles** — evolution work is triggered by scheduled reviews, by Evolve Monitoring alerts, or by cross-track retrospectives. The cadence is typically quarterly or aligned to major organizational change events, but individual definition tasks may be executed continuously.

The Evolve Track has four entity types and one transitional artifact: **Plan, Assess, Define, Monitor, and Learn.**

#### Evolve Monitoring (Monitor — continuous vigilance)

Evolve Monitoring is continuous tracking of process adherence, artifact quality trends, DoD compliance rates, and guidance usage across all tracks. It surfaces when processes are not followed, when artifact quality degrades, when DoD criteria are routinely skipped, or when guidance is outdated or unused. Triggers: Evolve Review scheduling, Evolve Planning input. (e.g., "Monitor Discovery Track DoD compliance — alert when >20% of PSDs skip cross-dimensional review; track artifact quality scores quarterly").

#### Evolve Planning (Plan — evolution cycle scoping)

Evolve Planning is work to plan evolution cycles: which processes to review, which artifact types to define or refine, which guidance to develop, and which cross-track handoffs to audit. Aligns to strategic or operational improvement objectives. (e.g., "Q3 Evolve cycle: review Win Track artifact quality, define DoD for 5 Discovery Track entities, develop Build Track onboarding playbook").

Evolve Planning carries: scope (which tracks/entities/artifacts), improvement objectives, timeline, participants.

#### Evolve Review (Assess — structured assessment)

Evolve Review is a structured assessment of current process effectiveness, artifact quality, and guidance adequacy. It is the Evolve Track's equivalent of Win Review (Track 4) and Deliberation (Track 1) — a collaborative, judgment-based assessment that produces structured findings.

  * **Evolve Review types:** Process Effectiveness Review (is the process achieving its goal?), Artifact Quality Review (are artifacts meeting assessment criteria?), Guidance Adequacy Review (is guidance current, complete, and used?), Cross-Track Handoff Review (are transitional artifacts flowing correctly across track boundaries?).

Evolve Review produces **Evolve Findings** — structured observations, gap analyses, and improvement recommendations. Evolve Findings may feed Evolve Definition Tasks (process changes) or, when a process gap reveals a product-level issue, may be promoted to a Signal in the Discovery Track.

#### Evolve Definition Task (Define — meta-work)

Evolve Definition Task is the core meta-work entity — the work of creating or updating: (a) Work Model entity definitions (fields, statuses, relationships), (b) artifact type definitions and assessment criteria, (c) DoD criteria (entry/exit criteria, artifact checklists), (d) Operating Model guidance structures (playbook templates, ceremony definitions, role descriptions). This is where the model evolves.

An Evolve Definition Task may be triggered by Evolve Findings (a review identified a gap), by Evolve Planning (a planned improvement), or by a new track/entity introduction. (e.g., "Define DoD for Win Activity entities", "Add assessment criteria for Build Track Delivery Artifacts", "Update Discovery Track playbook template for Signal Exploration", "Define Evolve Track entity files for new Track 5").

Status lifecycle: `Planned` → `In Progress` → `Reviewed` → `Applied`.

#### Evolve Findings (Learn — transitional artifact)

Evolve Findings is a structured observation record produced by Evolve Reviews. It is an **artifact**, not a work item — you do an Evolve Review and *produce* Evolve Findings, just as you do a Win Review and *produce* Feedback. Evolve Findings capture process gaps, artifact quality issues, guidance deficiencies, and cross-track handoff failures.

Evolve Findings is a **transitional artifact**: born in the Evolve Track, consumed by the Evolve Track itself (Evolve Definition Task acts on findings) or by the Discovery Track when a process gap reveals a product-level Signal. Not every finding leads to a change — findings that don't warrant action are archived with rationale.



---

### Cross-Track Relationship: Customer Release Intent Lifecycle

A **Customer Release Intent** (Definition Model, Dimension 1) is a cross-cutting strategy entity whose realization spans multiple tracks:

| Track | Contribution |
|---|---|
| **Discovery Track** | Strategic planning defines Customer Release Intents as part of Initiative scoping |
| **Build Track** | Release Planning scopes PSDs/Initiatives; build work produces Component Versions, System Versions, and Product Versions |
| **Run Track** | Deployment Planning produces System and Product Deployment Specifications; Change Requests govern promotion through Deployment Trains; Deployment Tasks apply specifications; operational Systems versioned via same Build Track chain |
| **Win Track** | Customer Release Planning coordinates market delivery; GTM Planning prepares launch messaging; the Win Track **activates** the realized Customer Release through engagement, enablement, and reactive support |

A Customer Release Intent becomes `Launched` when required Deployment Specifications are successfully applied by Deployment Tasks to target environments, all Change Requests are complete, AND the business activates the realized release (Win Track).

---

### Track 6: The Governance Track (ACE Extension)

* **Goal:** Execute governance rituals and policy enforcement; produce decisions, evidence, findings, approvals, exceptions, register entries, action items, and recognition.
* **Primary Owner:** Governance, Product Operations, Engineering Managers, Compliance, Security.
* **Operating Model dependency:** Governance policies, ritual definitions, cadences, participant roles, decision authority, evidence requirements, reports, dashboards, and register definitions live in the Operating Model. Governance Track work executes those definitions.

* **Primary orchestration items:**
  * **Governance Ritual:** Cadence-based or event-triggered governance practice that brings participants, reports, dashboards, evidence, and decision authority together. Produces decisions, action items, findings, approvals, exceptions, risk/debt/compliance entries, and recognition.
  * **Governance Enforcement:** Policy assertion/control execution against an orchestration item, transition, artifact, evidence bundle, or state. Produces pass/warn/fail/exception outcomes, findings, register entries, remediation work, or Evolve Cases.

Governance Rituals and Governance Enforcement may trigger each other. A ritual may run enforcement. Enforcement may reveal a concern that requires a ritual. Repeated findings, policy drift, dashboard gaps, or ineffective rituals trigger **Evolve Cases** to evolve governance practice.

---
