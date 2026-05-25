# Customer Release Intent

**Model:** Definition Model
**Dimension:** Dimension 1: The Strategy Dimension
**Owner:** Product Management, Product Marketing

## Definition

A named, business-scoped intent to make capabilities available to customers based on business and customer needs. A Customer Release Intent bundles the expected outcomes of one or more Initiatives into a coherent customer-facing delivery target. Customer Release Intents use **names** (not version numbers or semver) to emphasize business identity and decouple strategic customer availability from technical versioning.

> **Terminology note:** Earlier drafts called this entity **Customer Release**. In Dimension 1, the intended meaning is **Customer Release Intent** — the planned customer-facing delivery outcome. The realized release package or event belongs to Release/Win execution and may be referred to as the **Customer Release** that fulfills this intent.

## Purpose

Customer Release Intent separates the *strategic intention to make functionality available to customers* from the *technical act of deploying artifacts* and the *actual release execution*. This follows the SAFe / Continuous Delivery convention where releases are decoupled from deployments. Without this separation, teams conflate "the code is deployed" with "customers can use it," which prevents strategies like dark launches, phased rollouts, and feature-flagged releases.

Customer Release Intent is a cross-cutting strategy entity whose realization spans multiple Work Model tracks: scoped during Discovery (strategic planning), built during Build, enabled by Run (deployments), and activated by Win (GTM execution). See FAQ Q12 for the terminology rationale.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Descriptive business name (e.g., "LATAM Expansion", "Project Mercury"). No version numbers. |
| Description | Text | Intended customer-facing delivery outcome and business rationale |
| Target Date | Date | Planned or committed customer availability date |
| Customer Segment(s) | List of References (Dim 3) | Customer segments targeted by this release intent |
| Customer Promise(s) | List of References (Dim 3) | Customer promises this release intent fulfills, strengthens, or introduces |
| Product Intent(s) | List of References (Dim 1) | Product Intents expected to realize this release intent |
| Product Version(s) | Reference | Product Version(s) (Work Model) expected to compose the realized release |
| _Other fields to be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| Planning | Customer Release Intent is being scoped — Initiatives and Product Intents being identified |
| In Progress | Product Intents, PSD refinement, build, deployment, and GTM work are underway |
| Ready | Required Product Intents are delivered or accepted for launch; GTM materials prepared |
| Launched | Business activation complete — functionality available to customers |
| Cancelled | Customer Release Intent is abandoned (with rationale documented) |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Upstream | Initiative (Dim 1) | Customer Release Intent advances Initiative(s) (many-to-many) |
| Downstream | Product Intent (Dim 1) | Customer Release Intent is realized through one or more Product Intents |
| Fulfills / strengthens | Customer Promise (Dim 3) | Customer Release Intent may fulfill, strengthen, or introduce Customer Promises |
| References | Product Version (Work Model) | Customer Release Intent may reference Product Version(s) expected to underpin the realized delivery |
| Realized by | Customer Release (Release / Win execution) | The actual customer-facing release event fulfills this intent |
| Deployed via | Product Deployment Specification(s) (Track 3) | Realization may be deployed via Product Deployment Specifications referencing certified Product Version(s) |
| May span | Deployment Train(s) (Dim 7) | A realized Customer Release may span multiple Deployment Trains when different modules follow different promotion paths |
| Governed by | Change Request(s) (Track 3) | Deployment-related changes for this release intent are governed by Change Requests scoped to Deployment Trains |
| Work Model | Initiative Scoping Task (Track 1) | Customer Release Intent may be defined as part of Initiative scoping (strategic planning) |
| Work Model | Release Planning Task (Track 2) | Release Planning Tasks scope the technical content, PSDs, and timeline needed to realize the intent |
| Work Model | Deployment Planning Task (Track 3) | Deployment Planning Tasks produce System and Product Deployment Specifications for required deployables |
| Work Model | Go-to-Market Planning Task (Track 4) | GTM Planning Tasks prepare the launch |
| Work Model | Customer Rollout Planning Task (Track 4) | Rollout Planning Tasks plan phased customer delivery |

## Example

"LATAM Expansion" — intent to make LATAM currency support (BRL, MXN, COP, CLP), LATAM compliance (local regulatory requirements), and LATAM onboarding (Spanish-language flows, local bank integrations) available to LATAM Enterprise customers by the committed launch date.

> **Note:** The corresponding Product Version might be `v3.2.0`, but the Customer Release Intent is identified by its name "LATAM Expansion," not by a version number. A single Customer Release Intent may be realized across multiple Product Versions (e.g., `v3.2.0` through `v3.2.4` as patches are applied during rollout).
