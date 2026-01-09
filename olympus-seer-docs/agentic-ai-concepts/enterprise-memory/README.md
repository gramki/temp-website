# Enterprise Memory

Enterprise Memory is the organization’s **lived cognition over time**:

- what happened,
- what was decided,
- why it was decided,
- with what evidence,
- and how it influenced future behavior.

It answers the question:

> *“What did we experience and learn, and how did it shape our actions?”*

This folder breaks Enterprise Memory into four canonical types and makes each type **operable** (capture, retention/forgetting, promotion, and governance).

## Doc ownership (avoid duplication)

- **Canonical conceptual model** (definitions, OLTP placement, “storage ≠ cognition”, vocabulary mapping, core anti-patterns): [`../enterprise-knowledge-memory-other-data.md`](../enterprise-knowledge-memory-other-data.md)
- **This folder** is the Enterprise Memory handbook (ESPP types + capture/retention/promotion guidance per type).
- **Applied guide** with worked examples: [`../designing-an-agent.md`](../designing-an-agent.md)

## Related docs

- [`../enterprise-knowledge-memory-other-data.md`](../enterprise-knowledge-memory-other-data.md): Enterprise Knowledge vs Enterprise Memory vs Agent Memory (conceptual framing and anti-patterns)
- [`../agent-memory/knowledge-memory-context-session.md`](../agent-memory/knowledge-memory-context-session.md): Knowledge vs Session vs Memory vs Context (agent-centric clarity that avoids common conflations)
- [`../agent-memory/agent-memory-management.md`](../agent-memory/agent-memory-management.md): Memory lifecycle mechanics (useful patterns for retrieval/decay/eviction)
- [`../designing-an-agent.md`](../designing-an-agent.md): Practical guide to using enterprise knowledge, enterprise memory, and operational stores in context compilation
- **Hub docs (implementation concepts)**:
  - [`../../../olympus-hub-docs/04-subsystems/memory-services/hub-enterprise-memory.md`](../../../olympus-hub-docs/04-subsystems/memory-services/hub-enterprise-memory.md): Enterprise Memory as a Hub subsystem concept (stub, but aligned)
  - [`../../../olympus-hub-docs/02-system-design/implementation-concepts/cognitive-audit-fabric.md`](../../../olympus-hub-docs/02-system-design/implementation-concepts/cognitive-audit-fabric.md): Cognitive Audit Fabric (CAF) as governance control plane
  - [`../../../olympus-hub-docs/04-subsystems/cognitive-audit-fabric/README.md`](../../../olympus-hub-docs/04-subsystems/cognitive-audit-fabric/README.md): CAF subsystem overview (stub)

## Why Enterprise Memory matters (especially with agentic systems)

When agents (and humans) act autonomously and must be audited, **history alone is not enough**. OLTP and logs store events and state, but often do not preserve:

- rationale and intent
- evidence selection and weighting
- exceptions/overrides and accountability
- how understanding and procedures evolved

Enterprise Memory is the missing institutional layer that makes decisions **explainable, defensible, and learnable** across time and across agents.

## The four memory types (ESPP)

- **Episodic Memory** — “What happened?”  
  Discrete events, interactions, decisions, incidents, traces.
  - See: [`episodic-memory.md`](./episodic-memory.md)

- **Semantic Memory (Learned)** — “What did we learn from experience?”  
  Probabilistic patterns/hypotheses derived from episodes, challengeable and revisable.
  - See: [`semantic-memory.md`](./semantic-memory.md)

- **Procedural Memory** — “How do we actually do this?”  
  The organization’s practiced workflows, runbooks, and operational heuristics (often diverging from written SOPs).
  - See: [`procedural-memory.md`](./procedural-memory.md)

- **Preference Memory** — “What do we tend to favor in practice?”  
  Revealed priorities and trade-offs inferred from repeated choices, overrides, and tolerated risk.
  - See: [`preference-memory.md`](./preference-memory.md)

## A common lifecycle (make memory operable)

Across all types, treat Enterprise Memory as a managed lifecycle:

1. **Identification** — detect a signal worth remembering (events, decisions, overrides, anomalies)
2. **Capture** — write structured memory artifacts (not just raw text/logs)
3. **Retention / Forgetting** — manage relevance (TTL, decay, summarization, archival)
4. **Promotion** — strengthen commitments where appropriate

Promotion paths should be deliberate:

- **Promotion model (canonical)**: see [`../enterprise-knowledge-memory-other-data.md`](../enterprise-knowledge-memory-other-data.md) and [`../enterprise-knowledge/lifecycle-and-management.md`](../enterprise-knowledge/lifecycle-and-management.md)

## What Enterprise Memory is *not*

- **Not “historical data”**: history without causality and rationale is an archive, not memory
- **Not curated truth**: memory can be noisy and probabilistic
- **Not agent-local state**: enterprise memory must survive agent versions, handoffs, and organizational change
- **Not safe by default**: memory must be governed (scope, access, retention, privacy, provenance)

## How to use these docs

When designing a feature, workflow, or audit requirement, ask:

- **Which memory type is this?** (episodic/semantic/procedural/preference)
- **What artifact are we writing?** (decision record, override record, incident timeline, hypothesis record)
- **What is the retention and forgetting policy?**
- **What is promotable, by whom, and under what evidence thresholds?**

## Cross-cutting further reading

- Laird et al., *Cognitive Architectures: Past and Present* (unified view across memory types): [https://ai.stanford.edu/~nilsson/OnlinePubs-Nils/cogarch.pdf](https://ai.stanford.edu/~nilsson/OnlinePubs-Nils/cogarch.pdf)
- BDTechTalks, *A Deep Dive into AI Agent Memory* (accessible synthesis of modern patterns): [https://bdtechtalks.substack.com/p/a-deep-dive-in-ai-agent-memory-and](https://bdtechtalks.substack.com/p/a-deep-dive-in-ai-agent-memory-and)


