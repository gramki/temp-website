# Deployment Planning Task

**Model:** Work Model
**Track:** Track 3: The Run Track (Stability & Operations)
**Owner:** DevOps, Site Reliability Engineers (SRE)

## Definition

Work to plan a deployment and **produce deployment descriptors** (SDD, MDD, or PDD versions) for target environments. Deployment Planning Tasks encompass rollout strategy selection (canary, blue-green, rolling), environment-specific configuration, deployment script authoring (pre-rollout, validation, rollback), compliance window coordination, and change management review. The Deployment Planning Task is where deployment descriptors are created, validated, and approved.

At the atomic level, Deployment Planning produces SDD versions. At the integrated level, it produces MDD versions (composing SDDs, adding Module-level config and scripts). At the complete level, it produces PDD versions (composing MDDs, adding product-level orchestration and scripts). The Operating Model determines whether the SDD (atomic) or MDD (integrated) is the logical unit for change management in a given organization.

> **Scripts within descriptors are engineering work.** Pre-rollout scripts (database migrations, cache warming), validation scripts (post-deployment health checks, integration smoke tests), and rollback scripts (migration reversals, state restoration) are code artifacts developed as sub-tasks of the Deployment Planning Task. See DR-028.

## Purpose

Makes deployment planning explicit in the Run Track. Deploying to production is not a button press — it requires planning around rollout strategy, environment readiness, rollback procedures, compliance windows (e.g., PCI audit freezes), composition-level coordination, cross-track handoffs, and the creation of deployment descriptors that encapsulate all environment-specific details. The composition level (atomic vs. integrated vs. complete) is itself a planning decision with different risk, coordination, and rollback implications.

## Fields

| Field | Type | Description |
|---|---|---|
| Composition Level | Enum | `Atomic` / `Integrated` / `Complete` — the deployment granularity being planned |
| Deployable Artifact | Reference | The artifact being deployed: System Version (atomic), Module Package Version (integrated), or Product Package Version (complete) |
| Target Environment | Reference (Dim 7) | The Deployment Environment being targeted |
| Deployment Strategy | Enum | `Canary` / `Blue-Green` / `Rolling` / `Direct` |
| Compliance Windows | List | Relevant compliance/change-freeze windows that constrain deployment timing |
| Pre-rollout Scripts | List | Scripts/applications to be included in the descriptor: migrations, cache warming, prerequisite validation |
| Validation Scripts | List | Scripts/applications to be included in the descriptor: health checks, smoke tests, SLA verification |
| Rollback Scripts | List | Scripts/applications to be included in the descriptor: migration reversals, state restoration |
| Risk Assessment | Text | Risk analysis for this deployment: blast radius, rollback complexity, data migration risks |

## Statuses

| Status | Description |
|---|---|
| Planning | Deployment plan being developed; scripts being authored; environment-specific configuration being determined |
| Descriptor Ready | SDD/MDD/PDD version created with all configuration, scripts, and references validated |
| Approved | Descriptor has passed change management review and is cleared for deployment |
| Executing | Deployment Task is in progress using the produced descriptor |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Governed by | Deployment Plan (Track 3) | Deployment Planning Task is produced by and governed by a Deployment Plan |
| Produces | SDD version (Track 3) | Deployment Planning Task produces SDD versions (atomic level) |
| Produces | MDD version (Track 3) | Deployment Planning Task produces MDD versions (integrated level) |
| Produces | PDD version (Track 3) | Deployment Planning Task produces PDD versions (complete level) |
| Plans for | Deployment Task (Track 3) | Deployment Planning Task produces the descriptor for Deployment Task execution |
| May produce | Verification Task(s) (Track 3) | Planning may produce Verification Tasks for post-deployment validation |
| May produce | Maintenance Task(s) (Track 3) | Planning may discover maintenance prerequisites |
| Considers | Operational Readiness (Dim 7) | Planning considers environment readiness status |
| Informed by | Incident history (Track 3) | Incident history for affected Module/System informs deployment risk assessment — a Module with recent SEV-1 incidents may warrant a more cautious strategy (canary, drill) or block promotion |
| Supports | Customer Release (Dim 1) | Deployment planning ensures Customer Release's deployable compositions are deployed |

## Examples

- **Atomic:** "Plan payments-service v2.3.3 deployment to production-us: produce SDD v1.2, canary to 5% → 25% → 100% over 72 hours, PCI audit window avoidance."
- **Integrated:** "Plan Payments Module Package Version v2.3.0 deployment to production-latam: produce MDD v3.1 composing 4 SDDs, author pre-rollout migration script, validation smoke test, rollback script, LATAM regulatory window."
- **Complete:** "Plan Product Package Version v3.2.0 deployment to production-latam: produce PDD v1.0 composing 3 MDDs, define deployment ordering (Compliance → FX → Payments), author cross-module e2e verification script, coordinated rollback plan."
