# Risks and Mitigations

This section describes risks that arise when implementing DDD with Spring Boot (no ORM, one app per domain) and gives mitigations and guidelines. Concepts are as defined in [DDD concepts](02-ddd-concepts.md) and implemented as in [Spring Boot mapping](05-spring-boot-mapping.md).

---

## Domain depending on Spring

**Risk:** Putting Spring annotations (e.g. `@Component`, `@Autowired`) on domain types ties the domain to the framework. The domain is no longer framework-agnostic; tests and reuse suffer, and the dependency rule is broken.

**Mitigation:** Keep the **domain package free of Spring**. Domain services can be plain classes; the application layer instantiates them or obtains them via a factory. If you need dependency injection for a domain service, define the interface in the domain and put the implementation (with `@Component`) in the application or infrastructure layer so the domain depends only on its own interface.

**Guideline:** No Spring annotations in the domain package. Domain types depend only on other domain types (and optionally domain-side interfaces implemented elsewhere).

---

## Aggregate reconstitution

**Risk:** Building aggregates from the database (e.g. from a `ResultSet`) in infrastructure can bypass invariants if the repository constructs the aggregate via setters or reflection. The aggregate might be reconstituted in an invalid state, and the domain’s guarantees are weakened.

**Mitigation:** Reconstitute aggregates in a **domain-controlled** way. Provide a factory method or a dedicated reconstitution constructor on the aggregate (e.g. `Order.reconstitute(id, lines, status, ...)`) that is used only when loading from persistence. The repository implementation calls this method with data mapped from the database; it does not set internal state directly. The domain owns the rules for a valid aggregate, including when reconstituting from persistence.

**Guideline:** The repository implementation does not construct aggregates by setting fields from outside. It uses a domain-provided factory or reconstitution method. Document reconstitution as a first-class concept in the domain.

---

## Schema and mapping ownership, N+1

**Risk:** With no ORM, you own all SQL and mapping. Complex aggregates (nested value objects, collections) can lead to many tables, N+1 queries, or unclear schema ownership. Schema drift between domain and database can occur if mapping is ad hoc.

**Mitigation:** Use a **persistence model** in infrastructure (as in [Spring Boot mapping](05-spring-boot-mapping.md)): simple types that mirror the database (e.g. `OrderRow`, `OrderLineRow`). The repository implementation maps: domain aggregate ↔ persistence model ↔ database. Schema changes are confined to the persistence model and JDBC code; the domain stays independent of table shape. Design loading so that one aggregate load does not trigger N+1 queries (e.g. load order and lines in one or two queries, then map to aggregate).

**Guideline:** Decide how aggregates map to storage (normalised tables, JSON column, etc.) and document it. Use a persistence model when domain shape and table shape diverge. Review repository implementations for N+1 and connection usage.

---

## Domain service depending on repositories

**Risk:** To avoid “application service loads and passes to domain service,” someone injects a repository (or a “read-only” repository) into a domain service. Persistence concerns leak into the domain; the domain service is no longer pure domain logic.

**Mitigation:** **Domain services do not depend on repositories.** The application service loads all required data (aggregates, value objects) via repositories and passes it to the domain service. If the domain service needs read-only data (e.g. a policy, a rate), either (a) the application service loads it and passes it in, or (b) the domain defines a small read-only interface (e.g. `PolicySource.getPolicy(id)`) implemented in infrastructure. Do not inject full repositories into domain services.

**Guideline:** Domain services receive domain objects (or data) from the caller. They do not perform load/save. Pass data in or use a minimal domain interface for read-only lookups, implemented in infrastructure.

---

## Transaction boundary and cross-app

**Risk:** With one app per domain, cross-domain flows involve multiple applications. A single `@Transactional` cannot span processes. Teams may assume they can “just add a transaction” when integrating with another service, leading to inconsistent state or hidden distributed transaction attempts.

**Mitigation:** Treat **one transaction = one process, one database** as a hard rule. Cross-application coordination uses events, outbox, or sagas—not distributed transactions. Document this in the context map: which boundaries are process boundaries, and how consistency is achieved (eventual consistency, saga steps). When a use case spans two applications, design for explicit handoffs (e.g. publish domain event; other app consumes and updates its own aggregate in its own transaction).

**Guideline:** Do not assume a single ACID transaction across applications. Model process boundaries on the context map. Use sagas, outbox, or events for cross-app consistency; keep transactions local to one application.

---

## Persistence model and when to use it

**Risk:** Mapping domain aggregates directly to SQL in the repository can tie the domain to table shape. When the schema changes (new columns, denormalisation, legacy integration), the mapping code becomes complex and the domain may be distorted to match the database.

**Mitigation:** When domain shape and table shape diverge (or will diverge), introduce a **persistence model** in infrastructure (as in [Spring Boot mapping](05-spring-boot-mapping.md)). The repository implementation does: domain aggregate ↔ persistence model (in memory) and persistence model ↔ database (JDBC). The persistence model absorbs schema; the domain stays independent. Use it when you have legacy or shared schemas, or when you expect schema to evolve independently of the domain.

**Guideline:** Use a persistence model when the database layout does not match the domain 1:1, or when schema evolution is independent. Keep the domain free of column and table names.

---

## Summary table

| Risk | Mitigation | Guideline |
|------|------------|-----------|
| Domain depending on Spring | No Spring in domain; interfaces in domain, implementations elsewhere | No Spring annotations in domain package |
| Aggregate reconstitution | Domain-controlled factory or reconstitute method | Repository uses domain reconstitution; no external setters for invariant state |
| Schema/mapping, N+1 | Persistence model; explicit mapping and load design | Document mapping; use persistence model when shapes diverge; avoid N+1 |
| Domain service + repositories | Application service loads and passes data; or minimal read-only interface in domain | Domain services do not depend on repositories |
| Transaction boundary, cross-app | One transaction = one process; events/sagas/outbox for cross-app | No distributed transactions; model process boundaries on context map |
| Persistence model | Dedicated persistence model in infrastructure when domain and DB diverge | Use when schema ≠ domain 1:1 or schema evolves independently |
