# Memory Governance (Agent Memory)

This document is a practical checklist for making agent memory safe, auditable, and operable in real systems.

## Governance goals

- **User trust**: predictable use of remembered information
- **Safety**: prevent prompt injection and policy bypass
- **Privacy**: consent, minimization, and deletion
- **Compliance**: retention, audit trails, access control
- **Operational resilience**: versioning, rollbacks, incident response

---

## Memory classification and data handling

Classify memory at ingestion:

- **PII / sensitive personal data** (names, phone, health, precise location)
- **Confidential business data** (contracts, financials, customer records)
- **Public / non-sensitive**

Controls by class:

- Encryption at rest + in transit
- Field-level redaction (mask or drop)
- Per-tenant isolation
- Strict retention defaults for sensitive classes

---

## Consent, transparency, and user controls

Minimum recommended features:

- **Explicit “remember / forget”** operations
- **Memory viewer** (what is stored, confidence, last used)
- **Deletion semantics**: hard delete for user-requested removal; tombstone + audit for system records
- **Scope controls**: per-app vs global; per-domain vs universal

---

## Access control and scoping

Model memory access like any other privileged data:

- Authentication + authorization
- Role-based access (RBAC) for operators
- Contextual scoping (only retrieve within user/app/tenant)
- Policy gating (procedural memory is often highest risk)

---

## Retention, decay, and legal holds

- Default episodic TTL (e.g., 30–180 days) with archival options
- Prefer **summaries** over raw transcripts for long retention
- Semantic facts are **versioned** with effective dates
- Support legal holds and audit retention where required

---

## Provenance and auditability

Store the following for every memory inclusion:

- Memory ID + type
- Source (conversation/tool/system) + timestamp
- Confidence / freshness
- Retrieval method and score
- Reason for inclusion (salience tag)

This enables:

- Debugging
- Compliance audits
- “Why did the agent do that?” answers

---

## Security hardening: memory as an attack surface

- Treat retrieved memory as **untrusted input**
- Strip/neutralize instructions inside retrieved text
- Enforce tool allowlists and policy precedence
- Rate-limit and monitor memory writes (poisoning attempts)

## Navigation

- Back: [`README.md`](./README.md)
- Related: [`context-building.md`](./context-building.md)

