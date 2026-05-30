# User Persona

**Model:** Definition Model
**Dimension:** User Experience
**Owner:** UX Designers, Product Management

## Definition

A role archetype that uses the product's Human-Interactive Modules. A User Persona represents a distinct type of human who interacts with the product — their context, goals, frustrations, technical proficiency, and jobs to be done. User Personas are *users* of the product; they are distinct from Buying Personas (Customer Value), who are *purchasers* of the product.

> **Role definition, not agent identity.** User Persona is a **role** in the Definition Model — it describes a type of user, not a specific person. Internal agents (e.g., dogfood testers) who match this persona are tracked in the Workforce Repository (WFR). External users who match this persona at scale are not individually tracked; specific external users (e.g., beta participants, advisory board members) may be referenced in the External Stakeholder Registry (ESR). See DR-034.

**Role Basis:** Personas are defined by **product role** (what they do in the product — "Approver," "Analyst," "Admin") or **business domain role** (what they do in their organization — "AP Clerk," "Compliance Officer," "Treasury Analyst"). Both are valid bases. Product role personas emphasize the functional relationship with the product; business domain role personas emphasize the real-world context and jobs. Most personas combine both: "AP Clerk" is a business domain role, but their product role is "Payment Initiator." The product's RBAC (role-based access control) mapping — which features and journeys are available to which product roles — is a Structural / implementation concern, not a User Experience entity.

## Purpose

Anchors the Experience dimension by identifying *who* interacts with the product. Without User Personas:
- Jobs, Journeys, and Channels have no one to design for — they float without a subject
- Pain (Customer Value) has no one to endure it — Pain is "endured by User Persona, cared about by Buying Persona"
- Feature experience attributes (simplicity, delight, control) have no reference point — what delights an AP Clerk may frustrate a developer

**Distinction from Buying Persona (Customer Value):** A Buying Persona decides to purchase; a User Persona uses the product. They may overlap (a CFO who both approves budget and uses the executive dashboard) but often diverge (the CFO approves; the AP Clerk uses daily). User Personas endure Pains; Buying Personas *care about* those Pains.

**Discovery provenance:** User Personas are hypothesized during Signal Exploration, validated through Research Tasks (user interviews, contextual inquiry), and formalized through Modeling Tasks triggered by PDRs.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Descriptive role name (e.g., "AP Clerk," "Treasury Analyst") |
| Description | Text | Who this persona is — role context, daily responsibilities, organizational position |
| Customer Segment(s) | List of References (Customer Value) | Which segments this persona exists in (an AP Clerk at LATAM Enterprise vs. US Mid-Market may differ) |
| Goals | Text | What this persona wants to achieve when using the product |
| Frustrations | Text | What makes this persona's current experience painful or inefficient |
| Technical Proficiency | Enum | `Non-technical` / `Technical` / `Developer` — influences channel preference and feature complexity tolerance |
| Frequency of Use | Enum | `Daily` / `Weekly` / `Occasional` / `Rare` — influences journey design (power user vs. infrequent visitor) |
| Jobs (JTBD) | List of References (User Experience) | The Jobs this persona needs to accomplish |
| Preferred Channel(s) | List of References (User Experience) | Which UX Channel(s) this persona prefers or primarily uses. Influences channel investment priority and journey design. |

## Statuses

_Not applicable — User Persona is a structural descriptor. Changes are governed through PDRs (e.g., "We've identified a new persona: Compliance Auditor")._

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Has | Job (User Experience) | Persona has Jobs to be done |
| Follows | User Journey (User Experience) | Persona follows Journeys to accomplish Jobs |
| Prefers | UX Channel (User Experience) | Persona prefers specific Channel(s) |
| Endures | Pain (Customer Value) | Persona endures Pains (which Buying Personas care about) |
| Belongs to | Customer Segment (Customer Value) | Persona exists within Customer Segment(s) |
| Work Model | Research Task (Discovery) | Research Tasks validate Persona hypotheses |
| Work Model | Modeling Task (Discovery) | Modeling Tasks formalize Personas in User Experience |

## Examples

| Persona | Segment | Goals | Frustrations | Proficiency | Frequency | Jobs |
|---|---|---|---|---|---|---|
| AP Clerk | LATAM Enterprise | Process payouts accurately and quickly | Manual reconciliation, multiple systems, FX confusion | Non-technical | Daily | "Process cross-border payout," "Verify FX rate applied" |
| Treasury Analyst | LATAM Enterprise | Monitor FX exposure, optimize currency timing | Fragmented data, no real-time visibility, manual reporting | Technical | Daily | "Analyze FX exposure," "Generate treasury report" |
| Compliance Officer | LATAM Enterprise | Ensure regulatory compliance for all transactions | Manual OFAC screening, audit trail gaps | Technical | Weekly | "Verify OFAC screening completed," "Generate compliance audit report" |
| Finance Admin | US Mid-Market | Set up and manage payment workflows | Complex setup, no self-service, needs vendor support | Non-technical | Occasional | "Configure payment rules," "Manage user permissions" |
