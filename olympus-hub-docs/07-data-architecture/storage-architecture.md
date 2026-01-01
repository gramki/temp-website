# Storage Architecture

Hub data is organized into **three layers**, each with distinct scope, lifecycle, and access patterns. All Hub subsystems are required to model and maintain data across these three layers.

## Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    STORAGE LAYERS                                │
│                                                                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │ LAYER 1: SYSTEM DATA                                       │  │
│  │ Scope: Platform-wide, shared across all tenants            │  │
│  │ Examples: Blueprints, Command Registries, Industry KB      │  │
│  └───────────────────────────────────────────────────────────┘  │
│                              │                                   │
│                              ▼                                   │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │ LAYER 2: TENANT SPEC / METADATA                            │  │
│  │ Scope: Tenant-specific configuration and definitions       │  │
│  │ Examples: Workbench Definitions, IAM, Triggers, Tenant KB  │  │
│  └───────────────────────────────────────────────────────────┘  │
│                              │                                   │
│                              ▼                                   │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │ LAYER 3: OPERATIONS DATA                                   │  │
│  │ Scope: Runtime/transactional data for active operations   │  │
│  │ Examples: Signals, Requests, Activities, Tasks, Actions   │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │ AUDIT STORE (Partitioned by Layer)                         │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Layer 1: System Data

**Scope:** Platform-wide data shared across all tenants. Managed by Hub platform operators.

**Characteristics:**
- Read-only for tenants (consume, not modify)
- Versioned with controlled release cycles
- High availability, low change frequency

### Data Categories

| Category | Description | Examples |
|----------|-------------|----------|
| **Workbench Blueprints** | Reusable templates/patterns that tenants can instantiate | Dispute Resolution Blueprint, KYC Blueprint, Reconciliation Blueprint |
| **Command Registries** | Catalog of Commands/Actuators available platform-wide | Payment Commands, Account Commands, Notification Commands |
| **Domain/Industry Knowledge Base** | Pre-built knowledge for specific industries | Banking regulations, Insurance claim patterns, Healthcare compliance |
| **I/O Gateway Discovery** | Available I/O Gateways and their capabilities | Atropos endpoints, Heracles routes, Dia storage locations |
| **Ontology Definitions** | Core ontology concepts and relationships | Signal types, Request types, Operation patterns |

### Access Patterns

| Actor | Access |
|-------|--------|
| Platform Operators | Read/Write |
| Tenant Admins | Read (reference in Tenant Spec) |
| Agents | Read (runtime reference) |

---

## Layer 2: Tenant Spec / Metadata

**Scope:** Tenant-specific configuration and definitions. Managed by tenant administrators.

**Characteristics:**
- Tenant-isolated (strict multi-tenancy)
- Versioned with migration support
- Configuration-time data (not runtime)

### Data Categories

| Category | Description | Examples |
|----------|-------------|----------|
| **Workbench Definitions** | Instantiated workbenches with tenant-specific configuration | Tenant's Dispute Workbench, Tenant's KYC Workbench |
| **Machines** | Registered machines in the tenant's environment | Core Banking System, Payment Gateway, CRM |
| **Environments** | Sandboxes and deployment contexts | Production, Staging, UAT |
| **IAM Configuration** | Identity and access management settings | Roles, Groups, Permissions, Agent enrollments |
| **User Management** | Tenant's human users and their assignments | Operators, Analysts, Supervisors |
| **I/O Gateway Configuration** | Tenant-specific gateway configurations | API routes, Event subscriptions, File endpoints |
| **Triggers** | Signal-to-Request binding definitions | Event triggers, Exception triggers, Scheduled triggers |
| **Tenant Knowledge Base** | Tenant-specific knowledge and policies | Product policies, SOPs, Business rules, Compliance requirements |
| **Notification Templates** | Message templates for subject communication | Email templates, SMS templates, Push notification templates |
| **Request Definitions** | Domain-specific request type specifications | Dispute Filing Request schema, Account Closure Request schema |

### Versioning

Tenant Spec data is versioned to support:
- **Change tracking** — Who changed what and when
- **Rollback** — Revert to previous configuration
- **Migration** — Controlled transition between versions (e.g., Workbench Definition v1 → v2)

### Access Patterns

| Actor | Access |
|-------|--------|
| Tenant Admins | Read/Write (via Workbench Studio, Control Center) |
| Agents | Read (runtime reference) |
| Platform Operators | Read (support/debugging) |

---

## Layer 3: Operations Data

**Scope:** Runtime and transactional data for active and completed operations. Generated during operation execution.

**Characteristics:**
- High volume, high velocity
- Tenant-isolated
- Lifecycle-managed (active → completed → archived)

### Data Categories

| Category | Description | Examples |
|----------|-------------|----------|
| **Signals** | Incoming signals from I/O Gateways | Events, Exceptions, Observations, HTTP-Requests, Batch-Requests |
| **Requests** | Standardized requests created from signals | Service Requests, Business Requests, System Requests |
| **Operations** | Running and completed operation instances | Procedures, Workflows, Cases |
| **Activities** | Observable steps within operations | "Verify Identity", "Review Transaction", "Approve Refund" |
| **Tasks** | Agent-assigned work items | Pending tasks, Completed tasks, Reassigned tasks |
| **Actions** | Atomic execution steps | Command invocations, Decisions, Data operations |
| **Agent Sessions** | Agent interaction sessions | Human sessions, AI agent sessions, MCP sessions |
| **Notifications** | Sent notifications and delivery status | Email sent, SMS delivered, Push failed |

### Retention Policies

| State | Storage Tier | Retention | Access Pattern |
|-------|--------------|-----------|----------------|
| **Active** | Hot storage | Until completion | Frequent read/write |
| **Completed** | Warm storage | Configurable (e.g., 90 days) | Occasional read |
| **Archived** | Cold storage | Configurable (e.g., 7 years) | Rare read (compliance) |

Retention policies are configurable per tenant and may vary by data category (e.g., financial operations retained longer than routine requests).

### Access Patterns

| Actor | Access |
|-------|--------|
| Agents | Read/Write (within assigned operations) |
| Supervisors | Read (monitoring, reporting) |
| Tenant Admins | Read (analytics, compliance) |
| Platform Operators | Read (support/debugging, with tenant consent) |

---

## Audit Store

All three layers share a **unified audit store**, partitioned by layer. The audit store captures:

| Audit Type | Description |
|------------|-------------|
| **Change Audit** | Who changed what, when, and the before/after state |
| **Access Audit** | Who accessed what data and when |
| **Action Audit** | What actions were taken in operations |

### Partitioning

| Partition | Scope |
|-----------|-------|
| `audit:system` | Changes to System Data (platform operators) |
| `audit:tenant:{tenant_id}:spec` | Changes to Tenant Spec (tenant admins) |
| `audit:tenant:{tenant_id}:ops` | Operations activity (agents, supervisors) |

### Retention

Audit data has its own retention policy, typically longer than operational data for compliance purposes.

---

## Subsystem Conformance

All Hub subsystems are expected to:

| Expectation | Description |
|-------------|-------------|
| **Layer Separation** | Clearly distinguish System, Tenant Spec, and Operations data in their data models |
| **Tenant Isolation** | Enforce strict tenant isolation for Layer 2 and Layer 3 data |
| **Versioning** | Support versioning for Layer 2 (Tenant Spec) data |
| **Retention** | Implement configurable retention policies for Layer 3 (Operations) data |
| **Audit Integration** | Emit audit events to the unified audit store, tagged by layer |
| **Schema Evolution** | Support backward-compatible schema changes |

### Data Model Documentation

Each subsystem should document:
- What data it stores at each layer
- Data schemas and relationships
- Access control requirements
- Retention and archival policies

---

## Related Documentation

- [Hub Architecture](../02-system-design/hub-architecture.md) — System context
- [Cipher IAM](../04-subsystems/supporting-systems/cipher-iam.md) — Identity and access management
- [Ontology Reference](../01-concepts/ontology-reference.md) — Core concepts

---

*Status: 🟡 WIP - 10K feet view established. To be enriched with specific data models, technology choices, and subsystem conformance details.*

