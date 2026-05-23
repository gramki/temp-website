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

## Open questions

- VS Code: fork vs extension vs hosted instance?
- Workspace-specific view customization mechanism
- Session lifecycle, cost model, isolation

## Read next

- [../../ace/workspaces/](../../ace/workspaces/README.md) — the six Workspace types
- [../../tldr-faq.md](../../tldr-faq.md) — interface design decisions
