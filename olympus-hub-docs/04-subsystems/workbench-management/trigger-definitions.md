# Trigger Definitions

> **Status:** 🔴 Stub — Placeholder for expansion

Defines how Triggers are configured within Workbenches.

---

## Overview

A **Trigger** binds Signals from Signal Providers to Scenarios:
- Matches signals based on conditions
- Transforms signals to Request format
- Routes to appropriate Scenario
- Defines response transformation for I/O Gateways

---

## Trigger Schema

```yaml
trigger:
  id: string
  name: string
  workbench_id: string
  
  # Signal source
  signal_source:
    provider: string        # atropos | cronus | heracles | dia | kale | custom
    gateway_config: object  # Provider-specific configuration
  
  # Matching conditions
  conditions:
    - field: string         # JSONPath to field in signal
      operator: string      # eq, ne, gt, lt, contains, matches, etc.
      value: any
    - field: string
      operator: string
      value: any
  
  # Transformation (signal → request)
  transformation:
    request_type: string    # ServiceRequest | BusinessRequest | SystemRequest
    mappings:
      - source: string      # JSONPath in signal
        target: string      # Field in request
    enrichments:
      - source: string      # External data source
        fields: array
  
  # Target scenario
  scenario_id: string
  
  # Request behavior
  request_behavior:
    mode: enum              # create_new | update_existing | create_or_update
    correlation_key: string # Field(s) for correlating updates
    idempotency_key: string # Field(s) for deduplication
  
  # Response transformation (for I/O Gateways)
  response:
    enabled: boolean        # Whether to send response
    success:
      template: object      # Success response mapping
    error:
      template: object      # Error response mapping
  
  # Access control
  access:
    auth_required: boolean
    auth_methods: array
    scopes: array
  
  # Metadata
  priority: number          # For multi-match ordering
  status: enum              # active | disabled
```

---

## Condition Operators

| Operator | Description |
|----------|-------------|
| `eq` | Equals |
| `ne` | Not equals |
| `gt` | Greater than |
| `lt` | Less than |
| `gte` | Greater than or equal |
| `lte` | Less than or equal |
| `contains` | String contains |
| `matches` | Regex match |
| `in` | Value in list |
| `exists` | Field exists |

---

## Transformation Mapping

```yaml
mappings:
  - source: "$.event.customer_id"
    target: "customer_id"
  - source: "$.event.transaction.amount"
    target: "disputed_amount"
  - source: "$.headers.X-Correlation-ID"
    target: "correlation_id"
  - source: "'DISPUTE_FILING'"   # Literal value
    target: "request_type"
```

---

## Related Documentation

- [Workbench Management Overview](./README.md)
- [Scenario Definitions](./scenario-definitions.md)
- [Signal Exchange - Trigger Evaluator](../signal-exchange/trigger-evaluator.md)

---

*TODO: Detailed design — condition DSL, enrichment sources, validation*

