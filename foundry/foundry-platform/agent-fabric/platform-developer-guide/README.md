# Agent Fabric — Foundry Platform developer guide

This guide contains implementation specifications for engineers building the **Agent Fabric** components of the Foundry Platform.

## Implementation overview

Agent Fabric provides agent infrastructure — two core registries (Raw Agent Registry and Swarm Registry), Skill Registry, quota enforcement, gateway policy, and usage analytics. It provides policy, configuration, and organizational structure; WO Runtime spawns and executes agents.

## ACE alignment

| ACE concept | How this module realizes it |
|-------------|----------------------------|
| [Agent](../../ace/concepts.md) | Manages Raw Agent, Trained Agent, Employed Agent hierarchy |
| [Skill](../../ace/concepts.md) | Packages capabilities following Agent Skills spec |
| [Scenario](../../ace/concepts.md) | Scenarios reference Swarms containing Trained Agents |

## Specification index

| Document | Scope |
|----------|-------|
| [requirements.md](requirements.md) | Implementation requirements (APIs, database, observability) |
| [skill-registry.md](skill-registry.md) | Skill distribution, packaging, and CLI tooling |
| [raw-agents.md](raw-agents.md) | Raw Agent OCI packaging, interfaces, and deployment modes |
| [raw-agent-registry.md](raw-agent-registry.md) | Raw Agent Registry: two-layer model, discovery, versioning |
| [trained-agents.md](trained-agents.md) | Trained Agent manifests, identity model, Swarm membership |
| [swarm-registry.md](swarm-registry.md) | Swarm Registry: hierarchy, two-layer model, governance |
| [employed-agents.md](employed-agents.md) | Runtime instantiation, JID + Delegation Token, attribution |
| [gateway-policy.md](gateway-policy.md) | OSS gateway configuration and quota enforcement |

## Dependencies

| Module / foundation | Integration |
|---------------------|-------------|
| [Work Order Runtime](../../work-order-runtime/platform-developer-guide/) | Resolves Swarms, spawns Employed Agents using Fabric configuration |
| [Management](../../management/platform-developer-guide/) | Workbench provisioning; registry storage |

## Related documentation

- [Module concepts](../README.md) — scope, boundaries, and documentation index
- [Agent Fabric user guide](../user-guide/) — agent lifecycle, Trained Agents, and Swarms
- [Foundry Platform README](../../README.md) — platform-wide module map and spec authoring rules
