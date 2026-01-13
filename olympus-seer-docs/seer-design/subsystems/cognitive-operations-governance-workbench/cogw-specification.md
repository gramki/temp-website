# COGW Specification

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-14  
> **Design Level**: C2 (Container)

---

## Overview

The COGW Specification defines the `cogw` workbench type, default COGW creation at subscription creation, and the COGW Blueprint containing standard governance scenarios.

---

## Workbench Type Definition

### COGW as Distinct Workbench Type

COGW introduces a new workbench type value:

```yaml
workbench_type: "business" | "devops" | "cogw"
```

| Type | Purpose |
|------|---------|
| `business` | Standard operational workbenches (default) |
| `devops` | Development operations workbenches |
| `cogw` | Cognitive Operations Governance Workbenches |

### COGW Workbench Structure

```yaml
apiVersion: hub.olympus.io/v1
kind: Workbench
metadata:
  name: acme-cogw
  namespace: acme-subscription
  labels:
    hub.olympus.io/workbench-type: cogw
spec:
  domain: cognitive-governance
  description: "ACME Cognitive Operations Governance Workbench"
  
  # Workbench type marker
  workbench_type: cogw    # "business" (default) | "devops" | "cogw"
  
  dev_lifecycle_stage: PROD
  
  # Standard workbench configuration
  scenarios:
    - id: token-governance
      name: "Token Usage Governance"
      application_id: token-governance-app
    - id: compliance-sampling
      name: "Compliance Sampling"
      application_id: compliance-app
    - id: quality-assurance
      name: "Quality Assurance"
      application_id: qa-app
  
  # Triggers for governance scenarios
  triggers:
    - id: token-threshold-trigger
      signal_source: cronus
      conditions:
        - event_type: "token_usage_alert"
      scenario_id: token-governance
  
  # Access configuration
  machine_access:
    - all-subscription-workbenches  # COGW has broad access
  
  # Request policies
  request_policies:
    lifecycle:
      max_depth: 3
    storage:
      retention_days: 90
```

### Validation Rules

| Rule | Description |
|------|-------------|
| **Type Value** | `workbench_type` must be one of: `business`, `devops`, `cogw` |
| **COGW in Subscription** | COGW workbenches must be in a valid subscription |
| **COG Sentinels Only** | Only COGW workbenches can define COG Sentinels |
| **Non-COGW Restriction** | Non-COGW workbenches cannot have COG Sentinel label or cogSpec |

---

## Default COGW Creation

### Automatic Creation at Subscription Creation

Every subscription automatically receives a default COGW:

| Aspect | Behavior |
|--------|----------|
| **Trigger** | Subscription creation event |
| **Timing** | During subscription provisioning |
| **Name** | `<subscription-id>-default-cogw` |
| **Namespace** | Same as subscription namespace |
| **Content** | Standard governance scenarios from COGW Blueprint |

### Default COGW Structure

```yaml
apiVersion: hub.olympus.io/v1
kind: Workbench
metadata:
  name: sub-acme-default-cogw
  namespace: acme-subscription
  labels:
    hub.olympus.io/workbench-type: cogw
    hub.olympus.io/default-cogw: "true"
  annotations:
    hub.olympus.io/created-by: subscription-provisioning
spec:
  domain: cognitive-governance
  description: "Default Cognitive Operations Governance Workbench"
  
  workbench_type: cogw
  
  # Standard governance scenarios from Blueprint
  scenarios:
    - id: token-usage-governance
      name: "Token Usage Governance"
    - id: compliance-sampling
      name: "Compliance Sampling"
    - id: quality-assurance-sampling
      name: "Quality Assurance Sampling"
    - id: security-monitoring
      name: "Security Monitoring"
```

### Lifecycle

| Operation | Behavior |
|-----------|----------|
| **Create** | Automatic at subscription creation |
| **Delete** | Allowed — can delete default COGW if not needed |
| **Recreate** | Can create new COGWs manually |
| **Modify** | Standard workbench modification workflows |

---

## COGW Blueprint

### Standard Governance Scenarios

The default COGW Blueprint includes:

| Scenario | Purpose | Default COG Sentinel |
|----------|---------|---------------------|
| **Token Usage Governance** | Monitor and enforce token budgets | ✅ |
| **Compliance Sampling** | Sample AI decisions for compliance review | ✅ |
| **Quality Assurance Sampling** | Evaluate output quality across agents | ✅ |
| **Security Monitoring** | Detect security-relevant patterns | ✅ |

### Blueprint Structure

```yaml
apiVersion: hub.olympus.io/v1
kind: WorkbenchBlueprintSpec
metadata:
  name: cogw-default-blueprint
  labels:
    hub.olympus.io/blueprint-type: cogw
spec:
  display_name: "Default COGW Blueprint"
  description: "Standard governance scenarios for cognitive operations"
  
  workbench_type: cogw
  
  scenarios:
    - name: token-usage-governance
      display_name: "Token Usage Governance"
      description: "Monitor and enforce token budgets across workbenches"
      normative:
        goals:
          primary:
            description: "Ensure token usage adheres to budget limits"
        agent_roles:
          - id: token-governance-agent
            name: "Token Governance Agent"
      automation:
        ai_agent:
          model:
            provider: bedrock
            model_id: anthropic.claude-3-sonnet
        sentinel:
          participation:
            mode: observe_and_participate
    
    - name: compliance-sampling
      display_name: "Compliance Sampling"
      description: "Sample and verify AI decisions for regulatory compliance"
    
    - name: quality-assurance-sampling
      display_name: "Quality Assurance Sampling"
      description: "Evaluate AI output quality and identify improvement areas"
    
    - name: security-monitoring
      display_name: "Security Monitoring"
      description: "Monitor for security-relevant patterns and anomalies"
```

---

## Multiple COGW Workbenches

### Subscription Support

Subscriptions can have multiple COGW workbenches:

| Aspect | Behavior |
|--------|----------|
| **Count** | Unlimited COGW workbenches per subscription |
| **Naming** | Standard workbench naming rules |
| **Independence** | Each COGW operates independently |
| **No Conflicts** | COG Sentinels from different COGWs can target same workbenches |

### Use Cases for Multiple COGWs

| Use Case | Example |
|----------|---------|
| **Domain-specific governance** | Lending COGW, Payments COGW |
| **Team ownership** | Security team COGW, Compliance team COGW |
| **Environment separation** | Production COGW, Staging COGW |
| **Graduated rollout** | Pilot COGW with limited targeting |

### Overlap Handling

When multiple COG Sentinels from different COGWs target the same workbench:

1. **All are enrolled** — Each COG Sentinel creates its own child request
2. **Independent operation** — No coordination required
3. **Separate contexts** — Each has its own context compilation
4. **Local controls** — Each can be independently enabled/disabled

---

## Lifecycle States

| State | Description | Transitions |
|-------|-------------|-------------|
| **Creating** | COGW being provisioned | → Active |
| **Active** | COGW fully operational | → Suspended, Deleting |
| **Suspended** | COGW temporarily disabled | → Active, Deleting |
| **Deleting** | COGW being removed | → (deleted) |

---

## Related Documentation

- [COGW README](./README.md) — Subsystem overview
- [COG Sentinel Specification](./cog-sentinel-specification.md) — COG Sentinel definition
- [Hub Workbench Management](../../../../olympus-hub-docs/04-subsystems/workbench-management/README.md) — Base workbench concepts
- [Subscription Management](../../../../olympus-hub-docs/04-subsystems/subscription-management/README.md) — Subscription lifecycle

---

*COGW Specification defines the `cogw` workbench type, automatic creation at subscription provisioning, and the standard Blueprint for governance scenarios.*
