# Release Tools — Foundry Platform developer guide

This guide contains implementation specifications for engineers building the **Release Tools** components of the Foundry Platform.

## Implementation overview

Release Tools provides CI/CD pipelines with embedded agents, CD integrations, distribution stores, and tool integrations. Agent lifecycle in CI is owned by Release Tools, not Work Order Runtime.

## ACE alignment

| ACE concept | How this module realizes it |
|-------------|----------------------------|
| [Release Workspace](../../ace/workspaces/release.md) | Release Tools operationalizes the Release Workspace |
| [Build Track](../../ace/concepts.md) | CI pipelines serve the Build Track |
| [Governance](../../ace/governance.md) | Quality gates in pipelines invoke Governance Scenarios |

## Specification index

| Document | Scope |
|----------|-------|
| [ci-agent-architecture.md](ci-agent-architecture.md) | CI agent harness — independent of WO Runtime |
| [ci/README.md](ci/README.md) | Foundry CI documentation |
| [ci/ci.TODO](ci/ci.TODO) | CI backlog |

## Dependencies

| Module / foundation | Integration |
|---------------------|-------------|
| [Management](..//management/platform-developer-guide/validation/) | Foundry config validation (not CI) |
| [Work Order Runtime](..//work-order-runtime/platform-developer-guide/) | Work Order execution (separate from CI agents) |

## Related documentation

- [Module concepts](../README.md) — scope, boundaries, and documentation index
- [Release Tools user guide](../user-guide/) — links to Web App persona guides
- [Foundry Platform README](../../README.md) — platform-wide module map and spec authoring rules
