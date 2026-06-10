# Agent Spawner

The Agent Spawner is the component that prepares execution harnesses and spawns Employed Agents for ready tasks — resolving Swarms, loading Trained Agent manifests, selecting Raw Agents, and assembling environment, tools, skills, knowledge, and delegation into a complete agent runtime.

## What it is

When the Task Manager identifies a ready task with a coordinator or designated Trained Agent, it passes the task to the Agent Spawner. The Agent Spawner's job is to turn a Trained Agent definition into a running Employed Agent process.

This involves:

1. **Resolving the Swarm** — Locating the referenced Swarm at the appropriate scope
2. **Loading the Trained Agent manifest** — From `swarms/{swarm}/trained-agents/{agent}.yaml`
3. **Resolving the Raw Agent** — Pulling the OCI container reference from the manifest's `raw-agent-ref`
4. **Preparing the harness** — Environment variables, MCP connectors, skills, knowledge, delegation token
5. **Spawning the process** — Starting the agent with harness injected
6. **Monitoring** — Tracking agent status and handling failures

The Agent Spawner is the boundary between "what work needs to be done" (Task Manager) and "who does it and how" (agent runtime). It abstracts the diversity of Raw Agents (Codex, Cursor Agent, Claude Code) behind a consistent spawn interface.

## Where it lives

| Component | Location |
|-----------|----------|
| **Agent Spawner** | WO Runtime Daemon |
| **Agent processes** | Sibling processes in Coder workspace |
| **Harness state** | Local SQLite `agents` table |
| **Skills** | `~/.foundry/skills/` directory |

## Harness components

The harness is everything an Employed Agent needs to execute:

| Component | Source | Purpose |
|-----------|--------|---------|
| **Environment** | Session config + WO context | Configuration variables |
| **MCP connectors** | Auto-provisioned + Scenario-defined | Tool access (Jira, GitHub, etc.) |
| **Skills** | Skill Registry | Capabilities installed at session start |
| **Knowledge** | Merged hierarchy | Context from Workshop → Workbench → WO |
| **Delegation Token** | Generated per spawn | Authority to act on session owner's behalf |

## Harness preparation flow

```
Scenario trigger (with Swarm references)
    │
    ├── 1. Resolve referenced Swarms
    │       │
    │       ├── Check Swarm visibility at current scope
    │       └── Load Swarm manifest from swarms/{swarm}/swarm.yaml
    │
    ├── 2. Get coordinator/designated agent from Swarm
    │       │
    │       └── From Scenario's coordinator-agent: {swarm}/{agent}
    │
    ├── 3. Load Trained Agent manifest
    │       │
    │       └── From swarms/{swarm}/trained-agents/{agent}.yaml
    │
    ├── 4. Resolve Raw Agent from Trained Agent
    │       │
    │       ├── raw-agent-ref: registry.foundry.io/raw-agents/codex:v2.4.1
    │       ├── Check availability in Raw Agent Registry
    │       └── Pull OCI image if needed
    │
    ├── 5. Prepare environment variables
    │       │
    │       └── FOUNDRY_WORKBENCH_ID, FOUNDRY_TASK_KEY, FOUNDRY_AGENT_JID, etc.
    │
    ├── 6. Configure MCP connectors
    │       │
    │       ├── Jira MCP (always)
    │       ├── GitHub MCP (if repo linked)
    │       └── Foundry MCP (always)
    │
    ├── 7. Resolve installed skills
    │       │
    │       └── Skills installed at session start → ~/.foundry/skills/
    │
    ├── 8. Merge knowledge context
    │       │
    │       └── Workshop + Workbench + Scenario + WO context
    │
    ├── 9. Generate Delegation Token
    │       │
    │       └── Session owner identity + scoped permissions + quota
    │
    └── 10. Spawn agent process
            │
            └── Execute Raw Agent spawn command with harness injected
```

## Raw Agent selection

The Agent Spawner resolves a Raw Agent from the Trained Agent's manifest:

```yaml
# Trained Agent manifest
name: feature-implementer
swarm: build-swarm
raw-agent-ref: registry.foundry.io/raw-agents/codex:v2.4.1
identity:
  jid: feature-implementer@build-swarm.agents.acme.foundry.io
```

Selection considers:
- **Availability** — Is the Raw Agent available in the registry (platform or tenant)?
- **Quota** — Does the session have remaining quota for this agent type?
- **Version** — Does the resolved version meet the manifest constraint?

If the primary Raw Agent fails (quota exhausted, disabled, error), the spawner applies fallback rules defined in gateway policy.

## Raw Agent spawn configurations

Each Raw Agent has a specific spawn configuration:

| Agent | Command | I/O Mode |
|-------|---------|----------|
| Codex | `codex --workspace $PATH` | Terminal |
| Cursor Agent | `cursor-agent --workspace $PATH` | VS Code panel or terminal |
| Claude Code | `claude-code --project $PATH` | Terminal |

## Recoverable failures

Some spawn failures pause the task without permanent failure:

| Failure | Recovery |
|---------|----------|
| Quota exhausted | Auto-resume when quota refreshes |
| Raw Agent disabled | Auto-resume when admin re-enables |
| All fallbacks fail | Auto-resume when any option restored |
| Model rate limited | Auto-resume after backoff |

The task enters `blocked` state with `blocked_reason` recorded. The daemon monitors for resolution and resumes automatically.

## Agent process management

| Aspect | Behavior |
|--------|----------|
| **Isolation** | Each agent is a separate process |
| **Monitoring** | Daemon tracks PID and status |
| **Crash recovery** | Retry task up to 2 times |
| **Resource limits** | CPU capped at 2 cores per agent |

## Related concepts

- [Task Manager](task-manager.md) — Sends ready tasks to Agent Spawner
- [Context Compilation](context-compilation.md) — How knowledge is assembled
- [WO Runtime Daemon](wo-runtime-daemon.md) — Hosts the Agent Spawner
- [Agent Model](../../concepts/agent-model.md) — Raw → Trained → Employed
- [Skill](../../concepts/skill.md) — Capabilities installed into harness
- [Delegation](../../concepts/delegation.md) — Tokens granting agent authority
- [Swarm](../../agent-fabric/concepts/swarm.md) — Organizational unit resolved during spawning

## Further reading

- [../platform-developer-guide/agent-spawning.md](../platform-developer-guide/agent-spawning.md) — Detailed spawn specification
- [../platform-developer-guide/requirements.md](../platform-developer-guide/requirements.md) — Spawner requirements (WOR-FR-0007, WOR-FR-0008)
- [../../agent-fabric/platform-developer-guide/raw-agents.md](../../agent-fabric/platform-developer-guide/raw-agents.md) — Raw Agent OCI specification
- [../../agent-fabric/platform-developer-guide/swarm-registry.md](../../agent-fabric/platform-developer-guide/swarm-registry.md) — Swarm Registry API
