# Product Specification Workspace Console

The Product Specification Workspace console shows work execution within the Product Specification workspace.

## Type

Queue + List + Detail

## Audience

Product Managers, Product Analysts, Business Analysts

## Sections

### Work Queue

Work Orders waiting to be picked up:
- Ordered by priority
- Shows estimated effort
- Governance badges

### In Progress

Work Orders currently being worked:
- Assignee
- Active session indicator
- Time in progress
- Blockers

### Active Sessions

Sessions currently running in this workspace:
- Session owner
- Attached Work Orders
- Session duration
- Quick actions

### Completed

Recently completed Work Orders:
- Completion date
- Deliverables produced
- Linked to downstream workspaces

## Actions

| Action | Description |
|--------|-------------|
| Pick up Work Order | Assign Work Order to self |
| Start session | Launch Workspace Session |
| View Work Order | Open Work Order detail |
| View session | Open canonical [Workspace Session Details](workspace-session-details.md) page |
| Mark complete | Complete Work Order |

Session detail contract source of truth: [workspace-session-details.md](workspace-session-details.md).

## URL

`/workbenches/{workbenchId}/consoles/workspace-product-spec`
