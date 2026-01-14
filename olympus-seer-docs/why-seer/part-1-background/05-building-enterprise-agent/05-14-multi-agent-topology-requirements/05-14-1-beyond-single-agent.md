# 5.14.1 Beyond Single-Agent Scenarios

Enterprise business processes are rarely simple enough to be handled by a single agent. Complex cases—dispute investigations, credit approvals, policy changes, fraud detection—require multiple specialized agents working together, each contributing their expertise to reach a comprehensive decision. A single agent cannot be an expert in risk assessment, compliance, customer service, document analysis, and regulatory requirements simultaneously.

This subsection establishes why single-agent scenarios are insufficient for complex business processes and what capabilities are required to support multi-agent topologies. It explains the need for composite applications that enable multiple agents to operate on the same request, and the requirement for cross-runtime composition that allows agents from different runtimes (Seer, Rhea, Atlantis) to collaborate.

## Purpose of this Subsection

This subsection establishes the fundamental need for multi-agent topologies in enterprise deployments. It explains why complex business processes require multiple specialized agents, why composite applications are necessary, and why cross-runtime composition is essential. It distinguishes topology patterns (architectural structures) from coordination mechanisms (interaction protocols) established in Section 5.9.

## Core Concepts & Definitions

### Complex Business Processes

**Complex business processes** are enterprise workflows that require multiple specialized perspectives, expertise domains, or decision criteria to reach a comprehensive outcome. Unlike simple processes that can be handled by a single agent, complex processes require coordination among multiple agents, each contributing their specialized knowledge or capabilities.

Examples of complex business processes include:
*   **Dispute investigations**: Require risk assessment, compliance checking, customer service, and document analysis
*   **Credit approvals**: Require risk evaluation, regulatory compliance, relationship management, and policy adherence
*   **Policy changes**: Require legal review, risk assessment, operational impact analysis, and stakeholder coordination
*   **Fraud detection**: Require pattern recognition, behavioral analysis, compliance checking, and investigation coordination

Each of these processes requires multiple agents because no single agent can possess all necessary expertise or perspectives.

### Composite Applications

**Composite applications** are specifications that enable multiple Hub Applications (agents) to participate in the same Request without explicit orchestration. Composite applications allow agents to coordinate through shared Request state (blackboard pattern) rather than task assignment, enabling sophisticated multi-agent collaboration patterns.

Composite applications must provide:
*   **Multiple apps per request**: Multiple agents can operate on the same request simultaneously
*   **Shared state coordination**: Agents coordinate through shared Request state rather than explicit messaging
*   **Independent operation**: Each agent operates independently with its own session
*   **Update routing**: OPA filters determine which agents receive which request updates

Without composite applications, organizations must use explicit orchestration (task assignment, workflow engines) which is too rigid for dynamic multi-agent topologies.

### Cross-Runtime Composition

**Cross-runtime composition** is the capability for agents from different runtimes (Seer, Rhea, Atlantis, Perseus) to participate in the same composite application. Cross-runtime composition enables organizations to leverage the strengths of different runtimes: Seer agents for reasoning and decision-making, Rhea agents for workflow orchestration, Atlantis agents for document processing, and Perseus agents for specialized tasks.

Cross-runtime composition requires:
*   **Runtime-agnostic coordination**: Coordination mechanisms that work across runtimes
*   **Shared state model**: Request state model that all runtimes can access
*   **Update routing**: Update routing that works across runtimes
*   **Governance consistency**: Governance and audit that work consistently across runtimes

Without cross-runtime composition, organizations are limited to single-runtime solutions, preventing them from leveraging the best runtime for each agent type.

## Conceptual Models / Frameworks

### The Multi-Agent Topology Model

Multi-agent topologies operate on a shared state model:

```
┌─────────────────────────────────────────────────────────┐
│              Shared Request State (Blackboard)            │
│  (Request Updates, Tasks, Decisions, Artifacts)          │
└─────────────────────────────────────────────────────────┘
         ↑              ↑              ↑              ↑
    ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐
    │ Agent 1 │   │ Agent 2 │   │ Agent 3 │   │ Agent 4 │
    │ (Seer)  │   │ (Seer)  │   │(Atlantis)│   │ (Rhea)  │
    └─────────┘   └─────────┘   └─────────┘   └─────────┘
```

Agents read and write to shared state, with OPA filters determining which agents receive which updates. This enables loose coupling and dynamic coordination without explicit orchestration.

### The Composite Application Model

Composite applications group multiple agents:

```
┌─────────────────────────────────────────────────────────┐
│         Composite Application Specification              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │ Risk Agent   │  │ Compliance   │  │ Customer     │ │
│  │ (Seer)       │  │ Agent (Seer) │  │ Service      │ │
│  │              │  │              │  │ Agent (Seer)  │ │
│  └──────────────┘  └──────────────┘  └──────────────┘ │
│  ┌──────────────┐                                     │
│  │ Document     │                                     │
│  │ Analyzer     │                                     │
│  │ (Atlantis)   │                                     │
│  └──────────────┘                                     │
└─────────────────────────────────────────────────────────┘
                        ↓
┌─────────────────────────────────────────────────────────┐
│              Shared Request State                        │
└─────────────────────────────────────────────────────────┘
```

All agents in the composite operate on the same Request, coordinating through shared state.

## Systemic and Enterprise Considerations

### Specialization Requirements

Enterprise processes require specialization:

*   **Domain expertise**: Different agents specialize in different domains (risk, compliance, customer service)
*   **Technology expertise**: Different agents use different technologies (LLMs for reasoning, document processors for extraction)
*   **Regulatory expertise**: Different agents understand different regulatory requirements

Specialization enables agents to be experts in their domains rather than generalists that are mediocre at everything.

### Coordination Complexity

Multi-agent coordination introduces complexity:

*   **State management**: Shared state must be managed consistently across agents
*   **Conflict resolution**: Multiple agents may update the same state concurrently
*   **Update routing**: OPA filters must correctly route updates to appropriate agents
*   **Governance**: Governance must work consistently across all agents in a composite

This complexity must be managed by the platform, not by individual agents.

### Cross-Runtime Requirements

Cross-runtime composition requires:

*   **Runtime interoperability**: Different runtimes must interoperate through shared state
*   **Consistent governance**: Governance must work consistently across runtimes
*   **Unified observability**: Observability must provide unified views across runtimes
*   **Deployment coordination**: Deployment must coordinate across runtimes

Cross-runtime composition enables organizations to use the best runtime for each agent type.

## Common Misconceptions & Failure Modes

### Misconception: Single Agents Can Handle Complex Processes

Some organizations assume that a single, highly capable agent can handle complex business processes. However, complex processes require multiple perspectives and expertise domains that no single agent can possess.

**Failure mode**: Organizations deploy single agents for complex processes, resulting in poor decision quality, missed perspectives, or regulatory violations.

### Misconception: Explicit Orchestration Is Sufficient

Some organizations assume that explicit orchestration (workflow engines, task assignment) is sufficient for multi-agent coordination. However, explicit orchestration is too rigid for dynamic multi-agent topologies and doesn't support patterns like Blackboard or Market-Based coordination.

**Failure mode**: Organizations use explicit orchestration, limiting themselves to Manager-Worker patterns and missing the benefits of dynamic coordination.

### Misconception: Single-Runtime Solutions Are Sufficient

Some organizations assume that single-runtime solutions (all Seer agents, all Rhea agents) are sufficient. However, different agent types benefit from different runtimes: reasoning agents benefit from Seer, workflow agents benefit from Rhea, document processors benefit from Atlantis.

**Failure mode**: Organizations use single-runtime solutions, preventing them from leveraging the best runtime for each agent type.

### Misconception: Topology Patterns Replace Coordination Mechanisms

Some organizations assume that topology patterns (Blackboard, PEC Loop) replace coordination mechanisms (Scenario-as-Tool, Scenario-as-Agent). However, topology patterns and coordination mechanisms serve different purposes: topology patterns define architectural structures, while coordination mechanisms define interaction protocols.

**Failure mode**: Organizations confuse topology patterns with coordination mechanisms, missing opportunities to use both appropriately.

## Practical Implications

### Process Design Considerations

Organizations should design processes that:

*   **Identify specialization needs**: Determine which expertise domains are required
*   **Design agent roles**: Define agent roles based on specialization needs
*   **Choose topology patterns**: Select topology patterns (Blackboard, PEC Loop, etc.) that fit the process
*   **Design coordination**: Design how agents coordinate through shared state

Process design directly impacts agent effectiveness and decision quality.

### Composite Application Strategy

Organizations should develop a composite application strategy that:

*   **Identifies composite candidates**: Identify processes that benefit from multi-agent collaboration
*   **Designs agent composition**: Design which agents participate in each composite
*   **Defines update routing**: Define OPA filters for update routing
*   **Plans cross-runtime usage**: Plan which runtimes to use for which agents

Composite application strategy enables sophisticated multi-agent collaboration.

### Runtime Selection

Organizations should select runtimes based on:

*   **Agent type**: Reasoning agents use Seer, workflow agents use Rhea, document processors use Atlantis
*   **Performance requirements**: Different runtimes have different performance characteristics
*   **Integration needs**: Different runtimes integrate differently with external systems
*   **Governance requirements**: Different runtimes provide different governance capabilities

Runtime selection directly impacts agent performance and capabilities.

## Cross-References

*   **Section 5.9 (Multi-Agent Coordination Requirements)**: Establishes coordination mechanisms that complement topology patterns
*   **Section 22.1 (Hub Composite Applications)**: Describes how Hub Composite Applications implement these requirements
*   **Section 22.2 (Supported Topologies)**: Describes the specific topology patterns that Hub Composite Applications support

---

**References:**

*   `olympus-hub-docs/02-system-design/implementation-concepts/hub-composite-application.md` — Hub Composite Application design
*   `olympus-seer-docs/agentic-ai-concepts/multi-agent-topologies.md` — Multi-agent topology patterns
