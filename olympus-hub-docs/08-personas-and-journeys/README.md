# Personas and Journeys

This section describes **who uses Olympus Hub** and **how they accomplish their objectives**. It bridges the conceptual foundation (what Hub is) with the practical guides (how to configure it).

---

## Overview

| Section | Purpose |
|---------|---------|
| **Personas** | Who are the actors in the system? What are their roles, objectives, and scope? |
| **Journeys** | How do personas collaborate to achieve outcomes? What are the key workflows? |

---

## Reading Order

1. Start with the [Personas Overview](#personas) to understand the key actors
2. Read the [Journeys](#journeys) to see how personas collaborate
3. Reference [04-Subsystems](../04-subsystems/) for technical details
4. Use [10-Guides](../10-guides/) for step-by-step configuration

---

## Personas

Personas are organized into two main categories:

- **Hub Personas** — People who use Hub as a platform (configure, operate, administer)
- **Business Domain Actors** — People/systems whose activities generate Requests

---

### Hub Personas

#### Hub System (Publisher Domain)

The Publisher (Zeta) operates the Hub platform itself.

| Persona | Role | Document |
|---------|------|----------|
| **SRE** | Deploy, maintain, monitor Hub infrastructure | [sre.md](./personas/sre.md) |
| **Customer Success** | Onboard tenants, support adoption | [customer-success.md](./personas/customer-success.md) |

#### Workbench Designers

Design and build the operational structure within Workbenches.

| Persona | Role | Document |
|---------|------|----------|
| **Automation Product Owner (APO)** | Own automation intent, business outcomes, autonomy proposals | [automation-product-owner.md](./personas/automation-product-owner.md) |
| **Process Architect** | Design Scenarios, SOPs, knowledge structure | [process-architect.md](./personas/process-architect.md) |
| **Developer** | Build Hub Applications, define Triggers | [developer.md](./personas/developer.md) |

#### Workbench Operations

Execute and oversee day-to-day operations within Workbenches.

| Persona | Role | Document |
|---------|------|----------|
| **Supervisor** | Deploy Scenarios, manage queues, oversee agents | [supervisor.md](./personas/supervisor.md) |
| **Agent** | Complete tasks, process requests | [agent.md](./personas/agent.md) |

#### Tenant Administration

Govern resources, compliance, and access across the tenant subscription.

| Persona | Role | Document |
|---------|------|----------|
| **Administrator** | Manage subscription, resources, users | [administrator.md](./personas/administrator.md) |
| **Auditor** | Review compliance, investigate decisions | [auditor.md](./personas/auditor.md) |

---

### Business Domain Actors

These are the actors whose activities **generate Requests** that Hub processes. They interact with the business, not necessarily with Hub directly.

| Actor | Can Originate | Document |
|-------|---------------|----------|
| **Business Customer** | Service Request (self-serve or assisted) | [business-customer.md](./personas/business-domain/business-customer.md) |
| **Business Employee** | Service Request (assisted), Business Request | [business-employee.md](./personas/business-domain/business-employee.md) |
| **Business System Actor** | All types (Service, Business, System) | [business-system-actor.md](./personas/business-domain/business-system-actor.md) |

> **Note:** The request type is determined by **the nature of the work**, not the originator. See [Request Types](./journeys/request-lifecycle.md#request-types) for details.

> **Note:** Business Employees may also be Agents — they can both trigger requests (as Business Actor) and process tasks (as Hub Persona). See [Persona Overlap](#persona-overlap).

---

## Persona Overlap

Some individuals wear multiple hats:

| Person | As Business Actor | As Hub Persona |
|--------|-------------------|----------------|
| **Relationship Manager** | Triggers onboarding (Business Request) | Works tasks as Agent |
| **Compliance Officer** | Requests review (Business Request) | Reviews as Supervisor/Auditor |
| **Customer** | Files dispute (Service Request) | May complete Subject tasks (Self-Serve) |

The distinction is:
- **Business Actor** = Their activity *creates* the Request
- **Hub Persona** = They *use Hub* to process Requests

---

## Journeys

Journeys describe **cross-persona workflows** — how multiple personas collaborate to achieve an outcome.

### Hub Configuration Journeys

| Journey | Personas Involved | Document |
|---------|-------------------|----------|
| **Automation Lifecycle (Conventional)** | APO → Process Architect → Developer → Supervisor → (Evolve) | [automation-lifecycle.md](./journeys/automation-lifecycle.md) |
| **Scenario Development** | Process Architect → Developer → Supervisor | [scenario-development.md](./journeys/scenario-development.md) |
| **Workbench Configuration** | Administrator → Process Architect → Supervisor | [workbench-configuration.md](./journeys/workbench-configuration.md) |

> **Note:** For agentic automation (AI agents), see the [Agentic Automation Lifecycle](../../olympus-seer-docs/seer-design/personas-and-needs/journeys/agentic-automation-lifecycle.md) in Seer documentation.

### Operations Journeys

| Journey | Personas Involved | Document |
|---------|-------------------|----------|
| **Request Lifecycle** | Business Actor → Signal → Application → Agent | [request-lifecycle.md](./journeys/request-lifecycle.md) |
| **Audit Investigation** | Auditor (with CAF, Memory Services) | [audit-investigation.md](./journeys/audit-investigation.md) |

### Evolution Journeys

| Journey | Personas Involved | Document |
|---------|-------------------|----------|
| **Production Feedback Loop** | Agent, Supervisor → APO → PA, Developer | [production-feedback-loop.md](./journeys/production-feedback-loop.md) |

---

## Persona-Journey Matrix

### Hub Personas

| Journey | Admin | APO | Proc Arch | Developer | Supervisor | Agent | Auditor |
|---------|:-----:|:---:|:---------:|:---------:|:----------:|:-----:|:-------:|
| Automation Lifecycle (Conventional) | ● | ●● | ●● | ●● | ● | | ● |
| Scenario Development | | ● | ●● | ●● | ● | | |
| Workbench Configuration | ●● | | ● | | ● | | |
| Request Lifecycle | | ● | | | ● | ●● | |
| Audit Investigation | | | | | | | ●● |
| Production Feedback Loop | | ●● | ● | ● | ●● | ● | |

### Business Domain Actors

| Journey | Customer | Employee | System Actor |
|---------|:--------:|:--------:|:------------:|
| Request Lifecycle | ●● | ●● | ●● |

Legend: ●● Primary, ● Supporting

---

## Visual Summary

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           OLYMPUS HUB ACTORS                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  HUB PERSONAS (Use Hub as Platform)                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                                                                     │    │
│  │  Hub System (Publisher)     Workbench Designers                    │    │
│  │  ├── SRE                    ├── Automation Product Owner (APO)     │    │
│  │  └── Customer Success       ├── Process Architect                  │    │
│  │                             └── Developer                          │    │
│  │                                                                     │    │
│  │  Workbench Operations       Tenant Administration                  │    │
│  │  ├── Supervisor             ├── Administrator                      │    │
│  │  └── Agent ◄────────────────┼── Auditor                           │    │
│  │            │                │                                      │    │
│  └────────────┼────────────────┼──────────────────────────────────────┘    │
│               │                │                                            │
│               │   (may overlap)│                                            │
│               ▼                ▼                                            │
│  BUSINESS DOMAIN ACTORS (Generate Requests)                                 │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                                                                     │    │
│  │  Business Customer     ──→ Service Request                         │    │
│  │  Business Employee     ──→ Service Request (assisted), Business    │    │
│  │  Business System Actor ──→ Service, Business, or System Request    │    │
│  │                                                                     │    │
│  │  (Request type = nature of work, not originator)                   │    │
│  │                                                                     │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Related Documentation

- [01-Concepts](../01-concepts/) — What is Hub?
- [04-Subsystems](../04-subsystems/) — How does Hub work?
- [10-Guides](../10-guides/) — How do I configure Hub?

---

*Status: 🟡 WIP — Persona and journey documents being developed*
