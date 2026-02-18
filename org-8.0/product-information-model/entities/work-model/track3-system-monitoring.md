# System Monitoring

**Model:** Work Model
**Track:** Track 3: The Run Track (Stability & Operations)
**Category:** Monitoring
**Owner:** DevOps, SRE

## Definition

Continuous tracking of infrastructure health, SLA/uptime metrics, capacity utilization, and performance baselines. System Monitoring sits between periodic assessment (Capacity Planning, deployment reviews) and reactive work (Incident, Change Request) — it surfaces when thresholds are breached, when capacity is strained, or when SLAs are at risk.

System Monitoring is the Run Track's instantiation of the cross-track monitoring pattern. It is the most established monitoring practice in the model — SRE and DevOps teams routinely run 24/7 monitoring — and is now explicitly represented as a work entity.

## Purpose

Makes the continuous oversight of production and infrastructure explicit as a work type. Without System Monitoring (as a modeled entity):
- The work of watching dashboards, tuning alerts, and responding to thresholds is invisible in the Work Model
- The link between monitoring outputs and Incident creation or Capacity Planning is implicit
- SLA and performance baselines are not clearly owned as ongoing work

**Triggers downstream work:** Incident creation, Change Request, Capacity Planning adjustment, Deployment rollback.

## Fields

| Field | Type | Description |
|---|---|---|
| Scope | Text | What is being monitored (e.g., "Production US — API latency and uptime", "FX service — capacity and error rate") |
| Metrics Tracked | List (text or reference to Dim 7) | Uptime, latency (P50/P95/P99), error rate, capacity utilization, SLA metrics |
| Thresholds / Alerts | List (text) | When does monitoring trigger action (e.g., "Latency P95 > 500ms", "Error rate > 1%") |
| Cadence | Enum | `Continuous` / `Daily` / `Weekly` |
| Owner | String | Role/person or team responsible (e.g., SRE on-call) |
| Environment(s) | Reference (Dim 7) | Which environment(s) this monitoring covers |
| _Other fields to be refined._ | | |

## Statuses

| Status | Description |
|---|---|
| Active | Monitoring is in effect; thresholds and cadence are defined |
| Paused | Monitoring is temporarily suspended |
| Retired | Monitoring scope is no longer relevant (e.g., environment decommissioned) |

## Outputs / Artifacts

| Artifact | Category | Description | Downstream Consumer |
|---|---|---|---|
| Alert / Trigger | Evidence | When threshold is breached — prompts Incident creation or runbook execution | Incident, Change Request |
| SLA Report / Dashboard | Assessment | Periodic snapshot of uptime, latency, capacity | Capacity Planning, Win Review (for Customer Promise metrics) |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| May trigger | Incident (Track 3) | Monitoring surfaces service degradation |
| May trigger | Change Request (Track 3) | Monitoring may surface need for capacity or config change |
| Informs | Capacity Planning Task (Track 3) | Utilization and growth trends inform capacity forecasts |
| Informs | Deployment (Track 3) | Monitoring validates post-deployment health |
| May inform | Customer Value Metric (Dim 3) | SLA metrics may evidence Service Commitment fulfillment |

## Example

"Monitor production-us API — continuous; alert on P95 latency > 300ms or availability < 99.9%. Daily SLA report. Owner: SRE. Triggers Incident creation; feeds Capacity Planning and Win Review (Service Commitment)."
