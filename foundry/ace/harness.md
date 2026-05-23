# Agent harness taxonomy

“Harness” is often used too narrowly:

```
context → tools → edit → run tests → recover
```

The fuller definition should include the **whole execution envelope** around the model.

## Agent harness capabilities

### 1. Local execution loop

The classic coding-agent harness:

| Capability | Example |
| --- | --- |
| Context discovery | Finds relevant files, symbols, tests |
| Tool use | grep, AST search, shell, browser, MCP |
| Patch application | Edits files cleanly |
| Test execution | Runs build/tests/lint |
| Error recovery | Interprets failures and retries |
| Permissioning | Ask/allow/deny commands |
| Rollback | Revert bad changes |
| Session memory | Maintains working hypotheses |

This is where Claude Code and Codex are often discussed.

### 2. Work orchestration harness

This is what I underweighted:

| Capability | Example |
| --- | --- |
| Remote sessions | Start or continue an agent away from local machine |
| Background execution | Agent works while developer is not actively driving |
| Parallel agents | Run multiple agents/subagents/fleets |
| Swarm/fleet management | Assign subtasks, compare outputs, coordinate work |
| Work queue integration | Pick up tasks from issues, tickets, specs, PRs |
| Agent state tracking | See what each agent is doing |
| Human intervention | Pause, redirect, approve, kill, merge |
| Artifact routing | Convert work into branches, diffs, PRs, summaries |

This is also harness. For an engineering organization, it may become the **more important** harness layer.

### 3. Governance harness

Another major layer:

| Capability | Example |
| --- | --- |
| Identity and auth | Which human/agent did what |
| Policy enforcement | What repos/tools/secrets can be accessed |
| Audit logs | Reconstruct agent actions |
| Approval workflows | Require human approval for sensitive operations |
| Environment isolation | Devcontainers, remote sandboxes, ephemeral workspaces |
| Cost/rate controls | Budget per agent/task/team |
| Data boundary controls | Prevent leakage to external models/tools |
| Compliance evidence | Export logs to SIEM/GRC |

This is where enterprise adoption will be decided.

### 4. Collaboration harness

Also real:

| Capability | Example |
| --- | --- |
| PR review collaboration | Agent comments, fixes, responds |
| Multi-user sessions | Human and agent share context |
| Handoff | One engineer starts; another continues |
| Agent-to-agent delegation | Planner agent, implementer agent, reviewer agent |
| Shared instructions | Repo/org/team-level rules |
| Knowledge capture | Decision notes, rationale, summaries |

This is not “model quality.” It is product/system design.

## Where does that leave Copilot?

This strengthens the case that Copilot may not be inferior at all.

If Copilot CLI has better:

- remote sessions
- fleet/swarm orchestration
- background task execution
- GitHub-native task routing
- PR lifecycle control
- review/fix loops
- enterprise identity/policy/audit

then it may have a **superior orchestration harness**, even if Claude Code or Codex feel better for local pair-programming.

### The correct distinction

**Claude/Codex** may be stronger as **local coding harnesses** — one engineer, one repo, one terminal, tight reasoning/edit/test loop.

**Copilot** may be stronger as an **engineering-work orchestration harness** — many tasks, many agents, remote sessions, PRs, reviews, fleet/subagent execution, organization-wide policy and traceability.

That is not a minor difference. It may be strategically bigger.

## Comparison by harness layer

| Harness layer | Claude Code | Codex CLI | Copilot CLI |
| --- | --- | --- | --- |
| Local interactive repo loop | Very strong | Strong | Possibly strong; needs direct test |
| Context discovery | Strong reputation | Improving/strong | Needs direct test |
| Patch/test loop | Strong | Strong | Likely capable; needs direct test |
| Lifecycle hooks | Strong concrete feature | Config/sandbox strong | Plugins/hooks emerging (CLI-dependent) |
| Sandbox/approval model | Strong | Very explicit | Exists; assess depth |
| Remote sessions | Less central | Less central | Potentially stronger |
| Parallel/fleet/swarm | Less central | Less central | Potentially stronger |
| Work queue / issue routing | Not core | Not core | Stronger |
| PR/review lifecycle | Available via tools, not core | Available via tools, not core | Stronger |
| Enterprise governance | Depends on wrapper | Depends on wrapper | Stronger if GitHub is control plane |

## Which question are you asking?

**“Which is best for an individual senior engineer sitting in a repo?”**

Test Claude Code or Codex first.

**“Which is best for an engineering organization building an agentic software delivery system?”**

Copilot becomes much more compelling. Remote/fleet/workflow/governance are not side features — they are core harness capabilities.

## The refined answer

A coding-agent system has at least two important harnesses:

1. **Inner-loop harness** — How well does one agent work with one developer inside one repo?
2. **Outer-loop harness** — How well does the platform coordinate many agents, many tasks, many repos, many humans, and many approvals?

Claude Code and Codex may lead on the inner loop.

Copilot may lead on the outer loop.

For an enterprise, the outer loop may matter more than raw local coding feel.
