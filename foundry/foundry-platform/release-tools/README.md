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

## CI folder

The [ci/](ci/README.md) folder contains Foundry CI documentation. Release Tools subsumes and extends that work:

- Evidence packs
- Test runners and reports
- Build Quality Indicators (BQI)
- Tech debt management
- Agentic quality gates
- MS Teams integration
- TestRail support

## Key design decisions

- **Agent lifecycle in CI is owned by CI.** Work Order Runtime owns agent lifecycle for Work Order execution; Release Tools (CI) owns it for pipeline-embedded agents.
- **Integrations are owned by this module.** CI/CD/distribution integrations live here, not in a horizontal "Integrations" module.
- **Release ≠ Deployment.** Release is publishing verified artifacts (Build Track). Deployment is Run Track work and out of Phase 1 scope.

## Open questions

- Agent embedding in CI — how are agents invoked in pipeline steps?
- Quality gate mechanics — blocking vs advisory
- Artifact signing and provenance
- Distribution store targets

## Read next

- [../ci/](../ci/README.md) — existing CI documentation
- [../../ace/workspaces/release.md](../../ace/workspaces/release.md) — Release Workspace definition
- [../../tldr-faq.md](../../tldr-faq.md) — release tools design decisions
