# Operational Readiness

**Model:** Definition Model
**Dimension:** Dimension 7: The Operational Dimension (Runtime & DevOps)
**Owner:** Engineering Leadership, Platform Engineering, SRE

## Definition

A per-System assessment of whether a specific System (Dim 5) meets the operational acceptance criteria for a specific Deployment Environment. The criteria span the Operational Quality Taxonomy: observability, security, performance, operability, DR, and compliance. Operational Readiness captures the criteria definition (what "production-ready" means) and the readiness state (does this System meet those criteria here?).

Distinct from Evolve Track (Track 5), which assesses process effectiveness ("are our entity definitions and DoD criteria working?"). Operational Readiness assesses System readiness ("is this System ready for production in this environment?"). The criteria definition is a Definition Model concern; the assessment work is Run Track (Track 3) activity.

> **Why per-System, not per-Module?** The Run Track operates Systems — SREs deploy `payments-service`, monitor `fx-service` metrics, write runbooks for `bank-adapter` failover. Observability, security scans, performance benchmarks, DR procedures — all are naturally System-scoped. The System is the operational unit, just as it is the deployment unit (System Version) and the build unit (CI/CD pipeline). Module-level readiness ("is the Payments capability ready for production in LATAM?") is a derived view that aggregates readiness across all Systems implementing that Module. If any constituent System has gaps, the Module has gaps.
>
> **Module-level operational concern remains legitimate.** A Module Version is a composite system — not merely a collection of System Versions, but a system in its own right with emergent operational properties (end-to-end latency across the Module's Systems, integrated failure modes, cross-system data consistency) that do not exist at the individual System level. SREs legitimately reason about "the Payments Module" because it represents an operable capability with its own health profile. Module-level readiness is derived from constituent System readiness, but the Module itself has emergent concerns (e.g., "end-to-end payout latency exceeds SLO even though each System meets its individual target") that System-level assessment alone cannot surface. The primary operational vocabulary and assessment granularity remains System-level; Module-level readiness aggregates and extends it. See DR-026.

## Purpose

Captures the operational acceptance criteria that every System must meet before being considered production-ready in a given environment. Without Operational Readiness:
- "Production-ready" is undefined — different teams have different implicit standards
- Systems go live with missing observability, incomplete runbooks, or untested DR procedures
- There is no structured entity to assess a System's operational maturity across quality dimensions
- The gap between "code complete" (Build Track) and "operationally ready" (Run Track) is invisible

**Per-System × per-Environment scope:** A System may be Fully Ready in Production US-East (well-established, extensively monitored) but Gaps Identified in Production LATAM (new region, runbooks not yet localized, load testing incomplete).

**Module-level aggregation:** "Is the Payments Module ready for production in LATAM?" is answered by aggregating Operational Readiness across all Systems implementing the Payments Module (e.g., payments-service, payment-gateway) in Production LATAM. This is a derived view, not a separate entity instance.

## Fields

| Field | Type | Description |
|---|---|---|
| System | Reference (Dim 5) | Which System is being assessed |
| Deployment Environment | Reference (Dim 7) | Which environment this assessment applies to |
| Overall Status | Enum | `Not Assessed` / `Gaps Identified` / `Conditionally Ready` / `Fully Ready` |
| Observability | Text + Status | Logs, metrics, traces, SLIs defined? Readiness status for this dimension. |
| Security | Text + Status | Encryption, access control, vulnerability scanning, key management? |
| Performance | Text + Status | Benchmarks, load testing, scaling behavior validated? |
| Operability | Text + Status | Alerts configured, runbooks written, admin controls available, levers documented? |
| DR | Text + Status | Backup, restore, failover procedures defined and tested? |
| Compliance | Text + Status | Audit trails, data handling, regulatory requirements met? |
| Last Assessed | Date | When this readiness was last evaluated |
| Gaps | List | Specific gaps identified, with severity and remediation plan |

## Statuses

| Status | Description |
|---|---|
| Not Assessed | System has not yet been evaluated for this environment |
| Gaps Identified | Assessment completed; gaps found in one or more quality dimensions |
| Conditionally Ready | Most criteria met; known gaps accepted with documented risk and remediation timeline |
| Fully Ready | All criteria met across all quality dimensions for this environment |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Scoped to | System (Dim 5) | Readiness is assessed per-System |
| Scoped to | Deployment Environment (Dim 7) | Readiness is assessed per-environment |
| Aggregates to | Module (Dim 8) | Module-level readiness is derived from constituent Systems' readiness |
| References | Operational Target (Dim 7) | Readiness criteria reference target compliance (e.g., "SLIs defined for all active Operational Targets") |
| Assessed by | Run Track activities (Track 3) | Readiness assessment is Run Track operational work |
| Triggers | Run Epic (Track 3) | Readiness gaps trigger Run Epics for operational engineering work (e.g., missing probes, insufficient automation) |
| Context from | Infrastructure Model (Dim 7) | Infrastructure Model determines which criteria are relevant |
| Informs | Deployment (Track 3) | Deployment decisions consider readiness status |
| Fed by | System Version (Track 2) | System Version quality gate results (test coverage, security scan, performance benchmarks) feed Operational Readiness assessment |

## Example

**"payments-service in Production US-East"**
- System: payments-service (Dim 5)
- Environment: Production US-East
- Overall Status: **Conditionally Ready**
- Observability: **Fully Ready** — structured JSON logs, Prometheus metrics (15 golden signals), distributed traces via OpenTelemetry, SLIs defined for all 4 Operational Targets
- Security: **Conditionally Ready** — encryption at rest (AES-256), mTLS in transit, RBAC configured. Gap: automated key rotation not yet implemented (manual rotation, 8hr/week — see Operational Pain)
- Performance: **Fully Ready** — load tested to 3x peak (30K TPS), auto-scale verified, baseline benchmarks established
- Operability: **Gaps Identified** — alerts configured (but 40% false positive rate — see Operational Pain), runbooks complete for deployment and rollback, incomplete for multi-AZ failover scenario
- DR: **Fully Ready** — automated backup every 15 min, point-in-time recovery tested, failover to DR US-West tested quarterly, RTO validated at 2 hours (within 4-hour target)
- Compliance: **Fully Ready** — PCI-DSS audit trail complete, data classification tags applied, SOC 2 controls verified
- Last Assessed: 2026-02-01
- Gaps: (1) Automated key rotation — Security — severity: medium, remediation: Q2 2026 Initiative. (2) Alert false positive rate — Observability — severity: high, remediation: in progress, alert tuning Sprint 15.

**Module-level aggregation example:** "Is the Payments Module ready for Production US-East?" → Check readiness of all Systems implementing the Payments Module: payments-service (Conditionally Ready), payment-gateway (Fully Ready). Aggregate: **Conditionally Ready** (constrained by payments-service gaps).

---
