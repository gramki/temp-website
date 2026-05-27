# Workbench Consoles

Consoles are focused views accessible from the Workbench Home side navigation.

## Console Groups

### Work

| Console | File | Purpose |
|---------|------|---------|
| [PI Console](pi-console.md) | `pi-console.md` | Discovery Cases, Product Intent types, Strategy Frame, Traceability Maps |
| [Workspaces Console](workspaces-console.md) | `workspaces-console.md` | 6 Workspaces, Work Orders |
| [Progress Console](progress-console.md) | `progress-console.md` | Completion analytics, burndown |
| [Track Console](track-console.md) | `track-console.md` | Per-Track work analytics |

### Build

| Console | File | Purpose |
|---------|------|---------|
| [CI Console](ci-console.md) | `ci-console.md` | Build/pipeline status |
| [Components Console](components-console.md) | `components-console.md` | Ontology — Systems, capabilities |
| [Quality Status](quality-status.md) | `quality-status.md` | Test results, coverage |
| [Release Console](release-console.md) | `release-console.md` | Deployments, Weave integration |

### Resources

| Console | File | Purpose |
|---------|------|---------|
| [Repositories & Tools](repositories-tools.md) | `repositories-tools.md` | Git repos, external tools |

### Workforce

| Console | File | Purpose |
|---------|------|---------|
| [Team Console](team-console.md) | `team-console.md` | Team analytics, contributions |
| [Agent Console](agent-console.md) | `agent-console.md` | Agent activity, performance |

### Governance

| Console | File | Purpose |
|---------|------|---------|
| [Governance Overview](governance-overview.md) | `governance-overview.md` | Governance health, attention queue, pending approvals |
| [Rituals](rituals-console.md) | `rituals-console.md` | Governance Ritual calendar, inputs, outputs, action items |
| [Controls & Enforcement](controls-enforcement.md) | `controls-enforcement.md` | Control Objectives, indicators, thresholds, enforcement outcomes |
| [Registers](registers-console.md) | `registers-console.md` | Risk, debt, exceptions, compliance, findings |
| [Reports & Dashboards](reports-console.md) | `reports-console.md` | Governance dashboards, ritual inputs, audit exports |
| [Quality Controls](quality-compliance.md) | `quality-compliance.md` | Build/release quality controls and threshold evaluation |

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
    │   ├── PI Console
    │   ├── Workspaces Console
    │   ├── Progress Console
    │   └── Track Console
    ├── Build
    │   ├── CI Console
    │   ├── Components Console
    │   ├── Quality Status
    │   └── Release Console
    ├── Resources
    │   └── Repositories & Tools
    ├── Workforce
    │   ├── Team Console
    │   └── Agent Console
    ├── Governance
    │   ├── Governance Overview
    │   ├── Rituals
    │   ├── Controls & Enforcement
    │   ├── Registers
    │   ├── Reports & Dashboards
    │   └── Quality Controls
    └── Settings
        ├── Admin Console
        └── Governance Admin
```
