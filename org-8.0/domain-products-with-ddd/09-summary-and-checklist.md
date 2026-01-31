# Summary and Checklist

This section summarizes the guide and provides an implementation checklist and a quick-reference table. Use it to verify that the domain, application, infrastructure, and deployment align with the approach described in the preceding sections.

> **For your next assignment.** Before you submit code, run through the **Implementation checklist** below. If you're unsure where a class or method belongs, use the **Quick reference** table (DDD concept → Spring Boot artifact). For "where does this logic go?" use [02 DDD concepts](02-ddd-concepts.md) and [06 Anemic domain](06-anemic-domain.md). For "how do I test this?" use [08 Testability and testing patterns](08-testability-and-testing-patterns.md).

---

## Implementation checklist

### Domain

- [ ] Domain package contains only domain types: entities, value objects, aggregate roots, domain events, repository **interface**, domain services (plain classes or interfaces).
- [ ] No Spring annotations in the domain package.
- [ ] Aggregates enforce invariants; behavior (e.g. `addLineItem`) is on the aggregate root or entity; no setters for invariant-breaking state.
- [ ] Domain services do not depend on repositories; they receive domain objects (or data) from the caller.
- [ ] Repository interface is in the domain and uses only domain types (e.g. `Order`, `OrderId`).
- [ ] Ubiquitous language is used consistently in type and method names.

### Application

- [ ] Application package contains application services (use-case orchestration), commands/DTOs.
- [ ] Application services are thin: load (via repository), call domain (aggregate or domain service), save (via repository), publish events. No business logic.
- [ ] Transaction boundary is at the application service (`@Transactional` on the use-case method).
- [ ] Application services depend only on domain (repository interface, domain types, domain services) and infrastructure ports (e.g. event publisher).

### Infrastructure

- [ ] Repository implementation is in infrastructure; it implements the domain repository interface and uses JDBC (e.g. `JdbcTemplate`).
- [ ] Persistence model (e.g. `OrderRow`, `OrderLineRow`) is in infrastructure when domain and table shape diverge; mapping is domain aggregate ↔ persistence model ↔ database.
- [ ] Aggregate reconstitution uses a domain-provided factory or reconstitute method; repository does not set aggregate state from outside.
- [ ] REST controllers (or other entry points) delegate to application services; they do not contain business logic.

### Deployment

- [ ] One application (one deployment unit, e.g. one Kubernetes Deployment) owns one bounded context.
- [ ] Context map documents bounded contexts, ownership, consistency boundaries, and deployment units.
- [ ] New deployment units are justified by the context map (new bounded context), not by “new Domain Service” or “new use case.”
- [ ] Cross-application consistency uses events, sagas, or outbox—not distributed transactions.

---

## Quick reference: DDD concept → Spring Boot artifact (no ORM, one app per domain)

| DDD concept | Spring Boot artifact |
|-------------|----------------------|
| **Bounded context** | The whole application (one domain/subdomain per deployable). |
| **Entity / aggregate root** | Plain POJO in **domain/**. No JPA. |
| **Value object** | Immutable POJO or `record` in **domain/**. |
| **Repository (interface)** | Interface in **domain/**. Methods use domain types only. |
| **Repository (implementation)** | Class in **infrastructure.persistence**; implements domain interface; uses **JdbcTemplate** or raw JDBC; optional persistence model (domain ↔ persistence model ↔ DB). |
| **Domain service** | Class in **domain/**. No repository references. Optional: interface in domain, implementation in application/infrastructure if DI needed. |
| **Application service** | Class in **application/** with `@Service`. Uses repository interface, domain types, domain services. `@Transactional` for use-case boundary. |
| **Domain event** | POJO in **domain/**. Published by application service (in-process: `ApplicationEventPublisher`; cross-process: outbound port in infrastructure). |
| **Persistence model** | Optional. Types in **infrastructure.persistence** that mirror DB; repository impl maps domain ↔ persistence model ↔ JDBC. |

---

## References

- **Eric Evans,** *Domain-Driven Design: Tackling Complexity in the Heart of Software.* Addison-Wesley, 2003. The foundational reference for DDD concepts, bounded context, ubiquitous language, and tactical patterns.
- **Vaughn Vernon,** *Implementing Domain-Driven Design.* Addison-Wesley, 2013. Practical treatment of aggregates, repositories, domain services, and application services.
- **Product Line Engineering:** For organizational context on product lines, domain engineering, and team structure, see the [Product Line Engineering](../product-line-engineering/README.md) documentation.

---

## Summary

- **Domain** and **ubiquitous language** define the “what”; **bounded contexts** and the **context map** define boundaries and integrations.
- **Use cases** map to **application services** and scenarios; **value streams** span **bounded contexts** and inform the context map.
- **Domain Service** = domain logic, no CRUD, no repository references. **Application Service** = orchestration, uses repositories, owns transaction boundary. **Repository** = persistence of aggregates.
- **“Service” in DDD** is a design role, not a process. One deployment (e.g. Kubernetes Deployment) can contain many Domain Services and Application Services in one process; do not confuse DDD Domain Service with microservice.
- **Product requirements** map to DDD by: value streams → context map and bounded contexts; use cases → application services and domain model (entities, aggregates, domain services, events); persistence → repositories used by application services.
- **Rich domain:** Behaviour and invariants live in aggregates and entities; domain services only when the operation doesn’t fit one entity. Avoid anemic domain.
- **No ORM:** Persistence via JDBC and optional persistence model in infrastructure; domain stays independent of schema.
- **One app per domain:** One bounded context per Spring Boot application; context map is the source of truth for ownership, consistency, and deployment.
