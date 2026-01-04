# MS Teams Integration — FAQ

> **Status:** 🟡 WIP — Capturing design decisions and clarifications

This document captures Q&A from the design discussion for the MS Teams Integration subsystem.

---

## Scope

### Q: Who is this integration for?

**A:** Business Employees, Agents, and Supervisors only. **Not** for Business Customers.

### Q: Is excluding Business Customers a design decision or phase limitation?

**A:** Current limitation. Could consider adding a "Subject_Bot" for customers in a future phase if tenants want.

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
- The Signal Exchange Bot orchestrates the group, adding members as needed
- All collaboration is captured as Request updates

---

### Q: What types of bots are there?

**A:** Two conceptual bot types per workbench:

| Bot Type | Codename | Primary Users | Purpose |
|----------|----------|---------------|---------|
| **Agent Copilot** | Me_Bot | Agents, Supervisors | Task processing, workbench operations |
| **Business Employee Copilot** | Ask_Bot | Business Employees | Request initiation, assigned task handling |

Additionally, there is a **Signal Exchange Bot** per workbench for chat group lifecycle management.

### Q: Are "Me_Bot" and "Ask_Bot" the actual names?

**A:** No, these are **conceptual/code names** for documentation. Process Architects can name bots as they please per workbench. Suggested convention: include workbench code/name in the bot name for uniqueness.

### Q: How many bot instances are there?

**A:** **One bot of each kind per workbench**, registered on MS Teams. All bots are scoped to a workbench only. For example:
- `dispute-ops-me-bot` (Agent Copilot for Dispute Operations workbench)
- `dispute-ops-ask-bot` (Business Employee Copilot for Dispute Operations workbench)
- `dispute-ops-system-bot` (Signal Exchange Bot for Dispute Operations workbench)

Bot names must be unique across workbenches.

### Q: Does Supervisor use a different bot than Agents?

**A:** No, Supervisors use the same **Me_Bot** as Agents.

---

## Me_Bot (Agent Copilot)

### Q: Can an Agent complete the full task lifecycle via MS Teams?

**A:** **Yes, if the Task Solver is Adaptive Card compatible.** The task solver component can be rendered directly in MS Teams if it's compatible with MS Teams Adaptive Cards.

**If not compatible:** The agent can launch the Task Solver via Hercules Launcher from Teams messages. This provides a direct link to the task without navigating through Hub Home → Workbench → Agent Desk → Pick Task.

### Q: Who decides if a Task Solver is Adaptive Card compatible?

**A:** **Developer.** They explicitly register a task-solver component to be used for MS Teams integration.

### Q: What is the fallback if no Adaptive Card component is specified?

**A:** If the Adaptive Card component is not specified, the integration uses **Hercules Launcher** to launch the default/web-based task-solver component.

### Q: Are there size/complexity limits for Adaptive Cards?

**A:** No. This is solely dependent on developer-provided configuration.

### Q: What can an Agent do via Me_Bot?

| Capability | Supported? |
|------------|------------|
| View assigned tasks | ✅ Yes |
| Query knowledge base | ✅ Yes |
| Record decisions and thoughts | ✅ Yes |
| Complete tasks | ✅ Yes |
| Escalate tasks | ✅ Yes |
| Reassign tasks | ✅ Yes |
| Reject tasks (send back to allocation) | ✅ Yes |
| **Directly invoke tools** | ❌ No — must go through Hub Applications and Consoles |

### Q: Is Me_Bot conversational or command-based?

**A:** The MS Teams module may start with **structured/command-based** but is certainly expected to support **NLP-based mapping**. The very first version itself could be NLP-based with support for structured messages as well.

### Q: Do Supervisors get additional capabilities in Me_Bot?

**A:** **Yes.** Supervisors get additional capabilities:
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
| **Bot as orchestrator** | Signal Exchange Bot manages membership, relays system updates |
| **Dynamic membership** | As tasks are assigned, assignees join automatically |
| **Persistent history** | All messages become Request updates, preserved for audit |

This approach recognizes that:
- Complex requests involve handoffs between agents
- Agents need to coordinate, ask questions, share context
- Supervisors need visibility into collaboration
- Traditional task assignment doesn't capture the human interaction

---

### Q: Is a new Teams group created for each Request?

**A:** Yes, for **scenarios configured to use Teams integration**. Not all scenarios need Teams chat groups.

### Q: Who are the initial members of a Request chat group?

**A:** At request creation (before automation application is initiated):

| Member | When Added | Condition |
|--------|------------|-----------|
| **Signal Exchange Bot** | Immediately | Always (represents the system) |
| **Scenario Default Participants** | Immediately | As configured in scenario |
| **Subject** | Immediately | If scenario's Teams integration is configured to include subject |
| **Task Assignees** | When tasks are assigned | As Hub Applications create and assign tasks |
| **Supervisor** | Per configuration | As per scenario manifest/deployment config |

### Q: What does the Signal Exchange Bot do in the chat group?

**A:** The Signal Exchange Bot:
- **Handles lifecycle** — adds members to chat, archives the chat when done
- **Relays system updates** — posts updates that are not originated by any individual participant
- **Represents the workbench's Signal Exchange** (the bot is a construct of the MS Teams integration module; Signal Exchange itself is unaware of this)

**Important flow:**
- When messages are received to a request from MS Teams channel, the MS Teams module adds them as updates to the request
- All agents watching the request are dispatched this update by Signal Exchange
- The origination channel (MS Teams) is captured in envelope metadata
- All agents with active tasks in a request are by default deemed as watchers
- The MS Teams Chat Group reflects all updates to the Request, regardless of Signal Exchange dispatch

### Q: What happens when a new task is assigned?

**A:** The new assignee is added to the chat group.

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

## Signal & Message Flow

### Q: Is there a dedicated MS Teams Signal Provider?

**A:** The MS Teams integration module uses **Heracles as underlying infrastructure**, but Signal Exchange sees messages as signals from the **MS Teams integration module**, not directly from Heracles.

### Q: How does a Business Employee message trigger a Scenario?

**A:** 
1. Business Employee sends message in Ask_Bot
2. Message is treated as a **signal**
3. All triggers evaluate the signal to check if it matches their conditions
4. Highest precedence matching trigger wins
5. If matched → Scenario is triggered, Request is created
6. If no trigger matches → Message is handled by MS Teams module directly (enquiry, help, etc.)

### Q: What services does the MS Teams module handle directly (not via Signal Exchange)?

**A:** The module handles directly:
- Request status queries
- Knowledge base lookups
- Task list queries
- Other interactions that don't need to create/update Requests

The catalog of direct services may expand.

### Q: Why do some requests bypass Signal Exchange?

**A:** Signal Exchange need not be in the path for requests that may not correspond to scenarios. Requests don't go through Signal Exchange only for services that Signal Exchange may not offer. 

Each I/O Gateway/module may have value-additions for efficiency and supported channel nuances that are specific to that module's contract.

### Q: How are Request updates sent to Teams?

**A:** MS Teams module **listens to updates on Request entity** and relays them to the corresponding chat or chat group.

---

## Identity & Authentication

### Q: How are bots authenticated in MS Teams?

**A:** Each bot is registered in **AD/Entra ID** following MS Teams bot identity guidelines.

### Q: Do bots exist in Cipher IAM?

**A:** **Yes.** Each bot also exists in Cipher IAM as a **Bot identity**.

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
- Trigger evaluation for Ask_Bot messages
- Chat group lifecycle management
- Request update → Teams relay
- Direct services (queries not going to Signal Exchange)
- Chat history archival
- Identity and registration
- Task Solver rendering (Adaptive Cards vs Hercules Launcher)

---

## Summary Tables

### Bot Types per Workbench

| Bot | Codename | Users | Purpose |
|-----|----------|-------|---------|
| Agent Copilot | Me_Bot | Agents, Supervisors | Task processing, KB queries, decisions |
| Business Employee Copilot | Ask_Bot | Business Employees | Request initiation, assigned tasks |
| System Bot | Signal Exchange Bot | System | Chat group lifecycle, system updates |

### Capability Matrix

| Capability | Me_Bot (Agent) | Me_Bot (Supervisor) | Ask_Bot |
|------------|----------------|---------------------|---------|
| View tasks | ✅ Assigned | ✅ All + Queue | ✅ Explicitly assigned |
| Complete tasks | ✅ | ✅ | ✅ |
| Query KB | ✅ | ✅ | ✅ |
| Initiate requests | ❌ | ❌ | ✅ |
| Queue metrics | ❌ | ✅ | ❌ |
| Reassign across agents | ❌ | ✅ | ❌ |
| Escalation handling | ❌ | ✅ | ❌ |
| Invoke tools directly | ❌ | ❌ | ❌ |

---

*Last updated: 2026-01-05*
