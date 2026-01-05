# Olympus LakeStack

> **Status:** 🔴 Stub — Reference only

**Olympus LakeStack** is the Olympus ecosystem's analytics, data infrastructure, and reporting platform. It includes **Pontus** (data infrastructure) and **ETSL** (Enterprise Truth & Semantics Layer). Hub integrates with LakeStack for operational analytics, ETSL integration, and the Report Center.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Type** | Olympus Platform Service |
| **Purpose** | Analytics, data lake, semantic layer (ETSL), reporting |
| **Components** | Pontus (data infrastructure), ETSL (semantic layer), Report Center |
| **Hub Usage** | Hub Analytics subsystem integrates with LakeStack |

---

## Components

### Pontus (Data Infrastructure)

Pontus provides the data infrastructure layer:

| Capability | Description |
|------------|-------------|
| **Aggregated Data** | Data from enterprise systems collected and prepared for consumption |
| **Originated Data** | New data produced by Olympus product lines |
| **Enterprise Golden Data Model** | Base facts and dimensions, master data across functional domains |
| **Serving Stores** | Purpose-specific data stores (Operations, Customer Service, etc.) |
| **Data Marts** | Pre-built analytical views for specific use cases |

### ETSL (Enterprise Truth & Semantics Layer)

ETSL provides the semantic layer:

| Capability | Description |
|------------|-------------|
| **Assertion Management** | Captures claims from systems about facts at points in time |
| **Authority Modeling** | Explicitly models who decides what is true for what scope |
| **Reconciliation** | Resolves multiple assertions into accepted enterprise truth |
| **State Derivation** | Derives point-in-time state from reconciled assertions |
| **ETSL Data Artifacts** | Authority-qualified, time-aware representations of enterprise truth |
| **Data Products** | Consumer-aligned interpretations of ETSL Data Artifacts |

### Report Center

| Capability | Hub Usage |
|------------|-----------|
| **Report Builder** | Create operational and business reports |
| **Report Publisher** | Publish reports to catalogs accessible by Hub |
| **Report Dispatcher** | Schedule and trigger report generation |
| **Embedding SDK** | Render reports within Hub console frames |

---

## Hub Integration Points

| Integration | Description |
|-------------|-------------|
| **Hub Analytics → ETSL** | Registers Operations Data into ETSL as assertions |
| **Hub Analytics → Pontus** | Creates Operations Data Marts using Pontus infrastructure |
| **Hub Analytics → Report Center** | Creates Data Products for operations reporting |
| **Report Consoles** | Agent, Supervisor, Steward desks consume reports |
| **Context Binding** | Hub passes workbench/user context for filtering |
| **Enterprise Memory ↔ ETSL** | Future: configurable integration of Enterprise Memory as ETSL assertions |

---

## Related Documentation

- [Hub Analytics](../04-subsystems/hub-analytics/README.md) — Hub's integration with LakeStack
- [Storage Architecture — ETSL Integration](../07-data-architecture/storage-architecture.md#etsl-and-pontus-integration-touch-points) — Detailed touch points
- [Olympus Platform Dependencies](./olympus-platform-dependencies.md) — Other platform services

---

*Note: Detailed LakeStack, Pontus, and ETSL documentation is maintained separately. This document covers Hub's integration touch points only.*

