# Hub Agent vs Seer Agent: Anti-Patterns

> **Status**: 🟢 Design Complete  
> **Target Audience**: Process Architects, CSAs, Agent Engineers, Developers  
> **Purpose**: When NOT to use Hub Agent pattern and what to use instead

---

## Overview

The Hub Agent pattern is designed for automations that participate in task queues alongside human agents. Not all automations need this pattern. This document describes anti-patterns — situations where using Hub Agent is inappropriate — and provides alternatives.

---

## Anti-Pattern 1: Simple, Stateless Function Calls

### When

The operation is a single, synchronous, stateless function call (e.g., currency conversion, data lookup, validation) that doesn't require complex orchestration, task management, or audit trails.

### Why It's Wrong

Hub Agent pattern adds unnecessary overhead:
- Task queue routing and assignment
- Request lifecycle management
- Async processing complexity
- Agent enrollment and identity management

These overheads are not justified for simple function calls.

### Use Instead

[Hub Application as Standalone Tool](../../02-system-design/implementation-concepts/hub-application-as-standalone-tool.md) — direct HTTP tool invocation without Signal Exchange/Request lifecycle overhead.

### Example

- Currency conversion API
- Customer lookup by ID
- Data validation (format, range checks)
- Simple calculations

These should be standalone tools, not Hub Agents.

> **Reference**: [Hub Application as Standalone Tool](../../02-system-design/implementation-concepts/hub-application-as-standalone-tool.md) describes the pattern for direct tool invocation.

---

## Anti-Pattern 2: Synchronous, Immediate Responses Required

### When

The calling system requires an immediate, synchronous response without waiting for a task to be picked up from a queue or a full request lifecycle to complete.

### Why It's Wrong

Hub Agents operate via task queues (async):
- Tasks are assigned, worked on, then completed
- Adds latency from queue routing and assignment
- Breaks synchronous request/response expectations
- Caller cannot wait for async processing

### Use Instead

- [Hub Application as Standalone Tool](../../02-system-design/implementation-concepts/hub-application-as-standalone-tool.md) for direct invocation
- Direct API integration for system-to-system calls

### Example

- Real-time payment processing requiring immediate confirmation
- Fraud detection requiring immediate approve/deny
- Authentication/authorization checks
- Real-time data validation in UI

Use direct integration, not task queues.

---

## Anti-Pattern 3: Operations That Don't Fit the Task Model

### When

The automation doesn't involve discrete "tasks" that can be assigned, worked on, completed, or abandoned, or doesn't require human-in-the-loop intervention.

### Why It's Wrong

Hub Agent pattern assumes task lifecycle:
- Task assignment
- Work-in-progress tracking
- Completion or abandonment
- Human escalation paths

If the operation doesn't fit this model, you're forcing a square peg into a round hole.

### Use Instead

- Regular [Hub Application](../../02-system-design/implementation-concepts/hub-application.md) triggered directly by Signal Exchange
- Batch processing application for scheduled operations

### Example

- Event stream processing (continuous, not discrete tasks)
- Scheduled ETL jobs (time-based, not task-based)
- Continuous monitoring (ongoing, not task-completion)
- Background data synchronization

These aren't "tasks" in the agent sense.

> **Reference**: [Hub Application](../../02-system-design/implementation-concepts/hub-application.md) describes event-driven applications without task queue participation.

---

## Anti-Pattern 4: Cannot Abandon or Escalate Gracefully

### When

The automation is designed such that it *must* complete its work without any possibility of failure, abandonment, or escalation to a human.

### Why It's Wrong

A core tenet of Hub Agents (especially AI agents) is directability and the ability to gracefully hand off work to a human when encountering unresolvable situations. An agent that cannot abandon or escalate is brittle and lacks resilience.

### Use Instead

Re-evaluate the automation's design to include robust error handling and escalation paths, or consider a simpler, deterministic workflow if no human intervention is ever desired.

### Example

- An agent that crashes if it can't find a specific piece of information, rather than escalating
- A workflow that must complete within a fixed time window with no fallback
- Operations that cannot tolerate any failure mode

> **Reference**: [Agent Directability](../../02-system-design/implementation-concepts/agent-directability.md) describes human intervention patterns.

---

## Anti-Pattern 5: No Need for Task Queue Participation

### When

The automation doesn't need to be managed alongside human agents, doesn't require load balancing across multiple instances, or doesn't benefit from the Supervisor's ability to enroll/unenroll agents from queues.

### Why It's Wrong

The overhead of task queue integration is unnecessary if the automation is a standalone service or a simple event listener.

### Use Instead

Regular [Hub Application](../../02-system-design/implementation-concepts/hub-application.md) that directly consumes signals from Signal Exchange.

### Example

- Notification service that sends an email whenever a specific event occurs
- Log aggregation service
- Metrics collection service
- Simple event-to-action mapping

Use regular Hub Application, not Hub Agent.

---

## Anti-Pattern 6: Missing Identity and Authority Management

### When

The automation performs actions on behalf of a user or a scenario but lacks proper identity (Agent Persona) and authority (Delegation Access Tokens) management.

### Why It's Wrong

Introduces significant security, audit, and compliance risks:
- Actions cannot be attributed
- Unauthorized operations may occur
- Breaks audit trails
- Violates authority chains

### Use Instead

Ensure the automation is properly registered as an Agent Persona in Cipher IAM via [ScenarioAsAgent CRD](../../02-system-design/implementation-concepts/scenario-as-agent.md) and uses the [Unified Delegation Model](../../decision-logs/0130-unified-delegation-model.md) for all actions.

### Example

- A script that modifies customer data without a clear audit trail of who (or what agent) initiated the change
- Quick automation without identity setup
- Background jobs that act on user data without proper authorization

> **Reference**: [ADR-0129: Agent Identity Model](../../decision-logs/0129-agent-identity-model.md) explains identity requirements. [ADR-0130: Unified Delegation Model](../../decision-logs/0130-unified-delegation-model.md) describes authority delegation.

---

## Anti-Pattern 7: Over-engineering for Simple Operations

### When

The task is extremely simple, deterministic, and could be handled by a basic rule or a single API call without any "intelligence" or complex decision-making.

### Why It's Wrong

The Hub Agent pattern, especially with Seer Agents, is designed for complex, cognitive operations. Using it for trivial tasks adds unnecessary complexity, cost, and cognitive overhead for developers and operators.

### Use Instead

- Simple rule in Automation Spec
- [Hub Application as Standalone Tool](../../02-system-design/implementation-concepts/hub-application-as-standalone-tool.md) for reusable logic
- Direct rule engine for simple conditionals

### Example

- "If amount > 1000, flag for review" — this is a simple rule, not an agent task
- "If status = 'pending', send notification" — simple event-to-action
- Basic data transformation without decision logic

---

## Anti-Pattern 8: Need Direct Integration Without Queue Overhead

### When

An external system needs to directly trigger a Hub Application without the overhead of creating a Request, managing a task, or waiting for queue processing.

### Why It's Wrong

While Hub Agents participate in the Hub ecosystem, sometimes a more direct, lightweight integration is needed for specific use cases. Forcing everything through the full Hub Agent lifecycle can be inefficient.

### Use Instead

- Direct signal emission to [Signal Exchange](../04-subsystems/signal-exchange/README.md) (if asynchronous and event-driven)
- [Hub Application as Standalone Tool](../../02-system-design/implementation-concepts/hub-application-as-standalone-tool.md) (if synchronous and function-like)

### Example

- A legacy system that needs to fire a one-off event to Hub without expecting a managed response
- System-to-system integration where you control routing
- Microservice-to-microservice communication

---

## Anti-Pattern 9: Cannot Support Full Agent Lifecycle

### When

The underlying automation cannot support the full lifecycle of an agent, including enrollment, task acceptance, work-in-progress updates, completion, and abandonment.

### Why It's Wrong

The Hub Agent pattern assumes these capabilities. If the automation is a "fire-and-forget" system, it's not truly acting as an agent in the Hub sense.

### Use Instead

A simpler [Hub Application](../../02-system-design/implementation-concepts/hub-application.md) or a different integration pattern.

### Example

- A system that only logs an event and has no further interaction with Hub
- One-way notification systems
- Fire-and-forget operations
- Systems that cannot report completion status

---

## Anti-Pattern 10: Should Be Human-Only Task

### When

The task requires nuanced human judgment, empathy, creativity, or complex physical interaction that cannot be automated by current technology, or where automation would violate ethical guidelines or regulatory requirements.

### Why It's Wrong

Attempting to automate tasks that are fundamentally human-centric can lead to poor outcomes, customer dissatisfaction, and compliance issues.

### Use Instead

Keep the task assigned to human agents, potentially using Hub to provide them with better context and tools.

### Example

- Tasks requiring direct negotiation with a distressed customer
- Creative design work
- Strategic business decisions
- Tasks requiring physical presence or manual inspection

---

## Summary Decision Rule

Use the Hub Agent pattern when the automation needs to:

1. **Participate in a task queue** (alongside humans or other agents)
2. **Be assigned to a Request** and manage its lifecycle
3. **Have a distinct Agent Persona** for accountability and delegation
4. **Produce structured Request Updates** (memos, decisions, outcomes)
5. **Gracefully abandon/escalate** tasks when unable to proceed

If any of these don't apply, consider:

- [Hub Application as Standalone Tool](../../02-system-design/implementation-concepts/hub-application-as-standalone-tool.md) (for simple, synchronous operations)
- Regular [Hub Application](../../02-system-design/implementation-concepts/hub-application.md) (for event-driven, signal-based processing)
- Direct Integration (for system-to-system without queue overhead)

---

## Alternatives Guide

| Pattern | Use When | Characteristics |
|---------|----------|-----------------|
| **Hub Agent** | Task queue participation, human collaboration | Async, task lifecycle, Agent Persona, enrollment |
| **Hub Application as Standalone Tool** | Simple, synchronous function calls | Direct invocation, tool-native response, no Request lifecycle |
| **Regular Hub Application** | Event-driven processing, no task queues | Signal-driven, no enrollment, no Agent Persona required |
| **Direct Integration** | System-to-system, controlled routing | Bypasses Hub patterns, direct API calls |

> **Reference**: [Hub Application](../../02-system-design/implementation-concepts/hub-application.md) describes regular applications. [Hub Application as Standalone Tool](../../02-system-design/implementation-concepts/hub-application-as-standalone-tool.md) describes tool invocation pattern.

---

## Related Documentation

### This Documentation Suite
- [Hub Agent vs Seer Agent](./hub-agent-vs-seer-agent.md) — Entry point and overview
- [Core Concepts](./hub-agent-vs-seer-agent-core.md) — Understanding Hub Agent and Seer Agent
- [Examples](./hub-agent-vs-seer-agent-examples.md) — Concrete use cases
- [Decision Framework](./hub-agent-vs-seer-agent-core.md#part-3-decision-framework) — When to use what
- [Architectural Details](./hub-agent-vs-seer-agent-architectural-details.md) — C2-level implementation references
- [Customer Guide](./hub-agent-vs-seer-agent-customer-guide.md) — Customer-facing explanations
