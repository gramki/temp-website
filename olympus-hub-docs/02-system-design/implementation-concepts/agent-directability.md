# Agent Directability

> **Category:** Cognitive Operations  
> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-08

---

## Overview

**Agent Directability** is the ability for humans (and authorized systems) to intervene in, redirect, or override AI agent behavior during cognitive operations. It is one of the three OPD (Observability, Predictability, Directability) properties that agents must exhibit to participate effectively in Human-AI Teams (HAT).

In the AOSM framework, directability is defined as:

> *"The ability to require or request a teammate to perform a desired activity, including deciding whether to direct."*

---

## Ontology Context

### Relationship to AOSM

| AOSM Concept | Hub Implementation | Relationship |
|--------------|-------------------|--------------|
| OPD as Property | Agent Directability | Agents are directable BY humans |
| Controlled Autonomy | Escalation + Override | Autonomy bounded by intervention |
| HAT Coordination | Rejection → Escalation | Team-based problem resolution |
| Accountability | Accountable Human Notification | Human remains responsible |

### Gap This Fills

The AOSM defines directability conceptually. This document specifies:
1. **Intervention Triggers**: What causes intervention?
2. **Escalation Hierarchy**: Who handles interventions?
3. **Resolution Options**: What actions can humans take?
4. **Audit Trail**: How are interventions recorded?

---

## Definition

**Agent Directability** in Hub is the operational mechanism by which:
- AI agents can be redirected when their outputs are rejected
- Humans can intervene to change decisions, context, or task assignments
- The intervention lifecycle is recorded for audit and learning

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Operational (business domain); excludes infrastructure concerns |
| **Trigger** | Rejection events (not proactive commands) |
| **Mechanism** | Escalation via Task Queues with Supervisor-defined matrices |
| **Ownership** | Supervisor defines all escalation matrices |
| **Audit** | CAF records all interventions in Enterprise Memory |

---

## Rationale

### Why This Design?

Reactive directability (rejection → escalation) provides:

1. **Clear Trigger**: Every intervention has an auditable cause
2. **Structured Resolution**: Escalation matrices provide consistent handling
3. **Human Accountability**: Accountable Human is always notified
4. **Audit Completeness**: All interventions recorded in CAF
5. **Learning Foundation**: Interventions feed Enterprise Learning workflows

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Proactive Directive Records** | Confusing overlap with guardrails/policies; rejection-based model is cleaner |
| **Direct Human→Agent Commands** | Bypasses orchestration; loses audit trail; inconsistent with Hub's application-centric model |
| **Kill-switch as Directability** | Infrastructure concern, not business domain; handled by Seer Runtime |

---

## Agent Archetypes

Hub recognizes four functional archetypes that describe what an agent does at any moment. **An agent may wear all hats** — these are perspectives, not exclusive roles.

| Archetype | Function | Rejectable Artifacts |
|-----------|----------|---------------------|
| **Thinker** | Reasoning, decisions | Decision Request, Decision Result |
| **Doer** | Executing actions | Action Request, Action Result |
| **Orchestrator** | Assigning work | Task Assignment |
| **Governor** | Observing, auditing | None (observations are facts, not proposals) |

### Governor Special Case

Governor observations are **never rejected** — they are recorded facts. However, Governor observations may trigger **Enterprise Learning** workflows for pattern analysis and potential authority changes. This is distinct from operational directability.

---

## Rejection as Universal Trigger

All operational directability in Hub flows from **rejection events**. Rejections can originate from:

| Rejection Source | Description |
|------------------|-------------|
| **Agent** | Agent rejects a request or result from another agent |
| **Guardrail** | Seer guardrail blocks an action or output |
| **Scenario Policy** | Scenario-level policy rejects the operation |
| **Hub Application** | Cognitive application logic rejects the artifact |

### Proactive Directability

Proactive human intervention (e.g., "pause and await my review") is achieved by:
1. Defining a **Guardrail** or **Policy** that generates a rejection under specific conditions
2. The rejection triggers normal escalation flow

This keeps the directability model unified and auditable.

---

## Escalation Hierarchy

### Escalation Matrix Ownership

**All escalation matrices are defined by the Supervisor** as part of Workbench operations:

| Escalation Matrix | Scope | Configuration Location | Trigger |
|-------------------|-------|----------------------|---------|
| **Task Queue EM** | Task-level | Task Queue configuration | Time-based (task age) |
| **Scenario EM** | Request/Scenario-level | Scenario Deployment Spec | Rejection-based (guardrail, policy, application) |

### Two Escalation Matrix Types

#### Task Queue Escalation Matrix

Handles **time-based** escalation for stalled tasks:
- Configured per Task Queue by Supervisor
- Adds agents at higher levels when task age exceeds threshold
- Cumulative assignment (lower levels remain assigned)

See [Task Queues](../../04-subsystems/task-management/task-queues.md) for configuration details.

#### Scenario Escalation Matrix

Handles **rejection-based** escalation for application exceptions:
- Configured per Scenario Deployment by Supervisor
- Creates escalation tasks when agent outputs are rejected
- Specifies resolution options (override, context change, etc.)
- Designates Accountable Human for notification

See [Scenario Specification Types](./scenario-specification-types.md) for the `scenario_escalation` block in ScenarioDeploymentSpec.

### Escalation Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          REJECTION EVENT                                     │
│                                                                              │
│  Sources: Agent, Guardrail, Scenario Policy, Application                    │
└──────────────────────────────────┬──────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                          SIGNAL EXCHANGE                                     │
│                                                                              │
│  • Routes REQUEST_UPDATE containing rejection                                │
│  • Notifies Hub Application                                                  │
│  • Task Management observes and handles escalation                          │
└──────────────────────────────────┬──────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                       ESCALATION RESOLUTION                                  │
│                                                                              │
│  1. Identify applicable Escalation Matrix:                                   │
│     • Task exceptions → Task Queue EM                                        │
│     • Application exceptions → Scenario EM                                   │
│                                                                              │
│  2. Create Escalation Task:                                                  │
│     • Assign to next level in escalation queue                               │
│     • Notify Accountable Human                                               │
│     • Notify additional watchers                                             │
│                                                                              │
│  3. Human resolves (see Resolution Options below)                            │
│                                                                              │
│  4. Resolution recorded in CAF                                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Resolution Options

When an escalation is handled, the human (or escalation agent) has specific resolution options based on the rejection type:

### Resolution by Rejection Type

| Rejection Type | Resolution Options |
|----------------|-------------------|
| **Decision Result** | • Change context and re-run thinking |
|                     | • Change the decision and continue scenario |
| **Decision Request** | • Change context and re-run thinking |
|                      | • Fail the scenario |
| **Task Assignment** | • Reassign to alternative agent in queue |
|                     | • Give task failure result |
|                     | • Abandon task |
| **Action Request** | • Reject the action (block execution) |
| **Action Result** | • Create corrective action task (may be different scenario) |
|                   | • Reassign to alternative agent |
|                   | • Give task failure result |
|                   | • Abandon task |

### Task Completion Exception

Task Completion is **not rejectable**:
- A task is either an action task or decision task
- Completion is expressed as Action Result or Decision Result (both rejectable)
- Governance tasks (Governor observations) cannot be rejected

---

## CAF Integration

All directability interventions are recorded in the **Cognitive Audit Fabric** as part of Enterprise Memory (Episodic Memory Store).

### Intervention Records

| Record Type | Purpose | When Created |
|-------------|---------|--------------|
| **Override Record** | Documents decision changes | Human changes a decision |
| **ContextIntervention Record** | Documents context changes | Human modifies context for re-run |
| **DirectiveResolution Record** | Tracks intervention lifecycle | Acknowledgment and outcome of intervention |
| **Handoff Context** | Documents state transfer | Escalation between agents/levels |

### DirectiveResolution Record

New record type for tracking the complete intervention lifecycle:

```json
{
  "record_type": "DirectiveResolution",
  "record_id": "uuid",
  "request_id": "uuid",
  "case_id": "uuid",
  
  "subtype": "ack | outcome",
  
  "intervention_ref": {
    "record_type": "Override | ContextIntervention",
    "record_id": "uuid"
  },
  
  "resolution": {
    "status": "acknowledged | executed | failed | superseded",
    "resolved_by": "user_id | agent_id",
    "resolved_at": "timestamp",
    "notes": "string"
  },
  
  "outcome": {
    "result_type": "decision_changed | context_rerun | task_reassigned | scenario_failed | corrective_action_spawned",
    "result_ref": "reference to new decision/task/scenario if applicable"
  },
  
  "hub_metadata": {
    "tenant_id": "string",
    "subscription_id": "string",
    "workbench_id": "string"
  }
}
```

### Existing Task Records

Task Management already records task lifecycle events. These are **referenced, not duplicated** in CAF:

| Task Event | Task Management Record | CAF Relationship |
|------------|----------------------|------------------|
| ASSIGNED | Task History | Referenced by case_id |
| ESCALATED | Task History | Referenced; triggers HandoffContext |
| ABANDONED | Task History + Memo | Referenced by case_id |
| REASSIGNED | Task History | May trigger Override if decision-related |

---

## Cross-Scenario Tracing

When resolution spawns work in another scenario, tracing is provided by existing mechanisms:

| Scenario Relationship | Tracing Mechanism |
|-----------------------|-------------------|
| **Same Workbench** | Parent-child request refs (`parent_request_id`) |
| **Cross-Workbench** | Tool use traces (correlation via Tool invocation record) |

No additional CAF schema is required for cross-scenario directability tracing.

---

## Out of Scope

The following are **not part of operational directability**:

| Concern | Reason | Where Handled |
|---------|--------|---------------|
| **Kill-switch** | Infrastructure concern, not business domain | Seer Runtime (Agent Lifecycle Service) |
| **Authority Revocation** | Requires deliberation from multiple observations; not inline decision | Enterprise Learning workflow |
| **Governor Observations** | Facts, not proposals; cannot be rejected | Recorded as-is; may feed Enterprise Learning |

---

## Behavior

### Directability Flow Example

```
1. Agent (Thinker) produces Decision Result
   └── Guardrail rejects: "Confidence below threshold"

2. Rejection routed via Signal Exchange
   └── Hub Application receives REQUEST_UPDATE with rejection

3. Task Management creates Escalation Task
   └── Assigned to Escalation Queue Level 1 (Senior Analyst)
   └── Accountable Human notified

4. Senior Analyst reviews
   └── Decision: Change context and re-run
   └── ContextIntervention record created

5. Agent re-runs with new context
   └── New Decision Result produced
   └── DirectiveResolution record created (subtype: outcome)

6. Scenario continues
```

### Integration with Task States

Directability integrates with existing Task Management states:

| Intervention | Task State Impact |
|--------------|-------------------|
| Context change, re-run | Task remains IN_PROGRESS; new attempt |
| Decision override | Task may complete with overridden decision |
| Task reassignment | New ASSIGNED event; original assignee remains |
| Task abandonment | ABANDONED → PENDING (re-queued) |
| Scenario failure | All tasks CANCELLED |

---

## Related Concepts

| Concept | Relationship |
|---------|-------------|
| [Escalation Matrix](./escalation-matrix.md) | Defines escalation levels and candidates |
| [Cognitive Audit Fabric](./cognitive-audit-fabric.md) | Control plane for intervention records |
| [Signal Exchange](./signal-exchange.md) | Routes rejection events |
| [Task Allocation](./task-allocation.md) | Handles reassignment after intervention |
| [Observer Pattern](./observer-pattern.md) | Task Management observes rejection events |

---

## Subsystem References

| Subsystem | Relevance |
|-----------|-----------|
| [Task Management](../../04-subsystems/task-management/README.md) | Escalation execution, task reassignment |
| [Task Queues](../../04-subsystems/task-management/task-queues.md) | Escalation Task Queue for rejection handling |
| [Agent Task Operations](../../04-subsystems/task-management/agent-task-operations.md) | Directability operations (override, context change, etc.) |
| [Signal Exchange](../../04-subsystems/signal-exchange/README.md) | Rejection routing |
| [Cognitive Audit Fabric](../../04-subsystems/cognitive-audit-fabric/README.md) | Intervention record storage |
| [Notification Services](../../04-subsystems/notification-services/README.md) | Accountable Human alerts |
| [Workbench Management](../../04-subsystems/workbench-management/README.md) | Escalation matrix configuration |

## UX References

| UX Component | Relevance |
|--------------|-----------|
| [Agent Desk](../../06-ux-architecture/tenant-domain/agent-desk.md) | Intervention Solver Interface |
| [REST Channels](../../06-ux-architecture/tenant-domain/rest-channels.md) | Directability REST APIs |
| [MCP Channels](../../06-ux-architecture/tenant-domain/mcp-channels.md) | Directability MCP methods |

---

## Persona Responsibilities

| Persona | Directability Responsibility |
|---------|------------------------------|
| **Supervisor** | Defines all escalation matrices; handles escalated tasks; overrides decisions |
| **Agent** | Completes escalated tasks; may trigger rejection by abandoning |
| **Process Architect** | Defines guardrails and policies that trigger rejections |
| **Developer** | Implements application logic that may reject artifacts |

See [Personas and Journeys](../../08-personas-and-journeys/README.md) for full persona definitions.

---

## Enterprise Learning Connection

While operational directability handles immediate intervention, patterns in interventions feed **Enterprise Learning Services**:

| Learning Input | Learning Output |
|----------------|-----------------|
| Repeated overrides of same decision type | Potential guardrail adjustment |
| Frequent context interventions | Potential SOP refinement |
| Governor observations across cases | Pattern detection for semantic memory |

See [Enterprise Learning Services](../../04-subsystems/cognitive-audit-fabric/enterprise-learning-services.md) for details.

---

## ADR References

| ADR | Decision |
|-----|----------|
| [ADR-0078](../../decision-logs/0078-agent-directability-rejection-escalation.md) | Agent Directability via Rejection-Escalation Model |
| [ADR-0079](../../decision-logs/0079-scenario-escalation-matrix.md) | Scenario Escalation Matrix for Application Exceptions |
| [ADR-0080](../../decision-logs/0080-directability-operations.md) | Directability Operations in Task Management |

---

