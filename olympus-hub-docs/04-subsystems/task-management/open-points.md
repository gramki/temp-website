# Task Management - Open Points

> **Status:** 🟡 Open Questions — Requiring Clarification

This document captures open points and questions that need clarification for the Task Management subsystem.

---

## Task Priority Model

**Issue:** Task priority is referenced in Task Solver UI but the priority model is not fully specified.

**Questions:**
- What are the valid priority levels? (e.g., low, normal, high, urgent, critical)
- How does priority affect allocation algorithms?
- Can priority be changed after task creation? By whom?
- Does priority override SLA calculations?

**Current State:**
- `priority.level` and `priority.override_reason` in task entity
- No priority level enumeration defined
- No allocation algorithm priority handling specified

---

## ~~Task Creation via Signal Exchange~~ ✅ Resolved

**Clarifications:**
- `CREATE_TASK` is a type of `REQUEST_UPDATE` message
- Tasks can be created by Hub Applications AND external systems (via signals)
- Validation: The data provided must agree with the task schema defined in the Scenario. No additional validation required.

---

## Escalation Timer Management

**Issue:** How escalation timers are managed during various task state changes.

**Questions:**
- When task goes ON_HOLD, do escalation timers pause?
- If escalation timer expires while task is ON_HOLD, does escalation still occur?
- How are escalation timers reset (or not) when task is abandoned and reallocated?

**Current State:**
- SLA clock pause during ON_HOLD is documented
- Escalation timer behavior during ON_HOLD not explicitly stated

---

## Multiple Escalation Level Agents

**Issue:** How multiple agents at the same escalation level are handled.

**Questions:**
- Can multiple agents be assigned at the same escalation level?
- If yes, is this controlled by the allocation algorithm?
- How does "first wins" apply when multiple agents are at the same level?

**Current State:**
- Documentation implies one agent per escalation level
- Not explicitly stated whether multiple assignments at same level are possible

**Partial Clarification:** If SLA pauses (ON_HOLD), escalation timers can also pause.
---

## ~~Task Dependency / Sequencing~~ ✅ Resolved

**Clarifications:**
- Hub Applications manage task sequencing (not Task Management)
- Scenario settings can:
  - Disallow tasks from any source other than the application
  - Prevent concurrent pending/incomplete tasks
- Task Management does not natively support task dependencies 
---

## ~~Skills Management~~ ✅ Resolved

**Clarifications:**
- Skills are defined in Workbench and Scenario Specifications
- All skills have a tenant-wide unique code
- Skills are assigned to IAM profiles (Hub-specific extensions to Cipher IAM profiles)
- Supervisors assign skills to agents
- Allocation algorithms reference skills from IAM profiles 

---

## Workload Metrics Collection

**Issue:** How agent workload and capacity metrics are collected.

**Questions:**
- Real-time or periodic collection?
- Where is agent state (availability, load) stored?
- How is capacity calculated (task count, weighted, time-based)?

**Current State:**
- Agent state structure defined
- Collection mechanism not specified

> This can left open until further revision of the documentation.
---

## ~~Request Cancellation Cascade~~ ✅ Resolved

**Clarifications:**
- All tasks are automatically cancelled when request is cancelled
- All assignees are notified
- IN_PROGRESS tasks are cancelled; any completion submitted is ignored
- No provision for agents to save work before cancellation

---

## ~~AI Agent Escalation Path~~ ✅ Resolved

**Clarifications:**
- No conceptual difference between Human Agent and AI Agent
- AI agent can escalate or abandon—up to the agent
- No AI-specific escalation path (e.g., AI → Human)
- "AI cannot complete" determination is no different from Human Agent approaches

---

## ~~Queue Configuration Lifecycle~~ ✅ Resolved

**Clarifications:**
- In-flight tasks are not affected by queue configuration changes
- No rollback mechanism
- No task migration to new configuration
- Tasks continue under the queue configuration version at task creation time

---

## Related Documentation

- [Task Management README](./README.md) — Main documentation
- [Task Lifecycle](./task-lifecycle.md) — States and transitions
- [Task Queues](./task-queues.md) — Queue configuration
- [Task Allocation](./task-allocation.md) — Allocation algorithms

---

*These open points should be resolved during detailed design phase.*

