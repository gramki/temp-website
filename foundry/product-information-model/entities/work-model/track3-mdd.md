# Module Deployment Descriptor (MDD)

**Model:** Work Model
**Track:** Track 3: The Run Track (Stability & Operations) — Artifact
**Owner:** SRE, DevOps, Platform Engineering

## Definition

An **environment-specific deployment specification** for a Module Package Version in a specific environment. The MDD composes SDDs by reference, adds Module-level environment configuration (monitoring thresholds, scaling policies, probe schedules), and includes **pre-rollout, validation, and rollback scripts or applications** that facilitate migrations, post-deployment checks, and recovery. The MDD is a **system in its own right** — it orchestrates the coordinated deployment of all systems within a Module Package Version to a specific environment.

MDD = Module Package Version (by reference) + SDDs (by reference) + Module-level Environment Config + Deployment Scripts.

MDD is the **integrated deployment specification** — it describes how a Module Package Version is deployed as a coordinated unit to a specific environment. Where the Module Package Version defines *what* is deployed (environment-independent composition), the MDD defines *how* and *where* it is deployed (environment-specific specification).

MDD has its own version, reflecting **deployment progression** — changes to deployment scripts, environment configuration, or SDD composition — independent of both Module Version (functional) and Module Package Version (operator-facing systems). Three independent version streams exist at the integrated level: Module Version, Module Package Version, and MDD.

**Multiple MDDs per environment are valid.** Reasons include:
- **Fault isolation:** Separate deployment descriptors for different fault domains within the same environment
- **Service quality differentiation:** Different resource allocations for different tenant segments
- **Deployment stages:** Canary MDD vs. full-rollout MDD for the same environment
- **Product-level isolation:** Different products sharing a Module may need isolated deployments in the same environment

> **MDD is not Module Package Version.** Module Package Version is an environment-independent artifact that enriches Module Version with operational systems and wiring. MDD is an environment-specific specification that describes how to deploy that Module Package Version to a specific environment. Module Package Version answers "what is deployed?" MDD answers "how is it deployed here?" See DR-028, DR-029.
>
> **MDD scripts are engineering work.** Pre-rollout scripts (database migrations, cache warming), validation scripts (post-deployment health checks, integration smoke tests), and rollback scripts (revert migrations, restore state) are code artifacts. Creating or modifying these scripts is work within Deployment Planning Tasks. The MDD is a "system" because it contains executable logic, not just configuration.

## Fields

| Field | Type | Description |
|---|---|---|
| Module Package Version | Reference (Track 3) | The Module Package Version this descriptor deploys |
| Target Environment | Reference (Dim 7) | The Deployment Environment this descriptor targets |
| MDD Version | String | Deployment progression version (e.g., `mdd-1.0`, `mdd-2.1`) — independent of Module Version and Module Package Version |
| SDDs | List of References (Track 3) | SDD versions composed by reference — one per System (product + operational) in the Module Package Version |
| Module-level Environment Config | Structured Config | Environment-specific Module-level configuration: monitoring thresholds, alerting rules, scaling coordination, probe schedules, cross-system communication config |
| Pre-rollout Scripts | List | Scripts/applications to run before deployment: database migrations, cache warming, feature flag activation, prerequisite validation |
| Validation Scripts | List | Scripts/applications to run after deployment: health checks, integration smoke tests, SLA verification, data consistency checks |
| Rollback Scripts | List | Scripts/applications to run on rollback: migration reversals, state restoration, flag deactivation |
| Deployment Strategy Override | Enum (optional) | If different from the default for this environment: `Canary` / `Blue-Green` / `Rolling` / `Direct` |
| Last Updated | DateTime | When this MDD version was created or modified |

## Statuses

| Status | Description |
|---|---|
| Draft | MDD is being authored or modified; scripts under development |
| Ready | All SDDs referenced; all scripts validated; environment config complete |
| Approved | MDD has passed change management review and is cleared for deployment |
| Active | MDD is the current deployment specification for this Module Package Version in this environment |
| Superseded | A newer MDD version has replaced this one |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Specifies deployment of | Module Package Version (Track 3) | MDD specifies how a Module Package Version is deployed to a specific environment |
| Composes | SDD(s) (Track 3) | MDD composes SDDs by reference for all systems within the Module Package Version |
| Targets | Deployment Environment (Dim 7) | MDD targets a specific environment |
| Composed into | PDD (Track 3) | MDD is composed by reference into a PDD for complete-level deployment |
| Applied by | Deployment Task (Track 3) | MDD version is applied to an environment by a Deployment Task (integrated level) |
| Produced by | Deployment Planning Task (Track 3) | Deployment Planning Task creates/updates MDD versions and their scripts |
| Informed by | Operational Readiness (Dim 7) | Operational readiness status informs whether an MDD should be created for an environment |

## Examples

### MDD for Payments Module Package Version in production-latam

```
MDD: Payments Module Package Version v2.3.0 → production-latam (mdd-3.1)
├── Module Package Version: Payments Module Package Version v2.3.0
├── Target Environment: production-latam
├── SDDs (by reference):
│   ├── payments-service v2.3.3 → production-latam (sdd-1.2)
│   ├── payment-gateway v1.2.1 → production-latam (sdd-2.0)
│   ├── payments-healthcheck v1.2.0 → production-latam (sdd-1.0)
│   └── payment-reconciler v2.1.0 → production-latam (sdd-1.1)
├── Module-level Environment Config:
│   ├── Monitoring: P95 latency alert threshold = 250ms (LATAM baseline is higher)
│   ├── Alerting: PagerDuty escalation → latam-payments-oncall
│   ├── Probe schedule: payments-healthcheck runs every 60s against BRL/MXN corridors
│   └── Automation: payment-reconciler runs daily at 02:00 BRT
├── Pre-rollout Scripts:
│   ├── 001-migrate-payments-db.sh (schema migration for new settlement fields)
│   └── 002-warm-fx-rate-cache.py (pre-populate FX rate cache for LATAM corridors)
├── Validation Scripts:
│   ├── 001-healthcheck-all-systems.sh (verify all pods healthy)
│   ├── 002-smoke-test-brl-payment.py (end-to-end BRL payment test)
│   └── 003-verify-reconciler-schedule.sh (confirm CronJob is scheduled)
└── Rollback Scripts:
    ├── 001-rollback-payments-db.sh (revert schema migration)
    └── 002-restore-previous-deployment.sh (kubectl rollout undo)
```

### Multiple MDDs for same environment (fault isolation)

```
MDD: Payments Module Package Version v2.3.0 → production-latam/zone-a (mdd-3.1-zone-a)
  └── Isolated to availability zone A for fault domain separation

MDD: Payments Module Package Version v2.3.0 → production-latam/zone-b (mdd-3.1-zone-b)
  └── Isolated to availability zone B, different scaling thresholds
```

---
