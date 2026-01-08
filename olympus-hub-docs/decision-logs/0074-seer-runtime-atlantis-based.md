# ADR-0074: Seer Runtime on Atlantis Infrastructure

**Status**: Accepted  
**Date**: 2026-01-08  
**Category**: seer

---

## Context

Seer agents require a runtime execution environment. We needed to decide whether to build a custom runtime or leverage existing Olympus infrastructure.

Options considered:
1. Custom Seer runtime (new infrastructure)
2. AWS Lambda / serverless functions
3. Atlantis (Olympus managed Kubernetes)
4. Hybrid approach

---

## Decision

Seer Runtime is built entirely on **Olympus Atlantis** (managed EKS) with these components:

### Infrastructure Stack

| Component | Technology | Role |
|-----------|------------|------|
| **Atlantis** | AWS EKS | Container orchestration |
| **Heracles** | Kong-based | API Gateway, ingress |
| **Istio** | Service mesh | mTLS, traffic control |
| **Argo Rollouts** | Progressive delivery | Canary, blue-green |
| **zone-vault** | Banzai Vault | Secrets management |

### Deployment Flow

```
Hub Operators → emit CRDs → Seer Operator → K8s Deployments → Atlantis
```

### Pod Composition

Each Employed Agent pod contains:
1. **Main container**: Raw Agent (OCI image from Training Spec)
2. **Istio sidecar**: mTLS, telemetry (auto-injected)
3. **Guardrail sidecars**: Before/after enforcement

### Request Dispatch

```
Signal Exchange → Heracles → K8s Service → Istio → Agent Pod
```

Session affinity is opportunistic (agents must be stateless).

---

## Consequences

### Positive
- Leverages proven, battle-tested infrastructure
- Consistent with other Olympus services
- Rich observability via Watch integration
- Istio provides mTLS, traffic management for free
- Argo Rollouts enables safe progressive delivery

### Negative
- Cold start latency for new pods
- Kubernetes complexity (mitigated by Seer Operator abstraction)
- No VM affinity (agents must use Agent Memory for state)

### Neutral
- Credentials injected as environment variables (zone-vault)
- Configuration changes require redeployment (no hot-reload)
- All egress through Istio Egress Gateway

---

## Related

- [Runtime Deployment Subsystem](../../olympus-seer-docs/seer-design/subsystems/runtime-deployment.md)
- [Atlantis Documentation](https://atlantis.olympus.tech/)
- [Heracles Documentation](https://heracles.olympus.tech/)
- [Employment Spec CRD](../../olympus-seer-docs/seer-design/hub-integration/employment-spec-crd.md)

