# Agent Lifecycle

> **Status**: 🟢 Implemented — Concept  
> **Last Updated**: 2026-01-12

## Overview

The Agent Lifecycle concept defines how agents are managed as **versioned, deployable products** with full lifecycle governance. It implements Zeta's three-layer agent model and provides the control plane for agent creation, training, employment, and retirement.

**Key Integration**: **Cipher IAM Extensions** provide the identity, credential, and policy infrastructure for each lifecycle stage, ensuring that agents have appropriate profiles and credentials at each layer.

---

## The Three-Layer Agent Model

Seer implements Zeta's three-layer agent model, grounded in **Agent-Oriented Systems Modeling (AOSM)**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         EMPLOYED AGENT                                       │
│  Delegated authority to act in a specific work context                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                         TRAINED AGENT                                        │
│  Tenant-configured agent with domain knowledge and skills                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                         RAW AGENT                                            │
│  Deployable application artifact with technical capabilities                │
└─────────────────────────────────────────────────────────────────────────────┘
```

| Layer | AOSM Concept | What It Has | What It Lacks | IAM Profile |
|-------|--------------|-------------|---------------|-------------|
| **Raw Agent** | Abilities | Technical execution capabilities | Knowledge, Skills, Role, Authority | `raw-agent` tag |
| **Trained Agent** | Knowledge, Skills, Role | Domain expertise, defined responsibilities | Authority to act | `trained-agent` tag |
| **Employed Agent** | Authority, Autonomy | Delegated authority, team allocation | — (complete) | `employed-agent` tag + SPIFFE ID |

> For the complete agent model, see [Raw, Trained, Employed Agents](../../../aosm-meta-model/raw-trained-employed-agents.md).

---

## Raw Agent

A **Raw Agent** is the deployable technical artifact—the software application or container—that implements the foundational mechanisms for agent behavior.

In AOSM terms, a Raw Agent possesses **Abilities** (technical execution capabilities) but has not yet been assigned Knowledge, Skills, Role, or Responsibilities.

### Raw Agent Characteristics

**Artifact Type:**
- OCI container image
- Framework-agnostic (LangChain, LangGraph, Strands, CrewAI, custom, etc.)
- Can be compound (multi-agent internally, but Hub sees as single agent)

**Capabilities:**
- **Abilities**: Technical execution capabilities (tool calling, orchestration, archetype roles)
- **Structured Capabilities**: Declared in Raw Agent Spec (not free-form)
- **Framework Flexibility**: Any agentic framework can be used
- **Externalized Configuration**: Tools, resources, skills, knowledge bases, guardrails injected at Training/Employment

**Container Requirements:**
- Required endpoints: `/invoke` (POST), `/health/live`, `/health/ready`, `/health/startup`
- Environment variables injected by Seer Runtime
- Health probes for Kubernetes orchestration

**Lifecycle States:**
```
[Developed] → [Built] → [Published] → [Deployed*] → [Retired]
                                          │
                                          └── *Deployed via Training/Employment
```

**Important**: Raw Agents are **NOT deployable on their own**. They are containers referenced by Training Specs and deployed only as part of Employed Agent instances within workbench environments.

**Cipher IAM Profile:**
- Profile tagged as `raw-agent` in Cipher IAM Extensions
- No runtime credentials (not yet employed)
- Declares supported models, tools, and capabilities
- Infrastructure identity (vs. delegated identity at Employment)

**Raw Agent Spec Components:**
- Container image reference (registry, repository, tag, digest)
- Structured/typed capabilities (tool calling, orchestration, archetype roles, prompt tags)
- Documentation references (for Agent Engineers, Trained Agent developers, Employed Agent developers)
- Version information (semantic versioning)

**Raw Agent Directory:**
- Registry of all Raw Agents
- Capability-based search and discovery
- Version tracking and compatibility
- Impact analysis (which Trained/Employed Agents use this Raw Agent)

> **See**: [Profile Tags](../subsystems/cipher-iam-extensions/profile-tags.md) for Raw Agent profile attributes.  
> **See**: [Raw Agent Lifecycle Manager](../subsystems/raw-agent-lifecycle-manager/README.md) for Raw Agent management.  
> **See**: [Raw Agent in Hub Context](../hub-integration/raw-agent.md) for Hub integration details.

---

## Trained Agent

A **Trained Agent** is a Raw Agent configured with organizational Knowledge, domain-specific Skills, defined Responsibilities, and a Role—but not yet granted Authority to act.

In AOSM terms, a Trained Agent represents the outcome of *Training*—the development of KSA appropriate to an assigned Role. Its capabilities are **latent**—ready but not activated.

**Training Spec Components:**
- Context Definitions (tenant identity, domain, role, PIDA mapping)
- Behavioral Configuration (system prompts, style guidelines, procedures)
- Guardrails (safety constraints — **immutable at Employment**)
- Knowledge Bindings (knowledge bases, reference data)
- Tool Bindings (available tools, tool configurations)

**Cipher IAM Profile:**
- Profile tagged as `trained-agent` in Cipher IAM Extensions
- Inherits from Raw Agent profile
- Adds allowed models (subset of Raw Agent's declared models)
- No runtime credentials (not yet employed)

> **See**: [Profile Tags](../subsystems/cipher-iam-extensions/profile-tags.md) for Trained Agent profile attributes.

---

## Employed Agent

An **Employed Agent** is a Trained Agent that has been granted Authority to act in a specific work context (workbench, scenarios, customers).

In AOSM terms, an Employed Agent has **Authority** and **Autonomy**—it can act on behalf of a principal within defined limits.

**Employment Spec Components:**
- Authority Delegation (IAM role, scopes, ceilings)
- Workbench Assignment (which workbench(s) the agent operates in)
- Scenario Bindings (which scenarios the agent can participate in)
- Resource Quotas (compute, memory, token budgets)
- Fair Usage Budgets (per subject, per signal, etc.)
- Delegation Chain (who delegated authority to this agent)

**Employment States:**
```
[Requested] → [Approved] → [Active] → [Suspended] → [Revoked]
```

**Cipher IAM Profile (Full Agent Identity):**
- Profile tagged as `employed-agent` in Cipher IAM Extensions
- **SPIFFE Identity**: Unique cryptographic identity (e.g., `spiffe://hub.olympus.io/seer/tenant/{tenant_id}/workbench/{workbench_id}/agent/{agent_id}`)
- **Virtual Key**: Unique key for Model Gateway access, budget tracking, and audit
- **Policy Attachments**: PEP-specific policies (tool-gateway, model-gateway, signal-exchange)
- **Accountable Human**: Reference to the Supervisor who delegated authority
- **Authority Ceiling**: Inherited and narrowed authority from delegation chain

> **See**: [Credential Management](../subsystems/cipher-iam-extensions/credential-management.md) for virtual key and SPIFFE certificate provisioning.

---

## Lifecycle Transitions

### Raw → Trained
- **Process**: Training Spec applied to Raw Agent
- **Owner**: Domain/product team
- **Outcome**: Trained Agent with Knowledge, Skills, Role
- **IAM Action**: Cipher IAM Extensions creates `trained-agent` profile inheriting from Raw Agent

### Trained → Employed
- **Process**: Employment Spec applied to Trained Agent
- **Owner**: Supervisor (with approvals)
- **Outcome**: Employed Agent with Authority
- **IAM Actions**:
  - Cipher IAM Extensions creates `employed-agent` profile
  - SPIFFE identity issued via SPIRE
  - Virtual key provisioned for Model Gateway
  - Policy attachments registered for relevant PEPs
  - Accountable human (Supervisor) recorded

### Employment State Changes
- **Suspend**: Retains authority, stops execution; credentials remain valid but agent pod is scaled to zero
- **Resume**: Restores execution; agent pod scaled up
- **Revoke**: Permanently removes authority; SPIFFE identity revoked, virtual key invalidated, profile archived

---

## Credential Management

Cipher IAM Extensions manage all agent credentials through the lifecycle:

```mermaid
graph TD
    subgraph "Raw Agent"
        RA[No Runtime Credentials]
    end

    subgraph "Trained Agent"
        TA[No Runtime Credentials]
    end

    subgraph "Employed Agent"
        EA[Full Credential Set]
        SPIFFE[SPIFFE Certificate<br/>(X.509, auto-rotated)]
        VK[Virtual Key<br/>(Model Gateway access)]
        ZV[Zone-Vault Reference<br/>(Tool credentials)]
    end

    RA --> TA
    TA --> EA
    EA --> SPIFFE
    EA --> VK
    EA --> ZV
```

| Credential Type | Provisioned By | Purpose | Rotation |
|-----------------|----------------|---------|----------|
| **SPIFFE Certificate** | SPIRE Agent | mTLS identity, service mesh auth | Automatic (hourly) |
| **Virtual Key** | Seer Operator | Model Gateway access, budget tracking | On employment or rotation request |
| **Zone-Vault Reference** | Seer Operator | Tool credential injection | On demand |

> **See**: [Credential Management](../subsystems/cipher-iam-extensions/credential-management.md) for detailed provisioning and injection mechanisms.

---

## Key Principles

- **Three-Layer Model** — Raw → Trained → Employed progression
- **Versioning** — All layers are versioned independently
- **Immutability** — Training Spec guardrails cannot be relaxed at Employment
- **Authority Delegation** — Employment grants authority, not Training
- **Lifecycle Governance** — Full audit trail of all state transitions
- **IAM Integration** — Each layer has a corresponding Cipher IAM profile
- **Credential Lifecycle** — Credentials provisioned at Employment, revoked at termination
- **Human Accountability** — All Employed Agents traceable to accountable human

---

## Persona Twins

**Persona Twins** are a specialized use case of the three-layer agent model, enabling collaborators to create personal AI agents for delegation.

### Three-Layer Model for Persona Twins

| Layer | Persona Twin Implementation |
|-------|-----------------------------|
| **Raw Agent** | Standard Raw Agent (e.g., `assistant-raw`) |
| **Trained Agent** | Training Spec with `persona-twin` label, delegator metadata |
| **Employed Agent** | Employment Spec with user delegation, delegator = accountable |

### Key Differences from Business Agents

| Aspect | Business Agent | Persona Twin |
|--------|----------------|--------------|
| **Created by** | Developer persona | Any collaborator |
| **Delegation** | Role or user delegation | User delegation (delegator = accountable) |
| **Visibility** | Typically public | Typically private |
| **Scenarios** | Business Scenarios | Persona Twin Scenarios |
| **Triggers** | Business events | Personal events (tasks, notifications, schedules) |

### Persona Twin Lifecycle

```
1. Collaborator selects Persona Twin Blueprint
   └── Blueprint provides signal suggestions and OPA filters

2. Training Spec created with persona-twin label
   └── Delegator metadata captures the collaborator

3. Trained Agent created via standard training
   └── Tagged in Trained Agent Directory as personaTwin

4. Employment Spec created with user delegation
   └── delegator = accountable = collaborator
   └── Authority inherits from delegator

5. Persona Twin Scenario activated
   └── Triggers respond to delegator's tasks/notifications/schedules
```

### Related Documentation

- [Persona Twins](./persona-twins.md) — Full Persona Twin concept
- [Persona Twin Blueprint](./persona-twin-blueprint.md) — Blueprint for creating twins
- [Training Spec Manager](../subsystems/trained-agent-lifecycle-manager/training-spec-manager.md) — Persona Twin metadata validation
- [Employment Spec Manager](../subsystems/agent-lifecycle-manager/employment-spec-manager.md) — Persona Twin authority delegation

---

## Related

### Cipher IAM Extensions (Identity & Credentials)
- [Cipher IAM Extensions README](../subsystems/cipher-iam-extensions/README.md) — Extensions overview
- [Architecture](../subsystems/cipher-iam-extensions/architecture.md) — Agent identity types, SPIFFE integration
- [Profile Tags](../subsystems/cipher-iam-extensions/profile-tags.md) — Raw/Trained/Employed agent profile attributes
- [Credential Management](../subsystems/cipher-iam-extensions/credential-management.md) — Virtual keys, SPIFFE certificates, injection
- [Human Accountability](../subsystems/cipher-iam-extensions/human-accountability.md) — Accountable human assignment
- [Integration Patterns](../subsystems/cipher-iam-extensions/integration-patterns.md) — Seer Operator integration
- [ADR-0106: Cipher IAM Extensions for Agent Profiles](../../../olympus-hub-docs/decision-logs/0106-seer-cipher-iam-extensions-agent-profiles.md)

### Agent Lifecycle Manager (Employed Agent Lifecycle)
- [Agent Lifecycle Manager README](../subsystems/agent-lifecycle-manager/README.md) — Subsystem overview
- [Employment Spec Manager](../subsystems/agent-lifecycle-manager/employment-spec-manager.md) — Authority controls, quotas, budgets, delegation chains
- [Delegation Chain Sync Service](../subsystems/agent-lifecycle-manager/delegation-chain-sync-service.md) — Authority change detection and synchronization
- [Agent Levers Service](../subsystems/agent-lifecycle-manager/agent-levers-service.md) — Kill switches, authority enforcement
- [Employed Agent Directory](../subsystems/agent-lifecycle-manager/employed-agent-directory.md) — Agent profiles, accountability, change log

### Other Lifecycle Managers
- [Raw Agent Lifecycle Manager](../subsystems/raw-agent-lifecycle-manager/README.md) — Raw Agent management
- [Trained Agent Lifecycle Manager](../subsystems/trained-agent-lifecycle-manager/README.md) — Trained Agent management

### Related Systems
- `olympus-hub-docs/04-subsystems/cipher-iam/README.md` — Hub Cipher IAM (foundation)

---

*For detailed implementation, see the [Agent Lifecycle Manager](../subsystems/agent-lifecycle-manager/README.md) subsystem design documents. For identity and credential management, see [Cipher IAM Extensions](../subsystems/cipher-iam-extensions/README.md).*
