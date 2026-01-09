# Agent Memory in Agentic Frameworks — State of the World

This document analyzes how popular agentic frameworks implement **agent-level memory** — the operational, session-scoped memory that supports agent continuity, personalization, and working state.

---

## Document Metadata

| Field | Value |
|-------|-------|
| **Analysis Date** | January 8, 2026 |
| **Last Updated** | January 8, 2026 |
| **Status** | Draft (Scratchpad) |

---

## Frameworks and Versions Analyzed

| Framework | Version | Release Date | Documentation URL |
|-----------|---------|--------------|-------------------|
| LangChain | 0.3.x | Dec 2025 | [python.langchain.com](https://python.langchain.com/docs/modules/memory/) |
| LangGraph | 0.2.x | Dec 2025 | [langchain-ai.github.io/langgraph](https://langchain-ai.github.io/langgraph/concepts/persistence/) |
| Semantic Kernel | 1.x | Dec 2025 | [learn.microsoft.com](https://learn.microsoft.com/semantic-kernel/memories/) |
| CrewAI | 0.8x | Dec 2025 | [docs.crewai.com](https://docs.crewai.com/concepts/memory) |
| AutoGen | 0.4.x | Dec 2025 | [microsoft.github.io/autogen](https://microsoft.github.io/autogen/docs/notebooks/agentchat_teachability) |
| OpenAI Assistants API | v2 | Nov 2024 | [platform.openai.com](https://platform.openai.com/docs/assistants/overview) |
| AWS Strands Agents SDK | 0.1.x (Python) | Jan 2026 | [strandsagents.com](https://strandsagents.com/latest/) |
| Bedrock AgentCore Memory | 0.1.x | Jan 2026 | [github.com/aws/bedrock-agentcore-sdk-python](https://github.com/aws/bedrock-agentcore-sdk-python/) |

> **Note:** Framework capabilities evolve rapidly. Version numbers are approximate based on documentation reviewed. Verify current versions before making architectural decisions.

---

## Table of Contents

1. [Scope Clarification](#scope-clarification)
2. [Memory Types Referenced](#memory-types-referenced)
3. [Framework Analysis](#framework-analysis)
   - [1. LangChain](#1-langchain)
   - [2. LangGraph](#2-langgraph)
   - [3. Semantic Kernel (Microsoft)](#3-semantic-kernel-microsoft)
   - [4. CrewAI](#4-crewai)
   - [5. AutoGen (Microsoft)](#5-autogen-microsoft)
   - [6. OpenAI Assistants API](#6-openai-assistants-api)
   - [7. AWS Strands Agents SDK](#7-aws-strands-agents-sdk)
4. [Technique Comparison Matrix](#technique-comparison-matrix)
5. [Storage Backend Patterns](#storage-backend-patterns)
6. [Relevant Patterns for Hub Agent Memory](#relevant-patterns-for-hub-agent-memory)
7. [Gaps in Current Frameworks](#gaps-in-current-frameworks)
8. [Recommendations for Hub Agent Memory](#recommendations-for-hub-agent-memory)
9. [References](#references)

---

## Scope Clarification

This analysis focuses on **Agent Memory** as defined in Hub's memory architecture:

| Aspect | Agent Memory (This Analysis) | Enterprise Memory (Out of Scope) |
|--------|------------------------------|----------------------------------|
| **Scope** | Agent/Session — individual context | Organizational — cross-agent |
| **Persistence** | Ephemeral — days to months | Durable — 7+ years |
| **Purpose** | Operational continuity, personalization | Audit, compliance, institutional learning |
| **Governance** | Minimal — decay and TTL | Full — CAF, immutability, promotion |

Most agentic frameworks do not distinguish these two memory scopes. This analysis extracts what is relevant to **agent memory** design from their approaches.

---

## Memory Types Referenced

| Type | Description | Relevance to Agent Memory |
|------|-------------|---------------------------|
| **Episodic** | What happened, in sequence, in a session | ✅ Primary — session history, tool calls, turns |
| **Semantic** | Learned facts about entities/context | ✅ Relevant — user facts, session-learned context |
| **Procedural** | How to perform tasks | 🟡 Partial — preferred tool sequences, patterns |
| **Preference** | User/agent behavioral preferences | ✅ Relevant — interaction style, format preferences |

---

## Framework Analysis

### 1. LangChain

**Memory Abstractions:**

| Memory Type | Implementation | Storage |
|-------------|----------------|---------|
| `ConversationBufferMemory` | Full message history | In-memory |
| `ConversationBufferWindowMemory` | Last N messages | In-memory |
| `ConversationSummaryMemory` | LLM-generated summaries | In-memory + LLM calls |
| `ConversationSummaryBufferMemory` | Hybrid: recent + summary | In-memory + LLM calls |
| `VectorStoreRetrieverMemory` | Embedding-based retrieval | Vector DB (FAISS, Chroma, Pinecone) |
| `EntityMemory` | Entity extraction + tracking | In-memory or vector DB |

**Key Techniques:**

| Technique | How It Works | Agent Memory Relevance |
|-----------|--------------|------------------------|
| **Windowing** | Keep only last N turns | ✅ Simple context budget management |
| **Summarization** | LLM compresses older history | ✅ Context compression |
| **Entity extraction** | Track entities mentioned in conversation | ✅ Semantic memory primitive |
| **Hybrid buffer+summary** | Recent detail + older summary | ✅ Tiered retention |

**Storage Backends:**
- In-memory (default)
- Redis (for persistence across sessions)
- SQLite (local persistence)
- Vector DBs (FAISS, Chroma, Pinecone, Weaviate)

**Observations:**
- Memory is **per-chain**, not per-agent — no cross-chain memory sharing
- No built-in decay or forgetting beyond window truncation
- Entity memory is promising but requires explicit configuration

---

### 2. LangGraph

**Memory Model:**

LangGraph uses **explicit state** passed through graph nodes:

```python
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]
    user_preferences: dict
    session_facts: list[str]
    tool_results: list[ToolResult]
```

**Key Techniques:**

| Technique | How It Works | Agent Memory Relevance |
|-----------|--------------|------------------------|
| **Typed state schema** | Explicit structure for all memory | ✅ Schema-driven memory |
| **Checkpointing** | Persist state at graph nodes | ✅ Session recovery, replay |
| **State reducers** | Custom merge logic for state updates | ✅ Conflict resolution |
| **Memory nodes** | Dedicated nodes for memory operations | ✅ Explicit memory management |

**Storage Backends:**
- In-memory (default)
- SQLite checkpointer
- Postgres checkpointer
- Redis checkpointer
- Custom checkpointer interface

**Observations:**
- State is **explicit and typed** — developer controls exactly what's remembered
- Checkpointing enables **session persistence and recovery**
- No built-in semantic/procedural/preference memory — must be modeled in state
- Memory operations are **synchronous with execution** — no background learning

---

### 3. Semantic Kernel (Microsoft)

**Memory Architecture:**

| Component | Purpose | Storage |
|-----------|---------|---------|
| `ChatHistory` | Conversation turns | In-memory |
| `SemanticMemory` | Facts and embeddings | Vector DB |
| `VolatileMemoryStore` | Ephemeral key-value | In-memory |
| `TextMemoryPlugin` | Memory as a skill | Any memory store |

**Key Techniques:**

| Technique | How It Works | Agent Memory Relevance |
|-----------|--------------|------------------------|
| **Memory as skill** | Memory operations exposed as callable functions | ✅ Agent can explicitly remember/recall |
| **Collection-based organization** | Memories grouped by collection | ✅ Scope separation |
| **Relevance scoring** | Similarity-based retrieval | ✅ Context-relevant recall |
| **User profiles** | Structured preference storage | ✅ Preference memory primitive |

**Storage Backends:**
- In-memory (volatile)
- Azure Cognitive Search
- Chroma, Pinecone, Weaviate
- PostgreSQL with pgvector
- Qdrant

**Observations:**
- More **enterprise-friendly abstractions** than LangChain
- Explicit distinction between **volatile** and **persistent** memory
- User profiles provide **preference memory** foundation
- Skills system could support **procedural memory** patterns

---

### 4. CrewAI

**Memory Model:**

| Memory Type | Implementation | Scope |
|-------------|----------------|-------|
| Short-term | RAG-style conversation memory | Task execution |
| Long-term | Vector store persistence | Cross-task |
| Entity | Named entity tracking | Cross-conversation |
| Contextual | Task-specific context | Single task |

**Key Techniques:**

| Technique | How It Works | Agent Memory Relevance |
|-----------|--------------|------------------------|
| **Shared crew memory** | Memory accessible to all agents in crew | 🟡 Multi-agent coordination |
| **Entity extraction** | Automatic entity identification and tracking | ✅ Semantic memory |
| **Memory providers** | Pluggable storage backends | ✅ Storage flexibility |
| **Task context injection** | Relevant memory injected per task | ✅ Context assembly |

**Storage Backends:**
- In-memory (default)
- Custom memory providers
- Vector DB integration

**Observations:**
- Focus on **multi-agent collaboration** memory sharing
- Entity memory is **automatic**, not opt-in
- Less granular control than LangGraph
- Good model for **shared working memory** patterns

---

### 5. AutoGen (Microsoft)

**Memory Model:**

| Component | Purpose | Characteristics |
|-----------|---------|-----------------|
| `ConversableAgent.chat_messages` | Conversation history | Per-agent, in-memory |
| `teachable_agent` | Learning from corrections | Stores facts in vector DB |
| Custom memory handlers | Developer-defined | Flexible |

**Key Techniques:**

| Technique | How It Works | Agent Memory Relevance |
|-----------|--------------|------------------------|
| **Teachability** | Agent learns from user corrections | ✅ Preference/fact learning |
| **Message filtering** | Selective message inclusion | ✅ Context budget |
| **Agent-specific memory** | Each agent maintains own history | ✅ Agent isolation |
| **Human feedback integration** | Corrections stored as memories | ✅ Supervised learning |

**Storage Backends:**
- In-memory (default)
- ChromaDB (for teachable agents)
- Custom stores

**Observations:**
- **Teachability** is unique — explicit learning from corrections
- Good separation of **agent-specific** vs **shared** memory
- Less structured than Semantic Kernel

---

### 6. OpenAI Assistants API

**Memory Model:**

| Component | Purpose | Managed By |
|-----------|---------|------------|
| Threads | Conversation history | OpenAI |
| Files | Document storage | OpenAI |
| Vector Store | Retrieval-augmented context | OpenAI |
| Tool outputs | Tool call results | OpenAI |

**Key Techniques:**

| Technique | How It Works | Agent Memory Relevance |
|-----------|--------------|------------------------|
| **Thread persistence** | Automatic history management | ✅ Session continuity |
| **Run context** | Instructions + tools per run | ✅ Context injection |
| **Retrieval augmentation** | Automatic relevant file retrieval | 🟡 Knowledge, not memory |
| **Annotations** | Citation of retrieved content | 🟡 Provenance |

**Observations:**
- **Fully managed** — no storage decisions
- **Opaque internals** — no control over compression, decay
- Thread model is **pure episodic** — no semantic/preference primitives
- Good baseline for **minimal agent memory** requirements

---

### 7. AWS Strands Agents SDK

**Memory Architecture:**

Strands provides a layered memory system with clear separation between conversation history, agent state, and session persistence:

| Component | Purpose | Scope |
|-----------|---------|-------|
| `agent.messages` | Conversation history (user, assistant, tool calls/results) | Request/Session |
| `agent.state` | Key-value storage for stateful information | Agent lifetime |
| `request_state` | Contextual information within a single request | Single request |
| Session Managers | Persistence layer for messages and state | Cross-session |

**Session Management:**

| Session Manager | Storage | Use Case |
|-----------------|---------|----------|
| `FileSessionManager` | Local filesystem | Development, single-node |
| `S3SessionManager` | Amazon S3 | Cloud, distributed |
| `AgentCoreMemorySessionManager` | Bedrock AgentCore Memory | Advanced memory with LTM strategies |
| Custom `SessionRepository` | Any backend | Enterprise integration |

**Key Techniques:**

| Technique | How It Works | Agent Memory Relevance |
|-----------|--------------|------------------------|
| **Typed agent state** | JSON-serializable key-value store accessible via `agent.state` | ✅ Structured preference/fact storage |
| **Conversation managers** | Pluggable strategies for history management | ✅ Context budget |
| **Sliding window** | Keep last N messages, auto-trim on overflow | ✅ Simple windowing |
| **Summarization** | LLM-generated summaries of older messages | ✅ Context compression |
| **Session persistence** | Automatic save/restore of messages + state | ✅ Cross-session continuity |
| **Multi-agent sessions** | Orchestrator state, cross-agent context, node history | ✅ Multi-agent coordination |
| **Request state** | Per-invocation state for callback handlers | ✅ Request-scoped context |

**Conversation Managers:**

| Manager | Strategy | Characteristics |
|---------|----------|-----------------|
| `NullConversationManager` | No modification | Manual control, debugging |
| `SlidingWindowConversationManager` | Keep recent N messages | Default, auto-trim on overflow |
| `SummarizingConversationManager` | Summarize older, preserve recent | Context compression |
| Custom | Implement `ConversationManager` interface | Full control |

**AgentCore Memory Integration (Community):**

The `AgentCoreMemorySessionManager` provides advanced memory capabilities via Amazon Bedrock AgentCore Memory:

| Memory Type | Strategy | Purpose |
|-------------|----------|---------|
| Short-term (STM) | Conversation persistence | Session continuity |
| Long-term (LTM) | `summaryMemoryStrategy` | Session summaries |
| Long-term (LTM) | `userPreferenceMemoryStrategy` | Preference learning |
| Long-term (LTM) | `semanticMemoryStrategy` | Fact extraction |

**Namespace-based scoping:**
- `/preferences/{actorId}` — User preferences across sessions
- `/facts/{actorId}` — User facts across sessions
- `/summaries/{actorId}/{sessionId}` — Session-specific summaries

**Storage Backends:**
- In-memory (default)
- Local filesystem (`FileSessionManager`)
- Amazon S3 (`S3SessionManager`)
- Amazon Bedrock AgentCore Memory (community integration)
- Custom via `SessionRepository` interface (any database)

**Observations:**
- **Three-tier state model** — conversation history, agent state, request state — with clear semantics
- **Pluggable conversation managers** with built-in windowing and summarization
- **Session persistence is first-class** — not bolted on; agents restore state automatically
- **Multi-agent aware** — orchestrator state, cross-agent context, node execution history
- **AgentCore Memory** provides closest analog to ESPP taxonomy — short-term for episodic, long-term strategies for semantic/preference
- **Namespace scoping** aligns with workbench/agent isolation concepts
- **Tools have access to state** via `ToolContext` — enabling stateful tool execution
- **JSON serialization enforced** — ensures state can be persisted and restored

---

## Technique Comparison Matrix

| Technique | LangChain | LangGraph | Semantic Kernel | CrewAI | AutoGen | Assistants | Strands |
|-----------|-----------|-----------|-----------------|--------|---------|------------|---------|
| **Message windowing** | ✅ | Manual | ✅ | ✅ | Manual | Managed | ✅ |
| **Summarization** | ✅ | Manual | ❌ | ❌ | ❌ | Managed | ✅ |
| **Entity extraction** | ✅ | Manual | ❌ | ✅ | ❌ | ❌ | ❌ |
| **Typed state schema** | ❌ | ✅ | 🟡 | ❌ | ❌ | ❌ | ✅ |
| **Checkpointing** | ❌ | ✅ | ❌ | ❌ | ❌ | Managed | ✅ |
| **Memory as callable** | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | 🟡 |
| **Preference storage** | ❌ | Manual | ✅ | ❌ | 🟡 | ❌ | ✅ (AgentCore) |
| **Teachability** | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |
| **Multi-agent sharing** | ❌ | 🟡 | ❌ | ✅ | ✅ | ❌ | ✅ |
| **Decay/forgetting** | Window | Manual | ❌ | ❌ | ❌ | Managed | Window |
| **Session persistence** | 🟡 | ✅ | ❌ | ❌ | ❌ | Managed | ✅ |
| **Cloud-native storage** | ❌ | ❌ | 🟡 | ❌ | ❌ | ✅ | ✅ (S3, AgentCore) |

---

## Storage Backend Patterns

### Pattern 1: In-Memory (Default)
- **Used by**: All frameworks as default
- **Characteristics**: Fast, no persistence, lost on restart
- **Agent Memory Use**: Development, short sessions

### Pattern 2: Key-Value Store (Redis, SQLite)
- **Used by**: LangChain, LangGraph, Semantic Kernel
- **Characteristics**: Fast lookup, simple persistence, no semantic search
- **Agent Memory Use**: Session state, preferences, structured facts

### Pattern 3: Vector Store (Chroma, Pinecone, Weaviate)
- **Used by**: All frameworks for "semantic memory"
- **Characteristics**: Similarity search, embedding-based, no structure
- **Agent Memory Use**: Relevant context retrieval, entity facts

### Pattern 4: Relational (PostgreSQL, SQLite)
- **Used by**: LangGraph (checkpointing), custom implementations
- **Characteristics**: Structured, queryable, transactional
- **Agent Memory Use**: Session history, typed state persistence

### Pattern 5: Managed/Opaque (OpenAI)
- **Used by**: OpenAI Assistants
- **Characteristics**: No control, automatic, black-box
- **Agent Memory Use**: Simplest case — full delegation

### Pattern 6: Cloud Object Storage (Amazon S3)
- **Used by**: Strands (`S3SessionManager`)
- **Characteristics**: Durable, distributed, cost-effective, eventual consistency
- **Agent Memory Use**: Cross-region session persistence, cloud-native deployments

### Pattern 7: Managed Memory Service (Bedrock AgentCore Memory)
- **Used by**: Strands (community `AgentCoreMemorySessionManager`)
- **Characteristics**: Managed, namespace-scoped, LTM strategies (summary, preferences, facts)
- **Agent Memory Use**: Long-term memory with intelligent retrieval, preference learning

---

## Relevant Patterns for Hub Agent Memory

Based on this analysis, the following patterns are relevant for Hub Agent Memory design:

### 1. Session State with Typed Schema (LangGraph)
- Explicit state structure
- Checkpointing for recovery
- Custom reducers for update logic

### 2. Memory as Callable Tool (Semantic Kernel)
- Agent explicitly invokes remember/recall
- Memory operations are observable
- Audit-friendly

### 3. Entity Tracking (LangChain, CrewAI)
- Automatic extraction of entities
- Entity-scoped facts
- Cross-turn entity persistence

### 4. Tiered Retention (LangChain Hybrid)
- Recent history in detail
- Older history summarized or decayed
- Token budget management

### 5. Preference Learning (AutoGen Teachability)
- Learn from corrections
- Store revealed preferences
- Apply in future turns

### 6. Multi-Agent Sharing (CrewAI, Strands)
- Shared working memory
- Agent-specific memory
- Coordination context

### 7. First-Class Session Persistence (Strands)
- Automatic save/restore of messages + state
- Multiple storage backends (file, S3, custom)
- Multi-agent session support with orchestrator state

### 8. Pluggable Conversation Management (Strands)
- Windowing, summarization as built-in strategies
- Custom conversation manager interface
- Per-turn management for long-running agents

### 9. Namespace-Scoped LTM Strategies (Strands + AgentCore)
- Separate namespaces for preferences, facts, summaries
- Actor/session scoping for isolation
- Configurable relevance thresholds per namespace

---

## Gaps in Current Frameworks

| Gap | Description | Hub Agent Memory Implication |
|-----|-------------|------------------------------|
| **No structured decay** | Memory removed by truncation, not relevance | Need decay models based on recency, access, confidence |
| **No preference formalization** | Preferences are implicit or manual (Strands+AgentCore addresses partially) | Need explicit preference memory with sources |
| **No procedural learning** | Skills/tools are static | Consider procedural memory for learned patterns |
| **No memory → action audit** | Can't trace decision to memory | Need provenance in context assembly |
| **No cross-session continuity** | Sessions are isolated (Strands addresses this) | Need agent identity and cross-session memory |
| **No workbench/tenant scoping** | Most frameworks are single-agent focused | Need multi-tenant memory isolation |

---

## Recommendations for Hub Agent Memory

1. **Support typed session state** — Like LangGraph and Strands, with explicit schema and JSON serialization
2. **Provide memory access tools** — Like Semantic Kernel, make memory operations observable
3. **Implement entity tracking** — Automatic extraction and persistence
4. **Design decay models** — Beyond simple windowing
5. **Separate preference memory** — Explicit, not conflated with facts (learn from Strands+AgentCore strategies)
6. **Enable context assembly** — Ranking and budget allocation from memory
7. **First-class session persistence** — Like Strands, automatic save/restore with pluggable backends
8. **Pluggable conversation management** — Like Strands, support windowing and summarization as strategies
9. **Multi-agent session support** — Like Strands, track orchestrator state and cross-agent context
10. **Namespace-based scoping** — Like AgentCore, isolate memory by actor/session/workbench

---

## References

- [LangChain Memory](https://python.langchain.com/docs/modules/memory/)
- [LangGraph Persistence](https://langchain-ai.github.io/langgraph/concepts/persistence/)
- [Semantic Kernel Memory](https://learn.microsoft.com/semantic-kernel/memories/)
- [CrewAI Memory](https://docs.crewai.com/concepts/memory)
- [AutoGen Teachability](https://microsoft.github.io/autogen/docs/notebooks/agentchat_teachability)
- [OpenAI Assistants](https://platform.openai.com/docs/assistants/overview)
- [Strands Agents Session Management](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/agents/session-management/)
- [Strands Agents State Management](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/agents/state/)
- [Strands Agents Conversation Management](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/agents/conversation-management/)
- [AgentCore Memory Session Manager](https://github.com/aws/bedrock-agentcore-sdk-python/tree/main/src/bedrock_agentcore/memory/integrations/strands)

---

*This document surveys agent memory approaches as of January 2026. Framework capabilities evolve; verify current documentation.*
