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
| **Governance** | Governance Ritual / Governance Enforcement | Rituals, policy assertion, evidence, approvals, findings, registers, recognition. |

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
- **Governance orchestration has two modes.** Rituals organize cadence/event reviews; Enforcement asserts policy and produces verdicts, findings, and register entries.
- **Governance Enforcement evaluates controls.** Enforcement resolves the effective Control Objective, Control Objective Indicators, thresholds, and Approver before allowing Debt + Catch-Up or Exception / Waiver outcomes.
- **Orchestration items are Track-scoped; Work Orders are Workspace-scoped.** One orchestration item can create many Workspace Work Orders.

## Work Order Creation

When an orchestration item reaches a (Track, Workspace) state, Orchestrator creates a Work Order:

### Creation Process

1. **Determine context** — Identify (Track, Workspace Type) from orchestration state
2. **Select Workbench** — From orchestration item's product affiliation
3. **Create in Jira** — Create WO in Workbench's Jira project (one project per Workbench)
4. **Set Scenario** — From Workspace definition or orchestration item metadata
5. **Record linkage** — Link WO to parent orchestration item

### Jira Integration

Each Workbench has a dedicated Jira project for Work Orders:

```
Jira Project: PRODUCT-ABC-WO
├── WO-567: Implement user preferences feature
│   ├── Scenario: implement-feature
│   ├── Work Type: Development
│   └── Source: PI-123 (Product Intent)
└── WO-568: Review code for preferences feature
    ├── Scenario: code-review
    ├── Work Type: Development
    └── Source: PI-123
```

## Work Order Assignment

Orchestrator assigns Work Orders to users based on:

| Factor | Weight | Description |
|--------|--------|-------------|
| **Skill matching** | High | User has skills matching the Scenario |
| **Capacity** | High | User has available capacity (not overloaded) |
| **Affinity** | Medium | User worked on related orchestration items |
| **Workload balance** | Medium | Distribute work across team |
| **Manual override** | Override | Admin explicitly assigns |

### Assignment Flow

```
1. Identify candidate users (Workspace membership)
2. Filter by skill match (Scenario requirements)
3. Score by capacity and affinity
4. Assign to highest-scoring user
5. Or: queue for team pickup if no clear assignee
```

## Session Activation

After assigning a WO, Orchestrator may activate the user's Workspace Session.

### Activation Decision

```
WO assigned to user
    │
    ├── Is session running?
    │   └── Yes → Done (WO Runtime will pick up)
    │
    └── No → Check user's auto-activation config
            │
            ├── auto-activate: true
            │   ├── Check quiet hours
            │   │   ├── In quiet hours → Wait
            │   │   └── Outside quiet hours → Activate
            │   └── Check trigger scenarios
            │       ├── Scenario matches → Activate
            │       └── Scenario doesn't match → Wait
            │
            └── auto-activate: false → Wait
```

### User Configuration

Users configure auto-activation preferences:

```yaml
session-activation:
  auto-activate: true
  trigger-scenarios:
    - implement-feature
    - code-review
    - fix-bug
  quiet-hours:
    enabled: true
    start: "22:00"
    end: "08:00"
    timezone: "America/New_York"
```

### Cross-User Dependency Activation

When a task completion unblocks another user's task:

1. Orchestrator detects blocked task now Ready
2. Orchestrator checks if assignee's session is stopped
3. If auto-activate configured, Orchestrator starts their session

This enables parallel work across users without manual coordination.

## Completion Handling

### Receiving Completion Notifications

WO Runtime notifies Orchestrator when a Work Order completes:

```json
{
  "work_order": "WO-567",
  "verdict": "success",
  "completed_at": "2026-05-28T14:30:00Z",
  "artifacts": {
    "pull_requests": ["PR-234", "PR-235"],
    "test_coverage": 0.87,
    "build_id": "build-12345"
  },
  "metrics": {
    "total_tasks": 12,
    "agent_tasks": 8,
    "human_tasks": 4,
    "total_duration_hours": 6.5,
    "agent_cost_usd": 12.34
  }
}
```

### Advancing Orchestration Items

Upon completion:

1. Record WO completion in orchestration history
2. Evaluate gate conditions (if at transition)
3. If gates pass, advance orchestration item to next Workspace
4. Create next Work Order(s) as needed

### Verdict Handling

| Verdict | Action |
|---------|--------|
| `success` | Advance orchestration item |
| `partial` | Advance with warnings; may require human review |
| `failed` | Block; require human intervention |
| `cancelled` | Record cancellation; may unblock alternatives |

## Orchestration Item Workflows

Each orchestration item type has a YAML workflow definition that specifies:
- **Stages** — Named states the item progresses through
- **Handlers** — Event-driven logic (when/then blocks)
- **Actions** — Operations like creating WOs or transitioning stages

Workflows are defined at Foundry, Workshop, or Workbench level (closest wins).

See [orchestration-item-workflow.md](orchestration-item-workflow.md) for the complete schema specification and [sample-pi-workflow.yaml](sample-pi-workflow.yaml) for a working Product Intent example.

## Open Questions

- How does Orchestrator resolve the effective Control Owner and Approver from the Governance Authority Matrix?
- When Enforcement returns Debt + Catch-Up or Exception / Waiver, does Orchestrator block until the required register record exists?

## Read Next

- [pi-journey.md](pi-journey.md) — end-to-end Product Intent walkthrough
- [orchestrator-requirements.md](orchestrator-requirements.md) — detailed module requirements
- [orchestration-item-workflow.md](orchestration-item-workflow.md) — workflow YAML schema
- [sample-pi-workflow.yaml](sample-pi-workflow.yaml) — complete PI workflow example
- [../work-order-runtime/end-to-end-work-order-flow.md](../work-order-runtime/end-to-end-work-order-flow.md) — complete WO lifecycle including Orchestrator phases
- [../work-order-runtime/README.md](../work-order-runtime/README.md) — WO Runtime execution engine
- [../../ace/governance.md](../../ace/governance.md) — governance model
- [../../ace/product-evolution-cycle.md](../../ace/product-evolution-cycle.md) — how Product Intent moves
- [../../ace/how-product-evolves/orchestration-items.md](../../ace/how-product-evolves/orchestration-items.md) — orchestration item model
- [../../tldr-faq.md](../../tldr-faq.md) — orchestration design decisions
