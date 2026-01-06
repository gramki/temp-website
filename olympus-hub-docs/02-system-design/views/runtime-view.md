# Runtime View

> **What runs where**

---

## Audience

- Developers
- Operators
- Platform Engineers

---

## Overview

This view shows what components run in the Olympus Hub platform, where they execute, and how they're hosted. It covers the execution model for Hub Applications, platform services, and supporting infrastructure.

---

## Runtime Topology

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         RUNTIME TOPOLOGY                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   PLATFORM SERVICES                  TENANT WORKLOADS                        │
│   (Shared, managed by SRE)           (Per-workbench, tenant-owned)           │
│                                                                              │
│   ┌─────────────────────────┐       ┌─────────────────────────────────────┐ │
│   │ Signal Exchange         │       │ Hub Applications (Atlantis)         │ │
│   │ Notification Services   │       │   • Container applications          │ │
│   │ Task Management         │       │   • Decision applications           │ │
│   │ Registry Services       │       │   • Prediction applications         │ │
│   └─────────────────────────┘       └─────────────────────────────────────┘ │
│                                                                              │
│   ┌─────────────────────────┐       ┌─────────────────────────────────────┐ │
│   │ I/O Gateways            │       │ Hub Applications (Rhea)             │ │
│   │   Heracles, Atropos,    │       │   • BPMN Workflows                  │ │
│   │   Cronus, Dia, Kale     │       │   • Deterministic processes         │ │
│   └─────────────────────────┘       └─────────────────────────────────────┘ │
│                                                                              │
│   ┌─────────────────────────┐       ┌─────────────────────────────────────┐ │
│   │ Operators               │       │ Hub Applications (ChronoShift)      │ │
│   │   SRE, Win, Resource,   │       │   • Long-running cases              │ │
│   │   Workbench, Scenario   │       │   • Durable workflows               │ │
│   └─────────────────────────┘       └─────────────────────────────────────┘ │
│                                                                              │
│   ┌─────────────────────────┐       ┌─────────────────────────────────────┐ │
│   │ Data Services           │       │ Hub Applications (Seer)             │ │
│   │   Cipher, Memory,       │       │   • AI Agent cases                  │ │
│   │   Knowledge, CAF        │       │   • LLM-based reasoning             │ │
│   └─────────────────────────┘       └─────────────────────────────────────┘ │
│                                                                              │
│   ┌─────────────────────────┐       ┌─────────────────────────────────────┐ │
│   │ Web Applications        │       │ Hub Applications (Perseus)          │ │
│   │   Angelos Consoles      │       │   • Batch processing                │ │
│   │   MS Teams Bots         │       │   • File applications               │ │
│   └─────────────────────────┘       └─────────────────────────────────────┘ │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Automation Runtimes

### Atlantis (Container Runtime)

| Aspect | Detail |
|--------|--------|
| **Technology** | Knative Serving |
| **Use Cases** | Procedures, Decision Apps, Prediction Apps, Custom Services |
| **Scaling** | Scale-to-zero, auto-scale on demand |
| **State** | Stateless; use data stores for persistence |

### Rhea (Workflow Engine)

| Aspect | Detail |
|--------|--------|
| **Technology** | BPMN 2.0 Engine |
| **Use Cases** | Deterministic workflows, multi-step processes |
| **Scaling** | Engine-managed |
| **State** | Workflow instance state persisted |

### ChronoShift (Durable Workflow)

| Aspect | Detail |
|--------|--------|
| **Technology** | Temporal.io |
| **Use Cases** | Long-running cases, complex orchestration |
| **Scaling** | Worker-based scaling |
| **State** | Event-sourced, durable |

### Seer (AI Agent Runtime)

| Aspect | Detail |
|--------|--------|
| **Technology** | LLM orchestration platform |
| **Use Cases** | AI-driven case handling, reasoning tasks |
| **Scaling** | LLM request-based |
| **State** | Memory services for context |

### Perseus (Batch Processing)

| Aspect | Detail |
|--------|--------|
| **Technology** | Batch job executor |
| **Use Cases** | File processing, ETL, map-reduce |
| **Scaling** | Job-based |
| **State** | Job state tracked |

---

## Execution Contexts

### Hub Application Container

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  HUB APPLICATION CONTAINER                                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   INJECTED BY RUNTIME              APPLICATION CODE                          │
│   ──────────────────               ────────────────                          │
│                                                                              │
│   ┌─────────────────────┐         ┌─────────────────────────────────────┐   │
│   │ Environment         │         │ Business Logic                       │   │
│   │   • LOG_LEVEL       │         │                                     │   │
│   │   • SERVICE_URL     │         │   • Request handling                │   │
│   │   • CONFIG_PATH     │         │   • Tool invocation                 │   │
│   └─────────────────────┘         │   • Task delegation                 │   │
│                                   │   • Decision making                 │   │
│   ┌─────────────────────┐         │                                     │   │
│   │ Secrets (mounted)   │         └─────────────────────────────────────┘   │
│   │   • API_KEY         │                                                   │
│   │   • DB_PASSWORD     │                                                   │
│   └─────────────────────┘                                                   │
│                                                                              │
│   ┌─────────────────────┐                                                   │
│   │ Service Discovery   │                                                   │
│   │   • SX endpoint     │                                                   │
│   │   • Registry URLs   │                                                   │
│   └─────────────────────┘                                                   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Resource Allocation

| Resource | Platform Services | Tenant Workloads |
|----------|-------------------|------------------|
| **CPU** | Reserved capacity | Per-application limits |
| **Memory** | Reserved capacity | Per-application limits |
| **Storage** | Managed storage | Per-workbench quotas |
| **Network** | Platform network | Tenant-isolated |

---

## Delivery Interfaces

Hub Applications receive work through configured delivery interfaces:

| Interface | Protocol | Use Case |
|-----------|----------|----------|
| **HTTP** | REST/JSON | Request/response, sync |
| **Atropos** | Kafka/Event | Event-driven, async |
| **OMS** | Outbound messaging | Push notifications |

---

## Related Documentation

- [Hub Application](../implementation-concepts/hub-application.md)
- [Automation Runtime](../implementation-concepts/automation-runtime.md)
- [Subsystem Map](../subsystem-map.md)

