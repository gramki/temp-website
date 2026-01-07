# Memory Record Routing

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-07  
> **Related**: [Signal Exchange README](./README.md) | [Memory Services](../memory-services/README.md) | [CAF](../cognitive-audit-fabric/README.md)

---

## Overview

Signal Exchange is responsible for **routing all enterprise memory writes** from Hub Applications and agents to the appropriate memory stores. No Hub agent or application directly accesses memory store write APIs — all writes flow through Signal Exchange.

### Key Principles

| Principle | Description |
|-----------|-------------|
| **Centralized Write Path** | All episodic memory writes flow through Signal Exchange |
| **Request-Bound Records** | Memory records are attached to Request Updates |
| **Async Ingestion** | Records are written asynchronously via Atropos topics |
| **Scenario-Based Routing** | Target memory store determined by Scenario configuration |
| **No Direct Write APIs** | Applications and agents never call memory store write APIs directly |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       MEMORY WRITE PATH (via Signal Exchange)                 │
│                                                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐    │
│   │                    HUB APPLICATION / AGENT                            │    │
│   │                                                                       │    │
│   │   Creates memory records as part of processing:                       │    │
│   │   - Decision Records (when making decisions)                          │    │
│   │   - Evidence Bundles (context at decision time)                       │    │
│   │   - Context Snapshots (compiled context per turn)                     │    │
│   │   - Handoff Context (when transitioning work)                         │    │
│   │   - Outcome Records (when outcomes are observed)                      │    │
│   │                                                                       │    │
│   │   Attaches records to REQUEST_UPDATE message                          │    │
│   └───────────────────────────────────┬───────────────────────────────────┘    │
│                                       │                                        │
│                                       │ REQUEST_UPDATE with memory_records     │
│                                       ▼                                        │
│   ┌───────────────────────────────────────────────────────────────────────┐    │
│   │                         SIGNAL EXCHANGE                                │    │
│   │                                                                        │    │
│   │   ┌─────────────────────────────────────────────────────────────────┐ │    │
│   │   │                   REQUEST UPDATE HANDLER                         │ │    │
│   │   │                                                                  │ │    │
│   │   │   1. Parse REQUEST_UPDATE message                                │ │    │
│   │   │   2. Extract memory_records from payload                         │ │    │
│   │   │   3. Identify Scenario from request context                      │ │    │
│   │   │   4. Look up target memory store from Scenario config            │ │    │
│   │   └─────────────────────────────────────────────────────────────────┘ │    │
│   │                            │                                          │    │
│   │                            ▼                                          │    │
│   │   ┌─────────────────────────────────────────────────────────────────┐ │    │
│   │   │                   MEMORY RECORD ROUTER                           │ │    │
│   │   │                                                                  │ │    │
│   │   │   For each memory record:                                        │ │    │
│   │   │   1. Validate record structure against CAF schema                │ │    │
│   │   │   2. Generate content_hash if not provided                       │ │    │
│   │   │   3. Enrich with hub_metadata (tenant, workbench, scenario)      │ │    │
│   │   │   4. Determine target Atropos topic by memory_class              │ │    │
│   │   │   5. Publish to Atropos topic                                    │ │    │
│   │   └─────────────────────────────────────────────────────────────────┘ │    │
│   │                            │                                          │    │
│   └────────────────────────────┼──────────────────────────────────────────┘    │
│                                │                                               │
│           ┌────────────────────┼────────────────────┐                         │
│           │                    │                    │                         │
│           ▼                    ▼                    ▼                         │
│   ┌───────────────┐    ┌───────────────┐    ┌───────────────┐                 │
│   │   Atropos     │    │   Atropos     │    │   Atropos     │                 │
│   │   Topic:      │    │   Topic:      │    │   Topic:      │                 │
│   │   episodic    │    │   semantic    │    │   procedural  │                 │
│   └───────┬───────┘    └───────┬───────┘    └───────┬───────┘                 │
│           │                    │                    │                         │
│           ▼                    ▼                    ▼                         │
│   ┌───────────────────────────────────────────────────────────────────────┐   │
│   │                    MEMORY STORE WRITER SERVICE                         │   │
│   │                                                                        │   │
│   │   Consumes from Atropos topics → Validates → Indexes in OpenSearch    │   │
│   └───────────────────────────────────────────────────────────────────────┘   │
│                                                                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Request Update with Memory Records

### Message Structure

Hub Applications attach memory records to REQUEST_UPDATE messages:

```yaml
# REQUEST_UPDATE message envelope
message:
  message_type: REQUEST_UPDATE
  request_id: "req-12345"
  timestamp: "2026-01-07T10:15:00Z"
  
  # Application-specific update payload
  update_payload:
    status: "in_progress"
    
    # Memory records to be persisted
    memory_records:
      - record_type: decision_record
        record_id: "dec-abc123"
        case_id: "req-12345"                    # Usually same as request_id
        timestamp: "2026-01-07T10:15:00Z"
        
        data:
          decision_type: "classification"
          action: "classify_high_priority"
          confidence: 0.92
          actor:
            actor_id: "agent-triage-001"
            actor_type: "agent"
          rationale:
            summary: "Pattern match with known fraud ring indicates high priority"
            factors_considered:
              - factor: "transaction_pattern"
                weight: 0.4
                assessment: "Matches FR-2025-0034 signature"
              - factor: "customer_history"
                weight: 0.3
                assessment: "Clean history, 8-year tenure"
          evidence_bundle_id: "evb-def456"
      
      - record_type: evidence_bundle
        record_id: "evb-def456"
        case_id: "req-12345"
        timestamp: "2026-01-07T10:15:00Z"
        
        data:
          decision_id: "dec-abc123"
          context_snapshot_id: "ctx-ghi789"
          evidence_items:
            - type: "pattern_match"
              source: "fraud_detection_model"
              content:
                pattern_id: "FR-2025-0034"
                confidence: 0.87
            - type: "customer_profile"
              source: "customer_360"
              content:
                segment: "premium"
                tenure_years: 8
                prior_disputes: 0
```

### Memory Record Identification

Signal Exchange identifies memory records by looking for the `memory_records` field in the update payload:

```python
def process_request_update(message: RequestUpdate):
    # 1. Process standard update (status, progress, etc.)
    process_standard_update(message)
    
    # 2. Check for memory records
    if "memory_records" in message.update_payload:
        memory_records = message.update_payload["memory_records"]
        route_memory_records(
            records=memory_records,
            request_context=message.request_context
        )
```

---

## Routing Logic

### Scenario-Based Store Resolution

Each Scenario specifies which memory stores to use:

```yaml
# Scenario configuration (in Workbench Management)
scenario:
  id: "fraud-dispute-resolution"
  
  memory_stores:
    episodic:
      store_name: "fraud-ops.episodic.primary"
      atropos_topic: "fraud-ops-episodic-records"
    
    semantic:
      store_name: "fraud-ops.semantic.primary"
      atropos_topic: "fraud-ops-semantic-records"
    
    procedural:
      store_name: "fraud-ops.procedural.primary"
      atropos_topic: "fraud-ops-procedural-records"
```

### Routing by Memory Class

Signal Exchange routes records based on their `record_type`:

```python
# Memory class mapping
RECORD_TYPE_TO_MEMORY_CLASS = {
    # Episodic (case-bound, event-based)
    "case_record": "episodic",
    "decision_record": "episodic",
    "evidence_bundle": "episodic",
    "context_snapshot": "episodic",
    "outcome_record": "episodic",
    "override_record": "episodic",
    "handoff_context": "episodic",
    "hypothesis_record": "episodic",  # May promote to semantic
    "incident_timeline": "episodic",
    
    # Semantic (domain-scoped, not case-bound)
    "pattern_summary": "semantic",
    "learned_constraint": "semantic",
    "entity_belief": "semantic",
    "relationship_belief": "semantic",
    "evaluation_finding": "semantic",
    
    # Procedural (skill-anchored)
    "learned_skill": "procedural",
    "procedure": "procedural",
    "action_sequence": "procedural",
    "tool_usage_pattern": "procedural",
    
    # Preference (subject-anchored)
    "user_preference": "preference",
    "agent_behavior": "preference",
    "interaction_pattern": "preference",
    "contextual_preference": "preference",
}

def route_memory_records(records: list, request_context: RequestContext):
    # Get scenario config
    scenario = get_scenario(request_context.scenario_id)
    
    for record in records:
        # 1. Determine memory class
        memory_class = RECORD_TYPE_TO_MEMORY_CLASS.get(record["record_type"])
        if not memory_class:
            log_error(f"Unknown record type: {record['record_type']}")
            continue
        
        # 2. Get target Atropos topic
        store_config = scenario.memory_stores.get(memory_class)
        if not store_config:
            log_error(f"No {memory_class} store configured for scenario")
            continue
        
        # 3. Enrich record with hub metadata
        enriched_record = enrich_with_metadata(record, request_context)
        
        # 4. Validate against CAF schema
        if not validate_caf_schema(enriched_record):
            log_error(f"Schema validation failed for {record['record_id']}")
            continue
        
        # 5. Publish to Atropos topic
        atropos.publish(
            topic=store_config.atropos_topic,
            message=enriched_record
        )
```

### Record Enrichment

Signal Exchange enriches records with hub metadata before routing:

```python
def enrich_with_metadata(record: dict, context: RequestContext) -> dict:
    enriched = record.copy()
    
    # Add hub_metadata if not present
    if "hub_metadata" not in enriched:
        enriched["hub_metadata"] = {}
    
    enriched["hub_metadata"].update({
        "tenant_id": context.tenant_id,
        "subscription_id": context.subscription_id,
        "workbench_id": context.workbench_id,
        "scenario_id": context.scenario_id,
        "request_id": context.request_id,
    })
    
    # Generate content_hash if not provided
    if "content_hash" not in enriched or not enriched["content_hash"]:
        enriched["content_hash"] = compute_content_hash(enriched["data"])
    
    # Ensure case_id is set (default to request_id if not specified)
    if "case_id" not in enriched or not enriched["case_id"]:
        enriched["case_id"] = context.request_id
    
    return enriched
```

---

## Atropos Topic Configuration

### Topic Per Store

Each memory store has a dedicated Atropos topic:

```yaml
# Atropos topic configuration
atropos_topics:
  - name: "fraud-ops-episodic-records"
    workbench: "wb-fraud-ops"
    memory_class: "episodic"
    
    config:
      partitions: 6
      replication_factor: 3
      retention_hours: 168       # 7 days
      
      consumer_groups:
        - "memory-store-writer"
        - "caf-indexer"
  
  - name: "fraud-ops-semantic-records"
    workbench: "wb-fraud-ops"
    memory_class: "semantic"
    
    config:
      partitions: 3
      replication_factor: 3
      retention_hours: 168
```

### Message Format on Atropos

```yaml
# Atropos message format
atropos_message:
  headers:
    message_id: "msg-xyz789"
    source: "signal-exchange"
    timestamp: "2026-01-07T10:15:01Z"
    workbench_id: "wb-fraud-ops"
    memory_class: "episodic"
    record_type: "decision_record"
  
  payload:
    # Full enriched CAF record
    record_type: "decision_record"
    record_id: "dec-abc123"
    case_id: "req-12345"
    content_hash: "sha256:9f86d081884c..."
    timestamp: "2026-01-07T10:15:00Z"
    
    hub_metadata:
      tenant_id: "tenant-acme-bank"
      subscription_id: "sub-fraud-premium"
      workbench_id: "wb-fraud-ops"
      scenario_id: "fraud-dispute-resolution"
      request_id: "req-12345"
    
    data:
      # Full decision record content
      ...
```

---

## Memory Store Writer Service

The Memory Store Writer Service consumes from Atropos topics and persists to OpenSearch:

```yaml
writer_service:
  consumers:
    - topic: "fraud-ops-episodic-records"
      consumer_group: "memory-store-writer"
      
      processing:
        - step: validate_schema
          action: Validate against CAF record schema
          on_failure: send_to_dlq
        
        - step: verify_hash
          action: Verify content_hash matches computed hash
          on_failure: reject_record
        
        - step: generate_embedding
          action: Generate embedding for semantic search
          model: "olympus-embed-v2"
        
        - step: index_to_opensearch
          action: Index record in OpenSearch
          index: "{workbench_id}_episodic_{record_type}"
          deduplication: by_record_id_and_hash
        
        - step: register_in_catalog
          action: Update CAF catalog with record reference
```

---

## Error Handling

### Validation Failures

```yaml
# On schema validation failure
validation_failure:
  action: log_and_continue
  
  logging:
    level: error
    fields:
      - record_id
      - record_type
      - validation_errors
      - request_id
      - scenario_id
  
  # Optionally send to dead letter queue for investigation
  dlq:
    enabled: true
    topic: "memory-records-dlq"
```

### Routing Failures

```yaml
# On routing failure (no store configured)
routing_failure:
  action: log_and_alert
  
  logging:
    level: error
    message: "No memory store configured for memory class"
    fields:
      - memory_class
      - record_type
      - scenario_id
  
  alert:
    severity: high
    channel: "ops-alerts"
```

---

## Monitoring & Metrics

### Key Metrics

| Metric | Description |
|--------|-------------|
| `sx.memory.records_routed` | Count of records routed, by memory_class and record_type |
| `sx.memory.routing_latency` | Latency from REQUEST_UPDATE to Atropos publish |
| `sx.memory.validation_failures` | Count of schema validation failures |
| `sx.memory.routing_failures` | Count of routing failures (no store configured) |

### Tracing

Memory record routing is traced as part of the request flow:

```yaml
trace:
  span_name: "route_memory_records"
  parent_span: "process_request_update"
  
  attributes:
    request_id: "req-12345"
    record_count: 2
    memory_classes: ["episodic"]
    record_types: ["decision_record", "evidence_bundle"]
  
  events:
    - name: "record_validated"
      record_id: "dec-abc123"
    - name: "record_enriched"
      record_id: "dec-abc123"
    - name: "record_published"
      record_id: "dec-abc123"
      topic: "fraud-ops-episodic-records"
```

---

## Related Documents

- [Signal Exchange README](./README.md) — Signal Exchange overview
- [Memory Services](../memory-services/README.md) — Memory architecture
- [Enterprise Memory](../memory-services/enterprise-memory/README.md) — Enterprise memory overview
- [CAF Store REST API](../cognitive-audit-fabric/episodic-memory-store/caf-store-rest-api.md) — Write API spec
- [Message Envelope](./message-envelope.md) — REQUEST_UPDATE format

---

*TODO: Detailed error recovery, batch optimization, cross-workbench scenarios*

