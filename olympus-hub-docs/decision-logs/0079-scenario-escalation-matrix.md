# ADR-0079: Scenario Escalation Matrix for Application Exceptions

**Status**: Accepted  
**Date**: 2026-01-08  
**Category**: directability

---

## Context

Hub already had Task Queue Escalation Matrix for **time-based** escalation when tasks stall. However, we needed a mechanism for handling **rejection-based** escalation when agent outputs are rejected by guardrails, policies, or applications.

The question was: where should rejection-based escalation be configured?

---

## Decision

Introduce **Scenario Escalation Matrix** as a new configuration block in `ScenarioDeploymentSpec`:

### Two Escalation Matrix Types

| Matrix Type | Trigger | Scope | Purpose |
|-------------|---------|-------|---------|
| **Task Queue EM** | Time-based (task age) | Task-level | Bring in help for stalled tasks |
| **Scenario EM** | Rejection-based | Request/Scenario-level | Handle application-level exceptions |

### Scenario Escalation Matrix Configuration

```yaml
scenario_escalation:
  accountable_human:
    type: workbench_role
    value: supervisor
  
  levels:
    - level: 0
      name: "Senior Analyst Review"
      candidates:
        type: iam_role
        value: senior-analyst
      threshold_minutes: null  # Immediate on rejection
      notification:
        recipients:
          - role: accountable_human
        template: rejection_escalation_l0
        
    - level: 1
      name: "Supervisor Intervention"
      candidates:
        type: workbench_role
        value: supervisor
      threshold_minutes: 60
      notification:
        recipients:
          - role: supervisor
          - role: process_architect
        template: rejection_escalation_l1
        urgency: high
  
  resolution_options:
    allow_context_change: true
    allow_decision_override: true
    allow_scenario_fail: true
    allow_corrective_action: true
```

### Ownership

Both Task Queue EM and Scenario EM are **defined by the Supervisor** as part of Workbench operations.

---

## Consequences

### Positive
- **Clear Separation**: Time-based vs rejection-based escalation have distinct triggers and resolutions
- **Scenario-Scoped**: Application exceptions are handled at the right level
- **Accountable Human**: Explicit designation of who is notified
- **Resolution Options**: Granular control over what resolvers can do

### Negative
- **Additional Configuration**: Supervisors must configure two types of escalation matrices
- **Complexity**: Developers need to understand when each matrix applies

### Neutral
- **Task Queue EM Unchanged**: Existing time-based escalation continues to work
- **Supervisor Single Owner**: All escalation matrices owned by Supervisor (consistent)

---

## Related

- [Scenario Specification Types](../02-system-design/implementation-concepts/scenario-specification-types.md)
- [Agent Directability](../02-system-design/implementation-concepts/agent-directability.md)
- [Task Queues — Escalation Task Queue](../04-subsystems/task-management/task-queues.md)
- [ADR-0006: Task Queue Escalation Model](./0006-task-queue-escalation-model.md)
- [ADR-0078: Agent Directability via Rejection-Escalation Model](./0078-agent-directability-rejection-escalation.md)


