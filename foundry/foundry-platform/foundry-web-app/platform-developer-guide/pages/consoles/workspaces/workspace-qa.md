# QA Workspace Console

The QA Workspace console shows work execution within the QA workspace.

## Type

Queue + List + Detail

## Audience

QA Engineers, Test Analysts, QA Leads

## Sections

### Work Queue

Work Orders waiting to be picked up:
- Ordered by priority
- Shows estimated effort
- Links to upstream Development deliverables
- Test requirements summary
- Governance badges

### In Progress

Work Orders currently being worked:
- Assignee
- Active session indicator
- Time in progress
- Blockers
- Test execution status
- TestRail links

### Active Sessions

Sessions currently running in this workspace:
- Session owner
- Attached Work Orders
- Session duration
- Test runs in progress
- Quick actions

### Completed

Recently completed Work Orders:
- Completion date
- Test results summary
- Coverage metrics
- Linked to downstream Release workspace

## Actions

| Action | Description |
|--------|-------------|
| Pick up Work Order | Assign Work Order to self |
| Start session | Launch Workspace Session |
| View Work Order | Open Work Order detail |
| View session | Open canonical [Workspace Session Details](workspace-session-details.md) page |
| View in TestRail | Link to TestRail test run |
| Mark complete | Complete Work Order |

Session detail contract source of truth: [workspace-session-details.md](workspace-session-details.md).

## URL

`/workbenches/{workbenchId}/consoles/workspace-qa`
