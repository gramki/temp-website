# Work Order Runtime

**Module scope:** Execution engine — context compilation, agent lifecycle for WO execution, agent delegation, human-task surfacing, Workspace Session management.

## What this module does

Work Order Runtime is the execution engine that runs Work Orders. It provides:

- **Context compilation** — resolve and assemble the context a Work Order needs from the knowledge hierarchy
- **Agent lifecycle** — spin up agents per Scenario, configure with skills, manage lifecycle during WO execution
- **Agent delegation** — assign Tasks to agents, orchestrate multi-agent work within a Work Order
- **Human-task surfacing** — identify Tasks waiting on humans, surface them in the IDE
- **Workspace Session management** — create and manage Coder-based ephemeral dev environments for human work
- **Skill injection** — copy skills from Workbench into Session containers at launch

## ACE concepts realized

- **Work Order** — the unit of execution
- **Scenario** — defines the kind of work; agents are spun up per Scenario
- **Task** — Agent Tasks and Human Tasks within a Work Order
- **Orchestration-item graph** — the context source; every Work Order belongs to a graph rooted at its Track's orchestration item
- **Agent** — AI worker with skills, spun up per Scenario
- **Workspace Session** — Coder-based ephemeral dev environment for human work

## What Work Order Runtime does not do

Work Order Runtime executes Workspace Work Orders. It does not route orchestration items, enforce cross-Workspace gates, or decide the next Work Order to create — those are Orchestrator responsibilities. When a Work Order completes, Runtime notifies the Orchestrator so the parent orchestration item can advance.

---

## Workspace Sessions

Workspace Sessions are ephemeral development environments for humans to work on Tasks.

| Aspect | Detail |
|--------|--------|
| **Technology** | Coder (similar to GitHub Codespaces) |
| **Template** | Per (Workspace Type, Workbench) — from `.devcontainer/` in Workshop Definition Repo |
| **Ownership** | Owned by one person (not shared) |
| **WO relationship** | Multiple Work Orders can be attached to one Session |
| **Assignment** | Manual now; Orchestrator may automate later |
| **Lifecycle** | User explicitly closes; states: Active, Stopped, Archived |
| **Time tracking** | Tracks time spent per Work Order in each Session |

### Session Launch Process

When a Workspace Session is created:

```
1. User requests Session for (Workspace Type, Workbench)
2. WO Runtime reads Workshop Definition Repo
3. WO Runtime MERGES Workshop + Workbench workspace content:
   - Base: workshop-{id}/workspaces/{workspace}/
   - Overrides: workshop-{id}/workbenches/{product-code}/workspaces/{workspace}/
   - Index files (skills.yaml, catalog.yaml): MERGED
   - Other files: Workbench REPLACES Workshop if exists
4. WO Runtime re-prepares indexes with merged content
5. WO Runtime provisions Coder workspace using merged devcontainer.json
6. WO Runtime copies merged workspace into Session container
7. Session becomes Active
8. User can attach Work Orders to the Session
```

### Session Configuration Source

All sources are **merged** from Workshop base + Workbench overrides.

| Configuration | Workshop (Base) | Workbench (Override) | Merge Rule |
|---------------|-----------------|----------------------|------------|
| **Container image** | `workspaces/{ws}/.devcontainer/` | `workbenches/{wb}/workspaces/{ws}/.devcontainer/` | File replace |
| **Skills** | `workspaces/{ws}/skills/` | `workbenches/{wb}/workspaces/{ws}/skills/` | Index merged, folders replace |
| **Scenarios** | `workspaces/{ws}/scenarios/` | `workbenches/{wb}/workspaces/{ws}/scenarios/` | Index merged, files replace |
| **Hooks** | `workspaces/{ws}/hooks/` | `workbenches/{wb}/workspaces/{ws}/hooks/` | File replace |

---

## Knowledge Hierarchy and Context Assembly

WO Runtime builds agent context by merging knowledge from multiple levels.

### Hierarchy

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

### Context Assembly Process

When an Agent Task is executed:

```
1. Agent harness receives Task from Scenario
2. Harness identifies required knowledge:
   - WO context: parent orchestration item, related artifacts, current state
   - Workbench knowledge: from workbenches/{product-code}/knowledge/
   - Workshop knowledge: from workshop-{id}/knowledge/
3. Harness identifies required skills:
   - From workbenches/{product-code}/skills/
   - Filtered by Scenario definition (which skills are needed)
4. Harness assembles merged context
5. Harness invokes agent with context + skill + task prompt
```

### Knowledge Sources

| Level | Location in Workshop Definition Repo | Contents |
|-------|--------------------------------------|----------|
| **Workshop** | `knowledge/` | Domain knowledge, practices, standards |
| **Workbench** | `workbenches/{product-code}/knowledge/` | Product context, architecture, conventions |
| **Work Order** | Runtime state | Parent orchestration item artifacts, WO-specific data, current state |

---

## Skill Management

Skills are defined per Workspace at two levels: Workshop (base) and Workbench (overrides).

### Skill Storage

```
Workshop level (base):
workshop-{id}/workspaces/{workspace}/skills/
├── skills.yaml           # Base skill index
├── code-generator/
├── test-writer/
└── ...

Workbench level (overrides):
workshop-{id}/workbenches/{product-code}/workspaces/{workspace}/skills/
├── skills.yaml           # Additional skills (MERGED with Workshop)
├── product-analyzer/     # Workbench-specific skill
└── ...
```

### Skill Injection

At Session launch:
1. WO Runtime reads `skills/` from Workshop workspace (base)
2. WO Runtime reads `skills/` from Workbench workspace (overrides)
3. Merges `skills.yaml` indexes (Workbench entries added to Workshop entries)
4. For skill folders: Workbench replaces Workshop if same name
5. Re-prepares merged `skills.yaml` index
6. Copies merged skills into Session container at `/workspace/skills/`

At Agent Task execution:
1. Scenario specifies which skill(s) to use
2. Agent harness loads skill definition from `/workspace/skills/{skill}/skill.yaml`
3. Harness configures agent with skill's prompts, tools, constraints

---

## Scenario Execution

Scenarios are defined per Workspace in the Workshop Definition Repo.

### Scenario Location

```
workbenches/{product-code}/workspaces/{workspace}/scenarios/
├── catalog.yaml          # Enabled scenarios
└── {scenario}.yaml       # Scenario definitions
```

### Execution Flow

```
1. Orchestrator (or user) triggers Scenario on an orchestration item in a `(Track, Workspace)` context
2. WO Runtime creates Work Order
3. WO Runtime reads Scenario definition
4. For each Task in Scenario:
   a. If Agent Task:
      - Assemble context (knowledge hierarchy)
      - Load skill
      - Invoke agent
      - Capture output
   b. If Human Task:
      - Surface in Workspaces Console / IDE
      - Wait for human completion
5. On WO completion, execute hooks (if defined)
6. Update WO state; notify Orchestrator with orchestration item, Track, Workspace, Scenario, and verdict
```

### Hooks

Shell scripts executed at Work Order lifecycle events.

| Hook | Trigger |
|------|---------|
| `on-wo-start.sh` | When WO starts in this Workspace |
| `on-wo-complete.sh` | When WO completes |

Hooks are defined per Workspace: `workspaces/{workspace}/hooks/`

---

## Key design decisions

- **Agent lifecycle is context-dependent.** Work Order Runtime owns agent lifecycle for Work Order execution. (Release Tools owns it for CI-embedded agents.)
- **Agents are spun up per Scenario.** Not long-lived identities — each Scenario invocation gets its own agent.
- **Context flows with the work.** Work Orders carry their context via the parent orchestration-item graph.
- **Knowledge is hierarchical.** WO Runtime merges Workshop → Workbench → WO context for each agent invocation.
- **Sessions are user-owned.** One person per Session; multiple WOs can be attached.

---

## Open questions

- Work Order / orchestration-item graph schema — DAG or cyclic? typed edges?
- Agent runtime topology — process model, isolation, observability
- Per-user vs shared agent infrastructure
- Skill versioning — how to handle skill updates while Sessions are active
- Knowledge caching — how often to refresh from Workshop Definition Repo

---

## Read next

- [../management/workshop-repository.md](../management/workshop-repository.md) — Workshop Definition Repository structure
- [../management/workbench-architecture.md](../management/workbench-architecture.md) — Workbench architecture
- [../../ace/concepts.md](../../ace/concepts.md) — Work Order, Scenario, Task, Agent definitions
- [../../ace/how-product-evolves/orchestration-items.md](../../ace/how-product-evolves/orchestration-items.md) — orchestration item vs Work Order
- [../../tldr-faq.md](../../tldr-faq.md) — runtime design decisions
