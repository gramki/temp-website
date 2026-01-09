# Production Readiness Checklist

## For AI Agents and Agent-Oriented Systems (AOS)

This checklist is used to make a **binary production decision**.
Every item must be **explicitly verified**. “Planned”, “assumed”, or “implicit” is treated as **NO**.

---

# Part A — Agent-Level Production Readiness Checklist

Each agent must independently satisfy **all** items below.

---

## A1. Agent Identity & Ownership

* [ ] Agent has a stable, versioned Agent ID
* [ ] Agent purpose is documented (bounded, non-aspirational)
* [ ] Explicit non-goals are documented
* [ ] Owning APO is named
* [ ] Owning engineering team is named

**Gate owner:** APO

---

## A2. Capability Declaration

* [ ] All agent actions are explicitly listed
* [ ] All tools the agent can invoke are enumerated
* [ ] Read vs write permissions are declared
* [ ] No implicit or dynamic tool discovery in production

**Gate owner:** Agent Architect

---

## A3. Execution Safety Control Surface

* [ ] Agent-level kill switch exists and is tested
* [ ] Max reasoning steps enforced
* [ ] Max retries enforced
* [ ] Tool-level enable / disable controls exist
* [ ] Token and tool cost ceilings enforced
* [ ] Timeouts enforced
* [ ] Controls are tunable at runtime without redeploy

**Gate owner:** ARE

---

## A4. Deterministic Execution Bounds

* [ ] Hard upper bounds exist for reasoning loops
* [ ] Parallel execution is bounded
* [ ] Recursive or reflective loops have explicit caps
* [ ] No unbounded self-invocation paths

**Gate owner:** Agent Architect

---

## A5. Observability & Tracing

* [ ] Task start and end are logged
* [ ] All actions are logged
* [ ] Tool invocations are logged
* [ ] Retries and failures are logged
* [ ] Logs are correlated via task / trace ID

**Gate owner:** ARE

---

## A6. Operational Outcome Signals

* [ ] Task completion status emitted (success/failure)
* [ ] SLA adherence is measurable
* [ ] Rework / human follow-up events are recorded
* [ ] Override events are recorded

**Gate owner:** ARE

---

## A7. Memory Discipline

* [ ] Memory types used are declared
* [ ] Explicit write conditions exist
* [ ] Retention / decay rules are defined
* [ ] Memory size ceilings are enforced
* [ ] No implicit long-term memory writes

**Gate owner:** Knowledge & Memory Owner

---

## A8. Failure & Escalation Behavior

* [ ] Failure states are explicitly defined
* [ ] Escalation triggers are defined
* [ ] Human handoff behavior is documented
* [ ] Agent does not compensate failures with higher autonomy

**Gate owner:** Agent Architect

---

## A9. Cost Attribution

* [ ] Token usage attributable per task
* [ ] Tool/API usage attributable per task
* [ ] Runtime compute attributable per agent
* [ ] Cost visible to ARE dashboards

**Gate owner:** ARE

---

## A10. Versioning & Rollback

* [ ] Agent version is immutable and identifiable
* [ ] Prompt / policy versions are tracked
* [ ] Rollback mechanism exists and is tested

**Gate owner:** ARE

---

# Part B — Agent-Oriented System (AOS) Production Readiness Checklist

The system composed of agents must satisfy **all** items below.

---

## B1. System Topology Transparency

* [ ] All agents in the system are enumerated
* [ ] Invocation relationships are documented
* [ ] Human-in-the-loop touchpoints are explicit
* [ ] No undocumented agent-to-agent calls

**Gate owner:** Agent Architect

---

## B2. System-Level Safety Controls

* [ ] System-wide kill switch exists and is tested
* [ ] Agent isolation is enforced
* [ ] Blast-radius containment is defined
* [ ] Dependency circuit breakers exist

**Gate owner:** ARE

---

## B3. Unified Observability

* [ ] End-to-end trace across agents exists
* [ ] Aggregated latency is visible
* [ ] Aggregated cost is visible
* [ ] Failure propagation is observable

**Gate owner:** ARE

---

## B4. Cost Governance

* [ ] System-wide cost ceilings enforced
* [ ] Per-agent quotas enforced
* [ ] Cost anomaly detection enabled
* [ ] Automatic throttling configured

**Gate owner:** ARE

---

## B5. Operational Outcome Scoring (OOS)

* [ ] Action Quality signals collected
* [ ] Task Completion signals collected
* [ ] OOS computable near-real-time
* [ ] OOS visible to ARE dashboards

**Gate owner:** ARE

---

## B6. Incident Management Readiness

* [ ] Incident playbooks exist
* [ ] On-call ownership defined
* [ ] Safe shutdown procedures tested
* [ ] Post-incident data retained

**Gate owner:** ARE

---

## B7. Security & Isolation

* [ ] Tool access is least-privilege
* [ ] Secrets are isolated
* [ ] Prompt injection mitigations exist
* [ ] Tenant isolation enforced (if applicable)

**Gate owner:** Security / Platform

---

## B8. Audit & Evidence Readiness

* [ ] Decision and action logs retained
* [ ] Override records retained
* [ ] Safety control changes logged
* [ ] Version lineage reconstructable

**Gate owner:** AI Risk & Audit Owner

---

## B9. Dependency & Provider Resilience

* [ ] Provider failover strategy exists
* [ ] Graceful degradation tested
* [ ] Compatibility validation performed

**Gate owner:** ARE

---

# Final Production Gate

An Agent or AOS is **NOT production-ready** unless:

* [ ] All Agent-level checklist items are YES
* [ ] All AOS-level checklist items are YES
* [ ] APO signs off on intent
* [ ] ARE signs off on operational safety
* [ ] ARAO signs off on policy & audit

There are **no partial approvals**.

---

> **If a single checkbox cannot be answered with evidence, the system is not ready.**

*End of checklist*
