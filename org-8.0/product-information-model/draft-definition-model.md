Here is the comprehensive, clean-slate reference document. I have re-architected the numbering so it flows logically from strategy down to code, eliminating the disjointed numbering from our earlier iterations.

This document defines the **Unified Product Information Model (UPIM)** — a three-model architecture:

1. **Definition Model** — What the product *is* (9 Dimensions)
2. **Work Model** — What work *exists* to move the product (4 Tracks)
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
* *Structure/Relationship:*  Objective may advance  Strategic Theme (optional).  Objective is pursued through  Initiative(s).
* *Status Lifecycle:* `Draft` → `Active` → `Achieved` / `Deferred`.
* *Example:* "Expand cross-border payment coverage to LATAM markets by end of H2 2026." (Theme: "LATAM Market Leadership")


* **Initiative:** A strategic program to advance one or more Objectives. An Initiative is the prioritization vehicle that associates Signals (Problems, Needs, Opportunities) for discovery. Signals may exist independently before being associated with an Initiative during a planning cycle.
* *Structure/Relationship:*  Initiative advances  Objective(s).  Initiative ← associated →  {Problem, Need, Opportunity} (many-to-many).  Initiative → Customer Release(s).
* *Status Lifecycle:* `Proposed` → `Approved` → `In Progress` → `Completed` / `Cancelled`.
* *Example:* "LATAM Currency Expansion — enable FX payouts in BRL, MXN, COP, and CLP."


* **Customer Release:** A named, business-scoped delivery of capabilities made available to customers based on business and customer needs. A Customer Release bundles the outcomes of one or more Initiatives into a coherent customer-facing delivery. Customer Releases use **names** (not version numbers) to emphasize their business identity and decouple from technical versioning. The term "Customer Release" follows the SAFe / Continuous Delivery convention: the business act of making functionality available to users, decoupled from deployment.
* *Structure/Relationship:*  Customer Release advances  Initiative(s) (many-to-many).  Customer Release references  Product Version(s) (Work Model).  Customer Release is activated by Win Track (GTM execution).
* *Status Lifecycle:* `Planning` → `In Progress` → `Ready` → `Launched` / `Cancelled`.
* *Example:* "LATAM Expansion" (bundles LATAM currency support, LATAM compliance, LATAM onboarding).

> **Terminology Note:** "Customer Release" refers to the business act of making functionality available to customers. It is distinct from an artifact "release," which follows DevOps convention — a versioned build that has passed quality gates. DevOps tooling (GitHub Releases, Helm releases, etc.) uses "release" to mean a versioned artifact — in our model, this is captured by the Module Version reaching `Released` status in the Build Track.

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

*Owned by Product Marketing and Executives. This tier models the product strictly as a financial vehicle.*

#### Dimension 2: Business Value Dimension (Vendor Economics)

This dimension models how the organization building the software generates revenue.

* **Business Model:** The fundamental revenue engine.
* *Example:* Transaction-based B2B SaaS.


* **Pricing Tier / Package:** A bundled offering sold to a specific market segment.
* *Structure/Relationship:*  Package contains  Features.
* *Example:* The "Enterprise Volume Plan."


* **Value Metric (Pricing Axis):** The strict unit of measurement that dictates cost.
* *Example:* 0.5% flat fee per successful transaction + 1% markup on the baseline FX rate.


* **Business KPI:** The internal health metric for the vendor.
* *Example:* Total Payment Volume (TPV) and Gross FX Margin.



#### Dimension 3: The Customer Value Dimension (Why Buy)

This dimension models the complete "Why Buy" logic for the purchasing organization — who buys, what they achieve, what they suffer, what the product promises, how those promises are measured, and what barriers impede adoption. It answers the customer's question: "Why should I buy this product, and what will I get?"

> **TCO Note (parked for later):** Total Cost of Ownership — what it costs the customer to adopt and operate the product (integration, training, migration, ongoing operational overhead) — is a recognized gap. TCO is distinct from vendor pricing (Dim 2) and directly inputs the ROI calculation. The right anchoring point (Customer Promise? Customer Segment?) and qualification approach need further discussion. Parked for a future refinement cycle.

* **Customer Segment:** A defined group of potential buyers sharing common characteristics — industry vertical, company size, geography, maturity stage. Segments have distinct buying personas, outcomes, pains, promise expectations, and adoption patterns. All other Dim 3 entities are anchored to one or more Customer Segments.
* *Structure/Relationship:*  Segment has  Buying Persona(s).  Segment has  Pain(s).  Segment is promised  Customer Promise(s).  Segment is blocked by  Adoption Barrier(s).
* *Example:* "LATAM Enterprise (500+ employees, cross-border payables)" vs. "US Mid-Market (100–499 employees, domestic payables)."


* **Buying Persona:** A role within the purchasing organization's buying committee that influences or decides the purchase. Each Buying Persona represents a distinct evaluation lens. Role types: **Economic Buyer** (budget holder — evaluates ROI), **Technical Buyer** (IT/Eng — evaluates integration, security, architecture), **User Buyer** (department head — evaluates usability, team adoption), **Coach/Champion** (internal advocate — navigates buying process). Buying Personas *care about* Pains even if they don't personally endure them.
* *Structure/Relationship:*  Buying Persona belongs to  Customer Segment.  Economic Buyer pursues  Business Outcome(s).  Buying Persona cares about  Pain(s).
* *Example:* CFO (Economic), CTO (Technical), AP Ops Manager (User), Treasury Director (Coach) at LATAM Enterprise.


* **Business Outcome:** The macro-level benefit the buyer needs to achieve — the buyer's "job to be done" at a strategic level. Business Outcomes are what the Buying Persona (typically Economic Buyer) uses to justify the purchase internally.
* *Structure/Relationship:*  Business Outcome is pursued by  Buying Persona (Economic Buyer).  Business Outcome is addressed by  Value Proposition (Customer Promise subtype).
* *Example:* "Eliminate manual FX hedging and reduce cross-border wire fees."


* **Pain:** A specific, concrete suffering or frustration experienced by a User Persona (Dim 4) in their current workflow. Pains are *endured* by users but *cared about* by Buying Personas, who are motivated to purchase a solution that relieves them. Together with Business Outcome, Pain forms the complete "Why Buy" motivation — the buyer wants the outcome (strategic), but the pain makes it feel *urgent* (visceral).
* *Structure/Relationship:*  Pain is endured by  User Persona (Dim 4).  Pain is cared about by  Buying Persona(s) (Dim 3).  Pain is relieved by  Value Proposition (Customer Promise subtype).
* *Example:* "AP Clerk spends 4 hours/day manually reconciling FX transactions across 3 systems" — endured by AP Clerk (Dim 4), cared about by CFO (cost) and AP Ops Manager (productivity).


* **Customer Promise:** The product's formal commitment to a Customer Segment. Customer Promise has three subtypes, each representing a distinct category of commitment:

  * **Value Proposition** (subtype): Articulates how the product's capabilities deliver the buyer's outcomes and relieve user pains. Maps Business Outcomes and Pains to Value Streams (for outcome-based promises) or Capabilities (for ability-based promises) in Dim 8. Includes competitive positioning — why this product over the alternative.
    * *Outcome-mapped example:* "Reduce cross-border payment cost by 60%" → addresses Outcome "Eliminate manual FX hedging" + relieves Pain "4 hours/day manual reconciliation" → maps to Value Stream "Cross-Border Payout Processing."
    * *Ability-mapped example:* "Real-time FX rate locking for 24 hours" → relieves Pain "15% rate expiry on transactions" → maps to Capability "Automated Rate Locking."

  * **Service Commitment** (subtype): Guarantees reliability, performance, and support levels. Includes availability SLA, performance SLA, support SLA, data SLA, and breach remedies. Overlaps with Dim 7 (Operational) — Dim 3 captures the customer-facing commitment; Dim 7 captures the infrastructure that delivers it.
    * *Example:* "99.9% API uptime, sub-200ms P95 latency, P1 incidents: 15-minute response."

  * **Compliance Posture** (subtype): Certifies that the product meets regulatory, security, or industry standards. Compliance goes beyond operations — it is a core aspect of the product that influences many capabilities (Dim 8). It is an essential customer trust element in the buying decision.
    * *Example:* "PCI-DSS Level 1 certified, SOC 2 Type II audited, GDPR compliant."

* *Structure/Relationship:*  Customer Promise is made to  Customer Segment.  Customer Promise is evidenced by  Customer Value Metric(s).  Adoption Barrier may challenge  Customer Promise.


* **Customer Value Metric:** A measurable indicator that defines whether a Customer Promise is being kept. Unified metric entity with subtypes corresponding to promise types. All subtypes share a common structure (target, SLA threshold, measurement method, frequency) but measure different things. The Definition Model captures metric *definitions and targets* only — actual measured values are operational state tracked at runtime.

  * **ROI Metric** (subtype): Measures Value Proposition claims. Different for Value Stream-mapped and Capability-mapped promises.
    * *Value Stream-mapped examples:* End-to-end cycle time ("target <4 hours, SLA threshold <8 hours"), throughput ("500+ payouts per batch"), cost reduction ("60% lower per-transaction cost").
    * *Capability-mapped examples:* Feature performance ("FX rate locked within 200ms"), coverage ("35+ supported currencies").

  * **Service Level Metric** (subtype): Measures Service Commitment guarantees.
    * *Examples:* Uptime (target 99.9%, SLA threshold 99.5%), P95 latency, mean time to resolve P1 incidents.

  * **Compliance Metric** (subtype): Measures Compliance Posture adherence.
    * *Examples:* Audit pass/fail, certification validity period, vulnerability remediation time.

* *Structure/Relationship:*  Customer Value Metric evidences  Customer Promise.


* **Adoption Barrier:** A known impediment to purchase or adoption within a segment. Types: Regulatory, Technical, Organizational, Competitive, Financial, Contractual, Data, Cultural. Barriers may directly challenge or undermine a Customer Promise — exposing gaps between what the product promises and what prevents the customer from realizing that promise. Understanding barriers informs discovery prioritization — a barrier may surface as a Signal (Problem or Need) in Dim 1.
* *Structure/Relationship:*  Adoption Barrier blocks  Customer Segment.  Adoption Barrier may challenge  Customer Promise.
* *Example:* "LATAM enterprises require local data residency" (Regulatory, Blocker — challenges Compliance Posture "GDPR compliant").



### TIER 3: TECHNICAL EXECUTION (THE MODULES)

*Owned by Tech Leads, Developers, DevOps, and UX Designers. These dimensions describe the physical reality of specific modules.*

#### Dimension 4: The User-Centric Dimension (Experience)

This dimension maps human interactions for UI-driven modules.

* **User Persona:** The human interacting with the system.
* *Example:* Accounts Payable (AP) Clerk.


* **User Journey:** The end-to-end path to achieve a goal.
* *Structure/Relationship:*  Journey contains  Touchpoints.
* *Example:* Initiating and approving a cross-border invoice payment.


* **Touchpoint / UI Element:** The specific interface interaction.
* *Example:* The "Target Currency" dropdown and the "Lock Rate" confirmation button.



#### Dimension 5: The Technical & Architectural Dimension (Engineering)

This dimension maps the codebase structure and processing logic (aligned with C4 architecture).

* **Subsystem / Service:** A standalone, deployable unit of backend logic.
* *Structure/Relationship:*  Subsystem contains  Classes/Components.
* *Example:* The FX (Foreign Exchange) Microservice.


* **Class / Component:** The structural code definition.
* *Structure/Relationship:*  Class contains  Functions.
* *Example:* `ExchangeRateCalculator`.


* **Function / Method:** The executable block of code.
* *Example:* `calculateConversion(baseCurrency, targetCurrency, amount)`.



#### Dimension 6: The Ecosystem & Extensibility Dimension (Platform)

This dimension maps the programmatic boundaries for API-driven modules.

* **Interface Type:** The technological method of communication.
* *Example:* RESTful API and Asynchronous Webhooks.


* **Endpoint / Event Topic:** The programmatic address or trigger.
* *Structure/Relationship:*  Endpoint triggers  Functions (Dimension 5).
* *Example:* `POST /v1/payments/cross-border` and `payment.cleared` webhook.


* **Payload Schema:** The strict data contract sent or received.
* *Example:* JSON payload requiring `amount`, `source_currency`, and `target_currency`.



#### Dimension 7: The Operational Dimension (Runtime & DevOps)

This dimension maps where the code lives, how it scales, and how it is secured.

* **Environment:** An isolated deployment ecosystem.
* *Example:* Production (PCI-DSS Compliant Zone).


* **Cluster / Host:** The orchestration group running the software.
* *Structure/Relationship:*  Cluster runs  Containers.
* *Example:* Dedicated Kubernetes Cluster (EKS).


* **Container / Process:** The isolated runtime instance executing the Subsystem (Dimension 5).
* *Example:* FX Microservice Docker Container.



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


* **Module / Domain:** A major bounded context within the product.
* *Structure/Relationship:*  Module contains  Capabilities.  Module is traversed by  Value Stream(s).
* *Example:* Invoice & Payout Processing.


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

