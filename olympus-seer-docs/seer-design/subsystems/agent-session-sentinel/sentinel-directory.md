# Sentinel Directory

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-13  
> **Design Level**: C2 (Container)

---

## Overview

Sentinel Directory is the registry for Sentinel Specs and Deployments. It provides search, version tracking, and deployment status for sentinels.

**Key Principle**: Sentinel Directory maintains a searchable index of all sentinels, their versions, deployment status, and associated metadata.

---

## Architecture

```mermaid
flowchart TB
    subgraph SD[Sentinel Directory]
        Registry[Sentinel Registry]
        SearchIndex[Search Index]
        VersionTracker[Version Tracker]
        StatusTracker[Status Tracker]
    end
    
    subgraph ExternalSystems[External Systems]
        SSM[Sentinel Spec Manager]
        SO[Sentinel Operators]
        SL[Sentinel Levers]
        SeerOp[Seer Operator]
    end
    
    SSM --> Registry
    SO --> Registry
    SL --> StatusTracker
    SeerOp --> StatusTracker
    Registry --> SearchIndex
    Registry --> VersionTracker
```

---

## Functional Scope

### Sentinel Registry

Sentinel Directory maintains a registry of Sentinel Specs:

#### Registry Entry Structure

```yaml
sentinel_entry:
  sentinel_id: "stuck-agent-detector"
  sentinel_name: "Stuck Agent Detector"
  sentinel_type: "realtime"  # realtime | analytical
  version: "1.0.0"
  workbench_id: "acme-disputes"
  target_scope:
    workbench_ids: ["acme-disputes"]
    agent_ids: []
  state: "deployed"  # drafted | validated | deployed | suspended | archived
  deployment_status:
    deployment_id: "stuck-agent-detector-deployment"
    replicas: 2
    active_replicas: 2
    last_deployment: "2026-01-13T10:00:00Z"
  metadata:
    created_at: "2026-01-13T09:00:00Z"
    created_by: "user@acme.com"
    updated_at: "2026-01-13T10:00:00Z"
```

#### Registry Indexes

| Index | Purpose |
|-------|---------|
| **By Sentinel ID** | Direct lookup |
| **By Workbench** | Workbench-scoped sentinels |
| **By Sentinel Type** | Realtime vs. Analytical |
| **By State** | Active sentinels |
| **By Deployment Status** | Deployment health |

---

### Search & Discovery

Sentinel Directory provides search capabilities:

#### Search Queries

| Query Type | Description | Example |
|-----------|-------------|---------|
| **By Workbench** | Find sentinels for a workbench | `workbench_id=acme-disputes` |
| **By Sentinel Type** | Find realtime or analytical sentinels | `type=realtime` |
| **By Agent** | Find sentinels targeting an agent | `target_agent_id=fraud-analyst` |
| **By State** | Find sentinels in a specific state | `state=deployed` |
| **By Deployment Status** | Find sentinels by deployment health | `deployment_status=healthy` |

#### Search Example

```yaml
search_query:
  workbench_id: "acme-disputes"
  sentinel_type: "realtime"
  state: "deployed"
  
search_results:
  - sentinel_id: "stuck-agent-detector"
    sentinel_name: "Stuck Agent Detector"
    state: "deployed"
    deployment_status: "healthy"
  - sentinel_id: "cost-anomaly-detector"
    sentinel_name: "Cost Anomaly Detector"
    state: "deployed"
    deployment_status: "healthy"
```

---

### Version Tracking

Sentinel Directory tracks sentinel versions:

#### Version History

```yaml
version_history:
  sentinel_id: "stuck-agent-detector"
  versions:
    - version: "1.0.0"
      state: "deployed"
      deployed_at: "2026-01-13T10:00:00Z"
      deployment_id: "stuck-agent-detector-deployment-v1"
    - version: "0.9.0"
      state: "archived"
      archived_at: "2026-01-13T09:00:00Z"
```

#### Version Compatibility

- **Version tracking** for spec evolution
- **Compatibility matrix** for version upgrades
- **Migration paths** for version transitions

---

### Deployment Status Tracking

Sentinel Directory tracks deployment status:

#### Deployment Status

| Status | Description |
|--------|-------------|
| **Healthy** | All replicas active, no errors |
| **Degraded** | Some replicas inactive, errors present |
| **Unhealthy** | All replicas inactive, critical errors |
| **Unknown** | Status cannot be determined |

#### Status Update Flow

```mermaid
sequenceDiagram
    participant SeerOp as Seer Operator
    participant SD as Sentinel Directory
    participant Deployment as Sentinel Deployment
    
    SeerOp->>Deployment: Reconcile Deployment CRD
    Deployment->>Deployment: Update replica status
    Deployment->>SeerOp: Status update
    SeerOp->>SD: Update deployment status
    SD->>SD: Update registry entry
```

---

## Integration Points

### Upstream Integration

| Service | Integration Method | Purpose |
|---------|-------------------|---------|
| **Sentinel Spec Manager** | Spec registration API | Register new specs |
| **Sentinel Operators** | Lifecycle API | Update lifecycle state |
| **Sentinel Levers** | Status update API | Update runtime status |
| **Seer Operator** | Deployment status API | Update deployment status |

### Downstream Integration

| Service | Integration Method | Purpose |
|---------|-------------------|---------|
| **Search Consumers** | Search API | Query sentinel registry |

---

## Key Design Decisions

### Registry Model

- **Centralized registry** for all sentinels
- **Searchable indexes** for efficient queries
- **Version tracking** for spec evolution

### Status Tracking

- **Real-time status updates** from Seer Operator
- **Deployment health** monitoring
- **State synchronization** across systems

### Discovery Model

- **Workbench-scoped** sentinel discovery
- **Agent-scoped** sentinel discovery
- **Type-based** sentinel filtering

---

## Related Documentation

- [Sentinel Spec Manager](./sentinel-spec-manager.md) — Spec structure and registration
- [Sentinel Operators](./sentinel-operators.md) — Lifecycle management
- [Sentinel Levers](./sentinel-levers.md) — Runtime controls

---

*Sentinel Directory provides a searchable registry of Sentinel Specs and Deployments with version tracking and deployment status.*
