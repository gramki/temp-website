# Section 2: Why Enterprise Agents Are Different — Overview

> **Part 1, Section 2**  
> **Outline Reference:** §2

---

## Purpose of This Section

This section explains why enterprise agents face requirements that consumer and business agents do not. Having established in Section 1 what enterprise agent platforms must provide, this section explores the underlying reasons why these requirements exist.

The section addresses the question: *What makes enterprise agents categorically different from consumer and business agents?*

---

## Central Thesis

Enterprise agents operate in an environment defined by three fundamental challenges:

1. **The Accountability Gap:** When agents make decisions, humans must remain accountable—but existing systems provide no framework for this accountability.

2. **The Authority Question:** The critical question is not whether agents *can* act, but who authorized them to act and within what bounds.

3. **The Irreversibility Problem:** Unlike consumer contexts where undo is usually possible, enterprise actions may have irreversible consequences requiring pre-action controls.

These challenges are not technical limitations to be engineered away. They are structural realities of operating autonomous systems within regulated, accountable institutions.

---

## Chapters in This Section

| Chapter | Title | Purpose |
|---------|-------|---------|
| **2.1** | [Consumer vs. Business vs. Enterprise Agents](./02-1-agent-types-comparison.md) | Establishes the categorical distinctions between agent types across multiple dimensions |
| **2.2** | [The Accountability Gap](./02-2-accountability-gap.md) | Explains why "the system did it" is unacceptable and what accountability requires |
| **2.3** | [The Authority Question](./02-3-authority-question.md) | Addresses how authority flows from humans to agents and what constraints must exist |
| **2.4** | [The Irreversibility Problem](./02-4-irreversibility-problem.md) | Explains why enterprise actions require pre-action controls, not just post-action logging |

---

## Key Concepts Introduced

| Concept | Definition |
|---------|------------|
| **Consumer Agent** | An AI agent optimized to delight individual users, where the user accepts risk |
| **Business Agent** | An AI agent that solves business tasks, where the business accepts risk |
| **Enterprise Agent** | An AI agent that acts with delegated authority, where the organization must defend decisions |
| **Accountability Gap** | The absence of frameworks for tracing agent decisions to accountable humans |
| **Authority Ceiling** | A hard limit on what an agent may do, regardless of capability |
| **Controlled Autonomy** | Agent autonomy bounded by explicit authority granted by accountable humans |

---

## References

This section synthesizes concepts from:

- `aosm-meta-model/agent-oriented-system.md` — AOSM foundations including RASCI and Controlled Autonomy
- `aosm-meta-model/raw-trained-employed-agents.md` — Agent lifecycle and authority model
- `olympus-seer-docs/seer-design/subsystems/authority-enforcement.md` — Authority enforcement design

---

## Cross-References

- **Section 1** (What Is an Enterprise Agent Platform?) established what platforms must provide; this section explains why
- **Section 3** (Memory Requirements) addresses the memory governance implications of enterprise context
- **Section 4** (Audit Requirements) addresses the audit implications of accountability requirements
- **Section 5** (Building an Enterprise Agent) applies these concepts to practical agent construction

---

## Reading Guidance

Read this section sequentially. Each chapter builds on the previous:

1. **2.1** establishes the taxonomy of agent types
2. **2.2** explains the accountability challenge
3. **2.3** addresses authority and delegation
4. **2.4** covers the irreversibility constraint

After completing this section, proceed to [Section 3: Memory Requirements](../03-memory-requirements/_section-overview.md).
