<!-- CO-MAINTAINED: Any new input must be evaluated for updates to this file, presentation-outline.md, and book-writing-backlog.md simultaneously. -->

# Corporate Payments by Design — Presentation Contents Discussion

**Purpose:** Reference document for the marketing team to build the presentation. Each slide section provides the headline message, talking points, supporting detail from the book, suggested visuals, pitfalls to avoid, and source references.

---

## Act 1 — The Gap

---

### Slide 0: Title

**Headline:** Corporate Payments by Design with Tachyon and Electron — the first-principles design to solve for corporate concerns.

**Key Talking Points:**
- Frame the talk as an architectural walkthrough, not a product demo
- Establish that this is about how corporate payments should work — from problem to data model
- Set expectation: we will cover the problem, the framework, the domains, the entities, the data, and the lifecycle

**Supporting Detail:**
- The title "by Design" signals intentionality — every entity, every hierarchy, every control exists for a reason
- The subtitle "first-principles" signals that we start from what corporates need, not what banks currently offer

**Suggested Visuals:**
- Clean title slide with three-domain icon (Bank / ESP / Corporate) and platform names (Tachyon / Electron)

**What to Avoid:**
- Don't open with product features or client logos
- Don't use "industry-leading" or "best-in-class" language

**Source Reference:** Book title and front matter — `00-front-matter/01-purpose-audience-scope.md`

---

### Slide 1: The Provocation — Possibilities vs Needs

**Headline:** Banks describe possibilities with virtual cards — and they are genuinely promising. Corporates hear those possibilities and imagine answers to their real questions: budget, authority, attribution, reconciliation. The gap between the promise and the imagined answer is the required evolution.

**Key Talking Points:**
- Lead with possibilities, not features. Banks describe what virtual cards make possible — API issuance, single-use controls, MCC restrictions, real-time data. These are genuinely promising. Acknowledge them.
- Then pivot: corporates hear those possibilities and imagine them answering their real questions — budget enforcement, authority chains, GL attribution, automated reconciliation. The imagination is natural and reasonable. But the product does not yet deliver what the corporate imagines.
- Name the gap: the distance between the promise and the imagined answer. This is not a criticism of the bank's product — it is a market reality. The promise is real. The imagined answer is not yet built. That is the required evolution.
- Use this framing as a lens for the rest of the presentation: every architectural decision we'll show exists to close the gap between the promise and the imagined answer.

**Supporting Detail:**
- Bank possibilities (real): "Issue a card per PO." "Lock to a single merchant." "Set velocity limits." "Get L2/L3 data." "Real-time authorization notifications."
- Corporate needs (also real): "Can I enforce budget hierarchy across three legal entities?" "Can I attribute every transaction to a GL account, cost center, and project code?" "Can I cascade policy changes across 200 supplier cards without touching each one?" "Can I reconcile against my AP system automatically?"
- The capabilities are genuine. The needs are genuine. They are not the same conversation.
- Meridian's CFO evaluates on reconciliation labor saved, policy leakage prevented, and DPO extended — not on card issuance speed or MCC control granularity.

**Suggested Visuals:**
- Two-column layout: "The Promise" (list of possibilities banks describe) vs "The Imagined Answer" (what corporates hear and need) — showing the distance between the two
- Or a single provocation statement on screen with the promise and the imagined answer appearing sequentially to build tension

**What to Avoid:**
- Don't dismiss the possibilities — they are real and valuable. The point is that they are necessary but not sufficient.
- The headline names the "gap" — that's intentional. Slide 2's table will make the gap visceral and specific.
- Don't blame banks — frame this as a market reality. The promise is genuine. The evolution is required.
- Don't trigger defense by implying "you're packaging it wrong" — surface the tension that corporates already feel and banks already hear in RFPs.

**Source Reference:** `01-problem-space/01-corporate-payments-problem.md`, `01-problem-space/02-existing-solutions.md`. Framing originated in presentation discussions — see `book-writing-backlog.md` item #13.

---

### Slide 2: The Platform Reality

**Headline:** The promise itself has limits. The processing platforms behind today’s card programs were not architected for the possibilities they now describe.

**Key Talking Points:**
- This is not a vendor critique — it is an architectural observation. The card processing platforms behind most bank programs today (TSYS, Fiserv, FIS) carry architectural patterns — batch processing, flat hierarchies, static data models, pre-allocated card inventory — that reflect the constraints of the era and use cases they were designed for. These patterns are embedded at the foundation level.
- The possibilities banks describe to corporates are real — but they are bounded by infrastructure that was not designed for corporate spend governance. The processor doesn’t prevent the bank from making the promise, but it constrains how far the promise can actually deliver.
- This creates a second layer to the gap: not only do corporates imagine answers the product doesn’t yet provide, but the underlying infrastructure makes building those answers significantly harder than it should be.
- Frame this as market structure, not blame. The bank chose a processor for good reasons. The processor was designed for its original purpose. Neither is at fault — but the constraint is real, and it shapes what “evolution” actually requires.

**Supporting Detail:**
- The next slide provides the evidence — five architectural patterns that bound the promise. This slide establishes the framing; the next slide delivers the specifics.
- Avoid naming vendors on screen. The audience will map the constraints to their own platform. If they ask, acknowledge the examples in conversation — but the slide should remain vendor-neutral.
- This provocation works because the audience (bank product and technology leaders) have lived with these constraints. They will recognize them immediately.

**Suggested Visuals:**
- Single headline statement, large type, centered.
- Optional: a subtle visual showing a “ceiling” or “boundary” above the promise — suggesting the promise reaches up but hits an architectural limit.

**What to Avoid:**
- Do not list features or vendor names on this slide.
- Do not apologize for the observation. State it as fact.
- Do not frame this as “your platform is bad.” Frame it as “the platform was built for something else.”

**Source Reference:** Presentation-originated. See `book-writing-backlog.md` item #17 and the “Legacy Platform Constraints — Detailed Reference” section at the end of this document.

---

### Slide 3: The Semantic Dissonance

**Headline:** When corporates ask questions and banks answer with card capabilities, both sides are speaking accurately — and past each other.

**Key Talking Points:**
- Present the dissonance as a table: Corporate's Question / Bank's Answer / The Gap. Let the audience read the rows and recognize the pattern from their own client conversations.
- The pattern is consistent: every answer addresses the payment dimension. None address the governance, financial architecture, or operational dimensions.
- This is not a feature gap — it is a semantic gap. The bank and the corporate are organizing around different concerns.
- Don't rush through this slide. Let each row land. The audience should feel the accumulation — row after row, the same structural shape.

**Supporting Detail:**
- Six dissonance rows (use all six or select the strongest four for pacing):
  1. PO-to-card linkage: Corporate asks "issue per PO, close after payment" → Bank offers single-use cards with amount locks → Gap: no PO linkage, no three-way match, no auto-close confirmation to AP
  2. Budget governance: Corporate asks "enforce department budgets" → Bank offers credit sub-limits → Gap: sub-limits are risk tools, not budget governance; no OU hierarchy, no purpose-based allocation
  3. GL attribution: Corporate asks "attribute every transaction to GL and project" → Bank offers card-level reference fields → Gap: fields are unstructured, unvalidated, not pushed to ERP
  4. Policy cascade: Corporate asks "cascade policy changes to all cards" → Bank offers per-card controls → Gap: no program-level policy, no inheritance, no tighten-only cascade
  5. Reconciliation: Corporate asks "reconcile against AP invoices" → Bank offers L2/L3 data → Gap: data available but not matched; no PO linkage, no automated reconciliation
  6. Enrollment: Corporate asks "onboard supplier through procurement system" → Bank offers card issuance APIs → Gap: enrollment, eligibility, merchant validation, and card tagging unsupported
- The three dissonance examples from the book (Commonwealth vs Meridian) can be woven into supporting narration

**Suggested Visuals:**
- Full-screen table with three columns: Corporate's Question / Bank's Answer / The Gap — formatted so the gap column is visually distinct (different color or weight)
- Animate rows sequentially if the medium supports it — let the pattern build
- Or a split-screen: corporate persona on left asking questions, bank persona on right answering — with the gap shown in between

**What to Avoid:**
- Don't reduce this to "banks are doing it wrong" — both sides are speaking accurately; the problem is structural, not intentional
- Don't let the audience dismiss individual rows as "edge cases" — the accumulation is the point
- Don't present the table without narrating it — each row needs a beat to land

**Source Reference:** `01-problem-space/02-existing-solutions.md`, `01-problem-space/03-two-lenses.md`. Table originated in presentation discussions — see `book-writing-backlog.md` item #14.

---

### Slide 4: Five Dimensions of Corporate Need

**Headline:** The semantic dissonance reveals a pattern. Corporate payment needs span five dimensions — and today's card products answer only the first.

**Key Talking Points:**
- Name the five dimensions: (1) Payment Execution, (2) Financial Architecture, (3) Control Architecture, (4) Accounting & Attribution, (5) Reconciliation & Settlement
- Payment Execution is well-answered — networks, schemes, real-time auth. This is table stakes.
- Financial Architecture is partially answered — credit limits and sub-limits exist, but without budget semantics, OU-awareness, or purpose-based allocation.
- Control Architecture is primitively answered — per-card controls exist, but no program-level policy, no inheritance, no lifecycle orchestration.
- Accounting & Attribution is not answered — reference fields exist but lack structure, validation, and ERP integration.
- Reconciliation & Settlement is not answered — data is available but matching, consolidation, and settlement management are left to the corporate.
- No corporate CFO evaluates a card program on authorization speed. They evaluate on reconciliation labor, policy leakage, and attribution accuracy.

**Supporting Detail:**
- Dimension table: Dimension / What the corporate needs / What card products typically provide — five rows showing the gradient from "well-answered" to "not answered"
- The five dimensions are not a product checklist — they are an analytical framework for understanding why corporate adoption stalls. Each dimension represents a class of needs that must be addressed by the platform architecture.
- Meridian example: the CFO's evaluation criteria map directly to dimensions 2-5. Dimension 1 (payment execution) is assumed.

**Suggested Visuals:**
- Five-row table: Dimension / Corporate Need / Current Card Product Answer — with a visual gradient (green → yellow → red) showing how well each dimension is addressed
- Or a radar/spider chart with five axes, showing the coverage gap between card capabilities and corporate needs
- Or a stacked bar: the first bar (Payment Execution) is full, the rest progressively empty

**What to Avoid:**
- Don't present the five dimensions as a feature list — they are analytical categories, not product requirements
- Don't skip dimensions 4 and 5 (Accounting/Attribution and Reconciliation/Settlement) — these are where the most operational pain lives, even if they sound unglamorous
- Don't imply dimension 1 is unimportant — it is essential, just already solved

**Source Reference:** Presentation-originated framework — see `book-writing-backlog.md` item #15. Draws on `01-problem-space/01-corporate-payments-problem.md` and `01-problem-space/05-spend-mandates.md` for underlying concepts.

---

### Slide 5: The Counterparty Multiplier

**Headline:** The five dimensions do not present uniformly. They vary by the type of counterparty the corporate pays — and the AP landscape has at least six distinct shapes.

**Key Talking Points:**
- Name the counterparty types: goods suppliers, service providers, contractors, SaaS/software vendors, intermediaries/agencies, government/regulatory bodies.
- Each type has different payment patterns, data needs, compliance requirements, and card acceptance realities.
- Today's card products abstract all of these as "merchants" — a single MCC-classified entity. The corporate sees six fundamentally different relationships.
- This diversity multiplies the five dimensions: financial architecture for a goods supplier (PO-locked budget) looks nothing like financial architecture for a SaaS vendor (contract-locked renewal budget).
- Don't go deep here — name the diversity, let it land, and note that the archetype discussion in the next act addresses it directly.

**Supporting Detail:**
- Counterparty table: Type / Payment Pattern / Data Needs / Compliance / Card Acceptance — six rows showing the variety
- Specific contrasts to make it concrete:
  - Goods supplier: PO-driven, deterministic, L2/L3 critical, high card acceptance
  - Contractor: time-based, project-coded, 1099 compliance, low card acceptance (ACH preferred)
  - Government: fee-schedule, non-negotiable, regulatory deadlines, often requires wire/ACH
- The merchant abstraction is not wrong — it is insufficient. MCCs describe what the merchant sells, not how the corporate governs payments to them.

**Suggested Visuals:**
- Six-row table: Counterparty Type / Payment Pattern / Data Needs / Compliance / Card Acceptance
- Or a visual showing one "merchant" icon being unpacked into six distinct relationship types — illustrating the abstraction collapse
- Or a matrix: five dimensions (columns) × six counterparty types (rows), with cells indicating how each dimension manifests differently per type

**What to Avoid:**
- Don't go too deep into any single counterparty type — the archetype discussion handles that
- Don't present this as an exhaustive taxonomy — say "at least six" to signal that more may exist
- Don't dismiss low-card-acceptance counterparties (contractors, government) — their existence in the corporate's AP landscape is part of the problem, even if card programs don't serve them directly

**Source Reference:** Presentation-originated concept — see `book-writing-backlog.md` item #16. Draws on archetype concepts from `01-problem-space/04-spend-archetypes.md`.

---

### Slide 6: The Two-Lens Gap

**Headline:** Banks organize around financial risk. Corporates organize around operational governance. Both worldviews are coherent. The friction is in the translation.

**Key Talking Points:**
- Bank's organizing principle: credit facility → account → card → MCC/amount/velocity controls → interchange → lifecycle
- Corporate's organizing principle: department → project → cost center → budget/policy/approval → GL/project/client codes → reconciliation → DPO
- The structural mismatches: org structure ≠ account structure; budget ≠ credit limit; GL fields ≠ transaction data; workflow ≠ card controls; reconciliation ≠ data availability
- This is not a criticism — banks optimize for credit risk, regulatory compliance, and network settlement because they must. Corporates optimize for operational governance, financial attribution, and audit readiness because they must.
- The gap is architectural. It requires a design that respects both organizing principles without collapsing one into the other.

**Supporting Detail:**
- Why the dissonance is structural (not accidental):
  - Banks are regulated entities; their data models reflect prudential requirements (credit exposure, capital adequacy, AML/sanctions)
  - Corporates are operational entities; their data models reflect management requirements (budgets, projects, cost centers, GL)
  - Neither can adopt the other's model without violating its own obligations
- Result: even with one issuer, a corporate like Meridian ends up with four parallel programs, separate onboarding, controls, reconciliation streams, portals, and contacts
- Finance cannot see total exposure without manual aggregation; policy changes need four configuration passes

**Suggested Visuals:**
- Two-column diagram: "Bank's Lens" (credit facility → card → MCC/amount → interchange → lifecycle) vs "Corporate's Lens" (dept → project → cost center → budget/policy/approval → GL → recon → DPO)
- Gap zone in the middle showing the mismatches (org ≠ account, budget ≠ credit limit, GL ≠ txn data, workflow ≠ card controls)
- Or a Venn diagram showing the two organizing principles with a thin, contested overlap zone

**What to Avoid:**
- Don't position this as "banks are doing it wrong" — position it as a structural reality that the three-domain model solves
- Don't promise to eliminate the gap entirely — promise to make it manageable through clean separation of concerns
- Don't blame either side — the point is that both are right, and the architecture must honor both

**Source Reference:** `01-problem-space/03-two-lenses.md`, `01-problem-space/02-existing-solutions.md`

---

### Slide 7: The Infrastructure Evidence

**Headline:** We said the promise itself has limits. Here is what those limits look like — five architectural patterns in legacy card processors that bound the promise.

**Key Talking Points:**
- Open with the callback to Slide 2: “We said the promise has its own limits. Now that you’ve seen what the corporate actually needs — five dimensions, six counterparty types, two organizing principles — here’s specifically what the current infrastructure cannot do.”
- Walk through each of the five patterns. Each now maps to something the audience has just learned — the constraints aren’t abstract anymore:
- **Batch-native, not event-native:** Legacy processors were built around batch files — daily settlement, nightly posting, periodic reconciliation. Real-time authorization events, lifecycle notifications, webhook callbacks, and cooperative authorization require middleware stacks the platform was never designed for. Ask: “When was the last time your processor pushed an authorization event in real time without middleware?”
- **Flat hierarchies, not programmable:** Per-card spending limits exist. But hierarchical budgets — where a single transaction checks the card limit, the program budget, and the legal entity credit facility, with policy cascading and ancestor-chain enforcement — do not. Ask: “Can your processor enforce a three-level budget hierarchy at authorization?”
- **Static data, not contextual:** The card carries what the network provides — MCC, merchant name, transaction amount. It cannot carry PO numbers, project codes, cost center attribution, or GL line items through the transaction lifecycle. Ask: “Can you attach a PO number to a card at issuance and have it travel through authorization, clearing, and settlement?”
- **Pre-allocated inventory, not on-demand:** Card issuance was designed for bulk ordering — request a batch, wait for provisioning, distribute. API-triggered, single-use cards at hundreds per day per corporate client require a fundamentally different inventory model. Ask: “How many single-use cards can your processor issue per minute via API?”
- **Closed authorization, not cooperative:** The processor evaluates the transaction and decides alone. There is no hook — no callback, no enrichment step, no decisioning participation — for the ESP or the corporate client within network-mandated timeouts. Ask: “Can your corporate client participate in the authorization decision before the processor responds to the network?”

**Supporting Detail:**
- Each pattern maps directly to a capability the corporate will eventually need: real-time visibility, hierarchical budgets, contextual data, on-demand issuance, cooperative authorization. After seeing Slides 3–6, the audience understands *why* each matters.
- The five patterns represent foundational architectural assumptions, not feature gaps. A feature gap can be patched; an architectural assumption requires re-platforming or a purpose-built alternative.
- The callback to Slide 2 is essential — it closes the loop the audience has been holding open since the second provocation. The payoff arrives after the problem is fully understood, making the evidence land harder.
- See the “Legacy Platform Constraints — Detailed Reference” section at the end of this document for the full catalog of eight constraint categories with detailed examples.

**Suggested Visuals:**
- Five-row table, two columns: “Legacy Pattern” and “What It Means for Corporate Payments.” Clean, readable, no clutter.
- Consider progressive reveal (one row at a time) to let each pattern land before moving to the next.
- Optional: a subtle visual connection back to Slide 2 — same color palette or motif to signal the callback.

**What to Avoid:**
- Do not present this as a feature comparison chart. It is an architectural observation, not a competitive matrix.
- Do not rush through the table. Each row is a self-contained argument.
- Do not name specific vendors in the table. The patterns are universal across legacy processors.
- Do not skip the callback to Slide 2. Without it, the slide loses its structural role.

**Source Reference:** Presentation-originated. See `book-writing-backlog.md` item #17. Full constraint catalog in “Legacy Platform Constraints — Detailed Reference” section below.

---

### Slide 8: The Foundation and The Bridge

**Headline:** This is what we set out to solve. The foundation: a processing platform purpose-built for corporate spend governance — one that resolves the constraints we just identified, and is architected for the possibilities of this decade. The bridge: an architecture that answers the corporate's actual questions across all five dimensions, across all counterparty types, while preserving the bank's risk and compliance model.

**Key Talking Points:**
- The foundation: a processing platform that is event-native, hierarchy-aware, contextually rich, on-demand, and cooperatively authorized — the inverse of every pattern identified in Slide 7. Without the right foundation, the bridge cannot hold.
- "Designed for the possibilities of this decade" means more than resolving today's constraints. The foundation must also accommodate an evolving payment landscape: credentials beyond cards, authentication beyond static mechanisms, rails and clearing beyond card networks, and digital currencies — without re-platforming for each.
- The bridge requires three things: (1) a product model that encodes corporate governance patterns, not just payment capabilities; (2) a clean separation between the bank's domain and the corporate's domain; (3) an intermediary that translates between them without blurring boundaries.
- That is the three-domain model — Bank, ESP, Corporate, each owning what it understands best — running on a processing platform designed from the ground up for these requirements.
- This slide is a transition, not a deep-dive. Two clear statements of intent, then move to the framework.
- What follows: the foundation — the payment platform, its capabilities, and how it resolves the constraints we identified. Then the bridge — the three-domain architecture, Spend Archetypes that organize the counterparty diversity into actionable product patterns, a Spend Mandate framework that captures all five dimensions, and the entity architecture that connects them.

**Supporting Detail:**
- The foundation addresses Slide 7 (the infrastructure gap): the processing platform must be purpose-built for the requirements the bridge identifies. Without event-native processing, hierarchy-aware controls, contextual data, on-demand issuance, and cooperative authorization, the domain model cannot function as designed.
- The foundation must also be extensible across the evolving payment landscape:
  - Credentials beyond cards → tokens, virtual accounts, wallet instruments, programmable credentials that carry context
  - Authentication beyond static mechanisms → adaptive authentication, device-based security, step-up flows, biometrics, context-aware risk decisions
  - Rails and clearing beyond card networks → real-time payment systems (RTP, FedNow), alternative clearing, cross-border corridors, open banking rails
  - Digital currencies → stablecoins, CBDCs, tokenized settlement instruments
- The principle is architectural agnosticism: the platform must not be coupled to any single credential type, authentication method, payment rail, or settlement mechanism. Each axis evolves independently; the foundation must accommodate all without re-platforming.
- The bridge addresses Slides 3-6 (the need gap): what "answering the corporate's questions" means architecturally:
  - Financial Architecture → hierarchical budgets derived from credit facilities, enforced at authorization
  - Control Architecture → tighten-only policy cascades from bank product to card, with program-level governance
  - Accounting & Attribution → structured booking profiles that push to ERP, not manual reference fields
  - Reconciliation & Settlement → automated matching per archetype, consolidated settlement by program
- The three-domain model is not just separation of duties — it is separation of concerns, running on infrastructure designed for corporate spend governance.

**Suggested Visuals:**
- Two-layer layout: "The Foundation" (what to build on) at the base and "The Bridge" (what to build) above — each with a one-line summary
- Or a three-icon layout (Bank / ESP / Corporate) with one sentence under each: "Risk and Compliance" / "Translation and Packaging" / "Governance and Operations" — with a foundation bar underneath showing "Event-native | Hierarchy-aware | Contextual | On-demand | Cooperative"
- Transition arrow pointing to "Act 2: The Framework"

**What to Avoid:**
- Don't turn this into a product pitch — keep it architectural
- Don't go deep on the three-domain model here — that's Slide 13
- Don't list features — list design principles
- Don't linger — this slide should create momentum into the next act
- Don't collapse the foundation and the bridge into one idea — they are distinct. One is about infrastructure, the other is about domain design

**Source Reference:** `01-problem-space/03-two-lenses.md`. Bridge framing originated in presentation discussions — see `book-writing-backlog.md` items #13-15, #17.

---

## Act 2 — The Framework

---

### Slide 9: Spend Archetypes

**Headline:** Every corporate payment maps to one of four Spend Archetypes — each with a distinct control model, card lifecycle, enrollment pattern, and reconciliation approach.

**Key Talking Points:**
- Archetypes are the organizing principle — not product names, not market segments
- Four archetypes: Supplier Payments, Employee & Department Spend, Travel & Booking Payments, Central Recurring Merchant Payments
- Each maps 1:1 to a Corporate Payment Product — if a corporate needs two archetypes, the ESP creates two products, not one product covering both
- "Embedded" (API-triggered issuance) is a delivery mechanism, not an archetype — it can serve any of the four

**Supporting Detail:**
- Supplier: single-use per invoice, merchant-locked, PO-linked, ERP reconciliation via L2/L3 three-way match
- Employee: persistent cards, MCC/velocity limits, per-employee enrollment, expense report reconciliation
- Travel: lodge card (long-lived, shared with agency) or per-booking virtual card; booking system triggers issuance
- Recurring: one card per merchant/contract, renewal-aligned lifecycle, centrally administered
- Meridian examples: ~200 suppliers with API-issued cards; 120 engineering employees with $2,500 per-tx limits; travel desk with lodge card; 35 SaaS subscriptions with dedicated locked cards

**Suggested Visuals:**
- Comparison table: Archetype × (Control Model / Card Lifecycle / Enrollment / Reconciliation) — four columns, four rows
- Or the book's `graph TB` Mermaid diagram with four subgraphs

**What to Avoid:**
- Don't mix archetype descriptions with product feature lists
- Don't use the term "Spend Lane" — the book uses "Spend Archetype" consistently
- Don't imply archetypes are rigid categories — they are workflow patterns that products are built around

**Source Reference:** `01-problem-space/04-spend-archetypes.md`

---

### Slide 10: Archetype Detail

**Headline:** How each archetype differs in practice — card usage, enrollment, and data requirements.

**Key Talking Points:**
- Walk through each archetype's distinguishing characteristics in more detail
- Emphasize the differences in card lifecycle (single-use vs persistent vs lodge) and data richness (L2/L3 vs minimal)
- Show that enrollment model differs: supplier = enroll the payee; employee = enroll the payer
- Reconciliation approach differs by archetype: PO match, expense report, itinerary match, contract match

**Supporting Detail:**
- Supplier: ERP triggers card issuance for approved PO; card locked to exact amount and specific merchant; auto-closed after clearing; L2/L3 critical for automated three-way match; reconciliation target: 95%+ auto-match
- Employee: manager or self-enrollment; persistent card with monthly velocity limits; MCC allowlists (e.g., AMC-IT-Services, AMC-Cloud, AMC-SaaS); expense management system receives transaction data
- Travel: travel desk or employee self-books; lodge card shared with agency or per-booking virtual card; itinerary data for reconciliation; booking system as the trigger
- Recurring: central administrator enrolls; one card per vendor/contract; lifecycle matches contract renewal; subscription management as the trigger

**Suggested Visuals:**
- Four mini-diagrams showing card lifecycle for each archetype (Issue → Auth → Clear → Close vs Issue → Auth → Auth → ... → Renew)
- Or a timeline-style comparison showing the different lifecycle patterns

**What to Avoid:**
- Don't go too deep into technical implementation here — that comes in Acts 5-6
- Keep focus on the "what" and "why" rather than the "how"

**Source Reference:** `01-problem-space/04-spend-archetypes.md`, `02-ontology/10-members-eligibility-enrollment.md`

---

### Slide 11: Spend Mandates

**Headline:** Before any card is issued, the corporate defines an authorization envelope — the Spend Mandate — with eight components.

**Key Talking Points:**
- The Spend Mandate is a conceptual framework, not a single database entity
- Eight components: Purpose, Authority, Budget Source, Policy Scope, Limits, Attribution, Validity, Exceptions
- Use the Meridian "Client Implementation Travel" example to make it concrete
- The mandate is realized across multiple system entities: Budget, Spend Policy, Booking Profile, Card Profile, Program configuration

**Supporting Detail:**
- Meridian example mandate: "Client Implementation Travel" for Bank X
  - Purpose: travel for implementation engagement
  - Authority: Engineering VP authorizes enrollment
  - Budget Source: Professional Services Travel — $5M
  - Policy Scope: AMC-Travel-Agencies, AMC-Hotels, AMC-Airlines
  - Limits: $5,000 per booking, $35,000 cumulative per quarter
  - Attribution: Project BNK-X-2026, Phase IMPL-PHASE-2, GL 6200-Travel
  - Validity: Apr–Jun 2026
  - Exceptions: over-limit requires CFO approval

**Suggested Visuals:**
- Table: Component / What it governs / Meridian example
- Or a radial/spoke diagram with "Spend Mandate" at center and eight components around it

**What to Avoid:**
- Don't suggest there is a "Spend Mandate" table or API — it's a conceptual framework
- Don't skip any of the eight components — each maps to real system behavior

**Source Reference:** `01-problem-space/05-spend-mandates.md`

---

### Slide 12: Two Natures of Governance

**Headline:** Not all mandate components are enforced the same way. Two distinct natures.

**Key Talking Points:**
- Constraints: evaluated at authorization in real time — budget capacity, spend policy, limits. The bank checks these on every transaction. No exception.
- Structural Decisions: enforced through issuance, configuration, and audit — purpose, authority, attribution, validity, exceptions. These shape the spend channel before the transaction happens.
- The design challenge: enforce constraints in real time while making structural decisions auditable and traceable
- This is not a limitation — it's a deliberate separation. Constraints stop bad transactions. Structural decisions ensure only the right people have access to the right cards.

**Supporting Detail:**
- Constraints at authorization: Budget hierarchy check (all ancestors), AMC/MCC match, per-tx and velocity limits, currency/geography restrictions, single-use enforcement
- Structural enforcement: program membership controls who has a card; eligibility rules control who can be enrolled; card issuance controls what credentials exist; booking profiles control how spend is attributed; validity windows control when the program is active
- The corporate enforces structural decisions at the time of issuance — by restricting who gets a card and what that card can do — the bank then enforces constraints at authorization on whatever cards exist

**Suggested Visuals:**
- Two-column layout: "Constraints — Real-time at authorization" vs "Structural Decisions — Pre-transaction and post-transaction"
- Or the book's Mermaid `graph TB` showing eight components split into two subgraphs feeding Authorization vs Governance

**What to Avoid:**
- Don't frame structural decisions as "things we can't enforce" — frame them as "things enforced through design, not through real-time checks"
- Don't use "auditable but not enforceable" — the earlier framing that was deliberately revised

**Source Reference:** `01-problem-space/05-spend-mandates.md` (reframed "Two Natures of Governance" section)

---

## Act 3 — The Three Domains

---

### Slide 13: The Three Domains — Roles and Value Added

**Headline:** Three actors, three distinct responsibilities, one coordinated payment.

**Key Talking Points:**
- Bank: provides credit facilities and payment capabilities; underwrites risk, authorizes transactions, enforces compliance, settles with networks
- ESP: provides archetypes and corporate servicing; creates products per archetype, onboards corporates, manages billing, provides the operating layer
- Corporate: provides mandate-related value; configures programs, defines budgets and policies, enrolls members, operates day-to-day governance
- Each domain owns what it understands best — the platform enforces clean separation

**Supporting Detail:**
- The bank does not see departments, cost centers, or project codes — that's corporate domain knowledge
- The corporate does not touch underwriting, credit assessment, or network settlement — that's bank domain knowledge
- The ESP translates between the two: taking bank products (credit, accounts, cards) and packaging them as corporate solutions (programs, policies, workflows)
- Platform mapping: Commonwealth on Tachyon; Apex on Electron; Meridian on Electron (corporate portal)

**Suggested Visuals:**
- Three-domain horizontal layout: Bank (Tachyon) → ESP (Electron) → Corporate (Electron Portal) with responsibility bullet points in each
- Or the book's `graph LR` three-domain diagram

**What to Avoid:**
- Don't imply the ESP is optional or just a reseller — the ESP adds substantial product design and operational value
- Don't blur domain boundaries — the clean separation is the central architectural argument

**Source Reference:** `01-problem-space/03-two-lenses.md` (domain comparison table), `00-front-matter/02-running-example.md`

---

### Slide 14: All Stakeholders — Value Realized

**Headline:** Every participant captures distinct value from the model. Value is not zero-sum.

**Key Talking Points:**
- Bank: float income, customer retention (sticky multi-program relationships), network incentives, interchange income, account and card fees, regulatory compliance as a competitive moat
- ESP: revenue share from bank (portion of float, interchange, fees), direct fees and charges from corporate, portfolio scale (40+ corporates like Apex), branding and market positioning
- Corporate: control and governance benefits (mandate enforcement), AP automation (DPO extension ~12 days on $50M payables), rebates, rewards, reconciliation labor reduction, policy leakage prevention
- Members: cashflow benefits (supplier: faster payment, improved DSO), negotiated MDRs (supplier), AR story (supplier), expense simplification (employee), travel convenience (employee)

**Supporting Detail:**
- Specific Apex numbers: product-level rebate of 1.5% on supplier pay interchange; relationship-level rebate of 50 bps on aggregate spend > $10M/quarter
- Bank economics: Commonwealth earns from the facility (interest), the account (fees), and the network (interchange) — regardless of which ESP packages the product
- Corporate economics: Meridian CFO evaluates on reconciliation labor saved, DPO extension, and policy leakage prevention — not interchange

**Suggested Visuals:**
- Four-quadrant value matrix: Bank / ESP / Corporate / Members with key value items
- Or a value flow diagram showing how interchange, float, fees, and rebates distribute across stakeholders

**What to Avoid:**
- Don't use exact interchange percentages as if they are universal — they vary by network, region, and merchant
- Don't make this slide feel like a revenue pitch for the ESP — frame it as an ecosystem where all parties benefit
- Don't omit Members — their value is real and often overlooked in bank-focused presentations

**Source Reference:** `01-problem-space/03-two-lenses.md`, `04-esp-playbook/01-esp-wide-concerns.md`

---

### Slide 15: Systems and Bounded Contexts

**Headline:** Each domain operates through purpose-built systems. Understanding what runs where is essential to the architecture.

**Key Talking Points:**
- Tachyon (Bank): 14 subsystems of relevance — covering customer lifecycle, product management, BaaS/VBO management, payments processing, credit, accounting, rewards, fraud, disputes, IAM, notifications, operations, and data
- Electron (ESP): 7 subsystems of relevance — covering client contracts, billing/collections, product and program management, a Bank Gateway (anti-corruption/translation layer to Tachyon), and two data marts (corporate-facing and ESP-facing)
- Corporate Domain: the Electron-powered portal (Payment Program Management) plus the corporate's own systems — AP, AR, expense management, travel booking, ERP/GL, treasury, IAM, and LoB applications
- The Bank Gateway in Electron is a critical architectural element — it acts as an anti-corruption and translation layer between Electron and Tachyon, ensuring each domain's model stays clean
- Tachyon and Electron each maintain their own Data Marts; Electron provides separate data views for corporates and for the ESP

**Supporting Detail:**
- **Tachyon subsystems:**
  - Customer Lifecycle Management — HAH (Headless Account Holder: quasi-customer, no KYB/KYC), LAH (Legal Account Holder: legal person, KYB), RAH (Real Account Holder: real person, KYC)
  - Product Lifecycle Management — Account Product Families, Virtual Card Product Families; catalog creation, versioning, redistributability
  - BaaS Management — manages Virtual Banking Operators (VBOs); ESP onboarding, catalog access grants, partner agreements
  - Credit Management — Credit Facilities, Limit Hierarchy, Revolving and Non-revolving Credit Accounts, Secured Credit Accounts
  - Accounting System — Accounting, Fees, Interest, Billing, Statements (account-level financial operations)
  - Payments Switch — real-time authorization routing, network connectivity, scheme message processing
  - Payments Hub — clearing, settlement, posting; end-to-end payment lifecycle orchestration
  - Rewards System — Reward Programs, Rebate Programs at Account and Statement level (product-level rewards)
  - FRM (Fraud and Risk Management) — real-time fraud scoring, transaction monitoring, risk decisioning
  - Disputes Management — chargeback processing, representment, dispute case lifecycle
  - Consumer IAM — cardholder/member authentication, credential management
  - Enterprise IAM — bank staff, ESP staff, corporate admin authentication and access control
  - Notification — bank-originated notifications (regulatory, fraud, lifecycle events); non-suppressible alerts
  - Operations Hub — bank operations console for monitoring, exception handling, servicing
  - Data Mart — bank-side analytical data store for reporting, risk analytics, regulatory reporting
- **Electron subsystems:**
  - Client Contract Management — Corporate and Contract lifecycle; relationship-level terms, scope, duration, renewal
  - Payment Product Management System — Account Variants, Virtual Card Variants, CPP assembly; component programs
  - Payment Program Management System — Program configuration, Spend Policy, Booking/Settlement Profiles, eligibility, enrollment, member and card management
  - Billing and Collections System — Consolidated Invoices, Relationship-level Rebates, Rewards, Volume Commitments, Auto Debit
  - Bank Gateway — Anti-corruption and Translation layer between Electron and Tachyon; maps ESP domain concepts to bank domain entities and vice versa
  - Corporate Data Mart — comprehensive data regarding all programs, invoices, transactions, members; Data Extracts and Reports for corporates
  - ESP Data Mart — analytics on Contracts, Products, and Programs for the ESP's own portfolio management
- **Corporate systems** (unchanged): AP, AR, Expense Management, Travel Booking, ERP/GL, Treasury, IAM/Directory, LoB Applications

**Suggested Visuals:**
- Bounded context map: three large zones (Tachyon with 14 subsystem boxes, Electron with 7 subsystem boxes, Corporate with portal + external systems) with the Bank Gateway explicitly shown at the Tachyon-Electron boundary
- For Tachyon: group subsystems into clusters — Customer & Partner (CLM, BaaS Mgmt), Product & Credit (Product LM, Credit Mgmt), Payments (Switch, Hub), Financial (Accounting, Rewards), Risk & Compliance (FRM, Disputes), Operations & Data (IAM ×2, Notification, Ops Hub, Data Mart)
- For Electron: show Bank Gateway as the bridge to Tachyon; Product and Program management as the core; Billing and Data Marts as outputs
- For corporate domain: Electron Portal in the center with spokes to AP, AR, Expense, Travel, ERP, Treasury, IAM, LoB systems

**What to Avoid:**
- Don't refer to corporate systems by vendor names as primary labels — use functional names; vendor examples are fine in parentheses
- Don't make the corporate domain look simpler than it is — the multiplicity of systems is the point
- Don't skip the Bank Gateway — it is the architectural seam between Tachyon and Electron and a common question from technical audiences
- Don't conflate Tachyon's Rewards System (account/statement level) with Electron's Billing and Collections (relationship-level rebates) — they operate at different granularities in different systems
- Don't conflate Tachyon's two IAM subsystems (Consumer vs Enterprise) — they serve different populations

**Source Reference:** `02-ontology/02-account-product-virtual-card-product.md`, `03-bank-foundation/01-account-card-products.md`, `04-esp-playbook/01-esp-wide-concerns.md`, `05-corporate-playbook/01-corporate-wide-concerns.md`. Tachyon and Electron subsystem names from domain owner input (not yet in the book — see book-writing-backlog.md).

---

### Slide 16: Context Boundaries and Integration Points

**Headline:** The systems communicate across well-defined boundaries. No domain reaches into another's internals.

**Key Talking Points:**
- Four boundary types: Bank↔ESP, ESP↔Corporate Portal, Bank↔Corporate (indirect), Corporate Portal↔Corporate Systems
- Each boundary has a clear data and control contract
- The bank never directly sees corporate OUs, members, or budgets — it sees accounts, cards, and CF utilization
- The corporate never directly touches bank products or credit assessment — it works through ESP-provisioned programs
- ERP integration is through the Corporate Portal (Electron APIs), not direct bank APIs

**Supporting Detail:**
- Bank ↔ ESP (mediated through the Bank Gateway):
  - Product redistribution: Product Lifecycle Management (Tachyon) → Bank Gateway → Payment Product Management (Electron)
  - Authorization callbacks: Payments Switch (Tachyon) → Bank Gateway → ESP/Corporate participation
  - Rewards/rebate split: Rewards System (account/statement level, Tachyon) vs Billing and Collections (relationship-level rebates, Electron)
  - Data flow: Tachyon Data Mart → Bank Gateway → Corporate Data Mart / ESP Data Mart
  - The Bank Gateway ensures anti-corruption: Tachyon's model (accounts, products, CFs) and Electron's model (variants, CPPs, programs, contracts) stay clean; the gateway translates between them
- ESP ↔ Corporate Portal: Payment Program Management System handles program provisioning, enrollment workflows; Billing and Collections handles invoicing and rebates; Corporate Data Mart provides reporting and extracts
- Bank ↔ Corporate (mediated through ESP): CF utilization and budget enforcement at auth (bank checks budget hierarchy via Payments Switch/Hub), posting data flow (L1/L2/L3), regulatory/fraud notifications from FRM and Notification subsystems (non-suppressible)
- Corporate Portal ↔ Corporate Systems: all the integration touchpoints listed in Slide 15

**Suggested Visuals:**
- Architecture diagram showing the Bank Gateway as the explicit bridge between Tachyon and Electron, with subsystem-to-subsystem connections labeled
- Sequence-style diagram showing a transaction flowing: Corporate AP system → Payment Program Mgmt → Bank Gateway → Payments Switch → Network → back through all layers
- Or a boundary diagram with arrows labeled by what crosses each boundary (data, control, notifications)

**What to Avoid:**
- Don't show direct Bank↔Corporate connections — the ESP (via Bank Gateway) always mediates (except for non-suppressible notifications from Tachyon's Notification subsystem)
- Don't oversimplify the Corporate↔Corporate Systems boundary — it's where most integration complexity lives
- Don't omit the Bank Gateway — it is one of the most architecturally significant elements and will generate questions from technical bank audiences

**Source Reference:** `03-bank-foundation/03-processing-authorization-controls.md`, `04-esp-playbook/01-esp-wide-concerns.md`. Subsystem names from domain owner input (not yet in the book).

---

## Act 4 — Entities Within Bounded Contexts

---

### Slide 17: Bank Domain Entities

**Headline:** What exists in Tachyon — the bank's model of the world.

**Key Talking Points:**
- Three customer types: HAH (headless — logical entities without KYB/KYC), LAH (legal — KYB), RAH (real — KYC)
- Credit Facility: per legal entity, per currency; bank's risk exposure anchor
- Account Product: billing cycle, delinquency rules, base fees, single currency; organized as Product Family → Product
- Virtual Card Product: scheme, BIN ranges, settlement/dispute rules; Product Family → Product
- VBO: bank's partner model; every ESP is a VBO
- The bank's catalog is finite and standardized — not one product per corporate; differentiation is at the ESP variant layer

**Supporting Detail:**
- Commonwealth's Account Products: AP-US-30 (USD, 30-day cycle, 21-day grace), AP-US-45 (45-day, 25-day grace), AP-UK-30 (GBP, 21-day), AP-IN-30 (INR, 15-day grace)
- Commonwealth's Virtual Card Products: VCP-Visa-US, VCP-MC-Global, VCP-RuPay-IN
- Same AP-US-30 serves Apex and other ESPs — bank standardization enables ESP differentiation
- Bank retains: credit/AML/sanctions/compliance, delinquency controls, base fees, scheme obligations, network settlement
- Product Family → Product hierarchy allows banks to manage catalog scale

**Suggested Visuals:**
- Entity table: Entity / Context / Description with Commonwealth examples
- Or a catalog diagram showing Commonwealth's products fanning out to multiple ESPs

**What to Avoid:**
- Don't list every Account Product attribute — focus on what makes them different (cycle, grace, currency)
- Don't confuse Product with Variant — the bank creates Products; the ESP creates Variants

**Source Reference:** `02-ontology/02-account-product-virtual-card-product.md`, `03-bank-foundation/01-account-card-products.md`

---

### Slide 18: ESP Domain Entities

**Headline:** What exists in Electron — the ESP's product design and client management model.

**Key Talking Points:**
- Account Variant: customizes a bank Account Product with component programs (fees, interest, statement, rewards, rebates, notifications)
- Virtual Card Variant: customizes a bank Virtual Card Product with component programs (embossing, spend policy, auth rules, tokenization, 3DS, card fees, notifications)
- Corporate Payment Product: exactly one Account Variant + one Virtual Card Variant = one CPP, tagged to one Spend Archetype
- Client Contract: the ESP–corporate relationship entity; carries scope, relationship-level commercial terms, duration
- Product-level terms vs relationship-level terms are distinct

**Supporting Detail:**
- Apex's variants: Apex-AV-Standard (from CNB-AP-USD-30), Apex-AV-Extended (from CNB-AP-USD-45), Apex-VCV-Visa, Apex-VCV-MC
- Apex's four CPPs: Supplier Pay, Corporate Spend, Travel Pay, Subscription Manager
- Assembly rule: 1 Account Variant + 1 Virtual Card Variant = 1 Corporate Payment Product. Cannot combine multiple of either.
- Product-level terms example: 1.5% rebate on interchange from supplier transactions (computed in Tachyon)
- Relationship-level terms example: 50 bps on aggregate spend > $10M/quarter (computed in Electron)
- Client Contract: Apex–Meridian contract covers three legal entities, four archetypes

**Suggested Visuals:**
- Assembly diagram: Bank Products → Variants → CPP (the `graph LR` from the book)
- Or Apex-specific: Commonwealth products → Apex variants → four CPPs table

**What to Avoid:**
- Don't suggest the assembly rule is flexible — it is strictly 1+1=1
- Don't confuse product-level and relationship-level commercial terms — they are computed in different systems

**Source Reference:** `02-ontology/03-esp-variants-corporate-payment-product.md`, `04-esp-playbook/01-esp-wide-concerns.md`

---

### Slide 19: Corporate Domain Entities

**Headline:** What exists in the Corporate Portal — programs, members, budgets, and the operational model.

**Key Talking Points:**
- OU: hierarchical trees (functional, geographic, legal entity) — programs and budgets attach to OUs
- Program: operational instance of a CPP; carries authority, audience, governance, spend profile, booking profile, settlement profile
- Budget: hierarchical subdivision of Credit Facility; over-allocation allowed with hierarchical enforcement at authorization
- Member: participant types (Employee, Supplier, Contractor, Client) affiliated to OUs
- Enrollment: association of member to program + card provisioning; includes card-level overrides
- Settlement Account: external bank account for corporate settlement; one per program

**Supporting Detail:**
- Meridian's OU trees: by function (Engineering, Procurement, Sales), by geography (US, UK, India), by legal entity (three LEs)
- Meridian's programs: US Supplier Payments ($30M budget), Engineering Spend ($4M), Client Travel ($5M), SaaS Subscriptions ($5M)
- Members: ~18,000 employees, 147 suppliers, 42 contractors, 11 clients = ~18,200 total
- Budget hierarchy: US $50M CF → Procurement $30M, Engineering $10M, PS Travel $5M, Sales & Marketing $5M → Engineering sub-budgets: Platform $4M, Infrastructure $3.5M, Security $2.5M
- Settlement accounts at external banks (e.g., Wells Fargo, Chase)

**Suggested Visuals:**
- Meridian landscape diagram: Legal Entities → OUs → Programs → Budgets → Members (the book's `graph TB`)
- Or entity table with Meridian examples

**What to Avoid:**
- Don't conflate OU with Legal Entity — they are distinct (OU is organizational, LE is legal/credit)
- Don't suggest one settlement account per corporate — it's one per program
- Don't imply members are always employees — suppliers, contractors, and clients are members too

**Source Reference:** `02-ontology/01-corporate-legal-entity-ou-members.md`, `05-corporate-playbook/01-corporate-wide-concerns.md`

---

### Slide 20: Entity Relationships Across Domains

**Headline:** How bank products become ESP variants become corporate programs — the derivation chain.

**Key Talking Points:**
- The chain: Account Product → ESP Account Variant → (combined with Virtual Card Variant) → Corporate Payment Product → Corporate Payment Program
- Credit Facility connects bank to corporate: CF per LE → Budget → Program → Account → Card
- Bank retains credit, compliance, and processing; ESP adds branding, terms, and packaging; Corporate adds governance, budgets, and enrollment
- Entities cross context boundaries only through well-defined integration points

**Supporting Detail:**
- Complete chain for Meridian US Supplier: Commonwealth AP-US-30 → Apex-AV-Standard + Apex-VCV-Visa → Apex Supplier Pay CPP → Meridian US Supplier Payments Program → CF-US-Meridian ($50M) → Procurement Budget ($30M) → Account → Single-use cards per invoice
- Each layer adds without removing: bank sets billing cycle, ESP adds fee programs, corporate adds spend policy tightening

**Suggested Visuals:**
- Horizontal derivation chain diagram: three columns (Bank / ESP / Corporate) with entities and arrows
- Or the book's `graph LR` assembly + program flow

**What to Avoid:**
- Don't suggest entities are "copies" across domains — each domain owns its own representation
- Don't skip the CF → Budget connection — it's how financial capacity flows from bank to corporate

**Source Reference:** `02-ontology/03-esp-variants-corporate-payment-product.md`, `02-ontology/05-corporate-payment-program.md`

---

### Slide 21: Hierarchies — Corporate's and ESP's View

**Headline:** The corporate sees multiple interlocking hierarchies. Each answers a different question.

**Key Talking Points:**
- Credit hierarchy: Corporate → LAH → CF → Budget/Limit Hierarchy → Program → Account → Cards — answers "How much can we spend?"
- Organizational hierarchy: Corporate → OU → Program → Account → Cards — answers "Who owns this spend?"
- Settlement hierarchy: Corporate → Settlement Accounts → Programs → Account → Cards — answers "How do we pay for it?"
- These hierarchies are independent but correlated at the Program level
- The ESP correlates entities across these hierarchies and across the bank domain

**Supporting Detail:**
- Entity system-of-residence: CF in Tachyon, Budget in Electron, OU in Electron, Settlement Account external — all meet at the Program
- Meridian example: CF-US-Meridian ($50M, Tachyon) → Procurement Budget ($30M, Electron) → Supplier Payments Program (Electron) → Account (Tachyon) → Cards (Tachyon), with OUs and settlement accounts from corporate domain

**Suggested Visuals:**
- Three parallel vertical hierarchies side by side: Credit / Organizational / Settlement — connected at the Program level
- Color-code by system-of-residence (Tachyon entities vs Electron entities vs external)

**What to Avoid:**
- Don't show these as a single hierarchy — the point is that they are distinct but correlated
- Don't omit system-of-residence — it's key for the audience to understand where data lives

**Source Reference:** `02-ontology/04-credit-facility-budget-account.md`, `05-corporate-playbook/01-corporate-wide-concerns.md`

---

### Slide 22: Hierarchies — Bank's View

**Headline:** The bank sees a simpler, risk-anchored hierarchy. This is by design.

**Key Talking Points:**
- Bank's view: LAH → CF → Limit Hierarchy → Account → Cards
- The bank does not see departments, cost centers, project codes, budget allocations, OU trees, settlement preferences, or member roles
- The bank enforces: CF capacity, budget hierarchy (utilization at auth), spend policy (effective cascade), non-overridable controls
- Clean separation: bank focuses on risk and compliance; corporate focuses on governance and operations

**Supporting Detail:**
- Non-overridable bank controls: AML screening, sanctions, fraud scoring, regulatory holds, delinquency/NPA blocks, CF breaches, servicing compliance
- Budget enforcement at auth: bank checks the budget node and all its ancestors up to the CF root — even though the budget hierarchy is a corporate construct, the bank enforces it
- The bank does not know why a budget exists or who created it — it only knows the budget capacity and current utilization

**Suggested Visuals:**
- Simple vertical hierarchy: LAH → CF → Limits → Account → Cards
- Contrast with the corporate's three-hierarchy view from Slide 21
- Gray out what the bank doesn't see (OUs, cost centers, GL codes) to visually reinforce the separation

**What to Avoid:**
- Don't make the bank's limited view sound like a weakness — frame it as intentional separation of concerns
- Don't suggest the bank ignores budgets — it enforces them; it just doesn't define them

**Source Reference:** `03-bank-foundation/03-processing-authorization-controls.md`, `02-ontology/04-credit-facility-budget-account.md`

---

## Act 5 — How the Story Becomes Data

---

### Slide 23: Corporate Payment Program's Reflection on Bank's Entities

**Headline:** Every corporate program has a precise footprint in the bank's entity model.

**Key Talking Points:**
- A single program creates/references: one CF, one or more budget nodes, one account (supplier/recurring) or one account per member (employee/travel), virtual cards (per enrollment/transaction/merchant), effective spend policy, booking profile, settlement profile
- Account cardinality depends on archetype: supplier = one account per program; employee = one account per employee
- The bank sees account + card + CF utilization; the corporate sees program + budget + enrollment + attribution; both views are consistent

**Supporting Detail:**
- Meridian US Supplier Payments: CF-MER-USD ($50M) → Procurement Budget ($30M) → one account → single-use cards per approved invoice; effective policy = Apex product policy (AMC-Logistics, Cloud, Manufacturing; per-tx $1M) tightened by Meridian program (AMC-Logistics + Cloud only; per-tx $500K)
- Meridian Engineering Spend: same CF → Engineering Budget ($4M) → one account per engineer → persistent cards; effective policy per card may further tighten to specific AMC

**Suggested Visuals:**
- Diagram showing a single Program and all the bank/ESP/corporate entities it touches — like a "program footprint" map
- Or a table: Entity / Domain / What the program creates or references

**What to Avoid:**
- Don't oversimplify account cardinality — it varies by archetype and is a key design decision
- Don't conflate booking profile with spend policy — booking is attribution, spend policy is control

**Source Reference:** `02-ontology/05-corporate-payment-program.md`, `02-ontology/04-credit-facility-budget-account.md`

---

### Slide 24: Policy Cascade — Tighten-Only, Bank-Enforced

**Headline:** Controls narrow at each level. No level can widen what the level above has set.

**Key Talking Points:**
- Four levels: Bank Base (Account Product) → ESP Variant (Product Spend Policy) → Corporate Program → Card Profile
- Each level inherits from above and may only tighten — Program cannot exceed Product; Card cannot exceed Program
- The bank evaluates the effective policy (intersection of all four levels) at authorization — no override path
- This is the key technical differentiator — spend time here

**Supporting Detail:**
- Example cascade for Meridian Supplier:
  - L1 Bank: all MCCs, per-tx $10M, all currencies, all geographies
  - L2 ESP (Apex Supplier Pay): AMC-Logistics + Cloud + Manufacturing, per-tx $1M, 500 tx/month
  - L3 Program (Meridian US Supplier): AMC-Logistics + Cloud only, per-tx $500K, monthly aggregate $5M, 50 tx/month, US, USD
  - L4 Card (specific supplier): AMC-Logistics only, $25K, single-use
- Declined example: a $30K card at L4 with $25K limit → declined even though L3 allows $500K

**Suggested Visuals:**
- Funnel/narrowing diagram: four levels with progressively tighter controls
- Or side-by-side column: Level / AMC / Per-tx / Velocity / Geo — showing how each tightens
- The book's `graph TD` policy cascade flowchart

**What to Avoid:**
- Don't suggest there is a mechanism to override a higher level — there is not
- Don't confuse AMC (Authorized Merchant Category — corporate construct) with MCC (Merchant Category Code — network standard)

**Source Reference:** `02-ontology/07-spend-policy-controls.md`, `03-bank-foundation/03-processing-authorization-controls.md`

---

### Slide 25: Authorization Flow

**Headline:** Every transaction follows the same path. The bank is the single enforcement point.

**Key Talking Points:**
- Path: Merchant → Payment Network → Bank (Commonwealth/Tachyon) → optional callbacks to ESP (Apex) and Corporate (Meridian) → bank aggregates → response to network → merchant
- Sequential fail-fast checks: card active, account active, CF capacity, budget capacity (ancestor chain), spend policy, non-overridable controls
- Optional ESP/corporate participation: callback model with timeout fallback
- Non-overridable controls: AML, sanctions, fraud, regulatory holds, delinquency, NPA, CF breach — cannot be relaxed by any party
- After clearing: posting updates balance, CF utilization, budget consumption, rewards/rebates

**Supporting Detail:**
- Approved example: $3,000 electronics purchase by Meridian engineer; CF $42M of $50M available; Engineering budget $180K remaining; per-tx limit $5,000; 2nd tx this month vs 10/month velocity — all pass
- Declined example: $450 at restaurant on IT program — AMC-Restaurants not in allowlist (only AMC-IT-Services, AMC-Cloud, AMC-SaaS); declined before later checks even run (fail-fast)
- ESP callback: Apex may add enrichment data or confirm authorization within timeout window
- Corporate callback: Meridian may participate for specific programs (e.g., high-value supplier payments)

**Suggested Visuals:**
- Sequence diagram: Merchant → Network → Bank (check cascade) → optional ESP/Corp → response path (the book's sequence diagram)
- Or the simplified flow chart from the outline

**What to Avoid:**
- Don't imply ESP/corporate callbacks are required — they are optional participation
- Don't suggest the bank can be overridden by ESP or corporate decisions — bank has final authority
- Don't use the word "gateway" — the bank is not a gateway; it is the authorization authority

**Source Reference:** `03-bank-foundation/03-processing-authorization-controls.md`

---

### Slide 26: Transaction Posting — L1/L2/L3 Data

**Headline:** Every posted transaction carries data from three sources, enabling end-to-end attribution and reconciliation.

**Key Talking Points:**
- Three data levels: L1 (network core), L2 (tax and references), L3 (line items)
- Three sources: Network provides L1; Merchant enriches with L2/L3; Payer contributes via card tags set at issuance
- Card tags: PO number, invoice number, cost center, project code, GL account, client code — set at issuance, travel with the transaction
- Archetype determines data richness: supplier = deep L2/L3 for three-way match; employee = minimal L3, receipts post-facto; travel = itinerary data; recurring = contract references

**Supporting Detail:**
- LogiCorp example: $47,250, MCC 5085 (Industrial Equipment), PO-2847, INV-9921, tax $3,937.50 (8.33%), three L3 line items with quantities, unit prices, and commodity codes
- Datadog example: $2,400, MCC 5734 (Computer Software), project PLAT-OBSERVABILITY, GL routing 6310 vs default 6300
- Master statement: for multi-account programs, Electron generates a consolidated statement across all accounts in the program

**Suggested Visuals:**
- Table: Data Level / Source / Content with examples
- Or a three-source diagram: Network → L1, Merchant → L2/L3, Payer → Card Tags — all converging on the posted transaction

**What to Avoid:**
- Don't assume all transactions have L3 data — it depends on merchant capability and network support
- Don't suggest card tags are post-transaction — they are set at issuance and ride with the card

**Source Reference:** `02-ontology/11-transaction-posting-data.md`

---

### Slide 27: Comprehensive Manifestation at Every Transaction

**Headline:** At every transaction, every entity across all three domains is touched. One event, three views.

**Key Talking Points:**
- A single transaction updates entities in the bank, ESP, and corporate domains simultaneously
- Bank: CF utilization, account balance, card lifecycle state, spend policy compliance verified
- ESP: product-level rebate computed, relationship-level aggregate tracked
- Corporate: program reporting, budget consumption (hierarchy-aware), booking profile applied (GL/cost center/project), settlement profile (next billing cycle)
- The bank sees a transaction on an account. The corporate sees a governed spend event with full attribution. Both are the same event.

**Supporting Detail:**
- Full entity association table (from outline): 11 entities across three domains touched per transaction
- Budget update is hierarchy-aware: when a transaction clears, the budget node AND all its ancestors are updated
- If single-use card: card moves to "Closed" state after clearing
- Rewards split: product-level in Tachyon (e.g., 1.5% interchange), relationship-level in Electron (e.g., 50 bps aggregate)

**Suggested Visuals:**
- Three-column table: Domain / Entity / What is recorded/updated
- Or a radial diagram with the transaction at center and spokes to each entity

**What to Avoid:**
- Don't present this as a "feature list" — present it as the natural consequence of the architecture
- Don't skip the dual-system rewards split — it's a common question from bank prospects

**Source Reference:** `02-ontology/11-transaction-posting-data.md`, `03-bank-foundation/03-processing-authorization-controls.md`, `02-ontology/08-booking-settlement-profile.md`

---

## Act 6 — Program Lifecycle and Extensibility

---

### Slide 28: Program Lifecycle — Overview

**Headline:** A program's lifecycle spans setup, operations, and financial management — each with distinct system interactions.

**Key Talking Points:**
- 12 lifecycle steps from credit facility to dispute resolution
- Three phases: Setup (CF → Program → Enrollment → Cards), Operations (Auth → Notifications → Fraud → Card management), Financial (Statements → Reconciliation → Settlement → Disputes)
- Each phase involves different bounded contexts and integration points
- The lifecycle is the same across archetypes — what changes is the archetype-specific behavior within each step

**Supporting Detail:**
- The 12 steps listed in the outline, each with the system(s) involved:
  1. CF extended (Tachyon) → 2. Program created (Electron) → 3. Budget allocated (Electron) → 4. Eligibility defined (Electron) → 5. Members enrolled, cards issued (Electron + Tachyon) → 6. Auth callbacks (Tachyon → Electron → Corporate) → 7. Notifications (Tachyon → Electron → Corporate) → 8. Fraud alerts (Tachyon, non-suppressible) → 9. Statement generated (Electron) → 10. Reconciliation (Corporate systems) → 11. Settlement (Corporate treasury → bank) → 12. Disputes (Tachyon, Electron)

**Suggested Visuals:**
- Horizontal timeline or swimlane diagram: Setup → Operations → Financial, with key steps marked
- Color-code by which system is primary at each step

**What to Avoid:**
- Don't make this look like a sequential waterfall — many operational steps happen concurrently
- Don't skip dispute resolution — bank prospects care about it

**Source Reference:** `05-corporate-playbook/02-supplier-payments-program.md` (12-step journey), `03-bank-foundation/02-onboarding.md`

---

### Slide 29: Setup Phase

**Headline:** From credit facility to first card issued.

**Key Talking Points:**
- Bank extends CF to legal entity (KYB completed, limit set, covenants defined) — one CF per LE per currency
- Corporate selects CPP from ESP's catalog and creates a Program
- Program configuration: budget, spend policy, booking profile, settlement profile
- Eligibility rules define who may be enrolled (member type, OU affiliation, approval requirements)
- Enrollment: eligibility verified → optional approval → optional KYC → account provisioned → card issued
- For supplier programs: card issuance is typically API-triggered from ERP/AP system per approved invoice

**Supporting Detail:**
- Commonwealth KYB for Meridian: three LEs verified, three CFs extended ($50M USD, £12M GBP, ₹400M INR)
- Apex onboarding: Client Contract signed, variants selected, four CPPs offered
- Meridian creates four US programs: Supplier ($30M budget), Engineering Spend ($4M), Client Travel ($5M), SaaS ($5M)
- Supplier enrollment: LogiCorp registered, PO-4521 approved → single-use card issued for $47,250 → card carries tags PO-4521, INV-2847, AMC-Logistics

**Suggested Visuals:**
- Sequence diagram from onboarding chapter: Bank → ESP → Corporate with KYB, CF, product, program, enrollment steps
- Or a simplified version with three swimlanes

**What to Avoid:**
- Don't conflate ESP onboarding (one-time) with corporate onboarding (per-client, repeated)
- Don't skip KYB — it's per legal entity, not per corporate, and bank prospects care about regulatory compliance

**Source Reference:** `03-bank-foundation/02-onboarding.md`, `02-ontology/10-members-eligibility-enrollment.md`

---

### Slide 30: Operational Phase

**Headline:** Day-to-day transaction processing, monitoring, and card management.

**Key Talking Points:**
- Authorization with optional callbacks: ESP/corporate can participate in authorization decisions within timeout windows
- Real-time notifications: authorization approvals, declines, clearance confirmations
- Fraud notifications: bank-originated, non-suppressible — corporate receives for member communication
- Budget monitoring: threshold alerts at 75%, 90% utilization at budget and program level
- Card management: suspend, reactivate, close, replace, modify limits — all within program policy bounds
- Card lifecycle events: expiry warnings, closure confirmations, renewal triggers

**Supporting Detail:**
- Cooperative authorization: Apex receives callback from Commonwealth, may add data or confirm within timeout; Meridian may participate for high-value programs
- Notification hierarchy: bank regulatory/fraud → non-suppressible; ESP templates → corporate customizable; card-level → member preferences
- Budget alerts: Meridian configured at 75% and 90% of budget utilization; email to Program Admin, SMS for declines
- Card operations: Engineering VP can suspend employee cards during leave, reactivate on return — without program-level impact

**Suggested Visuals:**
- Operational flow diagram: Auth request → check cascade → optional callbacks → decision → notifications → posting
- Or day-in-the-life view showing concurrent operational activities

**What to Avoid:**
- Don't make callbacks seem mandatory — they are optional participation
- Don't suggest corporates can override bank fraud decisions

**Source Reference:** `03-bank-foundation/03-processing-authorization-controls.md`, `05-corporate-playbook/01-corporate-wide-concerns.md`

---

### Slide 31: Financial Phase

**Headline:** Billing, settlement, reconciliation, and dispute resolution.

**Key Talking Points:**
- Statement generation: ESP-generated (Electron), per billing cycle, per account; master statement aggregates multi-account programs
- Reconciliation: matched against corporate systems — PO/invoice match (supplier), expense reports (employee), itineraries (travel), contracts (recurring)
- Auto-repayment: settlement profile defines auto-sweep on due date from designated settlement account
- Disputes: initiated through bank dispute process; credits follow original booking attribution
- Rebates: product-level (Tachyon, per-product) and relationship-level (Electron, across products/entities)

**Supporting Detail:**
- Billing: 30-day cycle, 15-day payment window after close (Apex configuration)
- Master statement: Meridian Engineering Spend program with 200+ employee accounts → single consolidated statement
- Reconciliation targets: supplier programs target 95%+ auto-match via L2/L3 and card tags
- Rebate example: 1.5% on Supplier Pay interchange (product-level, Tachyon) + 50 bps on aggregate > $10M/quarter (relationship-level, Electron)
- Settlement: auto-sweep from Wells Fargo operating account (4481) for supplier program; manual for engineering spend via Chase (7722)
- Dispute credits follow the original booking profile: if original was GL 5100 / CC-3000, credit reverses the same allocation

**Suggested Visuals:**
- Financial cycle diagram: Statement → Review → Approval → Payment → Confirmation
- Or reconciliation flow: Transaction data + Corporate system data → match/exception → GL posting

**What to Avoid:**
- Don't conflate billing (ESP charges to corporate) with settlement (corporate pays bank for credit facility usage)
- Don't omit dispute resolution — it matters to bank prospects

**Source Reference:** `02-ontology/08-booking-settlement-profile.md`, `05-corporate-playbook/02-supplier-payments-program.md`

---

### Slide 32: Embedding and Extension

**Headline:** The platform supports deep integration with corporate systems and cooperative authorization.

**Key Talking Points:**
- ERP Embedding: AP systems trigger card issuance via ESP APIs; posting data flows to GL; reconciliation data exported for three-way match
- Cooperative Authorization: two capabilities — Authorization Decision (ESP/corporate participate in auth) and Posting Enrichment (corporate enriches posting data at clearing)
- These are extension points, not requirements — the platform works without them, but they unlock deeper automation

**Supporting Detail:**
- ERP integration patterns:
  - AP: approved PO → API call → card issued with exact amount + merchant + tags → authorization → clearing → posting data pushed to AP for three-way match
  - Expense: transaction data → expense management system → receipt match → policy compliance → GL posting
  - Travel: booking confirmation → card issued with itinerary tags → authorization → clearing → itinerary reconciliation
- Cooperative auth: Meridian's AP system receives callback, verifies PO is still open and unfulfilled, confirms authorization — all within network timeout
- Posting enrichment: at clearing, Meridian's system adds project code updates, GL routing adjustments, cost center overrides based on current organizational data

**Suggested Visuals:**
- Integration architecture diagram: Corporate Systems ↔ Electron APIs ↔ Tachyon
- Or a sequence diagram showing cooperative authorization flow

**What to Avoid:**
- Don't suggest cooperative auth replaces bank authority — bank retains final decision
- Don't make integration seem trivial — acknowledge that corporate system integration is the most complex part of deployment

**Source Reference:** `03-bank-foundation/03-processing-authorization-controls.md`, `05-corporate-playbook/02-supplier-payments-program.md`

---

## Act 7 — The Opportunity

---

### Slide 33: Meridian End-to-End

**Headline:** One corporate, four archetypes, three legal entities, one platform — all running simultaneously.

**Key Talking Points:**
- Four programs running on the same platform, same CF hierarchy, same OU structure, same member base
- Each with distinct controls, card lifecycle, enrollment model, and reconciliation approach
- UK and India run parallel programs with local currency CFs
- Finance gets consolidated exposure across all programs, all legal entities, all currencies — without manual aggregation
- This is what "by design" means — the architecture naturally supports this without workarounds

**Supporting Detail:**
- Summary table: Program / Archetype / Budget / Cards / Lifecycle / Reconciliation (from outline)
- Cross-program visibility: Meridian CFO sees total exposure of $50M (US) + £12M (UK) + ₹400M (India) across all four archetypes
- Policy changes: when Meridian restructures engineering OUs, budget and program OU affiliations update; CF unchanged; cards persist through program
- Scale: ~2,400 supplier payments/month; 200+ employee accounts; lodge cards and per-booking cards for travel; 35 SaaS subscription cards

**Suggested Visuals:**
- Four-archetype summary table with key dimensions
- Or a landscape diagram showing all four programs, three LEs, CFs, budgets, and settlement paths

**What to Avoid:**
- Don't make this a feature recap — make it a "this is what running looks like" story
- Don't introduce new concepts here — this slide should synthesize, not teach

**Source Reference:** `00-front-matter/02-running-example.md`, `05-corporate-playbook/01-corporate-wide-concerns.md`

---

### Slide 34: Next Steps / Engagement Path

**Headline:** Where to go from here.

**Key Talking Points:**
- Platform deep-dive: walk through a specific archetype with the bank's own use case
- Product catalog design: map existing card products to Account Product / Virtual Card Product model
- ESP partner discussion: how VBO partners would create variants and CPPs on the bank's platform
- Pilot scoping: identify a corporate client and archetype for proof-of-concept
- Technical architecture review: Tachyon + Electron integration, API capabilities, auth flow

**Supporting Detail:**
- Tailor the next step to the audience's readiness level
- If product-oriented: start with catalog design workshop
- If partnership-oriented: start with ESP/VBO discussion
- If implementation-oriented: start with pilot scoping

**Suggested Visuals:**
- Simple next-steps list or engagement timeline
- Keep this slide clean and action-oriented

**What to Avoid:**
- Don't end with a generic "contact us" — provide specific, valuable next steps
- Don't rush this slide — it's where commitment happens

**Source Reference:** N/A — engagement-specific

---

## Standalone Sections

---

### Legacy Platform Constraints — Detailed Reference

**Purpose:** Supporting material for the "Platform Reality" slide in Act 1. This catalog provides the speaker and marketing team with the full set of architectural constraints found in legacy card processors (TSYS/Global Payments, Fiserv, FIS, and similar). The slide itself should name *patterns*, not list features. This reference enables the speaker to provide specific examples when challenged.

**Constraint categories and specifics:**

**1. Batch-native, not event-native:**
- Authorization notifications, clearing confirmations, lifecycle events designed for batch file exchange
- No native webhook/event-driven architecture; real-time event streaming requires custom middleware
- Settlement and posting on batch cycles; real-time balance and utilization queries difficult
- Batch-oriented integration pattern limits how quickly corporate systems can react to payment events

**2. Flat hierarchies, not programmable:**
- Per-card or per-account limits only; no hierarchical budgets with ancestor-chain enforcement at authorization
- No program-level policy inheritance or tighten-only cascade
- Static MCC blocks and flat amount limits; no dynamic, context-aware controls (budget hierarchy, custom merchant categories, cross-program velocity)
- No custom merchant categorization (AMCs) — only network-standard MCC codes

**3. Static data fields, not contextual:**
- No mechanism to attach corporate context (PO, project code, cost center, GL account) to cards at issuance that persists through the transaction lifecycle
- Reference fields unstructured, unvalidated, not pushed to ERP
- Refunds/credits not attributed back to original booking profile — manual reconciliation required
- No clearing enrichment hooks for external systems to augment posting data

**4. Pre-allocated inventory, not on-demand:**
- Card numbers and BINs managed as static pools, pre-allocated in ranges
- Not designed for high-frequency, API-triggered, single-use issuance (hundreds/thousands per day)
- Card lifecycle operations (suspend, reactivate, close, replace) designed for call-center workflows, not programmatic bulk operations
- Coarse card states (active, suspended, closed); no granular distinction by suspension reason

**5. Closed authorization path, not cooperative:**
- Processor decides alone; no architectural hook for ESP or corporate participation within network timeouts
- No posting enrichment — transaction data cannot be augmented at clearing time
- Authorization decision and posting enrichment are the two cooperative capabilities absent from legacy architectures

**6. Token and authentication rigidity:**
- Token lifecycle not coordinated with card lifecycle (renewal, reissuance, replacement); token-to-card mapping breaks
- Token/authentication lifecycle invisible to FRM — fraud systems have credential lifecycle blind spots
- Limited authentication versatility across CNP/CP scenarios; limited 3DS 2.x, FIDO, biometric support
- PIN delivery limited to legacy channels (mail, IVR); no digital-first delivery (in-app, push, QR)

**7. Billing and statement rigidity:**
- Fixed billing cycles; no per-program or per-archetype configurability
- No master statement for multi-account programs (e.g., 200+ employee accounts)
- Rewards/rebates computed per account, not across a relationship or program

**8. Multi-currency constraints:**
- Single currency per account; multi-currency requires separate accounts, reconciliation, reporting
- No consolidated cross-currency exposure view without manual aggregation
- Limited support for corporate treasury FX policies at transaction time

**Usage guidance:** The speaker should name 2-3 specific constraints per architectural pattern when substantiating. Bank executives will recognize these from their own experience — the goal is shared recognition, not competitive attack. Frame constraints as the natural result of the era, technology stack, and use cases these platforms were designed for — not as engineering failures.

---

### Running Example Guidance

**Entities:** All three are fictitious. Always state this if presenting externally.

| Entity | Role | Platform | Key Facts |
|---|---|---|---|
| Commonwealth National Bank | Bank | Tachyon | Underwrites CFs, creates Account/Virtual Card Products, authorizes all transactions |
| Apex Payments | ESP | Electron | Creates variants and CPPs, onboards corporates, manages billing; 40+ corporate clients |
| Meridian Industries | Corporate | Electron Portal | 3 legal entities (US/UK/India), 18,000+ employees, 4 spend archetypes, multi-currency |

**Credit Facilities (canonical values — use consistently):**
- CF-US-Meridian: US $50M (USD)
- CF-UK-Meridian: £12M (GBP)
- CF-IN-Meridian: ₹400M (INR)

**US Budget allocations:**
- Procurement Operations: $30M
- Engineering: $10M (sub-budgets: Platform $4M, Infrastructure $3.5M, Security $2.5M)
- Professional Services Travel: $5M
- Sales & Marketing: $5M

**Members:**
- ~18,000 employees, 147 suppliers, 42 contractors, 11 clients

**Named suppliers/merchants:** Apex Logistics (LogiCorp), CloudVault, TravelRight, SaaSGrid, Datadog

**Settlement accounts:** Wells Fargo (4481 for supplier), Chase (7722, 7730, 7735 for other programs)

---

### Terminology Quick Reference

| Term | Definition |
|---|---|
| **Spend Archetype** | One of four workflow patterns: Supplier, Employee, Travel, Central Recurring |
| **Spend Mandate** | Conceptual authorization envelope with eight components; not a single system entity |
| **HAH** | Headless Account Holder — quasi-customer in bank CLM, no KYB/KYC; used for logical entities |
| **LAH** | Legal Account Holder — legal person subject to KYB obligations |
| **RAH** | Real Account Holder — real person subject to KYC obligations |
| **VBO** | Virtual Bank Officer — bank partner authorized to resell/distribute bank products; every ESP is a VBO |
| **Account Product** | Bank-defined (Tachyon) account template: billing cycle, delinquency, fees, single currency |
| **Virtual Card Product** | Bank-defined (Tachyon) card template: scheme, BIN, settlement/dispute rules |
| **ESP Account Variant** | ESP-defined (Electron) customization of a bank Account Product with component programs |
| **ESP Virtual Card Variant** | ESP-defined (Electron) customization of a bank Virtual Card Product with component programs |
| **Corporate Payment Product (CPP)** | Exactly 1 Account Variant + 1 Virtual Card Variant, tagged to 1 Spend Archetype |
| **Corporate Payment Program** | Corporate-configured operational instance of a CPP |
| **Credit Facility (CF)** | Bank's credit exposure per legal entity per currency |
| **Budget** | Hierarchical corporate subdivision of CF; over-allocation allowed, hierarchy-enforced at auth |
| **AMC** | Authorized Merchant Category — corporate/ESP construct for grouping merchants |
| **MCC** | Merchant Category Code — network-standard classification |
| **Client Contract** | ESP–corporate relationship entity: scope, terms, duration |
| **OU** | Organizational Unit — hierarchical corporate structuring mechanism |
| **Booking Profile** | Rules for GL, cost center, project, client attribution |
| **Settlement Profile** | Settlement account, billing entity, auto-sweep or manual timing |
| **Product Family** | Bank-level grouping of Account Products or Virtual Card Products |

---

### Anticipated Bank Questions

**Q: How does this differ from what we do today with our commercial card platform?**
- A: Most commercial card platforms package products around what the bank optimizes (credit risk, interchange). This model starts from what the corporate needs (governance, attribution, reconciliation) and maps bank capabilities to corporate workflows through the ESP layer. The key difference is the three-domain separation and the archetype-based product design.

**Q: Does the ESP replace our relationship with the corporate?**
- A: No. The bank retains the direct credit relationship (CF per legal entity), all regulatory obligations (KYB, AML, sanctions), and sole authorization authority. The ESP adds product packaging, corporate servicing, and billing — functions the bank typically does not provide at the operational depth corporates need.

**Q: Who controls the card authorization?**
- A: The bank. Always. The policy cascade is tighten-only (Bank → ESP → Program → Card), and the bank evaluates the effective policy at every transaction. Non-overridable controls (AML, sanctions, fraud, delinquency) cannot be relaxed by any party. ESP and corporate may optionally participate via callbacks, but the bank makes the final decision.

**Q: What happens to our existing card products?**
- A: Existing products map to Account Products and Virtual Card Products in the Tachyon model. The bank's catalog remains finite and standardized. ESPs create Variants and CPPs on top of the bank's products — the bank's products don't change; they gain a distribution and packaging layer.

**Q: How does this handle multi-entity, multi-currency corporates?**
- A: Each legal entity gets its own Credit Facility in the appropriate currency. The corporate's OU hierarchy can span legal entities. Programs are scoped to a single CF (and thus a single currency and LE), but the corporate portal provides consolidated visibility across all LEs, currencies, and programs.

**Q: What about data security — does the corporate see bank data or vice versa?**
- A: Clean separation. The bank does not see OUs, cost centers, project codes, or member roles. The corporate does not see bank product internals, credit assessment details, or other clients' data. Each domain sees only what it owns, plus the integration data that crosses boundaries (transaction posting, CF utilization, budget consumption).

**Q: Can a corporate work with multiple ESPs?**
- A: Yes. Different ESPs can create different Variants and CPPs from the same bank products. A corporate could use one ESP for supplier payments and another for employee spend. Each ESP has its own Client Contract and commercial terms with the corporate.

**Q: What if the corporate wants to change ESP?**
- A: Credit Facilities (bank-level) survive ESP changes. Programs (ESP-level) do not — they are tied to ESP Variants and CPPs. The new ESP would create new Variants and CPPs, and the corporate would create new Programs. This is a deliberate design: credit relationships are durable, commercial relationships are replaceable.

**Q: How does budget over-allocation work?**
- A: The corporate can allocate more budget to child nodes than the parent holds. Enforcement happens at authorization: the bank checks the budget node AND all ancestor nodes. If any ancestor is at capacity, the transaction is declined. This allows flexible planning without risk of overspend.

**Q: What about physical cards?**
- A: The architecture supports both physical and virtual cards. Virtual Card Products define the scheme and capabilities; physical cards are an issuance option within the same product model. The book focuses on virtual cards because they are the dominant form in corporate payments, but the entity model accommodates both.

---

### Source Mapping

| Slide | Book Chapter(s) |
|---|---|
| 0 — Title | `00-front-matter/01-purpose-audience-scope.md` |
| 1 — The Provocation — Possibilities vs Needs | `01-problem-space/01-corporate-payments-problem.md`, `01-problem-space/02-existing-solutions.md`. See `book-writing-backlog.md` #13 |
| 2 — The Platform Reality | Presentation-originated. See `book-writing-backlog.md` #17 |
| 3 — The Semantic Dissonance | `01-problem-space/02-existing-solutions.md`, `01-problem-space/03-two-lenses.md`. See `book-writing-backlog.md` #14 |
| 4 — Five Dimensions of Corporate Need | Presentation-originated. See `book-writing-backlog.md` #15 |
| 5 — The Counterparty Multiplier | Presentation-originated. See `book-writing-backlog.md` #16 |
| 6 — The Two-Lens Gap | `01-problem-space/03-two-lenses.md`, `01-problem-space/02-existing-solutions.md` |
| 7 — The Infrastructure Evidence | Presentation-originated. See `book-writing-backlog.md` #17, Legacy Platform Constraints reference section |
| 8 — The Foundation and The Bridge | `01-problem-space/03-two-lenses.md`. See `book-writing-backlog.md` #13-15, #17 |
| 9 — Spend Archetypes | `01-problem-space/04-spend-archetypes.md` |
| 10 — Archetype Detail | `01-problem-space/04-spend-archetypes.md`, `02-ontology/10-members-eligibility-enrollment.md` |
| 11 — Spend Mandates | `01-problem-space/05-spend-mandates.md` |
| 12 — Two Natures of Governance | `01-problem-space/05-spend-mandates.md` |
| 13 — Three Domains | `01-problem-space/03-two-lenses.md`, `00-front-matter/02-running-example.md` |
| 14 — Value Realized | `01-problem-space/03-two-lenses.md`, `04-esp-playbook/01-esp-wide-concerns.md` |
| 15 — Systems and Bounded Contexts | `02-ontology/02-account-product-virtual-card-product.md`, `03-bank-foundation/01-account-card-products.md`, `04-esp-playbook/01-esp-wide-concerns.md`, `05-corporate-playbook/01-corporate-wide-concerns.md` |
| 16 — Context Boundaries | `03-bank-foundation/03-processing-authorization-controls.md`, `04-esp-playbook/01-esp-wide-concerns.md` |
| 17 — Bank Domain Entities | `02-ontology/02-account-product-virtual-card-product.md`, `03-bank-foundation/01-account-card-products.md` |
| 18 — ESP Domain Entities | `02-ontology/03-esp-variants-corporate-payment-product.md`, `04-esp-playbook/01-esp-wide-concerns.md` |
| 19 — Corporate Domain Entities | `02-ontology/01-corporate-legal-entity-ou-members.md`, `05-corporate-playbook/01-corporate-wide-concerns.md` |
| 20 — Entity Relationships | `02-ontology/03-esp-variants-corporate-payment-product.md`, `02-ontology/05-corporate-payment-program.md` |
| 21 — Hierarchies (Corporate View) | `02-ontology/04-credit-facility-budget-account.md`, `05-corporate-playbook/01-corporate-wide-concerns.md` |
| 22 — Hierarchies (Bank View) | `03-bank-foundation/03-processing-authorization-controls.md`, `02-ontology/04-credit-facility-budget-account.md` |
| 23 — Program Reflection | `02-ontology/05-corporate-payment-program.md`, `02-ontology/04-credit-facility-budget-account.md` |
| 24 — Policy Cascade | `02-ontology/07-spend-policy-controls.md`, `03-bank-foundation/03-processing-authorization-controls.md` |
| 25 — Authorization Flow | `03-bank-foundation/03-processing-authorization-controls.md` |
| 26 — Transaction Posting | `02-ontology/11-transaction-posting-data.md` |
| 27 — Comprehensive Manifestation | `02-ontology/11-transaction-posting-data.md`, `03-bank-foundation/03-processing-authorization-controls.md`, `02-ontology/08-booking-settlement-profile.md` |
| 28 — Lifecycle Overview | `05-corporate-playbook/02-supplier-payments-program.md`, `03-bank-foundation/02-onboarding.md` |
| 29 — Setup Phase | `03-bank-foundation/02-onboarding.md`, `02-ontology/10-members-eligibility-enrollment.md` |
| 30 — Operational Phase | `03-bank-foundation/03-processing-authorization-controls.md`, `05-corporate-playbook/01-corporate-wide-concerns.md` |
| 31 — Financial Phase | `02-ontology/08-booking-settlement-profile.md`, `05-corporate-playbook/02-supplier-payments-program.md` |
| 32 — Embedding and Extension | `03-bank-foundation/03-processing-authorization-controls.md`, `05-corporate-playbook/02-supplier-payments-program.md` |
| 33 — Meridian End-to-End | `00-front-matter/02-running-example.md`, `05-corporate-playbook/01-corporate-wide-concerns.md` |
| 34 — Next Steps | N/A |
