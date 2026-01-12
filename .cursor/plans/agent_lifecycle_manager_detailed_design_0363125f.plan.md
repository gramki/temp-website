---
name: Agent Lifecycle Manager Detailed Design
overview: Create C2-level (Container) design documentation for all 5 sub-components of Agent Lifecycle Manager, focusing on functional scope, integration points, and hand-offs. Design at conceptual level without detailed data models or API specifications.
todos:
  - id: employment-spec-manager
    content: Create C2-level design for Employment Spec Manager covering functional scope (authority enforcement controls, resource quotas, fair usage budgets, delegation chain) and integration points
    status: completed
  - id: delegation-chain-sync
    content: Create C2-level design for Delegation Chain Sync Service covering functional scope (authority change detection, synchronization) and integration hand-offs
    status: completed
    dependencies:
      - employment-spec-manager
  - id: agent-levers-service
    content: Create C2-level design for Agent Levers Service covering functional scope (kill switches, authority enforcement actions) and integration hand-offs
    status: completed
    dependencies:
      - employment-spec-manager
  - id: employed-agent-directory
    content: Create C2-level design for Employed Agent Directory covering functional scope (agent profiles, accountability discovery, change log, dependency graph) and integration points
    status: completed
    dependencies:
      - employment-spec-manager
  - id: ecosystem-integration
    content: Create C2-level design for Agent Ecosystem Integration Services covering functional scope and integration hand-offs for all 10 integration points
    status: completed
    dependencies:
      - employment-spec-manager
      - delegation-chain-sync
      - agent-levers-service
  - id: create-scope-doc
    content: Create SCOPE.md document with coverage summary, design status, intended depth callout, "Implementation Details Deferred" section, and related documentation references
    status: completed
    dependencies:
      - employment-spec-manager
      - delegation-chain-sync
      - agent-levers-service
      - employed-agent-directory
      - ecosystem-integration
  - id: remove-old-content
    content: Remove "Existing Content" section (lines 61-66) from agent-lifecycle-manager/README.md that references agent-lifecycle-service.md and agent-lifecycle-api.md
    status: completed
  - id: update-readme
    content: Update agent-lifecycle-manager/README.md with links to all detailed design documents, remove old content references, update status to reflect design completion, add design documents table, and include "Key Design Decisions" section
    status: completed
    dependencies:
      - employment-spec-manager
      - delegation-chain-sync
      - agent-levers-service
      - employed-agent-directory
      - ecosystem-integration
      - create-scope-doc
      - remove-old-content
---

# Agent Lifecycle Manager Detailed Design Plan

## Objective

Create C2-level (Container) design documentation for the Agent Lifecycle Manager subsystem, covering all 5 sub-components with functional scope, integration points, and hand-offs. Design focuses on conceptual aspects and integration concerns without detailed data models or individual API specifications.

---

## Current State

- **Existing Structure**: 5 sub-component outline files with capability lists
- **Status**: Capability outlines complete; C2-level detailed design missing
- **Priority**: Employment Spec Manager (foundation) → Delegation Chain Sync → Levers → Directory → Ecosystem Integration
- **Design Level**: C2 (Container) in C4 architecture - focus on functional scope and integration concerns

---

## Implementation Plan

### Phase 1: Employment Spec Manager (Foundation)

**File**: `employment-spec-manager.md`

#### 1.1 Authority Enforcement Controls

- **Functional Scope**
- Authority ceiling architecture: Layered ceilings (Bank/Organization → Training Spec → Employment Spec → Request Context)
- Ceiling types: Value ceilings, Rate ceilings, Scope ceilings, Approval ceilings
- Ceiling immutability principle: Training ceilings cannot be relaxed at Employment
- Authority delegation models: User delegation vs Role delegation
- Delegation chain specification: Delegator identity, manager (accountable human), user-groups membership
- Authority inheritance rules: Agent authority always subset of delegator's current authority
- Bot mode: No delegator, base identity only, manager is accountable human
- OPA policy configuration: Policy references per PEP, file-based (not inline), unknown PEPs ignored

- **Integration Points and Hand-offs**
- **Cipher IAM Extensions**: Authority delegation configuration → IAM profile creation/updates
- **Seer Sidecar**: Authority ceilings → Runtime enforcement
- **Agent Runtime**: Employment Spec → IAM profile provisioning trigger
- **Delegation Chain Sync Service**: Authority changes → Employment Spec updates

#### 1.2 Resource Quota Management

- **Functional Scope**
- Quota types: Compute (CPU, memory, replicas), Token (daily/monthly budgets, per-request limits), API (rate limits per tool/service), Storage (memory store limits, conversation history)
- Quota specification: Employment Spec quota configuration
- Quota validation: Against Training Spec minimums, can only restrict not expand
- Quota enforcement: Runtime tracking, exhaustion handling (graceful degradation, escalation)

- **Integration Points and Hand-offs**
- **Agent Runtime**: Quota configuration → Resource allocation and enforcement
- **Seer Sidecar**: Quota limits → Runtime quota tracking
- **Agent Health Monitor**: Quota exhaustion → Health alerts

#### 1.3 Fair Usage Budget

- **Functional Scope**
- Budget dimensions: Per Subject (customer, account), Per Signal (request type, scenario), Per Time Period (hourly, daily, weekly, monthly), Per Action Type (tool, API endpoint)
- Budget configuration: Employment Spec budget specification, aggregation rules, reset policies
- Budget tracking and enforcement: Real-time consumption tracking, exhaustion policies (reject, escalate, throttle)

- **Integration Points and Hand-offs**
- **Seer Sidecar**: Budget limits → Runtime budget tracking and enforcement
- **Agent Health Monitor**: Budget exhaustion → Health alerts and reporting

#### 1.4 Delegation Chain Configuration

- **Functional Scope**
- Delegation chain specification: Chain structure (Delegator → Agent → optional sub-agents), depth limits, validation (authority narrowing, no cycles)
- Delegation chain metadata: Delegator identity, authority snapshot, timestamp, expiration (if time-bounded), scope (workbench, scenarios, customers), approval workflow state

- **Integration Points and Hand-offs**
- **Delegation Chain Sync Service**: Chain change detection → Authority synchronization
- **Employed Agent Directory**: Chain metadata → Accountability discovery

---

### Phase 2: Delegation Chain Sync Service

**File**: `delegation-chain-sync-service.md`

#### 2.1 Authority Change Detection

- **Functional Scope**
- IAM Observer Service integration: Listens to IAM changes, tracks delegator roles/groups changes
- Authority change detection at multiple levels: Bank/Organization policy changes, Agent Class (Training Spec) changes, Agent Instance (Employment Spec) changes, Delegator authority changes (human authority shrinks)
- Change detection mechanisms: IAM event subscriptions, policy update notifications, periodic reconciliation (if needed)

- **Integration Points and Hand-offs**
- **Agent Ecosystem Integration Services (IAM Observer)**: IAM changes → Authority change detection
- **Employment Spec Manager**: Detected changes → Employment Spec updates

#### 2.2 Authority Synchronization Flow

- **Functional Scope**
- Synchronization process: IAM Observer detects changes → Identifies affected agents → Updates EmploymentSpec CRD → Seer Operator detects change → Triggers respawning
- Authority inheritance updates: Calculate new agent authority (subset of delegator), update IAM profile, update Employment Spec ceilings, validate authority narrowing
- Delegation chain validation: Verify chain integrity, check authority violations, validate depth limits

- **Integration Points and Hand-offs**
- **Agent Ecosystem Integration Services (IAM Observer)**: IAM changes → EmploymentSpec CRD updates
- **Agent Runtime**: EmploymentSpec changes → Agent respawning trigger
- **Cipher IAM Extensions**: Authority updates → IAM profile updates
- **Employment Spec Manager**: Authority changes → Employment Spec configuration updates

---

### Phase 3: Agent Levers Service

**File**: `agent-levers-service.md`

#### 3.1 Kill Switch Mechanisms

- **Functional Scope**
- Kill switch actions: Suspend (retains authority, stops execution), Revoke (permanently removes authority), Bulk operations (by filter: training spec, tenant, workbench, scenario)
- Kill switch triggers: Manual (security team, supervisor), Automated (anomaly detection, policy violations), Emergency (platform-wide incidents)
- Kill switch execution: IAM profile revocation (for revoke), runtime scale-to-zero or network isolation, Employment Spec state update, event propagation

- **Integration Points and Hand-offs**
- **Agent Runtime**: Kill switch command → Scale-to-zero or network isolation
- **Cipher IAM Extensions**: Revoke action → IAM profile revocation
- **Employment Spec Manager**: Kill switch → Employment Spec state update
- **Agent Ecosystem Integration Services**: Kill switch events → Ecosystem notification

#### 3.2 Authority Enforcement Actions

- **Functional Scope**
- Enforcement action types: Authority ceiling reduction, tool access revocation, scenario access revocation, approval requirement escalation
- Enforcement action execution: Update Employment Spec constraints, trigger agent respawning, update IAM profile, propagate to runtime enforcement points

- **Integration Points and Hand-offs**
- **Employment Spec Manager**: Enforcement actions → Employment Spec constraint updates
- **Agent Runtime**: Constraint updates → Agent respawning trigger
- **Cipher IAM Extensions**: Authority changes → IAM profile updates
- **Seer Sidecar**: Authority constraints → Runtime enforcement point updates

---

### Phase 4: Employed Agent Directory

**File**: `employed-agent-directory.md`

#### 4.1 Agent Profile

- **Functional Scope**
- Core profile information: Agent identity (Employment Spec ID, name, namespace, versions), work scope (workbench, scenarios, temporal/functional scope), authority (delegation model, ceilings, OPA policies), resources (quotas, budgets, capacity)
- System prompts and configuration: Goals, Skills, Behaviors (from Training Spec), External Guardrails, Context Compiler DSL, Tools and Resources
- Derived information: Derived Skills/Capabilities (inferred from Training Spec), Skill Labels/Tags, Capability matrix

- **Integration Points and Hand-offs**
- **Employment Spec Manager**: Employment Spec → Profile core information
- **Training Management**: Training Spec → System prompts and derived capabilities
- **Agent Runtime**: Runtime state → Profile status

#### 4.2 Accountability Discovery

- **Functional Scope**
- Accountability relationships: Manager (Accountable human from delegation.accountable), Delegator (from delegation chain), Human Responsibility Span (all humans accountable)
- Accountability graph: Upward chain (Agent → Manager → Delegator), Downward chain (Agent → Sub-agents), Cross-agent relationships (same workbench, scenarios)

- **Integration Points and Hand-offs**
- **Employment Spec Manager**: Delegation chain → Accountability relationships
- **Delegation Chain Sync Service**: Chain updates → Accountability graph updates

#### 4.3 Agent Change Log

- **Functional Scope**
- Change log entries: Employment Spec changes (version, state transitions), Authority changes (ceiling updates, delegation changes), Enforcement actions (kill switches, authority enforcement), Resource quota changes, Work scope changes
- Change log structure: Timestamp, actor, change type, before/after state, change reason/approval, related resources

- **Integration Points and Hand-offs**
- **Employment Spec Manager**: Spec changes → Change log entries
- **Delegation Chain Sync Service**: Authority changes → Change log entries
- **Agent Levers Service**: Enforcement actions → Change log entries

#### 4.4 Agent Dependency Graph

- **Functional Scope**
- Dependency types: Agent-to-Agent (delegation chains, collaboration), Agent-to-Scenario (scenario participation), Agent-to-Tool (tool bindings), Agent-to-Resource (memory stores, knowledge bases)
- Dependency graph construction: Parse Employment Specs for explicit dependencies, infer from work scope, track runtime dependencies
- Dependency graph queries: Find agents by scenario, find delegation chains, find shared resources, impact analysis

- **Integration Points and Hand-offs**
- **Employment Spec Manager**: Employment Specs → Dependency graph construction
- **Agent Runtime**: Runtime interactions → Runtime dependency tracking
- **Signal Exchange**: Scenario subscriptions → Agent-to-Scenario dependencies

---

### Phase 5: Agent Ecosystem Integration Services

**File**: `agent-ecosystem-integration-services.md`

#### 5.1 Integration Architecture

- **Functional Scope**
- Integration pattern: Suite of services operating with tenant-admin authority
- Event-driven integration: Subscribe to events, propagate changes
- Bidirectional integration: Receive events, send updates

- **Integration Points and Hand-offs**
- All integration services follow same pattern: Event subscription → Change detection → Employment Spec updates → Ecosystem notification

#### 5.2 IAM Changes Integration

- **Functional Scope**
- IAM Observer Service: Listens to IAM changes (delegator roles/groups), propagates to Employment Specs, triggers delegation chain synchronization

- **Integration Points and Hand-offs**
- **Cipher IAM**: IAM changes → IAM Observer Service
- **Delegation Chain Sync Service**: IAM Observer → Authority synchronization
- **Employment Spec Manager**: IAM changes → Employment Spec updates

#### 5.3 Subscription Policy Changes Integration

- **Functional Scope**
- Receive subscription policy changes from Hub, update agent work scope if scenarios affected, propagate to agent runtime

- **Integration Points and Hand-offs**
- **Hub Subscription Service**: Policy changes → Agent Ecosystem Integration Services
- **Employment Spec Manager**: Policy changes → Work scope updates
- **Agent Runtime**: Work scope changes → Runtime updates

#### 5.4 Workbench Policy Changes Integration

- **Functional Scope**
- Receive workbench policy changes (authority ceilings, tool access), update affected Employment Specs, trigger authority re-evaluation

- **Integration Points and Hand-offs**
- **Hub Workbench Service**: Policy changes → Agent Ecosystem Integration Services
- **Employment Spec Manager**: Policy changes → Employment Spec updates
- **Delegation Chain Sync Service**: Policy changes → Authority re-evaluation

#### 5.5 Agent Lifecycle Changes Integration

- **Functional Scope**
- Lifecycle event propagation: Employment activation → notify Tools Gateway, Signal Exchange; Suspension/revocation → notify all ecosystem services; Authority changes → notify runtime, IAM, enforcement points

- **Integration Points and Hand-offs**
- **Employment Spec Manager**: Lifecycle changes → Agent Ecosystem Integration Services
- **Tools Gateway**: Activation events → Tool binding updates
- **Signal Exchange**: Activation events → Scenario subscription registration
- **Agent Runtime**: Lifecycle changes → Runtime state updates

#### 5.6 Agent Health Actions Integration

- **Functional Scope**
- Receive health alerts from Agent Health Monitor, trigger kill switches for critical issues, update agent state based on health status

- **Integration Points and Hand-offs**
- **Agent Health Monitor**: Health alerts → Agent Ecosystem Integration Services
- **Agent Levers Service**: Critical health issues → Kill switch triggers
- **Employment Spec Manager**: Health status → Agent state updates

#### 5.7 Platform SRE Directives Integration

- **Functional Scope**
- Receive platform-wide directives (maintenance, incidents), execute bulk operations (suspend agents, reduce quotas), coordinate with Agent Levers Service

- **Integration Points and Hand-offs**
- **Platform SRE**: Directives → Agent Ecosystem Integration Services
- **Agent Levers Service**: SRE directives → Bulk kill switch operations
- **Employment Spec Manager**: SRE directives → Quota reductions

#### 5.8 Tools Gateway Integration

- **Functional Scope**
- Notify Tools Gateway of agent tool bindings, update tool access when authority changes, handle tool revocation during kill switches

- **Integration Points and Hand-offs**
- **Employment Spec Manager**: Tool bindings → Tools Gateway notification
- **Agent Levers Service**: Kill switches → Tool revocation
- **Tools Gateway**: Tool access updates → Runtime tool access enforcement

#### 5.9 Signal Exchange Integration

- **Functional Scope**
- Register agent scenario subscriptions, update subscriptions when work scope changes, unregister on agent revocation

- **Integration Points and Hand-offs**
- **Employment Spec Manager**: Work scope → Scenario subscription registration
- **Agent Levers Service**: Agent revocation → Subscription unregistration
- **Signal Exchange**: Subscription updates → Request routing updates

#### 5.10 Training Management Integration

- **Functional Scope**
- Receive Training Spec changes (new versions, archived), update Employment Spec references, trigger re-validation if authority affected

- **Integration Points and Hand-offs**
- **Training Management**: Training Spec changes → Agent Ecosystem Integration Services
- **Employment Spec Manager**: Training Spec changes → Employment Spec reference updates
- **Delegation Chain Sync Service**: Authority-affecting changes → Re-validation triggers

---

## Design Artifacts

### Document Structure

- **Separate sub-files**: Each sub-component gets its own markdown file (following agent-runtime pattern)
- `employment-spec-manager.md`
- `delegation-chain-sync-service.md`
- `agent-levers-service.md`
- `employed-agent-directory.md`
- `agent-ecosystem-integration-services.md`
- **SCOPE.md**: Summary document with coverage status, intended depth callout, and "Implementation Details Deferred" section
- **README.md**: Updated with links to all design documents, removed old content references, and "Key Design Decisions" section
- **Structure flexibility**: Document structure can vary by component nature, but keep consistent for similar components

### Conceptual Models

- Employment Spec conceptual structure (authority, quotas, budgets, delegation chain)
- Authority ceiling architecture (layered ceilings, types, immutability)
- Delegation chain structure (chain relationships, inheritance rules)
- Agent profile structure (core info, system prompts, derived capabilities)
- Dependency graph structure (dependency types, relationships)
- **Complete illustrative YAML/JSON examples**: Include complete illustrative examples (like in `iam-provisioning.md`) to clarify concepts - not minimal snippets

### Integration Diagrams (C2 Level)

- **Mermaid diagrams**: Use mermaid for all diagrams (component interactions, event flows, sequences)
- Component interaction diagrams showing containers and their relationships
- Event flow diagrams for key operations (authority sync, kill switch, lifecycle events)
- Sequence diagrams for hand-offs between containers
- Integration point diagrams showing external system connections

### Operational Flows

- Employment Spec creation and validation flow (conceptual steps, hand-offs)
- Authority change detection and synchronization flow (event flow, container interactions)
- Kill switch execution flow (trigger → execution → propagation)
- Agent profile update flow (change sources → directory updates)
- Ecosystem event propagation flow (event sources → integration services → updates)

### Integration Patterns

- **CRD-based**: All control plane changes use CRD updates (EmploymentSpec, TrainingSpec)
- **Event-driven**: Data plane operations use event-driven patterns (Atropos, Signal Exchange)
- **Observer patterns**: Where applicable (IAM Observer Service, Signal Exchange observer pattern)

---

## Dependencies

- **Cipher IAM Extensions**: Authority delegation, IAM profile management
- **Agent Runtime**: Deployment, respawning, kill switch execution
- **Seer Sidecar**: Runtime enforcement
- **Tools Gateway**: Tool binding management
- **Signal Exchange**: Scenario subscription management
- **Agent Health Monitor**: Health status
- **Training Management**: Training Spec lifecycle

---

## Success Criteria

- All 5 sub-components have C2-level design documentation
- Functional scope clearly defined for each sub-component
- Integration points and hand-offs documented
- Conceptual models and operational flows documented
- Integration diagrams at C2 (Container) level
- Cross-references to related subsystems established
- Outdated content removed and references updated

---

## Document Structure and Standards

### File Organization

- **Separate sub-files**: Each of the 5 sub-components gets its own markdown file
- **SCOPE.md**: Summary document with coverage status and intended depth callout
- **README.md**: Updated with design documents table and links

### Design Standards

- **C2 (Container) level**: Focus on functional scope and integration concerns (not detailed data models or APIs)
- **Mermaid diagrams**: All diagrams use mermaid syntax (component interactions, event flows, sequences)
- **Conceptual examples**: Include YAML/JSON examples to illustrate concepts (like in `iam-provisioning.md`)
- **Integration patterns**:
- **CRD-based**: All control plane changes use CRD updates (EmploymentSpec, TrainingSpec)
- **Event-driven**: Data plane operations use event-driven patterns (Atropos, Signal Exchange)
- **Observer patterns**: Where applicable (IAM Observer Service, Signal Exchange observer)

### Intended Depth

- Functional scope clearly defined for each sub-component
- Integration points and hand-offs documented with container-level detail
- Conceptual models and operational flows documented
- Integration diagrams at C2 (Container) level
- Cross-references to related subsystems established
- **No detailed data models or individual API specifications** - keep at conceptual level

### Content Cleanup

- Remove "Existing Content" section from README.md (references to `agent-lifecycle-service.md` and `agent-lifecycle-api.md`)
- Update all references to point to new design documents
- Follow same depth and structure as `agent-runtime/SCOPE.md` for consistency

### Cross-References

- **Infer from codebase**: Cross-references to related subsystems and documentation should be inferred from existing codebase patterns
- Include references to related subsystems, implementation concepts, and Hub documentation as appropriate

### Document Structure Guidelines

- **Structure flexibility**: Document structure can vary by component nature, but keep consistent for similar components
- **Key Design Decisions**: Keep in README.md only (not in individual sub-component documents)
- **Complete examples**: Use complete illustrative YAML/JSON examples (not minimal snippets) to clarify concepts

### Notes

- Employment Spec and Training Spec schemas will evolve - enhance in respective subsystem documents
- Design documents should be detailed enough to convey conceptual aspects, integration points, and hand-offs