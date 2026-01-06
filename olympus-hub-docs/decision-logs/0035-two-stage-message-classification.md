# ADR-0035: Two-Stage Message Classification Pipeline

| Property       | Value                                           |
|----------------|-------------------------------------------------|
| **Status**     | Accepted                                        |
| **Date**       | 2026-01-06                                      |
| **Category**   | Integration                                     |
| **Deciders**   | Architecture Team                               |
| **Supersedes** | -                                               |

---

## Context

When a user sends a message to an MS Teams bot, the system needs to determine:

1. What is the user's intent?
2. Should this create/update a Request (Signal Exchange path)?
3. Or is this a direct query that can be handled immediately (Direct Services path)?

The classification responsibility could be:
- Entirely in MS Teams Module
- Entirely in Signal Exchange
- Split between both

---

## Decision

**Message classification is a two-stage pipeline: MS Teams Module performs first-level classification (NLP/structured), then Signal Exchange evaluates triggers for forwarded signals. Signal Exchange does NOT special-case MS Teams — it treats it like any other signal provider.**

### Pipeline Flow

```
User Message (unstructured/NLP/structured)
         │
         ▼
┌─────────────────────────────────────────────────────┐
│            MS TEAMS INTEGRATION MODULE               │
│                                                      │
│   Stage 1: Classification                            │
│   • NLP intent extraction                            │
│   • Structured command matching                      │
│   • May use trigger expectations for classification  │
│                                                      │
│   Decision: Handle Directly? OR Forward?             │
│                                                      │
│   ├─ Direct Services (KB, Status, Help) → Respond   │
│   └─ Trigger-worthy → Translate to Structured Signal │
│                                                      │
└─────────────────────────────────┬───────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────┐
│                  SIGNAL EXCHANGE                     │
│                                                      │
│   Stage 2: Trigger Evaluation                        │
│   • Receives structured signal (CHAT_MESSAGE type)   │
│   • Evaluates triggers (same as any signal provider) │
│   • Creates Request or dispatches update             │
│   • NO special handling for MS Teams source          │
│                                                      │
└─────────────────────────────────────────────────────┘
```

---

## Alternatives Considered

### 1. All Classification in Signal Exchange

MS Teams Module forwards all messages to Signal Exchange.

**Rejected because:**
- Signal Exchange would need NLP/Teams-specific logic
- Direct queries (status, KB) would create unnecessary overhead
- Violates Signal Exchange's focused responsibility
- Every message becomes a "signal" even when not needed

### 2. All Classification in MS Teams Module

MS Teams Module handles trigger evaluation and request creation.

**Rejected because:**
- Duplicates trigger logic already in Signal Exchange
- Signal Exchange's trigger evaluation is consistent across all providers
- Would create special code path for Teams vs. other channels
- Harder to maintain trigger consistency

### 3. Signal Exchange Special-Cases MS Teams

Signal Exchange has MS Teams-specific classification logic.

**Rejected because:**
- Violates principle of uniform signal handling
- Each I/O gateway would request similar special handling
- Complexity grows with channel count
- Testing and debugging becomes channel-specific

---

## Consequences

### Positive

1. **Clear separation** — Module handles Teams-specific; SX handles trigger evaluation
2. **Consistent triggers** — Same trigger logic for Teams as for any signal source
3. **Efficiency** — Direct queries bypass Signal Exchange overhead
4. **Channel autonomy** — Each I/O module can optimize for its channel
5. **Evolvable NLP** — Teams Module can evolve NLP independently

### Negative

1. **Trigger expectations** — Module may need trigger catalog for accurate classification
2. **Two places to debug** — Classification issues could be in either stage
3. **Entity extraction** — Module must extract entities before SX sees them
4. **Evolution coordination** — NLP and trigger changes need coordination

### Risks

1. **Classification accuracy** — First stage may misclassify trigger-worthy messages
2. **Sync drift** — Module's trigger expectations may drift from actual triggers
3. **NLP complexity** — Building accurate intent classification is non-trivial

---

## Implementation Notes

### Direct Services Catalog

Messages handled directly without Signal Exchange:
- Request status queries
- Task list queries
- Knowledge base lookups
- Help/menu requests
- Other read-only interactions

### Signal Structure for Forwarded Messages

```json
{
  "signal_type": "CHAT_MESSAGE",
  "source": {
    "gateway": "ms-teams-integration",
    "bot": "dispute-ops-ask-bot",
    "workbench": "dispute-operations"
  },
  "payload": {
    "raw_message": "I need to dispute transaction #12345",
    "extracted_entities": {
      "transaction_id": "12345",
      "intent": "dispute_initiation"
    }
  },
  "metadata": {
    "channel": "MS_TEAMS",
    "classification_confidence": 0.94
  }
}
```

### Evolution Path

| Phase | Classification Approach |
|-------|------------------------|
| **Initial** | Structured commands + basic NLP |
| **Evolved** | Full NLP with GenAI understanding |
| **Target** | Conversational with context awareness |

---

## Related Decisions

- [ADR-0001: Signal Normalization](./0001-signal-normalization.md)
- [ADR-0003: Signal Exchange Responsibility Boundaries](./0003-signal-exchange-responsibility-boundaries.md)
- [ADR-0032: Bots as Persona Copilots](./0032-bots-as-persona-copilots.md)

