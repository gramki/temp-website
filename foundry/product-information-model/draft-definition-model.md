Here is the comprehensive, clean-slate reference document. I have re-architected the numbering so it flows logically from strategy down to code, eliminating the disjointed numbering from our earlier iterations.

This document defines the **Unified Product Information Model (UPIM)** — a three-model architecture:

1. **Definition Model** — What the product *is* (9 Dimensions)
2. **Work Model** — What work *exists* to move the product (5 Tracks)
3. **Operating Model** — How the organization *executes* (Coordination + Organization) — covered separately

This document covers the **Definition Model**. See `draft-work-model.md` for the Work Model. See the PIM Architecture README for the full three-model stack.

---

# Unified Product Information Model: Reference Guide

**Target Audience:** Product Managers, Enterprise Architects, Developers, QA, and Business Analysts.
**Reference Example Used Throughout:** B2B Core Payment Gateway (Cross-Border Payouts).

---

## PART I: THE 9 DIMENSIONS (THE DEFINITION MODEL)

The 9 Dimensions define the structural reality of the product at any given moment. They are grouped into four logical tiers: Strategy, Business, Technical, and Bridge (the Bridge connects the other three).

### TIER 1: STRATEGY & INTENT

*Owned by Product Management and Executive Leadership. This tier models portfolio context, strategic themes, direction (Objectives, Initiatives, Customer Releases), Signals (Problems, Needs, Opportunities), solution hypotheses (Ideas), decisions (PDRs), and specifications (PSDs).*

#### Dimension 1: The Strategy Dimension

This dimension acts as the foundational ledger of strategic direction, Signals, and proposed solutions. It is where raw ambiguity is translated into formal hypotheses, guided by Strategic Themes and Objectives.

> **Signal** is the collective term for the three input types in this dimension: **Problem**, **Need**, and **Opportunity**. A Signal is an observation or indicator — from any source, internal or external — that something about the product warrants attention. A Signal is explicitly **not** a requirement, a commitment, or an obligation. It is an input to be *interpreted* and *investigated* through the Discovery Track. Multiple Signals may point to the same underlying issue; a single Signal may be noise. The word "Signal" is chosen deliberately to foster an investigation mindset rather than a fulfillment mindset (see FAQ Q16, DR-006).
>
> **Common Signal fields** (all three types): Title, Description, Source, Source Type, Date Captured, Related Signals.
> **Common Signal lifecycle:** `New` → `Triaged` → `Exploring` / `Associated` / `Parked` → `Addressed` / `Dismissed`.

The three Signal types are classified by origin, nature, and beneficiary lens. The strategy layer (Themes, Objectives, Initiatives) provides the prioritization context that determines which Signals warrant discovery investment.

**Portfolio & Theme Entities**

* **Portfolio:** A thin, local reference entity representing the product portfolio this UPIM instance belongs to. Not owned by the UPIM — serves as a traceable origin for portfolio-scoped Strategic Themes.
* *Example:* "Payments Platform Portfolio" — contains Core Payment Gateway, Merchant Portal, Settlement Platform.


* **Strategic Theme:** A persistent, cross-cutting strategic direction that organizes discovery, customer value positioning, and investment allocation across planning horizons. Themes are either Portfolio-scoped (originate from portfolio strategy, shared across products) or Product-scoped (originated locally, may be elevated to Portfolio).
* *Structure/Relationship:*  Theme is pursued through  Objective(s).  Theme influences  Customer Segments (Dim 3) and Capabilities / Value Streams (Dim 8).
* *Status Lifecycle:* `Proposed` → `Active` → `Dormant` / `Retired`.
* *Example:* "LATAM Market Leadership" (Portfolio scope) — drives Objectives across H2 2026, H1 2027, H2 2027.


**Strategic Entities**

* **Objective:** A strategic goal over a defined planning horizon. Objectives answer "where are we going?" and are set by executive and product leadership. They provide the top-level filter for all downstream prioritization. Objectives may optionally belong to a Strategic Theme for cross-horizon continuity; not every Objective requires a Theme.
* *Structure/Relationship:*  Objective may advance  Strategic Theme (optional).  Objective is pursued through  Initiative(s).  Objective may target  Win Outcome(s) (Dim 2).
* *Status Lifecycle:* `Draft` → `Active` → `Achieved` / `Deferred`.
* *Example:* "Expand cross-border payment coverage to LATAM markets by end of H2 2026." (Theme: "LATAM Market Leadership")


* **Initiative:** A cross-track strategic program to advance one or more Objectives. An Initiative is the coordination construct that associates Signals for discovery, targets Win Outcomes, declares a **Lever Mix** (weighted from the Business Model's Lever Portfolio), and carries **embedded Targets** (like Key Results in an OKR). Initiatives drive work across all tracks — not just Discovery → Build. A "LATAM Enterprise Market Entry" Initiative with lever mix Product 40% / GTM 25% / Sales Enablement 20% / CS 15% tells downstream planners that the Win Track needs as much investment as the Build Track.
* *Structure/Relationship:*  Initiative advances  Objective(s).  Initiative ← associated →  {Problem, Need, Opportunity} (many-to-many).  Initiative targets  Win Outcome(s) (Dim 2).  Initiative declares  Lever Mix (from Business Model's Lever Portfolio).  Initiative carries  embedded Targets (per Win Outcome, time-bound, quantitative).  Initiative → Customer Release(s).  Win Track planning, enablement, and engagement work aligns to Initiatives.  Win Reviews assess Initiative target progress.
* *Status Lifecycle:* `Proposed` → `Approved` → `In Progress` → `Completed` / `Cancelled`.
* *Example:* "LATAM Enterprise Market Entry" — Lever Mix: Product 40%, GTM 25%, Sales Enablement 20%, CS 15%. Targets: "Q3: 15 LATAM Enterprise deals closed", "Q3: 85% activation within 30 days", "Q3: CAC below $25K."


* **Customer Release:** A named, business-scoped delivery of capabilities made available to customers based on business and customer needs. A Customer Release bundles the outcomes of one or more Initiatives into a coherent customer-facing delivery. Customer Releases use **names** (not version numbers) to emphasize their business identity and decouple from technical versioning. The term "Customer Release" follows the SAFe / Continuous Delivery convention: the business act of making functionality available to users, decoupled from deployment.
* *Structure/Relationship:*  Customer Release advances  Initiative(s) (many-to-many).  Customer Release references  Product Version(s) (Work Model).  Customer Release is activated by Win Track (GTM execution).
* *Status Lifecycle:* `Planning` → `In Progress` → `Ready` → `Launched` / `Cancelled`.
* *Example:* "LATAM Expansion" (bundles LATAM currency support, LATAM compliance, LATAM onboarding).

> **Terminology Note:** "Customer Release" refers to the business act of making functionality available to customers. It is distinct from an artifact "release," which follows DevOps convention — a versioned build that has passed quality gates. DevOps tooling (GitHub Releases, Helm releases, etc.) uses "release" to mean a versioned artifact — in our model, a certified **Product Version** (Build Track) is the customer-facing artifact reference; constituent **System Versions** reach `Released` status as part of that certification chain. See DR-036.

**Signal Entities**

* **Problem:** A limitation, gap, or challenge associated with delivered Modules, Capabilities, or Features — but not a functional Bug (which belongs in the Build Track). Problems can be specified at any granularity of M/C/F and are reported by internal stakeholders (PMs, QAs, SREs, Support, Pre-Sales) or external stakeholders (Customers, Users). Reporters may upvote a Problem to express their interest in resolution.
* *Signal Type:* Problem.
* *Structure/Relationship:*  Problem spawns  Ideas.  Problem ← associated →  Initiative (during planning).
* *Example:* The FX rate-lock confirmation flow takes 6 clicks — mid-market AP clerks report it as too cumbersome for high-volume payout runs.


* **Need:** A missing Capability or Feature expressed by one or more customers or prospects. A Need always originates externally and is always about expanding the product. When picked for discovery, PMs should be able to trace back to the customers or users who expressed the need. Each customer or user may upvote to express their need.
* *Signal Type:* Need.
* *Structure/Relationship:*  Need spawns  Ideas.  Need ← associated →  Initiative (during planning).
* *Example:* Three enterprise prospects require batch payout file upload (CSV/SFTP) — a capability the product does not currently offer.


* **Opportunity:** An internally originated initiative to increase revenue, reduce cost, or expand target market segments. The beneficiary is always the vendor (the builder of the product). Opportunities are created by internal stakeholders (Product, Strategy, Sales Leadership).
* *Signal Type:* Opportunity.
* *Structure/Relationship:*  Opportunity spawns  Ideas.  Opportunity ← associated →  Initiative (during planning).
* *Example:* Expanding FX payout support to LATAM currencies could capture a $2M ARR segment currently served by competitors.

**Solution & Specification Entities**

* **Idea (Hypothesis):** The proposed solution bet. It states what will be built (Hypothesis Statement), the expected metric impact, and the confidence level. An Idea is always spawned by one or more Signals. Fields include: Source Signal(s), Target Customer Segment(s) (Dim 3), Expected Impact, Confidence Level (Low/Medium/High), Effort Estimate (XS–XL).
* *Structure/Relationship:*  Idea is spawned by  Signal(s).  Idea is validated/killed by  PDR.
* *Status Lifecycle:* `Proposed` → `Investigating` → `Validated` / `Killed`.
* *Example:* "If we add one-click FX rate locking, we expect a 60% reduction in per-transaction cost because manual hedging is the primary cost driver." (Confidence: Medium, Effort: L)


* **Product Decision Record (PDR):** A formal, referenceable record of a significant product decision — including the reasoning, evidence, and trade-offs. Captures Go, Kill, and Pivot decisions alike. A PDR may correspond to **multiple Ideas** and may also exist **without a specific Idea** (e.g., from a strategic Deliberation). References Discovery Track work (Research Tasks, Experiments, Prototypes, **Deliberations**) as evidence. Fields include: Decision Type (Go/Kill/Pivot), Decision Makers, Evidence References, Rationale, Trade-offs, Confidence Level, Triggers (PSDs, Modeling Tasks, or both).
* *Structure/Relationship:*  PDR validates/kills  Idea(s).  PDR justifies  PSD(s) and/or triggers  Modeling Task(s).
* *Status Lifecycle:* `Draft` → `Final` → `Superseded`.
* *Example:* "PDR-017: Go — Real-time FX rate locking. Based on: 23 user interviews, fake-door test (14% CTR), feasibility spike, product council deliberation. Trade-off: adds FX provider dependency. Triggers: PSD-042, PSD-043, Modeling Task (update Value Stream)."


* **PSD (Product Specification Document):** The validated, approved specification that acts as the contract between Product and Engineering. A PSD is scoped to a **single module** and specifies the advancement of that module's capabilities through new features, feature refinements, or feature retirements. It is a cross-dimensional impact assessment — specifying implications across all 9 dimensions, with depth varying by module archetype. PSD authoring is substantial work that follows a Go decision — it is not an automatic outcome.
* *Structure/Relationship:*  PSD is scoped to a Module (Dim 8).  PSD decomposes into  Epics (Build Track).  PSD references  PDR (justification).  Sibling PSDs from the same PDR coordinate cross-module changes.
* *Change Types:* New Feature(s) | Feature Refinement | Feature Retirement.
* *Templates:* PSD templates are provided per module archetype (Human-Interactive, Programmatic-Interactive, Reactive/Background) — see `entities/definition-model/psd-templates/`.
* *Example:* PSD-042: "Real-Time FX Rate Lock — Invoice & Payout Processing Module" (Human-Interactive, Feature Addition).



### TIER 2: BUSINESS & MARKET

*Owned by Product Marketing, Sales Leadership, and Executives. This tier models the product as a commercial vehicle — how the vendor wins across the full AAARRR lifecycle (Awareness, Acquisition, Activation, Retention, Revenue, Referral).*

#### Dimension 2: The Vendor Value Dimension (Why It Wins)

This dimension models the complete vendor-side AAARRR lifecycle — who's involved in making the product succeed commercially, what winning looks like at each stage, what frictions the vendor faces, how revenue is structured, how success is measured, and what barriers impede the vendor. All entities are scoped directly or transitively to Customer Segments (Dim 3), making Customer Segment the shared anchor between "Why Buy" (Dim 3) and "Why It Wins" (Dim 2).

> **Governance Note:** Any change to Dim 2 entities requires a corresponding PDR — whether originating from a Deliberation (strategic pricing design, AAARRR target-setting) or from the Signal pipeline (field observations of friction/barriers → Discovery → PDR). Win Stakeholders contribute observations as Signals and participate in Deliberations, but the PM/PMM is the Dim 2 modeler through Modeling Tasks.

* **Business Model:** The fundamental revenue engine that describes how the vendor generates income from this product. Lightweight structural root — all other Dim 2 entities derive from the Business Model. The Business Model also defines the product's **Lever Portfolio** — the finite, referenceable set of levers available to advance Win Outcomes. Levers are categorized as: **Product** (feature development → Build Track), **GTM** (marketing, pricing communication, partnership execution → Win Track), **Sales Enablement** (competitive tools, training → Win Track), **Customer Success** (onboarding, retention, expansion programs → Win Track), **Operational** (internal process, hiring → Operating Model). The lever portfolio varies by product — a developer API platform may not have a Sales Enablement lever; an enterprise SaaS product may use all five. Initiatives reference the lever portfolio when declaring their lever mix.
* *Structure/Relationship:*  Business Model defines the frame for  Pricing Tier(s) and  Value Metric(s).  Business Model defines the  Lever Portfolio referenced by Win Outcomes and Initiatives.
* *Example:* Transaction-based B2B SaaS (primary: per-transaction fees; secondary: FX markup; tertiary: implementation services). Lever Portfolio: Product, GTM, Sales Enablement, Customer Success, Operational.


* **Win Stakeholder:** A role in the vendor's AAARRR journey — a specific function that engages with customers or prospects to make the product commercially successful. Each Win Stakeholder has distinct concerns, friction points, and success criteria at their stage(s) of the lifecycle. Win Stakeholders are not organizational roles (those belong in the Operating Model) — they are functional archetypes that the product's commercial success depends on.
* *Structure/Relationship:*  Win Stakeholder is engaged with  Customer Segment(s).  Win Stakeholder endures  Delivery Friction(s).  Win Stakeholder is responsible for  Win Outcome(s).
* *AAARRR Stage Examples:* Awareness (Marketing Manager, Developer Advocate), Acquisition (Account Executive, Pre-Sales Engineer, Solution Architect), Activation (Implementation Consultant, CS Manager), Retention (CS Manager, Support Engineer), Revenue (Account Manager, Finance/Billing), Referral (CS Manager, Marketing Manager).
* *Example:* Pre-Sales Engineer — engaged with LATAM Enterprise segment; key concerns: POC success, integration feasibility, technical fit demonstration.


* **Win Outcome:** What success looks like for the vendor at a specific AAARRR stage for a specific Customer Segment. Not a time-bound Objective (Dim 1) but a structural definition of "what winning means here." Objectives and Initiatives (Dim 1) reference Win Outcomes as targets. Each Win Outcome carries **Achievement Levers** — categorized from the Business Model's Lever Portfolio — that identify what kinds of effort can advance it. This forces the question at modeling time: "Is this primarily a product problem, a GTM problem, or both?" Without explicit levers, organizations default to building features when the actual lever may be sales enablement or marketing.
* *Structure/Relationship:*  Win Outcome is scoped to  Customer Segment(s).  Win Outcome is evidenced by  Business KPI(s).  Win Outcome is the responsibility of  Win Stakeholder(s).  Win Outcome declares  Achievement Lever(s) from the Business Model's Lever Portfolio.  Win Outcome is enabled by  Value Stream(s) / Capability(ies) (Dim 8) when Product is a lever.  Objective / Initiative (Dim 1) may reference  Win Outcome(s) as targets.  Delivery Friction may undermine  Win Outcome.
* *Example:* "LATAM Enterprise — Activation: Customer processes first live cross-border transaction within 30 days of contract signing." Achievement Levers: Product (primary — self-service onboarding flow), Customer Success (secondary — LATAM implementation playbook).


* **Delivery Friction:** A specific, concrete suffering or inefficiency experienced by a Win Stakeholder in the vendor's AAARRR journey. Delivery Frictions are discoverable, not self-evident — they surface through field experience and must be investigated, not assumed. Together with Win Outcome, Delivery Friction forms the complete "Why It Wins" picture — the vendor wants the outcome (strategic), but the friction makes it *hard* (operational).
* *Structure/Relationship:*  Delivery Friction is endured by  Win Stakeholder(s).  Delivery Friction is scoped to  Customer Segment(s) (transitively through Win Stakeholder or directly).  Delivery Friction undermines  Win Outcome(s).  Delivery Friction may be rooted in  Module(s) / Capability(ies) (Dim 8) when the friction has a product root cause.  Delivery Friction may surface as an Opportunity or Problem Signal in Dim 1.
* *Example:* "Implementation Consultant spends 60 days on custom FX provider integration per LATAM Enterprise customer — $80K per-customer cost, delays go-live beyond 30-day target."


* **Pricing Tier / Package:** A bundled commercial offering targeting a specific Customer Segment. A Package groups Features (Dim 8) into a marketable unit with associated pricing structured around Value Metrics.
* *Structure/Relationship:*  Pricing Tier targets  Customer Segment(s) (Dim 3).  Pricing Tier contains  Feature(s) (Dim 8).  Pricing Tier is priced along  Value Metric(s).  Pricing Tier operates within the  Business Model.  Win Barrier may challenge  Pricing Tier.
* *Status Lifecycle:* `Draft` → `Active` → `Deprecated` / `Retired`.
* *Example:* "Enterprise Volume Plan" — targets LATAM Enterprise and US Enterprise segments; includes cross-border payouts, batch processing, dedicated support; priced at 0.5% per transaction + FX markup.


* **Value Metric (Pricing Axis):** The unit of measurement along which revenue scales. Defines the commercial mechanism that ties product usage to revenue generation. A product may have multiple Value Metrics across different Pricing Tiers.
* *Structure/Relationship:*  Value Metric is used by  Pricing Tier(s).  Value Metric is defined by the  Business Model.
* *Example:* Per-transaction fee (0.5% flat), FX markup (1% on baseline rate), monthly platform fee ($5K/month for Enterprise).


* **Business KPI:** A quantitative measure of the product's commercial health at a specific AAARRR stage. Business KPIs are typed (Revenue, Cost, Activity) and carry explicit targets, thresholds, and measurement cadence. The Definition Model captures metric definitions and targets — actual measured values are operational state.
* *Structure/Relationship:*  Business KPI evidences  Win Outcome(s).  Business KPI is scoped to  Customer Segment(s) (transitively through Win Outcome).  Opportunity Signal (Dim 1) may target improvement of a  Business KPI.
* *KPI Types:* **Revenue** (ACV, MRR, LTV, Net Revenue Retention), **Cost** (CAC, Implementation Cost, Cost-to-Serve, Infrastructure Cost per Customer), **Activity** (Activation Rate, Time-to-First-Value, NPS, Churn Rate, Referral Rate).
* *Example:* "Customer Acquisition Cost (CAC) — LATAM Enterprise: target <$25K, threshold $40K, measured monthly, owner VP Sales. AAARRR stage: Acquisition."


* **Win Barrier:** A known structural impediment that prevents the vendor from achieving a Win Outcome for a given Customer Segment. Always articulated with the aggrieved party as a Win Stakeholder or the vendor generally. Distinct from Adoption Barrier (Dim 3): Adoption Barrier captures the customer's impediment to purchasing or adopting; Win Barrier captures the vendor's impediment to winning commercially.
* *Types:* Competitive, Technical, Regulatory, Operational, Financial, Contractual, Resource, Market.
* *Structure/Relationship:*  Win Barrier blocks  Win Outcome(s).  Win Barrier affects  Win Stakeholder(s) or the vendor.  Win Barrier is scoped to  Customer Segment(s).  Win Barrier may challenge  Pricing Tier.  Win Barrier may have a structural root in  Capability / Feature (Dim 8) when the barrier points to a product gap.  Win Barrier may surface as a Signal in Dim 1.
* *Example:* "Competitor offers 30-day free trial; our minimum commitment is annual — blocks Acquisition Win Outcome for US Mid-Market. Aggrieved: Account Executive."



#### Dimension 3: The Customer Value Dimension (Why Buy)

This dimension models the complete "Why Buy" logic for the purchasing organization — who buys, what they achieve, what they suffer, what the product promises, how those promises are measured, and what barriers impede adoption. It answers the customer's question: "Why should I buy this product, and what will I get?"

> **TCO Note (parked for later):** Total Cost of Ownership — what it costs the customer to adopt and operate the product (integration, training, migration, ongoing operational overhead) — is a recognized gap. TCO is distinct from vendor pricing (Dim 2) and directly inputs the ROI calculation. The right anchoring point (Customer Promise? Customer Segment?) and qualification approach need further discussion. Parked for a future refinement cycle.

* **Customer Segment:** A defined group of potential buyers sharing common characteristics — industry vertical, company size, geography, maturity stage. Segments have distinct buyer personas, outcomes, pains, promise expectations, and adoption patterns. All other Dim 3 entities are anchored to one or more Customer Segments. Customer Segment also carries **Buying Motion** (PLG / SLG / Hybrid), **Segment Size (TAM)**, **Revenue Potential**, **Strategic Priority**, and a **Competitive Context** (key competitors, competitive position, primary threats, differentiators, incumbent/status quo) — making it the structural home for segment-level commercial planning and competitive intelligence.
* *Structure/Relationship:*  Segment has  Buying Persona(s).  Segment has  Pain(s).  Segment is promised  Customer Promise(s).  Segment is blocked by  Adoption Barrier(s).  Segment is scoped by  Win Outcome(s) (Dim 2).  Segment's Competitive Context references  Competitive-type Win Barrier(s) (Dim 2).
* *Example:* "LATAM Enterprise (500+ employees, cross-border payables, SLG buying motion, ~2,000 TAM, $500K+ ACV, Primary priority)" vs. "US Mid-Market (100–499 employees, Hybrid buying motion, ~15,000 TAM, $30K–50K ACV, Secondary priority)."


* **Buying Persona:** A role within the purchasing organization's buying committee that influences or decides the purchase. Each Buying Persona represents a distinct evaluation lens. Role types: **Economic Buyer** (budget holder — evaluates ROI), **Technical Buyer** (IT/Eng — evaluates integration, security, architecture), **User Buyer** (department head — evaluates usability, team adoption), **Coach/Champion** (internal advocate — navigates buying process). Buying Personas *care about* Pains even if they don't personally endure them.
* *Structure/Relationship:*  Buying Persona belongs to  Customer Segment.  Economic Buyer pursues  Business Outcome(s).  Buying Persona cares about  Pain(s).
* *Example:* CFO (Economic), CTO (Technical), AP Ops Manager (User), Treasury Director (Coach) at LATAM Enterprise.


* **Business Outcome:** The macro-level benefit the buyer needs to achieve — the buyer's "job to be done" at a strategic level. Business Outcomes are what the Buying Persona (typically Economic Buyer) uses to justify the purchase internally. Each Business Outcome carries a **Buyer's Internal KPI** (how the purchasing organization measures this outcome — distinct from Customer Value Metric, which measures the vendor's promise) and a **Current Baseline** (the buyer's starting state, establishing the "before" for ROI).
* *Structure/Relationship:*  Business Outcome is pursued by  Buying Persona (Economic Buyer).  Business Outcome is addressed by  Value Proposition (Customer Promise subtype).
* *Example:* "Eliminate manual FX hedging and reduce cross-border wire fees" — Buyer's KPI: cross-border payment cost as % of revenue (reported quarterly); Current Baseline: $6.25/transaction, 3 FX systems, 4 hours/day manual reconciliation.


* **Pain:** A specific, concrete suffering or frustration experienced by a User Persona (Dim 4) in their current workflow. Pains are *endured* by users but *cared about* by Buying Personas, who are motivated to purchase a solution that relieves them. Together with Business Outcome, Pain forms the complete "Why Buy" motivation — the buyer wants the outcome (strategic), but the pain makes it feel *urgent* (visceral).
* *Structure/Relationship:*  Pain is endured by  User Persona (Dim 4).  Pain is cared about by  Buying Persona(s) (Dim 3).  Pain is relieved by  Value Proposition (Customer Promise subtype).
* *Example:* "AP Clerk spends 4 hours/day manually reconciling FX transactions across 3 systems" — endured by AP Clerk (Dim 4), cared about by CFO (cost) and AP Ops Manager (productivity).


* **Customer Promise:** The product's formal commitment to a Customer Segment. Customer Promise has three subtypes, each representing a distinct category of commitment:

  * **Value Proposition** (subtype): Articulates how the product's capabilities deliver the buyer's outcomes and relieve user pains. Maps Business Outcomes and Pains to Value Streams (for outcome-based promises) or Capabilities (for ability-based promises) in Dim 8. Includes competitive positioning — why this product over the alternative.
    * *Outcome-mapped example:* "Reduce cross-border payment cost by 60%" → addresses Outcome "Eliminate manual FX hedging" + relieves Pain "4 hours/day manual reconciliation" → maps to Value Stream "Cross-Border Payout Processing."
    * *Ability-mapped example:* "Real-time FX rate locking for 24 hours" → relieves Pain "15% rate expiry on transactions" → maps to Capability "Automated Rate Locking."

  * **Service Commitment** (subtype): Guarantees reliability, performance, and support levels. Includes availability SLA, performance SLA, support SLA, data SLA, and breach remedies. Overlaps with Dim 7 (Operational) — Dim 3 captures the customer-facing commitment; Dim 7 captures the infrastructure that delivers it.
    * *Example:* "99.9% API uptime, sub-200ms P95 latency, SEV-1 incidents: 15-minute response."

  * **Compliance Posture** (subtype): Certifies that the product meets regulatory, security, or industry standards. Compliance goes beyond operations — it is a core aspect of the product that influences many capabilities (Dim 8). It is an essential customer trust element in the buying decision.
    * *Example:* "PCI-DSS Level 1 certified, SOC 2 Type II audited, GDPR compliant."

* *Structure/Relationship:*  Customer Promise is made to  Customer Segment.  Customer Promise is evidenced by  Customer Value Metric(s).  Adoption Barrier may challenge  Customer Promise.


* **Customer Value Metric:** A measurable indicator that defines whether a Customer Promise is being kept. Unified metric entity with subtypes corresponding to promise types. All subtypes share a common structure (target, SLA threshold, measurement method, frequency) but measure different things. The Definition Model captures metric *definitions and targets* only — actual measured values are operational state tracked at runtime.

  * **ROI Metric** (subtype): Measures Value Proposition claims. Different for Value Stream-mapped and Capability-mapped promises.
    * *Value Stream-mapped examples:* End-to-end cycle time ("target <4 hours, SLA threshold <8 hours"), throughput ("500+ payouts per batch"), cost reduction ("60% lower per-transaction cost").
    * *Capability-mapped examples:* Feature performance ("FX rate locked within 200ms"), coverage ("35+ supported currencies").

  * **Service Level Metric** (subtype): Measures Service Commitment guarantees.
    * *Examples:* Uptime (target 99.9%, SLA threshold 99.5%), P95 latency, mean time to resolve SEV-1 incidents.

  * **Compliance Metric** (subtype): Measures Compliance Posture adherence.
    * *Examples:* Audit pass/fail, certification validity period, vulnerability remediation time.

* *Structure/Relationship:*  Customer Value Metric evidences  Customer Promise.


* **Adoption Barrier:** A known impediment to purchase or adoption within a segment. Types: Regulatory, Technical, Organizational, Competitive, Financial, Contractual, Data, Cultural. Barriers may directly challenge or undermine a Customer Promise — exposing gaps between what the product promises and what prevents the customer from realizing that promise. Understanding barriers informs discovery prioritization — a barrier may surface as a Signal (Problem or Need) in Dim 1.
* *Structure/Relationship:*  Adoption Barrier blocks  Customer Segment.  Adoption Barrier may challenge  Customer Promise.  Adoption Barrier may have a structural root in  Capability / Feature (Dim 8) when the barrier points to a product gap.
* *Example:* "LATAM enterprises require local data residency" (Regulatory, Blocker — challenges Compliance Posture "GDPR compliant" — structural root: Data Storage — Regional Residency capability, missing).



### TIER 3: TECHNICAL EXECUTION (THE MODULES)

*Owned by Tech Leads, Developers, DevOps, and UX Designers. These dimensions describe the physical reality of specific modules.*

#### Dimension 4: The User-Centric Dimension (Experience)

This dimension models the complete user experience surface — who uses the product, what they need to accomplish, how they access the product, and what paths they follow. All Dim 4 entities are discovered and formalized through the Discovery Track (Research Tasks, Deliberations, Prototypes, PSDs). Dim 4 connects upward to Dim 3 (Persona endures Pain, Job contributes to Business Outcome) and downward to Dim 8 (Job maps to Value Streams/Capabilities, Channel is implemented by Human-Interactive Module).

* **User Persona:** A role archetype that uses the product's Human-Interactive Modules. Distinct from Buying Persona (Dim 3), which represents purchase decision-makers. User Personas *endure* Pains (Dim 3) and *have* Jobs to be done. Multiple User Personas may exist within the same Customer Segment — they interact with different parts of the product for different reasons.
* *Structure/Relationship:*  User Persona endures  Pain(s) (Dim 3).  User Persona has  Job(s) (Dim 4).  User Persona follows  User Journey(s) (Dim 4).  Buying Persona (Dim 3) cares about  User Persona's Pains.
* *Example:* AP Clerk — endures "4 hours/day manual FX reconciliation"; has Jobs: "Process a cross-border payout," "Verify FX rate applied."

* **Job (JTBD):** What the User Persona needs to accomplish — the user-level "job to be done." A Job is a functional, emotional, or social goal that the product must enable. Jobs bridge user intent (Dim 4) to product structure (Dim 8) and buyer justification (Dim 3). Jobs are reusable across Personas — different personas may share the same functional job but approach it through different Journeys and Channels.
* *Structure/Relationship:*  Job is pursued by  User Persona(s) (Dim 4).  Job is accomplished through  User Journey(s) (Dim 4).  Job is enabled by  Value Stream(s) / Capability(ies) (Dim 8).  Job contributes to  Business Outcome(s) (Dim 3).
* *Example:* "Process a cross-border payout without errors" — pursued by AP Clerk; enabled by Value Stream "Cross-Border Payout Processing"; contributes to Business Outcome "Eliminate manual FX hedging."

* **UX Channel:** The access mechanism through which a Persona reaches the product, typed by two orthogonal axes: **Interaction Modality** (Web, Mobile, Chat, Voice, Email, CLI) and **Engagement Mode** (Self-serve, Assisted, Managed). Each UX Channel is implemented by exactly one Human-Interactive Module (Dim 8). Channel investment decisions are PDR-level strategic choices.
* *Structure/Relationship:*  UX Channel is implemented by  Human-Interactive Module (Dim 8).  UX Channel supports  User Journey(s) (Dim 4).
* *Interaction Modality:* Web (browser), Mobile (native app), Chat (conversational), Voice (IVR/assistant), Email (asynchronous), CLI (developer-facing), Embedded (widget/plugin/component hosted in customer's or third-party application — a deliberate product strategy to make journeys embeddable).
* *Engagement Mode:* Self-serve (user acts independently), Assisted (user + agent collaborate), Managed (agent acts on behalf of user).
* *Status Lifecycle:* `Proposed` → `Approved` → `Active` → `Deprecated` → `Retired`.
* *Example:* "Web + Self-serve" (customer dashboard, implemented by Dashboard Web Module) vs. "Chat + Assisted" (live agent support, implemented by Support Chat Module).

* **User Journey:** The end-to-end path a User Persona follows to accomplish a Job through a specific UX Channel. The same Job may have different Journeys across different Channels — "Approve a cross-border payout" has a Web Journey (full form) and a Mobile Journey (simplified approval). Journeys carry cross-channel references: **equivalence** (same Job, different Channel — independent alternatives) and **continuity** (sequential handoff across Channels).
* *Structure/Relationship:*  User Journey accomplishes  Job(s) (Dim 4).  User Journey is followed by  User Persona(s) (Dim 4).  User Journey is experienced through  UX Channel (Dim 4).  User Journey traverses  Value Stream(s) (Dim 8).  User Journey engages  Capability(ies) (Dim 8).  User Journey may be equivalent to / continuable from  other User Journeys (cross-channel).
* *Example:* "Initiate and approve a cross-border payout" (Web + Self-serve) — AP Clerk follows this Journey to accomplish Job "Process a cross-border payout"; traverses Value Stream "Cross-Border Payout Processing"; equivalent to "Approve payout" (Mobile + Self-serve); continuable from "Request payout approval" (Email + Self-serve).

> **Touchpoint Note:** Touchpoints (specific UI elements — buttons, dropdowns, forms) are below the Definition Model's waterline. They are Build Track work artifacts (design specs, wireframes, UI component inventories) produced during PSD authoring and prototyping. The Definition Model captures down to User Journey; screen-level detail lives in work artifacts. See `dim4-touchpoint.md` (deprecated).



#### Dimension 5: The Technical & Architectural Dimension (Engineering)

This dimension captures the product's **technical model** — how it is architected, what systems implement the functional modules, what technology choices were made, what dependencies exist, and how systems interact. Dim 5 answers: "How is the product built?" It provides the technical perspective of the same product that Dim 8 describes functionally — where Dim 8 says "Payments Module with Cross-Border Payments capability," Dim 5 says "implemented by payments-service (Java/Spring Boot) communicating via Kafka events, depending on PostgreSQL and a third-party FX rate provider." Together they give the complete structural picture. See DR-024.

> **Dim 8 / Dim 5 Duality:** Dim 8 is the functional view (Product → Module → Capability → Feature, Value Streams). Dim 5 is the technical view (Architecture Model → Product Specification → System → Component, Interaction Flows, Dependencies). Two lenses, same product. Dim 8 serves PM and business stakeholders; Dim 5 serves architects and engineering leadership. Clean 1:1 pairings: **Product ↔ Product Specification**, **Module ↔ System** (many-to-many across modules). Components are the atomic deployable artifacts; Systems are their operational deployment groupings. See DR-035, DR-036.

* **Architecture Model:** The macro-level architectural strategy — how the product is designed and constructed. Lightweight structural root — all other Dim 5 entities exist within the Architecture Model's frame. Parallel to Business Model (Dim 2) — "how we make money" — and Infrastructure Model (Dim 7) — "how we run it." The Architecture Model captures "how we build it."
* *Fields:* Architectural Style (microservices / modular monolith / event-driven / serverless / hybrid), Key Principles (separation of concerns, DDD, API-first, event sourcing, etc.), Quality Attribute Priorities (maintainability, testability, extensibility, modularity — ordered), Technology Strategy (language portfolio, framework standards, cloud-native vs. portable), Architectural Evolution Direction (current state → target state).
* *Example:* "Event-driven microservices on AWS — 22 services organized by bounded contexts, Java/Spring Boot for transactional services, Python for analytics/batch, PostgreSQL for transactional data, Kafka for inter-service events, DDD principles with anti-corruption layers at domain boundaries. Evolution: migrating from shared database to database-per-service (3 of 22 complete)."

* **Product Specification:** The technical twin of Product (Dim 8) — a 1:1 companion that declares which Systems compose the product. Lists **all** Systems as equal members: product-facing Systems (tenant workflows, portals, integrations) and operational/SRE Systems (monitoring, reconciliation, health checks). There is no separate Package layer partitioning tenant-serving from operator-facing Systems; `Purpose / Serving Persona(s)` on each System is the distinguishing field. *(Introduced by DR-036.)*
* *Structure/Relationship:*  Product Specification is the twin of  Product (Dim 8, 1:1).  Product Specification composes  System(s) (Dim 5).  Product Specification is instantiated by  Product Version(s) (Track 2).  Product Specification exists within  Architecture Model (Dim 5).
* *Fields:* Product (Dim 8 ref), Systems (Dim 5 refs), Status (`Draft` → `Active` → `Superseded`).
* *Example:* "Core Payment Gateway Product Specification" — Systems: payments-system, fx-system, compliance-system, customer-portal-system, payments-monitoring-system (SRE), settlement-reconciliation-system (SRE).

* **System:** The operational deployment grouping of Components — what SRE versions and deploys as a whole. When SRE deploys "Payments System v3.1," they deploy a **sealed System Version** — an immutable BOM of Component Versions for that System. The technical counterpart to Module (Dim 8): where Module captures the functional boundary ("Payments Module"), System captures the operational deployment boundary ("payments-system"). Product-facing and operational Systems are structurally equal; persona references distinguish who they serve. *(Amended from DR-024 by DR-035; deployment semantics clarified by DR-036.)*
* *Structure/Relationship:*  System implements  Module(s) (Dim 8, many-to-many).  System is declared in  Product Specification (Dim 5).  System contains  Component(s) (Dim 5).  System depends on  Dependency(ies) (Dim 5).  System is deployed to  Deployment Environment(s) (Dim 7) via  System Deployment Specification(s) (Track 3).  System participates in  Interaction Flow(s) (Dim 5).  System has  Technical Knowledge Base (Dim 5).  System's architectural decisions are recorded as  ADR(s) (Dim 5).  System serves  Persona(s) (Dim 4) / Operational Persona(s) (Dim 7).  System is versioned as  System Version(s) (Track 2).
* *Fields:* Name, Technology Stack (language, framework, runtime), Data Store(s) (type + technology), Communication Protocols (REST, gRPC, Kafka, SFTP, etc.), Repository Reference, Module Mapping (which Dim 8 Modules this System implements), Purpose / Serving Persona(s) (which Persona(s) this System serves — distinguishes product Systems from operational Systems).
* *Example:* "payments-system" — operational grouping containing payments-service, payment-reconciler, and payment-notification-worker. Implements: Payments Module (primary), Settlement Module (partial). Deployed to: Production US-East, Production LATAM, Staging EU-West.

* **Component:** The atomic deployable artifact within a System — a container image, Lambda package, frontend bundle, or similar independently buildable unit. CI pipelines produce **Component Versions** (Track 2) continuously. Components are independently buildable (each has its own build artifact and CI pipeline) but are not independently deployed to production; they are deployed as part of their parent System's sealed System Version. Has a **Component Archetype** enum classifying the artifact type (API Service, Web Application, Event-Driven Worker, Batch Job, Data Store, Integration Adapter, Gateway, CLI/SDK — see `draft-archetypes.md`). *(Amended from DR-024 by DR-035; versioning tier clarified by DR-036.)*
* *Structure/Relationship:*  Component belongs to  System (Dim 5).  Component may map to  Capability(ies) (Dim 8).  Component is versioned as  Component Version(s) (Track 2).
* *Fields:* Name, Component Archetype (enum), Technology Stack (when different from parent System), Repository Reference, Responsibility.
* *Example:* "payments-service" — Component within payments-system. Archetype: API Service. Technology: Java 21 / Spring Boot 3.2. Responsibility: exposes REST API for payment initiation; produces/consumes Kafka events. "payment-reconciler" — Component within payments-system. Archetype: Batch Job. Responsibility: nightly reconciliation of settlement records.

* **Dependency:** An external system, service, library, or infrastructure resource the product depends on but does not own. Two subtypes: **Third-Party Service** (FX rate providers, bank networks, Twilio, SendGrid, Stripe) and **Infrastructure Resource** (PostgreSQL, Redis, Kafka, AWS SQS, S3, Lambda). Dependencies are risk, cost, and architectural constraint surfaces — what happens when this dependency fails? What does it cost? Are we over-reliant?
* *Structure/Relationship:*  Dependency is used by  System(s) (Dim 5).  Dependency may impose  Operational Constraint(s) (Dim 7).  Dependency has cost implications for  Infrastructure Model (Dim 7).
* *Fields:* Name, Type (Third-Party Service / Infrastructure Resource), Provider/Vendor, Criticality (Critical / Important / Convenience), Failure Impact, Alternative/Fallback, Cost Model, SLA (provider's commitment).
* *Example:* "CurrencyCloud FX API" — Type: Third-Party Service, Criticality: Critical (no fallback for FX rate quotes), Provider: CurrencyCloud Ltd, Failure Impact: all FX operations blocked, SLA: 99.9% availability / p99 < 200ms, Cost: per-quote pricing. "PostgreSQL 15" — Type: Infrastructure Resource, Criticality: Critical, Provider: AWS RDS, Failure Impact: transactional data unavailable, Alternative: Aurora PostgreSQL (migration path documented in ADR-008).

* **Interaction Flow:** How Systems communicate to fulfill Value Streams (Dim 8). The technical realization of the functional flow — where Value Stream says "Cross-Border Payout Processing traverses Invoice → FX → Compliance → Payment → Settlement," Interaction Flow says "payment request enters via REST → FX rate fetched via gRPC → compliance check via async Kafka event → payment executed via REST to bank-adapter → settlement confirmation via Kafka event." Interaction Flows anchor sequence diagrams and data flow diagrams — the entity defines the pattern; the diagram is a visualization artifact.
* *Structure/Relationship:*  Interaction Flow realizes  Value Stream(s) (Dim 8, technical counterpart).  Interaction Flow involves  System(s) (Dim 5).  Interaction Flow uses  Dependency(ies) (Dim 5, when external systems participate).
* *Fields:* Name, Realizes (Value Stream reference), Participating Systems (ordered sequence), Integration Style per step (sync request-reply / async event / batch / RPC), Protocol per step, Error Handling Strategy (retry, circuit breaker, compensation, dead-letter), Data Format (JSON, Protobuf, Avro, CSV).
* *Example:* "Cross-Border Payout Processing Flow" — Realizes: "Cross-Border Payout Processing" (Dim 8 Value Stream). Sequence: merchant-portal (REST) → payments-api (REST) → fx-service (gRPC, sync) → compliance-service (Kafka event, async, await response within 5s) → bank-adapter (REST, sync, circuit breaker on failure) → settlement-service (Kafka event, async, at-least-once delivery). Error handling: compensating transaction on bank-adapter failure; dead-letter queue for compliance timeout.

* **Architecture Decision Record (ADR):** A formal record of a significant technical or architectural decision — the Dim 5 counterpart of PDR (Dim 1). ADR captures what was decided architecturally and why — technology choices, system decomposition, integration patterns, data architecture, deprecation of technical approaches. Distinct from PDR: PDR captures product-level decisions ("Go on LATAM market"); ADR captures technical-level decisions ("Use PostgreSQL for transactional data because..."). Three relationship patterns: PDR triggers ADR(s), ADR exists independently, ADR constrains PDR. ADRs can be produced by both Discovery Track (Deliberation-driven) and Build Track (implementation-driven). Follows the Nygard ADR format (Context, Decision, Consequences, Status).
* *Structure/Relationship:*  ADR may be triggered by  PDR(s) (Dim 1).  ADR affects  System(s) (Dim 5).  ADR affects  Dependency(ies) (Dim 5).  ADR affects  Interaction Flow(s) (Dim 5).  ADR may supersede  ADR(s) (Dim 5).
* *Fields:* ID, Title, Status (Proposed / Accepted / Deprecated / Superseded), Context (what prompted the decision), Decision (what was decided), Consequences (positive and negative), Quality Attributes Addressed, Triggered by (PDR reference, if applicable), Supersedes/Superseded-by (ADR references), Affected Systems.
* *Example:* "ADR-012: Adopt event-driven architecture for inter-service payment flow. Context: synchronous REST calls between 5 services create cascading failure risk and 3s+ end-to-end latency. Decision: Replace synchronous inter-service calls with Kafka events for all non-query interactions. Consequences: (+) eliminates cascading failures, enables independent scaling, supports future CQRS; (−) adds Kafka dependency, increases debugging complexity, eventual consistency challenges. Triggered by PDR-023 (LATAM expansion requires <1s payment processing). Affects: payments-service, fx-service, compliance-service, bank-adapter, settlement-service."

* **Technical Knowledge Base:** A per-System assessment of whether the system's technical knowledge is current and complete — covering documentation, guides, and playbooks that enable Run and Win teams to understand and operate the system. Parallels Operational Readiness (Dim 7): a single instance per System with quality dimensions and coverage status. The actual documents are Work Model artifacts; this entity tracks "does the knowledge exist and is it current?"
* *Structure/Relationship:*  Technical Knowledge Base is scoped to  System (Dim 5).  Technical Knowledge Base is assessed by  Build Track / Run Track activities.
* *Fields:* System (reference), Overall Status (Not Assessed / Gaps Identified / Partially Documented / Fully Documented), Architecture Documentation (status + last updated), Operational Runbook (status + last updated), Release Notes (status + last updated), Integration Guide (status + last updated), Win Technical Guide (status + last updated), Troubleshooting Playbook (status + last updated), Gaps (list with severity and remediation plan).
* *Example:* "payments-service Technical Knowledge Base" — Overall: Partially Documented. Architecture Doc: Current (2026-01, covers service boundaries, data model, event contracts). Operational Runbook: Gaps (deployment runbook exists; failover runbook missing). Release Notes: Current (auto-generated from Component Version / System Version build pipeline). Integration Guide: Stale (last updated 2025-06, doesn't cover new Kafka events). Win Technical Guide: Current (technical overview for pre-sales, updated 2026-01). Troubleshooting Playbook: Missing. Gaps: (1) Failover runbook — high severity, remediation Q2 2026. (2) Troubleshooting playbook — medium, remediation Sprint 16.

> **Work Model: Versioning Chain (Build Track).** The Build Track produces three versioned artifact tiers aligned with Dim 5 structure. See `draft-work-model.md` for full Work Model detail; DR-036 is authoritative.
>
> | Tier | Artifact | Scope | Verification |
> |---|---|---|---|
> | Atomic | **Component Version** | Single Component build output | Per-Component quality gates (CI) |
> | Integrated | **System Version** | Sealed, immutable BOM of Component Versions for one System | Component-integration verification within the System boundary |
> | Complete | **Product Version** | Certified composition of System Versions for the Product | Cross-System integration verification and certification |
>
> **Module Version removed (DR-036):** Module (Dim 8) remains essential for product language, PSD scoping, and entitlement — but it is not an operational versioning boundary. Product Version composes System Versions directly. Capability availability is traced: Module → System → System Version in the current Product Version BOM.
>
> **All System Versions via Build Track (DR-036):** Build Track produces System Versions for product-facing and operational Systems alike (including SRE-introduced operational Systems). Run Track owns deployment governance and operations, not a separate engineering artifact layer.

**Deprecated and deleted from original Dim 5:**

* ~~**Subsystem / Service**~~ — Subsumed by the expanded System entity (DR-024). Entity file `dim5-subsystem.md` deleted (DR-035).
* ~~**Class / Component**~~ — Below the Definition Model waterline. Code-level structure belongs in PSD/Build Track artifacts. Entity file `dim5-class-component.md` deleted (DR-035).
* ~~**Function / Method**~~ — Below the Definition Model waterline. Entity file `dim5-function-method.md` deleted (DR-035).



#### Dimension 6: The Ecosystem & Extensibility Dimension (Platform)

This dimension captures a product's **deliberate extensibility strategy** — the programmatic surfaces, personas, and contracts through which external developers, applications, and systems consume and extend product capabilities. Dim 6 entities exist only when there is a strategic decision to make capabilities externally consumable for well-understood use cases (demand-driven from ecosystem, not incidental API exposure). See DR-021.

**Personas:**

* **Developer Persona:** The human building integrations — integration engineers, partner developers, internal platform developers. Concerns: API ergonomics, documentation quality, SDK completeness, error clarity, backward compatibility. Distinct from Dim 4 User Persona (different interaction paradigm, different quality criteria). The same human may appear in both: a Dim 4 Persona when using the Developer Portal, a Dim 6 Developer Persona when writing API integration code.
* *Example:* "Partner Integration Engineer" — builds card issuing integration for co-branded programs; needs sandbox environment, clear error codes, and versioning stability.

* **Programmatic User Persona:** The application or system consuming the API at runtime — a customer's ERP, partner's middleware, third-party app. Non-human consumer with throughput needs, SLA dependencies, and error-handling expectations.
* *Example:* "Customer Treasury Management System" — submits cross-border payment batches via SFTP, requires settlement confirmations within 30 minutes, processes 50K transactions/day.

**Module Types (all are Dim 8 modules carrying Dim 6 concerns):**

* **API Module:** A named, versioned, protocol-agnostic programmatic surface for external consumption. Encompasses REST, gRPC, batch/file (SFTP), event streams (Kafka), webhooks, GraphQL — all as delivery mechanisms within one module. Composes capabilities from one or more Dim 8 modules. Identity defined by use case and contract, not transport.
* *Structure/Relationship:* Composes capabilities from Dim 8 Module(s). Serves Developer Persona(s) and Programmatic User Persona(s). Governed by API Compatibility Contract. Contains API Operation(s).
* *Example:* "Cross-Border Payments API" — exposes Create Payment (REST + Kafka command), Get Rate Quote (REST query), payment.settled (webhook event), Daily Settlement Report (SFTP batch).

* **Integration Module:** A pre-built bridge between the product and a specific external system or system category. Includes data mappings, protocol translations, workflow adapters, and connectors — not just "our APIs" but the glue that translates between the product's model and the target system's model. If a product doesn't ship connectors to specific external systems, it has API Modules but no Integration Modules.
* *Structure/Relationship:* Bridges to specific external system(s). Relies on API Module(s) and other Dim 8 Module(s).
* *Example:* "SAP ERP Integration Module" — provides pre-built data mappings between product payment entities and SAP FI document types, BAPI adapters, and IDoc templates.

* **Extension Module:** A framework enabling third parties to extend product behavior — plugins, hooks, custom workflows. Provides governed extensibility points.
* *Structure/Relationship:* Exposes extensibility points from Dim 8 Module(s). Governed by Extension API contract.
* *Example:* "Compliance Workflow Extension" — enables customers to inject custom screening rules and approval chains into the payment processing pipeline.

* **SDK/Library Module:** A language-specific client providing idiomatic access to API Modules. Client-Distributed deployment topology (package registry → customer's codebase).
* *Structure/Relationship:* Wraps API Module(s). Published via package registry.
* *Example:* "Python Payments SDK" — wraps Cross-Border Payments API with typed models, automatic retry, and async/await support.

**Operations and Contracts:**

* **API Operation:** A named, versioned, contractual programmatic operation within an API Module. Classified by interaction pattern (Command, Query, Event, Callback, Batch), each with distinct SLO profiles. The atomic unit of programmatic capability that consumers depend on. Specific URL paths, HTTP methods, Kafka topic names, and payload schemas are PSD/Build territory — the Definition Model captures the operation's identity, pattern, and performance commitments.
* *Fields:* Name, Version, Pattern (Command / Query / Event / Callback / Batch), Description, SLOs (pattern-appropriate: latency/availability/throughput for Command/Query; delivery guarantee/latency/ordering for Event/Callback; processing window/throughput/completeness for Batch).
* *Structure/Relationship:* Belongs to API Module. May map to one or more Capabilities (Dim 8). SLOs feed Customer Promise SLAs (Dim 3). Monitored by Win Monitoring (Track 4) and System Monitoring (Track 3).
* *Example:* "Create Payment" (Command, p99 < 500ms, 99.95% availability, 10K calls/min) and "payment.settled" (Event, at-least-once delivery, < 30s delivery latency, ordered per payment).

* **API Compatibility Contract:** The module-level versioning and backward-compatibility commitment. Captures the product's promise to Developer and Programmatic Personas about stability — the Dim 6 analog of Customer Promise (Dim 3) for programmatic consumers.
* *Fields:* Versioning Strategy (semantic versioning, URL path, header), Deprecation Policy (sunset period, notification mechanism), Breaking Change Policy, Performance Stability Commitment (SLO degradation limits across versions).
* *Structure/Relationship:* Governs API Module. Referenced by Developer Persona(s). Assessed by Win Review (Track 4).
* *Example:* "v1 supported until 2027-12; breaking changes require major version bump with 6-month migration window; deprecated operations get 12-month sunset; SLOs guaranteed within 20% of published targets across minor versions."

**Deprecated from original Dim 6:**

* ~~**Interface Type**~~ — Subsumed by protocol-agnostic API Module. Becomes a field on the module ("Supported Protocols: REST, Kafka, SFTP"), not a standalone entity.
* ~~**Endpoint / Event Topic**~~ — Replaced by unified API Operation with pattern classification.
* ~~**Payload Schema**~~ — Demoted to PSD/Build artifact (too granular for Definition Model, same pattern as Touchpoint deprecation in Dim 4).



#### Dimension 7: The Operational Dimension (Runtime & DevOps)

This dimension captures the product's **operational reality** — how it is hosted, who operates it, what operational success looks like, what constraints limit operational choices, and whether each module is production-ready. Dim 7 answers: "How is the product operated and sustained in production?" It connects upward to Dim 3 (Service Commitment defines the customer-facing SLA; Dim 7 captures the infrastructure that delivers it) and Dim 6 (API Operation SLOs define programmatic commitments; Dim 7 Operational Targets back them). All Dim 7 entities are discovered and formalized through Discovery Track (Deliberations, PDRs, Modeling Tasks). See DR-023.

> **Operational Quality Taxonomy:** Dim 7 entities are classified by a quality taxonomy — **Reliability, Performance, Security, Compliance, Cost Efficiency, Observability, Scalability**. These are not standalone entities but a classification framework used as type/category axes on Dim 7 entities, parallel to how AAARRR stages classify Dim 2 entities.

> **Cost Coverage:** Infrastructure and operational cost is modeled through three complementary entities: Infrastructure Model carries a Cost Model field (overall cost strategy), Operational Target of type Cost sets specific targets ("infra cost per 1K transactions < $0.50"), and Operational Pain surfaces cost suffering. This connects to Business KPI (Dim 2) of type Cost ("Infrastructure Cost per Customer") — the commercial view of the same cost reality.

* **Infrastructure Model:** The fundamental hosting and operations strategy — how the vendor operates the product in production. Lightweight structural root — all other Dim 7 entities derive from or operate within the Infrastructure Model. Parallel to Business Model (Dim 2): "how we make money" vs. "how we run it." The Infrastructure Model also defines the product's **Tenancy Architecture** — the pattern for how customer tenants are organized within environments. Actual Tenants are Run Track (Track 3) operational artifacts; Dim 7 defines the architecture pattern.
* *Structure/Relationship:*  Infrastructure Model defines the frame for  Deployment Environment(s),  Operational Target(s) (product-level), and  Operational Constraint(s).
* *Fields:* Cloud Strategy (single-cloud / multi-cloud / hybrid / on-premise), Region Strategy (single-region / multi-region / global), Tenancy Architecture (shared / dedicated / hybrid), DR Strategy (active-active / active-passive / cold standby / none), Scale Model (horizontal auto-scale / vertical / manual / serverless), Cost Model (reserved / spot / committed / pay-as-you-go), Compliance Architecture (PCI scope, SOC 2 boundary, data sovereignty zones).
* *Example:* "Multi-region AWS SaaS — 3 production regions (US-East, EU-West, LATAM), shared tenancy for Mid-Market, dedicated tenancy for Enterprise, active-passive DR, horizontal auto-scale with reserved base capacity, PCI-DSS Level 1 scope across all payment-processing modules."

* **Operational Persona:** A functional archetype who operates the product — not an organizational role (those belong in the Operating Model) but a function the product's operational health depends on. Operational Personas are organized by the Operational Quality Taxonomy, not by job titles. Each persona has operational domains they own, tools/modules they use, and pains they endure. Distinct from User Persona (Dim 4) and Developer Persona (Dim 6) — different interaction paradigm, different quality criteria, different concerns.
* *Structure/Relationship:*  Operational Persona operates  Deployment Environment(s).  Operational Persona has  Operational Job(s) (Dim 7).  Operational Persona follows  Operational Journey(s) (Dim 7).  Operational Persona endures  Operational Pain(s) (Dim 7).  Operational Persona is responsible for  Operational Target(s) (Dim 7).  Operational Persona accesses product via  UX Channel(s) (Dim 4, cross-dimensional reference).
* *Quality-Taxonomy Archetypes:* **Reliability Operator** (availability, incident response, SLO compliance, error budgets), **Security Operator** (security posture, vulnerability management, access control, key management), **Platform Operator** (deployment infrastructure, CI/CD, environment provisioning, developer experience), **Data Operator** (data integrity, backup/restore, migration, schema management).
* *Example:* Reliability Operator — owns availability and incident response for production environments; uses Monitoring Dashboard (Web + Self-serve), Alert system (Email + Self-serve), Incident CLI (CLI + Self-serve); endures pain "Manual certificate rotation takes 8 hours/week across 12 environments."

* **Operational Job:** What the Operational Persona needs to accomplish through the product's operational tooling — the operational "job to be done." Operational Jobs bridge operational intent (Dim 7) to product structure (Dim 8) — they explain WHY operational modules exist and WHAT capabilities they must provide. The Run Track work entities (Deployment, Incident, etc.) are the instantiation of these jobs; the Definition Model captures the job definition and its structural enablers. Independent from Job (JTBD) in Dim 4 — same analytical pattern, different domain.
* *Structure/Relationship:*  Operational Job is pursued by  Operational Persona(s) (Dim 7).  Operational Job is accomplished through  Operational Journey(s) (Dim 7).  Operational Job is enabled by  Value Stream(s) / Capability(ies) (Dim 8).  Operational Job is measured against  Operational Target(s) (Dim 7).
* *Example:* "Deploy a release safely to production without service disruption" — pursued by Platform Operator; enabled by Value Stream "Release Management" and Capability "Canary Deployment"; measured against Operational Target "zero-downtime deployments, rollback within 5 minutes."

* **Operational Journey:** The end-to-end path an Operational Persona follows to accomplish an Operational Job, traversing operational modules and integration modules. Journeys trace through both native operational modules (admin consoles, deployment dashboards) and integration modules to third-party ops tooling (Datadog, PagerDuty, Terraform). Independent from User Journey (Dim 4) — same structural concept, different domain.
* *Structure/Relationship:*  Operational Journey accomplishes  Operational Job(s) (Dim 7).  Operational Journey is followed by  Operational Persona(s) (Dim 7).  Operational Journey traverses  Module(s) (Dim 8).  Operational Journey is experienced through  UX Channel(s) (Dim 4, cross-dimensional reference).  Operational Journey engages  Capability(ies) (Dim 8).
* *Example:* "Diagnose and resolve a SEV-1 incident" — Reliability Operator follows this Journey: Monitoring Dashboard (Web) → alert triggers PagerDuty (Integration Module, Email/Voice) → Log Aggregator (Web) → Deployment Console (Web) → rollback via CLI (CLI) → post-incident review tool (Web). Traverses modules: Monitoring Module, PagerDuty Integration Module, Log Module, Deployment Module.

* **Deployment Environment:** A named, typed, vendor-operated infrastructure target where modules are deployed and tenants are provisioned. Expanded from the original skeletal "Environment." The Deployment Environment carries the vendor's operational purpose — customer-facing purpose lives on the Tenant (Run Track entity). The Tenancy Architecture (inherited from Infrastructure Model or overridden) defines how customer isolation is organized within this environment.
* *Structure/Relationship:*  Deployment Environment is defined by  Infrastructure Model (Dim 7).  Deployment Environment hosts  Module(s) (Dim 8).  Deployment Environment is constrained by  Operational Constraint(s) (Dim 7).  Deployment Environment has  Operational Target(s) (Dim 7).  Deployment Environment is operated by  Operational Persona(s) (Dim 7).  Deployment Environment hosts  Tenant(s) (Run Track, Track 3).  Deployment Environment is targeted by  System Deployment Specification / Product Deployment Specification (Track 3) — environment-specific deployment configuration for sealed System Versions and Product Versions.  Deployment Environment is targeted by  Station(s) (Dim 7) within Deployment Trains.
* *Fields:* Name, Vendor Purpose (Production / Staging / Development / DR / CI/CD / Demo), Region, Tenancy Architecture (shared / dedicated / hybrid — inherited or overridden), Compliance Zone, Scale Policy, Change Windows, Freeze Periods, Cycle Cadence, Override Rules.
* *Status Lifecycle:* `Planned` → `Provisioning` → `Active` → `Maintenance` → `Decommissioning` → `Retired`.
* *Example:* "Production US-East" — Purpose: Production, Region: us-east-1, Tenancy: Shared, Compliance Zone: PCI-DSS Level 1, Scale: horizontal auto-scale with 3-node minimum. Hosts: payments-service, fx-engine, merchant-portal. Tenants: Customer A (prod), Customer A (UAT), Customer B (prod).

* **Operational Target (SLO):** An infrastructure-level objective that backs Service Commitments (Dim 3) and API Operation SLOs (Dim 6). The operational "how we deliver on promises." Each Operational Target carries **Achievement Levers** — categorized as Product (build self-healing, improve error handling) or Operational (improve procedures, add redundancy, scale infrastructure) — connecting Dim 7 into the Initiative/Lever framework. Definition Model captures targets; actual measured values are operational state tracked by System Monitoring (Track 3). SLIs (Service Level Indicators) — the specific metrics that feed into the SLO — are fields on the Operational Target.
* *Type (from quality taxonomy):* Availability, Latency, Throughput, Durability, Recovery (RTO/RPO), Cost, Security.
* *Structure/Relationship:*  Operational Target backs  Service Commitment (Dim 3).  Operational Target delivers  API Operation SLOs (Dim 6).  Operational Target is scoped to  Module (Dim 8) + Deployment Environment (Dim 7).  Operational Target is monitored by  System Monitoring (Track 3).  Operational Target is the responsibility of  Operational Persona(s).  Operational Target is undermined by  Operational Pain(s).  Operational Target declares  Achievement Lever(s).  Objective / Initiative (Dim 1) may reference  Operational Target(s).
* *Example:* "payments-service availability in Production US-East: 99.99% measured at load balancer (non-5xx responses). Achievement Levers: Product (primary — circuit breakers, graceful degradation), Operational (secondary — multi-AZ redundancy, automated failover)."

* **Operational Constraint:** A non-negotiable infrastructure requirement imposed by regulation, compliance, customer contract, or architectural decision. Parallel to Win Barrier (Dim 2) — structural impediment, but for operational choices rather than commercial outcomes. When unmet, an Operational Constraint may surface as an Adoption Barrier (Dim 3) or Win Barrier (Dim 2).
* *Type:* Data Residency, Compliance Boundary (PCI scope), Network Segmentation, Security Standard, Change Window, Audit Requirement, Regulatory.
* *Structure/Relationship:*  Operational Constraint is imposed by  Compliance Posture (Dim 3) or regulation.  Operational Constraint constrains  Deployment Environment(s) (Dim 7).  Operational Constraint may surface as  Adoption Barrier (Dim 3) /  Win Barrier (Dim 2) when unmet.  Operational Constraint may have a structural root in  Module / Capability (Dim 8).
* *Example:* "LATAM data residency: all payment transaction data for LATAM customers must be stored and processed within Brazil (LGPD compliance). Constrains: Production LATAM environment must exist with in-country data storage. Source: LGPD regulation + LATAM Enterprise contract requirements."

* **Operational Pain:** A specific, concrete suffering experienced by an Operational Persona in operating the product. Operational Pains are discoverable — they surface through Run Track experience and must be investigated, not assumed. Parallel to Delivery Friction (Dim 2) and Pain (Dim 3): same analytical structure, different beneficiary. May surface as a Signal (Dim 1) to drive Initiatives.
* *Structure/Relationship:*  Operational Pain is endured by  Operational Persona(s) (Dim 7).  Operational Pain undermines  Operational Target(s) (Dim 7).  Operational Pain may be rooted in  Module / Capability (Dim 8).  Operational Pain may surface as  Problem / Need / Opportunity Signal (Dim 1).  Operational Pain is scoped to  Deployment Environment(s) (Dim 7).
* *Fields:* Title, Quality Domain (from taxonomy), Endured by, Impact (quantified), Frequency, Undermines Operational Target, Rooted in (Dim 8).
* *Example:* "Manual certificate rotation across 12 environments takes 8 hours/week" — Quality Domain: Security, Endured by: Security Operator, Impact: 8 engineer-hours/week + risk of expired certificates, Undermines: "zero security incidents from operational lapses," Rooted in: Key Management (Capability, missing automation).

* **Operational Readiness:** A per-System assessment of whether a specific System (Dim 5) meets the operational acceptance criteria for a specific Deployment Environment. The criteria span the Operational Quality Taxonomy: observability (logs, metrics, traces, SLIs), security (encryption, access control, vulnerability scanning), performance (benchmarks, load testing), operability (alerts, runbooks, admin controls), DR (backup, restore, failover). Distinct from Evolve Track (Track 5) which assesses process effectiveness — Operational Readiness assesses System readiness. Module-level readiness is a derived view that aggregates across constituent Systems. The criteria definition is a Definition Model concern; the assessment work is Run Track activity.
* *Structure/Relationship:*  Operational Readiness is scoped to  System (Dim 5) ×  Deployment Environment (Dim 7).  Operational Readiness aggregates to  Module (Dim 8) for capability-level view.  Operational Readiness is assessed by  Run Track activities (Track 3).  Operational Readiness criteria reference  Operational Target(s) (Dim 7).  Operational Readiness informs  System Deployment Specification (Track 3) — readiness status informs whether deployment specs should be created for a given environment.  Operational Readiness informs  Deployment Plan (Track 3).
* *Status:* `Not Assessed` → `Gaps Identified` → `Conditionally Ready` → `Fully Ready`.
* *Example:* "payments-service in Production US-East: Observability — Fully Ready (structured logs, Prometheus metrics, distributed traces, SLIs defined). Security — Conditionally Ready (encryption at rest, mTLS in transit, pending: automated key rotation). Performance — Fully Ready (load tested to 3x peak). Operability — Gaps Identified (runbooks incomplete for failover scenario). DR — Fully Ready (automated backup, tested restore, failover tested quarterly)."

* **Operations Decision Record (ODR):** A formal record of a significant operational or infrastructure decision — the Dim 7 counterpart of PDR (Dim 1) and ADR (Dim 5). Completes the decision record triad: PDR captures what the product should *do* (strategy), ADR captures how it should be *built* (architecture), ODR captures how it should be *run* (operations). ODR scope includes cloud provider and service selection, deployment strategy, tenancy and isolation decisions, DR/BCP strategy, data governance and archival policies, observability tooling, compliance zone configuration, capacity and scaling strategy, and cost optimization decisions. Like ADR, ODR has dual provenance: Discovery Track (strategic infrastructure planning) and Run Track (decisions from operational experience). See DR-025.
* *Relationship patterns:* PDR triggers ODR(s) ("Go on LATAM" → "LGPD compliance in sa-east-1"); ADR triggers ODR(s) ("Adopt event-driven" → "Provision MSK 3-AZ"); ODR exists independently ("Archive transaction data after 24 months"); ODR constrains ADR/PDR ("4-hour RTO means active-active isn't justified").
* *Structure/Relationship:*  ODR may be triggered by  PDR (Dim 1) or  ADR (Dim 5).  ODR affects  Deployment Environment(s) (Dim 7),  Operational Target(s) (Dim 7),  Operational Constraint(s) (Dim 7).  ODR justifies  Infrastructure Model (Dim 7).  ODR affects  System(s) (Dim 5),  Dependency(ies) (Dim 5).  ODR may constrain  ADR(s) (Dim 5) or  PDR(s) (Dim 1).  ODR may supersede  ODR(s) (Dim 7).
* *Fields:* ID, Title, Status (Proposed / Accepted / Deprecated / Superseded), Category (Cloud Provider & Services / Deployment Strategy / Tenancy & Isolation / DR & BCP / Data Governance / Data Archival / Observability & Tooling / Compliance Zone / Capacity & Scaling / Cost Optimization), Context, Decision, Consequences (+/−), Quality Attributes Addressed, Triggered by (PDR/ADR references), Supersedes/Superseded-by, Affected Environments, Affected Systems, Affected Dependencies.
* *Example:* "ODR-011: Archive transaction data to S3 Glacier after 24 months. Context: PostgreSQL grows ~50GB/month; data >24 months old is accessed <0.1% of queries; 7-year regulatory retention required. Decision: Archive to S3 Glacier Deep Archive, maintain index metadata in PostgreSQL, 12-hour retrieval SLA. Consequences: (+) 60% storage reduction, faster backups, improved query performance; (−) 12-hour retrieval latency for archived records, archival pipeline maintenance."


* **Deployment Train:** A reusable promotion path defining the ordered sequence of environments through which deployments progress, carrying contractual and governance significance. Deployment Trains represent both a technical promotion workflow and a contractual commitment — tenants and commercial partners can rely on the promotion path for planning. Trains enable certain operating models while rejecting non-compliant ones. See DR-029.
* *Structure/Relationship:*  Deployment Train contains  Station(s) (Dim 7).  Deployment Train is scoped by  Change Request(s) (Track 3).  Deployment Train is referenced by  Customer Release (Dim 1).  Deployment Train provides derived visibility for  Tenant(s) (Track 3) via Deployment Environment.
* *Fields:* Name, Stations (ordered), Governance Level (Standard / Regulated / Critical), Contractual Commitments, Allowed Change Types.
* *Status:* `Draft` → `Active` → `Suspended` → `Retired`.
* *Example:* "PCI Regulated Train — Development → Staging (72h soak) → Production US-East (CAB approval, canary) → Production LATAM (CAB + LATAM compliance). Governance: Regulated. Allowed: Standard, Emergency-Technical."


* **Station:** A checkpoint within a Deployment Train (Dim 7), targeting a specific Deployment Environment with defined entry criteria, exit/promotion criteria, and approval requirements. Stations make the promotion path auditable and contractually enforceable. The same Deployment Environment may be a Station in multiple Deployment Trains with different governance requirements per train. See DR-029.
* *Structure/Relationship:*  Station belongs to  Deployment Train (Dim 7).  Station targets  Deployment Environment (Dim 7).  Station is scoped by  Change Request(s) (Track 3).  Station is verified by  Verification Task(s) (Track 3).
* *Fields:* Name, Deployment Environment (Dim 7 ref), Sequence Position, Entry Criteria, Exit/Promotion Criteria, Approval Requirements, Soak Time, Verification Requirements.
* *Status:* `Active` / `Bypassed` / `Retired`.
* *Example:* "Production LATAM Gate (PCI Regulated Train, position 4) — Entry: Prod-US soak 1 week + LATAM regulatory window + compliance officer sign-off. Exit: canary metrics within SLO at 5%→25%→100%. Soak: 1 week."


**Deprecated and deleted from Dim 7 (DR-036):**

* ~~**Module Package (Specification)**~~ — Removed. Operator-facing Systems are equal members of Product Specification (Dim 5), versioned through the same Build Track pipeline as product-facing Systems. See DR-036 D7, D9.
* ~~**Product Package (Specification)**~~ — Removed. Replaced by Product Specification (Dim 5) as the technical twin of Product. See DR-036 D4, D7.

**Deprecated from original Dim 7:**

* ~~**Environment**~~ — Superseded by the expanded Deployment Environment entity, which adds vendor purpose, tenancy architecture, compliance zone, scale policy, and full relationship set.
* ~~**Cluster / Host**~~ — Below the Definition Model waterline. Specific compute infrastructure (Kubernetes clusters, VM hosts) belongs in PSD/Run Track artifacts. Same deprecation pattern as Touchpoint (Dim 4) and Payload Schema (Dim 6).
* ~~**Container / Process**~~ — Below the Definition Model waterline. Runtime instances are PSD/Run Track artifacts, not Definition Model entities.

> **Dim 7 scope after DR-036:** Dim 7 retains operational runtime concerns only — Infrastructure Model, Deployment Environment, Deployment Train, Station, Operational Persona/Job/Journey, Operational Target/Constraint/Pain, Operational Readiness, ODR. Specification and Package entities are removed from Dim 7.


### TIER 4: THE BRIDGE (TAXONOMY & ONTOLOGY)

*Owned by Enterprise Architects and Business Analysts. This tier bridges Strategy, Business, and Technical entities—providing the taxonomy and ontology that connects high-level intent to technical execution.*

#### Dimension 8: The Structural Dimension (Topology)

This dimension provides the functional "table of contents" for the entire system, establishing logical boundaries. It has two complementary views: a **vertical decomposition** (Product → Module → Capability → Feature) and a **horizontal composition** (Value Streams that flow across Modules).

* **Product:** A marketable software offering.
* *Structure/Relationship:*  Product contains  Modules.  Product has  Value Stream(s).
* *Example:* Core Payment Gateway.


* **Value Stream:** An end-to-end sequence of activities — crossing multiple modules and capabilities — that delivers a complete unit of value to the customer. Value Streams represent *how value flows horizontally* across the product's vertical module structure. They are the natural mapping target for outcome-based Value Propositions (Dim 3), since outcomes require end-to-end flows, not single capabilities.
* *Structure/Relationship:*  Value Stream traverses  Module(s) / Capability(ies).  Value Stream is mapped by  Value Proposition (Dim 3).  Value Stream is experienced through  User Journey(s) (Dim 4).
* *Example:* "Cross-Border Payout Processing" — traverses Invoice Module (invoice creation) → FX Module (rate locking) → Compliance Module (OFAC screening) → Payment Module (execution) → Settlement Module (reconciliation).


* **Module / Domain:** A major bounded context within the product — the customer-facing unit of functional value. Each Module has a **Functional Classification** drawn from the Twelve System Types framework (Record, Enforcement, Data, Engagement, Action, Intelligence, Identity, Influence, Memory, Product, Innovation, Integration), which describes what the Module does for the customer rather than how it is implemented. The Functional Classification replaces the earlier Module Archetype (HI/Programmatic/Reactive), which conflated customer-value vocabulary with technical implementation vocabulary. Module structure is **flat** (no sub-modules). Entitlement (Pricing Tier link from Dim 2) is at the Module level — a customer buys access to a Module, not individual Features within it. *(See DR-035.)*
* *Structure/Relationship:*  Module contains  Capabilities.  Module is traversed by  Value Stream(s).  Module is implemented by  System(s) (Dim 5, many-to-many).  Module is linked to  Pricing Tier(s) (Dim 2) for entitlement.
* *Example:* Payments Module [Record] — authoritative state of payment transactions; included in Enterprise Volume Plan pricing tier.


* **Capability:** A high-level ability provided to the user/system. Capabilities are the promise-level unit — what you commit to customers. They are the natural mapping target for ability-based Value Propositions (Dim 3).
* *Structure/Relationship:*  Capability contains  Features.  Capability is engaged by  Value Stream(s).  Capability is mapped by  Value Proposition (Dim 3).
* *Example:* Cross-Border B2B Payments.


* **Feature:** A granular, distinct tool or behavior. Features are the delivery-level unit — how capabilities are implemented internally. Features are NOT directly referenced in Value Propositions.
* *Example:* Real-time FX auto-conversion lock.



#### Dimension 9: The Data & Information Dimension (State & Flow)

This dimension defines what information the system persists and how it is structured.

* **Data Domain:** A high-level category of business information.
* *Structure/Relationship:*  Domain manages  Data Entities.
* *Example:* Financial Transactions.


* **Data Entity:** A persistent object stored by a specific Module.
* *Structure/Relationship:* Strictly related via defined cardinality (e.g., ).
* *Example:* `Payment_Record`.


* **Attribute / Field:** A specific data point within an entity.
* *Example:* `settlement_amount`, `target_currency`, `fx_rate_applied`.


* **State:** The allowed lifecycle statuses of an entity.
* *Example:* `Initiated`  `Processing`  `Cleared`  `Settled`.

