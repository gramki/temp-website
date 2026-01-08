# Agent Definition & Lifecycle Service

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-08

## Overview

The Agent Definition & Lifecycle Service manages agents as **versioned, deployable products** with full lifecycle governance. It implements Zeta's three-layer agent model and provides the control plane for agent creation, training, employment, and retirement.

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

| Layer | AOSM Concept | What It Has | What It Lacks |
|-------|--------------|-------------|---------------|
| **Raw Agent** | Abilities | Technical execution capabilities | Knowledge, Skills, Role, Authority |
| **Trained Agent** | Knowledge, Skills, Role | Domain expertise, defined responsibilities | Authority to act |
| **Employed Agent** | Authority, Autonomy | Delegated authority, team allocation | — (complete) |

> For the complete agent model, see [Raw, Trained, Employed Agents](../../../aosm-meta-model/raw-trained-employed-agents.md).

---

## Raw Agent

A **Raw Agent** is the deployable technical artifact—the software application or container—that implements the foundational mechanisms for agent behavior.

In AOSM terms, a Raw Agent possesses **Abilities** (technical execution capabilities) but has not yet been assigned Knowledge, Skills, Role, or Responsibilities.

### Definition

| Dimension | Description |
|-----------|-------------|
| **Artifact** | Container image, serverless function, Kubernetes deployment |
| **Identity** | Infrastructure identity (SPIFFE SVID, cloud workload identity) |
| **Ownership** | Platform engineering team |
| **Multi-tenancy** | Designed for multi-tenant operation |

### Capabilities (Abilities)

| Capability | Description |
|------------|-------------|
| **Modality Support** | Text, voice, vision, multimodal I/O |
| **Orchestration** | Agent loop, context management, memory integration |
| **Multi-Agent Patterns** | Supervisor/worker, peer collaboration, handoffs |
| **Interaction Channels** | HTTP/REST, gRPC, WebSocket, message queues |
| **Model Integration** | Model routing, failover, token management |

### What a Raw Agent Does NOT Have

| AOSM Concept | Status |
|--------------|--------|
| Knowledge (organizational) | None — unaware of tenant, policies, procedures |
| Skills (task-specific) | None — no task-specific training |
| Role | None assigned — not part of any Goal hierarchy |
| Authority | None — cannot act on behalf of any principal |

### Lifecycle States

```
[Developed] → [Built] → [Deployed] → [Running] → [Retired]
```

| State | Description |
|-------|-------------|
| **Developed** | Source code complete, ready for build |
| **Built** | Container image available in registry |
| **Deployed** | Running in infrastructure (not yet serving) |
| **Running** | Actively serving requests |
| **Retired** | No longer available, decommissioned |

### Versioning

- Follows **semantic versioning** of the codebase (e.g., `v2.4.1`)
- Version tracks: orchestration code, model integrations, infrastructure bindings

### Ownership & Responsibility

| Role | Owner |
|------|-------|
| **Responsible** | Platform Team |
| **Approver** | Platform Lead + Security |
| **Auditor** | Platform Audit |
| **Accountable** | Platform Lead |

### Change Management

| Change Type | Review Required | Approval Gate | Rollback |
|-------------|-----------------|---------------|----------|
| Code patch | Code review | Platform lead | Redeploy previous |
| Model upgrade | Eval + security | Platform + AI lead | Revert config |
| Capacity change | Ops review | Platform lead | Previous config |

### Incident Response

| Issue Type | First Responder | Action |
|------------|-----------------|--------|
| Crash/OOM | Platform SRE | Restart/Scale |
| Performance degradation | Platform SRE | Scale/Optimize |
| Security vulnerability | Platform + Security | Patch/Redeploy |

### Audit Requirements

- Deployment events (who, when, what version)
- Configuration changes
- Error and crash logs
- Resource utilization metrics
- Availability events

---

## Trained Agent

A **Trained Agent** is a Raw Agent configured with organizational Knowledge, domain-specific Skills, defined Responsibilities, and a Role—but not yet granted Authority to act.

In AOSM terms, a Trained Agent represents the outcome of *Training*—the development of KSA appropriate to an assigned Role. Its capabilities are **latent**—ready but not activated.

### Definition

| Dimension | Description |
|-----------|-------------|
| **Artifact** | Training Spec (declarative configuration) |
| **Identity** | Application identity within tenant domain |
| **Ownership** | Domain/product team within the tenant |
| **Scope** | Always scoped to a single tenant |

### Training Spec

The Training Spec is a composite configuration that binds together what transforms a Raw Agent into a Trained Agent.

| Component | Ownership | Description |
|-----------|-----------|-------------|
| **Context Definitions** | Integral | Tenant identity, domain, role, PIDA mapping |
| **Behavioral Configuration** | Integral | System prompts, style guidelines, procedures |
| **Guardrails** | Referenced | Safety constraints — **immutable at Employment** |
| **Tool Specifications** | Referenced | Tool schemas, usage patterns, permissions |
| **Knowledge Bases** | Referenced | Accessible knowledge with retrieval strategies |
| **Memory Training** | Integral | Tool memory, procedural memory, semantic memory |

### Guardrail Immutability

> **Critical Constraint:** Training guardrails are **immutable** once published. They cannot be weakened, bypassed, or overridden at Employment.

This is the fundamental safety guarantee of the system.

### What a Trained Agent Has

| AOSM Concept | Status |
|--------------|--------|
| Knowledge | ✓ Domain and organizational knowledge acquired |
| Skills | ✓ Task-specific skills developed through training |
| Abilities | ✓ Inherited from Raw Agent |
| Role | ✓ Assigned — set of Responsibilities |
| Responsibilities (PIDA) | ✓ Defined — what to Perceive, Interpret, Decide, Act |

### What a Trained Agent Does NOT Have

| AOSM Concept | Status |
|--------------|--------|
| Authority | ✗ None — knows *what* to do but not authorized *to* do it |
| Credentials | ✗ No access to external systems |
| Work Context | ✗ Not scoped to specific work |

### Lifecycle States

```
[Drafted] → [Validated] → [Published] → [Active] → [Archived]
```

| State | Description |
|-------|-------------|
| **Drafted** | Training Spec in development |
| **Validated** | Tested in sandbox, ready for review |
| **Published** | Approved and available for employment |
| **Active** | In use by one or more Employed Agents |
| **Archived** | Superseded, no new employments allowed |

### Versioning

- Training Spec follows **semantic versioning** (e.g., `v1.7.0`)
- Referenced artifacts (Guardrails, Tools, Knowledge) are independently versioned
- Training Spec declares compatible version ranges (e.g., `guardrails: ^2.1.0`, `raw: ^2.0.0`)

### Ownership & Responsibility

| Role | Owner |
|------|-------|
| **Responsible** | Domain Team |
| **Approver** | Domain Lead + Compliance |
| **Auditor** | Domain Audit |
| **Accountable** | Domain Lead |

### Change Management

| Change Type | Review Required | Approval Gate | Rollback |
|-------------|-----------------|---------------|----------|
| Knowledge update | Content review | Domain lead | Re-index previous |
| Prompt update | Domain review | Domain lead | Version rollback |
| Tool training | Security review | Domain + security | Remove from spec |
| Guardrail change | Security + compliance | Domain + security lead | Version rollback |

### Incident Response

| Issue Type | First Responder | Action |
|------------|-----------------|--------|
| Hallucination | AI Engineering | Prompt/Guard update |
| Wrong domain behavior | Domain Team | Training Spec revision |
| Guardrail violation | Domain + Security | Training review |

### Audit Requirements

- Training Spec version history
- Prompt, knowledge, and tool changes
- Guardrail modifications (requires elevated review)
- Sandbox validation results
- Activation/deactivation events

---

## Employed Agent

An **Employed Agent** is a Trained Agent granted delegated Authority, allocated to a specific team context, and assigned RASCI responsibilities—operating under Controlled Autonomy with a designated Accountable human.

In AOSM terms, an Employed Agent is a full participant in a Human-AI Team, with all Four Components of Autonomy present: Authority, Availability, Capability, and Capacity.

### Definition

| Dimension | Description |
|-----------|-------------|
| **Artifact** | Employment Spec (delegation configuration) |
| **Identity** | Identity in Workforce IAM or Customer IAM |
| **Ownership** | Delegating principal (user, role, or manager) |
| **Scope** | Specific work context (team, project, customer) |

### Employment Spec

The Employment Spec configures how a Trained Agent is deployed with delegated authority.

| Component | Description |
|-----------|-------------|
| **Work Scope** | Project/team boundaries, temporal scope, functional scope |
| **Operational Environment** | Connection strings, credentials, tool endpoints |
| **Capacity & Resources** | Token limits, API budgets, compute allocation |
| **Authority Delegation** | User delegation or role delegation model |
| **Constraints & Policies** | Action limits, approval requirements, escalation triggers |
| **Delegator Preferences** | Communication style, decision guidelines |

### Authority Delegation Models

**User Delegation** — Agent acts as delegate of a specific user:

```
Delegating User (Alice, has permissions A, B, C, D)
    └── Employed Agent (Alice's Delegate, granted A, B only)
```

**Role Delegation** — Agent represents an organizational role:

```
Organizational Role (Compliance Reviewer)
    └── Employed Agent (Compliance Agent, has role's permissions)
        └── Manager: Compliance Team Lead (Accountable)
```

### Authority Inheritance Rule

> The delegated authority at any time is always a subset of what the delegator is currently authorized to do.

If Alice delegates permissions A and B, and later loses B, the agent immediately loses B as well.

### Employment Constraints

| Employment Can Do | Employment Cannot Do |
|-------------------|----------------------|
| Restrict tool access | Enable tools not in Training |
| Narrow scope of actions | Expand authority beyond Training |
| Add delegator preferences | Override Training guardrails |
| Set resource quotas | Remove safety constraints |
| Specify work context | Grant capabilities not trained |

### What an Employed Agent Has

| AOSM Concept | Status |
|--------------|--------|
| Authority | ✓ Delegated — right to act within defined scope |
| Autonomy | ✓ Controlled Autonomy — within bounds set by Accountable human |
| Allocation | ✓ Assigned to a specific Human-AI Team |
| RASCI | ✓ Responsible for specific activities, with human Accountable |
| OPD | ✓ Observable/Directable by HAT team members per role |

### Lifecycle States

```
[Requested] → [Approved] → [Active] → [Suspended] → [Revoked]
```

| State | Description |
|-------|-------------|
| **Requested** | Delegation pending approval |
| **Approved** | Authorized but not yet activated |
| **Active** | Operating with delegated authority |
| **Suspended** | Temporarily paused (authority retained) |
| **Revoked** | Authority permanently removed |

### Kill Switch

The Lifecycle Service can issue **kill switch commands** to immediately:

- Suspend an Employed Agent (retains authority, stops execution)
- Revoke an Employed Agent (permanently removes authority)

Kill switch commands are executed by the [Runtime & Deployment](./runtime-deployment.md) service.

### Versioning

- Employment Spec follows **semantic versioning** (e.g., `v3.2.0`)
- Declares compatible Training Spec version (e.g., `trained: ~1.7.0`)

### Complete Version Identifier

An Employed Agent's complete version:

```
raw:v2.4.1/trained:v1.7.0/employed:v3.2.0
```

### Ownership & Responsibility

| Role | Owner |
|------|-------|
| **Responsible** | Delegating Principal |
| **Approver** | Manager + Security |
| **Auditor** | Access Audit |
| **Accountable** | Manager (always human) |

### Change Management

| Change Type | Review Required | Approval Gate | Rollback |
|-------------|-----------------|---------------|----------|
| Scope expansion | Risk assessment | Delegator + security | Reduce scope |
| Quota change | Budget review | Delegator | Previous quota |
| Credential rotation | Automated | None (standard) | N/A |
| Delegation revocation | None | Security (emergency) | Re-delegate |

### Incident Response

| Issue Type | First Responder | Action |
|------------|-----------------|--------|
| Unauthorized action | Security | Delegation revocation |
| Scope violation | Security + Delegator | Scope reduction |
| Quota exhaustion | Delegator | Quota adjustment or suspension |

### Audit Requirements

- Delegation events (who delegated, what scope, when)
- Authority exercises (what actions, under whose authority)
- Credential usage
- Resource quota consumption
- Learning suggestions submitted
- Suspension and revocation events

---

## Cross-Layer Concerns

### Version Compatibility

| Dependency | Compatibility Rule |
|------------|--------------------|
| Trained → Raw | Training Spec declares compatible Raw Agent version range |
| Employed → Trained | Employment Spec declares compatible Training Spec version |

Incompatible upgrades require explicit re-validation.

### Audit Correlation

Every agent action must be traceable to:

1. The **Raw Agent version** executing
2. The **Training Spec version** in effect
3. The **Employment Spec** governing authority
4. The **Accountable human** (delegating principal or manager)

### Learning Feedback Loop

Employed Agents can **suggest learnings** for incorporation into future Training versions:

```
Employed Agent (runtime)
    │
    └── Suggests learnings ──→ Trainer (human or agent)
                                    │
                                    └── Reviews with change management controls
                                        │
                                        └── Incorporates into Trained Agent v(n+1)
```

Learnings are subject to change management controls and cannot bypass guardrails.

---

## Key Principles

- **Agents are products, not scripts** — versioned, governed, evolved
- **Versioning is independent per layer** — Raw, Trained, Employed evolve separately
- **Training guardrails are immutable** — cannot be overridden at Employment
- **Employment narrows, never expands** — authority ceiling set by Training
- **Every action is traceable** — to Raw + Training + Employment + Accountable human
- **Humans are always Accountable** — agents can be Responsible but never Accountable (RASCI)

---

## Dependencies

| System | Relationship |
|--------|--------------|
| **Cipher IAM** | Agent identity and authority; delegation enforcement |
| **Runtime & Deployment** | Executes lifecycle commands (suspend, revoke, kill) |
| **Model Gateway** | Model version management |
| **Cognitive Audit Fabric** | Audit trail storage |

---

## Related

- [Introduction](../introduction.md)
- [Raw, Trained, Employed Agents](../../../aosm-meta-model/raw-trained-employed-agents.md) — Complete agent model
- [Agent-Oriented System](../../../aosm-meta-model/agent-oriented-system.md) — AOSM foundations
- [Runtime & Deployment](./runtime-deployment.md) — Lifecycle execution

---

*TODO: Detailed design — API specifications, state machine implementation, approval workflow engine*

