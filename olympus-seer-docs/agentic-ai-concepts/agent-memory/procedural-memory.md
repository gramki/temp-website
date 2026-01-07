# Procedural Agent Memory

## Definition

**Procedural Agent Memory** stores “how to do things”: skills, workflows, playbooks, and tool chains the agent can reuse.

It answers:

> *“What procedure should I execute under these constraints?”*

Procedural memory is where agents become repeatable and reliable—when it is versioned, testable, and policy-gated.

## “Procedural” has three layers (avoid confusion)

The word “procedural” shows up in three different cognitive layers:

- **Procedural enterprise knowledge**: official SOPs/runbooks (what the enterprise asserts)  
  See: [`../enterprise-knowledge/procedural-knowledge.md`](../enterprise-knowledge/procedural-knowledge.md)
- **Procedural enterprise memory**: how work is actually done in practice (revealed behavior)  
  See: [`../enterprise-memory/procedural-memory.md`](../enterprise-memory/procedural-memory.md)
- **Procedural agent memory (this doc)**: agent-executable workflows/tool chains for repeatable action

## What to store

- **Workflows** (multi-step plans with decision points)
- **Tool chains** (which tools to call, in what order, with what checks)
- **Escalation playbooks** (when to hand off to a human)
- **Checklists** (what must be verified before acting)

## Storage patterns

- **Version-controlled artifacts** (preferred): DSL/workflow definitions/prompted routines
- **Policy engine integration**: OPA/Cedar-style checks for applicability and authorization
- **Metadata**: preconditions, expected outputs, failure modes, rollback steps

## Retrieval patterns

- **Applicability checks**: match procedure to conditions (domain, tools available, permissions)
- **Skill matching**: choose among procedures by success history, safety, and constraints
- **Fallback hierarchy**: safe baseline procedures when uncertain

## Update and governance

- Procedures must be **auditable**: “procedure vX ran at time T with inputs I.”
- Support **deprecation and rollback** (procedures silently rot as tools change).
- Guard against drift from policy: procedures should not become shadow policy.

## Failure modes to guard against

- **Prose-only procedures** (not testable, not enforceable)
- **Hidden coupling** to tools/permissions (breaks in production)
- **Policy bypass** via “helpful” steps discovered in text memory

## Navigation

- Back: [`README.md`](./README.md)
- Prev: [`preference-memory.md`](./preference-memory.md)
- Next: [`context-building.md`](./context-building.md)

