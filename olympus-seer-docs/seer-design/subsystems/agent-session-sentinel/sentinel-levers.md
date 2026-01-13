# Sentinel Levers

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-13  
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
    end
    
    EnableDisable --> SD
    SuspendControl --> SD
    EmergencyControl --> SD
    EnableDisable --> RTS
    EnableDisable --> ASS
    SuspendControl --> SeerOp
    EmergencyControl --> SeerOp
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
