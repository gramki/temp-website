# Trained Agent

A Trained Agent is a declarative manifest that binds a Raw Agent to a specific Swarm with configured skills, guardrails, and evaluation criteria. Each Trained Agent has a Service Principal identity expressed as a Jabber JID.

## What it is

Trained Agents represent the configuration layer of Foundry's three-tier agent model. They are configuration, not running processes — YAML manifests stored in `swarms/` directories that define how an agent should behave.

A Trained Agent manifest specifies:

- **Raw Agent reference** — Which OCI-packaged agent system to use, by registry URI and version
- **Swarm membership** — The Swarm this agent belongs to (exactly one)
- **Identity** — Service Principal JID: `{agent}@{swarm}.agents.{tenant}.foundry.io`
- **Skills** — References to skill packages from the registry (by name and version)
- **Guardrails** — Behavioral constraints (prohibitions, requirements, limits, scope restrictions)
- **Evaluation criteria** — Metrics and golden datasets for measuring agent performance

```yaml
name: feature-implementer
swarm: build-swarm
raw-agent-ref: registry.foundry.io/raw-agents/codex:v2.4.1
identity:
  jid: feature-implementer@build-swarm.agents.acme.foundry.io
skills:
  - name: code-generator
    version: ^2.1.0
guardrails:
  - no-force-push
  - require-tests-for-new-code
```

### Swarm Membership

Every Trained Agent belongs to exactly one Swarm. The Swarm determines the agent's organizational context, governance policies, and discoverability. Scenarios reference Swarms rather than individual Trained Agents; the coordinator agent is always explicitly specified.

### Identity Model

Each Trained Agent has a Service Principal identity using Jabber JID notation:

```
{agent}@{swarm}.agents.{tenant}.foundry.io
```

| Component | Example | Description |
|-----------|---------|-------------|
| `{agent}` | `feature-implementer` | Agent name (unique within Swarm) |
| `{swarm}` | `build-swarm` | Swarm the agent belongs to |
| `{tenant}` | `acme` | Tenant organization |

The JID is the agent's persistent identity in the management plane. When a Trained Agent is instantiated as an Employed Agent, the JID is paired with a Delegation Token to form the runtime identity.

### Distribution Model

Trained Agents follow a two-layer model that mirrors Swarm distribution:

| Layer | Description |
|-------|-------------|
| **Platform-shipped** | Standard Trained Agents in platform-shipped Swarms |
| **Tenant-added** | Tenant-created agents in tenant or platform Swarms |

Tenants can extend platform-shipped Swarms by adding Trained Agents with tenant-specific skills and guardrails.

## Where it lives in Foundry

| Component | Responsibility |
|-----------|----------------|
| **Swarm `swarms/` folder** | Stores Trained Agent manifests alongside Swarm definition |
| **Swarm Registry** (Agent Fabric) | Indexes Trained Agent metadata for discovery |
| **Metadata Service** | Serves Trained Agent definitions at runtime |
| **WO Runtime** | Reads manifest, resolves Raw Agent, spawns Employed Agent |

Folder structure within Swarms:

```
swarms/
└── build-swarm/
    ├── swarm.yaml                    # Swarm definition
    └── trained-agents/
        ├── feature-implementer.yaml  # Trained Agent manifest
        ├── code-refactorer.yaml
        └── test-writer.yaml
```

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Agent](../../../ace/concepts.md) | Trained Agent configures how capabilities are applied |
| [Skill](../../../ace/concepts.md) | Skills referenced by name from Skill Registry |
| Guardrail | Behavioral constraints defined per Trained Agent |

Trained Agents bridge the gap between generic agent packaging (Raw Agents) and specific work contexts (Scenarios via Swarm membership). They apply ACE's concept of agent configuration to Foundry's operational model.

## Related concepts

- [Agent Model](../../concepts/agent-model.md) — Three-tier hierarchy that includes Trained Agents
- [Raw Agent](raw-agent.md) — OCI containers that Trained Agents reference
- [Swarm](swarm.md) — Organizational unit that contains Trained Agents
- [Employed Agent](employed-agent.md) — Runtime instances spawned from Trained Agent definitions
- [Skill](../../concepts/skill.md) — Capability packages that Trained Agents reference
- [Scenario](../../concepts/scenario.md) — Work contracts that reference Swarms containing Trained Agents

## Further reading

- [../platform-developer-guide/trained-agents.md](../platform-developer-guide/trained-agents.md) — Schema reference, guardrails, evaluation
- [../user-guide/trained-agents.md](../user-guide/trained-agents.md) — How to create Trained Agent manifests
- [../platform-developer-guide/skill-registry.md](../platform-developer-guide/skill-registry.md) — Skill packaging and publishing
- [../platform-developer-guide/swarm-registry.md](../platform-developer-guide/swarm-registry.md) — Swarm registration and discovery
