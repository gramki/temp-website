# Workbench Home Page

**URL pattern:** `/workbenches/{workbenchId}`

**Purpose:** Central dashboard for a Product's Workbench; primary landing page for day-to-day work.

---

## Target Users

- Workbench Managers
- Workbench Members (Builders)
- Product Managers, QA, UX, Release teams working on this Product

---

## Page Layout

```
┌─────────────────────────────────────────────────────────────────────┐
│  Header: Product Name │ Product Code │ Workshop │ Quick Stats       │
├─────────────────────────────────────────────────────────────────────┤
│  PI Badges (top row): [PI-039] [PI-041] [PI-042] ...                │
├─────────────┬───────────────────────────────────────────────────────┤
│             │                                                       │
│  Side Nav   │              Workbench Wall                           │
│  (Consoles) │                                                       │
│             │  - Persona-specific summary                           │
│  Work       │  - Due Today                                          │
│  Build      │  - Chronological updates                              │
│  Resources  │  - Upcoming Deadlines                                 │
│  Workforce  │                                                       │
│  Governance │                                                       │
│  Settings   │                                                       │
│             │                                                       │
└─────────────┴───────────────────────────────────────────────────────┘
```

---

## Page Sections

### 1. Header

| Element | Description |
|---------|-------------|
| Product name | UPIM Product name |
| Product Code | Assigned by Olympus Weave |
| Workshop | Parent Workshop (link) |
| Quick stats | Active Work Orders, pending Tasks, recent deployments |

### 2. PI Badges (Top Row)

Active Product Intents displayed as badges, ordered by **oldest start date first**.

```
┌─────────────────────────────────────────────────────────────────────┐
│ ● PI-039 Mobile Auth    │ ● PI-041 Checkout v2   │ ○ PI-042 Rewards │
│   May 1 → Jun 1         │   May 8 → Jun 20       │   May 15 → Jul 10│
│   [Spec✓][UX✓][Dev●]... │   [Spec✓][UX●][Dev○].. │   [Spec●][UX○].. │
└─────────────────────────────────────────────────────────────────────┘
       ↑ Red (at risk)           ↑ Green                 ↑ Green
```

| Element | Description |
|---------|-------------|
| **PI ID + Title** | Identity |
| **Start → Due dates** | Time orientation |
| **Badge color** | Health based on **Governance risk flags** (not algorithmic) |
| **Track/Workspace dots** | Shown by default — where work currently sits |
| **Click action** | Filters Wall to that PI only |
| **Order** | Oldest start date first (left to right) |
| **Default view** | All PIs (Wall unfiltered) |
| **Archived PIs** | Visible in PI Console |

**Constraint:** A Workbench is not expected to have more than ~12 active PIs at any time.

### 3. Workbench Wall (Main Content)

Chronological stream of updates with persona-specific presentation.

| Element | Description |
|---------|-------------|
| **Persona-specific summary** | Tailored highlights based on logged-in user's role |
| **Due Today** | Prominent section — tasks and deadlines for today |
| **Work Done by Date** | Completed items, grouped by date |
| **Upcoming Deadlines** | Near-term due dates across all PIs |
| **Chronological updates** | Work Orders, commits, deployments, approvals |

**Filters:**
- By PI (via badge click)
- By Workspace
- By persona/role
- By date range

### 4. Side Navigation (Consoles)

Grouped consoles for focused views.

---

## Console Groups

### Work

| Console | Purpose |
|---------|---------|
| **PI Console** | Signals, Objectives, Initiatives, Discovery flow, Product Intents |
| **Workspaces Console** | 6 Workspace views, active Work Orders per Workspace |
| **Progress Console** | Work completion analytics, burndown |
| **Track Console** | Per-Track work analytics (Discovery, Build, etc.) |

### Build

| Console | Purpose |
|---------|---------|
| **CI Console** | Build/pipeline status, build history |
| **Components Console** | Ontology navigation — Systems, capabilities, features |
| **Quality Status** | Test pass/fail rates, coverage, automation health |
| **Release Console** | Deployment status, release history, Weave integration |

### Resources

| Console | Purpose |
|---------|---------|
| **Repositories & Tools** | Intent/Design/Code repos, external tools (Figma, TestRail, Jira) |

### Workforce

| Console | Purpose |
|---------|---------|
| **Team Console** | Team analytics — contributions, workload |
| **Agent Console** | Agent activity analytics — utilization, performance |

### Governance

| Console | Purpose |
|---------|---------|
| **Risk Console** | Governance risk flags (drives PI badge colors) |
| **Reports Console** | Generated reports, audit exports |
| **Quality Compliance** | Required thresholds, audit evidence, sign-offs |

### Settings

| Console | Purpose |
|---------|---------|
| **Admin Console** | Workbench settings, team management, integrations |

---

## Navigation

| Target | Path |
|--------|------|
| Foundry Home | Breadcrumb → `/` |
| Workshop Home | Breadcrumb → `/workshops/{workshopId}` |
| Console | Side nav → `/workbenches/{workbenchId}/{consoleId}` |
| PI Details | Badge click or PI Console → `/workbenches/{workbenchId}/intents/{piId}` |
| Work Order | Wall item → `/workbenches/{workbenchId}/work-orders/{woId}` |
| IDE | "Open in IDE" → Launches Foundry IDE with Workspace context |

---

## Access Control

| Role | Access |
|------|--------|
| Foundry Admin | Full access |
| Workshop Manager | Full access |
| Workbench Manager | Full access, manage team/repos/Scenario Catalogs |
| Workbench Member | View, execute Tasks, create Work Orders |

---

## Actions by Role

### Workbench Manager

| Action | Location |
|--------|----------|
| Manage Team | Admin Console |
| Manage Repositories | Repositories & Tools |
| Manage Scenario Catalogs | Workspaces Console |
| Configure Integrations | Admin Console |
| Review Risks | Risk Console |

### Workbench Member

| Action | Location |
|--------|----------|
| Create Intent | PI Console or Wall |
| Create Work Order | Workspaces Console or Wall |
| Complete Tasks | Wall (Due Today) or Workspaces Console |
| Open IDE | Any Workspace context |
| View Progress | Progress Console, Track Console |

---

## Wall Item Types

| Item Type | Source | Display |
|-----------|--------|---------|
| Work Order created | Orchestrator | PI, Workspace, creator |
| Work Order completed | Runtime | PI, Workspace, duration |
| Task assigned | Runtime | Assignee, Work Order, due date |
| Task completed | Runtime | Assignee, Work Order |
| Commit | GitHub (Metadata Service) | Repo, author, message |
| PR merged | GitHub | Repo, author, title |
| Build status | CI | Pipeline, status, duration |
| Test results | Quality Status | Pass/fail counts, coverage |
| Deployment | Weave | System, version, region |
| Gate approval | Governance | PI, gate, approver |
| Risk flag raised | Governance | PI, risk type, severity |

---

## Open Questions

- Wall pagination/infinite scroll vs. date-based grouping?
- Notification preferences per Workbench?
- Dashboard customization (reorder consoles, pin items)?
- Keyboard shortcuts for console navigation?
- Mobile/responsive layout considerations?
