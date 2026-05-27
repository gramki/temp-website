# Agent Spawning

This document describes how WO Runtime prepares the execution harness and spawns Employed Agents for task execution.

## WO Runtime Daemon

The WO Runtime runs as a daemon within each Workspace Session:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Coder Workspace (Workspace Session)                                         │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │  WO Runtime Daemon                                                      ││
│  │                                                                         ││
│  │  • Starts with workspace                                               ││
│  │  • Runs continuously while workspace active                            ││
│  │  • Polls Jira for assigned WOs                                         ││
│  │  • Spawns agents for tasks                                             ││
│  │  • Manages task lifecycle                                              ││
│  └─────────────────────────────────────────────────────────────────────────┘│
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────────┐│
│  │  Employed Agent Process (spawned by daemon)                             ││
│  │                                                                         ││
│  │  • One process per active task                                         ││
│  │  • Runs within workspace                                               ││
│  │  • Uses prepared harness                                               ││
│  └─────────────────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────────────────┘
```

### Daemon Lifecycle

1. **Startup** — Daemon starts when Coder workspace starts
2. **Authentication** — Daemon authenticates to Jira MCP
3. **Polling** — Daemon polls for WOs assigned to session owner
4. **Scheduling** — Daemon schedules ready tasks for execution
5. **Spawning** — Daemon spawns agents as needed
6. **Monitoring** — Daemon monitors task completion
7. **Shutdown** — Daemon stops when workspace stops

## Harness Preparation

Before spawning an agent, WO Runtime prepares the execution harness:

### Harness Components

| Component | Description |
|-----------|-------------|
| **Environment** | Environment variables for agent configuration |
| **Tools / MCP** | MCP connectors for external services |
| **Skills** | Skill packages copied to workspace |
| **Knowledge** | Context from merged hierarchy |
| **Delegation Token** | Authority token for model access |

### Harness Preparation Flow

```
1. Read Skilled Agent definition (agent.yaml)
2. Select Capable Agent (from compatible list)
3. Prepare environment variables
4. Configure MCP connectors
5. Copy skills to workspace
6. Merge knowledge context
7. Generate Delegation Token
8. Spawn agent process
9. Inject harness into agent
```

## Environment Variables

Environment variables configure the agent execution context:

```bash
# Core context
FOUNDRY_WORKBENCH_ID=product-abc
FOUNDRY_WORKSPACE_TYPE=development
FOUNDRY_SESSION_ID=ws-dev-12345
FOUNDRY_SESSION_OWNER=alice@example.com

# Work Order context
FOUNDRY_WORK_ORDER=WO-567
FOUNDRY_TASK_KEY=TASK-890
FOUNDRY_SCENARIO=implement-feature

# Agent context
FOUNDRY_AGENT_TYPE=cursor-agent
FOUNDRY_AGENT_MODEL=claude-opus
FOUNDRY_SKILLED_AGENT=feature-implementation-agent

# Access
FOUNDRY_ACCESS_GATEWAY_URL=https://gateway.foundry.example.com
FOUNDRY_DELEGATION_TOKEN=<token>

# MCP
FOUNDRY_JIRA_MCP_ENDPOINT=mcp://jira.foundry.example.com
```

## MCP Connectors

MCP (Model Context Protocol) connectors provide tool access to agents.

### Auto-Provisioned MCPs

| MCP | Auto-provisioned | Purpose |
|-----|------------------|---------|
| **Jira MCP** | Yes | Task management, WO operations |
| **GitHub MCP** | Yes (if repo linked) | Code operations |
| **Foundry MCP** | Yes | Foundry-specific operations |

### Jira MCP

Jira MCP is automatically provisioned for every agent:

```yaml
mcp_connectors:
  jira:
    endpoint: mcp://jira.foundry.example.com
    auth: delegated  # Uses session owner's Jira access
    tools:
      - jira_search
      - jira_get_issue
      - jira_create_issue
      - jira_update_issue
      - jira_transition_issue
```

### MCP Authentication

MCPs authenticate using the Delegation Token:

```
Agent → MCP Connector → Delegation Token validation → External service

Example:
Agent calls jira_create_issue
    │
    ├── Jira MCP receives call
    ├── Validates Delegation Token
    ├── Extracts session owner identity
    ├── Calls Jira API as session owner
    └── Returns result to agent
```

## Skills Loading

Skills are copied from the Workshop Definition Repository to the workspace.

### Skill Location

```
Workshop Definition Repository:
workspaces/{workspace-type}/scenarios/{scenario}/skilled-agent/skills/

Workspace (after copy):
~/.foundry/skills/{scenario}/
```

### Skill Copy Process

```
1. Read skilled-agent/agent.yaml to get skill list
2. For each skill:
   a. Locate skill folder in Workshop repo
   b. Copy to workspace skills directory
   c. Set permissions (read-only)
3. Configure SKILL_PATH environment variable
```

### Skill Injection

Skills are injected into agent context:

```
Capable Agent: Cursor Agent
    │
    ├── System prompt includes SKILL.md content
    ├── Rules from skills/rules/ added to rules
    └── Templates from skills/templates/ available
```

## Knowledge Context

Knowledge is assembled from the merged hierarchy:

### Knowledge Sources

```
Foundry Knowledge (global)
    │
    └── Workshop Knowledge (team)
            │
            └── Workbench Knowledge (product)
                    │
                    └── Scenario Knowledge (task-specific)
                            │
                            └── Work Order Knowledge (WO-specific)
```

### Knowledge Assembly

```yaml
knowledge_context:
  foundry:
    - foundry-standards.md
    - security-guidelines.md
  workshop:
    - team-conventions.md
    - domain-glossary.md
  workbench:
    - product-architecture.md
    - api-documentation.md
  scenario:
    - implement-feature-guide.md
  work_order:
    - wo-567-context.md
    - related-prs.md
```

Knowledge is injected as context to the agent.

## Delegation Token

The Delegation Token authorizes the agent to act on behalf of the session owner.

### Token Generation

```
WO Runtime generates token:
    │
    ├── Session owner identity
    ├── Session ID
    ├── Workbench ID
    ├── Workspace type
    ├── Granted scopes (tools, models)
    ├── Quota allocation
    ├── Expiry time (session-scoped)
    └── Signed with Foundry key
```

### Token Provisioning

```
1. WO Runtime generates Delegation Token
2. Token stored in agent environment (FOUNDRY_DELEGATION_TOKEN)
3. Agent includes token in all external calls
4. Access Gateway validates token on each call
```

See [access-gateway.md](../agent-model/access-gateway.md) for token flow details.

## Agent Spawning

### Capable-Agent-Specific Spawning

Each Capable Agent has a specific spawn mechanism:

#### Cursor Agent

```yaml
spawn:
  type: cursor-agent
  command: cursor-agent
  args:
    - --workspace
    - ${WORKSPACE_PATH}
    - --task
    - ${FOUNDRY_TASK_KEY}
  environment:
    CURSOR_SKILLS_PATH: ${SKILL_PATH}
    CURSOR_RULES_PATH: ${RULES_PATH}
  io:
    mode: vscode-panel  # or terminal
```

#### Copilot

```yaml
spawn:
  type: copilot
  command: gh copilot
  args:
    - --workspace
    - ${WORKSPACE_PATH}
  environment:
    GITHUB_TOKEN: ${GITHUB_TOKEN}
  io:
    mode: terminal
```

#### Claude Code

```yaml
spawn:
  type: claude-code
  command: claude-code
  args:
    - --project
    - ${WORKSPACE_PATH}
    - --context
    - ${CONTEXT_FILE}
  environment:
    ANTHROPIC_API_KEY: via-gateway  # Routed through Access Gateway
  io:
    mode: terminal
```

#### Codex CLI

```yaml
spawn:
  type: codex-cli
  command: codex
  args:
    - --workspace
    - ${WORKSPACE_PATH}
  environment:
    OPENAI_API_KEY: via-gateway
  io:
    mode: terminal
```

### Generic Spawn Interface

WO Runtime provides a generic spawn interface:

```python
def spawn_agent(
    capable_agent: str,
    model: str,
    task_key: str,
    harness: Harness
) -> AgentProcess:
    """
    Spawn an Employed Agent for a task.
    
    Args:
        capable_agent: Capable Agent identifier
        model: Model to use
        task_key: Jira task key
        harness: Prepared harness (env, mcp, skills, knowledge, token)
    
    Returns:
        AgentProcess handle for monitoring
    """
    spawn_config = get_spawn_config(capable_agent)
    
    process = subprocess.Popen(
        spawn_config.command,
        args=spawn_config.args,
        env=harness.environment,
        cwd=workspace_path
    )
    
    return AgentProcess(process, task_key, harness)
```

## Agent I/O

Agent I/O is routed through VS Code (WO Runtime does not mediate):

### Terminal Mode

```
User Input:  Terminal prompt → Agent process stdin
Agent Output: Agent process stdout → Terminal display
```

### Chat Panel Mode

```
User Input:  User → VS Code WO Runtime Chat Panel → Agent
Agent Output: Agent → VS Code WO Runtime Chat Panel → User
```

The I/O mode is determined by:

1. User preference (configured in settings)
2. Capable Agent support (some agents terminal-only)
3. Skill recommendation (some skills work better in chat)

## Task Completion Notification

Agents notify task completion via Jira MCP:

```
1. Agent completes work
2. Agent calls jira_transition_issue(task_key, "Done")
3. Jira MCP updates task status
4. WO Runtime detects task completion (via polling or webhook)
5. WO Runtime schedules next ready task
```

Alternatively, the user can mark tasks complete through the IDE UI.

## Read Next

- [ide-integration.md](ide-integration.md) — VS Code plugin for agent I/O
- [task-execution.md](task-execution.md) — Task tree and dependencies
- [../agent-model/employed-agents.md](../agent-model/employed-agents.md) — Employed Agent lifecycle
- [../agent-model/access-gateway.md](../agent-model/access-gateway.md) — Token validation and model access
