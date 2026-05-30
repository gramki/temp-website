# Delivery Friction

**Model:** Definition Model
**Dimension:** Vendor Value
**Owner:** Product Management, Product Marketing

## Definition

A specific, concrete suffering or inefficiency experienced by a Win Stakeholder in the vendor's AAARRR journey. Delivery Frictions are discoverable — they surface through field experience and must be investigated, not assumed. A Delivery Friction describes what the *vendor* suffers in serving a specific Customer Segment; it is distinct from Pain (Customer Value), which describes what the *user* suffers.

## Purpose

Analogous to Pain (Customer Value), which captures user-level suffering that motivates the buyer to purchase. Delivery Friction captures vendor-level suffering that undermines the product's commercial success. Without Delivery Friction:
- Opportunity Signals (Strategy) referencing vendor-side problems have no structured Vendor Value entity to point to
- The "cost" side of the vendor's economics is invisible — only revenue is modeled
- Product decisions to improve vendor-side workflows (e.g., "build self-service onboarding") have no explicit pain to trace to

**Discovery process:** Delivery Frictions are observed by Win Stakeholders in the field, surfaced as Signals (Problem or Opportunity) in Strategy, investigated through Discovery, and formally documented in Vendor Value through Modeling Tasks triggered by PDRs. Win Stakeholders are Signal *sources*, not entity authors.

**Relationship to Customer Value Pain:** Pain (Customer Value) is endured by User Persona (User Experience), cared about by Buying Persona (Customer Value). Delivery Friction is endured by Win Stakeholder (Vendor Value), suffered by the vendor. Same analytical structure, different beneficiary. In some cases, the same underlying issue manifests as both: "slow onboarding" is a Pain for the customer's IT team (Customer Value) AND a Delivery Friction for the Implementation Consultant (Vendor Value).

## Fields

| Field | Type | Description |
|---|---|---|
| Title | String | Concise description of the friction |
| AAARRR Stage | Enum | `Awareness` / `Acquisition` / `Activation` / `Retention` / `Revenue` / `Referral` |
| Endured by | Reference (Vendor Value) | Which Win Stakeholder(s) experience this friction |
| Customer Segment | Reference (Customer Value) | Which segment this friction is associated with (directly or through Win Stakeholder) |
| Impact | Text | Quantified impact — cost, time, revenue loss, opportunity cost |
| Undermines Win Outcome | Reference (Vendor Value) | Which Win Outcome(s) this friction makes harder to achieve |
| Rooted in (Structural) | List of References (Structural) | When the friction has a product root cause, which Module(s) or Capability(ies) are involved. Enables structural root-cause analysis. Optional — operational frictions (e.g., "manual renewal tracking") may have no product root. |

## Statuses

| Status | Description |
|---|---|
| Identified | Friction has been documented (via Modeling Task from PDR) |
| Under Investigation | Discovery work is investigating root causes or solutions |
| Mitigated | Product or process changes have reduced the friction (not eliminated) |
| Resolved | Friction has been eliminated through product changes |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Endured by | Win Stakeholder (Vendor Value) | Win Stakeholders experience this friction in their AAARRR work |
| Scoped to | Customer Segment (Customer Value) | Delivery Friction is associated with specific segments |
| Undermines | Win Outcome (Vendor Value) | Delivery Friction makes Win Outcomes harder to achieve |
| May surface as | Signal — Problem or Opportunity (Strategy) | Field observations of friction become Signals for Discovery |
| Work Model | Modeling Task (Discovery) | Modeling Tasks document Delivery Frictions in Vendor Value |
| Rooted in | Module / Capability (Structural) | When friction has a product root cause, identifies the structural source |

## Examples

| Friction | Stage | Endured by | Segment | Impact | Undermines | Rooted in (Structural) |
|---|---|---|---|---|---|---|
| "Custom FX provider integration per customer" | Activation | Implementation Consultant | LATAM Enterprise | $80K per-customer cost; 60-day delay | "First live transaction within 30 days" | FX Module — Integration Capability |
| "POC requires 6 weeks because sandbox lacks LATAM currencies" | Acquisition | Pre-Sales Engineer | LATAM Enterprise | 42-day POC extends 90-day sales cycle to 132 days | "Close deals within 90-day cycle" | Sandbox / Demo Environment (Capability) |
| "30% of implementations stall at data migration" | Activation | Implementation Consultant, CS Manager | LATAM Enterprise | 30% go-live failure rate; customer frustration | "First live transaction within 30 days" | Data Migration (Capability) |
| "Manual renewal tracking for 200+ accounts" | Retention | CS Manager | US Mid-Market | 15% of renewals missed or late; churn | "95% gross retention rate" | — (operational process) |
| "No self-service trial; every prospect requires AE engagement" | Acquisition | Account Executive | US Mid-Market | High CAC ($15K) for $30K ACV deals | "Self-service onboarding within 4 hours" | Self-Service Onboarding (Value Stream) |
