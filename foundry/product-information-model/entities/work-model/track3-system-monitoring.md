# System Monitoring

**Model:** Work Model
**Track:** Run
**Category:** Monitoring
**Owner:** DevOps, SRE

## Definition

Continuous tracking of operational health across Systems (Technical), composed **System Versions** and **Product Versions** in deployment, Tenant health, and cross-System operational wiring. System Monitoring sits between periodic assessment (Capacity Planning, deployment reviews) and reactive work (Incident, Change Request) — it surfaces when thresholds are breached, when capacity is strained, when SLAs are at risk, or when Tenant-level metrics degrade.

System Monitoring is the Run Track's **operational** monitoring entity — it monitors the health of running systems and compositions. It is distinct from Run Engineering Monitoring, which tracks the engineering velocity and quality of Run Track engineering work (Run Epics, Run Stories, Technical Tasks). System Monitoring is the most established monitoring practice in the model — SRE and DevOps teams routinely run 24/7 monitoring — and is now explicitly represented as a work entity.

> **Scope includes System and Product composition.** System Monitoring covers individual Systems, cross-System health within a deployed Product Version (do Systems in the Product Version BOM work together in production?), and Tenant health (customer-specific health within an environment). See DR-036.

## Purpose

Makes the continuous oversight of production and infrastructure explicit as a work type. Without System Monitoring (as a modeled entity):
- The work of watching dashboards, tuning alerts, and responding to thresholds is invisible in the Work Model
- The link between monitoring outputs and Incident creation or Capacity Planning is implicit
- SLA and performance baselines are not clearly owned as ongoing work

**Triggers downstream work:** Incident creation, Change Request, Capacity Planning adjustment, Deployment rollback, Run Epic creation (when monitoring reveals operational tooling gaps).

## Fields

| Field | Type | Description |
|---|---|---|
| Scope | Text | What is being monitored (e.g., "Production US — API latency and uptime", "FX service — capacity and error rate") |
| Metrics Tracked | List (text or reference to Operational) | Uptime, latency (P50/P95/P99), error rate, capacity utilization, SLA metrics |
| Thresholds / Alerts | List (text) | When does monitoring trigger action (e.g., "Latency P95 > 500ms", "Error rate > 1%") |
| Cadence | Enum | `Continuous` / `Daily` / `Weekly` |
| Owner | String | Role/person or team responsible (e.g., SRE on-call) |
| Environment(s) | Reference (Operational) | Which environment(s) this monitoring covers |
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
| Produces | Incident (Track 3, artifact) | Monitoring produces Incident records when service degradation is detected |
| Triggers | Incident Response Task (Run) | Incident creation triggers response work |
| May trigger | Change Request (Run) | Monitoring may surface need for capacity or config change |
| May trigger | Run Epic (Run) | Monitoring may reveal operational tooling gaps requiring engineering |
| Informs | Capacity Planning Task (Run) | Utilization and growth trends inform capacity forecasts |
| Informs | Deployment Task (Run) | Monitoring validates post-deployment health |
| May inform | Customer Value Metric (Customer Value) | SLA metrics may evidence Service Commitment fulfillment |

## Example

"Monitor production-us API — continuous; alert on P95 latency > 300ms or availability < 99.9%. Daily SLA report. Owner: SRE. Triggers Incident creation; feeds Capacity Planning and Win Review (Service Commitment)."

"Monitor payments-system v3.1.0 health in production-latam — alert on cross-Component latency degradation (payments-service → payment-reconciler P95 > 400ms); Product v4.0.0 cross-System smoke metrics; Tenant-level error rate > 1%. Owner: Payments SRE."
