# Release Tools Concepts

This folder contains module-specific concept definitions for Release Tools. Each concept file provides a single authoritative definition within the Release Tools domain, linking back to platform-wide concepts where appropriate.

## How to use these concepts

- **Reference, don't duplicate.** Link to these definitions rather than restating them in module docs.
- **Module-specific scope.** These concepts are Release Tools-specific specializations; platform-wide concepts live in [`../concepts/`](../../concepts/).
- **Implementation details elsewhere.** Concepts are definitions; implementation specs live in `platform-developer-guide/`.

## Concept Index

| Concept | Definition |
|---------|------------|
| [CI Agent Harness](ci-agent-harness.md) | Job-scoped, ephemeral agent execution environment for CI pipelines |
| [CI Delegation Token](ci-delegation-token.md) | Pipeline-identity-scoped authority token for CI agent actions |
| [Quality Gates](quality-gates.md) | Governance checkpoints embedded in CI pipelines |

## Relationship to Platform Concepts

These module concepts specialize and extend platform-wide concepts:

| Platform Concept | Release Tools Specialization |
|------------------|------------------------------|
| [Delegation](../../concepts/delegation.md) | CI Delegation Token adapts delegation for pipeline identity |
| [Governance](../../concepts/governance.md) | Quality Gates invoke governance within pipelines |
| [Agent Model](../../concepts/agent-model.md) | CI Agent Harness spawns agents outside WO Runtime |
| [Workspace Session](../../concepts/workspace-session.md) | CI uses ephemeral runner workspaces, not Coder Sessions |

## Key Distinction: CI vs WO Runtime

Release Tools operates agents independently from Work Order Runtime:

| Aspect | WO Runtime | Release Tools CI |
|--------|------------|------------------|
| **Trigger** | Jira WO assignment | Code events (commit, PR) |
| **Scope** | Session-scoped | Job-scoped |
| **Lifecycle** | Long-running daemon | Ephemeral per step |
| **Identity** | Human session owner | Pipeline service account |

This separation is intentional — CI agents have different triggers, lifecycles, and identity models than Work Order execution agents.

## Read next

- [ci-agent-harness.md](ci-agent-harness.md) — How agents run in pipelines
- [ci-delegation-token.md](ci-delegation-token.md) — Pipeline identity and authority
- [quality-gates.md](quality-gates.md) — Governance in CI
- [../../concepts/README.md](../../concepts/README.md) — Platform-wide concepts
