# Employed Agent

An Employed Agent is the runtime instantiation of a Skilled Agent — a running agent instance within a Workspace Session that holds delegated authority from the session owner and executes tasks on their behalf.

## What it is

Employed Agents represent the runtime layer of Foundry's three-tier agent model. They are what an agent *is doing* right now — an active process that has been spawned by WO Runtime to perform work.

An Employed Agent is bound to three things:

1. **Workspace Session** — The execution environment (Coder workspace)
2. **Session Owner** — The human whose authority is delegated
3. **Work Order / Task** — The specific work being performed

When spawned, the Employed Agent receives a **Delegation Token** that grants:

- Model access via the Gateway Policy Layer
- Tool access to MCP connectors in the workspace
- Repository access for reading and writing code
- Jira access for task management

All actions taken by the Employed Agent are attributed to the session owner. The agent uses the owner's credits and quota, works within the owner's permissions, and creates an audit trail that shows the agent as actor with the human as delegator.

The Employed Agent's role (Peer vs Assistant) depends on the autonomy level defined in its skills:

| Role | Autonomy | Behavior |
|------|----------|----------|
| **Peer** | High | Works independently, reports results |
| **Assistant** | Low | Requires approval for significant actions |

Employed Agents are not persistent identities. They are spun up per Scenario execution with the specific context, skills, and authority needed for that work, and terminate when the work completes or the session closes.

## Where it lives in Foundry

| Component | Responsibility |
|-----------|----------------|
| **Workspace Session** | Process host; provides credentials, tools, files |
| **WO Runtime** | Spawns, monitors, and terminates Employed Agents |
| **Agent Fabric** | Provides token infrastructure, quota enforcement |
| **Gateway Policy Layer** | Validates tokens, enforces quota, routes model calls |
| **Audit System** | Records all delegated actions |

Lifecycle:

```
WO Runtime detects task → Reads Skilled Agent manifest
    → Selects Capable Agent and Model
    → Prepares harness (env, tools, MCP, skills)
    → Spawns agent process with Delegation Token
    → Agent executes skills, calls models via Gateway
    → Task completes → Agent terminates
```

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Agent](../../../ace/concepts.md) | Employed Agent is the runtime participant in human-agent teams |
| [Delegation](../../../ace/concepts.md) | Token-based authority transfer from session owner |
| Human–Agent Team | Employed Agent works alongside humans in Sessions |
| [Task](../../concepts/task.md) | What Employed Agents execute |

From the Workforce Repository (UPIM): delegation rules, escalation chains, and approval authorities are part of the Responsibility Allocation Ledger. Employed Agents operate within these governance constraints.

## Related concepts

- [Agent Model](../../concepts/agent-model.md) — Three-tier hierarchy that includes Employed Agents
- [Capable Agent](capable-agent.md) — Systems that power Employed Agents
- [Skilled Agent](skilled-agent.md) — Manifests that define Employed Agent behavior
- [Delegation](../../concepts/delegation.md) — Authority tokens for Employed Agents
- [Workspace Session](../../concepts/workspace-session.md) — Where Employed Agents run
- [Task](../../concepts/task.md) — What Employed Agents execute

## Further reading

- [../platform-developer-guide/employed-agents.md](../platform-developer-guide/employed-agents.md) — Employment model, lifecycle, attribution
- [../platform-developer-guide/gateway-policy.md](../platform-developer-guide/gateway-policy.md) — Delegation Token handling
- [../../work-order-runtime/platform-developer-guide/agent-spawning.md](../../work-order-runtime/platform-developer-guide/agent-spawning.md) — How Employed Agents are spawned
