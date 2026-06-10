# Raw Agent

A Raw Agent is an OCI container that packages an agent system with its orchestration, tool use, context management, and swarm capabilities — the deployable "engine" that defines what an agent *can* do structurally.

## What it is

Raw Agents represent the packaging layer of Foundry's three-tier agent model. They are OCI containers that bundle agent systems for deployment: Codex, Cursor Agent, Claude Code, and others. The OCI format serves as the universal packaging standard, enabling consistent deployment whether the target is a container runtime or a Coder workspace program.

Unlike models (which are the LLMs that power reasoning), Raw Agents are agent *systems* that orchestrate model calls, manage context, use tools, and coordinate complex tasks. A single Raw Agent may support multiple models:

```
Raw Agent: registry.foundry.io/raw-agents/codex:v2.4.1
├── Model: codex-3
├── Model: gpt-5
└── Model: gpt-5-thinking

Raw Agent: registry.foundry.io/raw-agents/cursor-agent:v1.2.0
├── Model: claude-opus
├── Model: claude-sonnet
└── Model: gpt-5
```

Raw Agents are distributed through registries in a two-layer model:

| Layer | Registry URI | Managed By |
|-------|--------------|------------|
| **Platform-shipped** | `registry.foundry.io/raw-agents/{agent}:{version}` | Foundry Platform |
| **Tenant-added** | `registry.{tenant}.foundry.io/raw-agents/{agent}:{version}` | Tenant Organization |

The OCI manifest inside each container declares:

- Agent system identity, provider, and version
- Supported interfaces (app-server, agent-server, SDK, API, CLI)
- Deployment modes (container runtime, workspace program)
- Default models and capability requirements
- Resource requirements (CPU, memory, GPU)

## Where it lives in Foundry

| Component | Responsibility |
|-----------|----------------|
| **Raw Agent Registry** (Agent Fabric) | Stores OCI references and metadata |
| **OCI Container Registry** | Stores actual container images |
| **Foundry Definition Repo** | Source of truth for platform-shipped agents |
| **Gateway Policy Layer** | Resolves credentials at request time |
| **WO Runtime** | Pulls OCI image and spawns agent |

Distribution hierarchy:

| Source | Visibility | Examples |
|--------|------------|----------|
| **Platform-shipped** | All tenants | Codex, Cursor Agent, Claude Code |
| **Tenant-added** | Organization only | Custom agents, internal tooling |

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Agent](../../../ace/concepts.md) | Raw Agent is the packaging-layer realization |
| Workforce Repository | Raw Agent Registry stores OCI references and metadata |

Raw Agents operationalize the ACE concept of "agent" at the packaging layer. ACE describes agents as participants in human-agent teams; Raw Agents are the deployable containers Foundry supports for this role.

## Related concepts

- [Agent Model](../../concepts/agent-model.md) — Three-tier hierarchy (Raw, Trained, Employed)
- [Trained Agent](trained-agent.md) — Manifests that reference Raw Agents with skills and guardrails
- [Employed Agent](employed-agent.md) — Runtime instances spawned from Trained Agents
- [Swarm](swarm.md) — Organizational unit that contains Trained Agents
- [Delegation](../../concepts/delegation.md) — Authority granted when Raw Agent becomes Employed

## Further reading

- [../platform-developer-guide/raw-agents.md](../platform-developer-guide/raw-agents.md) — OCI manifest specification, interfaces, deployment modes
- [../platform-developer-guide/raw-agent-registry.md](../platform-developer-guide/raw-agent-registry.md) — Registry API, two-layer model, discovery
- [../platform-developer-guide/gateway-policy.md](../platform-developer-guide/gateway-policy.md) — Credential resolution and policy enforcement
- [../../work-order-runtime/platform-developer-guide/agent-spawning.md](../../work-order-runtime/platform-developer-guide/agent-spawning.md) — How Raw Agents are spawned
