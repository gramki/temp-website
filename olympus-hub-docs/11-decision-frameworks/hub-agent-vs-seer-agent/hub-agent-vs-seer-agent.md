# Hub Agent vs Seer Agent

> **Status**: 🟢 Design Complete  
> **Target Audience**: Process Architects, CSAs, Agent Engineers, Developers  
> **Purpose**: Entry point for understanding the distinction between Hub Agent (participation pattern) and Seer Agent (AI technology)

---

## Executive Summary

Hub Agent and Seer Agent are distinct concepts that are often conflated. **Hub Agent** is a participation pattern: any Scenario that can act autonomously like an agent, participating in task queues, being assigned to Requests, and producing Request Updates. **Seer Agent** is a concrete AI implementation: an agent that follows the Raw → Trained → Employed lifecycle, runs on Seer runtime, and has AI-specific capabilities (LLM reasoning, tool use, knowledge access).

The relationship is: **Seer Agent ⊆ Hub Agent**. When deployed, a Seer Agent is always a Hub Agent, but a Hub Agent is not always a Seer Agent. Hub Agents can be rule-based (Rhea), workflow-based (Perseus), or AI-based (Seer). The distinction matters for architectural decisions, customer conversations, and implementation choices.

This documentation suite provides decision frameworks, examples, and architectural guidance to clarify when to use which term and how they relate.

---

## The Confusion

Both terms use "Agent" and share characteristics:

- Both can participate in Task Queues
- Both can be assignees to Requests
- Both interact with Signal Exchange
- Both have IAM identities
- Both produce Request Updates

However, they represent different concerns:

- **Hub Agent**: How the automation participates in work (participation model)
- **Seer Agent**: How the automation thinks and reasons (AI technology)

This conflation creates confusion about:
- When to design a Scenario as a Hub Agent
- Whether AI capabilities are required
- How identity and authority work
- What runtime to choose
- How to explain to customers

---

## Quick Reference

| Aspect | Hub Agent | Seer Agent |
|--------|-----------|------------|
| **Nature** | Participation pattern | AI technology |
| **Scope** | Any Scenario that participates like an agent | AI agents on Seer runtime |
| **Runtime** | Rhea, Perseus, Seer, Atlantis | Seer (Atlantis) only |
| **Identity** | Agent Persona (primary) | Agent Persona + SPIFFE ID (two-layer) |
| **Creation** | ScenarioAsAgent CRD | Raw → Trained → Employed lifecycle |
| **Required** | Task queue participation, IAM registration | LLM reasoning, tool use |
| **Relationship** | Superset | Subset (always a Hub Agent when deployed) |

---

## Reading Guide by Audience

### Process Architects

**Start here**: [Core Document: Understanding](./hub-agent-vs-seer-agent-core.md#part-1-understanding) → [Decision Framework](./hub-agent-vs-seer-agent-core.md#part-3-decision-framework)

**Key questions answered**:
- When should I design a Scenario as a Hub Agent?
- What are the participation requirements?
- How does identity work?
- What runtime should I specify?

**Additional reading**:
- [Examples: Non-AI Hub Agents](./hub-agent-vs-seer-agent-examples.md#example-1-rhea-workflow-as-hub-agent)
- [Anti-patterns](./hub-agent-vs-seer-agent-anti-patterns.md)

### CSAs (Customer Solution Architects)

**Start here**: [Core Document: Understanding](./hub-agent-vs-seer-agent-core.md#part-1-understanding) → [Customer Guide](./hub-agent-vs-seer-agent-customer-guide.md) → [Examples](./hub-agent-vs-seer-agent-examples.md#example-4-customer-facing-scenarios)

**Key questions answered**:
- How do I explain Hub Agent vs Seer Agent to customers?
- When does a customer need Hub Agent (non-Seer)?
- When does a customer need Seer Agent?
- What are the business value examples?

**Additional reading**:
- [Decision Framework](./hub-agent-vs-seer-agent-core.md#part-3-decision-framework)
- [Anti-patterns](./hub-agent-vs-seer-agent-anti-patterns.md)

### Developers

**Start here**: [Core Document: Understanding](./hub-agent-vs-seer-agent-core.md#part-1-understanding) → [Core Document: Building](./hub-agent-vs-seer-agent-core.md#part-2-building) → [Architectural Details](./hub-agent-vs-seer-agent-architectural-details.md)

**Key questions answered**:
- What is the architectural relationship between Hub Application and Hub Agent?
- How do I create a Hub Agent from my Hub Application?
- What is ScenarioAsAgent CRD's role?
- Where do I find implementation details?

**Additional reading**:
- [Examples](./hub-agent-vs-seer-agent-examples.md)
- [Anti-patterns](./hub-agent-vs-seer-agent-anti-patterns.md)

### Agent Engineers

**Start here**: [Core Document: Understanding](./hub-agent-vs-seer-agent-core.md#part-1-understanding) → [Core Document: Building](./hub-agent-vs-seer-agent-core.md#part-2-building) → [Architectural Details](./hub-agent-vs-seer-agent-architectural-details.md)

**Key questions answered**:
- How does my Seer Agent become a Hub Agent?
- What is the identity model for Seer Agents?
- How does Scenario binding work?
- Where do I find Seer-specific details?

**Additional reading**:
- [Examples: Seer Agent as Hub Agent](./hub-agent-vs-seer-agent-examples.md#example-2-seer-agent-as-hub-agent)
- [Examples: Composite Applications](./hub-agent-vs-seer-agent-examples.md#example-3-composite-application)

---

## Document Map

This documentation suite consists of:

1. **[Core Document](./hub-agent-vs-seer-agent-core.md)** — Comprehensive understanding, building basics, and decision framework
   - Part 1: Understanding (what they are)
   - Part 2: Building (how they are created)
   - Part 3: Decision Framework (when to use what)

2. **[Examples](./hub-agent-vs-seer-agent-examples.md)** — Concrete use cases and scenarios
   - Rhea Workflow as Hub Agent (non-Seer)
   - Seer Agent as Hub Agent
   - Composite Applications
   - Customer-facing scenarios

3. **[Anti-patterns](./hub-agent-vs-seer-agent-anti-patterns.md)** — When NOT to use Hub Agent pattern
   - 10 anti-patterns with alternatives
   - Summary decision rule

4. **[Architectural Details](./hub-agent-vs-seer-agent-architectural-details.md)** — C2-level architectural details and references
   - ScenarioAsAgent CRD role
   - Identity management overview
   - Protocol interfaces
   - References to implementation documentation

5. **[Customer Guide](./hub-agent-vs-seer-agent-customer-guide.md)** — Customer-facing explanations for CSAs
   - Analogies and conversation guide
   - Decision matrix
   - Business value examples

---

## Key Takeaways

1. **Hub Agent is a pattern, not a technology**. Any Scenario can become a Hub Agent if it can participate in task queues, be assigned to Requests, and produce Request Updates.

2. **Seer Agent is AI technology**. It follows the Raw → Trained → Employed lifecycle and runs on Seer runtime with AI-specific capabilities.

3. **Seer Agent ⊆ Hub Agent**. When deployed, a Seer Agent is always a Hub Agent, but a Hub Agent is not always a Seer Agent.

4. **Identity differs**. Hub Agent identity is primarily Agent Persona (business identity). Seer Agent identity is two-layer: Agent Persona + SPIFFE ID (deployment identity).

5. **Creation differs**. Hub Agents are created via ScenarioAsAgent CRD. Seer Agents are created via the Raw → Trained → Employed lifecycle.

6. **Runtime selection is independent**. Choose runtime (Rhea, Perseus, Seer, Atlantis) based on capability needs, not Hub Agent requirements.

7. **Use the right term**. Use "Hub Agent" when discussing participation, enrollment, and task queues. Use "Seer Agent" when discussing AI capabilities, training, and knowledge.

---

## Related Documentation

### Hub Documentation
- [Scenario as Agent](../../02-system-design/implementation-concepts/scenario-as-agent.md) — Pattern for exposing Scenarios as agents
- [Hub Application](../../02-system-design/implementation-concepts/hub-application.md) — Automation artifact that can become a Hub Agent
- [Agent Model](../../02-system-design/agent-model.md) — How agents interact with Hub

### Seer Documentation
- [Agent Lifecycle](../../../olympus-seer-docs/seer-design/implementation-concepts/agent-lifecycle.md) — Raw → Trained → Employed progression
- [Employed Agent as Hub Application](../../../olympus-seer-docs/seer-design/hub-integration/employed-agent.md) — How Seer Agents integrate with Hub
- [Agent Identity and Credentials](../../../olympus-seer-docs/seer-design/implementation-concepts/agent-identity-credentials.md) — Identity model for Seer Agents

### Architectural Decisions
- [ADR-0129: Agent Identity Model](../../decision-logs/0129-agent-identity-model.md) — Two-layer identity model (Deployment vs Persona)
- [ADR-0130: Unified Delegation Model](../../decision-logs/0130-unified-delegation-model.md) — Unified delegation model (scenario-scoped vs request-scoped)
