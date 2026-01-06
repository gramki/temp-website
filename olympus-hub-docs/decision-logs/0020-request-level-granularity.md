# ADR-0020: Request-Level Granularity for Signal Exchange Operations

## Status

**Accepted**

## Date

2026-01-06

## Context

Hub manages complex hierarchies of entities:
- **Request**: A long-running session representing a Scenario instance
- **Task**: A unit of work within a Request, assigned to agents
- **Agent**: Human or AI entity completing tasks

Signal Exchange (SX) receives updates from Hub Applications and dispatches notifications. The question is at what granularity SX should operate:
- Request level only
- Task level (attribute updates to specific tasks)
- Agent level (route updates to specific agents)

This decision has significant architectural implications for:
- SX complexity and responsibilities
- Integration patterns with observer modules
- Coupling between SX and Task Management

## Decision

**Signal Exchange operates exclusively at the Request level.**

SX:
- **CAN** receive and dispatch Request Updates
- **CAN** track request history and state
- **CAN** dispatch updates to registered observer modules

SX **CANNOT**:
- Attribute an update to a specific task
- Attribute an update to a specific agent
- Determine which agent should receive a notification
- Route updates directly to tasks or agents

### Responsibility Boundaries

| Concern | Responsible Component |
|---------|----------------------|
| Request Updates | Signal Exchange |
| Task Attribution | Task Management (from TASK_LIFECYCLE payload) |
| Agent Routing | Observer Modules (Notification Services, MS Teams Module) |
| User Delivery | Cipher Notification Service (via observer modules) |

### Update Flow

```
Hub Application
       │
       ├── Request Update (with task_id in payload)
       │
       ▼
Signal Exchange
       │
       ├── Stores update in Request history
       ├── Dispatches to observer modules (Request-level)
       │
       ▼
Observer Modules (e.g., Notification Services)
       │
       ├── Parses TASK_LIFECYCLE payload
       ├── Extracts task_id, agent_id
       ├── Resolves recipients
       │
       ▼
Delivery to Agents/Users
```

## Alternatives Considered

### Alternative 1: Task-Aware Signal Exchange
SX maintains task registry and routes updates to specific tasks.

- **Pros**: Simpler observer modules, direct task updates
- **Cons**: SX duplicates Task Management functionality, tight coupling, increased complexity

### Alternative 2: Agent-Aware Signal Exchange
SX maintains agent registry and delivers notifications directly to agents.

- **Pros**: Reduced hops, faster agent notification
- **Cons**: SX becomes notification system, violates single responsibility, must understand all channels

### Alternative 3: Hybrid Approach
SX handles Request-level by default but can route to tasks for specific update types.

- **Pros**: Flexibility
- **Cons**: Complexity, unclear boundaries, maintenance burden

## Consequences

### Positive
- **Clear Boundaries**: SX has single responsibility (Request lifecycle)
- **Loose Coupling**: SX doesn't depend on Task Management internals
- **Simpler SX**: No task or agent registry in SX
- **Scalability**: Task Management and Notification Services scale independently

### Negative
- **Additional Parsing**: Observer modules must parse update payloads to extract task/agent info
- **Indirection**: Updates travel through observer modules before reaching agents
- **Payload Convention**: Hub Applications must include task_id/agent_id in payloads for routing

### Neutral
- Task information is conveyed in the update payload (e.g., TASK_LIFECYCLE events include task_id)
- Observer modules are responsible for recipient resolution

## Example: TASK_LIFECYCLE Update

Hub Application sends:
```json
{
  "update": {
    "update_type": "TASK_LIFECYCLE",
    "sequence": 5
  },
  "payload": {
    "task": {
      "task_id": "task-abc123",      // Task info in payload
      "event": "ASSIGNED",
      "agent_id": "agent-xyz789",    // Agent info in payload
      "queue_id": "dispute-intake"
    }
  }
}
```

Signal Exchange:
1. Receives update (doesn't interpret task_id or agent_id)
2. Stores in Request history
3. Dispatches to observer modules (Notification Services, Task Management)

Notification Services:
1. Receives Request Update
2. Parses `payload.task.agent_id`
3. Resolves agent to user
4. Delivers notification via CNS

## Related Decisions

- [ADR-0003: Signal Exchange Responsibility Boundaries](./0003-signal-exchange-responsibility-boundaries.md)
- [ADR-0019: Signal Exchange Observer Pattern](./0019-signal-exchange-observer-pattern.md)
- [ADR-0006: Task Queue Escalation Model](./0006-task-queue-escalation-model.md)

