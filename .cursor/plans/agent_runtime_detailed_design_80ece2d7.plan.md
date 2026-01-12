---
name: Agent Runtime Detailed Design
overview: ""
todos:
  - id: migrate-runtime-deployment
    content: Move runtime-deployment.md to agent-runtime/ folder and update references
    status: completed
  - id: create-iam-provisioning
    content: "Create iam-provisioning.md with IAM profile creation, lifecycle, roles/groups inheritance logic, bot mode, and configuration details. Note: EmploymentSpec schema will evolve - enhance in employment-spec-manager.md"
    status: completed
    dependencies:
      - migrate-runtime-deployment
  - id: create-authority-respawning
    content: Create authority-change-respawning.md with detection, triggers, and respawning process
    status: completed
    dependencies:
      - migrate-runtime-deployment
  - id: create-signal-exchange-integration
    content: Create signal-exchange-integration.md with scenario change detection and update flow
    status: completed
    dependencies:
      - migrate-runtime-deployment
  - id: create-ingress-gateway-integration
    content: Create agent-ingress-gateway-integration.md with request routing and subscription lifecycle
    status: completed
    dependencies:
      - migrate-runtime-deployment
  - id: enhance-ingress-config
    content: Enhance runtime-deployment.md with ingress path provisioning and lifecycle details
    status: completed
    dependencies:
      - migrate-runtime-deployment
  - id: update-scope-doc
    content: Update SCOPE.md to mark completed items and update next steps
    status: completed
    dependencies:
      - create-iam-provisioning
      - create-authority-respawning
      - create-signal-exchange-integration
      - create-ingress-gateway-integration
      - enhance-ingress-config
  - id: update-readme
    content: Update README.md with links to new documents and updated design status
    status: completed
    dependencies:
      - update-scope-doc
---

# Agent Runtime Detailed Design Plan

## Objective

Complete detailed design for all 5 open items identified in `agent-runtime/SCOPE.md`:

1. IAM Profile Provisioning
2. Respawning After Authority Enforcement Changes
3. Signal Exchange Scenario Updates (Seer handles)
4. Agent Ingress Gateway Integration
5. Ingress Path Configuration

---

## Current State

- **Existing Content**: `runtime-deployment.md` (650 lines) covers core runtime operations
- **Scope Document**: `agent-runtime/SCOPE.md` identifies gaps and priorities
- **Status**: Core deployment/scaling covered; IAM, authority, and integration details missing

---

## Implementation Plan

### Phase 1: Content Migration and Structure

1. **Migrate existing content**

   - Move `subsystems/runtime-deployment.md` → `subsystems/agent-runtime/runtime-deployment.md`
   - Update all references to the new location
   - Preserve all existing content

### Phase 2: IAM Profile Provisioning (High Priority)

2. **Create `agent-runtime/iam-provisioning.md`**

   - **IAM Profile Creation Flow**
     - EmploymentSpec contains unique code for Employed Agent (unique per tenant subscription)
     - Seer Operator watches EmploymentSpec CRD
     - Operator contacts IAM using Hub Environment endpoints/domain details from Workbench instance
     - Calls Cipher IAM Extensions API to create agent profile
     - User delegation vs Role delegation setup
     - Profile tags (Raw/Trained/Employed agent tags)
   - **EmploymentSpec Profile Information**
     - Authority Delegation Information (from `spec.delegation`)
     - Manager of the Employed Agent (from `spec.delegation.accountable`)
     - User-Groups the agent will be part of (from `spec.delegation.groups`)
     - OPA policies per PEP (from `spec.delegation.policies`)
       - Policies can be referenced files (not inline)
       - Unknown PEP policies are ignored
       - Policy specified per each PEP that Cipher recognizes
   - **IAM Profile Lifecycle**
     - Profile creation during deployment (before pod creation)
       - If Cipher cannot provision IAM profile, employment operation fails
     - Profile updates when EmploymentSpec changes (operator always updates to keep in sync)
     - Profile updates when authority changes (triggered by Delegation Chain Sync Service)
     - Profile revocation during kill switch (immediate IAM revocation)
     - Profile cleanup on agent retirement
   - **Roles and Groups Inheritance Logic**
     - If EmploymentSpec uses "*" for roles/groups:
       - All delegator's roles and groups are copied to agent at profile creation/update
     - If EmploymentSpec uses CSV value for roles/groups:
       - Only subset that delegator also has will be retained
       - Rest will be rejected and deployment continues with warning
       - Resource will be in out-of-sync status until unavailable roles/groups are removed
   - **Bot Mode (No Delegator)**
     - If there is no delegator, Employed Agent acts as a Bot
     - Has base identity only
     - Accountable human is the manager
     - Roles, groups, and policies are NOT inherited from any other profile
   - **IAM Profile Configuration**
     - EmploymentSpec authority delegation → IAM roles/permissions mapping
     - Integration with Cipher IAM policy enforcement points
     - Credential injection (bot tokens, service accounts) via zone-vault
   - **Schema Evolution**
     - EmploymentSpec and TrainingSpec schemas will evolve
     - Should enhance schemas in respective subsystem documents:
       - EmploymentSpec schema in `agent-lifecycle-manager/employment-spec-manager.md`
       - TrainingSpec schema in `trained-agent-lifecycle-manager/` (to be detailed)
   - **Integration Points and References**
     - Reference `cipher-iam-extensions/README.md` for IAM API details
     - Reference `implementation-concepts/agent-lifecycle.md` for delegation models
     - Reference `aosm-meta-model/raw-trained-employed-agents.md` for delegation model details
     - Reference `why-seer/part-2-how-seer-solves/03-identity-authority-in-seer/03-2-delegation-chains.md` for delegation chains
     - Reference `hub-integration/employment-spec-crd.md` for EmploymentSpec schema

### Phase 3: Authority Change Respawning (High Priority)

3. **Create `agent-runtime/authority-change-respawning.md`**

   - **Authority Change Detection Architecture**
     - **Seer Operator**: Only watches for changes to CRDs (EmploymentSpec, TrainingSpec)
     - **Agent Ecosystem Integration Services** (part of Agent Lifecycle Manager):
       - Suite of services operating with tenant-admin authority
       - **IAM Observer Service**: Listens to IAM changes and tracks if delegator roles/groups have changed
       - IAM Observer Service propagates changes to Employed Agent Specs by editing and publishing the corresponding CRDs
     - **Flow**:

       1. IAM Observer Service detects IAM changes (delegator roles/groups changed)
       2. IAM Observer Service edits EmploymentSpec CRD to reflect authority changes
       3. Seer Operator watches CRD and detects the change
       4. Seer Operator triggers respawning process

   - **Authority Change Sources**
     - Training Spec CRD updates (agent class authority changes)
     - Employment Spec CRD updates (agent instance authority changes)
       - Triggered by IAM Observer Service when delegator roles/groups change
       - Triggered by other Agent Ecosystem Integration Services for other changes
   - **Respawning Triggers**
     - Authority ceilings change (must respawn to apply new limits)
     - Delegation chain changes (delegator's authority shrinks) - detected via IAM Observer Service
     - OPA policy updates (affect runtime enforcement)
     - Kill switch deactivation (resume with new authority)
   - **Respawning Process**
     - Seer Operator detects EmploymentSpec CRD change
     - Graceful shutdown of existing pods (drain connections)
     - Update IAM profiles via Cipher IAM Extensions (if authority changed)
     - Redeploy with updated EmploymentSpec
     - Zero-downtime respawning (rolling update via Argo Rollouts)
     - Verification that new authority is active (health checks + policy validation)
   - **Integration Points**
     - Agent Lifecycle Manager (Agent Ecosystem Integration Services - IAM Observer Service)
     - Cipher IAM Extensions (authority changes detected by IAM Observer)
     - Seer Sidecar (policy enforcement updates)
   - **References**
     - `agent-lifecycle-manager/agent-ecosystem-integration-services.md` - IAM Observer Service
     - `agent-lifecycle-manager/README.md` - Agent Ecosystem Integration Services overview

### Phase 4: Signal Exchange Integration (Medium Priority)

4. **Create `agent-runtime/signal-exchange-integration.md`**

   - **SX Observer Service Architecture**
     - Runtime has `sx-observer` service that acts as an observer for Signal Exchange
     - **Signal Exchange Subscription Model**:
       - Signal Exchange does NOT accept subscriptions per scenario or per request
       - Seer sx-observer is an observer for the **workbench instance** (workbench-level subscription)
       - All request updates for the workbench are notified to sx-observer
     - **Architecture Separation**:
       - Signal Exchange is **unaware of Agent Ingress Gateway**
       - Signal Exchange only knows about sx-observer (the observer)
       - sx-observer is responsible for routing to Agent Ingress Gateway
   - **Store and Forward Capability**
     - sx-observer stores requests/updates before forwarding to agents
     - Enables reliable delivery even if agents are temporarily unavailable
     - Handles agent pod scale down to zero (requests stored until agents scale up)
     - Persistent storage for request queue (durable message queue)
     - **Implementation Details**: Common defaults or TBDs at detailed implementation stage
   - **Back-Pressure Handling**
     - sx-observer detects back-pressure from agents (slow processing, queue buildup)
     - Implements flow control to prevent overwhelming agents
     - Can throttle or pause dispatch when agents are overwhelmed
     - Signals back to Signal Exchange (if supported) to slow down delivery
     - **Implementation Details**: Common defaults or TBDs at detailed implementation stage
   - **Scale-to-Zero and Scale-Up**
     - sx-observer enables agent pod scale down to zero (no active pods)
     - When requests arrive and agents are scaled to zero:
       - sx-observer stores requests in queue
       - sx-observer triggers scale-up via Kubernetes HPA or custom scaling mechanism
       - Scale-up happens before dispatch (ensures agents are ready)
     - Signal Exchange can trigger scale-up before dispatch (via sx-observer)
     - Integration with Kubernetes Horizontal Pod Autoscaler (HPA) or custom scaling
     - **Implementation Details**: Common defaults or TBDs at detailed implementation stage
   - **Message Transport: Atropos**
     - Signal Exchange → sx-observer message routing happens through **Atropos** (event bus)
     - sx-observer → Agent Ingress Gateway → Agents routing also happens on **Atropos** (Response path)
     - Atropos provides pub-sub messaging for request updates and responses
     - Durable message delivery via Atropos
   - **Request Update Flow**
     - **Flow**: Signal Exchange → (Atropos) → sx-observer (store) → [scale-up if needed] → (Atropos) → Agent Ingress Gateway → Agents
     - Signal Exchange publishes request updates to Atropos (workbench-level topic)
     - sx-observer subscribes to Atropos and receives all request updates for the workbench
     - sx-observer stores requests/updates
     - sx-observer checks agent availability and triggers scale-up if needed
     - sx-observer filters relevant updates of relevant requests
     - sx-observer publishes filtered updates to Atropos (agent-specific topics)
     - Agent Ingress Gateway subscribes to Atropos and routes to deployed agent pods
   - **Filtering Logic**
     - sx-observer filters updates based on:
       - Which scenarios the updates belong to
       - Which agents are subscribed to those scenarios (from EmploymentSpec workScope.scenarios)
       - Request context and agent assignments
   - **Integration Points**
     - Signal Exchange (workbench-level observer registration - Signal Exchange only knows about sx-observer)
     - Agent Ingress Gateway (sx-observer dispatches to Agent Ingress Gateway)
     - Kubernetes HPA/Custom Scaling (sx-observer triggers scale-up)
     - EmploymentSpec (workScope.scenarios for filtering logic)
     - Reference Hub Signal Exchange documentation for observer pattern

5. **Create `agent-runtime/agent-ingress-gateway-integration.md`**

   - **Request Update Dispatch**
     - sx-observer dispatches filtered request updates to Employed Agents through Agent Ingress Gateway
     - Agent Ingress Gateway routes updates to deployed agent pods
     - Routing based on agent subscriptions (from EmploymentSpec workScope.scenarios)
     - Load balancing across agent pod replicas (via K8s Service)
     - **Note**: Signal Exchange is unaware of Agent Ingress Gateway - all routing is via sx-observer
   - **Request Routing (Initial Requests)**
     - Initial requests flow through sx-observer (which receives from Signal Exchange)
     - sx-observer routes to Agent Ingress Gateway
     - Agent Ingress Gateway routes to deployed agent pods
     - Load balancing across agent pod replicas (via K8s Service)
     - **Note**: All Signal Exchange communication goes through sx-observer - Signal Exchange is unaware of Agent Ingress Gateway
   - **SX Observer Service Lifecycle**
     - sx-observer registration during workbench instance setup
     - sx-observer updates when agents are deployed/retired (filtering logic updates)
     - sx-observer cleanup on workbench retirement
   - **Request Dispatch Integration**
     - Agent Ingress Gateway receives request updates from sx-observer via **Atropos** (subscribes to agent-specific topics)
     - **Note**: Signal Exchange is unaware of Agent Ingress Gateway - all communication goes through sx-observer
     - **Request Transformation**: No transformation by default - Atropos payload is dispatched as-is to agent with additional envelope details from sx-observer
     - **Optional Transformation**: Any transformation is optional and left to developer's requirements
     - **Response Handling**: Agents can directly update requests through agent APIs - SX need NOT forward any response from agent to Signal Exchange
   - **Response Path**
     - Agents update requests directly through agent APIs (not via sx-observer → Signal Exchange)
     - **Note**: Previous understanding updated - agents handle responses directly, not through sx-observer
   - **Load Balancing**
     - Load balancing details not required at this design stage
     - Implementation details to be determined during detailed design
   - **Agent Response Handling - External Resource References**
     - Agents can return references to external resources (files, images, large text streams, etc.)
     - Resources are stored in **Workbench Data Store** (Hub-provided Object and Stream store)
     - Agent responses include URIs to Workbench Data Store resources instead of inline content
     - Response format includes:
       - Resource references (URIs to Workbench Data Store)
       - Resource metadata (type, size, content-type)
       - Resource access information
     - Agent Ingress Gateway handles resource reference transformation
     - **Note**: Agents update requests directly through agent APIs, so sx-observer does not forward resource references to Signal Exchange
   - **Workbench Data Store Integration**
     - Hub provides Object and Stream store for workbench resources
     - Agents write large outputs (files, images, streams) to Workbench Data Store
     - Agents return URIs in responses instead of inline content
     - **Access Methods**: Stores can be accessed as tools, explicitly through SDK APIs, or through store service endpoints
     - **Resource Lifecycle**: Hub services manage resource cleanup
     - **References**: Refer to Hub documentation for stores and agent memory (retention policies, access permissions covered there)
     - **Implementation Details**: Further details to be determined during implementation
   - **Error Handling**
     - sx-observer maintains **Dead Letter Queue (DLQ)** in Atropos after configured retries
     - DLQ can be replayed
     - **Retry Configuration**: Retry thresholds configurable per employed agent, with defaults configured at Workbench Instance level
     - **Non-Retriable Failures**: Logged as Cronus Exception to the Workbench
     - **Agent Direct Updates**: Agents can directly update requests through agent APIs (no need for SX to forward responses)
   - **Observability**
     - Assume best practices for metrics, tracing, and logging
     - Implementation details to be determined during detailed design

### Phase 5: Ingress Path Configuration (Lower Priority)

6. **Enhance `agent-runtime/runtime-deployment.md`**

   - Add section: **Ingress Path Provisioning**
     - Seer Operator configures Heracles cluster-ingress path (not publicly accessible) as part of deployment
     - **Path Pattern**: `/seer/subscription/{subscription_id}/data-plane/workbench/{workbench_id}/agents/{agent_id}/dispatch`
     - Ingress paths created **per Employed Agent** (one data plane endpoint per agent)
     - Authentication/authorization at ingress:
       - Heracles sees the client as sx-observer
       - zone-auth is used to verify sx-observer credentials
       - Agents do NOT receive tokens that can be validated at ingress
       - Agents use their own token (from EmploymentSpec, Hub Environment, or Request Context)
       - Agents verify that message is dispatched by SX and belongs to their workbench
     - Rate limiting at ingress level (if applicable)
   - Add section: **Ingress Lifecycle**
     - Ingress creation: During deployment **after IAM profile creation/update**
     - Ingress updates: Seer Operator updates when agent configuration changes
     - Ingress cleanup: Seer Operator manages cleanup on agent retirement
   - Add section: **Integration with Heracles**
     - Heracles API Gateway configuration
     - TLS termination
     - Request routing rules
     - Cluster-ingress (internal, not publicly accessible)

### Phase 6: Documentation Updates

7. **Update `agent-runtime/SCOPE.md`**

   - Mark completed items as ✅
   - Update "Next Steps" section
   - Add references to new detailed design documents

8. **Update `agent-runtime/README.md`**

   - Update "Design Status" section with links to new documents
   - Update "Existing Content" section
   - Remove "Detailed design to be added" note

---

## File Structure

```




olympus-seer-docs/seer-design/subsystems/agent-runtime/
├── README.md (updated)
├── SCOPE.md (updated)
├── runtime-deployment.md (migrated from ../runtime-deployment.md)
├── iam-provisioning.md (NEW)
├── authority-change-respawning.md (NEW)
├── signal-exchange-integration.md (NEW)
├── agent-ingress-gateway-integration.md (NEW)
└── (runtime-deployment.md enhanced with ingress details)
```

---

## Dependencies

- **Cipher IAM Extensions**: Must understand IAM profile API
- **Agent Lifecycle Manager**: Delegation Chain Sync Service interface
- **Signal Exchange**: API for subscription management
- **Agent Ingress Gateway**: Integration patterns
- **Heracles**: Ingress configuration API

---

## Success Criteria

- All 5 open items have detailed design documents
- Integration points clearly documented with references
- Existing content preserved and properly organized
- Scope document updated to reflect completion
- README updated with new document links