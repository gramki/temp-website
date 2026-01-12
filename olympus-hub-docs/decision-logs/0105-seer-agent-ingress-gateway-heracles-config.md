# ADR-0105: Agent Ingress Gateway as Heracles Configuration Layer

**Status**: Accepted  
**Date**: 2026-01-12  
**Authors**: Architecture Team

---

## Context

Seer requires a mechanism to route requests from Signal Exchange to deployed agents. The architecture needs to:

1. Receive request updates from sx-observer
2. Route to the appropriate agent pods
3. Apply subscription-scoped policies
4. Load balance across agent replicas

Two approaches were considered:

1. **Separate Service**: Deploy Agent Ingress Gateway as a standalone service
2. **Heracles Configuration**: Implement as configuration on the existing Heracles gateway

---

## Decision

**Agent Ingress Gateway is implemented as configuration on Heracles, not as a separate service.**

### Implementation

- Ingress rules are created as Kong Ingress resources
- Atropos topics connect sx-observer to ingress paths
- K8s Services provide load balancing to agent pods
- zone-auth plugin provides authentication

### Path Structure

```
/seer/subscription/{subscription_id}/data-plane/workbench/{workbench_id}/agents/{agent_id}/dispatch
```

---

## Rationale

### Benefits of Configuration Approach

| Benefit | Description |
|---------|-------------|
| **Operational Simplicity** | No additional service to deploy, monitor, scale |
| **Proven Infrastructure** | Leverages battle-tested Heracles/Kong |
| **Consistent Security** | Same auth model as other Hub services |
| **Lower Latency** | One less hop in the request path |

### Why Not Separate Service

| Concern | Assessment |
|---------|------------|
| **Isolation** | Not required — agents are already isolated by namespace |
| **Custom Logic** | Minimal — filtering done by sx-observer, not ingress |
| **Scaling** | Kong already scales; no benefit from separate service |

---

## Consequences

### Positive

- Reduced operational complexity
- Consistent with Hub infrastructure patterns
- No new service to maintain
- Faster request routing

### Negative

- Less flexibility for custom routing logic at ingress
- Coupled to Heracles lifecycle and capabilities

### Neutral

- Seer Operator must create Kong Ingress resources
- Ingress configuration follows Heracles patterns

---

## Implementation Notes

### Seer Operator Responsibilities

1. Create Ingress resource when agent is deployed
2. Configure zone-auth plugin for sx-observer authentication
3. Create K8s Service for agent pods
4. Delete resources on agent retirement

### Signal Exchange Isolation

Signal Exchange remains **unaware** of Agent Ingress Gateway:

- Signal Exchange publishes to workbench-level topics
- sx-observer subscribes and filters
- sx-observer publishes to agent-specific topics
- Agent Ingress Gateway (Heracles) receives and routes

---

## Related Documentation

- [Agent Ingress Gateway Design](../../olympus-seer-docs/seer-design/subsystems/agent-ingress-gateway/README.md)
- [Heracles Gateway](../05-infrastructure/heracles-gateway.md)
- [ADR-0010: API Gateway Approach](./0010-api-gateway-approach.md) — Original Heracles decision
