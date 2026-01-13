---
name: Hub Composite Application Implementation
overview: Implement Hub Composite Application support with deployment-time resolution. Hub Operators flatten composites into routing tables; Signal Exchange routes to multiple apps per scenario without needing composite awareness.
todos:
  - id: crd_composite_spec
    content: Define HubCompositeApplicationSpec CRD with applications list, OPA filters, nested composite refs
    status: pending
  - id: crd_composite_deployment
    content: Define HubCompositeApplicationDeployment CRD with child ownership and status aggregation
    status: pending
  - id: crd_automation_spec
    content: Update ScenarioAutomationSpec to support composite_ref (mutually exclusive with ref)
    status: pending
  - id: operator_composite_app
    content: Implement Composite Application Operator for spec validation
    status: pending
    dependencies:
      - crd_composite_spec
  - id: operator_composite_deploy
    content: Implement Composite Deployment Operator - resolve, create children, populate routing table
    status: pending
    dependencies:
      - crd_composite_deployment
      - operator_composite_app
  - id: operator_scenario_deploy
    content: Update Scenario Deployment Operator to create HubCompositeApplicationDeployment for composite refs
    status: pending
    dependencies:
      - operator_composite_deploy
  - id: routing_table_schema
    content: Update routing table schema to support list of apps with OPA filters per scenario
    status: pending
  - id: app_router_multiapp
    content: Update Application Router to handle list of apps from routing table
    status: pending
    dependencies:
      - routing_table_schema
  - id: app_router_opa
    content: Add OPA filter evaluation in Application Router before dispatch
    status: pending
    dependencies:
      - app_router_multiapp
  - id: request_source_app
    content: Add source_app field to request history and update records
    status: pending
  - id: request_conflict
    content: Implement update conflict resolution (latest wins, rejection tracking)
    status: pending
    dependencies:
      - request_source_app
  - id: doc_concept
    content: Create hub-composite-application.md implementation concept in 02-system-design/implementation-concepts/
    status: completed
  - id: doc_hub_app_update
    content: Update hub-application.md implementation concept to reference composite applications
    status: completed
    dependencies:
      - doc_concept
  - id: doc_hub_app_deployment_update
    content: Update hub-application-deployment.md to document HubCompositeApplicationDeployment relationship
    status: completed
    dependencies:
      - doc_concept
  - id: doc_guide
    content: Create using-composite-applications.md guide in 10-guides/ with OPA filter examples
    status: completed
    dependencies:
      - doc_concept
  - id: adr_composite_apps
    content: Create ADR-0125-hub-composite-applications.md for composite application design decision
    status: completed
  - id: adr_composite_routing
    content: Create ADR-0126-composite-routing-table-schema.md for routing table multi-app schema decision
    status: completed
    dependencies:
      - adr_composite_apps
  - id: doc_crd_reference
    content: Update crd-reference.md to add HubCompositeApplicationSpec and HubCompositeApplicationDeployment
    status: completed
    dependencies:
      - doc_concept
  - id: doc_developer_operators
    content: Update developer-operators.md with Composite Application and Composite Deployment operators
    status: completed
    dependencies:
      - doc_concept
  - id: doc_app_router
    content: Update application-router.md with multi-app routing and OPA filter evaluation
    status: completed
    dependencies:
      - doc_concept
  - id: doc_sx_readme
    content: Update signal-exchange/README.md to reflect multi-app dispatch in architecture diagrams
    status: completed
    dependencies:
      - doc_concept
  - id: doc_scenario_defs
    content: Update scenario-definitions.md with routing table schema changes for composites
    status: completed
    dependencies:
      - doc_concept
  - id: doc_hub_apps_concept
    content: Update 01-concepts/hub-applications.md to add composite as application type
    status: completed
    dependencies:
      - doc_concept
  - id: doc_request_management
    content: Update request-management docs with source_app tracking and conflict resolution
    status: completed
    dependencies:
      - doc_concept
  - id: doc_seer_integration
    content: Update seer-design/hub-integration/employed-agent.md to note composite support (no code changes)
    status: completed
    dependencies:
      - doc_concept
  - id: scratchpad_cleanup
    content: Finalize scratchpad/hub-composite-app.md and remove Q&A section
    status: completed
    dependencies:
      - doc_concept
  - id: cross_ref_verification
    content: Verify and update all cross-references to hub-application docs across the codebase
    status: completed
    dependencies:
      - doc_hub_app_update
      - doc_hub_app_deployment_update
---

# Hub Composite Application Implementation Plan

## Overview

Implement **Hub Composite Applications** enabling multiple Hub Applications to participate in the same Request. Composites are resolved at **deployment time** - Signal Exchange sees only a list of apps per scenario, not composites.

## Key Architectural Decisions

| Decision | Choice | Rationale |

|----------|--------|-----------|

| Session Model | Each app gets independent session | Apps operate autonomously |

| Deployment CRD | Create `HubCompositeApplicationDeployment` | Proper ownership for lifecycle |

| OPA Filter Input | Full access | Maximum filtering flexibility |

| Resolution Time | Deployment time | Simpler SX, routing table has flattened list |

---

## Architecture

```mermaid
flowchart TB
    subgraph deployment [Deployment Time - Hub Operators]
        HCAS[HubCompositeApplicationSpec]
        HCAD[HubCompositeApplicationDeployment]
        HAD1[HubApplicationDeployment: App1]
        HAD2[HubApplicationDeployment: App2]
        HAD3[HubApplicationDeployment: App3]
        
        HCAS --> HCAD
        HCAD --> HAD1
        HCAD --> HAD2
        HCAD --> HAD3
    end
    
    subgraph wm [Workbench Management]
        RT[Routing Table]
    end
    
    subgraph sx [Signal Exchange - Runtime]
        AR[Application Router]
    end
    
    HAD1 --> RT
    HAD2 --> RT
    HAD3 --> RT
    RT --> AR
```

**Key Insight**: Signal Exchange doesn't know about composites. It just sees "Scenario X has apps [A, B, C] with filters [F1, F2, F3]" in the routing table.

---

## New CRDs

### 1. HubCompositeApplicationSpec

```yaml
apiVersion: hub.olympus.io/v1
kind: HubCompositeApplicationSpec
metadata:
  name: dispute-investigation-composite
  namespace: acme-disputes
spec:
  display_name: "Dispute Investigation Composite"
  
  applications:
  - name: risk-agent
      ref:
        name: risk-assessment-agent
        version: "1.0.0"
      opa_filter:
        policy: |
          package composite.filter
          default allow = false
          allow { input.update_type == "REQUEST_CREATED" }
          allow { input.update_type == "DOCUMENT_UPLOADED" }
    
  - name: compliance-agent
      ref:
        name: compliance-check-agent
        version: "1.0.0"
      opa_filter:
        policy: |
          package composite.filter
          default allow = false
          allow { input.update_type in ["REQUEST_CREATED", "RISK_ASSESSMENT_COMPLETE"] }
    
    # Nested composite
  - name: customer-service
      composite_ref:
        name: customer-service-composite
        version: "1.0.0"
```

### 2. HubCompositeApplicationDeployment

```yaml
apiVersion: hub.olympus.io/v1
kind: HubCompositeApplicationDeployment
metadata:
  name: dispute-investigation-composite-sandbox
  namespace: acme-disputes
spec:
  compositeRef:
    name: dispute-investigation-composite
    version: "1.0.0"
  workbenchInstance:
    name: acme-disputes-sandbox

status:
  phase: Running
  applicationDeployments:
  - name: risk-agent
      deploymentRef: risk-agent-deployment-sandbox
      phase: Running
  - name: compliance-agent
      deploymentRef: compliance-agent-deployment-sandbox
      phase: Running
```

**Ownership**: `HubCompositeApplicationDeployment` owns child `HubApplicationDeployment` resources via `ownerReference`.

---

## Component Changes

### 1. Hub Operators

**Location**: `olympus-hub-docs/04-subsystems/operators/developer-operators.md`

**New: Composite Application Operator**

- Watches `HubCompositeApplicationSpec`
- Validates structure (no circular refs)
- No deployment logic (just spec validation)

**New: Composite Deployment Operator**

- Watches `HubCompositeApplicationDeployment`
- Resolves composite recursively (flattens nested composites)
- Creates child `HubApplicationDeployment` for each app
- Sets `ownerReference` for garbage collection
- Aggregates child status → composite status
- **Populates routing table** with flattened app list + OPA filters

**Update: Scenario Deployment Operator**

- When `ScenarioAutomationSpec.application.composite_ref` is set:
                                                                                                                                                                                                                                                                - Create `HubCompositeApplicationDeployment` instead of `HubApplicationDeployment`

---

### 2. Routing Table (Workbench Management)

**Location**: `olympus-hub-docs/04-subsystems/workbench-management/`

**Current Schema**:

```yaml
scenario_routing:
  scenario_id: "dispute-investigation"
  application:
    deployment_id: "dispute-handler-sandbox"
    endpoint: "..."
```

**New Schema** (backward compatible):

```yaml
scenario_routing:
  scenario_id: "dispute-investigation"
  
  # Single app (existing)
  application:
    deployment_id: "dispute-handler-sandbox"
    endpoint: "..."
  
  # OR multiple apps (new - for composites)
  applications:
  - deployment_id: "risk-agent-deployment-sandbox"
      endpoint: "..."
      opa_filter: "<compiled policy>"
  - deployment_id: "compliance-agent-deployment-sandbox"
      endpoint: "..."
      opa_filter: "<compiled policy>"
```

If `applications` is present, Application Router routes to all. If only `application` is present, existing behavior.

---

### 3. Signal Exchange - Application Router

**Location**: `olympus-hub-docs/04-subsystems/signal-exchange/application-router.md`

**Changes** (minimal):

1. **Routing Lookup**: Accept list of apps from routing table
2. **Fan-out**: For each app in list, evaluate OPA filter and dispatch if allowed
3. **OPA Filter Evaluation**: New logic to evaluate inline Rego policy
```
routeRequestUpdate(request, update):
  routing = lookupRouting(request.scenario_id)
  
  if routing.applications exists:
    # Composite - fan-out
    for each app in routing.applications:
      filterInput = {
        update_type: update.type,
        request_state: request.state,
        update_payload: update.payload,
        timestamp: now(),
        app_identity: { name: app.name, deployment_id: app.deployment_id }
      }
      if app.opa_filter is None OR evaluateOPA(app.opa_filter, filterInput):
        asyncDispatch(app.endpoint, update)
  else:
    # Single app - existing behavior
    dispatch(routing.application.endpoint, update)
```


**Key**: SX doesn't know about composites. It just sees "this scenario has N apps".

---

### 4. Request Management

**Location**: `olympus-hub-docs/04-subsystems/request-management/`

**Changes**:

1. **Update Conflict Resolution**:

                                                                                                                                                                                                                                                                                                                                                                                                - Multiple apps can update same request concurrently
                                                                                                                                                                                                                                                                                                                                                                                                - Latest update wins (timestamp-based)
                                                                                                                                                                                                                                                                                                                                                                                                - Rejected updates recorded in history

2. **Request History Enhancement**:

                                                                                                                                                                                                                                                                                                                                                                                                - Add `source_app` field to each update record
                                                                                                                                                                                                                                                                                                                                                                                                - Track rejection reasons
```yaml
history:
 - timestamp: "2026-01-15T10:01:00Z"
    source_app: "risk-agent-deployment-sandbox"
    update_type: "RISK_ASSESSMENT_COMPLETE"
    status: "accepted"
```


---

### 5. ScenarioAutomationSpec Update

**Location**: `olympus-hub-docs/04-subsystems/operators/crd-reference.md`

```yaml
spec:
  application:
    # Option 1: Single app (existing)
    ref:
      name: dispute-handler
      version: "1.0.0"
    
    # Option 2: Composite (new - mutually exclusive)
    composite_ref:
      name: dispute-investigation-composite
      version: "1.0.0"
```

---

## Documentation

### New Documents

| Document | Purpose |

|----------|---------|

| `02-system-design/implementation-concepts/hub-composite-application.md` | Implementation concept for composite applications |

| `10-guides/using-composite-applications.md` | Developer guide with OPA filter examples |

| `decision-logs/0125-hub-composite-applications.md` | ADR: Composite application design decision |

| `decision-logs/0126-composite-routing-table-schema.md` | ADR: Routing table multi-app schema |

### Implementation Concept Updates

| Document | Changes |

|----------|---------|

| `02-system-design/implementation-concepts/hub-application.md` | Add reference to composite applications |

| `02-system-design/implementation-concepts/hub-application-deployment.md` | Document HubCompositeApplicationDeployment relationship |

### Subsystem Updates

| Document | Changes |

|----------|---------|

| `01-concepts/hub-applications.md` | Add composite as application type |

| `04-subsystems/operators/crd-reference.md` | Add HubCompositeApplicationSpec, HubCompositeApplicationDeployment |

| `04-subsystems/operators/developer-operators.md` | Add Composite Application and Composite Deployment operators |

| `04-subsystems/signal-exchange/README.md` | Update architecture diagrams for multi-app dispatch |

| `04-subsystems/signal-exchange/application-router.md` | Multi-app routing, OPA filter evaluation |

| `04-subsystems/workbench-management/scenario-definitions.md` | Routing table schema changes |

| `04-subsystems/request-management/` | source_app tracking, conflict resolution |

### Seer Documentation

| Document | Changes |

|----------|---------|

| `olympus-seer-docs/seer-design/hub-integration/employed-agent.md` | Note composite support (no code changes needed) |

### Cross-Reference Verification

After updates, verify all cross-references to:

- `hub-application.md`
- `hub-application-deployment.md`
- `application-router.md`

---

## Summary of Changes

| Component | Change |

|-----------|--------|

| **Hub Operators** | New Composite operators, resolve at deployment time |

| **Routing Table** | Support list of apps per scenario |

| **Application Router** | Fan-out to multiple apps with OPA filter |

| **Request Management** | Track source_app, handle concurrent updates |

| **Signal Exchange Core** | No changes - still Request-level only |

---

## Implementation Phases

### Phase 1: CRD Definitions

- `HubCompositeApplicationSpec`
- `HubCompositeApplicationDeployment`
- `ScenarioAutomationSpec` update

### Phase 2: Operator Support

- Composite Application Operator
- Composite Deployment Operator
- Routing table population

### Phase 3: Application Router

- Multi-app routing lookup
- OPA filter evaluation
- Fan-out dispatch

### Phase 4: Request Management

- source_app tracking
- Conflict resolution

### Phase 5: Documentation

- ADRs: composite-applications, composite-routing-table-schema
- New implementation concept: hub-composite-application.md
- Update implementation concepts: hub-application.md, hub-application-deployment.md
- Update subsystem docs: operators, signal-exchange, request-management
- New guide: using-composite-applications.md
- Seer integration docs update
- Cross-reference verification
- Scratchpad cleanup