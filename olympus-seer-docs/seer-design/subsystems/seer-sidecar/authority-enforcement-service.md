# Authority Enforcement Service

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-12  
> **Design Level**: C2 (Container)

---

## Overview

The Authority Enforcement Service ensures agents operate within their delegated authority limits. It provides **early enforcement** at the sidecar level for authority ceilings, complementing the authoritative enforcement at Tool Gateway and Signal Exchange.

**Key Principle**: Sidecar enforcement provides **defense in depth** — violations are caught early at the sidecar before reaching downstream systems.

---

## Authority Ceiling Architecture

### Layered Ceilings

Authority ceilings are layered, with each layer narrowing (never expanding) the authority:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AUTHORITY CEILING LAYERS                                  │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │            Bank/Organization Ceiling (Widest)                       │  │
│   │                                                                      │  │
│   │   ┌─────────────────────────────────────────────────────────────┐  │  │
│   │   │           Training Spec Ceiling                             │  │  │
│   │   │                                                              │  │  │
│   │   │   ┌─────────────────────────────────────────────────────┐  │  │  │
│   │   │   │        Employment Spec Ceiling                      │  │  │  │
│   │   │   │                                                      │  │  │  │
│   │   │   │   ┌─────────────────────────────────────────────┐  │  │  │  │
│   │   │   │   │     Request Context Ceiling (Narrowest)     │  │  │  │  │
│   │   │   │   └─────────────────────────────────────────────┘  │  │  │  │
│   │   │   │                                                      │  │  │  │
│   │   │   └─────────────────────────────────────────────────────┘  │  │  │
│   │   │                                                              │  │  │
│   │   └─────────────────────────────────────────────────────────────┘  │  │
│   │                                                                      │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│   Each layer can only narrow, never expand the authority                    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Ceiling Types

| Ceiling Type | Examples | Scope |
|--------------|----------|-------|
| **Value Ceilings** | `maxSingleTransaction`, `maxDailyTotal`, `maxPerCustomer` | Monetary/quantity limits |
| **Rate Ceilings** | `maxRequestsPerMinute`, `maxDecisionsPerHour` | Throughput limits |
| **Scope Ceilings** | `customerTiers`, `dataClasses`, `regions` | Access boundaries |
| **Approval Ceilings** | Threshold-based, always-required | Escalation triggers |

---

## Ceiling Configuration

### Training Spec Ceilings

```yaml
# In TrainingSpec
spec:
  authority:
    ceilings:
      value:
        maxSingleTransaction: 10000
        maxDailyTotal: 50000
        maxPerCustomer: 25000
      
      rate:
        maxDecisionsPerHour: 100
        maxToolInvocationsPerMinute: 30
      
      scope:
        customerTiers: ["standard", "premium"]
        dataClasses: ["public", "internal"]
        regions: ["US", "EU"]
      
      approval:
        thresholds:
          - amount: 5000
            requires: "supervisor_review"
          - amount: 10000
            requires: "manager_approval"
```

### Employment Spec Ceilings (Can Only Narrow)

```yaml
# In EmploymentSpec (stricter only)
spec:
  authority:
    ceilings:
      value:
        # Cannot exceed Training Spec limits
        maxSingleTransaction: 5000  # ✅ Narrower than 10000
        maxDailyTotal: 25000        # ✅ Narrower than 50000
      
      rate:
        maxDecisionsPerHour: 50     # ✅ Narrower than 100
      
      scope:
        customerTiers: ["standard"]  # ✅ Subset of ["standard", "premium"]
```

---

## Ceiling Evaluation Scope

The sidecar can evaluate ceilings on:

| Traffic Type | Ceiling Evaluation |
|--------------|-------------------|
| ✅ Inbound `/dispatch` requests | Value, scope ceilings on request content |
| ✅ Outbound Hub API calls | Value, scope ceilings on request updates, decisions |
| ⚠️ Tool invocations | Early enforcement; Tool Gateway enforces authoritatively |
| ⚠️ Model Gateway calls | Early enforcement; Model Gateway enforces authoritatively |

### Defense in Depth

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CEILING ENFORCEMENT FLOW                                  │
│                                                                              │
│   Agent Action                                                              │
│       │                                                                     │
│       ▼                                                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                 1. SIDECAR (Early Enforcement)                      │  │
│   │                 • Catches obvious violations early                  │  │
│   │                 • Reduces load on downstream systems                │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│       │                                                                     │
│       ▼                                                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │           2. TOOL GATEWAY / SIGNAL EXCHANGE (Authoritative)         │  │
│   │           • Full context evaluation                                 │  │
│   │           • Definitive enforcement                                  │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│       │                                                                     │
│       ▼                                                                     │
│   Action Proceeds or Rejected                                               │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Ceiling Immutability

| Action | Training Spec | Employment Spec |
|--------|---------------|-----------------|
| Define ceilings | ✅ Yes | ✅ Yes (narrower only) |
| Remove ceilings | ❌ No (once published) | ❌ No |
| Relax ceilings | N/A | ❌ No (cannot exceed Training) |
| Tighten ceilings | N/A | ✅ Yes |

---

## Request-Scoped Delegation Integration

For request-scoped authority delegation (where business users delegate authority to agents), the Authority Enforcement Service works in conjunction with the [Delegation Service](./delegation-service.md).

### Integration Points

| Component | Responsibility |
|-----------|----------------|
| **Delegation Service** | Pre-guardrail check for delegated authority, Authority Request initiation |
| **Authority Enforcement Service** | Ceiling enforcement, delegation chain validation |

### Delegation Token in Ceiling Evaluation

When evaluating authority ceilings, the service considers any active `Delegation Access Token`:

```python
def evaluate_ceiling(request, action):
    """Evaluate authority ceiling including delegation context."""
    # Get base ceilings from Training/Employment Spec
    base_ceilings = get_spec_ceilings(request.agent_id)
    
    # Check for active delegation token
    delegation_token = request.context.get("delegation_access_token")
    if delegation_token:
        # Validate token and extract delegated ceilings
        delegated_ceilings = validate_and_extract_ceilings(delegation_token)
        # Apply intersection (most restrictive)
        effective_ceilings = intersect_ceilings(base_ceilings, delegated_ceilings)
    else:
        effective_ceilings = base_ceilings
    
    # Evaluate action against effective ceilings
    return evaluate_against_ceilings(action, effective_ceilings)
```

---

## Delegation Chain Enforcement

### Authority Inheritance

Agent authority is always a subset of the delegator's current authority:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DELEGATION CHAIN                                          │
│                                                                              │
│   ┌─────────────────┐                                                       │
│   │ Bank Authority  │ ← Maximum possible authority                          │
│   └────────┬────────┘                                                       │
│            │                                                                 │
│            ▼                                                                 │
│   ┌─────────────────┐                                                       │
│   │ User Authority  │ ← User's current roles/permissions                    │
│   └────────┬────────┘                                                       │
│            │ delegation                                                      │
│            ▼                                                                 │
│   ┌─────────────────┐                                                       │
│   │ Agent Authority │ ← Cannot exceed delegator's authority                 │
│   └─────────────────┘                                                       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Delegation Chain Validation

The sidecar validates:

1. **Chain Integrity** — Delegation chain is valid and unbroken
2. **Authority Narrowing** — Each level is a subset of the parent
3. **Real-time Updates** — Authority changes are reflected in enforcement

---

## Real-time Authority Updates

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AUTHORITY CHANGE FLOW                                     │
│                                                                              │
│   IAM Authority Change                                                      │
│   (User role/scope change)                                                  │
│           │                                                                  │
│           ▼                                                                  │
│   ┌─────────────────┐                                                       │
│   │  IAM Observer   │ Detects change in delegator's authority               │
│   │    Service      │                                                       │
│   └────────┬────────┘                                                       │
│            │                                                                 │
│            ▼                                                                 │
│   ┌─────────────────┐                                                       │
│   │ Delegation Chain│ Recalculates agent's effective authority              │
│   │  Sync Service   │                                                       │
│   └────────┬────────┘                                                       │
│            │                                                                 │
│            ▼                                                                 │
│   ┌─────────────────┐                                                       │
│   │ Sidecar Config  │ Hot-reload with new authority ceilings                │
│   │     Update      │                                                       │
│   └─────────────────┘                                                       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## OPA Policy Integration

The Authority Enforcement Service uses OPA for policy evaluation:

```yaml
# Authority ceiling policy
spec:
  authority:
    ceilings:
      value:
        maxSingleTransaction: 5000
    
    opaPolicy: |
      package seer.authority.ceiling
      
      default decision = "ALLOW"
      
      decision = "DENY" {
        input.action.amount > data.ceilings.value.maxSingleTransaction
      }
      
      reason = sprintf("Amount %d exceeds ceiling of %d", [
        input.action.amount,
        data.ceilings.value.maxSingleTransaction
      ]) {
        input.action.amount > data.ceilings.value.maxSingleTransaction
      }
```

---

## Integration Points

### Agent Lifecycle Manager
- Authority ceilings from Employment Spec → Runtime enforcement configuration
- Ceiling changes trigger configuration reload

### Cipher IAM Extensions
- Authority delegation → IAM profile context
- Delegator authority → Agent authority ceiling

### Delegation Chain Sync Service
- Authority changes → Runtime authority updates
- Chain validation → Integrity checks

### OPA Policy Engine
- Authority ceiling policies → Policy evaluation
- Per-PEP policy references

### Tool Gateway (Authoritative)
- Tool invocation ceilings → Authoritative enforcement
- Sidecar provides early enforcement only

### Model Gateway (Authoritative)
- Model invocation ceilings → Authoritative enforcement
- Sidecar provides early enforcement only

### Signal Exchange
- Request update ceilings → Enforced by sidecar on outbound calls

---

## Observability

### Metrics

| Metric | Description |
|--------|-------------|
| `seer_ceiling_evaluation_total` | Total ceiling evaluations |
| `seer_ceiling_violation_total` | Ceiling violations by type |
| `seer_delegation_chain_update_total` | Authority updates processed |
| `seer_ceiling_enforcement_latency_seconds` | Evaluation latency |

### Violation Recording

All ceiling violations are recorded:

```json
{
  "record_type": "authority_violation",
  "request_id": "req-abc123",
  "agent_id": "fraud-analyst-001",
  "enforcement_point": "sidecar",
  "ceiling_type": "value",
  "ceiling_name": "maxSingleTransaction",
  "ceiling_value": 5000,
  "attempted_value": 7500,
  "decision": "DENY",
  "timestamp": "2026-01-12T14:30:00Z"
}
```

---

## Related Documentation

- [Delegation Service](./delegation-service.md) — Request-scoped delegation management
- [Policy Enforcement Service](./policy-enforcement-service.md) — OPA policy evaluation
- [Guardrail Service](./guardrail-service.md) — Request/response enforcement
- [Authority Enforcement Concepts](../../implementation-concepts/authority-enforcement.md) — Conceptual overview
- [Request-Scoped Authority Delegation](../../implementation-concepts/request-scoped-delegation.md) — End-to-end delegation design
- [Agent Lifecycle Manager](../agent-lifecycle-manager/README.md) — Ceiling configuration
- [ADR-0073: Authority Enforcement via OPA](../../../../olympus-hub-docs/decision-logs/0073-seer-authority-enforcement-opa.md)

---

*Authority Enforcement Service provides early enforcement of authority ceilings at the sidecar level, with layered ceiling architecture and real-time delegation chain validation.*
