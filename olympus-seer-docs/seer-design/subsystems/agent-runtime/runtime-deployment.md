# Seer Runtime & Deployment

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-08

---

## Overview

Seer Runtime provides the **execution environment for Employed Agents** within the Hub ecosystem. It leverages Olympus infrastructure services:

- **Atlantis** — Managed Kubernetes (EKS) for container orchestration
- **Heracles** — Traffic management (ingress, egress, service mesh)
- **Istio** — Service mesh for mTLS, traffic control, observability

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        SEER RUNTIME ARCHITECTURE                             │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                      HUB CONTROL PLANE                               │   │
│   │                                                                       │   │
│   │   Hub Operators                    Signal Exchange                   │   │
│   │        │                                │                            │   │
│   │        │ emit CRDs                      │ dispatch requests          │   │
│   │        ▼                                ▼                            │   │
│   └────────┼────────────────────────────────┼────────────────────────────┘   │
│            │                                │                                │
│   ┌────────┼────────────────────────────────┼────────────────────────────┐   │
│   │        │         SEER CONTROL PLANE     │                            │   │
│   │        ▼                                │                            │   │
│   │   ┌─────────────┐                       │                            │   │
│   │   │    Seer     │                       │                            │   │
│   │   │  Operator   │                       │                            │   │
│   │   └──────┬──────┘                       │                            │   │
│   │          │ create deployments           │                            │   │
│   └──────────┼──────────────────────────────┼────────────────────────────┘   │
│              │                              │                                │
│   ┌──────────┼──────────────────────────────┼────────────────────────────┐   │
│   │          │         ATLANTIS (EKS)       │                            │   │
│   │          ▼                              │                            │   │
│   │   ┌─────────────────────────────────────┼───────────────────────┐    │   │
│   │   │              HERACLES               │                       │    │   │
│   │   │         (API Gateway/Ingress)       │                       │    │   │
│   │   │                                     ▼                       │    │   │
│   │   │   ┌───────────────────────────────────────────────────┐    │    │   │
│   │   │   │                 ISTIO SERVICE MESH                 │    │    │   │
│   │   │   │                                                    │    │    │   │
│   │   │   │   ┌───────────┐  ┌───────────┐  ┌───────────┐    │    │    │   │
│   │   │   │   │ Agent Pod │  │ Agent Pod │  │ Agent Pod │    │    │    │   │
│   │   │   │   │    (1)    │  │    (2)    │  │   (N)     │    │    │    │   │
│   │   │   │   └───────────┘  └───────────┘  └───────────┘    │    │    │   │
│   │   │   │                                                    │    │    │   │
│   │   │   └───────────────────────────────────────────────────┘    │    │   │
│   │   └─────────────────────────────────────────────────────────────┘    │   │
│   │                                                                       │   │
│   │   ┌───────────────────────────────────────────────────────────────┐  │   │
│   │   │  OLYMPUS SERVICES                                              │  │   │
│   │   │  • zone-vault (secrets)    • zone-auth (authentication)       │  │   │
│   │   │  • Watch (observability)   • Callisto/Europa (storage)        │  │   │
│   │   └───────────────────────────────────────────────────────────────┘  │   │
│   └───────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Deployment Flow

### 1. Hub Operator Emits CRDs

When a Scenario Deployment is created in Hub:

```yaml
# Hub emits EmploymentSpec CRD
apiVersion: seer.olympus.io/v1
kind: EmploymentSpec
metadata:
  name: fraud-analyst-acme-retail
  namespace: acme-disputes
spec:
  trainingSpecRef:
    name: fraud-analyst-v2
  workScope:
    workbench: acme-disputes
    scenarios:
      - retail-fraud-triage
  # ... full spec
```

### 2. Seer Operator Creates Deployment

Seer Operator watches for EmploymentSpec CRDs and creates Kubernetes resources:

```yaml
# Seer creates K8s Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fraud-analyst-acme-retail
  namespace: acme-disputes
spec:
  replicas: 2  # From capacity in EmploymentSpec
  selector:
    matchLabels:
      app: fraud-analyst-acme-retail
  template:
    metadata:
      labels:
        app: fraud-analyst-acme-retail
        seer.olympus.io/training-spec: fraud-analyst-v2
        seer.olympus.io/employment-spec: fraud-analyst-acme-retail
      annotations:
        sidecar.istio.io/inject: "true"
    spec:
      containers:
        # Main agent container
        - name: agent
          image: registry.olympus.io/acme/fraud-analyst:v2.1.0
          ports:
            - containerPort: 8080
              name: http
            - containerPort: 9090
              name: metrics
          resources:
            requests:
              cpu: "500m"
              memory: "1Gi"
            limits:
              cpu: "2"
              memory: "4Gi"
          env:
            - name: TOOL_GATEWAY_URL
              value: "http://tool-gateway.hub-system.svc.cluster.local"
            - name: MODEL_GATEWAY_URL
              value: "http://model-gateway.seer-system.svc.cluster.local"
            - name: MEMORY_SERVICE_URL
              value: "http://memory-service.hub-system.svc.cluster.local"
            # Credentials from zone-vault
            - name: API_KEY
              valueFrom:
                secretKeyRef:
                  name: fraud-analyst-secrets
                  key: api-key
          readinessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 5
            periodSeconds: 10
          livenessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 15
            periodSeconds: 20
        
        # Guardrail sidecar containers
        - name: guardrail-pii-detector
          image: registry.olympus.io/seer/guardrails/pii-detector:v1.0
          # ... guardrail container spec
```

---

## Pod Architecture

### Container Composition

Each Employed Agent pod contains:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          EMPLOYED AGENT POD                                  │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    MAIN CONTAINER: Raw Agent                         │   │
│   │                                                                       │   │
│   │   • OCI image from Training Spec                                     │   │
│   │   • HTTP endpoint for request dispatch (:8080)                       │   │
│   │   • Health endpoint (/health)                                        │   │
│   │   • Prometheus metrics endpoint (:9090/metrics)                      │   │
│   │   • Optional: Agent SDK                                              │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    SIDECAR: Istio Envoy Proxy                        │   │
│   │                                                                       │   │
│   │   • Automatic injection by Istio                                     │   │
│   │   • mTLS for all service-to-service communication                    │   │
│   │   • Telemetry export (traces, metrics)                               │   │
│   │   • Traffic management (routing, retries, circuit breaking)          │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    SIDECARS: Guardrails                              │   │
│   │                                                                       │   │
│   │   • Containers from Training/Employment Spec guardrail refs          │   │
│   │   • Pre-warmed worker pools for low latency                          │   │
│   │   • HTTP interception for before/after processing                    │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Resource Specification

Resources are specified at two levels:

| Level | Purpose | Example |
|-------|---------|---------|
| **Training Spec** | Requirements (minimum) | `cpu: 500m, memory: 1Gi` |
| **Employment Spec** | Allocation (actual) | `cpu: 2, memory: 4Gi, gpu: 1` |

```yaml
# Training Spec - Requirements
spec:
  resources:
    requirements:
      cpu: "500m"
      memory: "1Gi"
    optional:
      gpu: true

# Employment Spec - Allocation
spec:
  runtimeConfig:
    resources:
      requests:
        cpu: "1"
        memory: "2Gi"
      limits:
        cpu: "4"
        memory: "8Gi"
        nvidia.com/gpu: "1"
```

---

## Request Dispatch Flow

### Traffic Path

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         REQUEST DISPATCH FLOW                                │
│                                                                              │
│   Signal Exchange                                                            │
│        │                                                                     │
│        │ HTTP POST /dispatch                                                 │
│        ▼                                                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    HERACLES (API Gateway)                            │   │
│   │                                                                       │   │
│   │   • Authentication (zone-auth)                                       │   │
│   │   • Rate limiting                                                     │   │
│   │   • Request routing based on headers                                  │   │
│   │   • Session affinity (opportunistic)                                  │   │
│   └──────────────────────────────┬──────────────────────────────────────┘   │
│                                  │                                           │
│                                  ▼                                           │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    KUBERNETES SERVICE                                │   │
│   │                                                                       │   │
│   │   service: fraud-analyst-acme-retail                                 │   │
│   │   selector: app=fraud-analyst-acme-retail                            │   │
│   └──────────────────────────────┬──────────────────────────────────────┘   │
│                                  │                                           │
│                                  ▼                                           │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    ISTIO SIDECAR (Envoy)                             │   │
│   │                                                                       │   │
│   │   • mTLS termination                                                  │   │
│   │   • Before guardrails interception                                    │   │
│   └──────────────────────────────┬──────────────────────────────────────┘   │
│                                  │                                           │
│                                  ▼                                           │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    GUARDRAIL SIDECARS (Before)                       │   │
│   │                                                                       │   │
│   │   • PII detector                                                      │   │
│   │   • Prompt injection filter                                           │   │
│   └──────────────────────────────┬──────────────────────────────────────┘   │
│                                  │                                           │
│                                  ▼                                           │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    RAW AGENT CONTAINER                               │   │
│   │                                                                       │   │
│   │   POST /dispatch                                                      │   │
│   │   { request_id, update, context }                                    │   │
│   └──────────────────────────────┬──────────────────────────────────────┘   │
│                                  │                                           │
│                                  ▼                                           │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    GUARDRAIL SIDECARS (After)                        │   │
│   │                                                                       │   │
│   │   • PII redactor                                                      │   │
│   │   • Response validator                                                │   │
│   └──────────────────────────────┬──────────────────────────────────────┘   │
│                                  │                                           │
│                                  ▼                                           │
│                          Response to SX                                      │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Session Affinity

Heracles provides **opportunistic session affinity**:

- Requests with the same `request_id` are routed to the same pod when possible
- Not guaranteed — agents must be stateless
- Agent Memory provides persistence across requests

---

## Networking

### Service-to-Service Communication

All agent communication flows through **Istio service mesh**:

```yaml
# Service endpoints injected as environment variables
env:
  - name: TOOL_GATEWAY_URL
    value: "http://tool-gateway.hub-system.svc.cluster.local"
  - name: MODEL_GATEWAY_URL
    value: "http://model-gateway.seer-system.svc.cluster.local"
  - name: MEMORY_SERVICE_URL
    value: "http://memory-service.hub-system.svc.cluster.local"
  - name: CAE_URL
    value: "http://context-assembly.seer-system.svc.cluster.local"
```

### Egress Control

All outbound traffic to services **outside the workbench** must go through an Egress Gateway:

```yaml
# Istio Egress Gateway configuration
apiVersion: networking.istio.io/v1alpha3
kind: ServiceEntry
metadata:
  name: allowed-external-apis
spec:
  hosts:
    - "api.vendor.com"
  location: MESH_EXTERNAL
  ports:
    - number: 443
      name: https
      protocol: HTTPS
  resolution: DNS

---
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: vendor-api-routing
spec:
  hosts:
    - "api.vendor.com"
  tls:
    - match:
        - port: 443
          sniHosts:
            - "api.vendor.com"
      route:
        - destination:
            host: istio-egressgateway.istio-system.svc.cluster.local
            port:
              number: 443
```

**Egress Control**:
- Tenant admins control allowed external endpoints via policies
- Direct external API calls are blocked by default
- All egress is audited and logged

---

## Secrets and Configuration

### Credential Injection

Credentials from Employment Spec are injected as **environment variables**:

```yaml
spec:
  containers:
    - name: agent
      env:
        # From Kubernetes secrets (populated by zone-vault)
        - name: DATABASE_PASSWORD
          valueFrom:
            secretKeyRef:
              name: fraud-analyst-secrets
              key: db-password
        - name: API_KEY
          valueFrom:
            secretKeyRef:
              name: fraud-analyst-secrets
              key: api-key
```

**Secret Management**:
- Secrets stored in **zone-vault** (Banzai cloud vault)
- Kubernetes secrets created by Seer Operator from vault references
- Secrets rotated via vault policies

### Configuration Updates

Configuration changes **require redeployment**:

- No hot-reload for ConfigMaps
- Changes trigger rolling update via Argo Rollouts
- Zero-downtime deployment

---

## Lifecycle Operations

### Rolling Updates

When a Training Spec or Employment Spec is updated:

1. **Employment Spec must explicitly reference new Training Spec**
2. **Seer Operator detects change** and triggers deployment update
3. **Argo Rollouts** manages progressive delivery:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: fraud-analyst-acme-retail
spec:
  strategy:
    canary:
      steps:
        - setWeight: 20
        - pause: { duration: 5m }
        - setWeight: 50
        - pause: { duration: 10m }
        - setWeight: 100
```

### Kill Switch

Kill switch can be executed via two mechanisms:

| Mechanism | Effect | Use Case |
|-----------|--------|----------|
| **Scale to 0** | No pods running | Graceful shutdown |
| **Network Policy** | Traffic blocked | Immediate isolation |

```yaml
# Scale to 0
kubectl scale deployment fraud-analyst-acme-retail --replicas=0

# Network Policy (immediate isolation)
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: kill-switch-fraud-analyst
spec:
  podSelector:
    matchLabels:
      app: fraud-analyst-acme-retail
  policyTypes:
    - Ingress
    - Egress
  ingress: []  # Block all ingress
  egress: []   # Block all egress
```

---

## Raw Agent Contract

### Required Endpoints

Every Raw Agent container must expose:

| Endpoint | Purpose | Required |
|----------|---------|----------|
| `POST /dispatch` | Request dispatch | ✅ Yes |
| `GET /health` | Health/readiness | ✅ Yes |
| `GET /metrics` | Prometheus metrics | ✅ Yes |

### Request Dispatch Endpoint

```http
POST /dispatch
Content-Type: application/json

{
  "request_id": "req-12345",
  "update": {
    "type": "REQUEST_UPDATE",
    "content": { ... }
  },
  "context": {
    "compiled": { ... },
    "agent_memory": { ... }
  }
}
```

**Response:**
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "status": "success",
  "updates": [
    {
      "type": "DECISION",
      "content": { ... }
    }
  ]
}
```

### Health Endpoint

```http
GET /health

{
  "status": "healthy",
  "checks": {
    "memory": "ok",
    "model_gateway": "ok"
  }
}
```

### Metrics Endpoint

Prometheus-compatible metrics:

```http
GET /metrics

# HELP agent_requests_total Total requests processed
# TYPE agent_requests_total counter
agent_requests_total{status="success"} 1234
agent_requests_total{status="error"} 56

# HELP agent_request_duration_seconds Request duration
# TYPE agent_request_duration_seconds histogram
agent_request_duration_seconds_bucket{le="0.1"} 500
agent_request_duration_seconds_bucket{le="0.5"} 900
```

---

## Autoscaling

### Horizontal Pod Autoscaler

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: fraud-analyst-acme-retail
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: fraud-analyst-acme-retail
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
    - type: Pods
      pods:
        metric:
          name: agent_active_requests
        target:
          type: AverageValue
          averageValue: "5"
```

---

## Observability

### Tracing

- **Jaeger** for distributed tracing
- Traces from Istio envoy sidecar + OTel Agent
- Trace context propagated through all service calls

### Metrics

- **Prometheus** for metrics collection
- Pod-level (CPU, memory) + agent-level (requests, latency)
- **Kiali** for service mesh visualization

### Logging

- Stdout/stderr → Atlantis log aggregation
- Structured JSON logging recommended
- Logs shipped to **Olympus Watch**

---

## Security

### Zero-Trust Model

- **mTLS** for all service-to-service communication (Istio)
- **Network Policies** for pod isolation
- **Pod Security Policies** for container constraints
- **RBAC** for Kubernetes API access

### Workload Segregation

- Olympus Spaces for tenant isolation
- Namespace-per-workbench
- Resource quotas per namespace

---

## Ingress Path Provisioning

Seer Operator configures **Heracles cluster-ingress paths** for each Employed Agent as part of deployment.

### Path Pattern

```
/seer/subscription/{subscription_id}/data-plane/workbench/{workbench_id}/agents/{agent_id}/dispatch
```

**Characteristics**:
- **Cluster-ingress only** — Not publicly accessible
- **Per Employed Agent** — One data plane endpoint per agent
- **Internal routing** — Used by sx-observer to dispatch requests

### Ingress Configuration

```yaml
# Heracles Ingress Configuration (conceptual)
apiVersion: heracles.olympus.io/v1
kind: ClusterIngress
metadata:
  name: fraud-analyst-acme-retail-ingress
  namespace: acme-disputes
spec:
  rules:
    - path: /seer/subscription/acme-corp/data-plane/workbench/acme-disputes/agents/fraud-analyst-acme-retail/dispatch
      backend:
        service:
          name: fraud-analyst-acme-retail
          port: 8080
  authentication:
    provider: zone-auth
    clientId: sx-observer
```

### Authentication/Authorization at Ingress

| Aspect | Behavior |
|--------|----------|
| **Client Identity** | Heracles sees the client as sx-observer |
| **Credential Verification** | zone-auth verifies sx-observer credentials |
| **Agent Tokens** | Agents do NOT receive tokens validated at ingress |
| **Agent Authentication** | Agents use their own token (from EmploymentSpec, Hub Environment, or Request Context) |
| **Message Verification** | Agents verify that message is dispatched by SX and belongs to their workbench |

### Rate Limiting

Rate limiting at ingress level (if applicable):

```yaml
spec:
  rateLimit:
    requestsPerSecond: 100
    burstSize: 200
```

---

## Ingress Lifecycle

### Creation

Ingress paths are created **during deployment** after IAM profile creation/update:

```
1. EmploymentSpec Created
2. Seer Operator provisions IAM profile (see iam-provisioning.md)
3. Seer Operator creates K8s Deployment
4. Seer Operator configures Heracles ingress path
5. Agent pods start receiving traffic
```

### Updates

Seer Operator updates ingress when agent configuration changes:

| Change Type | Ingress Update |
|-------------|----------------|
| Agent renamed | Path updated |
| Service port changed | Backend updated |
| Rate limits changed | Rate limit config updated |

### Cleanup

On agent retirement:

1. Ingress path is removed from Heracles
2. Traffic stops routing to agent
3. Agent pods are terminated

---

## Integration with Heracles

### Heracles API Gateway Configuration

| Aspect | Configuration |
|--------|---------------|
| **TLS Termination** | At Heracles gateway |
| **Request Routing** | Path-based routing to agent services |
| **Health Checks** | Heracles health checks agent endpoints |

### Cluster-Ingress (Internal)

- **Not publicly accessible** — Internal cluster traffic only
- **mTLS** — All traffic encrypted via Istio
- **Service Mesh** — Traffic flows through Istio sidecar

---

## Related Documentation

- [Atlantis Overview](https://atlantis.olympus.tech/docs/overview/) — Compute infrastructure
- [Heracles Overview](https://heracles.olympus.tech/docs/getting-started/) — Traffic management
- [Guardrails](../guardrails.md) — Sidecar guardrails
- [Authority Enforcement](../authority-enforcement.md) — Runtime policy enforcement
- [Employment Spec CRD](../../hub-integration/employment-spec-crd.md) — Deployment configuration
- [Agent Lifecycle API](../agent-lifecycle-api.md) — Lifecycle operations
- [IAM Provisioning](./iam-provisioning.md) — IAM profile lifecycle
- [Signal Exchange Integration](./signal-exchange-integration.md) — sx-observer architecture
- [Agent Ingress Gateway Integration](./agent-ingress-gateway-integration.md) — Request routing
- [ADR-0074: Runtime on Atlantis](../../../../olympus-hub-docs/decision-logs/0074-seer-runtime-atlantis-based.md)

---

*Seer Runtime leverages Atlantis and Heracles to provide secure, observable, and scalable execution for Employed Agents.*
