# 0062. Memory Writes via Signal Exchange

## Status

Accepted

## Date

2026-01-07

## Context

Hub Memory Services provides enterprise memory stores (episodic, semantic, procedural, preference) for Hub Applications and agents. The question arose: how should applications and agents write records to these memory stores?

Options included direct API access, SDK-mediated writes, or routing through an existing system component.

### Constraints

- Memory writes must be auditable and traceable
- Writes must be tied to Request context (for case binding)
- Applications should not be tightly coupled to storage implementation
- Async processing desirable to avoid impacting application latency
- Writes must be idempotent and deduplicated

### Requirements

- All memory writes must be attributable to a Request
- Write operations must be consistent across all Hub Applications
- Storage backend changes should not require application changes
- Write failures should not block application processing

## Decision

We will **route all enterprise memory writes through Signal Exchange**. Applications and agents attach memory records to REQUEST_UPDATE messages; Signal Exchange extracts, validates, enriches, and routes them to memory stores via Atropos topics.

### Key Points

- No Hub agent or application directly accesses memory store write APIs
- Applications add `memory_records` array to REQUEST_UPDATE payload
- Signal Exchange identifies memory records and routes by memory class
- Records are enriched with hub_metadata (tenant, workbench, scenario, request_id)
- Writes flow asynchronously via Atropos topics per memory store
- Memory Store Writer Service consumes and indexes in OpenSearch

## Alternatives Considered

### Alternative 1: Direct API Access

Applications call memory store REST APIs directly.

**Pros:**
- Simple, direct integration
- Lower latency (synchronous write)
- Applications have full control

**Cons:**
- Each application must implement authentication, validation, retry logic
- No centralized audit trail of writes
- Applications coupled to storage API changes
- Request context binding must be done by each application
- Synchronous writes impact application latency

**Why rejected:** Violates DRY principle; inconsistent implementations; audit complexity.

---

### Alternative 2: Memory SDK

Provide an SDK that applications use for memory operations.

**Pros:**
- Consistent client-side behavior
- SDK handles auth, validation, retry
- Can abstract storage changes

**Cons:**
- SDK must be maintained for each runtime (Python, Java, etc.)
- Still requires applications to explicitly call write operations
- Request context still manually provided
- Synchronous unless SDK implements async buffering

**Why rejected:** SDK solves some problems but still requires explicit calls and doesn't leverage existing message flow.

---

### Alternative 3: Sidecar/Agent Pattern

Deploy a sidecar that intercepts and captures memory records.

**Pros:**
- Application doesn't need to change
- Automatic capture

**Cons:**
- Complex deployment model
- Magic interception is hard to debug
- Doesn't work for all application types
- Sidecar must understand application semantics

**Why rejected:** Adds deployment complexity; magic behavior is hard to reason about.

---

## Consequences

### Positive

- **Centralized auditing**: All writes flow through Signal Exchange, logged
- **Request binding automatic**: Signal Exchange enriches with request context
- **Async processing**: Applications aren't blocked by storage latency
- **Consistent validation**: Schema validation happens once, centrally
- **Deduplication**: Signal Exchange handles idempotency
- **Storage agnostic**: Backend can change without application changes

### Negative

- **Eventual consistency**: Records available after async processing, not immediately
- **Indirect writes**: Debugging requires tracing through Signal Exchange
- **Atropos dependency**: Requires Atropos infrastructure

### Neutral

- Signal Exchange becomes the authoritative write path for memory
- Memory stores only accept writes from Signal Exchange (via Atropos)

## Implementation Notes

- Applications attach `memory_records` to REQUEST_UPDATE `update_payload`
- Signal Exchange parses `memory_records` and routes by `record_type`
- Each memory store has a dedicated Atropos topic
- Memory Store Writer Service validates, generates embeddings, and indexes
- Failed records go to dead-letter queue for investigation

## Related Decisions

- [ADR-0019: Signal Exchange Observer Pattern](./0019-signal-exchange-observer-pattern.md) — Observer notification model
- [ADR-0020: Request-Level Granularity](./0020-request-level-granularity.md) — Request as routing unit
- [ADR-0030: Workbench-Scoped Data Stores](./0030-workbench-scoped-data-stores.md) — Store scoping

## References

- [Signal Exchange - Memory Record Routing](../04-subsystems/signal-exchange/memory-record-routing.md)
- [Memory Services README](../04-subsystems/memory-services/README.md)

