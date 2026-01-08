# ADR-0080: Directability Operations in Task Management

**Status**: Accepted  
**Date**: 2026-01-08  
**Category**: directability

---

## Context

When agent outputs are rejected and escalation tasks are created, humans need structured ways to resolve these escalations. We needed to define:
1. What **resolution operations** are available?
2. How are resolutions **exposed** via UX/API?
3. How are resolutions **recorded** in CAF?

---

## Decision

Define six **Directability Operations** in Task Management for handling escalation tasks:

### Resolution Operations

| Operation | Description | CAF Records Created |
|-----------|-------------|---------------------|
| **Acknowledge Escalation** | Human acknowledges review | DirectiveResolution (ack) |
| **Override Decision** | Replace rejected decision with new value | Override + DirectiveResolution (outcome) |
| **Change Context & Re-run** | Modify context and trigger agent re-run | ContextIntervention + DirectiveResolution (outcome) |
| **Reassign for Retry** | Assign original task to different agent | Task History (REASSIGNED) + DirectiveResolution |
| **Fail Scenario** | Mark scenario as failed | Request State Change + DirectiveResolution |
| **Create Corrective Action** | Spawn new request in different scenario | New Request + DirectiveResolution |

### API Exposure

#### REST Endpoints (Agent REST Channel)

```
POST /api/agent/v1/tasks/{task_id}/acknowledge
POST /api/agent/v1/tasks/{task_id}/override
POST /api/agent/v1/tasks/{task_id}/change-context
POST /api/agent/v1/tasks/{task_id}/reassign-retry
POST /api/agent/v1/tasks/{task_id}/fail-scenario
POST /api/agent/v1/tasks/{task_id}/corrective-action
GET  /api/agent/v1/tasks/{task_id}/rejection-context
```

#### MCP Tools (Agent/Supervisor Channels)

```
acknowledge_escalation
override_decision
change_context_rerun
reassign_for_retry
fail_scenario
create_corrective_action
get_rejection_context
```

### UX — Intervention Solver Interface

Agent Desk includes an **Intervention Solver Interface** for escalation tasks with:
- Rejected artifact details
- Original context summary
- Resolution option buttons
- Rationale input fields
- Category selection

---

## Consequences

### Positive
- **Structured Resolution**: Consistent handling across all escalation types
- **Full Audit Trail**: Every resolution creates CAF records
- **Multi-Channel Access**: Web, REST, MCP all support the same operations
- **Learning Input**: Resolutions feed Enterprise Learning

### Negative
- **Learning Curve**: Agents need to understand escalation task workflow
- **Additional UI**: Intervention Solver is another interface to maintain

### Neutral
- **Permission Model**: Operations follow existing task permission model (Agent vs Supervisor)
- **AI Agents Included**: AI agents can resolve escalations via MCP (within their authority)

---

## Related

- [Agent Task Operations](../04-subsystems/task-management/agent-task-operations.md)
- [Agent Desk — Intervention Solver Interface](../06-ux-architecture/tenant-domain/agent-desk.md)
- [REST Channels — Directability APIs](../06-ux-architecture/tenant-domain/rest-channels.md)
- [MCP Channels — Directability Tools](../06-ux-architecture/tenant-domain/mcp-channels.md)
- [Directive Resolution Records](../04-subsystems/cognitive-audit-fabric/episodic-memory-store/directive-resolution-records.md)
- [ADR-0078: Agent Directability via Rejection-Escalation Model](./0078-agent-directability-rejection-escalation.md)
- [ADR-0079: Scenario Escalation Matrix](./0079-scenario-escalation-matrix.md)


