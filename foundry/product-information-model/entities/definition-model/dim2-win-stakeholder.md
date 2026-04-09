# Win Stakeholder

**Model:** Definition Model
**Dimension:** Dimension 2: The Vendor Value Dimension (Why It Wins)
**Owner:** Product Marketing, Sales Leadership, Customer Success Leadership

## Definition

A role in the vendor's AAARRR lifecycle — a specific function that engages with customers or prospects to make the product commercially successful. Each Win Stakeholder has distinct concerns, friction points, and success criteria at their stage(s) of the lifecycle. A Win Stakeholder is a functional archetype, not an organizational position — the same person may fill multiple Win Stakeholder roles, and multiple people may fill the same role.

> **Role definition, not agent identity.** Win Stakeholder is a **role** in the Definition Model. Specific people or AI agents who fulfill this role are tracked in the Workforce Repository (WFR); WFR agents reference this role definition via role bindings. External parties (customers, partners) that Win Stakeholders engage with are tracked in the External Stakeholder Registry (ESR). See DR-034.

## Purpose

Analogous to Buying Persona (Dim 3), which models the customer's buying committee. Win Stakeholder models the vendor's "winning committee" — the roles required for the product's commercial success across the full AAARRR lifecycle. Without Win Stakeholders:
- Delivery Frictions have no one who "endures" them — they're abstract vendor problems with no human face
- Win Outcomes have no one responsible — success criteria float without ownership
- Product decisions that affect vendor-side workflows (e.g., "build self-service onboarding to reduce implementation cost") have no explicit beneficiary to trace to

Win Stakeholders are **definition entities, not organizational roles**. The Operating Model will define team structures and staffing. Dim 2 defines what functional roles the product's commercial model *requires*. A startup may have one person covering Pre-Sales, Implementation, and CS; the Win Stakeholder model still distinguishes the three functions.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Descriptive role name (e.g., "Pre-Sales Engineer") |
| AAARRR Stage(s) | List of Enum | `Awareness` / `Acquisition` / `Activation` / `Retention` / `Revenue` / `Referral` |
| Key Concerns | Text | What this stakeholder cares about — their evaluation lens |
| Engaged Segments | List of References (Dim 3) | Which Customer Segments this stakeholder engages with |
| Delivery Frictions cared about | List of References (Dim 2) | Which Delivery Frictions this stakeholder endures or cares about |
| _Other fields to be refined._ | | |

## Statuses

_Not applicable — Win Stakeholder is a structural descriptor, not a lifecycle entity._

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Engaged with | Customer Segment (Dim 3) | Win Stakeholder engages with specific Customer Segments |
| Endures | Delivery Friction (Dim 2) | Win Stakeholder endures specific Delivery Frictions |
| Responsible for | Win Outcome (Dim 2) | Win Stakeholder is responsible for achieving Win Outcomes at their AAARRR stage |
| Aggrieved by | Win Barrier (Dim 2) | Win Barriers affect specific Win Stakeholders |
| Interacts with | Buying Persona (Dim 3) | Win Stakeholders interact with Buying Personas during the sales and implementation process |
| Fulfilled by | Agent (WFR) | Agents in WFR are bound to Win Stakeholder roles via role bindings (DR-034) |

## AAARRR Stage Mapping

| AAARRR Stage | Typical Win Stakeholders | Key Concerns |
|---|---|---|
| Awareness | Marketing Manager, Developer Advocate | Brand recognition, inbound pipeline, content reach |
| Acquisition | Account Executive, Pre-Sales Engineer, Solution Architect | Deal velocity, POC success, technical fit, competitive win rate |
| Activation | Implementation Consultant, Solution Architect, CS Manager | Time-to-first-value, integration success, go-live rate |
| Retention | CS Manager, Support Engineer | Health score, NPS, churn prevention, support quality |
| Revenue | Account Manager, Finance/Billing | ACV growth, upsell/cross-sell, net revenue retention |
| Referral | CS Manager, Marketing Manager | Referral pipeline, case study participation, community engagement |

## Examples

| Win Stakeholder | Stage(s) | Segment | Key Concern |
|---|---|---|---|
| Pre-Sales Engineer | Acquisition | LATAM Enterprise | "Can we demonstrate LATAM currency support in a 2-week POC?" |
| Implementation Consultant | Activation | LATAM Enterprise | "Can we get this customer live on cross-border payouts in 30 days?" |
| CS Manager | Retention, Referral | US Mid-Market | "Is this customer healthy enough to renew and refer?" |
| Account Manager | Revenue | LATAM Enterprise | "Can we expand this $500K deal to $750K with batch payouts?" |
