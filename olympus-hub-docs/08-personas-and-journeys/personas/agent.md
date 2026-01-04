# Persona: Agent

> **Status:** 🔴 Stub — Placeholder for expansion

---

## Overview

The **Agent** is the operational workforce — human operators who complete tasks assigned through Task Queues. Agents work within a Workbench scope, handling tasks from multiple Scenarios.

| Attribute | Value |
|-----------|-------|
| **Scope** | Workbench |
| **Domain** | Tenant Identity Domain |
| **Primary Console** | Ops Center (Agent View) |

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

---

## Tools and Interfaces

| Tool | Purpose |
|------|---------|
| **Ops Center** | Task inbox, entity views, actions |
| **Knowledge Bank** | Access SOPs, policies, guides |
| **Memory Services** | Access context, history |
| **Tool Invocation** | Query external systems |

---

## Key Journeys

- [Request Lifecycle](../journeys/request-lifecycle.md) — Primary journey

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
- [Ontology - Execution Layer](../../01-concepts/ontology-3-execution-layer.md)

---

*TODO: Detailed task workflows, tool patterns, collaboration modes*

