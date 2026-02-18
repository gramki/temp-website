# UPIM Narrative Seeds

## Purpose

This file captures **connective reasoning, insights, and perspectives** discovered during modeling discussions — the material that will eventually become the narrative documentation for the UPIM.

The UPIM has three layers of documentation:

1. **Entity files** (`entities/`) — capture **what**: fields, statuses, relationships, examples per entity
2. **Decision records** (`decisions/`) and **FAQs** (`draft-modeling-faqs.md`) — capture **why**: specific design choices and their rationale
3. **Narrative documentation** (future) — captures **how it all connects**: the flow of work, the interplay between dimensions, the reasoning that makes the model coherent rather than a collection of entity definitions

This file serves layer 3. Entity files and DRs are necessary but insufficient for someone to *understand* the UPIM. A reader who has read every entity file still doesn't know why the model is shaped the way it is, how work flows through it, or what the guiding philosophy behind the design is. The narrative seeds bridge that gap.

## What to Capture

Each seed should capture one or more of the following:

### Connective Insights
How entities, dimensions, or tracks relate to each other in ways that aren't obvious from reading individual entity files. These are the "aha moments" that emerge during design discussions.

*Example:* "Customer Segment is the shared anchor between Dim 2 and Dim 3 — the same segment viewed from the buyer's perspective (Why Buy) and the vendor's perspective (Why It Wins)."

### Design Philosophy
The guiding principles or mental models that shaped a set of decisions — not the individual decisions (those go in DRs) but the underlying reasoning pattern.

*Example:* "Win Stakeholders are Signal sources and Deliberation participants, not entity authors. This follows a consistent pattern: the people who experience reality contribute observations; the PM/PMM translates observations into structured model knowledge through governed processes (Signals, PDRs, Modeling Tasks)."

### Flow Narratives
How work moves within a track, across tracks, or between the Definition Model and Work Model. These are the dynamic stories that make the static entity definitions come alive.

*Example:* "A Pre-Sales Engineer observes that POC takes 6 weeks. They file a Problem Signal. Discovery investigates, produces a PDR. The PDR triggers both a Modeling Task (document the Delivery Friction in Dim 2) and a PSD (build LATAM sandbox support). Build Track implements. Run Track deploys. Win Track verifies the friction is reduced. If not, Feedback generates a new Signal."

### Cross-Dimensional Symmetries
Parallels between dimensions that reveal the model's coherence — where the same analytical pattern appears in different contexts.

*Example:* "Dim 2 and Dim 3 are mirror images anchored by Customer Segment. Buying Persona ↔ Win Stakeholder. Business Outcome ↔ Win Outcome. Pain ↔ Delivery Friction. Customer Promise ↔ Pricing Tier. Customer Value Metric ↔ Business KPI. Adoption Barrier ↔ Win Barrier."

### Debates and Resolutions
Key disagreements or tensions encountered during modeling, and how they were resolved. These reveal the trade-offs in the model and prevent future contributors from re-litigating settled decisions without understanding the context.

*Example:* "Initially dismissed vendor-side JTBD as unnecessary ('you already know your own goals'). Challenged by the insight that for complex enterprise products, the vendor's path to revenue is a discovery problem — implementation is bespoke, time-to-revenue varies by segment, multiple stakeholders with different frictions. The AAARRR framework provided the lifecycle structure."

## Depth Guidance

- **Not a summary.** Don't just say "we discussed Dim 2." Capture the specific insight.
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

Each model's internal subdivision earned its name through modeling work. The Definition Model has 9 Dimensions (because we modeled 9 independent axes). The Work Model has 4 Tracks (because we identified 4 parallel streams). The Operating Model's internal structure is deliberately unnamed — "Coordination" and "Organization" are working labels, not architectural terms. Premature naming would be like calling Dimension 3 "The ROI Dimension" before discovering it's about the full buying committee, pain, promises, and barriers.

### The dependency chain reads bottom-to-top

Define the product (Definition Model) → Define what work moves the product (Work Model) → Define how the org executes that work (Operating Model). Each layer depends on the one below. The Definition Model is the foundation that never depends on anything above it.

---

## Session: Dimension 1 — The Strategy Dimension

**Scope:** Dim 1 entities, Signal lifecycle, strategic entities, Discovery Track connection

### Signal is an investigation mindset, not a fulfillment mindset

The word "Signal" was chosen over "intake item," "backlog item," and "market signal" because it fosters investigation rather than obligation. A Signal is explicitly not a requirement, a commitment, or an obligation. It's an observation that warrants attention. Multiple Signals may point to the same issue; a single Signal may be noise. This framing is the philosophical foundation of the Discovery Track — everything that enters is questioned, investigated, and decided upon, not just processed.

### The Strategy Dimension is a ledger, not a pipeline

Dim 1 contains entities at very different levels of abstraction — Portfolio (organizational context), Strategic Themes (persistent direction), Objectives (time-bound goals), Initiatives (programs), Customer Releases (business deliveries), Signals (observations), Ideas (hypotheses), PDRs (decisions), PSDs (specifications). This isn't a pipeline where everything flows linearly. It's a ledger — a structured record of strategic intent at multiple levels, with explicit relationships between levels.

### The PDR fills a traceability gap

Without PDRs, the model goes Signal → Idea → PSD with no artifact recording *why* a decision was made. The PDR is a knowledge artifact, not a process artifact. "Kill" PDRs are as valuable as "Go" PDRs for institutional memory. PDRs can also exist without Ideas (from strategic Deliberations) and can correspond to multiple Ideas simultaneously.

### Strategic Themes provide "the why behind the why"

Objectives are time-bound ("achieve Y by H2 2026"). Themes are persistent ("we are investing in LATAM"). Without Themes, strategic continuity across planning horizons is implicit — you must read a sequence of Objectives and infer the pattern. Themes make investment direction explicit and queryable.

---

## Session: Dimension 3 — The Customer Value Dimension (Why Buy)

**Scope:** Dim 3 entities, JTBD mapping, buying committee, pain, promises, metrics, barriers

### The buying committee, not the buyer

Enterprise B2B purchases involve a committee: Economic Buyer (ROI), Technical Buyer (integration/security), User Buyer (usability/adoption), Coach/Champion (internal politics). Modeling only the Economic Buyer left the Technical Buyer invisible — yet many deals die at technical evaluation. Expanding to Buying Persona with role types captures the full committee compactly.

### Pain + Business Outcome = complete "Why Buy" motivation

Business Outcome is the rational justification ("reduce FX costs by 40%"). Pain is the visceral urgency ("4 hours/day manual reconciliation"). Value Propositions must address *both*. The critical distinction: User Personas (Dim 4) *endure* pains; Buying Personas (Dim 3) *care about* pains. The same pain is cared about by different buyers for different reasons — the CFO cares about cost, the AP Ops Manager cares about productivity, the CTO cares about error rates. Each needs a different message.

### Customer Promise has three peer subtypes, not one

Value Proposition, Service Commitment, and Compliance Posture are siblings under Customer Promise — not nested. Each speaks to a different facet of the buying decision, maps to different structural entities (Value Streams/Capabilities, Dim 7 infrastructure, Dim 8 Capabilities respectively), uses different metric types, and changes on different cadences.

### Customer Segment is the anchor entity for Dim 3

All other Dim 3 entities are scoped to Customer Segments — Buying Personas, Pains, Promises, Metrics, Barriers. Without segment scoping, the model can't express "LATAM Enterprise has different buying dynamics than US Mid-Market." This scoping principle later extended to Dim 2 as well.

---

## Session: Dimension 2 — The Vendor Value Dimension (Why It Wins)

**Scope:** Dim 2 restructure, AAARRR lens, Win entities, Dim 2 ↔ Dim 3 symmetry, governance

### The vendor's path to revenue is a discovery problem

Initially dismissed vendor-side JTBD ("you already know your own goals"). Challenged by the insight that for complex enterprise B2B products, the path from signed contract to steady-state revenue involves an elaborate, multi-stakeholder journey — Pre-Sales, Implementation, Go-Live, Revenue Ramp, Optimization, Renewal. Implementation is often bespoke. Time-to-revenue varies by segment. Cost-to-serve differs dramatically. None of this is self-evident; it requires the same investigation mindset as customer discovery.

The strategic *intent* (Dim 1 Objectives) is known. The operational *economics* of serving each segment are discovered. This distinction — known intent vs. discovered economics — is what justifies Dim 2's analytical depth.

### AAARRR provides the lifecycle, not just revenue

Revenue is one of six AAARRR stages. "Revenue Stakeholder" and "Revenue Outcome" would have been myopic. "Win Stakeholder" and "Win Outcome" capture the full lifecycle. The naming also creates a natural bridge to the Win Track — Dim 2 defines what winning looks like; the Win Track does the work to achieve it.

### Dim 2 ↔ Dim 3: mirror images through Customer Segment

The two dimensions are two sides of the same transaction, anchored by Customer Segment:

| Dim 3 (Customer's perspective) | Dim 2 (Vendor's perspective) |
|---|---|
| Buying Persona | Win Stakeholder |
| Business Outcome | Win Outcome |
| Pain | Delivery Friction |
| Customer Promise | Pricing Tier / Business Model |
| Customer Value Metric | Business KPI |
| Adoption Barrier | Win Barrier |

This symmetry is structural, not coincidental. It emerged from applying the same analytical lens (who's involved, what success looks like, what suffering exists, how it's measured, what blocks it) to both sides of the commercial relationship.

### Win Stakeholders are functional archetypes, not org chart roles

Dim 2 defines *what roles the product's commercial model requires* (Pre-Sales Engineer, Implementation Consultant, CS Manager). The Operating Model (future) defines *how teams are staffed and structured*. A startup with one person covering three Win Stakeholder roles still needs the model to distinguish the functions — because they have different concerns, different frictions, and different success criteria. When the startup hires, the Win Stakeholder model tells them what to hire for.

### All Dim 2 changes require PDRs — two governed paths

1. **Deliberation → PDR → Modeling Task:** For strategic design (pricing strategy, AAARRR target-setting). Win Stakeholders participate; PM/PMM authors.
2. **Signal → Discovery → PDR → Modeling Task:** For field observations (Delivery Frictions, Win Barriers). Win Stakeholders observe and file Signals; Discovery investigates; PDR records the decision.

This governance isn't bureaucracy — it's protection. Dim 2 entities define the commercial model. Changing a Pricing Tier affects active customers. Changing a KPI target affects resource allocation. These changes need traceability and deliberate decision-making.

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

### The Discovery Track produces three types of output

1. **PDRs** — decisions (any dimension)
2. **PSDs** — engineering specifications (module changes, via Specification Task)
3. **Definition Model updates** — knowledge changes (Dims 2–9, via Modeling Task)

A single PDR may trigger both PSDs and Modeling Tasks. Or just one. Or neither (if the decision is "Kill").

---

## Cross-Cutting Seeds

### The Win Track is the operational arm of Dim 2

Where Dim 2 defines *what winning looks like* (Win Outcomes, Business KPIs, Win Stakeholder roles), the Win Track defines *the work to achieve it*. Initiative embedded targets operationalize Win Outcomes for specific periods. Win Reviews assess target progress. Feedback surfaces Delivery Frictions and Win Barriers as Signals. Win Planning references Dim 2 entities for commercial coherence. This is the strongest Definition Model ↔ Work Model coupling in the UPIM.

### The Feedback → Signal loop is the UPIM's learning mechanism

Win Track Feedback → becomes Signal (Dim 1) → enters Discovery Track → may produce PDR → may trigger Modeling Task (updates Dim 2 or Dim 3) + PSD (updates product). This loop is how the UPIM learns from reality. Customer feedback surfaces product problems and unmet needs. Win Stakeholder feedback surfaces vendor-side frictions and barriers. Both re-enter the same governed discovery process.

### Every dimension has a natural "home track"

| Dimension | Primary Track | Why |
|---|---|---|
| Dim 1 (Strategy) | Discovery | Strategy entities are authored through Discovery planning and exploration |
| Dim 2 (Vendor Value) | Win | Win Track operationalizes Dim 2; Feedback updates it |
| Dim 3 (Customer Value) | Discovery + Win | Discovery models customer promises; Win validates them |
| Dim 4 (UX) | Discovery + Build | Discovery researches personas/journeys; Build implements |
| Dim 5 (Technical) | Build | Architecture and code are Build Track concerns |
| Dim 6 (Ecosystem) | Build | APIs and extensibility are Build Track concerns |
| Dim 7 (Operational) | Run | Infrastructure and runtime are Run Track concerns |
| Dim 8 (Structural) | Discovery + Build | Discovery defines topology; Build realizes it |
| Dim 9 (Data) | Build + Run | Build designs schemas; Run manages operational data |

But Modeling Tasks (Discovery Track) can update *any* dimension. The "home track" is where the most frequent mutations happen; Modeling Tasks provide cross-dimensional reach.

### PSD is the cross-dimensional impact assessment

A PSD is not just "what to build." It's a structured assessment of impact across all 9 dimensions — Pain implications (Dim 3), Win Outcome implications (Dim 2), UX impact (Dim 4), technical architecture (Dim 5), API changes (Dim 6), operational requirements (Dim 7), structural changes (Dim 8), data changes (Dim 9). The depth varies by module archetype, but every dimension must be acknowledged. This makes the PSD the most integrative artifact in the UPIM.

### Customer Release, Customer Promise, Win Outcome — the commercial triad

These three entities form a critical triangle spanning Dim 1 (Strategy), Dim 3 (Customer Value), and Dim 2 (Vendor Value):

- **Customer Promise** (Dim 3) = what we commit to the customer — the explicit contract
- **Win Outcome** (Dim 2) = what we need to achieve as a vendor — the implicit commercial target
- **Customer Release** (Dim 1) = the delivery vehicle that fulfills promises and advances outcomes

They are the three faces of a single commercial exchange. Customer Promise says "here's what you get." Win Outcome says "here's what we need for this to work for us." Customer Release is the event where promise meets outcome — where the vendor delivers on its commitments and either advances toward or falls short of its Win Outcomes.

The critical insight: **keeping promises and winning are not the same thing.** A product can keep every Customer Promise (99.9% uptime, sub-200ms latency) and still fail to achieve its Win Outcomes (CAC too high, Activation takes 90 days instead of 30). When promises are kept but the vendor isn't winning, the problem is in Dim 2 — the commercial model, the delivery economics, the Go-to-Market, the pricing structure. Conversely, if Win Outcomes are met but Customer Promises are not, it's a ticking time bomb — short-term revenue without long-term retention.

This is why the PSD's cross-dimensional sections are ordered the way they are: Section 2 (Vendor Value Impact) and Section 3 (Customer Value Impact) force the spec author to reason about *both* sides of the exchange before engineering begins.

### Customer Release is a Definition Model entity that the Win Track activates

Customer Release sits in Dim 1 (Strategy) because it's a business planning construct — deliberately scoped, named, and scheduled. But it is *activated* by the Win Track: GTM Planning prepares the launch, Customer Release Planning sequences the market delivery, and Win Reviews assess whether the release achieved its Win Outcomes (with progress tracked via Initiative embedded targets).

This makes Customer Release the primary handoff point between strategic intent and commercial execution. The Discovery Track scopes it (which Initiatives are included). The Build Track assembles it (which Product Versions realize it). The Win Track activates it (GTM, onboarding, adoption). The Run Track sustains it (deployment, uptime). All four tracks converge on Customer Release — it's the entity that most explicitly crosses every track boundary.

### Three-level versioning and the deliberate decoupling

Module Version → Product Version → Customer Release. Three levels, three different questions, three different owners:

| Level | Question | Owner | Cadence |
|---|---|---|---|
| Module Version | What did this module's CI/CD produce? | Dev team | Continuous (every merge) |
| Product Version | Which module versions are compatible as a tested composition? | Tech Lead / QA | Frequent (weekly to biweekly) |
| Customer Release | What capabilities are we making available to customers? | PM / Business | Deliberate (milestone-driven) |

The first two are Work Model entities (Build Track outputs) because they are *byproducts* of engineering progress — routinely and continuously incremented. Customer Release is a Definition Model entity (Dim 1) because it is a *decision* — someone decided "these capabilities, bundled this way, named this way, targeted to these segments."

The naming convention reinforces the decoupling: Customer Releases use names ("LATAM Expansion"), not version numbers. A single Customer Release may span multiple Product Versions (v3.2.0 through v3.2.4 as patches land during rollout). Pinning to a version creates a false 1:1 mapping that breaks in practice.

### Customer Promise subtypes map to different structural dimensions

This is one of the deepest cross-dimensional integrations in the model. Each Customer Promise subtype maps to different parts of the product's structural reality:

| Promise Subtype | Maps to | Why |
|---|---|---|
| Value Proposition (outcome-based) | Value Streams (Dim 8) | Outcomes require end-to-end flows across modules |
| Value Proposition (ability-based) | Capabilities (Dim 8) | Promise is about a specific product ability |
| Service Commitment | Infrastructure (Dim 7) | Uptime, latency, support are operational |
| Compliance Posture | Capabilities (Dim 8) | Compliance shapes many capabilities across modules |

This means a *single Customer Segment* receives promises that are delivered by different structural mechanisms — outcomes flow through Value Streams, abilities are provided by Capabilities, reliability depends on infrastructure, and compliance is woven through the capability layer. The Customer Promise entity unifies what the customer sees as one coherent "deal" while the model traces each commitment to its structural delivery mechanism.

### Win Outcome is structural, not time-bound — and that distinction matters

An Objective (Dim 1) is time-bound: "Expand to LATAM currencies by H2 2026." It comes and goes with planning horizons. A Win Outcome (Dim 2) is structural and persistent: "LATAM Enterprise — Activation: first live transaction within 30 days of contract." It persists across Objectives. Multiple Objectives may target the same Win Outcome across different planning horizons.

This distinction matters because Win Outcomes define what the vendor is *structurally optimizing for* — the enduring commercial targets that outlive any single planning cycle. When an Objective is "Achieved" or "Deferred," the Win Outcome it targeted remains. The next Objective in the next planning cycle may target the same Win Outcome with a different approach. Win Outcomes change only when the commercial model changes (new segment, pivoted business model, retired market) — and that change requires a PDR.

Business KPIs evidence Win Outcomes, not Objectives. Initiative embedded targets operationalize Win Outcomes for specific periods. Win Reviews assess target progress. This creates a clean separation: Dim 1 (Strategy) sets direction and time-bounds; Dim 2 (Vendor Value) defines enduring success criteria; the Win Track measures reality against both.

### Customer Promise ↔ Pricing Tier: the two halves of the customer-facing deal

Customer Promise (Dim 3) says "here's what you get." Pricing Tier (Dim 2) says "here's what you pay." Together they form the complete customer-facing commercial proposition. The symmetry is reinforced by both being scoped to Customer Segments — the same segment gets specific promises and pays a specific price.

But they live in different dimensions because they serve different analytical purposes. Customer Promise is about *value delivered* (analyzed from the customer's perspective in Dim 3). Pricing Tier is about *value captured* (analyzed from the vendor's perspective in Dim 2). A product strategist reasoning about Customer Promises asks "are we delivering enough value to justify purchase?" A product strategist reasoning about Pricing Tiers asks "are we capturing enough value to sustain the business?" The gap between these two questions is the strategic tension that drives product evolution.

---

## Session: Win Track Restructure and Initiative Evolution

**Scope:** Win Track entity landscape, levers, Initiative as cross-track construct, Win Review, Win Case, Enablement vs. Engagement, Feedback and target tracking

### Not all Win Outcomes are advanced by product capabilities alone

This is the insight that triggered the entire Win Track restructure. Consider "80% unaided brand recall in LATAM fintech CFO community" (Awareness Win Outcome) — product features barely move this needle. Or "close LATAM deals in 90-day cycle" (Acquisition) — the lever is sales enablement and competitive positioning, not code. When a Win Outcome is modeled, it's critical to identify the *means to achieve it*, and those means include non-product work: GTM, sales enablement, customer success programs.

Without explicit levers, organizations default to building features when the actual lever is a sales enablement program or a marketing campaign. The lever mix forces the question at modeling time: "Is this primarily a product problem, a GTM problem, or both?"

### Five categorical levers, defined as a master list on Business Model

The lever portfolio is a governed, finite set per Product/Portfolio, defined on the Business Model entity (Dim 2):

| Lever | What it covers | Primary Track |
|---|---|---|
| Product | Feature development, capability enhancement, UX improvement | Discovery → Build |
| GTM | Marketing, demand gen, pricing communication, partnership/channel, launch | Win |
| Sales Enablement | Competitive tools, demo environments, POC toolkits, sales training | Win |
| Customer Success | Onboarding programs, health monitoring, retention, expansion, advocacy | Win |
| Operational | Internal process, tooling, automation, hiring | Operating Model |

GTM is the umbrella for marketing, pricing *execution*, and partnership *execution*. Pricing *design* (tier structure, rates) is a Dim 2 / Discovery concern. Partnership *strategy* is a Dim 1/Dim 2 strategic decision. The levers capture the *execution* side.

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

Win Review assesses both sides of the commercial exchange — not just whether the vendor is winning (Dim 2: Win Outcomes, Business KPIs) but also whether the vendor is keeping its promises (Dim 3: Customer Promises, Customer Value Metrics). This operationalizes the insight that "keeping promises and winning are not the same thing."

The connection to Win Review types is direct: QBRs assess whether customers are getting what they were promised (uptime, value delivery, compliance). Post-Implementation Reviews check whether onboarding delivered on Value Propositions. Case Pattern Reviews reveal whether complaint patterns indicate Service Commitment failures. Adoption Reviews check whether the product delivers the value it promised (Customer Value Metrics alongside Business KPIs).

Without explicit promise assessment in Win Reviews, the Win Track only measures the vendor's commercial health — missing the customer's experience of whether commitments are being met. Strong Win Outcomes with broken promises are a retention time bomb; kept promises with failing Win Outcomes indicate a Dim 2 problem (commercial model, not product quality). Both signals require different interventions, and only dual assessment surfaces the distinction.

### Feedback is an artifact, not a work item

Feedback was reclassified from a "Win entity" to an **artifact** produced by Win Reviews. You don't "do" a Feedback — you do a Win Review and *produce* Feedback records. Feedback is to Win Engagements/Reviews what a PDR is to a Deliberation: the record produced by the work, not the work itself.

Feedback is a transitional artifact: born in the Win Track, consumed by the Discovery Track when promoted to a Signal. Not every customer observation becomes a Signal. Feedback is the raw, structured observation; Signal is the qualified, investigation-worthy version.

### Targets are not standalone entities — they're embedded in Initiatives

The "Adoption Goal" entity was eliminated. Targets (like Key Results in an OKR) are embedded in Initiatives. The reasoning: targets are set during planning, tracked during execution, and assessed during reviews. They're attributes of the coordination construct (Initiative), not independent entities.

The naming was also wrong: "Adoption" is stage-specific (only Activation), but targets span all AAARRR stages. "Goal" conflicts with Objectives. Embedding them in Initiatives resolved both problems.

### The UPIM's strategy layer follows the OKR pattern — and it's lever-agnostic

The structural mapping between the UPIM and OKRs is precise:

| OKR Concept | UPIM Entity | Relationship |
|---|---|---|
| **Objective** | Objective (Dim 1) | Qualitative, aspirational, time-bound direction |
| **Key Result** | Embedded Target (on Initiative) | Quantitative, time-bound, measurable |
| *(no direct equivalent)* | Initiative (Dim 1) | The strategic program that carries Key Results *and* declares how to achieve them |

The UPIM extends OKR by adding the **Initiative as a coordination layer** between the Objective (what) and the Targets (how much). In pure OKR, Key Results live directly on the Objective. In the UPIM, targets live on Initiatives — because the same Objective ("Expand to LATAM") may be advanced by multiple Initiatives with different lever mixes, each carrying distinct targets.

The critical insight: **this pattern is lever-agnostic**. Whether an Initiative is 100% Product (a pure engineering effort) or a mix of Product 40% / GTM 25% / Sales Enablement 20% / CS 15% (cross-functional market entry), the Objective → Initiative → Target structure applies identically. The OKR discipline of setting measurable targets against qualitative objectives doesn't care what *kind* of work advances the target — only that the target is measurable and time-bound. This means:

- A Build-heavy Initiative has targets like "Q3: API latency < 200ms for LATAM FX quotes"
- A GTM-heavy Initiative has targets like "Q3: 80% unaided brand recall in LATAM fintech CFOs"
- A CS-heavy Initiative has targets like "Q3: 95% gross retention rate for LATAM Enterprise"
- All three follow exactly the same structural pattern

This universality is why targets belong on Initiatives (which vary by lever mix) rather than on Objectives (which are lever-agnostic). The OKR pattern provides the measurement discipline; the lever mix provides the execution strategy. Together they answer: "What are we trying to achieve?" (Objective), "How are we going to do it?" (Initiative + lever mix), and "How will we know?" (embedded targets).

### Win Case captures reactive, customer-initiated work

A large portion of Win Team work is reactive — responding to customer queries, service requests, complaints, and escalations. Without Win Case, only proactive work was visible. Reactive work matters because:
- It's where Service Commitments (Dim 3) are tested — response times, resolution quality
- It reveals Delivery Frictions and Win Barriers through pattern analysis
- Cost-to-Serve (Business KPI) is measured against it
- CSAT and other targets can only be assessed through reactive work quality

Win Case types: Query, Service Request, Complaint, Escalation. "Complaint" was chosen over "Problem" because (a) "Problem" is already a Signal type in Dim 1, and (b) in the Win Track context, the customer is expressing dissatisfaction, not filing an ITSM Problem record.

The Run Track has its own reactive entities (Incident, Change Request) for infrastructure concerns. Win Case is customer-facing; Run Track entities are system-facing.

### Segment-level engagement exists both pre-sale and post-sale

Win Engagement isn't always one-to-one. Awareness campaigns, feature workshops, advocacy events, and customer webinars are segment-level engagements. Post-sale segment engagement (feature awareness webinars, capability workshops) is a significant class of work that sits alongside account-level engagements.

### The Win Track operates in continuous flow (kanban), not sprints

Win Track work doesn't align to sprint boundaries. A POC might take 3 weeks; a marketing campaign runs for 6 weeks; a QBR happens quarterly. Planning is periodic but work item duration varies. The model captures planning cycles without specifying duration.

### Signal templates structured as lever × signal type

Win Stakeholder Signals about lever effectiveness (not just Delivery Frictions) flow through the existing Signal pipeline. Templates are structured as a lever × signal type (Problem, Need, Opportunity) matrix, placed in the Signal entity definition (Dim 1). This applies to all Signal sources, not just Win Stakeholders.

---

## Session: Work Execution Framework

### The Work Model's asymmetric artifact coverage

The Work Model was detailed about *what kinds of work exist* but inconsistent about *what each work type produces*. Where artifacts fed back into the Definition Model (PDR, PSD, Feedback → Signal), they were well-modeled. Where artifacts were consumed internally within a track (Research findings, Experiment results, deployment runbooks, enablement assets, case resolution records), they were implied in descriptions but not structurally captured. This created a blind spot: stakeholders could see what work to do but not what "done" looks like or what outputs to expect.

### Three execution dimensions, not one

The gap isn't just artifacts. Three dimensions are needed to fully describe the execution semantics of a work entity: (1) **Artifacts** — what it produces, (2) **Definition of Done** — when it's complete, (3) **Guidance** — how to navigate it. These three form a coherent framework for any work entity, regardless of track. A product manager looking at a Win Review entity needs all three: what does it produce (Feedback + target progress), when is it done (findings documented, Feedback artifacts created, target progress updated), and how do I run one (QBR playbook).

### Artifacts and DoD belong to the Work Model; guidance belongs to the Operating Model

The key boundary: artifacts and Definition of Done describe properties of the work itself — what it produces and when it's complete. These are information model concerns. Guidance (playbooks, templates, procedures) describes how teams *execute* the work — that's methodology, which varies by team, product, and context. The Work Model captures the structure of guidance (what a playbook should cover) but not the content (which lives in the Operating Model). Entity files reference Operating Model playbooks; they don't contain them.

### Artifact taxonomy provides a shared vocabulary

Five artifact categories emerged: Decision (recorded choices), Evidence (findings and observations), Specification (what to build/deliver), Delivery (versioned outputs), Assessment (evaluations against targets). Every work entity's output can be classified into one or more of these categories. The taxonomy provides a common language across tracks — a PDR is a Decision Artifact, a Module Version is a Delivery Artifact, Feedback is an Evidence Artifact, a PSD is a Specification Artifact.

### Transitional vs. terminal artifacts mark track boundaries

Some artifacts are born in one track and consumed by another — Feedback (Win → Discovery), PSD (Discovery → Build), Module Version (Build → Run). These "transitional" artifacts are the track boundary contracts. Terminal artifacts are consumed within their own track or by external systems. Making this distinction explicit helps identify integration points and handoff contracts between tracks.

### The framework enables iterative detailing without losing coherence

By establishing the artifact taxonomy, DoD pattern, and guidance structure as a framework, individual tracks can be detailed independently. Detailing Track 1's artifacts doesn't require simultaneously detailing Track 3. The cross-track artifact inventory provides the global picture; per-entity execution sections provide the detail. Phase 5 (cross-track integration) validates that all transitional artifacts have matching producers and consumers.

---

## Session: Cross-Track Monitoring and Win Track Gaps

### Continuous monitoring is a work type in every track

Every track has ongoing monitoring work that sits between periodic assessment (Reviews, Deliberations) and reactive work (Cases, Incidents). This work was invisible in the model — teams did it, but it wasn't a first-class entity. Introducing Signal Monitoring (Discovery), Build Monitoring (Build), System Monitoring (Run), and Win Monitoring (Win) makes the pattern explicit: monitoring produces alerts (which trigger reactive work) and reports/dashboards (which feed periodic reviews). The same structure applies in all four tracks; only the scope and metrics differ.

### Partner/channel work is distinct from internal sales and customer engagement

Partners are intermediaries in the AAARRR journey (Awareness, Acquisition). They need enablement (partner demo environments, co-marketing kits, certification) and engagement (partner onboarding, co-selling, pipeline management) that is distinct from Sales Enablement (which equips *internal* teams) and from customer-facing Win Engagement. Partner Enablement and Partner Engagement were added as subtypes; Engagement Planning scope was extended to include partner prioritization and sequencing. References external PRM (Partner Relationship Management).

### Revenue realization is both operations and intelligence

Revenue Realization is an essential signal for Dim 2. Two additions: (1) **Revenue Operations Engagement** — account-level, customer-facing work to ensure revenue is collected (invoicing, collections, renewal processing, revenue recognition coordination). Advances Revenue Win Outcomes; billing disputes stay in Win Case. (2) **Revenue monitoring** — covered by Win Monitoring (NRR, pipeline, churn signals); when targets are missed, the signal feeds Win Review or Feedback → Signal. Both commercial operations and revenue intelligence belong in the Win Track.

### PLG segments shift Win Track from execution to monitoring

For segments where the Product lever dominates (self-service onboarding, free trial, in-product expansion), the same Win Engagement subtypes apply but the balance shifts. Implementation/Onboarding becomes in-product; Win Track monitors funnels and intervenes on stuck accounts. Pre-sales becomes trial/sandbox; Win Track monitors conversion. The Build Track effectively does "Win" work (self-service flows, in-product upsell). Win Monitoring becomes the primary Win Track activity; human engagement is for exceptions. No new entities — a conceptual note suffices.

### Advocacy encompasses customer education

Customer education (training, certification, knowledge bases, workshops) is already covered: CS Enablement builds the assets (training materials, certification curricula); Segment Engagement delivers them (webinars, training sessions). CS Planning plans education programs as part of advocacy. Advocacy was clarified to encompass both referral/case-study work and customer education; explicit examples were added (e.g., "LATAM API integration certification program"). No new entities.

---

## Session: Tier 2 Detailing — Structural Links, Segment Enrichment, and Competitive Context

### Dim 2 and Dim 3 are structural parallels, not operational mirrors

Dim 2 (Vendor Value) and Dim 3 (Customer Value) use the same analytical shape — stakeholder, outcome, suffering, impediment, metric — but from opposite sides of the commercial relationship. Win Outcome (vendor's target) and Business Outcome (buyer's target) are not equivalents that need linking. Delivery Friction (vendor suffering) and Pain (customer suffering) are different phenomena with different sufferers and remediation paths. Win Barrier (vendor impediment) and Adoption Barrier (customer impediment) are distinct; an Adoption Barrier *may cause* a Win Barrier, but the causal link flows through the Signal pipeline, not a direct entity relationship. Business KPI (vendor health) and Customer Value Metric (promise fulfillment) measure entirely different things. The two dimensions connect through Customer Segment — the shared anchor — not through pairwise entity relationships. Adding cross-dimensional links between the pairs would overstate connections that are conceptual, not operational.

### Dim 2/3 entities need structural links to Dim 8 (the product)

While Dim 2 and Dim 3 don't link to each other, several entities in both dimensions benefit from traceability to the product's structural dimension (Dim 8). When a Win Outcome lists Product as an Achievement Lever, "which product structure supports this?" should be answerable. When a Delivery Friction has a product root cause, "which module or capability is involved?" enables structural root-cause analysis. When a Win Barrier or Adoption Barrier points to a product gap, "which capability is missing?" enables product-level impact analysis. These links are optional — not every Win Outcome involves Product as a lever (pure GTM outcomes don't), not every Delivery Friction has a product root (operational frictions don't), and not every barrier is product-rooted (Financial, Contractual, Cultural barriers aren't). But when the link exists, it should be explicit.

Four entities received Dim 8 structural links:
- **Win Outcome** → `Enabled by | Value Stream / Capability (Dim 8)` — when Product is an Achievement Lever
- **Delivery Friction** → `Rooted in | Module / Capability (Dim 8)` — when friction has a product root cause
- **Win Barrier** → `Structural root | Capability / Feature (Dim 8)` — when barrier points to a product gap
- **Adoption Barrier** → `Structural root | Capability / Feature (Dim 8)` — when barrier points to a product gap

### Customer Segment is the structural home for competitive intelligence

Competitive intelligence was scattered: Value Proposition had "Primary Alternative" and "Key Differentiator" fields, Win Barrier had a "Competitive" type, and Win/Loss Analysis (a Win Review type) captured competitive dynamics. But there was no per-segment competitive summary — "who do we compete against in this segment, with what, at what position?" The decision: competitive intelligence belongs as a structured field on Customer Segment (the Competitive Context sub-structure), not as a standalone entity. Rationale: competitive positioning is always segment-scoped (you may be a leader in one segment and a new entrant in another); the competitive landscape changes faster than product definition; detailed competitive playbooks and battlecards are Operating Model / Sales Enablement content, not Definition Model entities. Customer Segment's Competitive Context references Competitive-type Win Barriers, closing the loop.

### Customer Segment carries commercial planning fields

Customer Segment was structurally correct but commercially thin — industry, geography, size, and maturity were modeled, but nothing about market sizing, revenue potential, buying patterns, or strategic priority. These are not operational state; they are structural market attributes that inform every downstream decision: which segments to target with Initiatives, how to size Pricing Tiers, which Win Outcomes to prioritize. Four fields were added: Buying Motion (PLG / SLG / Hybrid — influences Win Track engagement patterns), Segment Size (TAM), Revenue Potential (per-customer and segment-level), and Strategic Priority (Primary / Secondary / Exploratory / Deprioritized).

### Business Outcome needs the buyer's own yardstick

Customer Value Metric (Dim 3) measures whether the *vendor's promise* is being fulfilled — "did we deliver 99.9% uptime?" But the buyer has their own way of measuring whether the purchase paid off — "what's our cross-border payment cost as a percentage of revenue?" This is the buyer's internal KPI, reported to their board, used to justify renewal. It's distinct from what the vendor measures. Business Outcome was enriched with two fields: Buyer's Internal KPI (how the purchasing organization measures the outcome) and Current Baseline (the buyer's starting state, establishing the "before" for ROI). These fields are often sourced from pre-sales discovery and are critical for sales positioning and renewal justification.

### TCO remains a parked gap

Total Cost of Ownership — what it costs the customer to adopt and operate the product (integration, training, migration, ongoing operational overhead) — remains a recognized gap. It is distinct from vendor pricing (Dim 2) and directly inputs the buyer's ROI calculation. The anchoring point (Customer Promise? Customer Segment? Business Outcome?) and qualification approach need further discussion. Current Baseline on Business Outcome captures some TCO-adjacent information (the buyer's current state), but a structured TCO model would require its own design session.

---

## Session: Dimension 4 Expansion — The User-Centric Dimension (Experience)

### Discovery produces Dim 4 entities

The Discovery Track is the entry point for all Dim 4 entities. User Personas are hypothesized during Signal Exploration, validated through Research Tasks, and formalized through Modeling Tasks. Jobs (JTBD) are identified through user research and validated through Experiments and Prototypes. UX Channel decisions ("Should we build a mobile app?") are PDR-level strategic choices that emerge from Deliberations. User Journeys are designed during Specification (PSD authoring) and refined through Prototypes/Spikes. This is consistent with the model's governance pattern: Discovery defines, Build implements, Run stabilizes, Win realizes.

### Jobs to Be Done (JTBD) is a standalone entity, not a field on Persona

A Job is what the user needs to accomplish — "Process a cross-border payout without errors." It sits between Pain (Dim 3 — the visceral suffering that makes the current state intolerable) and Business Outcome (Dim 3 — the strategic justification the buyer uses internally). The Job is the *user-level* goal. It deserves standalone status because: (1) Jobs are reusable across Personas — an AP Clerk and a Treasury Analyst may share the job "Verify FX rate applied to a payment." (2) Jobs map to Capabilities and Value Streams (Dim 8), creating a structural bridge between user intent and product structure. (3) Jobs map to User Journeys — a Journey *accomplishes* a Job; without the Job entity, the question "why does this Journey exist?" has no formal answer. The relationship chain: Persona → has → Job → accomplished through → Journey → experienced through → Channel.

### Job bridges Dim 4 (user intent) to Dim 8 (product structure) and Dim 3 (buyer justification)

Job → Value Stream is the primary structural mapping: "Process a cross-border payout" maps to the "Cross-Border Payout Processing" Value Stream. A Value Stream may serve multiple Jobs across different Personas (AP Clerk processes, Treasury Analyst verifies, Compliance Officer audits — same stream, different jobs). Job → Capability is a direct mapping for simpler jobs that don't require a full end-to-end flow ("Check my FX rate lock status" → "Automated Rate Locking" Capability). Both relationships are many-to-many. Job → Business Outcome (Dim 3) connects user-level goals to buyer-level justification: the AP Clerk's Job "process payouts without errors" contributes to the CFO's Business Outcome "eliminate manual FX hedging."

### UX Channel is typed by two orthogonal axes: Interaction Modality and Engagement Mode

A UX Channel is the access mechanism through which a Persona reaches the product. It is identified by a tuple of two axes:

- **Interaction Modality** (by technology): Web, Mobile, Chat, Voice, Email, CLI
- **Engagement Mode** (by service model): Self-serve, Assisted, Managed

These axes are orthogonal — you can have Web + Self-serve (typical SaaS dashboard), Web + Assisted (co-browsing with support), Chat + Self-serve (chatbot), Chat + Assisted (live agent), Voice + Managed (phone-based concierge). The matrix produces the full channel landscape. Each product defines which cells in this matrix it occupies; most products serve a subset.

### Each UX Channel is implemented by exactly one Human-Interactive Module (Dim 8)

The module archetype taxonomy already defines Human-Interactive as one of three interaction boundaries (alongside Programmatic-Interactive and Reactive/Background). Each UX Channel is the experiential definition (Dim 4); the Human-Interactive Module is the structural realization (Dim 8). One-to-one: each Channel is implemented by one HI Module; each HI Module implements one Channel. The HI Module carries its Capabilities, Features, and technical implementation; the Channel carries its experiential characteristics — interaction modality, engagement mode, and the Journeys it supports.

### Features in HI Modules should document experience attributes

Features within Human-Interactive Modules are encouraged to specify experience attributes — simplicity, ease, delight, control, speed, discoverability, error tolerance — that articulate what makes the feature's experience distinctive beyond its functional specification. "Real-time FX rate locking" is the functional feature; "one-click rate lock with visual confirmation and undo within 5 seconds" conveys the experience quality. These are not mandatory structured fields but guidance hints in the feature template, encouraging PMs and UX designers to articulate experiential intent alongside functional spec.

### Touchpoint is too granular for the Definition Model

Touchpoints ("Target Currency dropdown," "Lock Rate button") are implementation-level UI artifacts that change with every sprint. Including them in the Definition Model would bloat the model with entities no team would maintain and conflate structural product definition with screen-level design. The Definition Model captures down to User Journey (a named, purposeful flow). Touchpoints live in Build Track work artifacts — PSDs (which specify what a module should deliver), prototypes, and design specifications. The existing `dim4-touchpoint.md` entity is deprecated; Touchpoints are referenced in the Work Execution Framework as Build Track design artifacts.

### Multi-channel journey continuity uses lightweight cross-references

When the same Job can be accomplished across multiple Channels, or when a user starts a Journey on one Channel and finishes on another, two lightweight mechanisms model this without complex cross-channel flow modeling: (1) **Journey Equivalence** — references to journeys in other channels that accomplish the same Job (independent alternatives; user picks one channel). (2) **Journey Continuity** — references to journeys in other channels that this journey can hand off to or receive from (sequential handoffs; user crosses channels mid-flow). Both are simple reference fields on User Journey — no new entities, no unified cross-channel flow model.

### UX Channels carry a lifecycle — channel investment is a PDR-level decision

Deciding to build a new Channel (e.g., "build a mobile app," "add a chatbot") is a strategic investment that should be governed through Discovery: Deliberation → PDR → PSD. Channels carry statuses: `Proposed → Approved → Active → Deprecated → Retired`. This is consistent with how other structural entities with significant investment implications are governed (Pricing Tiers, Customer Releases).

### Embedded is a channel modality, not just a technical concern

Making journeys embeddable — payment widgets, Salesforce plugins, white-label components — is a deliberate product strategy, not merely a technical design choice. A component being technically reusable is a Build Track artifact concern. But a product deciding that certain journeys should be embeddable in customer or third-party applications is a channel-level decision: it requires its own HI Module, its own journey design (fragment, not full flow), and its own constraints (vendor controls the component, not the host page; must be self-contained). Embedded was added as a seventh Interaction Modality alongside Web, Mobile, Chat, Voice, Email, CLI. It participates in the same Modality × Engagement Mode matrix — an Embedded + Self-serve widget (payment form in customer's app) vs. an Embedded + Managed component (agent-operated plugin in Salesforce).

### Accessibility is a channel-level concern

Accessibility standards (WCAG 2.1 AA, Section 508) are strategic commitments that vary by channel and influence HI Module design, testing, and certification. An Accessibility Standard field was added to UX Channel. This complements Compliance Posture (Dim 3), which captures the customer-facing accessibility commitment; the Channel field captures the specific standard each channel must meet.

### Personas are product role or business domain role based

User Personas can be defined by product role ("Approver," "Analyst," "Admin") or business domain role ("AP Clerk," "Compliance Officer"). Both are valid. Most personas combine both: "AP Clerk" is a business domain role whose product role is "Payment Initiator." The product's RBAC mapping — which features, journeys, and capabilities are available to which product roles — is a Dim 8 / implementation concern. The Definition Model captures the persona archetype; the product's permission model is below the waterline.

### User Journeys engage specific Capabilities, not just Value Streams

A Journey traverses Value Streams (end-to-end flows) but also engages specific Capabilities within those streams. "Initiate and approve a cross-border payout" engages Payment Initiation, Automated Rate Locking, OFAC Screening, and Payment Execution capabilities in sequence. This finer-grained structural link enables capability-level impact analysis: if a Capability changes, which Journeys are affected? Value Stream traversal identifies the broad flow; Capability engagement identifies the specific product abilities required at each step.

---

## Session: Dimension 6 Expansion — The Ecosystem & Extensibility Dimension (Platform)

### Dim 6 is about deliberate extensibility, not incidental APIs

Every module has APIs as a byproduct of its functional design — internal interfaces because the system is distributed. These are Dim 5 (Technical) and Dim 8 (Module boundary) concerns, not Dim 6 concerns. Dim 6 exists only when there is a **deliberate product strategy** to make capabilities externally consumable for well-understood customer, partner, or third-party use cases. The decision to expose a "Payments API" is not "we have internal APIs, let's publish them." It's "we understand that customers need to integrate payment processing into their ERP systems — so we will design, build, and maintain a purposeful programmatic surface for that scenario." Dim 6 is demand-driven from the ecosystem, not supply-driven from architecture.

### Developer Persona and Programmatic User Persona belong in Dim 6, not Dim 4

Dim 4 and Dim 6 represent fundamentally different interaction paradigms — visual/experiential vs. programmatic/contractual. A developer integrating via API doesn't follow a "journey" through a "channel" with "experience attributes." They read documentation, write code, test in a sandbox, debug error responses, iterate over days/weeks. The Dim 4 vocabulary (Journey, Channel, Touchpoint) doesn't describe this work. Dim 6 needs its own persona entities for the people and systems who consume its surface.

**Developer Persona** is the human building the integration — their concerns are API ergonomics, documentation quality, SDK completeness, error message clarity, backward compatibility. These are fundamentally different from Dim 4 User Persona concerns (simplicity, delight, visual clarity).

**Programmatic User Persona** is the application or system consuming the API at runtime — a customer's ERP, a partner's middleware, a third-party app. These are not human at all. They have integration requirements, throughput needs, SLA dependencies, and error handling expectations. You cannot model a machine as a Dim 4 User Persona with "Frustrations" and "Preferred Channel."

The same human may appear in both dimensions: an Integration Engineer is a Dim 4 Persona when using the Developer Portal (Web + Self-serve channel) and a Dim 6 Developer Persona when writing API integration code. This is correct modeling — the same person interacts through two different surfaces with different design concerns, quality criteria, and stakeholders.

### Dim 6 modules are Dim 8 modules — same product, different lens

A Dim 6 module (API Module, Integration Module, Extension Module, SDK/Library Module) **is** a Dim 8 module. It appears in the Product → Module → Capability → Feature hierarchy. It has its own bounded context, Capabilities, Features, Dim 5 internals, Build Track versioning, and archetype classification. What makes it a *Dim 6* module is: (1) its purpose is externally-facing extensibility, not internal product functionality; (2) its capabilities are often compositional — curating and simplifying capabilities from other Dim 8 modules for a use-case-oriented surface; (3) it carries Dim 6-specific concerns (Developer Personas, Programmatic Personas, API contracts, versioning commitments) that other modules don't carry.

This parallels Dim 4 exactly: Human-Interactive modules are Dim 8 modules that carry Dim 4 concerns (User Personas, Jobs, Channels, Journeys). Programmatic-Interactive and extensibility modules are Dim 8 modules that carry Dim 6 concerns. The dimensions are lenses on the same structural entities, not different entities.

### API Module is protocol-agnostic — defined by contract, not transport

An API Module's identity is the **use case it serves and the contract it commits to**, not the wire protocol. A Payments API Module might expose REST endpoints for synchronous operations, gRPC for low-latency calls, Kafka topics for event streaming, SFTP/file-based interfaces for batch processing, webhooks for callbacks, and GraphQL for flexible queries — all part of one cohesive module. File/SFTP batch interfaces, Kafka events, webhook callbacks, and REST APIs are all delivery mechanisms for the same programmatic capability. The module's contract is "Create Payment," "Get Rate Quote," "payment.settled notification" — how that contract is delivered (HTTP POST, Kafka message, batch file row) is an implementation characteristic within the module, not a defining distinction between modules.

### Three Dim 6 module types represent distinct strategic decisions

Each module type is a deliberate, PDR-level product strategy choice with different architectural concerns:

- **API Module** — a named, versioned, use-case-oriented programmatic surface for external consumption. Protocol-agnostic: encompasses REST, gRPC, batch/file, event streams, webhooks, GraphQL. Composes capabilities from one or more Dim 8 modules into a cohesive programmatic interface. Design concerns: versioning, backward compatibility, rate limiting, authentication, documentation, contract design.
- **Extension Module** — a framework enabling third parties to extend the product's behavior (plugins, hooks, custom workflows). Composes extensibility points from one or more Dim 8 modules into a governed extension surface. Design concerns: plugin API stability, sandboxing, permission model, marketplace governance.
- **SDK/Library Module** — a language-specific client providing idiomatic access to API modules. Wraps Dim 6 API modules in language-specific abstractions. Design concerns: language idioms, dependency management, auto-generated vs. hand-crafted, testing support, version tracking.

### Integration Module is a connector/adapter — not another API surface

Early modeling proposed Integration Module as "APIs bundled for a scenario," but this overlapped heavily with API Module (both are use-case-oriented, both compose from Dim 8 modules, both expose programmatic interfaces). The sharpened distinction: **Integration Module is a pre-built bridge between the product and a specific external system or system category.** It includes not just "our API" but also the glue — data mappings, protocol translations, workflow adapters, and pre-built connectors that translate between the product's model and the target system's model. API Module says "here's our programmatic interface"; Integration Module says "here's a ready-made bridge between us and Salesforce/SAP/your ERP." Design concerns diverge: data format translation, protocol bridging, polling vs. push, conflict resolution, target-system-specific error handling. If a product doesn't ship connectors to specific external systems, it has API Modules but no Integration Modules — and that's a valid product decision.

### Dim 6 modules are compositional — use-case-scoped, not module-scoped

A Dim 6 module does not mirror a Dim 8 module 1:1. It may span multiple Dim 8 modules, presenting a curated subset of capabilities oriented around a specific external use case. A Dispute Case Management API Module composes capabilities from Payment Module (retrieve transactions, initiate refunds), Compliance Module (retrieve screening results), Customer Module (lookup profile), and Communication Module (send notifications) — into a single, cohesive programmatic surface. The developer interacts with the Dim 6 surface; they never need to know about the vendor's internal module boundaries. This composition — the curation, simplification, and idiomatic presentation — is Dim 6's value add over "just exposing module APIs."

### SDK and mobile apps share the same deployment pattern — Client-Distributed

The archetype taxonomy's Deployment Topology axis implicitly assumes vendor-side deployment (monolith vs. distributed microservices). But many modules run in the customer's/user's environment: mobile apps (app stores → user's device), PWAs (CDN → user's browser), SDKs (package registry → customer's codebase), embedded widgets (CDN → customer's web app), CLI tools (package manager → developer's machine). These are all **Client-Distributed** modules — built by the vendor, distributed through a channel (app store, package registry, CDN), and instantiated in the consumer's environment. They are fully valid Dim 8 modules with Capabilities, Features, Dim 5 internals, and Build Track versioning. Their Dim 7 (Operational) footprint is lighter (CI/CD + distribution channel + version adoption tracking rather than clusters and containers), but the entity structure is identical. This is not a new concept — we've been modeling mobile apps and web clients this way all along. The archetype taxonomy's Deployment Topology may evolve to explicitly name this pattern: Vendor-Hosted (Monolith/Distributed) vs. Client-Distributed.

### Payload Schema is too granular — same pattern as Touchpoints

Payload Schema (specific field definitions for request/response payloads) follows the same granularity pattern as Touchpoints in Dim 4. The contractual *existence* of a schema matters — "Create Payment has a defined input and output contract" — but the specific fields, types, and validation rules change with each version and belong in PSD and Build Track artifacts. The Definition Model captures the operation and its commitments; the schema details live below the waterline.

### SLOs are the Dim 6 analog of experience attributes in Dim 4

In Dim 4, features carry experience characteristics (simplicity, ease, delight) — the qualitative promise to users. In Dim 6, the "experience" for programmatic consumers is quantitative: performance, reliability, throughput, consistency. SLOs on API Operations declare **what the product commits to** — p99 latency, availability percentage, throughput limits, delivery guarantees — without prescribing how the vendor achieves them (that's Dim 5/Dim 7/Run Track territory). SLOs connect richly to the existing model: Customer Promise (Dim 3) derives SLAs from operational SLOs; API Compatibility Contract includes performance stability alongside interface stability; Programmatic User Personas evaluate operations by their SLO profile; Win Monitoring tracks SLO compliance; Win Reviews assess SLO fulfillment.

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

**Interface Type** (REST, gRPC, Webhook, etc.) was a standalone entity in the original Dim 6. Since API Module is protocol-agnostic — REST, batch/SFTP, Kafka, webhooks, gRPC, GraphQL are all delivery mechanisms — Interface Type becomes a field on the module ("Supported Protocols"), not a first-class entity. **Payload Schema** is demoted to PSD/Build territory (see above). Both follow the same principle: the Definition Model captures strategic commitments and structural identity; implementation and schema details live below the waterline.

---
