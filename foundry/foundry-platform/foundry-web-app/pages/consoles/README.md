# Workbench Consoles

Consoles are focused views accessible from the Workbench Home side navigation.

For guidance on when to use console groups — and when to add a new console instead of expanding an existing one — see [CONSOLE-GUIDE.md](CONSOLE-GUIDE.md).

## Console Groups

### Work

| Console | File | Purpose |
|---------|------|---------|
| [Work Overview](work-overview.md) | `work-overview.md` | Attention queue, blocked items, due soon, navigation |
| [Orchestration](orchestration-console.md) | `orchestration-console.md` | All orchestration items (PI, Discovery Case, Release Intent) |
| [Progress](progress-console.md) | `progress-console.md` | By Orchestration/Track/Workspace/Initiative/Release; Burndown; Say/Do |
| [Rituals](work-rituals.md) | `work-rituals.md` | Standups; Sprint (Build); Kanban (Discovery, Run, Win, Evolve) |
| [My Work](my-work.md) | `my-work.md` | My Day / My Week / My Month |

**Sub-pages:**
- **Orchestration Item Details** — `/workbenches/{workbenchId}/orchestration/{type}/{itemId}` — Full item detail (see [Orchestration](orchestration-console.md))

### Workspaces

| Console | File | Purpose |
|---------|------|---------|
| [Workspaces Overview](workspaces-overview.md) | `workspaces-overview.md` | Sessions, capacity, work distribution across workspaces |
| [Product Specification](workspace-product-spec.md) | `workspace-product-spec.md` | Product Specification workspace work |
| [UX Design](workspace-ux-design.md) | `workspace-ux-design.md` | UX Design workspace work |
| [Development](workspace-development.md) | `workspace-development.md` | Development workspace work |
| [QA](workspace-qa.md) | `workspace-qa.md` | QA workspace work |
| [Release Workspace](workspace-release.md) | `workspace-release.md` | Release workspace work |
| [Governance Workspace](workspace-governance.md) | `workspace-governance.md` | Transition validation work |

**Sub-pages:**
- **Workspace Session Details** — `/workbenches/{workbenchId}/sessions/{sessionId}` — Full session activity, work done, time tracking

### Build

| Console | File | Purpose |
|---------|------|---------|
| [CI Console](ci-console.md) | `ci-console.md` | Build/pipeline status |
| [Components Console](components-console.md) | `components-console.md` | Ontology — Systems, capabilities |
| [Quality Status](quality-status.md) | `quality-status.md` | Test results, coverage |
| [Release Artifacts](release-artifacts.md) | `release-artifacts.md` | Versions, deployments, Weave integration |

### Workforce

| Console | File | Purpose |
|---------|------|---------|
| [Workforce Overview](workforce-overview.md) | `workforce-overview.md` | Team + Agent summary, capacity |
| [Team Console](team-console.md) | `team-console.md` | People, roles, kudos, capacity |
| [Agent Console](agent-console.md) | `agent-console.md` | Agents, metrics, performance |

**Sub-pages:**
- **Team Member Workbench Profile** — `/workbenches/{workbenchId}/team/{memberId}` — Full activity history and metrics (see [Team Console](team-console.md))

### Governance

| Console | File | Purpose |
|---------|------|---------|
| [Governance Overview](governance-overview.md) | `governance-overview.md` | Governance health, attention queue, pending approvals |
| [Rituals](rituals-console.md) | `rituals-console.md` | Governance Ritual calendar, inputs, outputs, action items |
| [Controls & Enforcement](controls-enforcement.md) | `controls-enforcement.md` | Control Objectives, indicators, thresholds, enforcement outcomes |
| [Registers](registers-console.md) | `registers-console.md` | Risk, debt, exceptions, compliance, findings |
| [Reports & Dashboards](reports-console.md) | `reports-console.md` | Governance dashboards, ritual inputs, audit exports |
| [Quality Controls](quality-compliance.md) | `quality-compliance.md` | Build/release quality controls and threshold evaluation |

### Resources

| Console | File | Purpose |
|---------|------|---------|
| [Repositories & Tools](repositories-tools.md) | `repositories-tools.md` | Git repos, external tools |

### Settings

| Console | File | Purpose |
|---------|------|---------|
| [Admin Console](admin-console.md) | `admin-console.md` | Workbench configuration |
| [Governance Admin](governance-admin.md) | `governance-admin.md` | Governance authority, controls, inheritance, rituals, registers |

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
