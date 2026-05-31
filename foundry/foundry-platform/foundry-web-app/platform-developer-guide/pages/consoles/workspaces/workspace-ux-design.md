# UX Design Workspace Console

The UX Design Workspace console shows work execution within the UX Design workspace.

## Type

Queue + List + Detail

## Audience

UX Designers, UI Designers, Product Designers

## Sections

### Work Queue

Work Orders waiting to be picked up:
- Ordered by priority
- Shows estimated effort
- Links to upstream Product Spec deliverables
- Governance badges

### In Progress

Work Orders currently being worked:
- Assignee
- Active session indicator
- Time in progress
- Blockers
- Design tool links (Figma)

### Active Sessions

Sessions currently running in this workspace:
- Session owner
- Attached Work Orders
- Session duration
- Quick actions

### Completed

Recently completed Work Orders:
- Completion date
- Design deliverables produced
- Linked to downstream Development workspace

## Actions

| Action | Description |
|--------|-------------|
| Pick up Work Order | Assign Work Order to self |
| Start session | Launch Workspace Session |
| View Work Order | Open Work Order detail |
| View session | Open canonical [Workspace Session Details](workspace-session-details.md) page |
| Open in Figma | Link to Figma project |
| Mark complete | Complete Work Order |

Session detail contract source of truth: [workspace-session-details.md](workspace-session-details.md).

## URL

`/workbenches/{workbenchId}/consoles/workspace-ux-design`
