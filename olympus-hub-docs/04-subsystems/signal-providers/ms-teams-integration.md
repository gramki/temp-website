# MS Teams Integration (I/O Gateway)

> **Status:** 🔴 Stub — Reference to detailed documentation

The MS Teams Integration module functions as an **I/O Gateway** for Hub, enabling signals from MS Teams channels and relaying responses back to Teams.

---

## Overview

MS Teams Integration is **more than a signal provider** — it's a full integration module that:
- Acts as an I/O Gateway for signals
- Provides **copilot bots** for Agents, Supervisors, and Business Employees
- Manages **chat groups as collaboration surfaces** for multi-participant orchestration
- Handles **direct services** (queries that don't go through Signal Exchange)

---

## Signal Provider Role

| Aspect | Description |
|--------|-------------|
| **Signal Type** | CHAT_MESSAGE |
| **Protocol** | MS Teams Bot Framework / Graph API |
| **Sources** | Me_Bot (Agents/Supervisors), Ask_Bot (Business Employees) |
| **Underlying Infrastructure** | Heracles (HTTP/API layer) |

### How It Differs from Other Gateways

| Characteristic | Standard I/O Gateways | MS Teams Integration |
|----------------|----------------------|----------------------|
| **Primary Role** | Signal routing | Persona copilot + signal routing |
| **Collaboration** | N/A | Chat groups as orchestration surfaces |
| **Direct Services** | Minimal | KB lookups, task queries, status checks |
| **Identity** | Machine/service identity | Per-workbench bots with human interaction |

---

## Architectural Position

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         MS TEAMS INTEGRATION                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐              │
│  │   Me_Bot    │  │  Ask_Bot    │  │  Group Orchestration    │              │
│  │   (Agent    │  │  (Business  │  │  Bot (System)           │              │
│  │   Copilot)  │  │  Employee)  │  │                         │              │
│  └──────┬──────┘  └──────┬──────┘  └────────────┬────────────┘              │
│         │                │                      │                           │
│         └────────────────┴──────────────────────┘                           │
│                          │                                                   │
│                          ▼                                                   │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                    MS TEAMS INTEGRATION MODULE                       │    │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐               │    │
│  │  │ Signal       │  │ Direct       │  │ Chat Group   │               │    │
│  │  │ Routing      │  │ Services     │  │ Management   │               │    │
│  │  └──────┬───────┘  └──────────────┘  └──────────────┘               │    │
│  └─────────┼───────────────────────────────────────────────────────────┘    │
│            │                                                                 │
│            ▼                                                                 │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                        HERACLES (HTTP Layer)                         │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│            │                                                                 │
│            ▼                                                                 │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                        SIGNAL EXCHANGE                               │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Detailed Documentation

For comprehensive documentation on MS Teams Integration, see:

| Document | Description |
|----------|-------------|
| [Overview](../ms-teams-integration/README.md) | Architecture and components |
| [FAQ](../ms-teams-integration/ms-teams-integration-faq.md) | Design decisions and clarifications |

---

## Related Documentation

- [Signal Exchange](../signal-exchange/README.md) — Request routing
- [Heracles Gateway](./heracles-api-gateway.md) — Underlying HTTP infrastructure
- [UX Architecture](../../06-ux-architecture/README.md) — Channel strategy

---

*For full documentation, see the [MS Teams Integration subsystem](../ms-teams-integration/).*

