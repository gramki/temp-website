# Release Tools

**Module scope:** CI/CD pipelines with embedded agents, CD integrations, distribution stores, tool integrations.

## What this module does

Release Tools provides the CI/CD layer for Foundry, with agents embedded in pipelines. It provides:

- **CI pipelines** — build, test, verify pipelines with agents embedded
- **Agent-embedded builds** — agents participate in CI as workers (lifecycle managed by CI, not Work Order Runtime)
- **CD integrations** — integration with deployment systems (out of Phase 1 scope for deployment itself)
- **Distribution stores** — publish verified artifacts to distribution stores
- **Tool integrations** — integrate with external CI/CD, testing, and release tools

## ACE concepts realized

- **Release Workspace** — Release Tools operationalizes the Release Workspace
- **Build Track** — CI pipelines serve the Build Track; Release is the Build-Track activity of publishing verified artifacts
- **Governance** — quality gates in pipelines invoke Governance Scenarios

## What this module does NOT do

| Boundary | Owned by |
|----------|----------|
| Foundry config / Work Catalog validation | Management → Validation module |
| Work Order execution | Work Order Runtime |
| Orchestration item routing | Orchestrator |

## Key design decisions

- **Agent lifecycle in CI is owned by CI.** Work Order Runtime owns agent lifecycle for Work Order execution; Release Tools (CI) owns it for pipeline-embedded agents.
- **Integrations are owned by this module.** CI/CD/distribution integrations live here, not in a horizontal "Integrations" module.
- **Release ≠ Deployment.** Release is publishing verified artifacts (Build Track). Deployment is Run Track work and out of Phase 1 scope.

## Key Concepts

### Platform-wide concepts

| Concept | What Release Tools does with it |
|---------|--------------------------------|
| [Delegation](../concepts/delegation.md) | Issues CI Delegation Tokens for pipeline identity |
| [Governance](../concepts/governance.md) | Invokes quality gates at pipeline checkpoints |
| [Agent Model](../concepts/agent-model.md) | Spawns agents in CI pipelines (outside WO Runtime) |
| [Workspace Session](../concepts/workspace-session.md) | Uses ephemeral runner workspaces, not Coder Sessions |

### Module-specific concepts

| Concept | Definition |
|---------|------------|
| [CI Agent Harness](concepts/ci-agent-harness.md) | Job-scoped, ephemeral agent execution environment |
| [CI Delegation Token](concepts/ci-delegation-token.md) | Pipeline-identity-scoped authority token |
| [Quality Gates](concepts/quality-gates.md) | Governance checkpoints in CI pipelines |

→ [concepts/README.md](concepts/README.md) — Full module concept index

## Open questions

- Agent embedding in CI — how are agents invoked in pipeline steps?
- Quality gate mechanics — blocking vs advisory
- Artifact signing and provenance
- Distribution store targets

## Documentation

| Guide | Audience | Index |
|-------|----------|-------|
| [Concepts](concepts/) | Anyone | Module-specific concept definitions |
| [User guide](user-guide/) | Admins, builders | Task-oriented usage |
| [Foundry Platform developer guide](platform-developer-guide/) | Platform engineers | Implementation specs |

## Read next

- [platform-developer-guide/ci/README.md](platform-developer-guide/ci/README.md) — Foundry CI documentation
- [user-guide/README.md](user-guide/README.md) — links to Web App persona guides for release workflows
- [../../ace/workspaces/release.md](../../ace/workspaces/release.md) — Release Workspace definition
- [../../tldr-faq.md](../../tldr-faq.md) — release tools design decisions
