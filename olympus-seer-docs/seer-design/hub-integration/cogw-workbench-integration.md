# COGW Workbench Integration

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-14

---

## Overview

This document describes how Cognitive Operations Governance Workbenches (COGWs) integrate with Hub Workbench Management, including workbench type extension, default COGW creation, and workbench enumeration for the COGW Operator.

---

## Workbench Type Extension

### Extended Workbench Type Enum

Hub Workbench Management extends the `workbench_type` field to include `cogw`:

```yaml
workbench_type: "business" | "devops" | "cogw"
```

| Type | Purpose | Introduced In |
|------|---------|---------------|
| `business` | Standard operational workbenches (default) | Hub 1.0 |
| `devops` | Development operations workbenches | Hub 1.5 |
| `cogw` | Cognitive Operations Governance Workbenches | Seer 1.0 |

### Workbench Type Validation

| Rule | Description |
|------|-------------|
| **Valid Values** | `workbench_type` must be one of: `business`, `devops`, `cogw` |
| **Default** | If not specified, defaults to `business` |
| **Immutable** | Cannot change `workbench_type` after creation |
| **COG Sentinel Constraint** | COG Sentinels only allowed in `cogw` workbenches |

---

## Default COGW Creation

### Integration with Subscription Lifecycle

Default COGW creation is integrated with Hub Subscription Management:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DEFAULT COGW CREATION FLOW                                │
│                                                                              │
│   Hub Subscription Management                                                │
│   ──────────────────────────                                                 │
│                                                                              │
│   ┌────────────────────────┐                                                 │
│   │ Subscription Created   │                                                 │
│   │ ├── subscription_id    │                                                 │
│   │ └── tier               │                                                 │
│   └───────────┬────────────┘                                                 │
│               │                                                               │
│               ▼                                                               │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │ Subscription Provisioning Operator                                  │    │
│   │                                                                     │    │
│   │ 1. Provision standard resources (data stores, etc.)                │    │
│   │ 2. Check if COGW is enabled for tier                               │    │
│   │ 3. If enabled: Create default COGW workbench                       │    │
│   │ 4. Apply COGW Blueprint to workbench                               │    │
│   └─────────────────────────────┬──────────────────────────────────────┘    │
│                                 │                                            │
│                                 ▼                                            │
│   ┌────────────────────────────────────────────────────────────────────┐    │
│   │ Hub Workbench Management                                            │    │
│   │                                                                     │    │
│   │ 1. Create workbench with type: cogw                                │    │
│   │ 2. Apply scenarios from COGW Blueprint                              │    │
│   │ 3. Register with COGW Operator                                      │    │
│   └────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Tier-Based COGW Availability

| Subscription Tier | Default COGW | Custom COGWs |
|-------------------|--------------|--------------|
| Starter | ❌ Not included | ❌ Not available |
| Professional | ✅ Included | ❌ Not available |
| Enterprise | ✅ Included | ✅ Unlimited |
| Custom | Configurable | Configurable |

### Default COGW Configuration

```yaml
# Default COGW created by Subscription Provisioning Operator
apiVersion: hub.olympus.io/v1
kind: Workbench
metadata:
  name: ${subscription_id}-default-cogw
  namespace: ${subscription_namespace}
  labels:
    hub.olympus.io/workbench-type: cogw
    hub.olympus.io/default-cogw: "true"
    hub.olympus.io/managed-by: subscription-provisioning
  annotations:
    hub.olympus.io/created-by: subscription-provisioning
    hub.olympus.io/blueprint-ref: cogw-default-blueprint/1.0.0
spec:
  domain: cognitive-governance
  description: "Default Cognitive Operations Governance Workbench"
  workbench_type: cogw
  dev_lifecycle_stage: PROD
  
  # Scenarios populated from Blueprint
  scenarios: []  # Populated by Blueprint application
```

---

## COGW Blueprint Structure

### BlueprintSpec for COGW

```yaml
apiVersion: hub.olympus.io/v1
kind: WorkbenchBlueprintSpec
metadata:
  name: cogw-default-blueprint
  labels:
    hub.olympus.io/blueprint-type: cogw
    hub.olympus.io/platform-provided: "true"
spec:
  display_name: "Default COGW Blueprint"
  description: "Standard governance scenarios for cognitive operations"
  version: "1.0.0"
  
  workbench:
    workbench_type: cogw
    domain: cognitive-governance
  
  scenarios:
    - id: token-usage-governance
      normative:
        name: token-usage-governance
        display_name: "Token Usage Governance"
        goals:
          primary:
            description: "Monitor and enforce token budgets"
      automation:
        sentinel:
          participation:
            mode: observe_and_participate
      deployment:
        activation:
          status: active
        cogSpec:
          workbench_patterns:
            - pattern: "*-cogw"
              action: disallow
            - pattern: "*"
              action: allow
    
    - id: compliance-sampling
      normative:
        name: compliance-sampling
        display_name: "Compliance Sampling"
      automation:
        sentinel:
          participation:
            mode: observe
      deployment:
        activation:
          status: active
    
    - id: quality-assurance-sampling
      normative:
        name: quality-assurance-sampling
        display_name: "Quality Assurance Sampling"
      deployment:
        activation:
          status: draft  # Not active by default
    
    - id: security-monitoring
      normative:
        name: security-monitoring
        display_name: "Security Monitoring"
      deployment:
        activation:
          status: draft  # Not active by default
```

---

## Workbench Enumeration API

### API for COGW Operator

The COGW Operator requires an API to enumerate workbenches in a subscription:

```yaml
# API: List Workbenches in Subscription
endpoint: /api/v1/subscriptions/{subscription_id}/workbenches
method: GET
parameters:
  - name: subscription_id
    in: path
    required: true
  - name: workbench_type
    in: query
    required: false
    description: "Filter by workbench type (business, devops, cogw)"
  - name: exclude_types
    in: query
    required: false
    description: "Exclude workbench types from results"

response:
  items:
    - id: string
      name: string
      namespace: string
      workbench_type: string
      status: string
      created_at: string
```

### Example API Call

```bash
# List all non-COGW workbenches (for pattern evaluation)
GET /api/v1/subscriptions/acme-subscription/workbenches?exclude_types=cogw

# Response
{
  "items": [
    {
      "id": "production-loans",
      "name": "production-loans",
      "namespace": "acme-subscription",
      "workbench_type": "business",
      "status": "active",
      "created_at": "2026-01-01T00:00:00Z"
    },
    {
      "id": "production-payments",
      "name": "production-payments",
      "namespace": "acme-subscription",
      "workbench_type": "business",
      "status": "active",
      "created_at": "2026-01-02T00:00:00Z"
    },
    {
      "id": "devops-central",
      "name": "devops-central",
      "namespace": "acme-subscription",
      "workbench_type": "devops",
      "status": "active",
      "created_at": "2026-01-03T00:00:00Z"
    }
  ]
}
```

### Watch API for Changes

```yaml
# API: Watch Workbenches in Subscription
endpoint: /api/v1/subscriptions/{subscription_id}/workbenches/watch
method: GET
parameters:
  - name: subscription_id
    in: path
    required: true
  - name: resource_version
    in: query
    required: false
    description: "Start watching from this version"

response:
  type: stream
  events:
    - type: ADDED | MODIFIED | DELETED
      object:
        id: string
        name: string
        workbench_type: string
```

---

## Cross-Workbench Context Access

### COGW Context Token

When a COG Sentinel creates a child request in COGW, it needs access to the parent request context in the target workbench. This uses the same mechanism as Cross-Workbench Context Sharing:

```yaml
# Child request in COGW with cross-workbench parent
apiVersion: hub.olympus.io/v1
kind: Request
metadata:
  name: cog-req-67890
  namespace: acme-cogw
spec:
  scenario: token-governance
  
  parent:
    request_id: req-12345
    workbench_id: production-loans
    cross_workbench: true
    context_token: "jwt-token-for-context-access"
  
  # ...
```

### Automatic Context Sharing

For COGW child requests, context sharing is **automatic** because:

1. **Same Subscription** — COGW and target workbench are in the same subscription
2. **COGW Privilege** — COGW workbenches have implicit read access to all workbenches in subscription
3. **Governance Purpose** — Context access is required for governance functions

### Context Sharing Configuration

```yaml
# Implicit context sharing for COGW
apiVersion: hub.olympus.io/v1
kind: WorkbenchContextSharingSpec
metadata:
  name: cogw-implicit-sharing
  namespace: acme-subscription
spec:
  workbench_ref:
    name: acme-cogw
    workbench_type: cogw
  
  # COGW implicitly has parent context access to all workbenches
  parent_contexts:
    - type: all_subscription_workbenches
      enabled: true
      access_scope: read_only
```

---

## Integration Points Summary

| Hub Component | Integration | Direction |
|---------------|-------------|-----------|
| **Workbench Management** | `workbench_type: cogw` | Hub ← Seer |
| **Subscription Management** | Default COGW creation | Hub → Seer |
| **Workbench Enumeration** | API for COGW Operator | Hub → Seer |
| **Cross-Workbench Context** | Automatic for COGW | Hub ↔ Seer |
| **Signal Exchange** | COG Sentinel registration | Seer → Hub |
| **Request Hierarchy** | Cross-workbench child requests | Seer → Hub |

---

## Related Documentation

- [COGW Specification](../subsystems/cognitive-operations-governance-workbench/cogw-specification.md) — Workbench type details
- [COGW Operator](../subsystems/cognitive-operations-governance-workbench/cogw-operator.md) — Operator using these APIs
- [Hub Workbench Management](../../../olympus-hub-docs/04-subsystems/workbench-management/README.md) — Hub workbench documentation
- [Cross-Workbench Context Sharing](../../../olympus-hub-docs/02-system-design/implementation-concepts/workbench-context-sharing.md) — Context sharing pattern
- [Subscription Management](../../../olympus-hub-docs/04-subsystems/subscription-management/README.md) — Subscription lifecycle

---

*COGW Workbench Integration extends Hub's workbench model with the `cogw` type, default COGW creation at subscription provisioning, and workbench enumeration APIs for cross-workbench governance.*
