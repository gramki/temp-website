# 4.7 Immutability & Data Governance

Enterprise Memory must satisfy stringent data governance requirements: immutability for audit defensibility, PII prohibition for long-term retention, and compliant right-to-erasure handling. This section details how Seer and Hub implement these requirements.

## Why These Constraints Matter

| Requirement | Business Driver | Regulatory Driver |
|-------------|-----------------|-------------------|
| **Immutability** | Audit defensibility | Tamper-evident records for regulators |
| **No PII** | 7+ year retention | GDPR/CCPA erasure compatibility |
| **Right to erasure** | Customer trust | Legal obligation |
| **Retention periods** | Institutional learning | Regulatory mandates |

## Immutability

### Principle

Enterprise Memory records are **append-only**:
- Once written, records cannot be modified
- Corrections are made via new amendment records
- Original record is preserved and linked to correction

### Implementation

```yaml
decision_record:
  record_id: "dr-original-123"
  content_hash: "sha256:abc123..."  # Computed at creation
  
  # If this record needs correction:
amendment_record:
  record_id: "dr-amendment-456"
  amends: "dr-original-123"
  reason: "Rationale summary was incomplete"
  corrected_fields:
    rationale.summary: "Updated summary with complete reasoning"
  content_hash: "sha256:def456..."
```

### Chain Linking

Records can be cryptographically linked:

```
Record 1 → hash₁
Record 2 → hash₂ = hash(content₂ + hash₁)
Record 3 → hash₃ = hash(content₃ + hash₂)
```

Any modification to earlier records breaks the chain, providing tamper evidence.

### Storage Backend

Enterprise Memory uses Olympus Europa (OpenSearch) with:
- Write-once index settings
- No update/delete API exposure
- Audit logging of all operations

## PII Prohibition

### Principle

Enterprise Memory contains **no direct PII**:
- Uses entity references instead of personal data
- Enables 7+ year retention without privacy conflicts
- Supports right-to-erasure via reference deletion

### Entity Reference Pattern

Instead of:
```yaml
# BAD: Direct PII
customer_name: "John Smith"
customer_email: "john@example.com"
```

Use:
```yaml
# GOOD: Entity reference
customer_ref: "cust-12345"
# Resolution via Customer Service (not in memory)
```

### What Can Be Stored

| Allowed | Not Allowed |
|---------|-------------|
| Entity references (IDs) | Names, addresses, emails |
| Business facts | Personal identifiers |
| Decision rationale | Personal data in rationale |
| Outcome categories | Individual-identifying outcomes |
| Anonymized patterns | PII patterns |

### PII Detection

CAF enforces PII prohibition:

```yaml
caf_policy:
  memory:
    enterprise_memory:
      pii_detection: enabled
      on_pii_detected: reject
      patterns:
        - email
        - phone
        - ssn
        - credit_card
        - name_patterns
```

Records containing detected PII are rejected at write time.

## Right to Erasure

### The Challenge

GDPR/CCPA require organizations to delete personal data on request. But:
- Enterprise Memory must be retained 7+ years
- Audit records must be immutable

### The Solution: Referential Erasure

1. **Enterprise Memory contains no PII** — only entity references
2. **Entity Reference Service holds the mapping** — `cust-12345` → "John Smith"
3. **On erasure request** — delete the mapping, not the memory
4. **Result** — Memory records remain for audit, but cannot be linked to individual

```
BEFORE ERASURE:
┌─────────────────────┐     ┌─────────────────────────┐
│ Enterprise Memory   │     │ Entity Reference Service │
│                     │     │                         │
│ customer_ref:       │────▶│ cust-12345 → John Smith │
│ cust-12345          │     │                         │
└─────────────────────┘     └─────────────────────────┘

AFTER ERASURE:
┌─────────────────────┐     ┌─────────────────────────┐
│ Enterprise Memory   │     │ Entity Reference Service │
│                     │     │                         │
│ customer_ref:       │────▶│ cust-12345 → [DELETED]  │
│ cust-12345          │     │                         │
└─────────────────────┘     └─────────────────────────┘

Memory retained; personal data erased.
```

### Erasure Workflow

```yaml
erasure_request:
  request_id: "erase-789"
  subject: "john@example.com"
  timestamp: 2026-01-10T10:00:00Z
  
erasure_execution:
  # Step 1: Identify entity references
  entity_refs_found:
    - cust-12345
    - contact-67890
    
  # Step 2: Delete reference mappings
  mappings_deleted:
    - cust-12345: deleted
    - contact-67890: deleted
    
  # Step 3: Log erasure
  erasure_log:
    request_id: "erase-789"
    completed_at: 2026-01-10T10:05:00Z
    entity_refs_erased: 2
    memory_records_preserved: 47
```

## Retention Policies

### Enterprise Memory

| Memory Class | Default Retention | Legal Hold |
|--------------|------------------|------------|
| **Episodic** | 7 years | Indefinite if hold applies |
| **Semantic** | 5 years | Indefinite if hold applies |
| **Procedural** | 3 years | Indefinite if hold applies |
| **Preference** | 2 years | Indefinite if hold applies |

### Agent Memory

| Storage Type | Default Retention |
|--------------|------------------|
| **Conversation** | Session + 48 hours |
| **KV Store** | Session + 24 hours |
| **Log Service** | Session + 72 hours |
| **Document Store** | Session + 7 days |

### Legal Hold

Records can be placed on legal hold:

```yaml
legal_hold:
  hold_id: "lh-litigation-001"
  scope:
    case_ids: [case-12345, case-12346]
    date_range:
      from: 2025-01-01
      to: 2025-12-31
  expires: never  # Until explicitly released
  
  effect:
    - retention policies suspended
    - deletion prohibited
    - modification prohibited
```

## Audit Trail

All governance operations are logged:

```yaml
governance_audit:
  operation: erasure_executed
  request_id: "erase-789"
  timestamp: 2026-01-10T10:05:00Z
  actor: "data-protection-officer@acme.com"
  affected_refs: ["cust-12345", "contact-67890"]
  memory_records_preserved: 47
  compliance_note: "GDPR Article 17 request fulfilled"
```

---

**References:**
*   `olympus-hub-docs/04-subsystems/memory-services/enterprise-memory/retention-policy.md`
*   `olympus-hub-docs/04-subsystems/memory-services/shared/pii-policy.md`
*   `olympus-seer-docs/why-seer/part-1-background/03-memory-requirements/03-4-governance-imperatives.md`
*   `olympus-seer-docs/why-seer/part-1-background/04-audit-requirements/04-4-immutability-tamper-evidence.md`
