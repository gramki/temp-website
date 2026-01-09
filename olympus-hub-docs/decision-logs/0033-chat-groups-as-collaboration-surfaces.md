# ADR-0033: Chat Groups as Collaboration Surfaces

| Property       | Value                                           |
|----------------|-------------------------------------------------|
| **Status**     | Accepted                                        |
| **Date**       | 2026-01-06                                      |
| **Category**   | Integration                                     |
| **Deciders**   | Architecture Team                               |
| **Supersedes** | -                                               |

---

## Context

Traditional task management systems capture **what** was done (task assignments, status updates) but not **how** teams collaborated to achieve outcomes. When multiple agents work on a request involving handoffs, escalations, and coordination:

1. Where should the collaboration happen?
2. How should collaboration be captured for audit and knowledge?
3. How should new participants be brought up to speed?

MS Teams is already the collaboration platform for most enterprise users.

---

## Decision

**When orchestration is required between multiple participants, create one chat group per request as the collaboration surface, with the Group Orchestration Bot managing membership and relaying system updates.**

### Design Principles

| Aspect | Approach |
|--------|----------|
| **One group per request** | All collaboration about a request in one place |
| **Bot as orchestrator** | Group Orchestration Bot manages membership, relays system updates |
| **Dynamic membership** | As tasks are assigned, assignees join automatically via Graph API |
| **Persistent history** | All messages become Request updates, preserved for audit |

### Why Chat Groups for Orchestration?

- Complex requests involve handoffs between agents
- Agents need to coordinate, ask questions, share context
- Supervisors need visibility into team collaboration
- Traditional task assignment doesn't capture the human interaction
- Chat groups provide natural, real-time collaboration

---

## Alternatives Considered

### 1. Individual Bot Conversations Only

Each agent interacts with their copilot bot privately.

**Rejected because:**
- No shared context between agents
- Collaboration requires external coordination (email, separate chats)
- Handoffs lose context
- Supervisor visibility is fragmented

### 2. Shared Teams Channel per Scenario

One channel for all requests of a scenario type.

**Rejected because:**
- Noisy with unrelated requests
- Difficult to find specific request context
- Privacy concerns (all agents see all requests)
- Archive/retention complexity

### 3. No Teams Collaboration

Use Hub UI for all collaboration.

**Rejected because:**
- Agents prefer Teams for real-time discussion
- Forces context switching
- Loses natural conversation flow
- Teams is already the enterprise standard

---

## Consequences

### Positive

1. **Full collaboration capture** — All discussion is preserved in Request record
2. **Context continuity** — New assignees can read history immediately
3. **Natural handoffs** — Explicit conversations replace implicit handoffs
4. **Shared understanding** — No knowledge silos between agents
5. **Supervisor visibility** — Can observe team collaboration in real-time
6. **Audit trail** — Every message is a timestamped, attributed update

### Negative

1. **Group proliferation** — Many requests = many groups
2. **Notification overload** — Active requests may generate many messages
3. **Archive management** — Need scheduled archival after completion
4. **Graph API dependency** — Membership management depends on MS Graph

### Risks

1. **Agent fatigue** — Too many groups to track
2. **Sensitive discussions** — Need to ensure appropriate membership
3. **Teams limits** — MS Teams has limits on groups per user

---

## Implementation Notes

### Membership Rules

- **Not removed on task completion** — Agent may need to reference context
- **Not removed on reassignment** — Original assignee stays for continuity  
- **Allowed to leave/mute** — Agent choice
- **Archived on schedule** — Configurable days after request completion

### Group Orchestration Bot Role

- Creates group on request creation
- Adds members via Graph API on task assignment
- Posts system updates (assignments, completions, milestones)
- Does NOT respond to queries (that's Me_Bot/Ask_Bot's role)
- Triggers archive after completion

### Cross-Channel Updates

Updates from other channels (Agent Desk, Mobile) are relayed to the chat group:
- If agent shared Teams credentials → posted as agent identity
- Otherwise → posted by Group Orchestration Bot with attribution

---

## Related Decisions

- [ADR-0032: Bots as Persona Copilots](./0032-bots-as-persona-copilots.md)
- [ADR-0036: Cross-Channel Update Attribution](./0036-cross-channel-update-attribution.md)
- [ADR-0019: Signal Exchange Observer Pattern](./0019-signal-exchange-observer-pattern.md)

