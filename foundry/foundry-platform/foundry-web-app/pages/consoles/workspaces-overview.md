# Workspaces Overview Console

The Workspaces Overview console provides a landing page for all 6 Workspace types, showing sessions, capacity, and work distribution.

## Type

Landing

## Audience

Engineering Managers, Team Leads, Governance

## Sections

### Workspace Summary Cards

One card per Workspace type:
- **Product Specification** — Spec work queue, active sessions
- **UX Design** — Design work queue, active sessions
- **Development** — Dev work queue, active sessions
- **QA** — QA work queue, active sessions
- **Release Workspace** — Release work queue, active sessions
- **Governance Workspace** — Transition validation queue, active sessions

Each card shows:
- Active sessions count
- Work Orders in queue
- Work Orders in progress
- Blocked items

### Active Sessions

Cross-workspace session summary:
- Total active sessions
- Session distribution by workspace
- Recent session activity

### Capacity Distribution

- Work distribution across workspaces
- Bottleneck indicators
- Handoff queues between workspaces

## Actions

| Action | Description |
|--------|-------------|
| Navigate to Workspace | Open specific Workspace console |
| View session | Open Workspace Session Details |
| Start session | Launch new session in a Workspace |

## URL

`/workbenches/{workbenchId}/consoles/workspaces-overview`
