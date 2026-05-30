# IDE Concepts

This folder contains module-specific concept definitions for the Foundry IDE. Each concept file provides a single authoritative definition within the IDE module's domain, linking back to platform-wide concepts where appropriate.

## How to use these concepts

- **Reference, don't duplicate.** Link to these definitions rather than restating them in module docs.
- **Module-specific scope.** These concepts are IDE-specific specializations; platform-wide concepts live in [`../concepts/`](../../concepts/).
- **Implementation details elsewhere.** Concepts are definitions; implementation specs live in `platform-developer-guide/`.

## Concept Index

| Concept | Definition |
|---------|------------|
| [Builder](builder.md) | Human user of the Foundry IDE — the term for anyone working in a Workspace Session |
| [Workspace Views](workspace-views.md) | Per-Workspace-type UI customizations providing context-specific panels, layouts, and tooling |
| [Scenario Editor](scenario-editor.md) | Schema-aware YAML editor extension for authoring Work Catalog Scenarios |
| [Employed Agents Panel](employed-agents-panel.md) | Right panel listing all employed agents in the session with status and filters |
| [Task Graph View](task-graph-view.md) | Editor-tab folder-style task tree for a Work Order with WO detail header |
| [Agent Employment](agent-employment.md) | How builders employ agents during Human Tasks and Personal Work |
| [Foundry Workspace Panel](foundry-workspace-panel.md) | Collapsible sidebar for workspace/workbench context, links, and WO Runtime settings |
| [Scenario Authoring](scenario-authoring.md) | Create Scenario journey scaffolding ingress/internal scenarios in user-work-catalog |
| [Workspace Folder Structure](workspace-folder-structure.md) | Local session folder layout, WO repos, work-context, and branch lifecycle |

## Relationship to Platform Concepts

These module concepts specialize and extend platform-wide concepts:

| Platform Concept | IDE Specialization |
|------------------|-------------------|
| [Workspace Session](../../concepts/workspace-session.md) | IDE provides the visual interface to Sessions via Builder UX |
| [Scenario](../../concepts/scenario.md) | IDE provides the Scenario Editor for authoring |
| [Work Order](../../concepts/work-order.md) | IDE provides the Work Orders Panel for visibility |
| [Task](../../concepts/task.md) | IDE provides task graph, Employed Agents panel, and editor Agent Output tabs |
| [Personal Work](../../concepts/personal-work.md) | IDE shows Personal Work in sidebar; association prompt for ad-hoc agents |

## Read next

- [builder.md](builder.md) — The term for Foundry IDE users
- [workspace-views.md](workspace-views.md) — How each Workspace type gets tailored UI
- [scenario-editor.md](scenario-editor.md) — Authoring Scenarios in the IDE
- [foundry-workspace-panel.md](foundry-workspace-panel.md) — Session context in the sidebar
- [workspace-folder-structure.md](workspace-folder-structure.md) — On-disk layout for repos and work-context
- [../../concepts/README.md](../../concepts/README.md) — Platform-wide concepts
