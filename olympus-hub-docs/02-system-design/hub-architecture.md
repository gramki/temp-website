# Olympus Hub — Architecture Overview

> **Everything is Ops**

---

## Executive Summary

Olympus Hub is a framework-agnostic operations management platform designed for large and medium enterprises to model, manage, and optimize business operations across any business domain through human-AI collaboration.

**Core Proposition:** Enterprises define domain-specific **Workbenches** that model business entities and operations. AI and human agents collaborate within these Workbenches to execute tasks, resolve exceptions, and drive business outcomes—regardless of underlying enterprise systems.

---

## Core Philosophy

### Everything is Ops

Olympus Hub treats all business operations as manageable, automatable, and optimizable processes. The platform is completely agnostic to specific enterprise systems (ERP, CRM, custom applications, cloud services) and instead provides a flexible framework for modeling and managing operations across any business domain.

**Key Insight:** Each business domain is viewed as a collection of **Business Entities** managed through **Operations**. Hub provides the tools to define, model, and operate on these entities—unifying human expertise and AI capabilities.

### Workbench as Core Abstraction

The **Workbench** is the fundamental organizational unit in Olympus Hub:

| Property | Description |
|----------|-------------|
| **Domain Encapsulation** | Each Workbench encapsulates a specific business domain (e.g., Payments, Order Processing, HR Operations) |
| **System Agnostic** | Independent of underlying systems—connects to any enterprise application |
| **Entity-Centric** | Models the domain as a collection of Business Entities |
| **Action-Oriented** | Defines actions possible on those entities |
| **Agent-Enabled** | Provides the operational interface for human and AI agents |

→ **Details:** [Workbench Anatomy](./workbench-anatomy.md)

---

## System Model

### Signal-Driven Operations

All operations in Hub begin with **Signals**—inputs from the environment that indicate something requiring attention:

```
Signal → I/O Gateway → Signal Exchange → Hub Application → Task → Agent
```

| Component | Role |
|-----------|------|
| **Signal** | Input indicating change or event (Event, Exception, Observation, Request) |
| **I/O Gateway** | Senses signals from specific protocols (HTTP, events, files, schedules) |
| **Signal Exchange** | Central routing engine that matches signals to triggers |
| **Hub Application** | Automation artifact that processes the request |
| **Task** | Unit of work assigned to an agent |
| **Agent** | Human or AI executor who completes the work |

→ **Details:** [Signal Flow](./signal-flow.md)

### Scenarios and Operations

When a signal matches a **Trigger**, it creates a **Request** that activates a **Scenario**. The Scenario determines:
- Which **Roles** are involved
- Which **Automations** execute
- What **Goals** must be achieved
- Which **SOPs** govern the response

→ **Details:** [Architecture Layers](./architecture-layers.md) | [Scenario Specification Types](./implementation-concepts/scenario-specification-types.md)

### Agent Collaboration

Hub enables human and AI agents to work together:

| Agent Type | Interaction Mode |
|------------|------------------|
| **Human Agents** | Task queues, direct assignment, consoles |
| **AI Agents** | Task delegation, event subscription, tool execution |
| **Mixed Teams** | Escalation, handoff, collaborative resolution |

→ **Details:** [Agent Model](./agent-model.md)

---

## Architectural Principles

| Principle | Description |
|-----------|-------------|
| **Framework Agnostic** | No dependency on specific enterprise systems |
| **Domain-Centric** | Workbenches encapsulate complete business domains |
| **Entity-Driven** | Operations centered on business entity lifecycle |
| **Modular** | Workbenches operate independently with clear interfaces |
| **Scalable** | Horizontal scaling for high-volume operations |
| **Secure** | Enterprise-grade security and multi-tenancy |
| **Observable** | Comprehensive monitoring across all components |
| **Resilient** | Fault tolerance and disaster recovery built-in |

---

## System Topology

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              OLYMPUS HUB                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐                 │
│   │  Workbench   │    │  Workbench   │    │  Workbench   │                 │
│   │  (Payments)  │    │  (Orders)    │    │    (HR)      │                 │
│   └──────┬───────┘    └──────┬───────┘    └──────┬───────┘                 │
│          │                   │                   │                          │
│          └───────────────────┼───────────────────┘                          │
│                              │                                               │
│                              ▼                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                       SIGNAL EXCHANGE                                 │   │
│   │              (Central routing and orchestration)                     │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                               │
│          ┌───────────────────┼───────────────────┐                          │
│          │                   │                   │                          │
│          ▼                   ▼                   ▼                          │
│   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐                 │
│   │  I/O Gateway │    │  I/O Gateway │    │  I/O Gateway │                 │
│   │  (Heracles)  │    │  (Atropos)   │    │    (Dia)     │                 │
│   │   HTTP/API   │    │    Events    │    │    Files     │                 │
│   └──────────────┘    └──────────────┘    └──────────────┘                 │
│                                                                              │
├─────────────────────────────────────────────────────────────────────────────┤
│   SUPPORTING SUBSYSTEMS                                                      │
│                                                                              │
│   ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐              │
│   │ Workbench  │ │ Operations │ │  Command   │ │ Automation │              │
│   │   Studio   │ │   Center   │ │  Registry  │ │  Runtimes  │              │
│   └────────────┘ └────────────┘ └────────────┘ └────────────┘              │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

→ **Details:** [Subsystem Map](./subsystem-map.md)

---

## Key Subsystems

| Subsystem | Purpose |
|-----------|---------|
| **Workbench Studio** | Design-time environment for defining Workbenches, entities, scenarios |
| **Operations Center** | Runtime environment hosting Workbenches, consoles, agent interfaces |
| **Signal Exchange** | Central routing engine matching signals to applications |
| **I/O Gateways** | Protocol-specific signal ingress/egress (Heracles, Atropos, Cronus, Dia, Kale) |
| **Command Registry** | Available commands (levers) that can be executed on entities |
| **Automation Runtimes** | Execution hosts for Hub Applications (Atlantis, Perseus, Rhea, ChronoShift) |

→ **Details:** [Subsystem Map](./subsystem-map.md) | [Subsystems Section](../04-subsystems/)

---

## Multi-Tenancy Model

Hub supports enterprise multi-tenancy with clear isolation boundaries:

```
Tenant (Enterprise)
  └── Subscription (Resource/Billing Boundary)
        └── Workbench (Domain Operational Environment)
              └── Hub Applications, Scenarios, Tasks
```

→ **Details:** [Tenant](./implementation-concepts/tenant.md) | [Subscription](./implementation-concepts/subscription.md) | [Deployment View](./views/deployment-view.md)

---

## Security Model

| Layer | Mechanism |
|-------|-----------|
| **Human IAM** | SSO integration (SAML/OIDC), RBAC scoped to Workbenches |
| **AI Agent IAM** | SPIFFE-based identity, fine-grained entity/action permissions |
| **Tool Authorization** | OAuth-like consent for agent tool access |
| **Cross-Agent** | Delegation, impersonation with explicit consent, scope limiting |
| **Audit** | Complete audit trail via Cognitive Audit Fabric |

→ **Details:** [Security View](./views/security-view.md) | [Cognitive Audit Fabric](./implementation-concepts/cognitive-audit-fabric.md)

---

## Document Map

This architecture overview connects to detailed documentation:

| Topic | Documents |
|-------|-----------|
| **How layers map** | [Architecture Layers](./architecture-layers.md) |
| **How signals flow** | [Signal Flow](./signal-flow.md) |
| **What's in a Workbench** | [Workbench Anatomy](./workbench-anatomy.md) |
| **How agents work** | [Agent Model](./agent-model.md) |
| **Subsystem boundaries** | [Subsystem Map](./subsystem-map.md) |
| **All concepts** | [Implementation Concepts](./implementation-concepts/README.md) |
| **All views** | [Architecture Views](./views/README.md) |

---

## Related Documentation

- [Ontology Reference](../01-concepts/ontology-reference.md) — Theoretical foundation
- [Personas](../06-personas/) — Who uses Hub
- [Subsystems](../04-subsystems/) — Technical details
- [Guides](../10-guides/) — Practical how-tos
