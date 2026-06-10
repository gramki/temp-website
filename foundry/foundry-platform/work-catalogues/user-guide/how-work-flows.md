# How Work Flows Through the System

This guide explains the big picture of how work moves through ACE Foundry — from an Orchestration Item (OI) through Scenarios to completed Tasks.

## The UPIM Foundation

ACE Foundry implements the [Unified Product Information Model (UPIM)](../../../upim/README.md) Work Model. UPIM defines:

- **6 Tracks:** Build, Discovery, Run, Win, Evolve, Governance
- **Orchestration Items (OIs):** The coordination tokens for each track (Product Intent, Discovery Case, etc.)
- **Work entities:** Epic, Story, Task, Bug, etc.

The Work Catalog is the **executable realization** of UPIM — it turns abstract work model definitions into concrete, runnable workflows and scenarios.

## The Flow: OI → Work Order → Tasks

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  1. Orchestration Item (OI)                                                 │
│     e.g., Product Intent "Add dark mode"                                    │
│                                                                             │
│     OI Workflow defines:                                                    │
│     - Stages: draft → specified → in-development → in-qa → released        │
│     - What Work Orders to create at each transition                         │
└─────────────────────────────────────┬───────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  2. Work Order                                                              │
│     Created when OI enters "in-development" stage                           │
│                                                                             │
│     Work Order specifies:                                                   │
│     - Workspace: development                                                │
│     - Scenario: implement-feature                                           │
│     - Input: { specification_id: "spec-123" }                               │
└─────────────────────────────────────┬───────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  3. Scenario Execution                                                      │
│     Scenario defines:                                                       │
│     - What inputs are required                                              │
│     - What tasks to create                                                  │
│     - What skills are needed                                                │
│     - What outputs to produce                                               │
│                                                                             │
│     Trained Agent assigned based on scenario requirements                   │
└─────────────────────────────────────┬───────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  4. Tasks                                                                   │
│     Human-Agent Team executes tasks:                                        │
│     - Agent drafts code changes                                             │
│     - Human reviews and approves                                            │
│     - Agent applies feedback                                                │
│     - Human completes final review                                          │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Key Concepts

### Orchestration Item (OI)

An **Orchestration Item** is UPIM's coordination token for a Track. Each OI type corresponds to a UPIM track:

| Track | Orchestration Item |
|-------|-------------------|
| Build | Product Intent |
| Discovery | Discovery Case |
| Run | Run Case |
| Win | Customer Release Intent |
| Evolve | Evolve Case |
| Governance | Governance Ritual |

An OI represents a unit of coordinated work that spans multiple Workspaces. "Add dark mode" as a Product Intent might touch Product Specification, UX Design, Development, QA, and Release workspaces.

### OI Workflow

An **OI Workflow** is a state machine that defines how an OI progresses through its lifecycle:

```yaml
orchestration-item: product-intent
stages:
  - name: draft-ready
    handlers:
      - when:
          event: user-task-completed
          params:
            task-label: draft-approval
        then:
          - action: transition-orchestration-item
            params:
              to-stage: ready-for-specification
```

OI Workflows define:
- **Stages** the OI moves through
- **Events** that trigger transitions (task completion, milestone reached, timeout)
- **Actions** to take at transitions (create Work Orders, invoke governance, notify)

OI Workflows are typically authored by Platform Admins and Foundry Admins — they represent organizational process definitions.

### Scenario

A **Scenario** is the **ingress contract** for a Workspace. It defines:

- **What** work the Workspace accepts
- **What** inputs are required
- **What** outputs will be produced
- **What** skills are needed to execute the work

**Crucially:** A Scenario defines WHAT, not HOW. The Trained Agent assigned to execute the scenario determines HOW.

```yaml
name: implement-feature
description: Implement a specified feature from product specification
workspace: development
scope: workspace-ingress

inputs:
  - name: specification_id
    type: string
    required: true

outputs:
  - name: implementation_pr_url
    type: string

required-skills:
  - code-generation
  - test-writing
  - git-operations
```

### Scenario Scope

Scenarios have a `scope` field that determines their visibility:

| Scope | Description | Who Can Invoke |
|-------|-------------|----------------|
| `workspace-ingress` | External contract | Orchestrator (via OI Workflow), other Workspaces |
| `workspace-internal` | Internal implementation | Only Tasks within a Work Order in this Workspace |

**`workspace-ingress`** scenarios form the Workspace's public interface — they're what the Orchestrator can trigger when transitioning an OI. Think of them as the Workspace's API.

**`workspace-internal`** scenarios are implementation details — helper scenarios that Tasks can invoke but that don't appear in the Workspace's external contract. A `review-code` scenario might be internal, called by Tasks within `implement-feature` but not directly invokable by the Orchestrator.

### Work Order

A **Work Order** is an instance of a Scenario — a specific request to do work:

```
Scenario: "implement-feature" (the template)
Work Order: "Implement dark mode toggle" (specific instance)
```

When an OI Workflow creates a Work Order, it specifies:
- Which Scenario to use
- Input values for this specific work
- Priority and assignment

### Trained Agent

A **Trained Agent** defines HOW work gets done. It consists of:

- **Raw Agent** — the base agent model (Claude, GPT-4, etc.)
- **Skills** — reusable capability packages from the registry
- **Guardrails** — constraints on what the agent can do

The relationship:
- **Scenario** = WHAT (the contract: accept these inputs, produce these outputs)
- **Trained Agent** = HOW (the implementation: use these skills, respect these guardrails)

### Skills and Tasks

**Skills** are reusable capability packages that agents can invoke. `code-generation`, `test-writing`, `jira-integration` are examples.

**Tasks** are the actual work items executed by the Human-Agent Team. A scenario might create tasks like:
- "Draft implementation" (agent task)
- "Review code changes" (human task)
- "Write unit tests" (agent task)

Skills can create sub-tasks during execution. For example, a skill processing a user story might create child tasks using internal scenarios — this is how work branches within a Work Order.

## Cross-Workspace Work Flow

Work often needs to move between Workspaces. The OI Workflow orchestrates this:

```
Development Workspace                    QA Workspace
┌────────────────────┐                  ┌────────────────────┐
│ WO: implement-feat │                  │ WO: test-feature   │
│                    │                  │                    │
│ Scenario:          │    OI moves     │ Scenario:          │
│ implement-feature  │ ──────────────► │ test-feature       │
│                    │   to in-qa      │                    │
│ Status: completed  │                  │ Status: in-progress│
└────────────────────┘                  └────────────────────┘
```

When the development Work Order completes:
1. OI Workflow detects `work-order-completed` event
2. Invokes governance check (e.g., code review gate)
3. Transitions OI to `in-qa` stage
4. Creates new Work Order in QA Workspace with `test-feature` scenario

The QA Workspace's `test-feature` scenario (with `scope: workspace-ingress`) accepts this external invocation.

## Putting It Together

1. **Product Manager** creates a Product Intent "Add dark mode"
2. **OI Workflow** governs the PI through draft review, specification, development, QA, release
3. At each stage transition, **Work Orders** are created in the appropriate Workspace
4. Each Work Order runs a **Scenario** that defines the work contract
5. **Trained Agents** execute the scenarios, working with humans on **Tasks**
6. **Skills** provide reusable capabilities; internal scenarios enable sub-task creation
7. When a Work Order completes, the OI Workflow advances the PI to the next stage

The Work Catalog — OI Workflows and Scenarios — is the executable definition of this entire flow.
