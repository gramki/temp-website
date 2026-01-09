# ADR-0056: CAF Episodic Memory Scope and Case Record

## Status

**Accepted**

## Date

2026-01-07

## Context

The CAF record types defined (Decision, Evidence, Outcome, etc.) are all **event-based, time-ordered, case-bound** records. This is the definition of **Episodic Memory** in cognitive science.

Questions arose:
1. Should we have a Case Record as the root anchor?
2. Should we explicitly qualify this scope?
3. What about other memory types (Semantic, Procedural, Preference)?

## Decision

### 1. Explicit Episodic Memory Scope

CAF's current record taxonomy and Memory Store Contract are explicitly scoped to **Episodic Memory**:

| Memory Class | Characteristics | CAF Status |
|--------------|-----------------|------------|
| **Episodic** | Event-based, time-ordered, case-bound | ✅ Defined |
| Semantic | Facts, entities, relationships | 🔴 Future |
| Procedural | Skills, patterns, procedures | 🔴 Future |
| Preference | User/agent preferences | 🔴 Future |

### 2. Case Record as Root Anchor

All episodic records reference a `case_id`. The **Case Record** is what that ID resolves to:

```yaml
case_id: uuid                    # Primary identifier
case_type: string                # e.g., fraud_investigation
status: enum                     # open → in_progress → resolved → closed
created_at: datetime
actors: [actor]                  # All actors involved
resolution: object               # Final outcome
hub_metadata: object             # Optional Hub context
```

### 3. Episodic Record Types (9 Total)

| # | Record Type | Purpose |
|---|-------------|---------|
| 1 | **Case Record** | Root anchor, lifecycle, resolution |
| 2 | Decision Record | Decision with rationale |
| 3 | Evidence Bundle | Context at decision time |
| 4 | Context Snapshot | Compiled context per turn |
| 5 | Outcome Record | Post-decision outcomes |
| 6 | Override Record | Manual override documentation |
| 7 | Handoff Context | State transfer between agents |
| 8 | Incident Timeline | Chronological event sequence |
| 9 | Hypothesis Record | Learned patterns (bridge to Semantic) |

### 4. Hypothesis as Bridge

`HypothesisRecord` is unique—it starts in Episodic Memory but can be **promoted** to:
- **Semantic Memory** → becomes a Fact or Entity
- **Procedural Memory** → becomes a Skill or Pattern

This promotion workflow will be defined separately.

### 5. Future Memory Classes

Separate contracts will define:

| Contract | Record Types | Priority |
|----------|--------------|----------|
| Semantic Memory Store | Entity, Fact, Relationship, Concept | P2 |
| Procedural Memory Store | Skill, Procedure, Pattern | P2 |
| Preference Memory Store | Preference, Behavior, Setting | P3 |

## Alternatives Considered

### Alternative 1: No Case Record
Use `case_id` as a pure reference without a corresponding record.

- **Pros**: Simpler, fewer record types
- **Cons**: No case metadata, lifecycle, actors, or resolution tracking

### Alternative 2: Mixed Memory Types in One Contract
Define all memory types in a single contract.

- **Pros**: Single comprehensive spec
- **Cons**: Very different record semantics, storage patterns, and lifecycles

## Consequences

### Positive
- **Clear Scope**: Episodic Memory is well-defined and bounded
- **Complete Anchor**: Case Record provides lifecycle and metadata
- **Future-Ready**: Other memory classes have clear boundaries
- **Learning Path**: Hypothesis → Semantic/Procedural promotion is explicit

### Negative
- **More Record Types**: 9 instead of 8
- **Future Work**: Three more contracts to define

### Neutral
- Memory Store CRD now includes `memory_class: episodic`
- CAF Store REST API explicitly supports all 9 episodic types

## Related Decisions

- [ADR-0052: CAF Record Type Taxonomy](./0052-caf-record-type-taxonomy.md)
- [ADR-0055: CAF Memory Store Contract](./0055-caf-memory-store-contract.md)

