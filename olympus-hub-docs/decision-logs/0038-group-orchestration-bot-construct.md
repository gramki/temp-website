# ADR-0038: Group Orchestration Bot as MS Teams Module Construct

| Property       | Value                                           |
|----------------|-------------------------------------------------|
| **Status**     | Accepted                                        |
| **Date**       | 2026-01-06                                      |
| **Category**   | Integration                                     |
| **Deciders**   | Architecture Team                               |
| **Supersedes** | -                                               |

---

## Context

In the MS Teams integration design, there's a need for a system presence in chat groups that:
- Creates and manages group lifecycle
- Posts system updates (task assignments, milestones, completions)
- Adds members to groups via Graph API

The question is: What is the relationship between this bot and Signal Exchange? Should Signal Exchange be aware of this bot construct?

---

## Decision

**The Group Orchestration Bot is a construct of the MS Teams integration module. Signal Exchange is unaware of this bot — it's purely a Teams-side implementation detail. The bot orchestrates collaboration between agents, not Signal Exchange operations.**

### Bot Identity

| Aspect | Description |
|--------|-------------|
| **Codename** | Group Orchestration Bot, Group_Bot |
| **Example** | `dispute-ops-hub` |
| **Owner** | MS Teams Integration Module |
| **SX Awareness** | Signal Exchange has no knowledge of this bot |

### Bot Responsibilities

| Responsibility | Description |
|----------------|-------------|
| **Chat group lifecycle** | Create groups for requests, add members via Graph API, archive on schedule |
| **System update relay** | Post updates not originated by any human participant |
| **Group orchestration** | Manage collaboration between agents on a request |

### What It Does NOT Do

| Not Responsible For | Why |
|--------------------|-----|
| Respond to queries | That's Me_Bot or Ask_Bot's job |
| Facilitate @mentions | Users @mention each other directly |
| Interactive conversation | It's a system presence, not a copilot |
| Signal Exchange operations | SX is unaware of this bot |

---

## Alternatives Considered

### 1. Signal Exchange Bot

Name the bot "Signal Exchange Bot" and have SX manage it.

**Rejected because:**
- Creates tight coupling between SX and Teams
- SX should be channel-agnostic
- Name implies SX awareness when there is none
- Confuses architectural boundaries

### 2. Hub Bot

A shared "Hub Bot" across all channels.

**Rejected because:**
- Each channel has different requirements
- Teams-specific functionality (Graph API, groups)
- Would need to be aware of all channel specifics
- Better to have channel-specific constructs

### 3. No System Bot

Use Me_Bot/Ask_Bot for all messages including system updates.

**Rejected because:**
- Copilot bots are for persona assistance
- System updates should have distinct identity
- Would confuse bot purpose
- Harder to distinguish user vs. system messages

---

## Consequences

### Positive

1. **Clean separation** — SX doesn't know about Teams-specific constructs
2. **Clear naming** — "Group Orchestration" describes what it does
3. **Channel encapsulation** — Teams details stay in Teams module
4. **Future flexibility** — Other channels can have their own constructs

### Negative

1. **Three bots** — Users see three different bots per workbench
2. **Bot confusion** — Users may not understand Group Bot purpose initially
3. **Limited interaction** — Group Bot doesn't respond to queries

### Risks

1. **User expectations** — Users may try to interact with Group Bot directly
2. **Naming clarity** — Need to communicate purpose clearly

---

## Implementation Notes

### Bot Registration

Group Orchestration Bot is registered:
- In Azure AD/Entra ID like other workbench bots
- In Cipher IAM with bot identity
- Associated with workbench during deployment

### Graph API Usage

The bot uses Microsoft Graph API to:
- Create chat groups
- Add/manage group members
- Post messages to groups
- Archive groups after completion

### Update Source Detection

The MS Teams module uses this bot identity to:
- Post updates received from Signal Exchange (as observer)
- Post updates on behalf of agents from other channels
- Post system messages (request created, task assigned, etc.)

---

## Related Decisions

- [ADR-0032: Bots as Persona Copilots](./0032-bots-as-persona-copilots.md)
- [ADR-0034: One Bot of Each Kind per Workbench](./0034-workbench-scoped-bots.md)
- [ADR-0037: MS Teams Module as Signal Exchange Observer](./0037-ms-teams-module-as-observer.md)

