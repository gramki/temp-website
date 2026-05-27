# Enterprise Knowledge vs Enterprise Memory vs Agent Memory

**Purpose of this note**
This document clarifies three concepts that are frequently conflated in AI, data, and platform discussions:

* **Enterprise Knowledge**
* **Enterprise Memory**
* **Agent Memory**

The goal is not terminology purity. The goal is **architectural correctness**—so that systems are designed, governed, and evolved without hidden cognitive gaps.

This note is intended to be **iterative**.

---

## 1. Why This Comparison Matters Now

In pre-AI enterprises, the distinction between knowledge and memory was mostly academic. Human cognition filled the gaps implicitly.

Agentic AI removes that safety net.

When agents:

* act autonomously,
* make decisions,
* learn over time, and
* must be audited,

then **what is remembered, how it is remembered, and who owns that memory** becomes a first‑order design concern.

---

## 2. Enterprise Knowledge

### 2.1 Definition

**Enterprise Knowledge** is the set of **codified, curated, and asserted truths** an organization recognizes as authoritative at a point in time.

It answers the question:

> *“What does the enterprise believe to be true or correct?”*

---

### 2.2 Core Characteristics

| Dimension        | Enterprise Knowledge        |
| ---------------- | --------------------------- |
| Nature           | Declarative, referential    |
| Time-awareness   | Weak (versioned snapshots)  |
| Mutability       | Slow, governed              |
| Confidence model | Asserted / approved         |
| Ownership        | Explicit (teams, functions) |
| Structure        | Schemas, documents, graphs  |
| Validation       | Human review + governance   |
| Failure mode     | Staleness, irrelevance      |

---

### 2.3 Typical Artifacts

* Policies and SOPs
* Data dictionaries
* Product definitions
* Risk rules
* Architecture standards
* Master data records

---

### 2.4 Typical Systems

Enterprise Knowledge does not live in a single kind of system. It is **asserted and curated across multiple system types**, some of which are traditionally thought of as “data systems.”

Typical systems that *host or operationalize* Enterprise Knowledge include:

* Knowledge graphs
* Wikis / documentation portals
* Policy repositories
* Master Data Management (MDM) systems
* **Data warehouses and data marts (when they store asserted, governed facts and metrics)**
* Reference data services
* Metadata and semantic layer systems

**Important clarification**
Data warehouses and marts are included **only insofar as they contain asserted, semantically owned knowledge** (for example: canonical KPIs, approved dimensions, reference tables).

They are *not* knowledge systems by default; they are **analytical substrates** that can host knowledge artifacts once meaning, ownership, and governance are explicitly attached.

---

### 2.5 Where OLTP Systems Fit (and Why They Are Often Misclassified)

OLTP systems (core banking systems, ERPs, CRMs, order-management systems) are frequently—and incorrectly—treated as enterprise *knowledge* or *memory* systems.

This confusion arises because OLTP systems are **authoritative for operational state**. Authority, however, is not cognition.

From a cognitive standpoint, OLTP systems are **systems of record for events and state**, not systems of belief, learning, or reasoning.

**What OLTP systems actually capture**

* Transactions and events ("this payment occurred")
* Current state derived from past events ("this account balance is X")
* Embedded business logic, policies, rules, and configurations

**What OLTP systems do *not* capture**

* Why a decision was taken
* What alternatives were considered
* What evidence was weighed
* Whether an action was an exception or override
* How understanding evolved over time

**Cognitive classification of OLTP data**

| OLTP Content                                             | Cognitive Role                           |
| -------------------------------------------------------- | ---------------------------------------- |
| Transaction records                                      | Source events for Enterprise Memory      |
| State tables                                             | Snapshot of memory-derived state         |
| Embedded business logic, policies, rules, configurations | Implicit policy (not explicit knowledge) |

**Key clarification**
OLTP systems are **inputs into Enterprise Memory and Derived Knowledge Artifacts**. They are *not* themselves memory systems, and they are *not* systems of enterprise belief.

This distinction is foundational for:

* agent reasoning
* auditability
* explainability
* institutional learning


OLTP systems therefore:

* Are **inputs to Enterprise Memory**, not memory themselves
* Are **sources for Derived Knowledge Artifacts**, not knowledge of record
* are **authoritative for operational state**

They do **not**:

* explain rationale
* capture decision intent
* retain historical supersession cleanly

For agentic and audit-heavy systems, OLTP data must be **interpreted and contextualized** before it becomes memory or knowledge.

---

### 2.6 What Enterprise Knowledge Is *Not*

* It is not experiential
* It does not capture rationale or causality
* It does not evolve automatically from usage
* It cannot explain *why* a decision was made

---

## 3. Enterprise Memory

With the role of OLTP systems clarified, we can now precisely define what *Enterprise Memory* actually is.

Before going deeper, it is important to clarify where **OLTP systems** fit, since they are often incorrectly assumed to be either knowledge or memory systems.

---


### 3.1 Definition

**Enterprise Memory** captures the organization’s **lived cognition over time**:

* what happened,
* what was decided,
* why it was decided,
* with what evidence,
* and how it influenced future behavior.

It answers the question:

> *“What did we experience and learn, and how did it shape our actions?”*

---

### 3.2 Core Characteristics

| Dimension        | Enterprise Memory            |
| ---------------- | ---------------------------- |
| Nature           | Experiential, causal         |
| Time-awareness   | Fundamental                  |
| Mutability       | Append-only, superseding     |
| Confidence model | Probabilistic                |
| Ownership        | Often implicit / distributed |
| Structure        | Events, traces, records      |
| Validation       | Emergent, corroborated       |
| Failure mode     | Noise, amnesia               |

---

### 3.3 Typical Artifacts

* Decision records
* Incident timelines
* Exception and override logs
* Investigations and postmortems
* Customer interaction histories
* Model explanations and rationales

---

### 3.4 Typical Systems

* Event stores
* Case management systems
* Workflow engines
* Observability stacks
* Audit logs (extended)

---

### 3.5 What Enterprise Memory Is *Not*

* It is not curated truth
* It is not always correct
* It is not optimized for lookup alone
* It is not inherently safe without governance

---

## 4. Agent Memory

### 4.1 Definition

**Agent Memory** is the **operational, scoped, and actionable memory** used by an agent to:

* maintain continuity,
* adapt behavior,
* personalize responses,
* and improve decision quality over time.

It answers the question:

> *“Given what I have experienced, how should I act now?”*

---

### 4.2 Core Characteristics

| Dimension        | Agent Memory                                              |
| ---------------- | --------------------------------------------------------- |
| Nature           | Tactical, contextual                                      |
| Time-awareness   | Explicit and fine-grained                                 |
| Mutability       | Fast, decay-driven                                        |
| Confidence model | Heuristic / weighted                                      |
| Ownership        | Agent- or platform-owned                                  |
| Structure        | Typed memory (episodic, semantic, preference, procedural) |
| Validation       | Continuous, feedback-driven                               |
| Failure mode     | Drift, overfitting                                        |

---

### 4.3 Typical Memory Types

* **Episodic:** interactions, events
* **Semantic:** facts promoted from experience
* **Preference:** learned or stated biases
* **Procedural:** workflows, skills, policies

---

### 4.4 Typical Systems

* Agent frameworks (LangGraph, CrewAI, Semantic Kernel)
* Vector stores
* Agent state machines
* Memory services embedded in platforms

---

### 4.5 What Agent Memory Is *Not*

* It is not the system of record
* It is not enterprise‑wide truth
* It cannot substitute governance
* It should not be unbounded

---

## 5. Side-by-Side Comparison

| Axis             | Enterprise Knowledge | Enterprise Memory    | Agent Memory             |
| ---------------- | -------------------- | -------------------- | ------------------------ |
| Primary question | What is true?        | What happened & why? | How should I act now?    |
| Temporal depth   | Low                  | High                 | Medium–high              |
| Scope            | Organization-wide    | Organization-wide    | Agent / context-specific |
| Stability        | High                 | Medium               | Low–medium               |
| Governance       | Strong, formal       | Weak–emerging        | Platform-enforced        |
| Update model     | Edit & approve       | Append & supersede   | Learn & decay            |
| Used by          | Humans, systems      | Humans, agents       | Agents                   |
| Explains         | Policy & facts       | Decisions & outcomes | Behavior                 |

---

## 6. Enterprise Memory in Agentic Systems

Agent Memory is operational—it helps agents act in the moment. Enterprise Memory is institutional — it captures what the organization learned from agent actions.

In an agentic world, **Enterprise Memory becomes the institutional learning layer** that enables:

* Governance and auditability
* Cross-agent learning
* Human-agent collaboration
* Institutional continuity

---

### Enterprise Memory as Part of Agent Decision Context

A common misconception is that an agent's decision context includes only **Agent Memory** (local, session-scoped) and **Enterprise Knowledge** (policies, rules, facts).

This is incomplete. A well-formed agent decision context draws from **three sources**:

| Source | What the Agent Asks | Nature |
|--------|---------------------|--------|
| **Enterprise Knowledge** | *"What should I do?"* | Normative — rules, policies, approved facts |
| **Enterprise Memory** | *"What has been done?"* | Historical — precedent, outcomes, exceptions |
| **Agent Memory** | *"What have I been doing?"* | Operational — session state, recent interactions |

**Why this matters:**

* Enterprise Knowledge tells the agent **what is permitted or required**
* Enterprise Memory tells the agent **what has happened before and how it turned out**
* Agent Memory tells the agent **what is happening now**

Without Enterprise Memory in context, agents cannot:

* Recognize precedent
* Learn from institutional experience
* Continue where others left off
* Calibrate risk based on historical outcomes

**Architectural implication:** The Context Assembly Engine must treat Enterprise Memory as a first-class context source, not an afterthought.

---

This section details specific use cases for Enterprise Memory in agentic systems.

---

### 6.1 Audit, Compliance, and Explainability

When regulators or internal audit ask *"Why did this decision happen?"*, Agent Memory cannot answer. It is ephemeral, scoped to a session, and may have decayed.

Enterprise Memory captures:

* The decision that was made
* The evidence and context available at decision time
* The reasoning or rationale (if captured)
* Who (human or agent) was accountable
* Whether an override or escalation occurred

**Use case:** A credit decision agent denies a loan. Six months later, the customer disputes. Enterprise Memory provides the full decision record—not just the outcome, but the inputs, rules applied, and confidence level.

---

### 6.2 Cross-Agent Learning

Agent Memory is local. What one agent learns stays with that agent.

Enterprise Memory enables **institutional learning across agents**:

* Patterns discovered by one agent become available to others
* Exception-handling approaches propagate across the organization
* Model improvements are informed by collective experience

**Use case:** A fraud detection agent identifies a new evasion pattern. The pattern is promoted to Enterprise Memory and eventually to Enterprise Knowledge (a new rule). Other agents—and human analysts—benefit immediately.

---

### 6.3 Human-Agent Collaboration and Handoffs

When humans need to pick up where an agent left off—or vice versa—they need shared memory.

Agent Memory is agent-private. Enterprise Memory is the **shared context layer** for Human-AI Teams.

**Use case:** An agent handles a customer complaint overnight, gathering information and attempting resolution. The next morning, a human specialist reviews the case. Enterprise Memory provides the full interaction history, decisions attempted, and outcomes—so the human doesn't start from scratch.

---

### 6.4 Institutional Continuity Across Agent Lifecycles

Agents are versioned, retired, and replaced. Agent Memory may not survive these transitions.

Enterprise Memory ensures **the institution remembers even when agents change**.

**Use case:** An underwriting agent is upgraded from v2 to v3 with a new model. Historical decisions made by v2 remain in Enterprise Memory, enabling comparison, regression detection, and continuity of service.

---

### 6.5 Exception and Override Pattern Recognition

When agents encounter ambiguous situations, past exceptions are invaluable.

Enterprise Memory captures:

* What the original decision was
* That an exception was granted
* Why the exception was justified
* The outcome of the exception

This allows future agents (and humans) to recognize similar situations.

**Use case:** A payment agent flags a transaction as suspicious, but a human overrides and approves it with a rationale. Enterprise Memory records this override. When similar transactions appear, the agent can surface the precedent—or the pattern can be promoted to policy.

---

### 6.6 Multi-Agent Coordination

In multi-agent systems, agents must share context beyond their individual sessions.

Enterprise Memory provides the **coordination substrate**:

* What did the upstream agent decide?
* What evidence was gathered by other agents in this workflow?
* What is the current state of the shared task?

**Use case:** A customer onboarding workflow involves identity verification, risk assessment, and account provisioning—each handled by different agents. Enterprise Memory ensures each agent has access to prior decisions and can explain the full workflow history.

---

### 6.7 Postmortem, Root Cause Analysis, and Continuous Improvement

When things go wrong, Enterprise Memory provides the **forensic trail**.

Agent Memory may have decayed or been scoped too narrowly. Enterprise Memory captures:

* The sequence of decisions across agents and humans
* What information was available at each step
* Where the failure or drift occurred

**Use case:** A customer receives an incorrect bill due to a cascading error across multiple agents. Enterprise Memory enables tracing the root cause back to the originating decision and identifying which agent (or human) made the error.

---

### 6.8 Training Data and Model Improvement

Enterprise Memory is a **curated source of real-world decisions and outcomes**.

Unlike raw logs or OLTP data, Enterprise Memory captures:

* Intent and rationale (not just transactions)
* Outcome quality (success, failure, escalation)
* Edge cases and exceptions

This makes it valuable for:

* Fine-tuning agent models
* Reinforcement learning from human feedback (RLHF)
* Evaluation benchmark creation

**Use case:** An agent evaluation suite is built from Enterprise Memory—using real decisions with known outcomes to test whether new agent versions would have made better choices.

---

### 6.9 Summary: Where Enterprise Memory Fits in Agentic Architecture

| Layer | Role | Scope | Persistence |
|-------|------|-------|-------------|
| **Agent Memory** | Operational continuity | Agent / session | Ephemeral |
| **Enterprise Memory** | Institutional cognition | Organization | Durable |
| **Enterprise Knowledge** | Asserted truth | Organization | Versioned |

Promotion flow:

```
Agent Memory → Enterprise Memory → Enterprise Knowledge
   (local)         (shared)           (governed)
```

Enterprise Memory is the **missing middle layer** that makes agentic systems:

* Auditable
* Learnable
* Collaborative
* Institutionally durable

---

## 7. Where Do Data Warehouses, Data Marts, and Data Lakes Fit?

This section demystifies a frequent source of confusion: **storage and processing architectures are not cognitive categories**. Enterprises often mistake *where data lives* (lake, warehouse) for *what the data represents* (knowledge or memory).

---

### 7.1 Data Warehouses and Data Marts

**What they are**
Data warehouses and data marts are **analytical storage and processing systems** optimized for:

* structured data
* historical aggregation
* reporting and analytics

They answer questions like:

* "What were our revenues last quarter?"
* "How many incidents occurred by category?"

**What they are not**
They are not inherently knowledge or memory systems.

**How they map cognitively**

| Warehouse / Mart Content    | Cognitive Classification              |
| --------------------------- | ------------------------------------- |
| Curated dimensions, metrics | Enterprise Knowledge                  |
| Historical fact tables      | Raw Enterprise Memory (uninterpreted) |
| Aggregated KPIs             | Derived Knowledge                     |

A warehouse typically contains:

* **Frozen summaries of past events** (memory-derived)
* **Curated schemas and metrics** (knowledge-like)

But it does **not** preserve:

* rationale
* causality
* decision context

---

### 7.2 Data Lakes and Lakehouses

**What they are**
Data lakes are **storage substrates**, not semantic constructs.

They optimize for:

* low-cost storage
* schema-on-read
* heterogeneous data (logs, events, files)

They answer no cognitive question by themselves.

**Key clarification**

> A data lake is *where data rests*, not *what the data means*.

**How they map cognitively**

| Lake Content        | Cognitive Classification   |
| ------------------- | -------------------------- |
| Raw logs, events    | Proto–Enterprise Memory    |
| Snapshots, extracts | Potential Knowledge inputs |
| ML features         | Neither (derived signals)  |

Without additional structure, lakes are:

* **pre-memory** (raw experience)
* **pre-knowledge** (unvalidated signals)

---

### 7.3 Storage ≠ Semantics ≠ Cognition

A critical distinction:

* **Storage architecture** answers: *How is data stored and processed?*
* **Semantic organization** answers: *What does this data represent?*
* **Cognitive classification** answers: *How does this data influence decisions over time?*

These axes are orthogonal but often conflated.

---

### 7.4 Reclassifying Enterprise Data Through a Cognitive Lens

To resolve common ambiguities, we introduce a **three-tier cognitive classification** rather than a binary one.

#### Tier 1 — Asserted Enterprise Knowledge

* Explicitly owned and governed
* Semantically stable
* Approved as *knowledge of record*
* Reusable across contexts

Examples:

* Policies and rules
* Canonical definitions
* Approved KPIs (with owned semantics)
* Reference and master data

---

#### Tier 2 — Derived Knowledge Artifacts

* Computed from enterprise memory
* Optimized for specific use cases or consumers
* Contextual, time-bound, and assumption-heavy
* Knowledge in a **functional sense**, not necessarily of record

Examples:

* Aggregated metrics and dashboards
* Fact tables (interpreted)
* Risk scores
* Feature views and feature stores

These artifacts **become Enterprise Knowledge only when explicitly asserted, governed, and stabilized**.

---

#### Tier 3 — Signals (Pre‑Knowledge)

* High-variance, model- or task-dependent
* Often non-interpretable
* Designed for utility, not explanation

Examples:

* Raw ML features
* Embeddings
* Telemetry-derived signals

---

### Updated Cognitive Classification Table

| Enterprise Data           | Asserted Knowledge  | Derived Knowledge Artifact  | Signal        |
| ------------------------- | ------------------- | -------------------------- | ------------- |
| Policies, rules           | ✓                   | –                          | –             |
| Canonical definitions     | ✓                   | –                          | –             |
| Reference data            | ✓                   | –                          | –             |
| Approved KPIs             | ✓                   | –                          | –             |
| Aggregated metrics        | –                   | ✓                          | –             |
| Fact tables               | –                   | ✓                          | –             |
| Risk / propensity scores  | –                   | ✓                          | –             |
| Decision records          | –                   | ✓                          | –             |
| Event logs                | –                   | ✓                          | –             |
| Feature views             | –                   | ✓                          | –             |
| Raw ML features           | –                   | –                          | ✓             |
| Embeddings                | –                   | –                          | ✓             |
| ML features               | –                   | –                          | ✓             |
| Raw telemetry / logs      | –                   | ✓ (proto)                  | ✓             |

---

### 7.5 Why Warehouses Feel Like Memory (but Aren't)

Warehouses feel memory-like because they store *history*.

But they lack:

* intent
* causality
* explanation
* linkage to decisions

They are **archives**, not memory.

Memory requires:

* narrative structure
* temporal reasoning
* confidence and supersession
* traceability to action

---

### 7.6 Implications for Agentic and Enterprise AI

* Do not point agents directly at raw lakes or warehouses
* Promote curated facts into **Enterprise Knowledge**
* Extract decisions, overrides, and rationales into **Enterprise Memory**
* Use warehouses as **analytical substrates**, not cognitive stores

---

## 8. How the Three Should Work Together

A healthy architecture separates responsibilities:

* **Enterprise Knowledge** provides ground truth and constraints
* **Enterprise Memory** captures institutional cognition
* **Agent Memory** enables local adaptation and continuity
* **Warehouses/Lakes** provide analytical and storage substrates (not cognitive systems)

Promotion paths are deliberate:

* Agent memory → Enterprise memory (decisions, outcomes)
* Enterprise memory → Enterprise knowledge (validated learning)
* Warehouses/Lakes → Knowledge or Memory (via interpretation and governance)

---

### 8.1 Anti-Pattern: Treating Knowledge as Memory

* Wikis used to explain incidents
* Policies used to justify exceptions

Result: loss of rationale, repeated mistakes.

---

### 8.2 Anti-Pattern: Treating Memory as Knowledge

* Decisions treated as permanent truth
* One-off overrides becoming policy

Result: drift, inconsistency, policy erosion.

---

### 8.3 Anti-Pattern: Treating Agent Memory as Enterprise Memory

* Agent-local learning without institutional capture
* No promotion or audit trail

Result: organizational amnesia, ungoverned AI behavior.

---

## 9. Implications for Architecture and Governance

* Do not overload one system to do all three jobs
* Design explicit promotion and decay paths
* Assign ownership at the correct layer
* Expect memory to require governance, not just storage

---

## 10. Why This Leads Naturally to Cognitive Audit Fabric (CAF)

CAF emerges as the **connecting tissue**:

* It does not replace knowledge systems
* It does not store raw agent memory
* It governs how memory is captured, linked, explained, and audited

CAF makes enterprise memory **legible and defensible**.

---

## 11. Closing Thought

Enterprises have spent decades managing *knowledge*.

The next decade will be about managing *memory* —human, machine, and hybrid.

Agentic AI makes this unavoidable.

---

## 12. Foundational Definitions: Truth, Semantics, Knowledge, and Memory

These terms are often used interchangeably in enterprise discourse, but they play **distinct cognitive roles**. Keeping them separate is a prerequisite for agentic and audit-grade systems.

### 12.1 Truth

**Truth** is an **asserted commitment** by the enterprise.

Truth answers:

> *“What does the enterprise commit to treating as correct and binding?”*

**Properties**

- Asserted (not inferred)
- Owned by an authority (function, committee, regulator)
- Normative (constrains behavior)
- Stable until explicitly revised
- Versioned (not probabilistic)

**Examples**

- A risk policy
- A canonical definition of a KPI
- An approved eligibility rule

Truth is not required to be perfect. It is required to be **declared**.

### 12.2 Semantics

**Semantics** provide **meaning and interpretation**.

Semantics answer:

> *“What does this symbol, value, or rule mean in context?”*

**Properties**

- Interpretive (not normative)
- Often shared across domains
- Can exist without assertion
- Enables translation across systems

**Examples**

- Column meaning in a data catalog
- Business meaning of a metric
- Ontologies and taxonomies

Semantics do **not** constrain behavior by themselves. They enable understanding.

### 12.3 Knowledge

**Knowledge** is **truth plus semantics**, stabilized for reuse.

Knowledge answers:

> *“What is true, and what does it mean?”*

**Properties**

- Declarative
- Governed
- Reusable across contexts
- Intended to inform and constrain decisions

**Examples**

- Policies with defined scope and meaning
- Canonical metrics with agreed definitions
- Reference data with business semantics

### 12.4 Relationship Between Truth, Semantics, and Knowledge

The relationship can be expressed as:

```
Knowledge = Truth × Semantics
```

- Truth without semantics is unusable
- Semantics without truth is unbinding
- Knowledge requires both

### 12.5 Knowledge vs Semantic Memory (Critical Distinction)

Semantic memory may inform revisions to knowledge, but it is not knowledge by default.

| Aspect          | Enterprise Knowledge | Semantic Memory (Learned)    |
| --------------- | -------------------- | ---------------------------- |
| Source          | Assertion            | Experience                   |
| Confidence      | Declared             | Probabilistic                |
| Temporal nature | Stable (versioned)   | Evolves (decay/supersession) |
| Governance      | Formal               | Analytical + review-based    |
| Role            | Constrain action      | Inform action                |

### 12.6 How ESPP Memory Relates to Truth and Knowledge

| Memory type  | Relation to Truth              | Relation to Knowledge                    |
| ----------- | ------------------------------ | ---------------------------------------- |
| Episodic    | May violate truth (exceptions) | Evidence for review                      |
| Semantic    | Challenges/refines truth       | Candidate for promotion                  |
| Procedural  | Operationalizes truth          | May diverge from it (drift)              |
| Preference  | Reveals gaps in truth          | Signals misalignment and prompts review  |

Truth constrains memory going forward. Memory pressures truth to evolve (deliberately).

---

## 13. Vocabulary Mapping Across Enterprise Data, Cognition, and Systems

Enterprises simultaneously use:

1. **Operational / OLTP terminology** (systems of record)
2. **Data & analytics terminology** (lakes, warehouses, marts)
3. **Common enterprise practice terminology** (colloquial usage)
4. **Cognitive systems terminology** (memory, knowledge, learning)
5. **ETSL / CAF terminology** (intentional, governance-oriented constructs)

Each vocabulary evolved to solve a different problem. Confusion arises when terms are mixed without translation.

### 13.1 The five vocabulary groups (what each optimizes for)

| Vocabulary group          | Primary optimization                     |
| ------------------------- | ---------------------------------------- |
| OLTP / Operations         | Correctness of transactions and state    |
| Data platforms            | Analytical performance and reuse         |
| Common enterprise usage   | Convenience and familiarity              |
| Cognitive systems         | Reasoning over time                      |
| ETSL / CAF                | Auditability, explainability, governance |

### 13.2 Core term mapping (side-by-side)

| Common term  | OLTP / ops meaning       | Data platform meaning | Cognitive meaning        | ETSL / CAF interpretation |
| ------------ | ------------------------ | --------------------- | ------------------------ | ------------------------- |
| Transaction  | Atomic state change      | Fact row              | Episodic signal          | Source event              |
| Record       | Row in table             | Row / document        | Memory fragment          | Evidence element          |
| History      | Past rows                | Time-series data      | Episodic memory          | Event lineage             |
| Policy       | Code/config rule         | Reference table       | Knowledge constraint     | Asserted knowledge        |
| Rule         | Conditional logic        | Filter / transform    | Constraint               | Policy artifact           |
| SOP          | Document                 | Unstructured text     | Procedural memory        | Procedural artifact       |
| Metric       | Calculated value         | Aggregate             | Derived knowledge        | Knowledge artifact        |
| Feature      | Input variable           | Feature column        | Signal                   | Derived signal            |
| State        | Current value            | Snapshot              | Memory-derived state     | Observed state            |
| Exception    | Error / override         | Outlier               | Preference signal        | Override record           |

### 13.3 Storage systems vs cognitive meaning (explicit decoupling)

| Storage system  | What it stores            | Cognitive role                           |
| --------------- | ------------------------- | ---------------------------------------- |
| OLTP DB         | Transactions, state       | Memory source (pre-cognitive)            |
| Event store     | Ordered events            | Episodic memory substrate                |
| Data lake       | Raw data                  | Proto-memory / proto-knowledge           |
| Warehouse       | Curated tables            | Derived knowledge artifacts               |
| Knowledge graph | Entities, relations       | Enterprise knowledge                     |
| Wiki / docs     | Text artifacts            | Often procedural memory                  |
| Vector store    | Embeddings                | Retrieval index (not memory by itself)   |

Key principle:

> **Storage systems do not define cognition; interpretation does.**

### 13.4 A practical translation rule (use this)

When you hear a term, ask:

1. *What system is this term coming from?*
2. *What decision is this term supposed to influence over time?*

Then map it:

- If it influences **beliefs and constraints** → Knowledge
- If it influences **future decisions via experience** → Memory
- If it influences **execution only** → Procedure / signal

### 13.5 Why ETSL / CAF needs its own vocabulary

ETSL/CAF terms (e.g., `DecisionRecord`, `EvidenceBundle`, `OverrideRecord`, `ExplanationRecord`) are not replacements for existing enterprise terms.

They exist to:

- make cognition explicit
- preserve causality
- support audits
- link actions to rationale

They form a meta-vocabulary that can reference OLTP, data, and knowledge systems without being trapped by any one of them.

---

## Appendix: further reading (now organized by memory type)

The “further reading” lists are maintained alongside the per-type Enterprise Memory pages:

- [./enterprise-memory/episodic-memory.md](./enterprise-memory/episodic-memory.md)
- [./enterprise-memory/semantic-memory.md](./enterprise-memory/semantic-memory.md)
- [./enterprise-memory/procedural-memory.md](./enterprise-memory/procedural-memory.md)
- [./enterprise-memory/preference-memory.md](./enterprise-memory/preference-memory.md)
- Cross-cutting: [./enterprise-memory/README.md](./enterprise-memory/README.md)
