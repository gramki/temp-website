# Memory in Open-Source Agent Frameworks

This document highlights how common OSS agent frameworks model memory, with practical pros/cons.

## LangGraph (LangChain) — State, Threads, and Checkpointed Persistence

**What the framework provides**

- **Short-term memory** as part of the agent/graph **state**.
- **Persistence** via **checkpointers** that checkpoint graph state to a **thread** at each super-step, enabling resuming, time-travel, and post-run inspection.

**Primary references**

- LangGraph Persistence: [https://langchain-ai.github.io/langgraph/concepts/persistence/](https://langchain-ai.github.io/langgraph/concepts/persistence/)
- LangGraph Memory: [https://langchain-ai.github.io/langgraph/concepts/memory/](https://langchain-ai.github.io/langgraph/concepts/memory/)

**How it maps to the memory lifecycle**

- Identify: application-defined (you decide what to write into state)
- Store: state checkpoints (threaded)
- Retrieve: load thread state; optionally long-term memory stores
- Compose: state acts as the structured context carrier
- Decay/Evict: mostly application-owned (retention policies depend on your checkpointer backend)

**Pros**

- Strong **state-first** design encourages structured context
- Persistence enables **debugging**, **HITL**, and **resumability**
- Works well for deterministic workflows + agent loops

**Cons / gotchas**

- Long-term memory governance (decay/eviction, provenance) is largely **your responsibility**
- Without discipline, state can become an untyped “junk drawer”

---

## CrewAI — Built-in Memory Types + External Memory Providers

**What the framework provides**

- A “basic” memory system with multiple memory types (short-term, long-term, entity memory) and support for external memory providers.

**Primary references**

- CrewAI Memory: [https://docs.crewai.com/concepts/memory](https://docs.crewai.com/concepts/memory)
- CrewAI Crews: [https://docs.crewai.com/concepts/crews](https://docs.crewai.com/concepts/crews)

**How it maps to the memory lifecycle**

- Identify: framework-supported (agent/task interactions are candidates)
- Store: framework-managed stores + optional external providers
- Retrieve: injected as context during execution
- Compose: convenience-oriented; can be less explicit than a “context compiler”
- Decay/Evict: varies by provider; must be designed for production use

**Pros**

- Clear developer ergonomics: memory is a first-class concept
- Distinct memory types reduce “everything is a chunk” behavior

**Cons / gotchas**

- Production-grade governance (provenance, retention, redaction) depends on your chosen storage/provider
- Context assembly can become opaque if not instrumented

---

## AutoGen — Memory as RAG Patterns and Ecosystem Extensions (optional)

AutoGen documents memory largely through a RAG lens ("retrieve useful facts and add to context") and supports ecosystem integrations.

**Primary references**

- AutoGen Memory: [https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/memory.html](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/memory.html)

**Commentary**

- Good fit for teams starting with RAG-centric “memory.”
- For full agent memory management, you will still need explicit lifecycle controls (promotion, decay, eviction, provenance).

---

## Semantic Kernel — Memory Stores, Skills, and Planner-Centric Context

**What the framework provides**

Semantic Kernel (SK) treats memory primarily as a **semantic recall system** integrated with skills and planners. Memory is externalized via **memory stores** (vector databases) and accessed through APIs such as `SaveInformationAsync` and `SearchAsync`.

Memory is typically:

- Semantic (facts, summaries, notes)
- Vector-based
- Skill- or planner-consumed rather than agent-state-centric

**Primary references**

- Semantic Kernel Vector Store Connectors: [https://learn.microsoft.com/en-us/semantic-kernel/concepts/vector-store-connectors/](https://learn.microsoft.com/en-us/semantic-kernel/concepts/vector-store-connectors/)
- Semantic Kernel Planning: [https://learn.microsoft.com/en-us/semantic-kernel/concepts/planning](https://learn.microsoft.com/en-us/semantic-kernel/concepts/planning)
- Semantic Kernel Overview: [https://learn.microsoft.com/en-us/semantic-kernel/](https://learn.microsoft.com/en-us/semantic-kernel/)

**How it maps to the memory lifecycle**

- **Identify:** Application-driven; developers decide what to write to memory (often summaries or extracted facts)
- **Store:** Vector memory stores (Azure AI Search, Qdrant, Pinecone, etc.)
- **Retrieve:** Similarity search scoped by collection / namespace
- **Compose:** Retrieved memories are injected into prompts via skills or planners
- **Decay:** Not native; must be implemented at the store or application layer
- **Evict:** Manual or store-level (TTL, deletion by key/collection)

**Pros**

- Clear, explicit APIs for semantic memory
- Strong alignment with enterprise .NET / Azure ecosystems
- Clean separation between skills, planners, and memory access

**Cons / gotchas**

- Memory is largely **semantic-only**; episodic and preference memory require custom modeling
- No built-in promotion, decay, or provenance model
- Context composition remains mostly prompt-oriented unless extended

**Architectural takeaway**

Semantic Kernel excels as a **semantic memory + skill orchestration layer**, but teams building long-lived agentic systems should:

- Add explicit episodic stores (event logs)
- Layer preference modeling separately
- Introduce a context compiler and governance controls above SK’s memory APIs

## Navigation

- Back: [README.md](./README.md)
- Related: [context-building.md](./context-building.md)

