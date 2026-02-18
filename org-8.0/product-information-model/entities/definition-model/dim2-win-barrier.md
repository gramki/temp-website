# Win Barrier

**Model:** Definition Model
**Dimension:** Dimension 2: The Vendor Value Dimension (Why It Wins)
**Owner:** Product Marketing, Sales Leadership

## Definition

A known structural impediment that prevents the vendor from achieving a Win Outcome for a given Customer Segment. Always articulated with the aggrieved party as a Win Stakeholder or the vendor generally. Distinct from Adoption Barrier (Dim 3), which captures the *customer's* impediment to purchasing or adopting. Win Barrier captures the *vendor's* impediment to winning commercially.

## Purpose

Analogous to Adoption Barrier (Dim 3), which captures what blocks the customer from buying or adopting. Win Barrier captures what blocks the vendor from succeeding commercially. Without Win Barriers:
- Competitive threats, market limitations, and structural disadvantages have no Dim 2 home
- Product decisions to address vendor-side blockers (e.g., "add free trial to compete") lack a formal entity to trace to
- The gap between "what we want to achieve" (Win Outcomes) and "what prevents us" (Win Barriers) is implicit

**Distinction from Delivery Friction:** Delivery Friction is an *operational* pain endured by Win Stakeholders in their daily work (e.g., "custom integration costs $80K per customer"). Win Barrier is a *structural* impediment that blocks Win Outcomes at a segment level (e.g., "competitor offers 30-day free trial; we require annual commitment"). Frictions can be mitigated incrementally; barriers often require strategic decisions (PDRs) to address.

## Fields

| Field | Type | Description |
|---|---|---|
| Title | String | Concise description of the barrier |
| Type | Enum | `Competitive` / `Technical` / `Regulatory` / `Operational` / `Financial` / `Contractual` / `Resource` / `Market` |
| AAARRR Stage | Enum | `Awareness` / `Acquisition` / `Activation` / `Retention` / `Revenue` / `Referral` |
| Customer Segment | Reference (Dim 3) | Which segment this barrier blocks |
| Aggrieved Party | Reference (Dim 2) or "Vendor" | Which Win Stakeholder is affected, or the vendor broadly |
| Impact on Win Outcome | Text | Which Win Outcome is blocked and how |
| Challenges | Reference (Dim 2) | Which Pricing Tier or other Dim 2 entity is challenged |
| Structural Root (Dim 8) | List of References (Dim 8) | When the barrier points to a product gap, which Capability or Feature is missing or insufficient. Enables product-level impact analysis. Optional — non-product barriers (Financial, Contractual, Market) typically have no product root. |

## Statuses

| Status | Description |
|---|---|
| Identified | Barrier has been documented (via Modeling Task from PDR) |
| Under Investigation | Discovery work is investigating mitigation strategies |
| Mitigated | Partial mitigation in place (e.g., workaround, competitive positioning) |
| Resolved | Barrier has been eliminated through product or strategy changes |
| Accepted | Barrier is acknowledged and accepted — not worth addressing |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Blocks | Win Outcome (Dim 2) | Win Barrier prevents achieving specific Win Outcomes |
| Affects | Win Stakeholder (Dim 2) | Win Barrier impacts specific Win Stakeholders or the vendor |
| Scoped to | Customer Segment (Dim 3) | Win Barrier is specific to Customer Segment(s) |
| Challenges | Pricing Tier / Package (Dim 2) | Win Barrier may challenge the competitiveness of a Pricing Tier |
| May surface as | Signal — Problem or Opportunity (Dim 1) | Observations of barriers become Signals for Discovery |
| Work Model | Modeling Task (Track 1) | Modeling Tasks document Win Barriers in Dim 2 |
| Structural root | Capability / Feature (Dim 8) | When barrier points to a product gap, identifies the missing or insufficient product structure |

## Win Barrier Types

| Type | Description | Example |
|---|---|---|
| **Competitive** | Competitor advantage that the vendor cannot currently match | "Competitor offers 30-day free trial; our minimum is annual commitment" |
| **Technical** | Technical limitation in the product that blocks a segment | "We can't offer on-prem deployment; regulated LATAM banks require it" |
| **Regulatory** | Regulatory requirement the vendor doesn't yet meet | "We lack LGPD-compliant data residency in Brazil" |
| **Operational** | Operational limitation in how the vendor serves customers | "Our support doesn't cover LATAM time zones (UTC-3 to UTC-5)" |
| **Financial** | Pricing structure that doesn't work for a segment | "Our minimum ACV ($100K) exceeds Mid-Market budget ceiling ($50K)" |
| **Contractual** | Contractual constraints (vendor's or customer's existing) | "Target customers locked into competitor's 3-year enterprise agreements" |
| **Resource** | Insufficient vendor resources to serve a segment | "Only 2 implementation consultants available for LATAM region" |
| **Market** | Market perception or positioning gap | "Low brand awareness in LATAM fintech — no local reference customers" |

## Examples

| Barrier | Type | Stage | Segment | Aggrieved | Blocks Win Outcome | Structural Root (Dim 8) |
|---|---|---|---|---|---|---|
| "Competitor offers 30-day free trial" | Competitive | Acquisition | US Mid-Market | Account Executive | "Self-service onboarding within 4 hours" | Trial / Freemium (Capability — missing) |
| "No LGPD data residency in Brazil" | Regulatory | Acquisition | LATAM Enterprise | Account Executive, Pre-Sales Engineer | "Close LATAM deals within 90-day cycle" | Data Storage — Regional Residency (Capability — missing) |
| "Support hours don't cover LATAM time zones" | Operational | Retention | LATAM Enterprise | CS Manager, Support Engineer | "95% annual gross retention rate" | — (operational) |
| "Minimum ACV exceeds Mid-Market budget" | Financial | Acquisition | US Mid-Market | Account Executive | "Close Mid-Market deals at positive unit economics" | — (pricing) |
| "Only 2 implementation consultants for LATAM" | Resource | Activation | LATAM Enterprise | Implementation Consultant | "First live transaction within 30 days" | — (resource) |
