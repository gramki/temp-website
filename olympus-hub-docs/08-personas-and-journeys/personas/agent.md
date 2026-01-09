# Persona: Agent

> **Status:** 🔴 Stub — Placeholder for expansion

---

## Overview

The **Agent** is the operational workforce that completes tasks assigned through Task Queues. Agents work within a Workbench scope, handling tasks from multiple Scenarios.

> **Note:** Agent refers to both **Human Agents** and **AI Agents** unless explicitly specified. AI Agents are a type of Agent with the same task processing model but automated decision-making capabilities.

| Attribute | Value |
|-----------|-------|
| **Category** | Hub Persona — Workbench Operations |
| **Scope** | Workbench |
| **Domain** | Tenant Identity Domain |
| **Primary Console** | Ops Center (Agent View) |

> **Note:** Many Agents are also Business Employees who trigger Business Requests. See [Persona Overlap](../README.md#persona-overlap).

---

## Objectives

| Objective | Description |
|-----------|-------------|
| **Complete Tasks** | Process assigned tasks within SLA |
| **Capture Decisions** | Document decisions with required evidence |
| **Collaborate** | Coordinate with other agents and AI systems |
| **Escalate** | Raise issues beyond authority or capability |

---

## Key Activities

### Task Processing

1. **Task Receipt**
   - Receive tasks from assigned queues
   - Review context and requirements
   - Access relevant knowledge and memory

2. **Investigation**
   - Query tools and external systems
   - Review entity history
   - Consult knowledge bases

3. **Decision & Action**
   - Make decisions within authority
   - Execute required actions
   - Capture evidence and rationale

4. **Completion**
   - Update task status
   - Add thoughts and memos
   - Complete or escalate

### Collaboration

| With | Activity |
|------|----------|
| **AI Agent** | Collaborate on shared requests, review AI decisions |
| **Supervisor** | Receive guidance, escalate issues |
| **Other Agents** | Hand off, consult, collaborate |

### Feedback Promotion (Non-Development Workbenches)

1. **Issue Identification**
   - Notice bugs during task processing
   - Observe behavioral patterns
   - Identify improvement opportunities

2. **Feedback Promotion**
   - Promote bugs and observations to development workbench
   - Include context: related request, task, scenario
   - Track promoted feedback status

---

## Hub Capabilities Consumed

### Ops Center — Agent View (Primary Interface)

| Capability | What It Provides |
|------------|------------------|
| **Task Inbox** | View assigned tasks, pick from queues |
| **Task Details** | Request context, entity information, history |
| **Action Panel** | Execute task actions, update status |
| **Entity Views** | View business entity details, lifecycle |
| **Request Timeline** | See full request history, decisions, updates |
| **Collaboration** | View other agents on request, handoff |

### Hub Services Accessed

| Service | Usage |
|---------|-------|
| **Task Management** | Receive tasks, update status, complete |
| **Knowledge Services** | Query SOPs, policies, procedures |
| **Memory Services** | Access Enterprise Memory (context), Agent Memory (session) |
| **Tool Registry** | Discover available tools |
| **Tool Invocation** | Query external systems via registered tools |
| **Request Management** | View request details, add updates |
| **CAF** | Record decisions, attach evidence |

### What They Produce

| Output | Stored In |
|--------|-----------|
| Task Completions | Operations Data |
| Decisions | Enterprise Memory (via CAF) |
| Thoughts/Memos | Request Updates |
| Evidence Bundles | Enterprise Memory (via CAF) |
| Memory Updates | Enterprise/User Memory |

---

## Key Journeys

- [Request Lifecycle](../journeys/request-lifecycle.md) — Primary journey
- [Production Feedback Loop](../journeys/production-feedback-loop.md) — Feedback promotion (non-dev workbenches)

---

## Task States (Agent Perspective)

```
[Assigned] ──→ [In Progress] ──→ [Completed]
                    │
                    ├──→ [Reassigned]
                    │
                    └──→ [Escalated]
```

---

## Related Documentation

- [Task Management](../../04-subsystems/task-management/README.md)
- [Memory Services](../../04-subsystems/memory-services/README.md)
- [Production Feedback](../../02-system-design/implementation-concepts/production-feedback.md) — Feedback promotion concept
- [Agent Desk](../../06-ux-architecture/tenant-domain/agent-desk.md) — Primary interface
- [Ontology - Execution Layer](../../01-concepts/ontology-3-execution-layer.md)

---

*TODO: Detailed task workflows, tool patterns, collaboration modes*

