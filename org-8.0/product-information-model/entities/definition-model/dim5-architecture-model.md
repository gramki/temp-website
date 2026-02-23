# Architecture Model

**Model:** Definition Model
**Dimension:** Dimension 5: The Technical & Architectural Dimension (Engineering)
**Owner:** Chief Architect, Engineering Leadership

## Definition

The macro-level architectural strategy — how the product is designed and constructed. The Architecture Model is the structural root of Dimension 5: all other Dim 5 entities exist within its frame. Parallel to Business Model (Dim 2) — "how we make money" — and Infrastructure Model (Dim 7) — "how we run it." The Architecture Model captures "how we build it."

## Purpose

Anchors the Technical & Architectural dimension by establishing the product's architectural identity. Like Business Model and Infrastructure Model, the Architecture Model is a lightweight, rarely-changing entity — it changes at the scale of years (e.g., migrating from monolith to microservices, adopting event sourcing), not quarters. Without Architecture Model:
- Systems exist without strategic context — no explanation of why the product is decomposed this way
- Technology choices are implicit — no explicit technology strategy or quality attribute priorities
- Architectural evolution has no documented direction — "where we are" and "where we're heading" are tribal knowledge
- ADRs lack a frame — individual decisions don't compose into a coherent strategy

## Fields

| Field | Type | Description |
|---|---|---|
| Name | String | Descriptive name (e.g., "Event-driven microservices on AWS") |
| Architectural Style | Enum / List | `Microservices` / `Modular monolith` / `Event-driven` / `Serverless` / `Hybrid` / `Layered` |
| Key Principles | List | Guiding architectural principles (e.g., DDD bounded contexts, API-first, event sourcing, CQRS, separation of concerns) |
| Quality Attribute Priorities | Ordered List | Non-functional quality attributes in priority order (e.g., maintainability > testability > extensibility > performance) |
| Technology Strategy | Text | Language portfolio, framework standards, cloud-native vs. portable, build vs. buy philosophy |
| Architectural Evolution | Text | Current state → target state — the architectural roadmap (e.g., "migrating from shared database to database-per-service: 3 of 22 services complete") |

## Statuses

_Not applicable — the Architecture Model is a structural descriptor that changes extremely rarely. When it does change, it is a company-level architectural event warranting its own ADR (and likely a PDR)._

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Context for | System (Dim 5) | Architecture Model frames how Systems are designed and decomposed |
| Context for | Component (Dim 5) | Architecture Model's principles guide Component design |
| Context for | Interaction Flow (Dim 5) | Architecture Model's style determines available Interaction Flow types |
| Context for | Dependency (Dim 5) | Architecture Model's technology strategy guides dependency selection |
| Justified by | ADR(s) (Dim 5) | Major architectural choices are recorded as ADRs |
| Complementary | Infrastructure Model (Dim 7) | "How we build it" (Dim 5) complements "how we run it" (Dim 7) |
| Work Model | Modeling Task (Track 1) | Architecture Model is evolved through Modeling Tasks |

## Example

**"Event-driven microservices on AWS"**
- Architectural Style: Microservices + Event-driven (hybrid — synchronous REST for queries, asynchronous Kafka events for commands and domain events)
- Key Principles: DDD bounded contexts (one service per bounded context), API-first (all inter-service communication through defined contracts), event sourcing for payment state (audit trail), CQRS for read-heavy query services, anti-corruption layers at domain boundaries
- Quality Attribute Priorities: Reliability > Maintainability > Testability > Extensibility > Performance
- Technology Strategy: Java 21 / Spring Boot 3.x for transactional services, Python 3.12 for analytics and batch processing, PostgreSQL for transactional data, ClickHouse for analytics, Kafka for inter-service events. Cloud-native (AWS) with portability layer for database access (no direct AWS SDK calls in domain logic).
- Architectural Evolution: Migrating from shared PostgreSQL database to database-per-service (3 of 22 services complete — payments, fx, settlement). Target: all transactional services own their data by Q4 2026. Analytics services already on ClickHouse.

---
