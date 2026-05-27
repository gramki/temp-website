---
name: Agent Identity Model Clarification
overview: Clarify the agent identity model by distinguishing Deployment Identity (SPIFFE) from Agent Persona (Scenario-derived), unifying scenario-scoped and request-scoped delegation as modes of the same mechanism, and updating documentation across Hub and Seer to reflect this model.
todos:
  - id: scratchpad-consolidate
    content: "Consolidate scratchpad: add hybrid token/sub-persona clarifications, remove answered questions"
    status: completed
  - id: adr-identity-model
    content: "Create ADR-0129: Agent Identity Model (Deployment vs Persona)"
    status: completed
  - id: adr-unified-delegation
    content: "Create ADR-0130: Unified Delegation Model (scenario/request modes)"
    status: completed
  - id: seer-identity-credentials
    content: Update agent-identity-credentials.md with two-layer identity model
    status: completed
  - id: seer-agent-lifecycle
    content: Update agent-lifecycle.md to clarify identity layers
    status: completed
  - id: seer-cipher-architecture
    content: Update Cipher IAM Extensions architecture.md with identity layers
    status: completed
  - id: seer-profile-tags
    content: Update profile-tags.md with persona vs deployment tags
    status: completed
  - id: seer-employment-spec
    content: Update employment-spec-crd.md with unified delegation mode
    status: completed
  - id: seer-request-scoped
    content: Update request-scoped-delegation.md with scenario-scoped mode
    status: completed
  - id: seer-authority-delegation
    content: Update authority-delegation.md with delegation modes
    status: completed
  - id: hub-agent-model
    content: Update agent-model.md with identity layers section
    status: completed
  - id: hub-scenario-as-agent
    content: Update scenario-as-agent.md with identity model
    status: completed
  - id: hub-cipher-infra
    content: Update cipher-iam-infrastructure.md with agent identity model
    status: completed
  - id: scratchpad-hub-vs-seer
    content: Update Hub Agent vs Seer Agent scratchpad with refined identity model
    status: completed
  - id: scratchpad-ambiguity
    content: "Final scratchpad update: mark resolved, reference ADRs, update next steps"
    status: completed
  - id: cross-cutting-updates
    content: Update delegation-chains.md, agent-lifecycle-service.md, why-seer identity
    status: completed
---

# Agent Identity Model Clarification

## Context

The current documentation conflates two distinct identities:

- **Deployment Identity (SPIFFE ID)**: Infrastructure-level, identifies the running pod/container — equivalent to an **OAuth Client**
- **Agent Persona**: Business-level identity derived from Scenario, carried in the **Delegation Access Token**

Key design decisions confirmed:

1. **SPIFFE ID = OAuth Client**: The deployment is the "client" presenting tokens on behalf of principals
2. **Delegation Access Token carries persona + authority**: Per-request, making deployments flexible
3. **One deployment can serve multiple personas**: Via different Delegation Access Tokens per request
4. **Scenario-scoped and request-scoped delegation use same semantics**: Different modes, not different mechanisms
5. **Employment Spec specifies delegation templates and policies**: Does not name identity profile (comes from Scenario/request)
6. **Hybrid Token Issuance**: Both modes use same pattern — Certificate at source time (deployment or request), Token always per-request
7. **Composite Application Sub-Personas**: Each agent in a composite gets its own sub-persona (e.g., `dispute-analyst-agent`, `dispute-reviewer-agent`)

---

## Phase 0: Consolidate Scratchpad

### 0.1 Update Identity Ambiguity Scratchpad with Clarifications

**File**: [olympus-hub-docs/scratchpad/0WIP-agent-identity-ambiguity-resolution.md](olympus-hub-docs/scratchpad/0WIP-agent-identity-ambiguity-resolution.md) (UPDATE)

**Changes**:

- Add confirmed decisions:
- Hybrid token issuance (Certificate at source, Token per-request)
- Sub-personas for Composite Applications (each agent gets own sub-persona)
- Remove answered questions from "Questions to Resolve" section (convert inline responses to confirmed decisions)
- Add Composite Application sub-persona model diagram
- Update status to reflect resolution progress

---

## Phase 1: Foundation (ADRs and Terminology)

### 1.1 Create ADR: Agent Identity Model

**File**: `olympus-hub-docs/decision-logs/0129-agent-identity-model.md` (NEW)

**Content**:

- Problem: Conflation of deployment identity and agent persona
- Decision: Two-layer identity model (Deployment Identity + Agent Persona)
- SPIFFE ID = OAuth Client equivalent (infrastructure)
- Agent Persona = Business identity (carried in Delegation Access Token)
- Token structure includes both: `client_id` (SPIFFE) + `sub` (Persona)

### 1.2 Create ADR: Unified Delegation Model

**File**: `olympus-hub-docs/decision-logs/0130-unified-delegation-model.md` (NEW)

**Content**:

- Problem: Scenario-scoped and request-scoped delegation appear as separate mechanisms
- Decision: Same mechanism, different modes (`scenario-scoped` vs `request-scoped`)
- Delegation Access Token semantics identical in both modes
- Employment Spec specifies delegation templates, not identity profile references
- Mode determines source: Scenario Identity Profile vs Business User consent

---

## Phase 2: Seer Design Documentation Updates

### 2.1 Update Agent Identity & Credentials

**File**: [olympus-seer-docs/seer-design/implementation-concepts/agent-identity-credentials.md](olympus-seer-docs/seer-design/implementation-concepts/agent-identity-credentials.md) (UPDATE)

**Changes**:

- Add "Two-Layer Identity Model" section distinguishing Deployment Identity vs Agent Persona
- Clarify SPIFFE ID as "OAuth Client equivalent" (infrastructure-level)
- Add "Delegation Access Token" as carrier of persona + authority
- Update terminology: use "Deployment Identity" not just "SPIFFE Identity"

### 2.2 Update Agent Lifecycle

**File**: [olympus-seer-docs/seer-design/implementation-concepts/agent-lifecycle.md](olympus-seer-docs/seer-design/implementation-concepts/agent-lifecycle.md) (UPDATE)

**Changes**:

- Employed Agent section: clarify SPIFFE = deployment identity (client)
- Add note that Agent Persona comes from Scenario binding
- Reference unified delegation model

### 2.3 Update Cipher IAM Extensions Architecture

**File**: [olympus-seer-docs/seer-design/subsystems/cipher-iam-extensions/architecture.md](olympus-seer-docs/seer-design/subsystems/cipher-iam-extensions/architecture.md) (UPDATE)

**Changes**:

- Add section on two identity layers
- Update SPIFFE Integration to clarify it's deployment/client identity
- Add Agent Persona management (Scenario-derived business identity)

### 2.4 Update Profile Tags

**File**: [olympus-seer-docs/seer-design/subsystems/cipher-iam-extensions/profile-tags.md](olympus-seer-docs/seer-design/subsystems/cipher-iam-extensions/profile-tags.md) (UPDATE)

**Changes**:

- Distinguish profile tags for deployment vs persona
- Add `scenario-persona` tag for Scenario-derived agent personas

### 2.5 Update Employment Spec CRD

**File**: [olympus-seer-docs/seer-design/hub-integration/employment-spec-crd.md](olympus-seer-docs/seer-design/hub-integration/employment-spec-crd.md) (UPDATE)

**Changes**:

- Update `delegation` section to show unified model
- Add `mode: scenario-scoped | request-scoped` 
- Clarify that Employment Spec specifies templates/policies, not identity profile
- Add note: deployment identity (SPIFFE) is auto-provisioned

### 2.6 Update Request-Scoped Delegation

**File**: [olympus-seer-docs/seer-design/implementation-concepts/request-scoped-delegation.md](olympus-seer-docs/seer-design/implementation-concepts/request-scoped-delegation.md) (UPDATE)

**Changes**:

- Add section on "Scenario-Scoped Delegation" as alternative mode
- Clarify SPIFFE ID = OAuth Client in the analogy section
- Update token structure to show `client_id` (SPIFFE) + `sub` (Persona) + `delegated_by`

### 2.7 Update Authority Delegation

**File**: [olympus-seer-docs/seer-design/subsystems/cipher-iam-extensions/authority-delegation.md](olympus-seer-docs/seer-design/subsystems/cipher-iam-extensions/authority-delegation.md) (UPDATE)

**Changes**:

- Add "Delegation Modes" section (scenario-scoped vs request-scoped)
- Clarify that both use same Delegation Access Token semantics
- Update diagrams to show identity layers

---

## Phase 3: Hub Design Documentation Updates

### 3.1 Update Agent Model

**File**: [olympus-hub-docs/02-system-design/agent-model.md](olympus-hub-docs/02-system-design/agent-model.md) (UPDATE)

**Changes**:

- Add "Agent Identity Layers" section
- Clarify AI Agent IAM: SPIFFE = deployment/client identity
- Reference Scenario as source of Agent Persona

### 3.2 Update Scenario as Agent

**File**: [olympus-hub-docs/02-system-design/implementation-concepts/scenario-as-agent.md](olympus-hub-docs/02-system-design/implementation-concepts/scenario-as-agent.md) (UPDATE)

**Changes**:

- Add "Identity Model" section
- Clarify: Scenario provides Agent Persona (business identity)
- ScenarioAsAgent CRD registers persona in Cipher IAM

### 3.3 Update Cipher IAM Infrastructure

**File**: [olympus-hub-docs/05-infrastructure/cipher-iam-infrastructure.md](olympus-hub-docs/05-infrastructure/cipher-iam-infrastructure.md) (UPDATE)

**Changes**:

- Add agent identity model section
- Clarify SPIFFE integration is for deployment identity
- Add Agent Persona registration for Scenarios

---

## Phase 4: Dependent Documentation Updates

### 4.1 Update Hub Agent vs Seer Agent Scratchpad

**File**: [olympus-hub-docs/scratchpad/0WIP-hub-agent-vs-seer-agent.md](olympus-hub-docs/scratchpad/0WIP-hub-agent-vs-seer-agent.md) (UPDATE)

**Changes**:

- Update Identity Model Differences section to reflect two-layer model
- Clarify: Hub Agent identity = Persona (from Scenario)
- Clarify: Seer Agent adds Deployment Identity layer (SPIFFE)

### 4.2 Finalize Identity Ambiguity Scratchpad

**File**: [olympus-hub-docs/scratchpad/0WIP-agent-identity-ambiguity-resolution.md](olympus-hub-docs/scratchpad/0WIP-agent-identity-ambiguity-resolution.md) (UPDATE)

**Changes**:

- Mark confirmed decisions as resolved
- Update Next Steps to reference created ADRs and updated docs
- Change status to indicate resolution in progress

---

## Phase 5: Cross-Cutting Updates

### 5.1 Update Delegation Chains

**File**: [olympus-seer-docs/seer-design/implementation-concepts/delegation-chains.md](olympus-seer-docs/seer-design/implementation-concepts/delegation-chains.md) (UPDATE)

**Changes**:

- Reference two identity layers
- Clarify delegation chain tracks Persona, not Deployment Identity
- Add mode distinction (scenario-scoped vs request-scoped)

### 5.2 Update Agent Lifecycle Service

**File**: [olympus-seer-docs/seer-design/subsystems/agent-lifecycle-service.md](olympus-seer-docs/seer-design/subsystems/agent-lifecycle-service.md) (UPDATE)

**Changes**:

- Employed Agent section: clarify two identity layers
- Reference unified delegation model

### 5.3 Update Why-Seer Agent Identity

**File**: [olympus-seer-docs/why-seer/part-2-how-seer-solves/03-identity-authority-in-seer/03-1-agent-identity.md](olympus-seer-docs/why-seer/part-2-how-seer-solves/03-identity-authority-in-seer/03-1-agent-identity.md) (UPDATE)

**Changes**:

- Update Identity Layers section with two-layer model
- Clarify: Infrastructure identity (SPIFFE) vs Business identity (Persona)
- Add OAuth Client analogy for SPIFFE

---

## Summary

| Category | Files | Type |
|----------|-------|------|
| Scratchpad Consolidation | 1 | UPDATE (Phase 0) |
| ADRs | 2 | NEW |
| Seer Design | 7 | UPDATE |
| Hub Design | 3 | UPDATE |
| Scratchpads | 2 | UPDATE |
| Why-Seer | 1 | UPDATE |
| **Total** | **16** | |

---

## Key Terminology Established

| Term | Definition |
|------|------------|
| **Deployment Identity** | SPIFFE-based cryptographic identity of the running agent pod; OAuth Client equivalent |
| **Agent Persona** | Business identity derived from Scenario; represents "who" the agent is |
| **Delegation Access Token** | Per-request token carrying both persona context and delegated authority |
| **Scenario-Scoped Delegation** | Mode where authority derives from Scenario Identity Profile |
| **Request-Scoped Delegation** | Mode where authority derives from Business User consent |
| **Unified Delegation Model** | Single mechanism with two modes, same token semantics |