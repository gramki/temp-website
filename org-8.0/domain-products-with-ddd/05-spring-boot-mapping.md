# Spring Boot Mapping (No ORM)

This section maps the DDD concepts defined in [DDD concepts](02-ddd-concepts.md) to a Spring Boot application: package layout, repository and persistence model, Domain Service and Application Service placement, domain events, and the dependency rule. It assumes **no JPA or ORM**—persistence is via JDBC (e.g. `JdbcTemplate`) with a dedicated persistence model in infrastructure—and **one application per bounded context**.

> **Before your first assignment.** (1) Put **domain** types (entities, value objects, aggregate roots, repository *interface*) in the `domain/` package—**no** `@Component`, `@Service`, or other Spring annotations there. (2) Put **application** use-case orchestration in `application/` with `@Service` and `@Transactional`. (3) Put **repository implementation** and JDBC in `infrastructure.persistence/`. (4) Remember: a DDD "Domain Service" is a **class** in the domain layer, not a microservice or Kubernetes Service. When in doubt, ask your tech lead or use the [implementation checklist](09-summary-and-checklist.md#implementation-checklist) in [09 Summary and checklist](09-summary-and-checklist.md).

---

## Package structure

One Spring Boot application owns one bounded context. The package layout reflects the layers:

```
com.example.ordering                    # Application = one bounded context (e.g. Ordering)
├── domain/                             # Domain layer (pure; no Spring in domain types)
│   ├── Order.java                      # Aggregate root (entity)
│   ├── OrderLine.java                  # Entity (inside aggregate)
│   ├── OrderId.java                    # Value object
│   ├── Money.java                      # Value object
│   ├── OrderPlaced.java                # Domain event
│   ├── OrderRepository.java            # Port: interface only (domain types)
│   └── OrderPricingService.java       # Domain service (optional; see below)
├── application/                         # Application layer
│   ├── PlaceOrderService.java          # Application service (@Service, @Transactional)
│   └── PlaceOrderCommand.java
└── infrastructure/                      # Infrastructure: persistence, HTTP, messaging
    ├── persistence/
    │   ├── OrderRepositoryImpl.java    # Implements domain OrderRepository; JDBC
    │   ├── OrderRowMapper.java         # Row ↔ domain Order (or inline)
    │   └── OrderRow.java               # Persistence model (see below)
    ├── web/
    │   └── OrderController.java
    └── messaging/                       # Optional: outgoing events
        └── OrderEventPublisher.java
```

- **domain:** Entities, value objects, aggregate roots, domain events, **repository interface** (no implementation), domain services. No framework types, no SQL, no JDBC.
- **application:** Use-case orchestration: application services, commands/DTOs. Uses repository interface and domain types only.
- **infrastructure:** Repository implementation (JDBC), persistence model, REST, messaging. Depends on domain and application.

---

## Repository: interface in domain, implementation with JDBC

The **repository interface** lives in the **domain** and uses only domain types (e.g. `Optional<Order> findById(OrderId id)`, `void save(Order order)`). The **implementation** lives in **infrastructure.persistence**: it implements the domain interface, uses **JdbcTemplate** (or raw JDBC), and maps between domain aggregates and the database. The domain and application layers never see JDBC or SQL.

**Trade-off:** No ORM avoids framework bloat and keeps persistence explicit; the trade-off is more mapping code and schema ownership in infrastructure. See [Risks and mitigations](07-risks-and-mitigations.md) for persistence model and reconstitution.

---

## Persistence model: domain ↔ persistence model ↔ DB

When the database shape and the domain shape diverge (e.g. denormalized tables, legacy schema, or schema that evolves independently), introduce a **persistence model** in infrastructure: simple data holders that mirror the database (e.g. `OrderRow`, `OrderLineRow` with columns like `order_id`, `total_amount_cents`). The repository implementation then does: **domain aggregate ↔ persistence model** (in memory) and **persistence model ↔ database** (JDBC). The domain never sees column names or table layout; the persistence model absorbs schema changes. See [Risks and mitigations](07-risks-and-mitigations.md) for when and how.

---

## Domain Service and Application Service placement

**Domain Service** (as defined in [DDD concepts](02-ddd-concepts.md)): a class in **domain/** that holds domain logic spanning multiple entities or aggregates. It does not perform CRUD and does not hold references to Repositories. It can be a plain class; if you need dependency injection, define an interface in domain and put the implementation in application or infrastructure so the domain stays free of Spring.

**Application Service:** a class in **application/** with `@Service`. It orchestrates one use case: loads via repository, calls domain (entity methods or domain service), saves via repository, publishes events. Use `@Transactional` here for the use-case transaction boundary. It injects the domain **repository interface** (and optionally domain services); the infrastructure provides the repository implementation.

---

## Domain events

**Domain events** are POJOs in the domain (e.g. `OrderPlaced`). The application service publishes them after persisting (e.g. via `ApplicationEventPublisher` for in-process listeners, or via an outbound port implemented in infrastructure for cross-process messaging). Subscribers use `@EventListener` or `@TransactionalEventListener` in application or infrastructure. For cross-context or cross-process, use messaging (e.g. Kafka, RabbitMQ) in infrastructure; the domain event remains a simple POJO.

---

## Dependency rule and no Spring in domain

The **dependency rule** is: domain does not depend on application or infrastructure; application depends only on domain; infrastructure depends on domain and application. To keep the domain durable and testable, **do not put Spring annotations (e.g. `@Component`) on domain types.** The domain package should be plain Java: entities, value objects, aggregate roots, domain events, repository interface, and domain services as plain classes. The application layer instantiates or obtains domain services (e.g. via a factory or an interface implemented in application/infrastructure). See [Risks and mitigations](07-risks-and-mitigations.md) and [Testability and testing patterns](08-testability-and-testing-patterns.md).

---

## “Service” in DDD is not a process boundary

**Domain Service** and **Application Service** (as defined in [DDD concepts](02-ddd-concepts.md)) are **design boundaries**—roles and responsibilities in the code. They are **not** process or deployment boundaries. One **process** (e.g. one Kubernetes Deployment/Pod, one monolith, one microservice) can contain:

- Application Service(s),
- Domain Service(s),
- Repository(ies),

all in the **same process**. The flow “Application Service → Repository (load) → Domain Service → Repository (save)” runs in that single process. If there is a single database, that can be **one local transaction**. No cross-process coordination is implied.

**Transaction management** is typically centralised at the Application Service: one use case = one transaction boundary. Repository and Domain Service are transaction-unaware. The overhead of having three layers does not by itself add multiple transactions; complexity comes when you **span process boundaries** (e.g. two microservices, two databases).

**Important:** Do **not** confuse a **DDD Domain Service** (a class that holds domain logic) with a **microservice** (a deployable process). A single microservice (or Kubernetes Deployment) can host many Domain Services and many Application Services inside one process.

---

## How DDD layers translate to Kubernetes deployments

A **Kubernetes Deployment** (or “microservice”) is a **process/deployment boundary**: one or more pods running the same application. **DDD layers** (Application Service, Domain Service, Repository) are **logical layers inside that process**. One Kubernetes Deployment can (and often does) contain:

- Multiple Application Services (one per use case or command),
- Multiple Domain Services,
- Multiple Repositories,

all in the **same process**, sharing the same transaction boundary when talking to one database.

**Bounded contexts** may or may not align with deployments:

- **Option A:** One bounded context = one Kubernetes Deployment (common in microservice architectures; this guide assumes this when “one app per domain”).
- **Option B:** Several bounded contexts in one Deployment (modular monolith).

The choice is driven by the context map, team boundaries, scalability, and deployment granularity—not by the DDD definitions of “Domain Service” or “Application Service.”

**Takeaway:** A DDD **Domain Service** is **not** a microservice. It is a component inside a process. When you deploy (e.g. as a Kubernetes Service), you are deploying a **process** that may contain many Domain Services and Application Services. Spreading a **single transaction** across process boundaries (e.g. across two Kubernetes Deployments) is where distributed transaction complexity appears; keeping Domain Service, Application Service, and Repository in one process keeps transactions local and simple.
