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

Personas are organized by their **scope of operations**:

### Hub System Scope (Publisher Domain)

| Persona | Role | Document |
|---------|------|----------|
| **SRE** | Deploy, maintain, monitor the Hub platform | [sre.md](./personas/sre.md) |
| **Customer Success** | Onboard tenants, support usage | [customer-success.md](./personas/customer-success.md) |

### Tenant Subscription Scope

| Persona | Role | Document |
|---------|------|----------|
| **Administrator** | Manage subscription, resources, users | [administrator.md](./personas/administrator.md) |
| **Process Architect** | Design Scenarios, SOPs, operational structure | [process-architect.md](./personas/process-architect.md) |
| **Developer** | Build Hub Applications, define Triggers | [developer.md](./personas/developer.md) |
| **Auditor** | Review compliance, investigate decisions | [auditor.md](./personas/auditor.md) |

### Workbench Scope

| Persona | Role | Document |
|---------|------|----------|
| **Supervisor** | Deploy Scenarios, manage queues, oversee agents | [supervisor.md](./personas/supervisor.md) |
| **Agent** | Complete tasks, handle requests | [agent.md](./personas/agent.md) |

### Tenant Customer Scope

| Persona | Role | Document |
|---------|------|----------|
| **Self-Serve User** | Initiate requests, track status | [self-serve-user.md](./personas/self-serve-user.md) |

---

## Journeys

Journeys describe **cross-persona workflows** — how multiple personas collaborate to achieve an outcome.

| Journey | Personas Involved | Document |
|---------|-------------------|----------|
| **Scenario Development** | Process Architect → Developer → Supervisor | [scenario-development.md](./journeys/scenario-development.md) |
| **Workbench Configuration** | Administrator → Process Architect → Supervisor | [workbench-configuration.md](./journeys/workbench-configuration.md) |
| **Request Lifecycle** | Signal → Application → Agent → Completion | [request-lifecycle.md](./journeys/request-lifecycle.md) |
| **Audit Investigation** | Auditor (with CAF, Memory Services) | [audit-investigation.md](./journeys/audit-investigation.md) |

---

## Persona-Journey Matrix

| Journey | Admin | Proc Arch | Developer | Supervisor | Agent | Auditor |
|---------|:-----:|:---------:|:---------:|:----------:|:-----:|:-------:|
| Scenario Development | | ●● | ●● | ● | | |
| Workbench Configuration | ● | ● | | ●● | | |
| Request Lifecycle | | | | ● | ●● | |
| Audit Investigation | | | | | | ●● |

Legend: ●● Primary, ● Supporting

---

## Related Documentation

- [01-Concepts](../01-concepts/) — What is Hub?
- [04-Subsystems](../04-subsystems/) — How does Hub work?
- [10-Guides](../10-guides/) — How do I configure Hub?

---

*Status: 🟡 WIP — Persona and journey documents being developed*

