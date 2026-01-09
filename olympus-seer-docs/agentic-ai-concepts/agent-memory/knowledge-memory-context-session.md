# Agent Fundamentals: Knowledge vs Session vs Memory vs Context

> **Audience:** Engineers building or integrating AI agents  
> **Goal:** Establish precise, non‑ambiguous meanings for four commonly confused terms

### Related Documents

- **[Primer on Agent Memory Management](./agent-memory-management.md)** — Deep dive into memory types, lifecycle, and governance
- **[Raw, Trained, Employed Agents](../../aosm-meta-model/raw-trained-employed-agents.md)** — How these concepts map to agent layers

---

## TL;DR

* **Knowledge** → What the agent can *look up*
* **Session** → The *interaction boundary* and continuity handle
* **Memory** → What the agent *remembers over time*
* **Context** → What the agent is *thinking with right now*

---

## 1. Knowledge

**Definition**
Knowledge is **authoritative information stored outside the agent** and retrieved on demand.

**Examples**

* Documents, PDFs, policies
* Databases, APIs
* Enterprise systems (CRM, ERP, ticketing)
* Grounded external facts

**Key Properties**

* Exists independently of the agent
* Shared across agents
* Not modified by reasoning
* Retrieved only when needed

**Mental Model**
📚 *Library / Database*

---

## 2. Session

**Definition**
A session is a **logical interaction boundary** that groups multiple turns between a user (or system) and an agent.

**What a Session Contains**

* Session ID
* User / actor identity
* Channel (web, API, voice)
* Conversation transcript
* Security and auth context
* Start/end timestamps

**Key Properties**

* Long‑lived (minutes → days)
* Persisted
* Append‑only
* Does **not** reason

**Mental Model**
📦 *Envelope / Folder*

---

## 3. Memory

**Definition**
Memory is **information the agent chooses to retain across interactions** because it may be useful later.

**Examples**

* User preferences
* Past decisions or outcomes
* Learned constraints
* Summaries of prior interactions

**Types of Memory**

* *Episodic* — what happened
* *Semantic* — what is true
* *Preference* — what is liked
* *Procedural* — how to do things

**Key Properties**

* Long‑term
* Agent‑owned
* Selectively retrieved
* Mutable (can be summarized or revised)

**Mental Model**
🗒️ *Agent’s notebook*

---

## 4. Context

**Definition**
Context is the **ephemeral working state assembled for a single reasoning step or turn**.

**What Context Includes**

* Current user input
* Recent conversation snippets
* Retrieved memory
* Retrieved knowledge
* Tool outputs
* Intermediate plans or variables

**Key Properties**

* Very short‑lived (milliseconds → seconds)
* Token‑bound
* Highly mutable
* Discarded after execution

**Mental Model**
🧠 *RAM / working memory*

---

## How They Relate

```
User Input
   ↓
Session (boundary)
   ↓
Context ← selective Memory + queried Knowledge
   ↓
Agent Reasoning
   ↓
(Optional) Memory update
```

* A **session spans many contexts**
* A **context never spans sessions**
* Knowledge is *queried*, not remembered
* Memory is *chosen*, not automatic

---

## Side‑by‑Side Comparison

| Dimension   | Knowledge     | Session              | Memory           | Context   |
| ----------- | ------------- | -------------------- | ---------------- | --------- |
| Purpose     | Look up facts | Interaction boundary | Recall over time | Think now |
| Lifetime    | Independent   | Minutes → days       | Days → years     | Seconds   |
| Persisted   | Yes           | Yes                  | Yes              | No        |
| Owned by    | System        | Platform             | Agent            | Runtime   |
| Token‑bound | On demand     | No                   | Sometimes        | Yes       |

---

## Common Mistakes to Avoid

* Calling RAG **memory** (it is knowledge access)
* Dumping full session transcripts into context
* Treating memory as immutable truth
* Blurring session data with reasoning state

---

## One‑Line Rules (Memorize These)

* *If the agent must look it up → Knowledge*
* *If it defines interaction continuity → Session*
* *If the agent learned it from experience → Memory*
* *If the agent is using it right now → Context*

---

## Final Takeaway

> **Sessions organize interactions. Context enables reasoning. Memory enables continuity. Knowledge enables grounding.**

Keeping these concepts cleanly separated is essential for scalable, auditable, and high‑quality agent systems.

