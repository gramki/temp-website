# Run Engineering Monitoring

**Model:** Work Model
**Track:** Track 3: The Run Track (Stability & Operations)
**Category:** Monitoring
**Owner:** SRE Lead, Platform Engineering Lead

## Definition

Continuous tracking of Run Track **engineering** health — CI/CD pipeline health for operational systems, quality metrics (test coverage, defect rates for probes/reconcilers/automation), and velocity trends for Run Epics and Run Stories. Run Engineering Monitoring sits between periodic assessment (Run Epic retrospectives, operational engineering reviews) and reactive work (Run Stories, Technical Tasks) — it surfaces when operational system quality degrades, when engineering velocity stalls, or when operational tooling gaps accumulate.

Run Engineering Monitoring is the Run Track's counterpart to Build Monitoring (Track 2). Where Build Monitoring watches product system CI/CD health and Build Track velocity, Run Engineering Monitoring watches operational system CI/CD health and Run Track engineering velocity. It is distinct from System Monitoring, which watches the operational health of running systems in production.

> **Why separate from System Monitoring?** System Monitoring watches production health (SLAs, latency, availability, Tenant health). Run Engineering Monitoring watches the *engineering process* that produces operational systems. A healthy production system (System Monitoring green) can coexist with a struggling operational engineering pipeline (Run Engineering Monitoring red — Run Epics behind schedule, probe test coverage declining, operational system CI flaky). Conflating the two would hide engineering velocity problems behind operational health.

## Purpose

Makes the continuous oversight of Run Track engineering health explicit. Without Run Engineering Monitoring:
- CI/CD failures for operational systems (probes, reconcilers, automation) go unnoticed
- Test coverage trends for operational systems are invisible — probes may lack tests themselves
- Run Epic and Run Story velocity is untracked — SRE engineering time gets crowded out by incident response without visibility
- The quality of operational systems degrades silently

**Triggers downstream work:** Run Story creation, Technical Task creation, Run Epic scope adjustment, Operational Readiness reassessment.

## Fields

| Field | Type | Description |
|---|---|---|
| Scope | Text | What is being monitored (e.g., "payments-healthcheck CI pipeline", "Payments Module Run Epic velocity") |
| Metrics Tracked | List (text) | Build pass/fail rate for operational systems, test coverage, Run Story cycle time, Run Epic burndown, operational system defect rate |
| Thresholds / Alerts | List (text) | When does monitoring trigger action (e.g., "Operational system build failure 2 consecutive runs", "Run Epic velocity < 50% of planned") |
| Cadence | Enum | `Continuous` / `Daily` / `Weekly` |
| Owner | String | Role/person responsible for watching (e.g., SRE Lead) |
| Module(s) | Reference (Dim 8) | Which Module(s) this monitoring covers (Run Epics are Module-scoped) |
| _Other fields to be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| Active | Monitoring is in effect; thresholds and cadence are defined |
| Paused | Monitoring is temporarily suspended |
| Retired | Monitoring scope is no longer relevant |

## Outputs / Artifacts

| Artifact | Category | Description | Downstream Consumer |
|---|---|---|---|
| Alert / Trigger | Evidence | When threshold is breached — prompts Run Story creation, scope adjustment, or planning review | Run Epic, Run Story, Technical Task |
| Engineering Quality Report | Assessment | Periodic snapshot of operational system build health, coverage, Run Epic velocity | Run Epic retrospective, Operational Readiness review |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| May trigger | Run Story (Track 3) | Monitoring surfaces operational system quality issues requiring engineering |
| Informs | Run Epic (Track 3) | Velocity and quality trends inform Run Epic scope and scheduling |
| Informs | Operational Readiness (Dim 7) | Operational system quality feeds readiness assessment |
| Complements | System Monitoring (Track 3) | Run Engineering Monitoring tracks engineering health; System Monitoring tracks operational health |
| Complements | Build Monitoring (Track 2) | Run Engineering Monitoring is the Run Track's counterpart to Build Monitoring |

## Example

"Monitor payments-healthcheck and payment-reconciler CI — continuous; alert on build failure or test coverage drop below 85%. Weekly Run Epic velocity report: Run Story completion rate, operational system defect count. Owner: Payments SRE Lead. Feeds Run Epic retrospective and Module Package readiness assessment."

---
