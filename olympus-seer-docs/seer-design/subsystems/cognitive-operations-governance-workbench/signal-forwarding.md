# Signal Forwarding

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-14  
> **Design Level**: C2 (Container)

---

## Overview

Signal Forwarding describes how request updates from target workbenches are filtered and forwarded to COG Sentinels in COGW workbenches. Filtering happens locally in the target workbench's Signal Exchange before forwarding.

---

## Signal Flow Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    COG SENTINEL SIGNAL FORWARDING                            │
│                                                                              │
│   TARGET WORKBENCH                           COGW WORKBENCH                  │
│   ────────────────                           ──────────────                  │
│                                                                              │
│   ┌────────────────┐                                                         │
│   │ Request Created│                                                         │
│   │ or Updated     │                                                         │
│   └───────┬────────┘                                                         │
│           │                                                                   │
│           ▼                                                                   │
│   ┌────────────────────────────────────────┐                                 │
│   │ Signal Exchange (Target WB)            │                                 │
│   │                                         │                                 │
│   │ 1. Check registered COG Sentinels      │                                 │
│   │ 2. Evaluate participation.filters      │                                 │
│   │    - scenario_whitelist/blacklist      │                                 │
│   │    - on_request_update OPA policy      │                                 │
│   │ 3. If match → Forward signal           │                                 │
│   │ 4. If no match → No action             │                                 │
│   │                                         │                                 │
│   └───────────────────┬────────────────────┘                                 │
│                       │                                                       │
│                       │ (Only if filters match)                               │
│                       ▼                                                       │
│                   ┌──────────────────────────────────────────────┐           │
│                   │ Signal Forwarding                            │           │
│                   │                                               │           │
│                   │ • Request update payload                      │           │
│                   │ • Source workbench ID                         │           │
│                   │ • Source request ID                           │           │
│                   │ • COG Sentinel reference                      │           │
│                   │                                               │           │
│                   └───────────────────────┬──────────────────────┘           │
│                                           │                                   │
│                                           ▼                                   │
│                               ┌───────────────────────────────────┐          │
│                               │ Signal Exchange (COGW)            │          │
│                               │                                    │          │
│                               │ 1. Receive forwarded signal       │          │
│                               │ 2. Create child request           │          │
│                               │ 3. Notify COG Sentinel via webhook │          │
│                               │                                    │          │
│                               └───────────────────────────────────┘          │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Filtering Mechanism

### Filter Evaluation Location

Filtering happens **locally** in the target workbench's Signal Exchange:

| Aspect | Description |
|--------|-------------|
| **Location** | Target workbench Signal Exchange |
| **Timing** | When request created or updated |
| **Evaluation** | Per-registered COG Sentinel |
| **Result** | Forward or no action |

### Filter Types

| Filter Type | Purpose | Configured In |
|-------------|---------|---------------|
| `scenario_whitelist` | Only process requests from listed scenarios | `SentinelScenarioAutomationSpec` |
| `scenario_blacklist` | Exclude requests from listed scenarios | `SentinelScenarioAutomationSpec` |
| `on_request_update` | OPA policy for fine-grained filtering | `SentinelScenarioAutomationSpec` |

### Filter Configuration Example

```yaml
apiVersion: seer.olympus.io/v1
kind: SentinelScenarioAutomationSpec
metadata:
  name: token-governance-automation
  namespace: acme-cogw
spec:
  # ... standard fields ...
  
  sentinel:
    participation:
      mode: observe_and_participate
      filters:
        # Scenario-level filtering
        scenario_whitelist:
          - "*"  # All scenarios (or specific list)
        scenario_blacklist:
          - "internal-testing"
          - "development-*"
        
        # Update-level filtering via OPA policy
        on_request_update:
          enabled: true
          update_filter_policy: |
            package seer.sentinel.token_filter
            
            default allow = false
            
            # Allow if token usage is reported
            allow {
              input.payload.metrics.token_usage != null
            }
            
            # Allow if request is completed
            allow {
              input.payload.status == "completed"
            }
            
            # Allow if token cost exceeds threshold
            allow {
              input.payload.metrics.token_cost > 50
            }
```

---

## Filter Evaluation Flow

### Step-by-Step Evaluation

1. **Request Event** — Request created or updated in target workbench
2. **Registered COG Sentinels** — Signal Exchange checks all registered COG Sentinels for this workbench
3. **For Each COG Sentinel**:
   - Check `scenario_whitelist` — Request's scenario must match
   - Check `scenario_blacklist` — Request's scenario must not match
   - Evaluate `on_request_update` OPA policy — Policy must allow
4. **Result**:
   - All checks pass → Forward signal to COGW
   - Any check fails → No action

### Evaluation Pseudocode

```python
def evaluate_cog_sentinel_filters(request_update, cog_sentinel):
    filters = cog_sentinel.automation_spec.sentinel.participation.filters
    
    # 1. Check scenario whitelist
    if filters.scenario_whitelist:
        if not matches_any(request_update.scenario, filters.scenario_whitelist):
            return False  # Scenario not in whitelist
    
    # 2. Check scenario blacklist
    if filters.scenario_blacklist:
        if matches_any(request_update.scenario, filters.scenario_blacklist):
            return False  # Scenario in blacklist
    
    # 3. Evaluate OPA policy
    if filters.on_request_update.enabled:
        policy = filters.on_request_update.update_filter_policy
        result = opa_evaluate(policy, request_update)
        if not result.allow:
            return False  # OPA policy denied
    
    return True  # All filters passed
```

---

## Signal Forwarding

### Forwarded Signal Payload

When a signal is forwarded to COGW:

```yaml
forwarded_signal:
  # Source information
  source:
    workbench_id: production-loans
    request_id: req-12345
    scenario: loan-application
    
  # Original request update
  payload:
    update_type: task_completed
    task_id: task-789
    status: completed
    metrics:
      token_usage: 1500
      token_cost: 75.00
    context:
      customer_id: cust-456
      loan_amount: 50000
  
  # COG Sentinel reference
  cog_sentinel:
    name: token-governance-sentinel
    workbench: acme-cogw
    
  # Metadata
  metadata:
    forwarded_at: "2026-01-14T10:30:00Z"
    filter_match:
      scenario_match: true
      opa_policy_match: true
```

---

## Child Request Creation

### In COGW Workbench

When COGW Signal Exchange receives a forwarded signal:

1. **Create Child Request** — In COGW workbench, using COG Sentinel's scenario
2. **Set Parent Reference** — Cross-workbench parent reference to source request
3. **Inherit Context** — Access parent context via request hierarchy
4. **Notify Sentinel** — Deliver webhook to COG Sentinel's Employed Agent

### Child Request Structure

```yaml
apiVersion: hub.olympus.io/v1
kind: Request
metadata:
  name: cog-req-67890
  namespace: acme-cogw
spec:
  scenario: token-governance
  
  # Cross-workbench parent reference
  parent:
    request_id: req-12345
    workbench_id: production-loans
    cross_workbench: true
    context_token: "jwt-token-for-context-access"
  
  # Request created for COG Sentinel
  assignees:
    - type: sentinel
      id: token-governance-sentinel
  
  # Initial context from forwarded signal
  initial_context:
    source_workbench: production-loans
    source_scenario: loan-application
    source_metrics:
      token_usage: 1500
      token_cost: 75.00
```

---

## Context Compilation

### Access to Parent Context

COG Sentinel child requests access parent context via Context Compiler:

| Source | Access | Description |
|--------|--------|-------------|
| Parent Request Context | Via context token | Full ancestor chain access |
| Source Workbench | Via cross-workbench context | Same-subscription access |
| COG Sentinel's TrainingSpec | Retriever configuration | Controls what context to include |

### Context Compilation Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    COG SENTINEL CONTEXT COMPILATION                          │
│                                                                              │
│   1. COG Sentinel receives webhook notification                              │
│                                                                              │
│   2. COG Sentinel invokes Context Compiler:                                  │
│      context = compiler.compile(                                             │
│          request_id=cog_request_id,                                          │
│          update_id=current_update_id                                         │
│      )                                                                       │
│                                                                              │
│   3. Context Compiler:                                                       │
│      a. Loads TrainingSpec retriever configurations                          │
│      b. Matches request update against selectors                             │
│      c. Retrieves from sources:                                              │
│         - hub_request_context (includes cross-workbench parent)              │
│         - enterprise_memory (if configured)                                  │
│         - knowledge_base (if configured)                                     │
│      d. Applies token budgets and ranking                                    │
│      e. Returns compiled context                                             │
│                                                                              │
│   4. COG Sentinel has access to:                                             │
│      - Parent request context (from source workbench)                        │
│      - Enterprise memory (precedents, patterns)                              │
│      - Knowledge (policies, rules)                                           │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### TrainingSpec Configuration

```yaml
spec:
  contextCompilation:
    retrieverConfigs:
      - selector:
          updateType: "task_created"
        retrievers:
          # Get parent request context (cross-workbench)
          - type: hub_request_context
            purpose: "parent request context"
            include:
              - request_id
              - scenario
              - workbench_id
              - context_records
              - metrics
              - ancestor_chain  # Full ancestry
          # Get governance precedents
          - type: enterprise_memory
            purpose: "governance precedents"
            query: "token violations, budget breaches"
            limit: 10
        tokenBudget:
          total: 8000
          allocation:
            parent_context: 5000
            precedents: 2000
            reserve: 1000
```

---

## Webhook Delivery

### Webhook Configuration

COG Sentinel webhooks are configured in `SentinelScenarioDeploymentSpec`:

```yaml
sentinel_deployment:
  notification_delivery:
    method: webhook
    retry_policy:
      max_attempts: 3
      initial_delay_ms: 1000
      max_delay_ms: 30000
      backoff_multiplier: 2.0
    timeout_ms: 5000
```

### Webhook Payload

```yaml
webhook_payload:
  event: REQUEST_UPDATE
  
  # Child request in COGW
  request:
    id: cog-req-67890
    workbench_id: acme-cogw
    scenario: token-governance
  
  # Update details
  update:
    id: update-123
    type: task_created
    timestamp: "2026-01-14T10:30:00Z"
  
  # Source information
  source:
    workbench_id: production-loans
    request_id: req-12345
    scenario: loan-application
  
  # Forwarded metrics
  metrics:
    token_usage: 1500
    token_cost: 75.00
```

---

## Related Documentation

- [COG Sentinel Specification](./cog-sentinel-specification.md) — COG Sentinel definition
- [COGW Operator](./cogw-operator.md) — Signal Exchange registration
- [Signal Exchange](../../../../olympus-hub-docs/04-subsystems/signal-exchange/README.md) — Hub Signal Exchange
- [Request Hierarchy](../../../../olympus-hub-docs/04-subsystems/request-management/request-hierarchy.md) — Cross-workbench requests
- [Context Compiler](../context-compiler/README.md) — Context compilation service

---

*Signal Forwarding enables COG Sentinels to observe and participate in requests across the subscription through filtered, forwarded signals and cross-workbench child requests.*
