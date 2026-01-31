# Mapping Product to DDD

This section explains how product requirements—use cases and value streams—map to DDD concepts. It gives a practitioner path from product or feature docs to bounded contexts, application services, and the domain model.

> **New to DDD?** When you get a user story or use case, use the tables below: **nouns** (Order, Claim, etc.) become entities or aggregate roots; **verbs** (Submit, Approve) become methods on aggregates or Domain Services; the **flow** is implemented by an Application Service that loads, calls domain, saves, and publishes events. If you're unsure which bounded context owns the story, ask your tech lead or Principal Engineer—see [04 One app per domain](04-one-app-per-domain.md).

---

## Use cases and the domain

**Use cases** describe who does what with the system and why (actor + goal + scenario). They sit on top of the domain: they are the scenarios that application and domain services implement. They help discover entities, aggregates, and events; they do not define the domain in isolation.

| Use-case idea | DDD mapping |
|---------------|-------------|
| **Actor + goal** | Often implemented by an **Application Service** (or a command handler) in one bounded context. One use case ≈ one or a few application services. |
| **Nouns** (e.g. Order, Claim, Policy) | Feed the **ubiquitous language** and become **entities**, **value objects**, or **aggregate roots**. |
| **Verbs** (e.g. Submit, Approve, Cancel) | Become **domain actions** (methods on aggregates or entities) or **Domain Services**. |
| **Outcome / postcondition** | Often expressed as **domain events** (e.g. `OrderPlaced`, `ClaimApproved`). |
| **Scenario steps** | Application Service orchestrates: load aggregate → call domain logic → persist → publish events. |

Use cases are refined through dialogue with domain experts; the nouns and verbs that emerge become the ubiquitous language and the building blocks defined in [DDD concepts](02-ddd-concepts.md).

---

## Value streams and bounded contexts

**Value streams** are end-to-end flows that deliver value (e.g. “Quote to Policy”, “Order to Cash”). They usually **span multiple bounded contexts**. Value streams are the “horizontal” flows; bounded contexts are the “vertical” slices of domain ownership. Value streams help decide **where** to draw context boundaries and **how** contexts integrate (context map).

| Value-stream idea | DDD mapping |
|-------------------|-------------|
| **Value stream** | End-to-end flow; one value stream often spans several **bounded contexts**. |
| **Stages / steps** | Each stage is often owned by (or heavily touches) **one bounded context**. Handoffs between stages align with **context boundaries**. |
| **Handoffs** | Show up on the **context map**: upstream vs. downstream, anti-corruption layers, events, or APIs. |
| **Capabilities in a stage** | Implemented inside a bounded context as aggregates, domain services, application services. |

The following picture summarises the relationship:

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

## Practitioner checklist: product requirements to DDD

For developers and principal engineers taking product requirements into implementation:

1. **From product/feature docs to bounded contexts**
   - Use **value streams** and **capabilities** to identify candidate bounded contexts. Stages and handoffs suggest context boundaries. Draw a **context map** (who integrates with whom, how). See [One app per domain](04-one-app-per-domain.md) for how the context map informs ownership, consistency boundary, and deployment unit.

2. **From use cases / user stories to application and domain**
   - **Use case** → implement with one or more **Application Services** (or command/query handlers) in the appropriate bounded context.
   - **Nouns** in the use case → **entities**, **value objects**, or **aggregate roots** in the ubiquitous language.
   - **Verbs** → **domain actions** on aggregates or **Domain Services**.
   - **Outcomes** → **domain events** and/or responses.

3. **From “we need to persist X”**
   - **Repository** per aggregate (or per aggregate root). Application Service uses Repositories for load/save; Domain Service does not (as defined in [DDD concepts](02-ddd-concepts.md)).

4. **From “we need a new deployable (e.g. new Kubernetes Service)”**
   - Decide based on **bounded context**, team ownership, and scalability—not because “we have a new Domain Service.” One deployment can host many Domain Services. See [One app per domain](04-one-app-per-domain.md) and [Spring Boot mapping](05-spring-boot-mapping.md).

5. **From “we need a transaction across multiple systems”**
   - That crosses **process boundaries**. Use sagas, outbox, or eventual consistency—and model the boundaries explicitly on the context map. The Domain Service vs Application Service split does not create this complexity; process boundaries do. See [Risks and mitigations](07-risks-and-mitigations.md).
