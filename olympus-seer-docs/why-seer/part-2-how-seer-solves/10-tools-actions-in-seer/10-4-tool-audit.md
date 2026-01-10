# 10.4 Tool Audit

Every tool invocation is recorded in the Cognitive Audit Fabric. This creates a complete, immutable record of all agent actions—essential for compliance, debugging, and accountability.

## What's Recorded

| Aspect | Details Captured |
|--------|------------------|
| **Who** | Agent identity, delegation chain |
| **What** | Tool, operation, parameters |
| **When** | Timestamp, duration |
| **Result** | Success/failure, response |
| **Context** | Case, request, policies applied |

## Audit Record Structure

```yaml
tool_audit_record:
  record_id: "tar-xyz789"
  record_type: tool_invocation
  timestamp: 2026-01-10T14:30:00Z
  
  # Who
  agent:
    identity: dispute-analyst-tier1
    employment_spec: dispute-analyst-acme-prod
    delegator: manager@acme.com
    delegation_id: del-456
    
  # What
  tool:
    protocol: approve-refund
    protocol_version: 2.0.0
    instance: acme-refund-api
    operation: create_refund
    
  # Parameters (PII-safe)
  request:
    case_id: case-12345
    amount: 450
    reason: "Merchant error confirmed"
    # Note: No customer PII in audit record
    
  # Result
  response:
    status: success
    refund_id: ref-abc123
    refund_status: approved
    
  # Timing
  timing:
    invoked_at: 2026-01-10T14:30:00.123Z
    completed_at: 2026-01-10T14:30:00.357Z
    duration_ms: 234
    
  # Authorization
  authorization:
    policies_evaluated:
      - tool-allowlist: passed
      - authority-ceiling: passed (450 <= 500)
      - rate-limit: passed
    
  # Context
  context:
    request_id: req-abc123
    case_id: case-12345
    decision_record_ref: dr-def456
    trace_id: trace-ghi789
    
  hub_metadata:
    tenant_id: acme
    workbench_id: dispute-ops-prod
    content_hash: sha256:abc123...
```

## Integration with CAF

Tool records link to other CAF records:

```
Decision Record (dr-def456)
    │
    ├── Evidence Bundle (what agent knew)
    │
    ├── Tool Invocation (tar-xyz789) ← This record
    │       └── Result of action
    │
    └── Outcome Record (what happened after)
```

## Audit Queries

### By Agent

```yaml
query:
  type: tool_invocations
  filters:
    agent: dispute-analyst-tier1
    time_range: last_24h
    
  returns:
    - 47 invocations
    - 45 successful, 2 failed
    - tools: [approve-refund (23), get-transaction (24)]
```

### By Case

```yaml
query:
  type: tool_invocations
  filters:
    case_id: case-12345
    
  returns:
    - get-transaction-details: success (14:28:00)
    - get-customer-history: success (14:28:30)
    - approve-refund: success (14:30:00)
    - send-notification: success (14:30:15)
```

### By Tool

```yaml
query:
  type: tool_invocations
  filters:
    tool: approve-refund
    time_range: last_7d
    status: failed
    
  returns:
    - 12 failed invocations
    - reasons: [authority_exceeded (5), backend_error (4), timeout (3)]
```

## Audit for Compliance

### Regulatory Response

When regulator asks "Show all actions this agent took for customer X":

```python
# Note: Query by entity reference, not PII
actions = await caf.query_tools(
    entity_refs=["cust-12345"],
    time_range=("2025-01-01", "2025-12-31")
)

# Returns all tool invocations affecting this customer
# With full context and decision linkage
```

### Investigation

When investigating unexpected behavior:

```python
# What did agent do in this request?
request_actions = await caf.query_tools(
    request_id="req-abc123"
)

# Returns: ordered list of tool invocations
# With parameters, responses, and timing
```

## Audit Retention

Tool audit records follow CAF retention:

```yaml
retention:
  tool_audit_records:
    default: 7_years
    
    legal_hold:
      applies_when: case_under_investigation
      retention: indefinite
      
    pii_handling:
      - no_pii_in_audit_records
      - entity_references_only
```

---

**References:**
*   `olympus-hub-docs/04-subsystems/cognitive-audit-fabric/README.md`
*   `olympus-seer-docs/why-seer/part-2-how-seer-solves/04-memory-knowledge-audit-in-seer/04-5-cognitive-audit-fabric.md`

