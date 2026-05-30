# Run Epic

**Model:** Work Model
**Track:** Run
**Owner:** SRE Lead, Platform Engineering Lead

## Definition

A large body of operational engineering work scoped to a single Module (Structural), producing operational **System Versions** through the **Build Track** (same versioning chain as product Systems). Run Epics are the Run Track's counterpart to Build Track Epics — they define committed operational engineering scope. Where Build Track Epics deliver product functionality, Run Epics deliver **operational capability**: monitoring, automation, resilience, and operational Systems declared in the Product Specification.

Run Epics may be triggered by:
- **Operational Readiness gaps** — a System's Operational Readiness assessment (Operational) reveals missing probes, insufficient automation, or inadequate monitoring
- **Post-Incident Reviews** — a PIR identifies operational tooling deficiencies (e.g., "we lacked synthetic probes for the LATAM payment corridor")
- **Operational improvement initiatives** — proactive investment in operational excellence (e.g., "reduce operational toil for Payments Module by 50%")
- **New System Version readiness** — a product System Version is Released and operational Systems need enhancement before deployment

Run Deliberations within Run Epic work produce **ODRs** (Operational), not ADRs (Technical). ODRs record operational decisions — probe strategy, automation approach, monitoring architecture — that emerge during operational engineering.

> **Run Track as engineering track.** The Run Track is not just an operational track — it is also an engineering track. Run Epics produce operational Systems with code, repos, CI/CD pipelines, tests, and System Versions. These Systems serve Operational Personas (Operational) and are independently deployable. The Run Track's Epic/Story/Task hierarchy mirrors the Build Track's, reflecting the reality that operational engineering follows the same work decomposition patterns as product engineering.

## Purpose

Makes operational engineering work visible and plannable. Without Run Epics:
- Operational system development (probes, automation, reconcilers) is informal and untracked
- The relationship between operational investment and System Version / Product Version readiness is invisible
- SRE engineering time is conflated with operational incident response — no distinction between "build operational systems" and "operate existing systems"
- Operational improvement initiatives have no structured work decomposition

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Descriptive name (e.g., "Build comprehensive health monitoring for Payments Module") |
| Module | Reference (Structural) | Which Module this Run Epic targets (same Module-scoping as Build Track Epics) |
| Trigger | Enum + Reference | What triggered this work: `Readiness Gap` (ref: Operational Readiness), `Post-Incident Review` (ref: PIR / Incident), `Incident Pattern` (ref: Incident history), `Improvement Initiative`, `System Version Readiness` (ref: System Version) |
| Operational Systems Targeted | List of References (Technical) | Which operational Systems (Technical) this Epic will build or enhance |
| Target System Version | Reference (Run) | Which System Version this Epic's work contributes to (if applicable) |
| Acceptance Criteria | Text | What "done" looks like for this operational engineering effort |

## Statuses

| Status | Description |
|---|---|
| Planned | Run Epic identified and scoped; not yet started |
| In Progress | Run Stories and Technical Tasks actively being worked |
| Done | All Run Stories delivered; operational System Versions produced and Released |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Scoped to | Module (Structural) | Run Epic is scoped to a single Module |
| Decomposes into | Run Story(ies) (Run) | Run Epic decomposes into Run Stories |
| Produces | Operational System Version(s) | Run Epic work produces operational System Versions (same System Version entity type) |
| Contributes to | System Version(s) (Build) | Run Epic's work produces Component Versions and sealed System Versions for operational Systems |
| Triggered by | Operational Readiness (Operational) | Readiness gaps trigger Run Epics |
| Triggered by | Post-Incident Review (Run) | PIR corrective actions trigger Run Epics |
| Informed by | Incident history (Run) | Incident patterns inform Run Epic scoping and prioritization |
| May produce | ODR(s) (Operational) | Run Deliberations within Run Epic work produce ODRs |

## Examples

| Run Epic | Module | Trigger | Operational Systems | Status |
|---|---|---|---|---|
| Build comprehensive health monitoring for Payments Module | Payments | Readiness Gap: payments-service lacks synthetic probes for LATAM corridors | payments-healthcheck (new), payment-reconciler (enhance) | In Progress |
| Automate cert rotation for FX Module | FX | Post-Incident Review: PIR for INC-2341 (expired cert caused 2-hour FX outage) | fx-cert-rotator (new) | Planned |
| Reduce operational toil for Compliance Module — LATAM | Compliance | Improvement Initiative: Q2 operational excellence | compliance-audit-reporter (new), compliance-alert-tuner (new) | Planned |

---
