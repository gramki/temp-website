# Agent Reliability Engineer (ARE)

> **Status:** Reference Document  
> **Last Updated:** 2026-01-09  
> **Related:** [Role Definitions](./roles.md) | [AE Deliverables to ARE](./ae-deliverables-to-are.md)

---

## Role Definition

The **Agent Reliability Engineer (ARE)** ensures that AI Agents and Agent-Oriented Systems (AOS) are:

* Operationally safe
* Reliable under real-world conditions
* Economically bounded
* Observable and diagnosable
* Recoverable during failure

ARE is **not** responsible for business correctness, agent intent, or value realization.

> **ARE controls the engine, not the destination.**

---

## Ownership Summary

| ARE Owns | ARE Does NOT Own |
|----------|------------------|
| Runtime safety enforcement | Agent intent or autonomy policy (APO) |
| Observability, OOS, and COR | Cognitive design (CSA) |
| Cost control and containment | Business outcomes (APO) |
| Incident response and recovery | Platform infrastructure (managed by provider) |
| Platform provider coordination | Autonomy approval (ARAO) |
| Production gate decisions | Knowledge governance (KMO) |
| Escalation operation | Cognitive health monitoring (COS) |
| Multi-agent system reliability | |

---

## Operating Principles

ARE operates only on signals that are:

1. **Visible** at runtime
2. **Attributable** to an agent or system
3. **Timely** enough for operational control
4. **Non-debatable** (not opinionated or lagging business metrics)

As a result:

* Business-adjacent outcome metrics (EOS, NPS, revenue impact, etc.) are **out of scope**
* ARE's control loop is based exclusively on **Action Quality + Task Completion**

---

## ARE Control Loop

### Operational Outcome Score (OOS)

OOS is the **only outcome signal** used by ARE.

It is derived from:

* Action Quality signals
* Task Completion signals

OOS represents **operational sanity**, not business success.

---

### Cost-to-Operation Ratio (COR)

```
COR = Total Operational Cost / OOS
```

This is the **primary efficiency and alerting metric** for ARE.

---

## Autonomy Boundary

| Responsibility | Owner |
|----------------|-------|
| Autonomy policy (what the agent is allowed to do) | APO + ARAO |
| Execution safety enforcement (whether autonomy may run *right now*) | ARE |

**ARE may:**

* Enforce safety ceilings
* Degrade execution modes
* Block unsafe execution paths
* Coordinate with platform provider

**ARE may NOT:**

* Change agent intent
* Expand autonomy
* Modify decision logic

---

## Observability Scope

| Focus Area | ARE Responsibility |
|------------|-------------------|
| **System health** (latency, errors, cost, availability) | Primary owner |
| **Cognitive health** (drift, confusion, quality) | Defers to COS |

---

# Part I — Agent-Level Operability Expectations

This section defines **what an Agent must expose** for ARE to operate it.

---

## 1. Agent-Level Metrics (Required)

### Action Quality Metrics

| Metric | Description |
|--------|-------------|
| Override rate | Frequency of human overrides |
| Escalation rate | Frequency of escalations |
| Retry amplification | Retry loops beyond normal |
| Policy violations | Policy breaches detected |
| Tool failure rate | Tool invocation failures |

### Task Completion Metrics

| Metric | Description |
|--------|-------------|
| Task success / failure | Binary outcome |
| SLA adherence | Within time bounds |
| Rework required | Task needed redo |
| Human follow-up invoked | Human intervention required |

---

## 2. Agent-Level Levers (Required)

ARE must be able to adjust the following **at runtime** (no redeployment required):

| Lever | Purpose |
|-------|---------|
| Execution enable / disable | Kill switch |
| Max reasoning steps | Bound cognitive loops |
| Max retries | Prevent retry storms |
| Tool-level enable / disable | Isolate tool failures |
| Confirmation thresholds | Require human approval |
| Token and tool cost ceilings | Cost containment |
| Execution timeouts | Prevent runaway execution |

---

## 3. Agent-Level KPIs (ARE-owned)

| KPI | Description |
|-----|-------------|
| OOS (per agent) | Operational Outcome Score |
| COR (per agent) | Cost-to-Operation Ratio |
| MTTC | Mean Time to Containment |
| Incident frequency | Incidents per agent per period |

---

## 4. Agent-Level SLOs

| SLO | Target |
|-----|--------|
| OOS | ≥ defined threshold |
| COR | ≤ defined ceiling |
| Latency | Within approved budget |
| Unbounded execution events | Zero |

---

## 5. Agent-Level Success Criteria

An agent is **operationally healthy** when:

* OOS is stable or improving
* COR remains within bounds
* Safety levers are rarely invoked
* Failures are predictable and contained

---

# Part II — AOS-Level Operability Expectations

This section defines **system-wide requirements** for Agent-Oriented Systems.

---

## 6. AOS-Level Metrics (Required)

### Aggregated Action Quality

| Metric | Description |
|--------|-------------|
| Cross-agent escalation rate | Escalations across system |
| Cross-agent override density | Override patterns |
| Policy violation density | System-wide violations |

### Aggregated Task Completion

| Metric | Description |
|--------|-------------|
| End-to-end task success | Full workflow completion |
| SLA compliance | System-wide SLA adherence |
| Human intervention density | Human involvement rate |

---

## 7. AOS-Level Levers (Required)

| Lever | Purpose |
|-------|---------|
| System-wide kill switch | Emergency halt |
| Per-agent isolation | Contain blast radius |
| Blast-radius containment | Prevent cascade |
| Dependency circuit breakers | Isolate dependencies |
| System-wide cost ceilings | Total cost control |
| Autonomy degradation modes | Graceful capability reduction |

---

## 8. AOS-Level KPIs (ARE-owned)

| KPI | Description |
|-----|-------------|
| System OOS | Aggregate Operational Outcome Score |
| System COR | Aggregate Cost-to-Operation Ratio |
| Incident containment time | Time to contain incidents |
| Cost anomaly frequency | Unexpected cost spikes |

---

## 9. AOS-Level SLOs

| SLO | Target |
|-----|--------|
| Cascading failures | None |
| Unbounded cost events | None |
| Shutdown behavior | Deterministic |
| Recovery | Within defined RTO |

---

## 10. AOS-Level Success Criteria

The AOS is **operationally healthy** when:

* Individual agent failures are isolated
* Cost scales predictably with workload
* Degradation is graceful, not catastrophic
* Operators retain control at all times

---

## Role Interfaces

| Role | ARE Interface |
|------|---------------|
| **APO** | Receives operational risk signals, not outcome judgments |
| **CSA** | Receives operability feedback on designs |
| **AE** | Supplies required controls and telemetry |
| **KMO** | Receives memory growth alerts |
| **COS** | Shares observability data; defers cognitive health |
| **ARAO** | Provides evidence for audits |

---

## Platform Provider Coordination

ARE is responsible for coordinating with the managed platform provider (Seer, Hub) for:

| Area | Coordination Type |
|------|-------------------|
| Capacity planning | Proactive |
| Capability requests | As needed |
| Platform incidents | Reactive escalation |
| Feature requests | Backlog input |

---

## Final Statement

> **ARE does not judge whether an agent is right.**
> **ARE ensures the agent can be allowed to run without loss of control.**

If an agent or system cannot expose the metrics and levers defined here, it is **not production-operable** — regardless of intelligence, accuracy, or promise.

---

*End of document*

