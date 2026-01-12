# Personas and OPDA Needs

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-11

---

## Overview

This document maps **OPDA capabilities** (Observability, Predictability, Directability, Authority Enforcement) to the **enterprise personas** defined in Seer. Each persona requires different aspects of OPDA to fulfill their responsibilities in the agent lifecycle.

**OPDA Definition:**
- **O** - Observability: Can we see what the agent is doing and why?
- **P** - Predictability: Will the agent behave consistently?
- **D** - Directability: Can humans guide or override the agent?
- **A** - Authority Enforcement: Are agents operating within delegated limits?

---

## 1. Automation Product Owner (APO)

**Primary Mandate:** Own intent and business accountability of automation (including agents).

### Observability Needs
- ❌ Business outcome metrics (agent contribution to business goals)
- ❌ Value delivery tracking (ROI, business impact)
- ❌ User satisfaction metrics (feedback, trust indicators)
- ❌ Agent performance against success criteria
- ❌ Cost-benefit analysis (cost vs. value delivered)

### Predictability Needs
- ❌ Behavioral consistency validation (agent behaves as intended)
- ❌ Outcome predictability (can anticipate agent results)
- ❌ Autonomy boundary validation (agent stays within intended scope)
- ❌ Business rule adherence (agent follows business policies)

### Directability Needs
- ❌ Autonomy adjustment (modify agent autonomy levels)
- ❌ Scope modification (change what agent is allowed to do)
- ❌ Priority adjustment (reprioritize agent work)
- ❌ Business rule updates (modify business constraints)

### Authority Needs
- ❌ Autonomy proposal framework (propose autonomy levels)
- ❌ Authority limit definition (define what agent can do)
- ❌ Business policy enforcement (ensure agent follows business rules)
- ❌ Autonomy approval workflow (submit for ARAO approval)

---

## 2. Cognitive Systems Architect (CSA)

**Primary Mandate:** Design how cognition is allowed to work across agents and AOS.

### Observability Needs
- ❌ Reasoning pattern visibility (how agents reason)
- ❌ Cognitive flow tracing (reasoning steps, decision points)
- ❌ Multi-agent interaction observability (agent-to-agent communication)
- ❌ Design validation metrics (does implementation match design?)
- ❌ Cognitive boundary compliance (agents stay within design boundaries)

### Predictability Needs
- ✅ Design-time constraints definition - `guardrails.md` §Guardrail Types
- ❌ Reasoning pattern consistency (agents reason as designed)
- ❌ Failure semantics validation (failures occur as designed)
- ❌ Escalation design validation (escalation works as designed)
- ❌ Multi-agent system predictability (interactions are predictable)

### Directability Needs
- ❌ Design pattern enforcement (ensure agents follow design patterns)
- ❌ Cognitive boundary enforcement (prevent agents from exceeding design scope)
- ❌ Escalation design implementation (ensure escalation works as designed)

### Authority Needs
- ❌ Design-time authority constraints (define authority limits in design)
- ❌ Cognitive authority boundaries (what agents can reason about)
- ❌ Authority ceiling design (design authority limits)

---

## 3. Agent Engineer (AE)

**Primary Mandate:** Implement agents correctly and completely.

### Observability Needs
- ✅ Agent-level observability (SDK metrics, logs, traces) - `agent-observability.md` §Layer 1: Agent-Level Observability
- ✅ Custom business metrics - `agent-observability.md` §Metrics
- ✅ Debugging observability (reasoning traces, tool calls) - `agent-observability.md` §Tracing
- ❌ Implementation validation (does code match design?)
- ❌ Test observability (observability during testing)

### Predictability Needs
- ❌ Implementation predictability (code behaves predictably)
- ❌ Test predictability (tests validate predictable behavior)
- ❌ Execution bounds validation (bounds are enforced)
- ❌ Safety hook validation (safety mechanisms work)

### Directability Needs
- ❌ Implementation of escalation hooks (per CSA design)
- ❌ Safety mechanism implementation (kill switches, bounds)
- ❌ Override mechanism implementation (allow human intervention)

### Authority Needs
- ❌ Authority implementation (implement authority constraints)
- ❌ Guardrail implementation (implement guardrails per design)
- ❌ Authority testing (test authority enforcement)

---

## 4. Knowledge & Memory Owner (KMO)

**Primary Mandate:** Own what agents know and remember.

### Observability Needs
- ❌ Knowledge usage tracking (what knowledge agents use)
- ❌ Memory access patterns (how agents access memory)
- ❌ Knowledge quality metrics (accuracy, freshness, relevance)
- ❌ Tool usage patterns (which tools agents use)
- ❌ Knowledge drift detection (knowledge changes affecting behavior)

### Predictability Needs
- ❌ Knowledge versioning (versioned knowledge for reproducibility)
- ❌ Knowledge binding (agents bound to specific knowledge versions)
- ❌ Knowledge change impact (predict behavior changes from knowledge updates)
- ❌ Tool availability predictability (tools available when needed)

### Directability Needs
- ❌ Knowledge curation (modify what agents know)
- ❌ Tool access control (enable/disable tool access)
- ❌ Memory governance (control what goes into memory)

### Authority Needs
- ❌ Knowledge authority (control what knowledge agents can access)
- ❌ Tool access authority (control which tools agents can use)
- ❌ Memory write authority (control what agents can remember)

---

## 5. Agent Reliability Engineer (ARE)

**Primary Mandate:** Ensure agents and AOS are safe to run in production.

### Observability Needs
- ✅ Agent Health Score (AHS) - `are.md` §The ARE Control Loop §Agent Health Score
- ✅ System health observability (latency, errors, availability) - `observability-extensions-to-watch/persona-dashboards.md` §Persona 3: SRE for Agentic Systems
- ✅ Cost observability (token usage, cost tracking) - `observability-extensions-to-watch/persona-dashboards.md` §Persona 3: SRE for Agentic Systems §Metrics §Cost Control Metrics
- ✅ Reliability metrics (requests, latency, SLA compliance) - `observability-extensions-to-watch/persona-dashboards.md` §Persona 3: SRE for Agentic Systems §Metrics §Reliability Metrics
- ✅ Retry and circuit breaker metrics - `observability-extensions-to-watch/persona-dashboards.md` §Persona 3: SRE for Agentic Systems §Metrics §Retry & Circuit Breaker Metrics
- ✅ Multi-agent metrics (delegations, cascade failures) - `observability-extensions-to-watch/persona-dashboards.md` §Persona 3: SRE for Agentic Systems §Metrics §Multi-Agent Metrics
- ✅ Platform health dashboards - `observability-extensions-to-watch/persona-dashboards.md` §Persona 1: AI Platform Engineer
- ✅ Operational tools (circuit breaker control, load shedder, agent throttle) - `observability-extensions-to-watch/operational-tools.md` §Agent Management Tools

### Predictability Needs
- ❌ Operational predictability (agents fail predictably)
- ❌ Recovery predictability (recovery procedures work)
- ❌ Cost predictability (cost stays within bounds)
- ❌ Failure mode predictability (failures are bounded)

### Directability Needs
- ✅ Kill switch capability - `agent-lifecycle-api.md` §Kill Switch
- ✅ Suspend/revoke employment - `agent-lifecycle-api.md` §Suspend Employment, §Revoke Employment
- ✅ Cost kill-switch - `observability-extensions-to-watch/operational-tools.md` §Agent Management Tools
- ✅ Agent throttle - `observability-extensions-to-watch/operational-tools.md` §Agent Management Tools
- ✅ Load shedder - `observability-extensions-to-watch/operational-tools.md` §Agent Management Tools
- ✅ Circuit breaker control - `observability-extensions-to-watch/operational-tools.md` §Agent Management Tools
- ❌ Graceful degradation controls
- ❌ Recovery operations

### Authority Needs
- ❌ Runtime authority enforcement (ensure agents stay within limits)
- ❌ Authority monitoring (monitor authority usage)
- ❌ Authority violation detection (detect when agents exceed authority)

---

## 6. Cognitive Operations Steward (COS)

**Primary Mandate:** Maintain day-to-day cognitive health of agents.

### Observability Needs
- ❌ Cognitive health metrics (reasoning quality, consistency)
- ❌ Behavioral drift detection (agent behavior changing over time)
- ❌ Confusion detection (agent misunderstanding situations)
- ❌ Decision quality metrics (accuracy, appropriateness)
- ❌ User satisfaction tracking (feedback, override frequency)
- ❌ Intent alignment metrics (agent pursuing right objectives)
- ❌ Reasoning consistency metrics (similar inputs produce similar outputs)

### Predictability Needs
- ❌ Behavioral consistency monitoring (track consistency over time)
- ❌ Drift detection (detect gradual behavior changes)
- ❌ Pattern break detection (detect unexpected behavior changes)
- ❌ Confidence calibration (track confidence vs. accuracy)

### Directability Needs
- ❌ Feedback routing (route issues to appropriate owners)
- ❌ Intervention recommendations (suggest when intervention needed)
- ❌ Quality improvement triggers (trigger improvements based on observations)

### Authority Needs
- ❌ Policy adherence monitoring (monitor if agents follow policies)
- ❌ Authority usage monitoring (monitor authority utilization)

---

## 7. AI Risk & Audit Owner (ARAO)

**Primary Mandate:** Ensure agents are defensible to regulators and stakeholders.

### Observability Needs
- ✅ Security metrics (prompt injection, jailbreak attempts) - `observability-extensions-to-watch/persona-dashboards.md` §Persona 4: Security Architect §Metrics §Security Metrics
- ✅ Tool access control metrics - `observability-extensions-to-watch/persona-dashboards.md` §Persona 4: Security Architect §Metrics §Security Metrics
- ✅ Data security metrics (PII access, exfiltration blocks) - `observability-extensions-to-watch/persona-dashboards.md` §Persona 4: Security Architect §Metrics §Security Metrics
- ✅ Audit metrics (sensitive decisions, human overrides) - `observability-extensions-to-watch/persona-dashboards.md` §Persona 4: Security Architect §Metrics §Security Metrics
- ✅ Security dashboards - `observability-extensions-to-watch/persona-dashboards.md` §Persona 4: Security Architect
- ❌ Policy compliance tracking (continuous policy adherence)
- ❌ Audit trail completeness (all decisions auditable)
- ❌ Explainability metrics (can we explain decisions?)

### Predictability Needs
- ❌ Policy compliance predictability (agents comply with policy)
- ❌ Security behavior predictability (agents resist attacks predictably)
- ❌ Audit readiness (audit evidence is complete)

### Directability Needs
- ❌ Autonomy approval authority (approve/reject autonomy proposals)
- ❌ Policy enforcement override (override policy when needed)
- ❌ Security control adjustment (adjust security controls)

### Authority Needs
- ✅ Authority approval (approve autonomy proposals) - `roles.md` §7. AI Risk & Audit Owner (ARAO) §Autonomy Lifecycle
- ✅ Policy compliance enforcement - `authority-enforcement.md` §OPA Policy Model
- ✅ Security authority controls (tool access, data access) - `authority-enforcement.md` §Integration with IAM
- ❌ Authority limit approval (approve authority ceilings)
- ❌ Authority violation response (respond to authority violations)

---

## Cross-Persona OPDA Needs

### Shared Observability Needs
- ✅ Platform-level dashboards (unified view) - `observability-extensions-to-watch/persona-dashboards.md` (all personas)
- ✅ Alerting infrastructure - `agent-observability.md` §Alerts
- ❌ Cross-persona observability (different views for different personas)
- ❌ Persona-specific dashboards (tailored to each persona's needs)

### Shared Predictability Needs
- ❌ Behavioral baseline establishment (shared baselines)
- ❌ Predictability certification (certify agents meet predictability requirements)

### Shared Directability Needs
- ❌ Unified directability interface (common interface for all personas)
- ❌ Directability workflow (standardized intervention process)

### Shared Authority Needs
- ✅ Authority enforcement infrastructure - `authority-enforcement.md`
- ✅ Guardrail infrastructure - `guardrails.md`
- ❌ Authority governance framework (shared authority governance)

---

## OPDA Capability Gaps by Persona

### APO Gaps
- ❌ Business outcome observability
- ❌ Autonomy proposal framework
- ❌ Business rule enforcement

### CSA Gaps
- ❌ Reasoning pattern observability
- ❌ Design validation metrics
- ❌ Cognitive boundary enforcement

### AE Gaps
- ❌ Implementation validation observability
- ❌ Test observability
- ❌ Implementation predictability validation

### KMO Gaps
- ❌ Knowledge usage observability
- ❌ Knowledge versioning and binding
- ❌ Knowledge authority controls

### ARE Gaps
- ❌ Cognitive health observability (deferred to COS)
- ❌ Operational predictability monitoring
- ❌ Recovery predictability

### COS Gaps
- ❌ Cognitive health metrics
- ❌ Behavioral drift detection
- ❌ Reasoning consistency metrics
- ❌ Feedback routing mechanisms

### ARAO Gaps
- ❌ Policy compliance tracking
- ❌ Audit trail completeness validation
- ❌ Explainability metrics
- ❌ Authority limit approval workflow

---

## Document References

- `olympus-seer-docs/seer-design/personas-and-needs/roles.md` - Persona definitions
- `olympus-seer-docs/seer-design/personas-and-needs/apo.md` - APO role details
- `olympus-seer-docs/seer-design/personas-and-needs/csa.md` - CSA role details
- `olympus-seer-docs/seer-design/personas-and-needs/ae.md` - AE role details
- `olympus-seer-docs/seer-design/personas-and-needs/kmo.md` - KMO role details
- `olympus-seer-docs/seer-design/personas-and-needs/are.md` - ARE role details
- `olympus-seer-docs/seer-design/personas-and-needs/cos.md` - COS role details
- `olympus-seer-docs/seer-design/personas-and-needs/arao.md` - ARAO role details
- `olympus-seer-docs/seer-design/subsystems/agent-observability.md` - Observability capabilities
- `olympus-seer-docs/seer-design/subsystems/observability-extensions-to-watch/README.md` - Platform observability
- `olympus-seer-docs/seer-design/subsystems/authority-enforcement.md` - Authority enforcement
- `olympus-seer-docs/seer-design/subsystems/guardrails.md` - Guardrails
- `olympus-seer-docs/seer-design/subsystems/agent-lifecycle-api.md` - Lifecycle and kill switch APIs

---

*This document maps OPDA capabilities to enterprise personas, identifying what each persona needs to fulfill their responsibilities in the agent lifecycle.*
