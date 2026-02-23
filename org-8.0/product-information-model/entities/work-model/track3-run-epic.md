# Run Epic

**Model:** Work Model
**Track:** Track 3: The Run Track (Stability & Operations)
**Owner:** SRE Lead, Platform Engineering Lead

## Definition

A large body of operational engineering work scoped to a single Module (Dim 8), producing operational System Versions that contribute to Module Packages. Run Epics are the Run Track's counterpart to Build Track Epics — they define committed operational engineering scope. Where Build Track Epics deliver product functionality, Run Epics deliver **operational capability**: monitoring, automation, resilience, and environment-specific operational systems.

Run Epics may be triggered by:
- **Operational Readiness gaps** — a System's Operational Readiness assessment (Dim 7) reveals missing probes, insufficient automation, or inadequate monitoring
- **Incidents** — a post-mortem identifies operational tooling deficiencies (e.g., "we lacked synthetic probes for the LATAM payment corridor")
- **Operational improvement initiatives** — proactive investment in operational excellence (e.g., "reduce operational toil for Payments Module by 50%")
- **New Module Version readiness** — the Build Track produces a new Module Version that needs Run Track enrichment into a Module Package

Run Deliberations within Run Epic work produce **ODRs** (Dim 7), not ADRs (Dim 5). ODRs record operational decisions — probe strategy, automation approach, monitoring architecture — that emerge during operational engineering.

> **Run Track as engineering track.** The Run Track is not just an operational track — it is also an engineering track. Run Epics produce operational Systems with code, repos, CI/CD pipelines, tests, and System Versions. These Systems serve Operational Personas (Dim 7) and are independently deployable. The Run Track's Epic/Story/Task hierarchy mirrors the Build Track's, reflecting the reality that operational engineering follows the same work decomposition patterns as product engineering.

## Purpose

Makes operational engineering work visible and plannable. Without Run Epics:
- Operational system development (probes, automation, reconcilers) is informal and untracked
- The relationship between operational investment and Module Package readiness is invisible
- SRE engineering time is conflated with operational incident response — no distinction between "build operational systems" and "operate existing systems"
- Operational improvement initiatives have no structured work decomposition

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Descriptive name (e.g., "Build comprehensive health monitoring for Payments Module") |
| Module | Reference (Dim 8) | Which Module this Run Epic targets (same Module-scoping as Build Track Epics) |
| Trigger | Enum + Reference | What triggered this work: `Readiness Gap` (ref: Operational Readiness), `Incident` (ref: Incident), `Improvement Initiative`, `Module Version Readiness` (ref: Module Version) |
| Operational Systems Targeted | List of References (Dim 5) | Which operational Systems (Dim 5) this Epic will build or enhance |
| Target Module Package | Reference (Track 3) | Which Module Package this Epic's work contributes to (if applicable) |
| Acceptance Criteria | Text | What "done" looks like for this operational engineering effort |

## Statuses

| Status | Description |
|---|---|
| Planned | Run Epic identified and scoped; not yet started |
| In Progress | Run Stories and Technical Tasks actively being worked |
| Done | All Run Stories delivered; operational System Versions produced; Module Package contribution complete |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Scoped to | Module (Dim 8) | Run Epic is scoped to a single Module |
| Decomposes into | Run Story(ies) (Track 3) | Run Epic decomposes into Run Stories |
| Produces | Operational System Version(s) (Track 2) | Run Epic work produces operational System Versions |
| Contributes to | Module Package (Track 3) | Run Epic's operational System Versions enrich a Module Package |
| Triggered by | Operational Readiness (Dim 7) | Readiness gaps trigger Run Epics |
| Triggered by | Incident (Track 3) | Post-mortem findings trigger Run Epics |
| May produce | ODR(s) (Dim 7) | Run Deliberations within Run Epic work produce ODRs |

## Examples

| Run Epic | Module | Trigger | Operational Systems | Status |
|---|---|---|---|---|
| Build comprehensive health monitoring for Payments Module | Payments | Readiness Gap: payments-service lacks synthetic probes for LATAM corridors | payments-healthcheck (new), payment-reconciler (enhance) | In Progress |
| Automate cert rotation for FX Module | FX | Incident: INC-2341 (expired cert caused 2-hour FX outage) | fx-cert-rotator (new) | Planned |
| Reduce operational toil for Compliance Module — LATAM | Compliance | Improvement Initiative: Q2 operational excellence | compliance-audit-reporter (new), compliance-alert-tuner (new) | Planned |

---
