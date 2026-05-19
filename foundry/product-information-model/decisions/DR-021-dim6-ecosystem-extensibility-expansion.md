> **⚠ Amendment (DR-035, 2026-05-19):** Three elements of this record are superseded by DR-035:
> - **D6 amended:** `Client-Distributed` as a Deployment Topology axis on Dim 8 modules is superseded. Deployment Topology is now a Component Archetype concern in Dim 5. Dim 8 modules are classified by Functional Classification (12 System Types), not by Deployment Topology.
> - **Consequence #3 amended:** "Dim 8 archetype taxonomy's Deployment Topology axis is refined to explicitly include Client-Distributed" is superseded. Deployment Topology moves to Component Archetype (Dim 5).
> - **D4 amended:** "archetype classification" for Dim 6 modules now refers to Functional Classification, not HI/Programmatic/Reactive Module Archetype.
> See DR-035 for full rationale.

# DR-021: Dimension 6 Expansion — Ecosystem & Extensibility with Personas, Module Types, and Deliberate Extensibility

**Status:** Accepted
**Date:** 2026-02-15

---

## Context

Dimension 6 (Ecosystem & Extensibility) was underspecified — it captured Interface Type, Endpoint/Event Topic, and Payload Schema as lightweight structural entities, but lacked the strategic vocabulary to model extensibility as a deliberate product dimension. Key gaps:

1. **No persona entities** — developers and programmatic consumers (customer applications, partner systems) interact through Dim 6 surfaces with fundamentally different concerns than Dim 4 users, yet the model had no way to represent them.
2. **No module taxonomy** — different extensibility strategies (API surface, integration suite, plugin framework, client SDK) represent distinct product decisions with different design concerns, but the model treated them uniformly.
3. **No articulation of deliberate intent** — the model didn't distinguish "a module happens to have APIs" (incidental) from "we strategically design and maintain an external programmatic surface for this use case" (deliberate).
4. **Unclear structural relationship** — it was ambiguous whether Dim 6 entities are parallel to, or separate from, Dim 8 structural entities.

## Decisions

### D1: Developer Persona and Programmatic User Persona are first-class Dim 6 entities

**Developer Persona** represents the human building integrations (integration engineer, partner developer, internal developer using the platform). Their concerns — API ergonomics, documentation quality, SDK completeness, error clarity, backward compatibility — are categorically different from Dim 4 User Persona concerns (visual clarity, simplicity, delight).

**Programmatic User Persona** represents the application or system consuming the API at runtime (customer's ERP, partner's middleware, third-party app). These are non-human consumers with throughput needs, SLA dependencies, integration requirements, and error-handling expectations. They cannot be modeled as Dim 4 User Personas.

Dim 6 personas are not conflated with Dim 4 personas. The same human may appear in both dimensions — an Integration Engineer is a Dim 4 Persona when using the Developer Portal and a Dim 6 Developer Persona when writing integration code.

### D2: API Module is protocol-agnostic — defined by contract, not transport

An API Module encompasses all programmatic delivery mechanisms: REST, gRPC, batch/file (SFTP), event streams (Kafka), webhooks, GraphQL. These are transport variations within a single module, not separate module types. The module's identity is the use case it serves and the contract it commits to ("Create Payment," "payment.settled notification"), not the wire protocol.

### D3: Three Dim 6 module types as distinct strategic choices, with Integration Module as connector/adapter

Each type represents a deliberate, PDR-level product strategy decision:

| Module Type | Purpose | Key Design Concerns |
|---|---|---|
| API Module | Named, versioned, protocol-agnostic programmatic surface | Versioning, backward compatibility, rate limiting, auth, contract design |
| Extension Module | Framework enabling third parties to extend product behavior | Plugin API stability, sandboxing, permission model, marketplace governance |
| SDK/Library Module | Language-specific client providing idiomatic access | Language idioms, dependency management, auto-gen vs. hand-crafted, version tracking |

**Integration Module** is retained but with a sharpened definition: it is a **pre-built bridge between the product and a specific external system or system category** (e.g., "SAP Connector," "ERP Integration," "Salesforce Adapter"). It includes not just APIs but also data mappings, protocol translations, workflow adapters, and pre-built connectors. The distinction from API Module: API Module says "here's our programmatic interface"; Integration Module says "here's a ready-made bridge between us and your system." Design concerns: data format translation, protocol bridging, polling vs. push, conflict resolution, target-system-specific error handling. If a product doesn't ship connectors to specific external systems, it has API Modules but no Integration Modules — a valid product decision.

### D4: Dim 6 modules ARE Dim 8 modules

A Dim 6 module is structurally a Dim 8 module — it participates in the Product → Module → Capability → Feature hierarchy, has a bounded context, archetype classification, Dim 5 internals, and Build Track versioning. What makes it a Dim 6 module is:

- Its purpose is externally-facing extensibility, not internal product functionality.
- Its capabilities are often compositional — curating capabilities from other Dim 8 modules for a use-case-scoped surface.
- It carries Dim 6-specific concerns (Developer Personas, Programmatic Personas, API contracts, versioning commitments) that other modules don't carry.

This parallels how Dim 4 HI modules are Dim 8 modules that carry Dim 4-specific concerns.

### D5: Extensibility is deliberate product strategy, not incidental API exposure

A module may have internal APIs as a byproduct of distributed architecture. These are Dim 5/Dim 8 concerns. Dim 6 entities exist only when there is a deliberate strategy to make capabilities externally consumable for well-understood use cases. The distinction is demand-driven (ecosystem need) vs. supply-driven (architecture happenstance). Dim 6 modules are use-case-scoped and compositional — they present a curated, simplified surface to external consumers, abstracting away internal module boundaries.

### D6: Client-Distributed as a recognized deployment topology

SDK/Library Modules, mobile apps, PWAs, CLI tools, and embedded widgets are all modules built by the vendor but deployed/instantiated in the consumer's environment. They are structurally valid Dim 8 modules with Capabilities, Features, Dim 5 internals, and Build Track versioning. Their operational footprint (Dim 7) is lighter — CI/CD + distribution channel + version adoption tracking. The Deployment Topology axis is refined to recognize this pattern: Vendor-Hosted (Monolith/Distributed) vs. Client-Distributed.

### D7: Unified API Operation entity with five interaction patterns

Rather than separate "Endpoint" and "Event" entities, a single **API Operation** entity is classified by interaction pattern: Command, Query, Event, Callback, Batch. Both endpoints and events are named, versioned, contractual commitments belonging to an API Module, consumed by the same personas, subject to the same compatibility contract. The transport mechanism (REST, Kafka, SFTP) blurs the boundary — a Kafka-submitted command and a REST-submitted command are the same operation via different transport. Each pattern carries distinct SLOs:

| Pattern | Direction | SLO Focus |
|---|---|---|
| Command | Consumer → Product | Latency, availability, throughput |
| Query | Consumer → Product | Latency, availability, throughput |
| Event | Product → Consumer | Delivery guarantee, delivery latency, ordering |
| Callback | Product → Consumer | Delivery guarantee, delivery latency |
| Batch | Bidirectional | Processing window, throughput, completeness |

This parallels existing model patterns: Win Case has subtypes (Query, Service Request, Complaint, Escalation); Signal has subtypes (Problem, Need, Opportunity).

### D8: SLOs as structured fields on API Operations

SLOs are the Dim 6 analog of experience attributes in Dim 4 — strategic commitments about quality of service for programmatic consumers. They declare what the product commits to (p99 latency, availability, delivery guarantees) without prescribing implementation. SLOs connect to Customer Promise (Dim 3) via SLAs, API Compatibility Contract (performance stability across versions), Programmatic User Persona (SLO-driven integration decisions), and Win Monitoring (SLO compliance tracking). SLO fields vary by operation pattern — commands/queries carry latency/availability/throughput targets; events/callbacks carry delivery guarantee/latency/ordering; batch carries processing window/throughput/completeness.

### D9: Payload Schema and Interface Type demoted from entity status

**Payload Schema** (specific request/response field definitions) follows the same granularity pattern as Touchpoints in Dim 4 — too granular for the Definition Model, belongs in PSD and Build Track artifacts. The API Operation declares "has a defined contract"; the specific schema lives below the waterline.

**Interface Type** (REST, gRPC, Webhook, etc.) is subsumed by the protocol-agnostic API Module. It becomes a field on the module ("Supported Protocols") rather than a standalone entity.

## Rationale

- **Dim 6 vs. Dim 4 separation:** Developer and programmatic consumers interact through fundamentally different surfaces with different quality criteria, lifecycle patterns, and stakeholders. Conflating them with Dim 4 personas would misrepresent both dimensions.
- **Protocol-agnostic API Module:** REST, batch/SFTP, Kafka events, webhooks, gRPC, and GraphQL are transport variations, not separate module types. The contractual surface ("Create Payment") is what matters; how it's delivered is an implementation characteristic. This eliminates the original overlap between API Module and Integration Module as "two kinds of API surface."
- **Module type taxonomy:** API, Extension, and SDK represent genuinely different product decisions with different architectural concerns, governance models, and lifecycle patterns. Integration Module is retained with a sharpened definition as connector/adapter (pre-built bridge to specific external systems), making it genuinely distinct from API Module. A single "API Product" entity would collapse these distinctions.
- **Structural unity with Dim 8:** Treating Dim 6 modules as separate from Dim 8 would create a parallel hierarchy, duplicate relationship management, and obscure the compositional relationship between Dim 6 surfaces and underlying Dim 8 capabilities.
- **Deliberate intent:** Without the deliberate/incidental distinction, every module with an API would appear in Dim 6, flooding the dimension with implementation detail and obscuring genuine strategic extensibility decisions.
- **Client-Distributed:** The existing Deployment Topology axis implicitly assumed vendor-side hosting. Mobile apps and web clients had already been modeled as modules without acknowledging this. Making the pattern explicit accommodates SDKs naturally and removes ambiguity.

## Consequences

1. Dim 6 gains 8 entities: Developer Persona, Programmatic User Persona, API Module, Integration Module, Extension Module, SDK/Library Module, API Operation (with 5 interaction patterns and SLOs), API Compatibility Contract.
2. Dim 6 loses 3 original entities: Interface Type (demoted to field), Endpoint/Event Topic (replaced by unified API Operation), Payload Schema (demoted to PSD/Build artifact).
3. Dim 8 archetype taxonomy's Deployment Topology axis is refined to explicitly include `Client-Distributed`.
4. Dim 6 module entities carry cross-references to the Dim 8 modules whose capabilities they compose.
5. PSD templates for Programmatic-Interactive modules will need Dim 6-specific sections (Developer Persona, Programmatic Persona, API Operations, SLOs, Versioning Strategy).
6. Discovery Track gains Dim 6-flavored work: researching developer needs, deliberating on API design, prototyping SDK ergonomics, modeling Integration Module scope.
7. Win Track gains ecosystem-oriented engagement: developer community, partner enablement, API adoption reviews.
8. API Operation SLOs connect to Customer Promise (Dim 3) SLAs, Win Monitoring, and Dim 7 operational alerting.

---
