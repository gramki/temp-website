# MS Teams Integration — FAQ

> **Status:** 🟡 WIP — Capturing design decisions and clarifications

This document captures Q&A from the design discussion for the MS Teams Integration subsystem.

---

## Scope

### Q: Who is this integration for?

**A:** Business Employees, Agents, and Supervisors only. **Not** for Business Customers.

### Q: Is excluding Business Customers a design decision or phase limitation?

**A:** *[Pending clarification]*

---

## Bot Architecture

### Q: What types of bots are there?

**A:** Two conceptual bot types per workbench:

| Bot Type | Codename | Primary Users | Purpose |
|----------|----------|---------------|---------|
| **Agent Copilot** | Me_Bot | Agents, Supervisors | Task processing, workbench operations |
| **Business Employee Copilot** | Ask_Bot | Business Employees | Request initiation, assigned task handling |

### Q: Are "Me_Bot" and "Ask_Bot" the actual names?

**A:** No, these are **conceptual/code names** for documentation. Process Architects can name bots as they please per workbench. Suggested convention: include workbench code/name in the bot name for uniqueness.

### Q: How many bot instances are there?

**A:** **One bot of each kind per workbench**, registered on MS Teams. For example:
- `dispute-ops-me-bot` (Agent Copilot for Dispute Operations workbench)
- `dispute-ops-ask-bot` (Business Employee Copilot for Dispute Operations workbench)

Bot names must be unique across workbenches.

### Q: Does Supervisor use a different bot than Agents?

**A:** No, Supervisors use the same **Me_Bot** as Agents.

---

## Me_Bot (Agent Copilot)

### Q: Can an Agent complete the full task lifecycle via MS Teams?

**A:** **Yes, if the Task Solver is Adaptive Card compatible.** The task solver component can be rendered directly in MS Teams if it's compatible with MS Teams Adaptive Cards.

**If not compatible:** The agent can launch the Task Solver via Hercules Launcher from Teams messages. This provides a direct link to the task without navigating through Hub Home → Workbench → Agent Desk → Pick Task.

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

**A:** Initial versions will likely be **command-based**. Expected to evolve into a **GenAI-based conversational bot**.

### Q: Do Supervisors get additional capabilities in Me_Bot?

**A:** *[Pending clarification — queue metrics, cross-agent reassignment, escalation handling?]*

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

---

## Chat Group per Request

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

**A:** 
- Request lifecycle queries
- Other interactions that don't need to create/update Requests

*[Pending clarification: KB lookups? Task list queries?]*

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
- Message → Signal transformation
- Trigger evaluation for Ask_Bot messages
- Chat group lifecycle management
- Request update → Teams relay
- Direct services (queries not going to Signal Exchange)
- Chat history archival
- Identity and registration

---

## Pending Clarifications

The following questions are awaiting answers:

### A. Task Solver Rendering

1. Who decides if a Task Solver is "Adaptive Card compatible"?
   - Developer marks it during Task Solver development?
   - Automatic detection?
2. Is there a fallback hierarchy? (Adaptive Card → Hercules Launcher)
3. Are there size/complexity limits for Adaptive Cards that force Hercules fallback?

### B. Chat Group Identity

1. Is the Signal Exchange bot a single bot per tenant or per workbench?
2. What does the Signal Exchange bot do in the group?
   - Post status updates?
   - Respond to queries about request status?
   - Facilitate @mentions of agents?

### C. Message → Signal Mapping

1. Is this intent classification (NLP-based) or structured command matching initially?
2. Can a Business Employee send a free-form message that gets classified to a scenario?
3. What happens if no trigger matches? (Error? Fallback to help?)

### D. Module Direct Services

1. What services does the module handle directly?
   - Request status queries?
   - Knowledge base lookups?
   - Task list queries?
2. Is this essentially a local API that bypasses Signal Exchange for read-only operations?

### E. Supervisor Capabilities

1. Do Supervisors get additional capabilities beyond what Agents see via Me_Bot?
   - Queue metrics?
   - Reassignment across agents?
   - Escalation handling?
2. Or do they primarily use Supervisor Desk for management and Me_Bot only for their own tasks?

### F. Scope Limitation

1. Is excluding Business Customers a design decision (customers shouldn't use Teams) or phase 1 limitation?
2. Could a future phase add a "Subject_Bot" for customers if tenants want?

---

*Last updated: 2026-01-04*

