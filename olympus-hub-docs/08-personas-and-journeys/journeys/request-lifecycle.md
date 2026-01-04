# Journey: Request Lifecycle

> **Status:** 🔴 Stub — Placeholder for expansion

This journey describes how a **Request** flows through the Hub system — from signal receipt through completion. It follows the path from Signal → Application → Agent → Completion.

---

## Overview

A **Request** is the fundamental unit of work in Hub. Each request represents a discrete operation that must be processed to completion.

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

- [Agent Persona](../personas/agent.md)
- [Request Lifecycle](../../04-subsystems/request-management/request-lifecycle.md)
- [Signal Exchange](../../04-subsystems/signal-exchange/README.md)
- [Task Management](../../04-subsystems/task-management/README.md)

---

*TODO: Detailed phase specifications, timing diagrams, exception handling*

