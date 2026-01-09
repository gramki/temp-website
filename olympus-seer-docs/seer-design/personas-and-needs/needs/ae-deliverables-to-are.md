# Agent Engineer (AE) Deliverables to Agent Reliability Engineer (ARE)

> **Status:** Reference Document  
> **Last Updated:** 2026-01-09  
> **Related:** [Role Definitions](./roles.md) | [ARE Reference](./are.md)

---

## Purpose

This document defines the **explicit deliverables** that the **Agent Reliability Engineer (ARE)** expects from **Agent Engineers (AE)** when building AI agents and Agent-Oriented Systems (AOS).

It exists to:

* Prevent ambiguity during production readiness reviews
* Avoid last-minute operability surprises
* Keep responsibility boundaries clean
* Make agent systems *runnable*, not just *intelligent*

**These are hard requirements, not guidelines.**

---

## Foundational Principle

> **ARE does not make agents reliable after the fact.**
> **Agent Engineers must design agents so that reliability can be enforced.**

If a capability cannot be constrained, observed, throttled, or stopped, it cannot be operated.

---

## Responsibility Boundary

| Role | Owns |
|------|------|
| **AE** | Agent implementation correctness and completeness |
| **ARE** | Runtime safety, operability, and enforcement |

This document specifies **what AE must deliver** so ARE can fulfill their mandate.

---

# Section 1 — Mandatory Agent Contracts

## 1.1 Explicit Agent Contract

Each agent must expose a **machine-readable operational contract**.

### AE Deliverables

| Deliverable | Description |
|-------------|-------------|
| Stable Agent ID | Unique, version-independent identifier |
| Version | Semantic version of the agent |
| Declared purpose | Bounded scope of what agent does |
| Declared non-goals | Explicit out-of-scope behaviors |
| Declared action types | Types of actions agent can perform |
| Declared tool usage | Tools the agent may invoke |

### ARE Expectations

* Contract is immutable per version
* Contract can be inspected without code access
* Contract is available at deployment time

---

## 1.2 Safety Control Contract

Agents must expose **runtime-adjustable safety controls**.

### AE Deliverables

| Control | Description |
|---------|-------------|
| Kill switch hook | Immediate execution halt |
| Max reasoning steps | Cognitive loop bound |
| Max retries | Retry attempt limit |
| Tool enable/disable switches | Per-tool control |
| Token cost ceiling | LLM token budget |
| Tool cost ceiling | External API budget |
| Execution timeout | Maximum execution duration |

### ARE Expectations

* Controls are enforceable externally (no code changes)
* Controls do not require redeployment
* Controls fail closed, not open

---

# Section 2 — Execution Determinism & Bounds

## 2.1 Bounded Reasoning

### AE Deliverables

| Requirement | Description |
|-------------|-------------|
| Hard upper bounds | All reasoning loops have limits |
| Capped reflection loops | Critique/reflection is bounded |
| Limited recursion | Recursive calls explicitly limited |

### ARE Expectations

* No unbounded execution paths exist
* Bounds are documented and enforceable

---

## 2.2 Deterministic Failure Modes

### AE Deliverables

| Requirement | Description |
|-------------|-------------|
| Explicit failure states | Named, documented failure modes |
| Structured error outputs | Machine-readable error format |
| Known escalation triggers | Documented escalation conditions |

### ARE Expectations

* Failures are observable and classifiable
* No silent retries
* No self-healing via increased autonomy

---

# Section 3 — Observability Obligations

## 3.1 Action-Level Telemetry

### AE Deliverables

| Event Type | Required Fields |
|------------|-----------------|
| Task start | Task ID, Agent ID, Timestamp |
| Task end | Task ID, Status, Duration |
| Action execution | Action type, Parameters, Result |
| Tool invocation | Tool name, Input, Output, Latency |
| Retry event | Retry count, Reason, Backoff |
| Failure event | Error type, Error message, Stack |

### ARE Expectations

* Telemetry is consistent and structured
* Events are correlated via task/trace ID
* No silent failures

---

## 3.2 Outcome & Completion Signals

### AE Deliverables

| Signal | Description |
|--------|-------------|
| Task completion status | Success, Failure, Partial |
| SLA breach signal | Emitted when SLA exceeded |
| Human override event | When human overrides agent |
| Rework indicator | When task requires redo |
| Escalation event | When agent escalates |

### ARE Expectations

* Signals are emitted regardless of success or failure
* Signals are emitted in real-time (not batched)

---

# Section 4 — Cost & Resource Transparency

## 4.1 Cost Attribution

### AE Deliverables

| Attribution | Granularity |
|-------------|-------------|
| Token usage | Per task |
| Tool/API cost | Per task |
| Compute usage | Per agent |

### ARE Expectations

* Cost data is real-time or near-real-time
* No hidden or bundled cost paths
* Cost is attributable to specific tasks/agents

---

# Section 5 — Memory Discipline

## 5.1 Explicit Memory Semantics

### AE Deliverables

| Requirement | Description |
|-------------|-------------|
| Declared memory types | Which memory types agent uses |
| Explicit write conditions | When agent writes to memory |
| Size limits | Maximum memory per session/agent |
| Retention policy | How long memory persists |

### ARE Expectations

* Memory growth is bounded and observable
* No implicit long-term memory writes
* Memory usage is attributable

---

# Section 6 — Versioning & Change Safety

## 6.1 Versioned Artifacts

### AE Deliverables

| Artifact | Versioning Requirement |
|----------|----------------------|
| Agent code | Semantic versioning |
| Prompts | Version-tracked |
| Policies | Version-tracked |
| Tool bindings | Version-tracked |

### ARE Expectations

* Runtime rollback is possible
* Version lineage is reconstructable
* No unversioned production changes

---

## 6.2 Safe Change Introduction

### AE Deliverables

| Requirement | Description |
|-------------|-------------|
| Backward compatibility | Where possible |
| Change impact notes | Operational impact documented |
| Rollback procedure | Documented rollback steps |

### ARE Expectations

* ARE can assess blast radius before rollout
* Changes are gradual (canary, staged)

---

# Section 7 — Interaction with ARE

## 7.1 Production Readiness Reviews

### AE Deliverables

| Item | Evidence Required |
|------|-------------------|
| Agent contract | Machine-readable contract file |
| Safety controls | Demo of each control |
| Observability | Working dashboards |
| Cost attribution | Cost tracking demo |
| Memory discipline | Memory bounds documentation |
| Versioning | Version history and rollback demo |

### ARE Expectations

* Evidence, not assurances
* Demonstrations, not promises
* Documentation, not verbal explanations

---

## 7.2 Incident Support

### AE Responsibilities

| Responsibility | Description |
|----------------|-------------|
| Incident participation | Join incident analysis |
| Failure classification | Help classify new failure modes |
| Root cause analysis | Contribute to RCA |
| Control tightening | Implement tighter controls post-incident |

### ARE Expectations

* Incidents result in tightened controls, not looser ones
* Learnings are codified in agent contracts

---

# Section 8 — Handoff Checklist

Before production deployment, AE must provide ARE with:

| # | Deliverable | Format |
|---|-------------|--------|
| 1 | Agent Contract | YAML/JSON |
| 2 | Safety Control Documentation | Markdown |
| 3 | Observability Dashboard | Grafana/Watch |
| 4 | Cost Attribution Setup | Verified in platform |
| 5 | Memory Configuration | Documented limits |
| 6 | Version Manifest | Version file |
| 7 | Rollback Procedure | Runbook |
| 8 | Failure Mode Catalog | Documented failures |

---

# Anti-Patterns (Explicitly Rejected)

| Anti-Pattern | Why It's Rejected |
|--------------|-------------------|
| "The model will usually behave" | Probability is not control |
| "We can add limits later" | Limits must be designed in |
| "This edge case is unlikely" | Edge cases cause incidents |
| "LLMs are probabilistic by nature" | Execution bounds are deterministic |
| "Trust the guardrails" | Guardrails are defense-in-depth, not primary |

These are **not acceptable responses** in production contexts.

---

## Final Statement

> **Agent Engineers build intelligence.**
> **ARE makes that intelligence survivable in the real world.**

If an agent cannot be constrained, observed, or stopped, it is **not ready** — regardless of how impressive it appears.

---

## Related Documents

* [Role Definitions](./roles.md) — Complete role definitions
* [ARE Reference](./are.md) — ARE scope and expectations
* [Production Readiness](./needs/production-readiness.md) — Full readiness criteria

---

*End of document*

