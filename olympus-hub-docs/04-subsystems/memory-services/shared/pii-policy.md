# PII Policy for Memory Services

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-07  
> **Parent**: [Shared Concepts](./README.md)

---

## Overview

This document defines PII (Personally Identifiable Information) handling policies across Hub Memory Services. **Enterprise Memory and Agent Memory have different PII policies** based on their purposes and compliance requirements.

---

## Policy Summary

| Memory Type | PII Policy | Rationale |
|-------------|------------|-----------|
| **Enterprise Memory** | **Prohibited** | Immutability conflicts with right-to-erasure; audit records must be clean |
| **Agent Memory** | **Permitted** | Mutable records allow deletion; personalization requires some PII |

---

## Enterprise Memory: No PII

### Critical Constraint

> **Design Principle:** No Episodic memory record in Enterprise Memory may contain PII.

This applies to all CAF-compliant episodic memory records:
- Decision Records
- Evidence Bundles
- Context Snapshots
- Outcome Records
- Override Records
- Handoff Context
- Hypothesis Records
- Incident Timelines

### Entity Reference Pattern

Instead of storing PII, use **entity references**:

```yaml
# ❌ WRONG - Contains PII
decision_record:
  customer_name: "John Smith"
  customer_email: "john.smith@example.com"
  customer_ssn: "123-45-6789"

# ✅ CORRECT - Uses entity references
decision_record:
  entity_type: "customer"
  entity_id: "cust-abc123"           # Opaque token
  customer_segment: "premium"         # Aggregated attribute
  tenure_years: 8                     # Aggregated attribute
```

### PII Resolution

When agents need customer details, they use separate PII-enabled tools:

```python
# Memory query returns entity reference
case = memory.get_case_history(case_id="case-12345")
# case.entity_id = "cust-abc123"

# Separate tool resolves PII (with audit logging)
customer = entity.get_customer_details(
    entity_id="cust-abc123",
    fields=["name", "email"],
    purpose="dispute_resolution"
)
```

### Enforcement

Enterprise Memory enforces no-PII at write time:

1. **Regex Detection**: Email, SSN, phone, credit card patterns
2. **NER Detection**: Named entity recognition for PERSON, ADDRESS, etc.
3. **Field Blocklist**: Known PII field names rejected

Records with detected PII are **rejected** (not redacted).

See [Retention and PII Policy](../enterprise-memory/retention-policy.md) for full enforcement details.

---

## Agent Memory: PII Permitted

### Permitted with Conditions

Agent Memory **may contain PII** because:
- Records are mutable (can be deleted)
- Personalization requires some user data
- Shorter retention reduces exposure
- Not subject to immutability constraints

### Conditions for PII Storage

| Condition | Requirement |
|-----------|-------------|
| **Consent** | User consent obtained for data storage |
| **Purpose Limitation** | PII stored only for specific purposes |
| **Minimization** | Only necessary PII stored |
| **Encryption** | PII encrypted at rest |
| **Access Control** | PII access logged and controlled |
| **Deletion Support** | PII deletable on request |

### PII Categories in Agent Memory

| Category | Examples | Storage Guidance |
|----------|----------|------------------|
| **Contact Info** | Email, phone | Store if needed for communication |
| **Preferences** | Timezone, locale | Store for personalization |
| **Behavioral** | Interaction patterns | May derive from behavior (not explicit PII) |
| **Identifiers** | User ID, session ID | Required for functionality |

### Data Subject Requests

Agent Memory supports data subject requests:

| Request Type | Agent Memory Response |
|--------------|----------------------|
| **Access (GDPR Art. 15)** | Export all agent memory for subject |
| **Erasure (GDPR Art. 17)** | Delete all agent memory for subject |
| **Rectification (Art. 16)** | Update incorrect data |
| **Portability (Art. 20)** | Export in machine-readable format |

---

## Cross-Memory Implications

### Promotion and PII

When Agent Memory promotes to Enterprise Memory:

```
Agent Memory (may have PII)
        │
        │ Promotion pipeline
        ▼
PII Stripping
        │
        │ Replace PII with entity references
        ▼
Enterprise Memory (no PII)
```

**Promotion removes PII**:
- Names → Entity IDs
- Emails → Entity IDs
- Specific values → Aggregated attributes

### Query Results

| Query Source | PII in Response |
|--------------|-----------------|
| Enterprise Memory | Never |
| Agent Memory | Possible (based on access control) |
| Cross-memory queries | Enterprise portion: no PII |

---

## Compliance Mapping

| Regulation | Enterprise Memory | Agent Memory |
|------------|-------------------|--------------|
| **GDPR Art. 17 (Erasure)** | Entity references allow deletion in source systems | Direct deletion supported |
| **GDPR Art. 5(1)(e) (Minimization)** | No PII stored | Only necessary PII |
| **CCPA §1798.105 (Delete)** | Entity references allow deletion | Direct deletion supported |
| **SOX (Audit Trail)** | Immutable records preserved | N/A |

---

## Implementation Notes

### Enterprise Memory PII Detection

```yaml
pii_detection:
  regex_patterns:
    - name: email
      pattern: "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}"
    - name: ssn
      pattern: "\\d{3}-\\d{2}-\\d{4}"
    - name: phone
      pattern: "\\+?\\d{1,3}[-.\\s]?\\(?\\d{3}\\)?[-.\\s]?\\d{3}[-.\\s]?\\d{4}"
    - name: credit_card
      pattern: "\\d{4}[-.\\s]?\\d{4}[-.\\s]?\\d{4}[-.\\s]?\\d{4}"
  
  ner_model: olympus-pii-ner-v1
  ner_entities: [PERSON, ADDRESS, FINANCIAL_ACCOUNT]
  
  field_blocklist:
    - name, full_name, first_name, last_name
    - email, email_address
    - phone, phone_number, mobile
    - ssn, social_security
    - address, street_address
```

### Agent Memory PII Encryption

```yaml
pii_encryption:
  algorithm: AES-256-GCM
  key_management: olympus-kms
  key_rotation_days: 90
  
  encrypted_fields:
    - email
    - phone
    - address
    - custom_pii_fields
```

---

## Related Documents

- [Enterprise Memory - Retention Policy](../enterprise-memory/retention-policy.md)
- [Agent Memory - Retention & Decay](../agent-memory/retention-and-decay.md)
- [CAF README - No PII Section](../../cognitive-audit-fabric/README.md)
- [ADR-0061: No PII in Episodic Memory](../../../decision-logs/0061-no-pii-in-episodic-memory.md)

