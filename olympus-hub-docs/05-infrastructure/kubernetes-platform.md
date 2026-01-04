# Kubernetes Platform

> **Status:** 🔴 Stub — Placeholder for expansion

## Overview

**Kubernetes** is the container orchestration platform underlying Olympus Hub, providing the runtime environment for all Hub services, Automation Runtimes, and Hub Applications.

---

## Purpose in Olympus Hub

Kubernetes provides:

- **Container Orchestration** — Pod scheduling, scaling, and management
- **Service Discovery** — DNS-based service resolution
- **Configuration Management** — ConfigMaps and Secrets
- **Resource Isolation** — Namespace-based multi-tenancy
- **Rolling Updates** — Zero-downtime deployments

---

## Cluster Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Kubernetes Cluster                        │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │                   Control Plane                         │ │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐   │ │
│  │  │  API    │  │ etcd    │  │ Sched   │  │ Control │   │ │
│  │  │ Server  │  │         │  │ uler    │  │ Manager │   │ │
│  │  └─────────┘  └─────────┘  └─────────┘  └─────────┘   │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │                    Worker Nodes                         │ │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐    │ │
│  │  │   Node 1    │  │   Node 2    │  │   Node 3    │    │ │
│  │  │  ┌───────┐  │  │  ┌───────┐  │  │  ┌───────┐  │    │ │
│  │  │  │ Pods  │  │  │  │ Pods  │  │  │  │ Pods  │  │    │ │
│  │  │  └───────┘  │  │  └───────┘  │  │  └───────┘  │    │ │
│  │  └─────────────┘  └─────────────┘  └─────────────┘    │ │
│  └────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

---

## Namespace Strategy

### Hub Core Namespaces

| Namespace | Purpose |
|-----------|---------|
| `hub-core` | Signal Exchange, Workbench Management |
| `hub-gateways` | Heracles, Atropos, other I/O gateways |
| `hub-runtimes` | Atlantis, Rhea, ChronoShift |
| `hub-services` | Memory, Knowledge, Registry services |
| `hub-infra` | Redis, Kafka operators |

### Tenant Namespaces

```
hub-tenant-<tenant-id>-<workbench-id>
```

Example: `hub-tenant-acme-disputes`

---

## Resource Management

### Pod Resource Limits

```yaml
resources:
  requests:
    cpu: "100m"
    memory: "256Mi"
  limits:
    cpu: "1000m"
    memory: "1Gi"
```

### Horizontal Pod Autoscaling

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: signal-exchange
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: signal-exchange
  minReplicas: 3
  maxReplicas: 50
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

---

## Networking

### Service Types

| Type | Use Case |
|------|----------|
| **ClusterIP** | Internal service communication |
| **LoadBalancer** | External gateway access |
| **NodePort** | Development/testing |

### Network Policies

Istio service mesh provides:
- Pod-to-pod mTLS
- Traffic authorization
- Rate limiting

---

## Configuration Management

### ConfigMaps

Non-sensitive configuration:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: hub-config
data:
  LOG_LEVEL: "INFO"
  KAFKA_BOOTSTRAP: "kafka.hub-infra.svc:9092"
```

### Secrets

Sensitive data (encrypted at rest):

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: hub-secrets
type: Opaque
data:
  DATABASE_PASSWORD: <base64>
  REDIS_PASSWORD: <base64>
```

---

## Storage Classes

| Class | Backend | Use Case |
|-------|---------|----------|
| `hub-standard` | EBS gp3 | General workloads |
| `hub-fast` | EBS io2 | Databases |
| `hub-shared` | EFS | Shared file systems |

---

## Operators

Custom operators for Hub:

| Operator | Purpose |
|----------|---------|
| **Workbench Operator** | Provision tenant namespaces |
| **Application Operator** | Deploy Hub Applications |
| **Ganymede Operator** | Provision databases |

---

## Node Pools

| Pool | Instance Type | Purpose |
|------|--------------|---------|
| `core` | m6i.2xlarge | Hub core services |
| `runtime` | c6i.4xlarge | Automation Runtimes |
| `data` | r6i.2xlarge | Data services |
| `gpu` | g5.xlarge | ML workloads |

---

## Monitoring

Kubernetes metrics in Olympus Watch:

- `kube_pod_status_phase` — Pod status
- `kube_deployment_status_replicas` — Replica counts
- `container_cpu_usage_seconds_total` — CPU usage
- `container_memory_usage_bytes` — Memory usage

---

## Related Documentation

- [Istio Service Mesh](./istio-service-mesh.md) — Service mesh
- [Atlantis Runtime](../04-subsystems/automation-runtimes/atlantis-runtime.md) — Knative/KServe
- [Olympus Watch](./olympus-watch.md) — Observability

---

*Expand this document with cluster provisioning, upgrade procedures, and disaster recovery.*

