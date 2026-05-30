# Foundry IDE

**Module scope:** Builder-facing interface — workspace-specific views on work, tasks, context, progress.

## What this module does

Foundry IDE is the builder-facing interface to Workspaces. It provides:

- **Workspace-specific views** — each Workspace type (Product Specification, UX Design, Development, QA, Release, Governance) has tailored views
- **Work Order visibility** — Work Orders in flight, progress, status
- **Human Task surfacing** — tasks waiting on the builder
- **Context access** — Product context from UPIM, pre-loaded per Workspace
- **Context refinement** — builders can add or refine context in Work Orders

## ACE concepts realized

- **Workspace** — the IDE is the interface to a Workspace
- **Work Order** — visible and actionable in the IDE
- **Task** — Human Tasks surface here; Agent Tasks are observable

## Technical direction

- Based on **VS Code**
- Think **GitHub Codespaces**, but for agentic software work
- Per-builder, per-Workspace sessions
- At runtime, the VS Code Workspace *is* the Foundry Workspace for that builder

## Key design decisions

- **"Builder"** is the term for Foundry IDE users
- **Workspace Session** was considered to disambiguate VS Code Workspace from ACE Workspace, but dropped — the 1:1 per-user mapping makes the overload theoretical, not practical

## WO Runtime Plugin

The IDE includes a **WO Runtime Plugin** that provides the user interface for Work Order execution:

| Component | Purpose |
|-----------|---------|
| **Work Orders Panel** | Tree view of assigned WOs and task trees with status |
| **Agent Chat Tabs** | Chat interface for agent-user interaction |
| **Agent Terminal Windows** | Terminal interface for CLI agents |

The plugin is a UI layer only — VS Code does not mediate agent I/O. Agents communicate directly with users through the UI components.

See [../work-order-runtime/ide-integration.md](../work-order-runtime/ide-integration.md) for full plugin architecture.

## Scenario Editor Extension

The IDE includes a **Scenario Editor Extension** for authoring and testing Work Catalog content:

| Feature | Description |
|---------|-------------|
| **Schema-aware YAML editing** | Autocomplete, validation, and hover docs for Scenario and OI Workflow schemas |
| **Effective catalog browser** | Browse resolved catalog for current Workbench context |
| **Dry-run execution** | Test scenarios with mock inputs before publishing |
| **Preview effective catalog** | See how changes affect the merged catalog |
| **Publish CLI integration** | Publish to User catalog or create PRs to team catalogs |

### Schema Support

| Schema | Features |
|--------|----------|
| **Scenario schema** | Field completion, skill reference validation, scope hints |
| **OI Workflow schema** | Stage completion, action templates, event suggestions |

### Authoring Workflow

1. **Create/edit YAML file** — Schema-aware editor with real-time validation
2. **Preview in catalog** — See where the item fits in the hierarchy
3. **Dry-run test** — Execute with mock inputs, observe behavior
4. **Publish** — Push to User catalog (direct) or create PR (team catalogs)

### Publish Targets

| Target | Method | Who |
|--------|--------|-----|
| **User catalog** | Direct push | All builders |
| **Workbench catalog** | PR to Workshop repo | Workbench Members |
| **Workshop catalog** | PR to Workshop repo | Workshop Members |
| **Foundry catalog** | PR to Foundry repo | Foundry Members |

See [../work-catalogues/user-guide/authoring-scenarios.md](../work-catalogues/user-guide/authoring-scenarios.md) for the complete authoring guide.

## Open questions

- VS Code: fork vs extension vs hosted instance?
- Workspace-specific view customization mechanism
- Session lifecycle, cost model, isolation

## Read next

- [../work-order-runtime/ide-integration.md](../work-order-runtime/ide-integration.md) — WO Runtime plugin architecture
- [../work-order-runtime/README.md](../work-order-runtime/README.md) — WO Runtime module
- [../../ace/workspaces/](../../ace/workspaces/README.md) — the six Workspace types
- [../../tldr-faq.md](../../tldr-faq.md) — interface design decisions
