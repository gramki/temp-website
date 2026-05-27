# GTM Planning

> **Note:** GTM Planning is a subtype of Win Planning. See `track4-win-planning.md` for the parent entity and other subtypes. (File retains legacy filename `track4-gtm-planning-task.md` for backward compatibility.)

**Model:** Work Model
**Track:** Track 4: The Win Track (Value Realization)
**Category:** Planning
**Owner:** Product Marketing, Sales, Customer Success

## Definition

Work to prepare launch messaging, pricing communication, partnership execution, marketing campaigns, channel strategy, and customer communication for a Customer Release Intent. Includes sales decks, webinars, help center articles, pricing page updates, internal enablement, and Win Stakeholder preparation.

## Purpose

Makes the go-to-market preparation work explicit in the Win Track. A Customer Release Intent requires deliberate GTM effort to become a realized Customer Release — the business doesn't just "flip a switch." Sales teams need enablement, marketing needs messaging, support needs documentation, customers need communication, and Win Stakeholders across all AAARRR stages need preparation.

**Dim 2 connection:** GTM Planning Tasks reference Dim 2 entities to ensure commercial coherence:
- Which **Win Outcomes** does this launch target? (e.g., Acquisition, Activation outcomes for LATAM Enterprise)
- Which **Pricing Tiers** are affected? (e.g., new LATAM Enterprise tier, modifications to existing Enterprise Volume Plan)
- Which **Win Stakeholders** need enablement? (e.g., Pre-Sales Engineers need LATAM demo environment, Account Executives need new pricing deck)
- Which **Win Barriers** should GTM materials address? (e.g., competitor free trial → emphasize value in messaging)

## Fields

| Field | Type | Description |
|---|---|---|
| Title | String | Brief description of the GTM work |
| Customer Release Intent | Reference (Dim 1) | Which Customer Release Intent this GTM work prepares to realize |
| Target Win Outcomes | List of References (Dim 2) | Which Win Outcomes this launch targets |
| Affected Pricing Tiers | List of References (Dim 2) | Which Pricing Tiers are involved |
| Win Stakeholders to enable | List of References (Dim 2) | Which Win Stakeholders need preparation |
| Deliverables | List (text) | Specific outputs — sales deck, webinar, help articles, pricing page, etc. |
| _Other fields to be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| Planned | GTM work is scoped but not started |
| In Progress | GTM materials and enablement are being created |
| Ready | All GTM materials are complete; Win Stakeholders are enabled |
| Launched | Customer Release Intent has been realized and activated with GTM support |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Subtype of | Win Planning (Track 4) | GTM Planning is a subtype of Win Planning |
| Advances | Initiative (Dim 1) | GTM Planning advances one or more Initiatives |
| Prepares for | Customer Release Intent (Dim 1) | GTM Planning Tasks prepare the launch that realizes a Customer Release Intent |
| Targets | Win Outcome (Dim 2) | GTM work targets specific Win Outcomes |
| References | Pricing Tier (Dim 2) | GTM work may involve pricing/packaging communication |
| Enables | Win Stakeholder (Dim 2) | GTM work enables Win Stakeholders with materials and training |
| Addresses | Win Barrier (Dim 2) | GTM messaging may proactively address known Win Barriers |

## Example

"Prepare LATAM Expansion launch"
- Customer Release Intent: "LATAM Expansion"
- Target Win Outcomes: Acquisition (close LATAM deals in 90 days), Activation (first transaction in 30 days)
- Affected Pricing Tiers: Enterprise Volume Plan (LATAM currencies added), new LATAM Starter tier
- Win Stakeholders to enable: Account Executives (pricing deck), Pre-Sales Engineers (LATAM demo environment), Implementation Consultants (LATAM onboarding guide)
- Deliverables: Sales deck, customer webinar, help center articles (5), pricing page update, internal enablement session, competitive battle card (addresses "competitor free trial" Win Barrier)
