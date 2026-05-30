# Release Tools user guide

Release workflows for builders and release teams are documented in the Foundry Web App persona guides and the Build consoles rather than duplicated here.

## Audience

| Role | Primary interest |
|------|------------------|
| Release Teams | CI/CD status, release pipelines, artifact management, evidence packs |
| Developers | Build quality indicators, pipeline results, CI integration |
| Program Managers | Release progress tracking, release blockers |

## Guide contents

Release Tools user documentation is organized by persona and console:

### Persona guides (task-oriented)

| Persona | Primary tasks | Guide |
|---------|---------------|-------|
| **Release Teams** | Monitor pipelines, review evidence, publish artifacts | [Release Teams](../../foundry-web-app/user-guide/personas/release-teams/README.md) |
| **Developers** | View CI results, build quality, pipeline status | [Developers](../../foundry-web-app/user-guide/personas/developers/README.md) |
| **QA Teams** | Test results integration, quality status | [Quality Teams](../../foundry-web-app/user-guide/personas/quality-teams/README.md) |

### Web App consoles (UI reference)

| Console | Purpose | Spec |
|---------|---------|------|
| **CI Console** | Pipeline visualization, job progress, failure triage | [ci-console.md](../../foundry-web-app/platform-developer-guide/pages/consoles/build/ci-console.md) |
| **Quality Status** | Test results, coverage, BQI trends | [quality-status.md](../../foundry-web-app/platform-developer-guide/pages/consoles/build/quality-status.md) |
| **Release Artifacts** | Artifact inventory, provenance, publishing | [release-artifacts.md](../../foundry-web-app/platform-developer-guide/pages/consoles/build/release-artifacts.md) |
| **Findings Console** | Security findings, lint results, static analysis | [findings-console.md](../../foundry-web-app/platform-developer-guide/pages/consoles/build/findings-console.md) |
| **Components Console** | Component registry, dependency tracking | [components-console.md](../../foundry-web-app/platform-developer-guide/pages/consoles/build/components-console.md) |

## Quick start paths

**"I need to check why a build failed"**
→ [CI Console](../../foundry-web-app/platform-developer-guide/pages/consoles/build/ci-console.md) → Find job → View logs

**"I need to prepare a release"**
→ [Release Teams guide](../../foundry-web-app/user-guide/personas/release-teams/README.md) → J3: Review evidence packs → J4: Publish artifacts

**"I need to understand test coverage"**
→ [Quality Status console](../../foundry-web-app/platform-developer-guide/pages/consoles/build/quality-status.md)

## Related documentation

- [Module concepts](../README.md) — Release Tools scope and boundaries
- [Foundry Platform developer guide](../platform-developer-guide/) — CI implementation specs
- [CI Agent Architecture](../platform-developer-guide/ci-agent-architecture.md) — How CI agents differ from WO Runtime agents
- [Foundry Web App user guide](../../foundry-web-app/user-guide/) — All persona guides
- [ACE](../../ace/README.md) — Build Track and Release concepts
