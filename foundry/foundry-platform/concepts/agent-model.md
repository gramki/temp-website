# Agent Model

The Agent Model is the three-tier hierarchy that defines how agents are managed in Foundry: Capable Agents (platform-level systems), Skilled Agents (definition-level manifests), and Employed Agents (runtime instances with delegated authority).

## What it is

Foundry's agent model separates concerns across three layers:

```
┌─────────────────────────────────────────────────────────────────┐
│  Platform Layer                                                  │
│  Capable Agent: Cursor Agent, Copilot, Claude Code, Codex CLI   │
│  (Whitelisted agent systems with orchestration capabilities)    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ configured in
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Definition Layer                                                │
│  Skilled Agent: Local manifest in Workshop/Workbench repo       │
│  (References skills, guardrails, compatible capable agents)     │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ instantiated as
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Runtime Layer                                                   │
│  Employed Agent: Running in Workspace Session                   │
│  (Delegated authority, quota-bound, session-scoped)             │
└─────────────────────────────────────────────────────────────────┘
```

### Capable Agent

A whitelisted agent system that the platform supports. Examples: Cursor Agent, Copilot, Claude Code, Codex CLI.

Capable Agents are managed at the Foundry level by Agent Fabric. The registry stores:

- Agent system identity and version
- Configuration for LLM gateway routing
- Default quotas and limits
- Auto-fallback preferences

### Skilled Agent

A local manifest (YAML) in a Workshop or Workbench repository that defines:

- Which Skills the agent should have
- Which Capable Agent(s) can execute it
- Guardrails and constraints
- Workspace type(s) it applies to

Skilled Agents are defined per (Workspace, Scenario). They are configuration, not running processes.

### Employed Agent

A running agent instance within a [Workspace Session](workspace-session.md), spawned by WO Runtime:

- Has a [Delegation](delegation.md) token for authority
- Is bound by quota limits
- Is scoped to the session (not long-lived)
- Executes [Tasks](task.md) from the Work Order

Each Scenario invocation gets its own Employed Agent. Agents are not persistent identities — they are spun up per Scenario execution with the specific context, skills, and authority needed.

## Where it lives in Foundry

| Concept | Where It Lives | Managed By |
|---------|----------------|------------|
| **Capable Agent** | Agent Fabric registry | Agent Fabric |
| **Skilled Agent** | Workshop/Workbench repo manifest | Work Catalog Management (validation) |
| **Employed Agent** | Workspace Session process | WO Runtime |

Agent Fabric provides the infrastructure; WO Runtime spawns the instances:

```
Agent Fabric                     WO Runtime
┌─────────────────────┐         ┌─────────────────────┐
│ Capable Agent       │         │ Reads Skilled Agent │
│ Registry            │──────────│ from Scenario      │
│                     │         │                     │
│ Skill Registry      │──────────│ Installs Skills    │
│                     │         │                     │
│ Gateway Policy      │──────────│ Spawns Employed    │
│ (quota, routing)    │         │ Agent with token   │
└─────────────────────┘         └─────────────────────┘
```

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Agent](../../ace/concepts.md#human-agent-team) | Three-tier model (Capable, Skilled, Employed) |
| Human–Agent Team | Employed Agents work alongside humans in Sessions |
| Workforce Repository | Stores agent identities, role bindings, governance |

From ACE: "A workspace's team is composed of human practitioners and AI agents working on the same scenarios and tasks. Both kinds of participants are members of the Workforce."

UPIM's Workforce Repository tracks both human and AI agents with role bindings, skills, availability, and governance. The Agent Model operationalizes this for AI participants.

## Related concepts

- [Skill](skill.md) — Capabilities that Skilled Agents reference
- [Delegation](delegation.md) — Authority tokens for Employed Agents
- [Workspace Session](workspace-session.md) — Where Employed Agents run
- [Scenario](scenario.md) — Defines Skilled Agent requirements
- [Task](task.md) — What Employed Agents execute

## Further reading

- [../agent-fabric/README.md](../agent-fabric/README.md) — Agent infrastructure
- [../agent-fabric/platform-developer-guide/capable-agents.md](../agent-fabric/platform-developer-guide/capable-agents.md) — Capable Agent registry
- [../agent-fabric/user-guide/skilled-agents.md](../agent-fabric/user-guide/skilled-agents.md) — Skilled Agent manifests
- [../work-order-runtime/README.md](../work-order-runtime/README.md) — Employed Agent spawning
