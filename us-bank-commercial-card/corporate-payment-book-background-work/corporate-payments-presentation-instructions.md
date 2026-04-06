# Corporate Payments by Design — Presentation Build Instructions

## 1) Purpose of This Document

This document is the source-of-truth brief for the deck team building the "Corporate Payments by Design" presentation. It translates the narrative and content from the presentation outline and discussion documents into actionable build instructions for each slide.

Use this as your construction guide:
- What each slide must accomplish (goal and business rationale)
- What content to include (tables, diagrams, key points)
- What visual format to use (infographic type and spatial layout)
- What to watch for during production (build notes, split candidates, cross-references)

Source materials:
- **Structure**: `presentation-outline.md` — 25 slides (0-24), 4 acts
- **Narration**: `presentation-contents-discussion.md` — detailed talking points, suggested visuals, what-to-avoid guidance
- **Entity Model**: `3-domain-erd.md` — Mermaid ER diagram for Slide 16

---

## 2) Audience + Outcome

**Primary audience**
- Bank product leadership evaluating the platform for corporate payments
- Bank technology and architecture teams assessing system design
- Bank commercial card strategy stakeholders

**Desired outcome**
- Establish that corporate payments require a purpose-built architecture, not incremental enhancement of legacy card platforms
- Demonstrate the three-domain model (Bank, ESP, Corporate) as both an architectural and business solution
- Show end-to-end lifecycle from contracting through financial operations
- Position the platform as the foundation for the bank's corporate payment strategy

---

## 3) Deck Storyline (Recommended Flow)

1. **Act 1 — The Gap** (Slides 0-8): Name the problem — the structural distance between what banks promise with virtual cards and what corporates actually need. Establish why legacy platforms cannot close this gap. Introduce the foundation and bridge as the solution thesis.
2. **Act 2 — The Framework** (Slides 9-13): Introduce Spend Archetypes, Spend Mandates, the governance model, the three-domain architecture, and the economics of separation.
3. **Act 3 — The System Design** (Slides 14-19): Map the bounded contexts (28 subsystems), integration boundaries, entity model, derivation chain, and hierarchies from corporate and bank perspectives.
4. **Act 4 — Program Lifecycle and Extensibility** (Slides 20-24): Walk through the 34-step lifecycle across five phases — contracting, corporate account configuration, program setup, operations, and financial management.

**General presenter guidance:**
- Use Meridian/Apex/Commonwealth as the running example (fictitious but comprehensive: 3 legal entities, 18,000 employees, 4 archetypes, multi-currency)
- Define Tachyon-specific terms (HAH, LAH, RAH, VBO) when they first appear
- The three-domain separation is the central architectural argument — return to it whenever the audience asks "who owns this?"
- Avoid commercial voice — frame capabilities as architectural decisions, not product features
- The policy cascade (tighten-only, bank-enforced) is a key technical differentiator

---

## 4) Design Palette

**Primary colors**
- Purple / violet — brand anchor; use for titles, key callouts, emphasis elements
- Light green — complementary accent; use for positive indicators, answered dimensions, ESP domain

**Domain coding** (apply consistently across all diagrams, table headers, entity fills, and boundary markers):
- Light blue — Bank domain (Tachyon)
- Light green — ESP domain (Electron)
- Light amber — Corporate domain (Electron Portal)

**Usage rules**
- Apply domain colors consistently on every diagram and table that shows cross-domain content
- Maximum four colors per slide (domain colors + one accent/emphasis color)
- Legibility over decoration — dark text on pastel fills; never use light text on light backgrounds
- Slide backgrounds: white or off-white; avoid dark or colored backgrounds
- Cross-domain arrows and dashed lines: use a neutral dark gray, not domain-colored
- Tables: use domain color as a subtle header row fill, not as cell backgrounds for data rows

---

## 5) Slide-by-Slide Build Instructions

---

## Slide 0 - Title

**Slide goal**
- Set the frame: this is an architectural walkthrough of how corporate payments should work, not a product demo or feature list.

**Why this matters**
- The title "by Design" signals intentionality — every entity, hierarchy, and control exists for a reason. "First-principles" signals that we start from what corporates need, not what banks currently offer.

**What to include**
- Title: "Corporate Payments by Design with Tachyon and Electron"
- Subtitle: "The first-principles design to solve for corporate concerns"
- Three-domain icon set establishing the visual vocabulary for the entire deck

**Infographic type:** Title card with three-domain icon arrangement

**Slide layout**
- *Top third:* Slide title in large type: "Corporate Payments by Design with Tachyon and Electron"
- *Below title:* Subtitle in lighter weight: "The first-principles design to solve for corporate concerns"
- *Center:* Three equal-width tiles in a single row, each with an icon and label:
  - Tile 1 (light blue fill): Bank icon — "Bank Domain · Tachyon"
  - Tile 2 (light green fill): ESP icon — "ESP Domain · Electron"
  - Tile 3 (light amber fill): Corporate icon — "Corporate Domain · Electron Portal"
- *Below tiles:* One line in smaller type: "An architectural walkthrough: from problem to data model to lifecycle"
- *Bottom-right:* Confidentiality marker

**Build notes**
- Do not open with product features, client logos, or "industry-leading" language.
- The three-domain tile colors (light blue, light green, light amber) are established here and must recur on every subsequent slide that shows cross-domain content.
- The tiles should feel like a visual vocabulary introduction, not decoration.

---

## Slide 1 - Possibilities vs Needs

**Slide goal**
- Establish the gap between what banks promise with virtual cards and what corporates actually need. Frame this gap as the required evolution — not a criticism, but a market reality.

**Why this matters**
- The audience (bank product leaders) has been describing virtual card possibilities to corporates. This slide names the dynamic they already feel: corporates imagine answers the product does not yet deliver.

**What to include**
- Two-column layout contrasting bank promises with corporate expectations
- A bridging statement that names the gap as "the required evolution"

**Infographic type:** Two-column comparison with bridging statement

**Slide layout**
- *Left column (45% width, light blue left border):* Header: "The Promise" — five numbered items:
  1. "Issue a card per PO"
  2. "Lock to a single merchant"
  3. "Set velocity limits"
  4. "Get L2/L3 data"
  5. "Real-time authorization notifications"
- *Right column (45% width, light amber left border):* Header: "The Imagined Answer" — five numbered items:
  1. "Budget enforcement across three legal entities"
  2. "GL attribution per transaction"
  3. "Policy cascades across 200 supplier cards"
  4. "Automated reconciliation against AP"
  5. "Settlement consolidated by program"
- *Below both columns, full width, purple/violet background bar:*
  - "The gap between the promise and the imagined answer is the required evolution."
- *Bottom-right footnote:* "Neither side is wrong. They are organizing around different concerns."

**Build notes**
- The two columns must feel balanced — neither side is wrong. The possibilities are real; the needs are real. They are not the same conversation.
- If animation is supported, reveal the right column after the left to build the tension.
- This framing ("promise → imagined answer → required evolution") recurs throughout Act 1 — establish it clearly here.

---

## Slide 2 - The Platform Reality

**Slide goal**
- Plant a provocation: the vision is compelling, but the platform beneath the strategy constrains delivery. This sets up a loop that Slide 7 will close with specifics.

**Why this matters**
- Bank executives live with platform constraints daily. Naming the gap between strategy and infrastructure creates immediate recognition and credibility.

**What to include**
- Two-sentence headline only. No feature lists, no vendor names, no product comparisons.

**Infographic type:** Statement slide — large typography, minimal visual

**Slide layout**
- *Center of slide, vertically and horizontally:* Two lines of large, clean type:
  - Line 1: "The vision of corporate payments is compelling."
  - Line 2 (slightly bolder, or in purple/violet): "The platform wasn't built for it."
- *No other visual elements.* White background. The emptiness is deliberate — it forces a pause.

**Build notes**
- This is a pause slide. The visual minimalism is deliberate — the audience needs a moment to absorb the provocation.
- Do not frame this as "your platform is bad." The first sentence validates the bank's vision. The second names the architectural constraint.
- Slide 7 closes the loop opened here. Maintain visual continuity between Slides 2 and 7 (same purple/violet treatment for the key phrase).

---

## Slide 3 - The Semantic Dissonance

**Slide goal**
- Make the gap visceral through four concrete Q&A pairs showing how corporates and banks talk past each other — both speaking accurately, from different frames.

**Why this matters**
- The audience will recognize these conversations from their own client interactions. The accumulation of four rows — each showing the same structural shape — makes the pattern undeniable.

**What to include**
- Two-column table with exact Q&A pairs drawn from real corporate-bank conversations
- Pattern summary below the table

**Infographic type:** Two-column table with sequential row animation

**Slide layout**
- *Top:* Slide title: "When corporates ask questions and banks answer with card capabilities, both sides are speaking accurately — from different frames."
- *Main area:* Two-column table with four rows:
  - Column headers: "Corporate's Question" (light amber header fill) | "Bank's Answer" (light blue header fill)
  - Row 1: "Our policy is to encourage local procurement. How can I specify my suppliers?" | "Please provide the MID and TID of all your suppliers."
  - Row 2: "Our policy requires maker and checker for high-value department spends. How can we specify that?" | "You can issue a card for every transaction, after checking whatever needs to be checked."
  - Row 3: "Every ticket purchased is subject to the project budget, the employee's location, and their career level." | "You can set limits per card."
  - Row 4: "Our marketing budget is shared across three regions operating with different currencies. Each region can spend up to their allocation, but the total must not exceed the consolidated budget." | "You can set credit sub-limits per account."
- *Below table, smaller type:* "The corporate asks about business rules, organizational context, and operational workflows. The bank answers with card-level primitives. Neither side is wrong."

**Build notes**
- Do not add a "Gap" column. The dissonance is more powerful when the audience names it themselves.
- If animation is supported, reveal rows sequentially — let the pattern build through accumulation.
- Each row should have a beat in the narration; do not rush through the table.

---

## Slide 4 - Five Dimensions of Corporate Need

**Slide goal**
- Name the analytical framework: corporate payment needs span five dimensions, and today's card products answer only the first. The remaining four are where programs succeed or fail.

**Why this matters**
- This framework structures the rest of the presentation. Every architectural decision in later slides maps back to one or more of these dimensions.

**What to include**
- Five-row, three-column table with a visual coverage gradient
- Closing observation about CFO evaluation criteria

**Infographic type:** Five-row table with coverage gradient (green → red)

**Slide layout**
- *Top:* Slide title: "Corporate payment needs span five dimensions — today's card products answer only the first."
- *Main area:* Three-column table:
  - Column headers: "Dimension" | "What the Corporate Needs" | "What Card Products Typically Provide"
  - Row 1 (green indicator on right column): "Payment Execution" | "Authorize, clear, settle reliably" | "Well-answered: networks, schemes, real-time auth"
  - Row 2 (yellow indicator): "Financial Architecture" | "Credit facilities allocated as budgets, tied to organizational purpose, with hierarchical enforcement" | "Partially answered: credit limits and sub-limits exist, but without budget semantics or OU-awareness"
  - Row 3 (orange indicator): "Control Architecture" | "Policy cascades, eligibility rules, enrollment workflows, lifecycle governance across programs" | "Primitively answered: per-card controls exist, but no program-level policy, no inheritance, no lifecycle orchestration"
  - Row 4 (red indicator): "Accounting & Attribution" | "Every transaction attributed to GL, cost center, project, client — structured, validated, pushed to ERP" | "Not answered: reference fields exist but lack structure, validation, and ERP integration"
  - Row 5 (red indicator): "Reconciliation & Settlement" | "Automated matching against PO/invoice/booking/contract; consolidated settlement by program" | "Not answered: transaction data is available but matching, consolidation, and settlement management are left to the corporate"
- *Below table, italicized:* "No corporate CFO evaluates a card program on authorization speed. They evaluate on reconciliation labor, policy leakage, and attribution accuracy."

**Build notes**
- The green-to-red gradient on the right column is the key visual — it makes the coverage gap immediately legible without requiring the audience to read every cell.
- Rows 4 and 5 (Accounting and Reconciliation) are where the most operational pain lives — they should have the strongest red visual treatment.
- The five dimensions are an analytical framework, not a product checklist.

---

## Slide 5 - The Counterparty Multiplier

**Slide goal**
- Show that the five dimensions multiply across at least seven distinct counterparty types — the problem is not just multi-dimensional, it is multi-dimensional per counterparty type.

**Why this matters**
- Today's card products abstract all counterparties as "merchants." The corporate sees seven fundamentally different relationships. This diversity is what makes archetype-based product design necessary (introduced in Act 2).

**What to include**
- Seven-row table with exact counterparty types and their characteristics
- Closing observation about the merchant abstraction

**Infographic type:** Seven-row reference table

**Slide layout**
- *Top:* Slide title: "The five dimensions do not present uniformly — the AP landscape has at least seven distinct shapes."
- *Main area:* Five-column table with seven data rows:
  - Column headers: "Counterparty Type" | "Payment Pattern" | "Data Needs" | "Compliance" | "Card Acceptance"
  - Row 1: "Goods suppliers" | "PO/invoice-driven, deterministic" | "L2/L3, three-way match" | "Trade compliance, tax" | "Generally high"
  - Row 2: "Service providers" | "Milestone or deliverable-based" | "SOW reference, project attribution" | "Contract compliance" | "Variable"
  - Row 3: "Employees" | "Reimbursable expenses or pre-approved budget-based spend; the actual merchant is not a direct party" | "Receipt, expense category, project/cost center" | "Expense policy, delegation of authority" | "High — employee transacts at merchant"
  - Row 4: "Contractors" | "Time/expense-based, recurring" | "Timesheet linkage, project codes" | "Labor compliance, 1099" | "Low — often ACH preferred"
  - Row 5: "SaaS / software vendors" | "Subscription, renewal-driven" | "Contract ID, license count" | "Procurement policy" | "High — most accept cards"
  - Row 6: "Intermediaries / agencies" | "Pass-through, consolidated" | "Booking reference, itinerary" | "Agency agreements, duty of care" | "High — travel, logistics"
  - Row 7: "Government / regulatory" | "Fee schedules, non-negotiable" | "Mandate reference, filing ID" | "Regulatory deadlines" | "Low — often requires wire/ACH"
- *Below table, full width:* "Today's card products abstract all of these as 'merchants' — a single MCC-classified entity. The corporate sees seven fundamentally different relationships, each with distinct governance requirements."

**Build notes**
- This is a reference slide — the audience scans the table while the speaker narrates 2-3 key contrasts.
- Key narrator point for row 3 (Employees): "For employees, the merchant isn't even the counterparty — the governance is between the corporate and its employee, not the corporate and the merchant."
- Do not go deep on any single counterparty type here — the archetype discussion (Slide 9) handles that.
- Low-card-acceptance counterparties (contractors, government) should not be visually diminished — their presence in the AP landscape is part of the problem.

---

## Slide 6 - The Two-Lens Gap — Hierarchy Is Not the Answer

**Slide goal**
- Deliver the cognitive pivot of Act 1: the bank's hierarchy of limits is sound for credit risk but structurally insufficient for corporate governance. The corporate's governance requires independent, concurrent dimensions — a coordinate system, not a tree.

**Why this matters**
- The audience's product teams have been reaching for deeper hierarchy — more granular limits, more sub-accounts, more MCC groups — every time a corporate asks for more control. This slide names why that instinct does not work.

**What to include**
- Side-by-side comparison of bank and corporate organizing models
- Structural mismatch labels between them
- Concrete example showing why hierarchy cannot accommodate two enterprises simultaneously
- "Hierarchy is not the answer" as the culminating statement

**Infographic type:** Split comparison with structural argument

**Slide layout**
- *Top:* Slide title: "Both control models are sound. A hierarchy forces a fixed nesting. The dimensions cannot be nested. They must remain independent."
- *Left half (light blue background):* Labeled "Hierarchy of Limits — single path"
  - Vertical tree diagram, top to bottom:
    - "Credit Facility"
    - → "Account"
    - → "Card"
    - → "MCC / Amount / Velocity Controls"
    - → "Interchange"
    - → "Lifecycle"
  - Below the tree: "Banks optimize for: credit risk, regulatory compliance, network settlement, treasury income (float, interchange, facility interest)"
- *Right half (light amber background):* Labeled "Coordinate System — concurrent dimensions"
  - Multi-axis grid showing six independent dimensions arranged as a star/radar shape or as six parallel horizontal bars:
    - "Budget"
    - "Policy"
    - "Authority"
    - "Attribution"
    - "Purpose"
    - "Validity"
  - Below the grid: "Corporates optimize for: operational governance, financial attribution, audit readiness, payment cost and process efficiency"
- *Center divider* between left and right, with four mismatch labels stacked vertically:
  - "org structure ≠ account structure"
  - "budget ≠ credit limit"
  - "GL fields ≠ transaction data"
  - "workflow ≠ card controls"
- *Bottom strip, full width, purple/violet background, large type:*
  - "Hierarchy is not the answer."
- *Below the strip, smaller type:*
  - "Does Department contain Project, or Project contain Department? Every corporate answers differently — and the answer changes when they restructure. No universal nesting exists."

**Build notes**
- This is the most important conceptual slide in Act 1. Do not rush it.
- The "Hierarchy is not the answer" strip should be the most visually prominent element — it is the cognitive pivot.
- Reference supporting document: *Why Hierarchy Is Not the Answer* contains the full structural analysis with ERP evidence, DoA matrices, and scenario walkthroughs.
- The audience needs to shift from "we need deeper hierarchy" to "we need independent dimensions."

---

## Slide 7 - The Promise Is Captive to the Platform

**Slide goal**
- Close the loop opened in Slide 2 with seven specific architectural constraints that define the captivity of legacy card processing platforms. Each constraint now maps to needs the audience has absorbed across Slides 3-6.

**Why this matters**
- After Slides 3-6, the audience understands what the corporate needs. These seven constraints name specifically why the existing platform cannot deliver it — transforming abstract architectural observations into concrete, recognizable limitations.

**What to include**
- Seven-row constraint table with exact constraint labels and descriptions
- Speaker probe questions per row (in presenter notes, not on slide)

**Infographic type:** Seven-row constraint table with progressive reveal

**Slide layout**
- *Top:* Slide title: "The compelling possibility of automated corporate payments is captive to the platform that delivers it."
- *Subtitle (smaller, callback to Slide 2):* "We said the platform wasn't built for it. Here's specifically what that captivity looks like."
- *Main area:* Two-column table with seven rows:
  - Column headers: "Constraint" (purple/violet bold, ~25% width) | "What It Means" (~75% width)
  - Row 1: **"Batch-native"** | "Real-time authorization events, lifecycle notifications, and cooperative callbacks require middleware the platform wasn't designed for"
  - Row 2: **"Rigid hierarchies"** | "The platform evaluates a hierarchy of limits along a single path; it cannot evaluate the corporate's coordinate system of concurrent dimensions — no multi-segment budgets, no category-dependent policy cascade, no concurrent dimensional enforcement at authorization"
  - Row 3: **"Limiting data structures"** | "Rigid data fields that cannot carry corporate context through the transaction lifecycle; refunds and credits not attributed back to original booking profile"
  - Row 4: **"Closed authorization"** | "The processor decides alone; no hook for ESP or corporate participation within network timeouts; no posting enrichment at clearing"
  - Row 5: **"Lack of token awareness"** | "Token lifecycle not coordinated with card lifecycle across renewals and replacements; authentication limited across CNP/CP scenarios; PIN delivery confined to legacy channels; FRM has credential lifecycle blind spots"
  - Row 6: **"Throughput constraints"** | "Not designed for high-frequency, API-triggered, single-use issuance at scale; card lifecycle operations designed for call-center workflows, not programmatic bulk operations"
  - Row 7: **"Inaccessible for extension"** | "No event subscriptions, no webhook-driven integration, no API-driven lifecycle customization; the platform is closed to the ecosystem that needs to build on it"
- If animation is supported, reveal one row at a time.

**Build notes**
- **Split candidate:** Consider splitting into 7a (constraints 1-4: Batch-native, Rigid hierarchies, Limiting data, Closed authorization) and 7b (constraints 5-7: Token awareness, Throughput, Inaccessibility). Breakpoint: after "Closed authorization" — the first four are about the processing model; the last three are about the platform model.
- Speaker probe questions (in presenter notes, not on slide):
  - Batch-native: "When was the last time your processor pushed an authorization event in real time without middleware?"
  - Rigid hierarchies: "Can your processor enforce budget, policy, and attribution across concurrent dimensions simultaneously at authorization — or does it evaluate one path down a limit hierarchy?"
  - Limiting data structures: "Can you attach a PO number to a card at issuance and have it travel through authorization, clearing, and settlement? When a refund arrives, does it attribute back to the original booking?"
  - Closed authorization: "Can your corporate client participate in the authorization decision before the processor responds to the network?"
  - Lack of token awareness: "When a virtual card is renewed, do the tokens migrate automatically? Does your FRM system see the full credential lifecycle — or just the card?"
  - Throughput: "How many single-use cards can your processor issue per minute via API?"
  - Inaccessible: "Can your ESP subscribe to card events in real time? Can a corporate system trigger a lifecycle operation via API?"
- Maintain visual continuity with Slide 2 (same purple/violet treatment for the subtitle callback).
- Do not present this as a competitive feature matrix — it is an architectural observation. Do not name specific vendors.

---

## Slide 8 - The Foundation and The Bridge

**Slide goal**
- Transition from problem (Act 1) to solution (Act 2) by naming the two-part thesis: a purpose-built foundation (processing platform) and a bridge (three-domain architecture) that closes the five-dimensional gap.

**Why this matters**
- This slide converts eight slides of problem framing into a clear statement of intent. It creates momentum into Act 2 without going deep on any architectural component.

**What to include**
- Two-layer visual: the foundation (platform capabilities) and the bridge (three-domain model)
- Roadmap of what follows in the rest of the presentation

**Infographic type:** Two-layer thesis diagram with transition arrow

**Slide layout**
- *Top:* Slide title: "This is what we set out to solve."
- *Upper layer, labeled "The Bridge":* Three equal-width tiles in a row, using domain colors:
  - Tile 1 (light blue): "Bank" — "Risk, Compliance, Treasury Income"
  - Tile 2 (light green): "ESP" — "Translation, Product Design, Engagement"
  - Tile 3 (light amber): "Corporate" — "Governance, Attribution, Operations"
  - Below the tiles: "Clean separation — each domain owns its vocabulary, control, pace, and scope. The full control matrix is present at every authorization."
- *Lower layer, labeled "The Foundation":* A single horizontal bar with eight labeled segments (light blue/neutral background):
  - "Event-native" | "Hierarchy-aware" | "Contextual" | "On-demand" | "Cooperatively authorized" | "Token-aware" | "Throughput-ready" | "Extensible"
  - Below the bar: "The inverse of every constraint we just identified — plus architected for credentials beyond cards, authentication beyond static mechanisms, rails beyond card networks, and digital currencies."
- *Bottom strip:* Roadmap in smaller type:
  - "What follows: **The Framework** — archetypes, mandates, governance, domains, economics → **The System Design** — bounded contexts, entities, hierarchies → **The Lifecycle** — contracting through financial operations"

**Build notes**
- This is a transition slide — do not linger. Two clear statements, then move.
- The eight foundation attributes are the inverse of the seven constraints from Slide 7 (plus "hierarchy-aware" and "on-demand" as separate attributes). The audience should see the inversion without needing it explained.
- Do not go deep on the three-domain model here — Slide 12 handles that.
- Do not collapse foundation and bridge into one idea — they are distinct (infrastructure vs. domain design).

---

## Act 2 — The Framework

---

## Slide 9 - Spend Archetypes

**Slide goal**
- Introduce the four Spend Archetypes as the organizing principle for how corporates govern spend — not product names, but distinct workflow patterns with different control models, card lifecycles, enrollment patterns, and reconciliation approaches.

**Why this matters**
- The seven counterparty types from Slide 5 collapse into four actionable product design patterns. Archetypes translate counterparty diversity into platform architecture — each archetype drives distinct product configuration, card behavior, and integration patterns.

**What to include**
- Comparison table: Archetype × four dimensions
  - Columns: Supplier Payments / Employee & Dept Spend / Travel & Booking / Central Recurring
  - Rows: Control model, Card lifecycle, Enrollment, Reconciliation
  - Supplier: tight, deterministic, PO/invoice match | single-use per invoice | payee (supplier) | PO/invoice match (L2/L3)
  - Employee: policy-bounded, discretionary within limits | persistent, renewable | payer (employee) | expense report, receipt matching
  - Travel: booking-locked or agency-managed | per-booking or lodge (long-lived) | traveler or travel desk | itinerary/booking match
  - Central Recurring: contract-aligned, merchant-locked | long-lived, merchant-locked | central administrator | contract/subscription match
- Key clarifications: archetypes are extensible (not a fixed four); "Embedded" (API-triggered issuance) is a delivery mechanism, not an archetype — it can serve any of the four
- Brief archetype details with Meridian examples: ~200 suppliers with API-issued cards; 120 engineering employees; travel desk with lodge card; 35 SaaS subscriptions

**Infographic type:** Four-column comparison table with archetype detail callouts

**Slide layout**
- *Main area (70%):* Four-column table with row labels on the left. Each column header uses a distinct icon or label for the archetype. Light amber column headers (corporate domain).
- *Below table (30%):* Four compact callout boxes (one per archetype) with 2-3 bullet details and a Meridian example

**Build notes**
- The table is the anchor — it must be readable and scannable without narration
- Do not use "Spend Lane" — use "Spend Archetype" consistently
- The archetypes map directly to CPPs in the entity model (Slide 16) and to program setup (Slides 20-22) — maintain consistent naming

---

## Slide 10 - Spend Mandates — The Authorization Envelope

**Slide goal**
- Introduce the Spend Mandate as a conceptual framework for reasoning about the complete chain of governance questions every corporate payment must answer. Make it concrete through a running example.

**Why this matters**
- The Spend Mandate connects the five dimensions (Slide 4) to the system entities that realize them. It transforms abstract governance requirements into eight explicit components that the audience can trace through the architecture.

**What to include**
- Eight-component table: Component / What it governs / Example (Meridian "Client Implementation Travel" mandate)
  - Purpose: why this spend exists → "Client Implementation Travel" for Bank X
  - Authority: who may authorize → Engineering VP for department spend
  - Budget Source: which budget funds it → Professional Services Travel — $5M
  - Policy Scope: what categories are allowed → AMC-Travel-Agencies, AMC-Hotels, AMC-Airlines
  - Limits: per-transaction, velocity, aggregate → $5,000 per booking, $35,000/quarter
  - Attribution: how spend is booked → Project BNK-X-2026, GL 6200-Travel
  - Validity: when the mandate is active → Apr–Jun 2026
  - Exceptions: what happens outside bounds → Escalation to CFO, manual review
- Key clarification: no single system entity called "Spend Mandate" — it is realized across Budget, Spend Program, Booking Profile, Card Profile, and Program configuration

**Infographic type:** Eight-row component table with example column

**Slide layout**
- *Main area:* Three-column table: Component / What it governs / Meridian Example. Clean, readable.
- *Bottom note:* "The Spend Mandate is a thinking tool — it is realized across multiple system entities, not stored as a single record."

**Build notes**
- The example column makes the abstract framework concrete — do not omit it
- Each component maps to real system behavior in later slides (Spend Programs → Slides 16, 22; Booking Profile → Slide 22; Budget → Slides 12, 18)
- Do not suggest there is a "Spend Mandate" table or API — it is explicitly a conceptual framework

---

## Slide 11 - Governance: Constraints and Decisions

**Slide goal**
- Decompose governance into three distinct types — constraints (real-time, autonomous), structured decisions (rule-based, configured), and unstructured decisions (human deliberation) — and name the design challenge of supporting all three simultaneously.

**Why this matters**
- A platform that only enforces constraints can say "no" but cannot explain why the channel exists. A platform that only supports structured decisions cannot prevent a single unauthorized transaction in real time. The three-type model shows the audience why their current platform's approach (primarily constraints) is insufficient.

**What to include**
- **Constraints** — evaluated at authorization in real time, no human in the loop:
  - Budget capacity (hierarchy-aware, ancestor chain), Spend Program controls (AMC, amount, currency, geography, velocity), Limits (per-transaction, daily, monthly, lifetime)
  - The bank evaluates these on every transaction without exception
- **Structured Decisions** — resolved before or after authorization through rules and configuration:
  - Purpose (which program), Participants (who is eligible/enrolled), Attribution (booking profile rules), Validity (program/card windows)
- **Unstructured Decisions** — require human deliberation; platform provides deliberation control:
  - Authority (who approved enrollment, escalation when contested), Exceptions (escalation workflows, approval chains, post-facto justification)
- Design challenge: all three must coexist in the same platform

**Infographic type:** Three-section governance model

**Slide layout**
- *Three horizontal bands,* top to bottom:
  - Top band (constraints): labeled "Real-time at Authorization" — list items in a compact row. Use a strong border or accent (purple/violet) to signal non-negotiability.
  - Middle band (structured decisions): labeled "Configuration-enforced" — list items. Use a moderate accent.
  - Bottom band (unstructured decisions): labeled "Deliberation-controlled" — list items. Use a lighter accent.
- *Right side:* A vertical arrow or bracket labeled "The design challenge: enforce all three simultaneously"

**Build notes**
- Do not collapse structured and unstructured decisions into one category — the distinction is architecturally significant
- The three bands should visually communicate the gradient from autonomous (top) to human-driven (bottom)
- Do not use the phrase "auditable but not enforceable" — an earlier framing that was deliberately revised

---

## Slide 12 - The Three Domains

**Slide goal**
- Present the three-domain model (Bank, ESP, Corporate) as the architectural answer to the hierarchy problem (Slide 6) and the governance challenge (Slide 11). Establish the "four owns" and immediately counter the objection that separation means isolation.

**Why this matters**
- This is the central architectural argument of the presentation. The three-domain separation is the design principle the audience will reference for every subsequent slide. Landing it clearly — and showing that separation includes integration — determines whether the rest of the deck resonates.

**What to include**
- Three domains with clear roles:
  - Bank: underwrites risk, authorizes transactions, enforces compliance, settles with networks
  - ESP: translates bank capabilities into corporate solutions — product design, onboarding, billing, operating layer
  - Corporate: configures programs, defines budgets and policies, enrolls members, operates day-to-day governance
- The "four owns" — presented as design principles, not observations:
  - Own vocabulary — each domain operates in its native semantics
  - Own control — each domain governs its own decisions
  - Own pace — each domain evolves independently
  - Own scope — banking stays within the regulatory perimeter; corporate stays outside it
- Separation is not isolation — the full control matrix is present at every authorization through:
  - Structured entities (flatten governance into computable authorization context)
  - Anti-corruption translation (each domain stays idiomatically native)
  - Cooperative authorization (ESP/corporate participate without owning the final decision)
- Core architectural value: designing data structures, algorithms, and processes that meet network-speed, security, and regulatory constraints simultaneously while keeping each domain native

**Infographic type:** Three-domain layout with integration overlay

**Slide layout**
- *Main area (65%):* Three horizontal or vertical blocks — Bank (light blue) / ESP (light green) / Corporate (light amber) — each with its role label and 1-2 line description
- *Overlay or connecting elements:* The "four owns" as a design principle strip across the top
- *Below or alongside:* Three integration mechanisms as connective arrows or bridges between the domain blocks: "Structured entities" / "Anti-corruption translation" / "Cooperative authorization"
- The visual must communicate both separation (distinct blocks) and integration (connective mechanisms) in one view

**Build notes**
- The bank does not see departments or cost centers; the corporate does not touch underwriting. But all three are present at authorization. This dual message must land.
- Platform mapping (for the speaker, not on-screen): Commonwealth = Bank on Tachyon; Apex = ESP on Electron; Meridian = Corporate on Electron Portal
- Reference *Why Hierarchy Is Not the Answer* (Sections 7-8) for detailed treatment of the integration mechanisms
- Do not imply the ESP is optional or just a reseller — the ESP adds substantial product design and operational value

---

## Slide 13 - The Economics of Separation

**Slide goal**
- Show that the three-domain architecture is also a business model: the bank provides BaaS, the ESP owns product design and engagement, and the corporate (their shared client) drives economics for both.

**Why this matters**
- This is where the architecture-to-business-model transition lands. The bank audience must see that three-domain separation creates value capture opportunities for them as BaaS providers, not just architectural elegance.

**What to include**
- Transition statement: Slide 12 established the three domains as an architectural design; this slide shows they are also a business model
- A bank can play the ESP role, but archetype × segment specialization makes partnership commercially rational
- Single table with stakeholders as rows, "Value Added" and "Value Realized" as columns:
  - Bank: adds CFs, authorization, compliance, settlement → realizes float, retention, interchange, fees
  - ESP: adds product design, onboarding, billing, operational layer → realizes revenue share, corporate fees, portfolio scale (40+ corporates)
  - Corporate: adds payment volume, payer-side ecosystem expansion, program config, budget/policy, enrollment → realizes spend governance, AP automation, rebates, DPO extension, reconciliation labor reduction
  - Members: add payee-side ecosystem expansion, transaction volume, sales/invoice data → realize cashflow improvement, expense simplification, travel convenience
- Closing: the economics work because the separation works

**Infographic type:** Four-row value exchange table

**Slide layout**
- *Main area:* Single table — Stakeholder / Value Added / Value Realized — four rows. Use domain colors for the Bank, ESP, and Corporate rows. Members row in neutral gray.
- *Below table:* One-line summary: "The bank earns from infrastructure. The ESP earns from engagement depth. The corporate gains governance capabilities neither could deliver alone."

**Build notes**
- Market evidence (for the speaker, not on-screen): Brex on Sutton Bank/Column, Ramp on Celtic Bank, Divvy/BILL on Cross River, Navan on various issuers. Use when challenged — do not put competitor names on the slide.
- Do not treat the corporate as a co-equal business entity — it is the client
- Do not make this feel like a revenue pitch for the ESP — frame it as a rational business model
- Do not omit Members — their value is real and often overlooked in bank-focused presentations
- The unspoken bank question ("why can't we just do this ourselves?") should be anticipated — the answer is specialization, not inability

---

## Act 3 — The System Design

---

## Slide 14 - Systems and Bounded Contexts

**Slide goal**
- Map the complete system landscape: 14 Tachyon subsystems (Bank), 7 Electron subsystems (ESP), and 9+ Corporate Domain systems. The audience should leave this slide knowing what runs where and why.

**Why this matters**
- This is where the audience anchors their understanding of system scope. Every subsequent slide — integration points, entity model, lifecycle — references subsystems introduced here. Bank architects will scrutinize this slide and ask deep questions.

**What to include**
- **Tachyon (Bank) — 14 subsystems:**
  - Customer Lifecycle Management (HAH, LAH, RAH)
  - Product Lifecycle Management (Account Product Families, Virtual Card Product Families; catalog creation, versioning, redistributability)
  - BaaS Management (VBOs; ESP onboarding, catalog access, partner agreements)
  - Credit Management (Credit Facilities, Limit Hierarchy, Revolving/Non-revolving/Secured Credit Accounts)
  - Accounting System (Accounting, Fees, Interest, Billing, Statements)
  - Payments Switch (real-time auth routing, network connectivity, scheme processing)
  - Payments Hub (clearing, settlement, posting; payment lifecycle orchestration)
  - Rewards System (Reward Programs, Rebate Programs at Account/Statement level)
  - FRM (real-time fraud scoring, transaction monitoring, risk decisioning)
  - Disputes Management (chargeback, representment, dispute lifecycle)
  - Consumer IAM (cardholder/member auth, credential management)
  - Enterprise IAM (bank staff, ESP staff, corporate admin auth and access control)
  - Notification (bank-originated; regulatory, fraud, lifecycle events; non-suppressible)
  - Operations Hub (bank ops console; monitoring, exception handling, servicing)
  - Data Mart (bank-side analytical data; reporting, risk analytics, regulatory reporting)
- **Electron (ESP) — 7 subsystems:**
  - Client Contract Management (Corporate and Contract lifecycle; terms, scope, renewal)
  - Payment Product Management System (Account Variants, Virtual Card Variants, CPP assembly; component programs)
  - Payment Program Management System (Program config, Spend Programs, Booking/Settlement Profiles, eligibility, enrollment, member/card management)
  - Billing and Collections System (Consolidated Invoices, Relationship-level Rebates, Rewards, Volume Commitments, Auto Debit)
  - Bank Gateway (anti-corruption and translation layer between Electron and Tachyon)
  - Corporate Data Mart (program, invoice, transaction, member data; extracts and reports for corporates)
  - ESP Data Mart (analytics on Contracts, Products, Programs for ESP portfolio management)
- **Corporate Domain — Electron Portal + corporate systems:**
  - Electron Corporate Portal (Organization Management, Program Administration, Member & Enrollment, Financial Control, Operations)
  - AP Systems (e.g., SAP Ariba, Oracle AP, Coupa)
  - AR Systems
  - Expense Management (e.g., Concur, Navan, Brex)
  - Travel Booking (e.g., Amex GBT, CWT, Navan)
  - ERP / GL (e.g., SAP, Oracle, NetSuite)
  - Treasury (e.g., Kyriba, FIS)
  - IAM / Directory Services (e.g., Okta, Azure AD, Ping)
  - LoB Applications

**Infographic type:** Bounded context map — three domain zones with subsystem blocks

**Slide layout**
- *Three large zones* arranged horizontally or in an L-shape:
  - **Tachyon zone** (light blue): 14 subsystem blocks, grouped into clusters:
    - Customer & Partner: CLM, BaaS Management
    - Product & Credit: Product LM, Credit Management
    - Payments: Switch, Hub
    - Financial: Accounting, Rewards
    - Risk & Compliance: FRM, Disputes
    - Operations & Data: Consumer IAM, Enterprise IAM, Notification, Ops Hub, Data Mart
  - **Electron zone** (light green): 7 subsystem blocks with Bank Gateway explicitly at the Tachyon-Electron boundary
  - **Corporate zone** (light amber): Electron Portal as central hub with spoke connections to 8 external system types
- *Bank Gateway* visually bridges the Tachyon and Electron zones — it should be prominent, not buried

**Build notes**
- **Split candidate:** Consider splitting into 14a (Tachyon 14 subsystems + Electron 7 subsystems — the platform) and 14b (Corporate Domain systems + integration philosophy callout — the ecosystem). Breakpoint: after listing all Electron subsystems. 14a establishes the platform; 14b establishes the corporate ecosystem that plugs into it.
- The clustering of Tachyon subsystems helps visual scanability — do not present 14 undifferentiated boxes
- Do not use vendor names as primary labels for corporate systems — use functional names with vendor examples in parentheses
- The Bank Gateway is architecturally critical — it acts as the anti-corruption layer. Place it prominently at the domain boundary.
- Do not conflate Tachyon's Rewards System (account/statement level) with Electron's Billing and Collections (relationship-level rebates) — they operate at different granularities
- Do not conflate Consumer IAM and Enterprise IAM — they serve different populations

---

## Slide 15 - Context Boundaries and Integration Points

**Slide goal**
- Show how the subsystems from Slide 14 communicate across four well-defined boundaries: Bank↔ESP, ESP↔Corporate Portal, Bank↔Corporate (indirect), and Corporate Portal↔Corporate Systems. No domain reaches into another's internals.

**Why this matters**
- Clean boundaries are what make the three-domain model work under network-speed authorization constraints. The audience needs to see that integration is disciplined, not ad-hoc — each boundary has a clear data and control contract.

**What to include**
- **Bank ↔ ESP** (mediated through Bank Gateway):
  - Product redistribution: Product LM (Tachyon) → Bank Gateway → Payment Product Mgmt (Electron)
  - Authorization callbacks: Payments Switch → Bank Gateway → ESP/Corporate participation
  - Rewards/rebate split: Rewards System (Tachyon, account-level) vs Billing & Collections (Electron, relationship-level)
  - Data flow: Tachyon Data Mart → Bank Gateway → Corporate Data Mart / ESP Data Mart
- **ESP ↔ Corporate Portal:**
  - Program provisioning, enrollment workflows, billing and master statements, notification customization
- **Bank ↔ Corporate** (indirect, always mediated through ESP):
  - CF utilization and budget enforcement at authorization
  - Posting data flow (L1/L2/L3)
  - Regulatory and fraud notifications (non-suppressible, bank-originated)
  - Standing repayment instructions (auto-debit)
  - Settlement account registration
- **Corporate Portal ↔ Corporate Systems:**
  - AP: card issuance triggered from PO/invoice
  - ERP: posting data pushed to GL
  - AP/AR: reconciliation matching
  - Expense Management: expense report integration
  - Travel Booking: booking-linked issuance
  - Treasury: settlement positioning
  - IAM/Directory: member/user provisioning and authentication
  - LoB: spend event triggers

**Infographic type:** Architecture boundary diagram with labeled integration arrows

**Slide layout**
- *Main area:* Four boundary zones showing the three domains from Slide 14 with explicit arrows crossing each boundary, labeled with what crosses (data type, control action, or notification)
- *Bank Gateway* shown as the explicit bridge at the Bank↔ESP boundary — subsystem-to-subsystem connections labeled
- *Alternative:* Sequence-style diagram showing a transaction flowing: Corporate AP → Payment Program Mgmt → Bank Gateway → Payments Switch → Network → back through all layers

**Build notes**
- Do not show direct Bank↔Corporate connections except for non-suppressible notifications from Tachyon's Notification subsystem — everything else is mediated through the ESP
- The Corporate↔Corporate Systems boundary is where most integration complexity lives — do not oversimplify it
- The Bank Gateway will generate questions from technical audiences — be prepared with details on what it translates and what it blocks

---

## Slide 16 - Entity Model Across Domains

**Slide goal**
- Present the three-domain ER diagram showing all entities and their cross-domain relationships. This is the definitive structural reference for the architecture.

**Why this matters**
- The entity model makes the three-domain separation concrete and traceable. Every lifecycle step (Act 4) references entities introduced here. The cross-domain mappings (Budget→Limit Hierarchy, Spend Program→bank-enforced Spend Program, Purchase Category→Posting Category) are the architectural seams the audience must understand.

**What to include**
- Three-domain ER diagram (source: `3-domain-erd.md`) showing:
  - **Bank Domain (Tachyon):** Account Holder (LAH/RAH/HAH), Credit Facility, Limit Hierarchy, Account Product, Virtual Card Product, VBO, Account, Virtual Card, Token, Spend Program (bank-enforced), Posting Category
  - **ESP Domain (Electron):** ESP, Account Variant, Virtual Card Variant, Corporate Payment Product, Client Contract
  - **Corporate Domain (Electron Portal):** Organizational Unit, Corporate Payment Program, Budget Hierarchy, Spend Program (corporate-defined), Purchase Category, Booking Profile, Settlement Profile, Settlement Account, Member, Enrollment
- Key cross-domain mappings (shown as dashed lines):
  - Budget Hierarchy ↔ Limit Hierarchy (optional translation)
  - Spend Program (corporate) ↔ Spend Program (bank-enforced)
  - Purchase Category ↔ Posting Category
  - ESP ↔ VBO (registered as)
- Key cardinality notes:
  - Budget Hierarchy optionally translates to Limit Hierarchy; a Limit Hierarchy need not originate from a Credit Facility
  - Spend Program cascade: program-level applies to all enrollments; enrollment-level translates to per-Virtual Card and per-Token Spend Programs in Bank Domain
  - Budgets are made accessible to OUs; a Program can only draw from budgets of the OU it is associated with

**Infographic type:** Three-subgraph entity relationship diagram

**Slide layout**
- *Full slide:* Three-subgraph ER diagram with domain-colored backgrounds:
  - Left subgraph: Bank Domain (light blue)
  - Center subgraph: ESP Domain (light green)
  - Right subgraph: Corporate Domain (light amber)
- Solid arrows for within-domain relationships; dashed arrows for cross-domain mappings
- Use neutral dark gray for cross-domain arrows
- Entity labels should be readable without zooming — use abbreviations where the full name was already introduced (e.g., CF, VC, TKN, OU, PRG, SP)

**Build notes**
- The diagram from `3-domain-erd.md` is the source — do not simplify it; the completeness is the point
- Entity reference tables exist in the Appendix of `presentation-outline.md` — the speaker should reference these for deep dives, but they are not built as separate slides
- Do not try to fit entity details (descriptions, contexts) on this slide — the ER diagram shows structure and relationships; the Appendix tables provide detail
- Do not confuse Product with Variant — the bank creates Products; the ESP creates Variants
- Do not conflate OU with Legal Entity — they are distinct

---

## Slide 17 - The Derivation Chain

**Slide goal**
- Show how bank products become ESP variants become corporate programs — the derivation chain that connects the three domains. Make it concrete with the Meridian US Supplier example.

**Why this matters**
- The derivation chain demonstrates that each domain layer adds value without removing what the previous layer established. The bank retains credit and compliance; the ESP adds packaging; the corporate adds governance.

**What to include**
- Derivation chain: Account Product → ESP Account Variant → (combined with Virtual Card Variant) → Corporate Payment Product → Corporate Payment Program
- Credit Facility connects bank to corporate: CF per LE → Budget → Program → Account → Card
- What each layer retains/adds:
  - Bank retains: credit/AML/sanctions/compliance, delinquency, base fees, scheme obligations
  - ESP adds: branding, component programs (fees, rewards, notifications), commercial terms, onboarding
  - Corporate configures: budget allocation, spend program tightening, booking rules, eligibility, enrollment, settlement
- Meridian US Supplier example: Commonwealth AP-US-30 → Apex-AV-Standard + Apex-VCV-Visa → Apex Supplier Pay CPP → Meridian US Supplier Payments Program → CF-US-Meridian ($50M) → Procurement Budget ($30M) → Account → Single-use cards per invoice

**Infographic type:** Horizontal derivation flow with three domain columns

**Slide layout**
- *Main area:* Left-to-right flow diagram with three columns (Bank / ESP / Corporate), each using domain colors
  - Bank column: Account Product + Virtual Card Product + Credit Facility
  - ESP column: Account Variant + Virtual Card Variant → CPP
  - Corporate column: Program → Budget → Account → Cards
- *Below flow:* Three-row summary — "Bank retains" / "ESP adds" / "Corporate configures" — each with a compact bullet list

**Build notes**
- Each layer adds without removing — this is a key point. The speaker should emphasize the additive nature.
- The CF → Budget connection is critical: it is how financial capacity flows from bank to corporate. Do not skip it.
- Do not suggest entities are "copies" across domains — each domain owns its own representation

---

## Slide 18 - Hierarchies — Corporate's and ESP's View

**Slide goal**
- Show that the corporate operates through three independent but correlated hierarchies — Credit, Organizational, and Settlement — each answering a different governance question, correlated at the Program level.

**Why this matters**
- This is the architectural realization of Slide 6's "coordinate system of independent dimensions." The audience sees that the platform does not force these into a single tree — they remain independent, correlated where needed.

**What to include**
- Three hierarchies:
  - Credit: Corporate → LAH → CF → Budget/Limit Hierarchy → Program → Account → Cards — "How much can we spend?" (risk-anchored, bank-enforced)
  - Organizational: Corporate → OU → Program → Account → Cards — "Who owns this spend?" (governance-anchored, corporate-defined)
  - Settlement: Corporate → Settlement Accounts → Programs → Account → Cards — "How do we pay for it?" (treasury-anchored, corporate-operated)
- Entity system-of-residence: CF in Tachyon, Budget in Electron, OU in Electron, Settlement Account external — all correlated at the Program level
- Meridian example: CF-US-Meridian ($50M, Tachyon) → Procurement Budget ($30M, Electron) → Supplier Payments Program (Electron) → Account (Tachyon) → Cards (Tachyon), with OUs and Settlement Accounts from corporate domain

**Infographic type:** Three parallel vertical hierarchies with correlation point

**Slide layout**
- *Three parallel vertical columns:* Credit hierarchy (light blue) / Organizational hierarchy (light amber) / Settlement hierarchy (neutral/gray)
- *Horizontal connection* at the Program level — a dashed line or bracket showing where all three hierarchies converge
- *System-of-residence labels* in small type next to each entity: "(Tachyon)" / "(Electron)" / "(External)"
- Domain colors applied to entity boxes based on where they reside, not which hierarchy they belong to

**Build notes**
- The three hierarchies must look independent — do not merge or nest them
- The correlation point at Program is the key structural insight — make it visually prominent
- Color-coding by system-of-residence (not by hierarchy) reinforces the three-domain model
- Contrast with Slide 19 (bank's view) — the corporate sees three hierarchies; the bank sees one

---

## Slide 19 - Hierarchies — Bank's View

**Slide goal**
- Show the bank's simpler, risk-anchored hierarchy and make explicit what the bank does not see — reinforcing that the separation is by design, not a limitation.

**Why this matters**
- The contrast with Slide 18 lands the architecture's clean separation. The bank focuses on risk and compliance; the corporate focuses on governance and operations. Neither domain leaks into the other.

**What to include**
- Bank's hierarchy: LAH → Credit Facility → Limit Hierarchy → Account → Cards
- What the bank does not see: departments, cost centers, project codes, budget allocations, OU trees, settlement preferences, member roles, enrollment logic
- What the bank enforces:
  - Credit Facility capacity
  - Budget hierarchy (utilization at authorization, all ancestors checked — even though the budget hierarchy is a corporate construct)
  - Spend Program controls (as defined by the effective policy cascade)
  - Non-overridable controls (AML, sanctions, fraud, delinquency, NPA, regulatory holds)
- This separation is by design: the bank focuses on risk and compliance; the corporate focuses on governance and operations

**Infographic type:** Simple vertical hierarchy with "invisible" elements grayed out

**Slide layout**
- *Left side (50%):* Simple vertical hierarchy: LAH → CF → Limit Hierarchy → Account → Cards. All in light blue (Bank domain). Clean, uncluttered.
- *Right side (50%):* "What the bank does not see" — grayed-out list of corporate concepts (departments, cost centers, project codes, budget allocations, OUs, settlement preferences, member roles). Visually dimmed to reinforce absence.
- *Below the hierarchy:* Four enforcement items as a compact strip: CF capacity / Budget hierarchy / Spend Programs / Non-overridable controls

**Build notes**
- The grayed-out elements are the visual payoff — they reinforce the clean separation principle from Slide 12
- Do not make the bank's limited view sound like a weakness — frame it as intentional separation of concerns
- Key nuance: the bank enforces budgets but does not define them. It checks the budget node and all ancestors at authorization — it does not know why the budget exists or who created it.
- This slide pairs with Slide 18 — consider keeping them as a visual pair (same layout structure, contrasting content)

---

## Act 4 — Program Lifecycle and Extensibility

---

## Slide 20 - Large-Scale Virtual Card Program Lifecycle — Overview

**Slide goal**
- Present the complete 34-step lifecycle across five phases as a single visual overview. The audience should see the full scope — from Client Contract initiation to dispute resolution — before the detail slides (21-24) unpack each phase.

**Why this matters**
- The lifecycle overview demonstrates that the platform handles the entire operational reality, not just authorization. Bank prospects need to see that contracting, onboarding, corporate configuration, program operations, and financial management are all architected — not bolted on.

**What to include**
- Five phases with step counts:
  - **Contracting & Onboarding** (ESP-driven, steps 1-9): Client Contract → Legal Entities → underwriting → CF issuance → CPP assignment → commercial terms → portal access
  - **Corporate Account Configuration** (Corporate Admin-driven, steps 10-14): Users/OUs → member provisioning (AD, SAP, SCIM, SFTP, API) → budgets (CF-derived + ERP-imported) → Payable Accounts (multi-bank, GL-mapped) → ongoing master data maintenance
  - **Program Setup** (Corporate Admin-driven, steps 15-23): Program initiation per archetype → Spend Programs with Purchase Categories → Booking/Settlement Profiles → eligibility → enrollment (API/SFTP) → card issuance with tags → dispatch notifications
  - **Operations** (transaction-driven, steps 24-28): Authorization with cooperative callbacks → near-real-time portal visibility → notifications → fraud alerts → card lifecycle management
  - **Financial** (cycle-driven, steps 29-34): Bank statement per billing cycle → auto-debit → ESP invoice per contract date → three reconciliation channels → disputes → single-use card closure
- The lifecycle is the same across archetypes — what changes is archetype-specific behavior within each step
- Each phase involves different primary actors: ESP, Bank, Corporate Admin, System/automated

**Infographic type:** Horizontal timeline or swimlane journey map

**Slide layout**
- *Full slide:* Horizontal timeline with five phase sections, each visually distinct:
  - Phase bars with labels and step ranges: "Contracting & Onboarding (1-9)" / "Corporate Account Configuration (10-14)" / "Program Setup (15-23)" / "Operations (24-28)" / "Financial (29-34)"
  - Key milestone markers within each phase (3-5 per phase, not all 34 steps)
  - Actor labels above or below each milestone: ESP (light green), Bank (light blue), Corporate Admin (light amber), System (neutral gray)
- *Alternative:* Three-lane swimlane (Bank / ESP / Corporate) with steps placed in the lane of the primary actor, connected by handoff arrows

**Build notes**
- **Split candidate:** Consider splitting into 20a (Contracting & Onboarding + Corporate Account Configuration, steps 1-14) and 20b (Program Setup + Operations + Financial, steps 15-34). Breakpoint: after step 14 — the first half is relationship setup; the second half is program operations. 20a shows the "getting started" journey; 20b shows the "running the program" journey.
- Do not try to show all 34 steps on one slide — show phase-level structure with 3-5 key milestones per phase. Slides 21-24 provide the detail.
- Do not make this look like a sequential waterfall — Corporate Account Configuration and Operations involve ongoing, concurrent activity
- The handoff at step 9 (portal access provisioned) is a key boundary — mark it visually

---

## Slide 21 - Contracting, Onboarding, and Corporate Account Configuration

**Slide goal**
- Detail the journey from Client Contract initiation to a fully configured corporate account ready for program creation. Show the handoff from ESP-driven contracting to corporate admin-driven configuration.

**Why this matters**
- Bank prospects need to see that credit underwriting stays firmly in their domain (steps 4-6), while the ESP handles contract management and product assignment. The corporate admin takes over only after the platform relationship is established — and can self-serve from that point.

**What to include**
- **Contracting & Onboarding** (ESP-driven, steps 1-9):
  - ESP initiates Client Contract → identifies Legal Entities → collects underwriting information
  - CF applications submitted per LAH (each LAH may apply for multiple CFs with distinct underwriting document sets)
  - Bank completes underwriting, issues CFs, notifies LAH billing contacts (Tachyon)
  - ESP assigns Corporate Payment Products across Spend Archetypes per corporate's requirements
  - ESP configures relationship-level commercial terms (Rebates, Volume Commitments) against the Client Contract
  - ESP provisions corporate portal access credentials — marks the transition to corporate-driven activity
- **Corporate Account Configuration** (Corporate Admin-driven, steps 10-14):
  - Admins configure corporate account — add users, set up OUs reflecting policy enforcement needs
  - Member provisioning through system integrations: Active Directory (employees), SAP (vendors/suppliers), SCIM (identity provisioning), SFTP (bulk import from non-integrated systems), Member Management API (programmatic access)
  - Budgets created against Credit Facilities and distributed across OUs; ERP-defined budgets imported through integration — budget hierarchy can reside independent of the CF hierarchy
  - Payable Accounts configured: multiple accounts at various banks registered for receiving invoices and making repayments; each maps to a GL in ERP
  - Ongoing maintenance of OU, Budget, Member, and Payable Account master data through API or SFTP integrations

**Infographic type:** Three-lane swimlane showing handoff sequence

**Slide layout**
- *Three horizontal lanes:* ESP (light green) / Bank (light blue) / Corporate Admin (light amber)
- *Steps placed in the lane of the primary actor:* Steps 1-3 and 7-9 in ESP lane; Steps 4-6 in Bank lane; Steps 10-14 in Corporate Admin lane
- *Handoff arrows* between lanes: ESP→Bank (underwriting request), Bank→ESP (CF issued, decision notified), ESP→Corporate (portal access provisioned)
- *Right side callout:* Corporate Account Configuration summary — OUs, Members, Budgets, Payable Accounts — as a checklist with integration channel annotations (AD, SAP, SCIM, SFTP, API)

**Build notes**
- Do not conflate ESP onboarding (one-time platform setup) with corporate onboarding (per-client, repeated for each corporate)
- Do not skip KYB — it is per legal entity, not per corporate, and bank audiences care about regulatory compliance
- Payable Account setup is not trivial — it is where the corporate's treasury operations connect to the platform; give it adequate visual weight
- Budget hierarchy independence (from CF hierarchy) is an important architectural point — call it out

---

## Slide 22 - Program Setup and Enrollment

**Slide goal**
- Detail the journey from program creation through Spend Program configuration, profile setup, and member enrollment to first card in a member's hands. Explain the distinction between booking-limit and non-booking Spend Programs.

**Why this matters**
- This is where the governance architecture from Act 2 materializes into operational configuration. The Spend Program mechanics (Purchase Categories, booking-limit vs. non-booking, precedence, 5-ledger constraint) are key differentiators that bank architects will want to understand deeply.

**What to include**
- **Program Creation** (steps 15-18):
  - Admin initiates a Program for a specific Spend Archetype, selecting a CPP offered by ESP; links to Credit Facility, assigns to OU
  - Spend Programs configured using Purchase Categories — program-level Spend Programs define default controls (AMC, amount, currency, geography, velocity); enrollment-level Spend Programs allow further tightening per member or group
  - Each Spend Program must reference a CF-derived Budget (bank credit risk protection); may additionally reference Spend Program Budgets or static limits for corporate policy enforcement
  - Booking-limit Spend Programs: for ERP-imported Budgets, the Spend Program can designate that budget as the booking destination; highest-precedence booking-limit Spend Program determines posting attribution; precedence is a numeric value set by the corporate admin
  - Non-booking Spend Programs: concurrent usage gates — all applicable ones evaluated together; control usage, not attribution
  - Hard constraint: per posting, no more than 3 non-booking, non-CF external limits evaluated by Tachyon; exceeding this declines the transaction (max 5 limit ledgers updated per posting, excluding ancestor traversal)
  - Booking Profile configured: GL account, cost center, project/client code, capex/opex; static defaults or dynamic rules
  - Settlement Profile configured: linked to a registered Payable Account, billing entity, repayment method and timing
- **Enrollment** (steps 19-23):
  - Eligibility rules define who may be enrolled (member type, OU affiliation, approval requirements)
  - Members enrolled via API (ERP/enterprise integration) or SFTP — member may be employee, supplier, contractor, client, or the corporate itself (central recurring)
  - Enrollment triggers virtual card issuance: card returned immediately (API response), dispatched digitally (secured email/portal), or dispatched physically — depending on archetype and ESP card variant configuration
  - Card carries tags set at enrollment: PO number, invoice number, cost center, project code
  - Enrollment-level Spend Programs configured where member-specific controls differ from program defaults (e.g., for supplier payments, exact authorized amount)
  - Card dispatch notification includes relevant context (e.g., supplier receives PO number, invoice number, authorized amount in secured email)
- **Purchase Category / Posting Category distinction:**
  - Purchase Category: corporate domain concept; bank provides pre-defined categories; corporate/ESP can define additional ones using bank's data dictionary
  - Posting Category: bank domain concept; richer grammar including bank-side dimensions (e.g., authentication method, authenticating parties)
  - Purchase Category maps to Posting Category via anti-corruption translation at authorization

**Infographic type:** Program configuration flow with Spend Program evaluation pipeline

**Slide layout**
- *Top half (55%):* Flow diagram: CPP → Program → Spend Programs (with Purchase Categories and Budget references) → Booking Profile → Settlement Profile → Eligibility → Enrollment → Cards
- *Bottom half (45%):* Spend Program evaluation pipeline — a horizontal pipeline showing: Posting Category match → applicable Spend Programs identified → booking-limit resolution (highest precedence) → non-booking gates (concurrent) → 5-ledger constraint check → authorization outcome
- Use light amber for corporate-domain entities and light blue for bank-domain entities (Posting Category, bank-enforced Spend Programs) to show the domain crossing

**Build notes**
- The booking-limit vs. non-booking distinction is fundamental — these serve different purposes (attribution vs. usage gates). Make it visually clear.
- The 5-ledger constraint should not be framed as a limitation — frame it as an engineered bound on authorization path complexity
- Purchase Categories are how corporates express governance intent in their own vocabulary — do not skip them
- The supplier enrollment example (PO → card with tags → secured email with context) makes the abstract flow concrete — include it as a callout or annotation

---

## Slide 23 - Operations

**Slide goal**
- Detail day-to-day transaction processing, cooperative authorization (with a concrete supplier payment example), posting enrichment, monitoring, and card lifecycle management.

**Why this matters**
- Cooperative authorization is one of the platform's most distinctive capabilities — the ability for a corporate to participate in the authorization decision in real time, within network timeouts, without owning the final decision. The supplier three-way match example makes this tangible.

**What to include**
- **Authorization and Cooperative Authorization** (steps 24-25):
  - Bank's check cascade: card active → account active → CF capacity → budget capacity (ancestor chain) → Posting Category → Spend Program controls → non-overridable controls (AML, sanctions, fraud, regulatory holds)
  - Cooperative authorization: corporate configures endpoint per payment program; bank routes callback during authorization
  - Supplier payment example: supplier presents card with L2 data including invoice number → corporate's endpoint verifies invoice is approved in AP system, amount matches approved value → positive response adds approval data to authorization, posting continues through remaining checks → negative response captures reason, authorization declined
  - Bank retains final authority — even after positive cooperative authorization response, non-overridable controls still apply
  - Posting Enrichment: at clearing, corporate systems can enrich posting data with updated attribution (project codes, GL overrides, cost center reassignment) before final booking
- **Visibility and Monitoring** (steps 25-27):
  - Corporate Portal reflects all transactions (authorized and cleared) per virtual card and program in near-real-time
  - Notifications: authorization approvals/declines, clearance confirmations, card expiry, closure
  - Fraud notifications: bank-originated, non-suppressible
  - Budget monitoring: threshold-based alerts (e.g., 75%, 90% utilization) at budget and program level
- **Card Lifecycle Management** (step 28):
  - Suspend, reactivate, close, replace, modify limits — within program policy bounds
  - Card replacement preserves enrollment, Spend Programs, and tags; new card inherits same controls
  - Single-use cards automatically closed after use and grace period

**Infographic type:** Authorization sequence diagram with monitoring dashboard callout

**Slide layout**
- *Left side (60%):* Sequence diagram showing the authorization flow:
  - Supplier → Network → Bank (check cascade, vertical steps) → cooperative auth callback to Corporate's AP system → response → remaining checks → decision → posting
  - Annotate the cooperative authorization callback as the distinctive step
  - Show posting enrichment as a separate step at clearing
- *Right side (40%):* Monitoring summary as a compact dashboard mockup:
  - Near-real-time transaction feed
  - Budget utilization bars
  - Notification indicators
  - Card lifecycle actions strip (suspend / reactivate / close / replace)

**Build notes**
- The three-way match example (PO from card tags + invoice from L2 + AP verification from callback) is the most concrete illustration of cooperative authorization's value — make it prominent
- Do not make cooperative authorization seem mandatory — it is optional, configured per program
- Do not suggest corporates can override bank fraud decisions or non-overridable controls
- Posting enrichment is a separate capability from cooperative authorization — they happen at different points (authorization vs. clearing)

---

## Slide 24 - Financial Phase

**Slide goal**
- Detail the dual billing streams, three reconciliation channels, dispute resolution, and single-use card closure. Emphasize that bank and ESP billing cycles are structurally independent.

**Why this matters**
- The financial phase is where the operational value of the architecture materializes for the corporate CFO: automated billing, multiple reconciliation channels, and dispute resolution that respects booking attribution. The structural independence of bank and ESP billing cycles is a key design decision the audience should appreciate.

**What to include**
- **Bank Billing** (steps 29-30):
  - Bank generates program statement per billing cycle (configured in Settlement Profile) — includes computation of rebates and rewards; invoices the net value
  - Statement received in corporate's registered Payable Account; auto-debited via ACH or intra-bank rails as applicable
  - For multi-account programs (e.g., employee spend with 200+ accounts), bank generates a consolidated master statement
- **ESP Billing** (step 31):
  - ESP invoices corporate for its services per Client Contract billing date — separate from bank's program billing cycle
  - ESP computes relationship-level rewards, rebates, and volume commitments; invoices the net
  - ESP has access to all program postings and bank statements sent to the corporate
  - When bank and ESP are the same entity, cycles can align — but corporates may configure different billing cycles per program, causing structural divergence
- **Reconciliation** (step 32):
  - Three channels: (1) near-real-time postings in Corporate Portal — corporate systems may already be updated before statement arrives; (2) bank provides rich data extract with each statement; (3) ESP provides data through a data mart
  - Corporate uses any combination of these three channels
  - Reconciliation targets vary by archetype: PO/invoice match (supplier), expense reports (employee), itineraries (travel), contracts (recurring)
- **Disputes and Card Closure** (steps 33-34):
  - Corporate can raise a dispute against any posting at any time from the Corporate Portal
  - Dispute credits follow original booking attribution (same GL, cost center, project code)
  - Single-use cards deemed closed after use and grace period; all card statuses visible in Corporate Portal

**Infographic type:** Dual billing timeline with reconciliation flow

**Slide layout**
- *Top half (50%):* Dual billing timeline showing two parallel cycles:
  - Upper timeline: "Bank Billing" — per program, per Settlement Profile cycle. Light blue. Shows statement generation → Payable Account receipt → auto-debit.
  - Lower timeline: "ESP Billing" — per Client Contract billing date. Light green. Shows ESP invoice → net computation → corporate receipt.
  - Visual marker showing the cycles are independent (different start/end dates, different frequencies possible)
- *Bottom half (50%):* Reconciliation flow:
  - Three input channels (near-real-time postings / bank data extract / ESP data mart) shown as three parallel pipes converging on "Corporate Reconciliation"
  - Dispute initiation shown as a side branch from "Corporate Portal" to "Disputes Management"
  - Single-use card closure shown as an automated terminal step

**Build notes**
- The structural independence of bank and ESP billing cycles is a key design decision — visualize it clearly with non-aligned timelines
- Do not conflate bank billing (per program, per Settlement Profile) with ESP billing (per contract, per Client Contract) — they are structurally independent
- Rebate split operates at different granularities: product-level (Tachyon, interchange-based) and relationship-level (Electron, aggregate-based) — computed in different systems
- Do not suggest reconciliation depends solely on statement delivery — near-real-time postings may have already updated corporate systems before the statement arrives
- Dispute credits following original booking attribution is an important detail — it means the corporate's GL entries remain clean without manual adjustments

---
