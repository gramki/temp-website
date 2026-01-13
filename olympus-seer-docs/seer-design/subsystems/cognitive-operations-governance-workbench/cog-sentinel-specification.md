# COG Sentinel Specification

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-14  
> **Design Level**: C2 (Container) with C3 (Component) details for pattern matching

---

## Overview

A **COG Sentinel** is a Request Sentinel defined in a COGW workbench that operates across multiple target workbenches. This document specifies COG Sentinel labeling, cogSpec structure, and pattern matching behavior.

---

## COG Sentinel Definition

### What is a COG Sentinel

A COG Sentinel is a Request Sentinel with:

| Characteristic | Description |
|----------------|-------------|
| **Type** | `request` sentinel type |
| **Location** | Defined only in COGW workbenches |
| **Targeting** | Operates across multiple workbenches via cogSpec |
| **Visibility** | Read-only specs in target workbenches |
| **Controls** | Full control in COGW, enable/disable in targets |

### COG Sentinel vs Regular Request Sentinel

| Aspect | Request Sentinel | COG Sentinel |
|--------|------------------|--------------|
| **Definition Location** | Any workbench | COGW workbench only |
| **Target Scope** | Same workbench | Multiple workbenches |
| **Targeting Mechanism** | Implicit | Explicit (cogSpec patterns) |
| **Spec Visibility** | Single workbench | Multiple (read-only) |
| **Label** | None required | `sentinel.olympus.io/cog-sentinel: "true"` |
| **cogSpec** | Not present | Required |

---

## COG Sentinel Labeling

### Identification Requirements

A COG Sentinel is identified by two requirements:

1. **Label in SentinelSpec metadata**: `sentinel.olympus.io/cog-sentinel: "true"`
2. **Presence of cogSpec** in `SentinelScenarioDeploymentSpec`

### SentinelSpec with COG Label

```yaml
apiVersion: seer.olympus.io/v1
kind: SentinelSpec
metadata:
  name: token-governance-sentinel
  namespace: acme-cogw
  labels:
    sentinel.olympus.io/cog-sentinel: "true"  # Required COG Sentinel label
    workbench: acme-cogw
spec:
  type: request  # Must be 'request' type
  
  target:
    workbench_ids: ["acme-cogw"]  # Home workbench
  
  sentinel_scenario_specs:
    normative_ref:
      name: token-governance-normative
      version: "1.0.0"
    automation_ref:
      name: token-governance-automation
      version: "1.0.0"
    deployment_ref:
      name: token-governance-deployment
      version: "1.0.0"
```

### Validation Rules

| Rule | Description | Error |
|------|-------------|-------|
| **COGW Only** | COG Sentinel label only allowed in COGW workbenches | "COG Sentinel must be defined in COGW workbench" |
| **Type Request** | COG Sentinels must have `type: request` | "COG Sentinel must be request type" |
| **cogSpec Required** | Label requires cogSpec in deployment spec | "COG Sentinel requires cogSpec in deployment" |
| **Label Required** | cogSpec requires COG Sentinel label | "cogSpec requires COG Sentinel label" |

---

## cogSpec Structure

### Specification

The `cogSpec` section in `SentinelScenarioDeploymentSpec` defines target workbenches:

```yaml
apiVersion: seer.olympus.io/v1
kind: SentinelScenarioDeploymentSpec
metadata:
  name: token-governance-deployment
  namespace: acme-cogw
spec:
  automation_ref:
    name: token-governance-automation
    version: "1.0.0"
  
  activation:
    status: active
  
  # Standard sentinel_deployment section
  sentinel_deployment:
    auto_activate: true
    enrollment_limits:
      max_concurrent_requests: 100
  
  # ═══════════════════════════════════════════════════════════════════════════
  # COG SENTINEL TARGETING SECTION
  # ═══════════════════════════════════════════════════════════════════════════
  cogSpec:
    # Workbench patterns - evaluated sequentially (first match wins)
    workbench_patterns:
      - pattern: "production-*"     # Allow all production-* workbenches
        action: allow
      - pattern: "production-dev"   # But disallow production-dev
        action: disallow
      - pattern: "acme-*"           # Allow all acme-* workbenches
        action: allow
      - pattern: "test-*"           # Disallow all test-* workbenches
        action: disallow
```

### cogSpec Schema

```yaml
cogSpec:
  workbench_patterns:
    - pattern: string      # Workbench name pattern (wildcards supported)
      action: string       # "allow" | "disallow"
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `workbench_patterns` | array | Yes | Ordered list of pattern rules |
| `pattern` | string | Yes | Workbench name pattern with wildcard support |
| `action` | string | Yes | `allow` or `disallow` |

---

## Pattern Matching Algorithm (C3 Detail)

### Sequential Evaluation

Pattern matching uses Apache webserver-style sequential evaluation:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PATTERN MATCHING ALGORITHM                                │
│                                                                              │
│   For each workbench in subscription:                                        │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │ 1. Iterate patterns in order (top to bottom)                       │    │
│   │                                                                     │    │
│   │ 2. For each pattern:                                                │    │
│   │    a. Apply wildcard matching                                       │    │
│   │    b. If match:                                                     │    │
│   │       - If action = "allow" → Workbench IS targeted (stop)          │    │
│   │       - If action = "disallow" → Workbench NOT targeted (stop)      │    │
│   │    c. If no match → Continue to next pattern                        │    │
│   │                                                                     │    │
│   │ 3. If no pattern matches → Workbench NOT targeted (default deny)    │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Algorithm Steps

1. **Evaluate patterns in order** — Top to bottom
2. **First match wins** — Allow or disallow based on first matching pattern
3. **Default deny** — If no pattern matches, workbench is not targeted
4. **Wildcard matching** — `*` matches any sequence of characters

### Wildcard Matching

| Pattern | Matches | Does Not Match |
|---------|---------|----------------|
| `workbench-*` | `workbench-loans`, `workbench-payments` | `other-wb` |
| `*-prod` | `loans-prod`, `payments-prod` | `loans-dev` |
| `acme-*-prod` | `acme-loans-prod`, `acme-payments-prod` | `acme-loans-dev` |
| `*` | Everything | (nothing) |

### Example Evaluation

Given patterns:
```yaml
workbench_patterns:
  - pattern: "workbench-*"    # Pattern 1
    action: allow
  - pattern: "workbench-dev"  # Pattern 2
    action: disallow
  - pattern: "acme-*"         # Pattern 3
    action: allow
  - pattern: "test-*"         # Pattern 4
    action: disallow
```

Evaluation results:

| Workbench Name | Matched Pattern | Action | Result |
|----------------|-----------------|--------|--------|
| `workbench-loans` | Pattern 1: `workbench-*` | allow | ✅ Targeted |
| `workbench-dev` | Pattern 1: `workbench-*` | allow | ✅ Targeted (Note: Pattern 2 comes after) |
| `workbench-payments` | Pattern 1: `workbench-*` | allow | ✅ Targeted |
| `acme-disputes` | Pattern 3: `acme-*` | allow | ✅ Targeted |
| `test-sandbox` | Pattern 4: `test-*` | disallow | ❌ Not targeted |
| `other-wb` | (no match) | — | ❌ Not targeted |

**Important**: To exclude `workbench-dev`, the disallow pattern must come **before** the allow pattern:

```yaml
workbench_patterns:
  - pattern: "workbench-dev"  # Disallow first
    action: disallow
  - pattern: "workbench-*"    # Then allow the rest
    action: allow
```

### Common Pattern Strategies

| Strategy | Patterns | Description |
|----------|----------|-------------|
| **Allow all, exclude some** | Disallow patterns first, then `*` allow | Blacklist approach |
| **Deny all, include some** | Only allow patterns (default deny) | Whitelist approach |
| **Environment-based** | `*-prod` allow, `*-dev` disallow | Environment filtering |
| **Domain-based** | `lending-*` allow, `payments-*` allow | Domain targeting |

---

## Context Filtering

### Via TrainingSpec contextCompilation

COG Sentinel child requests access parent context via TrainingSpec:

```yaml
apiVersion: seer.olympus.io/v1
kind: TrainingSpec
metadata:
  name: token-governance-trained-agent
  namespace: acme-cogw
spec:
  rawAgent:
    name: governance-base
    version: "^1.0.0"
  
  context:
    identity:
      displayName: "Token Governance Agent"
      role: governance-sentinel
      domain: cognitive-governance
  
  # Context compilation configuration
  contextCompilation:
    retrieverConfigs:
      # When task is created, get full parent context
      - selector:
          updateType: "task_created"
        retrievers:
          - type: hub_request_context
            purpose: "parent request context"
            include:
              - request_id
              - scenario
              - workbench_id
              - context_records
              - metrics
          - type: enterprise_memory
            purpose: "precedents"
            query: "governance violations"
        tokenBudget:
          total: 8000
          allocation:
            parent_context: 5000
            precedents: 2000
            reserve: 1000
      
      # On token usage updates, get token metrics
      - selector:
          updateType: "context_update"
          contextKeys: ["token_metrics"]
        retrievers:
          - type: hub_request_context
            purpose: "token metrics"
            include:
              - metrics.token_usage
              - metrics.token_cost
        tokenBudget:
          total: 4000
      
      # Default fallback
      - selector: {}
        retrievers:
          - type: hub_request_context
            include:
              - request_id
              - scenario
```

### Context Compiler Integration

The Context Compiler automatically:

1. **Selects retrievers** based on request update metadata matching selector criteria
2. **Compiles context** from multiple sources (knowledge, memory, request hierarchy)
3. **Applies token budgets** to manage context size
4. **Ranks results** by relevance

---

## Full COG Sentinel Example

See [examples/cog-sentinel-example.md](./examples/cog-sentinel-example.md) for a complete example.

---

## Related Documentation

- [COGW Specification](./cogw-specification.md) — COGW workbench type
- [COGW Operator](./cogw-operator.md) — Operator reconciliation
- [Signal Forwarding](./signal-forwarding.md) — Signal forwarding mechanism
- [Training Spec Manager](../trained-agent-lifecycle-manager/training-spec-manager.md) — TrainingSpec validation
- [Context Compiler](../context-compiler/README.md) — Context compilation service

---

*COG Sentinel Specification defines the labeling, cogSpec structure, and Apache-style pattern matching for cross-workbench targeting.*
