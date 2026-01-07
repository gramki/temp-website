# ADR-0052: CAF Record Type Taxonomy

## Status

**Accepted**

## Date

2026-01-07

## Context

CAF needed a complete taxonomy of record types to support:
- Decision auditability (what was decided, why)
- Outcome tracking (what happened after)
- Override accountability (who changed decisions)
- Agent handoffs (context preservation)
- Incident investigation (forensic reconstruction)
- Pattern learning (hypothesis promotion)

The original design had only Decision Records and Evidence Bundles marked as stubs. A complete taxonomy was needed to build the fraud-case-resolution-agent and similar enterprise agents.

## Decision

**CAF defines 8 distinct record types organized into three categories:**

### Core Records (Audit Foundation)

| Record Type | Purpose |
|-------------|---------|
| **Decision Record** | Captures rationale and context at decision time |
| **Evidence Bundle** | Packages complete context for reproducibility |
| **Context Snapshot** | Compiled context for every agent turn (not just decisions) |

### Lifecycle & Feedback Records

| Record Type | Purpose |
|-------------|---------|
| **Outcome Record** | Tracks what happened after a decision |
| **Override Record** | Documents manual overrides with accountability |
| **Handoff Context** | State transfer between agents |

### Learning & Investigation Records

| Record Type | Purpose |
|-------------|---------|
| **Hypothesis Record** | Learned patterns pending promotion to knowledge |
| **Incident Timeline** | Chronological event sequences for investigation |

### Key Design Principle: Context Snapshot vs Evidence Bundle

| Aspect | Context Snapshot | Evidence Bundle |
|--------|------------------|-----------------|
| **When** | Every agent turn | Decision points only |
| **Purpose** | Observability, debugging | Audit, compliance |
| **Retention** | Short (days-weeks) | Long (years) |
| **Linkage** | May have no decision | Always has DecisionRecord |

Evidence Bundle **references** a Context Snapshot and adds decision-specific evidence (model I/O, retrieval results).

## Alternatives Considered

### Alternative 1: Fewer Record Types (Collapse into 3)
Combine Outcome/Override into Decision; combine Handoff/Incident into "Events".

- **Pros**: Simpler model
- **Cons**: Loss of semantic clarity, harder querying, mixed retention policies

### Alternative 2: More Granular Record Types
Separate records for each evidence type, each outcome category, etc.

- **Pros**: Very fine-grained control
- **Cons**: Explosion of types, complex relationships, harder to understand

## Consequences

### Positive
- **Complete Coverage**: All cognitive artifacts have a home
- **Clear Semantics**: Each type has distinct purpose and lifecycle
- **Appropriate Retention**: Different types can have different retention policies
- **Query Clarity**: Can query by record type for specific use cases

### Negative
- **More Types to Learn**: 8 types vs 2 original stubs
- **Schema Maintenance**: Each type needs schema evolution management

### Neutral
- All types share common conventions (ID format, case binding, hub metadata)
- All types stored in Enterprise Memory (CAF is control plane, not storage)

## Related Decisions

- [ADR-0029: CAF as Control Plane](./0029-caf-control-plane.md)
- [ADR-0053: CAF Record ID and Traversal Conventions](./0053-caf-record-id-traversal.md)
- [ADR-0054: CAF Typed Content Convention](./0054-caf-typed-content-convention.md)

