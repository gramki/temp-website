# Foundry Workspace Panel

The Foundry Workspace Panel is a collapsible sidebar section in the Foundry IDE that surfaces workspace and workbench context, quick navigation, and WO Runtime settings for the active Workspace Session.

## What it is

Builders spend most of their time in a single Workspace Session. The Foundry Workspace Panel answers "where am I working?" and "what can I reach from here?" without leaving the IDE.

Core sections:

| Section | Content |
|---------|---------|
| **Workspace Info** | Workspace name, ID, type (e.g. Development, Product Specification), environment (dev / staging / prod) |
| **Workbench Info** | Workbench name, team membership summary, product scope |
| **Quick Links** | Related Git repos (Intent, Design, Code), external links (Jira, Confluence, dashboards) — open in browser or reveal in Explorer |
| **WO Runtime Settings** | Session-scoped options: default capable agent, quota display, approval policies, work-context sync interval |

The panel is **collapsible** in the sidebar (expand/collapse chevron). Default placement is above the Work Orders Panel so workspace context is visible before task navigation.

WO Runtime settings shown here are **read/write** where the builder has permission; changes apply to the current session and are persisted by WO Runtime in session configuration.

Example layout:

```
▼ FOUNDRY WORKSPACE
  Workspace: checkout-dev (Development)
  Workbench: checkout · Payments
  Environment: dev
  ─ Quick Links ─
  · checkout-intent (repo)
  · checkout-design (repo)
  · Jira board
  · Confluence space
  ─ WO Runtime ─
  Default agent: cursor-agent
  work-context sync: 60s
  [Open settings…]
```

## Where it lives in Foundry

| Module | Responsibility |
|--------|----------------|
| **IDE** | Renders the panel; handles collapse state and link actions |
| **WO Runtime** | Supplies workspace/workbench metadata, link registry, and settings API |
| **Session Management** | Owns session identity and environment binding |
| **Management** | Workbench and workspace definitions from workshop repos |

Data is loaded on session start and refreshed when WO Runtime pushes workspace metadata changes (e.g. after catalog recompute).

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Workspace Session](../../concepts/workspace-session.md) | Panel displays active Workspace type and session binding |
| Workbench | Team, product scope, and knowledge repo links |
| Builder | Primary consumer of workspace context in the IDE |

The panel does not replace the Work Orders Panel — it complements it with **static session context** versus **dynamic work assignment**.

## Related concepts

- [Workspace Folder Structure](workspace-folder-structure.md) — Local folder layout the panel's repo links map to
- [Builder](builder.md) — Who uses the panel
- [Workspace Views](workspace-views.md) — Per-workspace-type UI beyond this panel
- [Work Order](../../concepts/work-order.md) — Listed in the Work Orders Panel below

## Further reading

- [../platform-developer-guide/ux-requirements.md](../platform-developer-guide/ux-requirements.md) — IDE-UX-078 to IDE-UX-084
- [../../work-order-runtime/platform-developer-guide/ide-integration.md](../../work-order-runtime/platform-developer-guide/ide-integration.md) — Foundry Workspace Panel protocol
- [../../management/platform-developer-guide/git-infrastructure.md](../../management/platform-developer-guide/git-infrastructure.md) — Repository inventory for quick links
