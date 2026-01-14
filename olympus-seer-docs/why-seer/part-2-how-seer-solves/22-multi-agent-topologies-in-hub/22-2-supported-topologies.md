# 22.2 Supported Topologies

Hub Composite Applications support several multi-agent topology patterns documented in multi-agent topologies concepts: Blackboard (shared memory coordination), Planner-Executor-Critic (PEC Loop), Market-Based (broadcast and bid), and Role-Specialized Committees (multiple perspectives). Each pattern uses OPA filters for update routing and shared Request state for coordination.

This subsection describes how Hub Composite Applications implement these topology patterns, explaining how each pattern works, when each is appropriate, and how OPA filters enable pattern-specific routing.

## Purpose of this Subsection

This subsection describes the topology patterns that Hub Composite Applications support. It explains how each pattern (Blackboard, PEC Loop, Market-Based, Role-Specialized Committees) works, when each is appropriate, and how OPA filters enable pattern-specific routing.

## Core Concepts & Definitions

### Blackboard Pattern

**Blackboard pattern** is a coordination pattern where multiple agents coordinate through shared Request state (blackboard) rather than direct messaging. Agents read from and write to the shared state, with state changes triggering agent actions via OPA filters.

Blackboard pattern implementation:
*   **Shared state**: Request state serves as blackboard
*   **Update routing**: OPA filters route updates based on update type and state
*   **Independent operation**: Each agent operates independently
*   **Extensibility**: Agents can be added or removed without affecting others

The Blackboard pattern is best for multi-specialist collaboration where tasks emerge dynamically and agents contribute independently to shared knowledge.

### Planner-Executor-Critic (PEC Loop) Pattern

**Planner-Executor-Critic (PEC Loop) pattern** is a coordination pattern where a Planner agent creates a plan, an Executor agent performs actions, and a Critic agent evaluates outcomes, with the loop repeating as needed. PEC Loop uses update types for routing: PLAN_CREATED routes to Executor, EXECUTION_COMPLETE routes to Critic, CRITIC_FEEDBACK routes back to Planner.

PEC Loop pattern implementation:
*   **Update type routing**: Update types (PLAN_CREATED, EXECUTION_COMPLETE, CRITIC_FEEDBACK) route to appropriate agents
*   **Loop termination**: Clear termination criteria to prevent infinite loops
*   **Quality gates**: Critic evaluation determines whether to continue, revise, or terminate
*   **State consistency**: Plan, execution, and critique state must be consistent

The PEC Loop pattern is best for safety-sensitive actions requiring verification loops and quality gates.

### Market-Based Pattern

**Market-Based pattern** is a coordination pattern where tasks are broadcast, agents bid based on cost/confidence/availability, and a scheduler assigns tasks to the best bid. Market-Based uses request updates for broadcasting and bidding: broadcast updates route to all bidders, bid updates route to scheduler.

Market-Based pattern implementation:
*   **Broadcast mechanism**: Tasks broadcast via request updates to all eligible agents
*   **Bidding mechanism**: Agents bid via request updates with cost, confidence, or availability information
*   **Scheduling mechanism**: Scheduler agent evaluates bids and assigns tasks via request updates
*   **Utility functions**: Robust utility/cost functions for bid evaluation

The Market-Based pattern is best for dynamic resource allocation and load balancing across specialist agents.

### Role-Specialized Committees Pattern

**Role-Specialized Committees pattern** is a coordination pattern where multiple agents with fixed roles (risk, legal, ops, UX, security) review the same problem, with final decisions via consensus, voting, or an arbiter. Role-Specialized Committees route updates to all committee members, enabling multiple perspectives on the same request.

Role-Specialized Committees pattern implementation:
*   **Role definition**: Clear role definitions for each committee member
*   **Update routing**: Updates route to all committee members
*   **Consensus mechanism**: Consensus, voting, or arbiter for final decisions
*   **Perspective aggregation**: Mechanism to aggregate multiple perspectives

The Role-Specialized Committees pattern is best for high-stakes decisions requiring multiple perspectives and governance gates.

## Conceptual Models / Frameworks

### The Pattern Implementation Model

Each pattern uses OPA filters for update routing:

| Pattern | OPA Filter Strategy | Update Types |
|---------|---------------------|--------------|
| **Blackboard** | Route based on update type and state | All update types |
| **PEC Loop** | Route PLAN_CREATED to Executor, EXECUTION_COMPLETE to Critic | PLAN_CREATED, EXECUTION_COMPLETE, CRITIC_FEEDBACK |
| **Market-Based** | Route broadcasts to bidders, bids to scheduler | TASK_BROADCAST, BID, TASK_ASSIGNED |
| **Role-Specialized Committees** | Route updates to all committee members | All update types |

OPA filters enable pattern-specific routing while maintaining flexibility.

### The Pattern Selection Model

Pattern selection depends on process characteristics:

| Process Characteristic | Recommended Pattern |
|----------------------|---------------------|
| **Dynamic task emergence** | Blackboard |
| **Safety-sensitive actions** | PEC Loop |
| **Dynamic resource allocation** | Market-Based |
| **High-stakes decisions** | Role-Specialized Committees |
| **Multi-specialist collaboration** | Blackboard |
| **Quality verification** | PEC Loop |
| **Load balancing** | Market-Based |
| **Multiple perspectives** | Role-Specialized Committees |

Pattern selection directly impacts coordination effectiveness.

## Systemic and Enterprise Considerations

### Pattern Governance

All patterns must maintain governance:
*   **Authority enforcement**: All agents must respect authority constraints
*   **Audit trail**: All coordination actions must be auditable
*   **Policy compliance**: Coordination must comply with policies
*   **Observability**: Coordination must be observable for monitoring

Governance ensures that all patterns maintain enterprise standards.

### Pattern Performance

All patterns must be performant:
*   **Update routing**: OPA filter evaluation must be fast
*   **State management**: Shared state management must be efficient
*   **Scalability**: Patterns must scale to many agents
*   **Resource utilization**: Patterns must use resources efficiently

Performance directly impacts agent responsiveness and resource utilization.

### Pattern Combination

Organizations can combine patterns:
*   **Nested patterns**: Use patterns within patterns (PEC Loop within Blackboard)
*   **Hybrid patterns**: Combine pattern elements for specific needs
*   **Pattern evolution**: Evolve patterns as processes mature

Pattern combination enables sophisticated coordination for complex processes.

## Common Misconceptions & Failure Modes

### Misconception: One Pattern Fits All

Some organizations assume that one topology pattern (typically Blackboard) is sufficient for all use cases. However, different processes require different patterns: safety-sensitive processes require PEC Loop, dynamic allocation requires Market-Based, high-stakes decisions require Role-Specialized Committees.

**Failure mode**: Organizations use one pattern for all processes, resulting in poor coordination effectiveness or inappropriate patterns for specific use cases.

### Misconception: Patterns Require Explicit Orchestration

Some organizations assume that topology patterns require explicit orchestration (workflow engines, task assignment). However, patterns like Blackboard and Market-Based work through shared state and update routing, not explicit orchestration.

**Failure mode**: Organizations add explicit orchestration to patterns that don't need it, reducing flexibility and increasing complexity.

### Misconception: Patterns Are Mutually Exclusive

Some organizations assume that topology patterns are mutually exclusive—a process uses Blackboard OR PEC Loop, not both. However, patterns can be combined: a Blackboard composite can include a PEC Loop sub-process, or a Role-Specialized Committee can use Market-Based allocation for task distribution.

**Failure mode**: Organizations limit themselves to single patterns, missing opportunities to combine patterns for better coordination.

## Practical Implications

### Pattern Selection Process

Organizations should select patterns through:
*   **Process analysis**: Analyze process characteristics to identify pattern requirements
*   **Pattern matching**: Match process characteristics to pattern capabilities
*   **Prototyping**: Prototype patterns to validate effectiveness
*   **Iteration**: Iterate on pattern selection based on operational experience

Pattern selection directly impacts coordination effectiveness.

### Pattern Implementation

Organizations should implement patterns with:
*   **Clear role definitions**: Define agent roles clearly for each pattern
*   **Update routing design**: Design OPA filters for pattern-specific routing
*   **State management**: Implement robust state management for shared state
*   **Governance integration**: Integrate governance consistently across patterns

Pattern implementation directly impacts coordination reliability and governance compliance.

## Cross-References

*   **Section 5.14.2 (Coordination Pattern Requirements)**: Establishes the topology pattern requirements that Hub Composite Applications implement
*   **Section 22.1 (Hub Composite Applications)**: Describes the composite application architecture that enables these patterns
*   **Section 22.3 (Deployment Model)**: Describes how composites are deployed and routed

---

**References:**

*   `olympus-hub-docs/02-system-design/implementation-concepts/hub-composite-application.md` — Hub Composite Application design
*   `olympus-seer-docs/agentic-ai-concepts/multi-agent-topologies.md` — Multi-agent topology patterns
