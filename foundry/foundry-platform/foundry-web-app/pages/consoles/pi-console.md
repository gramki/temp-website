# PI Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/pi`

**Group:** Work

**Purpose:** Product Management control surface for the Workbench — surface relevant Product Intent Repository items, triage unprocessed Signals, maintain Objectives and Initiatives, observe Discovery Track conversion, and track Product Intents as they move into Product Specification and onward through the ACE Product Evolution Cycle.

---

## Key Concepts

| Term | Definition |
|------|------------|
| **Signal** | UPIM Dim 1 input: Problem, Need, or Opportunity. A Signal is an observation to investigate, not a requirement or delivery commitment. |
| **Unprocessed Signal** | A Signal in `New` or `Triaged` state that has not yet been explored, associated with an Initiative, parked, addressed, or dismissed. |
| **Objective** | Strategic goal over a planning horizon; answers "where are we going?" |
| **Initiative** | Cross-track strategic program that advances Objectives, associates Signals, declares lever mix, and carries embedded targets. |
| **Idea** | Hypothesis spawned from one or more Signals and validated through Discovery Track work. |
| **PDR** | Product Decision Record: Go / Kill / Pivot decision that records evidence. A Go or Pivot PDR may create Product Intent, Modeling Tasks, or Initiative changes. |
| **PSD** | Product Specification Document: the validated contract between Product and Engineering. PSDs are refined under Product Intent through Specification Tasks in the Product Specification Workspace. |
| **Product Intent** | ACE asset that flows through Workspaces. Created or updated from an accepted Go or Pivot PDR; triggers Product Specification Workspace scenarios where PSDs are drafted and refined. |

---

## Product Intent Repository Scope

The PI Console is the primary web view over the **Product Intent Repository (PIR)** for a Workbench. PIR is broader than a list of active Product Intents: it is the ledger where strategy, Signals, discovery decisions, Product Intents, specifications, and the business/customer context needed to evaluate intent are brought together.

The console should surface **relevant** PIR items — enough for a Product Manager to understand why intent exists, how it was decided, and what it is meant to advance. It should not try to become the full editor for every Definition Model entity.

### Definition Model Items Surfaced

| Repository section | Definition Model items | Why the PI Console shows them |
|--------------------|------------------------|-------------------------------|
| **Strategy** | Portfolio, Strategic Theme, Objective, Initiative, Customer Release | Shows product direction: where the Product sits, what strategic themes are active, what Objectives are being pursued, what Initiatives group the work, and what customer-facing release outcomes may result. |
| **Signals** | Problem, Need, Opportunity | Shows the unprocessed or active observations that warrant product attention. These are the raw inputs to Discovery, not requirements or commitments. |
| **Hypotheses and decisions** | Idea, Product Decision Record (PDR) | Shows how Signals are synthesized into hypotheses, and how Go / Kill / Pivot decisions are recorded with evidence. |
| **Product Intents** | Product Intent | Shows the execution token created from Go/Pivot PDRs and routed through ACE Workspaces. |
| **Specifications** | Product Specification Document (PSD) and PSD template references | Shows specification contracts refined under each Product Intent. |
| **Vendor-value context** | Business Model, Pricing Tier / Package, Value Metric, Lever Portfolio, Business KPI / Cost KPI, Win Outcome, Win Barrier, Delivery Friction, Win Stakeholder role | Explains why an Initiative matters commercially, which lever mix is being activated, and how vendor-side success is measured. |
| **Customer-value context** | Customer Segment, Buying Persona, Business Outcome, Customer Promise, Customer Value Metric | Explains who benefits, what buyer outcome or promise the intent advances, and how customer value will be measured. |

### Standing vs. Flowing Items

| Item type | Examples | Console treatment |
|-----------|----------|-------------------|
| **Standing strategy/context** | Portfolio, Strategic Theme, Objective, Business Model, Customer Segment, Win Outcome, Customer Promise | Display as filters, side-panel context, and traceability anchors. These items explain the frame for intent. |
| **Flowing discovery items** | Problem, Need, Opportunity, Idea, PDR | Display as queues, cards, status flows, and detail pages through Discovery. |
| **Flowing execution items** | Product Intent, PSD | Display as queues and detail pages once a Go/Pivot PDR creates intent; PSD refinement is tracked under that intent. |

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
│ DISCOVERY & COMMITMENT FLOW                                         │
│   Discovery: Signals → Ideas → PDRs                                 │
│   Commitment: PDR (Go/Pivot) → Product Intent → PSD refinement      │
│   18 unprocessed │ 5 exploring │ 3 PDRs final │ 2 PIs in spec       │
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

The Discovery Flow section shows how Signals are converted into buildable direction. It does not replace Track Console analytics; it gives Product Managers the specific Signal -> Idea -> PDR -> Product Intent -> PSD chain for this Workbench.

```
Signal
  └── Signal Exploration Task
        └── Idea
              └── Research / Experiment / Prototype / Deliberation
                    └── PDR (Go / Kill / Pivot)
                          ├── Kill → archived (no Product Intent)
                          ├── Modeling Task(s)
                          └── Go / Pivot
                                └── Product Intent
                                      └── PSD refinement (Specification Tasks)
                                            └── ACE Workspaces
```

| Stage | What the PI Console shows |
|-------|---------------------------|
| **Signals** | New, Triaged, Exploring, Associated, Parked, Addressed, Dismissed |
| **Exploration** | Signal Exploration Tasks and their open questions |
| **Ideas** | Proposed / Investigating / Validated / Killed hypotheses |
| **Evidence** | Research Tasks, Experiments, Prototypes / Spikes, Deliberations |
| **PDRs** | Draft / Final / Superseded decisions with Go / Kill / Pivot type |
| **Product Intent** | Active and archived ACE Product Intents created from Go/Pivot PDRs |
| **PSDs** | Draft / In Technical Review / Approved / Superseded / Cancelled specification documents linked to parent Product Intent |

### 4. Product Intents

Product Intents remain visible in the PI Console, but they are shown as the commitment object after an accepted PDR rather than the only object on the page. PSD refinement status appears under each intent.

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
| **Source chain** | Signal(s) -> Idea -> PDR -> Product Intent -> PSD(s), where available |
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
| **Traceability** | Source Signals, Ideas, and authorizing PDR |
| **Product Intent** | Intent identity, owner, lifecycle state, and current Workspace |
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
4. A Go or Pivot PDR creates or updates Product Intent and routes it to the Product Specification Workspace.
5. Specification Tasks refine PSDs under that Product Intent; each PSD references the PDR.
6. Approved PSDs enable Product Intent to fan out to UX Design, Development, and QA per the ACE cycle.

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
| Create Intent | Product Manager, Manager | Create or update Product Intent from a Go/Pivot PDR |
| Create / link PSD | Product Manager | Start or refine PSD authoring under an existing Product Intent |
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
| **Intent creation rate** | Go/Pivot PDRs that produced Product Intent |
| **PSD refinement progress** | PSDs by status per active Product Intent |
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
