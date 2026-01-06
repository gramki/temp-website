# Hub Environment

> **Category:** Data Architecture

---

## Overview

A **Hub Environment** is a business/operations domain runtime configuration that defines runtime variables, secrets, external system references, and operational parameters for a workbench. Unlike Dev-Lifecycle-Stage (development phase), Hub Environment represents the business context (e.g., Production vs Sandbox for different customer segments).

---

## Ontology Context

### Relationship to Ontology

The ontology describes **Domain** as a conceptual scope of operations. Hub Environment provides runtime configuration for how operations execute in different business contexts.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Domain context | Hub Environment | Runtime configuration for domain |
| (not covered) | Environment variables | Implementation-level config |

### Gap This Fills

The ontology focuses on concepts. Hub Environment addresses:
1. **Runtime configuration**: How are variables and secrets managed?
2. **Business contexts**: How do Production vs Sandbox differ?
3. **External references**: How are external systems referenced?
4. **Promotion isolation**: What doesn't promote?

---

## Definition

**Hub Environment** is a workbench configuration that:
- Defines environment variables and secrets
- References external systems (Machine instances)
- Provides business-context-specific settings
- Is NOT promoted (configured per workbench)

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Workbench-level; one per workbench |
| **Lifecycle** | Configured by Admin; used at runtime |
| **Ownership** | Admin configures; applications consume |
| **Multiplicity** | One per workbench |

---

## Rationale

### Why This Design?

Explicit environment configuration enables:
1. **Separation**: Keep secrets out of promotable CRDs
2. **Flexibility**: Different configs per business context
3. **Security**: Secrets managed separately
4. **Clarity**: Clear what's environment-specific

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Inline in CRDs** | Secrets would promote; security issue |
| **External config management only** | No Hub integration |
| **No environment concept** | Can't differentiate contexts |

---

## Structure

### Environment Specification

```yaml
apiVersion: hub.olympus.io/v1
kind: EnvironmentSpec
metadata:
  name: dispute-ops-prod-env
  namespace: acme-bank
spec:
  workbench_ref: dispute-ops-prod
  
  # Environment variables
  variables:
    LOG_LEVEL: "INFO"
    FEATURE_FLAG_NEW_UI: "true"
    MAX_CONCURRENT_REQUESTS: "100"
    
  # Secrets (references, not values)
  secrets:
    - name: DATABASE_PASSWORD
      secret_ref: ganymede-db-password
    - name: API_KEY
      secret_ref: external-api-key
      
  # Machine instance bindings
  machines:
    - alias: core-banking
      instance_ref: core-banking-prod
    - alias: crm
      instance_ref: salesforce-prod
      
  # Tool instance bindings
  tools:
    - alias: email-sender
      instance_ref: sendgrid-prod
```

### Environment vs Dev-Lifecycle-Stage

| Aspect | Dev-Lifecycle-Stage | Hub Environment |
|--------|--------------------|-----------------| 
| Purpose | Development phase | Business context |
| Examples | DEV, STAGING, PROD | Production, Sandbox, Demo |
| Scope | Workbench maturity | Runtime configuration |
| Promotes | N/A (tag on workbench) | Does NOT promote |

---

## Behavior

### How Applications Use Environment

```python
class DisputeHandler(HubApplication):
    def __init__(self):
        # Environment variables available
        self.log_level = self.env.get("LOG_LEVEL", "INFO")
        self.max_concurrent = int(self.env.get("MAX_CONCURRENT_REQUESTS", "50"))
        
        # Secrets available
        self.db_password = self.secrets.get("DATABASE_PASSWORD")
        
        # Machine aliases resolved
        self.core_banking = self.machines.get("core-banking")
        self.crm = self.machines.get("crm")
```

### Environment Isolation

```
Promotion does NOT include:
├── Environment variables
├── Secrets
├── Machine instance bindings
└── Tool instance bindings

Admin must configure these in each target workbench:
├── dispute-ops-dev: points to dev systems
├── dispute-ops-staging: points to staging systems
└── dispute-ops-prod: points to prod systems
```

### Machine/Tool Resolution

```
Scenario references: machines.core-banking
                                │
                                ▼
Environment binding:    alias: core-banking
                       instance_ref: core-banking-prod
                                │
                                ▼
Machine Instance:       core-banking-prod
                       └── connection: https://core.acme.com
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Hub Application | ← consumed by | Apps read env config |
| Machine Registry | → references | Binds aliases to instances |
| Secret Store | → references | Secrets resolved at runtime |
| Promotion | (excluded) | Not part of promotion |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Not promoted** | Environment configs are per-workbench |
| **Secrets by reference** | Values not in CRD |
| **Valid references** | Referenced secrets/instances must exist |
| **Admin managed** | Only Admin can modify |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Security** | Secrets not in promotable CRDs |
| ✅ **Flexibility** | Different configs per context |
| ✅ **Clarity** | Clear separation |
| ✅ **Alias abstraction** | Apps use aliases, not concrete refs |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Manual config per workbench** | Templates; documentation |
| ⚠️ **Drift possible** | Validation; comparison tools |

---

## Examples

### Example 1: Dev vs Prod Environment

```yaml
# dispute-ops-dev environment
spec:
  variables:
    LOG_LEVEL: "DEBUG"
    MOCK_EXTERNAL_CALLS: "true"
  machines:
    - alias: core-banking
      instance_ref: core-banking-sandbox
---
# dispute-ops-prod environment
spec:
  variables:
    LOG_LEVEL: "INFO"
    MOCK_EXTERNAL_CALLS: "false"
  machines:
    - alias: core-banking
      instance_ref: core-banking-prod
```

### Example 2: Test Data Reset

```yaml
# Test environment with resettable data
spec:
  workbench_ref: dispute-ops-test
  
  # Flag for Hub Test Runner
  test_config:
    data_resettable: true
    reset_before_suite: true
    
  # Reference to test-specific instances
  machines:
    - alias: core-banking
      instance_ref: core-banking-test-stub
```

---

## Implementation Notes

### For Developers

- Use environment aliases, not hardcoded references
- Check for required variables at startup
- Handle missing optional variables gracefully

### For Operators

- Configure environments before first use
- Document required variables per scenario
- Rotate secrets regularly

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Dev-Lifecycle-Stage](./dev-lifecycle-stage.md) | Different concept |
| [Promotion](./promotion.md) | Environment not promoted |
| [Operator](./operator.md) | workbench-admin-operator manages |

---

## References

- [Admin Operators](../../04-subsystems/operators/admin-operators.md)
- [Workbench Management](../../04-subsystems/workbench-management/README.md)

