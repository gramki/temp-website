# MS Teams Integration — FAQ

> **Status:** 🟡 WIP — Capturing design decisions and clarifications

This document captures Q&A from the design discussion for the MS Teams Integration subsystem.

---

## Scope

### Q: Who is this integration for?

**A:** Business Employees, Agents, and Supervisors only. **Not** for Business Customers.

### Q: Is excluding Business Customers a design decision or phase limitation?

**A:** Current limitation. Could consider adding a "Subject_Bot" for customers in a future phase if tenants want.

### Q: What are the prerequisites for using MS Teams integration?

**A:** 
- Organization must be using Microsoft Teams
- Users must have Teams accounts
- Each workbench corresponds to exactly one Azure/MS Teams tenant
- Tenant's employees and bots belong to the same Azure tenant

---

## Bot Architecture

### Design Rationale

The MS Teams integration architecture is driven by two key objectives:

| Objective | Approach |
|-----------|----------|
| **Bots as Copilots** | Each bot serves as a dedicated copilot for its persona, providing contextual assistance within their natural workspace (MS Teams) |
| **Chat Groups as Collaboration Surfaces** | When orchestration is required between multiple participants, the bot becomes the orchestrator using chat groups as the collaboration surface |

**Why Copilots?**
- Agents and Business Employees already work in MS Teams
- Rather than forcing context switches to Hub UIs, bring Hub capabilities to where they work
- Each persona gets a dedicated copilot tuned to their needs and permissions

**Why Chat Groups for Orchestration?**
- Requests often involve multiple agents across different tasks
- Chat groups provide natural, real-time collaboration
- The Group Orchestration Bot orchestrates the group, adding members as needed
- All collaboration is captured as Request updates

---

### Q: What types of bots are there?

**A:** Three bot types per workbench:

| Bot Type | Codename | Primary Users | Purpose |
|----------|----------|---------------|---------|
| **Agent Copilot** | Me_Bot | Agents, Supervisors | Full Agent Desk capabilities via Teams |
| **Business Employee Copilot** | Ask_Bot | Business Employees | Request initiation, assigned task handling |
| **Group Orchestration Bot** | Group_Bot | System | Chat group lifecycle, system updates |

### Q: Why "Group Orchestration Bot" instead of "Signal Exchange Bot"?

**A:** The bot orchestrates collaboration between agents working on a request. Signal Exchange itself is unaware of this bot — it's a construct of the MS Teams integration module. The name signifies its orchestration role for group collaboration.

### Q: Are "Me_Bot", "Ask_Bot", and "Group_Bot" the actual names?

**A:** No, these are **conceptual/code names** for documentation. Process Architects can name bots as they please per workbench. Suggested convention: include workbench code/name in the bot name for uniqueness.

### Q: How many bot instances are there?

**A:** **One bot of each kind per workbench**, registered on MS Teams. All bots are scoped to a workbench only. For example:
- `dispute-ops-agent` (Agent Copilot for Dispute Operations workbench)
- `dispute-ops-assist` (Business Employee Copilot for Dispute Operations workbench)
- `dispute-ops-hub` (Group Orchestration Bot for Dispute Operations workbench)

Bot names must be unique across workbenches.

### Q: Does Supervisor use a different bot than Agents?

**A:** No, Supervisors use the same **Me_Bot** as Agents, with additional capabilities.

---

## Me_Bot (Agent Copilot)

### Q: What can an Agent do via Me_Bot?

**A:** An Agent should be able to do via Me_Bot **everything they can do on Agent Desk**:

| Capability | Supported | Notes |
|------------|-----------|-------|
| View assigned tasks | ✅ | My Tasks, Queue Tasks |
| Pick tasks from queue | ✅ | |
| Complete tasks | ✅ | Via Adaptive Card or Hercules Launcher |
| Escalate tasks | ✅ | |
| Reassign tasks | ✅ | Own tasks |
| Reject tasks | ✅ | Returns to allocation queue |
| Query knowledge base | ✅ | SOPs, policies, reference materials |
| View signals | ✅ | Exceptions, observations |
| View/complete routines & checklists | ✅ | |
| Record decisions | ✅ | CAF-compliant |
| Record thoughts/memos | ✅ | Request updates |
| Access files | ✅ | Related to requests and entities |
| Initiate requests | ✅ | Trigger scenarios explicitly |
| View agents & roles | ✅ | Who is working on what, own roles |
| **Direct tool invocation** | ❌ | Must use Consoles/Applications |

> **Principle:** Me_Bot provides Agent Desk capabilities via the Teams channel.

### Q: Can an Agent complete the full task lifecycle via MS Teams?

**A:** **Yes, if the Task Solver is Adaptive Card compatible.** The task solver component can be rendered directly in MS Teams if it's compatible with MS Teams Adaptive Cards.

**If not compatible:** The agent can launch the Task Solver via Hercules Launcher from Teams messages. This provides a direct link to the task without navigating through Hub Home → Workbench → Agent Desk → Pick Task.

### Q: Who decides if a Task Solver is Adaptive Card compatible?

**A:** **Developer.** They explicitly register a task-solver component to be used for MS Teams integration.

### Q: What is the fallback if no Adaptive Card component is specified?

**A:** If the Adaptive Card component is not specified, the integration uses **Hercules Launcher** to launch the default/web-based task-solver component.

### Q: Are there size/complexity limits for Adaptive Cards?

**A:** No. This is solely dependent on developer-provided configuration.

### Q: Is Me_Bot conversational or command-based?

**A:** The MS Teams module may start with **structured/command-based** but is certainly expected to support **NLP-based mapping**. The very first version itself could be NLP-based with support for structured messages as well.

### Q: Do Supervisors get additional capabilities in Me_Bot?

**A:** **Yes.** Supervisors get additional capabilities beyond Agent capabilities:
- Queue metrics
- Reassignment across agents
- Escalation handling

These capabilities will evolve over time.

### Q: Do Supervisors primarily use Supervisor Desk or Me_Bot?

**A:** **Both.** Supervisors primarily use **Supervisor Desk** for management operations, and **Me_Bot** for their own tasks and quick actions.

---

## Ask_Bot (Business Employee Copilot)

### Q: What is Ask_Bot for?

**A:** Two primary purposes:
1. **Initiating requests** — Business Employee messages can trigger scenarios
2. **Acting on assigned tasks** — Tasks explicitly assigned to them (as subject or explicit assignment)

### Q: Can Business Employees see Agent-role tasks via Ask_Bot?

**A:** **No.** They only see tasks **explicitly assigned to them**, not tasks assigned through agent queue allocation.

### Q: Is Ask_Bot the same as using Hub via Heracles?

**A:** Yes, conceptually. It's using Hub with **MS Teams as the channel**.

### Q: Can a Business Employee send a free-form message that gets classified to a scenario?

**A:** **Yes.** Free-form messages can be classified to scenarios through NLP-based mapping.

### Q: What happens if no trigger matches a Business Employee's message?

**A:** The MS Teams integration module will respond with a suitable message (help, clarification, etc.).

---

## Chat Group per Request

### Design Rationale

Chat groups serve as **collaboration surfaces** for multi-participant orchestration:

| Aspect | Rationale |
|--------|-----------|
| **One group per request** | Natural mapping — all collaboration about a request in one place |
| **Bot as orchestrator** | Group Orchestration Bot manages membership, relays system updates |
| **Dynamic membership** | As tasks are assigned, assignees join automatically |
| **Persistent history** | All messages become Request updates, preserved for audit |

This approach recognizes that:
- Complex requests involve handoffs between agents
- Agents need to coordinate, ask questions, share context
- Supervisors need visibility into collaboration
- Traditional task assignment doesn't capture the human interaction

---

### Q: Is a new Teams chat group created for each Request?

**A:** Yes, for **scenarios configured to use Teams integration**. Not all scenarios need Teams chat groups.

### Q: Who are the initial members of a Request chat group?

**A:** At request creation (before automation application is initiated):

| Member | When Added | Condition |
|--------|------------|-----------|
| **Group Orchestration Bot** | Immediately | Always (represents the system) |
| **Scenario Default Participants** | Immediately | As configured in scenario |
| **Subject** | Immediately | If scenario's Teams integration is configured to include subject |
| **Task Assignees** | When tasks are assigned | As Hub Applications create and assign tasks |
| **Supervisor** | Per configuration | As per scenario manifest/deployment config |

### Q: How are members added to the chat group?

**A:** Via Microsoft Graph API. The MS Teams integration module uses Graph API to manage group membership.

### Q: What does the Group Orchestration Bot do in the chat group?

**A:** The Group Orchestration Bot:
- **Handles lifecycle** — creates group, adds members, archives when done
- **Relays system updates** — posts updates that are not originated by any individual participant
- **Represents the workbench** (the bot is a construct of the MS Teams integration module; Signal Exchange itself is unaware of this)

**Important flow:**
- When messages are received from MS Teams, the Teams module adds them as updates to the Request
- Signal Exchange dispatches Request Updates to registered **observers** (like MS Teams module), NOT to agents directly
- Signal Exchange operates at the Request level — it cannot attribute updates to specific tasks or agents
- The MS Teams module, as an observer, parses updates to determine which agents to notify
- The origination channel (MS Teams) is captured in envelope metadata
- The MS Teams chat group reflects all updates to the Request

### Q: What happens when a new task is assigned?

**A:** The new assignee is added to the chat group via Graph API.

### Q: Are agents removed from the group when their task is completed?

**A:** **No.** Agents are not automatically removed. They may choose to:
- Leave the group
- Mute the group

### Q: What happens when the Request is completed?

**A:** 
1. Chat group is updated with completion status
2. Group remains accessible to agents and configured participants
3. Group is **archived on a configured schedule** (could be months after completion)

### Q: Is the chat history preserved?

**A:** **Yes.** Each message exchanged in the group is an update to the Request and is preserved until the Request is archived.

---

## Message Classification Pipeline

### Q: Who handles message classification?

**A:** The classification is a **pipeline across modules**:

1. **Teams Module (First):**
   - Receives message from Teams channel
   - Performs NLP/structured classification
   - Decides: handle directly (query, help) OR forward to Signal Exchange
   - For forwarded messages: translates unstructured/NLP input to structured signal format

2. **Signal Exchange (Second):**
   - Receives structured signal from Teams module
   - Evaluates triggers as it would for any signal provider
   - **Does NOT short-circuit** its logic for MS Teams — treats it like any other signal source
   - Creates Request or dispatches update

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MESSAGE CLASSIFICATION PIPELINE                           │
│                                                                              │
│   User Message (unstructured/NLP/structured)                                 │
│         │                                                                    │
│         ▼                                                                    │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                  MS TEAMS INTEGRATION MODULE                         │   │
│   │                                                                      │   │
│   │   ┌─────────────────────────────────────────────────────────────┐   │   │
│   │   │                    CLASSIFICATION                            │   │   │
│   │   │  • NLP intent extraction                                     │   │   │
│   │   │  • Structured command matching                               │   │   │
│   │   │  • May need trigger expectations for classification          │   │   │
│   │   └─────────────────────────┬───────────────────────────────────┘   │   │
│   │                             │                                        │   │
│   │               ┌─────────────┴─────────────┐                         │   │
│   │               │                           │                         │   │
│   │         Handle Directly?           Forward to Signal Exchange?      │   │
│   │               │                           │                         │   │
│   │               ▼                           ▼                         │   │
│   │   ┌─────────────────┐        ┌─────────────────────────────────┐   │   │
│   │   │ Direct Service  │        │ Translate to Structured Signal  │   │   │
│   │   │ (KB, Status,    │        │ (Extract entities, format       │   │   │
│   │   │  Help, etc.)    │        │  payload for Signal Exchange)   │   │   │
│   │   └─────────────────┘        └───────────────┬─────────────────┘   │   │
│   │                                              │                      │   │
│   └──────────────────────────────────────────────┼──────────────────────┘   │
│                                                  │                          │
│                                                  ▼                          │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                       SIGNAL EXCHANGE                                │   │
│   │                                                                      │   │
│   │   • Receives structured signal (CHAT_MESSAGE type)                   │   │
│   │   • Evaluates triggers (same as any signal provider)                 │   │
│   │   • Creates Request or dispatches update                             │   │
│   │   • NO special handling for MS Teams source                          │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Q: Why does the Teams module need trigger expectations?

**A:** To perform accurate NLP classification, the module may need to understand what triggers exist in the workbench. This helps it:
- Extract relevant entities
- Determine if a message is likely to match a trigger
- Format the structured signal appropriately

This is an implementation concern and may evolve.

### Q: Does Signal Exchange know it's receiving from MS Teams?

**A:** Signal Exchange receives the signal with metadata indicating the source is MS Teams. However, it **does not alter its processing logic** based on this. The trigger evaluation, request creation, and dispatch follow the same path as any other signal provider.

---

## Signal & Message Flow

### Q: Is there a dedicated MS Teams Signal Provider?

**A:** The MS Teams integration module uses **Heracles as underlying infrastructure**, but Signal Exchange sees signals from the **MS Teams integration module** with signal type `CHAT_MESSAGE`.

### Q: How does a Business Employee message trigger a Scenario?

**A:** 
1. Business Employee sends message in Ask_Bot
2. MS Teams module receives and classifies the message
3. If trigger-worthy, module translates to structured signal
4. Signal is sent to Signal Exchange
5. Signal Exchange evaluates triggers (as for any signal)
6. Highest precedence matching trigger wins
7. If matched → Scenario is triggered, Request is created
8. If no trigger matches → Response returned to Teams module → module handles directly

### Q: What services does the MS Teams module handle directly (not via Signal Exchange)?

**A:** The module handles directly:
- Request status queries
- Knowledge base lookups
- Task list queries
- Help/menu requests
- Other interactions that don't need to create/update Requests

The catalog of direct services may expand.

### Q: Why do some requests bypass Signal Exchange?

**A:** Signal Exchange handles scenario-based request creation and updates. For read-only queries (status, KB lookup, task list), there's no need to involve Signal Exchange. Each I/O module may have value-additions for efficiency and channel-specific optimizations.

### Q: How are Request updates sent to Teams?

**A:** MS Teams module is a **registered observer** for Request Updates. When Signal Exchange dispatches a Request Update to observers, the MS Teams module:
1. Receives the update (at Request level, not agent/task level)
2. Parses the update to determine which agents are affected
3. Relays relevant information to the corresponding chat group

**Note:** Signal Exchange dispatches to observers, not to agents or tasks directly. It operates at the Request level.

### Q: How are cross-channel updates attributed in chat groups?

**A:** When an agent makes an update through a **different channel** (e.g., Agent Desk, Mobile), the MS Teams module relays it to the chat group with attribution based on credential sharing:

| Condition | Attribution |
|-----------|-------------|
| Agent shared Teams credentials | Posted **as the agent** (their Teams identity) |
| No credential sharing | Posted **by Group Orchestration Bot** with on-behalf-of attribution |

**With credentials shared:**
```
[Alice] — 3:15 PM
I've reviewed the documentation and approved the claim.
(Updated via Agent Desk)
```

**Without credentials:**
```
[Dispute Ops Hub] — 3:15 PM
📝 Update from @Alice (via Agent Desk):

"I've reviewed the documentation and approved the claim."
```

**Key points:**
- Credential sharing is **opt-in** and **per workbench**
- Credentials are stored securely in Cipher IAM
- Agent can revoke at any time
- This ensures conversation continuity regardless of which channel agents use

---

## Bot Provisioning & Identity

### Q: How are bots provisioned?

**A:** Bots are onboarded as part of the **Workbench Deployment** process:

1. **Tenant Admin** provisions bots on Azure AD/Entra ID
2. Admin provides the relevant identity and credentials
3. These are associated to the **Bot Profile in Cipher IAM** during deployment

### Q: What's the relationship between Hub tenant and Azure tenant?

**A:** Each workbench under a Hub Tenant corresponds to **exactly one Azure/MS Teams tenant**. Tenant's employees and bots belong to the same Azure tenant.

### Q: How are bots authenticated in MS Teams?

**A:** Each bot is registered in **Azure AD/Entra ID** following MS Teams bot identity guidelines.

### Q: Do bots exist in Cipher IAM?

**A:** **Yes.** Each bot also exists in Cipher IAM as a **Bot identity**, associated with the workbench during deployment.

### Q: How is Hub identity mapped to Teams identity?

**A:** 
- Hub users who are Agents must have corresponding Teams accounts
- The MS Teams module uses **Graph API** to add users to chat groups
- The module only works for users who are on Teams

### Q: Can a person access multiple workbenches' bots?

**A:** **Yes.** A person can have access to any number of workbenches' bots. This is why bot names must be unique across workbenches.

---

## Architecture & Placement

### Q: Where should MS Teams integration be documented?

**A:** 
- Main content: `04-subsystems/ms-teams-integration/`
- Reference in: `04-subsystems/signal-providers/` (since it's also a signal provider)

### Q: What should the subsystem document cover?

**A:** MS Teams integration is **more than a signal provider**. It should cover:
- Bot types and configuration
- Message → Signal transformation (structured + NLP)
- Classification pipeline
- Chat group lifecycle management
- Request update → Teams relay
- Direct services (queries not going to Signal Exchange)
- Chat history archival
- Bot provisioning and identity
- Task Solver rendering (Adaptive Cards vs Hercules Launcher)

---

## Summary Tables

### Bot Types per Workbench

| Bot | Codename | Users | Purpose |
|-----|----------|-------|---------|
| Agent Copilot | Me_Bot | Agents, Supervisors | Full Agent Desk capabilities via Teams |
| Business Employee Copilot | Ask_Bot | Business Employees | Request initiation, assigned tasks |
| Group Orchestration Bot | Group_Bot | System | Chat group lifecycle, system updates |

### Capability Matrix

| Capability | Me_Bot (Agent) | Me_Bot (Supervisor) | Ask_Bot |
|------------|----------------|---------------------|---------|
| View tasks | ✅ Assigned + Queue | ✅ All + Queue | ✅ Explicitly assigned |
| Complete tasks | ✅ | ✅ | ✅ |
| Initiate requests | ✅ | ✅ | ✅ |
| Query KB | ✅ | ✅ | ✅ |
| View signals | ✅ | ✅ | ❌ |
| Routines & checklists | ✅ | ✅ | ❌ |
| Queue metrics | ❌ | ✅ | ❌ |
| Reassign across agents | ❌ | ✅ | ❌ |
| Escalation handling | ❌ | ✅ | ❌ |
| Invoke tools directly | ❌ | ❌ | ❌ |

---

## Open Questions

The following questions remain open for future clarification:

### Adaptive Cards
- What version of Adaptive Cards is supported?
- What actions are supported within cards?
- How do cards submit data back to Hub?
- Can cards update dynamically (refresh)?

### File Handling
- Can users attach files in chat that become part of the Request?
- Can bots share files (evidence, documents)?
- How are attachments stored (Dia integration)?

### Notification Preferences
- Can users mute specific types of notifications?
- Are there preferences for what updates trigger Teams messages?
- Can agents choose email-only vs. Teams notifications?

### Offline/Async Handling
- What happens when user sends message but Hub is unavailable?
- How are long-running requests with no updates for days handled?

### Security & Compliance
- What data classification applies to chat content?
- How do message retention policies interact (Teams vs. Hub)?
- What compliance certifications are relevant?

### Monitoring & Observability
- How are bot interactions logged?
- What metrics are collected?
- How to debug message classification issues?

### Multi-Workbench Experience
- How does a user switch between workbench bots?
- Is there a unified view across workbenches?

### Mobile Experience
- Are there MS Teams mobile behavior differences?
- What are Adaptive Card limitations on mobile?

---

*Last updated: 2026-01-05*
