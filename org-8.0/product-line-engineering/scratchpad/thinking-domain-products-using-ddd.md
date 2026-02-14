# Thinking Domain Products using DDD

A note for **Developers** and **Principal Engineers** on how to use Domain-Driven Design (DDD) to model domain products, map product requirements to DDD concepts, and avoid confusing DDD “services” with deployment units (e.g. microservices, K8s Services).

---

## 1. Why This Note

- **Product requirements** (use cases, value streams, features) need a clear path into **design and code**. DDD gives a shared language and structure.
- **“Service”** in DDD (Domain Service, Application Service) is a **design role**, not a process or deployment boundary. Confusing it with a “microservice” or a K8s Service leads to wrong expectations about boundaries and transactions.
- This note clarifies: (1) core DDD concepts, (2) how use cases and value streams map to the domain, (3) Domain Service vs Application Service, (4) how DDD layers translate to deployments (e.g. K8s), and (5) how to map product requirements to DDD.

---

## 2. Core DDD Concepts (Recap)

| Concept | Meaning |
|--------|---------|
| **Domain** | The subject area the software supports (e.g. underwriting, claims, orders). The “problem” the system exists to solve. |
| **Ubiquitous Language** | A single, shared vocabulary used by domain experts and the dev team. Same terms in code, docs, and conversation. |
| **Bounded Context** | An explicit boundary within which a particular model and its ubiquitous language apply. Different contexts can use the same word with different meaning (e.g. “Customer” in Sales vs. Shipping). |
| **Context Map** | A description or diagram of how bounded contexts relate: who depends on whom, and how they integrate (APIs, events, ACL). |
| **Entity** | An object with a stable identity over time, even if its attributes change (e.g. `Customer`, `Order`). |
| **Value Object** | An object defined only by its attributes; no identity. Immutable (e.g. `Money`, `Address`, `DateRange`). |
| **Aggregate** | A cluster of entities and value objects treated as one unit. One entity is the **aggregate root**; external code only holds references to the root and goes through it to change the aggregate. |
| **Aggregate Root** | The single entry point for all changes to an aggregate. Enforces invariants inside the aggregate. |
| **Domain Event** | Something that happened in the domain that other parts of the system might care about (e.g. `OrderPlaced`, `PaymentReceived`). Used for decoupling and eventual consistency. |
| **Repository** | Abstraction for loading and saving aggregates (or entities) as if they were in a collection. Hides persistence. **Repositories are responsible for persistence (load/save) of domain entities/aggregates.** |
| **Domain Service** | Domain logic that doesn’t naturally sit on a single entity or value object; operates across multiple domain objects (e.g. “transfer money between accounts”). **Does not perform CRUD; does not hold references to Repositories.** |
| **Application Service** | Orchestrates a use case: loads aggregates via repositories, calls domain logic (entities or domain services), persists, publishes events. **Thin orchestration; no business rules.** |

---

## 3. Use Cases and Value Streams: Mapping to the Domain

### 3.1 Use Cases

**Use cases** describe who does what with the system and why (actor + goal + scenario). For developers and principal engineers:

| Use-case idea | DDD mapping |
|---------------|-------------|
| **Actor + goal** | Often implemented by an **Application Service** (or a command handler) in one bounded context. One use case ≈ one or a few application services. |
| **Nouns** (e.g. Order, Claim, Policy) | Feed **ubiquitous language** and become **entities**, **value objects**, or **aggregate roots**. |
| **Verbs** (e.g. Submit, Approve, Cancel) | Become **domain actions** (methods on aggregates/entities) or **Domain Services**. |
| **Outcome / postcondition** | Often expressed as **domain events** (e.g. `OrderPlaced`, `ClaimApproved`). |
| **Scenario steps** | Application Service orchestrates: load aggregate → call domain logic → persist → publish events. |

Use cases **sit on top of** the domain: they are the scenarios that application and domain services implement. They help discover entities, aggregates, and events; they don’t define the domain in isolation.

### 3.2 Value Streams

**Value streams** are end-to-end flows that deliver value (e.g. “Quote to Policy”, “Order to Cash”). They usually **span multiple bounded contexts**:

| Value-stream idea | DDD mapping |
|-------------------|-------------|
| **Value stream** | End-to-end flow; one value stream often spans several **bounded contexts**. |
| **Stages / steps** | Each stage is often owned by (or heavily touches) **one bounded context**. Handoffs between stages align with **context boundaries**. |
| **Handoffs** | Show up on the **context map**: upstream vs. downstream, anti-corruption layers, events, or APIs. |
| **Capabilities in a stage** | Implemented inside a bounded context as aggregates, domain services, application services. |

Value streams are the “horizontal” flows; bounded contexts are the “vertical” slices of domain ownership. Value streams help decide **where** to draw context boundaries and **how** contexts integrate (context map).

**Picture:**

```
Value stream:  [Stage A] ——→ [Stage B] ——→ [Stage C]
                     │            │            │
Bounded contexts:  Context 1   Context 2   Context 3
                     │            │            │
Use cases:      UC1, UC2      UC3, UC4      UC5
                     │            │            │
Domain:         Aggregates,   Aggregates,   Aggregates,
                events,       events,       events,
                services      services      services
```

---

## 4. Domain Service vs Application Service (Critical for Developers)

### 4.1 Domain Service

- **Layer:** Domain.
- **Responsibility:** Holds **domain logic** that doesn’t naturally belong to a single entity or value object (e.g. logic involving multiple aggregates or a concept that isn’t “owned” by one thing).
- **Characteristics:**
  - Expressed in the **ubiquitous language** (e.g. `TransferMoneyService`, `PricingService`).
  - **Stateless**: operates on domain objects passed in (or data provided by the caller).
  - **Does not perform CRUD.** Does not hold references to Repositories. The **caller** (typically an Application Service) loads and saves via Repositories.
  - Depends only on **domain types** (entities, value objects, other domain services).

### 4.2 Application Service

- **Layer:** Application (use-case / application layer).
- **Responsibility:** **Orchestrates** a use case: “load → call domain → persist → publish”.
- **Characteristics:**
  - **Thin**: no business rules; only flow.
  - Depends on **Repositories**, **Domain Services**, **aggregates**, and infrastructure (e.g. event bus, external APIs).
  - Handles **transactions**, **authorization**, **mapping** (DTOs ↔ domain).
  - Named after the use case (e.g. `PlaceOrderApplicationService`, `SubmitClaimHandler`).

### 4.3 Who Does CRUD?

- **Repositories** are responsible for **persistence** (load by id, save, and optionally delete) of aggregates. That is the “CRUD” for domain entities.
- **Domain Services** do **not** do CRUD. They receive already-loaded entities/aggregates from the Application Service and perform domain logic. The Application Service uses Repositories to load before calling the Domain Service and to save after.

### 4.4 Summary Table

| | Domain Service | Application Service |
|---|----------------|---------------------|
| **Layer** | Domain | Application |
| **Contains** | Domain logic | Orchestration only |
| **Knows about** | Entities, value objects, domain concepts | Repositories, transactions, infrastructure |
| **CRUD** | No | No (orchestrates Repository for load/save) |
| **Naming** | Domain concept (e.g. `TransferService`) | Use case / action (e.g. `TransferMoneyCommandHandler`) |

---

## 5. “Service” in DDD Is Not a Process Boundary

- **“Service” in DDD** (Domain Service, Application Service) is a **design boundary** — a role/responsibility in the code. It does **not** mean “one process” or “one deployable unit.”
- **One process** (e.g. one K8s Deployment/Pod, one monolith, one microservice) can contain:
  - Application Service(s),
  - Domain Service(s),
  - Repository(ies),
  all in the **same process**. The flow “Application Service → Repository (load) → Domain Service → Repository (save)” runs in that single process. If there is a single database, that can be **one local transaction**. No cross-process coordination is implied.
- **Transaction management** is typically **centralized at the Application Service**: one use case = one transaction boundary. Repository and Domain Service are transaction-unaware. The overhead of having three layers (Application Service, Domain Service, Repository) does **not** by itself add multiple transactions; complexity comes when you **span process boundaries** (e.g. two microservices, two databases).

**Important:** Do **not** confuse a **DDD Domain Service** (a class/component that holds domain logic) with a **microservice** (a deployable process). A single microservice (or K8s Deployment) can host many Domain Services and many Application Services inside one process.

---

## 6. How DDD Translates to K8s Deployments

- A **K8s Deployment** (or “microservice”) is a **process/deployment boundary**. It is a runtime unit: one or more pods running the same application.
- **DDD layers** (Application Service, Domain Service, Repository) are **logical layers inside that process**. One K8s Deployment can (and often does) contain:
  - Multiple Application Services (one per use case or command),
  - Multiple Domain Services,
  - Multiple Repositories,
  all in the **same process**, sharing the same transaction boundary when talking to one database.
- **Bounded contexts** may or may not align with deployments:
  - **Option A:** One bounded context = one K8s Deployment (common in microservice architectures).
  - **Option B:** Several bounded contexts in one Deployment (modular monolith).
  - The choice is driven by team boundaries, scalability, and deployment granularity — not by the DDD definitions of “Domain Service” or “Application Service.”

**Takeaway for developers:** A DDD **Domain Service** is **not** a microservice. It is a component inside a process. When you deploy (e.g. as a K8s Service), you are deploying a **process** that may contain many Domain Services and Application Services. Spreading a **single transaction** across process boundaries (e.g. across two K8s Deployments) is where distributed transaction complexity appears; keeping Domain Service + Application Service + Repository in one process keeps transactions local and simple.

---

## 7. Mapping Product Requirements to DDD (Practitioner Guide)

For **Developers** and **Principal Engineers** taking product requirements into implementation:

1. **From product/feature docs to bounded contexts**
   - Use **value streams** and **capabilities** to identify candidate bounded contexts. Stages and handoffs suggest context boundaries. Draw a **context map** (who integrates with whom, how).

2. **From use cases / user stories to application and domain**
   - **Use case** → implement with one or more **Application Services** (or command/query handlers) in the appropriate bounded context.
   - **Nouns** in the use case → **entities**, **value objects**, or **aggregate roots** in the ubiquitous language.
   - **Verbs** → **domain actions** on aggregates or **Domain Services**.
   - **Outcomes** → **domain events** and/or responses.

3. **From “we need to persist X”**
   - **Repository** per aggregate (or per aggregate root). Application Service uses Repositories for load/save; Domain Service does not.

4. **From “we need a new deployable (e.g. new K8s Service)”**
   - Decide based on **bounded context**, team ownership, and scalability — not because “we have a new Domain Service.” One Deployment can host many Domain Services.

5. **From “we need a transaction across multiple systems”**
   - That crosses **process boundaries**. Use sagas, outbox, or eventual consistency — and model the boundaries explicitly on the context map. DDD’s Domain Service vs Application Service split does not create this complexity; process boundaries do.

---

## 8. Summary

- **Domain** and **Ubiquitous Language** define the “what”; **Bounded Contexts** and **Context Map** define boundaries and integrations.
- **Use cases** map to **Application Services** and scenarios; **value streams** span **bounded contexts** and inform the context map.
- **Domain Service** = domain logic, no CRUD, no Repository references. **Application Service** = orchestration, uses Repositories, owns transaction boundary. **Repository** = persistence of aggregates.
- **“Service” in DDD** is a design role, not a process. One K8s Deployment (microservice) can contain many Domain Services and Application Services in one process; don’t confuse DDD Domain Service with microservice.
- **Product requirements** map to DDD by: value streams → context map and bounded contexts; use cases → application services and domain model (entities, aggregates, domain services, events); persistence → repositories used by application services.

This note aligns with standard DDD (Evans, Vernon) and with the Product Capability Management (PCMM) / meta-model use of Domain, Bounded Context, Value Streams, Domain Services, and Context Map.
