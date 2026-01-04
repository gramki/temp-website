# MS Teams Integration

> **Status:** 🟡 WIP — Architecture and FAQ documented, detailed specs pending

MS Teams Integration is a dedicated subsystem that brings Hub capabilities into Microsoft Teams, enabling Agents, Supervisors, and Business Employees to work within their natural collaboration environment.

---

## Design Philosophy

### Bots as Copilots

The core objective is to make bots **copilots** of the personas they serve:

| Persona | Copilot | Purpose |
|---------|---------|---------|
| **Agents** | Me_Bot | Full Agent Desk capabilities via Teams |
| **Supervisors** | Me_Bot | Same as agents, plus queue metrics and oversight |
| **Business Employees** | Ask_Bot | Request initiation and assigned task handling |

**Why Copilots?**
- Users already work in MS Teams
- Reduce context switching to Hub UIs
- Each persona gets assistance tuned to their needs and permissions
- Natural, conversational interaction (evolving toward GenAI-based)

### Chat Groups as Collaboration Surfaces

When orchestration is required between multiple participants:

| Aspect | Approach |
|--------|----------|
| **One group per request** | All collaboration about a request in one place |
| **Bot as orchestrator** | Group Orchestration Bot manages membership and relays updates |
| **Dynamic membership** | Assignees join automatically as tasks are created |
| **Persistent history** | All messages become Request updates for audit |

**Why Chat Groups?**
- Complex requests involve handoffs between agents
- Agents need to coordinate, share context, ask questions
- Traditional task assignment doesn't capture human interaction
- Supervisors need visibility into team collaboration

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          MS TEAMS INTEGRATION                                │
│                                                                              │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                        BOT LAYER (Per Workbench)                       │  │
│  │                                                                        │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐        │  │
│  │  │   Me_Bot    │  │  Ask_Bot    │  │  Group Orchestration    │        │  │
│  │  │   (Agent    │  │  (Business  │  │  Bot (System)           │        │  │
│  │  │   Copilot)  │  │  Employee)  │  │                         │        │  │
│  │  └──────┬──────┘  └──────┬──────┘  └────────────┬────────────┘        │  │
│  │         │                │                      │                      │  │
│  └─────────┴────────────────┴──────────────────────┴──────────────────────┘  │
│                             │                                                │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                      INTEGRATION MODULE                                │  │
│  │                                                                        │  │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                 │  │
│  │  │ Message      │  │ Direct       │  │ Chat Group   │                 │  │
│  │  │ Classification│ │ Services     │  │ Lifecycle    │                 │  │
│  │  │ (NLP/Struct) │  │ (KB, Tasks)  │  │ Management   │                 │  │
│  │  └──────┬───────┘  └──────────────┘  └──────────────┘                 │  │
│  │         │                                                              │  │
│  └─────────┼──────────────────────────────────────────────────────────────┘  │
│            │                                                                 │
│            ▼                                                                 │
│  ┌─────────────────────┐              ┌─────────────────────┐               │
│  │ SIGNAL EXCHANGE     │              │ HUB SERVICES        │               │
│  │ (Triggers, Requests)│              │ (KB, Memory, Tasks) │               │
│  └─────────────────────┘              └─────────────────────┘               │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Bot Types

### Me_Bot (Agent/Supervisor Copilot)

| Capability | Agent | Supervisor |
|------------|-------|------------|
| View assigned tasks | ✅ | ✅ All + Queue |
| Complete/Escalate/Reassign tasks | ✅ | ✅ |
| Query knowledge base | ✅ | ✅ |
| Record decisions and thoughts | ✅ | ✅ |
| View signals | ✅ | ✅ |
| Routines & checklists | ✅ | ✅ |
| Initiate requests | ✅ | ✅ |
| Queue metrics | ❌ | ✅ |
| Cross-agent reassignment | ❌ | ✅ |
| Escalation handling | ❌ | ✅ |

**Task Solver Rendering:**
- If Adaptive Card compatible → Render in Teams
- Otherwise → Launch via Hercules Launcher

### Ask_Bot (Business Employee Copilot)

| Capability | Supported |
|------------|-----------|
| Initiate requests (free-form or structured) | ✅ |
| View explicitly assigned tasks | ✅ |
| Complete assigned tasks | ✅ |
| Query knowledge base | ✅ |
| See agent-queue tasks | ❌ |

### Group Orchestration Bot (System)

| Responsibility | Description |
|----------------|-------------|
| Chat group lifecycle | Create groups, add members (via Graph API), archive |
| System updates | Post updates not from individual participants |
| Group representation | Orchestrates collaboration between agents on a request |

> **Note:** The Group Orchestration Bot is a construct of the MS Teams integration module. Signal Exchange itself is unaware of this bot.

---

## Message Flow

### Signal Path (Request Initiation)

```
Business Employee           Ask_Bot                MS Teams Module            Signal Exchange
      │                        │                         │                          │
      │ ──── Message ────────> │                         │                          │
      │                        │ ─── Classify ─────────> │                          │
      │                        │                         │ ─── Signal ────────────> │
      │                        │                         │                          │ Evaluate
      │                        │                         │                          │ Triggers
      │                        │                         │ <── Create Request ───── │
      │ <── Confirmation ───── │ <── Response ────────── │                          │
      │                        │                         │                          │
```

### Direct Services Path (No Signal Exchange)

```
Agent/Employee              Me_Bot/Ask_Bot          MS Teams Module            Hub Services
      │                        │                         │                          │
      │ ──── Query ──────────> │                         │                          │
      │                        │ ─── Query ────────────> │                          │
      │                        │                         │ ─── Direct Call ───────> │
      │                        │                         │ <── Response ─────────── │
      │ <── Response ───────── │ <── Response ────────── │                          │
      │                        │                         │                          │
```

---

## Documents

| Document | Description | Status |
|----------|-------------|--------|
| [Bot Architecture](./bot-architecture.md) | Me_Bot, Ask_Bot, Signal Exchange Bot | 🟡 WIP |
| [Chat Group Lifecycle](./chat-group-lifecycle.md) | Request → Group mapping, membership, archival | 🟡 WIP |
| [Message Flow](./message-flow.md) | Signal routing, direct services, responses | 🟡 WIP |
| [FAQ](./ms-teams-integration-faq.md) | Design decisions and Q&A | 🟡 WIP |

---

## Scope & Limitations

### In Scope
- Business Employees
- Agents
- Supervisors

### Out of Scope (Current)
- Business Customers (potential future: Subject_Bot)

---

## Related Documentation

- [Signal Providers](../signal-providers/) — I/O Gateway context
- [Signal Exchange](../signal-exchange/) — Request routing
- [UX Architecture](../../06-ux-architecture/) — Channel strategy
- [User Management](../user-management/) — Persona definitions

---

*Last updated: 2026-01-05*

