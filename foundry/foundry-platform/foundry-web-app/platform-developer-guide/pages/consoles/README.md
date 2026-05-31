# Workbench Consoles (Developer Guide)

Consoles are focused views accessible from the Workbench Home side navigation.

For guidance on when to use console groups — and when to add a new console instead of expanding an existing one — see [CONSOLE-GUIDE.md](CONSOLE-GUIDE.md).

## Console Groups

### Work

| Console | File | Purpose |
|---------|------|---------|
| [Work Overview](work/work-overview.md) | `work/work-overview.md` | Attention queue, blocked items, due soon, navigation |
| [Orchestration](work/orchestration-console.md) | `work/orchestration-console.md` | All orchestration items (PI, Discovery Case, Release Intent) |
| [Progress](work/progress-console.md) | `work/progress-console.md` | By Orchestration/Track/Workspace/Initiative/Release; Burndown; Say/Do |
| [Rituals](work/work-rituals.md) | `work/work-rituals.md` | Standups; Sprint (Build); Kanban (Discovery, Run, Win, Evolve) |
| [My Work](work/my-work.md) | `work/my-work.md` | My Day / My Week / My Month |

**Sub-pages:**
- **Orchestration Item Details** — `/workbenches/{workbenchId}/orchestration/{type}/{itemId}` — Full item detail (see [Orchestration](work/orchestration-console.md))

### Workspaces

| Console | File | Purpose |
|---------|------|---------|
| [Workspaces Overview](workspaces/workspaces-overview.md) | `workspaces/workspaces-overview.md` | Unified workspace-type cards and session visibility |
| [Infrastructure](workspaces/workspace-infrastructure.md) | `workspaces/workspace-infrastructure.md` | Running pods, cluster placement, and resource totals |
| [Agents](workspaces/workspace-agents.md) | `workspaces/workspace-agents.md` | Workbench-wide agent, skill, and token usage |

**Sub-pages:**
- **[Workspace Session Details](workspaces/workspace-session-details.md)** — `/workbenches/{workbenchId}/sessions/{sessionId}` — Canonical session contract (overview, linked WOs, coder pod, employed agents, token usage, activity)

### Build

| Console | File | Purpose |
|---------|------|---------|
| [CI Console](build/ci-console.md) | `build/ci-console.md` | Build/pipeline status |
| [Components Console](build/components-console.md) | `build/components-console.md` | Ontology — Systems, capabilities; Supply Chain (SBOM, dependencies) |
| [Findings Console](build/findings-console.md) | `build/findings-console.md` | Vulnerabilities, license violations, code quality, policy violations |
| [Quality Status](build/quality-status.md) | `build/quality-status.md` | Test results, coverage |
| [Release Artifacts](build/release-artifacts.md) | `build/release-artifacts.md` | Versions, deployments, Weave integration |

### Workforce

| Console | File | Purpose |
|---------|------|---------|
| [Workforce Overview](workforce/workforce-overview.md) | `workforce/workforce-overview.md` | Team + Agent summary, capacity |
| [Team Console](workforce/team-console.md) | `workforce/team-console.md` | People, roles, kudos, capacity |
| [Agent Console](workforce/agent-console.md) | `workforce/agent-console.md` | Agents, metrics, performance |

**Sub-pages:**
- **Team Member Workbench Profile** — `/workbenches/{workbenchId}/team/{memberId}` — Full activity history and metrics (see [Team Console](workforce/team-console.md))

### Governance

| Console | File | Purpose |
|---------|------|---------|
| [Governance Overview](governance/governance-overview.md) | `governance/governance-overview.md` | Governance health, attention queue, pending approvals |
| [Rituals](governance/rituals-console.md) | `governance/rituals-console.md` | Governance Ritual calendar, inputs, outputs, action items |
| [Controls & Enforcement](governance/controls-enforcement.md) | `governance/controls-enforcement.md` | Control Objectives, indicators, thresholds, enforcement outcomes |
| [Registers](governance/registers-console.md) | `governance/registers-console.md` | Risk, debt, exceptions, compliance, findings |
| [Reports & Dashboards](governance/reports-console.md) | `governance/reports-console.md` | Governance dashboards, ritual inputs, audit exports |
| [Quality Controls](governance/quality-compliance.md) | `governance/quality-compliance.md` | Build/release quality controls and threshold evaluation |

### Resources

| Console | File | Purpose |
|---------|------|---------|
| [Repositories & Tools](resources/repositories-tools.md) | `resources/repositories-tools.md` | Git repos, external tools |

### Settings

| Console | File | Purpose |
|---------|------|---------|
| [Admin Console](settings/admin-console.md) | `settings/admin-console.md` | Workbench configuration |
| [Governance Admin](settings/governance-admin.md) | `settings/governance-admin.md` | Governance authority, controls, inheritance, rituals, registers |

## URL Pattern

All consoles follow: `/workbenches/{workbenchId}/consoles/{consoleId}`

## Navigation

```
Workbench Home
└── Side Nav
    ├── Work
    │   ├── Work Overview
    │   ├── Orchestration
    │   ├── Progress
    │   ├── Rituals
    │   └── My Work
    ├── Workspaces
    │   ├── Workspaces Overview
    │   ├── Infrastructure
    │   └── Agents
    ├── Build
    │   ├── CI Console
    │   ├── Components Console
    │   ├── Findings Console
    │   ├── Quality Status
    │   └── Release Artifacts
    ├── Workforce
    │   ├── Workforce Overview
    │   ├── Team Console
    │   └── Agent Console
    ├── Governance
    │   ├── Governance Overview
    │   ├── Rituals
    │   ├── Controls & Enforcement
    │   ├── Registers
    │   ├── Reports & Dashboards
    │   └── Quality Controls
    ├── Resources
    │   └── Repositories & Tools
    └── Settings
        ├── Admin Console
        └── Governance Admin
```
