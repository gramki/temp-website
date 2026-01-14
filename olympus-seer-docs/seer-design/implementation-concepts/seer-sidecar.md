# Seer Sidecar

> **Category:** DevOps and Lifecycle  
> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-15

---

## Overview

Seer Sidecar provides **runtime enforcement capabilities** for Employed Agents through Istio service mesh interception. It enforces guardrails, authority ceilings, OPA policies, resource quotas, and fair usage budgets on all agent traffic—both inbound requests and outbound Hub API calls. The sidecar operates as a defense-in-depth layer, catching violations early before they reach downstream systems.

---

## Ontology Context

### Relationship to Ontology

Seer Sidecar implements the **enforcement layer** for Controlled Autonomy and Directability principles:

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|-------------|
| **Controlled Autonomy** | Authority ceiling enforcement, policy evaluation | Sidecar enforces autonomy boundaries |
| **Directability** | Guardrail enforcement, policy violations | Sidecar enables programmatic control |
| **Observability** | Metrics collection, violation logging | Sidecar provides visibility into agent behavior |
| **Authority** | Authority ceiling checks, delegation validation | Sidecar enforces authority limits |
| **OPD (Observability, Predictability, Directability)** | All three principles enforced at runtime | Sidecar provides runtime OPD enforcement |

### Gap This Fills

The AOSM ontology defines Controlled Autonomy and Directability but doesn't specify how to enforce them programmatically at runtime. Seer Sidecar fills this gap by providing:

1. **Programmatic Enforcement**: Guardrails and policies enforced at network layer (cannot be bypassed)
2. **Defense in Depth**: Early enforcement before requests reach downstream systems
3. **Per-API Configuration**: Fine-grained control over which APIs are protected
4. **Hot-Reload**: Configuration updates without pod restarts
5. **Comprehensive Coverage**: Inbound and outbound traffic interception

---

## Definition

**Seer Sidecar** is a runtime enforcement layer that intercepts all agent traffic via Istio service mesh to enforce guardrails, authority ceilings, OPA policies, resource quotas, and fair usage budgets. It operates on both inbound `/dispatch` requests and outbound Hub API calls, providing defense-in-depth enforcement that cannot be bypassed by agents.

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Per-agent-pod (sidecar container injected into each pod) |
| **Lifecycle** | Injected automatically by Istio when pod created; hot-reload for configuration updates |
| **Ownership** | Agent Reliability Engineer (ARE) manages sidecar configuration; Seer Operator provisions |
| **Multiplicity** | One sidecar per agent pod; multiple guardrail containers per sidecar |

---

## Rationale

### Why This Design?

**Istio-Based Interception**:
- Leverages existing service mesh infrastructure
- Automatic sidecar injection (no code changes required)
- mTLS and observability built-in

**Inbound and Outbound Enforcement**:
- Inbound: Validates requests before agent processes them
- Outbound: Validates agent actions before they reach Hub APIs
- Comprehensive coverage of all agent interactions

**Defense in Depth**:
- Early enforcement at sidecar reduces load on downstream systems
- Catches obvious violations before reaching Tool Gateway, Signal Exchange
- Downstream systems still enforce authoritatively (final check)

**Per-API Configuration**:
- Wildcard pattern matching (e.g., `/api/agent/v1/requests/*/updates`)
- Fine-grained control over which APIs are protected
- Different guardrails for different API endpoints

**Hot-Reload**:
- Configuration updates without pod restarts
- Enables rapid policy changes
- No service disruption

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Application-Level Enforcement** | Can be bypassed; sidecar provides network-layer enforcement |
| **Gateway-Only Enforcement** | No early enforcement; violations reach downstream systems |
| **Restart-Based Updates** | Service disruption; hot-reload enables zero-downtime updates |

### Related ADRs

| ADR | Decision |
|-----|----------|
| [ADR-0072: Guardrails Two-Layer Model](../../../olympus-hub-docs/decision-logs/0072-seer-guardrails-two-layer-model.md) | Two-layer guardrail model (behavioral guidelines + sidecar enforcement) |
| [ADR-0073: Authority Enforcement via OPA](../../../olympus-hub-docs/decision-logs/0073-seer-authority-enforcement-opa.md) | OPA-based policy enforcement |
| [ADR-0074: Runtime on Atlantis](../../../olympus-hub-docs/decision-logs/0074-seer-runtime-atlantis-based.md) | Istio service mesh integration |

---

## Structure

### Key Attributes

```yaml
# Conceptual sidecar configuration structure
seer_sidecar:
  guardrails:
    inbound:
      - ref: string
        config: object
        apis: [string]  # ["/dispatch"]
    
    outbound:
      - ref: string
        config: object
        apis: [string]  # ["/api/agent/v1/requests/*/updates"]
  
  authority_enforcement:
    ceilings:
      value:
        maxSingleTransaction: number
        maxDailyTotal: number
      rate:
        maxDecisionsPerHour: number
      scope:
        customerTiers: [string]
        dataClasses: [string]
  
  policies:
    - pep: string  # Policy Enforcement Point
      policyRef: string
      inline: string  # Optional inline policy
  
  resource_quotas:
    cpu: string
    memory: string
    requests_per_minute: number
  
  fair_usage_budgets:
    per_user:
      max_requests_per_day: number
    per_customer:
      max_requests_per_day: number
  
  metrics:
    enabled: boolean
    export_endpoint: string
```

### States

| State | Description | Transitions |
|-------|-------------|-------------|
| **Injected** | Sidecar injected by Istio | → Active |
| **Active** | Sidecar enforcing policies | → Reloading, → Disabled |
| **Reloading** | Configuration being hot-reloaded | → Active |
| **Disabled** | Sidecar disabled (emergency) | → Active |

---

## Behavior

### How It Works

#### Inbound Request Flow

```
1. Request arrives at /dispatch endpoint
2. Istio routes to sidecar (before agent container)
3. Inbound guardrails execute (Training Spec → Employment Spec order)
4. Authority ceiling checks (value, rate, scope)
5. OPA policy evaluation
6. If all pass: Request forwarded to agent container
7. If violation: Request denied with error response
```

#### Outbound API Call Flow

```
1. Agent makes Hub API call (e.g., POST /api/agent/v1/requests/{id}/updates)
2. Istio intercepts call (before leaving pod)
3. Outbound guardrails execute (pattern-matched by API path)
4. Authority ceiling checks
5. OPA policy evaluation
6. Resource quota checks
7. Fair usage budget checks
8. If all pass: Call forwarded to Hub API
9. If violation: Call denied with error response
```

#### Hot-Reload Flow

```
1. Configuration update (EmploymentSpec CRD change)
2. Seer Operator updates sidecar configuration
3. Sidecar hot-reload service receives update
4. Configuration reloaded without pod restart
5. New policies/guardrails active immediately
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| **Istio Service Mesh** | ↔ | Intercepts traffic, provides mTLS, telemetry |
| **Agent Container** | ↔ | Receives inbound requests, intercepts outbound calls |
| **Guardrail Services** | → | Executes guardrail processors |
| **OPA Engine** | → | Evaluates policies |
| **Cipher IAM** | → | Validates authority, delegation chains |
| **Hub APIs** | → | Forwards validated outbound calls |
| **Tool Gateway** | → | Early enforcement before authoritative enforcement |
| **Model Gateway** | → | Early enforcement before authoritative enforcement |
| **Watch (Observability)** | → | Exports metrics, traces, violation logs |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Fail-Closed Default** | Default failure policy is Deny (fail-closed) |
| **Training Spec Immutability** | Training Spec guardrails cannot be relaxed in Employment Spec |
| **Narrowing-Only** | Employment Spec can only narrow (never expand) Training Spec limits |
| **Per-API Matching** | Outbound guardrails matched by API path patterns |
| **Early Enforcement** | Sidecar provides early enforcement; downstream systems enforce authoritatively |
| **Hot-Reload Only** | Configuration updates via hot-reload (no pod restarts) |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Network-Layer Enforcement** | Cannot be bypassed by agents (enforced at Istio level) |
| ✅ **Defense in Depth** | Early enforcement reduces load on downstream systems |
| ✅ **Comprehensive Coverage** | Inbound and outbound traffic interception |
| ✅ **Fine-Grained Control** | Per-API configuration with pattern matching |
| ✅ **Zero-Downtime Updates** | Hot-reload enables configuration updates without restarts |
| ✅ **Observable** | Metrics, traces, violation logs exported to Watch |
| ✅ **Standard Infrastructure** | Leverages Istio (proven service mesh) |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Sidecar Overhead** | Sidecar is lightweight; overhead is minimal |
| ⚠️ **Configuration Complexity** | Clear documentation and examples for common patterns |
| ⚠️ **Early vs. Authoritative** | Downstream systems still enforce authoritatively (final check) |
| ⚠️ **Hot-Reload Edge Cases** | Configuration validation ensures safe reloads |

---

## Examples

### Example 1: Inbound Guardrail - PII Detection

**Use Case**: Detect and block requests containing PII before agent processes them

```yaml
# In EmploymentSpec
spec:
  sidecar:
    guardrails:
      inbound:
        - ref: pii-detector
          config:
            mode: deny  # Block requests with PII
            patterns:
              - ssn: "\\d{3}-\\d{2}-\\d{4}"
              - credit_card: "\\d{4}[\\s-]?\\d{4}[\\s-]?\\d{4}[\\s-]?\\d{4}"
          apis: ["/dispatch"]
```

**Behavior**: When request arrives at `/dispatch`, PII detector scans content. If PII detected, request is denied with error response. Agent never receives the request.

---

### Example 2: Outbound Guardrail - Request Update Validation

**Use Case**: Validate request updates before they reach Hub APIs

```yaml
spec:
  sidecar:
    guardrails:
      outbound:
        - ref: request-update-validator
          config:
            mode: alert  # Allow but alert on violations
            rules:
              - field: "payload.decision.amount"
                max_value: 10000
                action: alert
          apis: ["/api/agent/v1/requests/*/updates"]
```

**Behavior**: When agent calls `/api/agent/v1/requests/{id}/updates`, validator checks decision amount. If exceeds $10,000, call proceeds but alert sent to observers.

---

### Example 3: Authority Ceiling Enforcement

**Use Case**: Enforce transaction amount limits

```yaml
spec:
  sidecar:
    authority_enforcement:
      ceilings:
        value:
          maxSingleTransaction: 5000
          maxDailyTotal: 25000
        approval:
          thresholds:
            - amount: 2000
              requires: "supervisor_review"
```

**Behavior**: Sidecar checks transaction amounts on outbound decision calls. If amount exceeds $5,000, call denied. If amount exceeds $2,000, call requires supervisor review (escalation).

---

### Example 4: OPA Policy Enforcement

**Use Case**: Enforce scenario-scoped access policies

```yaml
spec:
  sidecar:
    policies:
      - pep: "request-dispatch"
        policyRef: "policies/scenario-access.rego"
```

**OPA Policy** (`scenario-access.rego`):
```rego
package seer.policy.scenario

default allow = false

allow {
    input.scenario_id == data.allowed_scenarios[_]
    input.workbench_id == data.workbench_id
}
```

**Behavior**: On inbound `/dispatch` requests, OPA evaluates scenario access policy. Only requests for allowed scenarios proceed.

---

## Implementation Notes

### For Developers

- **Guardrail Development**: Guardrails are containerized processors; implement HTTP interface
- **Pattern Matching**: Use wildcard patterns for API path matching (e.g., `/api/agent/v1/requests/*/updates`)
- **Response Model**: Guardrails return Allow, Alert, or Deny; can also transform/redact payloads
- **Hot-Reload**: Configuration changes trigger hot-reload; ensure guardrails handle reload gracefully

### For Operators

- **Configuration Management**: Sidecar configuration in EmploymentSpec; changes trigger hot-reload
- **Monitoring**: Monitor sidecar metrics (violation rates, enforcement latency)
- **Policy Tuning**: Tune policies based on false positive rates; use Alert mode for borderline cases
- **Emergency Disable**: Sidecar can be disabled in emergency (via kill switch)

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Guardrails](./guardrails.md) | Sidecar implements programmatic guardrail enforcement |
| [Authority Enforcement](./authority-enforcement.md) | Sidecar provides early authority enforcement |
| [Agent Runtime](./agent-runtime.md) | Sidecar injected into agent pods at runtime |
| [Agent Lifecycle](./agent-lifecycle.md) | Sidecar configuration in Employment Spec |
| [Kill Switch & Emergency Controls](./kill-switch-emergency-controls.md) | Sidecar can be disabled via kill switch |

---

## References

- [Seer Sidecar Subsystem](../subsystems/seer-sidecar/README.md) — Complete subsystem documentation
- [Guardrail Service](../subsystems/seer-sidecar/guardrail-service.md) — Guardrail execution model
- [Authority Enforcement Service](../subsystems/seer-sidecar/authority-enforcement-service.md) — Authority ceiling enforcement
- [Policy Enforcement Service](../subsystems/seer-sidecar/policy-enforcement-service.md) — OPA policy evaluation
- [Resource Quota Service](../subsystems/seer-sidecar/resource-quota-service.md) — Resource consumption tracking
- [Fair Usage Budget Service](../subsystems/seer-sidecar/fair-usage-budget-service.md) — User/customer usage tracking
- [Hot-Reload Service](../subsystems/seer-sidecar/guardrail-hot-reload-service.md) — Configuration updates without restart
- [Istio Service Mesh](../../../olympus-hub-docs/05-infrastructure/istio.md) — Service mesh integration
- [ADR-0072: Guardrails Two-Layer Model](../../../olympus-hub-docs/decision-logs/0072-seer-guardrails-two-layer-model.md)

---

*Seer Sidecar provides defense-in-depth runtime enforcement for Employed Agents, ensuring they operate within controlled autonomy boundaries and governance policies.*
