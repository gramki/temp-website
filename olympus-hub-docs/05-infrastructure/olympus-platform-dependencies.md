# Olympus Platform Dependencies

> **Status:** 🟡 WIP — Reference document for Hub's platform dependencies

## Overview

Olympus Hub is built on the **Olympus Platform** — Zeta's comprehensive compute and operations platform. Rather than directly consuming infrastructure primitives (Kubernetes, Kafka, PostgreSQL, etc.), Hub leverages Olympus Platform services that abstract and manage these infrastructure concerns.

This document catalogs all Olympus Platform services that Hub depends upon.

---

## Platform Services Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                         OLYMPUS HUB                                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│    ┌──────────────────────────────────────────────────────────┐     │
│    │               Olympus Platform Services                   │     │
│    │                                                           │     │
│    │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐        │     │
│    │  │Atlantis │ │ Atropos │ │Ganymede │ │Callisto │        │     │
│    │  │(Compute)│ │ (Events)│ │ (RDBMS) │ │  (KV)   │        │     │
│    │  └─────────┘ └─────────┘ └─────────┘ └─────────┘        │     │
│    │                                                           │     │
│    │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐        │     │
│    │  │  Dia    │ │ Europa  │ │ Cipher  │ │  Watch  │        │     │
│    │  │ (Files) │ │ (Search)│ │  (IAM)  │ │  (APM)  │        │     │
│    │  └─────────┘ └─────────┘ └─────────┘ └─────────┘        │     │
│    │                                                           │     │
│    │  ┌─────────┐ ┌─────────┐ ┌─────────┐                    │     │
│    │  │Heracles │ │ Elenchos│ │  Velos  │                    │     │
│    │  │(Traffic)│ │(Tenancy)│ │ (Zones) │                    │     │
│    │  └─────────┘ └─────────┘ └─────────┘                    │     │
│    └──────────────────────────────────────────────────────────┘     │
│                              │                                       │
│    ┌─────────────────────────┴─────────────────────────────────┐    │
│    │              Infrastructure (Abstracted)                   │    │
│    │   Kubernetes │ Kafka │ PostgreSQL │ Redis │ OpenSearch    │    │
│    └────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Core Platform Dependencies

### Compute & Runtimes

| Service | Purpose | Hub Usage |
|---------|---------|-----------|
| **[Atlantis](https://atlantis.olympus.tech/)** | Compute infrastructure as a service | Hosts all Hub services and Hub Applications. Abstracts Kubernetes, Knative, and Istio. |
| **[Perseus](https://perseus.olympus.tech/)** | Record processing runtime as a service | Batch processing runtime for Hub Applications |

### Traffic & Networking

| Service | Purpose | Hub Usage |
|---------|---------|-----------|
| **[Heracles](https://heracles.olympus.tech/)** | Traffic management as a service | API Gateway, MCP Gateway for Hub |

### Integration & Messaging

| Service | Purpose | Hub Usage |
|---------|---------|-----------|
| **[Atropos](https://atropos.olympus.tech/)** | Event bus as a service | Signal delivery, async messaging. Abstracts Kafka. |

### Data Stores

| Service | Purpose | Hub Usage |
|---------|---------|-----------|
| **[Ganymede](https://jupiter.olympus.tech/ganymede/)** | Relational DBaaS | Hub operational data, tenant workbench data, Hub Application data |
| **[Callisto](https://jupiter.olympus.tech/callisto/)** | Collections (Key-Value) as a service | Session state, entity caching |
| **[Europa](./europa-opensearch.md)** | Document store / Search as a service | Full-text search, analytics |
| **[Dia](https://dia.olympus.tech/)** | Object and file store as a service | File I/O Gateway for Hub |

### Security & Identity

| Service | Purpose | Hub Usage |
|---------|---------|-----------|
| **[Cipher](https://cipher.olympus.tech/)** | Identity and access management as a service | User authentication, service identity (SPIFFE/SPIRE), authorization |

### Observability

| Service | Purpose | Hub Usage |
|---------|---------|-----------|
| **[Watch](https://watch.olympus.tech/)** | Observability as a service | Logs, metrics, traces, APM for all Hub services |

### Zone & Tenant Management

| Service | Purpose | Hub Usage |
|---------|---------|-----------|
| **[Velos](https://velos.olympus.tech/)** | Zone provisioning as a service | Hub deployment infrastructure |
| **[Weave](https://weave.olympus.tech/)** | Continuous delivery as a service | Hub CI/CD pipelines |
| **[Elenchos](https://elenchos.olympus.tech/)** | Tenant lifecycle management as a service | Tenant onboarding, subscription management |

---

## Abstraction Layers

### What Atlantis Abstracts

Hub does **not** directly interact with:
- Kubernetes clusters, namespaces, or pods
- Istio service mesh configuration
- Knative serverless resources
- Container networking

Instead, Hub uses **Atlantis APIs** for:
- Service deployment and scaling
- Resource allocation
- Health management
- Traffic policies

### What Atropos Abstracts

Hub does **not** directly interact with:
- Kafka brokers, topics, or consumers
- Message serialization formats
- Partition management

Instead, Hub uses **Atropos APIs** for:
- Topic creation and management
- Event publishing and subscription
- Scheduling and delivery guarantees

### What Ganymede Abstracts

Hub does **not** directly interact with:
- PostgreSQL instances or connections
- Database schemas or migrations (directly)
- Connection pooling

Instead, Hub uses **Ganymede APIs** for:
- Database provisioning
- DDL lifecycle management
- REST-based data access
- Backup and recovery

---

## Hub Internal Usage vs Application Usage

| Service | Hub Internal | Hub Applications |
|---------|--------------|------------------|
| **Atlantis** | ✅ Hosts Hub services | ✅ Hosts applications |
| **Atropos** | ✅ Signal Exchange messaging | ⚠️ Via Hub APIs only |
| **Ganymede** | ✅ Operational data | ✅ Application data stores |
| **Callisto** | ✅ Session/cache | ✅ Application state |
| **Europa** | ⚠️ Log aggregation via Watch | ✅ Application search |
| **Dia** | ✅ File I/O Gateway | ⚠️ Optional file storage |
| **Cipher** | ✅ All authentication | ✅ Application auth |
| **Watch** | ✅ Hub observability | ✅ Application APM |

---

## Related Documentation

- [Heracles Gateway](./heracles-gateway.md) — Hub's MCP gateway
- [MCP Orchestrator](./mcp-orchestrator.md) — Tool orchestration
- [Ganymede RDBMS](./ganymede-rdbms.md) — Database service details
- [Callisto KV Store](./callisto-kv-store.md) — Key-value store details
- [Europa OpenSearch](./europa-opensearch.md) — Search service details
- [Olympus Watch](./olympus-watch.md) — Observability platform
- [Cipher IAM Infrastructure](./cipher-iam-infrastructure.md) — Identity infrastructure

---

## External References

- [Olympus Academy](https://academy.olympus.tech/) — Complete platform documentation
- [Olympus Architecture](https://architecture.olympus.tech/) — Platform architecture

---

*This document should be kept in sync with platform service updates.*

