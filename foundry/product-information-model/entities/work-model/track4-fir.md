# First Information Report (FIR)

**Model:** Work Model
**Track:** Win
**Category:** Reactive (Intake / Envelope)
**Owner:** Customer Support (Win Team) — triage and routing; any team may create

## Definition

The atomic intake unit for all product-in-operation feedback. Every piece of feedback — whether from an external customer, a prospect, an SRE detecting a monitoring alert, or a QA engineer observing a regression — enters the system as an FIR. The FIR is triaged (typically by the Win team's customer support function) and then routed: the full FIR, or specific sub-parts of it, are dispatched as work items to appropriate tracks.

> **Always FIR-first.** Win Cases, Incidents, Bugs, Signals, and Maintenance Tasks that originate from product-in-operation feedback are always sub-items of an FIR. They cannot be created independently of the FIR intake flow. This ensures PFR-Win is the single, comprehensive origination point for all operational feedback and guarantees full traceability from initial report through resolution. See DR-032.
>
> **Envelope pattern.** FIR parallels Change Request (Run): Change Request is the governance envelope for deployment-related work; FIR is the intake envelope for all product-in-operation feedback. Both are parent entities whose lifecycle depends on the completion of their sub-items.

## Purpose

Makes every feedback interaction — internal or external — visible, traceable, and accountable. Without FIR:
- Customer complaints route directly to Win Cases with no universal tracking of what entered the system
- SRE alerts create Incidents with no record visible to the Win team or customer-facing view
- The same issue reported by three customers produces three disconnected work items with no common parent
- There is no single point to answer "what happened, who reported it, and what did we do about it?"
- Cross-track traceability from initial report to final resolution is incomplete

FIR also serves as the customer-facing (or reporter-facing) envelope: the reporter interacts with the FIR lifecycle (notified on triage, updated on progress, notified on resolution), while sub-items represent track-specific internal work.

## Fields

| Field | Type | Description |
|---|---|---|
| ID | String | Unique identifier (e.g., `FIR-2026-04291`) |
| Title | String | Brief summary of the report |
| Reporter | String | Who reported — person name, team, or monitoring system identifier |
| Reporter Type | Enum | `Customer` / `User` / `Partner` / `SRE` / `QA` / `Developer` / `Support` / `Monitoring System` |
| Provenance | Enum | `External` (customer/partner/prospect) / `Run` (SRE, monitoring) / `Build` (QA, developer) / `Internal` (PM, support proactive observation) |
| Channel | Enum | `Email` / `Phone` / `Chat` / `Portal` / `Monitoring Alert` / `Internal Observation` / `API` |
| Customer / Tenant | Reference (ESR / Operational) | Optional — which customer organization or tenant is affected. References ESR for customer identity, Deployment Environment (Operational) for tenant. |
| Description | Text | Raw report as received — unedited original content |
| Category (Pre-Triage) | Enum | `Service Degradation` / `Defect` / `Missing Capability` / `Question` / `Request` / `Dissatisfaction` / `Observation` / `Other` |
| Triage Assessment | Text | Triage team's routing rationale — why sub-items were created in the tracks they were |
| Sub-Items | List of References | Routed work items with their track, entity type, and ID |
| Priority | Enum | `Critical` / `High` / `Medium` / `Low` — initial triage assessment |
| Resolution Summary | Text | How the FIR was ultimately resolved — aggregated from sub-item resolutions |

## Statuses

| Status | Description |
|---|---|
| Created | Report received, awaiting triage |
| Triaged | Sub-items routed to appropriate tracks (or resolved directly for trivial inquiries) |
| In Progress | One or more sub-items are being actively worked |
| Resolved | All sub-items resolved; resolution summary prepared |
| Closed | Reporter notified of resolution; FIR archived |

> **Direct resolution.** An FIR can transition `Created` → `Triaged` → `Resolved` → `Closed` with zero sub-items when the response is immediate and trivial (e.g., "What are your supported currencies?" — answered during triage). The Triage Assessment captures the response.

```
Created ──► Triaged ──► In Progress ──► Resolved ──► Closed
                │                                       ▲
                └──── (direct resolution, 0 sub-items) ─┘
```

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| May produce | Incident (Track 3, OPR) | Service degradation routed as Incident artifact; Incident Response Task created |
| May produce | Bug (Track 2, WR) | Defect routed to Build Track (provenance: Win or Run) |
| May produce | Signal — Problem / Need / Opportunity (Strategy, PIR) | Feedback routed as discovery input |
| May produce | Win Case (Track 4, WR) | Query / Service Request / Complaint / Escalation — always a sub-item of this FIR |
| May produce | Maintenance Task (Track 3, WR) | Operational maintenance identified during triage |
| Contains | Sub-work items (all tracks) | All routed items are sub-items of the FIR and retain bidirectional references |
| Assessed by | Win Review (Win) | FIR volume, triage quality, routing patterns, and resolution quality are assessed |
| Monitored by | Win Monitoring (Win) | FIR volume, resolution time, and routing patterns are continuously tracked |
| Feeds | Customer Value Metric (Customer Value) | FIR response and resolution times feed Service Level Metrics |
| References | Customer / Tenant (ESR / Operational) | Which external stakeholder and/or tenant is affected |
| May correlate with | Other FIR(s) | Multiple FIRs may report the same underlying issue; correlation noted during triage |

## Outputs / Artifacts

| Artifact | Category | Description | Downstream Consumer |
|---|---|---|---|
| Routed sub-items | Specification | Triage routing decisions that create work items in other tracks | Track 2 (Bug), Track 3 (Incident, Maintenance Task), Track 4 (Win Case), Strategy (Signal) |
| FIR Resolution Record | Evidence | Complete record of the FIR lifecycle: original report, triage assessment, sub-item references, resolution summary | Win Review, PEIR lineage |

## Definition of Done

| Component | Criteria |
|---|---|
| Entry Criteria | A report about the product in operation has been received from any source |
| Exit Criteria | All sub-items are resolved; resolution summary is prepared; reporter has been notified |
| Artifact Checklist | (1) Triage Assessment recorded, (2) All sub-items created with FIR reference, (3) Resolution Summary captures aggregated outcome, (4) Reporter notification sent |

## Guidance Reference

_See: [Operating Model — FIR Triage Process, FIR Escalation Protocol, Run Team FIR Creation Process, FIR Resolution Notification — to be developed]_

## Examples

| ID | Reporter Type | Channel | Category | Priority | Sub-Items | Status |
|---|---|---|---|---|---|---|
| FIR-2026-04291 | Customer | Portal | Service Degradation | Critical | INC-2026-0847 (Run), WC-2026-1203 Complaint (Win) | In Progress |
| FIR-2026-04292 | Monitoring System | Monitoring Alert | Service Degradation | Critical | INC-2026-0848 (Run) | In Progress |
| FIR-2026-04293 | Customer | Email | Missing Capability | Medium | SIG-2026-0412 Need (Strategy) | Triaged |
| FIR-2026-04294 | Customer | Chat | Question | Low | _(direct resolution — answered during triage)_ | Closed |
| FIR-2026-04295 | SRE | Internal Observation | Defect | High | BUG-2026-0891 (Build), INC-2026-0849 (Run) | In Progress |
| FIR-2026-04296 | QA | Internal Observation | Defect | Medium | BUG-2026-0892 (Build) | Resolved |
| FIR-2026-04297 | Partner | Portal | Request | Medium | WC-2026-1204 Service Request (Win) | In Progress |

### Narrative Example

**FIR-2026-04291:** Customer "GlobalPay SA" reports via the support portal: "FX API latency spiked to 5000ms during our peak settlement window — we lost 3 hours of processing." The Win team creates FIR-2026-04291 with Category: Service Degradation, Priority: Critical.

**Triage:** The support engineer reviews the report, correlates with monitoring data, and routes:
- **Incident INC-2026-0847** (Run) — for SRE investigation and service restoration
- **Win Case WC-2026-1203** (Track 4, Complaint) — for customer communication and relationship management

Both sub-items carry `Originating FIR: FIR-2026-04291`. The FIR moves to `In Progress`.

**Resolution:** INC-2026-0847 is resolved (FX cache rebuilt, latency restored). The Incident Response Task produces Bug BUG-2026-0893 (provenance: Run) for the root cause fix. WC-2026-1203 is resolved (customer notified, SLA breach acknowledged). FIR-2026-04291 moves to `Resolved`, resolution summary prepared, and GlobalPay SA is notified. FIR moves to `Closed`.
