# 2026-01-07 — Agentic AI Concepts docs cleanup (previous + current session)

## Why

We had redundancy/confusion across `olympus-seer-docs/agentic-ai-concepts/` where multiple docs re-taught the same core framing (promotion path, anti-patterns) and terminology collisions (especially “procedural” and “semantic”) made it easy to conflate layers (enterprise knowledge vs enterprise memory vs agent memory).

## High-level structure (source-of-truth decisions)

- **Canonical conceptual model**: `olympus-seer-docs/agentic-ai-concepts/enterprise-knowledge-memory-other-data.md`
  - Owns: definitions; OLTP placement; “storage ≠ cognition”; vocabulary mapping; core category-level anti-patterns; promotion framing.
- **Operational handbooks**:
  - `.../enterprise-memory/` (ESPP types + capture/retention/promotion/governance per type)
  - `.../enterprise-knowledge/` (knowledge types + lifecycle/management)
  - `.../agent-memory/` (agent-local memory types + context-building mechanics + governance)
- **Applied coaching**: `.../designing-an-agent.md` (worked examples + implementation-level anti-patterns)
- **Platform overview**: `.../enterprise-agent-platform.md` (capability inventory; links out for conceptual depth)

## Main issues addressed

### 1) Terminology collision: “Procedural” in 3 layers

Problem: “procedural” correctly exists in multiple layers, but without an explicit callout readers can conflate them.

Fix: ensure a consistent “Procedural has three layers” callout across:

- `.../enterprise-memory/procedural-memory.md` (practice / how work is actually done)
- `.../enterprise-knowledge/procedural-knowledge.md` (official SOPs/runbooks / asserted guidance)
- `.../agent-memory/procedural-memory.md` (agent-executable workflows/tool chains)

### 2) Terminology collision: “Semantic memory” (agent vs enterprise)

Problem: “semantic memory” appears in both agent and enterprise layers and can be mistaken for knowledge-of-record.

Fix: add explicit scope clarification + reciprocal cross-links between:

- `.../agent-memory/semantic-memory.md`
- `.../enterprise-memory/semantic-memory.md`

Also clarified: if a semantic claim must **constrain behavior**, it belongs in **Enterprise Knowledge-of-record**, not in agent memory.

### 3) Reduce overlap between platform overview and applied guide

Problem: `enterprise-agent-platform.md` overlaps conceptually with the applied/canonical docs without direct navigation.

Fix: add “Related Documents” links from `enterprise-agent-platform.md` to:

- `enterprise-knowledge-memory-other-data.md` (canonical conceptual model)
- `designing-an-agent.md` (applied guide)
- `agent-memory/context-building.md` (context compiler mechanics)

## Files changed in this combined session

- Updated: `olympus-seer-docs/agentic-ai-concepts/enterprise-knowledge/procedural-knowledge.md`
  - Added “Procedural has three layers (avoid confusion)” section + cross-links.
- Updated: `olympus-seer-docs/agentic-ai-concepts/agent-memory/semantic-memory.md`
  - Added “Scope clarification (avoid semantic-memory collisions)” section + links to enterprise semantic memory + knowledge-of-record docs.
- Updated: `olympus-seer-docs/agentic-ai-concepts/enterprise-memory/semantic-memory.md`
  - Added reciprocal “Scope clarification” section + link to agent semantic memory.
- Updated: `olympus-seer-docs/agentic-ai-concepts/enterprise-agent-platform.md`
  - Added “Related Documents” links to the canonical/applied/context-building docs.

## Verification

- Lint: no linter errors reported for the edited markdown files.
- Search: no remaining `enprise` references in `olympus-seer-docs/agentic-ai-concepts/` (canonical filename is consistent as `enterprise-...`).

## Follow-ups (optional)

- Tighten “semantic memory vs semantics/ontologies” navigation by adding a short “See also” pointer between:
  - `enterprise-knowledge/semantics-and-ontologies.md` (interpretive meaning systems)
  - `enterprise-memory/semantic-memory.md` (learned patterns/hypotheses)
- Do a final pass to ensure anti-pattern ownership is consistent:
  - category-level anti-patterns stay canonical (`enterprise-knowledge-memory-other-data.md`)
  - implementation-level anti-patterns stay in `designing-an-agent.md`
  - READMEs keep only minimal bullets + links.


