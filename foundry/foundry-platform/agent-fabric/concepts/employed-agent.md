# Employed Agent

An Employed Agent is the runtime instantiation of a Trained Agent — a running agent instance within a Workspace Session that holds a JID (Service Principal) paired with a Delegation Token from the workspace owner, executing tasks on their behalf.

## What it is

Employed Agents represent the runtime layer of Foundry's three-tier agent model. They are what an agent *is doing* right now — an active process that has been spawned by WO Runtime to perform work.

An Employed Agent is bound to four things:

1. **Trained Agent JID** — The Service Principal identity: `{agent}@{swarm}.agents.{tenant}.foundry.io`
2. **Delegation Token** — OAuth Access Token from the workspace owner, granting scoped authority
3. **Workspace Session** — The execution environment (Coder workspace)
4. **Work Order / Task** — The specific work being performed

### Identity Model

The Employed Agent's identity combines two elements:

| Element | Type | Source |
|---------|------|--------|
| **JID** | Service Principal | From the Trained Agent manifest; persistent identity in the management plane |
| **Delegation Token** | OAuth Access Token | Issued at spawn time from the workspace owner's authority; scoped and ephemeral |

The JID identifies *who* the agent is. The Delegation Token authorizes *what* the agent can do.

When spawned, the Delegation Token grants:

- Model access via the Gateway Policy Layer
- Tool access to MCP connectors in the workspace
- Repository access for reading and writing code
- Jira access for task management

All actions taken by the Employed Agent are attributed to the session owner. The agent uses the owner's credits and quota, works within the owner's permissions, and creates an audit trail that shows the JID as actor with the human as delegator.

### Quotas

Quotas are enforced at the Employed Agent level, with aggregate limits at higher scopes:

| Scope | Limit Type | Description |
|-------|------------|-------------|
| **Employed Agent** | Per-instance | Token budget, cost cap, duration |
| **Workbench** | Aggregate | Combined limit across all Employed Agents in Workbench |
| **Workshop** | Aggregate | Combined limit across all Workbenches |
| **Foundry** | Aggregate | Tenant-wide limit |

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
| **Gateway Policy Layer** | Validates JID + Delegation Token, enforces quota, routes model calls |
| **Audit System** | Records all delegated actions with JID attribution |

Lifecycle:

```
WO Runtime detects task → Resolves Swarm and coordinator agent
    → Loads Trained Agent manifest from swarms/{swarm}/trained-agents/
    → Resolves Raw Agent from raw-agent-ref
    → Prepares harness (env, tools, MCP, skills)
    → Spawns agent process with JID + Delegation Token
    → Agent executes skills, calls models via Gateway
    → Task completes → Agent terminates
```

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Agent](../../../ace/concepts.md) | Employed Agent is the runtime participant in human-agent teams |
| [Delegation](../../../ace/concepts.md) | OAuth Access Token from session owner scoped to workspace authority |
| Human–Agent Team | Employed Agent works alongside humans in Sessions |
| [Task](../../concepts/task.md) | What Employed Agents execute |

From the Workforce Repository (UPIM): delegation rules, escalation chains, and approval authorities are part of the Responsibility Allocation Ledger. Employed Agents operate within these governance constraints.

## Related concepts

- [Agent Model](../../concepts/agent-model.md) — Three-tier hierarchy that includes Employed Agents
- [Raw Agent](raw-agent.md) — OCI containers that power Employed Agents
- [Trained Agent](trained-agent.md) — Manifests that define Employed Agent behavior and JID
- [Swarm](swarm.md) — Organizational unit whose members become Employed Agents
- [Delegation](../../concepts/delegation.md) — Authority tokens for Employed Agents
- [Workspace Session](../../concepts/workspace-session.md) — Where Employed Agents run
- [Task](../../concepts/task.md) — What Employed Agents execute

## Further reading

- [../platform-developer-guide/employed-agents.md](../platform-developer-guide/employed-agents.md) — Employment model, lifecycle, attribution
- [../platform-developer-guide/gateway-policy.md](../platform-developer-guide/gateway-policy.md) — Delegation Token handling
- [../../work-order-runtime/platform-developer-guide/agent-spawning.md](../../work-order-runtime/platform-developer-guide/agent-spawning.md) — How Employed Agents are spawned
