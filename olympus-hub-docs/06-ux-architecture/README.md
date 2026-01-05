# UX Architecture

This section covers the user experience architecture for Olympus Hub — the applications, channels, and interaction patterns that enable humans and AI to interact with Hub operations.

---

## Design Philosophy

### Meta Approach: (Persona, Channel, Use Case)

Hub's UX architecture is built on three organizing principles:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         UX ARCHITECTURE PRINCIPLES                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. PERSONA-FOCUSED                                                         │
│     • Each persona has dedicated applications optimized for their work      │
│     • Common capabilities shared, specialized views per role                │
│                                                                              │
│  2. CHANNEL-AGNOSTIC                                                        │
│     • Headless access services provide core functionality                   │
│     • Channel adapters render for specific platforms                        │
│     • Same capabilities, multiple delivery mechanisms                       │
│                                                                              │
│  3. USE-CASE DRIVEN                                                         │
│     • Interfaces organized by what users need to accomplish                 │
│     • Workflows, not just screens                                           │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### First-Class Channels

Hub treats these as first-class interaction channels:

| Category | Channels | Details |
|----------|----------|---------|
| **Traditional** | Web, Mobile, Email | Standard web/mobile apps |
| **Collaboration** | [MS Teams](../04-subsystems/ms-teams-integration/README.md), Slack | Agent/Employee copilots, chat groups |
| **AI Assistants** | ChatGPT, Claude, Gemini | Via [MCP Channels](./tenant-domain/mcp-channels.md) |
| **Customer-Facing** | [Neutrino](./frameworks-and-integrations/neutrino-integration.md) | Web Portal, Mobile App, IVR, Chat |

### Architecture Pattern

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│                           CHANNEL ADAPTERS                                   │
│     ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐        │
│     │   Web   │  │ Mobile  │  │ MS Teams│  │  Email  │  │   AI    │        │
│     └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘        │
│          │            │            │            │            │              │
│          └────────────┴─────┬──────┴────────────┴────────────┘              │
│                             │                                                │
│                             ▼                                                │
│     ┌─────────────────────────────────────────────────────────────────┐     │
│     │              HEADLESS ACCESS SERVICES                            │     │
│     │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐           │     │
│     │  │  MCP Gateway │  │  REST APIs   │  │  GraphQL     │           │     │
│     │  └──────────────┘  └──────────────┘  └──────────────┘           │     │
│     └─────────────────────────────────────────────────────────────────┘     │
│                             │                                                │
│                             ▼                                                │
│     ┌─────────────────────────────────────────────────────────────────┐     │
│     │                    HUB SERVICES                                  │     │
│     └─────────────────────────────────────────────────────────────────┘     │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Applications by Persona

### Hub System (Publisher Domain)

| Application | Persona | Purpose |
|-------------|---------|---------|
| **[Hub SRE Operations Center](./publisher-domain/hub-sre-ops-center.md)** | SRE | Monitor, maintain, and operate Hub infrastructure |
| **[Hub Win Operations Center](./publisher-domain/hub-win-ops-center.md)** | Customer Success | Onboard tenants, support adoption, review usage |

### Tenant Administration

| Application | Persona | Purpose |
|-------------|---------|---------|
| **[Hub Control Center](./tenant-domain/hub-control-center.md)** | Administrator | Configure subscription, resources, users, machines |

### Workbench Designers

| Application | Persona | Purpose |
|-------------|---------|---------|
| **[Hub Workbench Studio](./tenant-domain/workbench-studio.md)** | Process Architect, Developer | Design scenarios, build applications, manage knowledge |
| **[Steward Desk](./tenant-domain/steward-desk.md)** | Process Architect, Developer | Runtime monitoring, incident triage, production support |

### Workbench Operations

| Application | Persona | Purpose |
|-------------|---------|---------|
| **[Hub Home](./tenant-domain/hub-home.md)** | Agent, Supervisor | Landing page with workbenches, tasks, alerts |
| **[Agent Desk](./tenant-domain/agent-desk.md)** | Agent | Complete tasks, investigate, decide |
| **[Supervisor Desk](./tenant-domain/supervisor-desk.md)** | Supervisor | Monitor queues, manage agents, handle escalations |

### Business Domain Actors

| Application | Persona | Purpose |
|-------------|---------|---------|
| **[Neutrino Channels](./frameworks-and-integrations/neutrino-integration.md)** | Business Customer | Self-serve, track requests, complete subject tasks |
| **[MS Teams Integration](../04-subsystems/ms-teams-integration/README.md)** | Business Employee, Agent, Supervisor | Request initiation, task management, collaboration |

---

## Application Architecture

### Hub Control Center (Tenant Admins)

The administrative console for managing the tenant subscription.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          HUB CONTROL CENTER                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  SUBSYSTEMS CONFIGURATION           │  TENANT ECOSYSTEM SETUP               │
│  ├── Task Management System         │  ├── User & Access Management         │
│  ├── API Gateway (Heracles)         │  ├── Machine Registry Management      │
│  ├── Event Bus (Atropos)            │  ├── Tool Registry Management         │
│  ├── File Gateway (Dia)             │  ├── Workbench Management             │
│  ├── Automation Engines             │  └── Environments Management          │
│  └── Notification Services          │                                       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

See [Hub Control Center](./tenant-domain/hub-control-center.md) for details.

---

### Workbench Studio (Designers)

The design and development environment for Process Architects and Developers.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          WORKBENCH STUDIO                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  DESIGN                              │  DEVELOPMENT                          │
│  ├── Scenario Builder                │  ├── Automation Builder               │
│  │   (Signal→Trigger→Scenario)       │  │   (Hub Application Development)    │
│  ├── Knowledge Base Manager          │  ├── Automation Publisher             │
│  │   (SOPs, Reference Manuals)       │  └── Tool Registry (Workbench scope)  │
│  └── Memory Configuration            │                                       │
│                                      │                                       │
│  UI BUILDING                         │                                       │
│  ├── Angelos Page Builder            │                                       │
│  │   (Custom Console Building)       │                                       │
│  ├── Angelos Components & Binders    │                                       │
│  │   (Event wiring between components)                                       │
│  └── Angelos Action Repository       │                                       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

See [Workbench Studio](./tenant-domain/workbench-studio.md) for details.

---

### Hub Home (Landing Page)

The central landing page for Agents and Supervisors.

| Feature | Description |
|---------|-------------|
| **Workbench List** | All workbenches the user has access to |
| **My Tasks** | Tasks assigned across all workbenches |
| **Quick Actions** | Shortcuts to common tasks |
| **Alerts & Notifications** | Real-time updates requiring attention |
| **Recent Activity** | Recently accessed requests, tasks |

See [Hub Home](./tenant-domain/hub-home.md) for details.

---

### Agent Desk

The operational interface for Agents to complete tasks.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            AGENT DESK                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  CONSOLES                                                                    │
│  ├── Utility Consoles (shared with Supervisor)                              │
│  │   ├── Tasks Console                                                      │
│  │   ├── Files Console                                                      │
│  │   ├── Reports Console                                                    │
│  │   ├── Knowledge Base Console                                             │
│  │   ├── Signals Console (Exceptions, Observations)                         │
│  │   └── Routines & Checklists Console                                      │
│  │                                                                          │
│  └── Custom Consoles (workbench-specific)                                   │
│                                                                              │
│  TASK SOLVER INTERFACE                                                       │
│  ├── Custom per task type                                                   │
│  ├── Defined by Workbench Developer                                         │
│  ├── Read-only view (investigation)                                         │
│  └── Solver view (action/decision)                                          │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

See [Agent Desk](./tenant-domain/agent-desk.md) for details.

---

### Supervisor Desk

The management interface for Supervisors to oversee operations.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          SUPERVISOR DESK                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  UTILITY CONSOLES (shared with Agent)                                       │
│  ├── Tasks, Files, Reports, Knowledge Base                                  │
│  ├── Signals, Routines & Checklists                                         │
│                                                                              │
│  SUPERVISOR-ONLY CONSOLES                                                   │
│  ├── Analytics Console                                                      │
│  │   (Queue metrics, SLA tracking, throughput)                              │
│  ├── Task Allocation Management                                             │
│  │   (Queue configuration, escalation policies)                             │
│  └── Agents & Access Management                                             │
│      (Agent enrollment, capabilities, availability)                         │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

See [Supervisor Desk](./tenant-domain/supervisor-desk.md) for details.

---

## MCP Gateway Architecture

Hub exposes Model Context Protocol (MCP) gateways for AI agent integration.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         MCP GATEWAY ARCHITECTURE                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  CONTROL PLANE GATEWAYS              │  DATA PLANE GATEWAY                   │
│  ┌────────────────────────────┐      │  ┌────────────────────────────┐      │
│  │ Tenant Admin MCP Gateway   │      │  │ Scenario MCP Gateway       │      │
│  │ (Subscription management)  │      │  │ (Request initiation)       │      │
│  └────────────────────────────┘      │  │                            │      │
│  ┌────────────────────────────┐      │  │ • Service Request          │      │
│  │ Creator MCP Gateway        │      │  │ • Business Request         │      │
│  │ (Workbench design)         │      │  │ • System Request           │      │
│  └────────────────────────────┘      │  └────────────────────────────┘      │
│  ┌────────────────────────────┐      │                                       │
│  │ Agent MCP Gateway          │      │                                       │
│  │ (Task processing)          │      │                                       │
│  └────────────────────────────┘      │                                       │
│  ┌────────────────────────────┐      │                                       │
│  │ Supervisor MCP Gateway     │      │                                       │
│  │ (Operations management)    │      │                                       │
│  └────────────────────────────┘      │                                       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

See [MCP Channels](./tenant-domain/mcp-channels.md) for details.

---

## UI Framework Components

### Angelos — UI Component Framework

Angelos provides reusable UI components for building operational interfaces:

| Component Category | Examples |
|-------------------|----------|
| **Task Components** | Task forms, wizards, decision panels |
| **Entity Components** | Request detail views, entity timelines |
| **Notification Components** | Alert banners, toast notifications |
| **Action Components** | CTA buttons, action menus |
| **Data Components** | Tables, charts, dashboards |

Key capabilities:
- **Page Builder** — Visual tool for composing custom consoles
- **Component Binders** — Event wiring between components
- **Action Repository** — Reusable action definitions

See [Angelos Framework](./frameworks-and-integrations/angelos-framework.md) for details.

### Hercules Framework & Launcher

**Hercules** is a framework for web application development and hosting. **Hercules Launcher** is scaffolding that converts any HTML5 component into a launchable web app with a URL.

Hercules Launcher provides deep-linking into Hub applications via Launch URLs:

| Capability | Description |
|------------|-------------|
| **Bearer URLs** | Pre-authenticated access (like "anyone with link") |
| **Subject Binding** | URLs scoped to specific subject |
| **Tenant Scoping** | Bound to web stack subscription |
| **CTA Generation** | Dynamic links in notifications and emails |

See [Hercules Launcher](./frameworks-and-integrations/hercules-launcher.md) for details.

---

## Documents

| Document | Description | Status |
|----------|-------------|--------|
| [Hub Control Center](./tenant-domain/hub-control-center.md) | Tenant admin console | 🔴 Stub |
| [Hub SRE Operations Center](./publisher-domain/hub-sre-ops-center.md) | Infrastructure operations for SRE | 🔴 Stub |
| [Hub Win Operations Center](./publisher-domain/hub-win-ops-center.md) | Customer Success operations | 🔴 Stub |
| [Hub Workbench Studio](./tenant-domain/workbench-studio.md) | Designer environment | 🔴 Stub |
| [Hub Home](./tenant-domain/hub-home.md) | Landing page | 🔴 Stub |
| [Agent Desk](./tenant-domain/agent-desk.md) | Agent operations console | 🔴 Stub |
| [Supervisor Desk](./tenant-domain/supervisor-desk.md) | Supervisor management console | 🔴 Stub |
| [Steward Desk](./tenant-domain/steward-desk.md) | Workbench admin console | 🔴 Stub |
| [MCP Channels](./tenant-domain/mcp-channels.md) | MCP architecture | 🔴 Stub |
| [Angelos Framework](./frameworks-and-integrations/angelos-framework.md) | UI component framework | 🔴 Stub |
| [Hercules Launcher](./frameworks-and-integrations/hercules-launcher.md) | Launch URL service | 🔴 Stub |
| [Neutrino Integration](./frameworks-and-integrations/neutrino-integration.md) | Customer channel integration | 🔴 Stub |
| [User Interaction Channels](./frameworks-and-integrations/user-interaction-channels.md) | Subject interaction patterns | ⚠️ Notes |
| [MS Teams Integration](../04-subsystems/ms-teams-integration/README.md) | MS Teams channel for Agents/Employees | 🟡 WIP |

> **Note:** Reports are powered by [Hub Analytics](../04-subsystems/hub-analytics/README.md), which integrates with [Olympus LakeStack](../05-infrastructure/olympus-lakestack.md) for report building, publishing, and dispatching. Reports appear in the Reports Console of Agent Desk, Supervisor Desk, and Steward Desk.

---

## Related Documentation

- [Personas and Journeys](../08-personas-and-journeys/) — Who uses Hub and how
- [Heracles Gateway](../05-infrastructure/heracles-gateway.md) — API gateway infrastructure
- [MCP Router](../05-infrastructure/mcp-router.md) — MCP infrastructure
- [MS Teams Integration](../04-subsystems/ms-teams-integration/README.md) — Collaboration channel
- [Hub Analytics](../04-subsystems/hub-analytics/README.md) — Operational analytics and Report Center integration
- [Olympus LakeStack](../05-infrastructure/olympus-lakestack.md) — Analytics platform

---

*Status: 🟡 WIP — Architecture defined, application documents in progress*
