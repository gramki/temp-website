# Win Enablement

**Model:** Work Model
**Track:** Track 4: The Win Track (Value Realization)
**Category:** Enablement
**Owner:** Product Marketing, Sales, Customer Success

## Definition

A parent entity type for reusable assets and programs that equip Win Stakeholders to execute at scale. Win Enablement is one-to-many work — an asset is created once and used across many engagements, customers, or segments. Four lever-specific subtypes:

1. **GTM Enablement** — Marketing collateral, pricing tools, partner materials, campaign assets. These are the reusable artifacts that support GTM execution across multiple customers and segments.

2. **Sales Enablement Asset** — Competitive battlecards, demo environments, ROI calculators, segment playbooks. These equip the *internal* sales organization with tools for acquisition and expansion conversations.

3. **CS Enablement** — Onboarding playbooks, health score models, QBR templates, expansion frameworks, and **customer education/training assets** (training materials, certification curricula, knowledge bases, learning paths). Advocacy program materials include both referral/case-study assets and customer education content. These standardize and scale post-sale customer success operations.

4. **Partner Enablement** — Partner demo environments, co-marketing kits, partner training, certification programs, partner playbooks. These equip *channel partners* (resellers, integrators, referral partners) — distinct from Sales Enablement, which equips internal teams. Used when the product has a partner or channel model for Awareness or Acquisition.

## Purpose

Makes the one-to-many enablement work of Win Teams explicit. Without Win Enablement:
- Reusable assets are created ad hoc without tracking their lifecycle or availability
- There is no distinction between creating an asset (one-to-many) and using it in a specific engagement (one-to-one)
- Win Stakeholders lack visibility into what assets exist, what stage they support, and who maintains them
- The connection between enablement assets and the Win Outcomes they support is invisible

## Fields

| Field | Type | Description |
|---|---|---|
| Title | String | Name of the enablement asset or program |
| Subtype | Enum | `GTM Enablement` / `Sales Enablement Asset` / `CS Enablement` / `Partner Enablement` |
| Lever | Enum | `GTM` / `Sales Enablement` / `Customer Success` (Partner Enablement uses GTM lever; distinct from internal Sales Enablement) |
| AAARRR Stage(s) Supported | List of Enums | Which stage(s) this asset supports (`Awareness` / `Acquisition` / `Activation` / `Retention` / `Revenue` / `Referral`) |
| Win Stakeholder(s) | List of References (Dim 2) | Which Win Stakeholders will use this asset |
| Initiative | Reference (Dim 1) | Which Initiative this enablement is aligned to |
| Output / Deliverable | Text | Description of what this enablement produces (e.g., "Competitive battlecard for LATAM market") |
| Owner | String | Role/person accountable for creating and maintaining this asset |
| _Other fields to be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| Planned | Enablement asset is scoped but creation has not started |
| In Progress | Asset is being created or program is being developed |
| Available | Asset is complete and available for use by Win Stakeholders |
| Retired | Asset is no longer current; superseded or no longer relevant |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Aligned to | Initiative (Dim 1) | Win Enablement is aligned to one or more Initiatives |
| Used by | Win Stakeholder (Dim 2) | Win Stakeholders use enablement assets in their work |
| Supports | Win Engagement (Track 4) | Enablement assets are used in specific engagements |
| Driven by | Win Planning (Track 4) | Win Planning drives the creation of enablement assets |
| Assessed by | Win Review (Track 4) | Campaign/Program Reviews assess enablement effectiveness |
| Serves | Developer Persona (Dim 6) | Developer-facing enablement assets (API docs, SDK guides, sandbox environments, developer training) |

## Examples

| Subtype | Title | Lever | AAARRR Stage | Win Stakeholder | Initiative |
|---|---|---|---|---|---|
| GTM Enablement | "LATAM Cross-Border pricing calculator" | GTM | Acquisition | Account Executives | LATAM Cross-Border Expansion |
| GTM Enablement | "LATAM partner co-marketing kit" | GTM | Awareness | Partner Managers | LATAM Cross-Border Expansion |
| Sales Enablement Asset | "LATAM competitive battlecard vs. Competitor X" | Sales Enablement | Acquisition | Pre-Sales Engineers, Account Executives | LATAM Cross-Border Expansion |
| Sales Enablement Asset | "LATAM demo environment with BRL/MXN corridors" | Sales Enablement | Acquisition | Pre-Sales Engineers | LATAM Cross-Border Expansion |
| CS Enablement | "LATAM Enterprise onboarding playbook" | Customer Success | Activation | Implementation Consultants | LATAM Cross-Border Expansion |
| CS Enablement | "Cross-Border health score model" | Customer Success | Retention | CS Managers | LATAM Cross-Border Expansion |
| CS Enablement | "LATAM API integration certification program" | Customer Success | Activation, Referral | CS Managers, Partner Managers | LATAM Cross-Border Expansion (customer education) |
| CS Enablement | "Cross-Border API developer onboarding guide and sandbox" | Customer Success | Activation | Implementation Consultants, Developer Relations | LATAM Cross-Border Expansion |
| Partner Enablement | "LATAM bank partner certification program" | GTM | Awareness, Acquisition | Partner Managers | LATAM Cross-Border Expansion |
| Partner Enablement | "LATAM fintech co-marketing kit" | GTM | Awareness | Partner Managers | LATAM Cross-Border Expansion |
