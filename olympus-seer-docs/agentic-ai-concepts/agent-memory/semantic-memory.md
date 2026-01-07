# Semantic Agent Memory

## Definition

**Semantic Agent Memory** is the agent’s store of **stable, reusable facts and concepts** it uses to reason and act.

It answers:

> *“What do I know that is likely still true and useful?”*

Semantic memory is often built by consolidating episodic traces into **normalized facts**, **entity models**, and **relations**.

## Scope clarification (avoid semantic-memory collisions)

“Semantic memory” is used at both agent and enterprise layers:

- **Semantic agent memory (this doc)**: the agent’s local, tactical store of “what I know” to act effectively.
- **Semantic enterprise memory (learned)**: institutional learned patterns derived from cases/episodes (shared across agents and humans).  
  See: [`../enterprise-memory/semantic-memory.md`](../enterprise-memory/semantic-memory.md)

If a semantic claim must **constrain behavior** (policy, eligibility, binding decision criteria), it belongs in **Enterprise Knowledge-of-record**, not in agent memory.  
See: [`../enterprise-knowledge/README.md`](../enterprise-knowledge/README.md) and [`../enterprise-knowledge-memory-other-data.md`](../enterprise-knowledge-memory-other-data.md)

## What to store

- **Entity facts** (customer attributes, case metadata, product definitions) with provenance
- **Learned constraints** (what tends to be safe/unsafe) with confidence and scope
- **Concept graphs** (relationships among entities) where structured reasoning helps

## Storage patterns

- **Knowledge graph / structured store** for entity-centric access and relationships
- **Vector index** for fuzzy recall / paraphrase retrieval
- **Versioned records** for facts that change (effective dates, supersession)

## Retrieval patterns

- **Entity-centric lookup**: “what do we know about X?”
- **Hybrid retrieval**: symbolic filters + vector recall
- **Conflict-aware recall**: prefer newer/higher-confidence sources; surface uncertainty

## Update and conflict handling

Semantic memory needs explicit policies for:

- **provenance** (where did this fact come from?)
- **freshness** (how recent is it?)
- **confidence** (how sure are we?)
- **supersession** (what replaces what?)

Avoid turning semantic memory into “truth” by accident: if it must bind behavior, it belongs in enterprise knowledge/policy.

## Failure modes to guard against

- **Stale facts** (no freshness model)
- **Contradictory records** (no conflict resolver)
- **No provenance** (“why did you claim that?” becomes unanswerable)

## Navigation

- Back: [`README.md`](./README.md)
- Prev: [`episodic-memory.md`](./episodic-memory.md)
- Next: [`preference-memory.md`](./preference-memory.md)

