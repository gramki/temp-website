# Operations Decision Record (ODR)

**Model:** Definition Model
**Dimension:** Operational
**Owner:** SRE, Platform Engineering, DevOps Leadership

## Definition

A formal, referenceable record of a significant operational or infrastructure decision — the Operational counterpart of PDR (Strategy) and ADR (Technical). Where PDR captures product-level decisions ("Go on LATAM market"), ADR captures architectural decisions ("Adopt event-driven architecture"), ODR captures operational decisions ("Use AWS MSK for Kafka in 3-AZ deployment with 7-day retention," "Archive transaction data to S3 Glacier after 24 months," "Adopt blue-green deployments for payment-critical services"). Follows the same Nygard-inspired format (Context, Decision, Consequences, Status) as ADR for consistency across the decision record triad.

## Purpose

Fills the traceability gap between architectural decisions (ADRs) and operational reality. Without ODRs:
- Infrastructure decisions are tribal knowledge — "why AWS over GCP?" has no referenceable answer
- Cloud service selection rationale is lost — "why MSK instead of self-managed Kafka?" has no documented context
- Data governance decisions are implicit — retention periods, archival policies, encryption choices have no decision trail
- Deployment strategy rationale is undocumented — "why blue-green?" has no record of the alternatives considered
- DR/BCP decisions lack traceability — RTO/RPO targets have no documented rationale connecting them to business requirements
- Compliance zone decisions are invisible — why PCI scope includes certain environments but not others

**PDR / ADR / ODR — the decision record triad:**
- **PDR (Strategy):** What should the product *do*? Product strategy and intent. Audience: PM, business stakeholders.
- **ADR (Technical):** How should the product be *built*? Architecture and technology. Audience: Architects, engineering leadership.
- **ODR (Operational):** How should the product be *run*? Operations, infrastructure, and data governance. Audience: SRE, Platform Engineering, DevOps.

**ODR relationship patterns (paralleling ADR):**
1. **PDR triggers ODR(s):** A product decision has operational implications. "PDR: Go on LATAM" triggers "ODR: Provision sa-east-1 with LGPD-compliant encryption and dedicated tenancy for Tier-1 banks."
2. **ADR triggers ODR(s):** An architectural decision requires operational provisioning. "ADR: Adopt event-driven architecture" triggers "ODR: Provision AWS MSK 3-AZ with 7-day retention."
3. **ODR exists independently:** Purely operational decisions that don't require architectural or product deliberation. "ODR: Migrate from DataDog to Grafana for cost optimization" or "ODR: Increase financial data archival retention from 5 to 7 years per new regulation."
4. **ODR constrains ADR/PDR:** An operational reality limits architectural or product options. "Our 4-hour RTO (ODR-003) means active-active architecture isn't justified for this tier" or "Data residency constraint (ODR-007) means no cross-region read replicas for PII."

**Dual provenance:** ODRs can be produced by both the Discovery Track (Deliberation-driven — strategic infrastructure decisions like cloud provider selection) and the Run Track (operationally-driven — decisions emerging from operational experience, incidents, or capacity reviews). Both paths produce the same Operational entity; provenance is tracked through relationships.

**ODR scope categories:**

| Category | Examples |
|---|---|
| Cloud Provider & Services | AWS vs. GCP, MSK vs. self-managed Kafka, RDS vs. Aurora, S3 storage class selection |
| Deployment Strategy | Blue-green, canary rollout parameters, immutable infrastructure, rollback policy |
| Tenancy & Isolation | Dedicated vs. shared schema, VPC isolation per compliance zone, tenant resource limits |
| DR / BCP | RTO/RPO targets per service tier, DR site location, failover strategy, replication topology |
| Data Governance | PII classification and encryption, data retention periods, archival strategy, access control model |
| Data Archival | Archive-to-cold-storage timing, retention duration, retrieval SLA for archived data |
| Observability & Tooling | APM selection, alerting platform, log retention, tracing infrastructure |
| Compliance Zones | PCI-DSS scope boundaries, data residency enforcement, SOC 2 audit boundary |
| Capacity & Scaling | Auto-scale thresholds, reserved vs. on-demand ratio, spot instance strategy |
| Cost Optimization | Reserved instance commitments, right-sizing cadence, cost allocation model |

## Fields

| Field | Type | Description |
|---|---|---|
| ID | String | Unique identifier (e.g., "ODR-007") |
| Title | String | Descriptive title (e.g., "Adopt blue-green deployment for payment-critical services") |
| Status | Enum | `Proposed` / `Accepted` / `Deprecated` / `Superseded` |
| Category | Enum | `Cloud Provider & Services` / `Deployment Strategy` / `Tenancy & Isolation` / `DR & BCP` / `Data Governance` / `Data Archival` / `Observability & Tooling` / `Compliance Zone` / `Capacity & Scaling` / `Cost Optimization` |
| Context | Text | What situation or problem prompted the decision — the forces at play |
| Decision | Text | What was decided — the chosen approach |
| Consequences | Text | What follows from the decision — both positive and negative |
| Quality Attributes Addressed | List | Which quality attributes this decision serves (e.g., availability, durability, cost efficiency, compliance) |
| Triggered by PDR | Reference (Strategy) | If this ODR was triggered by a product decision (optional) |
| Triggered by ADR | Reference (Technical) | If this ODR was triggered by an architectural decision (optional) |
| Supersedes | Reference (Operational) | Which ODR(s) this supersedes (optional) |
| Superseded by | Reference (Operational) | Which ODR supersedes this one (optional) |
| Affected Environments | List of References (Operational) | Which Deployment Environments are affected |
| Affected Systems | List of References (Technical) | Which Systems are operationally affected |
| Affected Dependencies | List of References (Technical) | Which Dependencies are affected (e.g., cloud service changes) |
| Decision Date | Date | When the decision was made |
| Decision Makers | List | Who participated (roles or names) |

## Statuses

| Status | Description |
|---|---|
| Proposed | Decision is being considered (options, costs, and trade-offs being evaluated) |
| Accepted | Decision is recorded and the team is committed to it |
| Deprecated | Decision is no longer recommended but not yet replaced |
| Superseded | Replaced by a newer ODR (context changed, better approach found, regulation changed) |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Triggered by | PDR (Strategy) | Product decision with operational implications |
| Triggered by | ADR (Technical) | Architectural decision requiring operational provisioning |
| Affects | Deployment Environment(s) (Operational) | Environments impacted by this decision |
| Affects | Operational Target(s) (Operational) | Targets influenced by this decision (e.g., RTO/RPO from DR decisions) |
| Affects | Operational Constraint(s) (Operational) | Constraints introduced or modified |
| Justifies | Infrastructure Model (Operational) | ODR justifies aspects of the Infrastructure Model |
| Affects | System(s) (Technical) | Systems operationally affected (e.g., deployment strategy applies to specific systems) |
| Affects | Dependency(ies) (Technical) | Dependencies introduced, changed, or removed operationally |
| Constrains | ADR (Technical) | ODR may constrain architectural options |
| Constrains | PDR (Strategy) | ODR may constrain product options |
| Supersedes | ODR (Operational) | This ODR replaces a previous ODR |
| Produced by | Deliberation (Discovery) | When ODR originates from Discovery Track |
| Produced by | Run Track work (Run) | When ODR originates from operational experience |
| Produced by | Run Epic / Run Deliberation (Run) | Run Deliberations within Run Epics produce ODRs for operational engineering decisions (probe strategy, automation approach, monitoring architecture) |

## Examples

**"ODR-003: Adopt blue-green deployment for payment-critical services"**
- Status: Accepted
- Category: Deployment Strategy
- Context: Rolling deployments for payments-service caused 3 incidents in Q4 2025 — partial rollouts left the service in an inconsistent state when new code accessed old database schema. Rollback from a partial rolling deployment took 45 minutes (well beyond 30-min MTTR target). Canary deployments were considered but rejected because payment processing is stateful and partial routing causes transaction inconsistencies.
- Decision: Adopt blue-green deployment for all payment-critical services (payments-service, fx-service, bank-adapter, settlement-service). Full environment swap with automated smoke tests before traffic switch. Non-critical services remain on rolling deployments.
- Consequences: (+) Zero-downtime deployments, instant rollback (< 2 min), consistent state during deployment, reduced deployment-related incidents. (−) Doubles compute cost during deployment window (~15 min per deployment), requires automated smoke test suite per service, increases deployment pipeline complexity.
- Quality Attributes: Availability, Reliability, Recovery
- Triggered by: — (independent operational decision, driven by incident pattern)
- Affected Environments: Production US-East, Production LATAM, Staging EU-West
- Affected Systems: payments-service, fx-service, bank-adapter, settlement-service

**"ODR-007: LATAM data residency — LGPD compliance in sa-east-1"**
- Status: Accepted
- Category: Compliance Zone
- Context: LATAM expansion (PDR-023) requires serving Brazilian financial institutions. LGPD (Lei Geral de Proteção de Dados) mandates that personal data of Brazilian individuals must be stored and processed within Brazilian territory. The product currently stores all data in us-east-1.
- Decision: All PII and transaction data for LATAM customers must be stored and processed exclusively in sa-east-1. Non-PII analytics data may be replicated to us-east-1 for global dashboards. Encryption at rest (AES-256) and in transit (TLS 1.3) mandated for all LATAM environments. Quarterly LGPD compliance audit.
- Consequences: (+) Legal compliance for Brazilian market, enables Tier-1 bank customer acquisition, establishes compliance zone pattern reusable for GDPR (eu-west-1). (−) No cross-region read replicas for PII (latency for global admin views), dedicated LATAM infrastructure cost, operational complexity of multi-region compliance zones.
- Quality Attributes: Compliance, Security, Durability
- Triggered by: PDR-023 (LATAM expansion)
- Affected Environments: Production LATAM (sa-east-1)
- Affected Systems: All services handling PII — payments-service, compliance-service, onboarding-service

**"ODR-011: Transaction data archival to S3 Glacier after 24 months"**
- Status: Accepted
- Category: Data Archival
- Context: Transaction data in PostgreSQL grows at ~50GB/month. After 24 months, data is rarely accessed (< 0.1% of queries touch records older than 18 months) but must be retained for 7 years per financial regulatory requirements. Keeping all data in hot storage increases backup time, query performance degradation, and storage cost.
- Decision: Archive transaction data older than 24 months to S3 Glacier Deep Archive. Maintain index metadata in PostgreSQL for lookup. Retrieval SLA: 12 hours for archived records (acceptable for audit and regulatory queries). Automated archival pipeline runs monthly.
- Consequences: (+) ~60% reduction in PostgreSQL storage after 2-year ramp, faster backups, improved query performance on active data, regulatory compliance maintained. (−) 12-hour retrieval latency for archived records, archival pipeline maintenance, need to handle edge cases (e.g., dispute resolution requiring old transaction data).
- Quality Attributes: Cost Efficiency, Durability, Compliance
- Triggered by: — (independent operational decision, driven by cost and performance trends)
- Affected Environments: Production US-East, Production LATAM
- Affected Systems: payments-service (data source), analytics-service (historical queries)
- Affected Dependencies: Adds AWS S3 Glacier Deep Archive

**"ODR-014: Adopt AWS MSK over self-managed Kafka"**
- Status: Accepted
- Category: Cloud Provider & Services
- Context: ADR-012 introduced Kafka as a critical dependency for event-driven architecture. Two options: self-managed Kafka on EC2 or AWS MSK (managed Kafka). Self-managed provides full control but requires dedicated Kafka operations expertise (cluster management, ZooKeeper, broker rebalancing, security patching). Current team has 2 engineers with Kafka operations experience.
- Decision: Adopt AWS MSK for all Kafka workloads. 3-AZ deployment for production, single-AZ for staging. 7-day retention for production, 3-day for staging. Encryption in transit and at rest enabled. MSK Connect for external integrations.
- Consequences: (+) No Kafka operations burden (patching, broker management, ZooKeeper), AWS-managed availability (99.9% SLA), integrated CloudWatch monitoring, simplified security (IAM + TLS). (−) Higher per-hour cost than self-managed (~30% premium), limited Kafka version flexibility (AWS release lag), vendor lock-in to AWS for messaging layer.
- Quality Attributes: Availability, Maintainability, Cost Efficiency
- Triggered by: ADR-012 (event-driven architecture adoption)
- Affected Environments: Production US-East, Production LATAM, Staging EU-West
- Affected Dependencies: Apache Kafka 3.6 → AWS MSK (managed)

---
