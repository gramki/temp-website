# Foundry Web App

The Foundry Web App is the primary web interface for the Foundry Platform. It serves multiple personas across all Workspaces, providing access to Work Orders, Tasks, context, analytics, and administration.

## Relationship to Platform Modules

The web app consumes and surfaces capabilities from all platform modules:

| Module | What the Web App Exposes |
|--------|--------------------------|
| **Foundry Management** | Admin console — Workbenches, repositories, teams, agents, tenancy |
| **Foundry IDE** | Links to/from IDE; context synchronization |
| **Work Order Runtime** | Work Order views, Task queues, context display, progress tracking |
| **Foundry Orchestrator** | Orchestration item flow visualization, gate status, transition triggers |
| **Work Catalogs** | Work Catalogs browsing (read-only for most personas) |
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
- Core JTBD for each persona (see [user-guide/personas/](user-guide/personas/))

## Documentation

| Guide | Audience | Index |
|-------|----------|-------|
| Concepts | Anyone | This README |
| [User guide](user-guide/) | Admins, builders | Task-oriented usage |
| [Foundry Platform developer guide](platform-developer-guide/) | Platform engineers | Implementation specs |

## Read Next

- [user-guide/personas/README.md](user-guide/personas/README.md) — persona index
- [platform-developer-guide/pages/README.md](platform-developer-guide/pages/README.md) — page specifications
- [../README.md](../README.md) — Foundry Platform overview
- [../../ace/workspaces/](../../ace/workspaces/README.md) — Workspace definitions
- [../../tldr.md](../../tldr.md) — One-page Foundry overview
