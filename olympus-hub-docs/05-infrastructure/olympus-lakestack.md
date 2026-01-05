# Olympus LakeStack

> **Status:** 🔴 Stub — Reference only

**Olympus LakeStack** is the Olympus ecosystem's analytics and reporting platform. Hub integrates with LakeStack for operational analytics and the Report Center.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Type** | Olympus Platform Service |
| **Purpose** | Analytics, data lake, reporting |
| **Hub Usage** | Hub Analytics subsystem integrates with LakeStack |

---

## Capabilities Used by Hub

| Capability | Hub Usage |
|------------|-----------|
| **Report Center** | Build, publish, and dispatch reports |
| **Report Builder** | Create operational and business reports |
| **Report Publisher** | Publish reports to catalogs accessible by Hub |
| **Report Dispatcher** | Schedule and trigger report generation |
| **Embedding SDK** | Render reports within Hub console frames |

---

## Integration Points

| Integration | Description |
|-------------|-------------|
| **Hub Analytics** | Primary integration point for report catalog sync |
| **Report Consoles** | Agent, Supervisor, Steward desks consume reports |
| **Context Binding** | Hub passes workbench/user context for filtering |

---

## Related Documentation

- [Hub Analytics](../04-subsystems/hub-analytics/README.md) — Hub's integration with LakeStack
- [Olympus Platform Dependencies](./olympus-platform-dependencies.md) — Other platform services

---

*Note: Detailed LakeStack documentation is maintained separately. This document covers Hub's integration only.*

