# ADR-0039: Direct Services Bypass Signal Exchange

| Property       | Value                                           |
|----------------|-------------------------------------------------|
| **Status**     | Accepted                                        |
| **Date**       | 2026-01-06                                      |
| **Category**   | Integration                                     |
| **Deciders**   | Architecture Team                               |
| **Supersedes** | -                                               |

---

## Context

When users interact with MS Teams bots, not all interactions need to create or update Requests. Many are simple queries:

- "What's the status of my dispute?"
- "Show me my open tasks"
- "Search knowledge base for chargeback rules"
- "What can you help me with?"

These read-only queries don't need Signal Exchange's trigger evaluation or request creation capabilities. The question is: Should all messages go through Signal Exchange, or can some bypass it?

---

## Decision

**Direct service queries (status checks, task lists, KB lookups, help) are handled directly by the MS Teams module without involving Signal Exchange. Signal Exchange is reserved for scenario-based request creation and updates.**

### Direct Services Catalog

| Query Type | Example | Service |
|------------|---------|---------|
| **Status check** | "What's the status of DSP-2024-0042?" | Request status lookup |
| **Task list** | "Show me my open tasks" | Task query |
| **Knowledge lookup** | "What's the chargeback time limit?" | Knowledge Bank API |
| **Help** | "What can you help me with?" | Bot help/menu |

### Why Bypass Signal Exchange?

| Reason | Explanation |
|--------|-------------|
| **Efficiency** | No trigger evaluation needed for simple queries |
| **No scenario context** | Queries don't belong to scenarios |
| **Module autonomy** | Each I/O module can add channel-specific optimizations |
| **Channel nuances** | Teams-specific formatting, caching, etc. |

---

## Alternatives Considered

### 1. All Messages Through Signal Exchange

Every user message goes to Signal Exchange for routing.

**Rejected because:**
- Unnecessary overhead for read-only queries
- Trigger evaluation not needed
- No Request context for status queries
- Would slow down simple interactions

### 2. Separate Query Gateway

Create a dedicated query gateway alongside Signal Exchange.

**Rejected because:**
- Adds architectural complexity
- Duplicates some classification logic
- Another component to maintain
- Each I/O module already has direct Hub service access

### 3. Signal Exchange with Query Mode

Add a "query mode" to Signal Exchange for read-only operations.

**Rejected because:**
- Expands SX scope beyond signals and triggers
- Mixes read and write operations
- Different latency requirements
- Better to keep SX focused

---

## Consequences

### Positive

1. **Performance** — Queries return faster without SX overhead
2. **Simplicity** — No trigger evaluation for queries
3. **Channel optimization** — Teams module can cache, format for Teams
4. **SX focus** — Signal Exchange stays focused on request lifecycle
5. **Extensibility** — Direct service catalog can grow independently

### Negative

1. **Two paths** — Debugging needs to consider both paths
2. **Classification accuracy** — Module must correctly identify direct service vs. trigger-worthy
3. **Service duplication** — Some services available in both paths
4. **Consistency** — Need to ensure consistent data across paths

### Risks

1. **Misclassification** — Query classified as trigger-worthy or vice versa
2. **Stale data** — Cached data may be outdated
3. **Feature creep** — Direct services catalog may grow too large

---

## Implementation Notes

### Classification Decision

The MS Teams module classifies messages as:
1. **Structured commands** — `/task`, `/status`, `/kb` → Direct services
2. **NLP-classified queries** — Status/list/help intents → Direct services
3. **Trigger-worthy** — Create/update intents → Forward to Signal Exchange
4. **No match** — Help/menu response

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

## Related Decisions

- [ADR-0035: Two-Stage Message Classification Pipeline](./0035-two-stage-message-classification.md)
- [ADR-0003: Signal Exchange Responsibility Boundaries](./0003-signal-exchange-responsibility-boundaries.md)
- [ADR-0032: Bots as Persona Copilots](./0032-bots-as-persona-copilots.md)

