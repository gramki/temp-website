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

### Work Catalog Resolution

WO Runtime resolves Scenarios from the **Work Catalog** hierarchy:

```
Platform Default                    ← work-catalogues/platform-defaults/
└── Foundry Catalog                 ← foundry-{id}/work-catalog/
    └── Workshop Catalog            ← workshop-{id}/work-catalog/
        └── Workbench Catalog       ← workbench settings
            └── User Catalog        ← user-work-catalog-{id}/ (if activated)
```

**Resolution rules:**
- Closest wins: User → Workbench → Workshop → Foundry → Platform
- Scenarios at lower levels override (not merge with) parent levels
- User catalog must be explicitly activated (see below)

**User catalog activation:**
| Method | Description |
|--------|-------------|
| **Session flag** | Per-session opt-in via Workspace Session settings |
| **User profile** | Persistent preference in user profile settings |

When user catalog is active, the user's personal `user-work-catalog-{id}/` repository is included in resolution. This allows builders to experiment with Scenario modifications without affecting team workflows.

→ [../work-catalogues/README.md](../work-catalogues/README.md) — Work Catalog overview
→ [../management/platform-developer-guide/work-catalog-management/resolution-algorithm.md](../management/platform-developer-guide/work-catalog-management/resolution-algorithm.md) — Full resolution algorithm

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
| **Skills** | Installed from [Skill Registry](../agent-fabric/platform-developer-guide/skill-registry.md) at session start |
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

- **Work Catalog is the source for Scenarios.** Scenarios are resolved from the Work Catalog hierarchy (Platform → Foundry → Workshop → Workbench → User). This enables org-wide defaults with product-specific overrides.
- **User catalogs are opt-in.** Builders must explicitly activate their personal Work Catalog (per session or in profile) to include it in resolution. This prevents accidental interference with team workflows.
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

→ See [platform-developer-guide/design-discussions/control-plane-and-agent-interfaces.md](platform-developer-guide/design-discussions/control-plane-and-agent-interfaces.md) for options and trade-offs

## Key Concepts

### Platform-wide concepts

These concepts are defined centrally and used across Foundry modules:

| Concept | What WO Runtime does with it |
|---------|------------------------------|
| [Work Order](../concepts/work-order.md) | Executes WOs as units of work |
| [Task](../concepts/task.md) | Manages Agent Tasks and Human Tasks within WOs |
| [Scenario](../concepts/scenario.md) | Reads definitions; spawns agents per Scenario |
| [Agent Model](../concepts/agent-model.md) | Spawns Employed Agents with context and skills |
| [Workspace Session](../concepts/workspace-session.md) | Creates and manages Coder-based dev environments |
| [Delegation](../concepts/delegation.md) | Issues delegation tokens for Employed Agents |
| [Work Catalog](../concepts/work-catalog.md) | Resolves Scenarios from hierarchy |
| [Knowledge Hierarchy](../concepts/knowledge-hierarchy.md) | Merges Workshop → Workbench → WO context |

### Module-specific concepts

These concepts describe WO Runtime internals:

| Concept | Definition |
|---------|------------|
| [WO Runtime Daemon](concepts/wo-runtime-daemon.md) | Long-running process that coordinates WO execution |
| [Task Manager](concepts/task-manager.md) | Manages task trees, dependencies, and state transitions |
| [Agent Spawner](concepts/agent-spawner.md) | Prepares harnesses and spawns Employed Agents |
| [Context Compilation](concepts/context-compilation.md) | Assembles hierarchical knowledge into agent context |
| [Completion Reporter](concepts/completion-reporter.md) | Notifies Orchestrator when Work Orders complete |
| [Local State Store](concepts/local-state-store.md) | Per-session SQLite database for WO and task state |

→ [concepts/README.md](concepts/README.md) — Full module concept index

## Documentation

| Guide | Audience | Index |
|-------|----------|-------|
| Concepts | Anyone | This README, [concepts/](concepts/) |
| [User guide](user-guide/) | Admins, builders | Task-oriented usage |
| [Foundry Platform developer guide](platform-developer-guide/) | Platform engineers | Implementation specs |

## Read Next

- [../orchestrator/README.md](../orchestrator/README.md) — WO creation and routing
- [../agent-fabric/README.md](../agent-fabric/README.md) — Agent infrastructure (Skills, Capable Agents)
- [../management/README.md](../management/README.md) — Workbench provisioning
- [../management/platform-developer-guide/workshop-repository.md](../management/platform-developer-guide/workshop-repository.md) — Workshop Definition Repository structure
- [../../ace/concepts.md](../../ace/concepts.md) — Work Order, Scenario, Task, Agent definitions
