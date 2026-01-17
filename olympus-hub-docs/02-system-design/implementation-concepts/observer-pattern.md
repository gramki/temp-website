# Observer Pattern

> **Category:** Signal Architecture

---

## Overview

The **Observer Pattern** is Signal Exchange's integration mechanism for connecting subsystems without tight coupling. Subsystems (Notification Services, Task Management, MS Teams) register as observers and receive request events, allowing them to react to state changes without Signal Exchange knowing their implementation details.

---

## Ontology Context

### Relationship to Ontology

The ontology doesn't address subsystem integration patterns. Observer Pattern is an implementation concept for loose coupling between Hub modules.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| (not covered) | Observer Pattern | Integration mechanism |
| (not covered) | Observer Notifier | SX component for broadcasting |

### Gap This Fills

The ontology focuses on operations. Observer Pattern addresses:
1. **Module integration**: How do subsystems learn about events?
2. **Loose coupling**: How do we avoid dependencies?
3. **Extensibility**: How can we add new observers?
4. **Failure isolation**: How do observer failures affect core flow?

---

## Definition

**Observer Pattern** is an integration approach where:
- Signal Exchange broadcasts events to registered observers
- Observers subscribe to event types they care about
- Observer failures don't block core request processing
- New observers can be added without SX changes

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | System-wide integration pattern |
| **Lifecycle** | Observers register at startup; receive events during operation |
| **Ownership** | SX broadcasts; observers consume independently |
| **Multiplicity** | Multiple observers per event type |

---

## Rationale

### Why This Design?

Observer pattern enables:
1. **Loose coupling**: SX doesn't depend on observer implementations
2. **Extensibility**: Add observers without core changes
3. **Failure isolation**: Observer failure doesn't break request flow
4. **Selective subscription**: Observers get only relevant events

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Direct calls from SX** | Tight coupling; SX becomes complex |
| **Polling by observers** | Inefficient; delays |
| **Shared database triggers** | Coupling to storage; limited event richness |

### Related ADRs

| ADR | Decision |
|-----|----------|
| [ADR-0019](../../decision-logs/0019-signal-exchange-observer-pattern.md) | Observer pattern for SX module integration |

---

## Structure

### Hub Observers

| Observer | Purpose | Events of Interest |
|----------|---------|-------------------|
| **Channels** | User interaction, delegation handling | AUTHORITY_REQUEST, all updates for originated requests |
| **Notification Services** | User notifications | Request created, updated, completed; Task assigned |
| **Task Management** | Task lifecycle | Request created (for task creation); Request cancelled |
| **MS Teams Module** | Chat notifications | Mentions, assignments, updates |
| **Audit Service** | Compliance logging | All events |
| **Analytics Service** | Metrics collection | All events |

### Channels as Delegation Observers

Channels are a special category of observers that handle request-scoped delegation:

| Responsibility | Description |
|----------------|-------------|
| **AUTHORITY_REQUEST** | Receive requests for delegation; prompt user or implicit fulfill |
| **AUTHORITY_GRANTED** | Post when user grants consent or certificate exists |
| **AUTHORITY_DENIED** | Post when user denies or request times out |

Unlike other observers, Channels can **respond** to events by posting REQUEST_UPDATEs back to Signal Exchange.

→ See [Request-Scoped Delegation](./request-scoped-delegation.md) for the complete delegation flow.

### Observer Registration

```yaml
# Observer registration configuration
observer:
  id: notification-services
  
  # Event types to receive
  subscriptions:
    - REQUEST_CREATED
    - REQUEST_UPDATED
    - REQUEST_COMPLETED
    - TASK_ASSIGNED
    - TASK_COMPLETED
    
  # Delivery configuration
  delivery:
    interface: atropos          # http | atropos
    topic: hub.observers.notifications
    
  # Failure handling
  failure_policy:
    retry_count: 3
    retry_delay_ms: 1000
    dead_letter_topic: hub.observers.dlq
```

### Event Structure

```json
{
  "event_id": "evt-12345",
  "event_type": "REQUEST_UPDATED",
  "timestamp": "2026-01-06T10:30:00Z",
  
  "request_context": {
    "request_id": "req-abc-123",
    "tenant_id": "acme-bank",
    "subscription_id": "sub-prod-001",
    "workbench_id": "dispute-ops-prod",
    "scenario_id": "standard-dispute"
  },
  
  "event_data": {
    "update_sequence": 5,
    "update_type": "APPLICATION_UPDATE",
    "status": "IN_PROGRESS",
    "payload": {
      // Update-specific data
    }
  },
  
  "metadata": {
    "source": "signal-exchange",
    "trace_id": "trace-xyz"
  }
}
```

---

## Behavior

### How It Works

**Observer Registration:**
```
1. Observer service starts
2. Registers with SX Observer Notifier:
   ├── Observer ID
   ├── Event subscriptions
   └── Delivery configuration
3. SX stores registration
4. Observer receives acknowledgment
```

**Event Broadcasting:**
```
1. SX processes request update
2. Core flow completes (update stored)
3. Observer Notifier:
   ├── Matches event type to subscribed observers
   ├── Constructs event for each observer
   └── Delivers asynchronously
4. Observer receives and processes
5. Delivery failures handled per policy
```

**Failure Isolation:**
```
Observer failure handling:
├── Observer timeout → retry per policy
├── Retry exhausted → dead letter queue
├── Core flow NOT blocked
└── Alerts for operations team
```

### Observer Notifier Component

```
Signal Exchange
└── Observer Notifier
    ├── Observer Registry
    │   └── Registered observers and subscriptions
    ├── Event Matcher
    │   └── Match events to subscribers
    ├── Delivery Manager
    │   └── Async delivery to observers
    └── DLQ Handler
        └── Failed event handling
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Signal Exchange | ← part of | Observer Notifier is SX component |
| Notification Services | → notifies | Receives user notification events |
| Task Management | → notifies | Receives task-relevant events |
| MS Teams Module | → notifies | Receives collaboration events |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Async delivery** | Observers notified asynchronously |
| **At-least-once** | Events may be delivered more than once |
| **Order not guaranteed** | Cross-request event order not guaranteed |
| **Core flow independent** | Observer failures don't block SX |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Loose coupling** | SX doesn't know observer implementations |
| ✅ **Extensibility** | Add observers without SX changes |
| ✅ **Failure isolation** | Observer issues don't break core |
| ✅ **Selective subscription** | Observers get relevant events only |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Eventual consistency** | Observers may lag slightly |
| ⚠️ **Duplicate events** | Observers handle idempotently |
| ⚠️ **Debug complexity** | Comprehensive tracing |

---

## Examples

### Example 1: Notification Services Observer

```python
# Notification Services observer implementation
class NotificationObserver:
    async def handle_event(self, event):
        if event.event_type == "TASK_ASSIGNED":
            await self.notify_agent_of_assignment(event)
        elif event.event_type == "REQUEST_COMPLETED":
            await self.notify_customer_of_resolution(event)
    
    async def notify_agent_of_assignment(self, event):
        agent_id = event.event_data.assignee_id
        task = event.event_data.task
        
        # Render notification from template
        notification = await self.render_template(
            template="task_assigned",
            context={"task": task}
        )
        
        # Dispatch via CNS
        await self.cns_client.send(
            recipient=agent_id,
            notification=notification
        )
```

### Example 2: Task Management Observer

```python
# Task Management observer implementation
class TaskManagementObserver:
    async def handle_event(self, event):
        if event.event_type == "REQUEST_CANCELLED":
            await self.cancel_related_tasks(event)
    
    async def cancel_related_tasks(self, event):
        request_id = event.request_context.request_id
        
        # Find all tasks for this request
        tasks = await self.task_store.find_by_request(request_id)
        
        # Cancel non-terminal tasks
        for task in tasks:
            if task.status not in ["COMPLETED", "CANCELLED"]:
                await self.task_store.cancel(
                    task_id=task.id,
                    reason="Request cancelled"
                )
```

---

## Implementation Notes

### For Developers

- Handle events idempotently (may receive duplicates)
- Don't assume event order across requests
- Include timeout handling in event processors
- Log event processing for debugging

### For Operators

- Monitor observer lag (time between event and processing)
- Check DLQ for failed events
- Review observer health independently
- Configure appropriate retry policies

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Signal Exchange](./signal-exchange.md) | Contains Observer Notifier |
| [Notification Services](./notification-services.md) | Key observer |
| [Task Allocation](./task-allocation.md) | Task Management is observer |

---

## References

- [Observer Notifications Subsystem](../../04-subsystems/signal-exchange/observer-notifications.md)
- [ADR-0019: Observer Pattern](../../decision-logs/0019-signal-exchange-observer-pattern.md)

