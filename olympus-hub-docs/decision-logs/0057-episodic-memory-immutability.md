# ADR 0057: Episodic Memory Immutability

**Status**: Accepted  
**Date**: 2026-01-07  
**Category**: caf

---

## Context

Episodic Memory stores event-based, time-ordered records that document decisions, evidence, outcomes, and other cognitive artifacts. These records serve as the audit trail for AI agent behavior and must be trustworthy for compliance, reproducibility, and dispute resolution.

The question arose: should episodic records be mutable (allowing updates and corrections) or immutable (append-only)?

---

## Decision

**All episodic memory records are immutable.** Once written, they cannot be modified or deleted.

### Implementation

1. **Content Hash**: Every episodic record includes a `content_hash` field (SHA-256) computed from the record content
2. **No Updates**: PUT and PATCH methods return 405 Method Not Allowed
3. **No Deletes**: DELETE method returns 405 Method Not Allowed
4. **Idempotent Writes**: Same ID + same hash = duplicate accepted; same ID + different hash = 409 Conflict
5. **Corrections via New Records**: Errors are corrected by creating `override_record` referencing the original

### Hash Format

```
sha256:<hex-encoded-64-character-hash>
```

Computed from canonical JSON (sorted keys, no whitespace) of the `data` field.

---

## Consequences

### Positive

- **Audit Integrity**: Records cannot be tampered with after the fact
- **Reproducibility**: Decisions can be exactly reconstructed using the same context
- **Compliance**: Meets regulatory requirements for decision traceability
- **Trust**: Consumers can trust that what they read is what was written
- **Simplification**: No version tracking, conflict resolution, or merge logic needed

### Negative

- **Storage Growth**: Cannot compact or summarize old records
- **Correction Complexity**: Errors require new records rather than in-place fixes
- **No Soft Deletes**: Cannot remove erroneous records (only supersede them)

### Neutral

- Legal holds are implicitly satisfied by immutability (no separate mechanism needed)
- Retention policies will be the only mechanism for eventual cleanup (if ever needed)

---

## Related

- [CAF Store REST API](../04-subsystems/cognitive-audit-fabric/episodic-memory-store/caf-store-rest-api.md) — Immutability enforcement
- [Case Records](../04-subsystems/cognitive-audit-fabric/episodic-memory-store/case-records.md) — Content hash in schema
- [ADR 0056](./0056-caf-episodic-memory-scope.md) — Episodic Memory scope


