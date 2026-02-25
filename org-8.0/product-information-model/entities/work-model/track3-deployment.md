# Deployment

**Model:** Work Model
**Track:** Track 3: The Run Track (Stability & Operations) — Artifact
**Owner:** DevOps, Site Reliability Engineers (SRE)

## Definition

A durable record that a deployment descriptor was applied to a specific environment — the work artifact produced by a Deployment Task. A Deployment records *what* was deployed (descriptor version), *where* (environment), *when* (timestamp), *by whom* (deployer), and *how it went* (result). Deployments operate at three **composition levels**: **atomic** (SDD applied), **integrated** (MDD applied), or **complete** (PDD applied).

Deployment is an **artifact**, not a work entity. The *work* of deploying is a Deployment Task; the *record* of having deployed is a Deployment. This follows the pattern established throughout the Work Model: work entities produce work artifacts (Specification Task → PSD, Deployment Planning Task → SDD/MDD/PDD, Deployment Task → Deployment).

> **Deployment applies descriptors, not artifacts directly (DR-028, refined by DR-029).** The descriptor version determines *what* is deployed *how* — the deployable artifact (System Version, Module Package Version, Product Package Version) is referenced indirectly through the descriptor. See DR-026 (System Version as atomic deployment unit), DR-027 (Module Package and Product Package), DR-028 (deployment descriptors), DR-029 (Deployment refactored from work entity to artifact).

## Purpose

Deployment is the durable link between quality-gated Build/Run Track artifacts and running production systems. It is a distinct concept from a Customer Release (the business act of making functionality available to customers). An artifact can be deployed (code running in production) without being released to customers — enabling dark launches, feature flags, and canary rollouts. The Customer Release becomes `Launched` only when all required deployments (MDD or PDD applications) are complete AND the business activates the release.

As an artifact, the Deployment record provides:
- An auditable history of what is running in each environment
- The basis for supersession tracking (which deployment replaced which)
- Evidence for compliance and change management audit trails
- The anchor for rollback decisions (roll back to a previous Deployment's descriptor version)

## Fields

| Field | Type | Description |
|---|---|---|
| Composition Level | Enum | `Atomic` / `Integrated` / `Complete` — the deployment granularity |
| Descriptor | Reference | The descriptor version that was applied: SDD version (atomic), MDD version (integrated), or PDD version (complete) |
| Environment | Reference (Dim 7) | The Deployment Environment where the descriptor was applied |
| Deployment Strategy | Enum | `Canary` / `Blue-Green` / `Rolling` / `Direct` — the strategy used |
| Deployment Timestamp | DateTime | When the deployment was executed |
| Deployer | String | Person or automation that executed the deployment |
| Deployment Task | Reference (Track 3) | The Deployment Task that produced this record (provenance) |
| Previous Deployment | Reference (Track 3) | The Deployment record this one supersedes (if any) |

## Statuses

| Status | Description |
|---|---|
| Active | This deployment is the current running state in the target environment |
| Superseded | This deployment has been replaced by a newer Deployment in the same environment |
| Rolled Back | This deployment was reverted — a rollback Deployment Task produced a new Deployment record pointing to a previous descriptor version |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Produced by | Deployment Task (Track 3) | Deployment record is produced by a Deployment Task |
| Records application of | SDD version (Track 3) | Deployment records an SDD version application (atomic level) |
| Records application of | MDD version (Track 3) | Deployment records an MDD version application (integrated level) |
| Records application of | PDD version (Track 3) | Deployment records a PDD version application (complete level) |
| Targets | Deployment Environment (Dim 7) | Deployment records which environment the descriptor was applied to |
| Supersedes | Deployment (Track 3) | A newer Deployment supersedes the previous one in the same environment |
| Enables | Customer Release (Dim 1) | Successful deployments enable Customer Release activation |

## Examples

- **Active Deployment (Integrated):** "Payments MDD v3.1 applied to production-latam at 2026-02-12T14:30:00Z by deploy-pipeline. Status: Active. Supersedes: Deployment of Payments MDD v3.0 (now Superseded)."
- **Rolled Back Deployment:** "Payments MDD v3.1 applied to production-latam. Status: Rolled Back. A rollback Deployment Task applied Payments MDD v3.0 (the previous version), producing a new Active Deployment."
- **Atomic Deployment:** "payments-service SDD v1.2 applied to production-us at 2026-02-11T10:00:00Z. Status: Active."

---
