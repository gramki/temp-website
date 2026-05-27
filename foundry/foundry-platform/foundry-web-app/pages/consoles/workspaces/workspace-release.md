# Release Workspace Console

The Release Workspace console shows work execution within the Release workspace.

## Type

Queue + List + Detail

## Audience

Release Engineers, DevOps Engineers, Release Managers

## Sections

### Work Queue

Work Orders waiting to be picked up:
- Ordered by priority
- Shows estimated effort
- Links to upstream QA deliverables
- Release checklist status
- Governance badges

### In Progress

Work Orders currently being worked:
- Assignee
- Active session indicator
- Time in progress
- Blockers
- Deployment status
- Weave integration status

### Active Sessions

Sessions currently running in this workspace:
- Session owner
- Attached Work Orders
- Session duration
- Active deployments
- Quick actions

### Completed

Recently completed Work Orders:
- Completion date
- Release artifacts produced
- Deployment status
- Post-release validation

## Actions

| Action | Description |
|--------|-------------|
| Pick up Work Order | Assign Work Order to self |
| Start session | Launch Workspace Session |
| View Work Order | Open Work Order detail |
| View session | Open Workspace Session Details |
| View in Weave | Link to Olympus Weave deployment |
| Trigger deployment | Initiate deployment pipeline |
| Mark complete | Complete Work Order |

## URL

`/workbenches/{workbenchId}/consoles/workspace-release`
