# Foundry Orchestrator

**Module scope:** Coordination — route Track orchestration items through Workspaces, create Workspace Work Orders, invoke Governance Scenarios, enforce gates.

## Purpose

The Orchestrator is the coordination layer that enables assembly-line product evolution. Without it, work would be ad-hoc — teams wouldn't know when to start, what gates to pass, or how their work connects to the broader product journey.

Orchestrator treats product evolution like a manufacturing line: orchestration items (like Product Intents) flow through stations (Workspaces), triggering work (Work Orders) at each stop. Gates ensure quality before items advance. This model scales from small teams to large organizations because the coordination logic is declarative (YAML workflows) rather than embedded in code or tribal knowledge.

The primary beneficiaries are Program Managers (who see work flowing through the system), Workbench teams (who receive well-defined Work Orders with context), and Governance teams (who can enforce policy at transitions without manual intervention).

## What this module does

- **Orchestration-item routing** — move each Track's primary orchestration item across Workspaces and link items at cross-track handoffs
- **Workspace Work Order creation** — instantiate `(Track, Workspace, Scenario)` as Work Orders when triggered by workflow events
- **Work Order assignment** — assign WOs to users based on skill matching, capacity, and affinity
- **Session activation** — activate user Workspace Sessions when WOs are assigned (per user configuration)
- **Governance invocation** — invoke Governance Scenarios at gates and transitions
- **Gate enforcement** — validate transitions, block or allow based on Governance Scenario outcomes
- **Completion handling** — receive WO completion notifications and advance orchestration items
- **Workflow engine** — evaluate YAML workflow definitions and execute handlers

## What this module does NOT do

- **Does not execute Work Orders** — WO Runtime executes work; Orchestrator only creates and tracks WOs
- **Does not manage agents** — Agent Fabric manages Capable Agents, Skills, and quotas
- **Does not spawn agents** — WO Runtime spawns Employed Agents within Workspace Sessions
- **Does not store artifacts** — Repositories store code, designs, specs; Orchestrator only links to them
- **Does not define Scenarios** — Scenario Management (in Management module) defines schema; Work Catalogues module contains definitions
- **Does not manage Workbenches** — Management module provisions and configures Workbenches

## Architecture

```
                                    ┌─────────────────────────────────────────────┐
                                    │             Foundry Orchestrator            │
                                    │                                             │
┌─────────────┐                     │  ┌─────────────┐    ┌─────────────────┐    │
│    Jira     │───── webhooks ─────▶│  │  Webhook    │───▶│    Workflow     │    │
│  (events)   │                     │  │  Listener   │    │     Engine      │    │
└─────────────┘                     │  └─────────────┘    └────────┬────────┘    │
                                    │                              │             │
                                    │                              ▼             │
                                    │                     ┌─────────────────┐    │
                                    │                     │     Action      │    │
                                    │                     │    Executor     │    │
                                    │                     └────────┬────────┘    │
                                    │                              │             │
                                    └──────────────────────────────┼─────────────┘
                                                                   │
                     ┌─────────────────────────┬───────────────────┼───────────────────┐
                     │                         │                   │                   │
                     ▼                         ▼                   ▼                   ▼
            ┌─────────────────┐       ┌─────────────────┐  ┌─────────────┐    ┌─────────────┐
            │  Jira (write)   │       │  Message Queue  │  │  Postgres   │    │  Metadata   │
            │  - Create WOs   │       │  - WO Runtime   │  │  - State    │    │   Service   │
            │  - Transitions  │       │  - Sessions     │  │  - History  │    │  - IDs      │
            └─────────────────┘       └─────────────────┘  └─────────────┘    └─────────────┘
```

**Data flow:**
1. Jira webhooks notify Orchestrator of orchestration item and WO events
2. Workflow Engine matches events to handlers in the workflow YAML
3. Action Executor creates WOs, transitions items, invokes governance
4. State persisted to Postgres; Jira updated; WO Runtime notified via message queue

## Key Components

### Webhook Listener

Receives events from Jira and routes them to the Workflow Engine.

### Workflow Engine

Loads workflow YAML definitions and evaluates handlers against incoming events. Workflows are sourced from the **Work Catalog** with hierarchical resolution: Platform → Foundry → Workshop → Workbench → User (closest wins).

→ [orchestration-item-workflow.md](orchestration-item-workflow.md) — Workflow authoring guide
→ [../management/work-catalog-management/oi-workflow-schema.md](../management/work-catalog-management/oi-workflow-schema.md) — Canonical OI Workflow schema
→ [../work-catalogues/platform-defaults/](../work-catalogues/platform-defaults/) — Platform default OI Workflows

### Action Executor

Executes workflow actions: `create-work-order`, `create-work-order-group`, `transition-orchestration-item`, `invoke-governance-scenario`, `notify`.

### State Store

Postgres database for workflow state, WO labels, group completion tracking, and transition history. Jira is the secondary store for work items.

→ [orchestrator-requirements.md](orchestrator-requirements.md) — detailed requirements

## Per-Track Primary Orchestration Items

| Track | Primary orchestration item | Orchestrator moves... |
|-------|----------------------------|------------------------|
| **Discovery** | Discovery Case | Discovery Case across Discovery-relevant Workspaces until it is dismissed, parked, decided, or routed. |
| **Build** | Product Intent | Product Intent through Product Specification, UX Design, Development, QA, Release, and Governance. |
| **Run** | Run Case | Change, incident, capacity, or maintenance case through Run-relevant Workspaces. |
| **Win** | Customer Release Intent / Win Case | Customer Release Intent through proactive market delivery; Win Case through reactive response and resolution. |
| **Evolve** | Evolve Case | Process/model/practice evolution through review, definition, and adoption. |
| **Governance** | Governance Ritual / Governance Enforcement | Rituals, policy assertion, evidence, approvals, findings, registers, recognition. |

## Orchestration Item vs Workspace Work Order

| | Orchestration item | Workspace Work Order |
|---|---|---|
| Layer | Coordination | Execution |
| Scope | Track-level assembly-line item | One `(Track, Workspace, Scenario)` execution instance |
| Cardinality | One item spawns many Work Orders across Workspaces | One Work Order belongs to one orchestration item graph |
| Lifecycle | Routed, gated, linked across Workspaces or Tracks | Created, executed, completed, failed, or cancelled |
| Owner | Orchestrator | Work Order Runtime and Workspace team |

Do not conflate them. Moving Product Intent from Specification to Development is orchestration. Instantiating a `refine-psd` Scenario in Product Specification Workspace is a Workspace Work Order.

## ACE Concepts Realized

| Concept | How Orchestrator realizes it |
|---------|------------------------------|
| **Track** | Routes orchestration items through Track-specific flows |
| **Workspace** | Creates Work Orders when items reach Workspaces |
| **Orchestration item** | Manages lifecycle of Track-level coordination tokens |
| **Governance** | Invokes Governance Scenarios at transition gates |
| **Work Order** | Creates WOs; does not execute them |

## Key Design Decisions

- **Governance is distributed.** Definition is via Scenarios (Work Catalogues), enforcement is via Orchestrator, evidence is captured in repositories.
- **Governance Scenarios are first-class.** They're invoked like any other Scenario, but at transition points.
- **Governance orchestration has two modes.** Rituals organize cadence/event reviews; Enforcement asserts policy and produces verdicts, findings, and register entries.
- **Orchestration items are Track-scoped; Work Orders are Workspace-scoped.** One orchestration item can create many Workspace Work Orders.
- **Workflows are declarative YAML.** Coordination logic is configuration, not code — enables customization without development.
- **Work Catalog is the source for OI Workflows.** Workflows are resolved from the Work Catalog hierarchy (Platform → Foundry → Workshop → Workbench → User). Users with activated personal catalogs can experiment with workflow modifications in their sessions.
- **Closest workflow wins.** User overrides Workbench overrides Workshop overrides Foundry overrides Platform — allows org-wide defaults with product-specific exceptions.
- **Jira is bidirectional.** Orchestrator reads (webhooks) AND writes (REST API) to Jira.
- **Separate state database.** Postgres for workflow state; Jira is secondary for work items.

## Open Questions

- How does Orchestrator resolve the effective Control Owner and Approver from the Governance Authority Matrix?
- When Enforcement returns Debt + Catch-Up or Exception / Waiver, does Orchestrator block until the required register record exists?

## Module Documents

| Document | Content |
|----------|---------|
| [orchestrator-requirements.md](orchestrator-requirements.md) | Detailed implementation requirements (architecture, APIs, scalability) |
| [orchestration-item-workflow.md](orchestration-item-workflow.md) | OI Workflow authoring guide and reference |
| [workflow.yaml](../work-catalogues/platform-defaults/build/product-intent/workflow.yaml) | Complete Product Intent workflow example |
| [pi-journey.md](pi-journey.md) | End-to-end Product Intent walkthrough |

**Work Catalog Integration:**

| Document | Content |
|----------|---------|
| [../work-catalogues/README.md](../work-catalogues/README.md) | Work Catalog conceptual overview |
| [../work-catalogues/platform-defaults/build/product-intent/](../work-catalogues/platform-defaults/build/product-intent/) | Platform default Product Intent workflow |
| [../management/work-catalog-management/oi-workflow-schema.md](../management/work-catalog-management/oi-workflow-schema.md) | Canonical OI Workflow YAML schema |
| [../management/work-catalog-management/resolution-algorithm.md](../management/work-catalog-management/resolution-algorithm.md) | Hierarchy resolution implementation |

## Read Next

- [pi-journey.md](pi-journey.md) — end-to-end Product Intent walkthrough
- [../work-order-runtime/README.md](../work-order-runtime/README.md) — WO Runtime execution engine
- [../agent-fabric/README.md](../agent-fabric/README.md) — Agent infrastructure
- [../management/README.md](../management/README.md) — Workbench provisioning
- [../../ace/governance.md](../../ace/governance.md) — governance model
- [../../ace/product-evolution-cycle.md](../../ace/product-evolution-cycle.md) — how Product Intent moves
