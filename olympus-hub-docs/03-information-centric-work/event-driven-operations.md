# Event-Driven Operations

Event-driven operations are triggered by events in the environment — system alerts, schedule triggers, threshold breaches, or external notifications — and require response within defined time constraints.

---

## What Are Event-Driven Operations?

In event-driven work, something happens in the environment that requires a response. The work is reactive: detect the event, evaluate it, and respond appropriately. Speed often matters.

### Characteristics

| Dimension | Description |
|-----------|-------------|
| **Trigger** | External event or condition |
| **Response** | Reactive, often time-sensitive |
| **Determinism** | Often starts deterministic, may branch |
| **Duration** | Varies — minutes to resolution |
| **Goal** | Handle the event appropriately |

### Examples

- Alert response (system, security, business)
- Scheduled batch processing
- Threshold-triggered actions (limits, quotas)
- Webhook handling from external systems
- Scheduled reports and notifications
- Deadline reminders
- SLA breach warnings

---

## Anatomy of Event-Driven Operations

### Event Flow

```
1. Detection
   Event occurs in environment
        ↓
2. Signal
   Event communicated to the system
        ↓
3. Evaluation
   Determine if and how to respond
        ↓
4. Response
   Execute appropriate action
        ↓
5. Resolution
   Event handled, outcome recorded
```

### Event Types

| Type | Source | Examples |
|------|--------|----------|
| **System Events** | Infrastructure, applications | Alerts, errors, state changes, health checks |
| **Time Events** | Clock, schedule | Cron jobs, deadlines, reminders |
| **Business Events** | Business systems | Transactions, approvals, exceptions |
| **External Events** | Third parties | Webhooks, notifications, feeds |
| **Threshold Events** | Monitoring | Limit breaches, quota warnings |

### Response Patterns

| Pattern | Description |
|---------|-------------|
| **Immediate** | Respond right away (alerts) |
| **Scheduled** | Respond at specific time (batch) |
| **Conditional** | Respond only if conditions met |
| **Aggregated** | Batch similar events together |
| **Cascading** | Event triggers chain of responses |

---

## Event Characteristics

### Urgency

| Level | Response Time | Examples |
|-------|---------------|----------|
| **Critical** | Minutes | Security breach, outage |
| **High** | Hours | SLA warning, compliance issue |
| **Normal** | Same day | Routine notifications |
| **Low** | Days | Reports, summaries |

### Complexity

| Level | Response Type | Examples |
|-------|---------------|----------|
| **Simple** | Automated procedure | Send notification |
| **Standard** | Human-assisted procedure | Acknowledge and investigate |
| **Complex** | Case-based investigation | Incident response |

---

## Event-Driven to Case-Based Transition

Many event-driven operations transition to case-based work when complexity warrants:

```
Event detected (simple trigger)
        ↓
Initial response (automated)
        ↓
Assessment: Is this complex?
        │
        ├── No → Complete (procedure)
        │
        └── Yes → Escalate to case
                    ↓
              Case-based investigation
```

This is common in incident response — the alert triggers immediate action, but complex incidents become cases.

---

## Scheduling and Timing

Event-driven operations often involve time:

| Concept | Description |
|---------|-------------|
| **Schedule** | When to run (cron, calendar) |
| **Deadline** | When something must be done |
| **Timeout** | How long to wait before escalating |
| **SLA** | Time commitment for response/resolution |
| **Window** | Time period when action is allowed |

---

## Mapping to Hub Ontology

| Work Pattern Concept | Hub Ontology Concept |
|----------------------|----------------------|
| Event | Signal |
| Event type matching | Trigger |
| Response definition | Scenario |
| Response instance | Request |
| Response execution | Procedure or Case |
| Time-based events | Scheduled Signals |
| SLA constraints | Goals with time bounds |

### How Hub Models Event-Driven Operations

```
Event occurs in environment
    ↓
Signal received by Hub
    ↓
Trigger evaluates conditions
    ↓
Matching Scenario identified
    ↓
Request created
    ↓
Procedure or Case initiated
    ↓
Response executed
    ↓
Request completes
```

### Why Event-Driven Work Suits Hub

| Hub Concept | Why It Fits |
|-------------|-------------|
| **Signal** | Events are signals from the environment |
| **Trigger** | Conditions evaluated to match events to scenarios |
| **Scenario** | Response procedures defined per event type |
| **Goals with SLAs** | Time constraints modeled as goals |
| **Escalation** | Complex events can become cases |

---

## Automation in Event-Driven Operations

Event-driven work is highly automatable:

| Level | Description | Examples |
|-------|-------------|----------|
| **Fully automated** | No human involvement | Retry failed job, send notification |
| **Human-verified** | Automated with human check | Alert with acknowledge requirement |
| **Human-executed** | Automation assists human | Investigation with suggested actions |
| **Human-only** | Human judgment required | Complex incident triage |

Hub supports all levels through configurable automation and human involvement.

---

## Related

- [Ontology: Signal](../01-concepts/ontology-1-perception-layer.md#signal)
- [Ontology: Trigger](../01-concepts/ontology-1-perception-layer.md#trigger)
- [Case-Based Work](./case-based-work.md) — Complex events become cases
- [Glossary: Scenario](../01-concepts/glossary.md#scenario)
