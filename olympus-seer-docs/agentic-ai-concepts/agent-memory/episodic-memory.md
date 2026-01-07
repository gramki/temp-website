# Episodic Agent Memory

## Definition

**Episodic Agent Memory** is the agent’s record of **what happened**: interactions, events, tool calls, decisions taken, and outcomes.

It answers:

> *“What happened before that might matter now?”*

Episodic memory is usually high-volume and time-ordered; it is often the raw substrate from which **semantic**, **preference**, and **procedural** memories are derived.

## What to capture (signals worth remembering)

- **User corrections** (“No, that’s wrong; do X instead”)
- **Decisions and outcomes** (what was chosen; did it work)
- **Tool traces** (inputs/outputs, failures, retries, latency)
- **Exceptions and overrides** (where policy/procedure was bypassed)
- **New entities** (IDs, contacts, cases) and the context they appeared in

## Storage patterns

- **Append-only event log** (time-indexed) + optional embeddings for semantic search
- **Thread/session summaries** for long-lived continuity (avoid storing full transcripts forever)
- **Pointers over copies** for large tool outputs (store references + hashes + provenance)

## Retrieval patterns

- **Time-window retrieval**: last N minutes/hours/days; “recent relevant”
- **Similarity retrieval**: “similar past situations” (vector search)
- **Trace reconstruction**: link tool calls → decisions → outcomes for explanation/debug

## Update, decay, and eviction

- Episodic memory should **decay** in influence before it is deleted (freshness scoring).
- Use **TTL + summarization**: keep high-fidelity recent traces; compress older ones.
- Preserve **audit-critical** traces via tombstoning/archival policies where needed.

## Failure modes to guard against

- **Unbounded growth** (cost + retrieval noise)
- **Prompt stuffing** (dumping too much episodic text into the model)
- **Privacy leakage** (storing sensitive data without minimization and consent)
- **Instruction injection via memory** (treat retrieved text as untrusted input)

## Navigation

- Back: [`README.md`](./README.md)
- Next: [`semantic-memory.md`](./semantic-memory.md)

