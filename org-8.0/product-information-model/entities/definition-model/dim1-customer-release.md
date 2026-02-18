# Customer Release

**Model:** Definition Model
**Dimension:** Dimension 1: The Strategy Dimension
**Owner:** Product Management, Product Marketing

## Definition

A named, business-scoped delivery of capabilities made available to customers based on business and customer needs. A Customer Release bundles the outcomes of one or more Initiatives into a coherent customer-facing delivery. Customer Releases use **names** (not version numbers or semver) to emphasize their business identity and decouple from technical versioning.

## Purpose

Customer Release separates the *business act of making functionality available to customers* from the *technical act of deploying artifacts*. This follows the SAFe / Continuous Delivery convention where releases are decoupled from deployments. Without this separation, teams conflate "the code is deployed" with "customers can use it," which prevents strategies like dark launches, phased rollouts, and feature-flagged releases.

Customer Release is a cross-cutting entity whose lifecycle spans multiple Work Model tracks: scoped during Discovery (strategic planning), built during Build, enabled by Run (deployments), and activated by Win (GTM execution). See FAQ Q12 for the terminology rationale.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Descriptive business name (e.g., "LATAM Expansion", "Project Mercury"). No version numbers. |
| Description | Text | What capabilities are included and the business rationale |
| Target Date | Date | Planned launch date |
| Product Version(s) | Reference | Product Version(s) (Work Model) that compose this release |
| _Other fields to be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| Planning | Customer Release is being scoped — Initiatives and PSDs being identified |
| In Progress | Build and deployment work is underway |
| Ready | All required Module Versions are deployed, GTM materials prepared |
| Launched | Business activation complete — functionality available to customers |
| Cancelled | Customer Release is abandoned (with rationale documented) |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Upstream | Initiative (Dim 1) | Customer Release advances Initiative(s) (many-to-many) |
| References | Product Version (Work Model) | Customer Release references Product Version(s) — the certified compositions that underpin the delivery |
| Work Model | Initiative Scoping Task (Track 1) | Customer Release may be defined as part of Initiative scoping (strategic planning) |
| Work Model | Release Planning Task (Track 2) | Release Planning Tasks scope the Customer Release (technical content, PSDs, timeline) |
| Work Model | Deployment Planning Task (Track 3) | Deployment Planning Tasks ensure required Module Versions are deployed |
| Work Model | Go-to-Market Planning Task (Track 4) | GTM Planning Tasks prepare the launch |
| Work Model | Customer Rollout Planning Task (Track 4) | Rollout Planning Tasks plan phased customer delivery |

## Example

"LATAM Expansion" — bundles LATAM currency support (BRL, MXN, COP, CLP), LATAM compliance (local regulatory requirements), and LATAM onboarding (Spanish-language flows, local bank integrations).

> **Note:** The corresponding Product Version might be `v3.2.0`, but the Customer Release is identified by its name "LATAM Expansion," not by a version number. A single Customer Release may span multiple Product Versions (e.g., `v3.2.0` through `v3.2.4` as patches are applied during rollout).
