# Deployment Task

**Model:** Work Model
**Track:** Track 3: The Run Track (Stability & Operations)
**Owner:** DevOps, Site Reliability Engineers (SRE)

## Definition

The work of applying a **Deployment Specification** (System Deployment Specification or Product Deployment Specification) to a specific Deployment Environment. A Deployment Task is the **execution act** — it takes a specification produced by a Deployment Planning Task and applies it to the target environment, producing a **Deployment** record (artifact) upon completion.

Deployment Tasks are scoped to **System Deployment** (applying a System Deployment Specification for one System Version) or **Product Deployment** (applying a Product Deployment Specification for a Product Version). See DR-036 D11.

> **Deployment Task vs. Deployment.** A Deployment Task is the *work entity*; a Deployment is the *work artifact* — the durable record that a specification was applied. See DR-029 D6, D7; DR-036.

## Purpose

Makes deployment execution a distinct, trackable work entity in the Run Track. Without Deployment Tasks:
- The act of deploying and the record of deployment are conflated
- Deployment work cannot be governed by a Deployment Plan or preceded by a Deployment Drill
- Change Request completion criteria cannot reference a distinct execution entity

## Fields

| Field | Type | Description |
|---|---|---|
| Deployment Scope | Enum | `System` / `Product` |
| Specification | Reference (Track 3) | System Deployment Specification or Product Deployment Specification being applied |
| Target Environment | Reference (Dim 7) | The Deployment Environment being targeted |
| Deployment Strategy | Enum | `Canary` / `Blue-Green` / `Rolling` / `Direct` |
| Deployer | String | Person or automation that executes the deployment |
| Scheduled Time | DateTime | When the deployment is scheduled to execute |

## Statuses

| Status | Description |
|---|---|
| Ready | Specification is approved; prerequisites (drill, maintenance) are complete |
| Executing | Specification is being applied to the target environment |
| Complete | Specification successfully applied; Deployment record produced |
| Failed | Deployment failed — rollback may be initiated |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Applies | System Deployment Specification (Track 3) | System-scoped deployment |
| Applies | Product Deployment Specification (Track 3) | Product-scoped deployment |
| Produces | Deployment (Track 3) | Produces a Deployment record |
| Governed by | Deployment Plan (Track 3) | Executed within a Deployment Plan |
| Preceded by | Deployment Drill Task (Track 3) | When present, drill must pass before execution |
| Targets | Deployment Environment (Dim 7) | Targets a specific environment |
| Verified by | Verification Task(s) (Track 3) | Post-deployment validation |
| Enables | Customer Release (Dim 1) | Successful deployment enables Customer Release activation |
| Informed by | Operational Readiness (Dim 7) | Readiness status informs go/no-go |

## Examples

- **System:** "Apply payments-system System Deployment Specification sds-1.2 to production-us." Deploys sealed payments-system v3.1.0 with production-us configuration.
- **System:** "Apply payments-monitoring-system System Deployment Specification sds-1.0 to production-latam." Deploys operational System v1.2.0.
- **Product:** "Apply Product Deployment Specification pds-1.0 to production-latam." Deploys Product v4.0.0 — all System specifications in order (Compliance → FX → Payments), product-level e2e verification, coordinated rollback if e2e fails.

---
