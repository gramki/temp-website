# ADR-0032: Bots as Persona Copilots

| Property       | Value                                           |
|----------------|-------------------------------------------------|
| **Status**     | Accepted                                        |
| **Date**       | 2026-01-06                                      |
| **Category**   | Integration                                     |
| **Deciders**   | Architecture Team                               |
| **Supersedes** | -                                               |

---

## Context

Hub needs to integrate with MS Teams to enable Agents, Supervisors, and Business Employees to work within their natural collaboration environment. The fundamental question is how to design the bot experience:

1. Should bots be generic "Hub portals" in Teams?
2. Should bots be task-specific utilities?
3. Should bots be persona-specific assistants?

Users already spend significant time in MS Teams. Forcing them to context-switch to Hub UIs for every interaction reduces productivity and adoption.

---

## Decision

**Each bot serves as a dedicated copilot for its target persona, providing contextual assistance within their natural workspace (MS Teams).**

Three bot types per workbench:

| Bot Type | Codename | Primary Users | Purpose |
|----------|----------|---------------|---------|
| **Agent Copilot** | Me_Bot | Agents, Supervisors | Full Agent Desk capabilities via Teams |
| **Business Employee Copilot** | Ask_Bot | Business Employees | Request initiation, assigned task handling |
| **Group Orchestration Bot** | Group_Bot | System | Chat group lifecycle, system updates |

### Design Principles

1. **Meet users where they work** — Agents and Business Employees already spend time in MS Teams
2. **Reduce context switching** — Bring Hub capabilities to Teams rather than forcing navigation to Hub UIs
3. **Persona-tuned assistance** — Each bot is tailored to its persona's needs and permissions
4. **Conversational evolution** — Start structured, evolve toward GenAI-based natural interaction

---

## Alternatives Considered

### 1. Single Universal Bot

A single bot for all personas with role-based feature filtering.

**Rejected because:**
- User experience becomes cluttered
- Difficult to optimize for specific persona workflows
- Permission model becomes complex
- Conversational context harder to maintain

### 2. Feature-Specific Bots

Multiple bots per feature (Task Bot, KB Bot, Decision Bot, etc.).

**Rejected because:**
- Users need to know which bot to use
- Increases cognitive load
- Fragmented experience
- No unified assistance model

### 3. Portal-Style Bot

A bot that simply links to Hub UI screens.

**Rejected because:**
- Doesn't reduce context switching
- Misses the opportunity for in-Teams task completion
- Feels like a workaround, not integration

---

## Consequences

### Positive

1. **Natural workflow** — Users complete Hub tasks without leaving Teams
2. **Persona optimization** — Each bot can be tuned for its users' specific needs
3. **Permission clarity** — Bot capabilities align with persona permissions
4. **Adoption friendly** — Familiar Teams interface reduces training needs
5. **Scalable design** — New personas can get new copilots

### Negative

1. **Bot proliferation** — Three bots per workbench could be many bots in large tenants
2. **Bot naming complexity** — Need unique names across workbenches
3. **Capability parity** — Must maintain feature parity between Agent Desk and Me_Bot
4. **Initial structured** — Full NLP/GenAI capabilities require evolution

### Risks

1. **Scope creep** — Pressure to add features beyond persona scope
2. **Teams limitations** — Some Hub features may not translate well to Teams

---

## Implementation Notes

- Agents using Me_Bot should be able to do **everything they can do on Agent Desk**
- Supervisors use the same Me_Bot with additional capabilities (queue metrics, cross-agent operations)
- Bot names are configurable by Process Architects (suggested: include workbench identifier)
- Task Solver rendering: Adaptive Card if compatible, otherwise Hercules Launcher link

---

## Related Decisions

- [ADR-0033: Chat Groups as Collaboration Surfaces](./0033-chat-groups-as-collaboration-surfaces.md)
- [ADR-0034: One Bot of Each Kind per Workbench](./0034-workbench-scoped-bots.md)
- [ADR-0010: AI Assistants as First-Class Channel](./0010-ai-assistants-first-class-channel.md)

