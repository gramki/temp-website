# Agent Memory

This folder contains agent-centric memory concepts and design guidance:

- how agent memory differs from **knowledge**, **session**, and **context**
- the canonical memory types (episodic, semantic, preference, procedural) as used by agents
- lifecycle mechanics (identify → store → retrieve → compose context → decay → evict)
- governance considerations for production agent deployments

## Doc ownership (avoid duplication)

- **Canonical conceptual model** (knowledge vs memory vs agent memory; “storage ≠ cognition”): [../enterprise-knowledge-memory-other-data.md](../enterprise-knowledge-memory-other-data.md)
- **This folder** is the Agent Memory handbook (agent-local memory types + context compiler mechanics + governance).
- **Applied guide** with worked examples: [../designing-an-agent.md](../designing-an-agent.md)

## Documents

- [knowledge-memory-context-session.md](./knowledge-memory-context-session.md): Clean definitions and common confusions
- [agent-memory-management.md](./agent-memory-management.md): Overview + navigation (this folder is the “book”)

## Agent memory types

- [episodic-memory.md](./episodic-memory.md): what happened (events, traces, outcomes)
- [semantic-memory.md](./semantic-memory.md): what the agent knows (facts, concepts, relations)
- [preference-memory.md](./preference-memory.md): how the agent should behave (soft constraints)
- [procedural-memory.md](./procedural-memory.md): how to do things (workflows, tool chains)

## Context building

- [context-building.md](./context-building.md): context compiler pipeline, structure, and safety

## Governance + references

- [governance.md](./governance.md): agent memory governance checklist (privacy, retention, provenance, security)
- [frameworks.md](./frameworks.md): how OSS frameworks model memory (LangGraph, CrewAI, AutoGen, Semantic Kernel)

## Related (enterprise-level)

- [../designing-an-agent.md](../designing-an-agent.md): Practical guide to using enterprise knowledge, enterprise memory, and operational stores in context compilation
- [../enterprise-memory/README.md](../enterprise-memory/README.md): Enterprise Memory types (institutional layer)
- [../enterprise-knowledge-memory-other-data.md](../enterprise-knowledge-memory-other-data.md): Enterprise Knowledge vs Enterprise Memory vs Agent Memory (conceptual framing)

