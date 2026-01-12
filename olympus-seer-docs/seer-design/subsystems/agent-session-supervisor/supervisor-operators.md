# Supervisor Operators

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-13  
> **Design Level**: C2 (Container)

---

## Overview

Supervisor Operators manage the lifecycle of Supervisor Specs and Deployments via Seer Operator. They handle registration, validation, versioning, and state transitions for supervisors.

**Key Principle**: Supervisor Operators coordinate lifecycle management across Supervisor Spec Manager, Supervisor Directory, and Seer Operator, following the same pattern as Trained/Employed Agent lifecycle managers.

---

## Architecture

```mermaid
flowchart TB
    subgraph SO[Supervisor Operators]
        RegistrationService[Registration Service]
        ValidationOrchestration[Validation Orchestration]
        VersionManagement[Version Management]
        StateTransitionService[State Transition Service]
    end
    
    subgraph ExternalSystems[External Systems]
        SSM[Supervisor Spec Manager]
        SD[Supervisor Directory]
        SeerOp[Seer Operator]
        RTS[Realtime Supervisor Service]
        ASS[Analytical Supervisor Service]
    end
    
    RegistrationService --> SSM
    ValidationOrchestration --> SSM
    ValidationOrchestration --> SeerOp
    VersionManagement --> SD
    StateTransitionService --> SeerOp
    StateTransitionService --> SD
```

---

## Functional Scope

### Registration Service

Supervisor Operators register new Supervisor Specs:

#### Registration Flow

```mermaid
sequenceDiagram
    participant User as User
    participant SO as Supervisor Operators
    participant SSM as Supervisor Spec Manager
    participant SeerOp as Seer Operator
    participant SD as Supervisor Directory
    
    User->>SO: Create SupervisorSpec
    SO->>SSM: Validate spec structure
    SSM->>SO: Validation result
    SO->>SeerOp: Create SupervisorSpec CRD
    SeerOp->>SeerOp: Register CRD
    SO->>SD: Register in directory
    SD->>SO: Registration complete
    SO->>User: Registration success
```

#### Registration Steps

1. **Spec Validation**: Validate spec structure via Supervisor Spec Manager
2. **CRD Creation**: Create SupervisorSpec CRD via Seer Operator
3. **Directory Registration**: Register spec in Supervisor Directory
4. **State Initialization**: Initialize spec state (Drafted)

---

### Validation Orchestration

Supervisor Operators orchestrate validation across systems:

#### Validation Checks

| Check | Description | Validated By |
|-------|-------------|--------------|
| **Structure Validation** | Spec structure, required fields | Supervisor Spec Manager |
| **Policy Syntax Validation** | OPA policy syntax (Realtime) or SQL syntax (Analytical) | Supervisor Spec Manager |
| **Target Scope Validation** | Target agents/workbenches exist | Supervisor Spec Manager |
| **Deployment Config Validation** | Deployment configuration valid | Supervisor Spec Manager |

#### Validation Flow

```mermaid
sequenceDiagram
    participant SO as Supervisor Operators
    participant SSM as Supervisor Spec Manager
    participant SeerOp as Seer Operator
    
    SO->>SSM: Validate spec
    SSM->>SSM: Structure validation
    SSM->>SSM: Policy syntax validation
    SSM->>SSM: Target scope validation
    SSM->>SSM: Deployment config validation
    SSM->>SO: Validation result
    SO->>SeerOp: Update CRD status
```

---

### Version Management

Supervisor Operators manage supervisor versions:

#### Version Assignment

| State | Version Rule |
|-------|-------------|
| **Drafted** | No version assigned |
| **Validated** | Version assigned (e.g., `1.0.0`) |
| **Deployed** | Version locked |

#### Version Compatibility

- **Major version**: Breaking changes (incompatible policies)
- **Minor version**: New features (backward compatible)
- **Patch version**: Bug fixes (backward compatible)

---

### State Transition Service

Supervisor Operators manage supervisor state transitions:

#### Lifecycle States

| State | Description | Allowed Transitions |
|-------|-------------|-------------------|
| **Drafted** | Spec created, not validated | → Validated |
| **Validated** | Spec validated, ready for deployment | → Deployed, → Archived |
| **Deployed** | Supervisor deployed and active | → Suspended, → Archived |
| **Suspended** | Supervisor suspended (temporarily disabled) | → Deployed, → Archived |
| **Archived** | Supervisor archived (no longer active) | (terminal) |

#### State Transition Flow

```mermaid
stateDiagram-v2
    [*] --> Drafted
    Drafted --> Validated: Validate
    Validated --> Deployed: Deploy
    Validated --> Archived: Archive
    Deployed --> Suspended: Suspend
    Deployed --> Archived: Archive
    Suspended --> Deployed: Resume
    Suspended --> Archived: Archive
    Archived --> [*]
```

#### State Transition Rules

| Transition | Condition | Action |
|-----------|-----------|--------|
| **Drafted → Validated** | Spec validation passes | Assign version, update CRD status |
| **Validated → Deployed** | Deployment CRD created | Deploy supervisor service |
| **Deployed → Suspended** | Suspend lever activated | Stop supervisor service |
| **Suspended → Deployed** | Resume lever activated | Restart supervisor service |
| **Any → Archived** | Archive lever activated | Remove supervisor service, mark archived |

---

## Integration Points

### Upstream Integration

| Service | Integration Method | Purpose |
|---------|-------------------|---------|
| **Supervisor Spec Manager** | Spec validation API | Validate specs before registration |
| **Seer Operator** | CRD reconciliation | CRD creation and state management |

### Downstream Integration

| Service | Integration Method | Purpose |
|---------|-------------------|---------|
| **Supervisor Directory** | Spec registration API | Register specs in directory |
| **Realtime Supervisor Service** | Deployment trigger | Deploy realtime supervisors |
| **Analytical Supervisor Service** | Deployment trigger | Deploy analytical supervisors |

---

## Key Design Decisions

### Lifecycle Pattern

- **Follows same pattern** as Trained/Employed Agent lifecycle managers
- **State-based lifecycle** with clear transition rules
- **Version management** for spec evolution

### Seer Operator Boundary

- **Supervisor Operators coordinate** lifecycle management
- **Seer Operator reconciles** CRDs to Kubernetes state
- **Clear separation** between business logic and controller logic

### Deployment Model

- **Deployment CRDs** reference SupervisorSpec CRDs
- **Deployment triggers** supervisor service deployment
- **State transitions** control supervisor lifecycle

---

## Related Documentation

- [Supervisor Spec Manager](./supervisor-spec-manager.md) — Spec structure and validation
- [Supervisor Levers](./supervisor-levers.md) — Runtime controls and state transitions
- [Supervisor Directory](./supervisor-directory.md) — Registry and search
- [Seer Operator](../../hub-integration/training-spec-crd.md) — CRD reconciliation

---

*Supervisor Operators manage the lifecycle of Supervisor Specs and Deployments via Seer Operator.*
