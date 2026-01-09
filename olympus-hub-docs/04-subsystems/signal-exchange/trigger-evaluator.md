# Trigger Evaluator

> **Status:** 🔴 Stub — Placeholder for expansion

The Trigger Evaluator matches incoming signals against trigger definitions and executes transformations to create Request payloads.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Match signals to triggers, execute transformations |
| **Input** | Signals from Signal Providers |
| **Output** | Transformed payloads for Request Factory |
| **Configuration** | Trigger definitions from Workbench Management |

---

## Responsibilities

| Function | Description |
|----------|-------------|
| **Trigger Loading** | Load and cache trigger definitions from Workbench Management |
| **Signal Matching** | Evaluate signal against trigger conditions |
| **Transformation** | Apply trigger transformation rules |
| **Context Enrichment** | Fetch additional context for transformation |
| **Multi-match Handling** | Handle signals that match multiple triggers |

---

## Trigger Definition Structure

Trigger definitions are maintained in Workbench Management:

```yaml
trigger:
  id: string
  name: string
  workbench_id: string
  
  # Signal matching
  signal_source: string      # Which Signal Provider
  conditions:                # Matching conditions
    - field: string
      operator: string
      value: any
  
  # Transformation
  transformation:
    request_type: string
    mappings:
      - source: string       # JSONPath in signal
        target: string       # Field in request
    enrichments:
      - source: string       # External data source
        fields: array
  
  # Target
  scenario_id: string        # Which Scenario to activate
  
  # Behavior
  create_or_update: enum     # create_new | update_existing | create_or_update
  idempotency_key: string    # Field(s) for deduplication
```

---

## Matching Algorithm

```
For each incoming signal:
  1. Identify Signal Provider source
  2. Load triggers for that source (cached)
  3. For each trigger:
     a. Evaluate conditions against signal
     b. If all conditions match → trigger matches
  4. Handle match results:
     - No matches → log and discard (or dead-letter)
     - Single match → proceed to transformation
     - Multiple matches → apply multi-match policy
```

---

## Multi-Match Policies

| Policy | Description |
|--------|-------------|
| **First Match** | Use first matching trigger (by priority) |
| **All Matches** | Create request for each matching trigger |
| **Error** | Treat as configuration error |

---

## Related Documentation

- [Signal Exchange Overview](./README.md)
- [Request Factory](./request-factory.md)
- [Workbench Management](../workbench-management/README.md)

---

*TODO: Detailed design — condition operators, transformation DSL, caching strategy*

