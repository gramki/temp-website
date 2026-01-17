# Seer Sidecar

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-12

## Overview

Seer Sidecar provides runtime enforcement capabilities for Employed Agents, including guardrails, authority enforcement, policy enforcement, resource quotas, fair usage budgets, and metrics collection. The sidecar runs alongside agent pods via Istio service mesh to intercept and validate all agent traffic.

---

## Design Documents

| Document | Description | Level |
|----------|-------------|-------|
| [SCOPE.md](./SCOPE.md) | Design scope, coverage summary, key decisions | Overview |
| [Guardrail Service](./guardrail-service.md) | Inbound/outbound guardrail execution, per-API configuration | C2 |
| [Authority Enforcement Service](./authority-enforcement-service.md) | Ceiling enforcement, delegation chain validation | C2 |
| [Policy Enforcement Service](./policy-enforcement-service.md) | OPA policy evaluation, violation handling | C3 |
| [Delegation Service](./delegation-service.md) | Request-scoped delegation check, authority request, token injection | C2 |
| [Resource Quota Service](./resource-quota-service.md) | Agent resource consumption tracking | C2 |
| [Fair Usage Budget Service](./fair-usage-budget-service.md) | User/customer usage tracking | C2 |
| [Metrics Service](./metrics-service.md) | Runtime metrics collection and export | C2 |
| [Hot-reload Service](./guardrail-hot-reload-service.md) | Configuration updates without restart | C2 |

---

## Key Design Decisions

### Guardrail Execution Model

- **Inbound guardrails**: Execute on `/dispatch` requests coming into the agent
- **Outbound guardrails**: Execute on **every Hub API call** from the agent (request updates, decisions, task completions, etc.)
- **Per-API configuration**: Support for wildcard patterns (e.g., `/api/agent/v1/requests/*/updates`)
- **Response model**: Each guardrail returns **Allow**, **Alert**, or **Deny**
- **Failure policy**: Defaults to **Deny** (fail-closed)

### Agent Response Handling

- Agents update requests **directly via Hub APIs** (Option A)
- sx-observer does NOT forward responses back to Signal Exchange
- Outbound Hub API calls pass through sidecar guardrails

### Sidecar Interception Scope

| Traffic Type | Sidecar Can Intercept |
|--------------|----------------------|
| ✅ Inbound `/dispatch` requests | Yes |
| ✅ Outbound Hub API calls | Yes |
| ⚠️ Tool/Model Gateway calls | Yes (early enforcement); gateways also enforce authoritatively |
| ❌ CPU/memory/token usage | No (tracked by K8s/Model Gateway) |

---

## Capabilities

Based on `olympus-hub-docs/scratchpad/seer-subsystems.md`:

- ✅ Guardrail execution (inbound on dispatch, outbound on Hub API calls)
- ✅ Ability to update guardrails without restarts (hot-reload)
- ✅ Metrics collection
- ✅ Policy enforcement (OPA-based)
- ✅ Authority enforcement (ceilings, delegation chains)
- ✅ Request-scoped delegation (pre-guardrail check, authority request, token injection)
- ✅ Resource quotas (agent resource consumption)
- ✅ Fair usage budgets (user/customer usage)

---

## Related Documentation

### Conceptual
- [Seer Sidecar Concept](../../implementation-concepts/seer-sidecar.md) — Sidecar runtime enforcement concept
- [Guardrails Concepts](../../implementation-concepts/guardrails.md) — Two-layer model, behavioral guidelines
- [Authority Enforcement Concepts](../../implementation-concepts/authority-enforcement.md) — Multi-enforcement point architecture

### Decision Logs
- [ADR-0072: Guardrails Two-Layer Model](../../../../olympus-hub-docs/decision-logs/0072-seer-guardrails-two-layer-model.md)
- [ADR-0073: Authority Enforcement via OPA](../../../../olympus-hub-docs/decision-logs/0073-seer-authority-enforcement-opa.md)
- [ADR-0074: Seer Runtime on Atlantis](../../../../olympus-hub-docs/decision-logs/0074-seer-runtime-atlantis-based.md)
- [ADR-0104: Agent Runtime Detailed Design](../../../../olympus-hub-docs/decision-logs/0104-seer-agent-runtime-detailed-design.md)

### Related Subsystems
- [Agent Runtime](../agent-runtime/README.md) — Pod deployment, Istio sidecar integration
- [Agent Lifecycle Manager](../agent-lifecycle-manager/README.md) — Employment Spec configuration

---

*Seer Sidecar provides defense-in-depth runtime enforcement for Employed Agents through Istio service mesh interception.*
