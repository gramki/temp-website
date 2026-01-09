# Ontology Guide: Operations Engineers & Operators

**For:** Operations Engineers, Workbench Designers, Process Analysts, Operations Team Leads

**Your goal:** Understand how to configure and operate workbenches, define scenarios, and manage day-to-day operations.

---

## How to Use This Guide

1. **Review the [Business Glossary](./ontology-guide-business.md#quick-reference-glossary)** if any terms are unfamiliar
2. **Focus on sections relevant to your work** (see table below)
3. **Study the diagrams** to understand relationships

---

## Key Concepts by Focus Area

| Focus Area | Relevant Concepts | Document |
|------------|-------------------|----------|
| **Workbench Design** | Workbench, Domain, Scenario, Trigger | [Perception Layer](./ontology-1-perception-layer.md) |
| **Request & Signal Flow** | Signal, Request, Trigger, I/O Gateway Signal Types | [Perception Layer](./ontology-1-perception-layer.md) |
| **Work Execution** | Operation, Procedure, Workflow, Case | [Execution Layer](./ontology-3-execution-layer.md) |
| **Task Management** | Task, Task Queue, Escalation, Activity | [Execution Layer](./ontology-3-execution-layer.md) |
| **Agent Configuration** | Agent, Role, Capability, Capacity, Training | [Normative](./ontology-2-normative-layer.md) + [Execution](./ontology-3-execution-layer.md) |
| **Knowledge Management** | SOP, Knowledge Base, Runbook, Checklist | [Normative Layer](./ontology-2-normative-layer.md) |
| **Tool & Machine Access** | Tool Registry, Machine Registry, Command | [Automation Layer](./ontology-4-automation-layer.md) |

---

## Essential Concepts for Operations

### Workbench Design

The **Workbench** is the central organizing construct. Everything you configure belongs to a Workbench:

```
Workbench
├── Domain Model (Business Entities)
├── Environment (Machines, Sensors)
├── Scenarios (What situations to handle)
├── Triggers (How signals become requests)
├── Request Definitions (Domain-specific request types)
├── Tool Registry (Available tools)
├── Machine Registry (Accessible systems)
├── Task Queues (Work distribution)
├── Agents (Enrolled Human and AI)
└── Knowledge Base (SOPs, Runbooks, Checklists)
```

**Key principle:** All Signals, Triggers, Requests, Scenarios, and Operations are **scoped to exactly one Workbench**.

→ [Full Workbench Definition](./ontology-1-perception-layer.md#workbench)

---

### Signal → Request → Operation Flow

Understanding this flow is essential for operations design:

```
Signal (something happened)
    │
    ▼
Trigger (filter, transform, bind)
    │
    ▼
Request (standardized input)
    │
    ▼
Scenario (situational context)
    │
    ▼
Automation (recipe to follow)
    │
    ▼
Operation (runtime work instance)
    │
    ▼
Activities → Tasks → Actions
```

→ [Signal Definition](./ontology-1-perception-layer.md#signal)  
→ [Trigger Definition](./ontology-1-perception-layer.md#trigger)  
→ [Request Definition](./ontology-1-perception-layer.md#request)

---

### Task Management

Tasks are the work units assigned to agents. Key management concepts:

| Concept | Purpose |
|---------|---------|
| **Task Queue** | Where tasks wait for assignment |
| **Escalation Matrix** | How unresolved tasks escalate |
| **Assignment Strategies** | FIFO, Priority, Round-Robin, Skills-Based, Load-Balanced |

```
Task Created
     │
     ▼
Task Queue (pending)
     │
     ├── Agent picks up (pull model)
     │   or
     └── System assigns (push model)
           │
           ▼
     Agent works on Task
           │
           ├── Task Completed
           └── Threshold exceeded → Escalation
```

→ [Task Definition](./ontology-3-execution-layer.md#task)  
→ [Task Queue Definition](./ontology-3-execution-layer.md#task-queue)  
→ [Escalation Definition](./ontology-3-execution-layer.md#escalation)

---

### Agent Configuration

Agents need proper configuration before they can work:

| Configuration | Description |
|---------------|-------------|
| **Role Assignment** | What roles the agent can play |
| **Capability Profile** | What skills/certifications they have |
| **Capacity Limits** | How much work they can handle |
| **Queue Eligibility** | Which task queues they can access |
| **Training Status** | Completed training for roles |

→ [Agent Definition](./ontology-3-execution-layer.md#agent)  
→ [Role Definition](./ontology-2-normative-layer.md#role)  
→ [Capability Definition](./ontology-2-normative-layer.md#capability)

---

## Diagrams to Study

These diagrams show the full structure and relationships:

- **[Class Diagram](./ontology-diagrams.md#appendix-mermaid-class-diagram-layered)** — Shows inheritance and structure
- **[Ontology Graph](./ontology-diagrams.md#appendix-mermaid-ontology-graph)** — Shows relationships between concepts

---

## Layer Documents

| Layer | Content | Document |
|-------|---------|----------|
| **Perception** | Domain, Workbench, Environment, Signal, Trigger, Scenario | [ontology-1-perception-layer.md](./ontology-1-perception-layer.md) |
| **Normative** | Role, Goal, SOP, KB, Runbook, Checklist | [ontology-2-normative-layer.md](./ontology-2-normative-layer.md) |
| **Execution** | Operation, Activity, Task, Escalation, Agent | [ontology-3-execution-layer.md](./ontology-3-execution-layer.md) |
| **Automation** | Automation, Tools, Registries | [ontology-4-automation-layer.md](./ontology-4-automation-layer.md) |

---

## Navigation

- [← Back to Ontology Reference](./ontology-reference.md)
- [Business Guide](./ontology-guide-business.md) — Glossary and high-level overview
- [Technical Guide](./ontology-guide-technical.md) — Implementation details

