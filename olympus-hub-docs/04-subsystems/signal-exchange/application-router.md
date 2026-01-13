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

### Single Application (Existing Behavior)

```
1. Receive Request from Request Factory
2. Identify Scenario from Request
3. Look up Application mapping for Scenario
4. If single application (routing.application exists):
   a. Determine Application type and Automation Runtime
   b. Identify Application Runtime's preferred interface (HTTP, Atropos, or OMS)
   c. Route Request via selected interface:
      - HTTP: POST to Application endpoint
      - Atropos: Publish to Application's topic
      - OMS: Send message to Application's queue
5. Track Application session binding
```

### Multiple Applications (Composite)

```
1. Receive Request from Request Factory
2. Identify Scenario from Request
3. Look up Application mapping for Scenario
4. If multiple applications (routing.applications exists):
   a. For each application in list:
      i. Evaluate OPA filter (if present)
      ii. If filter allows or no filter:
         - Determine Application type and Automation Runtime
         - Identify Application Runtime's preferred interface
         - Async dispatch Request Update via selected interface
      iii. If filter rejects: skip this application
   b. Track all active application sessions
```

**Key**: Signal Exchange doesn't know about composites. It just sees "this scenario has N apps" in the routing table.

> **Note:** Signal Exchange delivers messages to Application Runtimes over HTTP, Atropos, or OMS interfaces as per the preference of the Application Runtime. Signal Exchange also accepts updates from Applications on any of these interfaces.

---

## Request Updates

### Single Application (Existing Behavior)

For ongoing Application sessions:

```
1. Receive Request update
2. Find active Application session for Request
3. Route update via Application Runtime's preferred interface:
   - HTTP: POST update to Application endpoint
   - Atropos: Publish update to Application's topic
   - OMS: Send update message to Application's queue
```

### Multiple Applications (Composite)

For composite scenarios with multiple active sessions:

```
1. Receive Request update
2. Look up all active Application sessions for Request (from routing table)
3. For each application session:
   a. Build OPA filter input:
      {
        update_type: update.type,
        request_state: request.state,
        update_payload: update.payload,
        timestamp: now(),
        app_identity: { name: app.name, deployment_id: app.deployment_id }
      }
   b. Evaluate OPA filter (if present)
   c. If filter allows or no filter:
      - Route update via Application Runtime's preferred interface
      - Async dispatch (non-blocking)
   d. If filter rejects: skip this application
4. Track which apps received the update (for observability)
```

### OPA Filter Evaluation

OPA filters are evaluated inline using the OPA engine. Filters receive full context:

- `update_type`: Type of update (REQUEST_CREATED, STATE_UPDATE, etc.)
- `request_state`: Current request state (id, status, scenario_id, etc.)
- `update_payload`: Full update payload
- `timestamp`: Update timestamp
- `app_identity`: App name and deployment ID

Filters return `allow: true/false`. If filter is absent, update is allowed by default.

**Performance**: Compiled filters are cached in the routing table for performance.

### Message Delivery Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Out-of-Order Delivery** | Messages may arrive out of order — Application Runtimes must handle ordering if required |
| **Deduplication** | Deduplication is the responsibility of the recipient (Application Runtime), not Signal Exchange |
| **Idempotency** | Application Runtimes should design message handlers to be idempotent |
| **Interface Flexibility** | Applications can receive on one interface and send updates on a different interface |

---

## Routing Table Schema

The routing table supports both single-app and multi-app scenarios:

**Single App** (backward compatible):
```yaml
scenario_routing:
  scenario_id: "dispute-investigation"
  application:
    deployment_id: "dispute-handler-sandbox"
    endpoint: "http://..."
```

**Multiple Apps** (for composites):
```yaml
scenario_routing:
  scenario_id: "dispute-investigation"
  applications:
    - deployment_id: "risk-agent-deployment-sandbox"
      endpoint: "http://..."
      opa_filter: "<compiled Rego policy>"
    - deployment_id: "compliance-agent-deployment-sandbox"
      endpoint: "http://..."
      opa_filter: "<compiled Rego policy>"
```

The routing table is populated by the Composite Deployment Operator at deployment time. See [ADR-0126](../../decision-logs/0126-composite-routing-table-schema.md) for details.

---

## Related Documentation

- [Signal Exchange Overview](./README.md)
- [Request Factory](./request-factory.md)
- [Automation Runtimes](../automation-runtimes/README.md)
- [Hub Applications](../../01-concepts/hub-applications.md)
- [Hub Composite Application](../../02-system-design/implementation-concepts/hub-composite-application.md)
- [ADR-0126: Composite Routing Table Schema](../../decision-logs/0126-composite-routing-table-schema.md)

---

*Application Router supports both single-app and multi-app routing, enabling composite applications while maintaining backward compatibility.*

