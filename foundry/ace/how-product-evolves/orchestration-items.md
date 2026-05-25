# Orchestration Items

An **orchestration item** is the Track-level coordination item the Foundry Orchestrator routes. It is not the same thing as a Workspace Work Order.

## Primary orchestration items by track

| Track | Primary orchestration item | Notes |
|-------|----------------------------|-------|
| Discovery | **Discovery Case** | Cross-functional; no Signal required. |
| Build | **Product Intent** | Includes delivery and discovery-supporting intent. |
| Run | **Run Case** | Change, incident, capacity, maintenance. |
| Win | **Customer Release Intent** / **Win Case** | Proactive release/market delivery and reactive customer work. |
| Evolve | **Evolve Case** | Process, model, and practice changes. |
| Governance | **Governance Case** | Transition, evidence, approval, audit. |

## Orchestration item vs Workspace Work Order

| | Orchestration item | Workspace Work Order |
|---|---|---|
| Layer | Coordination | Execution |
| Scope | Track-level assembly-line item | One Workspace Scenario invocation |
| Cardinality | One item spawns many Work Orders | One Work Order belongs to one orchestration item graph |
| Lifecycle | Routed, gated, linked across Workspaces or Tracks | Created, executed, completed, failed, or cancelled |
| Owner | Orchestrator | Work Order Runtime and Workspace team |

Examples:

- Moving Product Intent from Specification to Development is orchestration.
- Running a `refine-psd` Scenario in Product Specification Workspace is a Workspace Work Order.
- Opening a Governance Case on that transition is governance orchestration.

## Cross-track handoff examples

```text
Discovery Case -> Product Intent
Product Intent -> Run Case (deployment/change)
Customer Release Intent -> Win Planning / Win Case
Evolve Finding -> Evolve Case
Any transition -> Governance Case
```

## Rule

Do not conflate Work Orders with the item being orchestrated. Work Orders are execution slices. Orchestration items are the durable coordination context.
