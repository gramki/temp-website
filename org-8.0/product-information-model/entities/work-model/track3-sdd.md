# System Deployment Descriptor (SDD)

**Model:** Work Model
**Track:** Track 3: The Run Track (Stability & Operations) — Artifact
**Owner:** DevOps, Platform Engineering

## Definition

An **environment-specific deployment specification** for a single System Version. The SDD maps a System Version to one or more runtime-defined artifacts with platform-specific names — Kubernetes Services, Pod specs, Deployments, CRDs, Helm releases, cloud-native resources, or any other infrastructure primitives defined by the runtime platform. The SDD captures everything needed to deploy *this* System Version to *this* environment: resource limits, replica counts, environment variables, secrets references, network policies, and platform-specific configuration.

SDD = System Version + Environment-Specific Configuration + Runtime Artifact References.

SDD is the **atomic deployment specification** — it describes how a single System Version is deployed to a single environment. SDDs are **composed by reference** into MDDs (Module Deployment Descriptors), which add Module-level coordination, scripts, and cross-system configuration. An SDD may also be deployed independently for atomic-level deployments.

SDD has its own version, reflecting **deployment progression** — changes to resource limits, scaling policies, or runtime artifact configuration — independent of the System Version's functional version. A System Version may have multiple SDD versions as deployment configuration evolves.

> **SDD maps to runtime-defined artifacts, not UPIM entities.** The specific artifact names (Kubernetes Deployment, Helm release, ECS Task Definition, Lambda function configuration) are determined by the runtime platform, not by the information model. SDD is the model's abstraction over these platform-specific deployment primitives. The SDD does not prescribe the platform; it describes what the platform must provide for this System Version in this environment.

## Fields

| Field | Type | Description |
|---|---|---|
| System Version | Reference (Track 2) | The System Version this descriptor deploys |
| Target Environment | Reference (Dim 7) | The Deployment Environment this descriptor targets |
| SDD Version | String | Deployment progression version (e.g., `sdd-1.0`, `sdd-1.1`) — independent of System Version |
| Resource Configuration | Structured Config | CPU limits, memory limits, storage, GPU allocation — environment-specific resource sizing |
| Replica Configuration | Structured Config | Replica count, autoscaling policies, availability zone distribution |
| Environment Variables | Map | Environment-specific variables and secrets references |
| Runtime Artifact References | List | Platform-specific artifact references (e.g., K8s Deployment name, Helm release name, pod spec) |
| Network Configuration | Structured Config | Ingress rules, network policies, service mesh configuration |
| Last Updated | DateTime | When this SDD version was created or modified |

## Statuses

| Status | Description |
|---|---|
| Draft | SDD is being authored or modified |
| Ready | SDD configuration is complete and validated for the target environment |
| Active | SDD is the current deployment specification for this System Version in this environment |
| Superseded | A newer SDD version has replaced this one for the same System Version + environment |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Specifies deployment of | System Version (Track 2) | SDD specifies how a System Version is deployed to an environment |
| Targets | Deployment Environment (Dim 7) | SDD targets a specific environment |
| Composed into | MDD (Track 3) | SDD is composed by reference into an MDD for integrated-level deployment |
| Applied by | Deployment Task (Track 3) | SDD is applied to an environment by a Deployment Task (atomic level) |
| Produced by | Deployment Planning Task (Track 3) | Deployment Planning Task creates/updates SDD versions |

## Examples

### SDD for payments-service v2.3.3 in production-latam

```
SDD: payments-service v2.3.3 → production-latam (sdd-1.2)
├── System Version: payments-service v2.3.3
├── Target Environment: production-latam
├── Resource Configuration:
│   ├── CPU: 2 cores (limit: 4 cores)
│   ├── Memory: 4Gi (limit: 8Gi)
│   └── Storage: 20Gi persistent volume
├── Replica Configuration:
│   ├── Min replicas: 3 (LATAM regulatory: 3-AZ)
│   ├── Max replicas: 12
│   └── Autoscaling: target CPU utilization 70%
├── Environment Variables:
│   ├── DB_HOST: payments-db.latam.internal
│   ├── SETTLEMENT_REGION: LATAM
│   └── SECRETS_REF: vault://payments/prod-latam
├── Runtime Artifacts:
│   ├── K8s Deployment: payments-service
│   ├── K8s Service: payments-service-svc
│   └── K8s HPA: payments-service-hpa
└── Network:
    ├── Ingress: payments.latam.internal (internal only)
    └── Network Policy: allow from fx-service, payment-gateway
```

### SDD for payments-healthcheck v1.2.0 in production-latam (operational system)

```
SDD: payments-healthcheck v1.2.0 → production-latam (sdd-1.0)
├── System Version: payments-healthcheck v1.2.0
├── Target Environment: production-latam
├── Resource Configuration:
│   ├── CPU: 0.5 cores
│   └── Memory: 512Mi
├── Replica Configuration:
│   └── Replicas: 1 (probe, not load-bearing)
├── Environment Variables:
│   ├── PROBE_TARGET: payments-service-svc.latam.internal
│   ├── CORRIDORS: BRL,MXN
│   └── PROBE_INTERVAL_SEC: 60
├── Runtime Artifacts:
│   └── K8s CronJob: payments-healthcheck
└── Network:
    └── Network Policy: allow to payments-service, fx-service
```

---
