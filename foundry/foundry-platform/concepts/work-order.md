# Work Order

A Work Order is the instantiation of a Scenario for execution — a specific (Track, Workspace, Scenario) combination that has been created, assigned, and is ready to run within a Workspace Session.

## What it is

Work Orders are the execution layer of the Foundry Platform. While [Orchestration Items](orchestration-item.md) coordinate what needs to happen across the system, Work Orders are where work actually gets done.

The relationship between Orchestration Items and Work Orders:

| Aspect | Orchestration Item | Work Order |
|--------|-------------------|------------|
| **Layer** | Coordination | Execution |
| **Scope** | Track-level, spans Workspaces | Single Workspace |
| **Cardinality** | One creates many | Many belong to one |
| **Owner** | Orchestrator | WO Runtime |

When the Orchestrator's OI Workflow determines that an orchestration item has reached a Workspace, it creates a Work Order. That Work Order:

1. References the Scenario to execute
2. Carries context from the parent orchestration item
3. Gets assigned to users based on skill matching
4. Triggers [Workspace Session](workspace-session.md) activation
5. Creates a [Task](task.md) tree when execution starts
6. Reports completion back to Orchestrator

Work Orders are stored in Jira as Epics within the Workbench project. This provides:

- Unified tracking alongside other work
- Assignment and notification workflows
- History and audit trail
- Integration with existing team processes

Multiple Work Orders can be attached to a single Workspace Session. A developer might have WOs for two different features active in the same session.

## Where it lives in Foundry

| Module | Responsibility |
|--------|----------------|
| **Orchestrator** | Creates Work Orders when OI reaches Workspace |
| **WO Runtime** | Executes Work Orders, manages Task tree |
| **Jira** | System of record (Epic issue type) |
| **Metadata Service** | Generates unique IDs (WO-1234) |
| **Web App** | Displays WO status, assignment |
| **IDE** | Work Orders panel shows active WOs |

Work Order lifecycle:

```
Created (by Orchestrator)
    → Assigned (by Orchestrator, based on skills/capacity)
    → Session Activated (WO Runtime creates/attaches Session)
    → In Progress (Tasks created, agents spawned)
    → Completed / Failed / Cancelled
    → Orchestrator Notified (for OI advancement)
```

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Work Order](../../ace/concepts.md) | Jira Epic per (Track, Workspace, Scenario) |
| Scenario execution | WO Runtime reads Scenario, creates Tasks |
| Workspace work | Multiple WOs can run in one Session |

From Orchestrator README: "Do not conflate [Orchestration Items and Work Orders]. Moving Product Intent from Specification to Development is orchestration. Instantiating a `refine-psd` Scenario in Product Specification Workspace is a Workspace Work Order."

Work Orders connect UPIM's abstract Work Model to concrete execution. UPIM defines what work exists; Work Orders are the instances of that work being performed.

## Related concepts

- [Orchestration Item](orchestration-item.md) — Creates Work Orders at Workspaces
- [Scenario](scenario.md) — Defines what a Work Order executes
- [Task](task.md) — Work units within a Work Order
- [Workspace Session](workspace-session.md) — Where Work Orders execute
- [Delegation](delegation.md) — Authority agents have within a WO

## Further reading

- [../work-order-runtime/README.md](../work-order-runtime/README.md) — WO execution engine
- [../orchestrator/README.md](../orchestrator/README.md) — WO creation and routing
- [../orchestrator/user-guide/product-intent-journey.md](../orchestrator/user-guide/product-intent-journey.md) — End-to-end walkthrough
- [../../ace/concepts.md](../../ace/concepts.md) — ACE definitions
