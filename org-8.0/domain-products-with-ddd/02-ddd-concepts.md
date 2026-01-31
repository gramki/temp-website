# DDD Concepts

This section defines the core building blocks of Domain-Driven Design (DDD) used in this guide. The terms here are the single definition source for the rest of the guide.

> **For junior developers.** New to DDD? Read this section once, then keep it open as a reference while you work. When you see "aggregate," "Domain Service," or "Repository" in later sections, come back here for the definition. The table at the end is a quick lookup.

---

## Domain and ubiquitous language

The **domain** is the subject area the software supports—the “problem” the system exists to solve (e.g. underwriting, claims, orders). The **ubiquitous language** is a single, shared vocabulary used by domain experts and the development team: the same terms appear in code, documentation, and conversation. When an operation or concept has a name in the domain, that name is used in the model and in the code. The model is refined through dialogue with domain experts; the language is shared.

---

## Bounded context and context map

A **bounded context** is an explicit boundary within which a particular model and its ubiquitous language apply. Different bounded contexts can use the same word with different meaning (e.g. “Customer” in a Sales context vs. a Shipping context). The boundary is chosen so that the model inside it is consistent and coherent.

A **context map** is a description or diagram of how bounded contexts relate: who depends on whom, and how they integrate (APIs, events, anti-corruption layers). The context map is the source of truth for boundaries and integrations; it informs ownership, consistency boundaries, and deployment units.

---

## Building blocks: entities, value objects, aggregates

| Concept | Meaning |
|--------|---------|
| **Entity** | An object with a stable identity over time, even if its attributes change (e.g. `Customer`, `Order`). Identity is what distinguishes one entity from another. |
| **Value Object** | An object defined only by its attributes; it has no identity. Value objects are immutable (e.g. `Money`, `Address`, `DateRange`). Two value objects with the same attributes are interchangeable. |
| **Aggregate** | A cluster of entities and value objects treated as one unit. External code holds references only to one entity in the cluster—the **aggregate root**—and goes through the root to change the aggregate. The aggregate enforces invariants for the data it owns. |
| **Aggregate Root** | The single entry point for all changes to an aggregate. The aggregate root enforces invariants inside the aggregate. No external reference is held to entities inside the aggregate except through the root. |

---

## Domain events

A **domain event** is something that happened in the domain that other parts of the system might care about (e.g. `OrderPlaced`, `PaymentReceived`). Domain events are used for decoupling and eventual consistency: one bounded context can publish an event when something meaningful happens, and other contexts (or the same context) can react without a direct call. Events are named in the past tense and expressed in the ubiquitous language.

---

## Repository

A **repository** is an abstraction for loading and saving aggregates (or entities) as if they were in a collection. It hides the details of persistence. The repository interface lives in the domain and uses only domain types (e.g. `Order`, `OrderId`). **Repositories are responsible for persistence (load/save) of domain entities and aggregates.** The application layer uses the repository to load aggregates before calling domain logic and to save them after. The domain does not perform CRUD; the repository does.

---

## Domain Service and Application Service

When an operation doesn’t naturally fit on a single entity or value object—for example, when it involves multiple aggregates or a concept that isn’t “owned” by one thing—it can be modeled as a **Domain Service**. When the use case is a flow that coordinates loading, domain logic, persistence, and publishing, that flow is an **Application Service**. The distinction is critical for keeping the domain focused and the application layer thin.

### Domain Service

- **Layer:** Domain.
- **Responsibility:** Holds **domain logic** that doesn’t naturally belong to a single entity or value object (e.g. logic involving multiple aggregates or a concept that isn’t “owned” by one thing).
- **Characteristics:**
  - Expressed in the **ubiquitous language** (e.g. `TransferMoneyService`, `PricingService`).
  - **Stateless:** operates on domain objects passed in (or data provided by the caller).
  - **Does not perform CRUD.** Does not hold references to Repositories. The **caller** (typically an Application Service) loads and saves via Repositories.
  - Depends only on **domain types** (entities, value objects, other domain services).

### Application Service

- **Layer:** Application (use-case / application layer).
- **Responsibility:** **Orchestrates** a use case: “load → call domain → persist → publish”.
- **Characteristics:**
  - **Thin:** no business rules; only flow.
  - Depends on **Repositories**, **Domain Services**, **aggregates**, and infrastructure (e.g. event bus, external APIs).
  - Handles **transactions**, **authorization**, **mapping** (DTOs ↔ domain).
  - Named after the use case (e.g. `PlaceOrderApplicationService`, `SubmitClaimHandler`).

### Who does CRUD?

- **Repositories** are responsible for **persistence** (load by id, save, and optionally delete) of aggregates. That is the “CRUD” for domain entities.
- **Domain Services** do **not** do CRUD. They receive already-loaded entities or aggregates from the Application Service and perform domain logic. The Application Service uses Repositories to load before calling the Domain Service and to save after.

### Summary

| | Domain Service | Application Service |
|---|----------------|---------------------|
| **Layer** | Domain | Application |
| **Contains** | Domain logic | Orchestration only |
| **Knows about** | Entities, value objects, domain concepts | Repositories, transactions, infrastructure |
| **CRUD** | No | No (orchestrates Repository for load/save) |
| **Naming** | Domain concept (e.g. `TransferService`) | Use case / action (e.g. `TransferMoneyCommandHandler`) |

---

## Concept reference table

| Concept | Meaning |
|--------|---------|
| **Domain** | The subject area the software supports. The “problem” the system exists to solve. |
| **Ubiquitous Language** | A single, shared vocabulary used by domain experts and the dev team. Same terms in code, docs, and conversation. |
| **Bounded Context** | An explicit boundary within which a particular model and its ubiquitous language apply. |
| **Context Map** | A description or diagram of how bounded contexts relate: who depends on whom, and how they integrate. |
| **Entity** | An object with a stable identity over time. |
| **Value Object** | An object defined only by its attributes; no identity; immutable. |
| **Aggregate** | A cluster of entities and value objects treated as one unit; one entity is the aggregate root. |
| **Aggregate Root** | The single entry point for all changes to an aggregate. Enforces invariants. |
| **Domain Event** | Something that happened in the domain that other parts of the system might care about. |
| **Repository** | Abstraction for loading and saving aggregates. Responsible for persistence. |
| **Domain Service** | Domain logic that doesn’t sit on a single entity or value object. No CRUD; no Repository references. |
| **Application Service** | Orchestrates a use case: load, call domain, persist, publish. Thin; no business rules. |
