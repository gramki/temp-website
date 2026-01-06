# Data Flow View

> **How data moves through the system**

---

## Audience

- Data Engineers
- Integration Architects
- Solution Architects

---

## Overview

This view traces how data flows through Olympus Hub — from external signals entering the system to outcomes being delivered back. It shows transformation points, storage locations, and data formats at each stage.

---

## End-to-End Data Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         DATA FLOW OVERVIEW                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   INBOUND                    PROCESSING                    OUTBOUND          │
│   ───────                    ──────────                    ───────           │
│                                                                              │
│   Protocol      Normalized     Request      Task      Response    Protocol   │
│   Specific  ──▶  Signal   ──▶  Entity  ──▶ Entity ──▶  Data   ──▶ Specific  │
│   Format         DTO           + Updates   + Memos              Format       │
│                                                                              │
│   HTTP JSON      Standard      Ganymede    Ganymede   JSON/XML   HTTP JSON  │
│   Kafka Avro     Envelope      Storage     Storage    Rendered   Kafka Avro │
│   File CSV                                            Template   File CSV   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Data Transformation Points

### 1. Gateway Normalization

| Stage | Input | Output | Location |
|-------|-------|--------|----------|
| **HTTP** | REST/JSON | Normalized Signal DTO | Heracles Gateway |
| **Events** | Kafka/Avro | Normalized Signal DTO | Atropos Gateway |
| **Files** | CSV/Excel | Normalized Signal DTO | Dia Gateway |
| **Exceptions** | API/JSON | Normalized Signal DTO | Cronus Gateway |

**Normalized Signal DTO Format:**

```json
{
  "signal_header": {
    "tenant_id": "acme-bank",
    "subscription_id": "sub-prod-001",
    "signal_id": "sig-12345",
    "signal_type": "dispute.filed",
    "timestamp": "2026-01-06T10:00:00Z"
  },
  "payload": {
    "content_type": "application/json",
    "data": { /* business data */ }
  },
  "metadata": {
    "source_system": "customer-portal",
    "trace_id": "trace-abc123"
  }
}
```

### 2. Signal Exchange Processing

| Stage | Data Transformation |
|-------|---------------------|
| **Trigger Evaluation** | Signal matched against trigger patterns |
| **Request Creation** | Normalized signal → Request entity with initial update |
| **Correlation** | Matching signals attached to existing requests |
| **Routing** | Request wrapped in Message Envelope for delivery |

### 3. Application Processing

| Stage | Data Transformation |
|-------|---------------------|
| **Context Assembly** | Request + history + knowledge → processing context |
| **Business Logic** | Context → decisions, memos, task definitions |
| **Task Creation** | Decisions → structured task assignments |
| **Update Generation** | Outcomes → Request Updates |

---

## Storage Locations

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         DATA STORAGE MAP                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   TRANSACTIONAL (Workbench-scoped)           SEMANTIC (Workbench-scoped)    │
│   ────────────────────────────────           ───────────────────────────    │
│                                                                              │
│   ┌─────────────────────┐                   ┌─────────────────────────────┐ │
│   │ GANYMEDE (SQL)      │                   │ KNOWLEDGE BANK               │ │
│   │                     │                   │                              │ │
│   │ • Requests          │                   │ • SOPs, Runbooks            │ │
│   │ • Tasks             │                   │ • Decision criteria          │ │
│   │ • Business entities │                   │ • Reference documents        │ │
│   │ • Audit records     │                   │                              │ │
│   └─────────────────────┘                   └─────────────────────────────┘ │
│                                                                              │
│   ┌─────────────────────┐                   ┌─────────────────────────────┐ │
│   │ CALLISTO (KV)       │                   │ MEMORY SERVICES              │ │
│   │                     │                   │                              │ │
│   │ • Session state     │                   │ • Agent memory               │ │
│   │ • Caches            │                   │ • Enterprise memory          │ │
│   │ • Counters          │                   │ • User context               │ │
│   └─────────────────────┘                   └─────────────────────────────┘ │
│                                                                              │
│   ┌─────────────────────┐                   ┌─────────────────────────────┐ │
│   │ EUROPA (Search)     │                   │ COGNITIVE AUDIT FABRIC       │ │
│   │                     │                   │                              │ │
│   │ • Request search    │                   │ • Decision records           │ │
│   │ • Entity search     │                   │ • Evidence bundles           │ │
│   │ • Analytics         │                   │ • Explanations               │ │
│   └─────────────────────┘                   └─────────────────────────────┘ │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Data Formats

| Data Type | Format | Schema |
|-----------|--------|--------|
| **Signals** | JSON | Normalized Signal DTO |
| **Requests** | JSON | Request Entity |
| **Request Updates** | JSON | Append-only update records |
| **Tasks** | JSON | Task Entity |
| **Memos** | Markdown/JSON | Structured notes |
| **Configurations** | YAML | CRD specifications |
| **Knowledge** | Markdown/PDF | Document formats |

---

## Data Isolation

| Boundary | Isolation Level |
|----------|-----------------|
| **Tenant** | Complete isolation; separate credentials |
| **Subscription** | Separate registries, Git repos |
| **Workbench** | Separate data stores, no cross-access |
| **Request** | Scoped to single scenario |

---

## Related Documentation

- [Signal Flow](../signal-flow.md) — Complete signal processing narrative
- [Normalized Signal Format](../implementation-concepts/normalized-signal-format.md)
- [Application Data Store](../implementation-concepts/application-data-store.md)

