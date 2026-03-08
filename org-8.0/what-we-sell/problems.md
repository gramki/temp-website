# The Problem: Work in Banking Domains Has No Model

## The Core Problem

Every banking domain — payments, credit, servicing, compliance — has work that needs to get done. Commitments to customers, partners, and regulators that must be fulfilled. Internal disciplines — reconciliation, fraud monitoring, compliance verification — that must be maintained. People and systems that must collaborate to make it all happen.

But banks have no coherent model for this work.

It is scattered across systems — core banking, workflow engines, case management tools, batch schedulers, monitoring dashboards. It is buried in process maps that no one reads and BPM diagrams that describe what should happen, not what does happen. It is fragmented across teams that each see their slice but never the whole. There is no shared model, no common vocabulary, no coherent picture.

## What Banks Cannot Answer Today

In any given domain, a bank struggles to answer:

- **What do we owe the outside world?** Which commitments are active? What does "fulfilled" look like for each? Where are we falling behind?
- **What do we do for ourselves?** Which internal disciplines are running? Are they producing useful output? Are they actually keeping us healthy?
- **Who is doing the work?** Which agents — human and AI — are resolving which goals? Where is the capacity? Where is the bottleneck?
- **What tools are they using?** Which systems provide which capabilities? Are they registered, governed, auditable?
- **Where is the dial?** For each piece of work, how much is human, how much is AI, how much is automated? And where *could* it be?

These are not exotic questions. They are the most basic operational questions a domain leader should be able to answer. But the way banking work is currently modeled — or rather, not modeled — makes them unanswerable at scale.

## Why This Matters Now

Banks have always had fragmented work. What has changed is the cost of that fragmentation:

**AI cannot be introduced without visibility.** When work is invisible, you cannot decide where AI fits. You cannot identify which goals could be resolved by an AI agent, which need human-AI collaboration, and which should remain human. You end up with isolated AI experiments that don't connect to the operational fabric — or worse, big-bang transformations that rebuild everything at once.

**Gradual transformation requires a stable model.** Banks want to move from human-operated to AI-augmented gradually — one piece of work at a time, at their own pace. But gradual transformation requires a model that stays stable as the "who" changes. If the model is the process map, changing who does the work means redesigning the process. If the model is the work itself — goals, commitments, disciplines — then changing who resolves it is just moving a dial.

**Governance demands it.** Regulators increasingly ask: who made this decision? What information was used? Was an AI involved? These questions are unanswerable when work is scattered across systems without a coherent model connecting commitments to resolution to audit trails.

> **Hub Way response:** The Hub Way models work — not systems, not processes — as the primary abstraction. Streams capture external commitments. Loops capture internal disciplines. Scenarios define goal-oriented units of resolution. The model stays stable as the "who" changes: moving from human to AI to hybrid resolution is a dial on the Scenario, not a redesign of the model. Every Scenario produces a governed trace connecting commitment to resolution to audit trail.

## The Organizational Reality

### Banks are organized by domains, not by customers

Banks operate as federations of semi-autonomous business lines and domains — payments, credit cards, lending, wealth management, corporate banking, compliance. Each has its own P&L, leadership, technology stack, vendor relationships, and operational culture. This is the structural reality underneath all other problems.

It means every problem described in this document is **multiplied by the number of domains**. The bank does not have *a* technology estate — it has a portfolio of domain-specific technology estates, each evolved independently, each with its own history of vendor choices, integration patterns, and accumulated workarounds.

### Each domain has a different gap profile

The systems gap is not uniform across the bank. Each domain has its own unique mix of system maturity, integration depth, and technical debt. The payments domain might be sophisticated in real-time processing but have no intelligence layer. The credit card domain might have advanced fraud detection but primitive engagement. The mortgage domain might rely entirely on manual processes with spreadsheets compensating for missing systems of action.

No enterprise-wide assessment captures this accurately, because the reality is a matrix: *D* domains × *S* system types, with each cell at a different maturity level. This is why enterprise-wide modernization programs so often fail — they assume a uniform starting point that does not exist.

### The customer falls through the seams

A single customer has a savings account, a credit card, a mortgage, uses payments, and maybe holds an investment account. That customer interacts with five or more domains. But no domain owns the holistic customer relationship. Each domain sees its slice of the customer — the card holder, the borrower, the depositor — not the person.

The customer's experience is the *seam* between domains, and seams are exactly where coherence breaks down. The customer sees one bank. The bank sees five unrelated product holders.

### Channels fragment the view further

Banks think in **channels** — mobile, web, branch, contact center, ATM, partner portals. Each channel has its own team, budget, technology stack, and roadmap. Channels should be windows into the domain — surfaces through which the customer sees and interacts with their relationship. Instead, they become their own silos.

Even within a single domain, the customer sees a different version of their relationship depending on which channel they use. The mobile app shows the balance and recent transactions but cannot handle a dispute. The website shows statements and rewards but reads from a different cache. The contact center agent sees cases and alerts but not the journey the customer just attempted on mobile. The branch sees an even more limited view because it connects through older integration paths.

These are not different UIs over the same data. They often connect to different backend systems, have different feature sets, and present inconsistent information. The channel team built what it could access through whatever plumbing existed at the time. No single channel presents a coherent view of the customer's relationship with even *one* domain — let alone across domains.

Each channel is also an **identity-bearing system** — with its own authentication model, session management, and access control. The mobile app authenticates differently from the website, which authenticates differently from the branch system. Crossing channels means crossing trust boundaries. A customer who starts a mortgage application on the web and walks into a branch to continue it often has to start over, because the branch channel has no access to the web channel's session, context, or progress.

Channel teams are incentivized to deliver features *in their channel*. The mobile team ships mobile features. The web team ships web features. Nobody owns "the customer's coherent view of their credit card relationship across all channels." The cross-channel experience is an orphan — no team owns it, no budget funds it, no roadmap tracks it.

### Every bank's mix is unique

No two banks have the same combination of domain structure, system maturity per domain, vendor mix, plumbing topology, channel architecture, customer segment priorities, and accumulated technical debt. Bank A might be strong in payments but weak in credit. Bank B might have excellent consumer engagement but terrible corporate banking technology. Bank C might have a unified mobile app but completely siloed backend domains.

This means any approach that prescribes a fixed architecture or a standard migration path will fail. The solution must be adaptable to each bank's starting point — which is unique — and allow domain-by-domain, piece-by-piece evolution rather than enterprise-wide transformation.

> **Hub Way response:** The Hub is scoped to a single business domain — one Hub per domain, each modeled independently, each at its own pace. This matches how banks actually operate. Channels are modeled as domain-scoped interaction surfaces within a Hub, giving each domain a coherent view of its collaboration surfaces. Channel Products compose Channels from multiple Hubs into a coherent, cross-domain experience for a customer segment or persona — addressing the cross-domain seam at the organization level without requiring domains to merge. Teams are modeled as Hub constituents, making visible who resolves what within each domain. Because each Hub is independent, every bank can start with the domain that matters most and expand at its own pace, respecting its unique mix of gaps and starting points.

## The Systems Gap

Banking architecture was built around two things: **recording transactions** and **enforcing rules**. Core banking systems, card processors, payment switches, ledgers, fraud engines, compliance rule engines — these are mature, mission-critical, and well-invested. They are the systems banks trust.

But a modern enterprise needs far more than record and enforce. It needs systems that engage customers across channels, generate intelligence from data, influence behavior through personalization, manage identity and relationships, preserve institutional memory, define and compose products, enable experimentation, and orchestrate operational work. These are not luxuries — they are the systems required to leverage the full potential of data, mobile, internet, AI, wearables, and the evolving landscape of digital interaction.

Most banks do not have many of these systems. And the ones they do have are treated as **surrounds** — adjunct systems orbiting the gravitational center of the core. The core is "the system." Everything else is secondary, optional, or bolted on. This "core-systems thinking" limits the bank's possibilities to what the core can express. Products are defined inside the core banking system. Customer journeys are constrained by what the core's APIs expose. Innovation is bounded by what the core's change cycle permits.

The result is a lopsided architecture:

| What banks are strong at | What banks are weak or fragmented at |
|---|---|
| System of Record (ledgers, transactions) | System of Engagement (consistent cross-channel interactions) |
| System of Enforcement (fraud, AML, compliance) | System of Intelligence (real-time, operationalized insights) |
| | System of Influence (personalization, behavioral shaping) |
| | System of Identity (unified enterprise identity and relationships) |
| | System of Memory (structured institutional knowledge) |
| | System of Product (composable product definitions) |
| | System of Innovation (systematic experimentation) |
| | System of Action (end-to-end operational orchestration) |

Even where banks have invested in systems beyond core — a CRM here, an analytics platform there, a case management tool somewhere — the adoption is **uneven across business domains**. The credit card division may have a sophisticated engagement platform while the payments team relies on spreadsheets. The retail bank may have real-time fraud intelligence while corporate banking runs overnight batch analytics. Each domain makes its own choices about which modern systems to adopt, at what maturity, with what level of integration. There is no enterprise-wide coherence.

This unevenness compounds every other problem. It means the plumbing between domains is not just brittle — it connects systems at different maturity levels, with different data models, different interaction patterns, and different assumptions about what is even possible.

> **Hub Way response:** The Hub models every system — whether mature or nascent, vendor or bespoke — as a Machine that provides Tools. A core banking system and an AI prediction service are both Machines; they differ in what Tools they provide, not in how the Hub relates to them. This flattens the "core vs. surround" hierarchy. The Hub doesn't privilege the system of record over the system of intelligence — both are Machines offering Tools that Scenarios consume. New systems are introduced by registering new Machines, not by rewiring the architecture. The systems gap becomes a gap in available Tools, addressable incrementally.

## The Plumbing Problem

Banks buy systems from many vendors — fraud engines, card processors, CRM platforms, decisioning engines, document management, analytics tools. Each is competent at what it does. None speaks the bank's domain language. The fraud engine thinks in "alerts and scores." The CRM thinks in "cases and contacts." The card processor thinks in "authorizations and postings." None of them express what the bank actually needs: "this customer applied for a card, and fulfilling that commitment requires credit decisioning, fraud checking, card provisioning, and welcome communications — coordinated, governed, and auditable."

So the bank builds plumbing. Custom integrations, ETL jobs, message queues, middleware, glue code, manual handoffs, spreadsheets for what the integrations can't handle. This plumbing is where the actual operational work lives — not in the vendor systems, but in the brittle connections between them.

**The plumbing is the bank's technology IP.** The vendor systems are commodity — any bank can license the same fraud engine or card processor. What differentiates Bank A from Bank B is the bespoke integration layer: how they connected their specific combination of systems, the business rules embedded in the glue code, the edge cases handled in middleware, the manual procedures that compensate for what the integrations can't do. This is the bank's accumulated operational intelligence, encoded as technology.

The irony is that this IP is also the bank's most fragile, least documented, and hardest-to-evolve asset. It lives in custom code that only a few engineers understand. When those engineers leave, the IP becomes opaque. When a vendor upgrades, the IP breaks. Every bank rebuilds this plumbing from scratch — even when the business problem is identical to what another bank has already solved. It is simultaneously the most valuable and most vulnerable part of the bank's technology estate.

### The semantic translation burden

The plumbing problem would be manageable if integration were mechanical — just routing bytes between systems. But it is not. Each system speaks a different domain language. The fraud engine speaks "alerts and scores." The CRM speaks "cases and contacts." The core speaks "transactions and balances." The intelligence platform speaks "features and predictions." The engagement system speaks "journeys and events."

The plumbing does not just *connect* systems — it **translates meaning** between them. "This customer's fraud score exceeds threshold" must become "escalate this case" in CRM terms, "hold this transaction" in core terms, and "notify the customer" in engagement terms. That translation is where the domain knowledge lives. It is what makes every integration edge bespoke — the same two vendor systems at two different banks require different translation logic because the banks' domain rules, products, and risk appetites differ.

So the plumbing problem is not just a connectivity problem. It is a problem of **domain knowledge encoded as translation logic**, scattered across hundreds of bespoke integration edges, comprehensible only to the engineers who wrote them.

> **Hub Way response:** The Hub provides the shared domain vocabulary that the plumbing currently encodes. Systems register as Machines exposing Tools with domain-meaningful contracts — not vendor-specific APIs. The Scenario specifies what needs to happen in domain terms ("assess fraud risk for this application"). The Hub Application resolves that by invoking the right Tool from the right Machine. The semantic translation moves from scattered plumbing into the Machine's Tool contract — declared once, reused by every Scenario that needs it. The bank's IP transforms from fragile glue code into portable, auditable specifications: goals, commitments, disciplines, tool contracts.

## What The Plumbing Problem Costs

The plumbing problem is not abstract. It manifests as concrete, recurring costs that every bank bears:

### Migrations that take years

When a bank needs to replace a vendor system — a fraud engine, a card processor, a legacy core — the system itself is the easy part. The hard part is re-engineering all the plumbing connected to it. That plumbing encodes years of accumulated operational knowledge: edge cases, compensating logic, data transformations, business rules that exist nowhere except as code. Migrating means reverse-engineering that knowledge from brittle integrations, then re-encoding it for the new system's APIs, data model, and behavioral quirks. The work itself hasn't changed — the bank still needs to detect fraud, process payments, assess credit. But because the operational knowledge is fused into imperative plumbing — inseparable from the specific vendor system it connects to — changing the machine means rebuilding the knowledge. Migrations take years and cost multiples of the new system's license fee.

> *Hub Way: Migrations become rebinding. The Scenario specification says "I need a fraud assessment." Whether that comes from Vendor A or Vendor B is a Machine binding, not an operational redesign. Change the Tool contract, not the work.*

### Innovation trapped in code

Vendor systems provide commodity capabilities — a fraud score, a payment switch, a decisioning engine. Every bank licensing the same vendor gets the same capability. What differentiates Bank A from Bank B is how they *employ* those capabilities: the orchestration, the sequencing, the business rules that decide when to use which tool, the customer experience composed from vendor parts. That is where competitive differentiation lives — and it is all encoded as plumbing.

So the innovation bottleneck is not ideas. It is the cost of expressing ideas in plumbing. A domain expert sees an opportunity — "what if we ran the fraud check *before* the credit decision for this segment?" — but implementing it requires an engineering project: modify integrations, test regressions, deploy carefully. Innovation cycle time is gated by plumbing change velocity.

A/B testing across vendors is essentially impossible. If a bank wants to evaluate whether Vendor B's fraud engine outperforms Vendor A's on a specific transaction segment, they would need to build entirely separate integrations for Vendor B — parallel plumbing — just to run the experiment. The cost of the experiment dwarfs the cost of the vendor license. Banks make vendor commitments based on RFPs and demos, not empirical evidence from their own production traffic.

> *Hub Way: Innovation becomes specification change. "Run fraud check before credit decision for this segment" is an edit to the Scenario specification — a domain expert activity, not an engineering project. A/B testing across vendors becomes a binding decision: route a percentage of traffic to the alternative Machine's Tool, compare outcomes. The specification doesn't change; only the binding does.*

### Compensation plumbing that never stops growing

Some systems are too deeply embedded to replace. Core banking platforms, mainframe-based ledgers, entrenched payment switches — these carry enormous gravity. Not just data gravity, but integration gravity (everything connects through them), process gravity (business processes are shaped by their constraints), and contractual gravity (multi-year agreements, regulatory approvals tied to the platform).

So banks engineer around the limitations. The core system can't handle real-time events? Build a change-data-capture layer. The ledger's API can't express a new product? Build a shadow ledger in middleware. The payment switch doesn't support a new rail? Build a protocol adapter. The vendor's batch cycle is overnight but the business needs intra-day visibility? Build a caching and reconciliation layer.

Every workaround is bespoke plumbing. Over time, the workarounds accumulate into a shadow architecture — a layer of compensating logic that is often more complex than the vendor system it compensates for. This shadow architecture is undocumented, tightly coupled to specific vendor versions and quirks, breaks on upgrades, cannot be shared across banks, and becomes the *real* system of record for operational behavior — even though it was never designed to be.

> *Hub Way: Compensation becomes stated constraints. "I need intra-day balance visibility; the core provides end-of-day batch; here is the reconciliation contract" — the workaround becomes a declared constraint in the Tool contract, not hidden code. When the vendor eventually supports real-time, the constraint is relaxed and the compensation binding dissolves. Nothing needs to be torn down.*

## The Modernization Trap

Banks know they need to close the systems gap. They want to add systems of intelligence, engagement, influence, memory, and innovation to their architecture. The business demands it. The competitive landscape demands it.

But under current practices, **modernization makes the plumbing problem worse, not better**.

Every new system introduced must be plumbed into the existing systems it needs to interact with. A new intelligence platform needs data from core banking, card processing, payments, and CRM. It needs to push insights to engagement, enforcement, and action systems. Each of those connections is a bespoke integration edge — custom code, semantic translation, error handling, business rules.

Plumbing complexity does not grow linearly with the number of systems. It grows **combinatorially**. With *N* systems, the number of possible integration edges is *N(N-1)/2*. A bank with 5 systems has 10 possible edges. A bank with 12 has 66. Not every pair needs a direct edge, but in practice, modern systems are deeply interconnected — the intelligence platform feeds the engagement system which triggers the action system which updates the system of record which emits events consumed by the intelligence platform. The edges multiply.

Each edge is not a wire. It is a bespoke semantic translation layer with domain knowledge embedded in it. So the cost per edge is high, the edges are not reusable, and each new system introduced creates edges to *many* existing systems, not just one.

The result is a **decelerating modernization curve**. Each successive modern system takes longer to integrate than the last. Engineering teams spend increasing time maintaining existing plumbing — fixing breakages from vendor upgrades, adapting to new edge cases, supporting the shadow architecture of workarounds. The more plumbing exists, the more maintenance it demands, leaving *less* capacity for building the new integrations that modernization requires.

The bank needs to *accelerate* its evolution to stay competitive. But its architecture forces *deceleration*. The more it modernizes, the slower it gets. This is the trap: the systems gap demands modernization, but modernization under the current integration model produces plumbing at a rate the bank cannot sustain.

The industry has tried to solve this. Enterprise Service Buses centralized integration through a hub-and-spoke topology, but moved the complexity rather than eliminating it — each system still needed a bespoke adapter, and the bus became a monolithic bottleneck carrying the accumulated weight of every semantic translation. API gateways standardized protocols and improved discoverability, but they address *connectivity*, not the semantic translation burden. The business rules still live in custom code behind the gateway.

None of these approaches address the fundamental issue: that domain knowledge — the bank's operational intelligence — is encoded as imperative integration code, fused to specific vendor systems, and must be rebuilt every time anything changes.

> **Hub Way response:** The Hub replaces the N-squared bespoke edge topology with a domain-mediated star. Systems register as Machines. Scenarios invoke Tools by domain contract, not by vendor API. Adding a new Machine does not create edges to every other Machine — it registers Tool contracts that any Scenario can consume. The integration cost of adding a new system becomes proportional to the Tools it provides, not the number of other systems it must connect to. The combinatorial explosion is eliminated at the architectural level. Unbuilding — replacing imperative plumbing with declarative specifications — is gradual: one piece of coded integration at a time, with the existing plumbing as fallback until confidence is established.

## The Compound Picture

These problems do not exist in isolation. They compound:

- The **absence of a coherent work model** means no one can see what work exists, who does it, or how it gets done. This makes every other decision — where to apply AI, what to automate, what to migrate — a guess.
- The **organizational reality** — domain silos, uneven capabilities, channel fragmentation, customer-centricity gaps — means problems are multiplied across domains, each with a unique starting point, and the customer experience falls through the seams.
- The **systems gap** means banks lack the modern capabilities that customers, regulators, and competitors demand. But acquiring those capabilities under current practices accelerates plumbing growth.
- The **plumbing problem** means the bank's most valuable technology — its accumulated operational intelligence — is encoded in its most fragile, opaque, and hardest-to-evolve form. The semantic translation burden makes every integration edge bespoke.
- The **plumbing costs** — migrations that take years, innovation trapped in code, compensation that never stops growing — consume engineering capacity that should go toward evolution.
- The **modernization trap** means the faster the bank tries to evolve, the more plumbing it produces, the more maintenance it requires, and the slower it gets. The architecture fights the strategy.

A bank caught in this compound problem cannot introduce AI systematically, cannot transform gradually, cannot innovate at the speed its market demands, cannot migrate away from legacy without multi-year programs, cannot present a coherent experience to its customers, and cannot close the systems gap without deepening the plumbing crisis.

Each bank faces this compound problem in a unique configuration — different domains, different gaps, different debt, different starting points. Any path forward must work domain by domain, at each bank's own pace, without prescribing a fixed architecture or demanding enterprise-wide transformation.
