# Incident

**Model:** Work Model
**Track:** Run
**Category:** Work Artifact (Observation Record)
**Owner:** DevOps, Site Reliability Engineers (SRE)

## Definition

A durable observation record of unplanned service degradation — an event where the production system is performing below expected SLOs or is unavailable. An Incident is a **work artifact**, not a work entity: it records *what happened*, not *what to do about it*. The work of responding to an incident is modeled by Incident Response Task; the work of learning from it is modeled by Post-Incident Review.

This separation parallels the Deployment pattern: Deployment Task (work entity) produces Deployment (artifact/record). Similarly, System Monitoring, operator observations, or Win Case complaints produce Incident records, and Incident Response Tasks respond to them.

> **Severity uses SEV-0 through SEV-4.** SEV-0 is a total service outage affecting all tenants; SEV-4 is a minor degradation with no customer-visible impact. SEV-0, SEV-1, and SEV-2 incidents require a Post-Incident Review; the Operating Model may adjust this threshold.

## Purpose

Captures the factual record of service degradation as a structured, queryable artifact. Without Incident as a distinct artifact:
- The observation (what happened) is conflated with the response (what we did about it) — making it impossible to assess response effectiveness independently
- Incident correlation (parent/child, recurrence) has no anchor entity
- The feedback loop from incidents to Run Track planning (Deployment Planning, Capacity Planning, Run Epic scoping) has no structured input
- SLA breach tracking against Customer Promises (Customer Value) and error budget consumption against Operational Targets (Operational) has no evidence entity
- Change-caused incident tracking (linking a deployment to the incident it caused) has no formal mechanism

## Fields

| Field | Type | Description |
|---|---|---|
| ID | String | Unique identifier (e.g., "INC-2026-0847") |
| Title | String | Brief description (e.g., "FX API latency spiked to 5000ms") |
| Description | Text | Detailed description of the observed degradation |
| Severity | Enum | `SEV-0` / `SEV-1` / `SEV-2` / `SEV-3` / `SEV-4` |
| Originating FIR | Reference (Win) | Optional — the FIR from which this Incident was routed (DR-032). Present when a customer report or operator observation created an FIR that was triaged as a service degradation. Auto-created FIRs from monitoring alerts also carry this reference. |
| Detection Source | Enum | `Alert` (from System Monitoring) / `Complaint` (from Win Case) / `Observation` (operator-detected) / `Dependent` (reported by upstream/downstream system) |
| Detection Time | Timestamp | When the degradation was first detected |
| Affected System(s) | List of References (Technical) | Which System(s) are degraded |
| Affected Module(s) | List of References (Structural) | Which Module(s) are impacted |
| Affected Environment(s) | List of References (Operational) | Which Deployment Environment(s) are affected |
| Affected Tenant(s) | List of References (Run) | Optional — when impact is localized to specific tenants in an environment |
| Customer Impact Summary | Text | Business-level impact description (e.g., "All LATAM cross-border payments failing; ~200 tenants affected; estimated $50K/hour revenue impact") |
| Timeline | List (timestamp + event) | Key events: detection, acknowledgment, escalations, mitigation steps, resolution |
| Parent Incident | Reference (Run) | Optional — when this incident is a symptom of a broader root-cause incident (e.g., database failure causing incidents in Payments, FX, and Settlements) |
| Related Incidents | List of References (Run) | Optional — links to prior incidents of the same type (recurrence tracking) or concurrent incidents from the same root cause |
| Caused By | Reference (Run) | Optional — references a Deployment (artifact) or Change Request when the incident was caused by a deployment or change |
| SLA Breach | Text | Whether any Service Commitments (Customer Value) were breached, and which ones |
| Response Time | Duration | Time from detection to first responder acknowledgment |
| Resolution Time | Duration | Time from detection to service restored to SLO-compliant state |

## Statuses

| Status | Description |
|---|---|
| Open | Incident detected; record created; awaiting acknowledgment |
| Acknowledged | Responder has acknowledged the incident; Incident Response Task is active |
| Resolved | Service has been restored to SLO-compliant state; Incident Response Task is closed |
| Reviewed | Post-Incident Review has been completed; lessons absorbed into planning and Definition Model |

> **Reviewed is the terminal state.** An incident is not fully processed until its lessons have been absorbed — through PIR (for SEV-0/1/2) or through Run Track planning consumption (for SEV-3/4). The Operating Model determines what constitutes "reviewed" for lower-severity incidents.

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| May originate from | FIR (Track 4, PFR-Win) | Incidents routed from FIR intake — customer reports, operator observations, or auto-created monitoring FIRs (DR-032) |
| Produced by | System Monitoring (Run) | Alert-detected incidents are produced by System Monitoring |
| Corresponds to | Win Case — Complaint (Win) | Customer-reported degradation may have a corresponding Incident record |
| Responded to by | Incident Response Task (Run) | The work of triaging, investigating, and resolving the incident |
| Communicated by | Customer Communication Task (Run) | The work of communicating status, impact, and resolution to affected parties |
| Reviewed by | Post-Incident Review (Run) | Structured learning activity; mandatory for SEV-0/1/2 |
| References | Service Commitment (Customer Value) | Incident tests whether Service Commitments are being met |
| References | Operational Target / SLO (Operational) | Incident consumes error budget against Operational Targets |
| Reveals gaps in | Operational Readiness (Operational) | Incident patterns per System x Environment reveal readiness gaps |
| Evidences | Operational Pain (Operational) | Recurring incidents are evidence for Operational Pains |
| Caused by | Deployment (Run) or Change Request (Run) | When a deployment or change caused the incident |
| Informs | Deployment Planning Task (Run) | Incident history informs deployment risk assessment |
| Informs | Capacity Planning Task (Run) | Capacity-related incidents inform forecasting |
| Informs | Run Epic (Run) | Incident patterns inform operational engineering prioritization |
| Feeds | Customer Value Metric (Customer Value) | Incident response/resolution times feed Service Level Metric actuals |
| May affect | Interaction Flow (Technical) | Incidents often reveal failure points in cross-system flows |

## Severity Definitions

| Severity | Definition | Example | PIR Required |
|---|---|---|---|
| SEV-0 | Total service outage; all tenants affected; no workaround | "Complete payment processing failure across all environments" | Yes |
| SEV-1 | Major degradation; significant tenant impact; limited or no workaround | "FX API latency spiked to 5000ms; cross-border payments timing out for LATAM tenants" | Yes |
| SEV-2 | Partial degradation; subset of tenants or capabilities affected; workaround available | "Settlement file generation delayed by 4 hours; manual export available as workaround" | Yes |
| SEV-3 | Minor degradation; limited customer-visible impact; workaround available | "Dashboard loading slowly (8s vs. normal 2s) for compliance reports" | Operating Model decision |
| SEV-4 | Minimal degradation; no customer-visible impact; internal observation only | "Background reconciliation job running 20% slower than baseline" | No |

## Examples

| ID | Severity | Title | Detection | Affected | Caused By | SLA Breach |
|---|---|---|---|---|---|---|
| INC-2026-0847 | SEV-1 | "FX API latency spiked to 5000ms" | Alert (System Monitoring: P95 > 500ms threshold) | fx-service, FX Module, Production US-East | — | Yes: "sub-200ms P95 latency" Service Commitment |
| INC-2026-0848 | SEV-1 | "Cross-border payments timing out" | Alert (System Monitoring: error rate > 1%) | payments-service, Payments Module, Production US-East | — | Yes: "99.9% API uptime" Service Commitment |
| INC-2026-0849 | SEV-0 | "Database cluster failover — all services degraded" | Alert (System Monitoring: health check failures) | All Systems, All Modules, Production US-East | — | Yes: multiple commitments |
| INC-2026-0850 | SEV-2 | "Elevated error rate after payments-system v3.1.0 deployment" | Alert (Verification Task failure) | payments-system, Payments Module, Production LATAM | Deployment: "payments-system sds-1.2 → production-latam" | No (within SLA but degraded) |
| INC-2026-0851 | SEV-3 | "Compliance dashboard stale data" | Complaint (Win Case WC-445) | compliance-service, Compliance Module, Production US-East | — | No |

> **Parent/child example:** INC-2026-0849 (database cluster failover) is the parent incident. INC-2026-0847 (FX latency) and INC-2026-0848 (payment timeouts) are child incidents with `Parent Incident: INC-2026-0849`. This prevents counting 3 root causes when there is only 1.

---
