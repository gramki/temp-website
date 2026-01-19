# Developer Primer: Build What Matters

> **Audience:** Developers and Solution Architects building applications on Hub

---

## The Frustration You Know

You've been here before:

- **You build the same plumbing over and over** — auth, routing, notifications, audit trails
- **Infrastructure takes more time than business logic** — the interesting work is a fraction of the effort
- **AI integration is ad-hoc** — different for every project, every team, every tool
- **"Human-AI handoff" means emails and hope** — no structured collaboration
- **Your code runs, but you can't see its impact** — it disappears into the operational void
- **Testing operational scenarios requires standing up the world** — integration testing is painful

---

## The Shift: Platform Handles Infrastructure, You Handle Intelligence

Hub inverts the effort distribution. The platform provides the operational infrastructure. You focus on what makes your application valuable.

### What You Stop Building

- Signal routing and normalization
- Task queues and assignment logic
- Notification systems
- Audit infrastructure
- Identity and access control per application
- Data stores per application
- Monitoring and observability plumbing

### What You Focus On

- **Business logic for your Scenario** — the decisions that matter
- **Integration with external systems** — via Tools that Hub manages
- **AI agent behavior** — via Seer, with governance built in
- **Domain-specific intelligence** — what your application uniquely provides

---

## What This Means for You

### Your Code Has Context

When your Hub Application receives a Request, it knows:

- What **Scenario** this is — the goal-oriented definition of what needs to be achieved
- The **history** — what's happened so far on this Request
- The **entities** involved — customer, transaction, case, whatever matters
- The **agents** who are collaborating — human, AI, rules

You're not building in isolation. You're part of a governed collaboration.

### Your Work Connects to Something Larger

Hub has a clear division of labor:

| Role | Responsibility |
|------|----------------|
| **Process Architect** | Designs the Scenario — what ought to be done |
| **You (Developer)** | Implements the automation — how it's codified |
| **Supervisor** | Configures the deployment — how it's operationalized |

Your Hub Application implements the Process Architect's design. It runs in the Supervisor's deployment context. You're not alone — and you're not responsible for everything.

### AI Is a First-Class Concern

In Hub, AI agents are participants in the same operational model as human agents:

- AI agents receive Tasks, just like humans
- AI agents have **Employment Specs** that define their autonomy
- AI agents are governed by the same policies
- AI agent decisions are audited the same way

You build for human-AI collaboration, not around it.

### You Can See the Impact

Hub provides visibility into how your application participates in operations:

- Requests flow through your application
- Tasks get assigned, completed, escalated
- Outcomes are recorded with your application's contribution
- Audit trails show exactly what happened and why

---

## What You Can Now Do

| Before | Now |
|--------|-----|
| Build routing, auth, audit yourself | Platform provides infrastructure |
| Integrate AI ad-hoc | AI agents are first-class participants |
| Hope your code connects to process | Your code implements defined Scenarios |
| Test in isolation | Test against operational flows |
| Deploy and pray | GitOps promotion with observability |
| Wonder what happened | Trace the entire Request lifecycle |

---

## How Hub Works (The Mechanics)

### Hub Applications

A **Hub Application** is an automation artifact that:

1. **Receives Requests** from Signal Exchange
2. **Implements business logic** for one or more Scenarios
3. **Delegates Tasks** to human and AI agents
4. **Calls Tools** to interact with external systems
5. **Reports outcomes** back to Signal Exchange

```yaml
apiVersion: hub.olympus.io/v1
kind: HubApplicationSpec
metadata:
  name: dispute-handler
spec:
  display_name: "Dispute Handler"
  version: "1.2.3"
  runtime: chronoshift
  scenarios:
    - standard-dispute
    - fraud-dispute
  container:
    image: "registry.../dispute-handler:1.2.3"
```

### Runtime Options

Choose the right runtime for your use case:

| Runtime | Best For | Technology |
|---------|----------|------------|
| **Atlantis** | Custom business logic | Containers (Python, Node, Java, etc.) |
| **Rhea** | Deterministic multi-step processes | BPMN workflows |
| **Seer** | LLM-based reasoning | AI Agents (Strands, custom) |
| **ChronoShift** | Long-running cases | Temporal durable workflows |
| **Perseus** | File processing, ETL | Batch processing |

### The Signal-to-Outcome Flow

```
Signal arrives (HTTP, event, schedule)
    │
    ▼
I/O Gateway normalizes to standard DTO
    │
    ▼
Signal Exchange evaluates Triggers
    │
    ▼
Trigger matches → Request created
    │
    ▼
YOUR APPLICATION receives Request
    │
    ├── Process business logic
    ├── Call Tools (external systems)
    ├── Create Tasks (for agents)
    └── Send Request Updates
    │
    ▼
Tasks assigned to Agents (human or AI)
    │
    ▼
Agents complete Tasks, report outcomes
    │
    ▼
Request completes (or continues)
```

### Development Workflow

Hub uses a GitOps model:

1. **Write code** — Push to your repo
2. **CI builds** — Container pushed to Hub Registry
3. **Define specs** — CRDs in Subscription Git repo
4. **Operators reconcile** — Application deployed to Workbench
5. **Test in DEV** — Validate against scenarios
6. **Promote** — DEV → STAGING → PROD with approval gates

---

## Working with Tasks

### Creating Tasks

```python
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
    return task
```

### Receiving Task Completions

```python
def handle_task_completed(request_id, task_id, outcome):
    if outcome.decision == "refund_approved":
        # Call tool to initiate refund
        result = call_tool("core-banking", "initiate_refund", {
            "transaction_id": task.context.transaction_id,
            "amount": task.context.amount
        })
        complete_request(request_id, {
            "resolution": "refund_issued",
            "refund_id": result.refund_id
        })
```

---

## Working with Tools

Tools are registered capabilities on Machines (external systems):

```python
# Call a tool
result = call_tool(
    machine="core-banking",
    command="get_transaction",
    params={"transaction_id": "TXN-99999"}
)

transaction = result.data
```

Hub manages tool registration, permissions, and audit.

---

## Data Access

Each Workbench has isolated data stores:

| Store | Type | Use For |
|-------|------|---------|
| **Ganymede** | PostgreSQL | Structured data, transactions |
| **Callisto** | Redis | Session state, caches |
| **Europa** | Elasticsearch | Search, analytics |

```python
from hub.data import ganymede, callisto, europa

# SQL
db = ganymede.connect()
disputes = db.query("SELECT * FROM disputes WHERE status = 'open'")

# Key-Value
cache = callisto.connect()
cache.set(f"session:{request_id}", session_data, ttl=3600)

# Search
search = europa.connect()
results = search.query({"match": {"customer_name": "John Smith"}})
```

---

## Getting Started

1. **Pick a Scenario** — Understand what you're implementing
2. **Read the Normative Spec** — What the Process Architect designed
3. **Choose your runtime** — Container, workflow, AI agent, or durable workflow
4. **Build the Hub Application** — Focus on business logic
5. **Test against the Scenario** — Use Hub's test framework
6. **Promote through environments** — DEV → STAGING → PROD

---

## Deeper Understanding

- [Vision and Mission](../00-_why/vision.md) — The larger purpose
- [Foundational Beliefs](../00-_why/foundational-beliefs.md) — The thinking behind Hub
- [Hub Architecture](../02-system-design/hub-architecture.md) — How it all fits together
- [Hub Development Flow](../10-guides/hub-development-flow/README.md) — Development model
- [DevOps Workbench](../09-composite-systems-and-patterns/devops-workbench/README.md) — Development automation

---

## Next Steps

- [Hub Application](../02-system-design/implementation-concepts/hub-application.md) — Application specification
- [Signal Flow](../02-system-design/signal-flow.md) — How signals route
- [Automation Runtimes](../04-subsystems/automation-runtimes/README.md) — Runtime options
- [Glossary](../01-concepts/glossary.md) — Key terminology
