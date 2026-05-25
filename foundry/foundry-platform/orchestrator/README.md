# Foundry Orchestrator

**Module scope:** Coordination — route Track orchestration items through Workspaces, create Workspace Work Orders, invoke Governance Scenarios, enforce gates.

## What this module does

Foundry Orchestrator is the coordination layer that moves work through the SDLC. It provides:

- **Orchestration-item routing** — move each Track's primary orchestration item across Workspaces and link items at cross-track handoffs
- **Workspace Work Order creation** — instantiate `(Track, Workspace, Scenario)` as Work Orders when triggered
- **Governance invocation** — invoke Governance Scenarios at gates and transitions
- **Gate enforcement** — validate transitions, block or allow based on Governance Scenario outcomes

## ACE concepts realized

- **Track** — value streams (Discovery, Build, Run, Win, Evolve, Governance); Orchestrator moves work through Tracks
- **Workspace** — stations on the line; Orchestrator routes orchestration items to Workspaces
- **Orchestration item** — Track-level coordination token; Product Intent is the Build Track primary item
- **Governance** — Orchestrator invokes Governance Scenarios at transitions

## Per-track primary orchestration items

| Track | Primary orchestration item | Orchestrator moves... |
|-------|----------------------------|------------------------|
| **Discovery** | Discovery Case | Discovery Case across Discovery-relevant Workspaces until it is dismissed, parked, decided, or routed. |
| **Build** | Product Intent | Product Intent through Product Specification, UX Design, Development, QA, Release, and Governance. |
| **Run** | Run Case | Change, incident, capacity, or maintenance case through Run-relevant Workspaces. |
| **Win** | Customer Release Intent / Win Case | Customer Release Intent through proactive market delivery; Win Case through reactive response and resolution. |
| **Evolve** | Evolve Case | Process/model/practice evolution through review, definition, and adoption. |
| **Governance** | Governance Case | Transition/evidence/approval/audit case through Governance Workspace. |

## Orchestration item vs Workspace Work Order

| | Orchestration item | Workspace Work Order |
|---|---|---|
| Layer | Coordination | Execution |
| Scope | Track-level assembly-line item | One `(Track, Workspace, Scenario)` execution instance |
| Cardinality | One item spawns many Work Orders across Workspaces | One Work Order belongs to one orchestration item graph |
| Lifecycle | Routed, gated, linked across Workspaces or Tracks | Created, executed, completed, failed, or cancelled |
| Owner | Orchestrator | Work Order Runtime and Workspace team |

Do not conflate them. Moving Product Intent from Specification to Development is orchestration. Instantiating a `refine-psd` Scenario in Product Specification Workspace is a Workspace Work Order.

## Key design decisions

- **Governance is distributed.** Definition is via Scenarios (Scenario Authoring), enforcement is via Orchestrator, evidence is captured in repositories.
- **Governance Scenarios are first-class.** They're invoked like any other Scenario, but at transition points.
- **Orchestration items are Track-scoped; Work Orders are Workspace-scoped.** One orchestration item can create many Workspace Work Orders.

## Open questions

- How are orchestration item transitions triggered? (event-driven, explicit API, Scenario completion?)
- Work Order creation API
- Gate enforcement mechanics — blocking vs advisory
- Governance Scenario invocation timing

## Read next

- [../../ace/governance.md](../../ace/governance.md) — governance model
- [../../ace/product-evolution-cycle.md](../../ace/product-evolution-cycle.md) — how Product Intent moves
- [../../ace/how-product-evolves/orchestration-items.md](../../ace/how-product-evolves/orchestration-items.md) — orchestration item model
- [../../tldr-faq.md](../../tldr-faq.md) — orchestration design decisions
