# Primer on Agent Memory Management

**Audience:** Agentic AI Engineers, Platform Architects, Applied AI Researchers  
**Scope:** Episodic, Semantic, Preference, and Procedural Memory in Agent-Native Systems

### Related Documents

- **[Raw, Trained, Employed Agents](../../aosm-meta-model/raw-trained-employed-agents.md)** — Memory is configured at the Training layer and operationalized at the Employed layer
- **[Knowledge vs Memory vs Context vs Session](./knowledge-memory-context-session.md)** — Foundational distinctions

---

## 1. Why Agent Memory Is a First-Class System

Modern agentic systems are not stateless LLM wrappers. They are **long-running cognitive systems** that must:

* Accumulate experience
* Learn stable facts
* Adapt to users and environments
* Execute increasingly sophisticated procedures

Memory is therefore **infrastructure**, not an optimization.

This chapter treats agent memory as a **managed lifecycle**:

> **Identify → Store → Retrieve → Compose Context → Decay → Evict**

Each stage has architectural, algorithmic, and governance implications.

---

## 2. The Four Canonical Memory Types

### 2.1 Episodic Memory

**Definition:** Records of what happened—events, interactions, traces, outcomes.

* Examples: conversations, decisions taken, tool invocations, failures
* Time horizon: short to medium
* Mutability: append-only

**Primary risks:**

* Unbounded growth
* Over-inclusion in context
* Privacy leakage

---

### 2.2 Semantic Memory

**Definition:** Stable knowledge—facts, concepts, relationships, models of the world.

* Examples: entity attributes, domain facts, schemas
* Time horizon: long
* Mutability: versioned

**Primary risks:**

* Stale or contradictory facts
* Lack of provenance
* Weak grounding

---

### 2.3 Preference Memory

**Definition:** Learned or stated biases guiding behavior.

* Examples: verbosity, tone, risk appetite, format choices
* Time horizon: medium to long
* Mutability: confidence-weighted

**Primary risks:**

* Overfitting to transient signals
* Conflicting preferences
* Lack of explainability

---

### 2.4 Procedural Memory

**Definition:** How to do things—skills, workflows, policies, plans.

* Examples: escalation playbooks, compliance workflows, tool chains
* Time horizon: long
* Mutability: version-controlled

**Primary risks:**

* Drift from policy
* Silent obsolescence
* Hidden coupling to tools

---

## 3. Identifying What Should Become Memory

### 3.1 Salience Detection

Agents must decide *what is worth remembering*.

Common triggers:

* User corrections
* Explicit decisions
* Failures or overrides
* Novel entities or constraints
* Strong sentiment

**Techniques:**

* Rule-based triggers
* LLM-based salience classifiers
* Surprise / entropy scoring
* Explicit user directives ("remember this")

**Further reading:**

* [https://arxiv.org/abs/2303.11366](https://arxiv.org/abs/2303.11366) (Reflexion)
* [https://arxiv.org/abs/2210.03629](https://arxiv.org/abs/2210.03629) (ReAct)

---

### 3.2 Schema-Guided Extraction

Instead of storing raw text, agents should extract **structured memory artifacts**.

Example artifacts:

* Decision Records
* Action Records
* Evidence Bundles
* Explanation Records

This enables downstream reasoning and auditing.

**Further reading:**

* [https://adr.github.io/](https://adr.github.io/) (Architectural Decision Records)
* [https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/welcome.html](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/welcome.html) (AWS ADR Guidance)
* [https://arxiv.org/abs/2310.08560](https://arxiv.org/abs/2310.08560) (MemGPT: Memory Management for LLMs)

---

### 3.3 Reflection and Consolidation

Agents periodically reflect on accumulated episodes to:

* Summarize
* Promote stable facts to semantic memory
* Detect emerging preferences
* Refine procedures

This mirrors **memory consolidation** in cognitive science.

**Further reading:**

* [https://arxiv.org/abs/2304.03442](https://arxiv.org/abs/2304.03442) (Generative Agents)
* [https://arxiv.org/abs/2308.10144](https://arxiv.org/abs/2308.10144) (Self-Reflection in LLMs)

---

## 4. Storing Agent Memory

### 4.1 Polyglot Memory Persistence

Different memory types require different storage models.

| Memory Type | Storage Model                     |
| ----------- | --------------------------------- |
| Episodic    | Event log + embeddings            |
| Semantic    | Knowledge graph + vector index    |
| Preference  | Typed KV with confidence          |
| Procedural  | DSLs, policies, code repositories |

One memory ≠ one database.

---

### 4.2 Common Storage Technologies

* Vector Databases: Pinecone, Weaviate, Qdrant
* Knowledge Graphs: Neo4j, RDF stores
* Event Stores: Kafka, DynamoDB Streams
* Document Stores: PostgreSQL, MongoDB
* Policy Engines: OPA, Cedar

**Further reading:**

* [https://www.pinecone.io/learn/vector-database/](https://www.pinecone.io/learn/vector-database/)
* [https://weaviate.io/developers/weaviate](https://weaviate.io/developers/weaviate)
* [https://neo4j.com/developer/graph-database/](https://neo4j.com/developer/graph-database/)

---

## 5. Retrieving Memory

### 5.1 Episodic Retrieval

* Time-window queries
* Similarity search
* Trace reconstruction

Use cases:

* "What happened last time this failed?"

---

### 5.2 Semantic Retrieval

* Entity-centric lookup
* Graph traversal
* Hybrid symbolic + vector search

Use cases:

* "What do we know about customer X?"

---

### 5.3 Preference Retrieval

* Contextual matching
* Conflict resolution
* Confidence-weighted ranking

Use cases:

* "How should I respond to this user now?"

---

### 5.4 Procedural Retrieval

* Skill matching
* Policy applicability checks
* Tool-routing

Use cases:

* "Which workflow applies under these constraints?"

**Further reading:**

* [https://langchain-ai.github.io/langgraph/](https://langchain-ai.github.io/langgraph/) (LangGraph)
* [https://arxiv.org/abs/2302.04761](https://arxiv.org/abs/2302.04761) (Toolformer)

---

## 6. Context Composition: From Memory to Action

### 6.1 Why Context Composition Matters

Naive agents stuff memory into prompts.

Mature agents **compile context**.

---

### 6.2 Structured Context Frames

A well-formed context separates concerns:

* System goals and constraints
* Semantic ground truths
* Relevant episodes
* Preferences
* Applicable procedures

This enables predictable behavior.

**Further reading:**

* [https://arxiv.org/abs/2307.03172](https://arxiv.org/abs/2307.03172) (Lost in the Middle: Context Position Effects)

---

## 7. Memory Decay

Memory should weaken before it disappears.

### 7.1 Decay Mechanisms

* Time-based decay
* Confidence decay
* Usage-based reinforcement
* Contextual validity

Decay reduces *influence*, not existence.

---

## 8. Memory Eviction

Eviction is a **governance decision**.

### 8.1 Eviction Triggers

* TTL expiry
* Superseded facts
* User revocation
* Policy violations
* Deprecated procedures

### 8.2 Eviction Techniques

* Tombstoning
* Version replacement
* Archival
* Redaction

**Further reading:**

* [https://www.nist.gov/privacy-framework](https://www.nist.gov/privacy-framework)

---

## 9. Taxonomy of Memory: Agent Memory vs RAG vs Tool Memory

### 9.1 Three Different Problems Often Confused

| Dimension       | RAG Memory                  | Tool Memory                | Agent Memory                   |
| --------------- | --------------------------- | -------------------------- | ------------------------------ |
| Primary purpose | Retrieve external knowledge | Invoke external capability | Accumulate cognition over time |
| Persistence     | Passive                     | External                   | Native to agent                |
| Time-awareness  | None                        | None                       | Explicit                       |
| Decay model     | None                        | N/A                        | Required                       |
| Governance      | Minimal                     | External                   | Core concern                   |

**RAG** answers *"What should I look up?"*
**Tools** answer *"What can I do now?"*
**Agent memory** answers *"What have I learned and how should it shape future behavior?"*

---

## Part II — Architectures

## 10. Observability and Auditability

Advanced systems must answer:

> *Why did the agent behave this way?*

This requires:

* Memory provenance
* Influence tracing
* Decision explanations

This is emerging as **Cognitive Audit Fabric** in enterprise systems.

---

## 10. Common Failure Modes

* Treating memory as RAG only
* No promotion path (episodic → semantic)
* No decay model
* No conflict resolution
* No ownership of memory domains

---

## 11. Where the Field Is Headed

* Memory as first-class infrastructure
* Domain-owned memory repositories
* Memory governance APIs
* Context compilers
* Agent-to-agent memory contracts

---

## 11. Reference Architectures

### 11.1 Memory Lifecycle (Conceptual Diagram)

```
[Signal/Event]
      ↓
[Salience Detection]
      ↓
[Memory Classification]
  ┌────┬─────┬────────┬─────────┐
  │Epi │Sem  │Pref    │Proc     │
  └────┴─────┴────────┴─────────┘
      ↓
[Polyglot Storage]
      ↓
[Retrieval + Ranking]
      ↓
[Context Compiler]
      ↓
[Action / Decision]
      ↓
[Reflection / Consolidation]
      ↺ (promotion / decay)
```

---

### 11.2 Episodic → Semantic Promotion Flow

```
[Episodic Events]
      ↓ (summarize)
[Candidate Facts]
      ↓ (validate / corroborate)
[Semantic Memory]
      ↓ (versioned)
[Knowledge Graph / Index]
```

Promotion is **deliberate**, not automatic.

---

### 11.3 Context Compiler Architecture

```
[Query / Goal]
      ↓
[Memory Retrievers]
  ├─ Semantic
  ├─ Episodic
  ├─ Preferences
  └─ Procedures
      ↓
[Relevance + Conflict Resolver]
      ↓
[Token Budgeter]
      ↓
[Structured Context Frame]
      ↓
[LLM / Agent Core]
```

Context is **compiled**, not concatenated.

---

## 12. Anti-Patterns in Agent Memory Systems

This chapter catalogs failure patterns that repeatedly show up in production agent deployments. Treat these as **design smells**—if you see one, expect reliability, safety, or cost problems soon.

### 12.1 “Memory = Top‑K Chunks”

**Symptom:** Every interaction does a vector search and blindly pastes results into the prompt.

**Why it fails:**

* Conflates *retrieval* with *memory*
* No provenance, no conflict handling
* High token cost, unstable behavior

**Fix:** Introduce a **context compiler** that (a) structures memory by type, (b) enforces quotas, (c) resolves conflicts, and (d) justifies inclusions.

---

### 12.2 No Promotion Path (Episodic → Semantic)

**Symptom:** The system keeps re-discovering the same facts, storing them only as conversations.

**Why it fails:**

* Episodic logs are not durable knowledge
* Repeated hallucination risk increases
* Hard to audit “what the system knows”

**Fix:** Add **consolidation jobs** that extract candidate facts, validate/corroborate them, then write versioned semantic records.

---

### 12.3 Unbounded Episodic Growth

**Symptom:** Memory stores grow forever; retrieval latency and cost creep up.

**Why it fails:**

* Recall becomes noisy
* Budget blowups
* Privacy risk increases with time

**Fix:** Time-partition episodic stores; apply **TTL + archival**; store structured summaries; keep raw traces in cold storage.

---

### 12.4 Preference Overfitting and “Sticky Mislearning”

**Symptom:** A single interaction causes a long-term preference change (tone, verbosity, decisions).

**Why it fails:**

* Preferences become brittle and surprising
* Hard to recover without manual edits

**Fix:** Treat preferences as **probabilistic** (confidence-weighted), require repeated evidence, and decay them without reinforcement.

---

### 12.5 No Conflict Resolution (Stale vs Fresh)

**Symptom:** The agent alternates between contradictory “truths” depending on retrieval.

**Why it fails:**

* Semantic records drift
* Preferences conflict with policies

**Fix:** Maintain explicit **versioning** and **freshness scoring**; implement a conflict resolver (newer wins, higher-confidence wins, policy wins).

---

### 12.6 Mixing Policy/Procedure into “Freeform Notes”

**Symptom:** Critical procedures (e.g., compliance steps) are stored as untyped text.

**Why it fails:**

* Not enforceable
* Not testable
* Not auditable

**Fix:** Store procedural memory as **executable or checkable artifacts**: workflows, DSLs, policies, and version-controlled playbooks.

---

### 12.7 Prompt Injection via Memory

**Symptom:** Retrieved memories contain instructions that override system constraints.

**Why it fails:**

* Memory becomes an adversarial channel

**Fix:** Separate **data** from **instructions**; sanitize retrieved text; enforce “instruction hierarchy”; use allowlists for tool/procedure selection.

---

### 12.8 No Provenance / “Why did you say that?”

**Symptom:** Agent can’t explain which memory influenced a decision.

**Why it fails:**

* Breaks trust
* Blocks debugging
* Blocks compliance

**Fix:** Capture **memory provenance**, retrieval scores, and context assembly logs.

---

## 13. Summary

Agent memory management is not about storage.

It is about **controlled cognition over time**.

Engineers who design memory deliberately will build agents that are:

* More reliable
* More explainable
* More scalable
* More trustworthy

---

## 14. Suggested Reading (Consolidated)

* Generative Agents: [https://arxiv.org/abs/2304.03442](https://arxiv.org/abs/2304.03442)
* ReAct: [https://arxiv.org/abs/2210.03629](https://arxiv.org/abs/2210.03629)
* Reflexion: [https://arxiv.org/abs/2303.11366](https://arxiv.org/abs/2303.11366)
* LangGraph (overview): [https://langchain-ai.github.io/langgraph/](https://langchain-ai.github.io/langgraph/)
* LangGraph Persistence: [https://langchain-ai.github.io/langgraph/concepts/persistence/](https://langchain-ai.github.io/langgraph/concepts/persistence/)
* LangGraph Memory: [https://langchain-ai.github.io/langgraph/concepts/memory/](https://langchain-ai.github.io/langgraph/concepts/memory/)
* CrewAI Memory: [https://docs.crewai.com/concepts/memory](https://docs.crewai.com/concepts/memory)
* AutoGen Memory: [https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/memory.html](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/memory.html)
* Lost in the Middle (context management): [https://arxiv.org/abs/2307.03172](https://arxiv.org/abs/2307.03172)
* Toolformer: [https://arxiv.org/abs/2302.04761](https://arxiv.org/abs/2302.04761)

---

## Appendix A — Memory Governance (Enterprise-Grade)

This appendix is a practical checklist for making memory safe, auditable, and operable in real systems.

### A.1 Governance Goals

* **User trust:** predictable use of remembered information
* **Safety:** prevent prompt injection and policy bypass
* **Privacy:** consent, minimization, and deletion
* **Compliance:** retention, audit trails, access control
* **Operational resilience:** versioning, rollbacks, incident response

---

### A.2 Memory Classification and Data Handling

Classify memory at ingestion:

* **PII / sensitive personal data** (names, phone, health, precise location)
* **Confidential business data** (contracts, financials, customer records)
* **Public / non-sensitive**

Controls by class:

* Encryption at rest + in transit
* Field-level redaction (mask or drop)
* Per-tenant isolation
* Strict retention defaults for sensitive classes

---

### A.3 Consent, Transparency, and User Controls

Minimum recommended features:

* **Explicit “remember / forget”** operations
* **Memory viewer** (what is stored, confidence, last used)
* **Deletion semantics:** hard delete for user-requested removal; tombstone + audit for system records
* **Scope controls:** per-app vs global; per-domain vs universal

---

### A.4 Access Control and Scoping

Model memory access like any other privileged data:

* Authentication + authorization
* Role-based access (RBAC) for operators
* Contextual scoping (only retrieve within user/app/tenant)
* Policy gating (procedural memory is often highest risk)

---

### A.5 Retention, Decay, and Legal Holds

* Default episodic TTL (e.g., 30–180 days) with archival options
* Prefer **summaries** over raw transcripts for long retention
* Semantic facts are **versioned** with effective dates
* Support legal holds and audit retention where required

---

### A.6 Provenance and Auditability

Store the following for every memory inclusion:

* Memory ID + type
* Source (conversation/tool/system) + timestamp
* Confidence / freshness
* Retrieval method and score
* Reason for inclusion (salience tag)

This enables:

* Debugging
* Compliance audits
* “Why did the agent do that?” answers

---

### A.7 Security Hardening: Memory as an Attack Surface

* Treat retrieved memory as **untrusted input**
* Strip/neutralize instructions inside retrieved text
* Enforce tool allowlists and policy precedence
* Rate-limit and monitor memory writes (poisoning attempts)

---

## Appendix B — Memory in Open-Source Agent Frameworks

This appendix highlights how two popular OSS agent frameworks model memory, with practical pros/cons.

### B.1 LangGraph (LangChain) — State, Threads, and Checkpointed Persistence

**What the framework provides**

* **Short-term memory** as part of the agent/graph **state**.
* **Persistence** via **checkpointers** that checkpoint graph state to a **thread** at each super-step, enabling resuming, time-travel, and post-run inspection.

**Primary references**

* LangGraph Persistence: [https://langchain-ai.github.io/langgraph/concepts/persistence/](https://langchain-ai.github.io/langgraph/concepts/persistence/)
* LangGraph Memory: [https://langchain-ai.github.io/langgraph/concepts/memory/](https://langchain-ai.github.io/langgraph/concepts/memory/)

**How it maps to the memory lifecycle**

* Identify: application-defined (you decide what to write into state)
* Store: state checkpoints (threaded)
* Retrieve: load thread state; optionally long-term memory stores
* Compose: state acts as the structured context carrier
* Decay/Evict: mostly application-owned (retention policies depend on your checkpointer backend)

**Pros**

* Strong **state-first** design encourages structured context
* Persistence enables **debugging**, **HITL**, and **resumability**
* Works well for deterministic workflows + agent loops

**Cons / gotchas**

* Long-term memory governance (decay/eviction, provenance) is largely **your responsibility**
* Without discipline, state can become an untyped “junk drawer”

---

### B.2 CrewAI — Built-in Memory Types + External Memory Providers

**What the framework provides**

* A “basic” memory system with multiple memory types (short-term, long-term, entity memory) and support for external memory providers.

**Primary references**

* CrewAI Memory: [https://docs.crewai.com/concepts/memory](https://docs.crewai.com/concepts/memory)
* CrewAI Crews: [https://docs.crewai.com/concepts/crews](https://docs.crewai.com/concepts/crews)

**How it maps to the memory lifecycle**

* Identify: framework-supported (agent/task interactions are candidates)
* Store: framework-managed stores + optional external providers
* Retrieve: injected as context during execution
* Compose: convenience-oriented; can be less explicit than a “context compiler”
* Decay/Evict: varies by provider; must be designed for production use

**Pros**

* Clear developer ergonomics: memory is a first-class concept
* Distinct memory types reduce “everything is a chunk” behavior

**Cons / gotchas**

* Production-grade governance (provenance, retention, redaction) depends on your chosen storage/provider
* Context assembly can become opaque if not instrumented

---

### B.3 (Optional) AutoGen — Memory as RAG Patterns and Ecosystem Extensions

AutoGen documents memory largely through a RAG lens ("retrieve useful facts and add to context") and supports ecosystem integrations.

**Primary references**

* AutoGen Memory: [https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/memory.html](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/memory.html)

**Commentary**

* Good fit for teams starting with RAG-centric “memory.”
* For full agent memory management, you will still need explicit lifecycle controls (promotion, decay, eviction, provenance).

---

### B.4 Semantic Kernel — Memory Stores, Skills, and Planner-Centric Context

**What the framework provides**

Semantic Kernel (SK) treats memory primarily as a **semantic recall system** integrated with skills and planners. Memory is externalized via **memory stores** (vector databases) and accessed through APIs such as `SaveInformationAsync` and `SearchAsync`.

Memory is typically:

* Semantic (facts, summaries, notes)
* Vector-based
* Skill- or planner-consumed rather than agent-state-centric

**Primary references**

* Semantic Kernel Vector Store Connectors: [https://learn.microsoft.com/en-us/semantic-kernel/concepts/vector-store-connectors/](https://learn.microsoft.com/en-us/semantic-kernel/concepts/vector-store-connectors/)
* Semantic Kernel Planning: [https://learn.microsoft.com/en-us/semantic-kernel/concepts/planning](https://learn.microsoft.com/en-us/semantic-kernel/concepts/planning)
* Semantic Kernel Overview: [https://learn.microsoft.com/en-us/semantic-kernel/](https://learn.microsoft.com/en-us/semantic-kernel/)

**How it maps to the memory lifecycle**

* **Identify:** Application-driven; developers decide what to write to memory (often summaries or extracted facts)
* **Store:** Vector memory stores (Azure AI Search, Qdrant, Pinecone, etc.)
* **Retrieve:** Similarity search scoped by collection / namespace
* **Compose:** Retrieved memories are injected into prompts via skills or planners
* **Decay:** Not native; must be implemented at the store or application layer
* **Evict:** Manual or store-level (TTL, deletion by key/collection)

**Pros**

* Clear, explicit APIs for semantic memory
* Strong alignment with enterprise .NET / Azure ecosystems
* Clean separation between skills, planners, and memory access

**Cons / gotchas**

* Memory is largely **semantic-only**; episodic and preference memory require custom modeling
* No built-in promotion, decay, or provenance model
* Context composition remains mostly prompt-oriented unless extended

**Architectural takeaway**

Semantic Kernel excels as a **semantic memory + skill orchestration layer**, but teams building long-lived agentic systems should:

* Add explicit episodic stores (event logs)
* Layer preference modeling separately
* Introduce a context compiler and governance controls above SK’s memory APIs
