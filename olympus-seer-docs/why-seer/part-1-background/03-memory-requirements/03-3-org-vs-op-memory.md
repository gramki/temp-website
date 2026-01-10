# 3.3 Organizational vs. Operational Memory

*Distinguishing between what the institution knows and what agents need in-flight.*

---

## Purpose

This subsection establishes the critical distinction between organizational memory (long-lived, cross-agent, governance-intensive) and operational memory (session-scoped, agent-local, governance-light). This distinction determines data governance boundaries, retention policies, and the pathways through which learning becomes institutional knowledge.

Many enterprise agent failures stem from conflating these two memory scopes—either by treating operational memory as permanent record (creating governance liability) or by burdening in-flight operations with enterprise memory governance (creating performance problems).

---

## Core Concepts & Definitions

### Organizational Memory (Enterprise Memory)

**Definition**: Organizational memory is the durable cognitive record of the enterprise—decisions made, patterns learned, knowledge accumulated—that persists across agents, sessions, and time.

| Attribute | Description |
|-----------|-------------|
| **Scope** | Organizational—cross-agent, cross-session |
| **Lifetime** | Years to decades (7+ years for regulated records) |
| **Persistence** | Durable, replicated, backed up |
| **Governance** | Full—retention policies, legal holds, access controls |
| **PII Policy** | Prohibited—entity references only |
| **Mutability** | Immutable for episodic; confidence-updatable for semantic |

**What it contains**:
- Decision records with full rationale and context
- Outcome records linking decisions to results
- Override records documenting human intervention
- Learned patterns and institutional beliefs
- Evidence bundles for regulatory response

**Who accesses it**:
- Agents (read-only, via governed access tools)
- Auditors (for compliance inquiries)
- Compliance systems (for pattern detection)
- Learning services (for promotion workflows)

### Operational Memory (Agent Memory)

**Definition**: Operational memory is the session-scoped working state that agents use to maintain continuity during in-flight operations.

| Attribute | Description |
|-----------|-------------|
| **Scope** | Request/session—individual agent |
| **Lifetime** | Session duration + short retention (hours to days) |
| **Persistence** | Session store, short-term durability |
| **Governance** | Minimal—agent-scoped isolation, short retention |
| **PII Policy** | Permitted—within session scope |
| **Mutability** | Fully mutable—updates and deletes allowed |

**What it contains**:
- Conversation history (recent turns)
- Extracted entities from current session
- Tool outputs and intermediate results
- Working hypotheses (not yet validated)
- User preferences observed in session

**Who accesses it**:
- The agent itself (primary consumer)
- Seer context assembly (for prompt compilation)
- Session replay systems (for debugging)

---

## Why the Distinction Matters

### Governance Boundaries

Organizational and operational memory carry fundamentally different governance obligations:

| Dimension | Organizational Memory | Operational Memory |
|-----------|----------------------|-------------------|
| **Retention regulation** | OCC SR 11-7, EU AI Act | None specific |
| **Right to erasure** | Complex—must preserve audit integrity | Simple—delete on request |
| **Access control** | Role-based, scenario-scoped | Agent-specific |
| **Encryption** | Platform-level | Application-layer, session-keyed |
| **Legal holds** | Supported | Not applicable |

Organizations that fail to distinguish these scopes face two classes of risk:

1. **Over-retention risk**: Treating operational memory as organizational creates liability. Session-scoped PII that should expire in hours instead persists for years.

2. **Under-retention risk**: Treating significant decisions as operational means losing audit evidence. When regulators ask about a 2024 decision, the organization cannot answer.

### Performance Implications

Organizational memory governance creates overhead:

- Writes routed through governance services (not direct database access)
- Schema validation enforced on every record
- Immutability constraints prevent efficient updates
- Long retention increases storage costs

Imposing this overhead on every in-session operation would degrade agent responsiveness. Operational memory exists specifically to support low-latency operations without enterprise governance overhead.

### Learning Pathways

The organizational/operational distinction defines how learning happens:

```
Operational Memory (session-scoped)
        │
        │ Developer identifies cross-session value
        │ (explicit decision, not automatic)
        ▼
Organizational Memory (enterprise-scoped)
        │
        │ Pattern detection, validation
        ▼
Enterprise Knowledge (authoritative)
```

Key principle: **Operational memory cannot automatically become organizational memory.** The transition requires explicit developer action and governance review. This prevents session noise from polluting institutional records.

---

## Comparison Table

| Aspect | Organizational Memory | Operational Memory |
|--------|----------------------|-------------------|
| **Also called** | Enterprise Memory | Agent Memory |
| **Scope** | Cross-agent, cross-session | Per-agent, per-session |
| **Retention** | 7+ years (episodic) | Session + hours/days |
| **PII** | Prohibited (entity refs only) | Permitted |
| **Write path** | Via governance services | Direct SDK access |
| **Read path** | Via access tools | SDK methods, context assembly |
| **Immutability** | Required for episodic | Not required |
| **ESPP enforcement** | Mandatory | Optional |
| **Storage backend** | Enterprise-grade (managed services) | Session-optimized (mixed) |
| **Cross-agent sharing** | Yes | No |
| **Legal hold support** | Yes | No |

---

## When to Use Each

### Use Organizational Memory For:

| Use Case | Example |
|----------|---------|
| **Audit-relevant decisions** | "Agent approved this refund because..." |
| **Regulatory evidence** | "At decision time, the agent knew X, Y, Z" |
| **Institutional learning** | "Customers with pattern A have 3x dispute rate" |
| **Cross-agent precedent** | "Similar cases were resolved by..." |
| **Handoff context** | "Previous agent found these facts..." |

### Use Operational Memory For:

| Use Case | Example |
|----------|---------|
| **Conversation continuity** | "User mentioned their account number earlier" |
| **Session preferences** | "User prefers concise responses" |
| **Working hypotheses** | "Likely fraud based on current signals" |
| **Tool outputs** | "API call returned these results" |
| **Entity extraction** | "Customer name is..." (PII allowed) |

### Red Flags: Wrong Memory Type

| Signal | Problem | Fix |
|--------|---------|-----|
| PII in 7-year records | Operational data in organizational store | Use entity references; resolve at query time |
| Session data filling enterprise store | Over-retention | Review salience detection; tighten capture criteria |
| Decisions without audit trail | Under-retention | Ensure decision points write to organizational memory |
| Governance delays on every turn | Wrong scope | Move operational data to agent memory |

---

## Implementation Patterns

### Write Path Separation

Organizational and operational memory use different write paths:

**Organizational Memory**:
```
Agent/Application
    │
    │ Adds memory records to request
    ▼
Governance Services (Signal Exchange)
    │
    │ Validates, enriches, routes
    ▼
Enterprise Memory Store
```

**Operational Memory**:
```
Agent
    │
    │ Direct SDK call
    ▼
Agent Memory Store
```

The indirection in the organizational path is intentional—it ensures governance controls are applied uniformly without requiring every application to implement them.

### Read Path Differences

**Organizational Memory**:
- Access via governed tools (not raw database queries)
- Role-based access control enforced
- Scenario-scoped visibility

**Operational Memory**:
- Access via SDK methods
- Agent-scoped isolation (each agent sees only its own data)
- Session-scoped isolation (each session is separate)

---

## Common Misconceptions

### Misconception 1: "Just Store Everything in Enterprise Memory"

**The error**: Capture every agent interaction in enterprise-grade storage for completeness.

**Why it fails**: Creates massive governance liability (PII in long-retained records), performance problems (every interaction through governance services), and storage cost explosion.

**The fix**: Apply salience detection. Only decisions, outcomes, and governance-relevant events belong in organizational memory.

### Misconception 2: "Operational Memory Is Unimportant"

**The error**: Focus governance attention only on organizational memory.

**Why it fails**: Operational memory may contain PII, may influence decisions (and thus require audit explanation), and may create security exposure if not properly isolated.

**The fix**: Govern operational memory appropriately—isolation, encryption, short retention, session-scoped access—even if less intensively than organizational memory.

### Misconception 3: "Promotion Should Be Automatic"

**The error**: Automatically copy patterns from operational to organizational memory when thresholds are met.

**Why it fails**: Automatic promotion creates silent institutional learning without human oversight. Patterns may be spurious, biased, or domain-inappropriate.

**The fix**: Require explicit developer decision to promote from operational to organizational scope. Validate before institutional adoption.

---

## Practical Implications

### For Enterprise Architects

1. Design separate storage architectures for each memory scope
2. Implement different governance controls appropriate to each
3. Define clear criteria for what triggers organizational memory writes
4. Plan promotion workflows with explicit governance gates

### For Agent Developers

1. Default to operational memory for session data
2. Write to organizational memory only for audit-relevant events
3. Never include raw PII in organizational memory records
4. Design agents to work correctly if operational memory is cleared

### For Compliance Officers

1. Audit organizational memory governance controls
2. Verify that PII is not leaking into long-retained records
3. Review promotion pathways for appropriate oversight
4. Ensure operational memory retention aligns with data minimization requirements

---

## Cross-References

- **Section 3.2**: ESPP taxonomy applies to both scopes but is enforced only in organizational memory
- **Section 3.4**: Governance imperatives apply primarily to organizational memory
- **Section 3.5**: The learning imperative describes promotion from operational to organizational scope
- **Part 2, Section 4**: How Seer and Hub implement both memory scopes

For implementation details, see:
- `olympus-hub-docs/04-subsystems/memory-services/README.md` — Memory Services overview
- `olympus-hub-docs/04-subsystems/memory-services/enterprise-memory/README.md` — Organizational memory
- `olympus-hub-docs/04-subsystems/memory-services/agent-memory/README.md` — Operational memory

---

*Organizational memory is the institution's cognitive record. Operational memory is the agent's working state. Conflating them creates either governance liability or operational burden.*
