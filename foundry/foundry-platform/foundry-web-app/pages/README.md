# Foundry Web App — Pages

This folder contains requirements for key pages in the Foundry Web App.

## Page Hierarchy

```
Foundry Home (/)
└── Workshop Home (/workshops/{workshopId})
    └── Workbench Home (/workbenches/{workbenchId})
        ├── Consoles (/workbenches/{id}/consoles/{consoleId})
        │   ├── Work: PI, Workspaces, Progress, Track
        │   ├── Build: CI, Components, Quality Status, Release
        │   ├── Resources: Repositories & Tools
        │   ├── Workforce: Team, Agent
        │   ├── Governance: Risk, Reports, Quality Compliance
        │   └── Settings: Admin
        └── Detail Pages
            ├── Team Member Profile (/workbenches/{id}/team/{memberId})
            └── Workspace Session Details (/workbenches/{id}/sessions/{sessionId})
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
| **Work** | PI, Workspaces, Progress, Track |
| **Build** | CI, Components, Quality Status, Release |
| **Resources** | Repositories & Tools |
| **Workforce** | Team, Agent |
| **Governance** | Risk, Reports, Quality Compliance |
| **Settings** | Admin |

## Detail Pages

| Page | URL Pattern | Defined In |
|------|-------------|------------|
| Team Member Workbench Profile | `/workbenches/{id}/team/{memberId}` | [team-console.md](consoles/team-console.md) |
| Workspace Session Details | `/workbenches/{id}/sessions/{sessionId}` | [workspaces-console.md](consoles/workspaces-console.md) |

## Planned Pages (TBD)

| Page | URL Pattern | Notes |
|------|-------------|-------|
| Intent Details | `/workbenches/{id}/intents/{piId}` | Product Intent detail view |
| Work Order Details | `/workbenches/{id}/work-orders/{woId}` | Work Order progress, Tasks |
| Task View | `/workbenches/{id}/tasks/{taskId}` | Human Task execution |

## Navigation Model

Users navigate top-down:
1. **Foundry Home** — See all Workshops
2. **Workshop Home** — See Workbenches in a Workshop
3. **Workbench Home** — Primary work surface (Wall + PI Badges)
4. **Consoles** — Focused views via side navigation

Breadcrumbs always show the hierarchy: `Foundry > Workshop > Workbench > [Console]`
