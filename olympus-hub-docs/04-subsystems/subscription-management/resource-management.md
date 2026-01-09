# Resource Management

> **Status:** 🔴 Stub — Placeholder for expansion

Manages the allocation, provisioning, and lifecycle of platform resources for tenants.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Allocate and manage platform resources per tenant |
| **Scope** | Data stores, memory stores, knowledge stores, machines, I/O gateways, notification services |
| **Lifecycle** | Provision → Configure → Monitor → Scale → Deprovision |

---

## Managed Resource Types

| Resource Type | Description | Examples |
|---------------|-------------|----------|
| **Data Stores** | Persistent storage for operations data | PostgreSQL, MongoDB |
| **Memory Stores** | Agent and enterprise memory storage | Vector DB, Redis |
| **Knowledge Stores** | RAG and knowledge bank storage | Vector DB, Elasticsearch |
| **Machines** | External systems and integrations | Core banking, CRM, payment gateways |
| **I/O Gateways** | Signal provider instances | Atropos, Heracles, Cronus, Dia, Kale |
| **Notification Services** | Notification delivery channels | Email (SES), SMS (Twilio), Push |
| **Compute** | Automation system allocations | Container limits, workflow capacity |

---

## Resource Allocation Model

```
┌─────────────────────────────────────────────────────────────────┐
│                    TENANT RESOURCE ALLOCATION                    │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                    SHARED RESOURCES                      │    │
│  │         (Multi-tenant, isolated by tenant ID)            │    │
│  │                                                          │    │
│  │   • Shared database clusters (tenant schemas)            │    │
│  │   • Shared compute pools                                 │    │
│  │   • Shared I/O Gateway infrastructure                    │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                   DEDICATED RESOURCES                    │    │
│  │           (Single-tenant, enterprise tier)               │    │
│  │                                                          │    │
│  │   • Dedicated database instances                         │    │
│  │   • Dedicated compute clusters                           │    │
│  │   • Dedicated network isolation                          │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Resource Lifecycle

```
[Requested] → [Provisioning] → [Active] → [Scaling] → [Deprovisioning] → [Terminated]
```

| State | Description |
|-------|-------------|
| **Requested** | Resource allocation requested |
| **Provisioning** | Resource being created/allocated |
| **Active** | Resource available for use |
| **Scaling** | Resource being scaled up/down |
| **Deprovisioning** | Resource being released |
| **Terminated** | Resource fully released |

---

## Resource Provisioning by Tier

| Resource | Starter | Professional | Enterprise |
|----------|---------|--------------|------------|
| **Data Store** | Shared, 10GB | Shared, 100GB | Dedicated, 1TB+ |
| **Memory Store** | Shared, 1GB | Shared, 10GB | Dedicated, 100GB+ |
| **Knowledge Store** | Shared, 5GB | Shared, 50GB | Dedicated, 500GB+ |
| **I/O Gateways** | 2 | 5 | Unlimited |
| **Machines** | 5 | 20 | Unlimited |
| **Compute (vCPU)** | 2 | 8 | Dedicated pool |

---

## Related Documentation

- [Subscription Management Overview](./README.md)
- [Resource Configuration](./resource-configuration.md)
- [Budget Management](./budget-management.md)

---

*TODO: Detailed design — provisioning automation, scaling policies, resource isolation*

