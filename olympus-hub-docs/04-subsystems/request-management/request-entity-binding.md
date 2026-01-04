# Request Entity Binding

> **Status:** 🔴 Stub — Placeholder for expansion

Request Entity Binding manages the **mapping between Requests and Business Entities**—enabling operations to work with domain-specific data.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Map requests to business entities |
| **Examples** | Dispute Request → Transaction Dispute Entity |
| **Components** | Bindings, transformations, entity events |

---

## From Todo Notes

> *"Request to Business Entity Mapping (ex: Dispute service request to Transaction Dispute Entity mapping; Bindings, transformations, Business Entity Events)"*

---

## Binding Concept

```
┌─────────────────┐     ┌─────────────────────────┐
│     Request     │────▶│    Business Entity      │
│                 │     │                         │
│  - request_id   │     │  - entity_type          │
│  - request_type │     │  - entity_id            │
│  - parameters   │     │  - entity_state         │
└─────────────────┘     └─────────────────────────┘
```

---

## Binding Types

| Type | Description |
|------|-------------|
| **Creates** | Request creates a new entity |
| **Updates** | Request updates existing entity |
| **References** | Request references entity (read-only) |
| **Aggregates** | Request spans multiple entities |

---

## Binding Definition

```yaml
entity_binding:
  request_type: "DisputeFilingRequest"
  entity_type: "TransactionDispute"
  
  binding:
    type: creates  # creates | updates | references
    
    # How to find/create the entity
    entity_lookup:
      key_fields:
        - request.transaction_id
    
    # Field mappings
    transformations:
      - source: request.customer_id
        target: entity.customer_id
      - source: request.transaction_id
        target: entity.transaction_reference
      - source: request.reason
        target: entity.dispute_reason
      - source: request.amount
        target: entity.disputed_amount
```

---

## Business Entity Events

When entities change, events are emitted:
- Entity created
- Entity updated
- Entity state changed
- Entity resolved

These events can trigger subsequent operations.

---

## Enterprise Memory Integration

From Todo notes:
> *"Request to Enterprise Memory (Decision Records, Override Records, Evidence Bundles, Explanation Records, etc.)"*

Request-entity bindings connect to:
- Decision records about the entity
- Evidence bundles related to the request
- Explanation records for entity decisions

---

## Related Documentation

- [Request Management Overview](./README.md)
- [Request Lifecycle](./request-lifecycle.md)
- [Hub Architecture - Business Entities](../../02-system-design/hub-architecture.md#12-business-entities)

---

*TODO: Detailed design — binding DSL, transformation engine, event publishing*

