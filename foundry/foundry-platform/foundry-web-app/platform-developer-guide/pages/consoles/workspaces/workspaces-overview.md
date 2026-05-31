# Workspaces Overview Console

The Workspaces Overview console is the unified entry point for all workspace types.  
It consolidates the prior per-track workspace queue consoles into a single surface.

## Type

Landing

## Audience

Engineering Managers, Team Leads, Governance

## Sections

### Workspace Type Cards

One card per workspace type:
- Product Specification
- UX Design
- Development
- QA
- Release
- Governance

Each card lists active workspace sessions for that type:
- Session ID and title
- Status
- Owner

### View Options Menu

The header includes a hamburger menu with:
- `Show archived workspaces` toggle

When enabled, archived/closed sessions are included in each workspace type card list.

## Actions

| Action | Description |
|--------|-------------|
| View session | Open canonical [Workspace Session Details](workspace-session-details.md) page |
| Toggle archived visibility | Include/exclude archived workspace sessions |

Session detail contract source of truth: [workspace-session-details.md](workspace-session-details.md).

## URL

`/workbenches/{workbenchId}/consoles/workspaces-overview`
