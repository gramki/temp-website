# Seer Sidecar - Design Scope

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-12  
> **Design Level**: C2 (Container) / C3 for critical enforcement

---

## Coverage Summary

The Seer Sidecar subsystem provides runtime enforcement capabilities for Employed Agents through Istio service mesh interception.

| Service | Design Level | Status |
|---------|--------------|--------|
| [Guardrail Service](./guardrail-service.md) | C2 | ✅ Complete |
| [Authority Enforcement Service](./authority-enforcement-service.md) | C2 | ✅ Complete |
| [Policy Enforcement Service](./policy-enforcement-service.md) | C3 | ✅ Complete |
| [Resource Quota Service](./resource-quota-service.md) | C2 | ✅ Complete |
| [Fair Usage Budget Service](./fair-usage-budget-service.md) | C2 | ✅ Complete |
| [Metrics Service](./metrics-service.md) | C2 | ✅ Complete |
| [Hot-reload Service](./guardrail-hot-reload-service.md) | C2 | ✅ Complete |

---

## Intended Design Depth

### C2 (Container) Level — Most Components

- **Functional scope** clearly defined
- **Integration points** and hand-offs documented
- **Conceptual models** with illustrative examples
- **ASCII diagrams** for operational flows
- **No detailed data models** or individual API specifications

### C3 (Component) Level — Critical Enforcement

- **Policy Enforcement Service** includes detailed API specifications
- **OPA policy evaluation** context schemas
- **Violation handling** data structures

---

## Key Design Decisions

### Guardrail Model

- **Inbound guardrails**: Execute on `/dispatch` requests (unchanged from original model)
- **Outbound guardrails**: Execute on **every Hub API call** from the agent
- **Per-API configuration**: Wildcard pattern support (e.g., `/api/agent/v1/requests/*/updates`)
- **Response model**: Allow, Alert, Deny (each guardrail returns one of these)
- **Failure policy**: Defaults to Deny (fail-closed)

### Agent Response Handling

- **Agents update requests directly via Hub APIs** (Option A)
- **sx-observer does NOT forward responses** back to Signal Exchange
- **Outbound Hub API calls pass through sidecar guardrails**

### Sidecar Interception Scope

| Traffic Type | Sidecar Can Intercept |
|--------------|----------------------|
| ✅ Inbound `/dispatch` requests | Yes |
| ✅ Outbound Hub API calls | Yes |
| ⚠️ Tool Gateway calls | Yes (early enforcement); Tool Gateway also enforces authoritatively |
| ⚠️ Model Gateway calls | Yes (early enforcement); Model Gateway also enforces authoritatively |
| ❌ CPU/memory usage | No (tracked by Kubernetes) |
| ❌ Token consumption | No (tracked by Model Gateway) |

---

## Implementation Details Deferred

The following are explicitly deferred to implementation:

| Area | Deferred Items |
|------|----------------|
| **Performance** | Latency optimization, parallelization strategies, caching |
| **Algorithms** | Rate limiting algorithms, pattern matching optimization |
| **Thresholds** | Default quota values, timeout values, retry policies |
| **Storage** | State persistence for quotas and budgets |
| **Error Codes** | Complete error code taxonomy |
| **Wire Formats** | gRPC vs HTTP, serialization formats |

---

## Related Documentation

### Seer Design
- [Guardrails Concepts](../../implementation-concepts/guardrails.md)
- [Authority Enforcement Concepts](../../implementation-concepts/authority-enforcement.md)
- [Agent Runtime](../agent-runtime/README.md)
- [Agent Lifecycle Manager](../agent-lifecycle-manager/README.md)

### Hub Documentation
- [ADR-0072: Guardrails Two-Layer Model](../../../../olympus-hub-docs/decision-logs/0072-seer-guardrails-two-layer-model.md)
- [ADR-0073: Authority Enforcement via OPA](../../../../olympus-hub-docs/decision-logs/0073-seer-authority-enforcement-opa.md)
- [ADR-0074: Seer Runtime on Atlantis](../../../../olympus-hub-docs/decision-logs/0074-seer-runtime-atlantis-based.md)
- [ADR-0104: Agent Runtime Detailed Design](../../../../olympus-hub-docs/decision-logs/0104-seer-agent-runtime-detailed-design.md)

### Original Content (Migrated)
- `../guardrails.md` — Runtime enforcement content migrated to Guardrail Service
- `../authority-enforcement.md` — Runtime enforcement content migrated to Authority/Policy Enforcement Services

---

*This document summarizes the design scope for Seer Sidecar. Refer to individual service documents for detailed design.*
