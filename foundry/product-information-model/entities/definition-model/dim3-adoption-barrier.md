# Adoption Barrier

**Model:** Definition Model
**Dimension:** Dimension 3: The Customer Value Dimension (Why Buy)
**Owner:** Product Management, Sales, Customer Success

## Definition

A known impediment to purchase or adoption within a Customer Segment. Barriers capture the "Why NOT buy" logic that complements the "Why Buy" logic of other Dim 3 entities. They may originate from sales objection tracking, churn analysis, lost-deal reviews, or customer research.

## Purpose

Understanding barriers is as important as understanding outcomes. A product can deliver great ROI but fail if barriers aren't addressed. Adoption Barriers:
- Inform discovery prioritization — a barrier may surface as a Signal (Problem or Need) in Dim 1
- May directly challenge or undermine a Customer Promise — exposing gaps between what the product promises and what prevents the customer from realizing that promise
- Guide investment decisions — overcoming a Blocker-severity barrier for a high-value segment may warrant an Initiative

## Barrier Types

| Type | Description | Example |
|---|---|---|
| **Regulatory** | Legal, compliance, or government requirements | "LATAM enterprises require local data residency" |
| **Technical** | Integration complexity, infrastructure requirements, migration difficulty | "No self-service onboarding — requires API integration expertise" |
| **Organizational** | Internal process, team structure, or change management challenges | "Buyer's AP team resists workflow changes — entrenched manual processes" |
| **Competitive** | Lock-in to competitor products, switching costs, sunk costs | "Existing investment in Competitor X's reporting suite" |
| **Financial** | Budget constraints, unexpected total cost, pricing misalignment | "Mid-market budget ceiling of $50K/year; product minimum is $75K" |
| **Contractual** | Existing agreements, migration penalties, vendor lock-in terms | "3-year contract with incumbent expires in 18 months; early termination penalty" |
| **Data** | Data migration complexity, portability concerns, data quality gaps | "10 years of transaction history in proprietary format — migration estimated at 6 months" |
| **Cultural** | Organizational change resistance, trust deficit, risk aversion | "Risk-averse financial institution requires 12-month proof-of-concept before enterprise commitment" |

## Fields

| Field | Type | Description |
|---|---|---|
| Customer Segment | Reference (Dim 3) | Which segment this barrier affects |
| Barrier Type | Enum | `Regulatory` / `Technical` / `Organizational` / `Competitive` / `Financial` / `Contractual` / `Data` / `Cultural` |
| Description | Text | What the barrier is and why it prevents adoption |
| Severity | Enum | `Blocker` (cannot adopt) / `Friction` (can adopt but with difficulty) |
| Challenges Promise | List of References (Dim 3) | Which Customer Promise(s) this barrier undermines or contradicts |
| Structural Root (Dim 8) | List of References (Dim 8) | When the barrier points to a product gap, which Capability or Feature is missing or insufficient. Enables product-level impact analysis. Optional — non-product barriers (Contractual, Cultural, Financial) typically have no product root. |

## Statuses

| Status | Description |
|---|---|
| Active | Barrier is currently preventing adoption |
| Mitigated | Barrier has been addressed (through product changes, workarounds, or market shifts) |
| Accepted | Barrier is acknowledged but not being addressed (documented trade-off) |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Blocks | Customer Segment (Dim 3) | Adoption Barrier blocks a Customer Segment |
| Challenges | Customer Promise (Dim 3) | Barrier may undermine or contradict a Customer Promise |
| May surface as | Signal (Dim 1) | Barrier may generate a Problem or Need Signal |
| May inform | Initiative (Dim 1) | Overcoming a barrier may become an Initiative |
| Work Model | Modeling Task (Track 1) | Modeling Tasks identify and document barriers |
| Structural root | Capability / Feature (Dim 8) | When barrier points to a product gap, identifies the missing or insufficient product structure |

## Examples

- "LATAM enterprises require local data residency for regulatory compliance" (Regulatory, Blocker) — **challenges** Compliance Posture "GDPR compliant" — **structural root:** Data Storage — Regional Residency (Capability — missing)
- "Mid-market companies lack IT staff for API integration — need self-service onboarding" (Technical, Friction) — **challenges** Value Proposition "Get started in under 24 hours" — **structural root:** Self-Service Onboarding (Value Stream — insufficient)
- "Existing customers have sunk cost in Competitor X's reporting suite" (Competitive, Friction) — no product root
- "Mid-market budget ceiling of $50K/year; product minimum starts at $75K" (Financial, Blocker) — no product root
- "3-year contract with incumbent; early termination penalty of $200K" (Contractual, Blocker) — no product root
- "10 years of transaction history in proprietary format — estimated 6-month migration" (Data, Friction) — **structural root:** Data Migration (Capability — insufficient)
- "Risk-averse institution requires 12-month PoC before enterprise commitment" (Cultural, Friction) — **structural root:** Sandbox / Demo Environment (Capability)
