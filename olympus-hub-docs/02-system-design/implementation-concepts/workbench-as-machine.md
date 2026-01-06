# Workbench as Machine

> **Category:** Composite Patterns

---

## Overview

**Workbench as Machine** is a composite pattern where an entire Workbench is exposed as a Machine to other workbenches. This enables cross-workbench capability sharing, allowing one workbench's tools, scenarios-as-tools, and standalone applications to be consumed by another workbench as if they were external system integrations.

---

## Ontology Context

### Relationship to Ontology

The ontology describes **Machine** as an external system that provides capabilities. This pattern treats internal workbenches as machines for other workbenches.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Machine | Workbench as Machine | Workbench exposed as machine |
| Tool | Exposed tools | Tools available to consumers |

### Gap This Fills

The ontology focuses on external machines. This pattern addresses:
1. **Cross-workbench sharing**: How to share capabilities?
2. **Internal reuse**: How to treat internal like external?
3. **Transitive access**: How to chain capabilities?

---

## Definition

**Workbench as Machine** is a pattern where:
- A Workbench is registered as a Machine
- Selected tools and capabilities are exposed
- Other workbenches can consume via Machine interface
- Authentication uses Hub-native mechanisms

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Cross-workbench; possibly cross-subscription |
| **Lifecycle** | Created by Developer; consumed by others |
| **Ownership** | Provider workbench owns; consumers use |
| **Multiplicity** | One machine definition per workbench |

---

## Rationale

### Why This Design?

Workbench as Machine enables:
1. **Capability sharing**: Reuse across workbenches
2. **Consistent interface**: Machine pattern already understood
3. **Access control**: Standard authorization model
4. **Transitive chains**: A exposes B's tools via A

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Direct API sharing** | Ad-hoc; no standard pattern |
| **Copy tools** | Duplication; drift |
| **Single mega-workbench** | Violates domain boundaries |

---

## Structure

### WorkbenchAsMachine CRD

```yaml
apiVersion: hub.olympus.io/v1
kind: WorkbenchAsMachine
metadata:
  name: shared-services-machine
  namespace: acme-bank
spec:
  # Source workbench
  workbench_ref: shared-services-prod
  
  # Machine identity
  machine:
    name: shared-services
    display_name: "Shared Services"
    version: "1.0.0"
    description: "Common services for all workbenches"
    
  # Exposed capabilities
  exposed_tools:
    # Scenario as Tool
    - type: scenario_tool
      ref: validation-tool
      alias: validate
      
    # Standalone Hub App Tool
    - type: standalone_tool
      ref: email-sender-tool
      alias: email
      
    # Machine Tool (from another machine)
    - type: machine_tool
      ref: core-banking/account-lookup
      alias: account-lookup
      transitive: true    # Expose transitively
      
  # Access control
  access:
    allowed_workbenches:
      - dispute-ops-prod
      - fraud-ops-prod
    allowed_subscriptions:
      - acme-prod
```

### Exposed Tool Types

| Type | Source | Example |
|------|--------|---------|
| **scenario_tool** | Scenario as Tool | Validation scenario |
| **standalone_tool** | Hub App as Standalone | Email sender |
| **machine_tool** | Machine already connected | Core banking tools |
| **decision_tool** | Decision service | Risk scoring |

---

## Behavior

### How It Works

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    WORKBENCH AS MACHINE FLOW                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   CONSUMER WORKBENCH               PROVIDER WORKBENCH                       │
│   (dispute-ops-prod)               (shared-services-prod)                   │
│                                                                              │
│   ┌───────────────┐               ┌───────────────────────────────────────┐│
│   │ Hub App       │               │ Workbench as Machine                   ││
│   │               │               │                                        ││
│   │ tool.invoke(  │    HTTP       │  ┌─────────────┐                      ││
│   │   machine:    │──────────────▶│  │  Heracles   │                      ││
│   │     shared-   │               │  │  Gateway    │                      ││
│   │     services  │               │  └──────┬──────┘                      ││
│   │   tool:       │               │         │                              ││
│   │     validate  │               │         ▼                              ││
│   │   params:{}   │               │  ┌─────────────┐                      ││
│   │ )             │               │  │ Scenario    │                      ││
│   │               │               │  │ as Tool     │                      ││
│   │               │◀──────────────│  └─────────────┘                      ││
│   │               │   Response    │                                        ││
│   └───────────────┘               └───────────────────────────────────────┘│
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Authentication

```
Cross-workbench authentication options:

1. Bot credentials
   └── Consumer has bot registered; uses bot token

2. Credential forwarding
   └── Consumer forwards caller's credentials

3. Service account
   └── Machine-to-machine OAuth

Authorization checked at provider:
├── Is consumer workbench allowed?
├── Is specific tool accessible?
└── Apply fine-grained policies
```

### Transitive Exposure

```
Workbench A (consumer)
    │
    ├── uses shared-services machine
    │
    ▼
Workbench B (shared-services)
    │
    ├── exposes core-banking tools (transitive: true)
    │
    ▼
Core Banking System (external machine)

A can call core-banking tools through B
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Machine Registry | ← registered in | Machine available for discovery |
| Consumer Workbench | ← consumed by | Consumers invoke tools |
| Provider Tools | → routes to | Requests routed to actual tools |
| Heracles Gateway | ← protected by | HTTP authentication |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Explicit exposure** | Only exposed tools are accessible |
| **Access control** | Consumers must be authorized |
| **Version alignment** | Machine version for compatibility |
| **Transitive opt-in** | Transitive exposure explicit |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Reuse** | Share capabilities across workbenches |
| ✅ **Consistent interface** | Standard Machine pattern |
| ✅ **Controlled access** | Explicit authorization |
| ✅ **Chaining** | Transitive tool chains |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Latency** | Monitor cross-workbench calls |
| ⚠️ **Dependency** | Version management |

---

## Examples

### Example 1: Shared Validation Services

```yaml
# Provider: shared-services
spec:
  workbench_ref: shared-services-prod
  
  exposed_tools:
    - type: scenario_tool
      ref: amount-validation
      alias: validate-amount
    - type: scenario_tool
      ref: merchant-validation
      alias: validate-merchant
      
  access:
    allowed_workbenches:
      - dispute-ops-prod
      - fraud-ops-prod
```

### Example 2: Consumer Usage

```python
# Hub App in dispute-ops-prod
result = await self.machines.shared_services.validate_amount(
    amount=500,
    currency="USD"
)
```

---

## Implementation Notes

### For Developers

- Expose only what's needed
- Document tool contracts
- Version for compatibility
- Consider latency implications

### For Operators

- Monitor cross-workbench traffic
- Review access patterns
- Manage credential rotation

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Scenario as Tool](./scenario-as-tool.md) | Can be exposed via machine |
| [Hub Application as Standalone Tool](./hub-application-as-standalone-tool.md) | Can be exposed |
| [Direct Tool Dispatcher](./direct-tool-dispatcher.md) | May route through |

---

## References

- [Workbench as Machine Pattern](../../09-composite-systems-and-patterns/workbench-as-a-machine.md)
- [Developer Operators](../../04-subsystems/operators/developer-operators.md)

