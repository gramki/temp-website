# Business Model

**Model:** Definition Model
**Dimension:** Vendor Value
**Owner:** Executive Leadership, Product Marketing

## Definition

The fundamental revenue engine that describes how the vendor generates income from this product. The Business Model is the structural root of Dimension 2 — all other entities (Pricing Tiers, Value Metrics, Win Outcomes, KPIs) derive from or operate within the Business Model.

## Purpose

Anchors the Vendor Value dimension by establishing the macro-level commercial structure. The Business Model is a lightweight, rarely-changing entity — it provides context for the more dynamic entities in Vendor Value. It changes at the scale of years (e.g., shifting from perpetual license to SaaS), not quarters.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Descriptive name (e.g., "Transaction-based B2B SaaS") |
| Revenue Model Type | Enum | `Subscription` / `Transaction-based` / `Usage-based` / `License` / `Marketplace` / `Hybrid` |
| Revenue Streams | List (text) | Distinct revenue sources — e.g., "Per-transaction fees, FX markup, Platform subscription, Implementation services" |
| Target Markets | List of References (Customer Value) | Which Customer Segments this business model serves |
| Cost Structure Summary | Text | Key cost categories — infrastructure, compliance, support, sales. Not a full cost model; enough for unit economics context. |
| _Other fields to be refined._ | | |

## Lever Portfolio

The Business Model defines the product's **Lever Portfolio** — the finite, referenceable set of categorical levers available to advance Win Outcomes. Initiatives reference this portfolio when declaring their lever mix. Different products have different lever mixes — a developer API platform may not have a Sales Enablement lever; an enterprise SaaS product may use all five.

| Lever | What it covers | Primary Track | AAARRR Affinity |
|---|---|---|---|
| **Product** | Feature development, capability enhancement, UX improvement | Discovery → Build | All stages (esp. Activation, Retention) |
| **GTM** | Marketing, demand gen, pricing communication, partnership/channel execution, launch, positioning | Win | Awareness, Acquisition, Referral |
| **Sales Enablement** | Competitive tools, demo environments, POC toolkits, sales training | Win | Acquisition, Activation |
| **Customer Success** | Onboarding programs, health monitoring, retention, expansion, advocacy | Win | Activation, Retention, Revenue, Referral |
| **Operational** | Internal process, tooling, automation, hiring, training | Operating Model | All stages |

> **Design vs. Execution boundary:** The lever portfolio captures the *execution* side. Pricing *design* (tier structure, rates) is a Vendor Value / Discovery concern modeled through Modeling Tasks. Partnership *strategy* (who to partner with) is a Strategy/Vendor Value strategic decision. GTM covers pricing *communication*, partnership *execution*, and marketing *execution*.

## Statuses

_Not applicable — the Business Model is a structural descriptor that changes extremely rarely. When it does change, it is a company-level strategic event warranting its own PDR._

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Downstream | Pricing Tier / Package (Vendor Value) | Business Model defines the commercial frame for Packages |
| Downstream | Value Metric (Vendor Value) | Business Model defines available pricing axes |
| Context for | Win Outcome (Vendor Value) | Business Model provides the commercial context for Win Outcomes |
| Context for | Business KPI (Vendor Value) | Business Model determines which KPIs are relevant |
| Serves | Customer Segment (Customer Value) | Business Model targets specific segments |
| Defines | Lever Portfolio | Business Model defines the available levers for Win Outcomes and Initiatives |

## Example

"Transaction-based B2B SaaS"
- Revenue Streams: Per-transaction fee (0.5% flat), FX markup (1% on baseline rate), Monthly platform fee ($5K Enterprise), Implementation services (one-time)
- Target Markets: LATAM Enterprise, US Enterprise, US Mid-Market
- Cost Structure: FX provider fees (variable), cloud infrastructure (scaling), compliance/audit (annual), implementation consultants (per-customer), support staffing (per-segment)
