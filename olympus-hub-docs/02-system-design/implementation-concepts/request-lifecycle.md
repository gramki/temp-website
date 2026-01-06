# Request Lifecycle

> **Category:** Request and Task

---

## Overview

A **Request** is the runtime instance of work triggered by a Signal matching a Scenario. It represents the operational session boundary for a single occurrence of a Scenario — accumulating all updates, decisions, memos, tasks, and outcomes from initiation to completion. The Request Lifecycle defines the states, transitions, and behaviors that govern how Requests evolve over time.

---

## Ontology Context

### Relationship to Ontology

The ontology defines **Operation** (Procedure, Workflow, Case) as the runtime instance of work, but doesn't specify:
- How operations are instantiated and tracked
- How updates accumulate over time
- How multiple signals correlate to the same operation
- How operations terminate

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Operation | Request | Request is the runtime container for an Operation |
| Scenario | Request Type | Request type is determined by Scenario |
| Signal | Request Creation/Update | Signals create or update Requests |

### Gap This Fills

The ontology describes operations abstractly. Request Lifecycle specifies:
1. **State machine**: What states can a Request be in?
2. **Update model**: How do updates accumulate?
3. **Correlation**: How do subsequent signals attach to existing Requests?
4. **Termination**: How and when does a Request end?

---

## Definition

**Request** is a stateful container representing a single occurrence of a Scenario, with:
- A unique identifier and type
- A status indicating its current state
- An ordered sequence of updates (append-only)
- Associated tasks delegated to agents
- Metadata including subject, originator, and actors

**Request Lifecycle** is the state machine governing Request status transitions.

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Workbench-scoped; belongs to exactly one Scenario |
| **Lifecycle** | Created by Signal Exchange; updated by Applications; terminated by completion/cancellation |
| **Ownership** | Hub Application orchestrates; Signal Exchange manages state |
| **Multiplicity** | Many Requests can exist for a single Scenario simultaneously |

---

## Rationale

### Why This Design?

Request as a first-class entity enables:
1. **Audit trail**: Complete history of everything that happened
2. **Correlation**: Multiple signals can contribute to the same Request
3. **Visibility**: Supervisors and Agents can see Request status
4. **Recovery**: Requests can be resumed after failures

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Stateless processing** | No history; no correlation; no recovery |
| **Event sourcing only** | Query complexity; no clear status |
| **Process instance (BPMN)** | Too coupled to workflow paradigm |

### Related ADRs

| ADR | Decision |
|-----|----------|
| [ADR-0003](../../decision-logs/0003-signal-exchange-responsibility-boundaries.md) | SX routes to Applications, not tasks |
| [ADR-0020](../../decision-logs/0020-request-level-granularity.md) | SX operates at Request level only |

---

## Structure

### Request Entity

```yaml
request:
  id: "req-12345"
  type: "standard-dispute"              # From Scenario
  
  # Current status
  status: "IN_PROGRESS"                 # CREATED | IN_PROGRESS | ON_HOLD | COMPLETED | CANCELLED
  status_reason: "Awaiting customer documents"
  
  # Actors
  subject_id: "CUST-001"                # Business entity this Request is about
  originator_id: "user-alice"           # Who/what initiated the Request
  actors: ["agent-bob", "agent-carol"]  # All who have touched this Request
  
  # Timing
  created_at: "2026-01-06T10:00:00Z"
  updated_at: "2026-01-06T14:30:00Z"
  sla_due_at: "2026-01-08T10:00:00Z"
  completed_at: null
  
  # Correlation
  correlation_id: "txn-99999"           # External correlation
  parent_request_id: null               # If spawned from another Request
  
  # Updates (append-only)
  updates:
    - sequence: 1
      type: "CREATED"
      timestamp: "2026-01-06T10:00:00Z"
      payload: { ... initial signal data ... }
    - sequence: 2
      type: "APPLICATION_UPDATE"
      timestamp: "2026-01-06T10:05:00Z"
      payload: { ... }
  
  # Associated tasks
  tasks:
    - task_id: "task-001"
      status: "IN_PROGRESS"
    - task_id: "task-002"
      status: "PENDING"
```

### Request States

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    REQUEST STATE MACHINE                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│                              ┌──────────┐                                   │
│              Signal Match    │          │                                   │
│         ────────────────────▶│ CREATED  │                                   │
│                              │          │                                   │
│                              └────┬─────┘                                   │
│                                   │                                          │
│                                   │ App starts processing                    │
│                                   ▼                                          │
│                              ┌──────────┐                                   │
│                      ┌──────▶│   IN     │◀──────┐                           │
│                      │       │ PROGRESS │       │                           │
│                      │       └────┬─────┘       │                           │
│                      │            │             │                           │
│              Resume  │            │ Hold        │ Resume                    │
│                      │            ▼             │                           │
│                      │       ┌──────────┐       │                           │
│                      └───────│ ON_HOLD  │───────┘                           │
│                              └──────────┘                                   │
│                                   │                                          │
│          ┌────────────────────────┼────────────────────────┐                │
│          │                        │                        │                │
│          ▼                        ▼                        ▼                │
│     ┌──────────┐            ┌──────────┐            ┌──────────┐           │
│     │COMPLETED │            │CANCELLED │            │ EXPIRED  │           │
│     │          │            │          │            │          │           │
│     └──────────┘            └──────────┘            └──────────┘           │
│     (terminal)              (terminal)              (terminal)             │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### State Definitions

| State | Description | Allowed Transitions |
|-------|-------------|---------------------|
| **CREATED** | Request just created; not yet processed | → IN_PROGRESS, CANCELLED |
| **IN_PROGRESS** | Active work happening | → ON_HOLD, COMPLETED, CANCELLED |
| **ON_HOLD** | Paused awaiting external input | → IN_PROGRESS, CANCELLED |
| **COMPLETED** | Successfully finished | (terminal) |
| **CANCELLED** | Terminated without completion | (terminal) |
| **EXPIRED** | SLA exceeded without completion | (terminal) |

---

## Behavior

### How It Works

**Request Creation:**
```
1. Signal arrives at Signal Exchange
2. Trigger Evaluator finds matching trigger
3. Request Factory checks for correlation:
   ├── Correlation found → Update existing Request
   └── No correlation → Create new Request
4. New Request initialized with:
   ├── Unique ID
   ├── Type from Scenario
   ├── Status = CREATED
   └── First update with signal payload
5. Application Router delivers to Hub Application
```

**Request Updates:**
```
1. Hub Application receives Request
2. Application processes and sends update to SX:
   ├── Status change (optional)
   ├── Payload (memos, decisions, outcomes)
   └── Response status (for sync signals)
3. SX appends update with sequence number
4. Observer Notifier broadcasts to observers
5. If terminal status: Request is closed
```

**Request Correlation:**
```
Correlation matches by:
├── Explicit correlation_id in signal
├── Subject + Scenario + time window
└── Custom correlation rules per Scenario
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Signal Exchange | ↔ manages | SX creates and updates Requests |
| Hub Application | ↔ orchestrates | App drives Request through states |
| Task Management | → contains | Request contains associated Tasks |
| Notification Services | → observes | Notifies stakeholders of updates |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Append-only updates** | Updates cannot be modified or deleted |
| **Sequence ordering** | Updates are strictly ordered by sequence number |
| **Terminal finality** | Terminal states cannot transition to other states |
| **Single Scenario** | A Request belongs to exactly one Scenario |
| **Unique ID** | Request ID is globally unique |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Complete audit trail** | Every action is recorded |
| ✅ **Correlation** | Multiple signals contribute to same Request |
| ✅ **Visibility** | Clear status for all stakeholders |
| ✅ **Recovery** | Resume from any state after failure |
| ✅ **SLA tracking** | Due dates and expiration built-in |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Storage growth** | Archival policies; data lifecycle management |
| ⚠️ **Query complexity** | Indexed views; search integration (Europa) |

---

## Examples

### Example 1: Dispute Request Lifecycle

```
T+0:    Signal: dispute.filed
        → Request CREATED (req-001)

T+5m:   App starts processing
        → Request IN_PROGRESS

T+10m:  App creates investigation task
        → Task created (task-001)

T+1h:   Agent completes investigation
        → Task completed, Request updated

T+2h:   App awaits customer documents
        → Request ON_HOLD

T+26h:  Customer uploads documents
        → Signal: document.uploaded (correlates to req-001)
        → Request IN_PROGRESS

T+28h:  App makes decision
        → Request COMPLETED
```

### Example 2: Request Entity After Completion

```json
{
  "id": "req-dispute-001",
  "type": "standard-dispute",
  "status": "COMPLETED",
  "status_reason": "Resolved in customer favor",
  "subject_id": "CUST-001",
  "originator_id": "CUST-001",
  "actors": ["agent-bob", "supervisor-alice"],
  "created_at": "2026-01-06T10:00:00Z",
  "completed_at": "2026-01-06T14:00:00Z",
  "updates": [
    { "sequence": 1, "type": "CREATED", "timestamp": "..." },
    { "sequence": 2, "type": "APPLICATION_UPDATE", "payload": { "action": "task_created" } },
    { "sequence": 3, "type": "TASK_COMPLETED", "payload": { "task_id": "task-001" } },
    { "sequence": 4, "type": "DECISION", "payload": { "outcome": "refund_approved" } },
    { "sequence": 5, "type": "COMPLETED", "payload": { "resolution": "customer_favor" } }
  ]
}
```

---

## Implementation Notes

### For Developers

- Always check current Request status before making updates
- Use correlation_id for signals that should attach to existing Requests
- Terminal states are final — ensure you're ready before completing
- Include meaningful status_reason for visibility

### For Operators

- Monitor Request age to catch stuck Requests
- Review SLA breach rates by Scenario
- Archive completed Requests per retention policy

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Signal Exchange](./signal-exchange.md) | Creates and manages Requests |
| [Hub Application](./hub-application.md) | Orchestrates Request state |
| [Request Update](./request-update.md) | Individual update within Request |
| [Task Allocation](./task-allocation.md) | Tasks are created within Requests |

---

## References

- [Request Management Subsystem](../../04-subsystems/request-management/README.md)
- [Request Lifecycle (Subsystem)](../../04-subsystems/request-management/request-lifecycle.md)
- [ADR-0020: Request-Level Granularity](../../decision-logs/0020-request-level-granularity.md)

