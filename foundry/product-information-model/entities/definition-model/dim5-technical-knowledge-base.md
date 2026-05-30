# Technical Knowledge Base

**Model:** Definition Model
**Dimension:** Technical
**Owner:** Tech Leads, Engineering Leadership

## Definition

A per-System assessment of whether the system's technical knowledge is current and complete — covering documentation, guides, and playbooks that enable Run and Win teams to understand and operate the system. Parallels Operational Readiness (Operational): a single instance per System with knowledge-type dimensions and coverage status. The actual documents are Work Model artifacts; this entity tracks "does the knowledge exist and is it current?"

## Purpose

Makes documentation gaps visible in the Definition Model rather than leaving them as implicit Work Model concerns. Without Technical Knowledge Base:
- "Production-ready" is assessed without documentation — a System can pass Operational Readiness (Operational) checks but have no runbook for the Run Team
- Win Teams lack technical context — pre-sales and customer success have no structured way to know which Systems have technical guides and which don't
- Documentation currency is untracked — an integration guide written 18 months ago may be dangerously stale
- Documentation investment decisions have no entity to anchor to — "we need to write runbooks" has no structured gap analysis

**Technical Knowledge Base vs. Operational Readiness (Operational):** Both are per-System assessments with quality dimensions. Operational Readiness asks "is this System ready for production in this environment?" (observability, security, performance, DR criteria). Technical Knowledge Base asks "is this System's knowledge documented and current?" (architecture docs, runbooks, guides). They are complementary — a System can be operationally ready (metrics, alerts, failover all configured) but poorly documented (no runbook, stale integration guide). Both gaps matter.

## Fields

| Field | Type | Description |
|---|---|---|
| System | Reference (Technical) | Which System this assessment covers |
| Overall Status | Enum | `Not Assessed` / `Gaps Identified` / `Partially Documented` / `Fully Documented` |
| Architecture Documentation | Text + Status | System design, boundaries, data model, event contracts, dependencies. Status: Missing / Stale / Current |
| Operational Runbook | Text + Status | Deployment procedures, failover steps, scaling instructions, common troubleshooting. Status: Missing / Stale / Current |
| Release Notes | Text + Status | What changed, migration instructions, breaking changes. Status: Missing / Stale / Current |
| Integration Guide | Text + Status | How other Systems or external consumers interact with this System. Status: Missing / Stale / Current |
| Win Technical Guide | Text + Status | Technical overview for pre-sales, CS, and support teams — what the System does, how it works at a high level, common questions. Status: Missing / Stale / Current |
| Troubleshooting Playbook | Text + Status | Common failure modes, diagnostic steps, resolution procedures. Status: Missing / Stale / Current |
| Last Assessed | Date | When this knowledge base was last evaluated |
| Gaps | List | Specific gaps with severity and remediation plan |

## Statuses

| Status | Description |
|---|---|
| Not Assessed | System's documentation has not been evaluated |
| Gaps Identified | Assessment completed; gaps found in one or more knowledge types |
| Partially Documented | Most knowledge types exist; some gaps or stale content |
| Fully Documented | All knowledge types are current and complete |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Scoped to | System (Technical) | Knowledge Base is assessed per-System |
| Assessed by | Build Track / Run Track activities | Documentation creation and maintenance is work |
| Complements | Operational Readiness (Operational) | Technical knowledge complements operational readiness |
| Enables | Win Track (Win) | Win Technical Guide enables pre-sales and CS work |
| Enables | Run Track (Run) | Operational Runbook and Troubleshooting Playbook enable Run work |

## Example

**"payments-service Technical Knowledge Base"**
- System: payments-service
- Overall Status: **Partially Documented**
- Architecture Documentation: **Current** (2026-01) — covers service boundaries, data model (PostgreSQL schema), Kafka event contracts, dependency diagram, component-level architecture (Payment State Machine, Bank File Generator)
- Operational Runbook: **Gaps Identified** — deployment runbook exists and is current; failover runbook missing; scaling runbook exists but doesn't cover LATAM region
- Release Notes: **Current** — auto-generated from System Version build pipeline; includes migration notes
- Integration Guide: **Stale** (2025-06) — doesn't cover new Kafka event contracts introduced in ADR-012; REST API section current; missing gRPC section for fx-service interaction
- Win Technical Guide: **Current** (2026-01) — technical overview for pre-sales covering payment flow, compliance screening, settlement process; includes architecture diagram and common customer questions
- Troubleshooting Playbook: **Missing** — no documented troubleshooting procedures; incident resolution relies on tribal knowledge
- Last Assessed: 2026-02-01
- Gaps:
  1. Failover runbook — severity: high, remediation: Q2 2026 (Platform Operator initiative)
  2. Troubleshooting playbook — severity: medium, remediation: Sprint 16
  3. Integration guide update (Kafka events) — severity: medium, remediation: Sprint 17

---
