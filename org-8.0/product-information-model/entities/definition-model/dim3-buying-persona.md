# Buying Persona

**Model:** Definition Model
**Dimension:** Dimension 3: The Customer Value Dimension (Why Buy)
**Owner:** Product Marketing, Sales

## Definition

A role within the purchasing organization's buying committee that influences or decides the purchase. Each Buying Persona represents a distinct evaluation lens — financial justification, technical fit, user advocacy, or internal championing. A Customer Segment may have multiple Buying Personas, and a real purchase typically requires alignment across several.

> **Renamed from "Economic Buyer Persona."** The original entity modeled only the budget holder. In enterprise B2B, purchases involve a buying committee where multiple roles evaluate the product through different lenses. Expanding to Buying Persona with role types captures this reality without creating separate entities per role.

## Purpose

Anchors the buying decision by identifying *all* the people who influence or decide the purchase within each segment — not just the check-signer. Different Buying Personas care about different things: the CFO cares about ROI and Business Outcomes; the CTO cares about integration complexity and security; the department head cares about user adoption and pain relief. Understanding each persona's concerns enables:

- Segment-specific messaging per role
- Mapping which Pains (Dim 3) each persona *cares about* (even if they don't personally endure them)
- Identifying where deals stall (which persona is unconvinced?)

## Role Types

| Role | What they evaluate | Typical title |
|---|---|---|
| **Economic Buyer** | ROI, cost justification, budget alignment | CFO, VP Finance, Procurement |
| **Technical Buyer** | Integration complexity, security, architecture fit, infrastructure requirements | CTO, VP Engineering, Enterprise Architect, IT Director |
| **User Buyer** | Usability, workflow fit, team adoption readiness | Department Head, Operations Manager, Team Lead |
| **Coach / Champion** | Internal politics, change management, vendor advocacy | Internal sponsor who navigates the buying process |

## Fields

| Field | Type | Description |
|---|---|---|
| Title / Role | String | The persona's title (e.g., "CFO", "CTO") |
| Role Type | Enum | `Economic Buyer` / `Technical Buyer` / `User Buyer` / `Coach / Champion` |
| Customer Segment | Reference (Dim 3) | Which segment this persona belongs to |
| Decision Authority | Text | What they can approve, veto, or influence |
| Key Concerns | Text | What this persona cares about in evaluating a purchase |
| Success Criteria | Text | How this persona measures whether the purchase was worthwhile |
| Pains Cared About | List of References (Dim 3) | Which Pains this persona is motivated to resolve (even if endured by someone else) |
| _Other fields to be refined._ | | |

## Statuses

_Not applicable — structural descriptor._

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Upstream | Customer Segment (Dim 3) | Buying Persona exists within a Customer Segment |
| Downstream | Business Outcome (Dim 3) | Economic Buyer pursues Business Outcomes |
| Cares about | Pain (Dim 3) | Buying Persona cares about Pains (motivates purchase) |
| Cross-dim | User Persona (Dim 4) | User Buyer may overlap with or advocate for User Personas |
| Work Model | Modeling Task (Track 1) | Modeling Tasks define/refine Buying Personas |

## Examples

For Customer Segment "LATAM Enterprise":

| Role Type | Persona | Key Concerns | Pains Cared About |
|---|---|---|---|
| Economic Buyer | CFO | FX cost reduction, regulatory compliance, ROI within 6 months | "Manual FX hedging costs $500K/year" |
| Technical Buyer | VP Engineering | API integration complexity, PCI-DSS scope, data residency | "Current payment adapter requires 6 weeks to integrate new providers" |
| User Buyer | AP Operations Manager | Workflow simplicity, team adoption, reduced manual work | "AP Clerks spend 4 hours/day on manual reconciliation" |
| Coach / Champion | Treasury Director | Internal alignment, vendor selection process, change management | — |
