# Developer Primer: Building Applications on Hub

> **Audience:** Developers and Solution Architects building applications using Olympus Hub.

---

## Executive Summary

**Olympus Hub** provides a platform where you build **Hub Applications** — automation artifacts that execute business scenarios. Instead of building end-to-end systems, you focus on the business logic while Hub handles signal routing, task assignment, notifications, and audit. Your applications integrate with existing enterprise systems via well-defined interfaces.

**Key Value:** Less plumbing, more business logic. Hub provides the operational infrastructure; you provide the domain intelligence.

---

## What You Build

### Hub Applications

A **Hub Application** is an automation artifact that:
- Receives Requests from Signal Exchange
- Implements business logic for Scenarios
- Delegates Tasks to human and AI agents
- Calls Tools to interact with external systems
- Reports outcomes back to Signal Exchange

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    HUB APPLICATION ROLE                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   SIGNAL EXCHANGE                                                            │
│        │                                                                     │
│        │ Request                                                             │
│        ▼                                                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  YOUR HUB APPLICATION                                                │   │
│   │                                                                      │   │
│   │   ┌───────────┐    ┌───────────┐    ┌───────────┐                   │   │
│   │   │  Receive  │───▶│  Process  │───▶│  Delegate │                   │   │
│   │   │  Request  │    │  Logic    │    │   Tasks   │                   │   │
│   │   └───────────┘    └───────────┘    └─────┬─────┘                   │   │
│   │                          │                │                          │   │
│   │                          │                │                          │   │
│   │   ┌───────────┐    ┌─────▼─────┐    ┌─────▼─────┐                   │   │
│   │   │   Report  │◀───│  Call     │    │  Agents   │                   │   │
│   │   │  Outcome  │    │  Tools    │    │  Execute  │                   │   │
│   │   └───────────┘    └───────────┘    └───────────┘                   │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│        │                                                                     │
│        │ Request Update                                                      │
│        ▼                                                                     │
│   SIGNAL EXCHANGE (notifies observers, tracks state)                        │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Platform Infrastructure (What You Don't Build)

Hub provides:

| Capability | What Hub Handles |
|------------|------------------|
| **Signal Routing** | Receiving signals, matching triggers, routing to your app |
| **Request Management** | Lifecycle, state, correlation, storage |
| **Task Management** | Queues, assignment, escalation |
| **Notifications** | Multi-channel delivery |
| **Audit** | Decision records, evidence, explanations |
| **Identity** | Human SSO, AI agent identity |
| **Data Stores** | Relational, key-value, search (per workbench) |
| **Observability** | Logs, metrics, traces, APM |

---

## Development Model

### Application Types

Choose the right runtime for your use case:

| Type | Runtime | Best For | Technology |
|------|---------|----------|------------|
| **Container App** | Atlantis | Custom business logic | Any (Python, Node, Java) |
| **Workflow App** | Rhea | Deterministic multi-step | BPMN |
| **AI Agent App** | Seer | LLM-based reasoning | Strands Agents / custom |
| **Batch App** | Perseus | File processing, ETL | Any |
| **Durable Workflow** | ChronoShift | Long-running cases | Temporal |

### Application Specification

```yaml
apiVersion: hub.olympus.io/v1
kind: HubApplicationSpec
metadata:
  name: dispute-handler
  namespace: acme-bank
spec:
  display_name: "Dispute Handler"
  version: "1.2.3"
  
  # Runtime selection
  runtime: chronoshift  # For long-running cases
  
  # Container reference
  container:
    image: "registry.../dispute-handler"
    tag: "1.2.3"
    
  # Scenarios this application handles
  scenarios:
    - standard-dispute
    - fraud-dispute
    
  # How to receive requests
  delivery:
    interface: http
    endpoint: "/handle"
    
  # Resource requirements
  resources:
    cpu: "500m"
    memory: "512Mi"
```

---

## The Signal-to-Outcome Flow

### What Happens When a Signal Arrives

```
1. SIGNAL arrives (e.g., HTTP POST to /disputes)
   │
   ▼
2. I/O GATEWAY (Heracles) normalizes to standard DTO
   │
   ▼
3. SIGNAL EXCHANGE evaluates triggers
   │
   ▼
4. TRIGGER MATCHES → Creates REQUEST
   │
   ▼
5. YOUR APPLICATION receives Request
   │
   ├── Process business logic
   ├── Call Tools (external systems)
   ├── Create Tasks (for agents)
   └── Send Request Updates
   │
   ▼
6. SIGNAL EXCHANGE updates state, notifies observers
   │
   ▼
7. TASKS assigned to agents (human or AI)
   │
   ▼
8. AGENTS complete work, report outcomes
   │
   ▼
9. YOUR APPLICATION receives task completion
   │
   ▼
10. REQUEST completes (or continues)
```

### Your Application's Interface

**Receiving Requests:**

```json
// Incoming Request Update
{
  "request_id": "req-12345",
  "request_type": "standard-dispute",
  "update": {
    "type": "CREATED",
    "sequence": 1,
    "timestamp": "2026-01-06T10:00:00Z"
  },
  "payload": {
    "customer_id": "CUST-001",
    "transaction_id": "TXN-99999",
    "amount": 500.00,
    "reason": "unauthorized_charge"
  }
}
```

**Sending Updates:**

```json
// Outgoing Request Update
{
  "request_id": "req-12345",
  "update": {
    "type": "APPLICATION_UPDATE",
    "sequence": 2
  },
  "payload": {
    "action": "task_created",
    "task_id": "task-001",
    "task_type": "investigate",
    "assigned_to": "tier-1-disputes"
  }
}
```

---

## Working with Tasks

### Creating Tasks

```python
# Python example
def handle_dispute_request(request):
    # Create investigation task for human agent
    task = create_task(
        request_id=request.id,
        task_type="investigate",
        title="Investigate Dispute",
        description=f"Review transaction {request.payload.transaction_id}",
        assignment={
            "strategy": "queue",
            "queue": "tier-1-disputes"
        },
        context={
            "customer_id": request.payload.customer_id,
            "transaction_id": request.payload.transaction_id,
            "amount": request.payload.amount
        }
    )
    
    # Send update to Signal Exchange
    send_update(request.id, {
        "action": "task_created",
        "task_id": task.id
    })
```

### Receiving Task Completions

```python
def handle_task_completed(request_id, task_id, outcome):
    # Task completed by agent
    if outcome.decision == "refund_approved":
        # Call tool to initiate refund
        result = call_tool("core-banking", "initiate_refund", {
            "transaction_id": task.context.transaction_id,
            "amount": task.context.amount
        })
        
        # Complete the request
        complete_request(request_id, {
            "resolution": "refund_issued",
            "refund_id": result.refund_id
        })
```

---

## Working with Tools

### Calling External Systems

Tools are registered commands on Machines (external systems):

```python
# Call a tool
result = call_tool(
    machine="core-banking",
    command="get_transaction",
    params={
        "transaction_id": "TXN-99999"
    }
)

# Result includes the transaction details
transaction = result.data
```

### Tool Registry

Tools are defined in the registry:

```yaml
apiVersion: hub.olympus.io/v1
kind: ToolInstance
metadata:
  name: transaction-lookup
spec:
  machine_ref: core-banking-prod
  command: get_transaction
  
  input_schema:
    type: object
    properties:
      transaction_id:
        type: string
        
  output_schema:
    type: object
    properties:
      transaction:
        type: object
```

---

## Data Access

### Workbench-Scoped Data Stores

Each workbench has isolated data stores:

| Store | Type | Use For |
|-------|------|---------|
| **Ganymede** | PostgreSQL | Structured data, transactions |
| **Callisto** | Redis | Session state, caches |
| **Europa** | Elasticsearch | Search, analytics |

```python
# Ganymede (SQL)
from hub.data import ganymede

db = ganymede.connect()
disputes = db.query("SELECT * FROM disputes WHERE status = 'open'")

# Callisto (KV)
from hub.data import callisto

cache = callisto.connect()
cache.set(f"session:{request_id}", session_data, ttl=3600)

# Europa (Search)
from hub.data import europa

search = europa.connect()
results = search.query({"match": {"customer_name": "John Smith"}})
```

---

## Development Workflow

### GitOps Model

```
1. Write code → Push to your repo
2. CI builds container → Pushes to Hub Registry
3. Define CRD specs → Commit to Subscription Git repo
4. Operators reconcile → Application deployed
5. Test in DEV workbench
6. Promote to STAGING → Then to PROD
```

### Promotion Path

```
DEV Workbench (sub-dev)
    │
    │ Test and validate
    ▼
STAGING Workbench (sub-dev)
    │
    │ Cross-subscription promotion (with approval)
    ▼
PROD Workbench (sub-prod)
```

---

## Testing

### Hub Test Runner

```yaml
# Test CRD
apiVersion: hub.olympus.io/v1
kind: ScenarioTest
metadata:
  name: dispute-happy-path
spec:
  scenario_ref: standard-dispute
  
  test_cases:
    - name: "Standard dispute resolved"
      given:
        signal:
          type: dispute.filed
          payload:
            amount: 100
      when:
        - task: investigate
          outcome:
            decision: refund_approved
      then:
        - request_status: COMPLETED
        - request_outcome: refund_issued
```

---

## Key Concepts to Understand

| Concept | What It Means for You |
|---------|----------------------|
| **Scenario** | The operational situation your app handles |
| **Request** | A single occurrence of that Scenario |
| **Task** | Work you delegate to agents |
| **Tool** | External capability you invoke |
| **Signal Exchange** | The router that sends you work |
| **Workbench** | Your deployment context |

---

## Best Practices

1. **Stateless applications** — Keep state in Hub data stores, not in memory
2. **Idempotent handlers** — Same request update should produce same result
3. **Use reminders** — Don't build your own schedulers
4. **Delegate, don't do** — Let agents (human/AI) do the work
5. **Log decisions** — Audit fabric needs your decision context
6. **Version everything** — Containers, CRDs, migrations

---

## Next Steps

1. **Understand the flow** → [Signal Flow](../02-system-design/signal-flow.md)
2. **Learn about applications** → [Hub Application](../02-system-design/implementation-concepts/hub-application.md)
3. **See runtimes** → [Automation Runtime](../02-system-design/implementation-concepts/automation-runtime.md)
4. **Try building** → [Hub Development Flow](../10-guides/hub-development-flow/README.md)

