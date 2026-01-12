# Agent Lifecycle

> **Status**: 🟡 Draft — Concept  
> **Last Updated**: 2026-01-11

## Overview

The Agent Lifecycle concept defines how agents are managed as **versioned, deployable products** with full lifecycle governance. It implements Zeta's three-layer agent model and provides the control plane for agent creation, training, employment, and retirement.

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

**Lifecycle States:**
```
[Developed] → [Built] → [Deployed] → [Running] → [Retired]
```

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

---

## Lifecycle Transitions

### Raw → Trained
- **Process**: Training Spec applied to Raw Agent
- **Owner**: Domain/product team
- **Outcome**: Trained Agent with Knowledge, Skills, Role

### Trained → Employed
- **Process**: Employment Spec applied to Trained Agent
- **Owner**: Supervisor (with approvals)
- **Outcome**: Employed Agent with Authority

### Employment State Changes
- **Suspend**: Retains authority, stops execution
- **Resume**: Restores execution
- **Revoke**: Permanently removes authority

---

## Key Principles

- **Three-Layer Model** — Raw → Trained → Employed progression
- **Versioning** — All layers are versioned independently
- **Immutability** — Training Spec guardrails cannot be relaxed at Employment
- **Authority Delegation** — Employment grants authority, not Training
- **Lifecycle Governance** — Full audit trail of all state transitions

---

## Related

- `subsystems/agent-lifecycle-manager/README.md` - Agent Lifecycle Manager subsystem
- `subsystems/raw-agent-lifecycle-manager/README.md` - Raw Agent Lifecycle Manager
- `subsystems/trained-agent-lifecycle-manager/README.md` - Trained Agent Lifecycle Manager
- `olympus-hub-docs/04-subsystems/cipher-iam/README.md` - IAM for authority delegation

---

*For detailed implementation, see `subsystems/agent-lifecycle-service.md` and `subsystems/agent-lifecycle-api.md` (to be migrated to `subsystems/agent-lifecycle-manager/`).*
