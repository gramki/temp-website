# PI Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/pi`

**Group:** Work

**Purpose:** Product Intent Formation Console for the Workbench — visualize how Product Intent forms from Strategy, Signals, Product Decisions, customer commitments, and Release learnings; surface relevant Product Intent Repository items; and track Product Intents as they move into PSD refinement and ACE Workspace execution.

---

## Key Concepts

| Term | Definition |
|------|------------|
| **Signal** | UPIM Dim 1 input: Problem, Need, or Opportunity. A Signal is an observation to investigate, not a requirement or delivery commitment. |
| **Unprocessed Signal** | A Signal in `New` or `Triaged` state that has not yet been explored, associated with an Initiative, parked, addressed, or dismissed. |
| **Objective** | Strategic goal over a planning horizon; answers "where are we going?" |
| **Initiative** | Cross-track strategic program that advances Objectives, associates Signals, declares lever mix, and carries embedded targets. |
| **Customer Promise** | Customer Value commitment: what value, service level, or compliance posture the product promises to a customer segment. |
| **Customer Release Intent** | Strategy-layer intent for a planned customer-facing delivery outcome: what capabilities we intend to make available, to whom, why, and by when. |
| **Discovery Case** | Cross-functional Discovery Track orchestration item. Groups investigation work until the case resolves in a PDR, Product Intent, another track case, parking, or dismissal. A Signal is optional. |
| **Idea** | Hypothesis spawned from one or more Signals and validated through Discovery Track work. |
| **PDR** | Product Decision Record: Go / Kill / Pivot decision that records evidence. A Go or Pivot PDR may create Product Intent, Modeling Tasks, or Initiative changes. |
| **PSD** | Product Specification Document: the validated contract between Product and Engineering. PSDs are refined under Product Intent through Specification Tasks in the Product Specification Workspace. |
| **Product Intent** | ACE asset that flows through Workspaces. Created or updated from an accepted Go or Pivot PDR, requested as Discovery Support from a Discovery Case, or renewed from Release learnings. Carries an intent purpose; not every Product Intent in Build represents customer-committed delivery. |

---

## Product Intent Repository Scope

The PI Console is the primary web view over the **Product Intent Repository (PIR)** for a Workbench. PIR is broader than a list of active Product Intents: it is the ledger where strategy, Signals, discovery decisions, Product Intents, specifications, and the business/customer context needed to evaluate intent are brought together.

The console should surface **relevant** PIR items — enough for a Product Manager to understand why intent exists, how it was decided, and what it is meant to advance. It should not try to become the full editor for every Definition Model entity.

### Definition Model Items Surfaced

| Repository section | Definition Model items | Why the PI Console shows them |
|--------------------|------------------------|-------------------------------|
| **Strategy** | Portfolio, Strategic Theme, Objective, KRA / SLA context, Initiative, Customer Release Intent | Shows product direction: where the Product sits, what strategic themes are active, what Objectives or commitments are being pursued, what Initiatives group the work, and what customer-facing delivery outcomes are intended. |
| **Signals** | Problem, Need, Opportunity | Shows the unprocessed or active observations that warrant product attention. These are the raw inputs to Discovery, not requirements or commitments. |
| **Hypotheses, cases, and decisions** | Idea, Discovery Case, Product Decision Record (PDR) | Shows how inputs are grouped into discovery investigations, synthesized into hypotheses, and resolved through Go / Kill / Pivot decisions. |
| **Product Intents** | Product Intent | Shows the execution token created from Go/Pivot PDRs and routed through ACE Workspaces. |
| **Specifications** | Product Specification Document (PSD) and PSD template references | Shows specification contracts refined under each Product Intent. |
| **Vendor-value context** | Business Model, Pricing Tier / Package, Value Metric, Lever Portfolio, Business KPI / Cost KPI, Win Outcome, Win Barrier, Delivery Friction, Win Stakeholder role | Explains why an Initiative matters commercially, which lever mix is being activated, and how vendor-side success is measured. |
| **Customer-value context** | Customer Segment, Buying Persona, Business Outcome, Customer Promise, Customer Value Metric | Explains who benefits, what buyer outcome or promise the intent advances, and how customer value will be measured. |

### Standing vs. Flowing Items

| Item type | Examples | Console treatment |
|-----------|----------|-------------------|
| **Standing strategy/context** | Portfolio, Strategic Theme, Objective, KRA / SLA context, Customer Release Intent, Business Model, Customer Segment, Win Outcome, Customer Promise | Display as filters, side-panel context, and traceability anchors. These items explain the frame for intent. |
| **Flowing discovery items** | Problem, Need, Opportunity, Discovery Case, Idea, PDR | Display as queues, cards, status flows, and detail pages through Discovery. |
| **Flowing execution items** | Product Intent, PSD | Display as queues and detail pages once a Go/Pivot PDR creates intent; PSD refinement is tracked under that intent. |

---

## Page Layout

```
┌─────────────────────────────────────────────────────────────────────┐
│ STRATEGY FRAME                                                      │
│   Objectives: OBJ-12 LATAM Coverage │ OBJ-13 Activation Velocity     │
│   Initiatives: INIT-04 LATAM Entry │ CRI-02 LATAM Expansion          │
├─────────────────────────────────────────────────────────────────────┤
│ SIGNAL INTAKE                                                       │
│   [New (12)] [Triaged (8)] [Exploring (5)] [Parked (9)]             │
│   • SIG-231 Need — Batch payout file upload              [Triage]   │
│   • SIG-244 Problem — FX rate-lock flow too slow         [Triage]   │
├─────────────────────────────────────────────────────────────────────┤
│ DISCOVERY & COMMITMENT FLOW                                         │
│   Discovery: Signals → Discovery Cases → Ideas → PDRs               │
│   Commitment: PDR (Go/Pivot) → Product Intent (by type) → PSD       │
│   18 unprocessed │ 4 open cases │ 3 PDRs final │ 2 PIs in spec     │
├─────────────────────────────────────────────────────────────────────┤
│ PRODUCT INTENTS                                                     │
│   [Active] [Archived] [All]                                         │
│   PI-039 LATAM Currency Support [Spec✓][UX●][Dev○][QA○][Rel○]      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## PI Console Views

### 1. Funnel

Default view. Shows Product Intent formation from multiple valid starting points into downstream execution.

```text
Strategy / Signals / Commitments / Release Learnings
  -> Discovery Case (optional grouping)
  -> Product Decision / PDR
  -> Product Intent (typed)
  -> PSD refinement
  -> Workspace execution
  -> Delivery / Renewal
```

**Starting point filters:** Strategy, Signals, Discovery Case, Decisions, KRA / SLA, Customer Promise, Customer Release Intent, Release Learning, Compliance / contractual commitment.

**Product Intent purpose filters:** Evolution / Delivery, Discovery Support, Technical Validation, Internal / Enabling, Operational Enablement, Release Renewal. Default: All purposes; Delivery-only view for customer-commitment tracking.

### 2. Strategy Frame

Shows decision-grade strategy and the Product Intents it produces.

| Strategy element | What it answers |
|------------------|-----------------|
| Portfolio / Strategic Theme | What durable direction is active? |
| Objective / KRA | What goal or result are we pursuing? |
| SLA / Customer Commitment | What commitment constrains product evolution? |
| Initiative | What cross-track program groups the work? |
| Customer Release Intent | What customer-facing delivery outcome do we intend to make available? |
| Strategic Constraint | What regulatory, contractual, partner, market, or customer deadline shapes priority? |

#### What belongs in Strategy

- Portfolio context
- Strategic Themes
- Objectives, KRAs, and measurable goals
- SLAs and customer commitments that shape product evolution
- Initiatives
- Customer Release Intents
- Strategic constraints such as regulatory deadlines, contractual commitments, partner launch dependencies, market-event deadlines, and customer-committed dates
- Product Decisions / PDRs
- Product Intents

#### What must not go into Strategy

- Raw customer requests
- Untriaged Signals
- Individual bugs
- Jira stories
- Engineering tasks
- UX tasks
- Implementation designs
- PSD body content
- Deployment records
- Incident logs
- Unprocessed stakeholder opinions

Those items may inform strategy, but they are not strategy until they are interpreted, decided, and linked to Product Intent.

### 3. Signals

Shows raw discovery inputs and their processing state:

```text
Problem / Need / Opportunity
  -> New / Triaged / Exploring / Associated / Parked / Addressed / Dismissed
```

Signals may inform strategy, but Signals are not strategy.

### 4. Decisions

Shows Product Decisions and the Product Intents they create.

```text
Discovery Case
  -> PDR / Product Decision
  -> Product Intent(s) (with purpose)
  -> PSD(s)
```

One Discovery Case may produce zero, one, or many PDRs. One PDR can create multiple Product Intents. Product Intents can have different purposes.

### 5. Product Intents

Lifecycle view for Product Intent as a hybrid entity:

```text
Formed -> Accepted -> Parked -> In Specification -> Specified
  -> In Evolution -> Delivered -> Closed
  -> Superseded / Cancelled
```

Each Product Intent card shows a purpose badge: Evolution / Delivery, Discovery Support, Technical Validation, Internal / Enabling, Operational Enablement, or Release Renewal.

**Build-boundary note:** Discovery Support, Technical Validation, Internal / Enabling, and Operational Enablement Product Intents may enter Build Workspaces without implying a customer-committed delivery outcome.

### 6. Traceability Maps

Traceability Maps replace generic graph exploration. Each map answers a stakeholder question with a predefined graph shape.

| Map | Audience | Shape | Question answered |
|-----|----------|-------|-------------------|
| **Executive Strategy Map** | Executives, portfolio leaders | Strategic Theme -> Objective / KRA -> Initiative -> Product Intent -> Customer Release Intent / Delivered Outcome | Are strategic goals turning into product evolution? |
| **Product Manager Intent Map** | Product Managers | Signal / origin -> Discovery Case -> Idea -> PDR -> Product Intent (purpose) -> PSD | Why does this intent exist and what refines it? |
| **Technical / Architecture Origin Map** | Architects, engineers, PMs | Technical Idea / Architecture Concern -> Discovery Case -> PDR -> Product Intent -> PSD / ADR / Build Work | How does technical work become product intent? |
| **Delivery Execution Map** | Engineering managers, delivery leads | Product Intent -> PSD -> Work Orders -> Workspace Sessions -> Artifacts -> Release | What work is required and where is it blocked? |
| **Governance Evidence Map** | Governance, compliance, audit | PDR -> Product Intent -> Governance Events -> PSD Approval -> QA Evidence -> Release Evidence | Was every transition governed and evidenced? |
| **Customer Value Map** | Product, CS, GTM | Customer Segment -> Buying Persona / Business Outcome -> Customer Promise -> Product Intent -> Customer Release Intent -> Customer Value Metric | Which customer promise does this intent serve? |
| **Vendor Value Map** | Business and product leadership | Business Model -> Win Outcome -> Business KPI / Cost KPI -> Initiative -> Product Intent -> Win Review / Release | Which commercial outcome should move? |
| **Release Renewal Map** | Release, PM, governance | Delivered Product Intent -> Release Evidence -> Feedback / Learnings -> Renewed Product Intent -> Next Cycle | What did delivery teach us and what intent did it renew? |

### 7. Bottlenecks

Shows stalled items across the funnel:

- Untriaged Signals
- Old Triaged Signals
- Ideas stuck in validation
- Open Discovery Cases with no PDR progress
- Discovery Cases stuck awaiting evidence
- Draft PDRs
- Product Intents stuck in Formed / Accepted
- Product Intents stuck in Specification
- PSDs stuck in Technical Review
- Product Intents stuck in Evolution
- Non-delivery Product Intents in Build without clear evidence outcome
- Release renewals not acted on

---

## Page Sections

### 1. Strategy Frame

The top of the console shows the Product Management frame for the Workbench. This is where managers see the goals, commitments, constraints, and macro initiatives that determine how the Product should evolve.

| Element | Description |
|---------|-------------|
| **Active Objectives** | Current Objectives for the Workbench's Product, grouped by planning horizon |
| **Objective status** | Draft, Active, Achieved, Deferred |
| **Objective success criteria** | Measurable criteria and constraints that guide prioritization |
| **Initiatives** | Active or approved Initiatives pursuing the Objectives |
| **Customer Release Intents** | Planned customer-facing delivery outcomes and target availability dates |
| **Strategic commitments** | KRAs, SLAs, customer-committed deadlines, regulatory deadlines, partner launch dependencies |
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

The Discovery Flow section shows how inputs are converted into buildable direction. It does not replace Track Console analytics; it gives Product Managers the specific origin -> Discovery Case -> Idea -> PDR -> Product Intent -> PSD chain for this Workbench.

```
Origin (Signal, strategy, PM judgment, technical idea, release learning, etc.)
  └── Discovery Case
        └── Signal Exploration / Research / Experiment / Prototype / Deliberation
              └── Idea
                    └── PDR (Go / Kill / Pivot)
                          ├── Kill → archived (no Product Intent)
                          ├── Modeling Task(s)
                          ├── Discovery Support Product Intent → Build evidence
                          └── Go / Pivot
                                └── Evolution Product Intent
                                      └── PSD refinement (Specification Tasks)
                                            └── ACE Workspaces
```

| Stage | What the PI Console shows |
|-------|---------------------------|
| **Signals** | New, Triaged, Exploring, Associated, Parked, Addressed, Dismissed |
| **Exploration** | Signal Exploration Tasks and their open questions |
| **Discovery Cases** | Open / Scoped / In Progress / In Deliberation / Decided / Routed / Closed / Parked / Dismissed |
| **Ideas** | Proposed / Investigating / Validated / Killed hypotheses |
| **Evidence** | Research Tasks, Experiments, Prototypes / Spikes, Deliberations |
| **PDRs** | Draft / Final / Superseded decisions with Go / Kill / Pivot type |
| **Product Intent** | Active and archived ACE Product Intents created from Go/Pivot PDRs, Discovery Support requests, or Release renewal; shown with purpose badge |
| **PSDs** | Draft / In Technical Review / Approved / Superseded / Cancelled specification documents linked to parent Product Intent |

### 4. Product Intents

Product Intents remain visible in the PI Console, but they are shown as the commitment object after an accepted PDR rather than the only object on the page. PSD refinement status appears under each intent.

| Element | Description |
|---------|-------------|
| **Active PIs** | Product Intents currently moving through Workspaces |
| **Intent purpose** | Evolution / Delivery, Discovery Support, Technical Validation, Internal / Enabling, Operational Enablement, Release Renewal |
| **Customer delivery indicator** | Delivery / Release Renewal may link Customer Release Intent; other purposes show "Not customer-committed delivery" |
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
| **Discovery Case** | Originating or linked Discovery Case, if any |
| **Product Intent** | Intent identity, owner, lifecycle state, and current Workspace |
| **Discovery evidence** | Research, experiments, prototypes, deliberations that support the PDR |
| **Intent purpose** | Why this intent exists and whether customer-committed delivery is in scope |
| **Specification content** | PSD links and status; PSD is the contract for Product Specification and Build work when specification is required |
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

1. PM or another authorized function opens or selects a Discovery Case.
2. PM selects a Triaged or Associated Signal when the case is signal-led.
3. PM creates a Signal Exploration Task, Research Task, Experiment, Prototype, or Deliberation under the case.
4. Discovery work may spawn Ideas, evidence, PDRs, Modeling Tasks, or Discovery Support Product Intent.

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
- By Discovery Case status: Opened, Scoped, In Progress, In Deliberation, Decided, Routed, Closed, Parked, Dismissed
- By Signal type: Problem, Need, Opportunity
- By Objective
- By Initiative
- By lever: Product, GTM, Sales Enablement, Customer Success, Operational
- By Idea status: Proposed, Investigating, Validated, Killed
- By PDR decision type: Go, Kill, Pivot
- By Product Intent purpose: Evolution / Delivery, Discovery Support, Technical Validation, Internal / Enabling, Operational Enablement, Release Renewal
- By customer delivery scope: Customer-committed delivery, Not customer-committed delivery
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
| **Open Discovery Cases** | Cases in Opened, Scoped, In Progress, or In Deliberation |
| **Case-to-decision cycle time** | Discovery Case opened to PDR Final |
| **Intent creation rate** | Go/Pivot PDRs that produced Product Intent |
| **PIs by purpose** | Active Product Intents grouped by purpose |
| **Non-delivery PI WIP in Build** | Product Intents in Build Workspaces whose purpose is not Delivery |
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
