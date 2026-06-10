# Agent Spawning

This document describes how WO Runtime resolves Swarms, loads Trained Agent manifests, selects Raw Agents, prepares the execution harness, and spawns Employed Agents for task execution.

## ACE alignment

| ACE concept | How this module realizes it |
|-------------|---------------------------|
| **Agent** | Spawns Employed Agents as runtime instances within Workspace Sessions |
| **Skill** | Installs skills from Skill Registry and injects them into agent harness |
| **Delegation** | Generates Delegation Tokens granting session owner's authority to agents |
| **Workspace** | Prepares workspace context (knowledge, repos, tools) for agent execution |
| **Team** | Resolves agents from Swarms — organizational units for Trained Agents |

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
│  │  • Resolves Swarms and spawns agents for tasks                         ││
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
5. **Swarm Resolution** — Daemon resolves Swarms referenced by Scenarios
6. **Spawning** — Daemon spawns agents as needed
7. **Monitoring** — Daemon monitors task completion
8. **Shutdown** — Daemon stops when workspace stops

## Swarm Resolution

Before spawning an agent, WO Runtime resolves the Scenario's Swarm references:

### Resolution Flow

```
Scenario trigger
    │
    ├── 1. Read Scenario definition
    │       └── swarms: [build-swarm, review-swarm]
    │       └── coordinator-agent: build-swarm/feature-implementer
    │
    ├── 2. Resolve Swarm visibility
    │       │
    │       ├── Check Workspace-scope swarms/
    │       ├── Check Workbench-scope swarms/
    │       ├── Check Workshop-scope swarms/
    │       └── Check Foundry-scope swarms/
    │
    ├── 3. Load Trained Agent manifest
    │       └── swarms/{swarm}/trained-agents/{agent}.yaml
    │
    └── 4. Extract Raw Agent reference
            └── raw-agent-ref: registry.foundry.io/raw-agents/codex:v2.4.1
```

### Swarm Scope Resolution Order

The daemon checks for Swarm definitions from narrowest to broadest scope:

| Priority | Scope | Location |
|----------|-------|----------|
| 1 (highest) | Workspace | `workbench-{id}/workspaces/{type}/swarms/` |
| 2 | Workbench | `workbench-{id}/swarms/` |
| 3 | Workshop | `workshop-{id}/swarms/` |
| 4 (lowest) | Foundry | `foundry-{id}/swarms/` |

Platform-shipped Swarms are resolved at the Foundry scope. Tenant extensions to platform Swarms are merged — the effective member list includes both platform and tenant-added Trained Agents.

## Harness Preparation

After Swarm resolution, WO Runtime prepares the execution harness:

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
1. Resolve Swarms referenced by Scenario
2. Load Trained Agent manifest from Swarm
3. Resolve Raw Agent from manifest's raw-agent-ref
4. Prepare environment variables (including FOUNDRY_AGENT_JID)
5. Configure MCP connectors
6. Copy skills to workspace
7. Merge knowledge context
8. Generate Delegation Token
9. Spawn Raw Agent process
10. Inject harness into agent
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

# Agent context (Swarm-aware)
FOUNDRY_AGENT_JID=feature-implementer@build-swarm.agents.acme.foundry.io
FOUNDRY_AGENT_SWARM=build-swarm
FOUNDRY_RAW_AGENT=codex
FOUNDRY_RAW_AGENT_VERSION=v2.4.1
FOUNDRY_TRAINED_AGENT=feature-implementer

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

Skills are fetched from the [Skill Registry](../../agent-fabric/platform-developer-guide/skill-registry.md) and installed to the workspace at session start.

### Skill Installation (Session Start)

At Workspace Session start, before any tasks execute:

```
1. WO Runtime reads Trained Agent manifests for all Scenarios' referenced Swarms
2. Collects skill references: name + version constraint + registry
3. Resolves versions:
   - Check Foundry registry first
   - Fall back to Global registry
4. Downloads skills not in local cache
5. Installs to ~/.foundry/skills/{skill}@{resolved-version}/
6. Sets FOUNDRY_SKILLS_PATH environment variable
```

Skills are installed **once per session**, not per task.

### Skill Location (After Installation)

```
~/.foundry/skills/
├── code-generator@2.1.3/
│   ├── SKILL.md
│   ├── package.yaml
│   ├── rules/
│   └── templates/
├── test-writer@1.5.7/
│   ├── SKILL.md
│   └── ...
└── documentation-updater@3.0.1/
    └── ...
```

### Version Pinning at Task Start

When a task starts, WO Runtime records the resolved skill versions in task metadata:

```yaml
task_metadata:
  task_key: TASK-890
  trained_agent_jid: feature-implementer@build-swarm.agents.acme.foundry.io
  swarm: build-swarm
  raw_agent_ref: registry.foundry.io/raw-agents/codex:v2.4.1
  resolved_skills:
    - name: code-generator
      version: 2.1.3
      registry: foundry
    - name: test-writer
      version: 1.5.7
      registry: global
```

This ensures:
- Reproducibility: Re-running a task uses same skill versions
- Auditability: Know exactly which skills were used
- Debugging: Pinpoint skill version in failure analysis

### Skill Injection into Agent

Skills are injected into agent context:

```
Raw Agent: Codex (via OCI container)
    │
    ├── System prompt includes SKILL.md content
    ├── Rules from skills/rules/ added to agent rules
    └── Templates from skills/templates/ available as references
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
    ├── Agent JID (Trained Agent identity)
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

See [../../agent-fabric/platform-developer-guide/gateway-policy.md](../../agent-fabric/platform-developer-guide/gateway-policy.md) for token flow details.

## Agent Spawning

### Raw-Agent-Specific Spawning

Each Raw Agent has a specific spawn mechanism:

#### Codex

```yaml
spawn:
  type: codex
  raw-agent-ref: registry.foundry.io/raw-agents/codex:v2.4.1
  command: codex
  args:
    - --workspace
    - ${WORKSPACE_PATH}
    - --task
    - ${FOUNDRY_TASK_KEY}
  environment:
    FOUNDRY_AGENT_JID: ${AGENT_JID}
    FOUNDRY_SKILLS_PATH: ${SKILL_PATH}
  io:
    mode: terminal
```

#### Cursor Agent

```yaml
spawn:
  type: cursor-agent
  raw-agent-ref: registry.foundry.io/raw-agents/cursor-agent:v1.2.0
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

#### Claude Code

```yaml
spawn:
  type: claude-code
  raw-agent-ref: registry.foundry.io/raw-agents/claude-code:v3.1.0
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

### Generic Spawn Interface

WO Runtime provides a generic spawn interface:

```python
def spawn_agent(
    trained_agent_jid: str,
    raw_agent_ref: str,
    task_key: str,
    harness: Harness
) -> AgentProcess:
    """
    Spawn an Employed Agent for a task.
    
    Args:
        trained_agent_jid: Trained Agent JID from Swarm
        raw_agent_ref: Raw Agent OCI URI from Trained Agent manifest
        task_key: Jira task key
        harness: Prepared harness (env, mcp, skills, knowledge, token)
    
    Returns:
        AgentProcess handle for monitoring
    """
    spawn_config = get_spawn_config_for_raw_agent(raw_agent_ref)
    
    process = subprocess.Popen(
        spawn_config.command,
        args=spawn_config.args,
        env=harness.environment,
        cwd=workspace_path
    )
    
    return AgentProcess(process, task_key, trained_agent_jid, harness)
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
2. Raw Agent support (some agents terminal-only)
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

---

## Recoverable Failures

Certain failures pause task execution without failing the task permanently. Tasks can resume when the blocking condition resolves.

### Recoverable Failure Types

| Failure | Trigger | Resolution | Resume Behavior |
|---------|---------|------------|-----------------|
| **Quota Exhausted** | 429 from Gateway | Quota refreshes or increased | Automatic resume |
| **Raw Agent Disabled** | Agent disabled mid-task | Admin re-enables agent | Automatic resume |
| **All Fallbacks Exhausted** | Raw Agent unavailable | Agent restored in registry | Automatic resume |
| **Model Rate Limited** | Temporary 429 from provider | Wait + retry | Automatic after backoff |
| **Credential Expired** | Token refresh needed | Session re-authentication | Automatic after refresh |

### Recoverable Failure Flow

```
Task executing
    │
    ├── Failure detected (quota, agent disabled, etc.)
    │
    ├── WO Runtime attempts fallback (if configured in gateway policy)
    │
    ├── If all fallbacks fail:
    │   ├── Task state → Blocked (recoverable)
    │   ├── Jira status → "Blocked"
    │   ├── Record: blocked_reason, blocked_at, agent_jid
    │   └── Notify session owner via IDE panel
    │
    └── When condition resolves:
        ├── WO Runtime detects resolution (polling)
        ├── Task state → Ready
        └── Task resumes (possibly with different Raw Agent version)
```

### Task Metadata for Blocked Tasks

```yaml
task_metadata:
  task_key: TASK-890
  status: blocked
  trained_agent_jid: feature-implementer@build-swarm.agents.acme.foundry.io
  swarm: build-swarm
  blocked_reason: quota_exhausted
  blocked_at: 2026-05-28T03:00:00Z
  last_attempt:
    raw_agent_ref: registry.foundry.io/raw-agents/codex:v2.4.1
    model: codex-3
    error: "429: Monthly quota exceeded"
```

### IDE Notification

When a task enters recoverable failure:

1. Work Orders Panel shows task as "Blocked"
2. Tooltip shows reason and resolution path
3. Toast notification to session owner
4. Optional: Alert to Workbench admin (for quota/agent issues)

---

## Boundary with Agent Fabric

WO Runtime and Agent Fabric share responsibility for agent lifecycle. This section clarifies the boundary.

### WO Runtime Owns: When and How

| Responsibility | Description |
|----------------|-------------|
| **Swarm resolution** | WO Runtime resolves Swarms from Scenario references at the appropriate scope |
| **Spawning** | WO Runtime spawns Employed Agent processes within Workspace Sessions |
| **Harness preparation** | WO Runtime assembles environment, MCP connectors, skills, knowledge, and Delegation Token |
| **Task lifecycle** | WO Runtime manages task scheduling, execution, completion detection, and failure handling |
| **Agent process management** | WO Runtime monitors, restarts, and terminates agent processes |
| **Raw Agent selection** | WO Runtime resolves Raw Agent from Trained Agent manifest's `raw-agent-ref` |

### Agent Fabric Owns: What

| Responsibility | Description |
|----------------|-------------|
| **Raw Agent Registry** | Agent Fabric maintains the OCI catalog of available Raw Agents |
| **Swarm Registry** | Agent Fabric defines Swarm structure, membership, and visibility rules |
| **Trained Agent manifests** | Agent Fabric defines Trained Agent capabilities, skills, and Raw Agent references |
| **Quota allocation** | Agent Fabric (via Access Gateway) enforces token budgets and rate limits |
| **Policy enforcement** | Agent Fabric defines tool governance and approval policies |
| **Credential resolution** | Agent Fabric (via Delegation Token) provides scoped access to external services |

### Interface Contract

```
Agent Fabric provides:
├── Swarm Registry
│   ├── Swarm definitions (swarm.yaml)
│   ├── Trained Agent manifests (trained-agents/{agent}.yaml)
│   ├── Membership and visibility rules
│   └── Scope hierarchy enforcement
├── Raw Agent Registry
│   ├── OCI image references and metadata
│   └── Per-agent spawn configuration
├── Delegation Token generator
└── Access Gateway endpoint

WO Runtime consumes:
├── Resolves Swarms from Scenario references
├── Loads Trained Agent manifest from Swarm
├── Resolves Raw Agent from manifest's raw-agent-ref
├── Requests Delegation Token (with agent JID)
├── Routes model calls through Access Gateway
└── Reports usage metrics (attributed to agent JID)
```

### Coordination Points

1. **Swarm resolution** — WO Runtime resolves Swarms from Agent Fabric's Swarm Registry at task time
2. **Skill installation** — WO Runtime fetches skills from Agent Fabric's Skill Registry at session start
3. **Raw Agent resolution** — WO Runtime resolves Raw Agent from Trained Agent manifest; Agent Fabric determines availability
4. **Quota enforcement** — WO Runtime detects quota exhaustion (429 from Gateway); Agent Fabric manages allocation
5. **Identity attribution** — All actions attributed to the Trained Agent's JID for audit trail

## Read Next

- [ide-integration.md](ide-integration.md) — VS Code plugin for agent I/O
- [task-execution.md](task-execution.md) — Task tree and dependencies
- [../../agent-fabric/platform-developer-guide/employed-agents.md](../../agent-fabric/platform-developer-guide/employed-agents.md) — Employed Agent lifecycle
- [../../agent-fabric/platform-developer-guide/gateway-policy.md](../../agent-fabric/platform-developer-guide/gateway-policy.md) — Quota and token policies
- [../../agent-fabric/platform-developer-guide/raw-agents.md](../../agent-fabric/platform-developer-guide/raw-agents.md) — Raw Agent OCI specification
- [../../agent-fabric/platform-developer-guide/swarm-registry.md](../../agent-fabric/platform-developer-guide/swarm-registry.md) — Swarm Registry API
