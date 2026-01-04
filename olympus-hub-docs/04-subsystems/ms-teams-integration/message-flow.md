# Message Flow

> **Status:** 🟡 WIP

This document details how messages flow between MS Teams and Hub, including signal routing, direct services, and response handling.

---

## Overview

MS Teams messages take one of two paths:

| Path | When Used | Example |
|------|-----------|---------|
| **Signal Exchange Path** | Message triggers a scenario | "I need to dispute transaction #12345" |
| **Direct Services Path** | Query/action doesn't need a request | "What's the status of my dispute?" |

```
┌─────────────────────────────────────────────────────────────────┐
│                       MESSAGE ROUTING                            │
│                                                                  │
│   Incoming Message                                               │
│         │                                                        │
│         ▼                                                        │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │               MS TEAMS INTEGRATION MODULE                │   │
│   │                                                          │   │
│   │   ┌───────────────────────────────────────────────────┐ │   │
│   │   │              MESSAGE CLASSIFIER                    │ │   │
│   │   │         (NLP + Structured Commands)                │ │   │
│   │   └───────────────────────┬───────────────────────────┘ │   │
│   │                           │                              │   │
│   │             ┌─────────────┴─────────────┐               │   │
│   │             │                           │               │   │
│   │      Trigger Match?              Direct Service?         │   │
│   │             │                           │               │   │
│   │             ▼                           ▼               │   │
│   │   ┌─────────────────┐         ┌─────────────────┐       │   │
│   │   │ Signal Exchange │         │ Hub Services    │       │   │
│   │   │ Path            │         │ Path            │       │   │
│   │   └─────────────────┘         └─────────────────┘       │   │
│   │                                                          │   │
│   └──────────────────────────────────────────────────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Signal Exchange Path

### Flow: Request Initiation

When a Business Employee's message matches a trigger:

```
Business Employee           Ask_Bot           MS Teams Module         Signal Exchange         Hub App
       │                       │                    │                       │                   │
       │ ── "Dispute txn ────> │                    │                       │                   │
       │     #12345"           │                    │                       │                   │
       │                       │ ── Forward ──────> │                       │                   │
       │                       │                    │                       │                   │
       │                       │                    │ ── Classify ────────> │                   │
       │                       │                    │    (NLP/Structured)   │                   │
       │                       │                    │                       │                   │
       │                       │                    │ <── Match: Dispute ── │                   │
       │                       │                    │     Scenario          │                   │
       │                       │                    │                       │                   │
       │                       │                    │ ── Signal ──────────> │                   │
       │                       │                    │    (Chat-Message)     │                   │
       │                       │                    │                       │                   │
       │                       │                    │                       │ ── Evaluate ────> │
       │                       │                    │                       │    Triggers       │
       │                       │                    │                       │                   │
       │                       │                    │                       │ <── Create ────── │
       │                       │                    │                       │     Request       │
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

### Classification Approach

```
┌─────────────────────────────────────────────────────────────────┐
│                    MESSAGE CLASSIFICATION                        │
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
│   │ directly        │       │                             │    │
│   └─────────────────┘       │  Intent + Entity extraction │    │
│                             │                             │    │
│                             └──────────────┬──────────────┘    │
│                                            │                    │
│                              ┌─────────────┴─────────────┐     │
│                              │                           │     │
│                       Trigger Match?              Service Query? │
│                              │                           │     │
│                              ▼                           ▼     │
│                    ┌─────────────────┐       ┌─────────────┐   │
│                    │ Signal Exchange │       │ Direct      │   │
│                    │ Path            │       │ Service     │   │
│                    └─────────────────┘       └─────────────┘   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

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

When Signal Exchange dispatches updates to watchers:

```
Hub Application         Signal Exchange         MS Teams Module         Chat Group
       │                       │                       │                     │
       │ ── Task Assigned ───> │                       │                     │
       │    to Agent Bob       │                       │                     │
       │                       │                       │                     │
       │                       │ ── Dispatch Update ─> │                     │
       │                       │    (to all watchers)  │                     │
       │                       │                       │                     │
       │                       │                       │ ── Add Bob to ────> │
       │                       │                       │    group            │
       │                       │                       │                     │
       │                       │                       │ ── Post Message ──> │
       │                       │                       │    "Task assigned   │
       │                       │                       │     to @Bob"        │
       │                       │                       │                     │
```

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

