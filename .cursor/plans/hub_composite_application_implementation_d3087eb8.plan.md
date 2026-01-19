---
name: Hub Composite Application Implementation
overview: Implement Hub Composite Application support to enable multiple Hub Applications to participate in a single Request without explicit orchestration, supporting multi-agent topologies like Blackboard, PEC Loop, and Market-Based patterns.
todos:
  - id: crd_definition
    content: Define HubCompositeApplicationSpec CRD structure with application references, OPA filters, and nested composite support
    status: pending
  - id: automation_spec_update
    content: Update ScenarioAutomationSpec to support composite_ref in addition to application.ref
    status: pending
  - id: operator_composite_resolution
    content: Implement composite resolution logic in Hub Operators (recursive flattening of nested composites)
    status: pending
    dependencies:
      - crd_definition
  - id: operator_multi_deployment
    content: "Implement multi-deployment generation: create HubApplicationDeployment for each constituent app with all-or-nothing lifecycle"
    status: pending
    dependencies:
      - operator_composite_resolution
  - id: sx_request_app_mapping
    content: Implement request-to-applications mapping storage in Signal Exchange (track which apps participate in each request)
    status: pending
    dependencies:
      - operator_multi_deployment
  - id: sx_opa_filter_evaluation
    content: Implement OPA filter evaluation in Application Router (filter input structure, policy evaluation, caching)
    status: pending
    dependencies:
      - sx_request_app_mapping
  - id: sx_multi_app_dispatch
    content: Implement multi-app update dispatch in Signal Exchange (async dispatch, per-app queues, DLQ handling)
    status: pending
    dependencies:
      - sx_opa_filter_evaluation
  - id: request_state_model
    content: Update Request state model to track active_applications and per-app processing state
    status: pending
    dependencies:
      - sx_multi_app_dispatch
  - id: update_conflict_resolution
    content: Implement update conflict resolution logic (latest wins if legal, rejected updates tracking)
    status: pending
    dependencies:
      - request_state_model
  - id: request_history_enhancement
    content: Enhance Request history to include source_app field and rejected updates with reasons
    status: pending
    dependencies:
      - update_conflict_resolution
  - id: workbench_validation
    content: Add validation in Workbench Management for composite references (existence check, circular reference detection)
    status: pending
    dependencies:
      - automation_spec_update
  - id: documentation_composite_concept
    content: Create hub-composite-application.md concept document with use cases and examples
    status: pending
  - id: documentation_guide
    content: Create using-composite-applications.md guide with OPA filter examples and deployment instructions
    status: pending
    dependencies:
      - documentation_composite_concept
  - id: documentation_updates
    content: Update existing documentation (hub-applications.md, application-router.md, signal-exchange README) with composite support
    status: pending
    dependencies:
      - documentation_composite_concept
  - id: seer_documentation
    content: Update Seer integration docs to note composite support (no code changes needed)
    status: pending
    dependencies:
      - documentation_updates
---

# Hub Composite Application Implementation Plan

## Overview

This plan implements support for **Hub Composite Applications** - a new CRD type that allows multiple Hub Applications to participate in the same Request. Applications coordinate through shared Request state (blackboard pattern) rather than explicit task assignment, enabling multi-agent topologies without orchestrators.

## Architecture Changes

### 1. New CRD: HubCompositeApplicationSpec

**Location**: `olympus-hub-docs/04-subsystems/operators/crd-reference.md`

**Structure**:
```yaml
apiVersion: hub.olympus.io/v1
kind: HubCompositeApplicationSpec
metadata:
  name: dispute-investigation-composite
  namespace: acme-disputes
  labels:
    hub.olympus.io/workbench: acme-disputes
spec:
  display_name: "Dispute Investigation Composite"
  description: "Multi-agent composite for dispute resolution"
  
  # List of constituent applications
  applications:
    - name: risk-agent
      ref:
        name: risk-assessment-agent
        version: "1.0.0"
      # Optional OPA filter for update routing
      opa_filter:
        policy: |
          package composite.filter
          default allow = false
          allow {
            input.update_type == "REQUEST_CREATED"
          }
          allow {
            input.update_type == "DOCUMENT_UPLOADED"
          }
    
    - name: compliance-agent
      ref:
        name: compliance-check-agent
        version: "1.0.0"
      opa_filter:
        policy: |
          package composite.filter
          default allow = false
          allow {
            input.update_type in ["REQUEST_CREATED", "RISK_ASSESSMENT_COMPLETE"]
          }
    
    # Can reference other composites (nested)
    - name: customer-service-composite
      composite_ref:
        name: customer-service-composite
        version: "1.0.0"
  
  # Composite-level metadata
  metadata:
    topology_pattern: "blackboard"  # blackboard | pec_loop | market_based | committee
```

**Key Design Decisions**:
- Supports both `HubApplicationSpec` references and nested `HubCompositeApplicationSpec` references
- OPA filter is optional per application (default: all updates pass through)
- Filter input includes: `update_type`, `request_state`, `update_payload`, `timestamp`
- Composite resolution flattens nested composites to union of all apps

---

### 2. Update ScenarioAutomationSpec

**Location**: `olympus-hub-docs/04-subsystems/operators/crd-reference.md`

**Change**: Extend `application.ref` to support composite references:

```yaml
spec:
  application:
    # Existing: single app reference
    ref: { name, version }
    
    # New: composite reference (mutually exclusive with ref)
    composite_ref: { name, version }
    
    # Detection: Operator checks if ref points to HubApplicationSpec or HubCompositeApplicationSpec
```

**Validation**: Add webhook validation to ensure either `ref` or `composite_ref` is set, not both.

---

### 3. Hub Operators - Composite Resolution

**Location**: `olympus-hub-docs/04-subsystems/operators/developer-operators.md`

**Changes to Hub Application Operator**:

1. **Composite Detection**:
   - When processing `ScenarioDeploymentSpec`, check if `application.ref` points to `HubCompositeApplicationSpec`
   - If composite, resolve recursively to get flat list of constituent apps

2. **Recursive Resolution Algorithm**:
   ```
   resolveComposite(compositeRef):
     apps = []
     for each app in composite.spec.applications:
       if app.ref exists:
         apps.append(app.ref)
       else if app.composite_ref exists:
         apps.extend(resolveComposite(app.composite_ref))
     return apps
   ```

3. **Multi-Deployment Generation**:
   - Generate one `HubApplicationDeployment` per constituent app
   - Link deployments via labels: `hub.olympus.io/composite: {composite-name}`
   - Track deployment state: all must succeed or all rollback

4. **Deployment State Tracking**:
   - Add composite deployment status to `ScenarioDeploymentSpec.status`
   - Track per-app deployment states
   - All-or-nothing: if any app fails, mark composite as failed

---

### 4. Signal Exchange - Application Router

**Location**: `olympus-hub-docs/04-subsystems/signal-exchange/application-router.md`

**Changes**:

1. **Request-to-Applications Mapping**:
   - Store mapping: `request_id → [app_deployment_1, app_deployment_2, ...]`
   - Populate when request is created and composite is detected
   - Store in Request metadata or separate mapping table

2. **Update Routing Logic**:
   ```
   routeRequestUpdate(request, update):
     apps = getApplicationsForRequest(request.id)
     for each app in apps:
       if hasOpaFilter(app):
         if evaluateOpaFilter(app.opa_filter, update):
           dispatchToApp(app, update)
       else:
         dispatchToApp(app, update)
   ```

3. **OPA Filter Evaluation**:
   - Filter input structure:
     ```json
     {
       "update_type": "REQUEST_CREATED",
       "request_state": {...},
       "update_payload": {...},
       "timestamp": "2026-01-15T10:00:00Z",
       "app_name": "risk-agent"
     }
     ```
   - Use existing OPA integration (similar to Persona Twin triggers)
   - Cache filter evaluation results for performance

4. **Async Dispatch**:
   - All dispatches are asynchronous
   - Each app gets its own dispatch queue
   - DLQ per app for failed dispatches

---

### 5. Signal Exchange - Request Update Processing

**Location**: `olympus-hub-docs/04-subsystems/signal-exchange/README.md`

**Changes**:

1. **Multi-App Update Handling**:
   - When `REQUEST_UPDATE` received, dispatch to all apps in composite
   - Track which apps have processed which updates (for observability)
   - Handle conflicting updates: latest wins if legal, otherwise rejected

2. **Update Conflict Resolution**:
   - Store update sequence numbers or timestamps
   - Validate update legality via OPA (if policy exists)
   - Record rejected updates in request history with reason

3. **Request History Enhancement**:
   - Add `source_app` field to each update record
   - Track update processing status per app
   - Include rejected updates with rejection reason

---

### 6. Request Management

**Location**: `olympus-hub-docs/04-subsystems/request-management/` (various files)

**Changes**:

1. **Request State Model**:
   - Add `active_applications: [app_deployment_id, ...]` to Request
   - Track per-app processing state
   - Maintain request-to-applications mapping

2. **Request Lifecycle**:
   - When request created with composite app, initialize all app sessions
   - Track app lifecycle independently (app can crash/restart without affecting others)
   - Request completion: all apps can contribute, no explicit coordination needed

3. **Request Metadata**:
   ```yaml
   request:
     metadata:
       composite_app: "dispute-investigation-composite"
       active_applications:
         - app_id: "risk-agent-deployment-1"
           status: "active"
           last_update: "2026-01-15T10:00:00Z"
         - app_id: "compliance-agent-deployment-1"
           status: "active"
           last_update: "2026-01-15T10:01:00Z"
   ```

---

### 7. Workbench Management

**Location**: `olympus-hub-docs/04-subsystems/workbench-management/scenario-definitions.md`

**Changes**:

1. **Scenario Schema Update**:
   ```yaml
   scenario:
     application:
       # Support both single app and composite
       type: "single" | "composite"
       application_id: string  # For single
       composite_id: string   # For composite
   ```

2. **Validation**:
   - Ensure referenced composite exists
   - Validate composite structure (no circular references)
   - Check all constituent apps are valid

---

### 8. Documentation Updates

**New Documentation**:

1. **`olympus-hub-docs/02-system-design/implementation-concepts/hub-composite-application.md`**
   - Concept overview
   - Use cases and examples
   - Relationship to multi-agent topologies
   - Design decisions

2. **`olympus-hub-docs/10-guides/using-composite-applications.md`**
   - How to create composite apps
   - OPA filter examples
   - Deployment guide
   - Troubleshooting

**Update Existing Documentation**:

1. **`olympus-hub-docs/01-concepts/hub-applications.md`**
   - Add composite as new application type
   - Update application types table

2. **`olympus-hub-docs/02-system-design/implementation-concepts/hub-application.md`**
   - Add section on composite applications
   - Explain relationship to single apps

3. **`olympus-hub-docs/02-system-design/implementation-concepts/hub-application-deployment.md`**
   - Document multi-deployment handling
   - Composite deployment lifecycle

4. **`olympus-hub-docs/04-subsystems/signal-exchange/application-router.md`**
   - Update routing flow diagrams
   - Document composite routing logic
   - OPA filter evaluation

5. **`olympus-hub-docs/04-subsystems/signal-exchange/README.md`**
   - Update flow diagrams for multi-app dispatch
   - Document update conflict resolution

---

### 9. Seer Integration

**Location**: `olympus-seer-docs/seer-design/hub-integration/`

**Changes**:

1. **No Seer-Specific Changes Required**:
   - Seer agents operate independently
   - Each agent gets its own `EmploymentSpec` (generated from `HubApplicationDeployment`)
   - Agents don't need to know they're in a composite

2. **Documentation Update**:
   - `olympus-seer-docs/seer-design/hub-integration/employed-agent.md`
     - Note that agents can be part of composites
     - Explain independent operation

---

## Implementation Phases

### Phase 1: CRD and Operator Support
- Define `HubCompositeApplicationSpec` CRD
- Update `ScenarioAutomationSpec` to support composite references
- Implement composite resolution in Hub Operators
- Multi-deployment generation logic

### Phase 2: Signal Exchange Routing
- Request-to-applications mapping storage
- Multi-app update dispatch
- OPA filter evaluation integration
- Async dispatch with DLQ

### Phase 3: Request Management
- Request state model updates
- Multi-app session tracking
- Update conflict resolution
- Request history enhancements

### Phase 4: Documentation and Testing
- Complete documentation
- Example composite configurations
- Integration testing with all runtimes

---

## Open Questions Resolved

- ✅ Use cases: PEC Loop, Blackboard, Market-Based, Role-Specialized Committees
- ✅ OPA filters: Inline Rego policy, filter on `update_type`
- ✅ Task creation: Multiple apps can create tasks for same agent
- ✅ Composite lifecycle: Requires redeployment (not dynamic)
- ✅ Cross-runtime: Supported (Seer + Rhea + Atlantis)
- ✅ Nested composites: Supported (flattened to union)

---

## Testing Considerations

1. **Unit Tests**:
   - Composite resolution (including nested)
   - OPA filter evaluation
   - Update routing logic

2. **Integration Tests**:
   - Multi-app request processing
   - Cross-runtime composites
   - Update conflict scenarios
   - Deployment rollback scenarios

3. **Example Scenarios**:
   - PEC Loop: Planner-Executor-Critic
   - Blackboard: Risk-Compliance-CustomerService
   - Market-Based: Inquiry routing with bidding

---

## Migration Path

- Existing single-app scenarios continue to work unchanged
- New composite feature is additive
- No breaking changes to existing APIs
- Gradual adoption: teams can migrate to composites when needed