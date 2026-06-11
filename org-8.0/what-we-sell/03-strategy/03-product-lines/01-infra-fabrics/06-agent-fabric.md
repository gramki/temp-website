# Chapter 03.01.06: Agent Fabric — Product Note

**The platform infrastructure for packaging, distributing, and governing AI agent workforces — enabling products to ship Swarms of agents as a core part of their value proposition.**

---

## The Architectural Problem

Products are evolving. Software alone is no longer the deliverable — products increasingly ship with AI agents that operate the software, handle exceptions, and resolve operational situations. But there is no infrastructure for this shift.

The consequences compound:

- **No infrastructure for product-embedded agents.** Products that want to ship AI capabilities must build their own agent packaging, distribution, and governance from scratch. There is no standard way to define what agents a product includes, how they are configured, or how customers can extend them.
- **No organizational model for agent workforces.** Agents are deployed as isolated entities with no structure. There is no equivalent of teams or organizational units for agents — no way to group agents by function, scope their visibility, or ship coherent agent capabilities as a unit.
- **Agent governance is reimplemented per-product.** Each product team builds its own lifecycle management, identity model, cost controls, and guardrails. Quality varies. Customers face inconsistent governance across the products they use.
- **Model access is ungoverned — cost explosion, security risk.** Teams provision their own model access, often with overly broad API keys. There is no visibility into which agents use which models, no cost attribution, and no circuit breakers. A runaway agent can drain budgets before anyone notices.
- **Agent identity is ad-hoc.** Agents operate through service accounts, shared credentials, or hardcoded API keys. There is no structured identity that distinguishes one agent from another, no way to trace actions to a specific agent, and no mechanism to revoke access without affecting others.
- **Customers cannot customize or extend.** When a product ships agents, customers cannot add their own agents alongside, extend product-shipped agents with custom skills, or tailor agent behavior to their context. Products are closed; agent capabilities are take-it-or-leave-it.

The result: products cannot ship AI agents as a governed, extensible capability. Agent deployment is either ad-hoc and risky, or blocked entirely by compliance teams who have no visibility into what "governed product-embedded AI" would even mean.

---

## What Agent Fabric Is

Agent Fabric is the platform infrastructure that enables products to ship AI agent workforces — providing the packaging, distribution, and governance layers that make product-embedded agents scalable, extensible, and compliant.

Agent Fabric introduces three foundational concepts:

- **The Agent Model** — a three-tier hierarchy that separates packaging (Raw Agents), configuration (Trained Agents), and runtime (Employed Agents). Each tier has distinct governance requirements and lifecycle characteristics.
- **Swarms** — organizational units for agents, analogous to teams for humans. Products ship Swarms scoped to specific work domains. Customers deploy, extend, or supplement product-shipped Swarms with their own.
- **Two-Layer Distribution** — platform and products ship standard agents and Swarms; customers extend or add their own. The same infrastructure supports both.

With Agent Fabric:

- Products define **Swarms of agents** scoped to specific work domains — not monolithic "AI features" but coherent agent teams with defined skills, guardrails, and accountability.
- Customers **deploy product-shipped Swarms**, extend them with custom Trained Agents, or add tenant-specific Swarms alongside — all governed through the same infrastructure.
- Agent identity, authority, model access, guardrails, and operations are **structurally governed** — consistently across all products and all agents.
- Credentials are **never exposed to agents** — the platform injects them at runtime, eliminating credential sprawl and enabling centralized revocation.

Agent Fabric absorbs and extends what was previously called Seer — the AI agent runtime and governance layer — into a complete platform for product-embedded agent workforces.

---

## The Agent Model

Agent Fabric manages agents through a three-tier model that separates concerns cleanly:

| Tier | Name | What It Is | Governance Focus |
|------|------|------------|------------------|
| **Packaging** | Raw Agent | The deployable agent engine — an OCI container packaging an agent system (its orchestration, tool use, context management, and model access). Examples: Codex, Cursor Agent, Claude Code | Which agent systems are approved? Which versions? |
| **Configuration** | Trained Agent | A manifest that binds a Raw Agent to a Swarm with configured skills, guardrails, and evaluation criteria. The Trained Agent defines how an agent should behave in a specific role | What skills does this agent have? What are its boundaries? Who owns it? |
| **Runtime** | Employed Agent | A running instance — a Trained Agent paired with a delegation token, executing in a workspace session with scoped authority and quota | What is this agent doing right now? At what cost? Under whose authority? |

The separation matters:

- **Raw Agents** can be shared across many Trained Agents — the same engine configured for different roles
- **Trained Agents** are configuration, not running processes — they define behavior; they don't consume resources until employed
- **Employed Agents** are ephemeral — they run, complete their work, and terminate. Governance attaches at employment time

---

## Swarms — Organizational Units for Agents

Swarms are organizational units for agents — analogous to teams or departments for humans. Just as human users belong to teams, Trained Agents belong to Swarms.

```
Organization
├── Human Teams
│   ├── Dispute Resolution Team
│   ├── Fraud Investigation Team
│   └── Compliance Review Team
└── Agent Swarms
    ├── Dispute Resolution Swarm
    ├── Fraud Triage Swarm
    └── Compliance Screening Swarm
```

### What Products Ship

Products ship Swarms scoped to narrow work domains — not one giant swarm for "all card operations" but focused swarms for specific operational concerns:

| Product | Shipped Swarms |
|---------|----------------|
| Cards Product | Dispute Investigation Swarm, Chargeback Processing Swarm, Fraud Alert Triage Swarm, Limit Exception Review Swarm |
| Payments Product | Payment Failure Resolution Swarm, Reconciliation Exception Swarm, Return Processing Swarm |
| Compliance Hub | SAR Drafting Swarm, Screening Alert Triage Swarm, Periodic Review Swarm |

Narrow scoping matters:

- **Clear accountability** — each Swarm has defined ownership and governance
- **Domain-specific skills** — agents in a Swarm share context, skills, and guardrails appropriate to their work domain
- **Customer choice** — customers deploy the Swarms they need, not all-or-nothing
- **Independent versioning** — Swarms evolve independently; upgrading one doesn't force upgrading all

### Swarm Visibility Hierarchy

Swarms exist at four scopes, forming a visibility hierarchy:

| Scope | Visible To | Example |
|-------|------------|---------|
| **Platform Swarm** | All products, all customers | Platform-shipped agent teams (Build, Review, Test) |
| **Product Swarm** | Customers using that product | Product-shipped domain swarms |
| **Organization Swarm** | That customer organization | Customer-defined swarms |
| **Workspace Swarm** | That workspace only | Team-specific agents |

Lower scopes inherit visibility of higher-scope Swarms. A customer workspace can see: its own Swarms + organization Swarms + product Swarms + platform Swarms.

---

## Two-Layer Distribution

Both Raw Agents and Swarms follow a two-layer distribution model:

| Layer | Raw Agents | Swarms |
|-------|------------|--------|
| **Platform/Product-shipped** | Standard agent engines (Codex, Cursor Agent, Claude Code) | Domain-specific Swarms shipped with products |
| **Customer-extended** | N/A | Add Trained Agents to product-shipped Swarms |
| **Customer-added** | Custom agent engines for specialized needs | Organization-specific Swarms |

This model enables:

- **Products ship governed defaults** — customers get working agent capabilities out of the box
- **Customers extend, not fork** — add Trained Agents to product Swarms rather than rebuilding
- **Customization is governed** — customer-added agents use the same infrastructure, same governance, same auditability

---

## Capability Domains

The platform capabilities that make product-embedded agent workforces possible.

### 1. Agent Lifecycle Management

The complete lifecycle of agents across the three-tier model — from Raw Agent registration through Trained Agent configuration to Employed Agent runtime — with visibility and control at every stage.

| Capability | What It Delivers |
|---|---|
| Agent registry | Authoritative catalog of all enterprise agents — what they do, who owns them, what version is deployed, and what lifecycle stage they occupy. No agent operates without registry entry |
| Lifecycle stages | Structured progression — Raw (base model capability), Trained (domain-specialized), Employed (assigned to a specific role and context). Each stage carries different authority levels and governance requirements |
| Version management | Explicit versioning of agent configurations, prompts, and capabilities — with audit trails showing what changed, when, and why. Multiple versions can coexist; rollback is a configuration change |
| Deployment governance | Controlled deployment pipelines with approval workflows, staged rollouts, and automatic rollback triggers. No agent goes live without passing governance gates |
| Retirement process | Governed decommissioning — credential revocation, access removal, audit trail preservation, and knowledge transfer. Agents don't just stop running; they are formally retired |
| Ownership and accountability | Every registered agent has a designated owner and an accountable human. Ownership transfers are explicit and audited. No orphan agents |

The registry is not documentation — it is the source of truth for agent existence. If an agent is not in the registry, it does not run in the enterprise.

### 2. Agent Identity and Authority

Enterprise-grade identity for AI agents — not service accounts repurposed, but structured identities with explicit delegation, bounded authority, and traceable human accountability.

| Capability | What It Delivers |
|---|---|
| Structured agent identity | Two-layer identity model — Business Identity (the agent's persona, role, and domain context) and Deployment Identity (the technical runtime identity). The business identity persists across deployment changes |
| Authority delegation | Explicit delegation from a human or role to an agent, with inherited permissions and clear boundaries. The agent's authority is always derived — never self-asserted — and the delegation chain is auditable |
| Mandatory human accountability | Every agent, regardless of autonomy level, has a designated accountable human. The accountability chain is maintained through delegation changes, role reassignments, and agent lifecycle transitions. No agent operates without a human answerable for its actions |
| Context-specific permissions | Agent permissions configured per enforcement point — what an agent is permitted to do varies by the system, workflow, or domain it operates in. Permissions follow the agent's employment context |
| Credential lifecycle | Dedicated credentials for agents — virtual keys, scoped tokens, cryptographic identities — with managed issuance, rotation, injection, and revocation. Agent credentials are never shared, never static, and independently revocable |
| Delegation boundary enforcement | Hard limits on what delegated authority permits — preventing authority escalation, constraining scope to the delegating principal's own permissions, and enforcing that agents cannot delegate further without explicit policy |

The trust challenge with AI agents is not authentication — it is authorization and accountability. Agent Fabric extends enterprise identity governance to agents: who this agent is, who authorized it, what it may do, and who is accountable when it acts.

### 3. Model Access Management

Centralized governance of how agents access language models — with registry, policy enforcement, cost controls, and usage visibility that replace ungoverned API key sprawl.

| Capability | What It Delivers |
|---|---|
| Model registry | Authoritative catalog of approved models — which models are available, which versions, from which providers, and under what conditions. Unapproved models cannot be accessed |
| Access policies | Fine-grained control over which agents can access which models — based on agent classification, use case, sensitivity level, and cost tier. Access is granted, not assumed |
| Cost controls | Per-agent cost budgets with real-time tracking, alerting at thresholds, and automatic throttling or circuit breaking when limits are exceeded. Cost overruns are prevented, not discovered |
| Rate limiting | Request rate controls at the agent level — preventing runaway inference, protecting shared quotas, and ensuring fair allocation across enterprise agents |
| Usage visibility | Comprehensive telemetry on model usage — tokens consumed, latency, error rates, and cost — attributed to specific agents and aggregated for enterprise reporting |
| Provider abstraction | Unified interface across model providers — OpenAI, Anthropic, Azure, self-hosted — with consistent policy enforcement regardless of where the model runs. Switching providers is a configuration change |

Model access governance closes the gap between "we have an API key" and "we have governed AI." Every model invocation is policy-checked, cost-attributed, and auditable.

### 4. Guardrails and Governance

Enterprise-wide behavioral boundaries for AI agents — policy-defined, structurally enforced, and consistently applied rather than reimplemented per-agent.

| Capability | What It Delivers |
|---|---|
| Input validation | Policy-driven validation of all inputs to agents — filtering prompt injection attempts, detecting sensitive data exposure, and enforcing content policies before the model sees anything |
| Output filtering | Policy-driven filtering of agent outputs — detecting hallucinations, blocking prohibited content, redacting sensitive information, and enforcing response constraints before outputs reach consumers |
| Behavioral boundaries | Configurable limits on agent behavior — scope of actions permitted, topics allowed, assertion confidence thresholds, and interaction patterns. Boundaries are structural, not prompt-based |
| Escalation triggers | Defined conditions that force human intervention — confidence below threshold, high-stakes decision detected, anomalous behavior, or explicit escalation request. Agents escalate; they don't proceed blindly |
| Policy versioning | Guardrail policies are versioned, auditable, and deployable across agents. Policy changes roll out consistently; compliance posture is provable at any point in time |
| OPD assessment | Every agent is assessed across three dimensions: Observability (can we see what it's doing?), Predictability (does it behave within expected bounds?), and Directability (can we steer or stop it?). All three must be satisfied for enterprise deployment |

Guardrails are not suggestions embedded in prompts. They are enforcement infrastructure that operates between agents and the systems they interact with — applied consistently, logged completely, and auditable by design.

### 5. Agent Operations

Operational visibility and control for AI agents as first-class enterprise entities — with monitoring, diagnostics, and intervention capabilities that treat agents like the production services they are.

| Capability | What It Delivers |
|---|---|
| Agent monitoring | Real-time visibility into agent health, performance, and behavior — request volumes, latency distributions, error rates, and resource consumption. Agents have SLOs and SLIs like any service |
| Behavioral observability | Detailed logging of agent reasoning, tool invocations, and decision paths — not just inputs and outputs, but the chain of thought that led to actions. Explainability is operational, not post-hoc |
| Anomaly detection | Automated detection of behavioral deviation — unusual patterns, unexpected outputs, performance degradation, or interaction anomalies. Alerts surface before users complain |
| Intervention controls | Operational levers to pause, throttle, redirect, or stop agents — individually or by category. When something goes wrong, operators can act immediately without code changes |
| Diagnostic tooling | Investigation capabilities for agent failures — replay of interactions, comparison with expected behavior, and root cause analysis. Debugging agents is a supported workflow |
| Incident integration | Agent incidents feed into enterprise incident management — with automatic escalation, runbook integration, and post-incident review processes. Agent failures are first-class incidents |

Agent operations is not a dashboard bolted on after deployment. It is the operational surface through which the enterprise manages its AI workforce — with the same rigor applied to any production system.

### 6. Tool and Integration Contracts

Governed access to enterprise capabilities — through declared tool contracts that define what agents can do, how they do it, and under what conditions.

| Capability | What It Delivers |
|---|---|
| Tool registry | Catalog of capabilities agents can invoke — APIs, data sources, actuators, and services — with declared contracts specifying inputs, outputs, side effects, and governance requirements |
| Tool contracts | Structured definitions of what each tool does, what permissions it requires, what data it accesses, and what audit obligations it carries. Tools are not APIs; they are governed capabilities |
| Access governance | Per-tool authorization determining which agents can invoke which tools under which conditions. Access follows the agent's identity, role, and current context |
| Invocation audit | Complete audit trail of tool invocations — what was called, with what parameters, by which agent, in what context, and with what result. Every action is traceable |
| Context assembly | Structured context compilation for each agent invocation — assembling the right domain knowledge, entity relationships, applicable rules, and tool contracts. Agents operate with full domain context, not generic prompts |
| MCP integration | Native support for Model Context Protocol — enabling agents to access enterprise capabilities through a standardized interface that is inherently auditable and governable |

The tool contract is the boundary between agent autonomy and enterprise governance. Agents can do what their contracts permit, invoking tools they are authorized to use, with complete visibility into every action.

---

## Regulatory Alignment

Agent Fabric is designed to meet emerging regulatory requirements for AI governance from a unified architectural surface.

| Regulation | Relevant Capabilities |
|---|---|
| EU AI Act | Agent registry, human accountability, transparency logging, risk assessment, intervention controls |
| AI governance frameworks | Lifecycle management, guardrails, behavioral boundaries, audit trails |
| Financial services AI guidance | Cost controls, model governance, explainability, human oversight requirements |
| Data protection (GDPR/CCPA/DPDP) | Input/output filtering, data minimization, consent enforcement integration |
| Model risk management (SR 11-7) | Model registry, version control, validation workflows, ongoing monitoring |
| Operational resilience | Monitoring, incident management, intervention capabilities, recovery procedures |

Each regulatory requirement maps to capabilities present in the fabric. Compliance becomes demonstrable by design, not constructed per-audit.

---

## Architectural Position

Agent Fabric occupies a foundational layer in the enterprise architecture:

| Layer | Agent Fabric Role |
|---|---|
| **Product Enablement** | The infrastructure that allows products to ship agent workforces. Products define Swarms; Agent Fabric packages, distributes, and governs them |
| **Agent Control Plane** | The governance infrastructure for all agents — lifecycle, identity, authority, model access, guardrails, and operations — applied consistently across product-shipped and customer-added agents |
| **Runtime Integration** | Connection point between agents and enterprise systems — tool contracts, context assembly, and credential injection. Agents access capabilities through Agent Fabric, not around it |
| **Observability Surface** | The operational view of the enterprise's AI workforce — performance, behavior, cost, and compliance state across all agents |

Agent Fabric is the platform that makes product differentiation through AI agents possible. As products evolve to ship agent workforces as core value propositions, Agent Fabric provides the infrastructure that makes this shift governed, extensible, and scalable.

---

## Relationship to Other Fabrics

Agent Fabric integrates with other fabrics — and enables them to ship their own Swarms:

| Fabric | Relationship |
|---|---|
| **Trust Fabric** | Provides the identity, authentication, and delegation infrastructure that Agent Fabric builds on. Agent identity is a specialized extension of Trust Fabric's identity model |
| **Evolution Fabric** | Provides the operational context in which agents work — Hubs, Scenarios, Teams, and domain models. Swarms shipped by products operate within Evolution Fabric's operational substrate |
| **Memory Fabric** | Provides the institutional memory that agents access and contribute to — decision context, action history, and organizational knowledge |
| **Truth Fabric** | Provides the semantic layer that grounds agent actions in shared definitions. When an agent references "credit limit" or "dispute status," Truth Fabric ensures consistent meaning |
| **Cognition Fabric** | Provides the events and signals that trigger agent action — the perception layer that feeds Swarms with the situations they need to address |

Agent Fabric governs the agents. The other fabrics provide the context, meaning, memory, and operational substrate in which those agents work — and each fabric can ship its own Swarms for domain-specific agent capabilities.

---

## References

- [Agent Fabric Platform Documentation](../../../../foundry/foundry-platform/agent-fabric/README.md) — Technical architecture, registries, and implementation details
- [Evolution Fabric](./04-evolution-fabric.md) — The operational layer for banking domains
- [Trust Fabric](./01-trust-fabric.md) — Enterprise trust layer including AI agent identity foundations
- [Memory Fabric](./07-memory-fabric.md) — Institutional memory and decision reconstruction
- [The Thesis](../../../02-the-thesis/README.md) — The structural argument for enterprise AI infrastructure

> **Agent Fabric is the infrastructure that enables products to ship AI agent workforces — governed by design, extensible by customers, and differentiated by the Swarms they deliver.**
