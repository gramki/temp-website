# ADR-0013: Shared Utility Consoles Between Agent and Supervisor

## Status

Accepted

## Date

2026-01-06

## Context

Agent Desk and Supervisor Desk both need access to common operational capabilities:
- Viewing and managing tasks
- Accessing files
- Running reports
- Querying knowledge base
- Monitoring signals (exceptions, observations)
- Managing routines and checklists

Options considered:
1. **Separate consoles**: Build distinct consoles for each persona
2. **Shared consoles**: Share common consoles, add supervisor-specific ones
3. **Single application**: One app with role-based visibility

Separate consoles would mean duplicating functionality and divergent experiences. A single application would be complex to maintain with conditional logic everywhere.

## Decision

**Share utility consoles between Agent Desk and Supervisor Desk; add supervisor-only management consoles.**

### Shared Utility Consoles
| Console | Purpose | Agent | Supervisor |
|---------|---------|-------|------------|
| Tasks Console | View and manage tasks | ✅ (assigned) | ✅ (all) |
| Files Console | Access files and documents | ✅ | ✅ |
| Reports Console | Run and view reports | ✅ | ✅ |
| Knowledge Base Console | Search SOPs, policies | ✅ | ✅ |
| Signals Console | View exceptions, observations | ✅ | ✅ |
| Routines & Checklists Console | Manage personal routines | ✅ | ✅ |

### Supervisor-Only Consoles
| Console | Purpose |
|---------|---------|
| Analytics Console | Queue metrics, SLA tracking, throughput |
| Task Allocation Management | Queue configuration, escalation policies |
| Agents & Access Management | Agent enrollment, capabilities, availability |

### Scope Differences
When both personas access the same console, scope differs:
- **Agent**: Sees own tasks, assigned queues
- **Supervisor**: Sees all tasks, all queues in workbench

## Consequences

### Positive
- **Consistency**: Agents and supervisors have familiar interface for common tasks
- **Smooth promotion**: Agent promoted to supervisor already knows utility consoles
- **Less duplication**: Shared console code, single maintenance point
- **Clear separation**: Supervisor management clearly distinct

### Negative
- **Scope logic**: Consoles must handle different scopes per role
- **Feature creep risk**: Temptation to add supervisor features to shared consoles

### Neutral
- Custom consoles (workbench-specific) are separate from utility consoles

## Related

- [Agent Desk](../06-ux-architecture/tenant-domain/agent-desk.md)
- [Supervisor Desk](../06-ux-architecture/tenant-domain/supervisor-desk.md)
- [UX Architecture Overview](../06-ux-architecture/README.md)

