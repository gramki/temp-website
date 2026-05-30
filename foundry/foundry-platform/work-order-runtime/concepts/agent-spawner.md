# Agent Spawner

The Agent Spawner is the component that prepares execution harnesses and spawns Employed Agents for ready tasks — assembling environment, tools, skills, knowledge, and delegation into a complete agent runtime.

## What it is

When the Task Manager identifies a ready task with a Skilled Agent, it passes the task to the Agent Spawner. The Agent Spawner's job is to turn a Skilled Agent definition into a running Employed Agent process.

This involves:

1. **Reading the Skilled Agent manifest** — Capabilities, compatible agents, skill references
2. **Selecting a Capable Agent** — Choosing from compatible agents with fallback support
3. **Preparing the harness** — Environment variables, MCP connectors, skills, knowledge, delegation token
4. **Spawning the process** — Starting the agent with harness injected
5. **Monitoring** — Tracking agent status and handling failures

The Agent Spawner is the boundary between "what work needs to be done" (Task Manager) and "who does it and how" (agent runtime). It abstracts the diversity of Capable Agents (Cursor, Copilot, Claude Code, Codex) behind a consistent spawn interface.

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
Task ready (with Skilled Agent)
    │
    ├── 1. Read Skilled Agent definition (agent.yaml)
    │
    ├── 2. Select Capable Agent
    │       │
    │       ├── Check compatible agents in manifest
    │       ├── Check availability/quota
    │       └── Select highest-priority available
    │
    ├── 3. Prepare environment variables
    │       │
    │       └── FOUNDRY_WORKBENCH_ID, FOUNDRY_TASK_KEY, etc.
    │
    ├── 4. Configure MCP connectors
    │       │
    │       ├── Jira MCP (always)
    │       ├── GitHub MCP (if repo linked)
    │       └── Foundry MCP (always)
    │
    ├── 5. Resolve installed skills
    │       │
    │       └── Skills installed at session start → ~/.foundry/skills/
    │
    ├── 6. Merge knowledge context
    │       │
    │       └── Workshop + Workbench + Scenario + WO context
    │
    ├── 7. Generate Delegation Token
    │       │
    │       └── Session owner identity + scoped permissions + quota
    │
    └── 8. Spawn agent process
            │
            └── Execute spawn command with harness injected
```

## Capable Agent selection

The Agent Spawner selects a Capable Agent from the Skilled Agent's compatibility list:

```yaml
# Skilled Agent manifest
compatible_agents:
  - cursor-agent  # preferred
  - copilot
  - claude-code
```

Selection considers:
- **Availability** — Is the agent enabled for this Workbench?
- **Quota** — Does the session have remaining quota for this agent?
- **Priority** — Higher in the list = preferred

If the primary agent fails (quota exhausted, disabled, error), the spawner tries the next compatible agent (auto-fallback).

## Capable Agent spawn configurations

Each Capable Agent has a specific spawn configuration:

| Agent | Command | I/O Mode |
|-------|---------|----------|
| Cursor Agent | `cursor-agent --workspace $PATH` | VS Code panel or terminal |
| Copilot | `gh copilot --workspace $PATH` | Terminal |
| Claude Code | `claude-code --project $PATH` | Terminal |
| Codex CLI | `codex --workspace $PATH` | Terminal |

## Recoverable failures

Some spawn failures pause the task without permanent failure:

| Failure | Recovery |
|---------|----------|
| Quota exhausted | Auto-resume when quota refreshes |
| Agent disabled | Auto-resume when admin re-enables |
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
- [Agent Model](../../concepts/agent-model.md) — Capable → Skilled → Employed
- [Skill](../../concepts/skill.md) — Capabilities installed into harness
- [Delegation](../../concepts/delegation.md) — Tokens granting agent authority

## Further reading

- [../platform-developer-guide/agent-spawning.md](../platform-developer-guide/agent-spawning.md) — Detailed spawn specification
- [../platform-developer-guide/requirements.md](../platform-developer-guide/requirements.md) — Spawner requirements (WOR-FR-0007, WOR-FR-0008)
- [../../agent-fabric/platform-developer-guide/capable-agents.md](../../agent-fabric/platform-developer-guide/capable-agents.md) — Capable Agent registry
