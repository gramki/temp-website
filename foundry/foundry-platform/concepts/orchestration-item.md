# Orchestration Item

An Orchestration Item is a Track-level coordination token — such as Product Intent, Discovery Case, or Run Case — that flows through Workspaces, triggering Work Orders at each station and linking work across the product evolution lifecycle.

## What it is

Orchestration Items are the coordination layer of Foundry. They represent the "what" that moves through the system — the intent, case, or request that multiple Workspaces will act upon.

Each Track has a primary Orchestration Item:

| Track | Primary Orchestration Item | Description |
|-------|---------------------------|-------------|
| **Discovery** | Discovery Case | Exploration, research, and decision-making about what to build |
| **Build** | Product Intent | The intent to evolve a product, refined through PSDs |
| **Run** | Run Case | Change, incident, capacity, or maintenance case |
| **Win** | Customer Release Intent / Win Case | Proactive market delivery or reactive customer response |
| **Evolve** | Evolve Case | Process, model, or practice evolution |
| **Governance** | Governance Ritual / Governance Enforcement | Rituals, policy assertion, evidence, approvals |

### Dual representation (Discovery Case, Product Intent)

Discovery Case and Product Intent exist as both:

- **Work Items** in the Work Repository (orchestration record, workflow stage, `workRepoKey`)
- **Work Artifacts** in the Intent Repository (charter, PSDs, folder tree, `artifactUri`)

PDR is **artifact-only** in the Intent Repository — not a Work Item.

All orchestration APIs expose `title` and markdown `description`.

Orchestration Items are **not** Work Orders:

| | Orchestration Item | Work Order |
|---|-------------------|------------|
| **Layer** | Coordination | Execution |
| **Scope** | Track-level assembly-line item | One (Track, Workspace, Scenario) execution instance |
| **Cardinality** | One item spawns many Work Orders | One Work Order belongs to one orchestration item |
| **Lifecycle** | Routed, gated, linked across Workspaces | Created, executed, completed, failed, or cancelled |
| **Owner** | Orchestrator | Work Order Runtime |

## Where it lives in Foundry

| Module | Responsibility |
|--------|----------------|
| **Orchestrator** | Routes items through OI Workflows; creates Work Orders when items reach Workspaces |
| **WO Runtime** | Executes the Work Orders that Orchestrator creates |
| **Work Repository** | Work Item mirror for dual entities |
| **Intent Repository** | Git-backed artifacts for dual entities and PDR |
| **Metadata Service** | Generates unique IDs (PI-123, DC-456, etc.) |

Track-based APIs (Phase 1):

- Discovery: `/workbenches/{workbenchId}/tracks/discovery/cases/{dcId}`
- Build: `/workbenches/{workbenchId}/tracks/build/product-intents/{piId}`

See [../../foundry-work-plan/phase-1/api-surface.md](../../foundry-work-plan/phase-1/api-surface.md).

## ACE/UPIM alignment

| Orchestration Item | UPIM Entity | ACE Flow |
|-------------------|-------------|----------|
| Product Intent | Strategy & Intent (Intent Repository) | Discovery → Product Specification → UX → Development → QA → Release |
| Discovery Case | Work Model (Discovery) | Optional `sourceRefs[]`; closes into Product Intent or dismissal |
| Run Case | Work Model (Run) | Created from incidents or changes |
| Win Case | Feedback (Win) | Created from FIRs |
| Evolve Case | Operating Model | Practice improvement |
| Governance Ritual / Enforcement | Operating Model | Transition validation |

Product Intent is the **hybrid bridge entity** that flows through Build workspaces.

## Related concepts

- [Track](track.md) — The value stream an orchestration item belongs to
- [Work Order](work-order.md) — What gets created when an item reaches a Workspace
- [Scenario](scenario.md) — The contract that defines what Work Order to create
- [Governance](governance.md) — How transitions are validated

## Further reading

- [../../foundry-work-plan/phase-1/repository-contracts.md](../../foundry-work-plan/phase-1/repository-contracts.md) — entity storage model
- [../orchestrator/README.md](../orchestrator/README.md) — OI routing and WO creation
- [../../ace/product-evolution-cycle.md](../../ace/product-evolution-cycle.md) — How Product Intent moves
