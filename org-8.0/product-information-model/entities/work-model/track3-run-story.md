# Run Story

**Model:** Work Model
**Track:** Track 3: The Run Track (Stability & Operations)
**Owner:** SRE, Platform Engineers

## Definition

A unit of operational engineering work within a Run Epic, representing a functional increment of operational capability. Run Stories describe *what* operational capability needs to be built in Module (Dim 8) language — mirroring how Build Track Stories describe functional increments. Run Stories are implemented by Technical Tasks scoped to operational Systems (Dim 5).

Run Stories may be technical ("Create synthetic payment probe for end-to-end path verification") or automation-focused ("Build daily settlement reconciliation job for LATAM banks"). They produce operational System Versions — versioned, quality-gated artifacts of operational Systems.

## Purpose

Provides granular decomposition of operational engineering work. Without Run Stories:
- Run Epics are monolithic — no incremental delivery of operational capability
- Technical Tasks for operational systems have no specification-layer parent
- Acceptance criteria for individual operational capabilities have no structured home

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Descriptive name (e.g., "Create synthetic payment probe for BRL corridor") |
| Run Epic | Reference (Track 3) | Parent Run Epic |
| Module | Reference (Dim 8) | Inherited from parent Run Epic |
| Operational System | Reference (Dim 5) | Which operational System this Story targets |
| Acceptance Criteria | Text | What "done" looks like for this operational capability increment |

## Statuses

| Status | Description |
|---|---|
| To Do | Run Story identified; not yet started |
| In Progress | Technical Tasks actively being worked |
| Done | Acceptance criteria met; operational System Version produced |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Belongs to | Run Epic (Track 3) | Run Story is a unit of work within a Run Epic |
| Scoped to | Module (Dim 8) | Inherited from parent Run Epic |
| Targets | Operational System (Dim 5) | Run Story targets a specific operational System |
| Implemented by | Technical Task(s) (Track 2/3) | Run Story is implemented by Technical Tasks scoped to the operational System |
| Produces | Operational System Version (Track 2) | Run Story work produces a versioned artifact of the operational System |

## Examples

### Run Stories within "Build comprehensive health monitoring for Payments Module"

| Run Story | Operational System | Acceptance Criteria | Status |
|---|---|---|---|
| Create synthetic payment probe for BRL corridor | payments-healthcheck | Probe executes end-to-end synthetic BRL payment every 60s; alerts on failure or latency > 500ms; runs in production-latam | Done |
| Create synthetic payment probe for MXN corridor | payments-healthcheck | Probe executes end-to-end synthetic MXN payment every 60s; alerts on failure or latency > 500ms; runs in production-latam | In Progress |
| Build daily settlement reconciliation for LATAM banks | payment-reconciler | Reconciler compares payment records with bank settlement files daily at 02:00 BRT; alerts on discrepancies > $100; outputs reconciliation report | To Do |
| Add reconciliation dashboard to Grafana | payment-reconciler | Dashboard shows daily reconciliation status, discrepancy count, and trend; accessible to Payments SRE team | To Do |

---
