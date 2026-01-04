# Message Flow

> **Status:** 🟡 WIP

This document details how messages flow between MS Teams and Hub, including signal routing, direct services, and response handling.

---

## Overview

MS Teams messages flow through a **classification pipeline** across modules:

1. **MS Teams Module** — First, classifies and optionally handles directly
2. **Signal Exchange** — Second, evaluates triggers for forwarded signals

| Path | When Used | Example |
|------|-----------|---------|
| **Signal Exchange Path** | Message triggers a scenario | "I need to dispute transaction #12345" |
| **Direct Services Path** | Query/action doesn't need a request | "What's the status of my dispute?" |

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       MESSAGE CLASSIFICATION PIPELINE                        │
│                                                                              │
│   User Message (unstructured/NLP/structured)                                 │
│         │                                                                    │
│         ▼                                                                    │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                  MS TEAMS INTEGRATION MODULE                         │   │
│   │                                                                      │   │
│   │   ┌─────────────────────────────────────────────────────────────┐   │   │
│   │   │              CLASSIFICATION (Module Layer)                   │   │   │
│   │   │  • NLP intent extraction                                     │   │   │
│   │   │  • Structured command matching                               │   │   │
│   │   │  • May use trigger expectations for classification           │   │   │
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

**Key Points:**
- Teams Module does **first-level classification** (NLP, intent extraction)
- Signal Exchange does **trigger evaluation** (as for any signal provider)
- Signal Exchange does NOT short-circuit its logic for MS Teams — it treats it like any other source

---

## Signal Exchange Path

### Flow: Request Initiation

When a Business Employee's message is classified as trigger-worthy:

```
Business Employee           Ask_Bot           MS Teams Module         Signal Exchange         Hub App
       │                       │                    │                       │                   │
       │ ── "Dispute txn ────> │                    │                       │                   │
       │     #12345"           │                    │                       │                   │
       │                       │ ── Forward ──────> │                       │                   │
       │                       │                    │                       │                   │
       │                       │                    │ ── Classify (NLP) ──> │                   │
       │                       │                    │    Extract entities   │                   │
       │                       │                    │    transaction=12345  │                   │
       │                       │                    │    intent=dispute     │                   │
       │                       │                    │                       │                   │
       │                       │                    │ ── Structured Signal ─────────────────>   │
       │                       │                    │    type: CHAT_MESSAGE │                   │
       │                       │                    │                       │                   │
       │                       │                    │                       │ ── Evaluate ────> │
       │                       │                    │                       │    Triggers       │
       │                       │                    │                       │    (standard)     │
       │                       │                    │                       │                   │
       │                       │                    │                       │ ── Create ──────> │
       │                       │                    │                       │    Request        │
       │                       │                    │                       │                   │
       │                       │                    │                       │ ── Dispatch ────> │
       │                       │                    │                       │    to Hub App     │
       │                       │                    │                       │                   │
       │                       │                    │ <── Request Created ─ │                   │
       │                       │                    │     DSP-2024-0042     │                   │
       │                       │                    │                       │                   │
       │ <── "Created dispute ─┤ <── Response ───── │                       │                   │
       │      DSP-2024-0042"   │                    │                       │                   │
       │                       │                    │                       │                   │
```

**Note:** The MS Teams Module performs NLP classification and translation to structured signal. Signal Exchange then evaluates triggers as it would for any signal provider — it does not special-case MS Teams.

### Signal Structure

The MS Teams module transforms messages into Hub signals:

```json
{
  "signal_type": "CHAT_MESSAGE",
  "source": {
    "gateway": "ms-teams-integration",
    "bot": "dispute-ops-ask-bot",
    "workbench": "dispute-operations"
  },
  "originator": {
    "type": "BUSINESS_EMPLOYEE",
    "identity": {
      "teams_id": "alice@contoso.com",
      "cipher_id": "usr-12345"
    }
  },
  "payload": {
    "raw_message": "I need to dispute transaction #12345",
    "extracted_entities": {
      "transaction_id": "12345",
      "intent": "dispute_initiation"
    },
    "conversation_context": {
      "thread_id": "19:abc123...",
      "timestamp": "2024-01-15T14:34:00Z"
    }
  },
  "metadata": {
    "channel": "MS_TEAMS",
    "classification_confidence": 0.94
  }
}
```

### Flow: Request Updates from Chat Group

When an Agent posts in a request chat group:

```
Agent (in group)       MS Teams Module         Signal Exchange         Request Store
       │                     │                       │                       │
       │ ── "Confirmed ────> │                       │                       │
       │     fraud pattern"  │                       │                       │
       │                     │                       │                       │
       │                     │ ── ASYNC_UPDATE ────> │                       │
       │                     │    type: MEMO         │                       │
       │                     │    request_id: DSP-.. │                       │
       │                     │                       │                       │
       │                     │                       │ ── Record Update ───> │
       │                     │                       │                       │
       │                     │                       │                       │
       │                     │                       │ ── Dispatch to ─────> │ Notify
       │                     │                       │    all watchers       │ watchers
       │                     │                       │                       │
```

---

## Direct Services Path

### When to Use Direct Services

Messages that don't create or update requests:

| Query Type | Example | Service |
|------------|---------|---------|
| **Status check** | "What's the status of DSP-2024-0042?" | Request status lookup |
| **Task list** | "Show me my open tasks" | Task query |
| **Knowledge lookup** | "What's the chargeback time limit?" | Knowledge Bank |
| **Help** | "What can you help me with?" | Bot help/menu |

### Flow: Direct Service Query

```
Agent                   Me_Bot           MS Teams Module         Hub Services
  │                       │                    │                       │
  │ ── "What's the ─────> │                    │                       │
  │     status of         │                    │                       │
  │     DSP-2024-0042?"   │                    │                       │
  │                       │ ── Forward ──────> │                       │
  │                       │                    │                       │
  │                       │                    │ ── Classify ────────> │
  │                       │                    │    → Status Query      │
  │                       │                    │                       │
  │                       │                    │ ── Direct Call ─────> │
  │                       │                    │    GET /requests/     │
  │                       │                    │    DSP-2024-0042      │
  │                       │                    │                       │
  │                       │                    │ <── Response ──────── │
  │                       │                    │                       │
  │ <── "DSP-2024-0042 ── │ <── Response ───── │                       │
  │      is Active.       │                    │                       │
  │      2 tasks pending" │                    │                       │
  │                       │                    │                       │
```

### Why Bypass Signal Exchange?

| Reason | Explanation |
|--------|-------------|
| **Efficiency** | No trigger evaluation needed for simple queries |
| **No scenario context** | Queries don't belong to scenarios |
| **Module autonomy** | Each I/O module can add value-specific optimizations |
| **Channel nuances** | Teams-specific formatting, caching, etc. |

### Service Catalog

| Service | Capability | Notes |
|---------|------------|-------|
| **Request Status** | Query by ID, list by user | Full status + tasks |
| **Task List** | My tasks, filtered views | Supports pagination |
| **Knowledge Base** | Search, retrieve | Uses Knowledge Bank API |
| **Help/Menu** | Bot capabilities | Bot-specific |

---

## Message Classification

### Classification Pipeline (Two-Stage)

The classification is a **pipeline across modules**:

| Stage | Module | Responsibility |
|-------|--------|----------------|
| **1** | MS Teams Module | NLP/structured classification, decide handle vs. forward |
| **2** | Signal Exchange | Trigger evaluation for forwarded signals |

### Stage 1: MS Teams Module Classification

```
┌─────────────────────────────────────────────────────────────────┐
│               MS TEAMS MODULE CLASSIFICATION                     │
│                                                                  │
│   Incoming Message                                               │
│         │                                                        │
│         ▼                                                        │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │              STRUCTURED COMMAND CHECK                    │   │
│   │                                                          │   │
│   │   Does message match: /task, /status, /kb, etc.?        │   │
│   │                                                          │   │
│   └───────────────────────┬─────────────────────────────────┘   │
│                           │                                      │
│              ┌────────────┴────────────┐                        │
│              │ Yes                     │ No                     │
│              ▼                         ▼                        │
│   ┌─────────────────┐       ┌─────────────────────────────┐    │
│   │ Execute command │       │     NLP CLASSIFICATION      │    │
│   │ directly        │       │  (may use trigger           │    │
│   └─────────────────┘       │   expectations)             │    │
│                             │  Intent + Entity extraction │    │
│                             │                             │    │
│                             └──────────────┬──────────────┘    │
│                                            │                    │
│                              ┌─────────────┴─────────────┐     │
│                              │                           │     │
│                       Trigger-worthy?           Service Query?  │
│                              │                           │     │
│                              ▼                           ▼     │
│                    ┌─────────────────┐       ┌─────────────┐   │
│                    │ Translate to    │       │ Direct      │   │
│                    │ Structured      │       │ Service     │   │
│                    │ Signal → Send   │       │             │   │
│                    │ to Signal Exch. │       │             │   │
│                    └─────────────────┘       └─────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Stage 2: Signal Exchange Trigger Evaluation

Signal Exchange receives structured signals and evaluates triggers **as it would for any signal provider**. It does NOT short-circuit or special-case MS Teams signals.

### Why Does Module Need Trigger Expectations?

To perform accurate NLP classification, the module may need to understand what triggers exist in the workbench. This helps it:
- Extract relevant entities
- Determine if a message is likely to match a trigger
- Format the structured signal appropriately

This is an implementation concern and may evolve.

### Evolution Path

| Phase | Classification |
|-------|---------------|
| **Initial** | Structured commands + basic NLP |
| **Evolved** | Full NLP with GenAI understanding |
| **Target** | Conversational with context awareness |

### No Match Handling

When no trigger matches and no direct service applies:

```
┌─────────────────────────────────────────────────────────────────┐
│ [Ask_Bot] — 2:34 PM                                             │
│                                                                  │
│ I'm not sure how to help with that. Here's what I can do:       │
│                                                                  │
│ 📋 **Create Requests**                                           │
│    Tell me about disputes, complaints, or service issues         │
│                                                                  │
│ 🔍 **Check Status**                                              │
│    Ask about your existing requests or tasks                     │
│                                                                  │
│ 📚 **Knowledge Base**                                            │
│    Search for policies, procedures, or FAQs                      │
│                                                                  │
│ Type `/help` for more options.                                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Response Handling

### Request Creation Response

When Signal Exchange creates a request:

```json
{
  "response_type": "REQUEST_CREATED",
  "request_id": "DSP-2024-0042",
  "scenario": "Dispute Resolution",
  "chat_group": {
    "created": true,
    "group_id": "19:xyz789..."
  },
  "acknowledgment": {
    "message": "I've created dispute case DSP-2024-0042 for transaction #12345.",
    "next_steps": "You'll be added to a group chat for updates."
  }
}
```

### Teams Message Formatting

The module transforms responses into rich Teams messages:

```
┌─────────────────────────────────────────────────────────────────┐
│ [Ask_Bot] — 2:34 PM                                             │
│                                                                  │
│ ✅ **Dispute Case Created**                                      │
│                                                                  │
│ 📋 **Case ID:** DSP-2024-0042                                    │
│ 💳 **Transaction:** #12345                                       │
│ 📊 **Status:** Active                                            │
│                                                                  │
│ You've been added to a group chat where you can track progress  │
│ and communicate with the team working on your case.             │
│                                                                  │
│ ───────────────────────────────────────────                     │
│ [View Details] [Check Status]                                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Update Relay

### Hub → Teams Flow

When a Hub Application sends a Request Update (e.g., task assignment), Signal Exchange dispatches it to **registered observers** (not to agents directly). The MS Teams module, as an observer, determines which agents to notify:

```
Hub Application         Signal Exchange         MS Teams Module         Chat Group
       │                       │                       │                     │
       │ ── Request Update ──> │                       │                     │
       │    (Task Assigned     │                       │                     │
       │     to Agent Bob)     │                       │                     │
       │                       │                       │                     │
       │                       │ ── Dispatch to ─────> │                     │
       │                       │    Observers          │                     │
       │                       │    (Request-level)    │                     │
       │                       │                       │                     │
       │                       │                       │ ── Determine ─────> │
       │                       │                       │    affected agents  │
       │                       │                       │    (Bob in this     │
       │                       │                       │    case)            │
       │                       │                       │                     │
       │                       │                       │ ── Add Bob to ────> │
       │                       │                       │    group via        │
       │                       │                       │    Graph API        │
       │                       │                       │                     │
       │                       │                       │ ── Post Message ──> │
       │                       │                       │    "Task assigned   │
       │                       │                       │     to @Bob"        │
       │                       │                       │                     │
```

**Key Point:** Signal Exchange dispatches Request Updates to observers (like MS Teams module). It does NOT dispatch to agents or tasks directly. The MS Teams module parses the update content to determine which agents are affected and takes appropriate action.

### Update Types and Formatting

| Update Type | Teams Rendering |
|-------------|-----------------|
| `TASK_LIFECYCLE` | Assignment, completion, escalation cards |
| `DECISION` | Decision card with summary |
| `THOUGHT` | Quote block with author |
| `MEMO` | Note with context |
| `PROGRESS` | Progress indicator |
| `MILESTONE` | Milestone completion card |
| `STATUS_CHANGE` | Status badge update |

### Cross-Channel Update Attribution

When an agent makes an update through a **different channel** (e.g., Agent Desk, Mobile), the MS Teams module relays it to the chat group with appropriate attribution:

| Condition | Attribution |
|-----------|-------------|
| Agent shared Teams credentials | Posted **as the agent** (their Teams identity) |
| No credential sharing | Posted **by Group Orchestration Bot** with on-behalf-of attribution |

**With credentials:**
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

See [Chat Group Lifecycle - Cross-Channel Update Relay](./chat-group-lifecycle.md#cross-channel-update-relay) for configuration details.

---

## Error Handling

### Classification Errors

| Error | Handling |
|-------|----------|
| Low confidence | Ask for clarification |
| Ambiguous intent | Present options |
| Service unavailable | Graceful error message |

### Signal Exchange Errors

| Error | Handling |
|-------|----------|
| Trigger evaluation failed | Log, return user-friendly error |
| Request creation failed | Explain issue, suggest retry |
| Dispatch failed | Queue for retry, notify if persistent |

### Example Error Response

```
┌─────────────────────────────────────────────────────────────────┐
│ [Ask_Bot] — 2:34 PM                                             │
│                                                                  │
│ ⚠️ **Unable to Process Request**                                 │
│                                                                  │
│ I encountered an issue while creating your dispute case.        │
│ This has been logged and our team is looking into it.           │
│                                                                  │
│ **What you can do:**                                             │
│ • Try again in a few minutes                                    │
│ • Use the Hub portal: hub.contoso.com/disputes                  │
│ • Contact support: support@contoso.com                          │
│                                                                  │
│ Error reference: ERR-2024-0042-XYZ                              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Performance Considerations

### Latency Targets

| Path | Target | Notes |
|------|--------|-------|
| Direct services | < 500ms | Cached where possible |
| Signal Exchange (trigger eval) | < 1s | Depends on trigger complexity |
| Request creation | < 2s | Full scenario initialization |

### Caching Strategy

| Data | Cache Duration | Invalidation |
|------|----------------|--------------|
| User identity/permissions | 5 minutes | On permission change |
| Knowledge base results | 1 hour | On content update |
| Task list | 30 seconds | On task change |
| Request status | 30 seconds | On status change |

---

## Related Documentation

- [Bot Architecture](./bot-architecture.md) — Bot types and capabilities
- [Chat Group Lifecycle](./chat-group-lifecycle.md) — Group management
- [Signal Exchange](../signal-exchange/README.md) — Request routing
- [Heracles Gateway](../signal-providers/heracles-api-gateway.md) — Underlying HTTP layer

---

*Last updated: 2026-01-05*

