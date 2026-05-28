# Technical Task (Track 3)

**Model:** Work Model
**Track:** Track 3: The Run Track (Stability & Operations)
**Owner:** SRE, Platform Engineers

## Definition

A granular engineering step scoped to a specific operational System (Dim 5) and optionally a Component (Dim 5). Run Track Technical Tasks represent the actual developer-level work for operational engineering: writing probe code, writing automation scripts, writing tests for operational systems, configuring monitoring infrastructure, implementing operational contracts. Run Track Technical Tasks serve Run Stories.

> **Technical Task is a per-track concept.** Each engineering track has its own Technical Tasks with the same entity structure but distinct track ownership. The Run Track's Technical Tasks serve Run Stories (operational engineering). The Build Track has its own Technical Tasks serving Stories and Integration Stories (product engineering). This avoids cross-track borrowing and keeps ownership clean.

**System/Component scope:** Like Build Track Technical Tasks, Run Track Technical Tasks speak the System language ("Implement synthetic BRL payment probe in payments-healthcheck," "Add daily reconciliation job in payment-reconciler"). They bridge from operational intent (Run Stories, Module-scoped) to technical implementation (operational Systems, Dim 5).

## Purpose

Captures the actual engineering work that produces operational System Versions. Without Run Track Technical Tasks:
- Run Stories have no engineering decomposition — "create synthetic payment probe" has no implementation plan
- Operational system-level work assignment is impossible — SREs work on operational Systems, not Modules
- Operational System Versions have no traceability to the work they contain

## Fields

| Field | Type | Description |
|---|---|---|
| Title | String | Descriptive title (e.g., "Implement BRL corridor synthetic probe in payments-healthcheck") |
| Run Story | Reference (Track 3) | Parent Run Story this Task implements |
| System | Reference (Dim 5) | Which operational System this Task is implemented in |
| Component | Reference (Dim 5) | Which Component within the System (optional) |
| Task Type | Enum | `Code` / `Test` / `Config` / `Documentation` / `Spike` |
| Effort Estimate | String | Time estimate (hours or story points) |
| Assignee | String | SRE / Platform Engineer assigned |
| Branch / PR | String | Source control reference |

## Statuses

| Status | Description |
|---|---|
| To Do | Task is defined but not yet started |
| In Progress | Engineer is actively working on this Task |
| In Review | Code is written, awaiting review |
| Done | Task is complete, code merged, tests passing |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Implements | Run Story (Track 3) | Technical Task implements a Run Story |
| Scoped to | System (Dim 5) | Task is implemented within a specific operational System |
| Scoped to | Component (Dim 5) | Task may target a specific Component within the System (optional) |
| Included in | System Version | Completed Task is included in the next System Version of the operational System |
| Belongs to | Run Epic (Track 3) | Task belongs to a Run Epic (via Run Story) |

## Examples

| Task | Type | Run Story | System | Component |
|---|---|---|---|---|
| "Implement BRL corridor synthetic probe" | Code | "Create synthetic payment probe for BRL corridor" | payments-healthcheck | — |
| "Add MXN corridor to probe suite" | Code | "Create synthetic payment probe for MXN corridor" | payments-healthcheck | — |
| "Write unit tests for reconciliation logic" | Test | "Build daily settlement reconciliation for LATAM banks" | payment-reconciler | Reconciliation Engine |
| "Configure Grafana dashboard for reconciliation metrics" | Config | "Add reconciliation dashboard to Grafana" | payment-reconciler | — |
| "Spike: evaluate cert-manager vs. custom rotation" | Spike | "Design cert rotation approach for FX Module" | fx-cert-rotator | — |

---
