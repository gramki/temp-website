---
name: Model Gateway Ingress Gateway IAM Extensions Design
overview: Create C2-level design specifications for model-gateway, agent-ingress-gateway, and cipher-iam-extensions subsystems, with C3-level detail for critical enforcement/authorization mechanisms. Migrate and enhance existing Model Gateway content, create fresh designs for Ingress Gateway and IAM Extensions.
todos:
  - id: model-gateway-readme
    content: Update model-gateway/README.md with architecture overview, design status, and links to detailed documents
    status: completed
  - id: model-gateway-architecture
    content: Create model-gateway/architecture.md with deployment model, Bifrost integration, component architecture (C2)
    status: completed
    dependencies:
      - model-gateway-readme
  - id: model-gateway-catalog
    content: Create model-gateway/model-catalog.md with provider configuration, model selection hierarchy, whitelist enforcement (C2)
    status: completed
    dependencies:
      - model-gateway-architecture
  - id: model-gateway-routing
    content: Create model-gateway/routing-fallback.md with fallback strategies and C3 detail for fallback algorithms, circuit breakers
    status: completed
    dependencies:
      - model-gateway-catalog
  - id: model-gateway-governance
    content: Create model-gateway/governance.md with budget enforcement and C3 detail for budget tracking algorithms, quota enforcement
    status: completed
    dependencies:
      - model-gateway-routing
  - id: model-gateway-policy
    content: Create model-gateway/policy-enforcement.md with OPA integration and C3 detail for policy evaluation flow, PEP integration
    status: completed
    dependencies:
      - model-gateway-governance
  - id: model-gateway-observability
    content: Create model-gateway/observability.md with metrics, logging, Watch integration (C2)
    status: completed
    dependencies:
      - model-gateway-policy
  - id: model-gateway-access
    content: Create model-gateway/agent-access.md with OpenAI-compatible API, endpoint discovery, authentication (C2)
    status: completed
    dependencies:
      - model-gateway-observability
  - id: model-gateway-scope
    content: Create model-gateway/SCOPE.md with coverage summary, design status, intended depth callout
    status: completed
    dependencies:
      - model-gateway-access
  - id: ingress-gateway-readme
    content: Update agent-ingress-gateway/README.md with Heracles configuration layer overview and architecture
    status: completed
  - id: ingress-gateway-architecture
    content: Create agent-ingress-gateway/architecture.md with Heracles relationship, sx-observer integration, request flow (C2)
    status: completed
    dependencies:
      - ingress-gateway-readme
  - id: ingress-gateway-lifecycle
    content: Create agent-ingress-gateway/subscription-lifecycle.md with subscription management and C3 detail for state machine
    status: completed
    dependencies:
      - ingress-gateway-architecture
  - id: ingress-gateway-routing
    content: Create agent-ingress-gateway/request-routing.md with routing logic and C3 detail for filtering algorithms, load balancing
    status: completed
    dependencies:
      - ingress-gateway-lifecycle
  - id: ingress-gateway-policies
    content: Create agent-ingress-gateway/subscription-policies.md with subscription-scoped policies and C3 detail for policy evaluation
    status: completed
    dependencies:
      - ingress-gateway-routing
  - id: ingress-gateway-heracles
    content: Create agent-ingress-gateway/heracles-integration.md with cluster-ingress configuration, authentication, TLS (C2)
    status: completed
    dependencies:
      - ingress-gateway-policies
  - id: ingress-gateway-response
    content: Create agent-ingress-gateway/response-handling.md with agent direct updates, Workbench Data Store integration (C2)
    status: completed
    dependencies:
      - ingress-gateway-heracles
  - id: ingress-gateway-sx
    content: Create agent-ingress-gateway/signal-exchange-integration.md with sx-observer integration, Atropos topics, filtering (C2)
    status: completed
    dependencies:
      - ingress-gateway-response
  - id: ingress-gateway-scope
    content: Create agent-ingress-gateway/SCOPE.md with coverage summary, design status, intended depth callout
    status: completed
    dependencies:
      - ingress-gateway-sx
  - id: iam-extensions-readme
    content: Update cipher-iam-extensions/README.md with extensions overview, API + internal implementation scope
    status: completed
  - id: iam-extensions-architecture
    content: Create cipher-iam-extensions/architecture.md with Hub Cipher IAM relationship, agent identity types, SPIFFE (C2)
    status: completed
    dependencies:
      - iam-extensions-readme
  - id: iam-extensions-api
    content: Create cipher-iam-extensions/agent-profile-api.md with API specification, endpoints, schemas, error handling (C3)
    status: completed
    dependencies:
      - iam-extensions-architecture
  - id: iam-extensions-delegation
    content: Create cipher-iam-extensions/authority-delegation.md with delegation model and C3 detail for inheritance algorithms
    status: completed
    dependencies:
      - iam-extensions-api
  - id: iam-extensions-tags
    content: Create cipher-iam-extensions/profile-tags.md with Raw/Trained/Employed agent profile tags (C2)
    status: completed
    dependencies:
      - iam-extensions-delegation
  - id: iam-extensions-accountability
    content: Create cipher-iam-extensions/human-accountability.md with accountable human assignment, audit trail (C2)
    status: completed
    dependencies:
      - iam-extensions-tags
  - id: iam-extensions-pep
    content: Create cipher-iam-extensions/policy-enforcement-points.md with PEP registration and C3 detail for policy evaluation flow
    status: completed
    dependencies:
      - iam-extensions-accountability
  - id: iam-extensions-credentials
    content: Create cipher-iam-extensions/credential-management.md with credential issuance, injection, virtual keys (C2)
    status: completed
    dependencies:
      - iam-extensions-pep
  - id: iam-extensions-internal
    content: Create cipher-iam-extensions/internal-implementation.md with internal Cipher extensions, profile storage, policy attachment (C2)
    status: completed
    dependencies:
      - iam-extensions-credentials
  - id: iam-extensions-integration
    content: Create cipher-iam-extensions/integration-patterns.md with Seer Operator, Agent Runtime, PEP integration patterns (C2)
    status: completed
    dependencies:
      - iam-extensions-internal
  - id: iam-extensions-scope
    content: Create cipher-iam-extensions/SCOPE.md with coverage summary, design status, intended depth callout
    status: completed
    dependencies:
      - iam-extensions-integration
  - id: adr-ingress-gateway-heracles
    content: Create ADR for Agent Ingress Gateway as Heracles configuration layer (decision log entry in olympus-hub-docs/decision-logs/)
    status: completed
    dependencies:
      - ingress-gateway-scope
  - id: adr-iam-extensions-agent-profiles
    content: Create ADR for Cipher IAM Extensions agent profile architecture (decision log entry in olympus-hub-docs/decision-logs/)
    status: completed
    dependencies:
      - iam-extensions-scope
  - id: adr-model-gateway-budget-enforcement
    content: Create or update ADR for Model Gateway budget enforcement approach (workbench and agent levels, virtual keys)
    status: completed
    dependencies:
      - model-gateway-scope
  - id: update-authority-enforcement-concept
    content: Update implementation-concepts/authority-enforcement.md with Cipher IAM Extensions integration details and PEP policy model
    status: completed
    dependencies:
      - iam-extensions-pep
      - adr-iam-extensions-agent-profiles
  - id: update-agent-lifecycle-concept
    content: Update implementation-concepts/agent-lifecycle.md with IAM Extensions integration, agent profile lifecycle, and credential management
    status: completed
    dependencies:
      - iam-extensions-integration
      - adr-iam-extensions-agent-profiles
---

# Model Gateway, Ingress Gateway, and IAM Extensions Design Specifications

## Objective

Create comprehensive C2-level (Container) design documentation for three Seer subsystems:

1. **Model Gateway** - Migrate and enhance existing content
2. **Agent Ingress Gateway** - Fresh design as Heracles configuration layer
3. **Cipher IAM Extensions** - Fresh design covering both API surface and internal implementation

All designs at C2 detail with C3-level depth for critical enforcement/authorization mechanisms.

---

## Design Standards

### Detail Levels

- **C2 (Container)**: Functional scope, integration points, hand-offs, architectural patterns
- **C3 (Component)**: Critical enforcement mechanisms, state machines, complex algorithms, detailed API specifications

### Critical C3 Areas (All Modules)

- Policy enforcement mechanisms
- Authorization algorithms
- State machines for lifecycle management
- Budget/quota enforcement algorithms
- Request routing logic (where applicable)

---

## Module 1: Model Gateway

### Source Material

- Existing: `olympus-seer-docs/seer-design/subsystems/model-gateway.md` (484 lines)
- Target: `olympus-seer-docs/seer-design/subsystems/model-gateway/` folder structure

### Design Structure

1. **README.md** (Update)

   - Overview, capabilities, architecture diagram
   - Links to detailed design documents
   - Design status and related documentation

2. **architecture.md** (C2)

   - Deployment model (platform-level, shared instance)
   - Bifrost integration and customizations
   - Component architecture (authentication, routing, observability)
   - Integration with Cipher IAM, OPA, Olympus Watch

3. **model-catalog.md** (C2)

   - Provider configuration (tenant-admin managed)
   - Model selection hierarchy (Raw → Training → Employment Spec)
   - Custom model support (out of scope but acknowledge)
   - Model whitelist enforcement

4. **routing-fallback.md** (C2 with C3 for fallback algorithms)

   - Fallback configuration (tenant-admin configured)
   - Fallback strategies (priority, round-robin, cost-optimized)
   - **C3 Detail**: Fallback trigger logic, circuit breaker algorithms, timeout handling
   - Routing behavior matrix

5. **governance.md** (C2 with C3 for budget enforcement)

   - Budget enforcement (workbench and agent levels)
   - Virtual key management per Employed Agent
   - **C3 Detail**: Budget tracking algorithms, quota enforcement mechanisms, alert thresholds
   - Budget configuration and overrides

6. **policy-enforcement.md** (C3)

   - OPA policy integration
   - **C3 Detail**: Policy evaluation flow, PEP integration, violation handling
   - Model access control policies
   - Rate limiting policies
   - Policy configuration per PEP

7. **observability.md** (C2)

   - Metrics (Prometheus format)
   - Watch integration
   - Logging (operational logs, not CAF)
   - Cost tracking and attribution

8. **agent-access.md** (C2)

   - OpenAI-compatible API
   - Endpoint discovery (environment variables)
   - Virtual key injection
   - Authentication flow

9. **SCOPE.md** (New)

   - Coverage summary
   - Design status
   - Intended depth callout
   - Related documentation references

### Migration Strategy

- Preserve all existing content from `model-gateway.md`
- Reorganize into logical sub-documents
- Enhance with C3 detail for critical mechanisms
- Add missing integration details
- Update cross-references

---

## Module 2: Agent Ingress Gateway

### Source Material

- Existing: `olympus-seer-docs/seer-design/subsystems/agent-ingress-gateway/README.md` (capability outline only)
- Reference: `olympus-seer-docs/seer-design/subsystems/agent-runtime/agent-ingress-gateway-integration.md`
- Reference: `olympus-hub-docs/05-infrastructure/heracles-gateway.md`

### Design Structure

1. **README.md** (Update)

   - Overview: Heracles configuration layer for agent request routing
   - Architecture: Configuration-based gateway, not separate service
   - Links to detailed design documents

2. **architecture.md** (C2)

   - Relationship with Heracles (configuration layer, not separate service)
   - Integration with sx-observer (Atropos subscription)
   - Request flow: sx-observer → Agent Ingress Gateway (Heracles config) → Agent pods
   - Load balancing via Kubernetes Service

3. **subscription-lifecycle.md** (C2 with C3 for state machine)

   - Subscription creation (workbench instance setup)
   - Subscription updates (agent deployment/retirement)
   - Subscription cleanup (workbench retirement)
   - **C3 Detail**: Subscription state machine, transition logic

4. **request-routing.md** (C2 with C3 for routing logic)

   - Routing from sx-observer (Atropos topics)
   - Agent subscription matching (from EmploymentSpec workScope.scenarios)
   - **C3 Detail**: Request filtering algorithm, scenario-to-agent mapping, load balancing strategy
   - Request transformation (default: pass-through, optional: custom)

5. **subscription-policies.md** (C2 with C3 for policy evaluation)

   - Subscription-scoped policy configuration
   - Policy enforcement points
   - **C3 Detail**: Policy evaluation flow, policy precedence, violation handling
   - Integration with Cipher IAM for authorization

6. **heracles-integration.md** (C2)

   - Heracles cluster-ingress configuration
   - Ingress path provisioning (`/seer/subscription/{subscription_id}/data-plane/workbench/{workbench_id}/agents/{agent_id}/dispatch`)
   - Authentication at ingress (zone-auth for sx-observer)
   - TLS termination, rate limiting

7. **response-handling.md** (C2)

   - Agent direct API updates (not via sx-observer)
   - Workbench Data Store integration (resource references)
   - Response transformation (resource URI injection)
   - Error handling and DLQ

8. **signal-exchange-integration.md** (C2)

   - Integration via sx-observer (Signal Exchange unaware of Agent Ingress Gateway)
   - Atropos topic subscription model
   - Request update dispatch flow
   - Filtering logic (scenario-based, agent subscription-based)

9. **SCOPE.md** (New)

   - Coverage summary
   - Design status
   - Intended depth callout
   - Related documentation references

### Key Design Decisions

- Agent Ingress Gateway is **configuration on Heracles**, not a separate service
- All Signal Exchange communication goes through sx-observer
- Agents update requests directly via agent APIs (not through gateway)

---

## Module 3: Cipher IAM Extensions

### Source Material

- Existing: `olympus-seer-docs/seer-design/subsystems/cipher-iam-extensions/README.md` (capability outline only)
- Reference: `olympus-seer-docs/seer-design/subsystems/agent-runtime/iam-provisioning.md` (Seer Operator perspective)
- Reference: `olympus-seer-docs/why-seer/part-2-how-seer-solves/03-identity-authority-in-seer/03-5-cipher-iam-integration.md`

### Design Structure

1. **README.md** (Update)

   - Overview: Extensions to Hub Cipher IAM for agent identity and authority
   - Architecture: API surface + internal implementation
   - Links to detailed design documents

2. **architecture.md** (C2)

   - Relationship with Hub Cipher IAM (extensions, not replacement)
   - Agent identity types (Raw, Trained, Employed)
   - SPIFFE integration for agent identity
   - Division of responsibilities (Seer defines semantics, Cipher provides infrastructure)

3. **agent-profile-api.md** (C3)

   - **API Specification**: Profile creation, update, deletion
   - **C3 Detail**: API endpoints, request/response schemas, error handling
   - Profile lifecycle operations
   - Integration with Seer Operator (from iam-provisioning.md perspective)

4. **authority-delegation.md** (C2 with C3 for delegation algorithms)

   - Delegation model (user delegation, role delegation, bot mode)
   - Delegation chain representation
   - **C3 Detail**: Authority inheritance algorithms, role/group subset logic, wildcard handling
   - Delegation validation and constraints

5. **profile-tags.md** (C2)

   - Raw Agent profile tags
   - Trained Agent profile tags
   - Employed Agent profile tags
   - Tag lifecycle and updates

6. **human-accountability.md** (C2)

   - Accountable human assignment
   - Accountability chain
   - Manager relationship
   - Audit trail for accountability

7. **policy-enforcement-points.md** (C2 with C3 for policy evaluation)

   - PEP registration with Cipher IAM
   - Policy attachment per PEP (tool-gateway, signal-exchange, model-gateway, memory-service, knowledge-service)
   - **C3 Detail**: Policy evaluation flow, PEP routing, policy precedence
   - Unknown PEP handling

8. **credential-management.md** (C2)

   - Credential issuance (bot tokens, service accounts)
   - Credential injection via zone-vault
   - Virtual key management (for Model Gateway)
   - Credential rotation and lifecycle

9. **internal-implementation.md** (C2)

   - Internal Cipher extensions for agent support
   - Profile storage and retrieval
   - Authority delegation storage
   - Policy attachment mechanisms
   - Integration with Cipher core IAM

10. **integration-patterns.md** (C2)

    - Seer Operator integration (profile provisioning)
    - Agent Runtime integration (credential injection)
    - PEP integration (policy enforcement)
    - Audit logging integration

11. **SCOPE.md** (New)

    - Coverage summary
    - Design status
    - Intended depth callout
    - Related documentation references

### Key Design Decisions

- Covers both **API surface** (what Seer calls) and **internal implementation** (how Cipher supports agents)
- Agent profiles extend standard Cipher IAM profiles
- Policies are per-PEP, referenced files (not inline)
- Unknown PEPs are ignored (graceful degradation)

---

## File Structure

```
olympus-seer-docs/seer-design/subsystems/
├── model-gateway/
│   ├── README.md (updated)
│   ├── SCOPE.md (new)
│   ├── architecture.md (new)
│   ├── model-catalog.md (new)
│   ├── routing-fallback.md (new, C3 for algorithms)
│   ├── governance.md (new, C3 for budget enforcement)
│   ├── policy-enforcement.md (new, C3)
│   ├── observability.md (new)
│   └── agent-access.md (new)
│
├── agent-ingress-gateway/
│   ├── README.md (updated)
│   ├── SCOPE.md (new)
│   ├── architecture.md (new)
│   ├── subscription-lifecycle.md (new, C3 for state machine)
│   ├── request-routing.md (new, C3 for routing logic)
│   ├── subscription-policies.md (new, C3 for policy evaluation)
│   ├── heracles-integration.md (new)
│   ├── response-handling.md (new)
│   └── signal-exchange-integration.md (new)
│
└── cipher-iam-extensions/
    ├── README.md (updated)
    ├── SCOPE.md (new)
    ├── architecture.md (new)
    ├── agent-profile-api.md (new, C3)
    ├── authority-delegation.md (new, C3 for algorithms)
    ├── profile-tags.md (new)
    ├── human-accountability.md (new)
    ├── policy-enforcement-points.md (new, C3 for evaluation)
    ├── credential-management.md (new)
    ├── internal-implementation.md (new)
    └── integration-patterns.md (new)
```

---

## Dependencies

- **Model Gateway**: Bifrost OSS, Cipher IAM, OPA, Olympus Watch
- **Agent Ingress Gateway**: Heracles, sx-observer, Atropos, Agent Runtime
- **Cipher IAM Extensions**: Hub Cipher IAM, Seer Operator, Agent Runtime, PEPs

---

## Decision Logs (ADRs)

Significant architectural decisions will be documented as Architecture Decision Records:

1. **ADR: Agent Ingress Gateway as Heracles Configuration Layer**

   - Decision: Agent Ingress Gateway is configuration on Heracles, not a separate service
   - Context: Need to clarify architecture separation from Signal Exchange and sx-observer
   - Location: `olympus-hub-docs/decision-logs/0105-seer-agent-ingress-gateway-heracles-config.md` (or next available number)

2. **ADR: Cipher IAM Extensions Agent Profile Architecture**

   - Decision: Agent profiles extend Hub Cipher IAM with agent-specific identity and authority semantics
   - Context: Division of responsibilities between Seer (semantics) and Cipher (infrastructure)
   - Location: `olympus-hub-docs/decision-logs/0106-seer-cipher-iam-extensions-agent-profiles.md` (or next available number)

3. **ADR: Model Gateway Budget Enforcement Approach** (Update or new)

   - Decision: Two-level budget enforcement (workbench and agent) with virtual keys
   - Context: May update existing ADR-0075 or create new focused ADR
   - Location: `olympus-hub-docs/decision-logs/` (update 0075 or new entry)

## Implementation Concepts Updates

Conceptual documentation updates to reflect new design details:

1. **authority-enforcement.md**

   - Add Cipher IAM Extensions integration details
   - Document PEP policy model (per-PEP policies, unknown PEP handling)
   - Update enforcement flow to include IAM Extensions API calls
   - Reference new IAM Extensions subsystem documentation

2. **agent-lifecycle.md**

   - Add IAM Extensions integration to agent lifecycle stages
   - Document agent profile lifecycle (creation, updates, revocation)
   - Add credential management and virtual key concepts
   - Reference new IAM Extensions subsystem documentation

---

## Success Criteria

- All three modules have comprehensive C2-level design documentation
- Critical enforcement/authorization mechanisms documented at C3 level
- Model Gateway content migrated and enhanced
- Agent Ingress Gateway and IAM Extensions have fresh designs
- All integration points clearly documented
- SCOPE.md documents created for each module
- Cross-references established to related subsystems
- Consistent structure and depth across all modules
- Decision log entries created for significant architectural decisions
- Implementation concepts updated to reflect new design details