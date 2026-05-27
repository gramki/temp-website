# Workbench Consoles

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
| [Workspaces Overview](workspaces/workspaces-overview.md) | `workspaces/workspaces-overview.md` | Sessions, capacity, work distribution across workspaces |
| [Product Specification](workspaces/workspace-product-spec.md) | `workspaces/workspace-product-spec.md` | Product Specification workspace work |
| [UX Design](workspaces/workspace-ux-design.md) | `workspaces/workspace-ux-design.md` | UX Design workspace work |
| [Development](workspaces/workspace-development.md) | `workspaces/workspace-development.md` | Development workspace work |
| [QA](workspaces/workspace-qa.md) | `workspaces/workspace-qa.md` | QA workspace work |
| [Release Workspace](workspaces/workspace-release.md) | `workspaces/workspace-release.md` | Release workspace work |
| [Governance Workspace](workspaces/workspace-governance.md) | `workspaces/workspace-governance.md` | Transition validation work |

**Sub-pages:**
- **Workspace Session Details** — `/workbenches/{workbenchId}/sessions/{sessionId}` — Full session activity, work done, time tracking

### Build

| Console | File | Purpose |
|---------|------|---------|
| [CI Console](build/ci-console.md) | `build/ci-console.md` | Build/pipeline status |
| [Components Console](build/components-console.md) | `build/components-console.md` | Ontology — Systems, capabilities |
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
    │   ├── Product Specification
    │   ├── UX Design
    │   ├── Development
    │   ├── QA
    │   ├── Release Workspace
    │   └── Governance Workspace
    ├── Build
    │   ├── CI Console
    │   ├── Components Console
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
