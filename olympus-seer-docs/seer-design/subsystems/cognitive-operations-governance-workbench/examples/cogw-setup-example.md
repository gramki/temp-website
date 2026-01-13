# COGW Setup Example: Default COGW Configuration

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-14

---

## Overview

This example demonstrates the default COGW setup that every subscription receives at creation, including the COGW workbench, standard governance scenarios, and initial COG Sentinels.

---

## Default COGW Creation Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DEFAULT COGW CREATION                                     │
│                                                                              │
│   1. Subscription Created                                                    │
│      ├── subscription_id: acme-subscription                                  │
│      └── tier: enterprise                                                    │
│                                                                              │
│   2. Subscription Provisioning Operator                                      │
│      ├── Detects new subscription                                            │
│      └── Triggers default COGW creation                                      │
│                                                                              │
│   3. Default COGW Created                                                    │
│      ├── Name: acme-subscription-default-cogw                                │
│      ├── Type: cogw                                                          │
│      └── Content: Standard governance scenarios                              │
│                                                                              │
│   4. COGW Operator Initialized                                               │
│      ├── Watches COGW workbenches                                            │
│      └── Ready to sync COG Sentinels                                         │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Default COGW Workbench

```yaml
apiVersion: hub.olympus.io/v1
kind: Workbench
metadata:
  name: acme-subscription-default-cogw
  namespace: acme-subscription
  labels:
    hub.olympus.io/workbench-type: cogw
    hub.olympus.io/default-cogw: "true"
  annotations:
    hub.olympus.io/created-by: subscription-provisioning
    hub.olympus.io/created-at: "2026-01-14T00:00:00Z"
spec:
  domain: cognitive-governance
  description: "Default Cognitive Operations Governance Workbench for ACME Subscription"
  
  workbench_type: cogw
  dev_lifecycle_stage: PROD
  
  # Standard governance scenarios from Blueprint
  scenarios:
    - id: token-usage-governance
      name: "Token Usage Governance"
      application_id: token-governance-app
      description: "Monitor and enforce token budgets across workbenches"
    
    - id: compliance-sampling
      name: "Compliance Sampling"
      application_id: compliance-app
      description: "Sample and verify AI decisions for regulatory compliance"
    
    - id: quality-assurance-sampling
      name: "Quality Assurance Sampling"
      application_id: qa-app
      description: "Evaluate AI output quality across agents"
    
    - id: security-monitoring
      name: "Security Monitoring"
      application_id: security-app
      description: "Detect security-relevant patterns and anomalies"
  
  # Standard governance triggers
  triggers:
    - id: token-alert-trigger
      signal_source: cronus
      conditions:
        - event_type: "token_usage_alert"
      scenario_id: token-usage-governance
    
    - id: compliance-trigger
      signal_source: heracles
      conditions:
        - event_type: "scheduled"
          schedule: "0 */4 * * *"  # Every 4 hours
      scenario_id: compliance-sampling
  
  # COGW has broad access for governance
  machine_access:
    - all-subscription-workbenches
  
  # Governance request policies
  request_policies:
    lifecycle:
      max_depth: 3
      timeout_hours: 24
    storage:
      retention_days: 365  # Long retention for governance
```

---

## Standard COG Sentinels

### Token Usage Governance Sentinel

```yaml
apiVersion: seer.olympus.io/v1
kind: SentinelSpec
metadata:
  name: token-usage-governance-sentinel
  namespace: acme-subscription-default-cogw
  labels:
    sentinel.olympus.io/cog-sentinel: "true"
    sentinel.olympus.io/standard-sentinel: "true"
spec:
  type: request
  target:
    workbench_ids: ["acme-subscription-default-cogw"]
  sentinel_scenario_specs:
    normative_ref:
      name: token-usage-governance-normative
      version: "1.0.0"
    automation_ref:
      name: token-usage-governance-automation
      version: "1.0.0"
    deployment_ref:
      name: token-usage-governance-deployment
      version: "1.0.0"

---
apiVersion: seer.olympus.io/v1
kind: SentinelScenarioDeploymentSpec
metadata:
  name: token-usage-governance-deployment
  namespace: acme-subscription-default-cogw
spec:
  automation_ref:
    name: token-usage-governance-automation
    version: "1.0.0"
  activation:
    status: active
  sentinel_deployment:
    auto_activate: true
    enrollment_limits:
      max_concurrent_requests: 500
  cogSpec:
    workbench_patterns:
      # Exclude all COGW workbenches
      - pattern: "*-cogw"
        action: disallow
      - pattern: "*-default-cogw"
        action: disallow
      # Exclude test/dev workbenches
      - pattern: "dev-*"
        action: disallow
      - pattern: "test-*"
        action: disallow
      # Allow all other workbenches
      - pattern: "*"
        action: allow
```

### Compliance Sampling Sentinel

```yaml
apiVersion: seer.olympus.io/v1
kind: SentinelSpec
metadata:
  name: compliance-sampling-sentinel
  namespace: acme-subscription-default-cogw
  labels:
    sentinel.olympus.io/cog-sentinel: "true"
    sentinel.olympus.io/standard-sentinel: "true"
spec:
  type: request
  target:
    workbench_ids: ["acme-subscription-default-cogw"]
  sentinel_scenario_specs:
    normative_ref:
      name: compliance-sampling-normative
      version: "1.0.0"
    automation_ref:
      name: compliance-sampling-automation
      version: "1.0.0"
    deployment_ref:
      name: compliance-sampling-deployment
      version: "1.0.0"

---
apiVersion: seer.olympus.io/v1
kind: SentinelScenarioDeploymentSpec
metadata:
  name: compliance-sampling-deployment
  namespace: acme-subscription-default-cogw
spec:
  automation_ref:
    name: compliance-sampling-automation
    version: "1.0.0"
  activation:
    status: active  # Starts active by default
  sentinel_deployment:
    auto_activate: true
    enrollment_limits:
      max_concurrent_requests: 100
  cogSpec:
    workbench_patterns:
      # Only monitor production workbenches
      - pattern: "*-cogw"
        action: disallow
      - pattern: "dev-*"
        action: disallow
      - pattern: "test-*"
        action: disallow
      - pattern: "production-*"
        action: allow
```

### Quality Assurance Sentinel

```yaml
apiVersion: seer.olympus.io/v1
kind: SentinelSpec
metadata:
  name: qa-sampling-sentinel
  namespace: acme-subscription-default-cogw
  labels:
    sentinel.olympus.io/cog-sentinel: "true"
    sentinel.olympus.io/standard-sentinel: "true"
spec:
  type: request
  target:
    workbench_ids: ["acme-subscription-default-cogw"]
  sentinel_scenario_specs:
    normative_ref:
      name: qa-sampling-normative
      version: "1.0.0"
    automation_ref:
      name: qa-sampling-automation
      version: "1.0.0"
    deployment_ref:
      name: qa-sampling-deployment
      version: "1.0.0"

---
apiVersion: seer.olympus.io/v1
kind: SentinelScenarioDeploymentSpec
metadata:
  name: qa-sampling-deployment
  namespace: acme-subscription-default-cogw
spec:
  automation_ref:
    name: qa-sampling-automation
    version: "1.0.0"
  activation:
    status: draft  # Starts as draft for customer activation
  sentinel_deployment:
    auto_activate: false
    enrollment_limits:
      max_concurrent_requests: 50
  cogSpec:
    workbench_patterns:
      - pattern: "*-cogw"
        action: disallow
      - pattern: "*"
        action: allow
```

---

## Initial State After Subscription Creation

### COGW Dashboard View

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    COGW: acme-subscription-default-cogw                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Status: ● Active                                                            │
│  Type: Default COGW                                                          │
│  Created: 2026-01-14 (with subscription)                                     │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │ COG SENTINELS                                                        │    │
│  ├─────────────────────────────────────────────────────────────────────┤    │
│  │ Name                          Status    Target Workbenches           │    │
│  │ ──────────────────────────    ──────    ─────────────────────────    │    │
│  │ token-usage-governance        ● Active  5 workbenches               │    │
│  │ compliance-sampling           ● Active  3 workbenches               │    │
│  │ qa-sampling                   ○ Draft   0 workbenches (not active)  │    │
│  │ security-monitoring           ○ Draft   0 workbenches (not active)  │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │ TARGET WORKBENCHES                                                   │    │
│  ├─────────────────────────────────────────────────────────────────────┤    │
│  │ Workbench              Active COG Sentinels                          │    │
│  │ ─────────────────      ────────────────────                          │    │
│  │ production-loans       token-usage, compliance                       │    │
│  │ production-payments    token-usage, compliance                       │    │
│  │ production-disputes    token-usage, compliance                       │    │
│  │ acme-internal          token-usage                                   │    │
│  │ customer-service       token-usage                                   │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Customization Options

### Option 1: Activate Additional Sentinels

```yaml
# Activate QA Sampling sentinel
apiVersion: seer.olympus.io/v1
kind: SentinelScenarioDeploymentSpec
metadata:
  name: qa-sampling-deployment
  namespace: acme-subscription-default-cogw
spec:
  activation:
    status: active  # Changed from draft
  sentinel_deployment:
    auto_activate: true  # Changed from false
```

### Option 2: Customize Target Patterns

```yaml
# Update cogSpec to target specific workbenches
cogSpec:
  workbench_patterns:
    # Only monitor lending workbenches
    - pattern: "*-lending-*"
      action: allow
    - pattern: "loans-*"
      action: allow
```

### Option 3: Delete Default COGW

If the organization doesn't need subscription-wide governance:

```bash
# Delete the default COGW workbench
kubectl delete workbench acme-subscription-default-cogw -n acme-subscription
```

### Option 4: Create Custom COGW

```yaml
# Create a specialized COGW for security
apiVersion: hub.olympus.io/v1
kind: Workbench
metadata:
  name: acme-security-cogw
  namespace: acme-subscription
spec:
  workbench_type: cogw
  domain: security-governance
  description: "Security-focused COGW"
  # ... custom configuration
```

---

## Related Documentation

- [COGW Specification](../cogw-specification.md) — Workbench type details
- [COG Sentinel Example](./cog-sentinel-example.md) — Complete COG Sentinel example
- [Administrative Controls](../administrative-controls.md) — Managing COG Sentinels

---

*This example shows the default COGW setup that every subscription receives, providing immediate subscription-wide governance capabilities.*
