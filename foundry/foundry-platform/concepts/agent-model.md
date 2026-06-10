# Agent Model

The Agent Model is the three-tier hierarchy that defines how agents are managed in Foundry: Raw Agents (packaging-layer OCI containers), Trained Agents (configuration-layer manifests organized in Swarms), and Employed Agents (runtime instances with delegated authority).

## What it is

Foundry's agent model separates concerns across three layers:

```
┌─────────────────────────────────────────────────────────────────┐
│  Packaging Layer                                                 │
│  Raw Agent: OCI container (Codex, Cursor Agent, Claude Code)    │
│  URI: registry.foundry.io/raw-agents/{agent}:{version}          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ referenced by
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Configuration Layer                                             │
│  Trained Agent: Manifest with skills, guardrails, Swarm member  │
│  JID: {agent}@{swarm}.agents.{tenant}.foundry.io                │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ instantiated as
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Runtime Layer                                                   │
│  Employed Agent: Trained Agent + Delegation Token               │
│  (Delegated authority, quota-bound, session-scoped)             │
└─────────────────────────────────────────────────────────────────┘
```

### Raw Agent

An OCI container that packages an agent system — the deployable "engine" defining what an agent *can* do structurally. Examples: Codex, Cursor Agent, Claude Code.

Raw Agents are managed by the Raw Agent Registry in Agent Fabric. The registry stores:

- OCI image references and metadata
- Agent system identity, provider, and version
- Supported interfaces (app-server, agent-server, SDK, API, CLI)
- Deployment modes (container runtime, workspace program)
- Default models and capability requirements

Raw Agents follow a two-layer distribution model: platform-shipped (`registry.foundry.io/raw-agents/...`) and tenant-added (`registry.{tenant}.foundry.io/raw-agents/...`).

### Trained Agent

A manifest (YAML) within a Swarm's `trained-agents/` folder that defines:

- Which Raw Agent to use (by OCI URI reference)
- Which Skills the agent should have
- Guardrails and constraints
- JID identity: `{agent}@{swarm}.agents.{tenant}.foundry.io`

Trained Agents belong to exactly one [Swarm](../agent-fabric/concepts/swarm.md) — an organizational unit that groups agents by function. They are configuration, not running processes.

### Employed Agent

A running agent instance within a [Workspace Session](workspace-session.md), spawned by WO Runtime:

- Has a [Delegation](delegation.md) token (OAuth Access Token from workspace owner)
- Is bound by quota limits
- Is scoped to the Workspace Session, Work Order, and Task
- Executes [Tasks](task.md) from the Work Order

Each Scenario invocation gets its own Employed Agent. The identity at runtime is the Trained Agent's JID combined with the Delegation Token.

### Swarm

An organizational unit (OU) for Trained Agents — a named grouping that organizes agents by function, team, or purpose. Swarms have no lifecycle states; they simply contain members. They are scoped at Foundry, Workshop, Workbench, or Workspace level.

Scenarios reference Swarms rather than individual agents, with a coordinator agent explicitly specified.

## Where it lives in Foundry

| Concept | Where It Lives | Managed By |
|---------|----------------|------------|
| **Raw Agent** | Raw Agent Registry (OCI catalog) | Agent Fabric |
| **Trained Agent** | `swarms/{swarm}/trained-agents/` manifests | Swarm Registry (Agent Fabric) |
| **Employed Agent** | Workspace Session process | WO Runtime |
| **Swarm** | Swarm Registry + `swarms/` folders at each scope | Agent Fabric |

Agent Fabric provides the infrastructure; WO Runtime spawns the instances:

```
Agent Fabric                     WO Runtime
┌─────────────────────┐         ┌─────────────────────────────┐
│ Raw Agent Registry  │         │ 1. Resolve Swarms from      │
│                     │         │    Scenario                  │
│ Swarm Registry      │──────────│ 2. Load Trained Agent       │
│                     │         │    manifest from Swarm       │
│ Skill Registry      │──────────│ 3. Resolve Raw Agent        │
│                     │         │ 4. Install Skills            │
│ Gateway Policy      │──────────│ 5. Spawn Employed Agent     │
│ (quota, routing)    │         │    with Delegation Token     │
└─────────────────────┘         └─────────────────────────────┘
```

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Agent](../../ace/concepts.md#human-agent-team) | Three-tier model (Raw, Trained, Employed) |
| Human–Agent Team | Employed Agents work alongside humans in Sessions |
| Team | Swarms organize agents analogously to human OUs |
| Workforce Repository | Stores agent identities, role bindings, governance |

From ACE: "A workspace's team is composed of human practitioners and AI agents working on the same scenarios and tasks. Both kinds of participants are members of the Workforce."

UPIM's Workforce Repository tracks both human and AI agents with role bindings, skills, availability, and governance. The Agent Model operationalizes this for AI participants. Swarms provide the organizational structure for agent teams, paralleling human OUs.

## Related concepts

- [Skill](skill.md) — Capabilities that Trained Agents reference
- [Delegation](delegation.md) — Authority tokens for Employed Agents
- [Workspace Session](workspace-session.md) — Where Employed Agents run
- [Scenario](scenario.md) — References Swarms; defines coordinator agent
- [Task](task.md) — What Employed Agents execute

## Further reading

- [../agent-fabric/README.md](../agent-fabric/README.md) — Agent infrastructure
- [../agent-fabric/concepts/raw-agent.md](../agent-fabric/concepts/raw-agent.md) — Raw Agent concept
- [../agent-fabric/concepts/swarm.md](../agent-fabric/concepts/swarm.md) — Swarm concept
- [../agent-fabric/platform-developer-guide/raw-agents.md](../agent-fabric/platform-developer-guide/raw-agents.md) — Raw Agent OCI specification
- [../agent-fabric/platform-developer-guide/swarm-registry.md](../agent-fabric/platform-developer-guide/swarm-registry.md) — Swarm Registry
- [../agent-fabric/user-guide/trained-agents.md](../agent-fabric/user-guide/trained-agents.md) — Trained Agent manifests
- [../work-order-runtime/README.md](../work-order-runtime/README.md) — Employed Agent spawning
