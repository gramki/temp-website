# Istio Service Mesh

> **Status:** 🔴 Stub — Placeholder for expansion

## Overview

**Istio** is the service mesh infrastructure underlying Olympus Hub, providing service-to-service communication, traffic management, security, and observability for all workloads in the Kubernetes environment.

---

## Purpose in Olympus Hub

Istio provides:

- **Traffic Management** — Intelligent routing, load balancing, and traffic control
- **Security** — Mutual TLS (mTLS), authentication, and authorization between services
- **Observability** — Distributed tracing, metrics, and logging
- **Resilience** — Retries, timeouts, circuit breakers, and fault injection

---

## Key Components

### Envoy Sidecar Proxies

Every Hub service pod includes an Envoy sidecar proxy that:
- Intercepts all inbound/outbound traffic
- Enforces mTLS between services
- Collects telemetry data
- Applies traffic policies

### Control Plane (Istiod)

The Istio control plane manages:
- Service discovery
- Certificate management
- Configuration distribution
- Policy enforcement

---

## Integration with Hub Subsystems

| Subsystem | Istio Usage |
|-----------|-------------|
| **Signal Exchange** | Service-to-service routing for application dispatch |
| **Automation Runtimes** | Traffic routing to runtime pods |
| **I/O Gateways** | Ingress traffic management |
| **Heracles Gateway** | Upstream service routing |

---

## Extensions in Use

### SLIME (Smart Limiter for Istio Mesh Enablement)

- Intelligent traffic management extensions
- Enhanced load balancing algorithms
- Dynamic rate limiting

### Aeraki Mesh

- Protocol extensions beyond HTTP/gRPC
- Support for Dubbo, Thrift, and other protocols
- Enhanced observability for non-HTTP traffic

---

## Session Stickiness

For stateful agent sessions, Istio provides:

- **Header-based routing** — Route by `X-MCP-Transport-Session`
- **Consistent hashing** — Session affinity for agent instances
- **Subset routing** — Target specific host groups

---

## Security Configuration

### mTLS Mode

```yaml
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: hub-strict-mtls
  namespace: olympus-hub
spec:
  mtls:
    mode: STRICT
```

### Authorization Policies

Integration with Cipher IAM for:
- SPIFFE-based identity verification
- Request-level authorization
- Cross-namespace access control

---

## Traffic Policies

### Timeout Configuration

| Service Type | Connect | Read | Write |
|--------------|---------|------|-------|
| Sync APIs | 10s | 30s | 30s |
| MCP Sessions | 10s | 30min | 30min |
| Batch Jobs | 10s | 2h | 2h |

### Retry Policies

- Automatic retries for transient failures
- Configurable retry budgets per service
- Exponential backoff with jitter

---

## Observability Integration

Istio exports telemetry to:

- **Olympus Watch** — Metrics, traces, and access logs
- **OpenTelemetry Collector** — Distributed tracing
- **Prometheus** — Service mesh metrics

---

## Related Documentation

- [Traffic Management](./traffic-management.md) — Detailed traffic configuration
- [Heracles Gateway](./heracles-gateway.md) — API gateway integration
- [Hub Application APM](../04-subsystems/supporting-systems/hub-application-apm.md) — Application observability

---

## References

- [Istio Documentation](https://istio.io/latest/docs/)
- [SLIME Project](https://github.com/slime-io/slime)
- [Aeraki Mesh](https://www.aeraki.net/)
- [Tetrate Blog: SLIME and Aeraki](https://tetrate.io/blog/introducing-slime-and-aeraki-in-the-evolution-of-istio-open-source-ecosystem)

