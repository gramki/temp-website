# Capable Agent

A Capable Agent is a whitelisted agent system with orchestration, tool use, context management, and swarm capabilities — the "engine" that defines what an agent *can* do structurally.

## What it is

Capable Agents represent the platform layer of Foundry's three-tier agent model. They are the underlying agent systems that provide core capabilities for agentic work: Cursor Agent, GitHub Copilot, Claude Code, Codex CLI, and others.

Unlike models (which are the LLMs that power reasoning), Capable Agents are agent *systems* that orchestrate model calls, manage context, use tools, and coordinate complex tasks. A single Capable Agent may support multiple models:

```
Capable Agent: Cursor Agent
├── Model: claude-opus
├── Model: claude-sonnet
└── Model: gpt-5
```

Capable Agents are managed in a registry at the Foundry level, with enable/disable and credential configuration cascading through the containment hierarchy (Foundry → Workshop → Workbench). Disabling at a level cascades down; enabling requires the parent to be enabled. Credentials are resolved from the lowest level up — Workbench credentials override Workshop, which override Foundry.

The registry stores:

- Agent system identity, provider, and version
- Supported interfaces (app-server, agent-server, SDK, API, CLI)
- Default models and configurations
- Credential references (resolved from secrets store)
- Enable/disable state per scope

## Where it lives in Foundry

| Component | Responsibility |
|-----------|----------------|
| **Capable Agent Registry** (Agent Fabric) | Stores whitelist and configuration |
| **Foundry Definition Repo** | Source of truth for Foundry-level config |
| **Workshop Definition Repo** | Workshop and Workbench overrides |
| **Gateway Policy Layer** | Resolves credentials at request time |
| **WO Runtime** | Queries registry when spawning agents |

Configuration hierarchy:

| Level | Configuration | Examples |
|-------|---------------|----------|
| **Foundry** | Master whitelist, org-wide credentials | Enable Cursor Agent for entire org |
| **Workshop** | Team-specific overrides, billing keys | Disable Copilot for compliance team |
| **Workbench** | Product-specific credentials | Project-specific API key |

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Agent](../../../ace/concepts.md) | Capable Agent is the platform-layer realization |
| Workforce Repository | Registry stores agent identities and configurations |

Capable Agents operationalize the ACE concept of "agent" at the platform layer. ACE describes agents as participants in human-agent teams; Capable Agents are the specific systems Foundry supports for this role.

## Related concepts

- [Agent Model](../../concepts/agent-model.md) — Three-tier hierarchy that includes Capable Agents
- [Skilled Agent](skilled-agent.md) — Manifests that reference Capable Agents
- [Employed Agent](employed-agent.md) — Runtime instances of Capable Agents
- [Delegation](../../concepts/delegation.md) — Authority granted via Capable Agent's gateway

## Further reading

- [../platform-developer-guide/capable-agents.md](../platform-developer-guide/capable-agents.md) — Registry schema, interfaces, candidate evaluation
- [../platform-developer-guide/gateway-policy.md](../platform-developer-guide/gateway-policy.md) — Credential resolution and policy enforcement
- [../../work-order-runtime/platform-developer-guide/agent-spawning.md](../../work-order-runtime/platform-developer-guide/agent-spawning.md) — How Capable Agents are spawned
