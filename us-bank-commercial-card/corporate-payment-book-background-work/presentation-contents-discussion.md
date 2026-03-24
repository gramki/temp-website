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

### Slide 1: Possibilities vs Needs

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

**Headline:** The vision of corporate payments is compelling. The platform wasn’t built for it.

**Key Talking Points:**
- This is not a vendor critique — it is an architectural observation. Validate the vision: the bank sees the opportunity clearly. The gap is not in ambition or strategy — it is in the platform beneath the strategy.
- The card processing platforms behind most bank programs today (TSYS, Fiserv, FIS) carry architectural patterns that reflect the constraints of the era and use cases they were designed for. These patterns are embedded at the foundation level.
- The vision banks describe to corporates is real — but it is constrained by infrastructure that was not designed for corporate spend governance. The platform doesn’t prevent the bank from articulating the vision, but it constrains how far the vision can actually be delivered.
- Frame this as market structure, not blame. The bank chose a processor for good reasons. The processor was designed for its original purpose. Neither is at fault — but the constraint is real, and it shapes what “evolution” actually requires.

**Supporting Detail:**
- Slide 7 (“The Challenge of the Promise”) provides the specifics — seven constraints that define the captivity. This slide plants the seed; Slide 7 delivers the evidence after the audience understands the corporate’s needs.
- Avoid naming vendors on screen. The audience will map the constraints to their own platform. If they ask, acknowledge the examples in conversation — but the slide should remain vendor-neutral.
- This provocation works because the audience (bank product and technology leaders) have lived with these constraints. They will recognize them immediately.

**Suggested Visuals:**
- Single headline statement, large type, centered.
- The two sentences should feel like a pause — the first affirms, the second lands.

**What to Avoid:**
- Do not list features or vendor names on this slide.
- Do not apologize for the observation. State it as fact.
- Do not frame this as “your platform is bad.” Frame it as “the platform was built for something else.”
- Do not diminish the vision. The first sentence must land as genuine validation.

**Source Reference:** Presentation-originated. See `book-writing-backlog.md` item #17 and the “Legacy Platform Constraints — Detailed Reference” section at the end of this document.

---

### Slide 3: The Semantic Dissonance

**Headline:** When corporates ask questions and banks answer with card capabilities, both sides are speaking accurately — from different frames.

**Key Talking Points:**
- Present the dissonance as a two-column table: Corporate’s Question / Bank’s Answer. No “Gap” column — the dissonance is self-evident from reading the pairs side by side. Let the audience draw the conclusion.
- Walk through each row:
  1. **Supplier specification:** The corporate asks about procurement policy (“encourage local procurement, specify my suppliers”). The bank asks for MIDs and TIDs — network-level identifiers the corporate doesn’t think in.
  2. **Approval workflows:** The corporate asks about governance workflows (“maker and checker for high-value spends”). The bank offers a card-per-transaction workaround that doesn’t distinguish between spend types — an invoice payment and a travel expense look the same.
  3. **Multi-dimensional policy:** The corporate needs three intersecting dimensions evaluated at authorization (“project budget, employee location, career level”). The bank offers one dimension: per-card limits.
  4. **Multi-region budget governance:** The corporate needs a shared, floating budget pool across currencies with regional caps. The bank offers financial risk sub-limits with no organizational budget semantics.
- The pattern: the corporate asks about business rules, organizational context, and operational workflows. The bank answers with card-level primitives — limits, identifiers, individual cards. Neither side is wrong. They are organizing around different concerns.
- Don’t rush through this slide. Let each row land. The audience should feel the accumulation — row after row, the same structural shape.

**Supporting Detail:**
- These Q&A pairs are drawn from real corporate-bank conversations, not fabricated examples. The audience will recognize them.
- Each row maps to a dimension that will be named explicitly in Slide 4 (Five Dimensions): supplier specification → Control Architecture; approval workflows → Control Architecture; multi-dimensional policy → Control Architecture + Financial Architecture; multi-region budget → Financial Architecture.
- The dissonance is not about missing features. It is about different organizing principles: the corporate organizes around business rules and organizational structure; the bank organizes around payment instruments and financial risk controls.

**Suggested Visuals:**
- Two-column table: Corporate’s Question / Bank’s Answer. Clean, readable, no clutter.
- Animate rows sequentially if the medium supports it — let the pattern build.
- The absence of a “Gap” column is deliberate — the audience fills in the gap themselves, which makes it land harder.

**What to Avoid:**
- Don’t reduce this to “banks are doing it wrong” — both sides are speaking accurately; the problem is structural, not intentional.
- Don’t let the audience dismiss individual rows as “edge cases” — the accumulation is the point.
- Don’t present the table without narrating it — each row needs a beat to land.
- Don’t add a “Gap” column. The dissonance is more powerful when the audience names it themselves.

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

**Headline:** The five dimensions do not present uniformly. They vary by the type of counterparty the corporate pays — and the AP landscape has at least seven distinct shapes.

**Key Talking Points:**
- Name the counterparty types: goods suppliers, service providers, employees, contractors, SaaS/software vendors, intermediaries/agencies, government/regulatory bodies.
- Employees are a distinct counterparty type — they spend against reimbursable expenses or pre-approved budgets, and the actual merchant where the transaction happens is not a direct party to the corporate's governance of the spend.
- Each type has different payment patterns, data needs, compliance requirements, and card acceptance realities.
- Today's card products abstract all of these as "merchants" — a single MCC-classified entity. The corporate sees seven fundamentally different relationships.
- This diversity multiplies the five dimensions: financial architecture for a goods supplier (PO-locked budget) looks nothing like financial architecture for a SaaS vendor (contract-locked renewal budget).
- Don't go deep here — name the diversity, let it land, and note that the archetype discussion in the next act addresses it directly.

**Supporting Detail:**
- Counterparty table: Type / Payment Pattern / Data Needs / Compliance / Card Acceptance — seven rows showing the variety
- Specific contrasts to make it concrete:
  - Goods supplier: PO-driven, deterministic, L2/L3 critical, high card acceptance
  - Employee: reimbursable or budget-based, merchant is not a direct party, expense policy and delegation of authority govern
  - Contractor: time-based, project-coded, 1099 compliance, low card acceptance (ACH preferred)
  - Government: fee-schedule, non-negotiable, regulatory deadlines, often requires wire/ACH
- The merchant abstraction is not wrong — it is insufficient. MCCs describe what the merchant sells, not how the corporate governs payments to them.

**Suggested Visuals:**
- Seven-row table: Counterparty Type / Payment Pattern / Data Needs / Compliance / Card Acceptance
- Or a visual showing one "merchant" icon being unpacked into six distinct relationship types — illustrating the abstraction collapse
- Or a matrix: five dimensions (columns) × seven counterparty types (rows), with cells indicating how each dimension manifests differently per type

**What to Avoid:**
- Don't go too deep into any single counterparty type — the archetype discussion handles that
- Don't present this as an exhaustive taxonomy — say "at least six" to signal that more may exist
- Don't dismiss low-card-acceptance counterparties (contractors, government) — their existence in the corporate's AP landscape is part of the problem, even if card programs don't serve them directly

**Source Reference:** Presentation-originated concept — see `book-writing-backlog.md` item #16. Draws on archetype concepts from `01-problem-space/04-spend-archetypes.md`.

---

### Slide 6: The Two-Lens Gap — Hierarchy Is Not the Answer

**Headline:** The bank's control model is a hierarchy of limits — credit facility, account, card, evaluated along a single path. The corporate's is a coordinate system of concurrent dimensions — budget, policy, authority, attribution, purpose, validity — all evaluated simultaneously. Both are sound. A hierarchy forces a fixed nesting: does Department contain Project, or Project contain Department? Every corporate answers differently — and the answer changes when they restructure. The dimensions cannot be nested. They must remain independent. Hierarchy is not the answer.

**Key Talking Points:**
- Bank's organizing principle: credit facility → account → card → MCC/amount/velocity controls → interchange → lifecycle
- Corporate's organizing principle: department → project → cost center → budget/policy/approval → GL/project/client codes → reconciliation → DPO
- The structural mismatches: org structure ≠ account structure; budget ≠ credit limit; GL fields ≠ transaction data; workflow ≠ card controls; reconciliation ≠ data availability
- This is not a criticism — banks optimize for credit risk, regulatory compliance, network settlement, and treasury income (float, interchange, facility interest) because they must. Corporates optimize for operational governance, financial attribution, audit readiness, and payment cost and process efficiency because they must. The hierarchy is sound for credit risk. It is not the answer for corporate governance.
- Why hierarchy fails structurally:
  - A hierarchy requires a fixed ordering of dimensions. Corporate governance dimensions are enterprise-specific — Company A organizes by region → business unit → project; Company B by department → client → cost center. No universal ordering exists.
  - The dimensions are not static. Enterprises restructure, add regulatory dimensions, shift from project-based to product-based models. Each change would require rebuilding the hierarchy — not reconfiguring it.
  - Different governance questions within the same enterprise require different traversal orders simultaneously. "What did Department X spend across all projects?" and "What did Project Alpha cost across all departments?" need different primary axes. A hierarchy answers one efficiently. A coordinate system answers all — because the dimensions are independent.
- The gap is architectural — not a missing feature, not a configuration oversight. It requires a design that keeps the bank's hierarchy for credit risk and supports the corporate's coordinate system for governance — without collapsing one into the other.

**Supporting Detail:**
- Why the dissonance is structural (not accidental):
  - Banks are regulated entities; their data models reflect prudential requirements (credit exposure, capital adequacy, AML/sanctions)
  - Corporates are operational entities; their data models reflect management requirements (budgets, projects, cost centers, GL)
  - Neither can adopt the other's model without violating its own obligations
- Result: even with one issuer, a corporate like Meridian ends up with four parallel programs, separate onboarding, controls, reconciliation streams, portals, and contacts
- Finance cannot see total exposure without manual aggregation; policy changes need four configuration passes
- The hierarchy argument in detail:
  - A hierarchy forces an axis ordering: if the hierarchy is Region → Department → Project, then querying "all spend for Project Alpha across all departments" requires a full scan. A coordinate system of independent dimensions answers all traversal orders without structural bias.
  - No single hierarchy can accommodate two enterprises simultaneously — each enterprise's dimension order reflects its own governance structure, and that structure changes when the enterprise restructures.
  - Reference: the full structural analysis is in *Why Hierarchy Is Not the Answer*.

**Suggested Visuals:**
- Split visual: left side shows a tree (credit facility → account → card → limit) labeled "Hierarchy of Limits — single path"; right side shows a multi-axis grid (budget × policy × authority × attribution) labeled "Coordinate System — concurrent dimensions"
- Below the split: a concrete example — "Does Department contain Project, or Project contain Department?" with two enterprise structures shown side by side, each with a different nesting order
- Gap zone in the middle showing the mismatches (org ≠ account, budget ≠ credit limit, GL ≠ txn data, workflow ≠ card controls)

**What to Avoid:**
- Don't position this as "banks are doing it wrong" — the hierarchy is sound for credit risk; name it as structurally insufficient for corporate governance
- Don't promise to eliminate the gap entirely — promise to make it manageable through clean separation of concerns
- Don't blame either side — the point is that both are right, and the architecture must honor both
- Don't rush the "hierarchy is not the answer" moment — this is the cognitive pivot of Act 1; let the audience absorb the shift from "we need deeper hierarchy" to "we need independent dimensions"

**Source Reference:** `01-problem-space/03-two-lenses.md`, `01-problem-space/02-existing-solutions.md`, `why-hierarchy-is-not-the-answer.md`

---

### Slide 7: The Promise Is Captive to the Platform

**Headline:** The compelling possibility of automated corporate payments is captive to the platform that delivers it.

**Key Talking Points:**
- Open with the callback to Slide 2: “We said the platform wasn’t built for it. Now that you’ve seen what the corporate actually needs — five dimensions, seven counterparty types, a coordinate system of concurrent dimensions — here’s specifically what that captivity looks like.”
- Walk through each of the seven constraints. Each now maps to something the audience has just learned — the constraints aren’t abstract anymore:
- **Batch-native:** Real-time authorization events, lifecycle notifications, and cooperative callbacks require middleware the platform wasn’t designed for. Ask: “When was the last time your processor pushed an authorization event in real time without middleware?”
- **Rigid hierarchies:** The platform evaluates a hierarchy of limits along a single path; it cannot evaluate the corporate's coordinate system of concurrent dimensions — no multi-segment budgets, no category-dependent policy cascade, no concurrent dimensional enforcement at authorization. Ask: “We just said the corporate operates in a coordinate system of concurrent dimensions. Can your processor enforce budget, policy, and attribution across those dimensions simultaneously at authorization — or does it evaluate one path down a limit hierarchy?”
- **Limiting data structures:** Rigid data fields that cannot carry corporate context through the transaction lifecycle. Refunds and credits not attributed back to original booking profile. No clearing enrichment hooks. Ask: “Can you attach a PO number to a card at issuance and have it travel through authorization, clearing, and settlement? When a refund arrives, does it attribute back to the original booking?”
- **Closed authorization:** The processor evaluates the transaction and decides alone. There is no hook for ESP or corporate participation within network-mandated timeouts. No posting enrichment at clearing. Ask: “Can your corporate client participate in the authorization decision before the processor responds to the network?”
- **Lack of token awareness:** Token lifecycle not coordinated with card lifecycle across renewals and replacements. Authentication limited across CNP/CP scenarios. PIN delivery confined to legacy channels. FRM has credential lifecycle blind spots. Ask: “When a virtual card is renewed, do the tokens migrate automatically? Does your FRM system see the full credential lifecycle — or just the card?”
- **Throughput constraints:** Not designed for high-frequency, API-triggered, single-use issuance at scale. Card lifecycle operations (suspend, reactivate, close, replace) designed for call-center workflows, not programmatic bulk operations. Ask: “How many single-use cards can your processor issue per minute via API? What happens to lifecycle operations at scale?”
- **Inaccessible for extension:** No event subscriptions, no webhook-driven integration, no API-driven lifecycle customization. The platform is closed to the ecosystem that needs to build on it. Ask: “Can your ESP subscribe to card events in real time? Can a corporate system trigger a lifecycle operation via API?”

**Supporting Detail:**
- Each constraint maps directly to a capability the corporate will eventually need. After seeing Slides 3–6, the audience understands *why* each matters.
- These are not feature gaps. They are architectural characteristics. A feature gap can be patched; an architectural characteristic requires a purpose-built alternative.
- The callback to Slide 2 is essential — it closes the loop the audience has been holding open since the second provocation. The payoff arrives after the problem is fully understood, making the constraints land harder.
- See the “Legacy Platform Constraints — Detailed Reference” section at the end of this document for the full catalog of eight constraint categories with detailed examples.

**Suggested Visuals:**
- Seven-row table, two columns: “Constraint” and “What It Means.” Clean, readable, no clutter.
- Consider progressive reveal (one row at a time) to let each constraint land before moving to the next.
- Optional: a subtle visual connection back to Slide 2 — same color palette or motif to signal the callback.

**What to Avoid:**
- Do not present this as a feature comparison chart. It is an architectural observation, not a competitive matrix.
- Do not rush through the table. Each row is a self-contained argument.
- Do not name specific vendors in the table. The patterns are universal.
- Do not skip the callback to Slide 2. Without it, the slide loses its structural role.

**Source Reference:** Presentation-originated. See `book-writing-backlog.md` item #17. Full constraint catalog in “Legacy Platform Constraints — Detailed Reference” section below.

---

### Slide 8: The Foundation and The Bridge

**Headline:** This is what we set out to solve. The foundation: a processing platform purpose-built for corporate spend governance — one that resolves the constraints we just identified, and is architected for the possibilities of this decade. The bridge: an architecture that answers the corporate's actual questions across all five dimensions, across all counterparty types, while preserving the bank's risk and compliance model.

**Key Talking Points:**
- The foundation: a payment platform that is event-native, hierarchy-aware, contextually rich, on-demand, cooperatively authorized, token-aware, throughput-ready, and extensible — the inverse of every constraint identified in Slide 7. Without the right foundation, the bridge cannot hold.
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
- Or a three-icon layout (Bank / ESP / Corporate) with one sentence under each: "Risk, Compliance, and Treasury Income" / "Translation and Packaging" / "Governance and Operations" — with a foundation bar underneath showing "Event-native | Hierarchy-aware | Contextual | On-demand | Cooperative"
- Transition arrow pointing to "Act 2: The Framework"

**What to Avoid:**
- Don't turn this into a product pitch — keep it architectural
- Don't go deep on the three-domain model here — that's Slide 12
- Don't list features — list design principles
- Don't linger — this slide should create momentum into the next act
- Don't collapse the foundation and the bridge into one idea — they are distinct. One is about infrastructure, the other is about domain design

**Source Reference:** `01-problem-space/03-two-lenses.md`. Bridge framing originated in presentation discussions — see `book-writing-backlog.md` items #13-15, #17.

---

## Act 2 — The Framework

---

### Slide 9: Spend Archetypes

**Headline:** Corporate payments organize into Spend Archetypes — each with a distinct control model, card lifecycle, enrollment pattern, and reconciliation approach.

**Key Talking Points:**
- Archetypes are the organizing principle — not product names, not market segments
- Archetypes include: Supplier Payments, Employee & Department Spend, Travel & Booking Payments, Central Recurring Merchant Payments — and are extensible as new corporate spend patterns emerge
- "Embedded" (API-triggered issuance) is a delivery mechanism, not an archetype — it can serve any archetype
- Walk through each archetype's distinguishing characteristics: card lifecycle (single-use vs persistent vs lodge), enrollment model (supplier = enroll the payee; employee = enroll the payer), data richness (L2/L3 vs minimal), and reconciliation approach (PO match, expense report, itinerary match, contract match)

**Supporting Detail:**
- Supplier: single-use per invoice, merchant-locked, PO-linked, ERP reconciliation via L2/L3 three-way match; ERP triggers card issuance for approved PO; auto-closed after clearing; reconciliation target: 95%+ auto-match
- Employee: persistent cards, MCC/velocity limits, per-employee enrollment, expense report reconciliation; manager or self-enrollment; MCC allowlists (e.g., AMC-IT-Services, AMC-Cloud, AMC-SaaS); expense management system receives transaction data
- Travel: lodge card (long-lived, shared with agency) or per-booking virtual card; booking system triggers issuance; itinerary data for reconciliation
- Recurring: one card per merchant/contract, renewal-aligned lifecycle, centrally administered; subscription management as the trigger
- Meridian examples: ~200 suppliers with API-issued cards; 120 engineering employees with $2,500 per-tx limits; travel desk with lodge card; 35 SaaS subscriptions with dedicated locked cards

**Suggested Visuals:**
- Comparison table: Archetype × (Control Model / Card Lifecycle / Enrollment / Reconciliation) — four columns, four rows
- Or the book's `graph TB` Mermaid diagram with four subgraphs
- Four mini-diagrams showing card lifecycle for each archetype (Issue → Auth → Clear → Close vs Issue → Auth → Auth → ... → Renew)

**What to Avoid:**
- Don't mix archetype descriptions with product feature lists
- Don't use the term "Spend Lane" — the book uses "Spend Archetype" consistently
- Don't imply archetypes are rigid categories — they are workflow patterns that products are built around
- Don't state a fixed count of archetypes — they are extensible

**Source Reference:** `01-problem-space/04-spend-archetypes.md`, `02-ontology/10-members-eligibility-enrollment.md`

---

### Slide 10: Spend Mandates — The Authorization Envelope

**Headline:** Every corporate payment must answer a chain of questions: Why was this allowed? Who authorized it? Whose budget? Which rules? How is it booked? Who is accountable? The Spend Mandate is the framework that holds those answers.

**Key Talking Points:**
- Introduce the concept through the chain of questions — these are the governance requirements that every corporate payment must satisfy. The Spend Mandate makes them explicit.
- The Spend Mandate is a thinking tool, not a single database entity — it is a framework for reasoning about governance requirements that distribute across multiple system entities
- Components: Purpose, Authority, Budget Source, Policy Scope, Limits, Attribution, Validity, Exceptions
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

### Slide 11: Governance: Constraints and Decisions

**Headline:** Governance is not enforcement alone. It requires constraints that the platform enforces automatically, and decisions — structured and unstructured.

**Key Talking Points:**
- Constraints: evaluated at authorization in real time — budget capacity, spend policy, limits. The bank checks these on every transaction. No exception. Constraints gate the transaction: the system asks "Is this allowed?" and decides autonomously.
- Structured Decisions: resolved before or after authorization through rules and configuration — purpose, participants, attribution, validity. These shape the context in which the transaction occurs: who is enrolled, which program, how spend is attributed, when the channel is active.
- Unstructured Decisions: require human deliberation — authority escalation, exception handling. The platform provides deliberation control: workflows, approval chains, escalation paths, post-facto justification.
- The design challenge: enforce constraints automatically, enforce structured decision rules through configuration, and provide deliberation control for unstructured decisions.

**Supporting Detail:**
- The salient distinction: Constraints are real-time, non-negotiable, and autonomous — the system evaluates them at authorization with no human in the loop. Structured decisions are rule-based but operate at different timescales — enrollment, configuration, posting, reconciliation — shaping what the constraint engine evaluates against. Unstructured decisions are the residual: situations where rules don't cover the case, authority is ambiguous, or the situation is novel.
- Constraints at authorization: Budget hierarchy check (all ancestors), AMC/MCC match, per-tx and velocity limits, currency/geography restrictions, single-use enforcement
- Structured decisions through configuration: program membership controls who is eligible and enrolled; booking profiles control how spend is attributed at posting; validity windows control when the program is active; purpose determines which program a card belongs to
- Unstructured decisions through deliberation control: eligibility approval workflows when authority is contested or delegated; exception escalation chains; post-facto justification requirements for out-of-bounds spend
- A platform that only enforces constraints can say "no" but cannot explain why the spend channel exists, who should have access, or where the spend goes. A platform that only supports structured decisions cannot prevent a single unauthorized transaction in real time. Both must coexist.

**Suggested Visuals:**
- Three-section layout: "Constraints — Real-time at authorization" / "Structured Decisions — Configuration-enforced" / "Unstructured Decisions — Deliberation-controlled"
- Or the book's Mermaid `graph TB` showing components split into three subgraphs feeding Authorization, Configuration, and Deliberation

**What to Avoid:**
- Don't collapse structured and unstructured decisions into one category — the distinction is architecturally significant
- Don't frame unstructured decisions as "things we can't enforce" — frame them as decisions requiring human judgment, with the platform providing the control framework
- Don't use "auditable but not enforceable" — the earlier framing that was deliberately revised

**Source Reference:** `01-problem-space/05-spend-mandates.md` (reframed "Two Natures of Governance" section)

---

### Slide 12: The Three Domains

**Headline:** The bank organizes around risk and treasury income. The corporate organizes around governance and payment cost reduction. Neither can collapse into the other. The ESP exists to translate between them.

**Key Talking Points:**
- Three domains, each with a clear role: Bank underwrites risk, authorizes, enforces compliance, settles. ESP translates bank capabilities into corporate solutions — product design, onboarding, billing, operating layer. Corporate configures programs, defines budgets and policies, enrolls members, operates day-to-day governance.
- The architecture enforces clean separation through four principles — present these as the design answer, not an observation:
  - **Own vocabulary** — each domain operates in its native semantics
  - **Own control** — each domain governs its own decisions
  - **Own pace** — each domain evolves independently
  - **Own scope** — banking stays within the regulatory perimeter; corporate stays outside it
- Separation does not mean isolation. The full control matrix is present at every authorization — through structured entities, anti-corruption translation, and cooperative authorization. Designing the mechanisms that achieve this under the constraints of network speed, security, and regulation is the platform's core architectural value.

**Supporting Detail:**
- Why three domains: banks optimize for credit risk, regulatory compliance, network settlement, and treasury income — while corporates optimize for operational governance, financial attribution, audit readiness, and payment cost and process efficiency. These are structurally different organizing principles. Attempting to serve both from one domain model forces one side to adopt the other's vocabulary, violating its own obligations.
- The bank does not see departments, cost centers, or project codes — that's corporate domain knowledge. The corporate does not touch underwriting, credit assessment, or network settlement — that's bank domain knowledge. The ESP mediates without owning either worldview.
- Platform mapping: Commonwealth on Tachyon; Apex on Electron; Meridian on Electron (corporate portal)
- The three integration mechanisms that make separation work:
  - **Structured entities** flatten multi-level governance into computable authorization context: budget hierarchies with ancestor-chain enforcement, tighten-only policy cascades, booking profiles that carry attribution rules — all pre-configured so the effective control envelope is resolvable at authorization speed
  - **Anti-corruption translation** keeps integration idiomatically native to each domain: the bank sees accounts and facilities, the corporate sees programs and budgets, and the gateway translates without either side adopting the other's model
  - **Cooperative authorization** extends the authorization context on demand: ESP and corporate systems contribute data or decisions within network timeouts, without owning the final decision
- The core architectural value: designing the right combination of data structures, algorithms, and processes that meet technical constraints (network-speed authorization), security constraints (non-overridable controls), and regulatory constraints (AML, sanctions, compliance) simultaneously — while keeping each domain idiomatically native
- Reference the detailed analysis in *Why Hierarchy Is Not the Answer* (Sections 7–8) for the full treatment of these mechanisms

**Suggested Visuals:**
- Three-domain horizontal layout: Bank (Tachyon) → ESP (Electron) → Corporate (Electron Portal) with the "four owns" as a design principle overlay
- Or the book's `graph LR` three-domain diagram
- Consider a second visual showing the three integration mechanisms (structured entities, anti-corruption translation, cooperative authorization) as connective tissue between the three separated domains

**What to Avoid:**
- Don't present the "four owns" as a matter of fact — present them as the architecture's design answer to the problem from Slide 6
- Don't let separation read as silos — the integration counterpoint must land in the same breath
- Don't imply the ESP is optional or just a reseller — the ESP adds substantial product design and operational value
- Don't blur domain boundaries — the clean separation is the central architectural argument

**Source Reference:** `01-problem-space/03-two-lenses.md` (domain comparison table), `00-front-matter/02-running-example.md`, `why-hierarchy-is-not-the-answer.md` (Sections 7–8)

---

### Slide 13: The Economics of Separation

**Headline:** The framework enables a partnership model. The bank provides BaaS. The ESP owns product design and corporate engagement. The corporate — their shared client — contributes and captures value within this model.

**Key Talking Points:**
- Name the transition explicitly: Slide 12 established the three domains as an architectural design. This slide shows they are also a business model. The bank and ESP are distinct provider roles; the corporate is their shared client.
- A bank can play the ESP role. But each spend archetype, for each segment of corporate clients, demands distinct engagement expertise — product design, onboarding, support, billing. What a bank cannot or chooses not to focus on, a partner can own. The bank provides Banking-as-a-Service; the partner operates as the ESP (Enterprise Service Provider). The corporate operates programs and drives the economics for both.
- Present the table with stakeholders as rows, "Value Added" and "Value Realized" as columns — the symmetry between contribution and capture is the point
- Bank: adds Credit Facilities, authorization, compliance, settlement; realizes float, retention, interchange, fees
- ESP: adds product design, onboarding, billing, operational layer; realizes revenue share, corporate fees, portfolio scale
- Corporate (the client): adds payment volume, payer-side ecosystem expansion, program configuration, budget/policy, enrollment, governance; realizes spend governance and policy enforcement, AP process automation, rebates, DPO extension, reconciliation labor reduction
- Members: add payee-side ecosystem expansion, transaction volume, sales/invoice data; realize cashflow improvement, expense simplification, travel convenience
- The economics work because the separation works. The bank earns from infrastructure. The ESP earns from engagement depth. The corporate gains governance capabilities neither could deliver alone.

**Supporting Detail:**
- Why the ESP is a distinct business, not a bank department: each archetype × corporate segment combination demands specialized engagement expertise. An ESP that concentrates on specific combinations develops deeper expertise than a bank product team serving all combinations across all corporates — and amortizes that expertise across a portfolio (40+ corporates).
- The bank's business model: BaaS provider. Commonwealth earns from the facility (interest/float), the account (fees), and the network (interchange) — regardless of which ESP packages the product. Multiple ESPs can operate as VBOs on the same bank platform.
- The ESP's business model: product and engagement business. Apex earns product-level rebate of 1.5% on supplier pay interchange; relationship-level rebate of 50 bps on aggregate spend > $10M/quarter; plus direct fees from corporates.
- The corporate's perspective: Meridian's CFO evaluates on reconciliation labor saved, DPO extension, and policy leakage prevention — not interchange. The corporate is the client, not a co-equal business entity.
- Address the unspoken bank question: "Why can't we just do this ourselves?" Answer: you can. But the depth of engagement expertise per archetype × segment makes specialization commercially rational. What you choose not to focus on, a partner can own — and you earn from it as the BaaS provider.
- Market evidence: the model already exists. Brex (on Sutton Bank / Column), Ramp (on Celtic Bank), Divvy/BILL (on Cross River Bank), Navan (travel-focused, on various issuers) — each operates as an ESP on a bank's BaaS infrastructure. The pattern is proven. The question is whether the bank captures value as the BaaS provider or loses the corporate relationship to an ESP building on someone else's platform. Do not put competitor names on the slide — use them in conversation when challenged.

**Suggested Visuals:**
- Single table: Stakeholder / Value Added / Value Realized — four rows, two value columns
- Or a value flow diagram showing how interchange, float, fees, and rebates distribute across the bank (BaaS provider) and ESP (product business), with the corporate as the client driving economics for both

**What to Avoid:**
- Don't treat the corporate as a co-equal business entity — it is the client, not a partner in the supply chain
- Don't make this slide feel like a revenue pitch for the ESP — frame it as a rational business model where the bank earns from BaaS and the ESP earns from engagement
- Don't use exact interchange percentages as if they are universal — they vary by network, region, and merchant
- Don't omit Members — their value is real and often overlooked in bank-focused presentations

**Source Reference:** `01-problem-space/03-two-lenses.md`, `04-esp-playbook/01-esp-wide-concerns.md`

---

## Act 3 — The System Design

---

### Slide 14: Systems and Bounded Contexts

**Headline:** Each domain operates through purpose-built systems.

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

### Slide 15: Context Boundaries and Integration Points

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
- Bank ↔ Corporate (mediated through ESP): CF utilization and budget enforcement at auth (bank checks budget hierarchy via Payments Switch/Hub), posting data flow (L1/L2/L3), regulatory/fraud notifications from FRM and Notification subsystems (non-suppressible), standing repayment instructions (auto-debit from designated settlement accounts), settlement account registration and management
- Corporate Portal ↔ Corporate Systems: all the integration touchpoints listed in Slide 14

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

---

### Slide 16: Entity Model Across Domains

**Headline:** The entities across all three domains and how they relate.

**Key Talking Points:**
- Present the three-domain ER diagram showing all entities and their cross-domain relationships
- Bank Domain (Tachyon): Account Holder (LAH/RAH/HAH), Credit Facility, Limit Hierarchy, Account Product, Virtual Card Product, VBO, Account, Virtual Card, Token, Spend Policy (bank-enforced)
- ESP Domain (Electron): ESP (registered as VBO), Account Variant, Virtual Card Variant, Corporate Payment Product, Client Contract
- Corporate Domain (Electron Portal): OU, Corporate Payment Program, Budget Hierarchy, Spend Policy (corporate-defined), Booking Profile, Settlement Profile, Settlement Account, Member, Enrollment
- Key cross-domain mappings: Budget Hierarchy optionally translates to Limit Hierarchy; corporate Spend Policy maps to bank-enforced Spend Policy; ESP registered as VBO

**Supporting Detail:**
- Budget Hierarchy is hierarchical (mirroring Limit Hierarchy in Bank Domain); budgets are made accessible to OUs; a Program can only draw from budgets of the OU it is associated with
- Spend Policy cascade: program-level applies to all enrollments; enrollment-level translates to per-Virtual Card (and per-Token) Spend Policies in Bank Domain
- A Limit Hierarchy need not originate from a Credit Facility
- Virtual Card linked to Account at creation (not issued by); Virtual Card can have multiple Tokens
- Entity reference tables available in Appendix for detailed lookup

**Suggested Visuals:**
- Three-domain ER diagram with subgraphs for Bank, ESP, Corporate — see `3-domain-erd.md` for the Mermaid source
- Cross-domain arrows should be visually distinct (dashed) from within-domain relationships

**What to Avoid:**
- Don't try to fit all entity details on the slide — the ER diagram shows structure and relationships; the Appendix tables provide detail
- Don't confuse Product with Variant — the bank creates Products; the ESP creates Variants
- Don't conflate OU with Legal Entity — they are distinct (OU is organizational, LE is legal/credit)

**Source Reference:** `02-ontology/02-account-product-virtual-card-product.md`, `02-ontology/01-corporate-legal-entity-ou-members.md`, `03-bank-foundation/01-account-card-products.md`, `04-esp-playbook/01-esp-wide-concerns.md`, `05-corporate-playbook/01-corporate-wide-concerns.md`, `3-domain-erd.md`

---

### Slide 17: The Derivation Chain

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

### Slide 18: Hierarchies — Corporate's and ESP's View

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

### Slide 19: Hierarchies — Bank's View

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
- Contrast with the corporate's three-hierarchy view from Slide 18
- Gray out what the bank doesn't see (OUs, cost centers, GL codes) to visually reinforce the separation

**What to Avoid:**
- Don't make the bank's limited view sound like a weakness — frame it as intentional separation of concerns
- Don't suggest the bank ignores budgets — it enforces them; it just doesn't define them

**Source Reference:** `03-bank-foundation/03-processing-authorization-controls.md`, `02-ontology/04-credit-facility-budget-account.md`

---

## Act 4 — Program Lifecycle and Extensibility

---

### Slide 20: Large-Scale Virtual Card Program Lifecycle — Overview

**Headline:** The lifecycle spans contracting, corporate account configuration, program setup, operations, and financial management — each phase involves distinct actors and system interactions.

**Key Talking Points:**
- 32 lifecycle steps across five phases — from Client Contract to dispute resolution
- Five phases: Contracting & Onboarding (ESP-driven), Corporate Account Configuration (Corporate Admin-driven), Program Setup (Corporate Admin-driven), Operations (transaction-driven, concurrent), Financial (cycle-driven)
- Each phase involves different actors (ESP, bank, corporate admin) and different bounded contexts
- The lifecycle is the same across archetypes — what changes is the archetype-specific behavior within each step

**Supporting Detail:**
- **Contracting & Onboarding** (steps 1-9, primary systems: Electron + Tachyon):
  - ESP initiates Client Contract (Electron) → Legal Entities added → underwriting info collected → CF applications submitted per LAH (Electron → Tachyon) → bank underwrites and issues CFs (Tachyon) → bank notifies LAH billing contacts (Tachyon) → ESP assigns CPPs across Spend Archetypes (Electron) → ESP configures Rebates and Volume Commitments (Electron) → ESP provisions corporate portal access credentials (Electron)
- **Corporate Account Configuration** (steps 10-14, primary system: Electron Portal + corporate integrations):
  - Admin configures account, users, OUs (Electron Portal) → member provisioning via AD, SAP, SCIM, SFTP, API (Electron Portal ↔ corporate systems) → budgets created against CFs and distributed across OUs; ERP-defined budgets imported; budget hierarchy independent of CF hierarchy (Electron Portal ↔ ERP) → Payable Accounts configured — multiple accounts at various banks registered for invoices and repayments, each mapped to a GL in ERP (Electron Portal) → ongoing master data maintenance via API/SFTP
- **Program Setup** (steps 15-23, primary systems: Electron Portal + Tachyon):
  - Admin initiates Program for a specific Spend Archetype, selecting a CPP offered by ESP for that archetype; links to CF, assigns to OU (Electron Portal) → Spend Programs configured at program level with Purchase Categories and controls (Electron Portal) → Booking Profile configured (Electron Portal) → Settlement Profile linked to registered Payable Account (Electron Portal) → eligibility rules defined (Electron Portal) → members enrolled via API (ERP/enterprise integration) or SFTP (Electron Portal) → enrollment triggers virtual card issuance — card returned immediately, dispatched digitally (secured email), or physically depending on archetype; card carries tags (PO, invoice, cost center, project code) set at enrollment (Electron Portal → Tachyon) → enrollment-level Spend Programs configured with member-specific controls (e.g., exact amount for supplier cards) (Electron Portal) → card dispatch notification sent to member with relevant context (e.g., supplier receives PO number, invoice number, authorized amount)
- **Operations** (steps 24-28, primary systems: Tachyon → Electron → Corporate):
  - Auth with callbacks → Corporate Portal reflects all transactions (auth and cleared) per virtual card and program in near-real-time → notifications → fraud alerts (non-suppressible) → card lifecycle management
- **Financial** (steps 29-32, primary systems: Electron + Tachyon + Corporate):
  - Statement generated → reconciliation → settlement → disputes

**Suggested Visuals:**
- Horizontal timeline or swimlane diagram: five phases with key steps marked and actor labels (ESP, Bank, Corporate Admin, System)
- Color-code by primary actor at each step — ESP (blue), Bank (green), Corporate Admin (orange), System/automated (gray)
- Or a three-lane swimlane (Bank, ESP, Corporate) with steps placed in the lane of the primary actor

**What to Avoid:**
- Don't make this look like a sequential waterfall — Corporate Account Configuration (steps 10-14) and Operations (steps 24-28) involve ongoing, concurrent activity
- Don't skip the Contracting & Onboarding phase — bank prospects need to see that credit underwriting stays firmly in their domain
- Don't conflate ESP-driven contracting with corporate-driven program setup — the handoff at step 9 (portal access provisioned) is the boundary
- Don't skip dispute resolution — bank prospects care about it

**Source Reference:** `05-corporate-playbook/02-supplier-payments-program.md`, `03-bank-foundation/02-onboarding.md`, `04-esp-playbook/01-esp-wide-concerns.md`

---

### Slide 21: Contracting, Onboarding, and Corporate Account Configuration

**Headline:** From Client Contract to a fully configured corporate account ready for program creation.

**Key Talking Points:**
- ESP-driven contracting: Client Contract initiated, Legal Entities identified, underwriting information collected, CF applications submitted per LAH
- Bank-driven underwriting: CFs issued per LAH (each may apply for multiple CFs with distinct underwriting documents), LAH billing contacts notified
- ESP-driven product assignment: CPPs assigned across Spend Archetypes per corporate's requirements, relationship-level terms (Rebates, Volume Commitments) configured against Client Contract
- Corporate admin-driven account configuration: users, OUs, member provisioning (AD, SAP, SCIM, SFTP, API), budgets (CF-derived and ERP-imported, hierarchy independent of CF), Payable Accounts (multiple banks, GL-mapped)
- Handoff: ESP provisions corporate portal access credentials — marks the transition from ESP-driven to corporate-driven activity

**Supporting Detail:**
- Each LAH may apply for multiple CFs with distinct underwriting document sets — bank audiences will appreciate this flexibility
- Budget hierarchy independence: ERP-defined budgets imported through integration need not be sublimits of the Credit Facility; the hierarchy can reside independent of the CF hierarchy
- Payable Accounts: corporate registers accounts at various banks for receiving invoices and making repayments; each maps to a GL in ERP — multiple payable accounts support different programs routing to different bank accounts
- Member provisioning channels: Active Directory (employees), SAP (vendors/suppliers), SCIM (identity provisioning), SFTP (bulk import), Member Management API (programmatic access)
- Ongoing maintenance: OU, Budget, Member, and Payable Account master data maintained through API or SFTP integrations — this is continuous, not one-time

**Suggested Visuals:**
- Three-lane swimlane (ESP, Bank, Corporate Admin) showing the handoff sequence from contracting through account configuration
- Or a timeline with actor labels showing who drives each step

**What to Avoid:**
- Don't conflate ESP onboarding (one-time) with corporate onboarding (per-client, repeated)
- Don't skip KYB — it's per legal entity, not per corporate, and bank prospects care about regulatory compliance
- Don't make Payable Account setup seem trivial — it's where the corporate's treasury operations connect to the platform

**Source Reference:** `03-bank-foundation/02-onboarding.md`, `04-esp-playbook/01-esp-wide-concerns.md`, `02-ontology/01-corporate-legal-entity-ou-members.md`

---

### Slide 22: Program Setup and Enrollment

**Headline:** From program creation to first card in a member's hands.

**Key Talking Points:**
- Admin initiates a Program for a specific Spend Archetype, selecting a CPP offered by ESP; links to CF, assigns to OU
- Spend Programs configured using Purchase Categories — program-level defaults and enrollment-level tightening
- Each Spend Program must reference a CF-derived Budget (bank credit risk protection); may additionally reference Spend Program Budgets or static limits for corporate policy enforcement
- Booking-limit Spend Programs: for ERP-imported Budgets, the Spend Program can designate the budget as the booking destination; highest-precedence booking-limit Spend Program determines posting attribution
- Non-booking Spend Programs: concurrent usage gates — all applicable ones evaluated together
- Booking Profile and Settlement Profile configured per program
- Members enrolled via API (ERP/enterprise integration) or SFTP; enrollment triggers virtual card issuance with tags; enrollment-level Spend Programs configured for member-specific controls
- Card dispatched per archetype: immediate (API response), digital (secured email/portal), or physical; dispatch notification includes relevant context for the member

**Supporting Detail:**
- Purchase Categories: bank provides pre-defined categories accessible to corporates; corporate and ESP can define additional ones using bank's data dictionary; maps to Posting Categories in Bank Domain
- Spend Program precedence: numeric value set by admin; determines which booking-limit Spend Program wins when multiple match
- Hard constraint: per posting, no more than 3 non-booking, non-CF external limits evaluated by Tachyon; exceeding this declines the transaction (up to 5 limit ledgers updated per posting, excluding ancestor traversal)
- Supplier enrollment example: enrollment against PO → single-use card issued with exact authorized amount → card carries PO number, invoice number as tags → secured email sent to supplier with PO, invoice, authorized amount
- Booking Profile: GL account, cost center, project/client code, capex/opex; static defaults or dynamic rules based on transaction attributes
- Settlement Profile: linked to registered Payable Account, billing entity, repayment method and timing

**Suggested Visuals:**
- Program configuration diagram showing the relationships: CPP → Program → Spend Programs (with Purchase Categories and Budgets) → Booking Profile → Settlement Profile → Eligibility → Enrollment → Cards
- Or a Spend Program evaluation pipeline: Sources → Dimensions → Purchase Category → Spend Program → Controls

**What to Avoid:**
- Don't conflate booking-limit and non-booking Spend Programs — they serve fundamentally different purposes (attribution vs. usage gates)
- Don't suggest the 5-ledger constraint is a limitation — frame it as an engineered bound on authorization path complexity
- Don't skip Purchase Categories — they are the mechanism by which corporates express governance intent in their own vocabulary

**Source Reference:** `02-ontology/07-spend-policy-controls.md`, `02-ontology/10-members-eligibility-enrollment.md`, `02-ontology/05-corporate-payment-program.md`

---

### Slide 23: Operations

**Headline:** Day-to-day transaction processing, monitoring, and cooperative authorization.

**Key Talking Points:**
- Authorization through bank's check cascade: card active, account active, CF capacity, budget capacity (ancestor chain), Posting Category → Spend Program controls, non-overridable controls
- Cooperative authorization: corporate configures endpoint per payment program; bank routes callback during authorization; corporate verifies and responds
- Supplier payment example: supplier presents card with L2 data including invoice number → corporate's endpoint verifies invoice is approved in AP, amount matches → positive: approval data added, posting continues → negative: reason captured, authorization declined
- Posting enrichment: at clearing, corporate systems can augment posting data with updated attribution
- Corporate Portal reflects all transactions in near-real-time; notifications for auth, clearance, card events, fraud (non-suppressible)
- Budget monitoring: threshold-based alerts at budget and program level
- Card lifecycle management: suspend, reactivate, close, replace, modify limits — replacement preserves enrollment, Spend Programs, and tags

**Supporting Detail:**
- Bank retains final authority — even after positive cooperative authorization response, non-overridable controls (AML, sanctions, fraud, regulatory holds, delinquency, CF breach) still apply
- Cooperative authorization is real-time three-way match at auth time for supplier payments: PO (from card tags) + invoice (from L2 data) + AP verification (from callback)
- Posting enrichment examples: project code updates, GL routing adjustments, cost center reassignment based on current organizational data — applied before final booking
- Notification hierarchy: bank regulatory/fraud → non-suppressible; ESP templates → corporate customizable; card-level → member preferences
- Budget alerts configurable at thresholds (e.g., 75%, 90% utilization); alerts to Program Admin
- Single-use cards automatically closed after use and grace period

**Suggested Visuals:**
- Sequence diagram: Supplier → Network → Bank (check cascade) → cooperative auth callback to corporate's AP system → response → remaining checks → decision → posting
- Or operational flow: Auth → Portal visibility → Notifications → Budget monitoring → Card management

**What to Avoid:**
- Don't make cooperative authorization seem mandatory — it's optional, configured per program
- Don't suggest corporates can override bank fraud decisions or non-overridable controls
- Don't skip the three-way match example — it's the most concrete illustration of cooperative authorization's value

**Source Reference:** `03-bank-foundation/03-processing-authorization-controls.md`, `05-corporate-playbook/01-corporate-wide-concerns.md`, `05-corporate-playbook/02-supplier-payments-program.md`

---

### Slide 24: Financial Phase

**Headline:** Billing, settlement, reconciliation, and dispute resolution.

**Key Talking Points:**
- Two separate billing streams: bank bills per program billing cycle (Settlement Profile); ESP bills per Client Contract billing date — structurally independent cycles
- Bank statement includes rebate and reward computation; invoices net value; auto-debited via ACH or intra-bank rails from registered Payable Account
- ESP computes relationship-level rewards, rebates, and volume commitments; invoices net; has access to all program postings and bank statements
- Three reconciliation channels: near-real-time postings in Corporate Portal, bank's rich data extract per statement, ESP's data mart — corporate uses any combination
- Disputes raised from Corporate Portal at any time; credits follow original booking attribution
- Single-use cards closed after use and grace period; all card statuses visible in portal

**Supporting Detail:**
- When bank and ESP are the same entity, billing cycles can align; however, corporates may configure different billing cycles per program (each program has its own Settlement Profile), causing divergence even in the same-entity case
- Bank statement: per billing cycle, per program; master statement for multi-account programs (e.g., 200+ employee accounts)
- ESP invoice: relationship-level, may span multiple programs under the same Client Contract
- Rebate split: product-level (Tachyon, interchange-based) and relationship-level (Electron, aggregate-based) — computed in different systems
- Reconciliation targets vary by archetype: supplier programs target PO/invoice match; employee programs match expense reports; travel matches itineraries; recurring matches contracts
- Dispute credits follow original booking profile — if original was GL 5100 / CC-3000, credit reverses the same allocation

**Suggested Visuals:**
- Dual billing timeline: Bank statement cycle (per program) and ESP invoice cycle (per contract) shown in parallel
- Reconciliation flow: three input channels (real-time postings, statement data extract, data mart) converging on corporate reconciliation

**What to Avoid:**
- Don't conflate bank billing (per program, per Settlement Profile) with ESP billing (per contract, per Client Contract) — they are structurally independent
- Don't suggest reconciliation depends solely on statement delivery — near-real-time postings may have already updated corporate systems
- Don't omit dispute resolution — bank prospects care about it

**Source Reference:** `02-ontology/08-booking-settlement-profile.md`, `05-corporate-playbook/02-supplier-payments-program.md`, `04-esp-playbook/01-esp-wide-concerns.md`

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
| 1 — Possibilities vs Needs | `01-problem-space/01-corporate-payments-problem.md`, `01-problem-space/02-existing-solutions.md`. See `book-writing-backlog.md` #13 |
| 2 — The Platform Reality | Presentation-originated. See `book-writing-backlog.md` #17 |
| 3 — The Semantic Dissonance | `01-problem-space/02-existing-solutions.md`, `01-problem-space/03-two-lenses.md`. See `book-writing-backlog.md` #14 |
| 4 — Five Dimensions of Corporate Need | Presentation-originated. See `book-writing-backlog.md` #15 |
| 5 — The Counterparty Multiplier | Presentation-originated. See `book-writing-backlog.md` #16 |
| 6 — The Two-Lens Gap — Hierarchy Is Not the Answer | `01-problem-space/03-two-lenses.md`, `01-problem-space/02-existing-solutions.md`, `why-hierarchy-is-not-the-answer.md`. See `book-writing-backlog.md` #18 |
| 7 — The Promise Is Captive to the Platform | Presentation-originated. See `book-writing-backlog.md` #17, Legacy Platform Constraints reference section |
| 8 — The Foundation and The Bridge | `01-problem-space/03-two-lenses.md`. See `book-writing-backlog.md` #13-15, #17 |
| 9 — Spend Archetypes | `01-problem-space/04-spend-archetypes.md`, `02-ontology/10-members-eligibility-enrollment.md` |
| 10 — Spend Mandates | `01-problem-space/05-spend-mandates.md` |
| 11 — Governance: Constraints and Decisions | `01-problem-space/05-spend-mandates.md` |
| 12 — The Three Domains | `01-problem-space/03-two-lenses.md`, `00-front-matter/02-running-example.md` |
| 13 — The Economics of Separation | `01-problem-space/03-two-lenses.md`, `04-esp-playbook/01-esp-wide-concerns.md` |
| 14 — Systems and Bounded Contexts | `02-ontology/02-account-product-virtual-card-product.md`, `03-bank-foundation/01-account-card-products.md`, `04-esp-playbook/01-esp-wide-concerns.md`, `05-corporate-playbook/01-corporate-wide-concerns.md` |
| 15 — Context Boundaries and Integration Points | `03-bank-foundation/03-processing-authorization-controls.md`, `04-esp-playbook/01-esp-wide-concerns.md` |
| 16 — Entity Model Across Domains | `02-ontology/02-account-product-virtual-card-product.md`, `02-ontology/01-corporate-legal-entity-ou-members.md`, `03-bank-foundation/01-account-card-products.md`, `04-esp-playbook/01-esp-wide-concerns.md`, `05-corporate-playbook/01-corporate-wide-concerns.md`, `3-domain-erd.md` |
| 17 — The Derivation Chain | `02-ontology/03-esp-variants-corporate-payment-product.md`, `02-ontology/05-corporate-payment-program.md` |
| 18 — Hierarchies (Corporate's and ESP's View) | `02-ontology/04-credit-facility-budget-account.md`, `05-corporate-playbook/01-corporate-wide-concerns.md` |
| 19 — Hierarchies (Bank's View) | `03-bank-foundation/03-processing-authorization-controls.md`, `02-ontology/04-credit-facility-budget-account.md` |
| 20 — Lifecycle Overview | `05-corporate-playbook/02-supplier-payments-program.md`, `03-bank-foundation/02-onboarding.md`, `04-esp-playbook/01-esp-wide-concerns.md` |
| 21 — Contracting, Onboarding, and Corporate Account Configuration | `03-bank-foundation/02-onboarding.md`, `04-esp-playbook/01-esp-wide-concerns.md`, `02-ontology/01-corporate-legal-entity-ou-members.md` |
| 22 — Program Setup and Enrollment | `02-ontology/07-spend-policy-controls.md`, `02-ontology/10-members-eligibility-enrollment.md`, `02-ontology/05-corporate-payment-program.md` |
| 23 — Operations | `03-bank-foundation/03-processing-authorization-controls.md`, `05-corporate-playbook/01-corporate-wide-concerns.md`, `05-corporate-playbook/02-supplier-payments-program.md` |
| 24 — Financial Phase | `02-ontology/08-booking-settlement-profile.md`, `05-corporate-playbook/02-supplier-payments-program.md`, `04-esp-playbook/01-esp-wide-concerns.md` |
