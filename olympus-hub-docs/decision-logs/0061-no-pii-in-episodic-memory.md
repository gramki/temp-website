# 0061. No PII in Episodic Memory

## Status

Accepted

## Date

2026-01-07

## Context

Hub Memory Services implements CAF-compliant episodic memory stores that capture decisions, evidence, outcomes, and handoffs. These records are **immutable** by design (ADR-0057) to ensure audit integrity and tamper-evidence.

The question arose: should episodic memory records be allowed to contain Personally Identifiable Information (PII) such as customer names, emails, SSNs, or account numbers?

### Constraints

- Episodic records are append-only; modifications are not permitted
- Records may be retained for 7+ years for regulatory compliance
- GDPR Article 17 and CCPA §1798.105 require right-to-erasure capabilities
- Records may feed into ML training and pattern analysis
- Cross-workbench analysis may expose records to broader audiences

### Requirements

- Must support regulatory compliance (GDPR, CCPA, Fair Lending)
- Must enable audit and investigation without compromising privacy
- Must allow customer identification for case resolution
- Must support data subject access and erasure requests

## Decision

We will **prohibit PII in all episodic memory records**. Records must use **entity references** (opaque identifiers) instead of personal identifiers.

### Key Points

- Episodic records use `entity_id` (e.g., `cust-abc123`) instead of PII (names, emails, SSNs)
- PII resolution happens at query time via separate, audited PII-enabled tools
- Write-time validation detects and rejects records containing PII
- Entity references can be resolved through secure lookup when authorized

## Alternatives Considered

### Alternative 1: Allow PII with Encryption

Store PII in episodic records but encrypt sensitive fields.

**Pros:**
- Records are self-contained
- No need for external entity resolution

**Cons:**
- Immutability conflicts with right-to-erasure (cannot delete encrypted data from immutable record)
- Key rotation across years of records is operationally complex
- Encryption at rest doesn't prevent access by authorized users with keys

**Why rejected:** Immutability makes erasure impossible; encryption doesn't solve the fundamental conflict.

---

### Alternative 2: Allow PII with Redaction Markers

Store PII but mark fields for future redaction; redact when erasure requested.

**Pros:**
- Records remain self-contained initially
- Can track what was redacted

**Cons:**
- Violates immutability principle (redaction modifies record)
- Content hash would change on redaction, breaking integrity guarantees
- Partial redaction may still reveal identity through context

**Why rejected:** Conflicts with episodic record immutability (ADR-0057); undermines audit integrity.

---

### Alternative 3: Separate PII Store with Links

Store PII in a separate, mutable store; episodic records contain links.

**Pros:**
- Episodic records remain immutable
- PII can be deleted independently
- Clear separation of concerns

**Cons:**
- Adds complexity (two stores, link management)
- Link resolution adds latency
- Orphaned links when PII deleted

**Why rejected:** This is essentially what we're doing with entity references, but formalized. The simpler approach is to use existing entity/MDM systems rather than create a parallel PII store.

---

## Consequences

### Positive

- **Compliance simplified**: Right-to-erasure applies to entity systems, not episodic memory
- **Immutability preserved**: Records remain append-only with hash integrity
- **Cross-workbench safe**: No PII leakage when analyzing patterns across workbenches
- **ML training safe**: Records can feed into training without PII anonymization
- **Audit integrity**: Cannot tamper with records under guise of "PII correction"

### Negative

- **Entity resolution required**: Agents must call separate tools to get customer details
- **Context loss**: Record alone doesn't show "John Smith"; requires lookup
- **Integration effort**: Legacy systems may need to adapt to entity-reference pattern

### Neutral

- Existing entity/MDM systems become authoritative for PII
- Write validation pipeline required for PII detection

## Implementation Notes

- PII detection uses regex patterns (email, SSN, phone, credit card) + NER model
- Records with detected PII are rejected at write time with remediation guidance
- Entity references should be opaque tokens (not sequential IDs that could be enumerated)
- PII resolution tools must log access for audit

## Related Decisions

- [ADR-0057: Episodic Memory Immutability](./0057-episodic-memory-immutability.md) — Immutability makes PII storage problematic
- [ADR-0056: CAF Episodic Memory Scope](./0056-caf-episodic-memory-scope.md) — Episodic memory scope definition
- [ADR-0028: Data Classification](./0028-data-classification.md) — Data classification framework

## References

- [Retention Policy](../04-subsystems/memory-services/enterprise-memory/retention-policy.md)
- [PII Policy](../04-subsystems/memory-services/shared/pii-policy.md)
- [CAF README - No PII Section](../04-subsystems/cognitive-audit-fabric/README.md)
- GDPR Article 17 — Right to Erasure
- CCPA §1798.105 — Right to Delete

