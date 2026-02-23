# Deployment

**Model:** Work Model
**Track:** Track 3: The Run Track (Stability & Operations)
**Owner:** DevOps, Site Reliability Engineers (SRE)

## Definition

The operational act of deploying to a specific environment. Deployments are tracked **per-environment** and operate at three **composition levels**: **atomic** (a single System Version), **integrated** (a Module Package), or **complete** (a Product Package). A deployment is not "deployed" in absolute terms; it is deployed *somewhere*, at a specific composition level.

> **Three deployment levels (DR-027):** The Run Track deploys at three granularities. **Atomic:** a single System Version (Dim 5) to an environment — the most common deployment unit. **Integrated:** a Module Package (Module Version enriched with operational System Versions and configuration) to an environment — used when Module-level coordinated deployment is needed. **Complete:** a Product Package (Product Version enriched with Module Packages and cross-module operational wiring) to an environment — used for full product releases. The composition level is a deployment-planning decision. See DR-026 (System Version as atomic deployment unit), DR-027 (Module Package and Product Package).

## Purpose

Deployment is the link between quality-gated Build/Run Track artifacts and running production systems. It is a distinct concept from a Customer Release (the business act of making functionality available to customers). An artifact can be deployed (code running in production) without being released to customers — enabling dark launches, feature flags, and canary rollouts. The Customer Release becomes `Launched` only when all required deployments (Module Packages or Product Package) are complete AND the business activates the release.

## Fields

| Field | Type | Description |
|---|---|---|
| Composition Level | Enum | `Atomic` / `Integrated` / `Complete` — the deployment granularity |
| Deployable | Reference (Track 2/3) | The artifact being deployed: System Version (atomic), Module Package (integrated), or Product Package (complete) |
| Environment | Reference (Dim 7) | The target Deployment Environment |
| Deployment Strategy | Enum | `Canary` / `Blue-Green` / `Rolling` / `Direct` |
| Deployment Timestamp | DateTime | When the deployment was executed |
| Rollback Plan | Text | Steps to revert if deployment fails |
| Verification Results | Text | Post-deployment verification results |
| Deployer | String | Person or automation that executed the deployment |

## Statuses

| Status | Description |
|---|---|
| Planned | Deployment is scheduled but not yet executed |
| In Progress | Deployment is being executed |
| Succeeded | Deployable artifact is running in the target environment |
| Failed | Deployment failed — rollback may be in progress |
| Rolled Back | Deployment was reverted to the previous version |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Deploys | System Version (Track 2) | Deployment installs a System Version (atomic level) |
| Deploys | Module Package (Track 3) | Deployment installs a Module Package (integrated level) |
| Deploys | Product Package (Track 3) | Deployment installs a Product Package (complete level) |
| Targets | Deployment Environment (Dim 7) | Deployment targets a specific environment |
| Enables | Customer Release (Dim 1) | Successful deployments enable Customer Release activation |
| Informed by | Operational Readiness (Dim 7) | Deployment decisions consider readiness status |

## Example

- **Atomic:** "Deploy payments-service v2.3.3 to production-us." Tracked separately from "Deploy payments-service v2.3.3 to production-eu."
- **Integrated:** "Deploy Payments Module Package v2.3.0-latam to production-latam." Includes product System Versions + operational System Versions + operational config.
- **Complete:** "Deploy Product Package v3.2.0-latam to production-latam." Includes all Module Packages + cross-module operational wiring.
