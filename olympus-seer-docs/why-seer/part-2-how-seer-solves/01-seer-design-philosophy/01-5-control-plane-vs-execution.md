# 1.5 Control Plane vs. Execution Substrate

A critical architectural distinction in Seer is the separation between the **control plane** (what Seer owns) and the **execution substrate** (what infrastructure provides). This separation enables portability, governance, and clear accountability.

## The Distinction

| Dimension | Seer (Control Plane) | Infrastructure (Execution Substrate) |
|-----------|---------------------|--------------------------------------|
| **Focus** | Agent semantics | Resource provision |
| **Owns** | Identity, authority, lifecycle, guardrails | Compute, models, storage, networking |
| **Concern** | *What* the agent is and *how* it should behave | *Where* and *with what resources* it runs |
| **Change Rate** | Changes with business requirements | Changes with infrastructure evolution |
| **Provider** | Platform team | CSP or infrastructure team |

## What Seer Owns (Control Plane)

### Agent Semantics

Seer defines what an agent is at the semantic level:
- **Identity:** Who is this agent? What credentials does it hold?
- **Authority:** What is this agent allowed to do? Under whose delegation?
- **Lifecycle:** What version is deployed? What state is it in?
- **Guardrails:** What behaviors are prohibited?

These are enterprise concerns that must remain consistent regardless of where the agent runs.

### Policy and Governance

Seer enforces policies:
- Training guardrails that cannot be bypassed
- Authority ceilings that limit agent actions
- Audit requirements that capture decisions
- Approval workflows for lifecycle transitions

These policies apply regardless of the underlying infrastructure.

### Agent Intelligence

Seer manages the cognitive aspects:
- Context assembly logic
- Memory access patterns
- Knowledge retrieval strategies
- Tool invocation decisions

The "thinking" of an agent is governed by Seer, not by infrastructure.

## What Infrastructure Provides (Execution Substrate)

### Compute Resources

The infrastructure provides the resources to run agents:
- Container orchestration (Kubernetes)
- Serverless functions (Lambda, Cloud Functions)
- Compute instances for agent pods

### Model Access

The infrastructure provides access to AI models:
- LLM inference endpoints
- Model hosting (SageMaker, Bedrock, Vertex AI)
- GPU resources for local models

### Storage and Networking

The infrastructure provides:
- Persistent storage for state
- Network connectivity to tools and services
- Load balancing and traffic management

### Observability Infrastructure

The infrastructure provides:
- Metrics collection and aggregation
- Log storage and search
- Distributed tracing

## Why This Separation Matters

### Portability

Because Seer owns the semantic layer, the same agent can run on different infrastructures:
- Deploy on AWS, Azure, or GCP
- Switch between Kubernetes and serverless
- Use different model providers

The agent's behavior remains consistent because behavior is defined in Seer, not in infrastructure configuration.

### Governance Consistency

Governance policies are defined once and enforced everywhere:
- Authority ceilings apply regardless of where the agent runs
- Guardrails cannot be bypassed by infrastructure configuration
- Audit requirements are met on any infrastructure

### Clear Accountability

When issues arise, the separation helps identify responsibility:
- **Agent misbehaving within policy:** Control plane issue (training, guardrails)
- **Agent unable to run:** Infrastructure issue (compute, networking)
- **Agent violating policy:** Control plane enforcement issue
- **Agent slow or unavailable:** Infrastructure issue (capacity, scaling)

### Infrastructure Evolution

Infrastructure can evolve without changing agent semantics:
- Upgrade to new Kubernetes version
- Switch to better-priced model provider
- Adopt new observability tools

The agent's identity, authority, and behavior remain unchanged.

## Practical Implications

### For Architects

Design with clear separation:
- Define agent semantics in Training and Employment Specs (Seer)
- Define infrastructure requirements in deployment manifests (CSP)
- Avoid mixing semantic concerns with infrastructure configuration

### For Operators

Manage the layers independently:
- Agent issues → Seer observability
- Infrastructure issues → CSP monitoring
- Cross-layer issues → Correlation via case ID

### For Security

Apply controls at the right layer:
- Agent authority → Seer (identity, delegation)
- Network access → Infrastructure (firewall, VPC)
- Model access → Model Gateway (Seer) + credentials (Infrastructure)

---

**References:**
*   `olympus-seer-docs/seer-design/introduction.md`
*   `olympus-seer-docs/WHY-SEER-OUTLINE-DRAFT.md` — Section 6.5
