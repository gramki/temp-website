# Role Definitions

## Core Personas for an Agent-Oriented Enterprise

This document provides **concise, one-page role definitions** for the finalized set of personas required to design, operate, and govern AI Agents and Agent-Oriented Systems (AOS) in an enterprise.

Each role is intentionally **non-overlapping**, **decision-clear**, and **operationally defensible**.

---

## Platform Assumption

> **The AI Agent Platform (Seer, Hub) is a managed platform provided by the platform provider.**

Enterprise roles defined below are **consumers** of the managed platform, not owners of platform infrastructure. Coordination with the platform provider (for capacity, capabilities, incidents) is the responsibility of the **Agent Reliability Engineer (ARE)**.

---

## 1. Automation Product Owner (APO)

> **Note:** APO is a **Hub persona** that covers all automation. This section describes the agentic extensions. See [Hub APO Definition](../../../olympus-hub-docs/08-personas-and-journeys/personas/automation-product-owner.md) for the base role.

**Primary mandate:** Own *intent* and *business accountability* of automation (including agents).

**Owns**

* Automation goals and non-goals
* Business outcomes and success criteria
* Automation approach decision (agentic vs. conventional)
* Autonomy policy proposals (for agentic scenarios)
* Value justification and prioritization
* Improvement prioritization based on operational feedback

**Decides**

* Why the automation exists
* What problems it is allowed to solve
* Whether to pursue agentic or conventional path
* When autonomy expansion is desired (subject to ARAO approval)
* Priority of improvements based on COS/ARE feedback

**Does NOT own**

* Runtime safety or controls
* Cognitive architecture
* Day-to-day operability
* Autonomy approval (ARAO)

**Key question answered**

> "What should this automation do, and why does it matter?"

---

## 2. Cognitive Systems Architect (CSA)

**Primary mandate:** Design *how cognition is allowed to work* across agents and AOS.

**Owns**

* Cognitive patterns and reasoning models
* Agent-to-agent interaction models (including multi-agent systems)
* Failure semantics and escalation design
* Design-time constraints for agents
* Validation of agent designs before implementation

**Decides**

* How agents reason, collaborate, and fail
* What design patterns are acceptable or forbidden
* Escalation model design (implemented by AE, operated by ARE)

**Does NOT own**

* Business intent
* Runtime enforcement
* Knowledge correctness
* Escalation implementation or operation

**Key question answered**

> "How should intelligence be structured so it is predictable and governable?"

---

## 3. Agent Engineer (AE)

**Primary mandate:** Implement agents correctly and completely.

**Owns**

* Agent code, prompts, workflows, tools
* Safety hooks and telemetry required for operations
* Deterministic execution bounds
* Escalation hook implementation (per CSA design)
* Agent testing and validation (functional correctness)
* Tool integrations and bindings

**Decides**

* How designs are realized in code
* Implementation trade-offs
* Whether implementation meets design requirements (validated by CSA)

**Does NOT own**

* Agent intent
* Runtime policy enforcement
* Audit judgments
* Escalation design (CSA) or operation (ARE)
* Production gate decisions (ARE)

**Key question answered**

> "How do we make this agent actually work as designed?"

---

## 4. Knowledge & Memory Owner (KMO)

**Primary mandate:** Own *what agents know and remember*.

**Owns**

* Domain semantics and ontologies
* Knowledge sources and grounding
* Enterprise Memory governance (CAF policy, retention, decay)
* Tool and Machine Registry curation (what tools agents can use)

**Decides**

* What can become long-term memory
* What is treated as truth vs inference
* Tool availability and appropriateness for agents

**Does NOT own**

* Agent behavior
* Runtime operations
* Business prioritization
* Agent Memory (session state) — owned by AE/ARE

**Scope Clarification**

| Memory Type | KMO Role |
|-------------|----------|
| **Knowledge** (SOPs, policies, grounding data) | Owner |
| **Enterprise Memory** (episodic, semantic via CAF) | Governance |
| **Agent Memory** (session state, context) | Not owned |

**Key question answered**

> "What knowledge is safe, correct, and appropriate for agents to use?"

---

## 5. Agent Reliability Engineer (ARE)

**Primary mandate:** Ensure agents and AOS are *safe to run* in production.

**Owns**

* Runtime safety enforcement
* Observability, AHS (Agent Health Score), and CHR (Cost-to-Health Ratio)
* Cost control and containment
* Incident response and recovery
* Platform provider coordination (capacity, incidents, capabilities)
* Production gate decisions (release readiness)
* Escalation operation (per CSA design)
* Multi-agent system reliability

**Decides**

* Whether operational conditions are safe
* When to degrade or halt execution
* When an agent is ready for production (in coordination with AE, ARAO)
* Platform escalations to provider

**Does NOT own**

* Agent intent or autonomy policy
* Cognitive design
* Business outcomes
* Platform infrastructure (managed by provider)

**Scope Clarification**

| Observability Focus | ARE Role |
|---------------------|-----------|
| **System health** (latency, errors, cost, availability) | Primary owner |
| **Cognitive health** (drift, confusion, quality) | Defers to COS |

**Key question answered**

> "Can this system run right now without loss of control?"

---

## 6. Cognitive Operations Steward (COS)

**Primary mandate:** Maintain *day-to-day cognitive health* of agents.

**Owns**

* Ongoing review of agent behavior
* Detection of drift, confusion, or degradation
* Feedback loops to APO, CSA, and AE

**Decides**

* When behavior quality issues require attention
* When design or intent review should be triggered
* Routing of issues: intent (APO), design (CSA), implementation (AE)

**Does NOT own**

* Runtime controls
* Risk or compliance decisions
* Agent redesign

**Feedback Routing**

| Issue Type | Escalate To |
|------------|-------------|
| Intent misalignment | APO |
| Design flaw | CSA |
| Implementation bug | AE |
| System reliability | ARE |
| Compliance concern | ARAO |

**Key question answered**

> "Is this agent behaving sensibly and usefully over time?"

---

## 7. AI Risk & Audit Owner (ARAO)

**Primary mandate:** Ensure agents are *defensible* to regulators and stakeholders.

**Owns**

* Policy compliance
* Audit readiness and evidence
* Autonomy approvals and limits (approval authority for APO proposals)
* AI Security posture (prompt injection defense, data exfiltration prevention, tool access control)

**Decides**

* Whether agent behavior complies with policy
* Whether autonomy is acceptable (approves APO proposals)
* Whether security controls are sufficient

**Does NOT own**

* Runtime operations
* Agent implementation
* Business prioritization
* Autonomy policy design (APO)

**Autonomy Lifecycle**

| Stage | Responsible |
|-------|-------------|
| Propose autonomy policy | APO |
| Design controls | CSA + AE |
| Approve autonomy | ARAO |
| Enforce at runtime | ARE |

**Key question answered**

> "Can we explain and defend this system's behavior?"

---

## Role Interaction Summary

### Agent Lifecycle Flow

```
APO (Intent) → CSA (Design) → AE (Build) → ARE (Deploy & Operate)
                    ↑                              ↓
                    └──── COS (Monitor & Feedback) ←┘
                                   ↓
                              ARAO (Audit)
```

### Escalation Ownership

| Phase | Owner |
|-------|-------|
| Design | CSA |
| Implementation | AE |
| Operation | ARE |

### Autonomy Approval

| Phase | Owner |
|-------|-------|
| Propose | APO |
| Design controls | CSA + AE |
| Approve | ARAO |
| Enforce | ARE |

---

## Final Alignment Principle

> **Intent is owned by Product (APO).**
> **Cognition is shaped by Architecture (CSA).**
> **Execution is built by Engineering (AE).**
> **Knowledge is curated by Memory (KMO).**
> **Operations are controlled by Reliability (ARE).**
> **Behavior is stewarded continuously (COS).**
> **Risk and Security are judged independently (ARAO).**
> **Platform is managed by the provider; coordinated by Reliability (ARE).**

Together, these roles allow agentic systems to scale **without collapsing into chaos or politics**.

---

*End of document*
