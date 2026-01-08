# ADR-0078: Agent Directability via Rejection-Escalation Model

**Status**: Accepted  
**Date**: 2026-01-08  
**Category**: directability

---

## Context

AI agents in Hub need to be **directable** — humans must be able to intervene in, redirect, or override agent behavior during cognitive operations. This is one of the three OPD (Observability, Predictability, Directability) properties required by the AOSM framework for effective Human-AI Teams.

We needed to decide:
1. What **triggers** directability interventions?
2. How are interventions **handled**?
3. How are interventions **recorded**?

---

## Decision

Agent Directability in Hub is implemented via a **Rejection-Escalation Model**:

1. **Rejection as Universal Trigger**: All operational directability flows from rejection events. Rejections can originate from Agents, Guardrails, Scenario Policies, or Hub Applications.

2. **Escalation via Supervisor-Defined Matrices**: When a rejection occurs, an Escalation Task is created using the applicable Escalation Matrix (Task Queue EM or Scenario EM). The Supervisor defines all escalation matrices.

3. **Resolution via Defined Operations**: Humans resolve escalations through structured operations (override, context change, reassign, fail, corrective action).

4. **Audit via CAF Records**: All interventions are recorded in CAF (Override Records, ContextIntervention Records, DirectiveResolution Records).

### Agent Archetypes

Four functional archetypes describe what an agent does at any moment:

| Archetype | Function | Rejectable Artifacts |
|-----------|----------|---------------------|
| **Thinker** | Reasoning, decisions | Decision Request, Decision Result |
| **Doer** | Executing actions | Action Request, Action Result |
| **Orchestrator** | Assigning work | Task Assignment |
| **Governor** | Observing, auditing | None (observations are facts) |

### What's NOT Operational Directability

| Concern | Reason | Where Handled |
|---------|--------|---------------|
| **Kill-switch** | Infrastructure concern | Seer Runtime (Agent Lifecycle) |
| **Authority Revocation** | Requires deliberation | Enterprise Learning workflow |
| **Governor Observations** | Facts, not proposals | Recorded as-is; feed Enterprise Learning |

---

## Consequences

### Positive
- **Unified Model**: All interventions have auditable causes (rejections)
- **Clear Responsibility**: Supervisor owns all escalation matrices
- **Audit Completeness**: CAF records provide full intervention history
- **Learning Foundation**: Interventions feed Enterprise Learning for pattern detection

### Negative
- **Reactive Only**: No proactive "pause and review" unless modeled as guardrail rejection
- **Escalation Overhead**: Every intervention requires task creation

### Neutral
- **Proactive Control via Guardrails**: Proactive intervention is achieved by defining guardrails/policies that generate rejections under specific conditions

---

## Related

- [Agent Directability](../02-system-design/implementation-concepts/agent-directability.md)
- [Agent Model — Agent Directability Section](../02-system-design/agent-model.md#agent-directability)
- [ADR-0079: Scenario Escalation Matrix](./0079-scenario-escalation-matrix.md)
- [ADR-0080: Directability Operations](./0080-directability-operations.md)
- [Cognitive Audit Fabric](../04-subsystems/cognitive-audit-fabric/README.md)


