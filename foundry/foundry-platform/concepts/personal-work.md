# Personal Work

Personal Work is a workspace-local Work Order that captures ad-hoc agent usage not tied to orchestrated Work Order tasks — general exploration, tooling, and builder-initiated work within a Workspace Session.

## What it is

Foundry tracks most work through [Work Orders](work-order.md) created by the Orchestrator and synced to Jira. Builders also need to use agents for work that does not map to an assigned Human Task — understanding a codebase, experimenting with an approach, or running a one-off analysis.

Personal Work provides a dedicated local-only Work Order per [Workspace Session](workspace-session.md):

- **One per session** — Created on first ad-hoc agent employment when the builder associates a session with Personal Work (or chooses it from the task association prompt).
- **Workspace-local** — Not synced to Jira; not reported to the Orchestrator.
- **Has a task graph** — Agent sessions appear as tasks under Personal Work for uniform tracking in the IDE (same graph model as other WOs).
- **Consumes normal quota** — Agent employment uses the builder's standard [Delegation](delegation.md) token and Access Gateway quota; `sync_scope` affects tracking only, not access control.

Personal Work is distinct from [Workspace-Local Tasks](../work-order-runtime/concepts/workspace-local-tasks.md) under orchestrated WOs: those are sub-work the builder creates while executing a Human Task on an assigned Work Order. Personal Work is the catch-all when work is not associated with any assigned task.

## Where it lives in Foundry

| Module | Responsibility |
|--------|----------------|
| **WO Runtime** | Creates and maintains the Personal Work WO; stores tasks and agent sessions locally |
| **IDE** | Shows Personal Work in the Work Orders sidebar with a local-only indicator; Employed Agents panel lists agents under Personal Work |
| **Local State Store** | Persists Personal Work WO and its task tree across session restarts |

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Work Order](work-order.md) | Personal Work is a WO shape scoped to the session, not the work repository |
| [Workspace Session](workspace-session.md) | Personal Work exists only for the lifetime of one session |
| Human–Agent Team | Builder employs agents under Personal Work without a Scenario ingress contract |

Personal Work does not replace orchestrated work. It complements assigned WOs by giving builders a sanctioned place for unstructured agent use without polluting Jira or OI progress.

## Related concepts

- [Work Order](work-order.md) — Orchestrated execution instances (synced)
- [Task](task.md) — Units of work; Personal Work accumulates local task nodes for agent sessions
- [Workspace Session](workspace-session.md) — Session boundary for Personal Work
- [Workspace-Local Tasks](../work-order-runtime/concepts/workspace-local-tasks.md) — Local tasks under assigned WOs
- [Agent Employment](../ide/concepts/agent-employment.md) — How builders associate agent sessions with Personal Work

## Further reading

- [../work-order-runtime/concepts/workspace-local-tasks.md](../work-order-runtime/concepts/workspace-local-tasks.md) — Local task mechanism
- [../ide/concepts/agent-employment.md](../ide/concepts/agent-employment.md) — Task association prompt and Personal Work fallback
- [../ide/platform-developer-guide/ux-requirements.md](../ide/platform-developer-guide/ux-requirements.md) — IDE UX for Personal Work in the sidebar
