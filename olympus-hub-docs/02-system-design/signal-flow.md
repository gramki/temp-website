# Signal Flow

> **End-to-end journey from Signal to Outcome**

---

## Overview

This document traces the complete path a signal takes through Olympus Hub — from its origin in the external world to the final outcome delivered back. Understanding this flow is essential for developers building Hub Applications and architects designing operational scenarios.

---

## The Flow at a Glance

```
Signal → I/O Gateway → Signal Exchange → Hub Application → Task → Agent → Action → Outcome
```

### Component Roles

| Component | Role in Flow |
|-----------|--------------|
| **Signal** | Input from the environment indicating something happened |
| **I/O Gateway** | Protocol adapter that normalizes the signal |
| **Signal Exchange** | Central router that matches and orchestrates |
| **Hub Application** | Automation that processes the request |
| **Task** | Unit of work assigned to an agent |
| **Agent** | Human or AI executor |
| **Action** | Atomic operation performed |
| **Outcome** | Result delivered back to originators |

---

## Complete Signal Flow

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                           SIGNAL FLOW - END TO END                                       │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                          │
│  EXTERNAL WORLD                                                                          │
│  ──────────────                                                                          │
│                                                                                          │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐                      │
│  │ HTTP Request    │    │  Kafka Event    │    │  File Upload    │                      │
│  │ (Customer files │    │ (Transaction    │    │  (Batch data    │                      │
│  │  dispute)       │    │  completed)     │    │   arrives)      │                      │
│  └────────┬────────┘    └────────┬────────┘    └────────┬────────┘                      │
│           │                      │                      │                                │
│           ▼                      ▼                      ▼                                │
│                                                                                          │
│  PERCEPTION LAYER                                                                        │
│  ────────────────                                                                        │
│                                                                                          │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐                      │
│  │    HERACLES     │    │    ATROPOS      │    │      DIA        │                      │
│  │   I/O Gateway   │    │   I/O Gateway   │    │   I/O Gateway   │                      │
│  │   (HTTP/REST)   │    │   (Events)      │    │   (Files)       │                      │
│  └────────┬────────┘    └────────┬────────┘    └────────┬────────┘                      │
│           │                      │                      │                                │
│           │     NORMALIZE        │      NORMALIZE       │     NORMALIZE                  │
│           │                      │                      │                                │
│           └──────────────────────┼──────────────────────┘                                │
│                                  │                                                       │
│                                  ▼                                                       │
│                     ┌─────────────────────────┐                                         │
│                     │   NORMALIZED SIGNAL     │                                         │
│                     │   (Standard DTO)        │                                         │
│                     └────────────┬────────────┘                                         │
│                                  │                                                       │
│                                  ▼                                                       │
│                     ┌─────────────────────────────────────────────────────────────────┐ │
│                     │                   SIGNAL EXCHANGE                                │ │
│                     │                                                                  │ │
│                     │  ┌──────────────┐    ┌──────────────┐    ┌──────────────────┐  │ │
│                     │  │   Trigger    │───▶│   Request    │───▶│   Application    │  │ │
│                     │  │  Evaluator   │    │   Factory    │    │     Router       │  │ │
│                     │  └──────────────┘    └──────────────┘    └────────┬─────────┘  │ │
│                     │                                                   │             │ │
│                     └───────────────────────────────────────────────────┼─────────────┘ │
│                                                                         │               │
│                                                                         ▼               │
│  AUTOMATION LAYER                                                                       │
│  ────────────────                                                                       │
│                                                                         │               │
│                     ┌─────────────────────────────────────────────────────────────────┐ │
│                     │                   HUB APPLICATION                                │ │
│                     │                                                                  │ │
│                     │  ┌──────────────┐    ┌──────────────┐    ┌──────────────────┐  │ │
│                     │  │   Receive    │───▶│   Process    │───▶│   Delegate       │  │ │
│                     │  │   Request    │    │   Logic      │    │   Tasks          │  │ │
│                     │  └──────────────┘    └──────────────┘    └────────┬─────────┘  │ │
│                     │                                                   │             │ │
│                     └───────────────────────────────────────────────────┼─────────────┘ │
│                                                                         │               │
│                                                                         ▼               │
│  EXECUTION LAYER                                                                        │
│  ───────────────                                                                        │
│                                                                                          │
│  ┌─────────────────────────────────────────────────────────────────────────────────────┐│
│  │                            TASK MANAGEMENT                                           ││
│  │                                                                                      ││
│  │   ┌─────────────┐         ┌─────────────┐         ┌─────────────┐                   ││
│  │   │ Task Queue  │         │   Direct    │         │  Escalation │                   ││
│  │   │ Assignment  │         │  Assignment │         │    Matrix   │                   ││
│  │   └──────┬──────┘         └──────┬──────┘         └──────┬──────┘                   ││
│  │          │                       │                       │                          ││
│  │          └───────────────────────┼───────────────────────┘                          ││
│  │                                  │                                                   ││
│  │                                  ▼                                                   ││
│  │                         ┌─────────────────┐                                         ││
│  │                         │      AGENT      │                                         ││
│  │                         │  (Human or AI)  │                                         ││
│  │                         └────────┬────────┘                                         ││
│  │                                  │                                                   ││
│  │                                  │  Executes Actions                                 ││
│  │                                  ▼                                                   ││
│  │                         ┌─────────────────┐                                         ││
│  │                         │     TOOLS       │                                         ││
│  │                         │  (Commands on   │                                         ││
│  │                         │   Machines)     │                                         ││
│  │                         └────────┬────────┘                                         ││
│  │                                  │                                                   ││
│  └──────────────────────────────────┼───────────────────────────────────────────────────┘│
│                                     │                                                    │
│                                     │  Task Complete                                     │
│                                     ▼                                                    │
│                     ┌─────────────────────────┐                                         │
│                     │   REQUEST UPDATE        │                                         │
│                     │   (flows back to SX)    │                                         │
│                     └────────────┬────────────┘                                         │
│                                  │                                                       │
│                                  ▼                                                       │
│                     ┌─────────────────────────────────────────────────────────────────┐ │
│                     │   OBSERVER NOTIFICATION                                          │ │
│                     │                                                                  │ │
│                     │   ├── Notification Services → Customer notified                 │ │
│                     │   ├── Task Management → Dashboards updated                      │ │
│                     │   └── MS Teams → Collaboration channels updated                 │ │
│                     │                                                                  │ │
│                     └─────────────────────────────────────────────────────────────────┘ │
│                                                                                          │
└──────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## Flow Phases

### Phase 1: Signal Arrival

Signals originate from external systems and enter Hub through protocol-specific I/O Gateways.

| Gateway | Protocol | Example Signal |
|---------|----------|----------------|
| **Heracles** | HTTP/REST/MCP | Customer files dispute via API |
| **Atropos** | Event Bus | Transaction completed event |
| **Cronus** | Exception API | System exception requiring attention |
| **Dia** | File/Batch | Batch file uploaded via SFTP |
| **Kale** | Scheduler | Scheduled reconciliation trigger |

→ **Details:** [I/O Gateway](./implementation-concepts/io-gateway.md)

---

### Phase 2: Signal Normalization

Each Gateway normalizes its protocol-specific input to a standard Normalized Signal DTO:

```json
{
  "signal_header": {
    "tenant_id": "acme-bank",
    "subscription_id": "sub-prod-001",
    "signal_id": "sig-12345",
    "signal_type": "dispute.filed",
    "timestamp": "2026-01-06T10:00:00Z",
    "correlation_id": "txn-99999",
    "idempotency_key": "idem-22222"
  },
  "payload": {
    "content_type": "application/json",
    "data": { /* protocol-specific data */ }
  },
  "metadata": {
    "source_system": "customer-portal",
    "trace_id": "trace-abc123"
  }
}
```

→ **Details:** [Normalized Signal Format](./implementation-concepts/normalized-signal-format.md)

---

### Phase 3: Signal Exchange Processing

Signal Exchange is the central orchestration engine. It:

1. **Receives** normalized signal from Gateway
2. **Evaluates** registered triggers to find matches
3. **Creates** a Request (or correlates to existing Request)
4. **Routes** to the appropriate Hub Application
5. **Notifies** registered observers

```
┌──────────────────────────────────────────────────────────────────────────┐
│  SIGNAL EXCHANGE INTERNALS                                                │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  Normalized Signal                                                        │
│       │                                                                   │
│       ▼                                                                   │
│  ┌─────────────────┐                                                     │
│  │ Signal Intake   │                                                     │
│  └────────┬────────┘                                                     │
│           │                                                               │
│           ▼                                                               │
│  ┌─────────────────┐     ┌─────────────────────────────────────────────┐ │
│  │ Trigger         │     │ Registered Triggers:                         │ │
│  │ Evaluator       │────▶│   • dispute-filed-trigger → dispute-handler │ │
│  │                 │     │   • payment-completed → settlement-app       │ │
│  └────────┬────────┘     │   • batch-ready → batch-processor            │ │
│           │              └─────────────────────────────────────────────┘ │
│           │ Match Found                                                   │
│           ▼                                                               │
│  ┌─────────────────┐                                                     │
│  │ Request Factory │ ─── Check correlation ─── Create or Update Request │
│  └────────┬────────┘                                                     │
│           │                                                               │
│           ▼                                                               │
│  ┌─────────────────┐              ┌─────────────────┐                   │
│  │ Application     │─────────────▶│ Hub Application │                   │
│  │ Router          │              └─────────────────┘                   │
│  └─────────────────┘                                                     │
│                                                                           │
└──────────────────────────────────────────────────────────────────────────┘
```

**Key Responsibility Boundary:** Signal Exchange routes to Hub Applications only — never directly to tasks or agents. This boundary is critical for separation of concerns.

→ **Details:** [Signal Exchange](./implementation-concepts/signal-exchange.md)

---

### Phase 4: Hub Application Processing

The Hub Application receives the Request and implements the Scenario logic:

```
1. Receive Request Update from Signal Exchange
2. Evaluate current state and business rules
3. Decide next steps:
   ├── Execute automation directly
   ├── Delegate task to human agent
   ├── Delegate task to AI agent
   ├── Call external tools/machines
   └── Wait for external input (reminders)
4. Send Request Update back to Signal Exchange
```

#### Application Types

| Type | Runtime | Use Case |
|------|---------|----------|
| **Container App** | Atlantis | Custom microservices, complex logic |
| **Workflow App** | Rhea | BPMN deterministic workflows |
| **AI Agent App** | Seer | LLM-based reasoning and decisions |
| **Batch App** | Perseus | File processing, ETL |
| **Durable Workflow** | ChronoShift | Long-running cases |

→ **Details:** [Hub Application](./implementation-concepts/hub-application.md) | [Automation Runtime](./implementation-concepts/automation-runtime.md)

---

### Phase 5: Task Assignment

When work requires human or AI agent involvement, the Hub Application creates Tasks:

```
Hub Application
      │
      │ Create Task
      ▼
┌─────────────────────────────────────────────────────────────────┐
│  TASK ASSIGNMENT                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌────────────────┐    ┌────────────────┐    ┌────────────────┐ │
│  │  Task Queue    │    │     Direct     │    │  Escalation    │ │
│  │                │    │   Assignment   │    │    Matrix      │ │
│  │  • Skill-based │    │                │    │                │ │
│  │  • Priority    │    │  • To User     │    │  • Time-based  │ │
│  │  • Round-robin │    │  • To Group    │    │  • Cumulative  │ │
│  └────────────────┘    └────────────────┘    └────────────────┘ │
│                                                                  │
│  Assignment Decision                                             │
│         │                                                        │
│         ▼                                                        │
│  ┌────────────────────────────────────────────────────────────┐ │
│  │  AGENT (Human or AI)                                        │ │
│  │                                                              │ │
│  │  Human: Receives task in Operations Center, MS Teams, etc.  │ │
│  │  AI: Receives task via delegation interface                  │ │
│  │                                                              │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

→ **Details:** [Task Allocation](./implementation-concepts/task-allocation.md) | [Escalation Matrix](./implementation-concepts/escalation-matrix.md)

---

### Phase 6: Agent Execution

Agents (human or AI) execute the assigned task:

| Agent Type | Execution Pattern |
|------------|-------------------|
| **Human Agent** | Uses consoles, tools, makes decisions, documents outcomes |
| **AI Agent** | Uses LLM reasoning, calls tools, makes decisions, reports outcomes |

Both agent types:
- Receive task context and instructions
- Access tools via Command Registry
- Update task status and outcomes
- Trigger follow-up actions

---

### Phase 7: Request Updates and Completion

As work progresses, updates flow back through the system:

```
Agent completes action
       │
       ▼
Task Update → Hub Application
       │
       ▼
Request Update → Signal Exchange
       │
       ├──▶ Append to Request history
       │
       ├──▶ Notify observers:
       │       • Notification Services → Customer notified
       │       • Task Management → Dashboard updated
       │       • MS Teams → Collaboration channel updated
       │
       └──▶ If terminal state → Request closed
```

#### Request States

| State | Description |
|-------|-------------|
| **CREATED** | Just created, not yet processed |
| **IN_PROGRESS** | Active work happening |
| **ON_HOLD** | Awaiting external input |
| **COMPLETED** | Successfully finished |
| **CANCELLED** | Terminated without completion |

→ **Details:** [Request Lifecycle](./implementation-concepts/request-lifecycle.md) | [Request Update](./implementation-concepts/request-update.md)

---

## Flow Variations

### Synchronous Flow (HTTP Request-Response)

For signals requiring immediate response:

```
HTTP Request → Heracles → SX → App → (quick processing) → App → SX → Heracles → HTTP Response
```

### Asynchronous Flow (Event-Driven)

For signals that trigger background processing:

```
Event → Atropos → SX → App → (processing with tasks) → Updates → Observers → Notifications
```

### Correlated Flow (Multi-Signal)

When multiple signals contribute to the same Request:

```
Signal 1: dispute.filed → SX → Create Request (req-001)
Signal 2: document.uploaded (correlation_id: req-001) → SX → Update Request (req-001)
Signal 3: customer.responded (correlation_id: req-001) → SX → Update Request (req-001)
```

### Reminder Flow (Time-Based)

When applications need delayed triggers:

```
App → SX: REMIND (schedule: T+48h)
...time passes...
SX → App: REMINDER_NOTIFICATION (at scheduled time)
```

→ **Details:** [Reminder Capability](./implementation-concepts/reminder-capability.md)

---

## Error Handling

### Retry Patterns

| Stage | Retry Mechanism |
|-------|-----------------|
| **Gateway → SX** | Gateway retries with exponential backoff |
| **SX → Application** | SX store-and-forward with retry |
| **Application → Tools** | Application-level retry logic |
| **Task Assignment** | Escalation after timeout |

### Dead Letter Handling

Signals that cannot be processed after retries:
1. Moved to dead letter queue
2. Logged with full context
3. Alerting triggered for operator review

---

## Observability

### Trace Context

Every signal carries trace context through the flow:

```
trace_id: Unique ID for end-to-end tracking
span_id: Individual operation within the trace
```

### Key Metrics

| Metric | Description |
|--------|-------------|
| **Signal throughput** | Signals processed per second |
| **Trigger match rate** | % of signals matching triggers |
| **Request latency** | Time from signal to completion |
| **Task assignment time** | Time from task creation to agent pickup |
| **SLA compliance** | % of requests completed within SLA |

→ **Details:** [APM](./implementation-concepts/apm.md)

---

## Related Documentation

| Document | Purpose |
|----------|---------|
| [Architecture Layers](./architecture-layers.md) | How flow maps to ontology layers |
| [Agent Model](./agent-model.md) | How agents participate in the flow |
| [I/O Gateway](./implementation-concepts/io-gateway.md) | Signal ingestion details |
| [Signal Exchange](./implementation-concepts/signal-exchange.md) | Central routing details |
| [Hub Application](./implementation-concepts/hub-application.md) | Automation execution details |
| [Request Lifecycle](./implementation-concepts/request-lifecycle.md) | Request state machine |

