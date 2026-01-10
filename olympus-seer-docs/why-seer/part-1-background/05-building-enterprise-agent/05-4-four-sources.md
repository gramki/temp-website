# 5.4 The Four Sources

Enterprise agents draw on multiple sources of information to reason and act. A common source of confusion—and a frequent cause of system failures—is conflating these sources or misunderstanding their proper roles. This section establishes a clear taxonomy of the four primary sources and the cognitive questions each answers.

## The Foundational Principle

> **Classify information by its cognitive role, not by the storage system or the colloquial word people use.**

The same database can hold multiple cognitive categories. A "knowledge base" can contain content that is not authoritative knowledge. A warehouse can store facts that are derived artifacts, not institutional memory. Clear classification enables proper governance and appropriate use.

## The Four Sources Defined

### 1. Enterprise Knowledge: What Is True / Correct / Required

**Definition:** Enterprise Knowledge consists of codified, curated, asserted truths that the organization recognizes as authoritative. It represents the normative layer—what *should* happen, what is *correct*, what is *required*.

**Characteristics:**
- Governed lifecycle: draft → review → approved → deprecated
- Versioned with change tracking
- Source of normative guidance
- Explicitly managed and curated

**Examples:**
- Policies and regulations
- Standard operating procedures (SOPs)
- Reference data and definitions
- Regulatory requirements
- Business rules and decision criteria

**Where it should live:** Governed knowledge layer—document repositories, knowledge graphs, knowledge services.

**Agent use:** Grounding decisions in authoritative guidance; ensuring compliance with organizational requirements.

### 2. Enterprise Memory: What Happened and Why

**Definition:** Enterprise Memory is the institutional record of what occurred, why it occurred, and what was learned from it. It represents the experiential layer—the organization's accumulated experience.

**Characteristics:**
- Immutable and append-only (for episodic records)
- Case-bound and time-ordered
- No PII (entity references only)
- Long-retained (7+ years for compliance)
- Follows ESPP taxonomy (Episodic, Semantic, Procedural, Preference)

**Examples:**
- Decision records and rationale
- Override histories and their outcomes
- Incident timelines and resolutions
- Outcome records linking decisions to results
- Learned patterns and validated hypotheses

**Where it should live:** Memory services, case systems, audit stores—append-only with provenance.

**Agent use:** Precedent lookup; learning from past outcomes; supporting audit and investigation.

### 3. Operational Data: What Is the Current State

**Definition:** Operational Data represents the current state of business operations and event history as maintained by operational systems. It is the transactional layer—what *is* happening right now.

**Characteristics:**
- Authoritative for current operational state
- Typically mutable (reflects real-time changes)
- May contain PII (subject to appropriate controls)
- Event history alongside current state

**Examples:**
- Transaction ledgers and account balances
- Case management status and SLAs
- Customer records and interaction history
- Inventory levels and order status
- Real-time metrics and sensor readings

**Where it should live:** Business applications, OLTP databases, operational APIs.

**Agent use:** Understanding current context; accessing real-time information needed for decisions.

**Key caution:** Authority for operational state does not automatically make something knowledge or memory. An account balance is operational state; it becomes memory only when recorded as part of a decision record.

### 4. Agent Memory: How Should I Act Now

**Definition:** Agent Memory is session-scoped or request-scoped memory that supports operational continuity and tactical decision-making. It represents the working layer—the agent's immediate context and transient learnings.

**Characteristics:**
- Ephemeral: session-lived or short retention
- PII-allowed: can contain personal data within session scope
- Mutable: can be updated during session
- Not authoritative: cannot silently become policy

**Examples:**
- Current conversation context
- User preferences within the session
- Results of recent tool calls
- Working hypotheses under investigation
- Intermediate reasoning steps

**Where it should live:** Agent memory services, session stores.

**Agent use:** In-flight operations; personalization; context continuity.

**Key caution:** Agent memory is not enterprise truth. It must not silently become policy or influence other agents without governed promotion.

## Comparison of the Four Sources

| Source | Question Answered | Scope | Governance | Mutability |
|--------|-------------------|-------|------------|------------|
| **Enterprise Knowledge** | What is true/correct/required? | Organizational | High: curated, versioned, approved | Version-controlled |
| **Enterprise Memory** | What happened and why? | Organizational | High: immutable, audited | Append-only |
| **Operational Data** | What is the current state? | Operational | Medium: application-level | Real-time mutable |
| **Agent Memory** | How should I act now? | Session/Request | Low: operational | Freely mutable |

## The Promotion Path

Information can move between sources, but only through governed processes:

```
Agent Memory (transient observations)
    ↓ (pattern detection, validation)
Enterprise Memory - Semantic (hypotheses, beliefs)
    ↓ (human validation, approval)
Enterprise Knowledge (authoritative policy)
```

This promotion path ensures that learnings from operational experience can become institutional knowledge without silently changing policy.

## Using All Sources Together

When designing an agent, the context compiler should explicitly draw from each source for its appropriate cognitive role:

1. **Enterprise Knowledge** provides normative constraints and factual grounding.
2. **Enterprise Memory** provides precedent and institutional context.
3. **Operational Data** provides current state and real-time facts.
4. **Agent Memory** provides session continuity and tactical context.

The structured context frame (see Section 5.3) organizes these sources appropriately, with clear precedence when conflicts arise.

---

**References:**
*   `olympus-seer-docs/agentic-ai-concepts/designing-an-agent.md`
*   `olympus-seer-docs/agentic-ai-concepts/agent-memory/knowledge-memory-context-session.md`
*   `olympus-hub-docs/04-subsystems/memory-services/README.md`
