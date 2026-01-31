# Introduction

This guide explains how to implement domain products using Domain-Driven Design (DDD) with Spring Boot.

> **If you're new to DDD or this guide.** Read [02 DDD concepts](02-ddd-concepts.md) first so that terms like "aggregate," "Domain Service," and "Application Service" are clear. Then read [03 Mapping product to DDD](03-mapping-product-to-ddd.md) to see how a use case or user story maps to code. For your first implementation, follow [05 Spring Boot mapping](05-spring-boot-mapping.md) and use [09 Summary and checklist](09-summary-and-checklist.md) before you submit your work. It is written for developers and principal engineers who need a clear path from product requirements to design and code, and who want to keep the domain explicit, testable, and independent of framework or persistence details.

---

## Purpose

Product requirements—use cases, value streams, features—need a path into design and code. DDD provides a shared language and structure: the **domain** and **ubiquitous language** define what the system is about; **bounded contexts** and the **context map** define boundaries and integrations; **entities**, **aggregates**, **Domain Services**, and **Application Services** give concrete building blocks. This guide shows how to map those concepts to a Spring Boot application without an ORM, with one application per domain or subdomain, and how to avoid the common trap of an anemic domain.

A recurring source of confusion is the word **“service”** in DDD. A **Domain Service** and an **Application Service** are design roles—they are responsibilities in the code. They are not process boundaries. Confusing a DDD Domain Service with a “microservice” or a Kubernetes Service leads to wrong expectations about transactions and deployment. This guide clarifies the distinction and shows how DDD layers translate to a single process (e.g. one Kubernetes Deployment) and when complexity arises—when you span process boundaries.

---

## Audience

- **Developers:** You will find concrete guidance on package layout, repository and persistence model, Domain Service vs Application Service placement, and testing. Sections [05 Spring Boot mapping](05-spring-boot-mapping.md), [06 Anemic domain](06-anemic-domain.md), and [08 Testability and testing patterns](08-testability-and-testing-patterns.md) are especially relevant for day-to-day implementation.
- **Principal Engineers:** You will find guidance on bounded context vs subdomain, the context map as source of truth, when to split or keep applications together, and risks and mitigations. Sections [04 One app per domain](04-one-app-per-domain.md) and [07 Risks and mitigations](07-risks-and-mitigations.md) are especially relevant for boundary and governance decisions.

The full sequence of sections (01–09) is recommended when adopting the approach; individual sections can be used as reference once the concepts are familiar.

---

## Scope

- **DDD + Spring Boot:** The guide covers DDD concepts and their mapping to a Spring Boot application. It does not use JPA or any ORM: persistence is via JDBC (e.g. `JdbcTemplate`) with a dedicated persistence model in infrastructure, so the domain stays free of persistence concerns.
- **One app per domain or subdomain:** Each Spring Boot application is assumed to own one bounded context (one domain or subdomain). The guide explains how to decide that boundary and how to avoid both nanoservices and a single monolith.
- **Anemic domain and risks:** The guide includes a thorough treatment of anemic domain—what it is, why it is a slippery slope, and how to keep a rich domain—and a section on risks and mitigations (domain and Spring, aggregate reconstitution, transactions, and related topics).

---

## How to use this guide

1. **First time:** Read sections 01–09 in order. Concepts are introduced in [02 DDD concepts](02-ddd-concepts.md); product mapping in [03 Mapping product to DDD](03-mapping-product-to-ddd.md); deployment boundary in [04 One app per domain](04-one-app-per-domain.md); implementation in [05 Spring Boot mapping](05-spring-boot-mapping.md); then anemic domain, risks, testability, and summary.
2. **Reference:** Use [02 DDD concepts](02-ddd-concepts.md) as the definition source for terms (bounded context, aggregate, Domain Service, etc.). Use [09 Summary and checklist](09-summary-and-checklist.md) for the quick-reference table (DDD concept → Spring Boot artifact) and implementation checklist.
3. **By role:** Developers may jump to 05, 06, 08; principal engineers to 04, 07. Cross-references point back to 02 where concepts are defined.

---

## Positioning in the organization

This guide supports **domain products**: systems whose core is a well-modeled domain, with clear boundaries and a shared language. It aligns with practices that treat the domain as the heart of the design and that separate domain, application, and infrastructure. It can be used alongside product-line or domain-engineering models that emphasize core assets and derived products; for organizational context on product lines and team structure, see the [Product Line Engineering](../product-line-engineering/README.md) documentation. This guide remains self-contained for DDD and Spring Boot implementation.
