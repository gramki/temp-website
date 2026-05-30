# Foundry Platform Admin Web App — Foundry Platform developer guide

This guide contains UI specifications for engineers building the **Foundry Platform Admin Web App**.

## Implementation overview

The Platform Admin Web App is a dedicated super-admin interface for managing the entire Foundry Platform — Foundry creation, infrastructure monitoring, and platform-level settings. It is deployed separately from Foundry Web Apps.

## Specification index

| Document | Scope |
|----------|-------|
| [pages/dashboard.md](pages/dashboard.md) | Platform health overview, alerts |
| [pages/foundries.md](pages/foundries.md) | List and create Foundries |
| [pages/foundry-detail.md](pages/foundry-detail.md) | Single Foundry management |
| [pages/infrastructure.md](pages/infrastructure.md) | Database and storage monitoring |
| [pages/platform-settings.md](pages/platform-settings.md) | Global configuration |

## Dependencies

| Module / foundation | Integration |
|---------------------|-------------|
| [Management](..//management/platform-developer-guide/foundry-management/) | Foundry lifecycle APIs |
| [Foundry Web App](..//foundry-web-app/platform-developer-guide/) | Shared component library |

## Related documentation

- [Module concepts](../README.md) — scope, boundaries, and documentation index
- [Platform Admin user guide](../user-guide/) — Platform Admin persona
- [Foundry Platform README](../../README.md) — platform-wide module map and spec authoring rules
