# Registry Services

> **Status:** 🔴 Stub — Placeholder for expansion

Registry Services maintain the **catalogs of capabilities, machines, environments, and tools** available within the Hub ecosystem.

---

## Overview

Registries are essential for:
- **Discovery** — What capabilities are available?
- **Governance** — What is authorized for use?
- **Configuration** — How are capabilities configured?
- **Versioning** — Which versions are in use?

---

## Registry Inventory

| Registry | Description | Status |
|----------|-------------|--------|
| [Tool Registry](./tool-registry.md) | Tools available for agent/automation use | 🔴 Stub |
| [Machine Registry](./machine-registry.md) | Machines (systems) in the environment | 🔴 Stub |
| [Environment Registry](./environment-registry.md) | Environments and sandboxes | 🔴 Stub |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                   REGISTRY SERVICES                              │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                 REGISTRY API LAYER                       │    │
│  │        (CRUD, Discovery, Search, Versioning)             │    │
│  └─────────────────────────┬───────────────────────────────┘    │
│                            │                                     │
│  ┌─────────────────────────┼───────────────────────────────┐    │
│  │                 REGISTRIES                               │    │
│  │                                                          │    │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │    │
│  │  │    Tool      │  │   Machine    │  │ Environment  │   │    │
│  │  │   Registry   │  │   Registry   │  │  Registry    │   │    │
│  │  └──────────────┘  └──────────────┘  └──────────────┘   │    │
│  └──────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              STORAGE (System & Tenant Spec)              │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Storage Layers

Registries span two storage layers:

| Layer | Content | Ownership |
|-------|---------|-----------|
| **System Data** | Platform-provided blueprints, commands | Platform |
| **Tenant Spec** | Tenant-specific registrations | Tenant |

---

## Common Registry Patterns

### Registration
- Schema validation
- Version assignment
- Approval workflow (if required)

### Discovery
- List/search by criteria
- Filter by scope (workbench, tenant)
- Permission-aware filtering

### Versioning
- Semantic versioning
- Compatibility declarations
- Deprecation lifecycle

### Access Control
- Who can register?
- Who can discover?
- Who can invoke/use?

---

## Agent Registry (Special Case)

The Agent Registry is managed by **Cipher IAM**, not Hub Registry Services:

| Registry | Owner | Purpose |
|----------|-------|---------|
| **Agent Registry** | Cipher | Raw, Trained, Employed Agent identities |
| **AI Agent Registry** | Seer | AI Agent definitions and configurations |

Hub's role is to integrate with these registries for agent enrollment in Workbenches.

---

## Workbench Integration

Each Workbench can define:
- **Command Registry Subset** — Commands applicable to this workbench
- **Tool Access** — Tools available in this workbench
- **Machine Access** — Machines accessible from this workbench

---

## Related Documentation

- [Hub Architecture](../../02-system-design/hub-architecture.md) — System context
- [Storage Architecture](../../07-data-architecture/storage-architecture.md) — Storage layers
- [Cipher IAM](../supporting-systems/cipher-iam.md) — Agent identity

---

*TODO: Detailed design — registry schemas, versioning strategy, access control model*

