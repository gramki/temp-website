# Agent Memory Management (Overview)

**Audience:** Agentic AI Engineers, Platform Architects, Applied AI Researchers  
**Scope:** How agent memory works, how to manage it safely, and where to find the detailed pages per memory type.

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

## 2. The Four Canonical Memory Types (navigation)

This primer uses the canonical four memory types. The detailed pages live alongside this doc:

- **Episodic memory**: [`episodic-memory.md`](./episodic-memory.md)
- **Semantic memory**: [`semantic-memory.md`](./semantic-memory.md)
- **Preference memory**: [`preference-memory.md`](./preference-memory.md)
- **Procedural memory**: [`procedural-memory.md`](./procedural-memory.md)

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

## 5. Retrieval + context building

Agent memory isn’t useful unless it can be retrieved and assembled into a turn’s reasoning context.

- **Context building / context compiler**: [`context-building.md`](./context-building.md)

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

## Appendix: moved into dedicated pages

- **Memory governance checklist**: [`governance.md`](./governance.md)
- **OSS framework memory patterns**: [`frameworks.md`](./frameworks.md)

