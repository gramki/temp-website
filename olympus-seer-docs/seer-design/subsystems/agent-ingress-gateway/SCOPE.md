# Agent Ingress Gateway - Scope and Design Status

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-12

---

## Scope

The **Agent Ingress Gateway** subsystem provides request routing to deployed Employed Agents. It is responsible for:

1. **Heracles Configuration** — Not a separate service, but configuration on Heracles
2. **sx-observer Integration** — Receive and filter request updates
3. **Subscription Management** — Agent subscription lifecycle
4. **Request Routing** — Scenario-based filtering and dispatch
5. **Policy Enforcement** — Subscription-scoped policies

---

## Intended Depth

This design documentation is at **C2 (Container) level** with **C3 (Component) detail** for critical mechanisms:

| Aspect | Coverage |
|--------|----------|
| **Functional Scope** | Complete — what each component does |
| **Integration Points** | Complete — hand-offs between containers |
| **Conceptual Models** | Complete — illustrated with diagrams |
| **C3 Detail Areas** | Complete — state machines, filtering algorithms, policy evaluation |
| **Data Models** | Conceptual only — no detailed schemas |
| **API Specifications** | Conceptual only — patterns illustrated |

### C3 Detail Areas

The following areas are documented at C3 (Component) level:

| Area | Document | Details |
|------|----------|---------|
| **Subscription State Machine** | subscription-lifecycle.md | States, transitions, draining algorithm |
| **Request Filtering** | request-routing.md | Filtering algorithm, scenario-to-agent mapping |
| **Policy Evaluation** | subscription-policies.md | Evaluation pipeline, precedence, violation handling |

---

## Design Documents

| Document | Description | Status |
|----------|-------------|--------|
| [README.md](./README.md) | Overview, architecture diagram, design summary | ✅ Complete |
| [architecture.md](./architecture.md) | Heracles relationship, sx-observer integration | ✅ Complete |
| [subscription-lifecycle.md](./subscription-lifecycle.md) | Subscription states, draining (C3) | ✅ Complete |
| [request-routing.md](./request-routing.md) | Routing logic, filtering algorithms (C3) | ✅ Complete |
| [subscription-policies.md](./subscription-policies.md) | Policy types, evaluation flow (C3) | ✅ Complete |
| [heracles-integration.md](./heracles-integration.md) | Cluster-ingress, authentication, TLS | ✅ Complete |
| [response-handling.md](./response-handling.md) | Agent direct updates, Data Store | ✅ Complete |
| [signal-exchange-integration.md](./signal-exchange-integration.md) | sx-observer, Atropos topics | ✅ Complete |

---

## Coverage Summary

### ✅ Architecture (architecture.md)
- Configuration-based gateway (not separate service)
- Heracles relationship and rationale
- sx-observer integration flow
- Atropos topic structure

### ✅ Subscription Lifecycle (subscription-lifecycle.md)
- Subscription creation on agent deployment
- Subscription updates (scenario changes)
- Subscription cleanup on retirement
- **C3**: State machine (pending, active, draining, inactive, deleted)
- **C3**: Draining algorithm

### ✅ Request Routing (request-routing.md)
- Atropos topic structure
- Agent subscription matching from EmploymentSpec
- **C3**: Request filtering algorithm
- **C3**: Scenario-to-agent mapping index
- Request transformation (pass-through, optional custom)
- Load balancing strategy

### ✅ Subscription Policies (subscription-policies.md)
- Policy types (rate limiting, authorization, routing)
- Policy configuration via CRD
- **C3**: Policy evaluation pipeline
- **C3**: Policy precedence resolution
- **C3**: Violation handling and DLQ

### ✅ Heracles Integration (heracles-integration.md)
- Cluster-ingress configuration (internal)
- Ingress path structure and provisioning
- zone-auth authentication
- TLS termination
- Kong plugin stack

### ✅ Response Handling (response-handling.md)
- Agent direct response (not via gateway)
- Workbench Data Store integration
- Resource URI injection
- Error handling and DLQ
- Hub API access patterns

### ✅ Signal Exchange Integration (signal-exchange-integration.md)
- Signal Exchange isolation principle
- sx-observer role and responsibilities
- Atropos topic subscription model
- Filtering logic
- Scale-to-zero support (store and forward)

---

## Key Design Decisions

1. **Heracles Configuration Layer** — Agent Ingress Gateway is configuration on Heracles, not a separate service
2. **Signal Exchange Isolation** — Signal Exchange is unaware of agents; all routing via sx-observer
3. **Agent Direct Response** — Agents update requests directly via Hub APIs

---

## Implementation Details Deferred

The following implementation details are deferred to the detailed implementation stage:

| Area | Deferred Details |
|------|------------------|
| **Kong Plugin Configuration** | Detailed plugin parameters |
| **Message Store** | Redis configuration, retention policies |
| **DLQ Processing** | Retry strategies, manual intervention |

These will be addressed during implementation with common defaults applied.

---

## Related Subsystems

- **[Agent Runtime](../agent-runtime/README.md)** — Ingress path provisioning, agent deployment
- **[Seer Sidecar](../seer-sidecar/README.md)** — Additional policy enforcement at pod level
- **[Cipher IAM Extensions](../cipher-iam-extensions/README.md)** — sx-observer authentication

---

## Related Documentation

- [Agent Runtime: Agent Ingress Gateway Integration](../agent-runtime/agent-ingress-gateway-integration.md) — Runtime perspective
- [Heracles Gateway](../../../../olympus-hub-docs/05-infrastructure/heracles-gateway.md) — Heracles documentation

---

*This scope document reflects the completed detailed design of the Agent Ingress Gateway subsystem.*
