# Testability and Testing Patterns

This section explains why testability matters when implementing DDD with Spring Boot, and gives patterns for unit and integration testing so that the domain stays fast and simple to test and the application and infrastructure are covered appropriately.

> **New to DDD?** Test the **domain** (aggregates, value objects, domain services) with **no Spring and no database**—just plain Java and JUnit. Test the **application service** with mocks for the repository and event publisher. Use integration tests only for the repository (real DB) and for full flows when needed. If your domain tests need `@SpringBootTest` or a database, the domain likely has framework or persistence in it—refactor so the domain stays plain Java; see [05 Spring Boot mapping](05-spring-boot-mapping.md) and [07 Risks and mitigations](07-risks-and-mitigations.md).

---

## Why testability matters

A rich domain (as in [Anemic domain](06-anemic-domain.md)) is only valuable if it can be tested in isolation: invariants, behavior, and domain services should be verifiable without starting a Spring context or a database. When the domain is free of framework and persistence, unit tests are fast and focused. Refactoring the domain is safe because tests depend only on domain types. When the domain is mixed with Spring or infrastructure, tests become slower and more brittle, and the incentive to add behavior to the domain decreases. The guide’s approach (no Spring in domain, repository interface in domain, persistence in infrastructure) is designed so that the domain is easy to test and the rest of the system can be tested with clear boundaries.

---

## Unit testing the domain (no Spring)

**Goal:** Test aggregates, value objects, and domain services with no Spring context, no database, no mocks of infrastructure.

**What to test:**

- **Aggregates:** Invariants (e.g. order total equals sum of line items), domain actions (e.g. `order.addLineItem(...)` updates state correctly), and rejection of invalid operations (e.g. adding a line item that would violate a rule).
- **Value objects:** Equality, immutability, and any behavior (e.g. `Money.add(...)`).
- **Domain services:** Logic that operates on domain objects passed in; verify inputs and outputs with plain Java objects.

**How:** Instantiate domain types directly, call methods, assert on state or return values. No `@SpringBootTest`, no `@Autowired`. Use JUnit (or equivalent) and assertions only. If a domain service is a plain class, instantiate it and pass in domain objects built in the test.

**Guideline:** Keep domain tests framework-free. They should run in milliseconds and have no external dependencies. If a domain test needs Spring or a database, the domain has likely been contaminated; refactor so that the logic under test is pure domain.

---

## Unit testing application services (mocks)

**Goal:** Test the orchestration of a use case: that the application service loads (via repository), calls domain (aggregate or domain service), saves (via repository), and publishes events, with the correct arguments and order.

**What to test:** The application service’s flow: given a command, it should call the repository to load the aggregate (or create it), call domain methods or domain service, call the repository to save, and publish the expected domain event(s). Business logic is not tested here; it is tested in domain unit tests. Here you verify that the application service wires the right calls.

**How:** Use mocks (e.g. Mockito) for the repository interface and for any domain service or event publisher. Inject mocks into the application service. Execute the use case (e.g. `placeOrderService.place(command)`). Verify that the repository was called with the expected aggregate (or id), that the domain was invoked, and that the event publisher was called with the expected event. You can use a real domain type (aggregate, domain service) if it is a plain class with no dependencies, or a mock if the application service only needs a stub.

**Guideline:** Application service tests can run without Spring (manual instantiation of the service and mocks) or with a minimal Spring context that only provides the application service and its dependencies. Prefer no context for speed; use context only if you need to test `@Transactional` or other Spring behavior.

---

## Integration testing the repository (Testcontainers or in-memory DB)

**Goal:** Verify that the repository implementation correctly persists and loads aggregates (or persistence model), and that the mapping between domain and persistence model (and database) is correct.

**What to test:** Save an aggregate (via the domain repository interface, implemented by the real repository implementation); load it back; assert that the loaded aggregate equals the saved one (or that key state matches). If you use a persistence model, you can also test that the mapper (domain ↔ persistence model) round-trips correctly without the database, and then test the full repository with a real DB.

**How:** Use Testcontainers to start a real database (e.g. PostgreSQL) for the test, or use an in-memory database (e.g. H2) if acceptable for your project. Configure the repository implementation with the test datasource. Create a domain aggregate, save it via the repository, load it by id, assert equality or key fields. Optionally test the persistence model mapper in isolation (domain object → persistence model → domain object) with no DB.

**Guideline:** Repository integration tests are the place to verify schema, SQL, and mapping. Keep them focused on one aggregate type per test (or a small set). Use Testcontainers when you want to test against the same database engine as production.

---

## Integration testing application service with real repository

**Goal:** Optionally verify the full flow: application service + real repository + database, in one process, to ensure that transaction boundaries and persistence work together.

**What to test:** Run a use case end-to-end within the application layer: command → application service → repository (real impl) → database. Assert on database state or on the returned result. This catches issues that unit tests (with mocks) and repository-only integration tests might miss (e.g. transaction rollback, mapping errors in the full flow).

**How:** Use `@SpringBootTest` with a test database (Testcontainers or in-memory). Inject the application service (or the controller that delegates to it). Execute the use case. Query the database or use the repository to load and assert. Use `@Transactional` with rollback in tests if you do not want to persist.

**Guideline:** Use this sparingly; prefer domain unit tests and application service unit tests (with mocks) for speed. Use full application-service integration tests when you need to validate transaction behavior or the full stack for a critical path.

---

## Testing domain events

**In-process:** If the application service publishes domain events via `ApplicationEventPublisher`, use a test listener (e.g. `@EventListener` in the test) or a mock of the publisher to verify that the expected event was published with the expected payload. Application service unit tests can verify that the mock publisher was called with the right event.

**Cross-process:** If events are published to a message broker (e.g. Kafka), use integration tests that start the broker (e.g. Testcontainers) and assert that the correct message appears on the topic. Alternatively, test the outbound adapter (domain event → message) in isolation with a mock broker or a test double.

---

## Testing persistence model and anti-corruption at the DB boundary

**Goal:** Verify that the persistence model correctly represents the database shape and that the mapper (domain aggregate ↔ persistence model) round-trips without loss. When you have an anti-corruption layer (e.g. translating from a legacy or external schema), test the translation in both directions.

**How:** For the mapper: given a domain aggregate, map to persistence model; map back to domain; assert equality (or that key invariants hold). For persistence model ↔ database: use repository integration tests that write and read via the persistence model and assert on stored rows or on reloaded domain objects. For ACL: given an external representation (e.g. legacy DTO), translate to domain type and assert; given domain type, translate to external representation and assert.

**Guideline:** Persistence model and mappers are in infrastructure; test them with unit tests (mapper only) and integration tests (repository + DB). Keep domain out of these tests; only domain types at the boundary (e.g. repository interface) are used.

---

## Test pyramid and what to mock

- **Base (many):** Domain unit tests. No mocks; no Spring; no DB. Fast.
- **Middle:** Application service unit tests (mocks for repository, event publisher, domain service if needed). Domain logic tests in domain unit tests; here you verify orchestration. Fast.
- **Narrow (fewer):** Repository integration tests (real DB or Testcontainers). Verify persistence and mapping.
- **Top (few):** Full application service integration tests with real repository and DB when you need to validate transactions or full stack. Slower; use for critical paths.

**What to mock:** In application service unit tests, mock the repository interface and the event publisher (and any other outbound ports). Use a real domain type (aggregate, domain service) when it is a plain class. Do not mock the domain; mock only infrastructure and application-layer dependencies.

---

## Guidelines summary

- **Domain tests:** Framework-free; no Spring, no DB. Instantiate domain types; assert on behavior and invariants. Run in milliseconds.
- **When to use @SpringBootTest:** Only when you need to test Spring-managed behavior (e.g. transactions, component scanning) or the full stack. Prefer unit tests without a context for the domain and for application services (with mocks).
- **Avoid over-use of full context:** Loading the full Spring context for every test slows the suite and couples tests to the entire configuration. Use it for a small set of integration tests; keep the majority of tests unit-level with mocks or plain instantiation.
