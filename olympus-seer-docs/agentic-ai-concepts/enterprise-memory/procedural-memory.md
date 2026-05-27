# Procedural Enterprise Memory

## Definition

**Procedural Enterprise Memory** captures **how work is actually performed in practice**:

- workflows that reliably “get the job done”
- operational heuristics and escalation paths
- playbooks, runbooks, and stable workarounds
- agent execution strategies that prove effective

It answers:

> *“How do we actually do this (under real constraints)?”*

Procedural memory often diverges from written SOPs; that divergence is itself a valuable signal.

## “Procedural” has three layers (avoid confusion)

The word “procedural” shows up in three different cognitive layers:

- **Procedural enterprise knowledge**: official SOPs/runbooks (what the enterprise asserts)  
  See: [../enterprise-knowledge/procedural-knowledge.md](../enterprise-knowledge/procedural-knowledge.md)
- **Procedural enterprise memory (this doc)**: how work is actually done in practice (revealed behavior)
- **Procedural agent memory**: agent-executable workflows/tool chains for repeatable action  
  See: [../agent-memory/procedural-memory.md](../agent-memory/procedural-memory.md)

## What belongs here (signals worth remembering)

Procedural memory is revealed through **behavioral regularity**:

- repeated workarounds for known system constraints
- stable sequences of actions used by teams (even if undocumented)
- consistent exception handling and escalation heuristics
- “tribal knowledge” that appears across cases and operators
- agent tool-chains that reliably solve a class of problems

## Capture (recommended artifacts)

Procedural memory should be stored in **checkable** forms (not just prose).

Recommended artifact shapes:

- **Runbook / Playbook**: steps, prerequisites, safety checks, rollback, owners
- **WorkflowDefinition**: states, transitions, guard conditions, approvals
- **EscalationHeuristic**: triggers, thresholds, routing targets, timeouts
- **ToolChainRecipe**: tool sequence, inputs/outputs, failure handling, retries

Minimum capture fields:

- **intent** (goal of the procedure)
- **preconditions** (when it applies)
- **steps** (ordered; with decision points)
- **safety checks** (what must be verified)
- **evidence requirements** (what must be collected before acting)
- **failure modes** (what can go wrong; how to recover)
- **owners** (who maintains it; who approves changes)

## Retention & forgetting

Procedural memory decays when it stops working.

Recommended mechanisms:

- **versioning** (procedures are artifacts, not ephemeral notes)
- **deprecation** when tools/systems change
- **periodic validation** (dry-runs, audits, simulation)
- **drift detection** (compare practice vs documented procedure/policy)

## Retrieval (how it gets used)

Procedures are retrieved by **applicability**, not similarity alone:

- match on preconditions (domain, product, risk tier, jurisdiction, channel)
- match on resource availability (tools, permissions, SLAs)
- policy compatibility checks (procedures must not bypass binding constraints)

In agentic systems:

- procedural memory is how agents become reliable (repeatable workflows)
- it should be gated through policy/approval (procedures can be dangerous)

## Promotion (procedure → knowledge)

Procedural memory should be promoted when:

- it stabilizes and becomes broadly relied upon
- it has regulatory, safety, or customer-impact implications
- informal practice must become official

Promotion yields:

- revised **Enterprise Knowledge** (policy/standard/SOP) with explicit ownership and governance

## Governance (non-negotiables)

- **Policy precedence**: procedures must not override binding policy/knowledge
- **Change control**: procedures require versioning, review, and rollback
- **Tool safety**: explicit allowlists/denylists; guardrails for high-risk steps
- **Auditability**: link procedure use to episodic records (“we executed procedure v3.2”)

## Common failure modes

- **Prose-only procedures**: not testable, not enforceable, not safe
- **Silent obsolescence**: the procedure “works until it doesn’t” after a system change
- **Hidden coupling**: steps assume tools/permissions that aren’t explicit

## Further reading

- Anderson, J. R. *ACT‑R* (procedural memory as production rules): [https://act-r.psy.cmu.edu/](https://act-r.psy.cmu.edu/)
- Laird, J. *The Soar Cognitive Architecture* (procedural knowledge and chunking): [https://soar.eecs.umich.edu/](https://soar.eecs.umich.edu/)
- Zhou et al., *Remember Me, Refine Me: A Dynamic Procedural Memory Framework* (identification, retention, refinement): [https://arxiv.org/abs/2512.10696](https://arxiv.org/abs/2512.10696)
- Shinn et al., *Reflexion* (procedural improvement via reflection): [https://arxiv.org/abs/2303.11366](https://arxiv.org/abs/2303.11366)
- Redis, *Managing Memory for AI Agents* (practitioner overview): [https://redis.io/resources/managing-memory-for-ai-agents.pdf](https://redis.io/resources/managing-memory-for-ai-agents.pdf)

## Related concepts (Hub docs)

- [../../../olympus-hub-docs/02-system-design/implementation-concepts/cognitive-audit-fabric.md](../../../olympus-hub-docs/02-system-design/implementation-concepts/cognitive-audit-fabric.md): CAF policy enforcement (especially important for procedural/tool safety)
- [../../../olympus-hub-docs/04-subsystems/memory-services/hub-enterprise-memory.md](../../../olympus-hub-docs/04-subsystems/memory-services/hub-enterprise-memory.md): Enterprise Memory record types and retention table (stub)

## Navigation

- Back to overview: [README.md](./README.md)
- Prev: [semantic-memory.md](./semantic-memory.md)
- Next: [preference-memory.md](./preference-memory.md)

