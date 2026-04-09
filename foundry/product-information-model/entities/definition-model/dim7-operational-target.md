# Operational Target (SLO)

**Model:** Definition Model
**Dimension:** Dimension 7: The Operational Dimension (Runtime & DevOps)
**Owner:** Engineering Leadership, SRE/Platform Engineering

## Definition

An infrastructure-level objective that backs Service Commitments (Dim 3) and API Operation SLOs (Dim 6). The operational "how we deliver on promises." Each Operational Target carries **Achievement Levers** — categorized as Product (build self-healing, improve error handling, add circuit breakers) or Operational (improve procedures, add redundancy, scale infrastructure) — connecting Dim 7 into the Initiative/Lever framework. This parallels Win Outcome (Dim 2), which carries Achievement Levers from the Business Model's Lever Portfolio.

SLIs (Service Level Indicators) — the specific metrics that feed into the SLO — are fields on the Operational Target, not separate entities.

## Purpose

Analogous to Win Outcome (Dim 2), which captures what commercial success looks like. Operational Target captures what operational success looks like — per quality taxonomy type, per module or environment. Without Operational Targets:
- Service Commitments (Dim 3) have no infrastructure-level backing — "99.9% uptime" is a customer promise with no corresponding operational objective
- API Operation SLOs (Dim 6) float without infrastructure targets — "p99 < 500ms" is declared but not operationally committed
- Operational investment lacks a lever framework — improvements happen reactively rather than through strategic Initiative planning

**Three-layer SLO structure:** Customer-facing SLA (Dim 3 Service Commitment) → API Operation SLO (Dim 6) → Infrastructure Operational Target (Dim 7). Each layer is progressively more specific: the SLA promises "99.9% uptime" to the customer; the API SLO commits "99.95% availability per operation"; the Operational Target sets "99.99% compute availability per environment."

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Target name (e.g., "payments-service availability — Production US-East") |
| Type | Enum | Quality taxonomy type: `Availability` / `Latency` / `Throughput` / `Durability` / `Recovery` / `Cost` / `Security` |
| Target Value | String | Quantified target (e.g., "99.99%," "< 200ms p99," "< $0.50 per 1K transactions") |
| Threshold | String | Warning/breach threshold (e.g., "99.95%," "< 500ms p99") |
| SLI Definition | Text | What is measured and where (e.g., "percentage of non-5xx responses measured at load balancer") |
| Measurement Cadence | String | How often measured (e.g., "continuous," "hourly aggregation," "monthly") |
| Scope | Enum | `Product-level` / `Environment-level` / `Module-level` |
| Scoped Module | Reference (Dim 8) | Which module this target applies to (if module-level) |
| Scoped Environment | Reference (Dim 7) | Which environment this target applies to |
| Achievement Levers | List (Lever + Primary/Secondary) | What kinds of effort can improve this target: **Product** (build capabilities) or **Operational** (improve procedures/infrastructure). Forces the question: "Is this primarily a product engineering problem or an operational problem?" |
| Responsible Persona(s) | List of References (Dim 7) | Which Operational Persona(s) own this target |

## Statuses

| Status | Description |
|---|---|
| Draft | Target is being defined (aspirational; not yet achievable) |
| Active | Target is the current operational objective — actively measured and reported |
| At Risk | Target is being met but trending toward breach |
| Breached | Target has been breached — remediation required |
| Revised | Target has been updated based on new evidence or capability changes |
| Retired | Target is no longer relevant |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Backs | Service Commitment (Dim 3) | Operational Targets deliver the customer-facing SLA |
| Delivers | API Operation SLOs (Dim 6) | Operational Targets back per-operation performance commitments |
| Scoped to | Module (Dim 8) + Deployment Environment (Dim 7) | Target applies to a specific module in a specific environment |
| Monitored by | System Monitoring (Track 3) | Runtime performance tracked against target |
| Consumed by | Incident (Track 3, artifact) | Incidents consume error budget against Operational Targets — every incident erodes the margin toward breach |
| Responsibility of | Operational Persona (Dim 7) | Operational Personas own specific targets |
| Undermined by | Operational Pain (Dim 7) | Operational Pains make targets harder to achieve |
| Referenced by | Operational Readiness (Dim 7) | Readiness criteria reference target compliance |
| Referenced by | Objective / Initiative (Dim 1) | Initiatives may target Operational Target improvement |
| Measured by | Operational Job (Dim 7) | Jobs are measured against their relevant targets |
| Decisions | ODR(s) (Dim 7) | Operational decisions influencing targets (e.g., DR decisions setting RTO/RPO) are recorded as ODRs |

## Examples

| Target | Type | Scope | Value | Threshold | SLI | Levers |
|---|---|---|---|---|---|---|
| "payments-service availability — Prod US-East" | Availability | Module-level | 99.99% | 99.95% | % non-5xx responses at load balancer, 5-min rolling window | Product (primary — circuit breakers, graceful degradation), Operational (secondary — multi-AZ redundancy) |
| "Create Payment latency — Prod US-East" | Latency | Module-level | p99 < 500ms | p99 < 800ms | Request duration at API gateway, per-request | Product (primary — query optimization, caching), Operational (secondary — right-size compute) |
| "Production US-East compute availability" | Availability | Environment-level | 99.99% | 99.95% | Node health checks, 1-min intervals | Operational (primary — auto-healing, multi-AZ), Product (secondary — health check endpoints) |
| "Infrastructure cost per 1K transactions" | Cost | Product-level | < $0.50 | < $0.75 | Monthly compute + data transfer cost / transaction count | Operational (primary — right-sizing, reserved instances), Product (secondary — code efficiency) |
| "SEV-1 incident MTTR" | Recovery | Product-level | < 30 min | < 60 min | Incident open-to-resolved duration for SEV-1 | Product (primary — observability tooling, automated diagnostics), Operational (secondary — incident response procedures) |
| "Vulnerability remediation time" | Security | Product-level | < 72 hours (critical) | < 1 week | Time from CVE disclosure to patched deployment | Product (primary — dependency management, automated scanning), Operational (secondary — expedited deployment process) |

---
