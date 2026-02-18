# Customer Segment

**Model:** Definition Model
**Dimension:** Dimension 3: The Customer Value Dimension (Why Buy)
**Owner:** Product Management, Product Marketing

## Definition

A defined group of potential buyers sharing common characteristics — industry vertical, company size, geography, maturity stage. Segments have distinct buyer personas, outcomes, promise expectations, and adoption patterns. All other Dim 3 entities are anchored to one or more Customer Segments.

## Purpose

Customer Segment is the organizing entity for the entire Customer Value Dimension. Without it, buyer personas are unanchored ("CFO" is too generic), business outcomes can't be differentiated by market, and Customer Promises can't be tailored. Segments also connect to Pricing Tiers (Dim 2), enabling segment-specific packaging and pricing.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Descriptive segment name (e.g., "LATAM Enterprise") |
| Industry Vertical | String | Target industry or industries |
| Company Size | Range | Employee count or revenue range |
| Geography | String | Target geography or region |
| Maturity Stage | Enum | Startup / Growth / Enterprise / Regulated |
| Key Characteristics | Text | Defining traits that distinguish this segment |
| Buying Motion | Enum | `PLG` (self-serve, trial-driven) / `SLG` (sales-led, relationship-driven) / `Hybrid`. How this segment typically evaluates and purchases. Influences Win Track engagement patterns and lever mix. |
| Segment Size (TAM) | Text | Estimated total addressable market — number of potential customers and/or revenue opportunity. Order-of-magnitude is sufficient for prioritization. |
| Revenue Potential | Text | Estimated revenue per customer and segment-level revenue target. Informs Pricing Tier design and Initiative prioritization. |
| Strategic Priority | Enum | `Primary` / `Secondary` / `Exploratory` / `Deprioritized`. Current investment priority — drives resource allocation across Initiatives. |
| Competitive Context | Structured (see below) | Per-segment competitive landscape summary |

### Competitive Context (structured field)

Each Customer Segment carries a competitive context that captures the segment-specific competitive landscape. This is the structural home for competitive intelligence — the Definition Model captures the structural positioning; detailed competitive playbooks and battlecards are Operating Model / Sales Enablement content.

| Sub-field | Type | Description |
|---|---|---|
| Key Competitors | List of Strings | Named competitors active in this segment |
| Competitive Position | Enum | `Leader` / `Challenger` / `Niche` / `New Entrant` — vendor's position relative to competitors in this segment |
| Primary Competitive Threats | List of References (Dim 2) | References to Competitive-type Win Barriers that affect this segment |
| Key Differentiators | Text | What distinguishes the vendor's offering in this segment (summary-level; detailed positioning lives in Value Proposition) |
| Incumbent / Status Quo | Text | What customers in this segment currently use (competitor product, manual process, in-house solution) |

## Statuses

| Status | Description |
|---|---|
| Draft | Segment is being defined |
| Active | Segment is actively targeted |
| Deprioritized | Segment is known but not currently targeted |
| Retired | Segment is no longer relevant |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Downstream | Buying Persona (Dim 3) | Segment has Buying Persona(s) |
| Downstream | Business Outcome (Dim 3) | Segment has Business Outcome(s) pursued by its Buying Personas |
| Downstream | Pain (Dim 3) | Segment has Pain(s) |
| Downstream | Customer Promise (Dim 3) | Segment is promised Customer Promise(s) |
| Downstream | Adoption Barrier (Dim 3) | Segment is blocked by Adoption Barrier(s) |
| Cross-dim | Pricing Tier / Package (Dim 2) | Segment may map to Pricing Tier(s) |
| Cross-dim | Win Outcome (Dim 2) | Win Outcomes are scoped to this Segment |
| Cross-dim | Win Barrier (Dim 2) | Win Barriers are scoped to this Segment (Competitive Context references Competitive-type barriers) |
| Work Model | Modeling Task (Track 1) | Modeling Tasks define/refine Segments |
| Work Model | Segment Engagement (Track 4) | Win Track engagements target specific Segments |

## Examples

**LATAM Enterprise**
- Industry: Financial services, 500+ employees, cross-border payables
- Buying Motion: SLG (sales-led, 90-day enterprise sales cycle)
- Segment Size (TAM): ~2,000 companies in LATAM with cross-border payment needs, $800M addressable
- Revenue Potential: $500K+ ACV per customer; segment target $50M ARR
- Strategic Priority: Primary
- Competitive Context:
  - Key Competitors: GlobalPay, CompetitorX, in-house treasury systems
  - Position: Challenger (strong product, limited LATAM brand awareness)
  - Primary Threats: "Competitor offers 30-day free trial" (Win Barrier), "No LGPD data residency" (Win Barrier)
  - Key Differentiators: Real-time FX rate locking, single-API multi-currency payout
  - Incumbent: Manual bank wires + spreadsheet-based FX hedging

**US Mid-Market**
- Industry: Cross-industry, 100–499 employees, domestic + occasional cross-border
- Buying Motion: Hybrid (PLG trial with sales assist for conversion)
- Segment Size (TAM): ~15,000 companies, $200M addressable
- Revenue Potential: $30K–50K ACV per customer; segment target $30M ARR
- Strategic Priority: Secondary
- Competitive Context:
  - Key Competitors: StripeConnect, PayPalBusiness, legacy bank solutions
  - Position: New Entrant (no brand recognition in segment)
  - Primary Threats: "Minimum ACV exceeds budget" (Win Barrier)
  - Key Differentiators: API-first, developer-friendly integration
  - Incumbent: PayPal / bank ACH transfers
