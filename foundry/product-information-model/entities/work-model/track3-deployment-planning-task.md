# Deployment Planning Task

**Model:** Work Model
**Track:** Run
**Owner:** DevOps, Site Reliability Engineers (SRE)

## Definition

Work to plan a deployment and **produce or update Deployment Specifications** (System Deployment Specification or Product Deployment Specification) for target environments. Deployment Planning Tasks encompass rollout strategy selection (canary, blue-green, rolling), environment-specific configuration, deployment script authoring (pre-rollout, validation, rollback), compliance window coordination, and change management review.

At **System scope**, Deployment Planning produces **System Deployment Specification** versions referencing a sealed **System Version**. At **Product scope**, it produces **Product Deployment Specification** versions referencing a certified **Product Version** and composing constituent System Deployment Specifications. The Operating Model determines whether System-scoped or Product-scoped deployment is the default change-management unit in a given organization. See DR-036.

> **Scripts within specifications are engineering work.** Pre-rollout scripts (database migrations, cache warming), validation scripts (post-deployment health checks, integration smoke tests), and rollback scripts are code artifacts developed as sub-tasks of the Deployment Planning Task. See DR-028 (superseded for terminology by DR-036 D5, D6).

## Purpose

Makes deployment planning explicit in the Run Track. Deploying to production is not a button press — it requires planning around rollout strategy, environment readiness, rollback procedures, compliance windows, cross-System coordination (for Product scope), and creation of Deployment Specifications that encapsulate all environment-specific details.

## Fields

| Field | Type | Description |
|---|---|---|
| Deployment Scope | Enum | `System` / `Product` — whether planning targets one System or a full Product deployment |
| Deployable Artifact | Reference | **System Version** (System scope) or **Product Version** (Product scope) being deployed |
| Target Environment | Reference (Operational) | The Deployment Environment being targeted |
| Deployment Strategy | Enum | `Canary` / `Blue-Green` / `Rolling` / `Direct` |
| Compliance Windows | List | Relevant compliance/change-freeze windows that constrain deployment timing |
| Pre-rollout Scripts | List | Scripts to include in the specification: migrations, cache warming, prerequisite validation |
| Validation Scripts | List | Scripts to include: health checks, smoke tests, SLA verification |
| Rollback Scripts | List | Scripts to include: migration reversals, state restoration |
| Risk Assessment | Text | Risk analysis: blast radius, rollback complexity, data migration risks |

## Statuses

| Status | Description |
|---|---|
| Planning | Deployment plan being developed; scripts being authored; environment-specific configuration being determined |
| Specification Ready | System Deployment Specification or Product Deployment Specification created with all configuration, scripts, and references validated |
| Approved | Specification has passed change management review and is cleared for deployment |
| Executing | Deployment Task is in progress using the produced specification |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Governed by | Deployment Plan (Run) | Deployment Planning Task is produced by and governed by a Deployment Plan |
| Produces | System Deployment Specification (Run) | Produces System-scoped specifications (System scope) |
| Produces | Product Deployment Specification (Run) | Produces Product-scoped specifications (Product scope) |
| Plans for | Deployment Task (Run) | Produces the specification for Deployment Task execution |
| May produce | Verification Task(s) (Run) | Planning may produce Verification Tasks for post-deployment validation |
| May produce | Maintenance Task(s) (Run) | Planning may discover maintenance prerequisites |
| Considers | Operational Readiness (Operational) | Planning considers System readiness in the target environment |
| Informed by | Incident history (Run) | Recent incidents for affected Systems inform deployment risk assessment |
| Supports | Customer Release Intent (Strategy) | Ensures Customer Release Intent's Product Version reaches target environments |

## Examples

- **System scope:** "Plan payments-system v3.1.0 deployment to production-us: produce System Deployment Specification sds-1.2, canary to 5% → 25% → 100% over 72 hours, PCI audit window avoidance."
- **System scope:** "Plan payments-monitoring-system v1.2.0 deployment to production-latam: produce System Deployment Specification sds-1.0 for operational System."
- **Product scope:** "Plan Product v4.0.0 deployment to production-latam: produce Product Deployment Specification pds-1.0 composing System Deployment Specifications for all Systems, define deployment ordering (Compliance → FX → Payments), author cross-System e2e verification script, coordinated rollback plan."

---
