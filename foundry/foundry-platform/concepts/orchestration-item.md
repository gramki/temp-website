# Orchestration Item

An Orchestration Item is a Track-level coordination token — such as Product Intent, Discovery Case, or Run Case — that flows through Workspaces, triggering Work Orders at each station and linking work across the product evolution lifecycle.

## What it is

Orchestration Items are the coordination layer of Foundry. They represent the "what" that moves through the system — the intent, case, or request that multiple Workspaces will act upon. When Product Intent moves from Specification to Development, that's an Orchestration Item being routed. When a Discovery Case closes into Product Intent, that's cross-Track handoff.

Each Track has a primary Orchestration Item:

| Track | Primary Orchestration Item | Description |
|-------|---------------------------|-------------|
| **Discovery** | Discovery Case | Exploration, research, and decision-making about what to build |
| **Build** | Product Intent | The intent to evolve a product, refined through PSDs |
| **Run** | Run Case | Change, incident, capacity, or maintenance case |
| **Win** | Customer Release Intent / Win Case | Proactive market delivery or reactive customer response |
| **Evolve** | Evolve Case | Process, model, or practice evolution |
| **Governance** | Governance Ritual / Governance Enforcement | Rituals, policy assertion, evidence, approvals |

Orchestration Items are **not** Work Orders. The distinction is critical:

| | Orchestration Item | Work Order |
|---|-------------------|------------|
| **Layer** | Coordination | Execution |
| **Scope** | Track-level assembly-line item | One (Track, Workspace, Scenario) execution instance |
| **Cardinality** | One item spawns many Work Orders | One Work Order belongs to one orchestration item |
| **Lifecycle** | Routed, gated, linked across Workspaces | Created, executed, completed, failed, or cancelled |
| **Owner** | Orchestrator | Work Order Runtime |

Moving Product Intent from Specification to Development is orchestration. Instantiating a `refine-psd` Scenario in the Product Specification Workspace is creating a Work Order.

## Where it lives in Foundry

| Module | Responsibility |
|--------|----------------|
| **Orchestrator** | Routes items through OI Workflows; creates Work Orders when items reach Workspaces |
| **WO Runtime** | Executes the Work Orders that Orchestrator creates |
| **Jira** | System of record for orchestration items (as Epics or custom issue types) |
| **Metadata Service** | Generates unique IDs (PI-123, DC-456, etc.) |

The Orchestrator uses [OI Workflows](work-catalog.md) — YAML definitions that specify how orchestration items transition through stages and what Work Orders to create at each stage.

## ACE/UPIM alignment

| Orchestration Item | UPIM Entity | ACE Flow |
|-------------------|-------------|----------|
| Product Intent | Strategy & Intent (PIR) | Discovery → Product Specification → UX → Development → QA → Release |
| Discovery Case | Work Model (Discovery) | Created from signals; closes into Product Intent or dismissal |
| Run Case | Work Model (Run) | Created from incidents or changes; routed through Run Workspaces |
| Win Case | Feedback (Win) | Created from FIRs; routed through support and resolution |
| Evolve Case | Operating Model | Created for practice improvement; routed through definition and adoption |
| Governance Ritual / Enforcement | Operating Model | Invoked at transitions; produces verdicts and register entries |

Product Intent is the **hybrid bridge entity** that flows through Build workspaces. It is definition-bearing, work-triggering, and ACE-routable. Discovery and product decisions establish or update it; Release renews it for the next cycle.

## Related concepts

- [Track](track.md) — The value stream an orchestration item belongs to
- [Work Order](work-order.md) — What gets created when an item reaches a Workspace
- [Scenario](scenario.md) — The contract that defines what Work Order to create
- [Governance](governance.md) — How transitions are validated

## Further reading

- [../orchestrator/README.md](../orchestrator/README.md) — OI routing and WO creation
- [../orchestrator/user-guide/product-intent-journey.md](../orchestrator/user-guide/product-intent-journey.md) — End-to-end Product Intent walkthrough
- [../../ace/product-evolution-cycle.md](../../ace/product-evolution-cycle.md) — How Product Intent moves
- [../../ace/concepts.md#product-intent](../../ace/concepts.md#product-intent) — ACE definition
