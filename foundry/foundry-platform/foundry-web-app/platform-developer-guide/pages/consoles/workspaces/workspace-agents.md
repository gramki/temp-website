# Workspace Agents Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/workspace-agents`

**Purpose:** Workbench-wide view of agent, skill, and token usage across workspace sessions.

---

## Canonical Contract

This console aggregates usage across all workspace sessions in the selected workbench.

### Required views

| View | Behavior |
|------|----------|
| Agent usage summary | Number of active agents and total invocations |
| Skill usage summary | Top skills by invocation volume |
| Token summary | Total tokens and USD cost across sessions |
| Agent list | Per-agent invocation totals, session footprint, and top skills |

### Aggregation scope

- Workbench-wide scope only (across workspace sessions in the same workbench)
- Token cost is USD only
- Skills are aggregated from session employed-agent usage records

---

## Cross-links

- Session drill-down remains in [workspace-session-details.md](workspace-session-details.md) for per-session details.
