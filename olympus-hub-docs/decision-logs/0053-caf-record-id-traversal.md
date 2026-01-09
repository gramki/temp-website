# ADR-0053: CAF Record ID and Traversal Conventions

## Status

**Accepted**

## Date

2026-01-07

## Context

CAF records form a graph that must be traversable for:
- Case reconstruction (all records for a case)
- Decision audit (decision → evidence → context)
- Outcome analysis (outcome → decision → evidence)
- Session replay (all turns in a session)
- Cross-case pattern analysis (hypothesis validation)

We needed conventions for:
1. ID format (how records are identified)
2. Universal binding (how records relate to a case)
3. Hub context (optional context for Hub-originated records)
4. Foreign key format (how records reference each other)

## Decision

### 1. UUID v4 for All IDs

All CAF record identifiers use **UUID v4** format:

```yaml
id: uuid           # e.g., "550e8400-e29b-41d4-a716-446655440000"
case_id: uuid      # Universal binding anchor
*_id: uuid         # All foreign key references
```

**Rationale:**
- Globally unique without coordination
- No semantic meaning (opaque)
- Decentralized generation
- Standard format across all systems

### 2. case_id as Universal Binding

All CAF records include `case_id` as a universal binding identifier:

```yaml
case_id: uuid  # Universal binding (= hub request_id when Hub-originated)
```

| Context | case_id Value |
|---------|---------------|
| **Hub-originated** | Same as `hub_metadata.request_id` |
| **External system** | External case/ticket/reference ID |
| **Standalone agent** | Agent-assigned correlation ID |

**Rationale:**
- All records for a case reachable via single query
- Works regardless of record origin (Hub or external)
- Enables mixed-origin case correlation

### 3. hub_metadata Optional Section

All records include optional `hub_metadata` for Hub context:

```yaml
hub_metadata:
  tenant_id: uuid
  subscription_id: uuid
  workbench_id: uuid
  scenario_id: uuid
  request_id: uuid
  parent_request_id: uuid  # For nested requests
```

**Rationale:**
- CAF records may be created outside Hub context
- When present, enables workbench-scoped queries and analytics
- Supports request lineage tracking

### 4. Traversal Patterns

| Pattern | Starting Point | Use Case |
|---------|---------------|----------|
| **Case Reconstruction** | `case_id` → all record types | Complete case history |
| **Decision Audit** | `decision_record_id` → evidence, context, outcome | Audit package |
| **Session Replay** | `session_id` + `turn_number` | Agent debugging |
| **Backward Traversal** | `outcome_record_id` → decision → evidence | Root cause analysis |

### 5. Required Indexes

| Index | Purpose |
|-------|---------|
| `case_id` (all records) | Case reconstruction |
| `decision_record_id` | Decision audit |
| `session_id + turn_number` | Session replay |
| `timestamp` | Temporal ordering |

## Alternatives Considered

### Alternative 1: Sequential IDs
Use auto-incrementing integers per tenant.

- **Pros**: Smaller, sortable by creation time
- **Cons**: Requires coordination, leaks information, not globally unique

### Alternative 2: External Case ID as Primary Key
Use external system's case ID as the primary key.

- **Pros**: Direct correlation to external systems
- **Cons**: Format varies by system, collision risk, no control over uniqueness

## Consequences

### Positive
- **Universal Navigability**: Any record reachable from case_id
- **Consistent Format**: UUIDs everywhere, no format translation
- **Flexible Origin**: Works for Hub, Seer, and external systems
- **Efficient Queries**: Required indexes defined

### Negative
- **Larger IDs**: UUIDs are 36 characters vs sequential integers
- **No Time Ordering**: UUID v4 not sortable by time (use timestamp field)

### Neutral
- All foreign key references are UUIDs
- Consistency rules enforce referential integrity

## Related Decisions

- [ADR-0052: CAF Record Type Taxonomy](./0052-caf-record-type-taxonomy.md)
- [ADR-0029: CAF as Control Plane](./0029-caf-control-plane.md)

