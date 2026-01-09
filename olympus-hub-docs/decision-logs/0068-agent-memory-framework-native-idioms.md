# ADR-0068: Agent Memory Framework-Native Idioms

> **Status**: Accepted  
> **Date**: 2026-01-08  
> **Category**: memory-services

---

## Context

Hub encourages "Raw Agents" to be built with any agentic framework (LangChain, LangGraph, Strands, CrewAI, AutoGen, etc.). Each framework has its own idiomatic approach to memory management. Hub's Agent Memory Services must work with all these frameworks without imposing conflicting patterns.

### Analysis Findings

Review of popular agentic frameworks revealed:

| Framework | Memory Idiom | ESPP Enforcement |
|-----------|--------------|------------------|
| LangChain | Memory as chain component | ❌ None |
| LangGraph | Memory as typed state | ❌ None |
| Semantic Kernel | Memory as skill/plugin | 🟡 Collections only |
| CrewAI | Memory as shared crew context | 🟡 Short/Long-term only |
| AutoGen | Memory as conversation + teachability | ❌ None |
| OpenAI Assistants | Memory as managed threads | ❌ None |
| AWS Strands | Memory as state + messages + session | 🟡 via AgentCore |

**Key Finding**: No framework enforces ESPP (Episodic-Semantic-Procedural-Preference) taxonomy. All allow memory type boundaries to blur.

### Options Considered

1. **Enforce ESPP**: Require all agent memory to be classified into ESPP categories
2. **Framework-Native**: Provide storage primitives that work with any framework's idioms
3. **Prescriptive SDK**: Provide Hub-specific SDK that abstracts framework differences

---

## Decision

**Agent Memory Services enable framework-native idioms without imposing Hub-specific patterns.**

### Principles

| Principle | Description |
|-----------|-------------|
| **Enable, Don't Prescribe** | Provide storage infrastructure without mandating methodology |
| **No Conflict** | Hub's storage layer does not clash with framework memory patterns |
| **Native Code** | Agent code should look natural for the chosen framework |
| **No Hub-isms** | Avoid Hub-specific patterns that don't exist in frameworks |

### Implementation

1. **ESPP Not Enforced**: Agent Memory does not require memory classification
2. **Generic Primitives**: Provide KV Store, Conversation, Log, Documents — not "Episodic Store" or "Semantic Store"
3. **Logical Store Names**: Developers organize memory with domain-relevant names (`"preferences"`, `"entities"`)
4. **Both SDK and Tools**: Support programmatic SDK and LLM-callable tools
5. **JSON Serialization**: Enforce data can be persisted/restored; don't enforce schema

---

## Consequences

### Positive

1. **Framework compatibility**: Works with any framework without code translation
2. **Developer productivity**: No learning curve for Hub-specific patterns
3. **Future-proof**: New frameworks will work without Hub changes
4. **Reduced friction**: Developers write idiomatic code for their framework

### Negative

1. **No cross-agent interoperability**: Different agents may organize memory differently
2. **Developer responsibility**: Developers must understand when to use Enterprise Memory
3. **No automatic entity extraction**: Left to frameworks (domain-specific)

### Neutral

1. ESPP remains available as conceptual guidance (not enforcement)
2. Enterprise Memory continues to enforce ESPP (different governance requirements)

---

## Contrast with Enterprise Memory

| Aspect | Enterprise Memory | Agent Memory |
|--------|-------------------|--------------|
| ESPP Taxonomy | Enforced | Optional |
| Memory Classification | Required | Developer-organized |
| Schema Validation | Full CAF compliance | JSON serialization only |
| Rationale | 7+ year retention, regulatory | Session-scoped, operational |

---

## Related Decisions

- [ADR-0067: Agent Memory Session Scope](./0067-agent-memory-session-scope.md) — Session lifecycle
- [ADR-0061: No PII in Episodic Memory](./0061-no-pii-in-episodic-memory.md) — Enterprise Memory constraints

---

## References

- [Agent Memory Design Rationale](../04-subsystems/memory-services/agent-memory/design-rationale.md)
- [Framework Reference](../04-subsystems/memory-services/agent-memory/framework-reference/README.md)
- [Framework Analysis](../04-subsystems/memory-services/agent-memory/framework-reference/analysis.md)
- [ESPP Taxonomy](../04-subsystems/memory-services/shared/espp-taxonomy.md) — Conceptual reference

