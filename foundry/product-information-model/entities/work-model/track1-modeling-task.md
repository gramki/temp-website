# Modeling Task

**Model:** Work Model
**Track:** Discovery
**Owner:** Product Manager, Product Owner

## Definition

Work to evolve Definition Model entities in any dimension (Dims 2–9) based on discovery findings. Modeling Tasks produce updates to the product's self-description — customer segments, buyer personas, business outcomes, customer promises, value streams, capabilities, data domains, and more.

## Purpose

Discovery doesn't only produce PSDs (engineering changes) and Idea validations. Much of discovery work involves understanding and documenting the product's context — who buys it (Customer Value), how it's structured (Structural), what data it manages (Data), how it's operated (Operational). Without Modeling Tasks, this knowledge work is invisible, untracked, and often neglected.

Modeling Tasks make this knowledge work explicit and plannable:
- A PDR (decision) may trigger Modeling Tasks to update affected entities
- Product knowledge maintenance (e.g., new segment identified by Sales) also generates Modeling Tasks
- Modeling Tasks sit alongside Research Tasks, Experiments, Prototypes, and Specification Tasks as co-equal Discovery Track work entities

## Fields

| Field | Type | Description |
|---|---|---|
| Title | String | What's being modeled (e.g., "Map Cross-Border Payout Processing value stream") |
| Originating Discovery Case | Reference (Discovery) | Discovery Case this modeling work belongs to, if any |
| Target Dimension | Enum | Which dimension the work affects (Vendor Value–9) |
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
| Originates from | Discovery Case (Discovery) | Sub-item of a Discovery Case; carries bidirectional reference |
| Upstream | PDR (Strategy) | PDR may trigger Modeling Task(s) |
| Upstream | Research Task (Discovery) | Research findings may trigger Modeling Task(s) |
| Produces | Definition Model Entity (any Dim) | Modeling Task creates/updates entity(ies) |
| Sibling | Specification Task (Discovery) | Both are Discovery Track work; Specification Task produces PSDs that refine Product Intent, Modeling Task produces Definition Model updates |

## Examples

| Modeling Task | Target Dim | Target Entity | Triggered By |
|---|---|---|---|
| "Define LATAM AP Clerk user persona" | User Experience | User Persona | Research Task findings from user interviews |
| "Identify AP Clerk's cross-border payout jobs (JTBD)" | User Experience | Job | Research Task findings from contextual inquiry |
| "Define Web + Self-serve channel for customer dashboard" | User Experience | UX Channel | Deliberation on channel strategy → PDR |
| "Design 'Initiate and approve payout' journey (Web)" | User Experience | User Journey | Specification Task — PSD for Dashboard Web Module |
| "Map Cross-Border Payout Processing value stream" | Structural | Value Stream | PDR approving LATAM expansion initiative |
| "Design LATAM Enterprise pricing tier" | Vendor Value | Pricing Tier | PDR on segment-specific packaging |
| "Document LGPD compliance posture for Brazil" | Customer Value | Compliance Posture | PDR on LATAM regulatory requirements |
| "Add settlement_currency field to Payment_Record" | Data | Data Entity / Attribute | Research Task on settlement reporting needs |
| "Define LATAM Enterprise customer segment" | Customer Value | Customer Segment | Initiative scoping for LATAM market entry |
| "Define Partner Integration Engineer developer persona" | Ecosystem | Developer Persona | Research Task — developer experience interviews |
| "Define Customer Treasury System programmatic user persona" | Ecosystem | Programmatic User Persona | Research Task — integration requirements analysis |
| "Design Cross-Border Payments API Module with operations and SLOs" | Ecosystem | API Module, API Operation | PDR approving external API strategy |
| "Define API Compatibility Contract for Payments API v2" | Ecosystem | API Compatibility Contract | Deliberation on versioning strategy → PDR |
| "Define SAP ERP Integration Module scope and data mappings" | Ecosystem | Integration Module | PDR approving SAP connector initiative |
| "Define Compliance Workflow Extension points and governance" | Ecosystem | Extension Module | Research Task — customer custom-rules requirements |
| "Define Python Payments SDK scope and generation strategy" | Ecosystem | SDK/Library Module | Deliberation on SDK investment → PDR |
