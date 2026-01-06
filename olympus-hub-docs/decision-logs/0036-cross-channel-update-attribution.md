# ADR-0036: Cross-Channel Update Attribution

| Property       | Value                                           |
|----------------|-------------------------------------------------|
| **Status**     | Accepted                                        |
| **Date**       | 2026-01-06                                      |
| **Category**   | Integration                                     |
| **Deciders**   | Architecture Team                               |
| **Supersedes** | -                                               |

---

## Context

Agents may interact with Hub through multiple channels:
- Agent Desk (web UI)
- Mobile app
- MS Teams
- MCP-enabled AI assistants

When an agent makes an update through one channel (e.g., Agent Desk), that update should appear in the MS Teams chat group for the request. The question is:

1. How should cross-channel updates be attributed?
2. Should they appear as coming from the agent or from a system bot?
3. How can we maintain conversation continuity?

---

## Decision

**Cross-channel updates are relayed to MS Teams chat groups with attribution based on credential sharing. If the agent has shared Teams credentials with the module, updates are posted as the agent's identity. Otherwise, updates are posted by Group Orchestration Bot with on-behalf-of attribution.**

### Attribution Logic

| Condition | Message Appears As |
|-----------|-------------------|
| Agent has shared Teams credentials | Posted **as the agent** (their Teams identity) |
| Agent has NOT shared credentials | Posted **by Group Orchestration Bot** with on-behalf-of attribution |

### With Credential Sharing (Agent Identity)

```
[Alice] — 3:15 PM
I've reviewed the documentation and approved the claim.
(Updated via Agent Desk)
```

### Without Credential Sharing (Bot Proxy)

```
[Dispute Ops Hub] — 3:15 PM
📝 Update from @Alice (via Agent Desk):

"I've reviewed the documentation and approved the claim."
```

---

## Alternatives Considered

### 1. Always Post as Bot

All cross-channel updates appear as from Group Orchestration Bot.

**Rejected because:**
- Breaks conversation flow (all non-Teams messages look like system messages)
- Agent identity is hidden unless you read the body
- Harder to scan who said what
- Less personal/natural

### 2. Always Post as Agent (Require Credential Sharing)

Mandate credential sharing for MS Teams integration.

**Rejected because:**
- Privacy concerns — some agents may not want to share Teams credentials
- Compliance — some organizations may prohibit credential sharing
- Reduces adoption — friction to use the feature

### 3. No Cross-Channel Updates

Updates from other channels don't appear in Teams.

**Rejected because:**
- Breaks context continuity
- Agents in Teams miss updates from colleagues using other channels
- Creates information silos
- Defeats purpose of chat group as collaboration surface

---

## Consequences

### Positive

1. **Conversation continuity** — Regardless of channel, all updates in one place
2. **Agent choice** — Opt-in credential sharing respects privacy
3. **Clear attribution** — Always know who made the update and from where
4. **Flexibility** — Works with or without credential sharing
5. **Accountability** — Source channel is always indicated

### Negative

1. **Dual appearance** — Same agent may appear both directly and via bot
2. **Credential management** — Need secure storage for shared credentials
3. **User confusion** — Why some messages are from agent vs. bot
4. **Revocation complexity** — Agent must remember to revoke when leaving

### Risks

1. **Credential security** — Shared credentials must be protected
2. **Token expiry** — Need to handle Teams credential refresh
3. **Graph API limits** — Posting on behalf of users may hit rate limits

---

## Implementation Notes

### Credential Sharing

| Aspect | Details |
|--------|---------|
| **Opt-in** | Credential sharing is voluntary per agent |
| **Scope** | Per workbench (agent may share for some workbenches, not others) |
| **Storage** | Credentials stored securely in Cipher IAM |
| **Revocation** | Agent can revoke at any time |

### Source Channel Indicator

All cross-channel updates include the source channel:
- `(Updated via Agent Desk)`
- `(Updated via Mobile App)`
- `(Updated via API)`

This provides transparency even when posting as agent identity.

### Message Formatting

For bot-proxied messages:
- Clear "Update from @Agent" prefix
- Agent @mentioned for notification
- Quoted message content
- Channel indicator

---

## Related Decisions

- [ADR-0033: Chat Groups as Collaboration Surfaces](./0033-chat-groups-as-collaboration-surfaces.md)
- [ADR-0012: Control Plane and Data Plane Channel Separation](./0012-control-plane-data-plane-channel-separation.md)
- [ADR-0011: Persona-Scoped API Channels](./0011-persona-scoped-api-channels.md)

