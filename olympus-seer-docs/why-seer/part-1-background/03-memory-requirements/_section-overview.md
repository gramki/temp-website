# Section 3: Memory Requirements for Enterprise Agents — Overview

*Why memory governance is essential, and what taxonomy and lifecycle controls enterprise agents require.*

---

## Purpose of This Section

This section addresses one of the most commonly misunderstood aspects of enterprise AI agents: the distinction between memory and context, and the governance requirements that memory imposes on enterprise systems.

Many organizations approach agent memory as an extension of retrieval-augmented generation (RAG)—a mechanism for fetching relevant documents and inserting them into prompts. This perspective, while technically accurate for a narrow class of use cases, fundamentally misunderstands what memory means for agents that operate over extended time horizons in regulated environments.

Enterprise agents are not stateless. They accumulate experience, learn from outcomes, adapt to user preferences, and refine their procedures based on operational feedback. This accumulated cognition is memory—and unlike context, memory persists beyond individual interactions, crosses agent boundaries, and becomes subject to the same governance requirements that apply to any enterprise data asset.

This section establishes the foundational requirements that enterprise memory systems must satisfy: what types of memory exist, how they differ in purpose and governance, what isolation and retention requirements apply, and how learning must be controlled to prevent silent policy drift.

---

## Subsections

### 3.1 Why Memory Is Not Just Context

This subsection establishes the fundamental distinction between memory (what the agent retains over time) and context (what the agent is thinking with right now). It explains why treating memory as "enhanced RAG" leads to governance failures and operational surprises.

- [3.1 Why Memory Is Not Just Context](./03-1-memory-vs-context.md)

### 3.2 The Memory Taxonomy (ESPP)

This subsection introduces the four-type memory taxonomy—Episodic, Semantic, Procedural, and Preference—that provides a conceptual framework for understanding what agents remember and why. Each memory type serves a distinct cognitive purpose and carries different governance implications.

- [3.2 The Memory Taxonomy (ESPP)](./03-2-espp-taxonomy.md)

### 3.3 Organizational vs. Operational Memory

This subsection distinguishes between organizational memory (long-lived, cross-agent, for institutional learning and audit) and operational memory (session-scoped, for in-flight operations). This distinction is critical for understanding data governance boundaries and retention policies.

- [3.3 Organizational vs. Operational Memory](./03-3-org-vs-op-memory.md)

### 3.4 Memory Governance Imperatives

This subsection establishes the non-negotiable governance requirements that enterprise memory systems must satisfy: tenant and customer isolation, regulatory retention periods, right-to-erasure compliance, and the prohibition of personally identifiable information in audit records.

- [3.4 Memory Governance Imperatives](./03-4-governance-imperatives.md)

### 3.5 The Learning Imperative

This subsection addresses why agents must learn from experience—and why that learning must be governed. It introduces the controlled promotion path from operational feedback through agent memory to enterprise memory to authoritative knowledge, with human approval gates at each transition.

- [3.5 The Learning Imperative](./03-5-learning-imperative.md)

---

## Key Concepts Introduced

| Concept | Definition |
|---------|------------|
| **Memory** | Information the agent chooses to retain across interactions because it may be useful later |
| **Context** | Ephemeral working state assembled for a single reasoning step or turn |
| **ESPP Taxonomy** | Four memory types: Episodic (what happened), Semantic (what we know), Procedural (how to act), Preference (how to personalize) |
| **Enterprise Memory** | Organizational-scope memory with 7+ year retention, no PII, immutable records |
| **Agent Memory** | Session/request-scope memory for operational continuity, PII permitted |
| **Controlled Promotion** | Governed pathway for learnings to move from agent memory to enterprise knowledge |

---

## Prerequisites

This section assumes familiarity with:

- The distinction between enterprise and consumer agents (Section 2)
- The OPD triad and why enterprise agents require observability (Section 1.3)
- The core modules of an enterprise agent platform (Section 1.4)

---

## Relationship to Other Sections

**Section 4 (Audit Requirements)** builds directly on this section's memory concepts. The Cognitive Audit Fabric (CAF) is the control plane for Enterprise Memory, and understanding memory types is prerequisite to understanding audit record types.

**Section 5 (Building an Enterprise Agent)** references this section's memory taxonomy when discussing context compilation and the four sources of agent knowledge.

**Part 2, Section 4 (Memory, Knowledge & Audit in Seer)** demonstrates how Seer and Hub implement the memory requirements established here.

---

## Cross-References

For detailed implementation specifications, see:

- `olympus-hub-docs/04-subsystems/memory-services/README.md` — Hub Memory Services architecture
- `olympus-hub-docs/04-subsystems/memory-services/enterprise-memory/` — Enterprise Memory implementation
- `olympus-hub-docs/04-subsystems/memory-services/agent-memory/` — Agent Memory implementation
- `olympus-seer-docs/agentic-ai-concepts/agent-memory/agent-memory-management.md` — Conceptual primer
- `olympus-seer-docs/agentic-ai-concepts/agent-memory/knowledge-memory-context-session.md` — Foundational distinctions

---

*Memory is not storage—it is controlled cognition over time. This section establishes what that control requires in an enterprise context.*
