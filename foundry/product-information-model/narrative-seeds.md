# UPIM Narrative Seeds

## Purpose

This file captures **connective reasoning, insights, and perspectives** discovered during modeling discussions — the material that will eventually become the narrative documentation for the UPIM.

The UPIM has three layers of documentation:

1. **Entity files** (`entities/`) — capture **what**: fields, statuses, relationships, examples per entity
2. **Decision records** (`decisions/`) and **FAQs** (`draft-modeling-faqs.md`) — capture **why**: specific design choices and their rationale
3. **Narrative documentation** (future) — captures **how it all connects**: the flow of work, the interplay between dimensions, the reasoning that makes the model coherent rather than a collection of entity definitions

This file serves layer 3. Entity files and DRs are necessary but insufficient for someone to *understand* the UPIM. A reader who has read every entity file still doesn't know why the model is shaped the way it is, how work flows through it, or what the guiding philosophy behind the design is. The narrative seeds bridge that gap.

> **Authority for deployment and versioning (DR-036):** Seeds **16** and **17** and decision record **DR-036** are authoritative for the current model (Component Version → System Version → Product Version; System and Product Deployment Specifications). Earlier seeds that describe Module Version, Module Package, Product Package, SDD, MDD, or PDD are retained for design history and are marked **Superseded by DR-036** where applicable.

## What to Capture

Each seed should capture one or more of the following:

### Connective Insights
How entities, dimensions, or tracks relate to each other in ways that aren't obvious from reading individual entity files. These are the "aha moments" that emerge during design discussions.

*Example:* "Customer Segment is the shared anchor between Vendor Value and Customer Value — the same segment viewed from the buyer's perspective (Why Buy) and the vendor's perspective (Why It Wins)."

### Design Philosophy
The guiding principles or mental models that shaped a set of decisions — not the individual decisions (those go in DRs) but the underlying reasoning pattern.

*Example:* "Win Stakeholders are Signal sources and Deliberation participants, not entity authors. This follows a consistent pattern: the people who experience reality contribute observations; the PM/PMM translates observations into structured model knowledge through governed processes (Signals, PDRs, Modeling Tasks)."

### Flow Narratives
How work moves within a track, across tracks, or between the Definition Model and Work Model. These are the dynamic stories that make the static entity definitions come alive.

*Example:* "A Pre-Sales Engineer observes that POC takes 6 weeks. They file a Problem Signal. Discovery investigates, produces a PDR. The PDR triggers both a Modeling Task (document the Delivery Friction in Vendor Value) and a PSD (build LATAM sandbox support). Build Track implements. Run Track deploys. Win Track verifies the friction is reduced. If not, Feedback generates a new Signal."

### Cross-Dimensional Symmetries
Parallels between dimensions that reveal the model's coherence — where the same analytical pattern appears in different contexts.

*Example:* "Vendor Value and Customer Value are mirror images anchored by Customer Segment. Buying Persona ↔ Win Stakeholder. Business Outcome ↔ Win Outcome. Pain ↔ Delivery Friction. Customer Promise ↔ Pricing Tier. Customer Value Metric ↔ Business KPI. Adoption Barrier ↔ Win Barrier."

### Debates and Resolutions
Key disagreements or tensions encountered during modeling, and how they were resolved. These reveal the trade-offs in the model and prevent future contributors from re-litigating settled decisions without understanding the context.

*Example:* "Initially dismissed vendor-side JTBD as unnecessary ('you already know your own goals'). Challenged by the insight that for complex enterprise products, the vendor's path to revenue is a discovery problem — implementation is bespoke, time-to-revenue varies by segment, multiple stakeholders with different frictions. The AAARRR framework provided the lifecycle structure."

## Depth Guidance

- **Not a summary.** Don't just say "we discussed Vendor Value." Capture the specific insight.
- **Not an essay.** A few sentences to a short paragraph per seed. Enough to reconstruct the reasoning, not to publish.
- **Preserve the tension.** If there was a debate, capture both sides before the resolution. The tension is as valuable as the answer.
- **Name the entities.** Use specific UPIM entity names (Win Stakeholder, Signal, Modeling Task) so seeds are searchable and traceable.
- **Tag the scope.** Each seed section is tagged with which dimensions, tracks, or architectural concerns it touches.

## How This File Will Be Used

When the narrative documentation is written (enriching `draft-definition-model.md`, `draft-work-model.md`, or creating a standalone guide), the author will:

1. Read the seeds for the relevant dimension/track
2. Weave the connective insights into the narrative flow
3. Ensure the flow narratives are reflected in the document structure
4. Use the debates and resolutions to write honest, nuanced prose — not just "here's what we decided" but "here's what we wrestled with and why the answer matters"

Seeds may be consumed and removed from this file as they are incorporated into final documentation. Until then, they accumulate.

---

## Session: Architecture and Layering

**Scope:** Three-model architecture, Operating Model design, model relationships

### The four-to-three collapse

An initial design proposed four models: Definition Model, Work Model, Operating Model (ceremonies), and Organization Model (roles/teams/skills). The layering question — which sits above which — exposed a fundamental problem: strict layering requires one-way dependency, but coordination and organization have bidirectional dependency.

- "We chose Scrum → we need a Scrum Master" (coordination shapes organization)
- "We only have 3 PMs → we can't run 6 parallel Signal Reviews" (organization constrains coordination)

Every ordering felt wrong because the wrong architectural pattern was being applied. The resolution: don't layer them. They're two entangled facets of a single Operating Model. The UPIM is three models, not four.

### The naming discipline

Each model's internal subdivision earned its name through modeling work. The Definition Model has 9 Dimensions (because we modeled 9 independent axes). The Work Model has 5 Tracks (because we identified 5 parallel streams — four for product work, one for process evolution). The Operating Model's internal structure is deliberately unnamed — "Coordination" and "Organization" are working labels, not architectural terms. Premature naming would be like calling Dimension 3 "The ROI Dimension" before discovering it's about the full buying committee, pain, promises, and barriers.

### The dependency chain reads bottom-to-top

Define the product (Definition Model) → Define what work moves the product (Work Model) → Define how the org executes that work (Operating Model). Each layer depends on the one below. The Definition Model is the foundation that never depends on anything above it.

---

## Session: Strategy

**Scope:** Strategy entities, Signal lifecycle, strategic entities, Discovery Track connection

### Signal is an investigation mindset, not a fulfillment mindset

The word "Signal" was chosen over "intake item," "backlog item," and "market signal" because it fosters investigation rather than obligation. A Signal is explicitly not a requirement, a commitment, or an obligation. It's an observation that warrants attention. Multiple Signals may point to the same issue; a single Signal may be noise. This framing is the philosophical foundation of the Discovery Track — everything that enters is questioned, investigated, and decided upon, not just processed.

### The Strategy Dimension is a ledger, not a pipeline

Strategy contains entities at very different levels of abstraction — Portfolio (organizational context), Strategic Themes (persistent direction), Objectives (time-bound goals), Initiatives (programs), Customer Release Intents (planned customer availability), Signals (observations), Ideas (hypotheses), PDRs (decisions), Product Intents (routable commitments), PSDs (specifications). This isn't a pipeline where everything flows linearly. It's a ledger — a structured record of strategic intent at multiple levels, with explicit relationships between levels.

### The PDR fills a traceability gap

Without PDRs, the model goes Signal → Idea → PSD with no artifact recording *why* a decision was made. The PDR is a knowledge artifact, not a process artifact. "Kill" PDRs are as valuable as "Go" PDRs for institutional memory. PDRs can also exist without Ideas (from strategic Deliberations) and can correspond to multiple Ideas simultaneously.

### Strategic Themes provide "the why behind the why"

Objectives are time-bound ("achieve Y by H2 2026"). Themes are persistent ("we are investing in LATAM"). Without Themes, strategic continuity across planning horizons is implicit — you must read a sequence of Objectives and infer the pattern. Themes make investment direction explicit and queryable.

---

## Session: Customer Value

**Scope:** Customer Value entities, JTBD mapping, buying committee, pain, promises, metrics, barriers

### The buying committee, not the buyer

Enterprise B2B purchases involve a committee: Economic Buyer (ROI), Technical Buyer (integration/security), User Buyer (usability/adoption), Coach/Champion (internal politics). Modeling only the Economic Buyer left the Technical Buyer invisible — yet many deals die at technical evaluation. Expanding to Buying Persona with role types captures the full committee compactly.

### Pain + Business Outcome = complete "Why Buy" motivation

Business Outcome is the rational justification ("reduce FX costs by 40%"). Pain is the visceral urgency ("4 hours/day manual reconciliation"). Value Propositions must address *both*. The critical distinction: User Personas (User Experience) *endure* pains; Buying Personas (Customer Value) *care about* pains. The same pain is cared about by different buyers for different reasons — the CFO cares about cost, the AP Ops Manager cares about productivity, the CTO cares about error rates. Each needs a different message.

### Customer Promise has three peer subtypes, not one

Value Proposition, Service Commitment, and Compliance Posture are siblings under Customer Promise — not nested. Each speaks to a different facet of the buying decision, maps to different structural entities (Value Streams/Capabilities, Operational infrastructure, Structural Capabilities respectively), uses different metric types, and changes on different cadences.

### Customer Segment is the anchor entity for Customer Value

All other Customer Value entities are scoped to Customer Segments — Buying Personas, Pains, Promises, Metrics, Barriers. Without segment scoping, the model can't express "LATAM Enterprise has different buying dynamics than US Mid-Market." This scoping principle later extended to Vendor Value as well.

---

## Session: Vendor Value

**Scope:** Vendor Value restructure, AAARRR lens, Win entities, Vendor Value ↔ Customer Value symmetry, governance

### The vendor's path to revenue is a discovery problem

Initially dismissed vendor-side JTBD ("you already know your own goals"). Challenged by the insight that for complex enterprise B2B products, the path from signed contract to steady-state revenue involves an elaborate, multi-stakeholder journey — Pre-Sales, Implementation, Go-Live, Revenue Ramp, Optimization, Renewal. Implementation is often bespoke. Time-to-revenue varies by segment. Cost-to-serve differs dramatically. None of this is self-evident; it requires the same investigation mindset as customer discovery.

The strategic *intent* (Strategy Objectives) is known. The operational *economics* of serving each segment are discovered. This distinction — known intent vs. discovered economics — is what justifies Vendor Value's analytical depth.

### AAARRR provides the lifecycle, not just revenue

Revenue is one of six AAARRR stages. "Revenue Stakeholder" and "Revenue Outcome" would have been myopic. "Win Stakeholder" and "Win Outcome" capture the full lifecycle. The naming also creates a natural bridge to the Win Track — Vendor Value defines what winning looks like; the Win Track does the work to achieve it.

### Vendor Value ↔ Customer Value: mirror images through Customer Segment

The two dimensions are two sides of the same transaction, anchored by Customer Segment:

| Customer Value (Customer's perspective) | Vendor Value (Vendor's perspective) |
|---|---|
| Buying Persona | Win Stakeholder |
| Business Outcome | Win Outcome |
| Pain | Delivery Friction |
| Customer Promise | Pricing Tier / Business Model |
| Customer Value Metric | Business KPI |
| Adoption Barrier | Win Barrier |

This symmetry is structural, not coincidental. It emerged from applying the same analytical lens (who's involved, what success looks like, what suffering exists, how it's measured, what blocks it) to both sides of the commercial relationship.

### Win Stakeholders are functional archetypes, not org chart roles

Vendor Value defines *what roles the product's commercial model requires* (Pre-Sales Engineer, Implementation Consultant, CS Manager). The Operating Model (future) defines *how teams are staffed and structured*. A startup with one person covering three Win Stakeholder roles still needs the model to distinguish the functions — because they have different concerns, different frictions, and different success criteria. When the startup hires, the Win Stakeholder model tells them what to hire for.

### All Vendor Value changes require PDRs — two governed paths

1. **Deliberation → PDR → Modeling Task:** For strategic design (pricing strategy, AAARRR target-setting). Win Stakeholders participate; PM/PMM authors.
2. **Signal → Discovery → PDR → Modeling Task:** For field observations (Delivery Frictions, Win Barriers). Win Stakeholders observe and file Signals; Discovery investigates; PDR records the decision.

This governance isn't bureaucracy — it's protection. Vendor Value entities define the commercial model. Changing a Pricing Tier affects active customers. Changing a KPI target affects resource allocation. These changes need traceability and deliberate decision-making.

### Cost KPIs are first-class citizens

Business KPIs now explicitly include Cost type alongside Revenue and Activity. CAC, implementation cost, cost-to-serve, infrastructure cost per customer — critical for unit economics, historically invisible in product planning. The AAARRR staging of KPIs enables diagnosis: "Revenue is down" is a symptom; "Acquisition CAC is 2x target while Activation rate is healthy" is a diagnosis.

---

## Session: Discovery Track Design

**Scope:** Track 1 entities, Signal → Idea flow, exploration vs. validation, Deliberation, Modeling Task

### The Discovery Track has two distinct phases of work

1. **Signal Exploration** (divergent): Signal → Ideas. Open-ended investigation to understand a Signal and synthesize candidate hypotheses. You don't know the answer yet.
2. **Idea Validation** (convergent): Idea → Validated/Killed. Targeted evidence gathering to test a specific hypothesis. You know the question.

The original "Research Task" was conflating both phases under one name. Splitting into Signal Exploration Task (divergent) and Research Task (convergent) made each phase's nature, skills, and planning requirements explicit.

### Not all decisions are empirical — Deliberation is a first-class decision path

Product councils, architecture review boards, cross-functional brainstorms — these produce decisions through collective judgment, not through experiments or research. Before Deliberation, this entire class of decision-making work was invisible. Deliberation is the only Discovery entity that is inherently collaborative and can directly produce PDRs without prior empirical validation.

### Modeling Tasks make product knowledge work visible

Much of discovery work involves understanding and documenting the product's context — defining customer segments, mapping value streams, designing pricing tiers — rather than specifying engineering changes. Before Modeling Task, this knowledge work was invisible and untracked. Making it explicit ensures it's plannable, traceable, and visible ("we're investing in understanding our customer, not just building features").

### Discovery Case is the FIR of the Discovery Track

Not all learning starts with a Signal. PMs re-evaluate pricing without filing an Opportunity. Architects raise concerns before anyone writes a Problem. Sales brings customer commitments that need feasibility work, not automatic Signal filing. SREs see operational patterns that may imply product change. Discovery Case makes this visible: a cross-functional envelope with optional Signals, coordinated sub-work, and explicit outputs.

Discovery Case is not a replacement for Signal. Signal remains the governed observation type. Discovery Case is the orchestration wrapper that lets any authorized function organize learning until a decision or routing outcome is reached.

### Discovery Support Product Intent separates learning from commitment

Discovery may need Build evidence before a final PDR. A technical spike, PoC, prototype, or feasibility build may be essential to answer the Discovery Case. Discovery Support Product Intent prevents the anti-pattern of creating "fake" delivery intents or ungoverned engineering spikes just to learn something.

Learn first with Discovery Support intent. Commit later with Evolution intent from a Go/Pivot PDR and Product Management alignment.

### Technical ideas need product framing

Engineering and architecture can originate Discovery Cases. But a technical idea does not become Product Intent merely because it is technically attractive. It must be framed in product terms: what customer promise, SLA, KRA, Customer Release Intent, vendor KPI, operational commitment, or product capability does it serve?

If architecture work cannot fit an existing Product Intent, it must become Product Intent through Discovery, route to Run or Evolve, or remain local engineering hygiene.

### Governance works through rituals and enforcement

Governance is not only a gate. It has operating rhythm and control execution.

**Governance Rituals** are cadence-based or event-triggered practices: release readiness reviews, Product Intent reviews, compliance evidence reviews, architecture review boards, discovery case reviews, governance trend reviews. A ritual brings the right participants, reports, dashboards, metrics, evidence, decision authority, and register state into one repeatable practice. It produces decisions, action items, findings, approvals, exceptions, register entries, and recognition.

**Governance Enforcement** is policy assertion: evaluate a policy against an orchestration item, transition, artifact, evidence bundle, or state. Enforcement can pass, warn, fail, block, allow with debt, allow with risk, require exception, or create remediation work.

This split keeps governance from becoming only punitive. Rituals should surface good practice as well as problems. Kudos / Recognition entries capture evidence-backed positive behavior — excellent collaboration, strong evidence discipline, effective incident handling, reusable patterns — so governance reinforces the operating model instead of merely policing deviations. Because recognition attaches to people, teams, and agents, the durable recognition entry belongs in the Workforce Repository, with PEIR retaining traceability and Evolve promoting reusable practices into PPR.

### Governance evolves through Evolve Cases

Governance policies, rituals, reports, dashboards, cadences, participant roles, evidence requirements, and playbooks are Operating Model content. They cannot be static.

When rituals or enforcement produce repeated findings, policy drift, dashboard gaps, ineffective evidence requirements, or reusable positive patterns, the right response is often an **Evolve Case**. Evolve changes the governance practice itself: update the policy, change the ritual cadence, improve a dashboard, refine evidence requirements, or turn an observed good practice into a playbook.

### Admin configures, Owner is accountable, Approver authorizes

Governance roles should name functions, not organization-specific titles. A real enterprise may bind a Control Owner or Debt Approver to its own job titles, but the UPIM should not encode those titles. The model separates three responsibilities:

- **Admin configures** policies, controls, thresholds, rituals, dashboards, and register definitions.
- **Owner is accountable** for a policy, control, evidence contract, risk, or debt over time.
- **Approver authorizes** a specific decision: transition approval, debt, exception, waiver, or risk acceptance.

This separation prevents the "admin can approve everything" anti-pattern and keeps governance portable across organizations.

### Control Objective generalizes BQO

Build Quality Objective and Build Quality Indicator are useful engineering terms, but they should not become the only governance quality pattern. A **Control Objective** states what must hold; a **Control Objective Indicator** measures current state; a **Control Objective Threshold** defines pass/warn/fail boundaries. BQO/BQI are Build-quality specializations of this general model.

The same pattern works for release readiness, evidence completeness, PM alignment, operational readiness, compliance posture, and governance ritual health.

### Debt + Catch-Up makes deviations operational

An approved deviation should not disappear into a comment thread. If a control still applies and remediation is expected, the right outcome is **Debt + Catch-Up**: a Debt Register Entry, Catch-Up Plan, due date, accountable owner, and repayment evidence.

Exception / Waiver remains available when the policy does not apply, an alternate control is accepted, or a bounded one-time bypass is approved. Debt says "we still owe this." Exception says "this control is waived or replaced for this scoped case."

### Control inheritance prevents local chaos

Controls inherit from Foundry to Workspace to Workbench. Foundry defines baselines. Workspace and Workbench scopes can add or tighten controls. They can override only where the parent scope permits. Effective controls are resolved at enforcement time so exception and debt requests route to the effective Control Owner or delegated Approver.

### Governance does not own every cadence

Daily flow, sprint planning, sprint review, and retrospectives are Work or team operating cadences. Governance should not take them over. Governance checks whether required cadences happened, whether outputs were recorded, whether blockers were escalated, whether retrospective actions aged out, and whether repeated issues should trigger Evolve.

### Release readiness is multi-dimensional

Release readiness is not only build quality. A customer-facing release may also require documentation readiness, SRE/operational readiness, security readiness, evidence readiness, customer readiness, GTM readiness, data/migration readiness, and dependency readiness. Governance coordinates the readiness decision, but the underlying evidence comes from Build, Run, Win, Product, Security, Documentation, and other functions.

### Cost, velocity, and efficiency are governance indicators

Cost, velocity, and efficiency are not merely analytics and should not be used as individual surveillance metrics. They are operating health indicators. Work and Workforce systems produce the raw data; Governance uses trends and thresholds to detect systemic risk, debt, inefficiency, overcommitment, or improvement opportunities.

### Console groups answer different questions

Work consoles show the movement of work. Workforce consoles show the people and agents doing the work. Governance consoles show whether the work system is healthy, controlled, evidenced, authorized, efficient, compliant, and improving. New consoles should be added only when a distinct user question cannot be answered clearly as a tab, panel, or overlay inside an existing console.

### The Discovery Track produces four types of output

1. **PDRs** — decisions (any dimension)
2. **Product Intents** — routable commitments from decisions into product evolution
3. **PSDs** — engineering specifications that refine Product Intent (module changes, via Specification Task)
4. **Definition Model updates** — knowledge changes (Vendor Value through Data, via Modeling Task)

A single PDR may trigger Product Intent, PSDs, and Modeling Tasks. Or just one. Or neither (if the decision is "Kill").

---

## Cross-Cutting Seeds

### The Win Track is the operational arm of Vendor Value

Where Vendor Value defines *what winning looks like* (Win Outcomes, Business KPIs, Win Stakeholder roles), the Win Track defines *the work to achieve it*. Initiative embedded targets operationalize Win Outcomes for specific periods. Win Reviews assess target progress. Feedback surfaces Delivery Frictions and Win Barriers as Signals. Win Planning references Vendor Value entities for commercial coherence. This is the strongest Definition Model ↔ Work Model coupling in the UPIM.

### The Feedback → Signal loop is the UPIM's learning mechanism

Win Track Feedback → becomes Signal (Strategy) → enters Discovery Track → may produce PDR → may trigger Modeling Task (updates Vendor Value or Customer Value) + PSD (updates product). This loop is how the UPIM learns from reality. Customer feedback surfaces product problems and unmet needs. Win Stakeholder feedback surfaces vendor-side frictions and barriers. Both re-enter the same governed discovery process.

### Every dimension has a natural "home track"

| Dimension | Primary Track | Why |
|---|---|---|
| Strategy (Strategy) | Discovery | Strategy entities are authored through Discovery planning and exploration |
| Vendor Value | Win | Win Track operationalizes Vendor Value; Feedback updates it |
| Customer Value (Customer Value) | Discovery + Win | Discovery models customer promises; Win validates them |
| User Experience (UX) | Discovery + Build | Discovery researches personas/journeys; Build implements |
| Technical (Technical) | Build | Architecture and code are Build Track concerns |
| Ecosystem (Ecosystem) | Build | APIs and extensibility are Build Track concerns |
| Operational (Operational) | Run | Infrastructure and runtime are Run Track concerns |
| Structural (Structural) | Discovery + Build | Discovery defines topology; Build realizes it |
| Data (Data) | Build + Run | Build designs schemas; Run manages operational data |

But Modeling Tasks (Discovery Track) can update *any* dimension. The "home track" is where the most frequent mutations happen; Modeling Tasks provide cross-dimensional reach.

### PSD is the cross-dimensional impact assessment

A PSD is not just "what to build." It's a structured assessment of impact across all 9 dimensions — Pain implications (Customer Value), Win Outcome implications (Vendor Value), UX impact (User Experience), technical architecture (Technical), API changes (Ecosystem), operational requirements (Operational), structural changes (Structural), data changes (Data). The depth varies by module archetype, but every dimension must be acknowledged. This makes the PSD the most integrative artifact in the UPIM.

### Customer Release Intent, Customer Promise, Win Outcome — the commercial triad

These three entities form a critical triangle spanning Strategy (Strategy), Customer Value (Customer Value), and Vendor Value (Vendor Value):

- **Customer Promise** (Customer Value) = what we commit to the customer — the explicit contract
- **Win Outcome** (Vendor Value) = what we need to achieve as a vendor — the implicit commercial target
- **Customer Release Intent** (Strategy) = the planned customer-facing delivery outcome that fulfills promises and advances outcomes

They are the three faces of a single commercial exchange. Customer Promise says "here's what you get." Win Outcome says "here's what we need for this to work for us." Customer Release Intent says "here is the named customer-facing outcome we intend to make available." The realized Customer Release is the event where promise meets outcome — where the vendor delivers on its commitments and either advances toward or falls short of its Win Outcomes.

The critical insight: **keeping promises and winning are not the same thing.** A product can keep every Customer Promise (99.9% uptime, sub-200ms latency) and still fail to achieve its Win Outcomes (CAC too high, Activation takes 90 days instead of 30). When promises are kept but the vendor isn't winning, the problem is in Vendor Value — the commercial model, the delivery economics, the Go-to-Market, the pricing structure. Conversely, if Win Outcomes are met but Customer Promises are not, it's a ticking time bomb — short-term revenue without long-term retention.

This is why the PSD's cross-dimensional sections are ordered the way they are: Section 2 (Vendor Value Impact) and Section 3 (Customer Value Impact) force the spec author to reason about *both* sides of the exchange before engineering begins.

### Customer Release Intent is a Definition Model entity that the Win Track activates

Customer Release Intent sits in Strategy (Strategy) because it's a business planning construct — deliberately scoped, named, and scheduled. But it is *activated* by the Win Track: GTM Planning prepares the launch, Customer Release Planning sequences the market delivery, and Win Reviews assess whether the realized release achieved its Win Outcomes (with progress tracked via Initiative embedded targets).

This makes Customer Release Intent the primary handoff point between strategic intent and commercial execution. The Discovery Track scopes it (which Initiatives and Product Intents are included). The Build Track assembles it (which Product Versions realize it). The Win Track activates it (GTM, onboarding, adoption). The Run Track sustains it (deployment, uptime). All four tracks converge on fulfilling the Customer Release Intent — it's the entity that most explicitly crosses every track boundary.

### Three-level versioning and the deliberate decoupling

> **Superseded by DR-036 (Seeds 16–17) and DR-038.** Current chain: Component Version → System Version → Product Version → Customer Release Intent / realized Customer Release. Retained below for design history.

System Version → Module Version → Product Version → Customer Release. Four levels, four different questions, four different owners:

| Level | Question | Owner | Cadence |
|---|---|---|---|
| System Version | What did this System's CI/CD produce? What passed quality gates? | Dev team | Continuous (every merge) |
| Module Version | Do the Systems implementing this Module work together? | Tech Lead / Integration Architect | Periodic (after Integration Epic completion) |
| Product Version | Which Module Versions are compatible as a tested composition? | Tech Lead / QA | Frequent (weekly to biweekly) |
| Customer Release | What capabilities are we making available to customers? | PM / Business | Deliberate (milestone-driven) |

The first three are Work Model artifacts (Build Track outputs) because they are *byproducts* of engineering progress — routinely and continuously produced. Customer Release is a Definition Model entity (Strategy) because it is a *decision* — someone decided "these capabilities, bundled this way, named this way, targeted to these segments." See DR-026.

The naming convention reinforces the decoupling: Customer Releases use names ("LATAM Expansion"), not version numbers. A single Customer Release may span multiple Product Versions (v3.2.0 through v3.2.4 as patches land during rollout). Pinning to a version creates a false 1:1 mapping that breaks in practice.

### Customer Promise subtypes map to different structural dimensions

This is one of the deepest cross-dimensional integrations in the model. Each Customer Promise subtype maps to different parts of the product's structural reality:

| Promise Subtype | Maps to | Why |
|---|---|---|
| Value Proposition (outcome-based) | Value Streams (Structural) | Outcomes require end-to-end flows across modules |
| Value Proposition (ability-based) | Capabilities (Structural) | Promise is about a specific product ability |
| Service Commitment | Infrastructure (Operational) | Uptime, latency, support are operational |
| Compliance Posture | Capabilities (Structural) | Compliance shapes many capabilities across modules |

This means a *single Customer Segment* receives promises that are delivered by different structural mechanisms — outcomes flow through Value Streams, abilities are provided by Capabilities, reliability depends on infrastructure, and compliance is woven through the capability layer. The Customer Promise entity unifies what the customer sees as one coherent "deal" while the model traces each commitment to its structural delivery mechanism.

### Win Outcome is structural, not time-bound — and that distinction matters

An Objective (Strategy) is time-bound: "Expand to LATAM currencies by H2 2026." It comes and goes with planning horizons. A Win Outcome (Vendor Value) is structural and persistent: "LATAM Enterprise — Activation: first live transaction within 30 days of contract." It persists across Objectives. Multiple Objectives may target the same Win Outcome across different planning horizons.

This distinction matters because Win Outcomes define what the vendor is *structurally optimizing for* — the enduring commercial targets that outlive any single planning cycle. When an Objective is "Achieved" or "Deferred," the Win Outcome it targeted remains. The next Objective in the next planning cycle may target the same Win Outcome with a different approach. Win Outcomes change only when the commercial model changes (new segment, pivoted business model, retired market) — and that change requires a PDR.

Business KPIs evidence Win Outcomes, not Objectives. Initiative embedded targets operationalize Win Outcomes for specific periods. Win Reviews assess target progress. This creates a clean separation: Strategy (Strategy) sets direction and time-bounds; Vendor Value (Vendor Value) defines enduring success criteria; the Win Track measures reality against both.

### Customer Promise ↔ Pricing Tier: the two halves of the customer-facing deal

Customer Promise (Customer Value) says "here's what you get." Pricing Tier (Vendor Value) says "here's what you pay." Together they form the complete customer-facing commercial proposition. The symmetry is reinforced by both being scoped to Customer Segments — the same segment gets specific promises and pays a specific price.

But they live in different dimensions because they serve different analytical purposes. Customer Promise is about *value delivered* (analyzed from the customer's perspective in Customer Value). Pricing Tier is about *value captured* (analyzed from the vendor's perspective in Vendor Value). A product strategist reasoning about Customer Promises asks "are we delivering enough value to justify purchase?" A product strategist reasoning about Pricing Tiers asks "are we capturing enough value to sustain the business?" The gap between these two questions is the strategic tension that drives product evolution.

---

## Session: Win Track Restructure and Initiative Evolution

**Scope:** Win Track entity landscape, levers, Initiative as cross-track construct, Win Review, Win Case, Enablement vs. Engagement, Feedback and target tracking

### Not all Win Outcomes are advanced by product capabilities alone

This is the insight that triggered the entire Win Track restructure. Consider "80% unaided brand recall in LATAM fintech CFO community" (Awareness Win Outcome) — product features barely move this needle. Or "close LATAM deals in 90-day cycle" (Acquisition) — the lever is sales enablement and competitive positioning, not code. When a Win Outcome is modeled, it's critical to identify the *means to achieve it*, and those means include non-product work: GTM, sales enablement, customer success programs.

Without explicit levers, organizations default to building features when the actual lever is a sales enablement program or a marketing campaign. The lever mix forces the question at modeling time: "Is this primarily a product problem, a GTM problem, or both?"

### Five categorical levers, defined as a master list on Business Model

The lever portfolio is a governed, finite set per Product/Portfolio, defined on the Business Model entity (Vendor Value):

| Lever | What it covers | Primary Track |
|---|---|---|
| Product | Feature development, capability enhancement, UX improvement | Discovery → Build |
| GTM | Marketing, demand gen, pricing communication, partnership/channel, launch | Win |
| Sales Enablement | Competitive tools, demo environments, POC toolkits, sales training | Win |
| Customer Success | Onboarding programs, health monitoring, retention, expansion, advocacy | Win |
| Operational | Internal process, tooling, automation, hiring | Operating Model |

GTM is the umbrella for marketing, pricing *execution*, and partnership *execution*. Pricing *design* (tier structure, rates) is a Vendor Value / Discovery concern. Partnership *strategy* is a Strategy/Vendor Value strategic decision. The levers capture the *execution* side.

### Initiative evolved from "Discovery program" to "cross-track coordination construct"

Originally, Initiative was a mechanism for grouping Signals for discovery. The lever discussion revealed that an Initiative like "LATAM Enterprise Market Entry" drives work across *all four tracks*, not just Discovery → Build. Adding a lever mix with relative weights (e.g., Product 40%, GTM 25%, Sales Enablement 20%, CS 15%) makes this cross-track scope explicit.

Targets are embedded in Initiatives like Key Results in an OKR — not as standalone entities. "Q3: 85% activation rate" is a target on the Initiative, not a separate "Adoption Goal" entity. Win Reviews assess Initiative target progress. This eliminated the need for the standalone "Adoption Goal" entity.

Objectives remain lever-agnostic. The lever mix is an Initiative-level concern. This keeps the strategy → execution separation clean: Objectives say *where*; Initiatives say *how* and *with what lever mix*.

### Enablement vs. Engagement: building the arsenal vs. deploying it

This distinction emerged from the "Sales Enablement vs. Pre-sales" question and generalizes across the entire Win Track:

- **Enablement** = building reusable assets and programs (one-to-many). One battlecard serves fifty deals.
- **Engagement** = deploying those assets on specific targets (one-to-one or one-to-segment). Each POC advances one deal.

The pattern repeats across AAARRR stages: Sales Enablement (building arsenal for Acquisition) → Pre-sales Engagement (deploying on specific prospects). CS Enablement (building onboarding playbooks) → Implementation/Onboarding (deploying for specific customer). The lever is "what kind of effort"; Enablement is "prepare"; Engagement is "execute."

### Win Review parallels Deliberation — structured assessment producing artifacts

Just as Deliberation (Discovery Track) is a collaborative decision-making work entity that produces PDRs, Win Review is a structured assessment work entity that produces Feedback. The parallel is precise:

| Discovery Track | Win Track |
|---|---|
| Deliberation (collaborative decision work) | Win Review (structured assessment work) |
| Produces PDR (decision record) | Produces Feedback (observation record) + target progress updates |

Win Review encompasses QBRs, Win/Loss analyses, Post-Implementation Reviews, Campaign Reviews, Case Pattern Reviews. It has two outputs: **Feedback** (qualitative observations, may become Signals) and **target progress updates** (quantitative assessment against Initiative targets).

### Win Review has dual assessment scope: vendor success AND customer promise fulfillment

Win Review assesses both sides of the commercial exchange — not just whether the vendor is winning (Vendor Value: Win Outcomes, Business KPIs) but also whether the vendor is keeping its promises (Customer Value: Customer Promises, Customer Value Metrics). This operationalizes the insight that "keeping promises and winning are not the same thing."

The connection to Win Review types is direct: QBRs assess whether customers are getting what they were promised (uptime, value delivery, compliance). Post-Implementation Reviews check whether onboarding delivered on Value Propositions. Case Pattern Reviews reveal whether complaint patterns indicate Service Commitment failures. Adoption Reviews check whether the product delivers the value it promised (Customer Value Metrics alongside Business KPIs).

Without explicit promise assessment in Win Reviews, the Win Track only measures the vendor's commercial health — missing the customer's experience of whether commitments are being met. Strong Win Outcomes with broken promises are a retention time bomb; kept promises with failing Win Outcomes indicate a Vendor Value problem (commercial model, not product quality). Both signals require different interventions, and only dual assessment surfaces the distinction.

### Feedback is an artifact, not a work item

Feedback was reclassified from a "Win entity" to an **artifact** produced by Win Reviews. You don't "do" a Feedback — you do a Win Review and *produce* Feedback records. Feedback is to Win Activities/Reviews what a PDR is to a Deliberation: the record produced by the work, not the work itself.

Feedback is a transitional artifact: born in the Win Track, consumed by the Discovery Track when promoted to a Signal. Not every customer observation becomes a Signal. Feedback is the raw, structured observation; Signal is the qualified, investigation-worthy version.

### Targets are not standalone entities — they're embedded in Initiatives

The "Adoption Goal" entity was eliminated. Targets (like Key Results in an OKR) are embedded in Initiatives. The reasoning: targets are set during planning, tracked during execution, and assessed during reviews. They're attributes of the coordination construct (Initiative), not independent entities.

The naming was also wrong: "Adoption" is stage-specific (only Activation), but targets span all AAARRR stages. "Goal" conflicts with Objectives. Embedding them in Initiatives resolved both problems.

### The UPIM's strategy layer follows the OKR pattern — and it's lever-agnostic

The structural mapping between the UPIM and OKRs is precise:

| OKR Concept | UPIM Entity | Relationship |
|---|---|---|
| **Objective** | Objective (Strategy) | Qualitative, aspirational, time-bound direction |
| **Key Result** | Embedded Target (on Initiative) | Quantitative, time-bound, measurable |
| *(no direct equivalent)* | Initiative (Strategy) | The strategic program that carries Key Results *and* declares how to achieve them |

The UPIM extends OKR by adding the **Initiative as a coordination layer** between the Objective (what) and the Targets (how much). In pure OKR, Key Results live directly on the Objective. In the UPIM, targets live on Initiatives — because the same Objective ("Expand to LATAM") may be advanced by multiple Initiatives with different lever mixes, each carrying distinct targets.

The critical insight: **this pattern is lever-agnostic**. Whether an Initiative is 100% Product (a pure engineering effort) or a mix of Product 40% / GTM 25% / Sales Enablement 20% / CS 15% (cross-functional market entry), the Objective → Initiative → Target structure applies identically. The OKR discipline of setting measurable targets against qualitative objectives doesn't care what *kind* of work advances the target — only that the target is measurable and time-bound. This means:

- A Build-heavy Initiative has targets like "Q3: API latency < 200ms for LATAM FX quotes"
- A GTM-heavy Initiative has targets like "Q3: 80% unaided brand recall in LATAM fintech CFOs"
- A CS-heavy Initiative has targets like "Q3: 95% gross retention rate for LATAM Enterprise"
- All three follow exactly the same structural pattern

This universality is why targets belong on Initiatives (which vary by lever mix) rather than on Objectives (which are lever-agnostic). The OKR pattern provides the measurement discipline; the lever mix provides the execution strategy. Together they answer: "What are we trying to achieve?" (Objective), "How are we going to do it?" (Initiative + lever mix), and "How will we know?" (embedded targets).

### Win Case captures reactive, customer-initiated work

A large portion of Win Team work is reactive — responding to customer queries, service requests, complaints, and escalations. Without Win Case, only proactive work was visible. Reactive work matters because:
- It's where Service Commitments (Customer Value) are tested — response times, resolution quality
- It reveals Delivery Frictions and Win Barriers through pattern analysis
- Cost-to-Serve (Business KPI) is measured against it
- CSAT and other targets can only be assessed through reactive work quality

Win Case types: Query, Service Request, Complaint, Escalation. "Complaint" was chosen over "Problem" because (a) "Problem" is already a Signal type in Strategy, and (b) in the Win Track context, the customer is expressing dissatisfaction, not filing an ITSM Problem record.

The Run Track has its own reactive entities (Incident, Change Request) for infrastructure concerns. Win Case is customer-facing; Run Track entities are system-facing.

### Segment-level engagement exists both pre-sale and post-sale

Win Activity isn't always one-to-one. Awareness campaigns, feature workshops, advocacy events, and customer webinars are segment-level engagements. Post-sale segment engagement (feature awareness webinars, capability workshops) is a significant class of work that sits alongside account-level engagements.

### The Win Track operates in continuous flow (kanban), not sprints

Win Track work doesn't align to sprint boundaries. A POC might take 3 weeks; a marketing campaign runs for 6 weeks; a QBR happens quarterly. Planning is periodic but work item duration varies. The model captures planning cycles without specifying duration.

### Signal templates structured as lever × signal type

Win Stakeholder Signals about lever effectiveness (not just Delivery Frictions) flow through the existing Signal pipeline. Templates are structured as a lever × signal type (Problem, Need, Opportunity) matrix, placed in the Signal entity definition (Strategy). This applies to all Signal sources, not just Win Stakeholders.

---

## Session: Work Execution Framework

### The Work Model's asymmetric artifact coverage

The Work Model was detailed about *what kinds of work exist* but inconsistent about *what each work type produces*. Where artifacts fed back into the Definition Model (PDR, PSD, Feedback → Signal), they were well-modeled. Where artifacts were consumed internally within a track (Research findings, Experiment results, deployment runbooks, enablement assets, case resolution records), they were implied in descriptions but not structurally captured. This created a blind spot: stakeholders could see what work to do but not what "done" looks like or what outputs to expect.

### Three execution dimensions, not one

The gap isn't just artifacts. Three dimensions are needed to fully describe the execution semantics of a work entity: (1) **Artifacts** — what it produces, (2) **Definition of Done** — when it's complete, (3) **Guidance** — how to navigate it. These three form a coherent framework for any work entity, regardless of track. A product manager looking at a Win Review entity needs all three: what does it produce (Feedback + target progress), when is it done (findings documented, Feedback artifacts created, target progress updated), and how do I run one (QBR playbook).

### Artifacts and DoD belong to the Work Model; guidance belongs to the Operating Model

The key boundary: artifacts and Definition of Done describe properties of the work itself — what it produces and when it's complete. These are information model concerns. Guidance (playbooks, templates, procedures) describes how teams *execute* the work — that's methodology, which varies by team, product, and context. The Work Model captures the structure of guidance (what a playbook should cover) but not the content (which lives in the Operating Model). Entity files reference Operating Model playbooks; they don't contain them.

### Artifact taxonomy provides a shared vocabulary

Five artifact categories emerged: Decision (recorded choices), Evidence (findings and observations), Specification (what to build/deliver), Delivery (versioned outputs), Assessment (evaluations against targets). Every work entity's output can be classified into one or more of these categories. The taxonomy provides a common language across tracks — a PDR is a Decision Artifact, a System Version is a Delivery Artifact, Feedback is an Evidence Artifact, a PSD is a Specification Artifact.

### Transitional vs. terminal artifacts mark track boundaries

Some artifacts are born in one track and consumed by another — Feedback (Win → Discovery), PSD (Discovery → Build), System Version (Build → Run). These "transitional" artifacts are the track boundary contracts. Terminal artifacts are consumed within their own track or by external systems. Making this distinction explicit helps identify integration points and handoff contracts between tracks.

### The framework enables iterative detailing without losing coherence

By establishing the artifact taxonomy, DoD pattern, and guidance structure as a framework, individual tracks can be detailed independently. Detailing Track 1's artifacts doesn't require simultaneously detailing Track 3. The cross-track artifact inventory provides the global picture; per-entity execution sections provide the detail. Phase 5 (cross-track integration) validates that all transitional artifacts have matching producers and consumers.

---

## Session: Cross-Track Monitoring and Win Track Gaps

### Continuous monitoring is a work type in every track

Every track has ongoing monitoring work that sits between periodic assessment (Reviews, Deliberations) and reactive work (Cases, Incidents). This work was invisible in the model — teams did it, but it wasn't a first-class entity. Introducing Signal Monitoring (Discovery), Build Monitoring (Build), System Monitoring (Run), and Win Monitoring (Win) makes the pattern explicit: monitoring produces alerts (which trigger reactive work) and reports/dashboards (which feed periodic reviews). The same structure applies in all four tracks; only the scope and metrics differ.

### Partner/channel work is distinct from internal sales and customer engagement

Partners are intermediaries in the AAARRR journey (Awareness, Acquisition). They need enablement (partner demo environments, co-marketing kits, certification) and engagement (partner onboarding, co-selling, pipeline management) that is distinct from Sales Enablement (which equips *internal* teams) and from customer-facing Win Activity. Partner Enablement and Partner Engagement were added as subtypes; Engagement Planning scope was extended to include partner prioritization and sequencing. References external PRM (Partner Relationship Management).

### Revenue realization is both operations and intelligence

Revenue Realization is an essential signal for Vendor Value. Two additions: (1) **Revenue Operations Engagement** — account-level, customer-facing work to ensure revenue is collected (invoicing, collections, renewal processing, revenue recognition coordination). Advances Revenue Win Outcomes; billing disputes stay in Win Case. (2) **Revenue monitoring** — covered by Win Monitoring (NRR, pipeline, churn signals); when targets are missed, the signal feeds Win Review or Feedback → Signal. Both commercial operations and revenue intelligence belong in the Win Track.

### PLG segments shift Win Track from execution to monitoring

For segments where the Product lever dominates (self-service onboarding, free trial, in-product expansion), the same Win Activity subtypes apply but the balance shifts. Implementation/Onboarding becomes in-product; Win Track monitors funnels and intervenes on stuck accounts. Pre-sales becomes trial/sandbox; Win Track monitors conversion. The Build Track effectively does "Win" work (self-service flows, in-product upsell). Win Monitoring becomes the primary Win Track activity; human engagement is for exceptions. No new entities — a conceptual note suffices.

### Advocacy encompasses customer education

Customer education (training, certification, knowledge bases, workshops) is already covered: CS Enablement builds the assets (training materials, certification curricula); Segment Engagement delivers them (webinars, training sessions). CS Planning plans education programs as part of advocacy. Advocacy was clarified to encompass both referral/case-study work and customer education; explicit examples were added (e.g., "LATAM API integration certification program"). No new entities.

---

## Session: Tier 2 Detailing — Structural Links, Segment Enrichment, and Competitive Context

### Vendor Value and Customer Value are structural parallels, not operational mirrors

Vendor Value (Vendor Value) and Customer Value (Customer Value) use the same analytical shape — stakeholder, outcome, suffering, impediment, metric — but from opposite sides of the commercial relationship. Win Outcome (vendor's target) and Business Outcome (buyer's target) are not equivalents that need linking. Delivery Friction (vendor suffering) and Pain (customer suffering) are different phenomena with different sufferers and remediation paths. Win Barrier (vendor impediment) and Adoption Barrier (customer impediment) are distinct; an Adoption Barrier *may cause* a Win Barrier, but the causal link flows through the Signal pipeline, not a direct entity relationship. Business KPI (vendor health) and Customer Value Metric (promise fulfillment) measure entirely different things. The two dimensions connect through Customer Segment — the shared anchor — not through pairwise entity relationships. Adding cross-dimensional links between the pairs would overstate connections that are conceptual, not operational.

### Vendor Value/Customer Value entities need structural links to Structural (the product)

While Vendor Value and Customer Value don't link to each other, several entities in both dimensions benefit from traceability to the product's structural dimension (Structural). When a Win Outcome lists Product as an Achievement Lever, "which product structure supports this?" should be answerable. When a Delivery Friction has a product root cause, "which module or capability is involved?" enables structural root-cause analysis. When a Win Barrier or Adoption Barrier points to a product gap, "which capability is missing?" enables product-level impact analysis. These links are optional — not every Win Outcome involves Product as a lever (pure GTM outcomes don't), not every Delivery Friction has a product root (operational frictions don't), and not every barrier is product-rooted (Financial, Contractual, Cultural barriers aren't). But when the link exists, it should be explicit.

Four entities received Structural structural links:
- **Win Outcome** → `Enabled by | Value Stream / Capability (Structural)` — when Product is an Achievement Lever
- **Delivery Friction** → `Rooted in | Module / Capability (Structural)` — when friction has a product root cause
- **Win Barrier** → `Structural root | Capability / Feature (Structural)` — when barrier points to a product gap
- **Adoption Barrier** → `Structural root | Capability / Feature (Structural)` — when barrier points to a product gap

### Customer Segment is the structural home for competitive intelligence

Competitive intelligence was scattered: Value Proposition had "Primary Alternative" and "Key Differentiator" fields, Win Barrier had a "Competitive" type, and Win/Loss Analysis (a Win Review type) captured competitive dynamics. But there was no per-segment competitive summary — "who do we compete against in this segment, with what, at what position?" The decision: competitive intelligence belongs as a structured field on Customer Segment (the Competitive Context sub-structure), not as a standalone entity. Rationale: competitive positioning is always segment-scoped (you may be a leader in one segment and a new entrant in another); the competitive landscape changes faster than product definition; detailed competitive playbooks and battlecards are Operating Model / Sales Enablement content, not Definition Model entities. Customer Segment's Competitive Context references Competitive-type Win Barriers, closing the loop.

### Customer Segment carries commercial planning fields

Customer Segment was structurally correct but commercially thin — industry, geography, size, and maturity were modeled, but nothing about market sizing, revenue potential, buying patterns, or strategic priority. These are not operational state; they are structural market attributes that inform every downstream decision: which segments to target with Initiatives, how to size Pricing Tiers, which Win Outcomes to prioritize. Four fields were added: Buying Motion (PLG / SLG / Hybrid — influences Win Track engagement patterns), Segment Size (TAM), Revenue Potential (per-customer and segment-level), and Strategic Priority (Primary / Secondary / Exploratory / Deprioritized).

### Business Outcome needs the buyer's own yardstick

Customer Value Metric (Customer Value) measures whether the *vendor's promise* is being fulfilled — "did we deliver 99.9% uptime?" But the buyer has their own way of measuring whether the purchase paid off — "what's our cross-border payment cost as a percentage of revenue?" This is the buyer's internal KPI, reported to their board, used to justify renewal. It's distinct from what the vendor measures. Business Outcome was enriched with two fields: Buyer's Internal KPI (how the purchasing organization measures the outcome) and Current Baseline (the buyer's starting state, establishing the "before" for ROI). These fields are often sourced from pre-sales discovery and are critical for sales positioning and renewal justification.

### TCO remains a parked gap

Total Cost of Ownership — what it costs the customer to adopt and operate the product (integration, training, migration, ongoing operational overhead) — remains a recognized gap. It is distinct from vendor pricing (Vendor Value) and directly inputs the buyer's ROI calculation. The anchoring point (Customer Promise? Customer Segment? Business Outcome?) and qualification approach need further discussion. Current Baseline on Business Outcome captures some TCO-adjacent information (the buyer's current state), but a structured TCO model would require its own design session.

---

## Session: User Experience Expansion

### Discovery produces User Experience entities

The Discovery Track is the entry point for all User Experience entities. User Personas are hypothesized during Signal Exploration, validated through Research Tasks, and formalized through Modeling Tasks. Jobs (JTBD) are identified through user research and validated through Experiments and Prototypes. UX Channel decisions ("Should we build a mobile app?") are PDR-level strategic choices that emerge from Deliberations. User Journeys are designed during Specification (PSD authoring) and refined through Prototypes/Spikes. This is consistent with the model's governance pattern: Discovery defines, Build implements, Run stabilizes, Win realizes.

### Jobs to Be Done (JTBD) is a standalone entity, not a field on Persona

A Job is what the user needs to accomplish — "Process a cross-border payout without errors." It sits between Pain (Customer Value — the visceral suffering that makes the current state intolerable) and Business Outcome (Customer Value — the strategic justification the buyer uses internally). The Job is the *user-level* goal. It deserves standalone status because: (1) Jobs are reusable across Personas — an AP Clerk and a Treasury Analyst may share the job "Verify FX rate applied to a payment." (2) Jobs map to Capabilities and Value Streams (Structural), creating a structural bridge between user intent and product structure. (3) Jobs map to User Journeys — a Journey *accomplishes* a Job; without the Job entity, the question "why does this Journey exist?" has no formal answer. The relationship chain: Persona → has → Job → accomplished through → Journey → experienced through → Channel.

### Job bridges User Experience (user intent) to Structural (product structure) and Customer Value (buyer justification)

Job → Value Stream is the primary structural mapping: "Process a cross-border payout" maps to the "Cross-Border Payout Processing" Value Stream. A Value Stream may serve multiple Jobs across different Personas (AP Clerk processes, Treasury Analyst verifies, Compliance Officer audits — same stream, different jobs). Job → Capability is a direct mapping for simpler jobs that don't require a full end-to-end flow ("Check my FX rate lock status" → "Automated Rate Locking" Capability). Both relationships are many-to-many. Job → Business Outcome (Customer Value) connects user-level goals to buyer-level justification: the AP Clerk's Job "process payouts without errors" contributes to the CFO's Business Outcome "eliminate manual FX hedging."

### UX Channel is typed by two orthogonal axes: Interaction Modality and Engagement Mode

A UX Channel is the access mechanism through which a Persona reaches the product. It is identified by a tuple of two axes:

- **Interaction Modality** (by technology): Web, Mobile, Chat, Voice, Email, CLI
- **Engagement Mode** (by service model): Self-serve, Assisted, Managed

These axes are orthogonal — you can have Web + Self-serve (typical SaaS dashboard), Web + Assisted (co-browsing with support), Chat + Self-serve (chatbot), Chat + Assisted (live agent), Voice + Managed (phone-based concierge). The matrix produces the full channel landscape. Each product defines which cells in this matrix it occupies; most products serve a subset.

### Each UX Channel is implemented by exactly one Human-Interactive Module (Structural)

The module archetype taxonomy already defines Human-Interactive as one of three interaction boundaries (alongside Programmatic-Interactive and Reactive/Background). Each UX Channel is the experiential definition (User Experience); the Human-Interactive Module is the structural realization (Structural). One-to-one: each Channel is implemented by one HI Module; each HI Module implements one Channel. The HI Module carries its Capabilities, Features, and technical implementation; the Channel carries its experiential characteristics — interaction modality, engagement mode, and the Journeys it supports.

### Features in HI Modules should document experience attributes

Features within Human-Interactive Modules are encouraged to specify experience attributes — simplicity, ease, delight, control, speed, discoverability, error tolerance — that articulate what makes the feature's experience distinctive beyond its functional specification. "Real-time FX rate locking" is the functional feature; "one-click rate lock with visual confirmation and undo within 5 seconds" conveys the experience quality. These are not mandatory structured fields but guidance hints in the feature template, encouraging PMs and UX designers to articulate experiential intent alongside functional spec.

### Touchpoint is too granular for the Definition Model

Touchpoints ("Target Currency dropdown," "Lock Rate button") are implementation-level UI artifacts that change with every sprint. Including them in the Definition Model would bloat the model with entities no team would maintain and conflate structural product definition with screen-level design. The Definition Model captures down to User Journey (a named, purposeful flow). Touchpoints live in Build Track work artifacts — PSDs (which specify what a module should deliver), prototypes, and design specifications. The existing `dim4-touchpoint.md` entity is deprecated; Touchpoints are referenced in the Work Execution Framework as Build Track design artifacts.

### Multi-channel journey continuity uses lightweight cross-references

When the same Job can be accomplished across multiple Channels, or when a user starts a Journey on one Channel and finishes on another, two lightweight mechanisms model this without complex cross-channel flow modeling: (1) **Journey Equivalence** — references to journeys in other channels that accomplish the same Job (independent alternatives; user picks one channel). (2) **Journey Continuity** — references to journeys in other channels that this journey can hand off to or receive from (sequential handoffs; user crosses channels mid-flow). Both are simple reference fields on User Journey — no new entities, no unified cross-channel flow model.

### UX Channels carry a lifecycle — channel investment is a PDR-level decision

Deciding to build a new Channel (e.g., "build a mobile app," "add a chatbot") is a strategic investment that should be governed through Discovery: Deliberation → PDR → Product Intent → PSD. Channels carry statuses: `Proposed → Approved → Active → Deprecated → Retired`. This is consistent with how other structural entities with significant investment implications are governed (Pricing Tiers, Customer Releases).

### Embedded is a channel modality, not just a technical concern

Making journeys embeddable — payment widgets, Salesforce plugins, white-label components — is a deliberate product strategy, not merely a technical design choice. A component being technically reusable is a Build Track artifact concern. But a product deciding that certain journeys should be embeddable in customer or third-party applications is a channel-level decision: it requires its own HI Module, its own journey design (fragment, not full flow), and its own constraints (vendor controls the component, not the host page; must be self-contained). Embedded was added as a seventh Interaction Modality alongside Web, Mobile, Chat, Voice, Email, CLI. It participates in the same Modality × Engagement Mode matrix — an Embedded + Self-serve widget (payment form in customer's app) vs. an Embedded + Managed component (agent-operated plugin in Salesforce).

### Accessibility is a channel-level concern

Accessibility standards (WCAG 2.1 AA, Section 508) are strategic commitments that vary by channel and influence HI Module design, testing, and certification. An Accessibility Standard field was added to UX Channel. This complements Compliance Posture (Customer Value), which captures the customer-facing accessibility commitment; the Channel field captures the specific standard each channel must meet.

### Personas are product role or business domain role based

User Personas can be defined by product role ("Approver," "Analyst," "Admin") or business domain role ("AP Clerk," "Compliance Officer"). Both are valid. Most personas combine both: "AP Clerk" is a business domain role whose product role is "Payment Initiator." The product's RBAC mapping — which features, journeys, and capabilities are available to which product roles — is a Structural / implementation concern. The Definition Model captures the persona archetype; the product's permission model is below the waterline.

### User Journeys engage specific Capabilities, not just Value Streams

A Journey traverses Value Streams (end-to-end flows) but also engages specific Capabilities within those streams. "Initiate and approve a cross-border payout" engages Payment Initiation, Automated Rate Locking, OFAC Screening, and Payment Execution capabilities in sequence. This finer-grained structural link enables capability-level impact analysis: if a Capability changes, which Journeys are affected? Value Stream traversal identifies the broad flow; Capability engagement identifies the specific product abilities required at each step.

---

## Session: Ecosystem Expansion

### Ecosystem is about deliberate extensibility, not incidental APIs

Every module has APIs as a byproduct of its functional design — internal interfaces because the system is distributed. These are Technical (Technical) and Structural (Module boundary) concerns, not Ecosystem concerns. Ecosystem exists only when there is a **deliberate product strategy** to make capabilities externally consumable for well-understood customer, partner, or third-party use cases. The decision to expose a "Payments API" is not "we have internal APIs, let's publish them." It's "we understand that customers need to integrate payment processing into their ERP systems — so we will design, build, and maintain a purposeful programmatic surface for that scenario." Ecosystem is demand-driven from the ecosystem, not supply-driven from architecture.

### Developer Persona and Programmatic User Persona belong in Ecosystem, not User Experience

User Experience and Ecosystem represent fundamentally different interaction paradigms — visual/experiential vs. programmatic/contractual. A developer integrating via API doesn't follow a "journey" through a "channel" with "experience attributes." They read documentation, write code, test in a sandbox, debug error responses, iterate over days/weeks. The User Experience vocabulary (Journey, Channel, Touchpoint) doesn't describe this work. Ecosystem needs its own persona entities for the people and systems who consume its surface.

**Developer Persona** is the human building the integration — their concerns are API ergonomics, documentation quality, SDK completeness, error message clarity, backward compatibility. These are fundamentally different from User Experience User Persona concerns (simplicity, delight, visual clarity).

**Programmatic User Persona** is the application or system consuming the API at runtime — a customer's ERP, a partner's middleware, a third-party app. These are not human at all. They have integration requirements, throughput needs, SLA dependencies, and error handling expectations. You cannot model a machine as a User Experience User Persona with "Frustrations" and "Preferred Channel."

The same human may appear in both dimensions: an Integration Engineer is a User Experience Persona when using the Developer Portal (Web + Self-serve channel) and a Ecosystem Developer Persona when writing API integration code. This is correct modeling — the same person interacts through two different surfaces with different design concerns, quality criteria, and stakeholders.

### Ecosystem modules are Structural modules — same product, different lens

A Ecosystem module (API Module, Integration Module, Extension Module, SDK/Library Module) **is** a Structural module. It appears in the Product → Module → Capability → Feature hierarchy. It has its own bounded context, Capabilities, Features, Technical internals, Build Track versioning, and archetype classification. What makes it an *Ecosystem* module is: (1) its purpose is externally-facing extensibility, not internal product functionality; (2) its capabilities are often compositional — curating and simplifying capabilities from other Structural modules for a use-case-oriented surface; (3) it carries Ecosystem-specific concerns (Developer Personas, Programmatic Personas, API contracts, versioning commitments) that other modules don't carry.

This parallels User Experience exactly: Human-Interactive modules are Structural modules that carry User Experience concerns (User Personas, Jobs, Channels, Journeys). Programmatic-Interactive and extensibility modules are Structural modules that carry Ecosystem concerns. The dimensions are lenses on the same structural entities, not different entities.

### API Module is protocol-agnostic — defined by contract, not transport

An API Module's identity is the **use case it serves and the contract it commits to**, not the wire protocol. A Payments API Module might expose REST endpoints for synchronous operations, gRPC for low-latency calls, Kafka topics for event streaming, SFTP/file-based interfaces for batch processing, webhooks for callbacks, and GraphQL for flexible queries — all part of one cohesive module. File/SFTP batch interfaces, Kafka events, webhook callbacks, and REST APIs are all delivery mechanisms for the same programmatic capability. The module's contract is "Create Payment," "Get Rate Quote," "payment.settled notification" — how that contract is delivered (HTTP POST, Kafka message, batch file row) is an implementation characteristic within the module, not a defining distinction between modules.

### Three Ecosystem module types represent distinct strategic decisions

Each module type is a deliberate, PDR-level product strategy choice with different architectural concerns:

- **API Module** — a named, versioned, use-case-oriented programmatic surface for external consumption. Protocol-agnostic: encompasses REST, gRPC, batch/file, event streams, webhooks, GraphQL. Composes capabilities from one or more Structural modules into a cohesive programmatic interface. Design concerns: versioning, backward compatibility, rate limiting, authentication, documentation, contract design.
- **Extension Module** — a framework enabling third parties to extend the product's behavior (plugins, hooks, custom workflows). Composes extensibility points from one or more Structural modules into a governed extension surface. Design concerns: plugin API stability, sandboxing, permission model, marketplace governance.
- **SDK/Library Module** — a language-specific client providing idiomatic access to API modules. Wraps Ecosystem API modules in language-specific abstractions. Design concerns: language idioms, dependency management, auto-generated vs. hand-crafted, testing support, version tracking.

### Integration Module is a connector/adapter — not another API surface

Early modeling proposed Integration Module as "APIs bundled for a scenario," but this overlapped heavily with API Module (both are use-case-oriented, both compose from Structural modules, both expose programmatic interfaces). The sharpened distinction: **Integration Module is a pre-built bridge between the product and a specific external system or system category.** It includes not just "our API" but also the glue — data mappings, protocol translations, workflow adapters, and pre-built connectors that translate between the product's model and the target system's model. API Module says "here's our programmatic interface"; Integration Module says "here's a ready-made bridge between us and Salesforce/SAP/your ERP." Design concerns diverge: data format translation, protocol bridging, polling vs. push, conflict resolution, target-system-specific error handling. If a product doesn't ship connectors to specific external systems, it has API Modules but no Integration Modules — and that's a valid product decision.

### Ecosystem modules are compositional — use-case-scoped, not module-scoped

A Ecosystem module does not mirror a Structural module 1:1. It may span multiple Structural modules, presenting a curated subset of capabilities oriented around a specific external use case. A Dispute Case Management API Module composes capabilities from Payment Module (retrieve transactions, initiate refunds), Compliance Module (retrieve screening results), Customer Module (lookup profile), and Communication Module (send notifications) — into a single, cohesive programmatic surface. The developer interacts with the Ecosystem surface; they never need to know about the vendor's internal module boundaries. This composition — the curation, simplification, and idiomatic presentation — is Ecosystem's value add over "just exposing module APIs."

### SDK and mobile apps share the same deployment pattern — Client-Distributed

The archetype taxonomy's Deployment Topology axis implicitly assumes vendor-side deployment (monolith vs. distributed microservices). But many modules run in the customer's/user's environment: mobile apps (app stores → user's device), PWAs (CDN → user's browser), SDKs (package registry → customer's codebase), embedded widgets (CDN → customer's web app), CLI tools (package manager → developer's machine). These are all **Client-Distributed** modules — built by the vendor, distributed through a channel (app store, package registry, CDN), and instantiated in the consumer's environment. They are fully valid Structural modules with Capabilities, Features, Technical internals, and Build Track versioning. Their Operational (Operational) footprint is lighter (CI/CD + distribution channel + version adoption tracking rather than clusters and containers), but the entity structure is identical. This is not a new concept — we've been modeling mobile apps and web clients this way all along. The archetype taxonomy's Deployment Topology may evolve to explicitly name this pattern: Vendor-Hosted (Monolith/Distributed) vs. Client-Distributed.

### Payload Schema is too granular — same pattern as Touchpoints

Payload Schema (specific field definitions for request/response payloads) follows the same granularity pattern as Touchpoints in User Experience. The contractual *existence* of a schema matters — "Create Payment has a defined input and output contract" — but the specific fields, types, and validation rules change with each version and belong in PSD and Build Track artifacts. The Definition Model captures the operation and its commitments; the schema details live below the waterline.

### SLOs are the Ecosystem analog of experience attributes in User Experience

In User Experience, features carry experience characteristics (simplicity, ease, delight) — the qualitative promise to users. In Ecosystem, the "experience" for programmatic consumers is quantitative: performance, reliability, throughput, consistency. SLOs on API Operations declare **what the product commits to** — p99 latency, availability percentage, throughput limits, delivery guarantees — without prescribing how the vendor achieves them (that's Technical/Operational/Run Track territory). SLOs connect richly to the existing model: Customer Promise (Customer Value) derives SLAs from operational SLOs; API Compatibility Contract includes performance stability alongside interface stability; Programmatic User Personas evaluate operations by their SLO profile; Win Monitoring tracks SLO compliance; Win Reviews assess SLO fulfillment.

### Unified API Operation entity with pattern classification

Early modeling proposed separate "Endpoint" and "Event" entities. But both are named, versioned, contractual commitments belonging to an API Module, consumed by the same personas, subject to the same compatibility contract. The boundary between them blurs in practice: a "Create Payment" submitted via Kafka is a command message — is it an endpoint or an event? A "payment.settled" status retrieved via polling is a query — is it an endpoint or event notification? The cleaner model is a single **API Operation** entity classified by interaction pattern. This parallels existing patterns: Win Case has subtypes (Query, Service Request, Complaint, Escalation); Signal has subtypes (Problem, Need, Opportunity); Customer Promise has subtypes. The classification preserves analytical distinction ("what events do we publish?" "what commands do we expose?") while keeping one entity, one relationship set, one place in the Module → Operation hierarchy.

### Five interaction patterns with genuinely distinct SLO profiles

Each pattern represents a fundamentally different consumer interaction with different SLO dimensions:

- **Command** (Consumer → Product, state change): "Create Payment." SLO: latency, availability, throughput.
- **Query** (Consumer → Product, read): "Get Rate Quote." SLO: latency, availability, throughput.
- **Event** (Product → Consumer, notification): "payment.settled." SLO: delivery guarantee, delivery latency, ordering.
- **Callback** (Product → Consumer, async result): "payment.processing.complete." SLO: delivery guarantee, delivery latency.
- **Batch** (Bidirectional, bulk): "Upload Payment File," "Daily Settlement Report." SLO: processing window, throughput, completeness.

Batch is a genuinely distinct pattern, not "many Commands bundled together." Its SLOs (processing window, partial-success handling, reconciliation), error semantics (rejection reports), and consumer workflow (prepare → upload → wait → download results) are categorically different from per-request interactions.

### Interface Type and Payload Schema demoted — not standalone entities

**Interface Type** (REST, gRPC, Webhook, etc.) was a standalone entity in the original Ecosystem dimension. Since API Module is protocol-agnostic — REST, batch/SFTP, Kafka, webhooks, gRPC, GraphQL are all delivery mechanisms — Interface Type becomes a field on the module ("Supported Protocols"), not a first-class entity. **Payload Schema** is demoted to PSD/Build territory (see above). Both follow the same principle: the Definition Model captures strategic commitments and structural identity; implementation and schema details live below the waterline.

---

## Session: Track 5 — Evolve (Process Evolution) and Artifact Type Catalog

_Date: 2026-02-19_

### A model that cannot evolve is dead

The Work Model defines what work exists. But who defines the Work Model? Without explicit modeling of this meta-work, the model stagnates — it captures a snapshot of how work was organized at the time of its creation, but cannot adapt as the product, organization, and market change. A model that doesn't account for its own evolution is dead right out of the gate. The Evolve Track makes process evolution a first-class concern with the same structural rigor as Discovery, Build, Run, and Win.

### Process evolution is foundational work, not overhead

There is a temptation to view process evolution as optional overhead — "we'll improve our processes when we have time." This inverts the dependency: process quality directly affects the quality of every artifact produced by every track. A poorly defined DoD for PSDs means poorly specified builds. A missing playbook for Signal Exploration means inconsistent discovery. Process evolution is not something you do after the "real work" — it is work that makes all other work effective. This is why it earns a dedicated track rather than being buried in per-track "housekeeping."

### Track vs. bridge: structural form follows structural reality

Initial discussion explored modeling process evolution as a "bridge" between the Work Model and Operating Model — a lighter-weight architectural concept. But when you list what this "bridge" needs (goals, entity types, artifacts, participants, a lifecycle, assessment mechanisms, monitoring), you've described a track. Calling it something other than "track" invents new terminology that gives it less structural rigor. The bridge *relationship* is real — Track 5 is the only track that directly modifies both the Work Model and the Operating Model — but the structural *form* is a track.

### Evolve Findings parallel Feedback — transitional artifacts that bridge assessment and action

Win Review produces Feedback; Evolve Review produces Evolve Findings. Both are structured observation records that cross a boundary: Feedback flows from Win Track to Discovery Track (when promoted to Signal); Evolve Findings flow from Evolve Track to Evolve Definition Tasks (when actioned) or to Discovery Track (when a process gap reveals a product gap). The pattern is consistent: assessment produces structured observations, which are consumed by downstream work. Not every observation warrants action — the "Archived with rationale" path is as important as the "Actioned" path.

### Artifact assessment criteria belong in the Work Model

Assessment criteria define what a good instance of an artifact type looks like — "a PDR must include alternatives considered," "a System Version must pass vulnerability scan." These are properties of the artifact type, not of the team producing it. A poorly reasoned PDR is poor regardless of which team authored it. This makes assessment criteria a Work Model concern (intrinsic to the information model), not an Operating Model concern (team practices). The Operating Model may define *how* teams achieve these criteria (review ceremonies, checklists, tooling), but the criteria themselves are stable across teams.

### Named artifact types make the taxonomy actionable

The five artifact categories (Decision, Evidence, Specification, Delivery, Assessment) are necessary but insufficient. Telling a PM that Deliberation produces a "Decision Artifact" is true but unhelpful — they need to know it produces a PDR with specific quality expectations. Named types per track with assessment criteria bridge the gap between taxonomy and practice. They also provide the evaluation basis for Evolve Reviews — you can't assess artifact quality without knowing what "quality" means for each type.

### Track 5 is the mechanism for its own evolution

A natural question arises: "Who evolves Track 5?" The answer is Track 5 itself — Evolve Reviews can assess Evolve Track entity definitions, Evolve Definition Tasks can update Evolve Track DoD criteria. This is not circular; it is self-referential in the same way that a compiler can compile itself. The first version of Track 5 is bootstrapped (defined through the initial modeling work); subsequent versions are evolved through Track 5's own mechanisms.

---

## Session: Operational

*Scope: Operational expansion, cross-dimensional parallels (Vendor Value, Ecosystem), Run Track Tenant, UX Channel and Integration Module scope widenings. References DR-023.*

### Vendor Value and Ecosystem parallels drive Operational entity design

Operational was the least developed dimension — 3 skeletal entities (Environment, Cluster/Host, Container/Process) with no strategic framing, no personas, no relationships. The expansion drew structurally from two well-detailed dimensions: Vendor Value (vendor value) and Ecosystem (extensibility). The parallels are explicit and intentional: Business Model → Infrastructure Model (root entity framing the domain), Win Stakeholder → Operational Persona (functional archetype), Win Outcome → Operational Target (what success looks like), Delivery Friction → Operational Pain (concrete suffering), Win Barrier → Operational Constraint (structural impediment). From Ecosystem: Developer Persona → Operational Persona (domain-specific persona), API Operation SLOs → Operational Target SLOs (performance commitments at different layers). These are structural parallels — they inform entity design — but not inheritance. Each dimension is self-contained.

### Operational Quality Taxonomy is a classification framework, not entities

Reliability, Performance, Security, Compliance, Cost Efficiency, Observability, Scalability — these are the operational "ilities" that classify Operational entities. Initially proposed as standalone entities ("Operational Quality Attribute"), they were reconsidered: they are a categorization framework, not individual entities. The parallel is AAARRR in Vendor Value — Awareness, Acquisition, Activation, Retention, Revenue, Referral are not individual entities; they are a classification axis used to type Win Outcomes, Win Stakeholders, and Business KPIs. Similarly, the quality taxonomy types Operational Targets (Availability SLO, Cost SLO), Operational Constraints (Compliance Boundary, Security Standard), and Operational Personas (Reliability Operator, Security Operator). The vocabulary lives in the dimension introduction and appears as enumerated types on entities.

### Tenant is a Run Track work entity, not a Definition Model entity

The initial instinct was to model Tenant as a Operational entity. The corrected view: a Tenant is something that is provisioned, configured, monitored, scaled, and eventually decommissioned — it is the result of operational work, not a structural definition. The Definition Model captures "what the product IS" (including that it supports multi-tenancy via Tenancy Architecture on Deployment Environment); the Run Track captures "what work EXISTS" to create and manage tenants. This follows the standard Definition → Work separation: Structural defines Capability; Build Track does the work of implementing it. Operational defines Deployment Environment (with Tenancy Architecture); Run Track does the work of managing Tenants within it.

### Customer vs. Tenant vs. Customer Segment — a three-level distinction

Customer Segment (Customer Value) is a category of potential buyers ("LATAM Enterprise 500+ employees"). Customer is a legal/contracting entity — an instance of a Customer Segment, not a Definition Model entity (the model captures types, not instances). Tenant is a logical isolation unit within a Deployment Environment, belonging to a Customer, with a customer-facing purpose (Production, UAT, Sandbox, Trial, DR). The key insight: a single Customer can have multiple Tenants in the same environment, each with a different purpose. This applies in both shared-tenancy and dedicated-tenancy architectures. Customer remains implied — acknowledged in relationships but not a first-class entity — to avoid crossing into CRM/operational territory.

### Deployment Environment purpose duality resolved

A Deployment Environment's "purpose" depends on vantage point — what the vendor calls "Production" may be the customer's UAT environment. Resolution: vendor purpose and customer purpose are separated. Vendor purpose (Production, Staging, Development, DR, CI/CD, Demo) lives on the Deployment Environment — it's how the vendor classifies and operates the infrastructure. Customer-facing purpose (Production, UAT, Sandbox, Trial, DR) lives on the Tenant (Run Track entity) — it's what this logical slice means to the customer. This eliminates the ambiguity: the Environment is "Production" (vendor operates it with production-grade SLOs); within it, Customer A has Tenant "A-Prod" (production use) and Tenant "A-UAT" (testing).

### UX Channel serves all human personas — Option A

UX Channel (User Experience) was initially scoped for User Personas only. The Operational discussion revealed that Operational Personas interact with the product through the same channel types: an SRE uses Web dashboards, receives Email alerts, runs CLI commands, gets Voice/IVR escalation calls, uses Mobile apps for on-call, and gets Chat bot notifications. The Interaction Modality (Web, Mobile, Chat, Voice, Email, CLI, Embedded) and Engagement Mode (Self-serve, Assisted, Managed) taxonomy is universal for any human accessing the product, regardless of whether that human is a customer or an operator. Rather than duplicating the channel concept in Operational, UX Channel stays in User Experience with its scope widened to acknowledge it serves Operational Personas as well. This is cross-dimensional referencing, not entity sharing — Operational Journey references UX Channels from User Experience, same as Ecosystem modules reference Structural modules.

### Operational is independent from User Experience — parallels are not inheritance

Structural parallels between dimensions should not be confused with inheritance or overlap. User Experience has User Persona, Job (JTBD), User Journey; Operational has Operational Persona, Operational Job, Operational Journey. Same analytical pattern (persona → job → journey), different domain (user experience vs. operational reality), different relationships, different quality criteria. Merging them would dilute both: User Experience's "User-Centric" focus would absorb operational concerns it doesn't own, and operational jobs would lose their connections to SLOs, Deployment Environments, and Operational Constraints. The same principle keeps Delivery Friction (Vendor Value) independent from Pain (Customer Value) and Developer Persona (Ecosystem) independent from User Persona (User Experience).

### Operational Personas are organized by quality taxonomy, not job titles

Initial proposal listed SRE, Platform Engineer, DevOps Engineer as distinct archetypes. These are often-overlapping organizational job titles, not functional archetypes. The corrected approach: organize Operational Personas by the Operational Quality Taxonomy dimensions — Reliability Operator (availability, incident response, SLO compliance), Security Operator (security posture, vulnerability management), Platform Operator (deployment infrastructure, CI/CD, environment provisioning), Data Operator (data integrity, backup, migration). Whether an organization calls the Reliability Operator "SRE" or "DevOps Engineer" or "Infrastructure Lead" is an Operating Model concern. The Definition Model captures the functional archetype — the same pattern as Win Stakeholder (typed by AAARRR stage, not by CRM job title).

### Operational Persona JTBDs exist in both Definition and Work Models

The Run Track work entities (Deployment, Incident, Change Request, Maintenance Task) are the instantiation of operational jobs — individual deployments, individual incident resolutions. But the definition of what those jobs ARE belongs in the Definition Model as Operational Job, because those definitions drive product investment decisions: "Deploy a release safely" requires a Deployment Console (Structural module); "Resolve a SEV-1 incident within SLO" requires a Monitoring Dashboard (Structural module). Without Operational Job in the Definition Model, operational tooling becomes accidental rather than intentional — built because "we needed something" rather than because "we identified this operational job and designed a capability to serve it." The chain mirrors User Experience: Operational Persona → Operational Job → enabled by Value Stream/Capability (Structural).

### Third-party ops tools are the product's integrated solution for operations

When the product ships a Datadog exporter, pre-built Grafana dashboards, a PagerDuty webhook integration, or a Terraform provider — those are product capabilities deliberately built for the Operations team. They are no different from an SAP Integration Module (Ecosystem) built for a customer's ERP team. This widens Ecosystem Integration Module's scope: Integration Modules serve Developer Personas, Programmatic User Personas, AND Operational Personas. The Operational Journey traces through both native operational modules (admin console, deployment dashboard) and integration modules to third-party ops tooling (Datadog, PagerDuty, Terraform). The "specific external system" an Integration Module bridges to can be a customer's system (SAP, Salesforce) or an operational tool (Datadog, PagerDuty).

### Operational Readiness is per-System, not per-process — distinct from Evolve Track

Evolve Track (Evolve) assesses process effectiveness: "Are our entity definitions serving their purpose? Are DoD criteria followed? Are artifacts meeting quality standards?" Operational Readiness assesses System readiness: "Is this System ready for production in this environment?" The criteria span the quality taxonomy — observability (logs, metrics, traces, SLIs), security (encryption, access control, vulnerability scanning), performance (benchmarks, load testing), operability (alerts, runbooks, admin controls), DR (backup, restore, failover). Operational Readiness is a Definition Model entity scoped to System (Technical) × Deployment Environment (Operational) — it captures the criteria definition and readiness state. The actual assessment work is Run Track activity, but the criteria definition belongs in Operational because "what makes a System production-ready" is a product-level concern, not a team practice. Module-level readiness ("is the Payments capability ready for production in LATAM?") is a derived view that aggregates across all Systems implementing that Module. SREs primarily think in Systems — they deploy, monitor, and operate `payments-service`, not "the Payments Module" — though they may refer to Module-level capability health when discussing integrated system behavior, especially since Module Versions are integration-verified Build Track artifacts.

### Operational Target carries achievement levers — connecting Operational to the Initiative framework

Operational Targets define what operational success looks like (e.g., "99.99% availability for payments service"). Like Win Outcomes (Vendor Value), they can be advanced by different levers: Product lever (build self-healing capabilities, improve error handling), Operational lever (improve incident response procedures, add redundancy, scale infrastructure). Making Operational Targets "lever-aware" connects Operational into the Initiative/Objective planning cycle: an Initiative with Operational lever weight drives Run Track and Operating Model work to improve operational targets. Operational Pains feed the Signal pipeline (Strategy), which drives Initiatives, which declare lever mixes, which flow work to the appropriate tracks. Without this connection, operational improvements happen outside the strategic planning framework.

### Cost targets are explicitly modeled across three entities

Infrastructure and operational cost is modeled through three complementary entities rather than a dedicated FinOps entity: Infrastructure Model carries a Cost Model field (the overall cost strategy — reserved instances, spot, committed spend, cost allocation approach), Operational Target of type Cost sets specific targets ("infrastructure cost per 1000 transactions < $0.50," "cloud spend growth must not exceed 1.5x traffic growth"), and Operational Pain surfaces cost issues as concrete suffering ("cloud spend grew 3x while traffic grew 1.5x"). This connects to Vendor Value Business KPI of type Cost ("Infrastructure Cost per Customer") — the commercial view of the same cost reality. The layering: Operational Operational Target (Cost) is the infrastructure-level objective; Vendor Value Business KPI (Cost) is the commercial-level metric derived from it.

---

## Session: Technical

*Scope: Technical reframing from code structure to technical model, Structural / Technical duality, ADR vs PDR, Technical Knowledge Base. References DR-024.*

### Structural and Technical are two lenses on the same product

Structural (Structural/Topology) provides the functional view: Product → Module → Capability → Feature, plus Value Streams that flow horizontally. Technical (Technical & Architectural) provides the technical view: Architecture Model → System → Component, plus Interaction Flows that show how Systems communicate. Where Structural says "the product has a Payments Module with Cross-Border Payments capability," Technical says "the Payments Module is implemented by payments-service (Java/Spring Boot) and payments-worker (Python), communicating via Kafka events, depending on PostgreSQL and a third-party FX rate provider." The two views serve different audiences — Structural serves PM and business stakeholders ("what the product does"); Technical serves architects and engineering leadership ("how the product is built"). Neither is complete without the other; together they give the full picture of the product's structure.

### System-to-Module mapping is many-to-many

The functional decomposition (Modules) and technical decomposition (Systems) are independent. A Structural Module "Payments" may be implemented by multiple Technical Systems (payments-api, payments-processor, payments-scheduler). A shared Technical System (notification-service) may serve multiple Structural Modules (Payments, Compliance, Onboarding). This many-to-many mapping is deliberate — it reflects reality. The functional boundary (what the product does) is not always the same as the technical boundary (how the code is organized). Forcing 1:1 alignment would either fragment modules into too-granular functional units or bloat systems into monolithic technical units. The explicit mapping makes the relationship visible and traceable.

### ADR and PDR are complementary decision records in different dimensions

PDR (Strategy) answers "what product decision was made and why?" — market decisions, capability decisions, channel decisions. ADR (Technical) answers "what architectural/technical decision was made and why?" — technology stack, system decomposition, integration patterns, data architecture. Three relationship patterns exist: (1) PDR triggers ADR(s) — "PDR: Go on LATAM market" triggers "ADR: Deploy LATAM services in sa-east-1 with LGPD-compliant encryption"; (2) ADR exists independently — purely technical decisions like "ADR: Adopt OpenTelemetry for distributed tracing"; (3) ADR constrains PDR — an architectural reality limits product options, forcing a PDR to justify the architecture change. The separation respects the dimensional structure: Strategy is Strategy & Intent; Technical is Technical & Architectural. They have different audiences, different governance, and different lifecycles. But they cross-reference each other, maintaining full decision traceability from product strategy through technical implementation.

### ADR has dual provenance — Discovery and Build

Some ADRs emerge from deliberate Discovery: an architecture deliberation asks "should we adopt event sourcing for the payments domain?" and produces an ADR. Other ADRs emerge during Build: while implementing an Epic, the team discovers the need to split a service and records the decision as an ADR. This dual provenance is natural — architectural decisions happen both proactively (strategic architecture planning) and reactively (implementation-driven learning). In the Discovery Track, Deliberation produces ADRs alongside PDRs. In the Build Track, the mechanism for ADR production will be defined when Build Track entities are detailed further. Both paths result in the same Technical entity; the provenance is tracked through the ADR's relationships.

### Technology choices are fields, not entities

Initially considered as standalone entities, technology choices were reconsidered: the choice IS the System/Component (its tech stack is a set of fields — language, framework, database, protocols), and the rationale IS the ADR. A standalone "Technology Choice" entity would duplicate information that already lives on Systems (what was chosen) and ADRs (why it was chosen). This follows the UPIM principle of avoiding entities that don't carry their own fields, statuses, and lifecycle. The technology stack fields on System and Component make choices visible; ADRs make the reasoning traceable.

### Architecture Model parallels Business Model and Infrastructure Model

Each well-developed dimension has a root entity that frames the domain: Business Model (Vendor Value) frames "how we make money," Infrastructure Model (Operational) frames "how we run it," Architecture Model (Technical) frames "how we build it." The Architecture Model captures the macro-level architectural strategy — style (microservices, modular monolith, event-driven, serverless), key principles (separation of concerns, domain-driven design, API-first), quality attribute priorities (maintainability, testability, extensibility), and architectural evolution direction. Like Business Model and Infrastructure Model, the Architecture Model changes at the scale of years, not quarters. It provides context for the more dynamic entities (Systems, Components, Dependencies, ADRs).

### Technical Knowledge Base parallels Operational Readiness

Operational Readiness (Operational) answers "is this System ready for production in this Environment?" with per-quality-dimension assessment. Technical Knowledge Base (Technical) answers "is this System's technical knowledge current and complete?" with per-knowledge-type assessment — architecture documentation, operational runbooks, release notes, integration guides, technical guides for Win teams, troubleshooting playbooks. Both are per-System assessment entities: a single instance per scope (Operational Readiness per System × Environment; Technical Knowledge Base per System), with quality dimensions and coverage status. Making documentation gaps visible in the Definition Model (rather than as implicit Work Model concerns) gives them strategic weight — a System with no runbook is an operational risk; a System with no integration guide is a Win Track impediment.

### Deprecation follows the waterline principle

The original Technical entities (Subsystem/Service, Class/Component, Function/Method) mapped to C4 architecture levels but at too-fine granularity for the Definition Model. Subsystem/Service is subsumed by the new System entity (reframed from C4 Container to "independently deployable technical unit that implements Modules"). Class/Component and Function/Method are below the waterline — code-level structure belongs in PSD/Build Track artifacts. This follows the same deprecation pattern applied across the model: Touchpoint (User Experience), Payload Schema (Ecosystem), Cluster/Host and Container/Process (Operational). The Definition Model captures strategic technical decisions; specific code structure is work artifact territory.

### Dependency makes external reliance explicit and manageable

The product depends on systems, services, and resources it doesn't own — third-party APIs (FX rate providers, bank networks), cloud services (AWS SQS, S3, Lambda), infrastructure resources (PostgreSQL, Redis, Kafka), and operational tools (Datadog, PagerDuty). Making these Dependencies first-class entities — with type, criticality, risk assessment, and alternative/fallback — enables several concerns: risk management (what happens when this dependency fails?), cost modeling (what does this dependency cost?), architectural evaluation (are we over-dependent on a single provider?), and operational planning (Operational Operational Constraints may flow from Dependency limitations). No other dimension captures external dependencies explicitly; Technical is their natural home.

### Interaction Flow is the technical realization of Value Stream

Structural Value Stream says "Cross-Border Payout Processing traverses Invoice Module → FX Module → Compliance Module → Payment Module → Settlement Module." Technical Interaction Flow says "payment request enters via REST at payments-api → FX rate fetched via gRPC from fx-service → compliance check via async Kafka event to compliance-service → payment executed via REST to bank-adapter → settlement confirmation published as Kafka event." Same flow, different lens: Value Stream is the functional narrative (for PMs); Interaction Flow is the technical narrative (for architects). Interaction Flows capture integration style (sync/async, request-reply, event-driven, batch), protocol, data format, sequence, error handling strategy, and retry/compensation patterns. They anchor sequence diagrams and data flow diagrams — the entity defines the pattern; the diagram is a visualization artifact.

---

## Session: Dimension 7 — Operations Decision Record (ODR) — Completing the Decision Record Triad

### The decision record triad: PDR / ADR / ODR

The Definition Model had PDR (Strategy — what to *do*) and ADR (Technical — how to *build*), but no decision record for how to *run*. Significant operational decisions — cloud provider selection, deployment strategy, data governance, DR/BCP, tenancy isolation — were either shoehorned into ADRs or remained tribal knowledge. ODR (Operational) completes the triad. Each record type has its own audience (PM / Architect / SRE), governance (product council / architecture review / operations review), scope (strategy / design-time / runtime), and dimension. The triad provides complete decision traceability across the product lifecycle: what to do, how to build it, how to run it.

### PDR → ADR → ODR trigger chain

Decisions cascade across levels: "Go on LATAM market" (PDR) triggers "Deploy LATAM services in sa-east-1, event-driven architecture" (ADR) triggers "LGPD-compliant encryption in sa-east-1, MSK 3-AZ with 7-day retention, dedicated tenancy for Tier-1 banks, 4-hour RTO" (ODR). Each level refines the previous with domain-specific expertise — a PM doesn't choose encryption algorithms; an architect doesn't choose DR site locations; each decision has its own context, alternatives, and consequences. The trigger chain also works upward: ODR constrains ADR ("4-hour RTO means active-active isn't justified"), ADR constrains PDR ("batch architecture can't support real-time FX").

### ODR scope: ten categories of operational decisions

ODR covers a wide scope: Cloud Provider & Services (AWS vs. GCP, MSK vs. self-managed Kafka), Deployment Strategy (blue-green, canary parameters), Tenancy & Isolation (dedicated vs. shared schema), DR & BCP (RTO/RPO, failover topology), Data Governance (PII classification, encryption, access control), Data Archival (cold storage timing, retention periods), Observability & Tooling (APM selection, log retention), Compliance Zone (PCI scope, data residency enforcement), Capacity & Scaling (auto-scale thresholds, reserved vs. on-demand), Cost Optimization (reserved instance commitments, right-sizing). The Category field provides structured classification without requiring separate entities per domain.

### Data governance in ODR vs. data domains in Data

Operational aspects of data — retention periods, archival policies, encryption requirements, access control models, backup strategies — belong in ODR (Operational). They are decisions about how data is governed at runtime. Data (Data & Information, to be detailed) captures the structural view — what data the product manages and makes available, domain boundaries, ownership, schema, relationships. The split is clean: Data = what data exists (structural); ODR = how that data is governed operationally (runtime). This mirrors the Structural / Technical duality: functional structure vs. technical realization, applied to data.

### ODR dual provenance: Discovery Track and Run Track

Like ADR (Discovery + Build), ODR has dual provenance. Strategic operational decisions (cloud provider selection, tenancy architecture, initial DR strategy) originate from Discovery Track Deliberations. Operational-experience decisions (deployment strategy change after incident patterns, data retention increase after regulatory change, capacity adjustment after load testing) originate from Run Track work. Both paths produce the same Operational entity; the provenance is tracked through relationships. This gives the Run Track its own decision-making capability — previously, only Discovery (PDR) and Build (ADR) tracks formally produced decision records.

### ODR fills the Infrastructure Model justification gap

Operational's Infrastructure Model says "Multi-region AWS SaaS with active-passive DR and hybrid tenancy." But why AWS? Why active-passive? Why hybrid tenancy? Previously, the Infrastructure Model was "Justified by PDR" — but PDR doesn't capture "why MSK over self-managed Kafka." ODR fills this gap: the Infrastructure Model is now justified by both PDRs (strategic product decisions) and ODRs (operational decisions). Similarly, Deployment Environment configuration, Operational Target values, and Operational Constraint enforcement are now traceable to specific ODRs.

---

## Build Track Detailing — Work Entities, Artifacts, and Scoping

### Work entities vs. work artifacts: a universal distinction, sharpened by the Build Track

Every track in the Work Model produces both work entities (*work to be done* — with assignees, sprints, effort-driven status lifecycles) and work artifacts (*things produced by work* — emerging from completed work with quality-gated or completion-gated lifecycles). Discovery produces Deliberations (work entity) and PSDs, PDRs, ADRs (artifacts). Run produces Incidents and Change Requests (work entities) and Post-Incident Reports (artifacts). Win produces Win Cases (work entity) and resolution records (artifacts). The distinction is universal, not track-specific.

The Build Track made this distinction especially visible because earlier modeling had conflated the two categories: Epics, Stories, and System Versions were all treated as undifferentiated "Build Track things." Separating them — Epic, Story, Technical Task, Bug, Integration Epic, Integration Story as work entities; System Version, Module Version, Product Version, ADR, Technical Debt Item as work artifacts — clarified the track's structure. An Epic is not the same kind of thing as a System Version, even though both appear in the Build Track. This parallels a distinction in manufacturing: a work order (instruction to do something) is not the same as the widget it produces.

### Module scope for Epics, System scope for Technical Tasks: the functional-to-technical bridge

The scoping split — Epics and Stories at Module level (Structural), Technical Tasks at System level (Technical) — mirrors how organizations actually work. PMs think in capabilities and modules: "build real-time FX rate locking for the FX Module." Engineers think in systems and components: "implement the gRPC GetRate endpoint in fx-service." The Story sits at the junction — it speaks Module language ("lock FX rate for 24 hours") but is implemented by System-scoped Technical Tasks. A single Story often spawns Tasks in multiple Systems because the Module-to-System mapping is many-to-many. This scoping split keeps Epics accessible to product stakeholders (they don't need to know about fx-service internals) while giving developers work items at the right granularity.

### Three-tier versioning: composite systems and communication bridges

System Version → Module Version → Product Version is not arbitrary layering. Each tier is a **system in its own right** — with increasing composition scope and emergent properties at each level. System Version is an atomic system (a single deployable). Module Version is a **composite system** — its constituent Systems interact to produce emergent properties (end-to-end latency, integrated failure modes, cross-system data consistency) that don't exist at the individual System level. Product Version is a **higher-order composite system** — its constituent Modules interact to produce product-level properties (end-to-end user journeys, cross-module workflows, product-wide availability and compliance posture). All three tiers are operable, observable, and operationally meaningful — they are not verification checkpoints on an assembly line.

Each tier also serves as a **communication bridge** at a progressively broader organizational scope. System Version is the shared vocabulary between Build and Run teams — engineers build `payments-service v2.3.3` and SREs deploy and monitor it. Module Version bridges Build, Run, and Product teams — Product managers reason in Modules ("Payments capability v4.1"), SREs monitor integrated capability health, Build teams know which Systems compose it. Product Version is the **ubiquitous language** across all teams and customers — Win teams reference it in support cases ("customer X is on v3.2"), Release Notes are written against it, compliance certifies it, customers identify what they're running. Without Module Version and Product Version, these teams have no shared reference points and resort to ad-hoc translation between service names, feature names, and marketing labels.

The three tiers also reduce verification risk at different scopes: System-level quality gates, Module-level integration verification, Product-level certification. Without the middle tier, you jump from individual System testing to full-product testing — an O(n²) integration problem instead of Module-scoped O(k) verification. See `stories/versioning-alternatives-analysis.md` for how alternative approaches (monorepo, contract testing, GitOps, release trains) address these challenges and where they leave gaps.

### Integration Epics: making cross-System work visible

When Release Planning decomposes PSDs into Epics across Modules, it naturally surfaces cross-System integration needs: "the Payments Epic and the FX Epic require payments-service and fx-service to communicate." In traditional models, this integration work hides inside feature Epics as an afterthought — developers discover mid-sprint that they need to define an API contract, write integration tests, and handle error scenarios. Integration Epics make this work visible from the start. They reference the PSD-derived Epics they integrate, they validate Interaction Flows (Technical), and they produce the integration contracts and test suites that feed Module Version verification. The Integration Epic → Integration Story → Technical Task decomposition parallels the regular Epic → Story → Technical Task hierarchy.

### Design Deliberation: the Build Track's decision-making mechanism

Discovery Track has Deliberation (producing PDRs, ADRs, ODRs). The Build Track now has Design Deliberation (producing ADRs). This completes the architectural decision lifecycle: strategic architectural decisions originate from Discovery Deliberation during product planning; tactical architectural decisions originate from Design Deliberation during implementation. "Should we adopt event sourcing?" is a Discovery Deliberation question. "Should we use gRPC or REST for this specific service-to-service call?" is a Design Deliberation question. Both produce the same ADR entity (Technical) — the provenance differs but the artifact is identical. Without Design Deliberation, implementation-time ADRs exist as orphaned documents — they appear in the system but have no traceable origin in the Work Model.

### Technical Debt as artifact, not work entity

Technical debt is a pervasive concern in engineering organizations, but it doesn't fit cleanly as a work entity. You don't "do" a Technical Debt Item the way you "do" a Story or Task. Debt is *discovered* and *documented* during work; it is *resolved* through existing work entities (Epics and Stories). Making Technical Debt Item an artifact means it can be cataloged, prioritized, and competed against feature work for sprint capacity — all without introducing a parallel tracking system. When debt is prioritized, a regular Epic or Story is created to resolve it, linking back to the Technical Debt Item for traceability. This keeps the work entity hierarchy clean while making debt visible.

### Interaction Flow: naming for concrete technical realization

The Technical entity formerly called "Interaction Pattern" was renamed to **Interaction Flow**. "Pattern" suggests an abstract template — something reusable and non-committal. But each instance of this entity is concrete and specific: ordered steps, named Systems, specific protocols, explicit timeouts, defined error handling. It describes *what happens* when a Value Stream executes, not what *could* happen. "Flow" conveys sequential motion and commitment — the same quality that makes "Value Stream" effective in Structural. The rename also disambiguates from the Ecosystem usage of "interaction pattern" (Command, Query, Event, Callback, Batch), which classifies the *style* of a single API Operation rather than a multi-System execution path. Two uses of "pattern" in the model — one for an entity name, one for a classification axis — would have created confusion. The rename eliminates it.

## Composition Levels, Module Package, and Run Track Engineering

> **Superseded by DR-036 (Seeds 16–17).** Retained for design history. Do not use for current modeling.

*Scope: Composition levels formalization (atomic/integrated/complete), Module Package and Product Package as Run Track artifacts, Run Track engineering work entities (Run Epic, Run Story), binding configuration on Module Version, System Purpose field, Build Track two-layer framing. References DR-027.*

### Specification layer and execution layer within the Build Track

The Build Track contains two implicit layers that mirror how organizations actually work. The **specification/commitment layer** — Epics, Stories, Integration Epics, Integration Stories — defines *what* to build in Module (Structural) language. These entities inherit product intent from PSDs, carry acceptance criteria, and are defined by PMs and Tech Leads. They feel like specification entities because they *are* — they specify committed scope in functional language. The **execution layer** — Technical Tasks, Sub-Tasks — defines *how* to implement in System/Component (Technical) language. These entities are assigned to individual developers, scoped to specific Systems, and speak engineering language. The Story sits at the junction: it speaks Module language ("lock FX rate for 24 hours") but decomposes into System-scoped Technical Tasks. This two-layer structure is not a deficiency — it's a bridge between product intent and engineering execution. PSDs define what the product *should become* (aspirational, unbounded). Epics define what we *commit to building now* (time-bound, capacity-constrained). Stories define *functional increments within that commitment*. Technical Tasks define *what each developer does*. Each layer narrows scope and increases concreteness.

### Composition Levels: atomic, integrated, complete

The product is a hierarchy of deployable systems at three composition levels. **Atomic** — System (Technical): an independently buildable, deployable, operable technical unit (e.g., `payments-service`). **Integrated** — Module (Structural) realized through Module Version/Package: a composite system of Systems with emergent operational properties (end-to-end latency, integrated failure modes, cross-system data consistency). **Complete** — Product realized through Product Version/Package: the highest-order composite system with product-level emergent properties (end-to-end user journeys, cross-module workflows, product-wide compliance posture). All three levels are operationally real — deployable, monitorable, subject to incidents. "System" without qualification refers to the Technical atomic level. Module and Product are their own terms at their own composition levels. When we say "Module Version is a composite system," we use "system" in the systems-thinking sense (interacting parts with emergent properties), not as a reference to the System entity (Technical).

### Module Package: the Run Track's environment-independent deployable enrichment of Module Version

The Build Track produces Module Version — a functionally complete, commercially viable assembly of all tenant-serving Systems (product logic, subscription lifecycle, commercialization, integration adapters) plus binding configuration. What's deployed includes both this tenant-serving assembly and operator-facing support systems. The Run Track adds Systems built by operators to automate their own work — custom probes, scheduled reconciliation jobs, dashboards, log shippers, self-healing agents — and operational wiring to produce **Module Package Version** — an environment-independent composition. Module Package Version defines *what operator-facing systems accompany the Module*; the MDD (Module Deployment Descriptor) defines *how* and *where* the full composition is deployed. The boundary is ownership and provenance: if the Run Track builds it to solve their own pains, it goes in the Package; if the Build Track builds it as a product capability (even one targeting an operator persona), it stays in Module Version. Both paths are valid and complementary. Product Package Version follows the same pattern at the product level: Product Version plus Module Package Versions and cross-module operator-facing wiring, deployed via PDD.

> **DR-029 update:** Module Package is now a Operational Definition Model specification. The Work Model artifact has been renamed to Module Package Version. See also the seed 'Module Package specification vs. Module Package Version: the template and the instance.'

### The Run Track as engineering track: operational systems have code, tests, and versions

The Run Track is not just an operational track — it is also an engineering track. Custom probes, reconciliation jobs, cert rotation automation, environment-specific adapters — these are legitimate Systems with code, repos, CI/CD pipelines, tests, and System Versions. They are independently deployable. They differ from product Systems in purpose (they serve SRE/Operator personas rather than end-user personas) and provenance (Run Track engineering, not Build Track engineering). The Run Track has its own Epic/Story/Task hierarchy — Run Epics (Module-scoped, like Build Track Epics) decompose into Run Stories, which decompose into Run Track Technical Tasks scoped to operational Systems. Technical Task is a per-track concept: each engineering track owns its Technical Tasks with the same entity structure but distinct track ownership. Run Deliberations produce ODRs (Operational), not ADRs (Technical). The operational System Versions produced by this engineering work enrich Module Versions into Module Packages.

### Binding configuration: legal composition, not just assembly

Module Version's binding configuration is not mere wiring — it is **scoped, constrained, and deliberate**. When the Build Track composes System Versions into a Module Version, it makes composition-level decisions: which adapter to include, which protocol version to bind, which capability set to activate. These are build-time choices that determine *what this composition is intended to deliver* and *what it is not*. Not all possible combinations of System Versions are valid — some are incompatible, some would produce unexpected functionality. The binding configuration constrains the composition to its legal form: service mesh routes, event topic bindings, orchestration definitions, and composition constraints that enforce scoped functionality. This is analogous to compile-time feature flags or conditional dependency inclusion — the composition artifact is a deliberate selection, not an unconstrained assembly.

## Deployment Descriptors: SDD, MDD, PDD

> **Superseded by DR-036 (Seeds 16–17).** Replaced by System Deployment Specification and Product Deployment Specification. Retained for design history.

*Scope: Deployment descriptors as environment-specific specification layer; four-layer model (build artifact → run artifact → deployment descriptor → deployment act); three independent version streams at the integrated level; MDD as a system; tenant config vs. deployment config boundary. References DR-028.*

### The four-layer model: from build to production

Four distinct layers exist between code and production at each composition level. **Layer 1: Build artifact** (System Version, Module Version, Product Version) — functionally verified, quality-gated output of the Build Track. **Layer 2: Run artifact** (Module Package Version, Product Package Version) — environment-independent, adds operator-facing systems (probes, dashboards, reconcilers, log shippers) for observability and maintainability. **Layer 3: Deployment descriptor** (SDD, MDD, PDD) — environment-specific deployment specification with configuration, scripts, and runtime artifact references. **Layer 4: Deployment** — the operational act of applying a descriptor to an environment. Each layer has its own lifecycle, its own version, and its own ownership. Conflating any two layers — embedding environment config in the deployable artifact, or mixing deployment scripts with operational wiring — creates coupling that undermines independent evolution and multi-environment reuse.

### Deployment descriptors: the environment-specific specification layer

The model separates *what is deployed* (Module Package — environment-independent) from *how it is deployed here* (MDD — environment-specific). This separation is not bureaucratic overhead — it solves real problems. A single Module Package can be deployed to staging, production-us, and production-latam via three different MDDs, each with appropriate resource sizing, monitoring thresholds, and deployment scripts. When production-latam needs a monitoring threshold adjustment, only the LATAM MDD version increments — no rebuild, no re-enrichment. When a new migration script is needed for a production database, it is authored within the MDD — versioned, reviewed, and traceable as part of the deployment specification, not as a loose script alongside the deployment. SDDs (System Deployment Descriptors) handle the atomic level — mapping System Versions to runtime-defined artifacts (K8s resources, cloud-native primitives) with environment-specific configuration. MDDs compose SDDs by reference and add Module-level coordination. PDDs compose MDDs and add product-level orchestration.

### MDD as a system: scripts, validation, and rollback

The MDD is not just configuration — it is a **system in its own right**. It contains executable logic: pre-rollout scripts (database migrations, cache warming, feature flag activation), validation scripts (post-deployment health checks, integration smoke tests, SLA verification), and rollback scripts (migration reversals, state restoration, flag deactivation). Creating or modifying these scripts is engineering work — performed as sub-tasks of Deployment Planning Tasks. The MDD is authored, tested, reviewed, and versioned like code. This is why the MDD has its own version stream: a new migration script is a deployment-progression change (MDD version bump), not a functional change (Module Version) or an operator-facing change (Module Package Version). The MDD's scripts are the operational boundary between "what we deploy" and "what we guarantee about the deployment."

### Three independent version streams at the integrated level

At the Module level, three version streams co-exist: Module Version (functional — what product code changes), Module Package (operational — what operational systems and wiring are included), and MDD (deployment — how it deploys to a specific environment). These streams change at different rates and for different reasons. Module Version changes when developers ship new features. Module Package changes when SREs add a new probe or update operational wiring. MDD changes when DevOps adjusts resource limits, adds a migration script, or tunes monitoring thresholds for a specific environment. The independence is the point — each concern evolves on its own timeline without forcing changes in the others.

### Tenant config vs. deployment config: the runtime boundary

A critical boundary separates deployment-time configuration (in descriptors) from runtime-discovered configuration (in tenant systems). Deployment descriptors configure the *platform* — how systems run in an environment. Tenant configuration configures *behavior* — what features are enabled for a specific tenant, what rate limits apply, what branding is shown. These have different lifecycles: a new tenant can be onboarded without redeploying, and a deployment can change resource limits without affecting tenant settings. If an MDD contains tenant-specific values, it is a sign that deployment configuration and tenant configuration have been conflated. The MDD should never know about individual tenants — it configures the platform that serves all tenants in that environment.

## DR-029: Change-to-Deployment Workflow Redesign

> **Superseded for deployment/versioning semantics by DR-036 (Seeds 16–17).** Seeds below remain valid for Change Request, Deployment Train, and Verification Task patterns; replace Package/MDD references with System/Product Deployment Specification.

*Scope: Deployment Train, Change Request, Deployment Plan, Module Package vs Module Package Version, Verification Task. References DR-029.*

## Seed 1: Deployment Train: the contractual promotion path

The notion that a promotion path through environments is not just a technical convenience but a contractual construct. The Deployment Train tells tenants "your code will traverse these environments in this order with these soak times." When a payment processing tenant signs a contract referencing "PCI Regulated Train," they're relying on the promotion path for planning changes to their dependent applications. The same Deployment Environment can be a Station in multiple Trains with different governance requirements — staging-eu might be a 72-hour soak stop on the PCI Regulated Train but a zero-wait automated stop on the Fast-Track Train.

## Seed 2: Change Request as the auditable change management envelope

Every deployment to a governed environment goes through a Change Request — not because bureaucracy is good, but because regulated fintech demands audit trails. The Change Request scopes to a Deployment Train or Station, not to an environment directly. Three types reflect three realities: Standard (planned, CAB-reviewed), Emergency-Technical (incident-driven, abbreviated soak), Emergency-Business (business exigency like a campaign deadline, compressed but not skipped governance). A Change Request is "complete" only when all Deployment Tasks succeeded AND all Verification Tasks passed — deployment success alone is not enough.

## Seed 3: Deployment Plan as deliberation: learning while planning

The Deployment Plan is where the Run team discovers what they don't know. Like Discovery Track deliberations that produce PDRs and signals, the Deployment Plan is a deliberation activity that produces Deployment Planning Tasks, discovers maintenance prerequisites, identifies verification needs, and may trigger Deployment Drill Tasks. It's not a rigid waterfall gate — it's the structured space where operational knowledge is generated. The plan may evolve as planning tasks reveal new information (MDD scripts need database migration, staging environment needs capacity scaling).

## Seed 4: Module Package specification vs. Module Package Version: the template and the instance

> **Superseded by DR-036.** Product Specification (Technical) replaces Package specifications.

The Module Package (Operational) answers "what operator-facing systems and wiring are added to this Module?" The Module Package Version (Run) answers "which specific versions are assembled right now?" This follows the pattern Module (Structural) → Module Version (Build). The specification is stable and reusable — when you add a new probe to the Payments Module Package spec, it tells everyone "from now on, Payments always includes this probe." The version is specific and changing — v2.3.0 uses healthcheck v1.2.0, but v2.4.0 might use healthcheck v1.3.0.

The boundary is about ownership and provenance, not about who benefits. Everything an operator does ultimately benefits tenants — a self-healing service that restarts failed pods restores service for tenants, but it automates operator work and is built by the Run Track, so it belongs in the Package. Meanwhile, Module Version may also address operator needs: the product team might build an admin console or deployment API as first-class product capabilities. The difference: if the Run Track builds it to solve their own pains, it goes in the Package. If the Build Track builds it as a product capability (even one targeting an operator persona), it goes in the Module Version. Both paths are valid — operators should have the ability to solve their own pains through their own engineering, and the product should also invest in operator experience as a first-class concern.

## Seed 5: Verification Task: making post-deployment verification auditable work

Verification after deployment is not a check-the-box afterthought — it is a first-class work entity with criteria, evidence, and pass/fail results. Verification Tasks make the post-deployment phase visible, trackable, and auditable. They can be smoke tests ("can the service respond?"), SLA verification ("P95 latency < 300ms for 24 hours"), compliance checks ("PCI scan passes"), or business validation ("payment corridor active for BRL"). They are created during Deployment Planning (proactive) or added directly to Change Requests (reactive). Change Request closure requires all Verification Tasks to pass.

## Seed 6: Incident as artifact: separating the observation from the response

An Incident is not work — it is an observation. Something went wrong: a latency spike, a database failover, an error rate surge. The Incident record captures *what happened* with structured fields for severity (SEV-0..4), affected scope (Systems, Modules, Environments, Tenants), customer impact, SLA breach, and timeline. It does not capture what anyone did about it.

This separation parallels the Deployment pattern (DR-029): a Deployment Task (work entity) produces a Deployment (artifact/record). Similarly, System Monitoring alerts, operator observations, or Win Case complaints produce Incident records, and Incident Response Tasks respond to them. The benefit is the same: you can independently assess what happened and how well the organization responded.

Three work entities handle the incident lifecycle:

1. **Incident Response Task** — triage, investigate, mitigate, resolve. Its DoD is "service restored to SLO-compliant state" — root cause fix is not its job. Root cause fix is downstream: a Bug for the Build Track, a Run Epic for operational tooling, a Signal for Discovery.

2. **Post-Incident Review** — the Run Track's deliberation entity. Parallels Discovery Deliberation and Win Review. Produces the Post-Incident Report (durable knowledge artifact) and routes corrective actions to appropriate tracks. SEV-0, SEV-1, and SEV-2 incidents require PIR; the Operating Model may adjust this threshold.

3. **Customer Communication Task** — status page updates, tenant notifications, resolution summaries. Run Track owns this because SRE/DevOps has real-time technical context. Win Track consumes summarized views in QBRs and Win Reviews.

The Incident artifact is not just a historical record — it is a live evidence entity that feeds multiple assessment loops:

- **SLA breach tracking:** Each incident evaluates whether Service Commitments (Customer Value) were breached. This feeds Customer Value Metrics.
- **Error budget consumption:** Each incident erodes Operational Targets (Operational). Over time, incident history reveals whether targets are achievable.
- **Readiness assessment:** Incident patterns per System x Environment reveal Operational Readiness (Operational) gaps — "payments-service has 3 SEV-1s in LATAM but zero in NA."
- **Operational Pain evidence:** Recurring incident patterns are concrete evidence for Operational Pains (Operational).
- **Run Track planning:** Incident history informs Deployment Planning (deployment risk), Capacity Planning (capacity incidents), and Run Epic scoping (operational tooling gaps) — not just PIR and Discovery.

Incident correlation prevents inflated counts: a Parent Incident (database failover) with child incidents (FX latency, payment timeouts, settlement delays) is 1 root cause, not 4 incidents. The Caused By field closes the deployment-to-incident loop: "this SEV-2 was caused by Payments MDD v3.1 deployment to LATAM."

## Seed 7: Hotfix as a named pattern: P0 Bug to Emergency System Version

> **Operational update (DR-036):** Replace SDD with **System Deployment Specification** in the chain below.

A SEV-0 incident at 2 AM needs a code fix in production within hours, not days. The UPIM models this as a **named pattern** spanning Build and Run tracks, not a separate workflow.

The fast-path uses the same entities as standard work but with explicit conventions: P0 Bug → sprint bypass → Technical Task (immediate allocation) → System Version (Emergency gate profile) → SDD → Emergency-Technical Change Request (abbreviated soak, documented waivers) → Deployment Task → Deployment → Verification Task.

Two complementary fast-paths in different tracks make this work. The Build Track fast-path (DR-031) answers "how fast do we fix?" — P0 means sprint bypass, Emergency gate profile means peer review + security scan + smoke tests are non-negotiable but full regression and performance benchmarks are deferred. The Run Track fast-path (DR-029) answers "how fast do we deploy?" — Emergency-Technical CR means abbreviated soak and documented waivers. Neither is sufficient alone.

The critical constraint is the **deferred-gate obligation**: an Emergency System Version is not the end of the story. The originating Bug stays at `Fixed` (not `Closed`) until a subsequent Standard System Version passes all deferred gates. This prevents "we shipped it as an emergency, full tests never ran" from becoming permanent technical debt. The Bug entity is the natural tracker — it already stays open until the defect is fully resolved and verified.

This pattern is convention-based, not structurally enforced. P0 = sprint bypass is a convention that teams must know and honor. The Emergency gate profile is recorded on System Version (auditable), and the deferred-gate obligation is tracked on Bug (queryable). The Operating Model determines the sprint-bypass mechanism (interrupt capacity, dedicated on-call) and the hotfix branch strategy (branch from release tag, cherry-pick to main).

---

## Seed 8: FIR — Universal Intake: Why Every Feedback Starts the Same Way

The FIR (First Information Report) is the UPIM's answer to a fundamental traceability problem: when a customer calls about a latency spike, that single event may produce an Incident (Run), a Bug (Build), a Signal (Strategy), and a Win Case complaint (Win). Without a common parent, these are four disconnected work items with no shared origination record. Nobody can answer "what happened, who reported it, and what did we do about it?" holistically.

FIR solves this by adopting the **ITSM single-point-of-contact principle** and extending it across all tracks. Every piece of product-in-operation feedback — customer complaint, monitoring alert, SRE observation, QA regression report — enters the system as an FIR in PFR-Win. The Win team's triage function then routes: the full FIR or specific sub-parts go to the appropriate tracks as sub-items (Incident, Bug, Signal, Win Case, Maintenance Task). All sub-items carry an `Originating FIR` reference back to the parent; the FIR carries a `Sub-Items` list forward. Bidirectional.

The **always FIR-first** principle means Win Cases cannot be created independently. Even when a Win team member discovers a complaint during a QBR, they log an FIR first. The overhead is minimal — trivial inquiries can be resolved directly at triage with zero sub-items — but the traceability benefit is significant. FIR volume metrics become the single authoritative measure of the total feedback burden.

FIR parallels Change Request in the Run Track: Change Request is the governance envelope for deployment-related work; FIR is the intake envelope for all product-in-operation feedback. Both are parent entities whose lifecycle depends on the completion of their sub-items. The reporter interacts with the FIR lifecycle (notified on triage, updated on progress, notified on resolution), while sub-items represent track-specific internal work.

Auto-routing is permitted for monitoring alerts — a Provenance field (`External`/`Run`/`Build`/`Internal`) distinguishes human-triaged from auto-routed FIRs. The Operating Model defines which categories and provenances permit auto-routing.

Key tension resolved: Run teams create FIRs too. If only the Win team created FIRs, monitoring alerts and QA observations would bypass universal intake and PFR-Win would be incomplete. All teams create FIRs; PFR-Win becomes the comprehensive, single origination point.

See DR-032 for the six decisions and entity file `track4-fir.md` for full field/status/relationship definitions.

---

## Seed 9: Role vs. Agent — The Triad of Role → Agent → Work

The UPIM has persona/stakeholder entities in four dimensions: Win Stakeholder (Vendor Value), User Persona (User Experience), Developer and Programmatic User Persona (Ecosystem), Operational Persona (Operational). These describe *what* a role is — responsibilities, JTBD, outcomes, barriers. They are abstract, durable, and product-scoped.

Separately, the Workforce Repository (WFR) tracks *who* — specific people or AI agents enrolled to pick up work across tracks. And the Work Repository (WR) tracks *what they are doing* — live work instances.

This creates a clean triad: **Role (Definition Model) → Agent (WFR) → Work (WR)**.

- "What function is needed?" → the role definition in Vendor Value/User Experience/Ecosystem/Operational
- "Who can do it?" → the agent in WFR, bound to one or more role definitions
- "What are they doing?" → the work item in WR, assigned to an agent

The same person may fill multiple roles (startup scenario). Multiple people may fill the same role (enterprise scenario). The binding between person and role is an organizational/workforce concern (WFR), not a product definition concern (Definition Model).

**Why not just put agents in the Definition Model?** Because "the product needs a Pre-Sales Engineer function" is a product definition statement. "John Smith is a Pre-Sales Engineer and is also filling the CS Manager role this quarter" is a workforce statement. Conflating them makes the Definition Model fragile — it changes every time someone joins, leaves, or changes roles.

**Where do external stakeholders go?** Not in WFR. Customers, partners, prospects, and third-party developers are tracked in the External Stakeholder Registry (ESR) — a reference layer (projection from CRM/source systems). External parties are consumers of the product, not agents in the vendor's work model. They are referenced in work items (FIR reporters, Win Case customers, Incident affected tenants) but do not pick up work across tracks.

The cross-dimensional pattern is explicit: every persona entity in the Definition Model now carries a blockquote clarifying "this is a role definition, not an agent identity" with references to WFR and DR-034.

See DR-034 for the four decisions.

---

## Seed 10: Repository Architecture — 15 Repositories, 3 New

The Foundry repository architecture evolved from 11 to 15 repositories (including PFR sub-partitions) to align with the UPIM's 9 dimensions and 5 tracks. Three forces drove the expansion.

**Force 1: Build-time vs. run-time separation.** CAR (Code Artifact Repository) was holding deployment descriptors, incident records, and operational artifact versions alongside source code. These have different ownership (SRE/DevOps vs. developers), different lifecycle (deployment progression vs. build progression), and different governance (change management vs. CI/CD). OPR (Operations Repository) gives Run Track artifacts their own home. The verification evidence split follows the same logic: QVS for build-time quality evidence (tests, scans), OPR for run-time quality evidence (deployment verification, post-deployment SLA checks).

**Force 2: Feedback ownership alignment.** PFR was monolithic — feedback from Win, Run, and Build tracks had different ownership and lifecycle needs. PFR-Win (FIRs, Win Cases, customer communication records) is owned by the Win team. PFR-Run (incident mirrors referencing OPR) is owned by SRE/DevOps. PFR-Build (bug mirrors referencing WR) is owned by QA/Engineering. The key distinction: OPR and WR are the systems of record; PFR-Run and PFR-Build hold references/mirrors for the feedback perspective. PFR-Discovery was removed — Signals route directly from FIRs into PIR.

**Force 3: External stakeholder references.** External stakeholders are referenced extensively across the model (FIR reporters, Win Case customers, Incident affected tenants, Customer Release targets). Without ESR, these references were scattered. ESR provides a single, UPIM-internal reference point — but as a reference layer (projection from CRM), not a system of record.

Two renames accompanied the expansion: PIR (formerly "Product Idea Repository") became "Product Intent Repository" to reflect its expanded scope across Strategy, Vendor Value, and Customer Value. AWR became WFR (Workforce Repository) because "Agent" in current discourse is heavily associated with AI agents, and the repository tracks all internal workers — human and AI alike.

See DR-033 for the six decisions and `foundry/repositories.md` for the full architecture.

---

## Seed 11: Module Functional Classification — From Architecture Archetypes to Customer Value Vocabulary

**Scope:** Structural, Module entity, draft-archetypes.md

The question "what type of module is this?" has two valid answers depending on who is asking. An architect asks "how is it built?" (interaction model: HI, Programmatic, Reactive). A product manager asks "what does it do for the customer?" (functional role: Record, Engagement, Intelligence). The UPIM originally used the architect's answer at the Module level — Module Archetype (HI/Programmatic/Reactive) — because the same vocabulary drove PSD template selection. This conflated two concerns.

The resolution came from the "Twelve System Types" framework in the product thesis (`gap.md`), which classifies enterprise systems by the business capability they provide — Record, Enforcement, Data, Engagement, Action, Intelligence, Identity, Influence, Memory, Product, Innovation, Integration. This vocabulary answers the PM's question, not the architect's. It is customer-value-oriented and domain-specific (FinTech/banking). The field is named `Functional Classification` — avoiding the word "type" (too generic) and "system" (already used for Technical entities).

DDD's Core/Supporting/Generic was considered and rejected: it answers "how strategically important is this domain to engineering?" — an architecture and team-topology concern (Technical territory), not a customer-value concern (Structural territory).

See DR-035 D4.

---

## Seed 12: Capability Templates — PM's Specification Language, Decoupled from System Archetypes

**Scope:** Structural Capability entity, dim1-psd.md, psd-templates/

The old PSD had a single `Module Archetype` field (HI/Programmatic/Reactive) in the header, chosen by the PM. This field was doing two jobs: (1) classifying the module's primary interaction model, and (2) selecting the PSD depth profile (which dimensional sections were "Deep" vs "Light"). When Module classification moved to Functional Classification (customer-value vocabulary), the question arose: what drives PSD template depth now?

The answer required recognizing that a Module may contain Capabilities of multiple interaction types. An "Engagement Module" (Functional Classification) may have: a Capability that needs UX specification (formerly HI), a Capability that needs API contract specification (formerly Programmatic), and a Capability that needs processing intent specification (formerly Reactive). Template selection at the Module level was an oversimplification.

The resolution: Capability Templates are PM-facing specification guides applied at the Capability level, not the Module level. Renamed from HI/Programmatic/Reactive to `Experience/Integration/Processing` to make clear they are specification guidance labels, not architectural classifications. System/Component Archetypes remain in Technical, independent of Capability Templates — a deliberate decoupling. A PM specifying an "Experience Capability" is not prescribing that an HI System will realize it; the Architect makes that decision independently.

See DR-035 D5, D13.

---

## Seed 13: System / Component Redefinition — Operational Boundary vs. Build Artifact, and the Module/System Naming Debate

**Scope:** Technical, dim5-system.md, dim5-component.md, versioning model

DR-024 defined System as "independently deployable technical unit" with examples like `payments-service`, `fx-service`. This placed the definition at the microservice granularity — the natural level for engineers. But from a product information model perspective, "what is a System?" depends on the operational question being asked.

The resolution: System is the **operational deployment boundary** — what SRE versions and deploys as a whole. It is a logical grouping of Components, where "Component" is the individual deployable artifact (container image, Lambda package, frontend bundle). Components are independently buildable with their own artifacts, but are deployed as part of their parent System, not independently. When SRE deploys "Payments System v3.1," they deploy a composed release of payments-service (Component), bank-adapter (Component), and payment-reconciler (Component) — not each service individually.

**The naming debate:** The UPIM's use of "Module" for the Structural functional entity conflicts with the organization's internal usage of "Module" for deployment/technical groupings. Several alternatives were considered for the Technical entity before settling on "System":

- **Deployment Module / Functional Module** — Makes the duality explicit through qualified names. Rejected: introduces permanent ambiguity on the bare word "Module" throughout the UPIM; every reference would need qualification.
- **Domain** (for Structural, freeing "Module" for Technical) — "Domain" is already in the entity filename (`dim8-module-domain.md`) and aligns with DDD vocabulary. Rejected: "Module" is more tangible and natural in product conversations ("Payments Module," "Compliance Module"); "Domain" sounds conceptual and less accessible to customers and sales teams.
- **Cluster** (for Technical) — Conveys grouping. Rejected: "Cluster" has a dominant infrastructure connotation (Kubernetes cluster, database cluster); `dim7-cluster-host.md` was already deprecated from the UPIM for related reasons.
- **Service Group** / **Deployment Unit** — Descriptive but not natural in conversation.
- **System** — Architecturally standard (C4 model, TOGAF, AWS Well-Architected all use "System" for operational deployment groupings). Clearly distinct from "Module." No strong competing connotation in the UPIM.

**Resolution and vocabulary note:** "Module" (Structural) is the customer/product-facing functional grouping. "System" (Technical) is the engineering-facing operational deployment grouping. In the UPIM: *Module = what the product does; System = how it deploys.* Engineers who colloquially say "the payments module is deploying" are using "module" informally. The UPIM gives them a precise term: "the payments system is deploying." This vocabulary guidance is documented in `dim5-system.md` and `dim8-module-domain.md`.

**Cascading consequence (resolved in DR-036):** The Build Track versioning chain is now **Component Version → System Version → Product Version**. Component Version is what CI builds (atomic tier). System Version is a sealed, immutable BOM of Component Versions — what SRE deploys as a unit. Product Version composes System Versions directly; there is no Module Version tier. See Seeds 16–17 and DR-036.

See DR-035 D10, D15; DR-036 D1–D3, D12.

---

## Seed 14: Entitlement at Module Level — Keeping Pricing at the Right Granularity

**Scope:** Structural Module, Vendor Value Pricing Tier

Initial modeling placed entitlement (Pricing Tier link) on Feature — the most granular unit — reasoning that fine-grained packaging required feature-level control. Revised in this session: Feature is below the entitlement granularity that customers and sales teams work with. A customer buys access to the "Payments Module" (or a tier that includes it), not individual features within it. Feature-level entitlement adds governance overhead without corresponding commercial benefit at this stage.

The Module is the right entitlement boundary: it is the customer-facing unit of functional value, corresponds to a coherent business capability domain (Functional Classification), and aligns with how pricing conversations happen. The note "this may evolve" is intentional — as products mature, feature-level entitlement (feature flags, add-ons) may become appropriate and the link can be moved down.

See DR-035 D7.

---

## Seed 15: PSD Authorship Split — The PM/Architect Interface

**Scope:** dim1-psd.md, PSD templates, Track 1/2 boundary

The PSD is the contract between Product and Engineering. The question of who writes it — and which parts — was not explicitly modeled in the original design. The implicit assumption was "the PM writes the PSD" with Module Archetype as the PM's signal to engineering about what kind of system was being built.

The new model makes authorship zones explicit. PM-authored (Product Draft phase): PSD objective, Capability specifications using Capability Templates, Feature specifications, Acceptance Criteria, Epic decomposition proposal. Architect-authored (Technical Review phase): System mapping (which Systems/Components realize each Capability/Feature), technical sections (Technical, Ecosystem, Operational, Data). The PSD status progresses: `Draft` → `In Technical Review` → `Approved`.

The accountability principle is key: the Architect is responsible for ensuring that every Capability and Feature specified by the PM in the PSD is addressed through System and Component changes. The PM specifies WHAT needs to be achieved; the Architect designs HOW it is realized. The PSD becomes the interface document where both contribute, with clear ownership of each zone.

See DR-035 D8, D9, D13.

---

## Seed 16: Deployment Simplification — Eliminating the Run Artifact Layer

**Scope:** Track 2/3 versioning and deployment artifacts, Technical Product Specification, Operational Package entities

The four-layer deployment model (Build Artifacts / Run Artifacts / Deployment Descriptors / Deployment Execution) introduced a **Run Artifact** layer — Module Package and Product Package — to segregate "operator-facing" Systems from product-facing Systems. This created a structural distinction that did not match operational reality.

Operator-facing Systems (probes, reconcilers, monitoring agents, log shippers) are ordinary Systems: they have source code, repositories, CI/CD pipelines, Component Versions, and System Versions. SREs build them through the same Build Track as product engineers. The only difference is **who they serve** — Operational Personas rather than End-User or Programmatic Personas. The `Purpose / Serving Persona(s)` field on the System entity captures this distinction without requiring a parallel artifact taxonomy.

Removing Module Package and Product Package, and replacing SDD/MDD/PDD with **System Deployment Specification** and **Product Deployment Specification**, reduces core versioned/deployment entities from nine or more to five. The three-layer model is: Build Artifacts → Deployment Specifications → Deployment Execution.

All Systems — product-facing and operational — are equal members of **Product Specification** (Technical). Operational Systems appear in Product Version BOMs alongside tenant-serving Systems.

See DR-036 D5, D6, D7, D8, D9, D13.

---

## Seed 17: Versioning Chain Simplification — Removing Module Version

**Scope:** Track 2 versioning, Structural Module, integration verification boundaries

**Module Version** was introduced to bridge the gap between individual System build artifacts and Product Version. It represented "integration-verified composition of Systems for a Structural Module." Under DR-035, System became the operational deployment grouping and Component the atomic build artifact — but the Work Model still treated System Version as atomic (a single microservice). DR-036 completes the alignment:

| Tier | Artifact | Verification scope |
|---|---|---|
| Atomic | **Component Version** | Per-Component quality gates (CI) |
| Integrated | **System Version** | Component-integration within System boundary |
| Complete | **Product Version** | Cross-System integration and certification |

**Why Module Version was removed:** Module (Structural) is a functional boundary — how customers and PMs talk about the product ("Payments Module," "FX Module"). It is not an operational versioning boundary. Requiring a Module Version between System Version and Product Version added a tier that duplicated integration verification:

- Within-System integration → System Version assembly
- Cross-System integration → Product Version assembly

**Capability availability** does not require Module Version: trace **Module (Structural) → System (Technical) → System Version** in the current Product Version BOM. Example: "Real-Time FX Rate Lock" (Capability) → FX Module → fx-system → fx-system v2.0.1 in Product v4.0.0.

**Integration Epic semantics change:** Integration Epics contribute to System Version assembly and Product Version certification — not to a separate Module Version artifact.

See DR-036 D1, D2, D3, D12.

---
