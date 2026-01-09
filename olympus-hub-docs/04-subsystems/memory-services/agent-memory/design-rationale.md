# Agent Memory Design Rationale

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-08  
> **Parent**: [Agent Memory Services](./README.md)

---

## Overview

This document explains the design decisions behind Hub's Agent Memory Services, mapping industry framework patterns to Hub's approach and articulating trade-offs for recommendations not adopted.

---

## Table of Contents

1. [Design Philosophy](#design-philosophy)
2. [Framework Analysis Reference](#framework-analysis-reference)
3. [Recommendation Analysis](#recommendation-analysis)
4. [Trade-off Summary](#trade-off-summary)
5. [Future Considerations](#future-considerations)

---

## Design Philosophy

Hub's approach to Agent Memory is guided by four core principles:

### 1. Enable, Don't Prescribe

The agentic AI landscape is nascent. Standards and best practices are still emerging. Hub provides **infrastructure** (storage, isolation, encryption) without mandating **methodology** (memory algorithms, learning patterns).

### 2. Framework-Native Idiom Preservation

Hub's Agent Memory is designed to let agents be written in their development framework's **native and idiomatic style**:

| Principle | Description |
|-----------|-------------|
| **No Conflict** | Hub's storage layer does not clash with framework memory patterns |
| **Native Code** | Agent code should look natural for the chosen framework |
| **No Hub-isms** | Avoid Hub-specific patterns that don't exist in frameworks |
| **Maximally Enabling** | Provide infrastructure that works with any idiom |

**Why This Matters**:

Most agentic frameworks do not classify memory into ESPP (Episodic-Semantic-Procedural-Preference) taxonomy. They allow memory type boundaries to blur — treating all memory as operational state with different access patterns.

> **Key Finding**: No analyzed framework enforces ESPP taxonomy. See [Framework Analysis](./framework-reference/analysis.md#framework-idiom-summary) for detailed per-framework evidence.

**Hub's Response**: Agent Memory provides storage primitives (KV, Conversation, Log, Documents) without imposing memory type classification. Developers organize memory using their framework's natural patterns. Logical store names provide optional organization without enforcement.

### 3. Clear Boundary with Enterprise Memory

Agent Memory and Enterprise Memory serve different purposes with different governance requirements. Conflating them creates compliance risk. Hub enforces this boundary architecturally.

| Aspect | Agent Memory | Enterprise Memory |
|--------|--------------|-------------------|
| ESPP Taxonomy | Optional (developer-organized) | Enforced (CAF compliance) |
| Governance | Minimal | Full |
| Rationale | Session-scoped; no audit need | 7+ years; cross-agent; regulated |

### 4. Framework Agnosticism

Raw Agents can be built with any framework. Hub's Agent Memory must work with LangChain, LangGraph, Strands, custom implementations, and frameworks not yet invented.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│   Agent Developer's Framework                                                │
│   (LangChain, LangGraph, Strands, CrewAI, custom, etc.)                     │
│                                                                              │
│       │                                                                      │
│       │  Use framework's native memory patterns                             │
│       ▼                                                                      │
│                                                                              │
│   Hub Agent Memory Services                                                  │
│   (Storage primitives — no methodology imposed)                             │
│                                                                              │
│       │                                                                      │
│       │  Provides: persistence, isolation, encryption                       │
│       │  Does NOT provide: memory classification, learning algorithms       │
│       ▼                                                                      │
│                                                                              │
│   Durable, Isolated, Encrypted, Session-Scoped Storage                       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Framework Analysis Reference

Hub's Agent Memory design is informed by analysis of how popular agentic frameworks implement memory. See:

- **[Framework Reference Summary](./framework-reference/README.md)** — Key patterns and Hub's response
- **[Detailed Analysis](./framework-reference/analysis.md)** — Per-framework analysis with techniques and observations

**Key Insight from Analysis**: No framework enforces ESPP taxonomy. All allow memory type boundaries to blur. Hub follows this pattern — enabling framework-native idioms without imposing Hub-specific semantics.

---

## Recommendation Analysis

### ✅ Adopted: Typed Session State

**Recommendation**: Like LangGraph and Strands, support typed state with explicit schema and JSON serialization.

**Hub's Approach**:
- All values in KV Store, Conversation, and Log services must be **JSON-serializable**
- Validation occurs at write time; non-serializable values are rejected
- Store names follow strict ASCII pattern `(a-zA-Z_-)+`

**What We Adopted**:
| Aspect | Adopted |
|--------|---------|
| JSON serialization requirement | ✅ Yes |
| Write-time validation | ✅ Yes |
| Structured storage (KV, Conversation, Log, Documents) | ✅ Yes |

**What We Did NOT Adopt**:
| Aspect | Not Adopted | Rationale |
|--------|-------------|-----------|
| Enforced typed schemas | ❌ | Left to frameworks — Hub doesn't know what entities agents will track |
| State reducers/mergers | ❌ | Framework-specific concern — how agents merge state is their design |
| Schema registry | ❌ | Over-prescription — adds complexity without clear benefit for ephemeral data |

**Trade-off**: Hub ensures data can be persisted and restored (JSON), but doesn't enforce what that data looks like. This maximizes framework flexibility at the cost of cross-agent interoperability (which we don't want anyway due to isolation).

---

### ✅ Adopted: Memory Access Tools

**Recommendation**: Like Semantic Kernel, make memory operations observable as callable tools.

**Hub's Approach**:
- All four storage services expose **save** and **recall** operations as tools
- Tools are available to all agents (LLM-based and programmatic)
- Tool invocations are observable in agent traces

**What We Adopted**:
| Aspect | Adopted |
|--------|---------|
| Memory as callable tools | ✅ Yes |
| SDK access for programmatic use | ✅ Yes |
| Observable operations | ✅ Yes (traced) |

**What We Did NOT Adopt**:
| Aspect | Not Adopted | Rationale |
|--------|-------------|-----------|
| Memory operations in request history | ❌ | Agent memory is agent-private; no conflation with Enterprise Memory |
| Audit trail of memory access | ❌ | Session-scoped data doesn't require long-term audit |

**Trade-off**: Memory operations are observable within agent traces but not reported to Request updates. This maintains the Enterprise/Agent memory boundary while still providing debugging capability.

---

### 🟡 Partially Adopted: Entity Tracking

**Recommendation**: Automatic extraction of entities with cross-turn persistence.

**Hub's Approach**:
- Hub provides **KV Store** as infrastructure for entity storage
- Logical store names support domain organization (`"customer"`, `"merchant"`, etc.)
- **Automatic extraction is left to frameworks**

**What We Adopted**:
| Aspect | Adopted |
|--------|---------|
| Entity storage infrastructure | ✅ Yes (KV Store) |
| Logical store names for organization | ✅ Yes |
| Cross-turn persistence within session | ✅ Yes |

**What We Did NOT Adopt**:
| Aspect | Not Adopted | Rationale |
|--------|-------------|-----------|
| Automatic entity extraction | ❌ | See below |
| Entity type registry | ❌ | Framework-specific |
| Entity linking/resolution | ❌ | Framework-specific |

**Why No Automatic Entity Extraction**:

1. **Domain Specificity**: What constitutes an "entity" varies by domain. A banking agent cares about accounts, transactions, merchants. A support agent cares about tickets, products, customers. Hub cannot know what to extract.

2. **Framework Capability**: Modern frameworks (LangChain, CrewAI) already provide entity extraction. Duplicating this creates conflicts.

3. **LLM Dependency**: Entity extraction requires LLM calls. Hub's memory services are storage infrastructure, not AI services. Adding LLM calls would:
   - Increase latency on every write
   - Create cost implications Hub cannot control
   - Couple memory to specific models

4. **False Positives**: Automatic extraction produces errors. In session-scoped memory, these errors persist until session ends, potentially confusing the agent.

**Trade-off**: Agents must explicitly extract and store entities (via their frameworks), but they have full control over what and how. Hub provides the storage; frameworks provide the intelligence.

---

### 🟡 Partially Adopted: Decay Models

**Recommendation**: Design decay models beyond simple windowing — based on recency, access frequency, confidence.

**Hub's Approach**:
- Conversation Service supports **configurable compaction strategies**:
  - Sliding window (keep last N)
  - LLM-based summarization
  - Token budget management
- Compaction is **synchronous before write**
- Session lifecycle provides natural boundary (all memory deleted after retention period)

**What We Adopted**:
| Aspect | Adopted |
|--------|---------|
| Sliding window compaction | ✅ Yes |
| LLM summarization | ✅ Yes |
| Token budget constraints | ✅ Yes |
| Session-scoped lifecycle | ✅ Yes |

**What We Did NOT Adopt**:
| Aspect | Not Adopted | Rationale |
|--------|-------------|-----------|
| Access-frequency decay | ❌ | See below |
| Confidence-based decay | ❌ | See below |
| Relevance scoring | ❌ | See below |

**Why No Sophisticated Decay**:

1. **Session Scope Simplifies**: Agent Memory has a natural lifecycle boundary — the session. Unlike LTM systems that need decay over months/years, session-scoped memory simply expires when the session ends. Sophisticated decay is less valuable when the maximum lifetime is hours/days.

2. **Compaction Suffices**: For conversation context (the primary decay concern), windowing + summarization handles 90% of use cases. The remaining 10% are framework-specific optimizations.

3. **Complexity vs Value**: Tracking access frequency and computing relevance requires:
   - Additional metadata per record
   - Background processing
   - Tunable parameters per agent
   
   For ephemeral, session-scoped data, this complexity doesn't provide proportional value.

4. **Framework Responsibility**: Frameworks like LangGraph and Strands have their own decay/compaction logic. Hub providing another layer creates conflicts and confusion.

**Trade-off**: Hub provides simple, configurable compaction. Sophisticated decay (if needed) is framework responsibility. This keeps Hub's storage layer simple and fast.

---

### 🟡 Partially Adopted: Separate Preference Memory

**Recommendation**: Explicit preference memory, not conflated with semantic facts.

**Hub's Approach**:
- KV Store with logical store names supports separation (`"preferences"` vs `"facts"` vs `"entities"`)
- **No formal ESPP taxonomy enforcement** in Agent Memory (unlike Enterprise Memory)
- Developer organizes memory by logical store names

**What We Adopted**:
| Aspect | Adopted |
|--------|---------|
| Logical separation via store names | ✅ Yes |
| Developer control over organization | ✅ Yes |

**What We Did NOT Adopt**:
| Aspect | Not Adopted | Rationale |
|--------|-------------|-----------|
| Formal ESPP memory classes | ❌ | See below |
| Separate Preference service | ❌ | Overhead without benefit |
| Preference schema enforcement | ❌ | Over-prescription |

**Why No Formal ESPP in Agent Memory**:

1. **Framework-Native Idiom Preservation**: As documented in the [Framework Analysis](./framework-reference/analysis.md), **no popular agentic framework enforces ESPP taxonomy**. All allow memory type boundaries to blur:
   
   | Framework | ESPP Enforcement |
   |-----------|------------------|
   | LangChain | ❌ None — memory types are configuration options |
   | LangGraph | ❌ None — all memory is typed state |
   | Semantic Kernel | 🟡 Collections only — not ESPP |
   | CrewAI | 🟡 Short/Long-term only — not ESPP |
   | Strands | 🟡 via AgentCore — optional |
   
   Enforcing ESPP would require developers to translate their framework's natural patterns into Hub's classification, creating friction and unnatural code.

2. **ESPP is for Enterprise Memory Governance**: The ESPP taxonomy exists for organizational knowledge governance — understanding what decisions were made (Episodic), what we learned (Semantic), how we should act (Procedural), and how to personalize (Preference). These distinctions matter for 7+ year retention, cross-agent knowledge, and regulatory compliance.

3. **Session Scope Flattens Taxonomy Value**: In a session, the distinction between "preference" and "semantic fact" is less critical. Both are just "things the agent learned in this session." Enforcing taxonomy adds overhead without governance benefit.

4. **Native Code Principle**: Hub's design philosophy is that agent code should look **native to the development framework**. If a LangChain developer stores preferences in a dictionary, that should translate naturally to Hub's KV Store — not require classification into "Preference" memory class.

5. **Logical Store Names Provide Flexibility**: Developers can create `"preferences"`, `"facts"`, `"customer"`, `"workflow_state"` as logical store names. This provides organizational benefit without framework-level enforcement.

**Trade-off**: Hub doesn't formally distinguish memory types in Agent Memory (all are KV entries). Developers self-organize using framework-native patterns. This enables idiomatic code but requires developers to understand when to use Enterprise Memory for governed, cross-session knowledge.

**Guidance**: While Hub doesn't enforce ESPP in Agent Memory, developers are encouraged to understand the [ESPP Taxonomy](../shared/espp-taxonomy.md) to recognize when data should be promoted to Enterprise Memory.

---

### 🟡 Partially Adopted: Context Assembly

**Recommendation**: Enable ranking and budget allocation from memory for context compilation.

**Hub's Approach**:
- Conversation Service supports **token budget** retrieval
- Log Service supports **RAG search** for relevant entries
- Document Service supports **semantic search**
- **Actual context assembly is Seer's responsibility**

**What We Adopted**:
| Aspect | Adopted |
|--------|---------|
| Token budget retrieval | ✅ Yes |
| RAG/semantic search | ✅ Yes |
| Embeddings (Hub-provided) | ✅ Yes |

**What We Did NOT Adopt**:
| Aspect | Not Adopted | Rationale |
|--------|-------------|-----------|
| Context ranking algorithms | ❌ | Seer responsibility |
| Cross-service budget allocation | ❌ | Seer responsibility |
| Context compilation API | ❌ | Seer responsibility |

**Why Context Assembly is Seer's Responsibility**:

1. **Separation of Concerns**: Hub Memory Services provide storage and retrieval. Seer provides AI orchestration. Context assembly is AI orchestration.

2. **Model-Specific**: How to compile context depends on the model, task, and agent design. Hub cannot generalize this.

3. **Agent Control**: Agents should control their context. Hub providing opinionated assembly would conflict with agent-specific needs.

**Trade-off**: Hub provides the primitives (token-budgeted retrieval, semantic search). Seer and frameworks compose these into context. This is more work for Seer but maintains clean boundaries.

---

### ✅ Adopted: First-Class Session Persistence

**Recommendation**: Like Strands, provide automatic save/restore with pluggable backends.

**Hub's Approach**:
- **No in-memory stores** — all storage is durable
- Automatic persistence on every write
- Automatic restoration when agent resumes in session
- Storage backend is Hub-managed (not pluggable by developers)

**What We Adopted**:
| Aspect | Adopted |
|--------|---------|
| Durable storage (no in-memory) | ✅ Yes |
| Automatic persistence | ✅ Yes |
| Session continuity | ✅ Yes |

**What We Did NOT Adopt**:
| Aspect | Not Adopted | Rationale |
|--------|-------------|-----------|
| Pluggable backends | ❌ | See below |
| Developer storage choice | ❌ | See below |

**Why No Pluggable Backends**:

1. **Enterprise Constraint**: Hub runs in enterprise environments with security, compliance, and operational requirements. Allowing arbitrary storage backends (file, S3, custom DBs) creates:
   - Security review overhead
   - Compliance gaps
   - Operational complexity

2. **Hub Guarantees**: Hub must guarantee isolation, encryption, retention, and cleanup. With pluggable backends, Hub cannot make these guarantees.

3. **Multi-Tenancy**: Hub is multi-tenant. Storage backends must support tenant isolation at the platform level. Pluggable backends would need to independently implement this.

**Trade-off**: Developers cannot choose storage backends, but they get consistent security, isolation, and lifecycle management without configuration.

---

### ✅ Adopted: Pluggable Conversation Management

**Recommendation**: Like Strands, support windowing and summarization as strategies.

**Hub's Approach**:
- Configurable compaction strategies per store and per agent
- Strategies: `sliding_window`, `summarization`, `token_budget`
- Configuration in agent spec, tunable in deployment CRD
- **Synchronous execution** (before write)

**What We Adopted**:
| Aspect | Adopted |
|--------|---------|
| Sliding window | ✅ Yes |
| LLM summarization | ✅ Yes |
| Token budget | ✅ Yes |
| Developer configuration | ✅ Yes |
| Runtime override | ✅ Yes (deployment CRD) |

**What We Did NOT Adopt**:
| Aspect | Not Adopted | Rationale |
|--------|-------------|-----------|
| Custom strategy plugins | ❌ | Complexity; built-in strategies cover common cases |
| Async compaction | ❌ | Consistency; agent sees compacted state immediately |

**Trade-off**: Limited to built-in strategies, but these cover 95% of use cases. Custom compaction logic can be implemented in the framework before calling Hub's Conversation Service.

---

### ❌ Not Adopted: Multi-Agent Session Support

**Recommendation**: Like Strands, track orchestrator state and cross-agent context.

**Hub's Approach**:
- **Agents are strictly isolated** — no cross-talk
- Multi-agent coordination is via **Request context** (not agent memory)
- Sub-agents (within a compound Raw Agent) are outside Hub's purview

**Why Not Adopted**:

1. **Isolation is a Core Principle**: Agent Memory is agent-private for security and privacy reasons. If Agent A could see Agent B's memory:
   - Information leakage across agents
   - Complex access control requirements
   - Audit complexity

2. **Request is the Shared Context**: Hub already provides Request-level context that all agents in a session can access. This is the designed mechanism for cross-agent coordination.

3. **Enterprise Memory for Cross-Agent Knowledge**: If knowledge should be shared across agents, it belongs in Enterprise Memory (with appropriate governance).

4. **Compound Agents are Internal**: If a "Hub Agent" is actually a compound agent with sub-agents (e.g., a LangGraph graph or CrewAI crew), the internal topology is invisible to Hub. These sub-agents can share memory through their framework's mechanisms.

**Trade-off**: No built-in multi-agent memory sharing, but clean isolation guarantees. Cross-agent coordination uses Request context (designed for this purpose).

**Comparison with Strands**:

| Aspect | Strands | Hub |
|--------|---------|-----|
| Multi-agent session support | ✅ Yes (orchestrator state) | ❌ No |
| Cross-agent memory | ✅ Shared state | ❌ Isolated |
| Coordination mechanism | Session manager | Request context |

Hub's design reflects enterprise constraints (isolation, audit, multi-tenancy) that Strands (as a framework) doesn't need to address.

---

### ✅ Adopted: Namespace-Based Scoping

**Recommendation**: Like AgentCore, isolate memory by actor/session/workbench.

**Hub's Approach**:
- Strict scoping: `tenant → workbench → scenario → request → agent`
- All APIs operate only within this scope
- Logical store names provide additional organization within agent scope

**What We Adopted**:
| Aspect | Adopted |
|--------|---------|
| Hierarchical scoping | ✅ Yes |
| Strict isolation | ✅ Yes |
| No higher-scope access | ✅ Yes |
| Logical store names | ✅ Yes |

**What We Did NOT Adopt**:
| Aspect | Not Adopted | Rationale |
|--------|-------------|-----------|
| Cross-session namespaces | ❌ | Session-scoped by design |
| Actor-level namespaces (like AgentCore's `/preferences/{actorId}`) | ❌ | Cross-session = Enterprise Memory |

**Trade-off**: Hub's scoping is strictly session-bound. AgentCore's namespace patterns like `/preferences/{actorId}` enable cross-session memory, which Hub explicitly does not support in Agent Memory.

---

## Trade-off Summary

| Recommendation | Status | Trade-off |
|----------------|--------|-----------|
| Typed session state | ✅ Adopted (JSON) | Serialization enforced, schema left to frameworks |
| Memory access tools | ✅ Adopted | Observable in traces, not in Request history |
| Entity tracking | 🟡 Partial | Storage provided, extraction left to frameworks |
| Decay models | 🟡 Partial | Compaction strategies; sophisticated decay left to frameworks |
| Separate preference memory | 🟡 Partial | Logical store names; no formal ESPP enforcement |
| Context assembly | 🟡 Partial | Primitives provided; assembly is Seer's job |
| Session persistence | ✅ Adopted | Durable, not pluggable |
| Conversation management | ✅ Adopted | Built-in strategies, no custom plugins |
| Multi-agent support | ❌ Not Adopted | Isolation is core; use Request context |
| Namespace scoping | ✅ Adopted | Session-scoped only |

---

## Guiding Trade-off Principle

**Hub optimizes for enterprise constraints over framework features.**

| Priority | Constraint |
|----------|------------|
| 1 | Security & Isolation |
| 2 | Clear Enterprise/Agent boundary |
| 3 | Framework agnosticism |
| 4 | Operational simplicity |
| 5 | Feature parity with frameworks |

When framework patterns conflict with enterprise constraints, Hub chooses enterprise constraints.

---

## Future Considerations

### Potential Additions (If Demand Emerges)

| Feature | Condition for Addition |
|---------|------------------------|
| Automatic entity extraction | If common patterns emerge across frameworks |
| Access-frequency decay | If session durations increase significantly |
| Custom compaction plugins | If built-in strategies prove insufficient |
| Cross-agent read-only access | If governed, audited access patterns are designed |

### What Will NOT Change

| Constraint | Reason |
|------------|--------|
| Session-scoped maximum lifetime | Core boundary with Enterprise Memory |
| Agent isolation | Security and privacy foundation |
| No cross-session memory | Enterprise Memory serves this need |
| Encryption at application layer | Privacy guarantee |

---

## Related Documents

- [Agent Memory Services](./README.md) — Overview
- [Framework Reference](./framework-reference/README.md) — Summary of framework patterns
- [Framework Analysis](./framework-reference/analysis.md) — Detailed per-framework analysis
- [Enterprise Memory Services](../enterprise-memory/README.md) — Contrast with durable memory
- [ESPP Taxonomy](../shared/espp-taxonomy.md) — Enterprise Memory taxonomy (not enforced in Agent Memory)

### Related Decision Logs

- [ADR-0067: Agent Memory Session Scope](../../../decision-logs/0067-agent-memory-session-scope.md)
- [ADR-0068: Framework-Native Idioms](../../../decision-logs/0068-agent-memory-framework-native-idioms.md)
- [ADR-0069: Storage Services](../../../decision-logs/0069-agent-memory-storage-services.md)
- [ADR-0070: Encryption and Isolation](../../../decision-logs/0070-agent-memory-encryption-isolation.md)

---

*Hub's Agent Memory design prioritizes enterprise constraints while enabling framework flexibility within session scope.*

