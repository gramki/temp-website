# Post-Incident Review

**Model:** Work Model
**Track:** Run
**Category:** Work Entity (Deliberation / Assessment)
**Owner:** Engineering Leadership, SRE Lead

## Definition

A structured, collaborative assessment activity where stakeholders convene after an incident is resolved to reconstruct what happened, identify root causes and contributing factors, quantify impact, and determine corrective actions. Post-Incident Review is the Run Track's parallel to Deliberation (Discovery) and Win Review (Win) — all are structured assessment activities that produce structured outputs.

PIR produces two outputs:
1. **Post-Incident Report** (assessment artifact) — the durable knowledge artifact capturing timeline, root cause analysis, impact, corrective actions, and lessons learned
2. **Corrective actions** — follow-up work items routed to the appropriate track: Bugs (Build), Run Epics (Run), Signals (Discovery), ODRs (Operational), Evolve Findings (Evolve), Maintenance Tasks (Run)

> **PIR mandate.** SEV-0, SEV-1, and SEV-2 incidents require a Post-Incident Review. The Operating Model may adjust this threshold — for example, requiring PIR for all SEV-3 incidents in a specific module, or waiving PIR for SEV-2 incidents that were resolved within 15 minutes with no customer impact. The Work Model states the default; the Operating Model owns the policy.

> **Blameless by design.** PIR focuses on systemic causes and process improvements, not individual fault. The entity structure deliberately captures "Contributing Factors" (systemic conditions) rather than "Who caused this." This is a modeling choice — the Operating Model reinforces it through ceremony design and facilitation guidance.

## Purpose

Makes post-incident learning visible, structured, and actionable. Without Post-Incident Review:
- Incident response resolves the symptom but the organization doesn't learn from it
- Root cause analysis is informal and inconsistent
- Corrective actions are verbal commitments that are never tracked
- The feedback loop from incidents to product, operational, and process improvements is broken
- Incident patterns that should surface as Operational Pains or Signals are invisible

**PIR is the primary mechanism by which reactive incidents produce structured learning that flows back into the Definition Model and drives product/process improvement.**

## Fields

| Field | Type | Description |
|---|---|---|
| Incident(s) | List of References (Run) | Incident artifact(s) being reviewed — may batch related incidents (e.g., parent + children) |
| Incident Response Task(s) | List of References (Run) | The response task(s) for context on what was done |
| Participants | List (String) | Roles/persons participating (e.g., SRE Lead, FX Team Lead, Product Manager, Incident Commander) |
| Timeline Reconstruction | Text | Detailed chronological reconstruction of the incident from detection to resolution |
| Root Cause Analysis | Text | Final root cause determination (5-whys, fishbone, or other technique). Distinct from the preliminary root cause in Incident Response Task. |
| Contributing Factors | List (Text) | Systemic conditions that enabled or amplified the incident (e.g., "alert fatigue delayed initial response by 8 minutes", "no automated rollback for database migrations") |
| Impact Assessment (Final) | Text | Quantified impact: affected tenants, duration, revenue impact, SLA breaches, compliance implications |
| Customer Communication Assessment | Text | Evaluation of communication effectiveness: timeliness, accuracy, channel coverage |
| Corrective Actions | List (Action + Owner + Deadline + Track) | Specific follow-up actions with accountability and track routing |

## Statuses

| Status | Description |
|---|---|
| Scheduled | PIR has been scheduled; incident is resolved; participants identified |
| In Progress | PIR is being conducted; timeline and root cause being reconstructed |
| Complete | PIR is done; Post-Incident Report produced; corrective actions created and routed |

```
State Diagram:

  Scheduled ──→ In Progress ──→ Complete

Triggers:
  Scheduled → In Progress:  PIR session begins
  In Progress → Complete:   Post-Incident Report finalized; all corrective actions created
```

## Outputs

| Output | Category | Description | Downstream Consumer |
|---|---|---|---|
| Post-Incident Report | Assessment artifact | Durable knowledge artifact: timeline, RCA, contributing factors, impact, corrective actions, lessons learned | Run Track planning, Discovery Track, Win Track |
| Bug (Build) | Work entity (follow-up) | Product defect identified as root cause; provenance: Run | Build Track |
| Signal — Problem (Strategy) | Definition Model update | Systemic product issue surfaced for Discovery | Discovery Track |
| Run Epic (Run) | Work entity (follow-up) | Operational tooling gap identified (e.g., missing probes, insufficient automation) | Run Track |
| ODR (Operational) | Definition Model update | Operational decision driven by incident findings (e.g., deployment strategy change, monitoring architecture revision) | Definition Model |
| Evolve Finding (Evolve) | Work artifact (follow-up) | Process gap identified (e.g., "runbook was outdated", "escalation policy unclear") | Evolve Track |
| Maintenance Task (Run) | Work entity (follow-up) | Corrective maintenance needed (e.g., "patch library X across all environments") | Run Track |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Reviews | Incident(s) (Run) | PIR reviews one or more Incident artifacts |
| Reviews | Incident Response Task(s) (Run) | PIR reviews the response effectiveness |
| Produces | Post-Incident Report (artifact) | Primary output: durable assessment artifact |
| May produce | Bug (Build) | Root cause is a product defect |
| May produce | Signal — Problem (Strategy) | Systemic issue surfaced for Discovery |
| May trigger | Run Epic (Run) | Operational tooling gap requires engineering investment |
| May produce | ODR (Operational) | Operational decision required |
| May produce | Evolve Finding (Evolve) | Process gap identified |
| May produce | Maintenance Task (Run) | Corrective maintenance needed |
| May update | Operational Readiness (Operational) | PIR findings may downgrade readiness posture for affected System x Environment |
| May update | Operational Pain (Operational) | PIR may surface or provide evidence for Operational Pains |
| Informs | Deployment Planning Task (Run) | PIR findings inform deployment risk assessment |

## Examples

| PIR | Incident(s) | Root Cause | Corrective Actions | Status |
|---|---|---|---|---|
| "PIR: Database cluster failover — 2026-02-15" | INC-2026-0849, INC-2026-0847, INC-2026-0848 | "Cloud provider AZ failure triggered failover; application connection pool did not reconnect within timeout" | Bug: "Connection pool reconnect logic" (Build); Run Epic: "Automated AZ failover validation" (Run); ODR: "Multi-AZ deployment requirement for all stateful services" (Operational) | Complete |
| "PIR: Post-deployment error rate — Payments LATAM" | INC-2026-0850 | "Database migration script did not handle existing data format for LATAM-specific payment types" | Bug: "Migration script LATAM data handling" (Build); Evolve Finding: "Deployment Planning checklist should include LATAM data format validation" (Evolve) | Complete |
| "PIR: FX API latency spike" | INC-2026-0847 | "Cache eviction under load caused thundering herd to upstream FX provider" | Bug: "Cache stampede protection" (Build); Run Epic: "FX cache warming automation" (Run) | Scheduled |

---
