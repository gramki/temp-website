# Standalone Service vs Management Subsystem

**Status:** Decided

**Question:** Does Workspace Session Management deploy as a standalone service, or as a subsystem within the existing Management module?

## Options

| Aspect | Standalone service | Management subsystem |
|--------|-------------------|----------------------|
| **Deployment** | Own container, own scaling | Shares Management deployment |
| **Database** | Own schema/tables | Tables in Management database |
| **Scaling driver** | Heartbeats: 15s × N sessions ≈ 67/s per 1000 active sessions | Coupled to Management config-read load |
| **Failure isolation** | Session Management crash does not affect Validation, WCM, provisioning | Shared fate with all Management subsystems |
| **Event throughput** | High-frequency heartbeats + state events | Mixes with Management's low-frequency config events |
| **Latency** | Heartbeat + query must be fast (200ms target) | Management is less latency-sensitive |
| **Data relationships** | FK references to Foundry/Workbench/User (Management tables) | Natural join; same DB |
| **Operational surface** | +1 service to deploy and monitor | No additional deployment |
| **Event publishing** | Own Atropos producer | Shared with Management events |
| **Team ownership** | Can be separate team | Same team as Management |

## Factors favoring standalone

- **Heartbeat throughput** scales with session count, not admin API traffic. At 10,000 concurrent sessions, heartbeats alone are ~667/s per Foundry before counting state transitions and Orchestrator queries.
- **Failure isolation:** A bug in liveness timeout logic or heartbeat ingestion should not take down Foundry provisioning, Work Catalog sync, or Validation.
- **Independent release cycle:** Session lifecycle APIs can ship without redeploying all of Management.
- **Extract path:** Own schema without FK constraints makes a future dedicated database straightforward.

## Factors favoring subsystem

- **Smaller operational surface** for early deployments — one fewer container to operate.
- **Shared connection pooling** to PostgreSQL.
- **Simpler initial wiring** — Management already touches session-adjacent provisioning concepts.
- **Natural joins** if FK constraints to Foundry and Workbench tables are desired.

## Decision

**Standalone service, shared database, no FK constraints.**

Session Management deploys as a **separate container** in the same Kubernetes namespace as Management, with:

- **Same PostgreSQL instance**, dedicated schema (e.g. `session_management`)
- **No foreign key constraints** to Management tables — `foundry_id`, `workbench_id`, and `user_id` stored as plain columns
- **Logical coupling by convention** — callers (Orchestrator) supply valid IDs; Session Management does not call Management API on every request for validation
- **Own Atropos producer** for session events (outbox table in session schema recommended)
- **Independent horizontal scaling** based on heartbeat and query load

Rationale: The heartbeat throughput argument (~67/s per 1000 sessions) and failure isolation outweigh the operational cost of one additional service. Management remains the configuration plane; Session Management is the session control plane.

### Deployment sketch

```
Namespace: foundry-management
├── management (existing)
├── workspace-session-management (new)
└── workspace-session-infrastructure (new, separate concern)
```

Both Management and Session Management use the same database credentials secret; schema migration pipelines are independent.

### Migration and ownership boundaries

| Concern | Owner |
|---------|-------|
| Foundry / Workbench / User entities | Management |
| Session records and state | Session Management |
| Pod / PVC / URL | Session Infrastructure |
| Work Orders | Orchestrator + WO Runtime |

No cascading deletes from Management entity removal to session rows — orphaned sessions are cleaned by admin retention jobs or explicit delete APIs.

## Read next

- [../requirements.md](../requirements.md) — scalability NFRs
- [../session-api.md](../session-api.md) — service API surface
- [../../README.md](../../README.md) — module overview
