# Workspace Views

Workspace Views are per-Workspace-type UI customizations in the Foundry IDE — tailored panels, layouts, and tooling that surface relevant context and actions for each of the six Workspace types.

## What it is

Each Workspace type (Product Specification, UX Design, Development, QA, Release, Governance) has different work artifacts, context needs, and typical tasks. Workspace Views adapt the IDE interface to match:

| Workspace Type | View Adaptations |
|----------------|------------------|
| **Product Specification** | Intent and PSD documents, stakeholder context, specification status |
| **UX Design** | Design system references, wireframe previews, accessibility checks |
| **Development** | Code context, test results, PR status, branch state |
| **QA** | Test case libraries, execution history, coverage metrics |
| **Release** | Artifact inventories, quality gates, distribution targets |
| **Governance** | Evidence requirements, ritual schedules, finding registers |

Views provide:

- **Work Orders Panel** — Shows WOs relevant to the Workspace type with appropriate status badges
- **Context Panel** — Pre-loads product context appropriate to the Workspace (from UPIM)
- **Artifact Views** — Displays work artifacts in workspace-appropriate formats
- **Agent Interaction** — Chat tabs and terminal windows, consistent across views

The Work Orders Panel adapts its display based on Workspace type:

| Element | Development View | QA View | Release View |
|---------|------------------|---------|--------------|
| **Status badges** | Feature/PR-focused | Test execution states | Gate pass/fail |
| **Task tree** | Implementation tasks | Test case tasks | Release checklist |
| **Actions** | Open PR, Run tests | Execute suite, Approve | Publish, Sign |

Workspace Views are **not** separate applications. They are dynamic UI configurations within the same VS Code instance, activated based on the Workspace type of the active [Workspace Session](../../concepts/workspace-session.md).

## Where it lives in Foundry

| Module | Responsibility |
|--------|----------------|
| **IDE** | Implements Workspace Views via extensions and view providers |
| **WO Runtime** | Activates appropriate view when Session starts |
| **Workshop Definition Repo** | `.devcontainer/` templates can customize view defaults |
| **Metadata Service** | Provides view configuration per Workspace type |

View configuration hierarchy:

```
Platform default view
  → Workshop override (if defined)
    → Workbench override (if defined)
      → User preferences (within allowed bounds)
```

This follows the same [Knowledge Hierarchy](../../concepts/knowledge-hierarchy.md) pattern used elsewhere in Foundry.

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Workspace](../../ace/concepts.md#workspace) | Views operationalize Workspace-specific context |
| [IDE](../../ace/concepts.md#ide) | Views are the ACE IDE's Workspace-aware adaptation |
| Six Workspace types | Each type gets a corresponding View |

From ACE: "The IDE is the human's entry surface into a Workspace. ACE treats each Workspace as having its own IDE context."

Workspace Views realize this principle — each Workspace type has its own IDE context, surfaced through Views.

## Related concepts

- [Builder](builder.md) — Who uses Workspace Views
- [Workspace Session](../../concepts/workspace-session.md) — Runtime context that activates a View
- [Work Order](../../concepts/work-order.md) — What appears in the Work Orders Panel
- [Knowledge Hierarchy](../../concepts/knowledge-hierarchy.md) — How view configuration inherits

## Further reading

- [../user-guide/workspace-sessions.md](../user-guide/workspace-sessions.md) — Builder experience in views
- [../platform-developer-guide/extensions.md](../platform-developer-guide/extensions.md) — View implementation via extensions
- [../../ace/workspaces/](../../ace/workspaces/README.md) — The six Workspace types
