# Work Order

A Work Order is the instantiation of a Scenario for execution — a specific (Track, Workspace, Scenario) combination that has been created, assigned, and is ready to run within a Workspace Session.

## What it is

Work Orders are the execution layer of the Foundry Platform. While [Orchestration Items](orchestration-item.md) coordinate what needs to happen across the system, Work Orders are where work actually gets done.

The relationship between Orchestration Items and Work Orders:

| Aspect | Orchestration Item | Work Order |
|--------|-------------------|------------|
| **Layer** | Coordination | Execution |
| **Scope** | Track-level, spans Workspaces | Single Workspace |
| **Storage** | Dual (OI) or Work Item only | Work Item only |
| **Cardinality** | One creates many | Many belong to one |
| **Owner** | Orchestrator | WO Runtime |

When the Orchestrator's OI Workflow determines that an orchestration item has reached a Workspace, it creates a Work Order. That Work Order:

1. References the Scenario to execute
2. Carries `title` and markdown `description` from the orchestration context
3. Gets assigned to users based on skill matching
4. Triggers [Workspace Session](workspace-session.md) activation
5. Creates a [Task](task.md) tree when execution starts
6. Reports completion back to Orchestrator

Work Orders are **Work Items** in the Work Repository (Epics in the Jira adapter for Phase 1). Contract fields include `workRepoKey`, `workRepoProject`, and `workRepoStatus`.

Multiple Work Orders can be attached to a single Workspace Session.

## Where it lives in Foundry

| Module | Responsibility |
|--------|----------------|
| **Orchestrator** | Creates Work Orders when OI reaches Workspace |
| **WO Runtime** | Executes Work Orders, manages Task tree |
| **Work Repository** | System of record |
| **Metadata Service** | Generates unique IDs (WO-1234) |
| **Web App** | Displays WO status, assignment |
| **IDE** | Work Orders panel shows active WOs |

Track-based API: `/workbenches/{workbenchId}/tracks/build/work-orders` — see [../../foundry-work-plan/phase-1/api-surface.md](../../foundry-work-plan/phase-1/api-surface.md).

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Work Order](../../ace/concepts.md) | Work Item per (Track, Workspace, Scenario) |
| Scenario execution | WO Runtime reads Scenario, creates Tasks |
| Workspace work | Multiple WOs can run in one Session |

From Orchestrator README: "Do not conflate [Orchestration Items and Work Orders]. Moving Product Intent from Specification to Development is orchestration. Instantiating a `refine-psd` Scenario in Product Specification Workspace is a Workspace Work Order."

## Related concepts

- [Orchestration Item](orchestration-item.md) — Creates Work Orders at Workspaces
- [Scenario](scenario.md) — Defines what a Work Order executes
- [Task](task.md) — Work units within a Work Order
- [Workspace Session](workspace-session.md) — Where Work Orders execute
- [Delegation](delegation.md) — Authority agents have within a WO

## Further reading

- [../../foundry-work-plan/phase-1/repository-contracts.md](../../foundry-work-plan/phase-1/repository-contracts.md) — Work Order schema
- [../work-order-runtime/README.md](../work-order-runtime/README.md) — WO execution engine
- [../orchestrator/README.md](../orchestrator/README.md) — WO creation and routing
