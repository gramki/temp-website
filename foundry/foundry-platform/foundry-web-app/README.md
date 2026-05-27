# Foundry Web App

The Foundry Web App is the primary web interface for the Foundry Platform. It serves multiple personas across all Workspaces, providing access to Work Orders, Tasks, context, analytics, and administration.

## Key Pages

| Page | Path | Description |
|------|------|-------------|
| [Foundry Home](pages/foundry-home.md) | `/` | Entry point; Foundry-wide dashboard |
| [Workshop Home](pages/workshop-home.md) | `/workshops/{id}` | Workshop dashboard; Workbenches list |
| [Workbench Home](pages/workbench-home.md) | `/workbenches/{id}` | Product dashboard; primary work surface |

## Personas

| Persona | Folder | Primary Workspace |
|---------|--------|-------------------|
| [Developers](personas/developers/README.md) | `personas/developers/` | Development |
| [Product Managers](personas/product-managers/README.md) | `personas/product-managers/` | Product Specification |
| [Quality Teams](personas/quality-teams/README.md) | `personas/quality-teams/` | QA |
| [UX Teams](personas/ux-teams/README.md) | `personas/ux-teams/` | UX Design |
| [Release Teams](personas/release-teams/README.md) | `personas/release-teams/` | Release |
| [Governance Teams](personas/governance-teams/README.md) | `personas/governance-teams/` | Governance |
| [Foundry Admins](personas/foundry-admins/README.md) | `personas/foundry-admins/` | Foundry Management |

## Relationship to Platform Modules

The web app consumes and surfaces capabilities from all platform modules:

| Module | What the Web App Exposes |
|--------|--------------------------|
| **Foundry Management** | Admin console — Workbenches, repositories, teams, agents, tenancy |
| **Foundry IDE** | Links to/from IDE; context synchronization |
| **Work Order Runtime** | Work Order views, Task queues, context display, progress tracking |
| **Foundry Orchestrator** | Orchestration item flow visualization, gate status, transition triggers |
| **Scenario Authoring** | Scenario catalogue browsing (read-only for most personas) |
| **Release Tools** | CI/CD status, release pipelines, artifact management |
| **Platform Ops** | Health dashboards, observability (admin-facing) |

## Cross-Cutting Capabilities

All personas share these capabilities:

- **Search** — Find Work Orders, artifacts, decisions across the Foundry
- **Notifications** — Alerts for tasks, blockers, completions
- **Navigation** — Move between Workspaces, Workbenches, Work Orders
- **Context** — Always see the parent orchestration-item graph for current work
- **History** — View audit trail for any Work Order
- **Help** — Access documentation, glossary, onboarding

## Design Principles

1. **Workspace-centric views** — Each persona sees a view tailored to their Workspace
2. **Work Order is the unit of focus** — Every action relates to a Work Order
3. **Context flows with the work** — parent orchestration-item graph is always accessible
4. **Agents are visible** — Agent Tasks and progress are surfaced, not hidden
5. **Governance is integrated** — Gate status and evidence visible in-flow, not separate

## Phase 1 Scope

Phase 1 commits to four Tracks: Discovery, Build, Release, and Governance. The web app will support:

- All seven personas
- Subset of Scenarios per (Track, Workspace)
- Core JTBD for each persona (see persona folders)

## Read Next

- [../README.md](../README.md) — Foundry Platform overview
- [../../ace/workspaces/](../../ace/workspaces/README.md) — Workspace definitions
- [../../tldr.md](../../tldr.md) — One-page Foundry overview
