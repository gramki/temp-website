# Retention, Deletion, and PII Policy

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-07  
> **Related**: [Memory Services README](./README.md) | [CAF README](../cognitive-audit-fabric/README.md) | [Hub Enterprise Memory](./hub-enterprise-memory.md)

---

## Overview

This document defines the **retention, deletion, and PII handling policies** for Hub Memory Services. These policies ensure compliance with data protection regulations, legal hold requirements, and enterprise data governance standards.

### Key Principles

| Principle | Description |
|-----------|-------------|
| **No PII in Episodic Memory** | Episodic memory records must never contain PII |
| **Immutable Records** | Episodic records are append-only; deletion only via retention expiry or legal process |
| **Legal Hold Support** | Records can be placed on legal hold, preventing deletion |
| **Configurable Retention** | Retention periods are configurable per memory class and record type |
| **Audit Trail** | All retention and deletion actions are audited |

---

## PII Classification & Prohibition

### Critical Constraint: No PII in Episodic Memory

> **Design Principle:** No Episodic memory record may contain Personally Identifiable Information (PII).

This is a **non-negotiable design constraint** that applies to all CAF-compliant episodic memory stores, including Hub Memory Services.

### Why No PII?

| Reason | Description |
|--------|-------------|
| **Immutability** | Episodic records cannot be modified after creation; PII corrections would require new records |
| **Right to Erasure** | GDPR/CCPA deletion requests cannot easily target immutable episodic records |
| **Cross-System Sharing** | Episodic records may be analyzed across workbenches; PII increases exposure |
| **Audit Requirements** | Audit records must be retained for compliance; PII complicates retention |
| **Learning Use** | Records may feed into ML training; PII would require complex anonymization |

### What Qualifies as PII?

| Category | Examples | Handling |
|----------|----------|----------|
| **Direct Identifiers** | Name, SSN, Email, Phone, Address | ❌ Never stored — use entity references |
| **Account Identifiers** | Account numbers, Card numbers | ❌ Never stored — use tokenized references |
| **Biometric Data** | Fingerprints, voice prints | ❌ Never stored |
| **Location Data** | GPS coordinates, IP addresses | ❌ Never stored — use general location if needed |
| **Entity References** | Customer ID, Account ID (opaque tokens) | ✅ Allowed — these are not PII |
| **Aggregated Data** | "Premium customer segment" | ✅ Allowed — not individually identifying |

### Entity Reference Pattern

Instead of storing PII, use **entity references** that can be resolved through secure lookup:

```yaml
# ❌ WRONG - Contains PII
decision_record:
  case_id: "case-12345"
  customer_name: "John Smith"
  customer_email: "john.smith@example.com"
  customer_ssn: "123-45-6789"
  decision: "approve_refund"

# ✅ CORRECT - Uses entity references
decision_record:
  case_id: "case-12345"
  entity_type: "customer"
  entity_id: "cust-abc123"           # Opaque token, not PII
  customer_segment: "premium"         # Aggregated attribute, not PII
  tenure_years: 8                     # Aggregated attribute, not PII
  decision: "approve_refund"
```

### PII Resolution (At Query Time)

When agents need customer details, they use separate **PII-enabled tools** that:
1. Validate authorization for PII access
2. Retrieve PII from secure systems (MDM, Core Banking)
3. Apply data masking as appropriate
4. Log PII access for audit

```yaml
# Agent retrieves case from memory (no PII)
case = memory.get_case_history(case_id="case-12345")
# case.entity_id = "cust-abc123"

# Agent resolves customer details via secure tool (PII)
customer = entity.get_customer_details(
    entity_id="cust-abc123",
    fields=["name", "email"],
    purpose="dispute_resolution"
)
# Access logged, customer data returned with appropriate masking
```

---

## PII Enforcement

### Write-Time Validation

Hub Memory Services enforces no-PII policy at write time:

```yaml
validation_pipeline:
  - stage: pii_detection
    description: Scan record content for PII patterns
    
    detectors:
      - type: regex
        patterns:
          - name: email
            pattern: "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}"
          - name: ssn
            pattern: "\\d{3}-\\d{2}-\\d{4}"
          - name: phone
            pattern: "\\+?\\d{1,3}[-.\\s]?\\(?\\d{3}\\)?[-.\\s]?\\d{3}[-.\\s]?\\d{4}"
          - name: credit_card
            pattern: "\\d{4}[-.\\s]?\\d{4}[-.\\s]?\\d{4}[-.\\s]?\\d{4}"
      
      - type: named_entity
        model: olympus-pii-ner-v1
        entities:
          - PERSON
          - ADDRESS
          - FINANCIAL_ACCOUNT
      
      - type: field_blocklist
        blocked_fields:
          - name
          - full_name
          - first_name
          - last_name
          - email
          - email_address
          - phone
          - phone_number
          - ssn
          - social_security
          - address
          - street_address
    
    on_detection:
      action: reject
      error_code: PII_DETECTED
      message: "Record contains PII which is prohibited in episodic memory"
```

### Detection Response

When PII is detected:

```yaml
# API Response
{
  "status": "rejected",
  "error": {
    "code": "PII_DETECTED",
    "message": "Record contains prohibited PII",
    "details": {
      "record_type": "decision_record",
      "record_id": "dec-12345",
      "pii_findings": [
        {
          "field_path": "data.customer_context.email",
          "pii_type": "email",
          "detection_method": "regex"
        },
        {
          "field_path": "data.rationale",
          "pii_type": "PERSON",
          "detection_method": "named_entity",
          "snippet": "...approved for John S..."
        }
      ]
    },
    "remediation": "Replace PII with entity references. Use entity_id instead of personal identifiers."
  }
}
```

### Redaction Pipeline (Optional)

For legacy integrations, an optional redaction pipeline can be enabled (not recommended for new implementations):

```yaml
redaction_pipeline:
  enabled: false  # Default: off - prefer rejection over redaction
  
  # If enabled, redact rather than reject
  redaction_strategy:
    - type: replace_with_token
      applies_to: [email, phone, ssn]
      token_format: "[REDACTED:{type}]"
    
    - type: hash
      applies_to: [account_number, card_number]
      algorithm: sha256
      salt_source: workbench_secret
    
    - type: generalize
      applies_to: [address]
      generalization: city_state_only
```

---

## Retention Policies

### Default Retention by Memory Class

| Memory Class | Default Retention | Rationale |
|--------------|-------------------|-----------|
| **Episodic** | 7 years | Regulatory compliance (most jurisdictions) |
| **Semantic** | 5 years | Pattern relevance degrades over time |
| **Procedural** | 3 years | Procedures evolve with business changes |
| **Preference** | 2 years | Preferences change; stale data misleads |

### Retention by Record Type (Episodic)

| Record Type | Default Retention | Legal Hold Eligible |
|-------------|-------------------|---------------------|
| `case_record` | 7 years | Yes |
| `decision_record` | 7 years | Yes |
| `evidence_bundle` | 7 years | Yes |
| `context_snapshot` | 3 years | Yes |
| `outcome_record` | 7 years | Yes |
| `override_record` | 10 years | Yes (extended for compliance) |
| `handoff_context` | 1 year | Yes |
| `hypothesis_record` | 5 years | No |
| `incident_timeline` | 7 years | Yes |

### Workbench-Level Configuration

Retention policies are configured at the workbench level:

```yaml
apiVersion: hub.olympus.io/v1
kind: Workbench
metadata:
  name: fraud-ops-prod
spec:
  memory_services:
    retention_policies:
      episodic:
        default_days: 2555          # 7 years
        
        by_record_type:
          override_record:
            retention_days: 3650    # 10 years
            rationale: "Extended retention for regulatory compliance"
          
          handoff_context:
            retention_days: 365     # 1 year
            rationale: "Operational data, shorter retention"
          
          context_snapshot:
            retention_days: 1095    # 3 years
            rationale: "Context data, medium retention"
      
      semantic:
        default_days: 1825          # 5 years
      
      procedural:
        default_days: 1095          # 3 years
      
      preference:
        default_days: 730           # 2 years
```

---

## Legal Hold

### What is Legal Hold?

**Legal hold** (litigation hold) suspends normal retention policies to preserve records that may be relevant to pending or anticipated litigation, audit, or investigation.

### Legal Hold Mechanics

| Aspect | Description |
|--------|-------------|
| **Scope** | Applied to specific cases, requests, or entities |
| **Effect** | Prevents deletion regardless of retention policy |
| **Duration** | Until explicitly released by authorized party |
| **Audit** | All hold/release actions logged |

### Applying Legal Hold

```yaml
POST /v1/memory/{workbench_id}/legal-hold

Request:
{
  "action": "apply",
  
  "scope": {
    "type": "case",                    # case | entity | request | custom_query
    "case_ids": ["case-12345", "case-67890"]
  },
  
  "hold_details": {
    "hold_id": "hold-abc123",
    "matter_name": "Doe v. ACME Bank",
    "matter_id": "legal-2026-001",
    "custodian": "legal-team-alpha",
    "reason": "Pending litigation - preserve all related records",
    "applied_by": "user-legal-counsel",
    "applied_at": "2026-01-07T10:00:00Z"
  }
}

Response:
{
  "status": "applied",
  "hold_id": "hold-abc123",
  "affected_records": 47,
  "scope_summary": {
    "cases": 2,
    "decision_records": 12,
    "evidence_bundles": 8,
    "other_records": 25
  }
}
```

### Releasing Legal Hold

```yaml
POST /v1/memory/{workbench_id}/legal-hold

Request:
{
  "action": "release",
  
  "hold_id": "hold-abc123",
  
  "release_details": {
    "released_by": "user-legal-counsel",
    "released_at": "2026-06-15T14:00:00Z",
    "reason": "Litigation concluded",
    "post_release_retention": "apply_standard"  # apply_standard | extend_30_days | delete_immediately
  }
}
```

### Legal Hold Status

```yaml
GET /v1/memory/{workbench_id}/legal-hold/{hold_id}

Response:
{
  "hold_id": "hold-abc123",
  "status": "active",
  "matter_name": "Doe v. ACME Bank",
  "applied_at": "2026-01-07T10:00:00Z",
  "applied_by": "user-legal-counsel",
  
  "scope": {
    "type": "case",
    "case_ids": ["case-12345", "case-67890"]
  },
  
  "affected_records": {
    "total": 47,
    "by_type": {
      "case_record": 2,
      "decision_record": 12,
      "evidence_bundle": 8,
      "context_snapshot": 15,
      "outcome_record": 4,
      "handoff_context": 6
    }
  },
  
  "retention_impact": {
    "records_past_normal_retention": 0,
    "records_approaching_normal_retention": 3
  }
}
```

---

## Deletion Semantics

### Deletion Types

| Deletion Type | Trigger | Process | Audit |
|---------------|---------|---------|-------|
| **Retention Expiry** | Record age exceeds retention policy | Automatic, batch | Logged |
| **Legal Process** | Court order, regulatory requirement | Manual, authorized | Full audit trail |
| **Data Subject Request** | GDPR Article 17 (rare for episodic) | Manual, authorized | Full audit trail |

### Retention-Based Deletion

Automated deletion based on retention policies:

```yaml
retention_deletion_job:
  schedule: "0 2 * * *"              # Daily at 2 AM
  
  process:
    1. Identify records past retention
       - WHERE retention_expiry < NOW()
       - AND legal_hold IS NULL
       - AND NOT (record_type IN override_list)
    
    2. Create deletion manifest
       - Record IDs, types, ages
       - Estimated storage reclaim
    
    3. Execute deletion (soft delete)
       - Mark records as deleted
       - Remove from active indices
       - Retain deletion metadata
    
    4. Purge (after soft delete period)
       - Physical deletion after 30 days
       - Irreversible
    
    5. Audit logging
       - Records deleted count by type
       - Storage reclaimed
       - Job execution details
```

### Legal/Regulatory Deletion

For court-ordered or regulatory deletions:

```yaml
POST /v1/memory/{workbench_id}/deletion-request

Request:
{
  "request_type": "regulatory_order",
  
  "authorization": {
    "order_id": "court-2026-0001",
    "issuing_authority": "US District Court - Southern District",
    "order_date": "2026-01-05",
    "authorized_by": "user-legal-counsel",
    "authorization_document_ref": "doc-xyz789"
  },
  
  "scope": {
    "type": "specific_records",
    "record_ids": ["rec-11111", "rec-22222", "rec-33333"]
  },
  
  "execution": {
    "scheduled_at": "2026-01-10T00:00:00Z",
    "notify": ["user-legal-counsel", "user-compliance-officer"]
  }
}

Response:
{
  "deletion_request_id": "del-req-001",
  "status": "pending_approval",
  "requires_approval_from": ["user-compliance-officer", "user-data-protection-officer"],
  "scheduled_execution": "2026-01-10T00:00:00Z"
}
```

### Data Subject Requests (GDPR/CCPA)

For episodic memory, data subject deletion requests have limited scope due to entity reference pattern:

```yaml
# Data subject request handling
data_subject_request:
  # What CAN be deleted
  deletable:
    - preference_memory_records      # User preferences
    - agent_memory_records           # Agent memory about subject
    - entity_records_in_mdm          # Handled by MDM, not memory services
  
  # What CANNOT be deleted (entity reference pattern)
  non_deletable:
    - episodic_memory_records        # Contains entity_id, not PII
    - decision_records               # Business decisions (no PII)
    - evidence_bundles               # Context at decision time (no PII)
  
  # Response to data subject
  response:
    message: >
      Episodic memory records contain only anonymized entity references 
      (entity_id: cust-abc123), not personal information. Your personal 
      data is stored in identity systems which have been processed 
      separately. Episodic records will be retained for the standard 
      retention period for audit purposes.
```

---

## Audit Trail

### Deletion Audit Record

```yaml
deletion_audit_record:
  audit_id: "aud-del-001"
  timestamp: "2026-01-10T00:00:15Z"
  
  action: "record_deletion"
  deletion_type: "regulatory_order"
  
  authorization:
    order_id: "court-2026-0001"
    authorized_by: "user-legal-counsel"
    approved_by: ["user-compliance-officer", "user-data-protection-officer"]
  
  affected_records:
    count: 3
    record_ids: ["rec-11111", "rec-22222", "rec-33333"]
    record_types: ["decision_record", "decision_record", "evidence_bundle"]
  
  execution:
    executed_by: "system"
    execution_duration_ms: 1250
    storage_reclaimed_bytes: 45678
  
  # Deletion audit records are retained indefinitely
  retention: "indefinite"
```

### Retention Policy Change Audit

```yaml
policy_change_audit:
  audit_id: "aud-pol-001"
  timestamp: "2026-01-05T10:00:00Z"
  
  action: "retention_policy_change"
  
  change:
    scope: "workbench:fraud-ops-prod"
    record_type: "override_record"
    previous_retention_days: 2555
    new_retention_days: 3650
    reason: "Extended retention for regulatory compliance"
  
  changed_by: "user-compliance-officer"
  approved_by: "user-data-protection-officer"
```

---

## Compliance Mapping

### Regulatory Requirements

| Regulation | Requirement | Hub Memory Services Support |
|------------|-------------|----------------------------|
| **GDPR Art. 5(1)(e)** | Data minimization, limited retention | Configurable retention policies |
| **GDPR Art. 17** | Right to erasure | Entity reference pattern (no PII in episodic) |
| **GDPR Art. 20** | Data portability | Export APIs for preference/agent memory |
| **CCPA 1798.105** | Right to delete | Same as GDPR Art. 17 |
| **SOX** | 7-year retention for financial records | Default episodic retention = 7 years |
| **FINRA 4511** | 6-year retention for securities | Configurable per workbench |
| **Fair Lending** | Decision explainability | Decision records with rationale |

### Audit Support

| Audit Type | Memory Services Support |
|------------|------------------------|
| **Internal Audit** | Full query access to memory with audit logging |
| **External Audit** | Scoped access via audit credentials |
| **Regulatory Exam** | Export capabilities with legal hold |
| **Litigation Discovery** | Legal hold + targeted export |

---

## Related Documents

- [Memory Services README](./README.md) — Architecture overview
- [CAF README](../cognitive-audit-fabric/README.md) — Episodic memory principles
- [Hub Enterprise Memory](./hub-enterprise-memory.md) — Storage implementation
- [Data Classification Policy](../../05-infrastructure/data-classification.md) — Enterprise data classification

---

*TODO: PII detection model training, cross-jurisdiction retention rules, automated compliance reporting*

