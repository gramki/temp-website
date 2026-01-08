# Journey: Request Lifecycle

> **Status:** 🔴 Stub — Placeholder for expansion

This journey describes how a **Request** flows through the Hub system — from signal receipt through completion. It follows the path from Business Domain Actor → Signal → Application → Agent → Completion.

---

## Overview

A **Request** is the fundamental unit of work in Hub. Each request represents a discrete operation that must be processed to completion.

---

## Request Types

Requests are categorized by **the nature of the work**, not by who originates them:

| Request Type | Nature | Subject | Examples |
|--------------|--------|---------|----------|
| **Service Request** | Customer-facing work | **Always a customer** | Dispute filing, account inquiry, claim submission, service change |
| **Business Request** | Business operations | Optional (may be customer) | Onboarding, compliance review, approval workflow, exception handling |
| **System Request** | System/data integrity issues requiring business resolution | Optional (often an entity) | Reconciliation failure, data integrity violation, consistency error |

### Key Distinctions

| Aspect | Service Request | Business Request | System Request |
|--------|-----------------|------------------|----------------|
| **Subject** | **Always a customer** | Optional | Optional |
| **Self-serve by customer?** | ✅ Yes (only type) | ❌ No | ❌ No |
| **Can Customer originate?** | ✅ Yes (self-serve) | ❌ No | ❌ No |
| **Can Employee originate?** | ✅ Yes (assisted) | ✅ Yes | ❌ No |
| **Can System originate?** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Resolved by** | Business agents | Business agents | Business agents (not SRE) |

### Important Notes

1. **Originator ≠ Request Type**: A system can originate any request type. An employee can originate Service or Business requests. Only customers can self-serve (Service Requests only).

2. **System Requests are NOT technical incidents**: They are system-detected issues (reconciliation failures, data integrity violations, consistency errors) that **require business domain judgment** to resolve — not SRE or technical operations.

3. **Process Architect's choice**: The categorization is a design decision. When a customer is involved, the Process Architect decides whether to model it as a Service Request or Business Request based on operational intent.

See also:
- [Business Customer](../personas/business-domain/business-customer.md) — Can self-serve Service Requests
- [Business Employee](../personas/business-domain/business-employee.md) — Originates Service (assisted) and Business Requests
- [Business System](../personas/business-domain/business-system-actor.md) — Originates all types; System Requests for data/integrity issues

| Phase | Primary Actor | Key Activities |
|-------|---------------|----------------|
| **1. Signal Receipt** | Signal Provider | Event detection, signal delivery |
| **2. Trigger Evaluation** | Signal Exchange | Pattern matching, request creation |
| **3. Application Processing** | Hub Application | Automation, task delegation |
| **4. Task Completion** | Agent | Investigation, decision, action |
| **5. Resolution** | Hub Application | Aggregation, completion |

---

## Phase 1: Signal Receipt

### Actors

- **Signal Providers**: Atropos, Heracles, Cronus, Dia, Kale

### Flow

```
External Event ──→ Signal Provider ──→ Signal Exchange
                                            │
                                            ↓
                                     Trigger Evaluation
```

### Signal Types

| Provider | Signal Type | Example |
|----------|-------------|---------|
| Atropos | Event | Transaction posted |
| Heracles | API Request | Customer dispute submission |
| Cronus | Exception | Fraud alert |
| Dia | File Available | Batch file received |
| Kale | Schedule | Daily reconciliation |

---

## Phase 2: Trigger Evaluation

### Actor: Signal Exchange

### Flow

```
Signal ──→ Match Triggers ──→ Create Request ──→ Route to Application
```

### Activities

1. **Pattern Matching** — Find applicable triggers
2. **Request Creation** — Instantiate request with context
3. **Application Routing** — Dispatch to Hub Application

---

## Phase 3: Application Processing

### Actor: Hub Application

### Flow

```
Request Received ──→ Automation ──→ Task Delegation ──→ Updates
```

### Activities

1. **Context Assembly** — Gather memory, knowledge
2. **Automation Execution** — Run automated steps
3. **Task Delegation** — Create tasks for agents
4. **Progress Updates** — Send async updates to Signal Exchange

---

## Phase 4: Task Completion

### Actor: Agent (Human or AI)

### Flow

```
Task Assigned ──→ Investigation ──→ Decision ──→ Action ──→ Complete
```

### Activities

1. **Task Receipt** — Pick from queue or receive assignment
2. **Investigation** — Query tools, review context
3. **Decision** — Make decision with evidence
4. **Action** — Execute required actions
5. **Completion** — Update task status

---

## Phase 4.5: Rejection Handling (Agent Directability)

When an AI agent's output is **rejected** by guardrails, policies, or applications, the request enters an intervention flow.

### Actors

- **Guardrails/Policies/Applications**: Rejection sources
- **Task Management**: Creates escalation task
- **Supervisor/Senior Agent**: Resolves escalation

### Flow

```
Agent Output ──→ Rejection ──→ Escalation Task Created ──→ Human Resolves
                                      │
                                      ↓
                              ┌─────────────────┐
                              │ Resolution:     │
                              │ • Override      │
                              │ • Context Change│
                              │ • Reassign      │
                              │ • Fail Scenario │
                              │ • Corrective    │
                              └─────────────────┘
```

### Rejection Sources

| Source | Example |
|--------|---------|
| **Guardrail** | Confidence below threshold |
| **Policy** | Amount exceeds auto-approval limit |
| **Application** | Missing required evidence |
| **Another Agent** | Invalid transaction reference |

### Resolution Options

| Resolution | Effect |
|------------|--------|
| **Override Decision** | Replace rejected decision with human-provided value |
| **Change Context & Re-run** | Add context and trigger agent re-evaluation |
| **Reassign Task** | Assign to different agent for retry |
| **Fail Scenario** | Mark request as failed |
| **Corrective Action** | Spawn new request in different scenario |

### Audit Trail

All interventions are recorded in CAF:
- **Override Records** — Decision changes
- **ContextIntervention Records** — Context changes
- **DirectiveResolution Records** — Resolution lifecycle

See [Agent Directability](../../02-system-design/implementation-concepts/agent-directability.md) for the full directability model.

---

## Phase 5: Resolution

### Actor: Hub Application + Signal Exchange

### Flow

```
All Tasks Complete ──→ Aggregate Results ──→ Update Request ──→ Notify
```

### Request Status

| Status | Description |
|--------|-------------|
| ACTIVE | Being processed |
| PENDING | Awaiting external input |
| COMPLETED | Successfully finished |
| CANCELLED | Terminated before completion |

---

## Related Documentation

### Request Types and Originators

- [Business Customer](../personas/business-domain/business-customer.md) — Service Request originator
- [Business Employee](../personas/business-domain/business-employee.md) — Business Request originator
- [Business System](../personas/business-domain/business-system-actor.md) — System Request originator

### Hub Personas

- [Agent Persona](../personas/agent.md) — Processes tasks within requests

### Subsystems

- [Request Lifecycle (Subsystem)](../../04-subsystems/request-management/request-lifecycle.md) — Request states and updates
- [Signal Exchange](../../04-subsystems/signal-exchange/README.md) — Signal to request routing
- [Task Management](../../04-subsystems/task-management/README.md) — Task queues and assignment

### Concepts

- [Ontology - Perception Layer](../../01-concepts/ontology-1-perception-layer.md) — Request type definitions
- [Agent Directability](../../02-system-design/implementation-concepts/agent-directability.md) — Rejection and intervention handling

---

