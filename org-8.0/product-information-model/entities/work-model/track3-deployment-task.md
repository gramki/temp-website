# Deployment Task

**Model:** Work Model
**Track:** Track 3: The Run Track (Stability & Operations)
**Owner:** DevOps, Site Reliability Engineers (SRE)

## Definition

The work of applying a deployment descriptor (SDD, MDD, or PDD version) to a specific Deployment Environment. A Deployment Task is the **execution act** — it takes a descriptor produced by a Deployment Planning Task and applies it to the target environment, producing a Deployment record (artifact) upon completion.

Deployment Tasks operate at three **composition levels**: **atomic** (applying an SDD — a single System Version's deployment specification), **integrated** (applying an MDD — a Module Package Version's deployment specification), or **complete** (applying a PDD — a Product Package Version's deployment specification).

> **Deployment Task vs. Deployment.** A Deployment Task is the *work entity* — something an SRE or automation pipeline executes. A Deployment is the *work artifact* — the durable record that a descriptor was applied to an environment at a specific time. "We executed a deployment task and it produced a deployment." This separation follows the pattern established throughout the Work Model: work entities produce work artifacts (Specification Task → PSD, Deployment Planning Task → SDD/MDD/PDD, Deployment Task → Deployment). See DR-029 D6, D7.

## Purpose

Makes deployment execution a distinct, trackable work entity in the Run Track. Without Deployment Tasks:
- The act of deploying and the record of deployment are conflated into a single entity
- Deployment work cannot be governed by a Deployment Plan or preceded by a Deployment Drill
- The relationship between "planning a deployment" (Deployment Planning Task) and "executing a deployment" (Deployment Task) is structurally invisible
- Change Request completion criteria ("all deployment tasks and verification tasks succeed") cannot reference a distinct execution entity

## Fields

| Field | Type | Description |
|---|---|---|
| Composition Level | Enum | `Atomic` / `Integrated` / `Complete` — the deployment granularity |
| Descriptor | Reference (Track 3) | The descriptor version being applied: SDD version (atomic), MDD version (integrated), or PDD version (complete) |
| Target Environment | Reference (Dim 7) | The Deployment Environment being targeted |
| Deployment Strategy | Enum | `Canary` / `Blue-Green` / `Rolling` / `Direct` |
| Deployer | String | Person or automation that executes the deployment |
| Scheduled Time | DateTime | When the deployment is scheduled to execute |

## Statuses

| Status | Description |
|---|---|
| Ready | Descriptor is approved; prerequisites (drill, maintenance) are complete; deployment can proceed |
| Executing | Deployment is being executed — descriptor is being applied to the target environment |
| Complete | Descriptor successfully applied; Deployment record (artifact) produced |
| Failed | Deployment failed — rollback may be initiated |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Applies | SDD version (Track 3) | Deployment Task applies an SDD version (atomic level) |
| Applies | MDD version (Track 3) | Deployment Task applies an MDD version (integrated level) |
| Applies | PDD version (Track 3) | Deployment Task applies a PDD version (complete level) |
| Produces | Deployment (Track 3) | Deployment Task produces a Deployment record (artifact) |
| Governed by | Deployment Plan (Track 3) | Deployment Task is executed within the scope of a Deployment Plan |
| Preceded by | Deployment Drill Task (Track 3) | When present, drill must pass before deployment task proceeds |
| Targets | Deployment Environment (Dim 7) | Deployment Task targets a specific environment |
| Verified by | Verification Task(s) (Track 3) | Verification Tasks validate the deployment after execution |
| Enables | Customer Release (Dim 1) | Successful deployment tasks enable Customer Release activation |
| Informed by | Operational Readiness (Dim 7) | Deployment decisions consider readiness status |

## Examples

- **Atomic:** "Apply payments-service SDD v1.2 to production-us." Deploys payments-service v2.3.3 with production-us resource configuration and network policies.
- **Integrated:** "Apply Payments MDD v3.1 to production-latam." Runs pre-rollout scripts (DB migration, cache warming), deploys all SDDs within the Module, runs validation scripts (health checks, smoke tests).
- **Complete:** "Apply Product PDD v1.0 to production-latam." Deploys all MDDs in sequence (Compliance → FX → Payments), runs product-level e2e verification, coordinated rollback if e2e fails.

---
