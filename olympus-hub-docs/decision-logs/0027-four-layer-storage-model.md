# ADR-0027: Four-Layer Storage Model for Hub Data

## Status

**Accepted**

## Date

2026-01-06

## Context

Hub manages diverse data types with different:
- **Ownership**: Platform, Tenant Admin, Hub, Applications
- **Scope**: Platform-wide, tenant-specific, workbench-specific
- **Lifecycle**: Configuration-time vs runtime vs archival
- **Access patterns**: Read-only, read-write, append-only

A clear organizational model is needed to:
- Guide where different data types should be stored
- Enforce appropriate isolation and access control
- Enable proper lifecycle management
- Separate concerns between Hub-managed and application-managed data

## Decision

Hub data is organized into **four layers**, plus a separate **Cognitive Services** category:

### Layer 1: System Data
| Attribute | Value |
|-----------|-------|
| **Scope** | Platform-wide, shared across all tenants |
| **Owner** | Platform Operators (Zeta) |
| **Access** | Read-only for tenants |
| **Examples** | Blueprints, Command Registries, Industry Knowledge Base |

### Layer 2: Tenant Spec / Metadata
| Attribute | Value |
|-----------|-------|
| **Scope** | Tenant-specific configuration and definitions |
| **Owner** | Tenant Administrators |
| **Access** | Read/write for Tenant Admins, read for agents |
| **Examples** | Workbench Definitions, IAM, Triggers, Tenant Knowledge Base |

### Layer 3: Workbench-Scoped Data
Split into two categories:

**3A. Operations Data (Hub-Managed)**
| Attribute | Value |
|-----------|-------|
| **Scope** | Runtime and transactional data |
| **Owner** | Hub |
| **Access** | Hub APIs only (no direct application access) |
| **Examples** | Requests, Tasks, Activities, Signals, Sessions |

**3B. Application Data Stores (Application-Managed)**
| Attribute | Value |
|-----------|-------|
| **Scope** | Business domain entities |
| **Owner** | Hub Applications |
| **Access** | Direct access by applications |
| **Examples** | Ganymede (Relational), Callisto (KV), Europa (Search) |

### Cognitive Services (Hub-Managed with Specific Semantics)
| Attribute | Value |
|-----------|-------|
| **Scope** | What the organization knows and remembers |
| **Owner** | Hub (with specific contracts) |
| **Access** | Through Hub-specified interfaces |
| **Examples** | Memory Services (Enterprise, Agent, User), Knowledge Bank |

```
┌────────────────────────────────────────────────────────────────────────┐
│ LAYER 1: SYSTEM DATA (Platform-wide, Zeta-owned)                        │
├────────────────────────────────────────────────────────────────────────┤
│ LAYER 2: TENANT SPEC / METADATA (Tenant-scoped, Admin-owned)           │
├────────────────────────────────────────────────────────────────────────┤
│ LAYER 3: WORKBENCH-SCOPED DATA                                          │
│   ┌────────────────────────────┐  ┌────────────────────────────────┐   │
│   │ OPERATIONS DATA (Hub)      │  │ APPLICATION DATA (App-Managed) │   │
│   │ Requests, Tasks, Activities│  │ Ganymede, Callisto, Europa     │   │
│   └────────────────────────────┘  └────────────────────────────────┘   │
├────────────────────────────────────────────────────────────────────────┤
│ COGNITIVE SERVICES (Hub-Managed, Specific Semantics)                    │
│   Memory Services (CAF Control Plane) | Knowledge Services              │
└────────────────────────────────────────────────────────────────────────┘
```

## Alternatives Considered

### Alternative 1: Two-Layer Model (Platform vs Tenant)
Simple separation of platform and tenant data.

- **Pros**: Simple, familiar
- **Cons**: Doesn't distinguish workbench-scoped data, mixes operational and application data

### Alternative 2: Functional Grouping
Group by function (identity, workflow, storage, etc.).

- **Pros**: Clear functional boundaries
- **Cons**: Doesn't capture ownership model, scope confusion

### Alternative 3: Single Unified Data Layer
All data in one logical layer with metadata-based separation.

- **Pros**: Simpler model
- **Cons**: Blurs ownership, access control complexity, lifecycle confusion

## Consequences

### Positive
- **Clear Ownership**: Each layer has defined owner
- **Appropriate Isolation**: Tenant isolation enforced at Layer 2+
- **Lifecycle Management**: Each layer has appropriate retention policies
- **Separation of Concerns**: Hub-managed vs application-managed clearly separated
- **Access Control**: Access patterns match ownership model

### Negative
- **Complexity**: Four layers plus cognitive services to understand
- **Learning Curve**: Developers must understand layer model
- **Cross-Layer Queries**: Some use cases may need data from multiple layers

### Neutral
- Cognitive Services are a special category with Hub-specified semantics
- CAF is control plane for Memory Services, not a storage layer

## Related Decisions

- [ADR-0028: Cognitive vs Operational vs Domain Data Classification](./0028-data-classification.md)
- [ADR-0016: Typed Data Store CRDs](./0016-typed-data-store-crds.md)

