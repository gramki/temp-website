# Conversation-Based Work

Conversation-based work unfolds through dialogue — questions and answers, proposals and responses, clarifications and decisions — in real-time or near-real-time exchanges. The work progresses through communication.

---

## What Is Conversation-Based Work?

In conversation-based work, the primary medium is dialogue. Participants exchange messages to understand a situation, explore options, and reach resolution. The conversation itself is the work.

### Characteristics

| Dimension | Description |
|-----------|-------------|
| **Medium** | Dialogue (chat, voice, video) |
| **Pace** | Real-time or near-real-time |
| **Agents** | Two or more in active exchange |
| **Duration** | Minutes to hours per session |
| **Goal** | Resolution through understanding |

### Examples

- Customer support chat
- Technical troubleshooting
- Sales qualification
- Expert consultation
- Onboarding guidance
- Interview and assessment
- Collaborative problem-solving

---

## Anatomy of Conversation-Based Work

### Conversation Flow

```
1. Opening
   Context established, participants introduced
        ↓
2. Exploration
   Questions asked, information exchanged
        ↓
3. Clarification
   Misunderstandings addressed, details refined
        ↓
4. Resolution
   Answer provided, decision made, or handoff arranged
        ↓
5. Closing
   Summary, next steps, satisfaction check
```

### Participant Roles

| Role | Responsibility |
|------|----------------|
| **Initiator** | Starts the conversation (often customer/user) |
| **Responder** | Provides information, guidance, decisions |
| **Observer** | Monitors, may escalate or intervene |
| **Specialist** | Joins for specific expertise |

### Conversation Context

| Element | Purpose |
|---------|---------|
| **Transcript** | Record of the exchange |
| **Participant Identity** | Who is involved |
| **Topic/Intent** | What the conversation is about |
| **History** | Previous conversations if any |
| **Resolution** | Outcome of the conversation |

---

## Synchronous vs. Asynchronous

| Mode | Characteristics | Examples |
|------|-----------------|----------|
| **Synchronous** | Real-time, immediate responses | Chat, voice, video |
| **Asynchronous** | Delayed responses, persistent thread | Email, ticket comments, forum |
| **Hybrid** | Mix of both | Chat that continues via email |

Hub supports all modes — the conversation is modeled the same way, with different timing expectations.

---

## Multi-Party Conversations

Some conversations involve more than two participants:

| Pattern | Description |
|---------|-------------|
| **Handoff** | One agent transfers to another |
| **Conference** | Multiple agents join simultaneously |
| **Escalation** | Supervisor or specialist added |
| **Observation** | Others monitor without participating |

---

## Conversation Outcomes

| Outcome | Description |
|---------|-------------|
| **Resolved** | Question answered, problem solved |
| **Transferred** | Handed off to another agent/channel |
| **Escalated** | Elevated for higher expertise/authority |
| **Deferred** | Follow-up scheduled |
| **Abandoned** | Conversation ended without resolution |

---

## Mapping to Hub Ontology

| Work Pattern Concept | Hub Ontology Concept |
|----------------------|----------------------|
| Conversation start | Signal (initiator's message) |
| Conversation type | Scenario |
| Conversation instance | Request |
| Message (inbound) | Signal |
| Message (outbound) | Action |
| Participant | Agent |
| Conversation goal | Scenario Goal |
| Resolution | Request completion |
| Transcript | Request history |

### How Hub Models Conversation-Based Work

```
Signal (conversation initiated)
    ↓
Trigger (matches conversation type)
    ↓
Scenario (defines conversation handling)
    ↓
Request (conversation instance)
    ↓
Messages flow as Signals and Actions
    ↓
Agents respond to Signals
    ↓
Conversation progresses
    ↓
Resolution reached
    ↓
Request completes
```

### Why Conversation-Based Work Suits Hub

| Hub Concept | Why It Fits |
|-------------|-------------|
| **Signal as message** | Each message is a Signal that can trigger action |
| **Request as conversation** | Request tracks the entire exchange |
| **Agent participation** | Human and AI agents participate the same way |
| **Multi-channel** | Same conversation can span chat, voice, email |
| **Memory** | Conversation history persists |

---

## AI in Conversations

Conversation-based work is a natural fit for AI agents:

| Role | AI Contribution |
|------|-----------------|
| **First responder** | Handle initial contact, gather information |
| **Classifier** | Determine intent, route appropriately |
| **Assistant** | Help human agent with suggestions, lookups |
| **Resolver** | Handle routine requests autonomously |
| **Observer** | Monitor for quality, compliance |

Hub + Seer enables governed AI participation in conversations with appropriate oversight and escalation.

---

## Related

- [Ontology: Signal](../01-concepts/ontology-1-perception-layer.md#signal)
- [Ontology: Agent](../01-concepts/ontology-3-execution-layer.md#agent)
- [Case-Based Work](./case-based-work.md) — Complex conversations may become cases
- [Queue-Based Work](./queue-based-work.md) — Conversations often start from queue
