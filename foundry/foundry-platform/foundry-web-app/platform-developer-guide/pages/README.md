# Foundry Web App — Pages (Developer Guide)

This folder contains requirements for key pages in the Foundry Web App.

## Page Hierarchy

```
Foundry Home (/)
└── Workshop Home (/workshops/{workshopId})
    └── Workbench Home (/workbenches/{workbenchId})
        ├── Consoles (/workbenches/{id}/consoles/{consoleId})
        │   ├── Work: Overview, Orchestration, Progress, Rituals, My Work
        │   ├── Workspaces: Overview, Product Spec, UX Design, Development, QA, Release, Governance
        │   ├── Build: CI, Components, Findings, Quality Status, Release Artifacts
        │   ├── Workforce: Overview, Team, Agent
        │   ├── Governance: Overview, Rituals, Controls, Registers, Reports, Quality Controls
        │   ├── Resources: Repositories & Tools
        │   └── Settings: Admin, Governance Admin
        └── Detail Pages
            ├── Orchestration Item (/workbenches/{id}/orchestration/{type}/{itemId})
            ├── Team Member Profile (/workbenches/{id}/team/{memberId})
            └── Workspace Session (/workbenches/{id}/sessions/{sessionId})
```

## Home Pages

| Page | File | URL Pattern |
|------|------|-------------|
| [Foundry Home](foundry-home.md) | `foundry-home.md` | `/` |
| [Workshop Home](workshop-home.md) | `workshop-home.md` | `/workshops/{workshopId}` |
| [Workbench Home](workbench-home.md) | `workbench-home.md` | `/workbenches/{workbenchId}` |

## Workbench Consoles

See [consoles/README.md](consoles/README.md) for all console pages.

| Group | Consoles |
|-------|----------|
| **Work** | Work Overview, Orchestration, Progress, Rituals, My Work |
| **Workspaces** | Workspaces Overview, Product Specification, UX Design, Development, QA, Release Workspace, Governance Workspace |
| **Build** | CI, Components, Findings, Quality Status, Release Artifacts |
| **Workforce** | Workforce Overview, Team, Agent |
| **Governance** | Governance Overview, Rituals, Controls & Enforcement, Registers, Reports & Dashboards, Quality Controls |
| **Resources** | Repositories & Tools |
| **Settings** | Admin, Governance Admin |

## Detail Pages

| Page | URL Pattern | Defined In |
|------|-------------|------------|
| Orchestration Item Details | `/workbenches/{id}/orchestration/{type}/{itemId}` | [orchestration-console.md](consoles/work/orchestration-console.md) |
| Team Member Workbench Profile | `/workbenches/{id}/team/{memberId}` | [team-console.md](consoles/workforce/team-console.md) |
| Workspace Session Details | `/workbenches/{id}/sessions/{sessionId}` | [workspace-session-details.md](consoles/workspaces/workspace-session-details.md) |

## Planned Pages (TBD)

| Page | URL Pattern | Notes |
|------|-------------|-------|
| Work Order Details | `/workbenches/{id}/work-orders/{woId}` | Work Order progress, Tasks |
| Task View | `/workbenches/{id}/tasks/{taskId}` | Human Task execution |

## Navigation Model

Users navigate top-down:
1. **Foundry Home** — See all Workshops
2. **Workshop Home** — See Workbenches in a Workshop
3. **Workbench Home** — Primary work surface (Wall + PI Badges)
4. **Consoles** — Focused views via side navigation

Breadcrumbs always show the hierarchy: `Foundry > Workshop > Workbench > [Console]`
