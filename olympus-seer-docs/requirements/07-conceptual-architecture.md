# 7. Zeta Agent Platform: Conceptual Architecture

---

This section describes the **high-level architecture** of Zeta's Agent Platform. It defines the relationship between control plane and execution plane, how components interact, and how the platform achieves portability and resilience.

This is a conceptual model, not a detailed technical specification.

---

## 7.1 The Fundamental Split: Control Plane vs. Execution Plane

The platform architecture is organized around a fundamental separation:

```
┌─────────────────────────────────────────────────────────────────────┐
│                        ZETA CONTROL PLANE                           │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                    Platform Services                          │ │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ │ │
│  │  │Lifecycle│ │Identity │ │ Memory  │ │  Audit  │ │Governance│ │ │
│  │  │ Service │ │ Service │ │ Service │ │ Service │ │ Service │ │ │
│  │  └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘ │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                   Orchestration Layer                         │ │
│  │  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐ │ │
│  │  │Context Assembly │ │ Tool Executor   │ │ Policy Engine   │ │ │
│  │  └─────────────────┘ └─────────────────┘ └─────────────────┘ │ │
│  └───────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
                                   │
                                   │ Abstraction Layer
                                   ▼
┌─────────────────────────────────────────────────────────────────────┐
│                       EXECUTION SUBSTRATE                           │
│                                                                     │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────────────┐│
│  │  Model Layer   │  │  Storage Layer │  │   Compute Layer        ││
│  │                │  │                │  │                        ││
│  │ AWS Bedrock    │  │ S3/Blob/GCS    │  │ EKS/AKS/GKE           ││
│  │ Azure OpenAI   │  │ PostgreSQL     │  │ Lambda/Functions/      ││
│  │ Vertex AI      │  │ Vector DBs     │  │ Cloud Run              ││
│  │ Self-hosted    │  │                │  │                        ││
│  └────────────────┘  └────────────────┘  └────────────────────────┘│
│                                                                     │
│              AWS  │  Azure  │  GCP  │  Customer Cloud              │
└─────────────────────────────────────────────────────────────────────┘
```

### Control Plane Responsibilities

The **Zeta Control Plane** owns:

| Responsibility | Description |
|----------------|-------------|
| **Agent Lifecycle** | Definition, versioning, deployment, retirement |
| **Agent Identity** | Unique identifiers, credentials, authority scopes |
| **Memory Management** | Persistent state across sessions and regions |
| **Audit & Evidence** | Decision records, explanation generation, evidence packaging |
| **Governance** | Policies, guardrails, override mechanisms, kill switches |
| **Orchestration** | Context assembly, tool execution, reasoning coordination |

### Execution Substrate Responsibilities

The **Execution Substrate** (CSP infrastructure) provides:

| Responsibility | Description |
|----------------|-------------|
| **Model Inference** | Foundation model API calls |
| **Compute** | Container orchestration, serverless execution |
| **Storage** | Object storage, databases, vector stores |
| **Networking** | Connectivity, load balancing, DNS |
| **Observability Infrastructure** | Logs, metrics, traces collection |

### Why This Split Matters

| Concern | If Control Plane Is CSP-Owned | If Control Plane Is Zeta-Owned |
|---------|------------------------------|-------------------------------|
| Portability | Locked to one CSP | Deployable on any CSP |
| Customization | Limited to CSP capabilities | Bank-specific requirements possible |
| Resilience | Limited to CSP availability | Multi-CSP failover possible |
| Compliance | CSP determines evidence format | Zeta controls evidence generation |

---

## 7.2 Deployment Topologies

The platform supports multiple deployment topologies to meet bank requirements.

### Topology A: Zeta-Hosted, CSP-Backed

```
┌──────────────────────────────────────────────────────────────┐
│                      ZETA CLOUD                              │
│  ┌────────────────────────────────────────────────────────┐ │
│  │              Zeta Control Plane                        │ │
│  │   (Multi-tenant, managed by Zeta)                      │ │
│  └────────────────────────────────────────────────────────┘ │
│                           │                                  │
│                           ▼                                  │
│  ┌────────────────────────────────────────────────────────┐ │
│  │              Zeta Runtime                              │ │
│  │   (Running on CSP infrastructure)                      │ │
│  └────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
                           │
                           ▼
              ┌────────────────────────┐
              │   Bank Systems (APIs)  │
              └────────────────────────┘
```

**Use case:** Mid-sized banks comfortable with SaaS model, wanting rapid deployment.

### Topology B: Customer-Hosted Control Plane

```
┌──────────────────────────────────────────────────────────────┐
│                  BANK CLOUD ACCOUNT                          │
│  ┌────────────────────────────────────────────────────────┐ │
│  │              Zeta Control Plane                        │ │
│  │   (Single-tenant, deployed in bank's VPC)              │ │
│  └────────────────────────────────────────────────────────┘ │
│                           │                                  │
│                           ▼                                  │
│  ┌────────────────────────────────────────────────────────┐ │
│  │              Zeta Runtime                              │ │
│  │   (Running on bank's CSP infrastructure)               │ │
│  └────────────────────────────────────────────────────────┘ │
│                           │                                  │
│                           ▼                                  │
│  ┌────────────────────────────────────────────────────────┐ │
│  │              Bank Systems                              │ │
│  └────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
```

**Use case:** Large banks with strict data residency requirements, preferring control.

### Topology C: Multi-Cloud Active-Active

```
┌─────────────────────────┐      ┌─────────────────────────┐
│     AWS REGION 1        │      │    AZURE REGION 1       │
│ ┌─────────────────────┐ │      │ ┌─────────────────────┐ │
│ │ Zeta Control Plane  │◄──────►│ Zeta Control Plane  │ │
│ │ (Active)            │ │ Sync │ │ (Active)            │ │
│ └─────────────────────┘ │      │ └─────────────────────┘ │
│         │               │      │         │               │
│         ▼               │      │         ▼               │
│ ┌─────────────────────┐ │      │ ┌─────────────────────┐ │
│ │   Zeta Runtime      │ │      │ │   Zeta Runtime      │ │
│ │   (Bedrock Models)  │ │      │ │   (Azure OpenAI)    │ │
│ └─────────────────────┘ │      │ └─────────────────────┘ │
└─────────────────────────┘      └─────────────────────────┘
```

**Use case:** Banks requiring business continuity across CSP failures.

---

## 7.3 Component Interaction Model

### Request Flow

A typical agent interaction follows this flow:

```
                    ┌─────────────────┐
                    │   User/System   │
                    │     Request     │
                    └────────┬────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         CONTROL PLANE                               │
│                                                                     │
│  ┌─────────────────┐                                               │
│  │ 1. Identity &   │ ─── Verify agent identity, check authority    │
│  │    Authority    │                                               │
│  └────────┬────────┘                                               │
│           │                                                         │
│           ▼                                                         │
│  ┌─────────────────┐                                               │
│  │ 2. Context      │ ─── Assemble context from memory, knowledge,  │
│  │    Assembly     │     session state                             │
│  └────────┬────────┘                                               │
│           │                                                         │
│           ▼                                                         │
│  ┌─────────────────┐                                               │
│  │ 3. Policy       │ ─── Apply guardrails, check constraints       │
│  │    Enforcement  │                                               │
│  └────────┬────────┘                                               │
│           │                                                         │
└───────────┼─────────────────────────────────────────────────────────┘
            │
            ▼
┌─────────────────────────────────────────────────────────────────────┐
│                       EXECUTION SUBSTRATE                           │
│                                                                     │
│  ┌─────────────────┐                                               │
│  │ 4. Model        │ ─── Send prompt, receive response             │
│  │    Inference    │                                               │
│  └────────┬────────┘                                               │
│           │                                                         │
└───────────┼─────────────────────────────────────────────────────────┘
            │
            ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         CONTROL PLANE                               │
│                                                                     │
│  ┌─────────────────┐                                               │
│  │ 5. Response     │ ─── Parse response, determine action          │
│  │    Processing   │                                               │
│  └────────┬────────┘                                               │
│           │                                                         │
│           ▼                                                         │
│  ┌─────────────────┐                                               │
│  │ 6. Tool         │ ─── Execute tools if needed (loop back to 3)  │
│  │    Execution    │                                               │
│  └────────┬────────┘                                               │
│           │                                                         │
│           ▼                                                         │
│  ┌─────────────────┐                                               │
│  │ 7. Memory       │ ─── Update agent memory                       │
│  │    Update       │                                               │
│  └────────┬────────┘                                               │
│           │                                                         │
│           ▼                                                         │
│  ┌─────────────────┐                                               │
│  │ 8. Audit        │ ─── Log decision, generate explanation        │
│  │    Logging      │                                               │
│  └────────┬────────┘                                               │
│           │                                                         │
└───────────┼─────────────────────────────────────────────────────────┘
            │
            ▼
                    ┌─────────────────┐
                    │     Response    │
                    └─────────────────┘
```

### Key Design Points

1. **Model inference is a step, not the orchestration.** The control plane coordinates; the model is called as needed.

2. **Every step is logged.** The audit system captures each phase of processing.

3. **Policy enforcement happens before and after inference.** Guardrails are applied to both inputs and outputs.

4. **Tool execution may loop.** If the model requests tool calls, the flow returns to policy enforcement.

5. **Memory update is explicit.** Memory is not automatically modified; updates follow policy.

---

## 7.4 Abstraction Layer Design

The abstraction layer enables portability by defining stable interfaces for variable implementations.

### Model Abstraction

```
┌─────────────────────────────────────────────────────────────────────┐
│                      MODEL ABSTRACTION LAYER                        │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                     Unified Model Interface                   │ │
│  │   - complete(prompt, options) → response                      │ │
│  │   - embed(text) → vector                                      │ │
│  │   - capabilities() → model_info                               │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                │                                    │
│         ┌──────────────────────┼──────────────────────┐            │
│         ▼                      ▼                      ▼            │
│  ┌─────────────┐       ┌─────────────┐       ┌─────────────┐       │
│  │   Bedrock   │       │ Azure OpenAI│       │  Vertex AI  │       │
│  │   Adapter   │       │   Adapter   │       │   Adapter   │       │
│  └─────────────┘       └─────────────┘       └─────────────┘       │
└─────────────────────────────────────────────────────────────────────┘
```

### Storage Abstraction

```
┌─────────────────────────────────────────────────────────────────────┐
│                     STORAGE ABSTRACTION LAYER                       │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                   Unified Storage Interface                   │ │
│  │   - Memory Store: get, put, query, delete                     │ │
│  │   - Document Store: store, retrieve, search                   │ │
│  │   - Audit Store: append (immutable), query                    │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                │                                    │
│         ┌──────────────────────┼──────────────────────┐            │
│         ▼                      ▼                      ▼            │
│  ┌─────────────┐       ┌─────────────┐       ┌─────────────┐       │
│  │  PostgreSQL │       │   Cosmos DB │       │   AlloyDB   │       │
│  │   Adapter   │       │   Adapter   │       │   Adapter   │       │
│  └─────────────┘       └─────────────┘       └─────────────┘       │
└─────────────────────────────────────────────────────────────────────┘
```

### Why Abstraction Layers Matter

| Without Abstraction | With Abstraction |
|---------------------|------------------|
| Direct CSP API calls throughout code | CSP-specific code isolated to adapters |
| Changing CSP requires rewriting code | Changing CSP requires new adapter only |
| Testing requires CSP access | Testing can use mock adapters |
| Multi-cloud requires parallel implementations | Multi-cloud uses same core with different adapters |

---

## 7.5 State Management and Replication

### State Categories

| Category | Examples | Consistency Requirement | Replication Model |
|----------|----------|------------------------|-------------------|
| **Configuration** | Agent definitions, policies | Strong (must be consistent) | Synchronous |
| **Memory** | Episodic, semantic, preference | Eventual (tolerate lag) | Asynchronous |
| **Session** | Current interaction state | Strong within session | Session-affinity |
| **Audit** | Decision logs, evidence | Durable (must not lose) | Append-only, replicated |

### Replication Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                     STATE REPLICATION LAYER                         │
│                                                                     │
│  ┌────────────────────┐                                            │
│  │  Configuration     │──── GitOps / Sync Service                  │
│  │  (Strong Sync)     │     Changes propagate immediately          │
│  └────────────────────┘                                            │
│                                                                     │
│  ┌────────────────────┐                                            │
│  │  Memory            │──── CRDT / Event Sourcing                  │
│  │  (Eventual Sync)   │     Conflict resolution built-in           │
│  └────────────────────┘                                            │
│                                                                     │
│  ┌────────────────────┐                                            │
│  │  Audit             │──── Append-only Log                        │
│  │  (Durable)         │     Replicated to all regions              │
│  └────────────────────┘                                            │
└─────────────────────────────────────────────────────────────────────┘
```

### Cross-Region Consistency

For multi-region deployment:

1. **Session affinity:** A session is pinned to one region for duration
2. **Memory sync:** Memory updates propagate asynchronously (typically < 1 second)
3. **Config sync:** Configuration changes are synchronously applied
4. **Audit replication:** Audit logs are durably replicated before acknowledgment

---

## 7.6 Failure Handling Architecture

### Failure Detection

```
┌─────────────────────────────────────────────────────────────────────┐
│                      HEALTH MONITORING                              │
│                                                                     │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────┐ │
│  │ Component       │  │ Dependency      │  │ End-to-End          │ │
│  │ Health Checks   │  │ Health Checks   │  │ Synthetic Probes    │ │
│  └────────┬────────┘  └────────┬────────┘  └──────────┬──────────┘ │
│           │                    │                       │            │
│           └────────────────────┼───────────────────────┘            │
│                                ▼                                    │
│                    ┌─────────────────────┐                         │
│                    │  Health Aggregator  │                         │
│                    └──────────┬──────────┘                         │
│                               │                                     │
│              ┌────────────────┼────────────────┐                   │
│              ▼                ▼                ▼                   │
│       ┌──────────┐     ┌──────────┐     ┌──────────┐              │
│       │  Alert   │     │ Failover │     │ Dashboard│              │
│       │  System  │     │ Trigger  │     │          │              │
│       └──────────┘     └──────────┘     └──────────┘              │
└─────────────────────────────────────────────────────────────────────┘
```

### Failover Cascade

| Level | Detection | Response | Recovery |
|-------|-----------|----------|----------|
| **Component** | Health check fails | Restart, replace instance | Automatic |
| **Model** | Inference timeout/error | Switch to backup model | Automatic |
| **Region** | Multiple component failures | Route to standby region | Automatic |
| **CSP** | Regional failures + no recovery | Activate multi-cloud standby | Semi-automatic |

### Graceful Degradation Paths

```
┌─────────────────────────────────────────────────────────────────────┐
│                    DEGRADATION CASCADE                              │
│                                                                     │
│  Full Capability ──► Reduced Model ──► Rules Engine ──► Human      │
│                                                                     │
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────┐ │
│  │ Primary     │   │ Backup      │   │ Fallback    │   │ Escalate│ │
│  │ Model       │──►│ Model       │──►│ Rules       │──►│ to Human│ │
│  │ (GPT-4o)    │   │ (Claude)    │   │ Engine      │   │         │ │
│  └─────────────┘   └─────────────┘   └─────────────┘   └─────────┘ │
│                                                                     │
│  If unavailable:   If unavailable:   If unavailable:   Always      │
│  Try backup        Try rules         Escalate          available   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 7.7 Security Architecture

### Trust Boundaries

```
┌─────────────────────────────────────────────────────────────────────┐
│                      TRUST BOUNDARIES                               │
│                                                                     │
│  ┌────────────────────────────────────────────────────────────────┐│
│  │ TRUST BOUNDARY 1: Platform Perimeter                          ││
│  │ ┌────────────────────────────────────────────────────────────┐││
│  ││ TRUST BOUNDARY 2: Tenant Isolation                          │││
│  ││ ┌──────────────────────────────────────────────────────────┐│││
│  │││ TRUST BOUNDARY 3: Agent Sandbox                           ││││
│  │││                                                            ││││
│  │││  Agent executes with constrained capabilities             ││││
│  │││  - Limited network access                                 ││││
│  │││  - Scoped tool permissions                                ││││
│  │││  - Bounded resource usage                                 ││││
│  ││└──────────────────────────────────────────────────────────┘│││
│  │└────────────────────────────────────────────────────────────┘││
│  └────────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────────┘
```

### Authentication and Authorization

| Layer | Mechanism | Purpose |
|-------|-----------|---------|
| **User → Platform** | Bank SSO (SAML/OIDC) | Authenticate human users |
| **System → Platform** | mTLS + API keys | Authenticate system integrations |
| **Platform → Agent** | Internal identity | Associate requests with agent identity |
| **Agent → Tools** | Scoped credentials | Limit tool access to agent authority |
| **Agent → Model** | Platform-managed | Model access controlled by platform |

### Data Protection

| Data State | Protection |
|------------|------------|
| **At rest** | AES-256 encryption, tenant-specific keys |
| **In transit** | TLS 1.3 minimum |
| **In memory** | Memory isolation, no persistent caching of secrets |
| **In logs** | PII redaction, sensitive field masking |

---

## 7.8 Summary: Architecture Principles in Practice

| Principle | How Architecture Embodies It |
|-----------|------------------------------|
| **Zeta Owns Semantics** | Control plane defines all agent behavior |
| **CSPs Are Substrates** | Abstraction layer isolates CSP dependencies |
| **State Portability** | Replication layer enables cross-cloud state |
| **Failure-First** | Failover cascade at every level |
| **Products First** | Lifecycle service manages agent as product |
| **Transparency** | Audit logging at every step |
| **Defense in Depth** | Multiple trust boundaries, layered authorization |
| **Vendor Independence** | Adapter pattern for all external dependencies |

---

*Previous: [Section 6: Zeta's Solution Principles](./06-solution-principles.md)*

*Next: [Section 8: Platform Components & Design Rationale →](./08-platform-components.md)*

