# 5.1 The Agent Lifecycle

The lifecycle of an enterprise AI agent extends far beyond "deploy and run." Unlike traditional software, where a compiled artifact is deployed and executed, enterprise agents progress through distinct phases that correspond to different levels of capability, knowledge, and authority. Understanding this lifecycle is essential for establishing appropriate governance, ownership, and change management.

## The Three-Layer Model

Enterprise agent platforms benefit from a clear decomposition of what constitutes an "agent" at different stages. The **Raw, Trained, Employed** model provides this clarity:

### 1. Raw Agent: The Deployable Artifact

**Definition:** A Raw Agent is the deployable technical artifact—the container image, serverless function, or service—that implements the foundational mechanisms for agent behavior. It possesses technical *abilities* but has not yet been configured with organizational knowledge, domain skills, or operational authority.

A Raw Agent includes:
- **Orchestration capabilities:** The agent loop (observe → think → act → reflect), context window management, and memory integration infrastructure.
- **Model integration:** Connection to LLM providers, model routing, and token management.
- **Multi-agent patterns:** Support for supervisor/worker topologies, handoff protocols, and coordination.
- **Interaction channels:** HTTP, gRPC, WebSocket, message queue integration.
- **Infrastructure identity:** Workload identity (e.g., SPIFFE SVID, cloud workload identity) for platform-level authentication.

**What a Raw Agent does NOT have:**
- Organizational knowledge or domain-specific training
- Task-specific skills or behavioral patterns
- Role assignments or operational responsibilities
- Authority to act on behalf of any principal

A Raw Agent is analogous to an employee's underlying competencies (language skills, reasoning ability) before they have been trained for a specific role or granted authority to act.

### 2. Trained Agent: Configured with Knowledge and Skills

**Definition:** A Trained Agent is a Raw Agent that has been configured with organizational **Knowledge**, domain-specific **Skills**, defined **Responsibilities**, and a **Role** within the organization—but has not yet been granted authority to act in production.

Training transforms a Raw Agent's generic capabilities into domain-directed competencies through:

- **Knowledge binding:** Domain facts, organizational memory, relevant context, policies, and procedures.
- **Skill development:** Task-specific behaviors, problem-solving patterns, and tool usage proficiency.
- **System prompts:** Organization style, tone guidelines, and response format specifications.
- **Guardrails:** Prohibited behaviors and safety constraints that form immutable behavioral boundaries.
- **Tool specifications:** Schemas, descriptions, and usage policies for available tools.

Training is captured in a **Training Specification**—a declarative configuration that references versioned artifacts (guardrails, tool specs, knowledge bases) and defines the agent's behavioral envelope.

**What a Trained Agent does NOT have:**
- Credentials to access external systems
- Authority to act on behalf of users or roles
- Access tokens or delegated permissions
- Scope to specific work contexts

A Trained Agent knows *what* to do but is not yet authorized *to* do it.

### 3. Employed Agent: Delegated Authority

**Definition:** An Employed Agent is a Trained Agent that has been granted delegated authority, allocated to a specific work context, and assigned responsibilities—operating under controlled autonomy with a designated accountable human.

Employment transforms latent capability into operational authority through:

- **Work scope:** Project or team boundaries, temporal scope, and functional scope.
- **Operational environment:** Connection strings, credentials, and tool endpoints that make abstract training specifications concrete.
- **Capacity and resources:** Resource quotas, token limits, and budget allocation.
- **Authority delegation:** Either user delegation (agent acts as delegate of a specific user) or role delegation (agent represents an organizational role).
- **Constraints and policies:** Action limits, approval requirements, and escalation triggers.

**The critical constraint:** An Employed Agent may **never override the guardrails** set during Training. Employment can specialize behavior (narrow scope, add constraints, express preferences) but can never expand beyond what Training permits.

| Employment Can Do | Employment Cannot Do |
|-------------------|----------------------|
| Restrict tool access | Enable tools not in Training |
| Narrow scope of actions | Expand action authority |
| Add delegator preferences | Override Training guardrails |
| Set resource quotas | Remove safety constraints |
| Specify work context | Grant untrained capabilities |

## Lifecycle States and Transitions

Each layer has its own lifecycle states:

```
RAW AGENT:     [Developed] → [Built] → [Deployed] → [Running] → [Retired]
                                 │
                                 ▼ trained with
TRAINED AGENT: [Drafted] → [Validated] → [Published] → [Active] → [Archived]
                                 │
                                 ▼ employed as
EMPLOYED AGENT: [Requested] → [Approved] → [Active] → [Suspended] → [Revoked]
```

## Ownership and Responsibility

Each layer has distinct ownership:

| Layer | Owner | Approver | Accountable |
|-------|-------|----------|-------------|
| **Raw Agent** | Platform Team | Platform Lead + Security | Platform Lead |
| **Trained Agent** | Domain Team | Domain Lead + Compliance | Domain Lead |
| **Employed Agent** | Delegating Principal | Manager + Security | Manager (human) |

## Why This Decomposition Matters

The three-layer model provides several enterprise benefits:

1. **Clearer ownership:** Each layer has a distinct owner and change process.
2. **Proportionate governance:** Change management scales to the risk of each layer.
3. **Traceable audit:** Actions can be correlated through all three layers to an accountable human.
4. **Faster incident routing:** Issues are routed based on which layer is at fault.
5. **Explicit delegation:** Authority is bounded, constrained by Training, and revocable.
6. **Multi-tenant isolation:** Infrastructure (Raw Agent) can be shared while Training and Employment remain isolated per tenant.

---

**References:**
*   `aosm-meta-model/raw-trained-employed-agents.md`
*   `olympus-seer-docs/agentic-ai-concepts/designing-an-agent.md`
