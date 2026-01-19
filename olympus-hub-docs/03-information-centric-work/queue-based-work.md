# Queue-Based Work

Queue-based work is driven by work items that arrive in a stream and must be processed — typically with SLAs, throughput targets, and assignment logic. It's the backbone of operations centers, service desks, and processing functions.

---

## What Is Queue-Based Work?

In queue-based work, items arrive continuously, wait in queues, get assigned to agents, and are processed according to defined procedures. The focus is on **throughput**, **quality**, and **SLA compliance**.

### Characteristics

| Dimension | Description |
|-----------|-------------|
| **Determinism** | Mostly deterministic — known procedures for each item type |
| **Agents** | Often single agent per item; may escalate |
| **Duration** | Minutes to hours per item |
| **State** | Progression through defined states |
| **Goal** | Throughput, quality, SLA compliance |

### Examples

- Customer service tickets
- Claims processing
- Transaction reconciliation
- Loan application review
- Support request handling
- Order fulfillment processing
- Data entry and validation

---

## Anatomy of Queue-Based Work

### The Queue Flow

```
Items arrive (signals)
        ↓
Intake — items enter the queue
        ↓
Prioritization — ordered by urgency, SLA, type
        ↓
Assignment — routed to qualified agents
        ↓
Processing — agent works the item
        ↓
Completion — item resolved, next item pulled
```

### Queue Components

| Component | Purpose |
|-----------|---------|
| **Intake** | Where items enter the system |
| **Queue** | Where items wait for processing |
| **Prioritization Logic** | How items are ordered |
| **Assignment Logic** | How items are routed to agents |
| **Processing** | How agents handle items |
| **Completion** | How items exit the system |

### Assignment Patterns

| Pattern | Description | Best For |
|---------|-------------|----------|
| **Round-robin** | Distribute evenly across agents | Homogeneous items, balanced load |
| **Skill-based** | Match item type to agent capability | Specialized items, varied skills |
| **Load-based** | Consider agent current workload | Variable processing time |
| **Pull** | Agent selects next item | Agent autonomy, mixed complexity |
| **Push** | System assigns to agent | Strict SLAs, even distribution |

---

## Queue Metrics

Queue-based work is measured by operational metrics:

| Metric | Definition |
|--------|------------|
| **Queue Depth** | Number of items waiting |
| **Wait Time** | Time from arrival to assignment |
| **Handle Time** | Time from assignment to completion |
| **Throughput** | Items processed per time period |
| **SLA Compliance** | Percentage meeting time targets |
| **First Contact Resolution** | Resolved without escalation |

---

## Queue vs. Case

| Dimension | Queue-Based | Case-Based |
|-----------|-------------|------------|
| **Path** | Predefined procedure | Emerges during work |
| **Complexity** | Lower, routine | Higher, investigation |
| **Duration** | Minutes to hours | Hours to weeks |
| **Agents** | Usually one | Usually multiple |
| **Best for** | High volume, standard handling | Complex, judgment-heavy |

Many operations combine both: items start in a queue, but complex ones escalate to cases.

---

## Mapping to Hub Ontology

| Work Pattern Concept | Hub Ontology Concept |
|----------------------|----------------------|
| Work item arrival | Signal |
| Item type matching | Trigger → Scenario |
| Item instance | Request |
| Queue | Task Queue |
| Work item | Task |
| Assignment logic | Task Queue configuration |
| Processing | Procedure |
| Agent handling item | Agent assigned to Task |
| SLA | Goal with time constraint |

### How Hub Models Queue-Based Work

```
Signal (work item arrives)
    ↓
Trigger (matches item to Scenario)
    ↓
Scenario (defines processing procedure)
    ↓
Request (item instance created)
    ↓
Task created and queued
    ↓
Task Queue applies prioritization
    ↓
Assignment logic routes to Agent
    ↓
Agent processes Task (Procedure)
    ↓
Task completes
    ↓
Request completes (item resolved)
```

### Why Queue-Based Work Suits Hub

| Hub Concept | Why It Fits |
|-------------|-------------|
| **Task Queues** | Native support for queue management |
| **Scenarios** | Define procedure for each item type |
| **SLAs as Goals** | Built-in goal and constraint modeling |
| **Agent assignment** | Configurable assignment strategies |
| **Metrics** | Operational analytics for throughput, SLA |

---

## Multi-Tier Queues

Complex operations often use tiered queues:

```
Tier 1: General intake
    ↓ (escalate if needed)
Tier 2: Specialized handling
    ↓ (escalate if needed)
Tier 3: Expert resolution
```

Each tier may have:
- Different agents (skill levels)
- Different SLAs
- Different procedures

Hub models this through:
- Multiple Task Queues
- Escalation rules
- Role-based assignment

---

## Related

- [Ontology: Task Queue](../01-concepts/ontology-3-execution-layer.md#task-queue)
- [Ontology: Procedure](../01-concepts/ontology-3-execution-layer.md#procedure)
- [Case-Based Work](./case-based-work.md) — For complex items requiring investigation
- [Glossary: Scenario](../01-concepts/glossary.md#scenario)
