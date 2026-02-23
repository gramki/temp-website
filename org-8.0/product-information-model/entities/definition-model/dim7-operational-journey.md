# Operational Journey

**Model:** Definition Model
**Dimension:** Dimension 7: The Operational Dimension (Runtime & DevOps)
**Owner:** Engineering Leadership, Platform Engineering

## Definition

The end-to-end path an Operational Persona follows to accomplish an Operational Job, traversing operational modules and integration modules. Operational Journeys trace through both native operational modules (admin consoles, deployment dashboards, CLIs) and integration modules to third-party ops tooling (Datadog, PagerDuty, Terraform). Independent from User Journey (Dim 4) — same structural concept, different domain.

The Operational Journey captures the path through the product's modules only. The broader operational workflow (including external tools not integrated via the product, human communication protocols, escalation procedures) is Operating Model territory.

## Purpose

Without Operational Journeys:
- Operational module design is disconnected — each tool is designed independently without considering the end-to-end operational flow
- Operational experience gaps are invisible — you can't identify friction in a journey you haven't mapped
- Cross-module operational workflows are implicit — the SRE "just knows" to go from monitoring to logs to deployment, but this isn't documented

**Channel investment decisions:** Adding a new operational channel (e.g., "Mobile app for on-call alerts") is a PDR-level decision, just as it is for customer-facing channels.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | Text | Descriptive journey name (e.g., "Diagnose and resolve a P1 incident") |
| Accomplishes | Reference (Dim 7) | Which Operational Job(s) this journey accomplishes |
| Followed by | List of References (Dim 7) | Which Operational Persona(s) follow this journey |
| Traverses | List of References (Dim 8) | Which Module(s) are traversed (in order) |
| UX Channel(s) | List of References (Dim 4) | Through which UX Channels the journey is experienced |
| Capabilities Engaged | List of References (Dim 8) | Which Capabilities are exercised during the journey |
| Integration Modules Used | List of References (Dim 6) | Which Integration Modules to third-party ops tools are used |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Accomplishes | Operational Job (Dim 7) | Journey accomplishes one or more Operational Jobs |
| Followed by | Operational Persona (Dim 7) | Operational Personas follow this journey |
| Traverses | Module (Dim 8) | Journey traverses operational modules in sequence |
| Experienced through | UX Channel (Dim 4) | Cross-dimensional: journey steps use specific channels |
| Engages | Capability (Dim 8) | Journey exercises specific capabilities |
| Uses | Integration Module (Dim 6) | Journey steps may use integration modules to third-party ops tools |
| Work Model | Modeling Task (Track 1) | Operational Journeys are documented through Modeling Tasks |

## Example

**"Diagnose and resolve a P1 incident"**
- Accomplishes: "Diagnose and resolve a P1 incident within SLO"
- Followed by: Reliability Operator
- Journey steps:
  1. Alert triggers via PagerDuty Integration Module → Email + Voice/IVR (on-call notification)
  2. Open Monitoring Dashboard (Web + Self-serve) → assess scope and impact
  3. Open Log Aggregator Module (Web + Self-serve) → identify root cause
  4. If rollback needed: open Deployment Console (Web + Self-serve) → initiate rollback
  5. If config change needed: use Ops CLI (CLI + Self-serve) → apply fix
  6. Verify resolution via Monitoring Dashboard
  7. Create post-mortem in Incident Management Module (Web + Self-serve)
- Traverses: PagerDuty Integration Module, Monitoring Module, Log Module, Deployment Module, Ops CLI Module, Incident Module
- Capabilities Engaged: Alert Routing, Metric Visualization, Log Search, Canary Deployment/Rollback, Configuration Management, Post-Mortem Authoring

---
