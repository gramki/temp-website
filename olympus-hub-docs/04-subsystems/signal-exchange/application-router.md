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
| **Request Routing** | Route new Requests to Applications via preferred interface |
| **Update Routing** | Route Request updates to active Application sessions |
| **Interface Selection** | Route to Application Runtime's preferred interface (HTTP, Atropos, or OMS) |
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
5. Identify Application Runtime's preferred interface (HTTP, Atropos, or OMS)
6. Route Request via selected interface:
   - HTTP: POST to Application endpoint
   - Atropos: Publish to Application's topic
   - OMS: Send message to Application's queue
7. Track Application session binding
```

> **Note:** Signal Exchange delivers messages to Application Runtimes over HTTP, Atropos, or OMS interfaces as per the preference of the Application Runtime. Signal Exchange also accepts updates from Applications on any of these interfaces.

---

## Request Updates

For ongoing Application sessions:

```
1. Receive Request update
2. Find active Application session for Request
3. Route update via Application Runtime's preferred interface:
   - HTTP: POST update to Application endpoint
   - Atropos: Publish update to Application's topic
   - OMS: Send update message to Application's queue
```

### Message Delivery Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Out-of-Order Delivery** | Messages may arrive out of order — Application Runtimes must handle ordering if required |
| **Deduplication** | Deduplication is the responsibility of the recipient (Application Runtime), not Signal Exchange |
| **Idempotency** | Application Runtimes should design message handlers to be idempotent |
| **Interface Flexibility** | Applications can receive on one interface and send updates on a different interface |

---

## Related Documentation

- [Signal Exchange Overview](./README.md)
- [Request Factory](./request-factory.md)
- [Automation Runtimes](../automation-runtimes/README.md)
- [Hub Applications](../../01-concepts/hub-applications.md)

---

*TODO: Detailed design — routing table, invocation protocols, session tracking*

