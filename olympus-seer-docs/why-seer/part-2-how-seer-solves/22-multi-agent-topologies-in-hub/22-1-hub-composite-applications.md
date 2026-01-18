# 22.1 Hub Composite Applications

Hub Composite Applications enable multiple Hub Applications to participate in the same Request without explicit orchestration. Applications coordinate through shared Request state (blackboard pattern) rather than task assignment, supporting multi-agent topologies like Blackboard, Planner-Executor-Critic (PEC Loop), Market-Based, and Role-Specialized Committees.

Hub Composite Applications address the composite application requirements established in Section 5.14.1, enabling multiple specialized agents to collaborate on complex business processes while maintaining governance, observability, and operational controls.

## Purpose of this Subsection

This subsection describes how Hub implements composite applications. It explains how multiple applications participate in the same request, how OPA filters route updates to appropriate applications, how applications coordinate through shared state, and how cross-runtime composition enables agents from different runtimes to collaborate.

## Core Concepts & Definitions

### Hub Composite Application Definition

**Hub Composite Application** is a specification that groups multiple Hub Applications to participate in the same Request. Each application:
*   Receives Request Updates from Signal Exchange (subject to OPA filters)
*   Operates independently with its own session
*   Can create tasks, produce updates, and modify request state
*   Coordinates implicitly through shared Request state (blackboard pattern)

Composite applications enable sophisticated multi-agent collaboration without requiring explicit orchestration or workflow engines.

### Multiple Apps per Request

**Multiple apps per request** means that multiple Hub Applications can operate on the same Request simultaneously. This enables:
*   **Parallel perspectives**: Multiple agents can contribute different perspectives to the same request
*   **Specialized expertise**: Different agents can contribute their specialized expertise
*   **Dynamic coordination**: Agents coordinate through shared state rather than explicit messaging
*   **Cross-runtime composition**: Apps can span multiple runtimes (Seer, Rhea, Atlantis)

Multiple apps per request enable sophisticated multi-agent collaboration patterns that single-app scenarios cannot support.

### OPA Filters for Update Routing

**OPA filters** determine which applications receive which request updates. When a Request Update arrives:
1. Application Router looks up scenario in routing table
2. If scenario has multiple apps (composite):
   - For each app, evaluate OPA filter
   - If filter allows, dispatch update to app
3. If scenario has single app (standard):
   - Existing behavior (direct dispatch)

OPA filters enable pattern-specific routing: Blackboard patterns route based on update type and state, PEC Loop patterns route PLAN_CREATED to Executor, EXECUTION_COMPLETE to Critic, etc.

### Cross-Runtime Composition

**Cross-runtime composition** enables agents from different runtimes (Seer, Rhea, Atlantis, Perseus) to participate in the same composite application. This enables:
*   **Runtime selection**: Organizations can use the best runtime for each agent type
*   **Technology diversity**: Different agents can use different technologies
*   **Unified coordination**: All agents coordinate through shared Request state regardless of runtime

Cross-runtime composition enables organizations to leverage the strengths of different runtimes while maintaining unified coordination and governance.

### Sub-Personas for Composite Agents

In Hub Composite Applications, each agent in the composite receives its own **sub-persona** derived from the base Agent Persona:

```
Base Agent Persona: dispute-resolution-agent@acme.hub.io
    ↓
Composite Application creates:
    ├── Sub-Persona: dispute-analyst-agent (derived from base)
    ├── Sub-Persona: dispute-reviewer-agent (derived from base)
    └── Sub-Persona: dispute-approver-agent (derived from base)
```

Each sub-persona has its own distinct identity for delegation and audit, but all derive from the same base Agent Persona. This enables:
*   **Individual Accountability**: Each agent's actions are attributed to its specific sub-persona
*   **Shared Authority Source**: All sub-personas inherit from the same base delegation
*   **Audit Clarity**: Composite application actions can be traced to specific sub-personas while maintaining the base persona context

Sub-personas ensure that each agent in a composite has distinct identity for delegation chains and audit logs, while maintaining the relationship to the base Agent Persona from the Scenario.

> **See**: Section 8.1 (Agent Identity) for the two-layer identity model and Section 8.2 (Delegation Chains) for how sub-personas appear in delegation chains.

## Conceptual Models / Frameworks

### The Composite Application Architecture

Composite applications group multiple agents:

```
Hub Composite Application Specification
    ├── Risk Agent (Seer)
    ├── Compliance Agent (Seer)
    ├── Customer Service Agent (Seer)
    └── Document Analyzer (Atlantis)
            ↓
    Shared Request State (Blackboard)
    ├── Request Updates
    ├── Tasks
    ├── Decisions
    └── Artifacts
```

All agents in the composite operate on the same Request, coordinating through shared state.

### The Update Routing Model

OPA filters route updates to appropriate agents:

```
Request Update
    ↓
Application Router (Signal Exchange)
    ↓
OPA Filter Evaluation (per app)
    ├── Risk Agent (if filter allows)
    ├── Compliance Agent (if filter allows)
    ├── Customer Service Agent (if filter allows)
    └── Document Analyzer (if filter allows)
```

OPA filters enable pattern-specific routing while maintaining flexibility.

## Systemic and Enterprise Considerations

### Deployment-Time Resolution

Composites are resolved at deployment time by the Composite Deployment Operator:
1. **Recursive Resolution**: Flattens nested composites to union of all apps
2. **Child Deployment Creation**: Creates `HubApplicationDeployment` for each app
3. **Routing Table Population**: Populates routing table with flattened app list + OPA filters

Signal Exchange doesn't know about composites—it just sees "Scenario X has apps [A, B, C] with filters [F1, F2, F3]". This ensures that composite applications work seamlessly with existing Hub infrastructure.

### Update Conflict Resolution

Multiple apps can update the same request concurrently:
*   **Latest wins**: Timestamp-based resolution
*   **Illegal updates rejected**: OPA policy determines legality
*   **Rejected updates recorded**: History includes rejection reason and source app

Update conflict resolution ensures that composite applications maintain request state consistency while allowing parallel updates.

### Governance Requirements

Composite applications must maintain governance:
*   **Authority enforcement**: All apps must respect authority constraints
*   **Audit trail**: All coordination actions must be auditable
*   **Policy compliance**: Coordination must comply with policies
*   **Observability**: Coordination must be observable for monitoring

Governance ensures that composite applications maintain enterprise standards.

## Common Misconceptions & Failure Modes

### Misconception: Composites Require Explicit Orchestration

Some organizations assume that composite applications require explicit orchestration (workflow engines, task assignment). However, composites coordinate through shared state and OPA filters, not explicit orchestration.

**Failure mode**: Organizations add explicit orchestration to composites, reducing flexibility and increasing complexity.

### Misconception: All Apps Must Be Same Runtime

Some organizations assume that all apps in a composite must be from the same runtime. However, composites support cross-runtime composition, enabling agents from different runtimes to collaborate.

**Failure mode**: Organizations limit composites to single runtimes, preventing them from leveraging the best runtime for each agent type.

### Misconception: Composites Are Just Multiple Apps

Some organizations assume that composite applications are just multiple apps without special coordination. However, composites provide shared state coordination, OPA filter routing, and cross-runtime composition that multiple independent apps don't provide.

**Failure mode**: Organizations try to coordinate multiple independent apps manually, missing the benefits of composite applications.

## Practical Implications

### Composite Design

Organizations should design composites that:
*   **Identify agent roles**: Define which agents participate and their roles
*   **Design update routing**: Design OPA filters for pattern-specific routing
*   **Plan state management**: Plan how agents coordinate through shared state
*   **Consider cross-runtime**: Consider which runtimes to use for which agents

Composite design directly impacts coordination effectiveness and governance compliance.

### Pattern Selection

Organizations should select topology patterns that:
*   **Match process characteristics**: Select patterns that match process needs
*   **Enable effective coordination**: Select patterns that enable effective coordination
*   **Maintain governance**: Select patterns that maintain governance requirements
*   **Support scalability**: Select patterns that scale to process needs

Pattern selection directly impacts coordination effectiveness and system scalability.

## Cross-References

*   **Section 5.14.1 (Beyond Single-Agent Scenarios)**: Establishes the need for composite applications
*   **Section 5.14.2 (Coordination Pattern Requirements)**: Establishes topology pattern requirements
*   **Section 16.3 (Coordination Patterns in Hub)**: Describes Hub Composite Applications as a coordination pattern
*   **Section 22.2 (Supported Topologies)**: Describes the specific topology patterns that composites support

---

**References:**

*   `olympus-hub-docs/02-system-design/implementation-concepts/hub-composite-application.md` — Hub Composite Application design
