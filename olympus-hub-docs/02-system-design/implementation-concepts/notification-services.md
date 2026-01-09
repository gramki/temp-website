# Notification Services

> **Category:** UX Architecture

---

## Overview

**Notification Services** is the subsystem responsible for translating Hub events into user notifications. Acting as an observer of Signal Exchange, it receives request updates, determines recipients and mechanisms based on Scenario specifications and user preferences, and dispatches notifications via Cipher Notification Service (CNS).

---

## Ontology Context

### Relationship to Ontology

The ontology describes agents receiving information but doesn't detail notification mechanics. Notification Services implements how users are informed of relevant events.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Agent awareness | Notification | Users notified of relevant events |
| (not covered) | Multi-mechanism delivery | Email, SMS, push, webhook |

### Gap This Fills

The ontology focuses on operations. Notification Services addresses:
1. **Event translation**: Which events become notifications?
2. **Recipient resolution**: Who gets notified?
3. **Mechanism selection**: Email vs SMS vs push?
4. **Template rendering**: How is content formatted?

---

## Definition

**Notification Services** is a subsystem that:
- Observes Signal Exchange for request events
- Matches events to Scenario notification specifications
- Resolves recipients from request and scenario context
- Intersects specification with user preferences
- Dispatches via CNS to configured mechanisms

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | System-wide; processes all request events |
| **Lifecycle** | Platform-managed; always running |
| **Ownership** | Platform owns; scenarios configure |
| **Multiplicity** | Single service with persona-specific handlers |

---

## Rationale

### Why This Design?

Centralized notification services enable:
1. **Consistent delivery**: All notifications through one path
2. **User preferences**: Single source for delivery preferences
3. **Template management**: Centralized template rendering
4. **Audit trail**: All notifications logged

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Per-application notifications** | Inconsistent; duplicated logic |
| **Direct to CNS** | No preference management; no templates |
| **Channel-specific services** | Fragmented; hard to maintain |

### Related ADRs

| ADR | Decision |
|-----|----------|
| [ADR-0021](../../decision-logs/0021-notification-services-as-sx-observer.md) | Notification Services as SX observer |
| [ADR-0022](../../decision-logs/0022-mustache-templates-for-notifications.md) | Mustache templates for notification content |

---

## Structure

### Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    NOTIFICATION SERVICES                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   SIGNAL EXCHANGE                    NOTIFICATION SERVICES                   │
│   ──────────────                     ─────────────────────                   │
│                                                                              │
│   ┌─────────────┐                   ┌───────────────────────────────────┐   │
│   │   Request   │                   │                                   │   │
│   │   Events    │──── observe ─────▶│   Event Processor                 │   │
│   │             │                   │   ├── Match to notification spec  │   │
│   └─────────────┘                   │   ├── Resolve recipients          │   │
│                                     │   └── Determine mechanisms        │   │
│                                     │                                   │   │
│                                     │   Template Renderer               │   │
│                                     │   └── Render per mechanism        │   │
│                                     │                                   │   │
│                                     │   Preference Manager              │   │
│                                     │   └── User delivery preferences   │   │
│                                     │                                   │   │
│                                     └──────────────┬────────────────────┘   │
│                                                    │                         │
│                                                    ▼                         │
│                                     ┌───────────────────────────────────┐   │
│                                     │   CIPHER NOTIFICATION SERVICE     │   │
│                                     │   (CNS)                           │   │
│                                     │                                   │   │
│                                     │   Email │ SMS │ Push │ Webhook   │   │
│                                     └───────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Notification Specification (in Scenario)

```yaml
scenario:
  id: standard-dispute
  
  notifications:
    - event: task_assigned
      recipients:
        - type: assignee        # Dynamic: task assignee
      mechanisms:
        - type: email
          template_ref: task-assigned-email
        - type: push
          template_ref: task-assigned-push
        - type: ms_teams
          template_ref: task-assigned-teams
          
    - event: request_completed
      recipients:
        - type: subject         # The customer
        - type: originator      # Who filed the request
      mechanisms:
        - type: email
          template_ref: dispute-resolved-email
        - type: sms
          template_ref: dispute-resolved-sms
```

### Template Structure

```yaml
# Mustache template
template:
  id: task-assigned-email
  type: email
  
  subject: "New task assigned: {{task.type}}"
  
  body: |
    Hi {{recipient.name}},
    
    You have been assigned a new task:
    
    Task: {{task.type}}
    Request: {{request.id}}
    Priority: {{task.priority}}
    Due: {{task.due_at}}
    
    {{#task.context}}
    Customer: {{customer.name}}
    Amount: {{amount}}
    {{/task.context}}
    
    [View Task]({{cta.url}})
```

---

## Behavior

### Notification Flow

```
1. Signal Exchange broadcasts event
   └── REQUEST_UPDATED, TASK_ASSIGNED, etc.

2. Notification Services receives as observer

3. Event Processor:
   ├── Match event to Scenario notification specs
   ├── Resolve recipients (assignee, subject, originator)
   └── Determine persona for each recipient

4. For each recipient:
   ├── Get user preferences from preference store
   ├── Intersect spec mechanisms with preferences
   └── For each resulting mechanism:
       ├── Render template with context
       └── Dispatch to CNS

5. CNS delivers via provider
   └── Email/SMS/Push/Webhook

6. Handle callbacks:
   ├── Delivery receipts → log
   ├── Read receipts → log (where supported)
   └── CTAs → create signal back to SX
```

### Recipient Resolution

| Recipient Type | Resolution |
|----------------|------------|
| **assignee** | Task assignee(s) at current level |
| **subject** | Request subject (customer) |
| **originator** | Who initiated the request |
| **all_actors** | Everyone who touched the request |
| **supervisor** | Workbench supervisor(s) |
| **explicit** | Named user list |

### Mechanism Intersection

```
Scenario spec: [email, sms, push]
User preference: [email, push]
───────────────────────────────
Result: [email, push]

User gets notifications via their preferred mechanisms
that the scenario also supports
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Signal Exchange | ← observes | Receives request events |
| CNS | → dispatches | Sends notifications |
| Preference Store | → reads | User delivery preferences |
| Template Store | → reads | Notification templates |
| Heracles Gateway | ← CTA signals | CTAs come back as signals |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Observer only** | Doesn't modify requests |
| **User consent** | Respects preference opt-outs |
| **Template required** | No notification without template |
| **Audit logged** | All notifications recorded |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Centralized** | One place for all notifications |
| ✅ **User control** | Preferences respected |
| ✅ **Template-driven** | Consistent, branded content |
| ✅ **Multi-mechanism** | Email, SMS, push, webhook |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Observer lag** | Minimal; async is acceptable |
| ⚠️ **Template management** | Versioned with scenarios |

---

## Examples

### Example 1: Task Assignment Notification

```
Event: TASK_ASSIGNED
Task: investigate dispute
Assignee: agent-bob

1. Match: task_assigned notification spec found
2. Recipient: agent-bob (assignee)
3. Preferences: agent-bob prefers [email, push]
4. Intersect with spec [email, push, teams]: [email, push]
5. Render email template with task context
6. Render push template with task context
7. Dispatch both to CNS
8. Bob receives email and push notification
```

### Example 2: CTA (Call-to-Action)

```
Notification includes CTA button: "View Task"
CTA URL: https://hub.acme.com/cta/{{correlation_id}}

User clicks CTA:
1. Request hits Heracles Gateway
2. CNS correlation ID extracted
3. Creates signal with CTA context
4. Signal processed by application
```

---

## Implementation Notes

### For Developers

- Define notification specs in Scenario
- Create templates for each mechanism
- Test template rendering with sample data

### For Operators

- Monitor notification delivery rates
- Check CNS provider status
- Review failed deliveries

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Observer Pattern](./observer-pattern.md) | Notification is an observer |
| [Signal Exchange](./signal-exchange.md) | Source of events |
| [Persona](./persona.md) | Notifications persona-aware |

---

## References

- [Notification Services Subsystem](../../04-subsystems/notification-services/README.md)
- [ADR-0021: Notification Services as Observer](../../decision-logs/0021-notification-services-as-sx-observer.md)
- [ADR-0022: Mustache Templates](../../decision-logs/0022-mustache-templates-for-notifications.md)

