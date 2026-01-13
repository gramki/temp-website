# Sentinel Levers

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-14  
> **Design Level**: C2 (Container)

---

## Overview

Sentinel Levers provide runtime controls for sentinels. They enable/disable sentinels, suspend execution, and provide emergency controls for immediate sentinel management.

**Key Principle**: Sentinel Levers provide operational controls that affect sentinel execution without modifying sentinel specifications.

---

## Architecture

```mermaid
flowchart TB
    subgraph SL[Sentinel Levers]
        EnableDisable[Enable/Disable Control]
        SuspendControl[Suspend Control]
        EmergencyControl[Emergency Control]
    end
    
    subgraph ExternalSystems[External Systems]
        SD[Sentinel Directory]
        RTS[Realtime Sentinel Service]
        ASS[Analytical Sentinel Service]
        SeerOp[Seer Operator]
        SX[Signal Exchange]
        HO[Hub Operators]
    end
    
    EnableDisable --> SD
    SuspendControl --> SD
    EmergencyControl --> SD
    EnableDisable --> RTS
    EnableDisable --> ASS
    EnableDisable --> SX
    SuspendControl --> SeerOp
    SuspendControl --> SX
    EmergencyControl --> SeerOp
    EmergencyControl --> HO
```

---

## Functional Scope

### Enable/Disable Control

Sentinel Levers enable or disable sentinels:

#### Enable Action

```yaml
enable_action:
  sentinel_id: "stuck-agent-detector"
  deployment_id: "stuck-agent-detector-deployment"
  action: "enable"
  effect: "Resume sentinel execution"
```

#### Disable Action

```yaml
disable_action:
  sentinel_id: "stuck-agent-detector"
  deployment_id: "stuck-agent-detector-deployment"
  action: "disable"
  effect: "Stop sentinel execution"
```

#### Enable/Disable Flow

```mermaid
sequenceDiagram
    participant User as User
    participant SL as Sentinel Levers
    participant SD as Sentinel Directory
    participant RTS as Realtime Sentinel Service
    participant ASS as Analytical Sentinel Service
    
    User->>SL: Enable/Disable sentinel
    SL->>SD: Update sentinel status
    SD->>SL: Status updated
    SL->>RTS: Enable/Disable (if realtime)
    SL->>ASS: Enable/Disable (if analytical)
    RTS->>RTS: Start/Stop execution
    ASS->>ASS: Start/Stop execution
```

---

### Suspend Control

Sentinel Levers suspend sentinel execution:

#### Suspend Action

```yaml
suspend_action:
  sentinel_id: "stuck-agent-detector"
  deployment_id: "stuck-agent-detector-deployment"
  action: "suspend"
  reason: "Maintenance window"
  effect: "Temporarily stop sentinel execution"
```

#### Resume Action

```yaml
resume_action:
  sentinel_id: "stuck-agent-detector"
  deployment_id: "stuck-agent-detector-deployment"
  action: "resume"
  effect: "Resume sentinel execution"
```

#### Suspend Flow

```mermaid
sequenceDiagram
    participant User as User
    participant SL as Sentinel Levers
    participant SeerOp as Seer Operator
    participant Deployment as Sentinel Deployment
    
    User->>SL: Suspend sentinel
    SL->>SeerOp: Update Deployment CRD
    SeerOp->>Deployment: Scale down to 0 replicas
    Deployment->>Deployment: Sentinel suspended
    User->>SL: Resume sentinel
    SL->>SeerOp: Update Deployment CRD
    SeerOp->>Deployment: Scale up to configured replicas
    Deployment->>Deployment: Sentinel resumed
```

---

### Emergency Control

Sentinel Levers provide emergency controls:

#### Emergency Disable

```yaml
emergency_disable:
  sentinel_id: "stuck-agent-detector"
  deployment_id: "stuck-agent-detector-deployment"
  action: "emergency_disable"
  reason: "False positive rate too high"
  effect: "Immediately stop sentinel execution"
  bypass_checks: true
```

#### Emergency Controls

| Control | Description | Use Case |
|---------|-------------|----------|
| **Emergency Disable** | Immediately disable sentinel | False positives, performance issues |
| **Emergency Suspend** | Immediately suspend sentinel | Critical bug, security issue |
| **Emergency Archive** | Immediately archive sentinel | Deprecated sentinel |

---

### Request Sentinel Controls

Request Sentinels have additional control actions specific to their enrollment-based operation:

#### Request Sentinel States

| State | Description | Enrollment? | Processing Updates? |
|-------|-------------|-------------|---------------------|
| **Active** | Sentinel is fully operational | Yes | Yes |
| **Enrollment Suspended** | Not enrolling in new requests | No | Yes (existing) |
| **Fully Suspended** | Not enrolling, not processing | No | No |
| **Archived** | Permanently disabled | No | No |

#### Enable/Disable Enrollment

```yaml
enrollment_control:
  sentinel_id: "token-usage-governance"
  action: "disable_enrollment"
  effect: "Stop enrolling in new requests, continue processing existing"
```

When enrollment is disabled:
- Sentinel stops enrolling in new requests
- Existing child requests continue to receive updates
- Employed Agent remains active for existing work

#### Request Sentinel Suspend Flow

```mermaid
sequenceDiagram
    participant User as User
    participant SL as Sentinel Levers
    participant SX as Signal Exchange
    participant SD as Sentinel Directory
    participant EA as Employed Agent
    
    User->>SL: Suspend request sentinel
    SL->>SX: Remove from auto-enrollment
    SX->>SX: Stop matching new requests
    SL->>EA: Suspend Employed Agent
    EA->>EA: Stop processing updates
    SL->>SD: Update status to suspended
    SD->>User: Sentinel suspended
```

#### Request Sentinel Archive Flow

```mermaid
sequenceDiagram
    participant User as User
    participant SL as Sentinel Levers
    participant SX as Signal Exchange
    participant HO as Hub Operators
    participant SeerOp as Seer Operator
    participant SD as Sentinel Directory
    
    User->>SL: Archive request sentinel
    SL->>SX: Remove enrollment filters
    SL->>HO: Remove scenario deployment
    HO->>SeerOp: Revoke Employed Agent
    SeerOp->>SeerOp: Terminate agent pod
    SL->>SD: Update status to archived
    SD->>User: Sentinel archived
```

#### Existing Child Requests on Suspend/Archive

| Action | Existing Child Requests |
|--------|------------------------|
| **Disable Enrollment** | Continue processing until parent completes |
| **Suspend** | Stop processing, remain in current state |
| **Archive** | Mark as CANCELLED with reason `SENTINEL_ARCHIVED` |

#### Emergency Control Flow

```mermaid
sequenceDiagram
    participant User as User
    participant SL as Sentinel Levers
    participant SeerOp as Seer Operator
    participant Deployment as Sentinel Deployment
    
    User->>SL: Emergency disable
    SL->>SL: Bypass validation checks
    SL->>SeerOp: Immediately update Deployment CRD
    SeerOp->>Deployment: Force scale down
    Deployment->>Deployment: Sentinel disabled
```

---

### COG Sentinel Controls

COG Sentinels (sentinels defined in COGW workbenches) have a two-level control model:

#### Two-Level Status Model

| Level | Location | Controls | Scope |
|-------|----------|----------|-------|
| **Global** | COGW workbench | Full control | All target workbenches |
| **Local** | Target workbenches | Enable/disable only | Single workbench |

#### Effective Status

```
Effective Status = Global Status AND Local Status

Global: Active + Local: Active = Active (enrolled)
Global: Active + Local: Disabled = Disabled (not enrolled)
Global: Disabled + Local: Active = Disabled (not enrolled)
Global: Disabled + Local: Disabled = Disabled (not enrolled)
```

#### Local Enable/Disable (Target Workbench)

Target workbench admins can enable/disable COG Sentinels locally:

```yaml
cog_sentinel_local_control:
  sentinel_id: "token-governance-sentinel"
  source_workbench: "acme-cogw"
  action: "local_disable"
  workbench: "production-loans"
  reason: "Testing new deployment"
```

| Action | Allowed | Description |
|--------|---------|-------------|
| **local_enable** | ✅ | Enable COG Sentinel in this workbench |
| **local_disable** | ✅ | Disable COG Sentinel in this workbench |
| **modify** | ❌ | Cannot modify read-only specs |
| **delete** | ❌ | Managed by COGW Operator |

#### Global Enable/Disable (COGW)

COGW admins have full control:

```yaml
cog_sentinel_global_control:
  sentinel_id: "token-governance-sentinel"
  action: "global_disable"
  scope: "all_targets"
  reason: "Maintenance window"
```

> See [COG Sentinel Administrative Controls](../../subsystems/cognitive-operations-governance-workbench/administrative-controls.md) for details.

---

## Integration Points

### Upstream Integration

| Service | Integration Method | Purpose |
|---------|-------------------|---------|
| **Sentinel Directory** | Status update API | Update sentinel status |

### Downstream Integration

| Service | Integration Method | Purpose |
|---------|-------------------|---------|
| **Seer Operator** | Deployment CRD updates | Control sentinel deployment |
| **Realtime Sentinel Service** | Enable/disable API | Control realtime sentinel execution |
| **Analytical Sentinel Service** | Enable/disable API | Control analytical sentinel execution |
| **Signal Exchange** | Enrollment filter control | Enable/disable request sentinel enrollment |
| **Hub Operators** | Scenario deployment control | Archive request sentinel scenarios |

---

## Key Design Decisions

### Runtime Controls

- **Levers provide runtime controls** without modifying specs
- **Enable/disable** for normal operational control
- **Suspend/resume** for temporary suspension
- **Emergency controls** for immediate response

### State Management

- **Levers update sentinel state** in Sentinel Directory
- **State transitions** coordinated via Sentinel Operators
- **Deployment state** managed via Seer Operator

### Emergency Response

- **Emergency controls bypass validation** for immediate response
- **Force state transitions** for critical situations
- **Audit trail** for all lever actions

---

## Related Documentation

- [Sentinel Operators](./sentinel-operators.md) — Lifecycle management and state transitions
- [Sentinel Directory](./sentinel-directory.md) — Registry and status tracking
- [Seer Operator](../../hub-integration/training-spec-crd.md) — CRD reconciliation

---

*Sentinel Levers provide runtime controls for sentinels, enabling operational management without spec modifications.*
