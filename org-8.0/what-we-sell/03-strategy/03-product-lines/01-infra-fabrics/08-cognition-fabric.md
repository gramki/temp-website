# Chapter 03.01.08: Cognition Fabric — Product Note

**An enterprise perception and interpretation layer — sensing what happens, understanding what it means, and delivering enriched signals to whatever needs to act — before thinking begins.**

---

## The Architectural Problem

Banks do not lack data. They lack perception. They lack the ability to sense what is happening across the enterprise, interpret what it means, and deliver that interpretation to wherever it matters — fast enough, rich enough, and governed enough to be trusted.

Over time, event handling fragments. Each system captures its own events in its own format. Integration pipelines translate between formats without preserving meaning. Interpretation logic is duplicated across dozens of consuming systems — each with its own rules for classifying, enriching, and routing. Nothing is authoritative. Nothing is reusable.

The consequences compound:

- **Sensing is scattered.** A transaction completes in one system, a session ends in another, a document arrives in a third — each captured in isolation, with no unified model of what constitutes an event, who produces it, or how it relates to other events. The enterprise has no nervous system; it has disconnected nerve endings.
- **Interpretation is duplicated.** Every system that needs to understand an event builds its own interpretation layer — its own entity extraction, its own classification rules, its own context enrichment. The same transaction is interpreted ten different ways by ten different consumers. Inconsistency is guaranteed; maintenance is multiplied.
- **Schema governance is absent.** Event definitions drift. The same event type means different things in different systems, different vintages, different teams. There is no authoritative definition of what fields an event contains, what values are valid, or how the schema evolves. Breaking changes propagate silently until something fails in production.
- **Event lineage is invisible.** When an alert fires or an insight surfaces, there is no reliable way to trace it back to the raw events that produced it. Derived events are detached from their sources. Audit and debugging require archaeology.
- **AI cannot perceive without an event substrate.** Every AI deployment that needs to sense and interpret — fraud detection, customer intent recognition, anomaly detection — must build its own event ingestion, its own interpretation logic, its own feature pipelines. There is no shared perception layer for AI to plug into. Each initiative starts from scratch.
- **Speed and meaning are in tension.** Real-time pipelines sacrifice semantic richness for latency. Batch pipelines sacrifice latency for completeness. There is no unified architecture that delivers both — fast enough for operational response, rich enough for intelligent interpretation.

The result: the bank's data flows but doesn't perceive. Events move through the enterprise without carrying their meaning. Every consumer must reconstruct interpretation from scratch — or worse, invent it inconsistently.

---

## Why Cognition Is Distinct from Thinking

To understand what Cognition Fabric is — and is not — requires a distinction that enterprise architecture rarely makes explicit: the difference between cognition and thinking.

### The Cognitive Architecture

Human cognition operates through a well-documented dual-process architecture:

| System | Character | Function |
|---|---|---|
| **System 1** | Fast, automatic, continuous, effortless | Perception and interpretation — sensing patterns, recognizing meaning, forming impressions. Operates without explicit goals; runs constantly in the background |
| **System 2** | Slow, deliberate, effortful, goal-directed | Thinking and deciding — weighing alternatives, making judgments, selecting actions. Engages only when needed; requires attention and energy |

Daniel Kahneman's framework, now foundational in cognitive science, maps directly to enterprise information architecture:

- **System 1 is cognition:** Perception (P) + Interpretation (I). What happened? What does it mean?
- **System 2 is thinking:** Decision (D) + Action (A). What should we do about it?

### Why This Matters for Enterprise Architecture

Most enterprise architectures fuse these two systems together. A fraud detection system both interprets transaction patterns (cognition) and decides whether to block transactions (thinking). A customer analytics platform both enriches customer profiles (cognition) and recommends next-best-actions (thinking). The sensing and the acting are welded into single systems.

This fusion creates three problems:

1. **Interpretation cannot be shared.** When interpretation is locked inside decision systems, other systems that need the same interpretation must duplicate the work. The fraud system's understanding of transaction velocity cannot be reused by the credit system, even though both need it.

2. **Governance is confused.** Governing a perception layer (is this interpretation accurate?) is different from governing a decision layer (is this action appropriate?). When they are fused, accountability is unclear — is a bad outcome due to misperception or bad judgment?

3. **Evolution is constrained.** Changing how the enterprise perceives (new event sources, better interpretation models) becomes entangled with changing how it decides (new policies, different thresholds). Neither can evolve independently.

### The Architectural Separation

Cognition Fabric implements the clean separation:

| Layer | Scope | Output | Character |
|---|---|---|---|
| **Cognition Fabric** | Perception + Interpretation | Enriched events (event + derived attributes + confidence) | Continuous, reactive, pattern-matching. Events flow in → interpretation flows out. Can run without explicit goals |
| **Agent / Evolution Fabric** | Decision + Action | Decisions and actions | Deliberative, goal-directed, effortful. Requires weighing alternatives, selecting among options |

**The test is simple:**
- If the output is an enriched event — the original event plus derived attributes plus confidence scores — it belongs to Cognition Fabric.
- If the output is a decision — what to do about it, which action to take, whether to proceed — it belongs to Agent Fabric or Evolution Fabric.

An event arrives: "Customer transferred $50,000 to a new payee." Cognition Fabric enriches it: first-time payee, high-value relative to history, timing unusual, confidence-of-anomaly: 0.87, customer segment: high-net-worth, velocity-pattern: spike. This is perception and interpretation — no decision has been made.

Agent Fabric or Evolution Fabric receives the enriched event and decides: block the transaction, request confirmation, escalate to human review, or let it proceed. This is thinking — weighing alternatives against policy, risk appetite, and customer context.

The separation is not just conceptual. It is architectural. Cognition Fabric is the enterprise's nervous system — sensing and interpreting. Agent Fabric and Evolution Fabric are its executive function — deciding and acting.

---

## What Cognition Fabric Is

Cognition Fabric is the enterprise perception and interpretation layer — a unified substrate for sensing events, understanding what they mean, and delivering enriched signals to whatever systems, agents, or humans need to act.

Rather than leaving each system to build its own event ingestion, its own interpretation logic, and its own schema management, Cognition Fabric provides a shared architectural surface where:

- Events are **sourced** from across the enterprise — pushed, pulled, or scheduled — through a unified ingestion model.
- Events are **interpreted** through shared services — classification, entity extraction, context enrichment — that produce consistent meaning regardless of consumer.
- Interpretation is **governed** by authoritative schema definitions, with lifecycle management, breaking-change controls, and registry visibility.
- Derived events are **traceable** to their sources — lineage is structural, not reconstructed.
- Enriched signals are **routed** to subscribers based on declared interest — humans, systems, AI agents — without point-to-point integration.
- The perception layer is **continuous** — it operates whether or not any decision-maker is paying attention, accumulating interpreted state that decision systems can query when they need it.

Cognition Fabric does not decide. It does not act. It perceives and interprets — providing the foundation on which thinking systems operate.

---

## Capability Domains

### 1. Event Sourcing

A unified ingestion model for events from across the enterprise — regardless of source system, protocol, or timing.

| Capability | What It Delivers |
|---|---|
| Push ingestion | Real-time event reception from systems that emit events as they occur — webhooks, message queues, change data capture, streaming APIs |
| Pull ingestion | Scheduled or on-demand extraction from systems that don't push — polling APIs, database queries, file drops, legacy batch exports |
| Scheduled extraction | Time-triggered event collection for systems that produce events on cycles — end-of-day reconciliation, periodic snapshots, regulatory reporting windows |
| Source registry | Catalog of all event sources — system, protocol, frequency, reliability, latency characteristics — with ownership and health monitoring |
| Ingestion contracts | Declared expectations for each source: event types, schemas, delivery guarantees, retry policies. Contract violations are detected and surfaced |
| Deduplication and ordering | Event-level idempotency and sequence management — ensuring that duplicates don't pollute the event stream and ordering is preserved where it matters |

Event sourcing is the sensory surface — the point where the enterprise's activity becomes visible to the perception layer.

### 2. Event Derivation

Creating new events from existing events — enrichment, aggregation, pattern detection, and complex event processing.

| Capability | What It Delivers |
|---|---|
| Event enrichment | Augmenting raw events with context from reference data, historical patterns, and external sources — transforming a bare transaction into a contextually rich signal |
| Event aggregation | Combining multiple events into summary events — session summaries, daily totals, cohort rollups — at configurable granularity and timing |
| Pattern detection | Recognizing sequences, correlations, and anomalies across event streams — velocity spikes, behavioral shifts, coordinated activity patterns |
| Complex event processing | Multi-stream reasoning over temporal windows — detecting composite conditions that span sources, time ranges, and entity relationships |
| Derived event lineage | Every derived event carries provenance — which source events contributed, which derivation rules applied, at what time. Lineage is structural, not reconstructed |
| Derivation versioning | Derivation logic is versioned. When rules change, historical events can be traced to the derivation version that produced them |

Event derivation is the interpretive function — turning raw perception into meaningful signals without crossing into decision-making.

### 3. Event Schema Governance

Authoritative definitions of what events mean — structure, semantics, lifecycle, and evolution.

| Capability | What It Delivers |
|---|---|
| Schema registry | Central repository of event schemas — field definitions, types, constraints, semantic annotations — with versioning and access control |
| Schema authoring | Tools for defining, validating, and documenting event schemas — with enforcement of organizational standards and naming conventions |
| Schema evolution | Governed change management for schemas — backward compatibility checks, deprecation workflows, migration guides, breaking-change alerts |
| Schema assertions | Declarative constraints on event validity — required fields, value ranges, referential integrity, business rule compliance — enforced at ingestion and derivation |
| Cross-schema relationships | Explicit modeling of how event types relate — parent-child, before-after, part-of, causes — enabling reasoning across the event graph |
| Schema lifecycle management | Full lifecycle from draft through active to deprecated to retired — with visibility into which consumers depend on which schema versions |

Schema governance is the semantic foundation — ensuring that "payment completed" means the same thing everywhere it appears.

### 4. Event Registry

A catalog of the enterprise's event landscape — what events exist, who produces them, who consumes them, and how they flow.

| Capability | What It Delivers |
|---|---|
| Event type catalog | Comprehensive inventory of event types across the enterprise — definitions, schemas, examples, ownership, classification |
| Producer registry | Which systems, services, and processes emit which event types — with volume metrics, reliability history, and contact information |
| Consumer registry | Which systems, services, agents, and humans subscribe to which event types — with usage patterns, latency requirements, and dependency mapping |
| Flow visualization | Visual representation of event flows across the enterprise — from source through derivation through routing to consumption |
| Impact analysis | Before changing a schema or retiring an event type, understand who will be affected — downstream consumers, dependent derivations, active subscriptions |
| Discovery and search | Self-service exploration of the event landscape — find events by keyword, domain, schema, producer, or semantic similarity |

The event registry makes the enterprise's perception layer visible and navigable — turning implicit data flows into explicit architecture.

### 5. Interpretation Services

Shared services for extracting meaning from events — classification, entity recognition, context enrichment — available to all consumers.

| Capability | What It Delivers |
|---|---|
| Event classification | Categorizing events by type, intent, risk level, urgency, domain — using rules, ML models, or hybrid approaches. Classification is consistent across all consumers |
| Entity extraction | Identifying and extracting entities from event payloads — customers, accounts, products, counterparties, locations — with confidence scores and disambiguation |
| Entity resolution | Linking extracted entities to canonical records — determining that "John Smith" in this event is customer ID 12345, not a different John Smith |
| Context enrichment | Augmenting events with contextual data — customer segment, relationship tenure, product holdings, recent interaction history — assembled from across the enterprise |
| Semantic annotation | Attaching semantic labels and confidence scores to events — "this looks like a dispute," "this pattern suggests churn risk," "anomaly confidence: 0.87" |
| Interpretation model registry | Catalog of interpretation models — classifiers, extractors, enrichers — with versioning, performance metrics, and governance |

Interpretation services are the shared understanding layer — ensuring that when multiple systems need to interpret the same event, they reach the same conclusions.

### 6. Signal Routing

Delivering interpreted events to subscribers — humans, systems, AI agents — based on declared interest rather than point-to-point integration.

| Capability | What It Delivers |
|---|---|
| Subscription management | Consumers declare interest in event types, domains, or patterns — with filtering criteria, delivery preferences, and quality-of-service requirements |
| Topic-based routing | Events are routed to topics; consumers subscribe to topics. New consumers get events immediately without source-system changes |
| Content-based routing | Events are routed based on payload content — high-value transactions to one subscriber, international transactions to another — with declarative routing rules |
| Delivery guarantees | Configurable delivery semantics — at-least-once, exactly-once, ordered delivery — matched to consumer requirements |
| Backpressure management | When consumers fall behind, the routing layer manages backpressure — buffering, rate limiting, or alerting — without losing events |
| Dead-letter handling | Events that cannot be delivered are captured, diagnosed, and made available for retry or manual intervention |

Signal routing is the distribution network — ensuring that interpreted events reach every system, agent, or human that needs them, without requiring each producer to know each consumer.

---

## Architectural Position

Cognition Fabric occupies a distinct position in the enterprise architecture — upstream of decision-making, downstream of raw systems:

| Layer | Cognition Fabric Role |
|---|---|
| **Perception Surface** | The boundary where enterprise activity becomes visible — events are captured from all sources, in all formats, at all frequencies |
| **Interpretation Layer** | The shared substrate where raw events are enriched with meaning — classification, entity extraction, context, confidence — before any consumer receives them |
| **Signal Distribution** | The routing network that delivers enriched events to subscribers — humans, systems, AI agents — based on declared interest |

Cognition Fabric does not replace event-driven architectures, streaming platforms, or data pipelines. It provides the semantic layer that makes them coherent — ensuring that events carry meaning, interpretation is shared, schemas are governed, and signals reach the right destinations.

---

## Relationship to Other Fabrics

Cognition Fabric provides perception and interpretation; other fabrics provide the decision-making and action layers that consume its signals:

| Fabric | Relationship |
|---|---|
| **Evolution Fabric** | Receives enriched events as triggers for Scenarios. When Cognition Fabric interprets an event as "dispute initiated," Evolution Fabric's Hub determines how the dispute is resolved. Perception feeds resolution |
| **Agent Fabric** | AI agents consume interpreted events as context for their reasoning. Cognition Fabric provides the sensory input; Agent Fabric governs how agents think and act on that input |
| **Memory Fabric** | Interpreted events feed into enterprise memory. Cognition Fabric provides the "what happened and what it meant" that Memory Fabric preserves for future recall, explanation, and audit |
| **Truth Fabric** | Interpretation services depend on Truth Fabric's semantic definitions. When Cognition Fabric classifies an event, it draws on authoritative definitions of what classifications mean |
| **Trust Fabric** | Event routing respects consent and access control. An interpreted event about a customer reaches only subscribers authorized to see that customer's data — enforced through Trust Fabric |

The fabrics form a complete cognitive architecture: Cognition Fabric perceives and interprets (System 1). Evolution Fabric and Agent Fabric decide and act (System 2). Memory Fabric remembers. Truth Fabric grounds meaning. Trust Fabric governs access.

---

## References

- [Evolution Fabric](04-evolution-fabric.md) — The operational layer for domain resolution
- [Agent Fabric](06-agent-fabric.md) — AI agent lifecycle, identity, and governance
- [Memory Fabric](07-memory-fabric.md) — Enterprise decision and institutional memory
- [Truth Fabric](02-truth-fabric.md) — Semantic grounding and authoritative definitions
- [Trust Fabric](01-trust-fabric.md) — Identity, consent, and access governance

> **Cognition Fabric is the enterprise's nervous system — sensing what happens, understanding what it means, and delivering that understanding to whatever needs to act.**
