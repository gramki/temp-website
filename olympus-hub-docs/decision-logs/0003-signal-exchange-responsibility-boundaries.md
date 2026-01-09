# ADR-0003: Signal Exchange Routes to Applications, Not Tasks or Agents

## Status

Accepted

## Date

2026-01-05

## Context

Signal Exchange (SX) dispatches Request Updates to registered observers. The question arose whether SX should:
- Route notifications directly to agents working on tasks
- Route notifications to specific tasks within a request
- Route only to observer modules (like Hub Applications)

There was potential confusion about SX's routing granularity.

## Decision

**Signal Exchange operates at the Request level only. It routes to Hub Applications and observer modules, never to tasks or agents directly.**

Specific boundaries:

1. **SX directs messages to Hub Applications** — never to tasks or agents
2. **SX notifications are about "Request Updates"** — not updates directed at a specific task
3. **SX cannot attribute incoming updates to a task or agent** — it operates at the Request level only
4. **Task assignment, task-specific notifications, and agent-level routing** are responsibilities of Hub Applications and Task Management, not Signal Exchange

## Consequences

### Positive
- **Clear responsibility boundary**: SX is the data plane for Request-level routing only
- **Simpler SX design**: No need to understand task or agent models
- **Flexibility for Applications**: Hub Applications determine how to handle Request updates
- **Scalability**: SX doesn't need to track per-task or per-agent state

### Negative
- **Hub Applications must parse updates**: Applications determine which tasks/agents are affected
- **No direct agent notification from SX**: Must go through Notification Services or Application

### Neutral
- Observer modules (like Notification Services, Task Management) handle the fan-out to appropriate recipients

## Related

- [Signal Exchange Overview](../04-subsystems/signal-exchange/README.md)
- [Observer Notifications](../04-subsystems/signal-exchange/observer-notifications.md)
- [Task Management](../04-subsystems/task-management/README.md)

