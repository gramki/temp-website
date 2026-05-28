# Work Order Runtime

**Module scope:** Execution engine — context compilation, agent lifecycle for WO execution, agent delegation, human-task surfacing, Workspace Session management.

## Purpose

Work Order Runtime is the engine that makes Work Orders actually happen. While Orchestrator coordinates what work needs to be done and when, WO Runtime is responsible for the how — assembling context, spawning agents, managing tasks, and reporting results.

The module exists because agent-based execution requires careful orchestration of context, skills, and infrastructure. An agent can't just be "turned on" — it needs the right knowledge (from the hierarchical context), the right capabilities (from Skills), the right permissions (via delegation tokens), and the right environment (Workspace Session). WO Runtime handles all of this, presenting a clean interface to the rest of the platform.

Primary beneficiaries are builders who work in Workspace Sessions (developers, PMs, QA engineers) and the agents that assist them. Both see a consistent experience regardless of which Workbench or Scenario they're working on.

## What this module does

- **Context compilation** — resolve and assemble the context a Work Order needs from the knowledge hierarchy
- **Agent spawning** — spawn Employed Agents from Skilled Agent definitions with full harness (environment, tools, skills, knowledge, delegation)
- **Task tree management** — manage task trees with dependencies, state transitions, and completion tracking
- **Jira integration** — use Jira as the system of record for Work Orders and Tasks via MCP
- **Human-task surfacing** — identify Tasks without Skilled Agents, surface them in the web console and IDE
- **Workspace Session management** — create and manage Coder-based ephemeral dev environments
- **IDE integration** — VS Code plugin for Work Orders Panel, agent chat tabs, and terminal windows
- **Skill injection** — install and load skills from registries into Session containers

## What this module does NOT do

- **Does not route orchestration items** — Orchestrator routes items across Workspaces
- **Does not enforce cross-Workspace gates** — Orchestrator evaluates gate conditions
- **Does not decide what Work Order to create next** — Orchestrator's workflow engine handles this
- **Does not manage Capable Agents or Skills** — Agent Fabric provides the registry and policy
- **Does not provision Workbenches** — Management module handles provisioning

When a Work Order completes, Runtime notifies the Orchestrator so the parent orchestration item can advance.

## Architecture

WO Runtime runs as a **daemon** within each Workspace Session:

```
┌───────────────────────────────────────────────────────────────────────────┐
│                        Workspace Session (Coder)                          │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐ │
│  │                      WO Runtime Daemon                               │ │
│  │                                                                      │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐              │ │
│  │  │ Jira Poller  │  │ Task Manager │  │Agent Spawner │              │ │
│  │  │   (MCP)      │  │              │  │              │              │ │
│  │  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘              │ │
│  │         │                 │                 │                       │ │
│  │         └─────────────────┴─────────────────┘                       │ │
│  │                           │                                          │ │
│  │                    ┌──────┴──────┐                                  │ │
│  │                    │  Completion │──────▶ Orchestrator              │ │
│  │                    │  Reporter   │        (via MQ)                  │ │
│  │                    └─────────────┘                                  │ │
│  └─────────────────────────────────────────────────────────────────────┘ │
│                                                                           │
│  ┌─────────────────────────────────────────────────────────────────────┐ │
│  │                    Employed Agent Processes                          │ │
│  │                                                                      │ │
│  │    ┌─────────────┐   ┌─────────────┐   ┌─────────────┐             │ │
│  │    │   Agent 1   │   │   Agent 2   │   │   Agent N   │             │ │
│  │    │  (Task A)   │   │  (Task B)   │   │  (Task ...)  │             │ │
│  │    └──────┬──────┘   └──────┬──────┘   └──────┬──────┘             │ │
│  │           │                 │                 │                     │ │
│  │           └─────────────────┴─────────────────┘                     │ │
│  │                             │                                        │ │
│  │                      Gateway Policy Layer                           │ │
│  │                       (LLM model calls)                             │ │
│  └─────────────────────────────────────────────────────────────────────┘ │
└───────────────────────────────────────────────────────────────────────────┘
```

**Data flow:**
1. Daemon polls Jira for assigned WOs via MCP
2. Task Manager creates task tree and manages dependencies
3. Agent Spawner instantiates Employed Agents with context and skills
4. Agents execute tasks, creating sub-tasks via Jira MCP
5. Completion Reporter notifies Orchestrator when WO finishes

## Key Components

### Workspace Sessions

Ephemeral development environments for humans and agents to work on Tasks.

| Aspect | Detail |
|--------|--------|
| **Technology** | Coder (similar to GitHub Codespaces) |
| **Template** | Per (Workspace Type, Workbench) — from `.devcontainer/` in Workshop Definition Repo |
| **Ownership** | Owned by one person (not shared) |
| **WO relationship** | Multiple Work Orders can be attached to one Session |
| **Lifecycle** | User explicitly closes; states: Active, Stopped, Archived |

### Knowledge Hierarchy

WO Runtime builds agent context by merging knowledge from multiple levels:

```
┌─────────────────────────────────────────┐
│  Work Order Context                     │  ← Most specific
│  (parent item, WO artifacts, state)     │
├─────────────────────────────────────────┤
│  Workbench Knowledge                    │
│  (product-context, architecture,        │
│   conventions, templates)               │
├─────────────────────────────────────────┤
│  Workshop Knowledge                     │  ← Most general
│  (domain, practices, standards)         │
└─────────────────────────────────────────┘
```

### Agent Fabric Integration

| Concept | WO Runtime Role |
|---------|-----------------|
| **Capable Agent** | Selected based on Skilled Agent definition, with auto-fallback |
| **Skilled Agent** | Read from Scenario definition (local manifest) |
| **Skills** | Installed from [Skill Registry](../agent-fabric/skill-registry.md) at session start |
| **Employed Agent** | Spawned by WO Runtime with delegation token |
| **Gateway Policy** | All model calls routed through configured LLM gateway |

### Jira Integration

Jira is the system of record for Work Orders and Tasks:

| Entity | Jira Representation |
|--------|---------------------|
| Work Order | Epic in Workbench project |
| Root Task | Story under Epic |
| Sub-Task | Sub-task under Story |
| Dependencies | Custom field or linked issues |
| Scenario | Custom field |

WO Runtime accesses Jira through **Jira MCP Server**.

## ACE Concepts Realized

| Concept | How WO Runtime realizes it |
|---------|----------------------------|
| **Work Order** | Executes WOs as units of work |
| **Scenario** | Reads Scenario definitions; spawns agents per Scenario |
| **Task** | Manages Agent Tasks and Human Tasks within WOs |
| **Agent** | Spawns Employed Agents with context and skills |
| **Workspace Session** | Creates and manages Coder-based dev environments |

## Key Design Decisions

- **Agent lifecycle is context-dependent.** Work Order Runtime owns agent lifecycle for Work Order execution. (Release Tools owns it for CI-embedded agents.)
- **Agents are spun up per Scenario.** Not long-lived identities — each Scenario invocation gets its own agent.
- **Context flows with the work.** Work Orders carry their context via the parent orchestration-item graph.
- **Knowledge is hierarchical.** WO Runtime merges Workshop → Workbench → WO context for each agent invocation.
- **Sessions are user-owned.** One person per Session; multiple WOs can be attached.
- **Skills are installed at session launch.** Version resolution happens once; pinned versions recorded for reproducibility.

## Open Questions

- Work Order / orchestration-item graph schema — DAG or cyclic? typed edges?
- Agent runtime topology — process model, isolation, observability
- Per-user vs shared agent infrastructure
- Knowledge caching — how often to refresh from Workshop Definition Repo
- **Control plane strategy** — Build custom vs. extend Symphony vs. extend OpenHands?
- **Agent adapter architecture** — Per-agent adapters vs. unified protocol?
- **Priority Capable Agents** — Which agents to support first?

→ See [Design Discussion](design-discussion-control-plane-and-agent-interfaces.md) for options and trade-offs

## Module Documents

| Document | Content |
|----------|---------|
| [requirements.md](requirements.md) | Implementation requirements (APIs, database, observability) |
| [design-discussion-control-plane-and-agent-interfaces.md](design-discussion-control-plane-and-agent-interfaces.md) | Control plane options and agent interface patterns (decisions needed) |
| [agent_harness_comparison_codex_openhands_goose_cline_aider.md](agent_harness_comparison_codex_openhands_goose_cline_aider.md) | Comparative analysis of agent harness projects |
| [end-to-end-work-order-flow.md](end-to-end-work-order-flow.md) | Complete WO lifecycle from Orchestrator to completion |
| [task-execution.md](task-execution.md) | Task tree, state machine, Jira representation |
| [agent-spawning.md](agent-spawning.md) | Harness preparation and agent spawning |
| [ide-integration.md](ide-integration.md) | VS Code plugin architecture |
| [implementation-todos.md](implementation-todos.md) | Open items for engineering |

## Read Next

- [../orchestrator/README.md](../orchestrator/README.md) — WO creation and routing
- [../agent-fabric/README.md](../agent-fabric/README.md) — Agent infrastructure (Skills, Capable Agents)
- [../management/README.md](../management/README.md) — Workbench provisioning
- [../management/workshop-repository.md](../management/workshop-repository.md) — Workshop Definition Repository structure
- [../../ace/concepts.md](../../ace/concepts.md) — Work Order, Scenario, Task, Agent definitions
