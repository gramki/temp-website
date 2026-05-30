# Agent Fabric — Foundry Platform developer guide

This guide contains implementation specifications for engineers building the **Agent Fabric** components of the Foundry Platform.

## Implementation overview

Agent Fabric provides agent infrastructure — Skill Registry, Capable Agent management, quota enforcement, gateway policy, and usage analytics. It provides policy and configuration; WO Runtime spawns and executes agents.

## ACE alignment

| ACE concept | How this module realizes it |
|-------------|----------------------------|
| [Agent](../../ace/concepts.md) | Manages Capable Agent, Skilled Agent, Employed Agent hierarchy |
| [Skill](../../ace/concepts.md) | Packages capabilities following Agent Skills spec |
| [Scenario](../../ace/concepts.md) | Skilled Agents are defined per (Workspace, Scenario) |

## Specification index

| Document | Scope |
|----------|-------|
| [requirements.md](requirements.md) | Implementation requirements (APIs, database, observability) |
| [skill-registry.md](skill-registry.md) | Skill distribution, packaging, and CLI tooling |
| [capable-agents.md](capable-agents.md) | Capable Agent registry, fallback, credentials |
| [employed-agents.md](employed-agents.md) | Runtime instantiation and delegation model |
| [gateway-policy.md](gateway-policy.md) | OSS gateway configuration and quota enforcement |

## Dependencies

| Module / foundation | Integration |
|---------------------|-------------|
| [Work Order Runtime](..//work-order-runtime/platform-developer-guide/) | Spawns Employed Agents using Fabric configuration |
| [Management](..//management/platform-developer-guide/) | Workbench provisioning; agent registry storage |

## Related documentation

- [Module concepts](../README.md) — scope, boundaries, and documentation index
- [Agent Fabric user guide](../user-guide/) — agent lifecycle and Skilled Agents
- [Foundry Platform README](../../README.md) — platform-wide module map and spec authoring rules
