# Anemic Domain

This section explains what an **anemic domain** is, why it is a common and slippery slope, and how to keep a **rich domain** so that behavior and invariants live in the right place. It gives stringent guidelines and a code-review checklist.

> **For junior developers.** It's easy to put all logic in "services" and leave entities as getters/setters—that's anemic. The rule: **behavior and rules live on the aggregate or entity** (e.g. `order.addLineItem(...)`), and the Application Service only **orchestrates** (load, call domain, save, publish). Use the **Code review checklist** at the end of this section before you submit your code.

---

## What is anemic domain?

An **anemic domain** is one where the domain objects (entities, value objects, aggregates) are little more than data holders: getters and setters (or equivalent), with no meaningful behavior or invariants. The logic that should belong to the domain lives elsewhere—typically in “services” or “managers” that operate on the data. The domain model is reduced to a data structure; the behavior is scattered and duplicated.

**Symptoms:**

- Entities and value objects have only getters/setters (or public fields) and no methods that enforce rules or express domain actions.
- “Domain” services or application services contain most of the business logic; they pull data from entities, compute, and push results back.
- Invariants (e.g. “order total must equal sum of line items”) are enforced only in service code or in validators that sit outside the aggregate, so the same rule can be bypassed or duplicated.
- The ubiquitous language is not reflected in behavior: you say “Order” but the behavior of placing an order or adding a line is not on `Order`; it is in a service that manipulates `Order` from the outside.

When the domain is anemic, the model does not protect its own consistency, and changes to business rules require hunting through many service classes instead of changing the aggregate or entity that owns the concept.

---

## Why it is a slippery slope

Frameworks and common practice often push toward anemic models:

- **Spring’s default style:** Controllers, services, DTOs, and entities with getters/setters are the norm. Many tutorials and samples show “entities” that are just data bags and “services” that do everything. Without an explicit commitment to a rich domain, teams slip into this pattern.
- **Getters and setters:** Once every field is exposed via get/set, callers can bypass any intended invariant. The aggregate no longer controls how it is changed; any code can set any value. Logic that should live inside the aggregate (e.g. “add line item and recalculate total”) is instead implemented in a service that gets the order, gets the lines, adds a line, sets the total, and saves—and the aggregate cannot enforce that the total is correct.
- **“Services do everything”:** When Domain Services or Application Services hold all the logic, the domain objects become passive. The line between “orchestration” (application) and “domain logic” (domain) blurs; domain logic migrates into application or infrastructure, and the domain atrophies.

The slope is slippery because each new feature can be implemented “the easy way” (add a setter, add logic in a service) without breaking existing code—until the domain is a shell and every change touches many layers. The guide’s approach (rich domain, behavior on aggregates, Domain Service only when the operation doesn’t fit one entity) is the antidote.

---

## Rich domain vs anemic: comparison

| Aspect | Anemic | Rich |
|--------|--------|------|
| **Entities/aggregates** | Data only; getters/setters. | Behaviour and invariants on the aggregate root and entities. |
| **Invariants** | Enforced in services or validators outside the aggregate. | Enforced inside the aggregate; no way to put the aggregate in an invalid state from outside. |
| **Domain actions** | “Add line item” = service gets order, gets lines, adds, sets total, saves. | “Add line item” = `order.addLineItem(...)`; aggregate updates its state and enforces rules. |
| **Domain Service** | Often the place where “all” logic lives. | Used only when an operation doesn’t naturally fit a single entity (e.g. cross-aggregate logic). |
| **Application Service** | Thick: loads, computes, validates, saves. | Thin: load, call domain (aggregate or domain service), save, publish. |

**Example (anemic):** `Order` has `getLines()`, `setTotal(Money total)`. A `PlaceOrderService` creates an order, gets lines from the command, sets lines, computes total in the service, sets total on the order, saves. The aggregate does not enforce that total equals sum of lines.

**Example (rich):** `Order` has `addLineItem(OrderLine line)` that updates the order’s lines and recalculates total inside the aggregate; total is not settable from outside. `PlaceOrderService` creates the order, calls `order.addLineItem(...)` for each line, saves. The invariant “total = sum of lines” is guaranteed by the aggregate.

---

## Where behavior belongs

- **Invariants:** Enforced in the **aggregate root**. The root ensures that any change to the aggregate leaves it in a valid state. No external code can set internal state in a way that violates invariants.
- **Domain actions (single aggregate):** Methods on the **aggregate root** or entity (e.g. `order.addLineItem(...)`, `order.cancel()`). The aggregate encapsulates how its state changes.
- **Domain actions (cross-aggregate or cross-entity):** When an operation doesn’t naturally fit a single entity (e.g. “transfer money between accounts”), use a **Domain Service** that takes the relevant aggregates or data as arguments. The Domain Service expresses the operation in the ubiquitous language; it does not hold references to Repositories.
- **Orchestration:** **Application Service** only: load, call domain (aggregate or domain service), persist, publish. No business rules in the application service.

---

## Stringent guidelines and forbidden patterns

- **Do not** expose setters for fields that represent invariants (e.g. order total). Prefer methods that express domain actions (e.g. `addLineItem`) and update internal state inside the aggregate.
- **Do not** put business logic in Application Services beyond “load → call domain → save → publish.” If you are computing totals, validating rules, or deciding outcomes in the application layer, move that logic into the domain (aggregate or Domain Service).
- **Do not** use Domain Services as a dumping ground for all logic. Use them only when the operation genuinely doesn’t fit a single entity (e.g. involves multiple aggregates or a concept that isn’t “owned” by one thing).
- **Do** keep aggregates and entities responsible for their own invariants. The aggregate root is the single entry point for changes; external code does not bypass it.
- **Do** name methods in the ubiquitous language (`order.place()`, `order.addLineItem(...)`, `pricingService.calculateTotal(...)`).

---

## Code review checklist for anemic-domain slip

- [ ] Do entities/aggregates have behavior (methods that change state and enforce rules), or only getters/setters?
- [ ] Are invariants enforced inside the aggregate (e.g. total = sum of lines), or only in validators or services?
- [ ] Does the Application Service only orchestrate (load, call domain, save, publish), or does it contain business logic?
- [ ] Are Domain Services used only for operations that don’t fit a single entity, or are they holding logic that belongs on an aggregate?
- [ ] Can the domain be unit-tested without Spring or infrastructure (only domain types)?

---

## Refactoring from anemic to rich

1. **Identify invariants:** What rules must always hold (e.g. order total = sum of line items)? Document them.
2. **Move behavior into the aggregate:** For each invariant, introduce methods on the aggregate root that perform the state change and enforce the invariant. Remove setters that allowed invalid state.
3. **Thin the Application Service:** Replace “get data, compute in service, set on entity” with “call aggregate method.” The application service becomes: load aggregate, call method(s), save, publish.
4. **Extract Domain Services only when needed:** If an operation involves multiple aggregates or doesn’t belong to one entity, extract it to a Domain Service that takes the necessary data or aggregates as arguments. Do not inject Repositories into Domain Services.
5. **Test the domain in isolation:** Unit-test aggregates and Domain Services with no Spring, no database. Verify invariants and behavior.

Progress incrementally: one aggregate at a time, one use case at a time. The goal is a domain that speaks in the ubiquitous language and protects its own consistency.
