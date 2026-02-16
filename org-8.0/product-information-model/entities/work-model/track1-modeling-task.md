# Modeling Task

**Model:** Work Model
**Track:** Track 1: The Discovery Track (Intelligence)
**Owner:** Product Manager, Product Owner

## Definition

Work to evolve Definition Model entities in any dimension (Dims 2–9) based on discovery findings. Modeling Tasks produce updates to the product's self-description — customer segments, buyer personas, business outcomes, customer promises, value streams, capabilities, data domains, and more.

## Purpose

Discovery doesn't only produce PSDs (engineering changes) and Idea validations. Much of discovery work involves understanding and documenting the product's context — who buys it (Dim 3), how it's structured (Dim 8), what data it manages (Dim 9), how it's operated (Dim 7). Without Modeling Tasks, this knowledge work is invisible, untracked, and often neglected.

Modeling Tasks make this knowledge work explicit and plannable:
- A PDR (decision) may trigger Modeling Tasks to update affected entities
- Product knowledge maintenance (e.g., new segment identified by Sales) also generates Modeling Tasks
- Modeling Tasks sit alongside Research Tasks, Experiments, Prototypes, and Specification Tasks as co-equal Discovery Track work entities

## Fields

| Field | Type | Description |
|---|---|---|
| Title | String | What's being modeled (e.g., "Map Cross-Border Payout Processing value stream") |
| Target Dimension | Enum | Which dimension the work affects (Dim 2–9) |
| Target Entity Type | String | Which entity type is being created/updated |
| Triggered By | Reference | PDR, Research Task findings, or ad-hoc |
| Description | Text | What specifically needs to be modeled/updated |
| _Other fields to be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| To Do | Not yet started |
| In Progress | Actively being worked on |
| In Review | Draft entity/update under review |
| Done | Entity created/updated in the Definition Model |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Upstream | PDR (Dim 1) | PDR may trigger Modeling Task(s) |
| Upstream | Research Task (Track 1) | Research findings may trigger Modeling Task(s) |
| Produces | Definition Model Entity (any Dim) | Modeling Task creates/updates entity(ies) |
| Sibling | Specification Task (Track 1) | Both are Discovery Track work; Spec Task produces PSDs, Modeling Task produces Definition Model updates |

## Examples

| Modeling Task | Target Dim | Target Entity | Triggered By |
|---|---|---|---|
| "Define LATAM AP Clerk user persona" | Dim 4 | User Persona | Research Task findings from user interviews |
| "Map Cross-Border Payout Processing value stream" | Dim 8 | Value Stream | PDR approving LATAM expansion initiative |
| "Design LATAM Enterprise pricing tier" | Dim 2 | Pricing Tier | PDR on segment-specific packaging |
| "Document LGPD compliance posture for Brazil" | Dim 3 | Compliance Posture | PDR on LATAM regulatory requirements |
| "Add settlement_currency field to Payment_Record" | Dim 9 | Data Entity / Attribute | Research Task on settlement reporting needs |
| "Define LATAM Enterprise customer segment" | Dim 3 | Customer Segment | Initiative scoping for LATAM market entry |
