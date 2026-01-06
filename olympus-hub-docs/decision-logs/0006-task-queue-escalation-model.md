# ADR-0006: Cumulative Assignment Across Escalation Levels

## Status

Accepted

## Date

2026-01-06

## Context

Task queues have escalation matrices that define when and to whom tasks should be escalated. When a task escalates from Level 0 to Level 1, the question arose:

1. **Replace**: Does Level 1 agent replace Level 0 agent as the sole assignee?
2. **Cumulative**: Are Level 0 and Level 1 agents both assignees?

This affects:
- Who can act on the task
- Who is notified
- Who is tracked as an "actor" on the Request

## Decision

**Escalation is cumulative. All agents at all escalation levels the task has reached are assignees.**

Specifics:
1. When a task escalates from Level 0 to Level 1:
   - Level 0 agents remain assignees
   - Level 1 agents are added as assignees
   - Both levels can act on the task

2. **Any assignee at any level can complete the task** — first one to complete wins

3. **All assignees at all levels are actors** associated with the Request

4. **Practical behavior**: When escalated, higher-level agents typically either:
   - Work on the task directly, or
   - Nudge lower-level agents to complete it

## Consequences

### Positive
- **Flexibility**: Multiple agents can collaborate on escalated tasks
- **Visibility**: Supervisors (often at higher levels) can see and act on tasks
- **No handoff delay**: Lower-level agent can still complete if they're close to finishing
- **Full audit trail**: All involved agents are tracked as actors

### Negative
- **Potential confusion**: Multiple agents may work on the same task
- **Duplicate effort**: Without coordination, work may be duplicated
- **More notifications**: All assignees receive task updates

### Neutral
- Applications and agents should check task status before investing significant effort

## Related

- [Task Queues](../04-subsystems/task-management/task-queues.md)
- [Task Lifecycle](../04-subsystems/task-management/task-lifecycle.md)
- [Agent Task Operations](../04-subsystems/task-management/agent-task-operations.md)

