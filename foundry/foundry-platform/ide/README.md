# Foundry IDE

**Module scope:** Builder-facing interface — workspace-specific views on work, tasks, context, progress.

## What this module does

Foundry IDE is the builder-facing interface to Workspaces. It provides workspace-specific views, Work Order visibility, Human Task surfacing, and context access for builders working in Workspace Sessions.

→ [user-guide/workspace-sessions.md](user-guide/workspace-sessions.md) for builder-facing capabilities and session model

## ACE concepts realized

- **Workspace** — the IDE is the interface to a Workspace
- **Work Order** — visible and actionable in the IDE
- **Task** — Human Tasks surface here; Agent Tasks are observable

## Technical direction

- Based on **VS Code** (Code Server) running inside a Kubernetes pod
- Pod provisioned by [Workspace Session Infrastructure](../workspace-session-infrastructure/README.md); IDE extensions ship pre-installed in the platform base image
- IDE is available only when a session is **Active** per [Session Management](../workspace-session-management/concepts/session-lifecycle.md) state machine
- Per-builder, per-Workspace sessions at `{session-id}.sessions.{domain}`
- At runtime, the VS Code Workspace *is* the Foundry Workspace for that builder

## Relationship to session modules

| Module | IDE relationship |
|--------|------------------|
| [Session Infrastructure](../workspace-session-infrastructure/README.md) | Packages IDE extensions into base image (Layer 1); Foundry admins can add extensions via admin layering (Layer 3) |
| [Session Management](../workspace-session-management/README.md) | Session must be Active before IDE is accessible |
| [WO Runtime](../work-order-runtime/README.md) | Provides Work Orders Panel, task graph, Employed Agents panel, and agent output via plugin protocol |

## Dependencies

| Dependency | Relationship |
|------------|--------------|
| [Workspace Session Infrastructure](../workspace-session-infrastructure/README.md) | Image packaging pipeline for IDE extensions |
| [Workspace Session Management](../workspace-session-management/README.md) | Session must be Active for IDE access |
| [Work Order Runtime](../work-order-runtime/README.md) | Plugin protocol for Work Orders and agents |

## Key design decisions

- **"Builder"** is the term for Foundry IDE users
- **Workspace Session** was considered to disambiguate VS Code Workspace from ACE Workspace, but dropped — the 1:1 per-user mapping makes the overload theoretical, not practical

→ [platform-developer-guide/extensions.md](platform-developer-guide/extensions.md) for WO Runtime Plugin and Scenario Editor Extension specs  
→ [platform-developer-guide/ux-requirements.md](platform-developer-guide/ux-requirements.md) for IDE UX requirements and Figma mockup index

## Key Concepts

### Platform-wide concepts

| Concept | What IDE does with it |
|---------|----------------------|
| [Workspace Session](../concepts/workspace-session.md) | Provides the visual interface to Sessions |
| [Work Order](../concepts/work-order.md) | Displays in Work Orders Panel |
| [Task](../concepts/task.md) | Surfaces Human Tasks; provides chat tabs for Agent Tasks |
| [Scenario](../concepts/scenario.md) | Provides the Scenario Editor for authoring |

### Module-specific concepts

| Concept | Definition |
|---------|------------|
| [Builder](concepts/builder.md) | Human user of the Foundry IDE |
| [Workspace Views](concepts/workspace-views.md) | Per-Workspace-type UI customizations |
| [Scenario Editor](concepts/scenario-editor.md) | Schema-aware YAML editor for Work Catalog Scenarios |
| [Employed Agents Panel](concepts/employed-agents-panel.md) | Session-wide agent roster in the right panel |
| [Task Graph View](concepts/task-graph-view.md) | WO detail + folder-style task tree in editor tabs |
| [Agent Employment](concepts/agent-employment.md) | Employing agents during Human Tasks and Personal Work |
| [Foundry Workspace Panel](concepts/foundry-workspace-panel.md) | Workspace/workbench context, quick links, WO Runtime settings |
| [Scenario Authoring](concepts/scenario-authoring.md) | Create Scenario scaffold in user-work-catalog |
| [Workspace Folder Structure](concepts/workspace-folder-structure.md) | Session folder tree, WO repos, work-context sync |

→ [concepts/README.md](concepts/README.md) — Full module concept index

## Open questions

- VS Code: fork vs extension vs hosted instance?
- Workspace-specific view customization mechanism

## Documentation

| Guide | Audience | Index |
|-------|----------|-------|
| [Concepts](concepts/) | Anyone | Module-specific concept definitions |
| [User guide](user-guide/) | Admins, builders | Task-oriented usage |
| [Foundry Platform developer guide](platform-developer-guide/) | Platform engineers | Implementation specs |

## Read next

- [../workspace-session-infrastructure/README.md](../workspace-session-infrastructure/README.md) — extension packaging in session images
- [../workspace-session-management/README.md](../workspace-session-management/README.md) — session lifecycle
- [user-guide/workspace-sessions.md](user-guide/workspace-sessions.md) — builder-facing Workspace Session capabilities
- [platform-developer-guide/extensions.md](platform-developer-guide/extensions.md) — WO Runtime Plugin and Scenario Editor
- [../work-order-runtime/platform-developer-guide/ide-integration.md](../work-order-runtime/platform-developer-guide/ide-integration.md) — WO Runtime plugin architecture
- [../../ace/workspaces/](../../ace/workspaces/README.md) — the six Workspace types
