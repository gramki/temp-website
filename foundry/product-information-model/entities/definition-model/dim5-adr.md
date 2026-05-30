# Architecture Decision Record (ADR)

**Model:** Definition Model
**Dimension:** Technical
**Owner:** Architects, Tech Leads, Engineering Leadership

## Definition

A formal, referenceable record of a significant technical or architectural decision — the Technical counterpart of PDR (Strategy). Where PDR captures product-level decisions ("Go on LATAM market," "Add mobile channel"), ADR captures technical-level decisions ("Use PostgreSQL for transactional data," "Adopt event-driven architecture for inter-service communication," "Split payments monolith into three services"). Follows the Nygard ADR format (Context, Decision, Consequences, Status).

## Purpose

Fills the traceability gap between product decisions (PDRs) and technical implementation. Without ADRs:
- Architectural decisions are tribal knowledge — "why do we use Kafka?" has no referenceable answer
- Technical debt rationale is lost — "why is this service still on Java 11?" has no documented context
- Architecture evolution is implicit — the path from current state to target state has no decision trail
- New engineers lack onboarding context — they see the architecture but not the reasoning

**PDR vs. ADR — three relationship patterns:**
1. **PDR triggers ADR(s):** A product decision requires architectural decisions to implement. "PDR: Go on LATAM" triggers "ADR: Deploy LATAM services in sa-east-1 with LGPD-compliant encryption."
2. **ADR exists independently:** Purely technical decisions that don't require product-level deliberation. "ADR: Migrate from Log4j to SLF4J" or "ADR: Adopt OpenTelemetry for distributed tracing."
3. **ADR constrains PDR:** An architectural reality limits product options. "We can't offer real-time FX because the current batch architecture (ADR-005) doesn't support it; a new PDR is needed to justify the architecture change."

**Dual provenance:** ADRs can be produced by both the Discovery Track (Deliberation-driven — strategic architecture decisions) and the Build Track (implementation-driven — decisions that emerge during build work). Both paths produce the same Technical entity; provenance is tracked through relationships.

## Fields

| Field | Type | Description |
|---|---|---|
| ID | String | Unique identifier (e.g., "ADR-012") |
| Title | String | Descriptive title (e.g., "Adopt event-driven architecture for inter-service payment flow") |
| Status | Enum | `Proposed` / `Accepted` / `Deprecated` / `Superseded` |
| Context | Text | What situation or problem prompted the decision — the forces at play |
| Decision | Text | What was decided — the chosen approach |
| Consequences | Text | What follows from the decision — both positive and negative |
| Quality Attributes Addressed | List | Which quality attributes this decision serves (e.g., reliability, maintainability, performance) |
| Triggered by PDR | Reference (Strategy) | If this ADR was triggered by a product decision (optional) |
| Supersedes | Reference (Technical) | Which ADR(s) this supersedes (optional) |
| Superseded by | Reference (Technical) | Which ADR supersedes this one (optional) |
| Affected Systems | List of References (Technical) | Which Systems are affected by this decision |
| Affected Dependencies | List of References (Technical) | Which Dependencies are affected |
| Decision Date | Date | When the decision was made |
| Decision Makers | List | Who participated (roles or names) |

## Statuses

| Status | Description |
|---|---|
| Proposed | Decision is being considered (evidence and options being evaluated) |
| Accepted | Decision is recorded and the team is committed to it |
| Deprecated | Decision is no longer recommended but not yet replaced |
| Superseded | Replaced by a newer ADR (context changed, better approach found) |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Triggered by | PDR (Strategy) | Product decision that necessitated this architectural decision |
| Affects | System(s) (Technical) | Systems impacted by this decision |
| Affects | Dependency(ies) (Technical) | Dependencies introduced, removed, or changed |
| Affects | Interaction Flow(s) (Technical) | Communication patterns changed by this decision |
| Affects | Component(s) (Technical) | Components introduced, removed, or redesigned |
| Justifies | Architecture Model (Technical) | ADR justifies aspects of the Architecture Model |
| Supersedes | ADR (Technical) | This ADR replaces a previous ADR |
| Produced by | Deliberation (Discovery) | When ADR originates from Discovery Track |
| Downstream | ODR(s) (Operational) | ADR may trigger Operations Decision Records for operational provisioning required to implement the architectural decision |
| Produced by | Build Track work (Build) | When ADR originates from implementation work |

## Examples

**"ADR-012: Adopt event-driven architecture for inter-service payment flow"**
- Status: Accepted
- Context: Synchronous REST calls between 5 services in the payment processing path create cascading failure risk and 3s+ end-to-end latency. Under load, a single slow service blocks all upstream services. LATAM expansion (PDR-023) requires <1s payment processing.
- Decision: Replace synchronous inter-service calls with Kafka events for all non-query interactions. Queries remain synchronous (gRPC for internal, REST for external). Adopt eventual consistency with compensating transactions for failure cases.
- Consequences: (+) Eliminates cascading failures, enables independent scaling, supports future CQRS, reduces end-to-end latency to <800ms. (−) Adds Kafka as critical dependency, increases debugging complexity (distributed tracing required), eventual consistency challenges for real-time queries, team needs Kafka training.
- Quality Attributes: Reliability, Performance, Scalability, Maintainability
- Triggered by: PDR-023 (LATAM expansion)
- Affected Systems: payments-service, fx-service, compliance-service, bank-adapter, settlement-service
- Affected Dependencies: Adds Apache Kafka 3.6 (AWS MSK)

**"ADR-019: Adopt OpenTelemetry for distributed tracing"**
- Status: Accepted
- Context: Event-driven architecture (ADR-012) made request tracing across services difficult. Debugging production incidents requires manual log correlation across 5+ services. Current logging is unstructured and inconsistent.
- Decision: Adopt OpenTelemetry SDK for all services. Structured JSON logs with trace-id/span-id correlation. Export traces to Datadog (via Datadog Observability Integration Module, Ecosystem).
- Consequences: (+) End-to-end request tracing, structured searchable logs, Datadog dashboard integration, standard across all languages. (−) SDK integration effort (~2 days per service), slight performance overhead (measured at <1% in POC), Datadog trace ingestion cost.
- Quality Attributes: Observability, Maintainability
- Triggered by: — (independent technical decision)
- Affected Systems: All services (22)
- Affected Dependencies: Adds OpenTelemetry SDK (library), Datadog trace ingestion (service)

---
