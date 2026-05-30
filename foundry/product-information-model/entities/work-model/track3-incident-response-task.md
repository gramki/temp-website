# Incident Response Task

**Model:** Work Model
**Track:** Run
**Category:** Work Entity (Reactive)
**Owner:** DevOps, Site Reliability Engineers (SRE)

## Definition

The primary work entity for triaging, investigating, and resolving an Incident. An Incident Response Task is created when an Incident (artifact) is produced; it captures the work of restoring service to SLO-compliant state. The Incident Response Task's Definition of Done is **service restored** — not root cause eliminated. Root cause resolution is downstream work: Bugs (Build), Run Epics (Run), or Signals (Discovery).

> **Escalation within response.** SEV-0 and SEV-1 incidents often involve escalation from initial responders to specialized teams (e.g., database team, security team, vendor support). The Incident Response Task captures escalation as fields (Escalation Level, Escalated To). The escalation *policy* — who gets called at each level — is an Operating Model concern.
>
> **Major Incident coordination.** SEV-0 and SEV-1 incidents may require a dedicated Incident Commander role and war-room coordination. This is an Operating Model concern (roles and ceremonies); the Incident Response Task's timeline and decision fields capture the coordination artifacts.

## Purpose

Makes the work of incident response visible, trackable, and measurable. Without Incident Response Task:
- Incident handling is invisible in the Work Model — there is no structured entity for the triage-through-resolution work
- Response effectiveness cannot be measured (was the response fast enough? did escalation help?)
- The cross-track outputs of incident response (Bugs, Signals, emergency Change Requests) have no producing entity
- The distinction between "what happened" (Incident artifact) and "what we did about it" (Incident Response Task) is lost

## Fields

| Field | Type | Description |
|---|---|---|
| Incident | Reference (Run) | The Incident artifact this task responds to |
| Severity | Enum | `SEV-0` / `SEV-1` / `SEV-2` / `SEV-3` / `SEV-4` — inherited from Incident, may be revised during triage |
| Assigned Responder(s) | List (String) | Person(s) or team(s) assigned to respond |
| Escalation Level | Enum | `L1` / `L2` / `L3` / `Vendor` — current escalation level |
| Escalated To | List (String) | Team(s) or individual(s) the incident has been escalated to |
| Affected System(s) | List of References (Technical) | Which System(s) are degraded (inherited from Incident, may be refined) |
| Affected Module(s) | List of References (Structural) | Which Module(s) are impacted (inherited from Incident, may be refined) |
| Affected Environment(s) | List of References (Operational) | Which Deployment Environment(s) are affected |
| Affected Tenant(s) | List of References (Run) | Optional — when impact is localized to specific tenants |
| Impact Scope | Text | Quantified impact: tenant count, transaction volume affected, revenue impact estimate |
| Workaround Applied | Text | Description of any temporary workaround applied to restore service (feeds Bug's Workaround field if a Bug is created) |
| Root Cause (Preliminary) | Text | Initial root cause assessment during response — may be refined in Post-Incident Review |
| Resolution Summary | Text | How service was restored to SLO-compliant state |
| Communication Plan | Text | What was communicated to whom, via which channels (coordinates with Customer Communication Task) |

## Statuses

| Status | Description |
|---|---|
| Triaged | Incident acknowledged; severity confirmed or revised; responder(s) assigned |
| Investigating | Active investigation underway; root cause being determined |
| Mitigating | Workaround or mitigation being applied to restore service |
| Resolved | Service restored to SLO-compliant state; resolution documented |
| Closed | All follow-up outputs (Bug, Signal, Change Request) have been created; task is complete |

```
State Diagram:

  Triaged ──→ Investigating ──→ Mitigating ──→ Resolved ──→ Closed
                    │                              ↑
                    └──────────────────────────────┘
                    (direct resolution without mitigation)

Triggers:
  Triaged → Investigating:    Responder begins investigation
  Investigating → Mitigating: Root cause identified or workaround found
  Investigating → Resolved:   Direct fix applied without separate mitigation phase
  Mitigating → Resolved:      Workaround or fix confirmed effective; SLO restored
  Resolved → Closed:          All follow-up outputs created; no further action needed
```

## Definition of Done

**Service restored to SLO-compliant state.** The Incident Response Task is "done" when:
1. The affected System(s) are operating within their Operational Targets (Operational)
2. The Service Commitments (Customer Value) tested by this incident are no longer being breached
3. A resolution summary is documented
4. Any follow-up work items (Bug, Signal, emergency Change Request) have been created

Root cause elimination is **not** part of this DoD — it is downstream work tracked via Bug (Build), Run Epic (Run), or Signal → Discovery (Discovery).

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Responds to | Incident (Run) | Incident Response Task responds to an Incident artifact |
| Coordinates with | Customer Communication Task (Run) | Communication work runs in parallel with response |
| Followed by | Post-Incident Review (Run) | PIR follows response for SEV-0/1/2 incidents |
| May produce | Bug (Build) | Response investigation may reveal a product defect (provenance: Run) |
| May produce | Signal — Problem (Strategy) | Recurring or systemic issues may surface as Signals for Discovery |
| May trigger | Change Request (Run) | Emergency-Technical changes may originate from incident response |
| May trigger | Maintenance Task (Run) | Corrective maintenance may be needed |
| Restores | Operational Target / SLO (Operational) | Response restores service to SLO-compliant state |
| Tests | Service Commitment (Customer Value) | Response effectiveness tests whether SLA restoration meets commitments |

## Examples

| Incident | Severity | Assigned | Escalation | Workaround | Resolution | Status |
|---|---|---|---|---|---|---|
| INC-2026-0847 "FX API latency spike" | SEV-1 | SRE On-Call (L1) → FX Team (L2) | L2 | Rate-limiting applied to reduce load | FX cache rebuilt; latency restored to P95 < 200ms | Resolved |
| INC-2026-0849 "Database cluster failover" | SEV-0 | SRE On-Call (L1) → DBA Team (L2) → Cloud Vendor (L3) | L3 | Traffic routed to DR cluster | Primary cluster restored; failover validated; traffic returned | Closed |
| INC-2026-0850 "Post-deployment error rate" | SEV-2 | SRE On-Call (L1) | L1 | Deployment rolled back via rollback script | Rollback completed; error rate returned to baseline | Resolved |
| INC-2026-0851 "Compliance dashboard stale" | SEV-3 | Platform Engineer (L1) | L1 | — | Cache invalidation triggered; data refreshed | Closed |

---
