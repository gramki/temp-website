# Foundry IDE — Foundry Platform developer guide

This guide contains implementation specifications for engineers building the **Foundry IDE** components of the Foundry Platform.

## Implementation overview

The Foundry IDE is based on VS Code and provides builder-facing Workspace views plus extensions for Work Order execution UI and Work Catalog authoring. The WO Runtime Plugin surfaces Work Orders, agent chat, and terminal interfaces; the Scenario Editor Extension provides schema-aware YAML editing and catalog publishing integration.

## ACE alignment

| ACE concept | How this module realizes it |
|-------------|----------------------------|
| [Workspace](../../ace/workspaces/README.md) | IDE is the interface to a Workspace |
| [Work Order](../../ace/concepts.md) | Visible and actionable via WO Runtime Plugin |
| [Task](../../ace/concepts.md) | Human Tasks surface in IDE; Agent Tasks are observable |

## Specification index

| Document | Scope |
|----------|-------|
| [extensions.md](extensions.md) | WO Runtime Plugin, Scenario Editor Extension, Publish CLI integration |
| [ux-requirements.md](ux-requirements.md) | IDE UX requirements and Figma mockup frame index (IDE-UX-001+) |

## Dependencies

| Module / foundation | Integration |
|---------------------|-------------|
| [Work Order Runtime](..//work-order-runtime/platform-developer-guide/ide-integration.md) | Plugin architecture and agent UI |
| [Work Catalogues](..//work-catalogues/user-guide/authoring-scenarios.md) | Scenario authoring workflow |
| [Management](..//management/platform-developer-guide/work-catalog-management/) | Scenario and OI Workflow schemas |

## Related documentation

- [Module concepts](../README.md) — scope, boundaries, and documentation index
- [Foundry IDE user guide](../user-guide/) — builder tasks in Workspace Sessions
- [Foundry Platform README](../../README.md) — platform-wide module map and spec authoring rules
