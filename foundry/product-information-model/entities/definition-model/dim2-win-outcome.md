# Win Outcome

**Model:** Definition Model
**Dimension:** Vendor Value
**Owner:** Product Marketing, Sales Leadership, Customer Success Leadership

## Definition

What success looks like for the vendor at a specific AAARRR stage for a specific Customer Segment. A Win Outcome is a structural definition of "what winning means here" — not a time-bound Objective (Strategy) but a persistent target that Objectives and Initiatives reference. Win Outcomes are scoped to Customer Segments because the definition of success varies dramatically by segment.

## Purpose

Analogous to Business Outcome (Customer Value), which captures what the *customer* needs to achieve. Win Outcome captures what the *vendor* needs to achieve — per AAARRR stage, per segment. Without Win Outcomes:
- Objectives (Strategy) lack granular commercial targets — "Expand to LATAM" doesn't specify what winning looks like at each stage
- Business KPIs float without context — "CAC < $25K" is a number; the Win Outcome explains *what commercial success that number represents*
- Without Win Outcomes, Initiative targets lack a structural definition to anchor to — they set quantitative measures without defining what "success" means

**Distinction from Objectives (Strategy):** An Objective is time-bound and strategic ("Expand to LATAM currencies by H2 2026"). A Win Outcome is structural and persistent ("LATAM Enterprise — Activation: first live transaction within 30 days of contract"). Objectives *reference* Win Outcomes as their commercial targets; Win Outcomes persist across Objectives.

## Fields

| Field | Type | Description |
|---|---|---|
| Title | String | Concise success statement |
| AAARRR Stage | Enum | `Awareness` / `Acquisition` / `Activation` / `Retention` / `Revenue` / `Referral` |
| Customer Segment | Reference (Customer Value) | Which segment this Win Outcome applies to |
| Success Definition | Text | What achieving this outcome means — qualitative and quantitative |
| Win Stakeholder(s) responsible | List of References (Vendor Value) | Who owns achieving this outcome |
| Business KPI(s) evidencing | List of References (Vendor Value) | Which KPIs measure whether this outcome is being achieved |
| Achievement Levers | List (Lever + Primary/Secondary) | Categorized from the Business Model's Lever Portfolio. Identifies what kinds of effort can advance this Win Outcome. Forces the question: "Is this primarily a product problem, a GTM problem, or both?" |
| Enabled by (Structural) | List of References (Structural) | When Product is an Achievement Lever, which Value Streams or Capabilities structurally support this outcome. Provides traceability from commercial target to product structure. Optional when Product is not a lever. |

## Statuses

| Status | Description |
|---|---|
| Draft | Win Outcome is being defined (during Deliberation or Modeling Task) |
| Active | Win Outcome is the current target — Objectives and Initiatives reference it |
| Revised | Win Outcome has been updated based on new evidence (prior version archived) |
| Retired | Win Outcome is no longer relevant for this segment |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Scoped to | Customer Segment (Customer Value) | Win Outcome is defined per Customer Segment |
| Evidenced by | Business KPI (Vendor Value) | Business KPIs measure whether Win Outcome is achieved |
| Responsibility of | Win Stakeholder (Vendor Value) | Win Stakeholders own specific Win Outcomes |
| Undermined by | Delivery Friction (Vendor Value) | Delivery Frictions make Win Outcomes harder to achieve |
| Blocked by | Win Barrier (Vendor Value) | Win Barriers structurally prevent achieving Win Outcomes |
| Referenced by | Objective (Strategy) | Objectives target specific Win Outcomes |
| Targeted by | Initiative (Strategy) | Initiatives target Win Outcomes with lever mix and embedded targets |
| Advanced by | Win Activity (Win) | Win Activities advance specific Win Outcomes |
| Supported by | Win Enablement (Win) | Win Enablement assets support achieving Win Outcomes |
| Assessed by | Win Review (Win) | Win Reviews assess progress toward Win Outcomes |
| Enabled by | Value Stream / Capability (Structural) | When Product is an Achievement Lever, identifies which product structures support this outcome |

## Examples

| AAARRR Stage | Segment | Win Outcome | Evidencing KPIs | Achievement Levers | Enabled by (Structural) |
|---|---|---|---|---|---|
| Awareness | LATAM Enterprise | "80% unaided brand recall in LATAM fintech CFO community" | Brand awareness score, LATAM inbound pipeline | GTM (primary), Product (secondary) | — |
| Acquisition | LATAM Enterprise | "Close LATAM enterprise deals within 90-day sales cycle at $500K+ ACV" | Sales cycle length, ACV, competitive win rate | Sales Enablement (primary), Product (secondary), GTM (secondary) | Sandbox / Demo Environment (Capability) |
| Activation | LATAM Enterprise | "Customer processes first live cross-border transaction within 30 days of contract" | Time-to-first-value, Activation rate | Product (primary), Customer Success (secondary) | Cross-Border Payout Processing (Value Stream) |
| Retention | LATAM Enterprise | "95% annual gross retention rate" | Churn rate, NPS, Health score | Customer Success (primary), Product (secondary) | Multi-Currency Reporting (Capability) |
| Revenue | LATAM Enterprise | "Net revenue retention 120% — expand through batch payouts and additional currencies" | NRR, Expansion revenue, Upsell conversion | Sales Enablement (primary), Customer Success (secondary) | Batch Payout Processing (Value Stream) |
| Referral | LATAM Enterprise | "30% of new LATAM pipeline sourced from customer referrals" | Referral rate, Case study participation | Customer Success (primary), GTM (secondary) | — |
| Acquisition | US Mid-Market | "Self-service onboarding with first API call within 4 hours" | Time-to-first-API-call, Self-serve conversion rate | Product (primary), GTM (secondary) | Self-Service Onboarding (Value Stream) |
