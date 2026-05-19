# Deployment

**Model:** Work Model
**Track:** Track 3: The Run Track (Stability & Operations) — Artifact
**Owner:** DevOps, Site Reliability Engineers (SRE)

## Definition

A durable record that a **Deployment Specification** was applied to a specific environment — the work artifact produced by a Deployment Task. A Deployment records *what* was applied (specification version), *where* (environment), *when* (timestamp), *by whom* (deployer), and *how it went* (result). Deployments are scoped to **System Deployment** (System Deployment Specification applied) or **Product Deployment** (Product Deployment Specification applied).

Deployment is an **artifact**, not a work entity. The *work* of deploying is a Deployment Task; the *record* of having deployed is a Deployment. This follows the pattern established throughout the Work Model: work entities produce work artifacts (Specification Task → PSD, Deployment Planning Task → Deployment Specification, Deployment Task → Deployment).

> **Deployment applies specifications, not build artifacts directly (DR-036).** The specification references a sealed **System Version** or certified **Product Version** and provides environment-specific configuration. See DR-036 D5, D6; DR-029 (Deployment as artifact).

## Purpose

Deployment is the durable link between quality-gated Build Track artifacts and running production systems. It is distinct from a Customer Release (the business act of making functionality available to customers). Code can be deployed without being released to customers — enabling dark launches, feature flags, and canary rollouts. Customer Release becomes `Launched` when required deployments are complete AND the business activates the release.

As an artifact, the Deployment record provides:
- An auditable history of what is running in each environment
- The basis for supersession tracking (which deployment replaced which)
- Evidence for compliance and change management audit trails
- The anchor for rollback decisions (roll back to a previous specification version)

## Fields

| Field | Type | Description |
|---|---|---|
| Deployment Scope | Enum | `System` / `Product` — whether a System or Product Deployment Specification was applied |
| Specification | Reference | The specification version applied: System Deployment Specification or Product Deployment Specification |
| Environment | Reference (Dim 7) | The Deployment Environment where the specification was applied |
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
| Rolled Back | This deployment was reverted — a rollback Deployment Task applied a prior specification version |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Produced by | Deployment Task (Track 3) | Deployment record is produced by a Deployment Task |
| Records application of | System Deployment Specification (Track 3) | System-scoped deployment |
| Records application of | Product Deployment Specification (Track 3) | Product-scoped deployment |
| Targets | Deployment Environment (Dim 7) | Records which environment the specification was applied to |
| Supersedes | Deployment (Track 3) | A newer Deployment supersedes the previous one in the same environment |
| Enables | Customer Release (Dim 1) | Successful deployments enable Customer Release activation |

## Examples

- **Active (System):** "payments-system System Deployment Specification sds-1.2 applied to production-latam at 2026-02-12T14:30:00Z by deploy-pipeline. Status: Active. References payments-system v3.1.0. Supersedes sds-1.1 deployment."
- **Rolled Back (System):** "payments-system sds-1.2 applied to production-latam. Status: Rolled Back. Rollback Deployment Task applied sds-1.1, producing new Active Deployment."
- **Active (Product):** "Product Deployment Specification pds-1.0 for Product v4.0.0 applied to production-latam. Status: Active."

---
