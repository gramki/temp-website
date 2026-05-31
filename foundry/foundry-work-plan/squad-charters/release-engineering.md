# Squad Charter — Release Engineering

**Stream:** Release Engineering  
**Squad lead:** TBD

## Purpose

Build and own **CI pipelines and release mechanics** for product repositories: Foundry CI, GitHub integration for build/test on Development Work Orders, and release package artifacts for Release Work Orders. This stream does not define what Work Orders mean — that is Work Catalog Authoring.

## Boundaries

### In scope

- [Release Tools](../../foundry-platform/release-tools/README.md) — Foundry CI, pipeline-embedded agents (minimal Phase 1)
- GitHub integration behavior for product repos (PR checks, merge policies) aligned with [git-infrastructure](../../foundry-platform/management/platform-developer-guide/git-infrastructure.md)
- Release package artifact format consumed by Release station WOs

### Out of scope

- Work Catalog workflows and scenarios — [Work Catalog Authoring](work-catalog-authoring.md)
- Orchestrator / OI lifecycle — Control Plane
- WO Runtime session execution — Execution Plane
- Full CD / deployment to environments (Run track deferred)
- Olympus Weave integration (deferred per phase-1-scope)

## Phase 1 deliverables

| Milestone | Deliverable |
|-----------|-------------|
| M2 | CI runs on Development WO implementation PR (build + test) |
| M4 | Release package artifact produced; linked to Product Intent traceability |
| M5 | CI stable for demo; no manual pipeline triggers mid-demo |

## Dependencies

| Depends on | For |
|------------|-----|
| Execution Plane | PR exists from Development WO Git workflow |
| Control Plane | Workbench GitHub App installation |
| Work Catalog Authoring | Release scenarios define what "package" means |

## Interfaces

See [../integration/contract-gates.md](../integration/contract-gates.md). This stream **produces**:

- CI status webhooks / checks on product repo PRs
- Release package artifact reference (URL or registry ID)

This stream **consumes**:

- Git push/PR events from WO Runtime
- Workbench/repo configuration from Management

## Backlog themes

- Foundry CI: [release-tools/platform-developer-guide/ci/](../../foundry-platform/release-tools/platform-developer-guide/ci/README.md)
- PR gate integration with Development WO completion
- Release artifact layout for `prepare-customer-release` scenario outputs
- Pipeline agent lifecycle (context-dependent per tldr-faq — owned here for CI)

## Read next

- [../milestones.md](../milestones.md)
- [../phase-1/phase-1-scope.md](../phase-1/phase-1-scope.md) — integrations table
- [../../foundry-platform/release-tools/README.md](../../foundry-platform/release-tools/README.md)
