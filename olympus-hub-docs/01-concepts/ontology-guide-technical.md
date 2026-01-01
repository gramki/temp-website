# Ontology Guide: Architects & Developers

**For:** Solution Architects, Platform Engineers, Backend Developers, Integration Engineers

**Your goal:** Understand the complete conceptual model, relationships, and how to implement systems that conform to this ontology.

---

## How to Use This Guide

1. **Read the full [Introduction](./ontology-reference.md#introduction)** for the four-layer framework
2. **Study the [Class Diagram](./ontology-diagrams.md#appendix-mermaid-class-diagram-layered)** as your reference model
3. **Work through each layer systematically** for implementation details

---

## Key Concepts by Focus Area

| Focus Area | Relevant Concepts | Document |
|------------|-------------------|----------|
| **System Integration** | Machine, Sensors, Environment, Signal | [Perception Layer](./ontology-1-perception-layer.md) |
| **I/O Architecture** | Trigger, I/O Gateway Signal Types, Request types | [Perception Layer](./ontology-1-perception-layer.md) |
| **Automation Design** | Automation, Automation System, Operation | [Automation Layer](./ontology-4-automation-layer.md) |
| **Agent Framework** | Agent, Human, AI Agent, Human–AI Team | [Execution Layer](./ontology-3-execution-layer.md) |
| **Tool Development** | Tool, Prediction Application, Decision Application, Command | [Automation Layer](./ontology-4-automation-layer.md) |
| **Registry Design** | Tool Registry, Machine Registry, Workbench | [Automation Layer](./ontology-4-automation-layer.md) |
| **Data Model** | Business Entity, Data Element, Information Element | [Perception](./ontology-1-perception-layer.md) + [Normative](./ontology-2-normative-layer.md) |

---

## Implementation Notes

### Abstract Types (Require Specialization)

The following are abstract concepts that must be specialized:

| Abstract Type | Specializations | Notes |
|---------------|-----------------|-------|
| **Operation** | Procedure, Workflow, Case | Choose based on determinism and role count |
| **Tool** | Prediction Application, Decision Application, Command | Based on OPD function |
| **Agent** | Human, AI Agent | Implement different identity/capability models |
| **OPD Element** | Observe, Predict, Decide | Conceptual; not directly instantiated |

---

### Core Runtime Flow

The strict runtime lifecycle that all implementations must follow:

```
Signal → Trigger → Request → Scenario → Automation → Operation → Activity → Action
```

**No shortcuts allowed.** Every operation instance goes through this chain.

---

### Workbench as Tenant Boundary

The **Workbench** is the primary isolation boundary:

```
Tenant
├── Workbench A (Dispute Resolution)
│   ├── Scoped: Signals, Triggers, Requests, Scenarios, Operations
│   ├── Enrolled: Agents
│   ├── Whitelisted: Tools, Machines
│   └── Owned: Knowledge Base, Task Queues
│
└── Workbench B (Fraud Prevention)
    ├── Scoped: (own instances)
    └── ...
```

**Implementation requirements:**
- All entities must carry Workbench context
- Cross-workbench references are not allowed for runtime entities
- Registries (Tool, Machine) have System → Tenant → Workbench inheritance

---

### Registry Inheritance Model

```
System Registry (Platform-wide)
        │
        ▼
Tenant Registry (Inherits, Extends, Overrides)
        │
        ▼
Workbench Whitelist (Subset available in this Workbench)
```

Applies to both **Tool Registry** and **Machine Registry**.

---

### Signal Type → I/O Gateway Mapping

| I/O Gateway | Signal Type | Protocol | Implementation |
|-------------|-------------|----------|----------------|
| **Atropos** | Event | Pub-Sub | Event bus consumer |
| **Cronus** | Exception, Observation | Publisher API | REST/gRPC endpoint |
| **Heracles** | HTTP-Request | HTTP/REST/MCP | API gateway |
| **Dia** | Batch-Request | SFTP/HTTP/WebDAV | File watcher |
| **Kale** | Time-Signal | Scheduler | Cron/scheduler |

**Extensibility:** New I/O Gateways can introduce new signal types. Core flow remains stable.

---

### Task Lifecycle State Machine

```
                    ┌─────────────┐
                    │   Created   │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
              ┌─────│   Pending   │─────┐
              │     └──────┬──────┘     │
              │            │            │
         (timeout)    (assigned)    (cancelled)
              │            │            │
              ▼            ▼            ▼
       ┌───────────┐ ┌───────────┐ ┌───────────┐
       │ Escalated │ │In Progress│ │ Cancelled │
       └───────────┘ └─────┬─────┘ └───────────┘
                           │
                    ┌──────┴──────┐
                    │             │
               (completed)    (failed)
                    │             │
                    ▼             ▼
             ┌───────────┐ ┌───────────┐
             │ Completed │ │  Failed   │
             └───────────┘ └───────────┘
```

---

### Request Classification Impact

| Request Type | Subject Association | Authorization | Task Assignment |
|--------------|---------------------|---------------|-----------------|
| **Service Request** | Required (customer) | Identity or Role | Subject + Agents |
| **Business Request** | Optional | Role/Group | Agents only |
| **System Request** | Optional | Machine identity | Agents only |

**Service Request special handling:**
- Subject (customer) can receive tasks
- Customer is a special agent type
- Requires different enablement path

---

## Data Model References

### Key Entities and Relationships

```
Domain ──(1:1)──► Workbench
     │
     └──(1:N)──► Business Entity

Workbench ──(1:N)──► Scenario ──(1:1)──► Automation
                                              │
                                              ▼
                                         Operation ──(1:N)──► Activity
                                                                  │
                                                        ┌─────────┴─────────┐
                                                        │                   │
                                                   (some)               (all)
                                                        ▼                   ▼
                                                      Task              Action
                                                        │
                                                        ▼
                                                      Agent
```

---

## Layer Documents

| Layer | Content | Document |
|-------|---------|----------|
| **Perception** | Domain, Workbench, Environment, Signal, Trigger, Scenario | [ontology-1-perception-layer.md](./ontology-1-perception-layer.md) |
| **Normative** | Role, Goal, SOP, KB, Runbook, Checklist | [ontology-2-normative-layer.md](./ontology-2-normative-layer.md) |
| **Execution** | Operation, Activity, Task, Escalation, Agent | [ontology-3-execution-layer.md](./ontology-3-execution-layer.md) |
| **Automation** | Automation, Tools, Registries | [ontology-4-automation-layer.md](./ontology-4-automation-layer.md) |
| **Diagrams** | Class Diagram, Ontology Graph | [ontology-diagrams.md](./ontology-diagrams.md) |

---

## Diagrams for Implementation

- **[Class Diagram (Layered)](./ontology-diagrams.md#appendix-mermaid-class-diagram-layered)** — Reference data model with inheritance
- **[Ontology Graph](./ontology-diagrams.md#appendix-mermaid-ontology-graph)** — Relationship constraints

---

## Navigation

- [← Back to Ontology Reference](./ontology-reference.md)
- [Business Guide](./ontology-guide-business.md) — Glossary for non-technical stakeholders
- [Operations Guide](./ontology-guide-operations.md) — Configuration and operations focus

