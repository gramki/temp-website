# PI Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/pi`

**Group:** Work

**Purpose:** Product Management control surface for the Workbench — triage unprocessed Signals, maintain Objectives and Initiatives, observe Discovery Track conversion, and track Product Intents as they move into Product Specification and onward through the ACE Product Evolution Cycle.

---

## Key Concepts

| Term | Definition |
|------|------------|
| **Signal** | UPIM Dim 1 input: Problem, Need, or Opportunity. A Signal is an observation to investigate, not a requirement or delivery commitment. |
| **Unprocessed Signal** | A Signal in `New` or `Triaged` state that has not yet been explored, associated with an Initiative, parked, addressed, or dismissed. |
| **Objective** | Strategic goal over a planning horizon; answers "where are we going?" |
| **Initiative** | Cross-track strategic program that advances Objectives, associates Signals, declares lever mix, and carries embedded targets. |
| **Idea** | Hypothesis spawned from one or more Signals and validated through Discovery Track work. |
| **PDR** | Product Decision Record: Go / Kill / Pivot decision that records evidence and may trigger PSDs, Modeling Tasks, or Initiative changes. |
| **PSD** | Product Specification Document: the validated contract between Product and Engineering, authored through Specification Tasks and executed in the Product Specification Workspace. |
| **Product Intent** | ACE asset that flows through Workspaces. Discovery produces the decision/specification basis; Product Intent then triggers Product Specification Workspace scenarios. |

---

## Page Layout

```
┌─────────────────────────────────────────────────────────────────────┐
│ STRATEGIC CONTEXT                                                   │
│   Objectives: OBJ-12 LATAM Coverage │ OBJ-13 Activation Velocity     │
│   Initiatives: INIT-04 LATAM Entry [Product 40% | GTM 25% | ...]    │
├─────────────────────────────────────────────────────────────────────┤
│ SIGNAL INTAKE                                                       │
│   [New (12)] [Triaged (8)] [Exploring (5)] [Parked (9)]             │
│   • SIG-231 Need — Batch payout file upload              [Triage]   │
│   • SIG-244 Problem — FX rate-lock flow too slow         [Triage]   │
├─────────────────────────────────────────────────────────────────────┤
│ DISCOVERY FLOW                                                      │
│   Signals → Ideas → PDRs → PSDs → Product Intent                    │
│   18 unprocessed │ 5 exploring │ 3 ideas validating │ 2 PSD drafts  │
├─────────────────────────────────────────────────────────────────────┤
│ PRODUCT INTENTS                                                     │
│   [Active] [Archived] [All]                                         │
│   PI-039 LATAM Currency Support [Spec✓][UX●][Dev○][QA○][Rel○]      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Page Sections

### 1. Strategic Context

The top of the console shows the Product Management frame for the Workbench. This is where managers see the goals and macro initiatives that determine how the Product should evolve.

| Element | Description |
|---------|-------------|
| **Active Objectives** | Current Objectives for the Workbench's Product, grouped by planning horizon |
| **Objective status** | Draft, Active, Achieved, Deferred |
| **Objective success criteria** | Measurable criteria and constraints that guide prioritization |
| **Initiatives** | Active or approved Initiatives pursuing the Objectives |
| **Lever mix** | Initiative allocation across Product, GTM, Sales Enablement, Customer Success, Operational |
| **Embedded targets** | Initiative targets tied to Win Outcomes and Business KPIs |
| **Signal coverage** | Count of associated Signals by Initiative and Signal type |

**Primary behavior:**
- Clicking an Objective filters the console to its Initiatives, associated Signals, Ideas, PDRs, PSDs, and Product Intents.
- Clicking an Initiative opens a side panel with scope, lever mix, targets, associated Signals, active Discovery work, and downstream Product Intents.
- Objectives and Initiatives are strategic context; Work Orders for specification and downstream execution are created through the relevant Workspaces.

### 2. Signal Intake

Signals are the intake surface for discovery. The console emphasizes Signals that have not yet been processed: captured and acknowledged candidates that Product Management must triage, associate, park, dismiss, or send into exploration.

| Element | Description |
|---------|-------------|
| **New Signals** | Captured but not yet reviewed |
| **Triaged Signals** | Reviewed and acknowledged as legitimate, but not yet committed to exploration or association |
| **Signal type** | Problem, Need, Opportunity |
| **Source** | Customer, Prospect, Internal - Engineering, Internal - Operations, Internal - Strategy, Internal - Support, Data/Analytics |
| **Age** | Time since Date Captured; highlights stale unprocessed Signals |
| **Related Signals** | Potential duplicates or clustered Signals |
| **Suggested Initiative** | Candidate Initiative based on tags, source, affected module, or PM association |

**Unprocessed definition:** Signals in `New` or `Triaged` state. Once a Signal moves to `Exploring`, `Associated`, `Parked`, `Addressed`, or `Dismissed`, it is no longer counted as unprocessed.

**Signal row:**

| Element | Description |
|---------|-------------|
| **Signal ID + title** | Identity and short description |
| **Type badge** | Problem / Need / Opportunity |
| **Status** | New or Triaged in the default intake view |
| **Source and reporter** | Where the Signal came from |
| **Upvotes / affected customers** | Demand or impact indicator where available |
| **Affected entity** | Module, Capability, or Feature for Problems; blank where not applicable |
| **Actions** | Triage, Associate to Initiative, Start Exploration, Park, Dismiss |

### 3. Discovery Flow

The Discovery Flow section shows how Signals are converted into buildable direction. It does not replace Track Console analytics; it gives Product Managers the specific Signal -> Idea -> PDR -> PSD -> Product Intent chain for this Workbench.

```
Signal
  └── Signal Exploration Task
        └── Idea
              └── Research / Experiment / Prototype / Deliberation
                    └── PDR (Go / Kill / Pivot)
                          ├── PSD(s)
                          ├── Modeling Task(s)
                          └── Product Intent
```

| Stage | What the PI Console shows |
|-------|---------------------------|
| **Signals** | New, Triaged, Exploring, Associated, Parked, Addressed, Dismissed |
| **Exploration** | Signal Exploration Tasks and their open questions |
| **Ideas** | Proposed / Investigating / Validated / Killed hypotheses |
| **Evidence** | Research Tasks, Experiments, Prototypes / Spikes, Deliberations |
| **PDRs** | Draft / Final / Superseded decisions with Go / Kill / Pivot type |
| **PSDs** | Draft / In Technical Review / Approved / Superseded / Cancelled specification documents |
| **Product Intent** | Active and archived ACE Product Intents generated from the accepted discovery/specification basis |

### 4. Product Intents

Product Intents remain visible in the PI Console, but they are shown as the downstream flow of accepted direction rather than the only object on the page.

| Element | Description |
|---------|-------------|
| **Active PIs** | Product Intents currently moving through Workspaces |
| **Archived PIs** | Completed or shipped Product Intents |
| **View toggle** | Active / Archived / All |
| **Sort options** | By start date, due date, health, Objective, Initiative |
| **Search** | Find by PI ID, title, source Signal, PDR, PSD, Objective, or Initiative |

### 5. PI Card (List Item)

| Element | Description |
|---------|-------------|
| **PI ID + title** | Product Intent identity |
| **Source chain** | Signal(s) -> Idea -> PDR -> PSD(s), where available |
| **Objective / Initiative** | Strategic context that explains why the PI exists |
| **Start -> due dates** | Time orientation |
| **Health badge** | Color from Governance risk flags |
| **Workspace progress** | `[Spec✓][UX●][Dev○][QA○][Rel○][Gov○]` |
| **Active Work Orders** | Count of in-progress WOs across Workspaces |
| **Last activity** | Most recent update |

### 6. PI Detail View (Drill-down)

| Element | Description |
|---------|-------------|
| **Overview** | Title, description, owner, dates, current Workspace |
| **Strategic context** | Objective, Initiative, lever mix, embedded targets |
| **Traceability** | Source Signals, Ideas, PDRs, PSDs |
| **Discovery evidence** | Research, experiments, prototypes, deliberations that support the PDR |
| **Specification content** | PSD links and status; PSD is the contract for Product Specification and Build work |
| **Workspace timeline** | Visual flow through ACE Workspaces |
| **Work Orders** | All WOs for this PI, grouped by Workspace |
| **Artifacts** | Designs, code repositories, test suites, release artifacts |
| **History** | Audit trail of decisions, transitions, and status changes |
| **Risk flags** | Active Governance concerns |

---

## Product Manager Workflows

### Triage a New Signal

1. PM opens **Signal Intake**.
2. PM reviews a `New` Signal.
3. PM chooses one:
   - **Triage** -> status becomes `Triaged`.
   - **Dismiss** -> status becomes `Dismissed` with rationale.
   - **Merge / relate** -> links to related Signals, then triages or dismisses.

### Add a Signal to Product Backlog

In this console, "add to product backlog" means the PM acknowledges the Signal and makes it visible for planning. The Signal is typically moved from `New` to `Triaged`, optionally associated with an Objective or candidate Initiative. It is not yet a commitment to build.

### Associate Signals to an Initiative

1. PM selects one or more Triaged Signals.
2. PM associates them to an Approved or In Progress Initiative.
3. Signal status becomes `Associated`, unless active exploration is still required.
4. Initiative side panel updates Signal coverage and downstream discovery queue.

### Start Discovery Exploration

1. PM selects a Triaged or Associated Signal.
2. PM creates a Signal Exploration Task.
3. Signal status becomes `Exploring`.
4. Discovery work may spawn Ideas.

### Convert Discovery to Product Intent

1. Signal Exploration produces one or more Ideas.
2. Research, Experiments, Prototypes, or Deliberations validate the Idea.
3. A PDR records Go / Kill / Pivot.
4. A Go or Pivot decision may trigger PSD authoring through Specification Tasks.
5. Approved PSDs form the contract for Product Specification Workspace work.
6. Product Intent is created or updated and begins flowing through ACE Workspaces.

---

## Boundary With Product Specification Workspace

The PI Console depicts strategic direction, signal processing, discovery traceability, and Product Intent flow. The detailed work happens in Workspaces:

| Concern | Primary home |
|---------|--------------|
| Signal triage and Initiative association | PI Console |
| Objective and Initiative visibility | PI Console |
| Signal Exploration Tasks, Research, Experiments, Deliberations | Discovery Track; visible in PI Console and Track Console |
| PSD authoring work | Product Specification Workspace via Specification Tasks |
| UX design work | UX Design Workspace |
| Build implementation | Development Workspace |
| Verification | QA Workspace |
| Release packaging and next-cycle intent | Release Workspace |
| Transition validation | Governance Workspace |

The PI Console should not become a replacement editor for PSDs or Workspace execution. It is the Product Management console for deciding and observing what should enter that execution system.

---

## Actions

| Action | Who | Description |
|--------|-----|-------------|
| Capture Signal | Product Manager, Member | Create a Problem, Need, or Opportunity Signal |
| Triage Signal | Product Manager | Move Signal from New to Triaged or Dismissed |
| Associate Signal | Product Manager | Link Signal to an Initiative |
| Park Signal | Product Manager | Mark legitimate but not currently prioritized |
| Start Exploration | Product Manager | Create a Signal Exploration Task for a Signal |
| Create / update Objective | Product Manager, Manager | Maintain strategic goals for the Workbench |
| Create / update Initiative | Product Manager, Manager | Define cross-track program, lever mix, targets, and associated Signals |
| Create / link PDR | Product Manager | Record Go / Kill / Pivot decision and evidence |
| Create / link PSD | Product Manager | Initiate PSD authoring after a PDR |
| Create Intent | Product Manager, Manager | Start or update Product Intent after discovery/specification basis exists |
| Archive Intent | Manager | Move to archived after Release complete |
| View in Wall | All | Filter Workbench Wall to a Signal, Initiative, or Product Intent |

---

## Filters

- By Signal status: New, Triaged, Exploring, Associated, Parked, Addressed, Dismissed
- By Signal type: Problem, Need, Opportunity
- By Objective
- By Initiative
- By lever: Product, GTM, Sales Enablement, Customer Success, Operational
- By Idea status: Proposed, Investigating, Validated, Killed
- By PDR decision type: Go, Kill, Pivot
- By PSD status: Draft, In Technical Review, Approved, Superseded, Cancelled
- By Product Intent health: Green, Yellow, Red
- By current Workspace
- By date range
- By owner / sponsor / assignee

---

## Metrics

| Metric | Description |
|--------|-------------|
| **Unprocessed Signals** | Count of New + Triaged Signals |
| **Signal age** | Oldest and median age for unprocessed Signals |
| **Triage throughput** | Signals triaged per week |
| **Exploration WIP** | Signals currently in Exploring state |
| **Idea conversion** | Signals that spawned Ideas |
| **Decision throughput** | PDRs finalized per period |
| **PSD readiness** | PSDs Draft / In Technical Review / Approved |
| **Objective coverage** | Active Objectives with at least one Initiative |
| **Initiative signal coverage** | Signals associated per Initiative by type |
| **Product Intent WIP** | Active PIs by current Workspace |

---

## Related Consoles

- **Workspaces Console** — See WOs by Workspace once Product Intent enters Workspace execution
- **Track Console** — Discovery, Build, Run, Win, Evolve, Governance flow analytics
- **Progress Console** — Work completion metrics for WOs and PIs
- **Risk Console** — Governance risk flags affecting Product Intents
- **Repositories & Tools** — Product Intent Repository, Design Repository, external tools
