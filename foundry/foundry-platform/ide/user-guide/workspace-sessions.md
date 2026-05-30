# Workspace sessions

## Purpose

Use the Foundry IDE to work in Workspace-specific views, track Work Orders and Tasks, interact with agents, and complete human tasks while you build.

## Audience

Builders — developers, product managers, QA engineers, UX designers, and other Foundry IDE users working in a Workspace Session.

| Role | When to use this guide |
|------|------------------------|
| Developer | Working on Development Workspace tasks, reviewing agent output |
| Product Manager | Reviewing Product Specification Work Orders |
| QA Engineer | Executing and approving QA Workspace tasks |
| Any builder | Understanding how to interact with agents and complete human tasks |

## Prerequisites

- Access to a Workbench and Workspace
- An active Workspace Session (Coder-based ephemeral dev environment)
- Familiarity with [ACE Workspaces](../../../ace/workspaces/README.md) — the six Workspace types

## Builder-facing capabilities

Foundry IDE is the builder-facing interface to Workspaces. In a Workspace Session you can:

- **Workspace-specific views** — each Workspace type (Product Specification, UX Design, Development, QA, Release, Governance) has tailored views
- **Work Order visibility** — Work Orders in flight, progress, status
- **Human Task surfacing** — tasks waiting on the builder
- **Context access** — Product context from UPIM, pre-loaded per Workspace
- **Context refinement** — builders can add or refine context in Work Orders

## Work Orders Panel

The Work Orders Panel displays your assigned Work Orders and their task trees.

### What you see

| Element | Meaning |
|---------|---------|
| **Work Order row** | A WO assigned to your Workbench with type badge (Development, QA, etc.) |
| **Task tree** | Hierarchical breakdown of tasks under each WO |
| **Status badges** | ✓ Completed, ⟳ In Progress, ◯ Ready, ⊗ Blocked |
| **Agent/Human indicator** | Shows whether a task is agent-assigned or awaiting a human |

### Actions available

| Action | When to use |
|--------|-------------|
| **Expand/collapse** | Drill into task details or collapse for overview |
| **Open Chat** | Jump to an agent's chat tab for a running task |
| **Open Terminal** | Jump to an agent's terminal window |
| **Pick Up** | Claim a ready human task |
| **Refresh** | Manually refresh WO state |

### Status meanings

| Status | What it means | Your action |
|--------|---------------|-------------|
| **Ready** | Task can begin — dependencies satisfied | Pick up (human) or wait for agent |
| **In Progress** | Task is actively being worked | Monitor, interact if needed |
| **Blocked** | Waiting on upstream tasks | Check dependencies |
| **Completed** | Task finished successfully | Review if needed |
| **Failed** | Task encountered an error | Review error, retry or escalate |

## Agent Chat Tabs

When an agent executes a task in chat mode, a dedicated chat tab opens.

### What you see

- **Header** — Task ID, agent name, model, current status
- **Message history** — Chronological agent and user messages
- **Input field** — Where you type messages to the agent

### How to interact

| Action | How |
|--------|-----|
| **Send guidance** | Type in the input field and press Send |
| **Provide context** | Paste code, explain requirements, or reference files |
| **Approve changes** | Respond to agent prompts asking for approval |
| **Delegate decisions** | Answer agent questions about ambiguous requirements |
| **Request clarification** | Ask the agent to explain its approach |

### Approval prompts

Agents may pause and ask for approval before:

- Making destructive changes (deleting files, dropping tables)
- Committing code or creating PRs
- External actions (API calls, deployments)

When prompted, review the proposed action and respond with approval or rejection.

### Actions menu

The chat tab includes an actions menu (⋮) with:

| Option | Effect |
|--------|--------|
| **Cancel** | Stop agent execution |
| **Pause** | Suspend agent (if supported) |
| **View logs** | See detailed execution logs |

## Agent Terminal Windows

Terminal-based agents appear in dedicated terminal windows.

### What you see

- **Terminal header** — Task ID and agent CLI name
- **Process output** — Agent's stdout/stderr as it works
- **Cursor prompt** — For direct input when needed

### Observable activity

Terminal windows let you watch agent execution in real time:

- File operations and edits
- Test runs and their output
- Build commands and results
- Error messages and stack traces

### Interacting with terminal agents

| Action | How |
|--------|-----|
| **Send input** | Type directly at the terminal prompt |
| **Scroll history** | Review full execution log |
| **Copy output** | Select and copy for reference |
| **Cancel** | Ctrl+C or close the terminal |

## Human Tasks

Human Tasks are work items that require builder action — either because no agent has the required skill, or the Scenario explicitly requires human judgment.

### How they surface

Human Tasks appear in the Work Orders Panel marked with **[Human]**. You'll also receive notifications when:

- A new human task becomes ready
- A task is escalated from an agent to you
- A task is blocked on your input

### How to complete them

1. **Find the task** — Look in the Work Orders Panel for tasks marked [Human] with status Ready
2. **Pick up the task** — Click "Pick Up" to claim it and transition to In Progress
3. **Do the work** — Complete the task using your tools, expertise, and judgment
4. **Mark complete** — Click "Complete" when done; the system updates Jira and unblocks downstream tasks

### Escalated tasks

If an agent encounters something beyond its capability, it may escalate to a human. Escalated tasks appear with context about:

- What the agent attempted
- Why it escalated
- Relevant files or state

## Notifications

The IDE notifies you of key events:

| Event | Notification |
|-------|--------------|
| New WO assigned | "New Work Order: WO-567 assigned to you" |
| Task ready | "Task TASK-892 is now ready" |
| Agent needs input | "Agent on TASK-892 is waiting for your input" |
| Task completed | "Task TASK-892 completed successfully" |
| Task failed | "Task TASK-892 failed: [error summary]" |
| WO completed | "Work Order WO-567 completed" |

## Scenario Editor

The Foundry IDE includes a Scenario Editor extension for authoring and editing Scenarios in Work Catalogs.

### Opening the Scenario Editor

1. **Command Palette:** Cmd/Ctrl+Shift+P → "Scenario: Open Editor"
2. **Work Catalog Explorer:** Cmd/Ctrl+Shift+W → navigate to scenario file → double-click
3. **Context menu:** Right-click a `.yaml` file in a Work Catalog folder → "Edit as Scenario"

### Creating a new Scenario

| Step | Action |
|------|--------|
| 1. Open Work Catalog Explorer | Cmd/Ctrl+Shift+W |
| 2. Navigate to target folder | `work-catalog/{track}/{oi}/{workspace}/scenarios/` |
| 3. Create new file | Right-click → "New Scenario" |
| 4. Choose template or start blank | Select from template gallery |

The editor opens with schema-aware editing enabled.

### Editor capabilities

| Feature | What it does |
|---------|--------------|
| **Autocomplete** | Suggests valid field names and values as you type |
| **Type validation** | Flags type mismatches immediately |
| **Hover documentation** | Shows field descriptions on hover |
| **Quick fixes** | Offers one-click fixes for common errors |
| **Skill browser** | Cmd/Ctrl+K → browse available skills |
| **Schema outline** | Sidebar shows scenario structure |

### Validation

Run full validation from the Command Palette:

```
Scenario: Validate
```

Or use the CLI:

```bash
foundry scenario validate ./scenarios/implement-feature.yaml
```

The validator checks:
- Schema conformance
- Required fields present
- Skill references exist in registry
- Name uniqueness within workspace

### Quick reference: Scenario structure

```yaml
apiVersion: scenario/v1
name: implement-feature
workspace: development
scope: workspace-ingress

inputs:
  - name: specification_id
    type: string
    required: true

outputs:
  - name: implementation_pr_url
    type: string

required-skills:
  - code-generation
  - test-writing

tasks:
  - id: analyze
    type: agent
  - id: implement
    type: agent
    depends-on: [analyze]
```

For complete authoring guidance, see [Authoring Scenarios](../../work-catalogues/user-guide/authoring-scenarios.md).

## Technical direction

- Based on **VS Code**
- Think **GitHub Codespaces**, but for agentic software work
- Per-builder, per-Workspace sessions
- At runtime, the VS Code Workspace *is* the Foundry Workspace for that builder

## Related

### Concepts

- [Workspace Session](../../concepts/workspace-session.md) — Ephemeral development environment
- [Work Order](../../concepts/work-order.md) — Instantiation of a Scenario for execution
- [Task](../../concepts/task.md) — Unit of work completed by human-agent teams
- [Scenario](../../concepts/scenario.md) — Ingress contract defining what work a Workspace accepts
- [Builder](../concepts/builder.md) — Human user of the Foundry IDE (module-specific)
- [Workspace Views](../concepts/workspace-views.md) — Per-Workspace-type UI customizations (module-specific)

### Guides

- [IDE README](../README.md) — IDE scope and design decisions
- [Extensions spec](../platform-developer-guide/extensions.md) — plugin architecture and protocols
- [IDE integration spec](../../work-order-runtime/platform-developer-guide/ide-integration.md) — implementation details for platform developers
- [ACE Workspaces](../../../ace/workspaces/README.md) — the six Workspace types

## Troubleshooting

| Symptom | Likely cause | What to do |
|---------|--------------|------------|
| Work Orders not appearing | WO Runtime daemon not running | Restart Workspace Session |
| Agent chat not responding | Agent process crashed | Check terminal for errors, retry task |
| Human task stuck in Ready | Jira sync delay | Click Refresh in Work Orders Panel |
| Can't pick up task | Task assigned to another builder | Check Jira for current assignee |
