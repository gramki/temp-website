# Dependency

**Model:** Definition Model
**Dimension:** Dimension 5: The Technical & Architectural Dimension (Engineering)
**Owner:** Tech Leads, Engineering Leadership, Platform Engineering

## Definition

An external system, service, library, or infrastructure resource the product depends on but does not own. Dependencies represent the product's external reliance — the systems and resources that must be available for the product to function. Two subtypes: **Third-Party Service** (external APIs, SaaS platforms, partner systems) and **Infrastructure Resource** (databases, message brokers, cloud services, caches).

## Purpose

Makes the product's external dependencies explicit and manageable. Without Dependencies:
- Risk assessment is implicit — "what happens if this provider goes down?" has no entity to anchor to
- Cost modeling is incomplete — third-party service costs and infrastructure resource costs are invisible in the Definition Model
- Architectural evaluation lacks dependency analysis — over-reliance on a single provider is untracked
- Operational planning (Dim 7) lacks dependency context — Operational Constraints may flow from Dependency limitations
- Vendor lock-in risk is undocumented — no visibility into which dependencies have alternatives

**Dependency vs. Integration Module (Dim 6):** Integration Module is a product capability — a pre-built bridge the product ships to connect with external systems. Dependency is the external system itself that the product relies on. An Integration Module (Dim 6) "SAP ERP Connector" may depend on (Dim 5) "SAP BAPI API" as a Dependency. The Integration Module is what the product provides; the Dependency is what the product consumes.

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Dependency name (e.g., "CurrencyCloud FX API," "PostgreSQL 15," "AWS SQS") |
| Type | Enum | `Third-Party Service` / `Infrastructure Resource` |
| Subtype | String | More specific classification (e.g., "FX Rate Provider," "Relational Database," "Message Queue," "Object Storage") |
| Provider / Vendor | String | Who provides this dependency (e.g., "CurrencyCloud Ltd," "AWS," "Confluent") |
| Criticality | Enum | `Critical` (product cannot function without it) / `Important` (degraded operation possible) / `Convenience` (alternatives exist, minimal impact) |
| Failure Impact | Text | What happens when this dependency is unavailable |
| Alternative / Fallback | Text | Is there a fallback? Migration path? Multi-provider strategy? |
| Cost Model | Text | How this dependency is priced (per-call, per-GB, reserved, etc.) |
| Provider SLA | String | The provider's availability/performance commitment |
| Used by | List of References (Dim 5) | Which System(s) depend on this |

## Statuses

| Status | Description |
|---|---|
| Active | Dependency is in use in production |
| Evaluating | Dependency is being evaluated (POC, spike) but not yet committed |
| Migrating | Dependency is being replaced (migration to alternative in progress) |
| Deprecated | Dependency is scheduled for removal (alternative identified, timeline set) |
| Retired | Dependency has been fully removed |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Used by | System(s) (Dim 5) | Systems depend on this external resource |
| Used in | Interaction Flow(s) (Dim 5) | Interaction Flows may involve external Dependencies |
| May impose | Operational Constraint(s) (Dim 7) | Dependency limitations may become operational constraints |
| Cost for | Infrastructure Model (Dim 7) | Dependency costs feed the Infrastructure Model's Cost Model |
| Decisions | ADR(s) (Dim 5) | Dependency selection decisions are recorded as ADRs |
| Distinct from | Integration Module (Dim 6) | Integration Module is what the product provides; Dependency is what it consumes |

## Examples

| Dependency | Type | Criticality | Provider | Failure Impact | Alternative | Status |
|---|---|---|---|---|---|---|
| CurrencyCloud FX API | Third-Party Service | Critical | CurrencyCloud Ltd | All FX operations blocked; payments requiring FX conversion queued | Failover to secondary provider (XE) in ADR-015 | Active |
| OFAC Screening Service | Third-Party Service | Critical | Dow Jones | Compliance screening blocked; payments held in Pending_Screening | Manual screening fallback (Compliance team) | Active |
| PostgreSQL 15 | Infrastructure Resource | Critical | AWS RDS | Transactional data unavailable; all write operations fail | Aurora PostgreSQL (migration path in ADR-008) | Active |
| Apache Kafka 3.6 | Infrastructure Resource | Critical | AWS MSK | Inter-service events blocked; eventual consistency stalls | — (no fallback; architecture depends on it) | Active |
| Redis 7 | Infrastructure Resource | Important | AWS ElastiCache | FX rate cache unavailable; fallback to direct provider calls (higher latency) | Direct provider calls (degraded performance) | Active |
| AWS S3 | Infrastructure Resource | Important | AWS | File storage unavailable; batch report generation fails | — (AWS-native, no alternative in current architecture) | Active |
| Twilio SMS API | Third-Party Service | Convenience | Twilio | SMS notifications fail; email fallback available | Email notifications (automatic fallback) | Active |

---
