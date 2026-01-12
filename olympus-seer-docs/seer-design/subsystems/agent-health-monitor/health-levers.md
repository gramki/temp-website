# Health Levers

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-13  
> **Design Level**: C2 (Container)

---

## Overview

Health Levers provide runtime controls for health monitoring. They enable/disable health monitoring, suspend execution, and provide emergency controls for immediate health monitor management.

**Key Principle**: Health Levers provide operational controls that affect health monitor execution without modifying health specifications.

---

## Architecture

```mermaid
flowchart TB
    subgraph HL[Health Levers]
        EnableDisable[Enable/Disable Control]
        SuspendControl[Suspend Control]
        EmergencyControl[Emergency Control]
    end
    
    subgraph ExternalSystems[External Systems]
        HD[Health Directory]
        SLOT[SLO Tracking Service]
        SeerOp[Seer Operator]
    end
    
    EnableDisable --> HD
    SuspendControl --> HD
    EmergencyControl --> HD
    EnableDisable --> SLOT
    SuspendControl --> SeerOp
    EmergencyControl --> SeerOp
```

---

## Functional Scope

### Enable/Disable Control

Health Levers enable or disable health monitoring:

#### Enable Action

```yaml
enable_action:
  health_spec_id: "fraud-analyst-health"
  deployment_id: "fraud-analyst-health-deployment"
  action: "enable"
  effect: "Resume health monitoring"
```

#### Disable Action

```yaml
disable_action:
  health_spec_id: "fraud-analyst-health"
  deployment_id: "fraud-analyst-health-deployment"
  action: "disable"
  effect: "Stop health monitoring"
```

#### Enable/Disable Flow

```mermaid
sequenceDiagram
    participant User as User
    participant HL as Health Levers
    participant HD as Health Directory
    participant SLOT as SLO Tracking Service
    
    User->>HL: Enable/Disable health monitor
    HL->>HD: Update health monitor status
    HD->>HL: Status updated
    HL->>SLOT: Enable/Disable SLO tracking
    SLOT->>SLOT: Start/Stop evaluation
```

---

### Suspend Control

Health Levers suspend health monitor execution:

#### Suspend Action

```yaml
suspend_action:
  health_spec_id: "fraud-analyst-health"
  deployment_id: "fraud-analyst-health-deployment"
  action: "suspend"
  reason: "Maintenance window"
  effect: "Temporarily stop health monitoring"
```

#### Resume Action

```yaml
resume_action:
  health_spec_id: "fraud-analyst-health"
  deployment_id: "fraud-analyst-health-deployment"
  action: "resume"
  effect: "Resume health monitoring"
```

#### Suspend Flow

```mermaid
sequenceDiagram
    participant User as User
    participant HL as Health Levers
    participant SeerOp as Seer Operator
    participant Deployment as Health Deployment
    
    User->>HL: Suspend health monitor
    HL->>SeerOp: Update Deployment CRD
    SeerOp->>Deployment: Scale down to 0 replicas
    Deployment->>Deployment: Health monitor suspended
    User->>HL: Resume health monitor
    HL->>SeerOp: Update Deployment CRD
    SeerOp->>Deployment: Scale up to configured replicas
    Deployment->>Deployment: Health monitor resumed
```

---

### Emergency Control

Health Levers provide emergency controls:

#### Emergency Disable

```yaml
emergency_disable:
  health_spec_id: "fraud-analyst-health"
  deployment_id: "fraud-analyst-health-deployment"
  action: "emergency_disable"
  reason: "False positive rate too high"
  effect: "Immediately stop health monitoring"
  bypass_checks: true
```

#### Emergency Controls

| Control | Description | Use Case |
|---------|-------------|----------|
| **Emergency Disable** | Immediately disable health monitor | False positives, performance issues |
| **Emergency Suspend** | Immediately suspend health monitor | Critical bug, security issue |
| **Emergency Archive** | Immediately archive health monitor | Deprecated health monitor |

#### Emergency Control Flow

```mermaid
sequenceDiagram
    participant User as User
    participant HL as Health Levers
    participant SeerOp as Seer Operator
    participant Deployment as Health Deployment
    
    User->>HL: Emergency disable
    HL->>HL: Bypass validation checks
    HL->>SeerOp: Immediately update Deployment CRD
    SeerOp->>Deployment: Force scale down
    Deployment->>Deployment: Health monitor disabled
```

---

## Integration Points

### Upstream Integration

| Service | Integration Method | Purpose |
|---------|-------------------|---------|
| **Health Directory** | Status update API | Update health monitor status |

### Downstream Integration

| Service | Integration Method | Purpose |
|---------|-------------------|---------|
| **Seer Operator** | Deployment CRD updates | Control health monitor deployment |
| **SLO Tracking Service** | Enable/disable API | Control SLO tracking execution |

---

## Key Design Decisions

### Runtime Controls

- **Levers provide runtime controls** without modifying specs
- **Enable/disable** for normal operational control
- **Suspend/resume** for temporary suspension
- **Emergency controls** for immediate response

### State Management

- **Levers update health monitor state** in Health Directory
- **State transitions** coordinated via Health Operators
- **Deployment state** managed via Seer Operator

### Emergency Response

- **Emergency controls bypass validation** for immediate response
- **Force state transitions** for critical situations
- **Audit trail** for all lever actions

---

## Related Documentation

- [Health Operators](./health-operators.md) — Lifecycle management and state transitions
- [Health Directory](./health-directory.md) — Registry and status tracking
- [Seer Operator](../../hub-integration/training-spec-crd.md) — CRD reconciliation

---

*Health Levers provide runtime controls for health monitoring, enabling operational management without spec modifications.*
