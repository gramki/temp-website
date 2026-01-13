# 0123. Persona Twin Trigger Mechanisms

## Status

Accepted

## Date

2026-01-14

## Context

Persona Twins need to respond to events relevant to their delegator: tasks assigned to them, notifications meant for them, and personally configured schedules. These triggers must integrate with existing Signal Exchange infrastructure.

### Constraints

- Must use existing Signal Exchange trigger infrastructure
- Must support OPA-based filtering (consistent with other Hub patterns)
- Must integrate with Task Management System and Platform Notifications
- Must support time-based triggers via Kale scheduler

### Requirements

- Task assignment triggers when tasks assigned to delegator
- Platform notification triggers for workbench-scoped notifications
- Time schedule triggers via Kale
- OPA filters for fine-grained signal filtering
- Transform signals to Request payloads for Persona Twin Scenarios

## Decision

We will implement **three specialized trigger types** for Persona Twins that create new Requests in the twin's Scenario, with OPA-based filter support.

### Key Points

- **Task Assignment Trigger**: When task assigned to delegator → creates Request in twin's Scenario
- **Platform Notification Trigger**: When notification for delegator → creates Request in twin's Scenario
- **Time Schedule Trigger**: Cron-like schedules via Kale → creates Request in twin's Scenario
- All triggers support OPA filters (same pattern as COG Sentinel `on_request_update`)
- Triggers transform signals to Request payloads using standard mapping
- Task Management System observes assignments, dispatches signals to Signal Exchange

## Alternatives Considered

### Alternative 1: Direct Task Collaboration

Have Persona Twin directly collaborate on the original task (same Request).

**Pros:**
- Simpler—no new Request created
- Twin actions visible on original task

**Cons:**
- Mixes personal workflow with business workflow
- Original task state affected by twin
- No isolation of twin's work
- Complicates accountability

**Why rejected:** Persona Twin work should be isolated. Creating a new Request preserves the original task while giving the twin its own workflow.

---

### Alternative 2: Separate Notification System

Create a new notification system specifically for Persona Twins.

**Pros:**
- Custom behavior for twin notifications
- No changes to existing Platform Notifications

**Cons:**
- Duplicates notification infrastructure
- Inconsistent with existing patterns
- More systems to maintain

**Why rejected:** Existing Platform Notifications can route to triggers. No need for separate system.

---

### Alternative 3: Polling-Based Detection

Have Persona Twins poll for new tasks/notifications instead of event triggers.

**Pros:**
- Simpler—no trigger infrastructure
- Twin controls when to check

**Cons:**
- Latency (polling interval)
- Resource waste (constant polling)
- Inconsistent with event-driven Hub architecture

**Why rejected:** Hub is event-driven. Polling is inefficient and inconsistent with architecture.

## Consequences

### Positive

- Consistent with existing trigger patterns
- OPA filters enable fine-grained control
- Event-driven—low latency
- Reuses Signal Exchange infrastructure

### Negative

- Additional trigger types to maintain
- Task Management must emit signals for assignments

### Neutral

- Persona Twin Scenarios receive standard Requests
- Existing Request lifecycle applies

## Implementation Notes

- Add `task_assignment` and `platform_notification` trigger types to Trigger Definitions
- Task Management System observes assignments, emits `task.assigned` signals
- Platform Notifications routes to triggers when recipient has Persona Twin
- Trigger Evaluator evaluates OPA filters with `input.delegator_id` injected
- Kale scheduler integration for time-based triggers

## Related Decisions

- [ADR-0017: Trigger as Standalone Specification](./0017-trigger-as-standalone-specification.md) — Trigger model
- [ADR-0026: Signal Exchange Reminder Capability](./0026-signal-exchange-reminder-capability.md) — Time-based signals

## References

- [Trigger Definitions](../04-subsystems/workbench-management/trigger-definitions.md)
- [Trigger Evaluator](../04-subsystems/signal-exchange/trigger-evaluator.md)
- [Persona Twins Concept](../../olympus-seer-docs/seer-design/implementation-concepts/persona-twins.md)
