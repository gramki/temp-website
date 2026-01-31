# One App per Domain or Subdomain

This section clarifies the relationship between **subdomain**, **bounded context**, and **deployment unit**, and gives criteria for deciding “one app per X” so you avoid both nanoservices and a single monolith.

---

## Subdomain vs bounded context

A **subdomain** is a part of the larger domain—a coherent area of the business (e.g. underwriting, claims, payments). Subdomains are often classified as **core** (critical to the business, invest here), **supporting** (needed but not differentiators), or **generic** (could be bought or shared).

A **bounded context** is an explicit boundary within which a particular **model** and its **ubiquitous language** apply. It is a design boundary: what we build and how we talk about it. A bounded context often aligns with a subdomain, but the mapping is not one-to-one. One subdomain might be split into several bounded contexts if the models and language diverge; conversely, several related subdomains might be modeled in one bounded context if the team and consistency boundary are shared.

For this guide, **one Spring Boot application owns one bounded context** (one domain or subdomain as expressed in that context’s model). The context map is the source of truth for what that boundary is and how it relates to others.

---

## Context map as source of truth

The **context map** describes how bounded contexts relate: who depends on whom, and how they integrate (APIs, events, anti-corruption layers). Use it to define:

- **Ownership:** Which team or system owns which bounded context. Ownership informs who can change the model and the deployment.
- **Consistency boundary:** What is updated in a single transaction or within one process. What crosses process boundaries uses eventual consistency (sagas, outbox, events).
- **Deployment unit:** What is deployed together. In this guide, one bounded context = one deployment unit (one Spring Boot application, e.g. one Kubernetes Deployment). The context map, together with ownership and consistency, drives that decision.

Keep the context map explicit and up to date. When in doubt about a boundary, the context map (and the ubiquitous language inside each context) should resolve it.

---

## Criteria for “one app per X”

Use the following to decide what “X” is—what one application (one deployment unit) should own:

- **One bounded context per application.** The application’s model and ubiquitous language are those of a single bounded context. If you find two models or two languages in one codebase, consider splitting by bounded context.
- **Ownership:** The same team (or clear ownership) owns the context. If two teams own different parts of the same deployment, boundaries tend to blur; consider aligning deployment with ownership.
- **Consistency:** Data that must be consistent in one transaction lives in one context (one database, one process). Data that can be eventually consistent can cross context boundaries (events, sagas).
- **Scalability and deployment:** If one part of the context must scale or deploy independently, that can motivate splitting the context—but only after the model and ownership are clear. Do not split solely for technology; split when the bounded context itself divides.

Stick to the rule once decided: one app per bounded context (as drawn on the context map). Governance (e.g. architecture review) can enforce that new “services” or features are placed in the right context and that new deployment units are justified by the context map.

---

## When not to split (avoiding nanoservices)

Do **not** split into a new application just because:

- You have a new **Domain Service** (a Domain Service is a design role inside a process, not a deployment unit).
- You have a new use case (use cases are implemented by Application Services in the same application).
- You want “microservices” per feature (features belong to a bounded context; the context is the unit of deployment).

Splitting too finely leads to nanoservices: many tiny deployments, each with little logic, leading to operational and coordination overhead, distributed transaction complexity, and unclear ownership. If the bounded context is small but coherent, keep it in one application until the context map clearly shows a new boundary (e.g. a new team, a new consistency boundary, or a new subdomain).

---

## When to split (avoiding a monolith)

Consider a new application (new bounded context) when:

- The **model** or **ubiquitous language** in one area diverges from the rest. Different language and different invariants suggest a new bounded context.
- **Ownership** is split: different teams own different parts of the same codebase and the boundaries are contentious.
- **Consistency** demands it: one part must be updated and deployed independently, or must scale separately, and the consistency boundary is different.
- The **context map** already shows a separate context (e.g. a partner or legacy system) that you are now implementing as a first-class context.

Split when the context map and the above criteria justify it—not by default. One application can host a large bounded context; the guide’s approach (domain, application, infrastructure in one process) scales within that context.

---

## Governance: sticking to the rule

To keep “one app per bounded context” from drifting:

- **Review the context map** when adding a new deployment unit or a new “service” (in the infrastructure sense). Require that the new unit corresponds to a bounded context on the map and that ownership and consistency are documented.
- **Do not create a new deployment** for a new Domain Service or Application Service; those are components inside an application.
- **Document the rationale** for each bounded context and its deployment unit so that future changes (e.g. merging or splitting) are informed by the same criteria.
