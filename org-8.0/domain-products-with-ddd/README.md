# Implementing Domain Products with DDD and Spring Boot

A guide for **Developers** and **Principal Engineers** on implementing Domain-Driven Design (DDD) using Spring Boot: modeling domain products, mapping product requirements to DDD, and implementing with one application per domain and no ORM.

---

## When to use this guide

Use this guide when **implementing or reviewing domain products with Spring Boot**—when you need a clear path from product requirements (use cases, value streams) to design and code, and when you want to keep the domain explicit, testable, and independent of framework or persistence details. For organizational context on product lines, domain engineering, and team structure, see the [Product Line Engineering](../product-line-engineering/README.md) documentation.

---

## Audience and how to navigate

- **Developers:** Sections [05 Spring Boot mapping](05-spring-boot-mapping.md), [06 Anemic domain](06-anemic-domain.md), and [08 Testability and testing patterns](08-testability-and-testing-patterns.md) are especially relevant for day-to-day implementation and code quality. The full sequence 01–09 is recommended when adopting the approach.
- **Principal Engineers:** Sections [04 One app per domain](04-one-app-per-domain.md) and [07 Risks and mitigations](07-risks-and-mitigations.md) are especially relevant for boundary decisions, deployment strategy, and governance. The full sequence 01–09 is recommended when adopting the approach.

---

## For junior developers

> **Start here.** Read sections **01 → 02 → 03 → 05** in order before you code. Keep [02 DDD concepts](02-ddd-concepts.md) open as a reference—you will need the definitions of aggregate, Domain Service, Application Service, and Repository often.

> **Prerequisites.** You should be comfortable with Java, Spring Boot basics (e.g. `@Service`, dependency injection), and SQL/JDBC. You do **not** need prior DDD experience; the guide introduces the concepts. If terms like "invariant," "aggregate root," or "ubiquitous language" are new, they are defined in [02 DDD concepts](02-ddd-concepts.md).

> **Who can help.** For **domain questions** (what is an Order? what rules apply?): talk to your product or domain expert. For **boundary and deployment** (is this one app or two?): ask your Principal Engineer or tech lead. For **implementation** (where does this class go? how do I test it?): use [05 Spring Boot mapping](05-spring-boot-mapping.md), [06 Anemic domain](06-anemic-domain.md), and [08 Testability](08-testability-and-testing-patterns.md), and pair with a senior developer if stuck.

> **Common pitfalls.** (1) Putting business logic in the Application Service instead of the aggregate—see [06 Anemic domain](06-anemic-domain.md). (2) Confusing a DDD "Domain Service" with a microservice—they are not the same; see [05 Spring Boot mapping](05-spring-boot-mapping.md). (3) Adding Spring annotations (e.g. `@Component`) to domain classes—keep the domain package plain Java; see [05 Spring Boot mapping](05-spring-boot-mapping.md) and [07 Risks and mitigations](07-risks-and-mitigations.md).

> **Before your next assignment.** Use the [implementation checklist](09-summary-and-checklist.md#implementation-checklist) in [09 Summary and checklist](09-summary-and-checklist.md) to verify your code: domain vs application vs infrastructure, no anemic domain, repository interface in domain, tests for domain without Spring.

---

## Key terms

For definitions of **bounded context**, **aggregate**, **Domain Service**, **Application Service**, **Repository**, and other DDD concepts used in this guide, see [DDD concepts](02-ddd-concepts.md).

---

## Table of contents

| Section | Description |
|--------|-------------|
| [01 Introduction](01-introduction.md) | Purpose, audience, scope, how to use the guide. |
| [02 DDD concepts](02-ddd-concepts.md) | Domain, ubiquitous language, bounded context, entities, value objects, aggregates, repository, Domain Service vs Application Service, context map. |
| [03 Mapping product to DDD](03-mapping-product-to-ddd.md) | Use cases and value streams → application services and domain model; product requirements → DDD checklist. |
| [04 One app per domain](04-one-app-per-domain.md) | Subdomain vs bounded context; context map as source of truth; when to split or keep together; governance. |
| [05 Spring Boot mapping](05-spring-boot-mapping.md) | Package layout, repository and persistence model, Domain/Application Service placement, no ORM; service is not a process boundary. |
| [06 Anemic domain](06-anemic-domain.md) | What anemic domain is, why it is a slippery slope, rich vs anemic, guidelines and code review. |
| [07 Risks and mitigations](07-risks-and-mitigations.md) | Domain and Spring, reconstitution, schema/mapping, transactions; risk → mitigation → guideline. |
| [08 Testability and testing patterns](08-testability-and-testing-patterns.md) | Unit and integration testing; domain without Spring; test pyramid and guidelines. |
| [09 Summary and checklist](09-summary-and-checklist.md) | Implementation checklist, quick reference, references. |

---

## Scope

- **In scope:** DDD concepts, mapping product to DDD, one Spring Boot application per domain or subdomain, implementation without JPA/ORM (JDBC-based persistence), anemic domain avoidance, risks and mitigations, testability.
- **Out of scope:** Sample codebase or repository; changes to other documentation. The guide is documentation only.

---

## Positioning

This guide supports **domain products** and aligns with practices that treat the domain as the heart of the design: bounded contexts, ubiquitous language, and clear separation between domain, application, and infrastructure. It can be used alongside product-line or domain-engineering models that emphasize core assets and derived products.
