# Employed Agents

Employed Agents are Skilled Agents instantiated in a Workspace Session to perform work on behalf of the session owner.

## ACE alignment

| ACE concept | How this module realizes it |
|-------------|---------------------------|
| **Agent** | Employed Agents are runtime instances bound to Workspace Session, Session Owner, and Work Order/Task |
| **Delegation** | Session owner's authority captured in Delegation Token; all agent activity attributed to owner |
| **Workspace** | Employment is scoped to Workspace Session; agent borrows session's tools, repos, and quota |
| **Task** | Agent executes skills against assigned tasks; can create sub-tasks via Jira MCP |

## Definition

An **Employed Agent** is the runtime instantiation of a Skilled Agent, bound to:

- A **Workspace Session** — The execution environment
- A **Session Owner** — The human whose authority is delegated
- A **Work Order / Task** — The work being performed

Employed Agents represent the "worker" — what an agent *is doing* right now.

## Employment Model

Employment is scoped to a Workspace Session:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Session Owner (Human)                                                       │
│                                                                              │
│  • Owns the Workspace Session                                               │
│  • Provides Delegation Token                                                │
│  • Grants credits and quota                                                 │
│  • All agent activity attributed to owner                                   │
└─────────────────────────────────────────────────────────────────────────────┘
                          │
                          │ Delegation Token
                          │ (grants: credits, quota, tool access)
                          ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  Employed Agent                                                              │
│                                                                              │
│  • Peer or Assistant to session owner (based on skill autonomy)             │
│  • Scoped to Workspace Session                                              │
│  • Uses session owner's credits and quota                                   │
│  • Borrows tools/resources from workspace session                           │
│  • Works on delegated authority of session owner                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Key Properties

| Property | Value |
|----------|-------|
| **Scope** | One Employed Agent per Workspace Session |
| **Role** | Peer or Assistant (based on skill autonomy level) |
| **Authority** | Delegated from Session Owner |
| **Credits/Quota** | Session Owner's allocation |
| **Tools/Resources** | Borrowed from Workspace Session |
| **Attribution** | All activity attributed to Session Owner |

## Peer vs Assistant Role

The Employed Agent's role depends on the autonomy level defined in its skills:

| Role | Autonomy Level | Behavior |
|------|----------------|----------|
| **Peer** | High | Works independently, reports results |
| **Assistant** | Low | Requires approval for significant actions |

Skills define their autonomy level in `SKILL.md`:

```yaml
---
name: code-generator
autonomy: high  # peer mode
---
```

```yaml
---
name: code-reviewer
autonomy: low  # assistant mode - suggests, human approves
---
```

## Delegated Authority

Employed Agents operate on delegated authority from the session owner:

### What Delegation Grants

- **Model access** — Via Access Gateway, charged to session owner's quota
- **Tool access** — MCP connectors available in the workspace
- **Repository access** — Git repos linked to the workbench
- **Jira access** — WO and Task management via Jira MCP

### What Delegation Does NOT Grant

- **Elevated permissions** — Agent cannot exceed session owner's permissions
- **Persistent credentials** — All credentials are session-scoped
- **Cross-session access** — Agent cannot access other users' sessions

### Delegation Token

The session owner's authority is captured in a **Delegation Token**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Delegation Token                                                            │
│                                                                              │
│  • Session owner identity                                                   │
│  • Session ID                                                               │
│  • Workbench ID                                                             │
│  • Workspace type                                                           │
│  • Granted scopes (tools, repos, model access)                             │
│  • Expiry time                                                              │
│  • Quota allocation                                                         │
└─────────────────────────────────────────────────────────────────────────────┘
```

The token is provided to the Employed Agent at spawn time and used for all external calls.

## Session Context

Employed Agents have full awareness of their Workspace Session:

| Context | Source | Usage |
|---------|--------|-------|
| **Work Orders** | Jira via MCP | What work is assigned |
| **Task tree** | Jira via MCP | Current task structure and dependencies |
| **Repositories** | Workspace | Code, design, spec access |
| **Knowledge** | Merged hierarchy | Domain, product, WO-specific context |
| **Skills** | Workspace skills folder | What capabilities are available |
| **Tools** | MCP connectors | What actions can be taken |

## Employment Lifecycle

### Creation

1. WO Runtime daemon detects a task needs an Employed Agent
2. WO Runtime reads Skilled Agent definition from Scenario
3. WO Runtime selects Capable Agent and Model
4. WO Runtime prepares harness (environment, tools, MCP, skills)
5. WO Runtime spawns agent process with harness
6. Employed Agent receives Delegation Token

### Active

- Employed Agent executes skills against tasks
- All model calls route through Access Gateway
- All tool calls (Jira, repos) use Delegation Token
- Agent can create sub-tasks via Jira MCP
- Agent notifies WO Runtime of task completion

### Termination

- Task tree completed → Agent terminates
- Session owner closes session → Agent terminates
- Quota exhausted → Agent pauses or terminates (configurable)
- Error/timeout → Agent terminates with error state

## Workspace Session Binding

An Employed Agent is tightly bound to its Workspace Session:

| Aspect | Binding |
|--------|---------|
| **Process** | Runs inside the Workspace Session (Coder environment) |
| **Credentials** | Use session's configured credentials |
| **Tools** | Use session's MCP connectors |
| **Files** | Read/write to session's workspace |
| **Quota** | Charged against session owner |

### Session Not Running

If the Workspace Session is not running:

- WO Runtime daemon is not active
- Employed Agent cannot be spawned
- Work Orders wait in Jira
- Orchestrator may activate session (if user configured auto-activation)

## Attribution and Audit

All Employed Agent activity is attributed to the session owner:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Audit Record                                                                │
│                                                                              │
│  Session Owner: alice@example.com                                           │
│  Session ID: ws-dev-12345                                                   │
│  Employed Agent: feature-implementation-agent                               │
│  Work Order: WO-567                                                         │
│  Task: TASK-890                                                             │
│  Action: model-call                                                         │
│  Model: claude-opus                                                         │
│  Tokens: 15,234                                                             │
│  Cost: $0.45                                                                │
│  Timestamp: 2026-05-28T02:30:00Z                                           │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Multiple Employed Agents

Within a single Workspace Session:

- **One skill execution at a time** — Agent executes one skill per task
- **Multiple tasks may spawn agents** — Each task with a Skilled Agent gets its own execution
- **Sequential, not parallel** — Tasks execute based on dependency order

---

## Boundary with WO Runtime

Agent Fabric and WO Runtime share responsibility for agent lifecycle. This section clarifies the boundary.

### Agent Fabric Owns: What

| Responsibility | Description |
|----------------|-------------|
| **Skilled Agent manifests** | Defines agent capabilities, skills, compatible Capable Agents, and autonomy levels |
| **Capable Agent registry** | Maintains the catalog of available Capable Agents and their spawn configurations |
| **Skill Registry** | Provides skill packages (content, rules, templates) for installation |
| **Quota allocation** | Enforces token budgets, rate limits, and cost attribution per session owner |
| **Access Gateway** | Routes model calls, validates Delegation Tokens, applies policy |
| **Policy definition** | Specifies tool governance, approval thresholds, and allowed operations |
| **Credential resolution** | Issues Delegation Tokens scoped to session owner's permissions |

### WO Runtime Owns: When and How

| Responsibility | Description |
|----------------|-------------|
| **Spawning** | Spawns Employed Agent processes within Workspace Sessions |
| **Harness assembly** | Prepares environment, MCP connectors, skills, knowledge, and token |
| **Task scheduling** | Determines when tasks execute based on dependencies and readiness |
| **Agent process lifecycle** | Starts, monitors, restarts, and terminates agent processes |
| **Failure handling** | Detects failures, attempts fallback, manages recoverable states |
| **Completion reporting** | Detects task completion and updates Jira state |

### Interface Contract

```
Agent Fabric provides:
├── Skilled Agent manifest (agent.yaml)
├── Capable Agent registry (spawn configs per agent)
├── Skill Registry (skill packages)
├── Delegation Token generator
├── Access Gateway (model routing, quota enforcement)
└── Policy definitions (tool governance)

WO Runtime consumes:
├── Reads Skilled Agent manifest for task assignment
├── Queries Capable Agent registry for spawn config
├── Fetches skills from Skill Registry at session start
├── Requests Delegation Token per session
├── Routes model calls through Access Gateway
└── Reports task completion and usage metrics
```

### Why This Separation

- **Agent Fabric defines what**: Manifests, policies, and registries are declarative definitions
- **WO Runtime implements how**: Spawning, scheduling, and process management are runtime operations
- **Clear ownership**: Agent Fabric is authoritative for agent definitions; WO Runtime is authoritative for execution

This separation enables:
- Independent evolution of agent definitions and runtime implementation
- CI/Release Tools to use Agent Fabric definitions without WO Runtime (see [ci-agent-architecture.md](../../release-tools/platform-developer-guide/ci-agent-architecture.md))
- Testing agent manifests without full WO Runtime deployment

## Read Next

- [skilled-agents.md](skilled-agents.md) — Skilled Agent definitions
- [gateway-policy.md](gateway-policy.md) — How Delegation Tokens are used
- [../work-order-runtime/platform-developer-guide/agent-spawning.md](..//work-order-runtime/platform-developer-guide/agent-spawning.md) — How Employed Agents are spawned
- [../work-order-runtime/user-guide/work-order-lifecycle.md](..//work-order-runtime/user-guide/work-order-lifecycle.md) — Full execution flow
