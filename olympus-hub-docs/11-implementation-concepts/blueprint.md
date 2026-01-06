# Blueprint

> **Category:** Platform Foundation

---

## Overview

A **Blueprint** is a reusable template for creating Workbenches with predefined Scenarios, tools, configurations, and best practices. Blueprints accelerate workbench setup by encoding proven operational patterns, allowing organizations to quickly deploy standardized capabilities across different domains.

---

## Ontology Context

### Relationship to Ontology

The ontology defines **Domain** and **Workbench** but doesn't address reusability or templating. Blueprint is an implementation concept for codifying and sharing workbench patterns.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Domain | Workbench | Blueprint creates Workbenches |
| Scenario | Scenario Definitions | Blueprint includes Scenario templates |
| (not covered) | Blueprint | Reusable workbench template |

### Gap This Fills

The ontology focuses on concepts, not reuse. Blueprint addresses:
1. **Standardization**: Common patterns codified as templates
2. **Acceleration**: Faster workbench setup
3. **Best practices**: Proven configurations pre-packaged
4. **Industry solutions**: Domain-specific starting points

---

## Definition

**Blueprint** is a workbench template that:
- Contains pre-configured Scenario Normative Specifications
- Includes reference tool and machine definitions
- Provides sample Hub Application structures
- Defines recommended task queues and escalation patterns
- Can be customized during workbench instantiation

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Platform-level (system) or Tenant-level (custom) |
| **Lifecycle** | Created by Hub or Process Architects; versioned |
| **Ownership** | System Blueprints by Hub; Tenant Blueprints by Tenant |
| **Multiplicity** | Many Blueprints available; one used per Workbench creation |

---

## Rationale

### Why This Design?

Blueprints enable:
1. **Faster time-to-value**: Deploy proven patterns immediately
2. **Consistency**: Standard patterns across organization
3. **Knowledge capture**: Best practices codified
4. **Reduced errors**: Pre-validated configurations

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Manual setup each time** | Slow; error-prone; inconsistent |
| **Clone existing workbench** | Carries over unwanted state |
| **Documentation only** | Requires manual translation |

---

## Structure

### Blueprint Specification

```yaml
apiVersion: hub.olympus.io/v1
kind: BlueprintSpec
metadata:
  name: dispute-management-blueprint
  namespace: hub-system  # System blueprints in hub-system
spec:
  display_name: "Dispute Management"
  version: "2.0.0"
  description: "Standard dispute management for financial services"
  
  # Target industry
  industry: financial_services
  domain: customer_operations
  
  # Included Scenario templates
  scenarios:
    - name: standard-dispute
      type: case
      description: "Standard dispute resolution"
      normative_template:
        roles:
          - name: dispute-analyst
            type: agent
            goals: ["Investigate within SLA"]
        sla:
          target_hours: 72
          
    - name: fraud-dispute
      type: case
      description: "High-priority fraud disputes"
      
  # Recommended tools
  tools:
    - name: transaction-lookup
      type: machine_tool
      machine_ref: core-banking-system
      
  # Recommended queues
  task_queues:
    - name: tier-1-disputes
      escalation_minutes: 120
      
  # Knowledge templates
  knowledge:
    - name: dispute-sop
      type: sop
      template_ref: dispute-investigation-sop
```

### Blueprint Types

| Type | Scope | Examples |
|------|-------|----------|
| **System Blueprint** | Platform-provided | Dispute Management, Customer Service, Fraud Detection |
| **Industry Blueprint** | Industry-specific | Banking Operations, Insurance Claims |
| **Tenant Blueprint** | Organization custom | ACME Dispute Operations |

---

## Behavior

### How It Works

**Workbench Creation from Blueprint:**
```
1. Admin/Architect selects Blueprint
2. Provides customization parameters:
   ├── Workbench name
   ├── Subscription
   ├── Environment overrides
   └── Feature toggles
3. Hub creates Workbench with:
   ├── Scenario Normative Specs (from Blueprint)
   ├── Tool Definitions (from Blueprint)
   ├── Queue Configurations (from Blueprint)
   └── Knowledge templates (from Blueprint)
4. Developer completes Automation and Deployment specs
```

### Customization Points

```yaml
customization:
  # What can be overridden during instantiation
  overridable:
    - scenario_names
    - sla_parameters
    - queue_configurations
    - tool_bindings
    
  # What is fixed
  fixed:
    - compliance_requirements
    - role_definitions
    - evidence_requirements
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Workbench | → creates | Blueprint instantiates Workbench |
| Scenario Normative Spec | → provides | Blueprint contains Scenario templates |
| Tool Definition | → provides | Blueprint includes tool recommendations |
| Knowledge Bank | → seeds | Blueprint includes knowledge templates |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Versioned** | Blueprints have explicit versions |
| **Immutable** | Published Blueprint version cannot change |
| **Validation** | Blueprint must be internally consistent |
| **Compatibility** | Blueprint version compatible with Hub version |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Fast deployment** | Hours instead of weeks |
| ✅ **Proven patterns** | Validated configurations |
| ✅ **Consistency** | Standard approach across org |
| ✅ **Customizable** | Adapt to specific needs |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **May not fit exactly** | Customization points; can modify after |
| ⚠️ **Version management** | Clear upgrade paths |

---

## Examples

### Example 1: Creating Workbench from Blueprint

```bash
hub workbench create \
  --name dispute-ops-dev \
  --subscription acme-dev \
  --blueprint dispute-management-blueprint:2.0.0 \
  --stage DEV \
  --customize sla.target_hours=48
```

### Example 2: System Blueprint Catalog

```
Hub Blueprint Catalog:

Financial Services:
├── dispute-management (v2.0.0)
├── fraud-detection (v1.5.0)
├── customer-onboarding (v3.0.0)
└── regulatory-reporting (v1.0.0)

Insurance:
├── claims-processing (v2.0.0)
├── underwriting-support (v1.0.0)
└── policy-servicing (v1.5.0)

Cross-Industry:
├── it-service-desk (v2.0.0)
├── hr-operations (v1.0.0)
└── vendor-management (v1.0.0)
```

---

## Implementation Notes

### For Process Architects

- Evaluate available Blueprints before starting from scratch
- Customize during instantiation, then refine
- Create Tenant Blueprints for organization-specific patterns

### For Operators

- Manage Blueprint catalog and versions
- Communicate Blueprint updates to teams
- Support Blueprint customization requests

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Subscription](./subscription.md) | Workbenches from Blueprints created in Subscriptions |
| [Scenario Specification Types](./scenario-specification-types.md) | Blueprint contains Scenario templates |
| [Operator](./operator.md) | SRE Operator manages BlueprintSpec |

---

## References

- [Publisher Domain Operators](../04-subsystems/operators/publisher-domain-operators.md)
- [Workbench Management](../04-subsystems/workbench-management/README.md)

