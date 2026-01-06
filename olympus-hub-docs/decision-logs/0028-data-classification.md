# ADR-0028: Cognitive vs Operational vs Domain Data Classification

## Status

**Accepted**

## Date

2026-01-06

## Context

Hub Applications deal with diverse data types that have fundamentally different characteristics:
- Some data is about **what the enterprise knows and remembers** (cognitive)
- Some data is about **what is happening in the Hub** (operational)
- Some data is about **business entities managed by applications** (domain)

Mixing these data types leads to:
- Incorrect storage choices (storing decisions in relational databases instead of memory services)
- Lost audit trails and explainability
- Inappropriate lifecycle management

## Decision

Hub classifies data into **three categories** with distinct storage recommendations:

### 1. Cognitive Data
**Question answered**: *"What do we know, remember, and learn?"*

| Data Type | Storage | Description |
|-----------|---------|-------------|
| **Decisions, precedents** | Enterprise Memory (via CAF) | Institutional learning, audit trail |
| **Agent learning** | Agent Memory | Operational continuity within sessions |
| **User preferences** | User Memory | Personalization with decay |
| **Policies, SOPs, rules** | Knowledge Services | Curated, governed truth |

**Characteristics**:
- Captures rationale, not just facts
- Has temporal significance ("when did we learn this?")
- Requires decay and governance semantics
- Supports context assembly for future decisions

### 2. Operational Data
**Question answered**: *"What is happening in the Hub?"*

| Data Type | Storage | Description |
|-----------|---------|-------------|
| **Requests, Tasks** | Operations Data | Hub-managed lifecycle |
| **Activities, Actions** | Operations Data | Observable execution steps |
| **Signals, Sessions** | Operations Data | Incoming events, agent interactions |

**Characteristics**:
- Hub-managed lifecycle (active → completed → archived)
- Applications access through Hub APIs only
- High volume, high velocity
- Retention-managed

### 3. Domain Data
**Question answered**: *"What business entities does my application manage?"*

| Data Type | Storage | Description |
|-----------|---------|-------------|
| **Business entities with relationships** | Ganymede | Relational, transactional |
| **Entity state, caching** | Callisto | Fast key-value lookup |
| **Search, logs, analytics** | Europa | Full-text, aggregation |

**Characteristics**:
- Application-owned and directly accessed
- Domain-specific queries (SQL, key-value, full-text)
- Independent state machine and lifecycle
- Not cognitive (not about learning or memory)

## Classification Diagram

```
┌───────────────────────────────────────────────────────────────┐
│                    DATA CLASSIFICATION                         │
│                                                                │
│   ┌─────────────────────────────────────────────────────────┐ │
│   │              COGNITIVE DATA                              │ │
│   │   "What do we know, remember, and learn?"                │ │
│   │                                                          │ │
│   │      Memory Services      │      Knowledge Services      │ │
│   │   (Control Plane: CAF)    │                              │ │
│   └─────────────────────────────────────────────────────────┘ │
│                                                                │
│   ┌─────────────────────────────────────────────────────────┐ │
│   │              OPERATIONAL DATA                            │ │
│   │   "What is happening in the Hub?"                        │ │
│   │                                                          │ │
│   │   Requests │ Tasks │ Activities │ Actions │ Sessions     │ │
│   └─────────────────────────────────────────────────────────┘ │
│                                                                │
│   ┌─────────────────────────────────────────────────────────┐ │
│   │              DOMAIN DATA                                 │ │
│   │   "What business entities does my application manage?"   │ │
│   │                                                          │ │
│   │   Ganymede (Relational) │ Callisto (KV) │ Europa (Search)│ │
│   └─────────────────────────────────────────────────────────┘ │
└───────────────────────────────────────────────────────────────┘
```

## Decision Matrix

| Data Characteristic | Storage | Reason |
|---------------------|---------|--------|
| Authoritative enterprise facts | Knowledge Services | Asserted, governed truth |
| Decisions, outcomes, precedents | Enterprise Memory (via CAF) | Institutional learning and audit |
| Agent learning and preferences | Agent Memory | Operational continuity |
| User preferences and personalization | User Memory | Subject-specific adaptation |
| Hub operational data | Operations Data | Hub-managed lifecycle |
| Business domain entities | Application Data Stores | Application-specific, domain logic |

## Anti-Patterns to Avoid

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| Storing decisions in Ganymede | Bypasses Enterprise Memory, loses auditability | Use Enterprise Memory (via CAF) |
| Using Callisto for user preferences | Loses decay/governance semantics | Use User Memory |
| Treating Knowledge as Memory | Policies become exceptions | Separate curated knowledge from learned experience |
| Treating Memory as Knowledge | One-off decisions become policy | Require explicit promotion path |
| Direct access to Operations Data | Bypasses Hub lifecycle management | Use Hub APIs for requests/tasks |

## Alternatives Considered

### Alternative 1: No Classification (Developer Choice)
Let developers decide storage without guidance.

- **Pros**: Maximum flexibility
- **Cons**: Inconsistent choices, lost audit trails, incorrect lifecycle

### Alternative 2: Two Categories (Hot/Cold)
Classify by access pattern only.

- **Pros**: Simple
- **Cons**: Ignores semantic differences, mixes cognitive and operational

## Consequences

### Positive
- **Clear Guidance**: Developers know where to store each data type
- **Proper Audit**: Decisions go to Enterprise Memory, not lost in relational tables
- **Correct Lifecycle**: Each data type gets appropriate retention and governance
- **Semantic Integrity**: Cognitive data maintains its learning semantics

### Negative
- **Classification Effort**: Developers must classify their data
- **Multiple Stores**: May need to use multiple storage types for one application
- **Learning Curve**: Must understand cognitive vs operational vs domain distinction

### Neutral
- Classification applies at design time, not runtime
- Some data appears in multiple categories (decision recorded in both Enterprise Memory and Operations Data)

## Related Decisions

- [ADR-0027: Four-Layer Storage Model](./0027-four-layer-storage-model.md)
- [ADR-0029: CAF as Control Plane Not Storage](./0029-caf-control-plane.md)

