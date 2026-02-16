
## PART II: THE WORK MODEL (THE 4 TRACKS)

While the 9 Dimensions define the *Definition Model* of the product, the 4 Tracks define the *motion*. This is how Maker Roles (PMs, Devs, CS) organize their daily work to mutate the 9 Dimensions. Each track owns its own planning work alongside its core activities.

> **Scope Boundary Note:** The Work Model deliberately describes **what work exists** — entities, artifacts, and state transitions. It does NOT cover:
>
> - **Coordination patterns** — ceremonies, cadences, rituals, decision-making rhythms (e.g., Sprint Planning, Quarterly Business Review, Signal Review ceremonies)
> - **Organizational design** — roles, team structures, skills profiles, training, tools, and resource allocation
> - **Capacity and scheduling** — how much work fits in a period, who does it, velocity tracking
>
> These concerns belong to the **Operating Model** — the third model in the UPIM architecture, sitting above the Work Model. The Operating Model covers both coordination and organizational design as entangled facets of how the org executes. It depends on the Work Model (you must know what work entities exist before you can design ceremonies and roles around them) but is a separate modeling concern. See the PIM Architecture README for the full three-model stack.

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
  * **Modeling Task:** Work to evolve Definition Model entities in any dimension (Dims 2–9) based on discovery findings. Modeling Tasks produce updates to the product's self-description — customer segments, buyer personas, business outcomes, customer promises, value streams, capabilities, data domains, and more. A Modeling Task may be triggered by a PDR (a decision affecting a dimension) or by ongoing product knowledge maintenance. (e.g., "Define LATAM AP Clerk user persona", "Map Cross-Border Payout Processing value stream", "Design LATAM pricing tier structure").



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



### Track 4: The Win Track (Value Realization)

* **Goal:** Plan go-to-market and customer rollout, drive adoption, and ensure the shipped product achieves the metrics defined in the Business Dimensions.
* **Primary Owner:** Customer Success, Product Marketing, Sales.

* **Planning Entities:**
  * **Go-to-Market Planning Task:** Work to prepare launch messaging, enablement materials, channel strategy for a Customer Release. (e.g., "Prepare LATAM Expansion launch: sales deck, customer webinar, help center articles, pricing page update").
  * **Customer Rollout Planning Task:** Work to plan phased customer rollout — segments, sequencing, migration support. (e.g., "Plan LATAM rollout: Tier 1 (existing cross-border customers) first, Tier 2 (new LATAM prospects) 30 days later").

* **Win Entities:**
  * **Implementation / Onboarding:** Steps to integrate a specific client (e.g., "Connect SAP ERP to Cross-Border API").
  * **Adoption Goal:** Measurable usage targets (e.g., "Reach 50,000 FX transactions this quarter").
  * **Feedback:** Structured collection of customer satisfaction or friction, which loops directly back to the Discovery Track as a new Signal — specifically a *Problem* or *Need* (Dimension 1).



---

### Cross-Track Relationship: Customer Release Lifecycle

A **Customer Release** (Definition Model, Dimension 1) is a cross-cutting entity whose lifecycle spans multiple tracks:

| Track | Contribution |
|---|---|
| **Discovery Track** | Strategic planning defines Customer Releases as part of Initiative scoping |
| **Build Track** | Release Planning scopes which PSDs/Initiatives are included; build work produces Module Versions and Product Versions |
| **Run Track** | Deployment Planning ensures all required Module Versions are deployed to target environments |
| **Win Track** | Go-to-Market Planning prepares for business activation; the Win Track **launches** the Customer Release |

A Customer Release becomes `Launched` when all required Module Versions are deployed (Run Track confirms) AND the business activates the release (Win Track executes GTM plan).

---
