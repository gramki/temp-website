---
name: Multi-Agent Topology Implementation Guides
overview: Create 9 guide documents explaining how each multi-agent topology from the catalog can be implemented using Seer and Hub capabilities (Hub Applications, Composite Applications, Employed Agents, task queues, scenario-as-agent, scenario-as-tool, and sentinels).
todos:
  - id: guide_01_manager_worker
    content: Create 01-manager-worker.md guide with task delegation and scenario-as-agent approaches
    status: pending
  - id: guide_02_hierarchical
    content: Create 02-hierarchical.md guide with nested queues and composite app approaches
    status: pending
  - id: guide_03_pec_loop
    content: Create 03-planner-executor-critic.md guide with composite OPA filters and scenario-as-tool approaches
    status: pending
  - id: guide_04_blackboard
    content: Create 04-blackboard.md guide with composite application and multi-app coordination approaches
    status: pending
  - id: guide_05_market_based
    content: Create 05-market-based-auction.md guide with broadcast tasks and scenario-as-agent bidding approaches
    status: pending
  - id: guide_06_peer_to_peer
    content: Create 06-peer-to-peer-swarm.md guide with composite event-driven and independent apps approaches
    status: pending
  - id: guide_07_committees
    content: Create 07-role-specialized-committees.md guide with composite parallel and task queue role-based approaches
    status: pending
  - id: guide_08_event_driven
    content: Create 08-event-driven-reactive.md guide with composite OPA filters and signal-based coordination approaches
    status: pending
  - id: guide_09_cognitive_twin
    content: Create 09-cognitive-twin-shadow.md guide with composite shadow and request sentinel approaches
    status: pending
  - id: guide_readme
    content: Create README.md index with overview and links to all 9 topology guides
    status: pending
    dependencies:
      - guide_01_manager_worker
      - guide_02_hierarchical
      - guide_03_pec_loop
      - guide_04_blackboard
      - guide_05_market_based
      - guide_06_peer_to_peer
      - guide_07_committees
      - guide_08_event_driven
      - guide_09_cognitive_twin
---

# Multi-Agent Topology Implementation Guides

## Overview

Create 9 guide documents in `olympus-seer-docs/seer-design/guides/multi-agent-topologies/`, one for each topology from [multi-agent-topologies.md](../../agentic-ai-concepts/multi-agent-topologies.md). Each guide explains how to implement the topology using Seer and Hub capabilities.

## Structure for Each Guide

Each guide follows this structure:

1. **Overview** - Brief description of the topology and its characteristics
2. **Use Cases** - When to use this topology
3. **Implementation Approaches** - At least 2 different ways to achieve the topology
4. **Approach 1: [Name]** - Detailed explanation with:

- Architecture diagram (mermaid)
- Components used (Hub Apps, Composite Apps, Employed Agents, etc.)
- Configuration examples (CRD snippets)
- Flow description

5. **Approach 2: [Name]** - Alternative implementation
6. **Comparison** - When to use each approach
7. **Sentinels** - How sentinels can enhance this topology (optional)
8. **Related Patterns** - Links to other topologies or patterns

## Topologies to Document

### 1. Manager-Worker (Orchestrator)

**File:** `01-manager-worker.md`

**Approaches:**

- **Approach 1: Single Hub Application with Task Delegation** - Manager app creates tasks, workers are Employed Agents assigned to task queues
- **Approach 2: Composite Application with Scenario-as-Agent** - Manager as Hub App, Workers as Scenario-as-Agent enrolled in task queues

**Key Concepts:**

- Manager Hub Application creates tasks
- Worker Employed Agents assigned via task queue escalation matrix
- Manager aggregates worker outputs

### 2. Hierarchical (Multi-Level Orchestration)

**File:** `02-hierarchical.md`

**Approaches:**

- **Approach 1: Nested Task Queues with Escalation** - Each level has its own task queue, escalation creates parent-level tasks
- **Approach 2: Composite Application with Layered Apps** - Each layer is a Hub App in composite, coordination via Request state

**Key Concepts:**

- Multi-level task queues with escalation
- Parent-child request hierarchy
- Layer-specific Hub Applications

### 3. Planner-Executor-Critic (PEC Loop)

**File:** `03-planner-executor-critic.md`

**Approaches:**

- **Approach 1: Composite Application with OPA Filters** - Three apps (Planner, Executor, Critic) in composite, OPA filters route updates by update_type
- **Approach 2: Scenario-as-Tool Chain** - Planner creates plan, Executor invokes Critic as tool, Critic invokes Planner as tool for feedback

**Key Concepts:**

- Composite Application with OPA filter-based routing
- Update types as coordination mechanism (PLAN_CREATED, EXECUTION_COMPLETE, CRITIC_FEEDBACK)
- Scenario-as-Tool for synchronous feedback loops

### 4. Blackboard (Shared Memory Coordination)

**File:** `04-blackboard.md`

**Approaches:**

- **Approach 1: Composite Application (Primary)** - Multiple apps in composite, all read/write to shared Request state, OPA filters for selective updates
- **Approach 2: Multiple Hub Apps with Request State** - Separate apps coordinate via Request updates, no composite needed

**Key Concepts:**

- Composite Application with multiple apps
- Request state as blackboard
- OPA filters for selective update routing
- Cross-runtime support (Seer + Rhea + Atlantis)

### 5. Market-Based / Auction

**File:** `05-market-based-auction.md`

**Approaches:**

- **Approach 1: Composite Application with Broadcast Updates** - Broadcaster app creates tasks, Specialist apps bid via task assignment, Assigner app evaluates bids
- **Approach 2: Task Queue with Multiple Scenario-as-Agent** - Multiple Scenario-as-Agent enrolled in same queue, allocation algorithm selects best bidder

**Key Concepts:**

- Task creation as broadcast
- Multiple agents bid on tasks
- Allocation algorithm selects winner
- Scenario-as-Agent for automated bidding

### 6. Peer-to-Peer (Swarm)

**File:** `06-peer-to-peer-swarm.md`

**Approaches:**

- **Approach 1: Composite Application with Event-Driven Updates** - All apps in composite, each reacts to Request updates, no central coordinator
- **Approach 2: Multiple Independent Hub Apps** - Apps operate independently, coordinate via Request updates and signals

**Key Concepts:**

- No central coordinator
- Event-driven coordination
- Request updates trigger agent actions
- Sentinels for swarm health monitoring

### 7. Role-Specialized Committees

**File:** `07-role-specialized-committees.md`

**Approaches:**

- **Approach 1: Composite Application with Parallel Perspectives** - Multiple specialist apps in composite, each provides perspective, Coordinator app aggregates
- **Approach 2: Task Queue with Role-Based Assignment** - Committee task created, assigned to multiple agents by role, each provides input

**Key Concepts:**

- Composite Application with specialist apps
- Parallel task assignment to multiple agents
- Coordinator/Arbiter app for decision
- Role-based agent selection

### 8. Event-Driven Agents (Reactive Mesh)

**File:** `08-event-driven-reactive.md`

**Approaches:**

- **Approach 1: Composite Application with OPA Filters** - Multiple apps in composite, OPA filters route events to relevant apps
- **Approach 2: Signal-Based Coordination** - Apps subscribe to signals, react independently, no composite needed

**Key Concepts:**

- OPA filters for event routing
- Signal Exchange as event bus
- Reactive agent behavior
- Request Sentinels for event monitoring

### 9. Cognitive Twin / Shadow Agents

**File:** `09-cognitive-twin-shadow.md`

**Approaches:**

- **Approach 1: Composite Application with Shadow App** - Primary app proposes action, Shadow app evaluates, both in composite
- **Approach 2: Request Sentinel as Shadow** - Primary app operates normally, Request Sentinel observes and creates shadow evaluation request

**Key Concepts:**

- Composite Application with primary + shadow
- Scenario-as-Tool for shadow evaluation
- Request Sentinels for automatic shadow enrollment
- Shadow app creates child request for evaluation

## Implementation Details

### Common Sections Across All Guides

1. **Topology Overview** - Reference to the catalog entry
2. **Seer/Hub Mapping** - How topology concepts map to Seer/Hub concepts
3. **Architecture Diagrams** - Mermaid diagrams showing component relationships
4. **CRD Examples** - Key CRD snippets (HubApplicationSpec, HubCompositeApplicationSpec, ScenarioAsAgent, etc.)
5. **Flow Descriptions** - Step-by-step execution flows
6. **Configuration Examples** - OPA filters, task queue configurations, etc.
7. **Multi-Runtime Examples** - Where applicable, show Seer + Rhea + Atlantis combinations

### Key Patterns to Document

- **Composite Applications** - For topologies requiring multiple apps in same Request
- **Task Queues** - For topologies requiring task assignment and delegation
- **Scenario-as-Agent** - For topologies requiring automated task completion
- **Scenario-as-Tool** - For topologies requiring synchronous agent invocation
- **Request Sentinels** - For topologies requiring oversight or shadow evaluation
- **OPA Filters** - For selective update routing in composites

## Files to Create

1. `olympus-seer-docs/seer-design/guides/multi-agent-topologies/01-manager-worker.md`
2. `olympus-seer-docs/seer-design/guides/multi-agent-topologies/02-hierarchical.md`
3. `olympus-seer-docs/seer-design/guides/multi-agent-topologies/03-planner-executor-critic.md`
4. `olympus-seer-docs/seer-design/guides/multi-agent-topologies/04-blackboard.md`
5. `olympus-seer-docs/seer-design/guides/multi-agent-topologies/05-market-based-auction.md`
6. `olympus-seer-docs/seer-design/guides/multi-agent-topologies/06-peer-to-peer-swarm.md`
7. `olympus-seer-docs/seer-design/guides/multi-agent-topologies/07-role-specialized-committees.md`
8. `olympus-seer-docs/seer-design/guides/multi-agent-topologies/08-event-driven-reactive.md`
9. `olympus-seer-docs/seer-design/guides/multi-agent-topologies/09-cognitive-twin-shadow.md`
10. `olympus-seer-docs/seer-design/guides/multi-agent-topologies/README.md` - Index with links to all guides

## Dependencies

- Reference existing documentation:
- [Hub Composite Application](../../../olympus-hub-docs/02-system-design/implementation-concepts/hub-composite-application.md)
- [Scenario as Agent](../../../olympus-hub-docs/02-system-design/implementation-concepts/scenario-as-agent.md)
- [Scenario as Tool](../../../olympus-hub-docs/02-system-design/implementation-concepts/scenario-as-tool.md)
- [Employed Agent](../hub-integration/employed-agent.md)
- [Task Queues](../../../olympus-hub-docs/04-subsystems/task-management/task-queues.md)
- [Seer Sentinels](../subsystems/seer-sentinels/README.md)

## Questions to Resolve

1. **Task Queue Assignment**: Can Employed Agents be explicitly assigned to task queues, or only via IAM roles/groups?
2. **Scenario-as-Agent Enrollment**: Is enrollment automatic when ScenarioAsAgent CRD is created, or requires separate enrollment step?
3. **Composite App OPA Filters**: Should examples show inline Rego policies or reference external policies?
4. **Sentinels Integration**: Should sentinel examples be included in every topology, or only where particularly relevant?

## Success Criteria

- Each topology has at least 2 implementation approaches documented
- Each approach includes architecture diagram and configuration examples
- Guides are self-contained but cross-reference related patterns
- Examples show both Seer-only and multi-runtime scenarios where applicable
- All guides follow consistent structure and formatting