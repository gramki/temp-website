# Development Workspace Console

The Development Workspace console shows work execution within the Development workspace.

## Type

Queue + List + Detail

## Audience

Software Engineers, Tech Leads, Engineering Managers

## Sections

### Work Queue

Work Orders waiting to be picked up:
- Ordered by priority
- Shows estimated effort
- Links to upstream spec and design deliverables
- Governance badges

### In Progress

Work Orders currently being worked:
- Assignee
- Active session indicator
- Time in progress
- Blockers
- PR status
- Build status

### Active Sessions

Sessions currently running in this workspace:
- Session owner
- Attached Work Orders
- Session duration
- Active PRs
- Quick actions

### Completed

Recently completed Work Orders:
- Completion date
- Code deliverables (PRs merged)
- Linked to downstream QA workspace

## Actions

| Action | Description |
|--------|-------------|
| Pick up Work Order | Assign Work Order to self |
| Start session | Launch Workspace Session (Coder environment) |
| View Work Order | Open Work Order detail |
| View session | Open Workspace Session Details |
| View PR | Link to GitHub PR |
| View build | Link to CI build |
| Mark complete | Complete Work Order |

## URL

`/workbenches/{workbenchId}/consoles/workspace-development`
