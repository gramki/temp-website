# Deployment

**Model:** Work Model
**Track:** Track 3: The Run Track (Stability & Operations)
**Owner:** DevOps, Site Reliability Engineers (SRE)

## Definition

The operational act of installing a specific Module Version into a specific environment. Deployments are tracked **per-environment** — a Module Version is not "deployed" in absolute terms; it is deployed *somewhere*.

## Purpose

Deployment is the link between a quality-gated Module Version (Build Track output) and a running production system. It is a distinct concept from a Customer Release (the business act of making functionality available to customers). A Module Version can be deployed (code running in production) without being released to customers — enabling dark launches, feature flags, and canary rollouts. The Customer Release becomes `Launched` only when all required Module Versions are deployed AND the business activates the release.

## Fields

| Field | Type | Description |
|---|---|---|
| Module Version | Reference | The Module Version being deployed |
| Environment | Reference | The target environment (Dim 7) |
| Deployment Strategy | Enum | Canary / Blue-Green / Rolling / Direct |
| Deployment Timestamp | DateTime | When the deployment was executed |
| Rollback Plan | Text | Steps to revert if deployment fails |
| _Other fields to be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| Planned | Deployment is scheduled but not yet executed |
| In Progress | Deployment is being executed |
| Succeeded | Module Version is running in the target environment |
| Failed | Deployment failed — rollback may be in progress |
| Rolled Back | Deployment was reverted to the previous version |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Deploys | Module Version (Track 2) | Deployment installs a Module Version |
| Targets | Environment (Dim 7) | Deployment targets a specific environment |
| Enables | Customer Release (Dim 1) | Successful deployments enable Customer Release activation |

## Example

"Deploy payments-service v2.3.3 to production-us." Tracked separately from "Deploy payments-service v2.3.3 to production-eu."
