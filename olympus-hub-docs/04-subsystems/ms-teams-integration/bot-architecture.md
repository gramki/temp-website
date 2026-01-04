# Bot Architecture

> **Status:** 🟡 WIP

This document details the bot types, their capabilities, and architectural decisions for MS Teams Integration.

---

## Design Principles

### Bots as Persona Copilots

Each bot serves as a **dedicated copilot** for its target persona:

| Principle | Rationale |
|-----------|-----------|
| **Meet users where they work** | Agents and Business Employees already spend time in MS Teams |
| **Reduce context switching** | Bring Hub capabilities to Teams rather than forcing navigation to Hub UIs |
| **Persona-tuned assistance** | Each bot is tailored to its persona's needs and permissions |
| **Conversational evolution** | Start structured, evolve toward GenAI-based natural interaction |

### One Bot of Each Kind per Workbench

```
┌─────────────────────────────────────────────────────────────────┐
│                      TENANT SUBSCRIPTION                         │
│                                                                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │              WORKBENCH: Dispute Operations                 │  │
│  │                                                            │  │
│  │   ┌─────────────────┐  ┌─────────────────┐  ┌───────────┐ │  │
│  │   │ dispute-ops-me  │  │ dispute-ops-ask │  │ dispute-  │ │  │
│  │   │   (Me_Bot)      │  │   (Ask_Bot)     │  │ ops-hub   │ │  │
│  │   │                 │  │                 │  │(Group Bot)│ │  │
│  │   └─────────────────┘  └─────────────────┘  └───────────┘ │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │              WORKBENCH: Fraud Investigation                │  │
│  │                                                            │  │
│  │   ┌─────────────────┐  ┌─────────────────┐  ┌───────────┐ │  │
│  │   │ fraud-inv-me    │  │ fraud-inv-ask   │  │ fraud-    │ │  │
│  │   │   (Me_Bot)      │  │   (Ask_Bot)     │  │ inv-hub   │ │  │
│  │   │                 │  │                 │  │(Group Bot)│ │  │
│  │   └─────────────────┘  └─────────────────┘  └───────────┘ │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Key Decisions:**
- Bot names must be **unique across workbenches**
- Process Architects choose bot names (suggested: include workbench identifier)
- A user can interact with bots from **multiple workbenches**

---

## Bot Types

### 1. Me_Bot (Agent/Supervisor Copilot)

**Purpose:** Personal copilot for Agents and Supervisors working on Hub tasks.

#### Conceptual Names
- Codename: `Me_Bot`
- Example instance: `dispute-ops-me-bot`, `fraud-inv-agent`

#### Target Personas

| Persona | Access Level |
|---------|--------------|
| **Agent** | Own tasks, KB, decisions |
| **Supervisor** | All agent access + queue oversight, cross-agent operations |

#### Capabilities

An Agent should be able to do via Me_Bot **everything they can do on Agent Desk**:

| Capability | Agent | Supervisor | Notes |
|------------|-------|------------|-------|
| View assigned tasks | ✅ Own | ✅ All + Queue | Supervisor sees full queue |
| Pick tasks from queue | ✅ | ✅ | |
| Complete tasks | ✅ | ✅ | Via Adaptive Card or Hercules Launcher |
| Escalate tasks | ✅ | ✅ | |
| Reassign tasks | ✅ Own | ✅ Cross-agent | Agent can reassign own; Supervisor can reassign any |
| Reject tasks | ✅ | ✅ | Returns to allocation queue |
| Query knowledge base | ✅ | ✅ | SOPs, policies, reference materials |
| View signals | ✅ | ✅ | Exceptions, observations |
| Routines & checklists | ✅ | ✅ | View and complete |
| Record decisions | ✅ | ✅ | CAF-compliant |
| Record thoughts/memos | ✅ | ✅ | Request updates |
| Access files | ✅ | ✅ | Related to requests and entities |
| Initiate requests | ✅ | ✅ | Trigger scenarios explicitly |
| View agents & roles | ✅ | ✅ | Who is working on what |
| Queue metrics | ❌ | ✅ | |
| Escalation handling | ❌ | ✅ | |
| **Direct tool invocation** | ❌ | ❌ | Must use Consoles/Applications |

> **Principle:** Me_Bot provides Agent Desk capabilities via the Teams channel.

#### Task Solver Rendering

```
┌─────────────────────────────────────────────────────────────────┐
│                     TASK SOLVER RENDERING                        │
│                                                                  │
│   Task Assigned                                                  │
│        │                                                         │
│        ▼                                                         │
│   ┌─────────────────────────────────────────┐                   │
│   │ Developer registered Adaptive Card?     │                   │
│   └────────────────┬────────────────────────┘                   │
│                    │                                             │
│          ┌─────────┴─────────┐                                  │
│          │ Yes               │ No                               │
│          ▼                   ▼                                  │
│   ┌─────────────┐     ┌─────────────────┐                       │
│   │ Render in   │     │ Show Hercules   │                       │
│   │ MS Teams    │     │ Launcher Link   │                       │
│   │ (Adaptive   │     │ (opens web-     │                       │
│   │  Card)      │     │  based solver)  │                       │
│   └─────────────┘     └─────────────────┘                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Developer Configuration:**
- Developer explicitly registers a task-solver component for MS Teams
- No automatic detection or size limits
- Fallback to Hercules Launcher is automatic when not configured

---

### 2. Ask_Bot (Business Employee Copilot)

**Purpose:** Copilot for Business Employees to initiate requests and handle assigned tasks.

#### Conceptual Names
- Codename: `Ask_Bot`
- Example instance: `dispute-ops-ask-bot`, `fraud-inv-assist`

#### Target Persona
- **Business Employees** (not Agents, not Customers)

#### Capabilities

| Capability | Supported | Notes |
|------------|-----------|-------|
| Initiate requests | ✅ | Free-form or structured messages |
| View explicitly assigned tasks | ✅ | Only tasks assigned directly to them |
| Complete assigned tasks | ✅ | |
| Query knowledge base | ✅ | |
| View agent-queue tasks | ❌ | Not part of agent allocation |
| View request status | ✅ | For requests they initiated or are involved in |

#### Request Initiation Flow

```
Business Employee                  Ask_Bot                    MS Teams Module
       │                              │                              │
       │ ── "I need to dispute ────── │                              │
       │     transaction #12345"      │                              │
       │                              │ ─── Classify Message ──────> │
       │                              │                              │
       │                              │     [NLP + Structured]       │
       │                              │                              │
       │                              │ <── Matched Trigger ──────── │
       │                              │     "Dispute Scenario"       │
       │                              │                              │
       │ <── "I've created dispute ── │                              │
       │      case #DSP-2024-0042.    │                              │
       │      You'll receive updates  │                              │
       │      in the case chat."      │                              │
       │                              │                              │
```

**Key Distinction from Me_Bot:**
- Ask_Bot users are **not** Hub Agents
- They don't see agent queue or allocation
- They can only work on tasks **explicitly assigned to them** (as subject or direct assignment)

---

### 3. Group Orchestration Bot (System)

**Purpose:** System bot that orchestrates chat groups and relays system updates for requests.

#### Conceptual Names
- Codename: `Group Orchestration Bot`, `Group_Bot`
- Example instance: `dispute-ops-hub`, `fraud-inv-hub`

#### Why This Name?

The bot orchestrates collaboration between agents working on a request. Signal Exchange itself is **unaware of this bot** — it's a construct of the MS Teams integration module. The name signifies its role in group orchestration, not its relationship to Signal Exchange.

#### Role

| Responsibility | Description |
|----------------|-------------|
| **Chat group lifecycle** | Create groups for requests, add members via Graph API, archive on schedule |
| **System update relay** | Post updates not originated by any human participant |
| **Group orchestration** | Manage collaboration between agents on a request |

#### What It Does NOT Do

| Not Responsible For | Why |
|--------------------|-----|
| Respond to queries | That's Me_Bot or Ask_Bot's job |
| Facilitate @mentions | Users @mention each other directly |
| Interactive conversation | It's a system presence, not a copilot |

#### Relationship to Signal Exchange

```
┌─────────────────────────────────────────────────────────────────┐
│                         HUB BACKEND                              │
│                                                                  │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │                    SIGNAL EXCHANGE                       │   │
│   │                                                          │   │
│   │  • Dispatches request updates to observers (not agents)  │   │
│   │  • Unaware of MS Teams or bot construct                  │   │
│   │  • Treats MS Teams as just another channel               │   │
│   │                                                          │   │
│   └─────────────────────────┬───────────────────────────────┘   │
│                             │                                    │
│                             ▼                                    │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │               MS TEAMS INTEGRATION MODULE                │   │
│   │                                                          │   │
│   │  • Subscribes to request updates for Teams-enabled       │   │
│   │    scenarios                                             │   │
│   │  • Translates updates to Teams messages                  │   │
│   │  • Uses Group Orchestration Bot as the posting identity  │   │
│   │                                                          │   │
│   └─────────────────────────┬───────────────────────────────┘   │
│                             │                                    │
└─────────────────────────────┼────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                       MS TEAMS                                   │
│                                                                  │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │              REQUEST CHAT GROUP                          │   │
│   │                                                          │   │
│   │   [Dispute Ops Hub]: Request #DSP-2024-0042 created      │   │
│   │   [Agent Alice]: I'm reviewing the transaction...        │   │
│   │   [Dispute Ops Hub]: Task assigned to @Bob               │   │
│   │   [Bob]: On it!                                          │   │
│   │                                                          │   │
│   └─────────────────────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Identity & Registration

### Azure AD / Entra ID Registration

Each bot must be registered in the tenant's Azure AD following MS Teams bot framework requirements:

| Registration Aspect | Requirement |
|--------------------|-------------|
| **App Registration** | One app registration per bot |
| **Bot Framework** | Registered in Azure Bot Service |
| **Permissions** | Teams.ReadWrite, User.Read, etc. |
| **Naming** | Unique across tenant's bots |

### Cipher IAM Integration

Each bot also exists in Cipher IAM:

| Cipher Aspect | Purpose |
|---------------|---------|
| **Bot Identity** | Service principal in Cipher |
| **Workbench Binding** | Bot is bound to specific workbench |
| **Permission Scope** | Access controlled per workbench policies |
| **Audit Trail** | Bot actions are audited like any other actor |

---

## Bot Provisioning

### Provisioning Process

Bots are onboarded as part of the **Workbench Deployment** process:

| Step | Actor | Action |
|------|-------|--------|
| 1 | **Tenant Admin** | Provisions bots on Azure AD/Entra ID |
| 2 | **Tenant Admin** | Configures bot identity and credentials |
| 3 | **Deployment** | Associates bot to Bot Profile in Cipher IAM |
| 4 | **Workbench** | Bots become active for the workbench |

### Azure Tenant Relationship

| Aspect | Constraint |
|--------|------------|
| **Workbench ↔ Azure Tenant** | Each workbench corresponds to exactly one Azure/MS Teams tenant |
| **Employees & Bots** | Belong to the same Azure tenant |
| **Cross-Tenant** | Not supported (employees must be in the same tenant as bots) |

### Hub Identity ↔ Teams Identity

| Aspect | Implementation |
|--------|----------------|
| **Agent → Teams User** | Agents must have corresponding Teams accounts |
| **Membership Management** | Module uses Microsoft Graph API to add users to chat groups |
| **Prerequisite** | Module only works for users who are on Teams |

---

### Identity Flow

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   MS Teams   │     │ Azure AD /   │     │  Cipher IAM  │
│   User       │     │ Entra ID     │     │              │
└──────┬───────┘     └──────┬───────┘     └──────┬───────┘
       │                    │                    │
       │ ── Message ──────> │                    │
       │                    │ ── Validate ─────> │
       │                    │                    │ Lookup
       │                    │                    │ Bot + User
       │                    │ <── Token ──────── │
       │                    │                    │
       │ <── Authorized ─── │                    │
       │                    │                    │
```

---

## Configuration

### Workbench Studio Configuration

Process Architects configure bots in Workbench Studio:

```yaml
ms_teams_integration:
  enabled: true
  
  me_bot:
    name: "dispute-ops-agent"
    display_name: "Dispute Ops Agent Copilot"
    description: "Your assistant for dispute operations"
    
  ask_bot:
    name: "dispute-ops-assist"
    display_name: "Dispute Assistance"
    description: "Get help with disputes"
    
  group_bot:
    name: "dispute-ops-hub"
    display_name: "Dispute Ops Hub"
    description: "System updates and group orchestration"
    
  chat_groups:
    enabled: true
    auto_add_subject: true
    auto_add_supervisor: false
    archive_after_days: 90
```

### Scenario-Level Overrides

Individual scenarios can override chat group behavior:

```yaml
scenario:
  name: "High-Value Dispute"
  
  ms_teams:
    chat_group:
      enabled: true
      auto_add_supervisor: true  # Override workbench default
      default_participants:
        - role: "compliance-officer"
```

---

## Interaction Patterns

### Structured Commands (Initial)

```
/tasks              - List my assigned tasks
/task <id>          - View task details
/complete <id>      - Complete a task
/escalate <id>      - Escalate a task
/kb search <query>  - Search knowledge base
/status <request>   - Check request status
```

### NLP-Based (Evolved)

```
"Show me my open tasks"
"What's the status of dispute 12345?"
"I need to escalate the fraud case I'm working on"
"Search the knowledge base for chargeback rules"
```

---

## Related Documentation

- [Chat Group Lifecycle](./chat-group-lifecycle.md) — Request-to-group mapping
- [Message Flow](./message-flow.md) — Signal routing and direct services
- [FAQ](./ms-teams-integration-faq.md) — Design decisions

---

*Last updated: 2026-01-05*

