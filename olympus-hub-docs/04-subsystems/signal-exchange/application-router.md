# Application Router

> **Status:** 🔴 Stub — Placeholder for expansion

The Application Router routes Requests and Request updates to the appropriate Hub Applications based on Scenario configuration.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Route Requests to Hub Applications |
| **Input** | Requests from Request Factory |
| **Output** | Invocations to Hub Applications |
| **Configuration** | Scenario → Application mappings from Workbench Management |

---

## Responsibilities

| Function | Description |
|----------|-------------|
| **Application Selection** | Determine target Application from Scenario |
| **Request Routing** | Route new Requests to Applications |
| **Update Routing** | Route Request updates to active Application sessions |
| **Load Balancing** | Distribute across Application instances |
| **Failover** | Handle Application unavailability |

---

## Hub Application Types

Each Automation Runtime provides specialized Hub Application types:

| Automation Runtime | Hub Application Type(s) | Invocation Pattern |
|-------------------|------------------------|-------------------|
| **Atlantis** | Procedure Apps, Decision Apps, Prediction Apps | Synchronous |
| **Perseus** | File Apps, Map-Reduce Apps, Complex Event Apps | Batch/Async |
| **Rhea** | Workflow Apps | Process instantiation |
| **ChronoShift** | Durable Workflow Apps | Workflow signal |
| **Seer** | Seer Case Orchestration Agent | Case initiation |

---

## Routing Flow

```
1. Receive Request from Request Factory
2. Identify Scenario from Request
3. Look up Application mapping for Scenario
4. Determine Application type and Automation Runtime
5. Invoke appropriate Automation Runtime API:
   - Atlantis: Function invocation
   - Perseus: Job submission
   - Rhea: Process start
   - ChronoShift: Workflow start/signal
   - Seer: Case initiation/update
6. Track Application session binding
```

---

## Request Updates

For ongoing Application sessions:

```
1. Receive Request update
2. Find active Application session for Request
3. Route update to correct session:
   - ChronoShift: Workflow signal
   - Seer: Case event
   - Others: As appropriate for Application type
```

---

## Related Documentation

- [Signal Exchange Overview](./README.md)
- [Request Factory](./request-factory.md)
- [Automation Runtimes](../automation-runtimes/README.md)
- [Hub Applications](../../01-concepts/hub-applications.md)

---

*TODO: Detailed design — routing table, invocation protocols, session tracking*

