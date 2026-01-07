# 0063. Memory Reads via Access Tools

## Status

Accepted

## Date

2026-01-07

## Context

Hub Memory Services provides enterprise memory stores that applications and agents need to query for precedents, case histories, patterns, and context. The question arose: how should applications and agents access memory for reads?

Unlike writes (which are standardized through Signal Exchange), reads are more varied — different use cases require different query patterns, result formats, and access controls.

### Constraints

- Read access must be authorized and auditable
- Different query patterns needed (semantic search, case lookup, structured filters)
- Results must be formatted appropriately for agent consumption
- Cross-workbench reads must be prevented (isolation)
- Read operations should be traced as part of agent observability

### Requirements

- Agents must be able to find similar past cases (precedent search)
- Agents must be able to retrieve full case history
- Agents must be able to query patterns and beliefs
- All reads must be logged for audit
- Authorization must be checked per invocation

## Decision

We will **expose memory reads through defined Memory Access Tools**. Agents and applications invoke tools (e.g., `memory.search_precedent`, `memory.get_case_history`) rather than calling raw APIs. Tools encapsulate authorization, query building, and result formatting.

### Key Points

- Memory reads are available only through predefined tools, not raw APIs
- Each tool is purpose-built for a specific query pattern
- Tools extract caller identity and validate permissions
- Results are formatted for agent consumption (not raw API responses)
- All tool invocations are logged as part of agent traces
- Tools automatically scope queries to caller's workbench

## Alternatives Considered

### Alternative 1: Direct Query API Access

Expose Memory Query API directly to applications and agents.

**Pros:**
- Maximum flexibility for callers
- No abstraction layer overhead
- Callers can craft any query

**Cons:**
- Each caller must implement authorization checks
- Query construction must be done by each caller
- Results in raw API format, not agent-friendly
- No consistent audit logging
- Harder to evolve API without breaking callers

**Why rejected:** Inconsistent authorization; poor agent ergonomics; audit complexity.

---

### Alternative 2: GraphQL API

Expose a GraphQL API for flexible querying.

**Pros:**
- Flexible query composition
- Callers get exactly the fields they need
- Standard tooling available

**Cons:**
- Still requires callers to construct queries
- Authorization harder to enforce at field level
- GraphQL complexity may be overkill
- Agent LLMs would need to generate GraphQL

**Why rejected:** Overkill for current use cases; agents work better with defined tools than query languages.

---

### Alternative 3: Read SDK (Parallel to Tools)

Provide both SDK methods and tools, SDK for programmatic access.

**Pros:**
- SDK for workflow applications
- Tools for agents
- Covers both use cases

**Cons:**
- Two interfaces to maintain
- Potential inconsistency between SDK and tools
- SDK users might bypass authorization

**Why rejected:** Tools can serve both agents and programmatic access; single interface is simpler.

---

## Consequences

### Positive

- **Consistent authorization**: Tools validate permissions on every invocation
- **Agent-friendly**: Results formatted for LLM consumption
- **Audit trail**: All tool invocations logged with parameters and results
- **Workbench isolation**: Tools automatically scope to caller's workbench
- **Evolvable**: Tool implementations can change without changing tool contracts
- **Discoverable**: Tools are documented in tool catalog

### Negative

- **Less flexible**: Callers limited to predefined tool capabilities
- **New tools needed**: New query patterns require new tool development
- **Indirection**: Debugging requires tracing through tool executor

### Neutral

- Tools become the standard way to access memory
- Memory Query API is internal; not exposed to applications

## Implementation Notes

- Tools available: `memory.search_precedent`, `memory.get_case_history`, `memory.query_decisions`, `memory.get_handoff_context`, `memory.search_patterns`, `memory.get_entity_beliefs`
- Tools invoke Memory Query Service internally
- Seer SDK provides tool wrappers for agent use
- Direct Tool Executor API available for non-Seer applications

## Related Decisions

- [ADR-0040: Direct Tool Dispatcher](./0040-direct-tool-dispatcher.md) — Tool execution model
- [ADR-0041: Standalone Tool Variation](./0041-standalone-tool-variation.md) — Tool variations
- [ADR-0042: Scenario as Tool Granularity](./0042-scenario-as-tool-granularity.md) — Tool scoping

## References

- [Memory Access Tools](../04-subsystems/memory-services/memory-access-tools.md)
- [Memory Query API](../04-subsystems/memory-services/memory-query-api.md)

