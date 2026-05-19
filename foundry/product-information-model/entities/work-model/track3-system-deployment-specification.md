# System Deployment Specification

**Model:** Work Model
**Track:** Track 3: The Run Track (Stability & Operations) — Artifact
**Owner:** DevOps, Platform Engineering, SRE

## Definition

An **environment-specific deployment specification** for a sealed System Version. The System Deployment Specification references an immutable System Version and provides all environment-specific runtime and deployment configuration — resource limits, replica counts, environment variables, secrets references, network policies, and platform-specific artifact mappings. The System Version itself never changes between environments; only deployment parameters vary.

System Deployment Specification = System Version + Environment-Specific Configuration + Runtime Artifact References.

Replaces the former **System Deployment Descriptor (SDD)**. See DR-036 D5.

> **Maps to runtime-defined artifacts, not UPIM entities.** The specific artifact names (Kubernetes Deployment, Helm release, ECS Task Definition, Lambda function configuration) are determined by the runtime platform. The System Deployment Specification is the model's abstraction over these platform-specific deployment primitives.

> **Independent versioning.** The System Deployment Specification has its own version stream reflecting **deployment progression** — resource tuning, scaling policy changes, script updates — independent of the System Version's functional version.

## Purpose

Separates *what is built and verified* (System Version) from *how it runs in a specific environment* (System Deployment Specification). Without this separation:

- Environment-specific configuration gets embedded in build artifacts, preventing promotion across environments
- SRE cannot tune production sizing without triggering a new System Version
- Deployment scripts and rollback procedures have no structured, versioned home at the System level
- Product-level deployment cannot compose consistent System-level specifications

## Fields

| Field | Type | Description |
|---|---|---|
| System Version | Reference (Track 2) | The sealed System Version this specification deploys |
| Target Environment | Reference (Dim 7) | The Deployment Environment this specification targets |
| Specification Version | String | Deployment progression version (e.g., `sds-1.0`, `sds-1.2`) — independent of System Version |
| Resource Configuration | Structured Config | CPU limits, memory limits, storage, GPU allocation — environment-specific resource sizing |
| Replica Configuration | Structured Config | Replica count, autoscaling policies, availability zone distribution |
| Environment Variables | Map | Environment-specific variables and secrets references |
| Runtime Artifact References | List | Platform-specific artifact references (e.g., K8s Deployment name, Helm release name, pod spec) |
| Network Configuration | Structured Config | Ingress rules, network policies, service mesh configuration |
| Pre-rollout Scripts | List | Scripts/applications before deployment: prerequisite validation, cache warming |
| Post-deployment Validation Scripts | List | Scripts/applications after deployment: health checks, smoke tests |
| Rollback Scripts | List | Scripts/applications on rollback: state restoration, migration reversal |
| Last Updated | DateTime | When this specification version was created or modified |

## Statuses

| Status | Description |
|---|---|
| Draft | Specification is being authored or modified |
| Ready | Configuration complete and validated for the target environment |
| Active | Current deployment specification for this System Version in this environment |
| Superseded | A newer specification version has replaced this one |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Specifies deployment of | System Version (Track 2) | References a sealed System Version |
| Targets | Deployment Environment (Dim 7) | Targets a specific environment |
| Composed into | Product Deployment Specification (Track 3) | Composed by reference into Product Deployment Specifications |
| Applied by | Deployment Task (Track 3) | Applied to an environment by a Deployment Task (System-level) |
| Produced by | Deployment Planning Task (Track 3) | Deployment Planning Task creates/updates specification versions |

## Example

### payments-system v3.1.0 → production-latam

```
System Deployment Specification: payments-system v3.1.0 → production-latam (sds-1.2)
├── System Version: payments-system v3.1.0
│   └── BOM: payments-service v2.3.1, payment-reconciler v1.4.0, payment-notification-worker v1.2.0
├── Target Environment: production-latam
├── Resource Configuration:
│   ├── payments-service: CPU 2 cores (limit 4), Memory 4Gi (limit 8Gi)
│   ├── payment-reconciler: CPU 1 core, Memory 2Gi
│   └── payment-notification-worker: CPU 0.5 core, Memory 512Mi
├── Replica Configuration:
│   ├── payments-service: min 3 (3-AZ regulatory), max 12, target CPU 70%
│   └── payment-notification-worker: min 2, max 6
├── Environment Variables:
│   ├── DB_HOST: payments-db.latam.internal
│   ├── SETTLEMENT_REGION: LATAM
│   └── SECRETS_REF: vault://payments/prod-latam
├── Runtime Artifact References:
│   ├── K8s Deployment: payments-service
│   ├── K8s Deployment: payment-reconciler
│   ├── K8s CronJob: payment-reconciler-schedule
│   └── K8s Deployment: payment-notification-worker
├── Network Configuration:
│   ├── Ingress: payments.latam.internal (internal only)
│   └── Network Policy: allow from fx-system, compliance-system
├── Pre-rollout Scripts:
│   └── 001-validate-db-migration-prereqs.sh
├── Post-deployment Validation Scripts:
│   └── 002-payments-smoke-test.py
└── Rollback Scripts:
    └── 003-rollback-payments-migration.sh
```

---
