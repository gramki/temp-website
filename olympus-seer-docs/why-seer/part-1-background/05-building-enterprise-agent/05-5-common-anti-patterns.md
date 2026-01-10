# 5.5 Common Anti-Patterns

Building enterprise agents is difficult, and certain mistakes appear repeatedly across organizations. Understanding these anti-patterns—and their consequences—helps architects and engineers avoid months of painful debugging and rework.

## Cognitive Confusion Anti-Patterns

### Storage = Cognition

**The Pattern:** Assuming that where data lives determines its cognitive role. "It's in the warehouse, so it's knowledge." "It's in the vector store, so it's memory."

**Why It Happens:** Organizations often organize around storage systems rather than cognitive functions. Teams responsible for a database assume everything in it serves the same purpose.

**The Consequence:** Critical distinctions are lost. Derived metrics are treated as ground truth. Operational state is confused with institutional memory. Decision-making quality suffers because the agent cannot distinguish between what is authoritative and what is merely available.

**The Remedy:** Classify information by cognitive role, not storage location. Explicitly tag content with its source type. Design retrieval systems that preserve this classification.

### RAG = Memory

**The Pattern:** Treating retrieval-augmented generation (RAG) as a memory system. "We have RAG, so we have memory."

**Why It Happens:** RAG enables agents to access information beyond their training data, which *feels* like memory. The terminology overlap contributes to confusion.

**The Consequence:** RAG provides *knowledge access*, not *memory management*. RAG results are static documents; they do not evolve based on the agent's experience. There is no lifecycle, no decay, no promotion. Organizations that confuse RAG with memory fail to build the governance needed for true institutional learning.

**The Remedy:** Distinguish between knowledge retrieval (RAG) and memory management (episodic recording, semantic consolidation, procedural learning). Build separate systems for each.

### Top-K Chunks = Memory

**The Pattern:** Simulating memory by retrieving the K most similar chunks from a vector store and inserting them into the prompt.

**Why It Happens:** It's easy to implement. It appears to work in demos. The initial results seem reasonable.

**The Consequence:** This approach produces unstable prompts (small changes in the query can radically change retrieved content), high token costs (irrelevant content fills the context window), no provenance (the agent cannot explain why it knows something), and no governance (content is never validated, versioned, or expired).

**The Remedy:** Implement structured memory with explicit storage, retrieval, and lifecycle management. Treat retrieved content as candidates to be filtered and validated, not as ground truth to be injected directly.

## Authority Confusion Anti-Patterns

### Preferences as Policy

**The Pattern:** Allowing user preferences or agent observations to override binding constraints. "The user prefers this approach, so we'll skip the compliance check."

**Why It Happens:** Personalization is often prioritized over compliance. Preferences are easy to express; constraints are harder to enforce.

**The Consequence:** Regulatory violations. Audit failures. The agent learns that rules are negotiable. Preferences can change formatting or style; they cannot override policy.

**The Remedy:** Establish a clear precedence hierarchy in context compilation. System constraints always take priority. Preferences operate only within the space permitted by policy.

### Agent Memory Becomes Enterprise Truth

**The Pattern:** Allowing observations stored in agent memory to silently influence enterprise-wide behavior without validation. "The agent noticed this pattern, so now it applies to everyone."

**Why It Happens:** The boundaries between agent-local learning and institutional knowledge are not clearly defined or enforced.

**The Consequence:** Silent policy drift. An agent's local observation—possibly incorrect, possibly biased—becomes de facto organizational policy. This is especially dangerous when multiple agents share memory infrastructure without governance.

**The Remedy:** Implement a governed promotion path. Agent observations must be validated, reviewed, and explicitly approved before becoming enterprise knowledge. This process should be auditable.

### Policy Laundering

**The Pattern:** Repeated agent decisions silently become "rules" without formal governance. "We always do it this way now."

**Why It Happens:** Without explicit tracking, consistent behavior becomes implicit policy. No one made a decision to create a rule; it just emerged.

**The Consequence:** Unaccountable policy creation. When something goes wrong, there is no record of when the "policy" was established or who approved it. Compliance cannot validate rules that were never formally created.

**The Remedy:** All behavioral patterns that influence future decisions should be explicitly captured, reviewed, and promoted through governance processes. Implicit rules should be detected and formalized.

## Integration Anti-Patterns

### Pointing Agents at Raw OLTP/Logs

**The Pattern:** Giving agents direct access to operational databases and log files without semantic abstraction. "The agent can query the database directly."

**Why It Happens:** It's the fastest path to data access. Building semantic layers seems like unnecessary overhead.

**The Consequence:** No semantics (the agent must infer meaning from schema), no rationale (logs contain events but not reasoning), no audit trail (queries are not logged as cognitive events). The agent becomes dependent on database schema changes. Debugging is nearly impossible because there is no record of what the agent "thought."

**The Remedy:** Build semantic layers that provide meaningful abstractions. Log agent reasoning alongside data access. Treat tool calls as auditable events.

### Unbounded Context Windows

**The Pattern:** Attempting to simulate memory by dumping entire session transcripts, all retrieved documents, and extensive conversation history into the context window.

**Why It Happens:** Larger context windows enable more content. It seems logical to include everything potentially relevant.

**The Consequence:** High token costs. Reduced reasoning quality ("lost in the middle" phenomena where agents lose track of information in the middle of large contexts). Unpredictable behavior. Inability to explain what information was actually used.

**The Remedy:** Compile context deliberately. Allocate token budgets by section. Include only information that changes the decision. Summarize rather than dump.

## Learning and Improvement Anti-Patterns

### No Promotion Path

**The Pattern:** Agents rediscover the same patterns repeatedly because there is no mechanism to consolidate learnings into semantic memory.

**Why It Happens:** The focus is on immediate task completion, not on continuous improvement. Memory systems are not designed for consolidation.

**The Consequence:** Wasted computation. Inconsistent behavior across sessions. Failure to capture institutional learning. Agents remain perpetually naive despite accumulated experience.

**The Remedy:** Build promotion pathways. Detect repeated patterns and consolidate them. Govern the promotion of hypotheses to validated beliefs.

### No Feedback Attribution

**The Pattern:** Collecting feedback without tracking who provided it, in what context, or with what authority.

**Why It Happens:** Feedback systems focus on the signal itself, not on provenance. "Thumbs up/down" is easy to implement.

**The Consequence:** Untraceable learning. When agent behavior changes unexpectedly, there is no way to identify which feedback caused it. Malicious or incorrect feedback cannot be identified and removed.

**The Remedy:** Log feedback with full context: who, when, what authority, what the agent was doing, what the outcome was. Treat feedback as an auditable event.

---

**References:**
*   `olympus-seer-docs/agentic-ai-concepts/designing-an-agent.md`
*   `olympus-seer-docs/agentic-ai-concepts/agent-memory/agent-memory-management.md`
