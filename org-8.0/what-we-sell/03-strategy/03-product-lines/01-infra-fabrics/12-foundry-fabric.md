# Chapter 03.01.12: Foundry Fabric — Product Note

**An enterprise metadata compilation and session orchestration layer that enables banks to author, validate, deploy, and evolve their own custom fabrics, domain hubs, and agentic workflows — transforming the bank from a consumer of fixed software suites into an active builder of autonomous financial systems.**

---

## The Architectural Problem

Traditional enterprise banking systems operate as closed, proprietary monoliths or rigid black-box application suites. When a bank needs to introduce a new financial instrument (requiring a new System of Record), modify a complex operational procedure (requiring an altered Hub Scenario), or integrate a novel third-party API (requiring a custom Machine contract), they get trapped in expensive, multi-year vendor delivery cycles.

The consequences compound:
- **No extensibility for custom domains:** If a bank wants to ship a niche product line (e.g., Agricultural Micro-lending or Green Energy Financing), they cannot model it cleanly as a first-class fabric or hub. They must hack the logic into custom fields inside standard deposit or loan ledgers.
- **Tightly coupled operational logic:** Workflows, business rules, and UI behaviors are hardcoded into specific systems. There is no horizontal "compiler" that separates the declaration of a business process (such as an onboarding scenario) from the underlying transactional ledgers.
- **Untrained, blind AI integration:** Developers try to write custom wrappers or point-to-point integrations to connect LLM agents to core systems. Because they lack a secure, unified sandbox environment and a standardized "Tool Contract" protocol (like the Model Context Protocol, or MCP), these agents act blindly, fail frequently, and cannot be governed or audited.
- **Development sandbox fragmentation:** Testing a change requires synchronizing multiple staging databases, legacy core configurations, and visual channels. There is no unified, containerized workspace environment where developers, business analysts, and AI agents can collaborate to test and validate changes safely.

The result: banks are paralyzed. The system of record (the ledger) remains a bottleneck, preventing the bank from evolving its business operations to meet rapidly changing competitor and consumer needs.

---

## What Foundry Fabric Is

Foundry Fabric is the horizontal, domain-neutral meta-compilation and execution fabric. It provides the **Agent-Centric Engineering (ACE)** platform that empowers bank development and product teams to safely author, validate, and execute custom Banking Fabrics, specialized Domain Hubs, and custom-tailored Agent Swarms.

Instead of writing custom point-to-point code, developers and business analysts declare models using a standardized, git-governed schema language. Foundry Fabric compiles these declarative files into active, running operational systems:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          FOUNDRY FABRIC (META-ENGINE)                   │
│                                                                         │
│   ┌───────────────────────────┐           ┌──────────────────────────┐  │
│   │   Foundry Definition      │           │    Foundry IDE &         │  │
│   │   Repository (Git Schemas)│──────────>│    Workspace Services    │  │
│   │   - Tracks custom Hubs    │           │    - Hardened Sandboxes  │  │
│   │   - Validates invariants  │           │    - Scenario Authoring  │  │
│   └───────────────────────────┘           └────────────┬─────────────┘  │
│                                                        │                │
│                                                        ▼                │
│                                           ┌──────────────────────────┐  │
│                                           │    Work Order Runtime    │  │
│                                           │    (In-Session Spawning) │  │
│                                           └────────────┬─────────────┘  │
└────────────────────────────────────────────────────────┼────────────────┘
                                                         │
                                                         ▼ (Compiles & Runs)
                                            ┌──────────────────────────┐
                                            │ BANK'S CUSTOM SYSTEMS    │
                                            │ - Custom SOR Fabrics     │
                                            │ - Specialized Hubs       │
                                            └──────────────────────────┘
```

By running on Foundry Fabric, banks unlock:
- **Declarative System Creation:** New Banking Fabrics (Systems of Record) and custom Hubs are defined entirely in Git as high-level metadata (using the Universal Product Information Model, or UPIM, schema structure), which the fabric validates and instantiates.
- **Durable Sandbox Workspaces:** Spin up containerized, isolated Kubernetes-based workspaces where developers and AI agents collaborate on identical codebases, repositories, and tool contracts.
- **Pre-Integrated Tool Routing:** Translates declarative Machine declarations into secure, network-isolated Model Context Protocol (MCP) servers, giving authorized Agent Swarms instant, governed access to ledger tools.
- **Automated Work-Order Execution:** Coordinates the movement of "Product Intent" (requirements, code, design, test results) across specialized workspaces, using automated Governance Scenarios to audit every step.

---

## Source of Truth

- **Entities Owned:** Work Catalogues, Workbenches, Workshop Sessions, Repositories, Workspaces, Work Orders, Scenario Declarations, Tool Contracts, Session Pod Configurations.
- **Key Invariants:**
  - No custom fabric or hub configuration can be compiled without passing strict UPIM metadata validation rules.
  - Every agent-spawned process and tool execution must be cryptographically bound to a validated Work Order session token.
  - Development and testing environments (Workshop sessions) must run in isolated, rate-throttled containers with zero direct access to production ledgers.
- **Configurable vs. Compliance Floor:**
  - *Configurable:* Workspace types, custom scenario definitions, tool schema mappings, and container base images.
  - *Compliance Floor:* Immutable logging of all tool invocations, SPIFFE-based agent identity validation, and hard isolation of multi-tenant sessions.

---

## Capability Domains

### 1. Foundry Definition Repository

The authoritative administrative plane that manages Tenancy, Work Catalogues, and metadata schemas in Git.

| Capability | What It Delivers |
|---|---|
| **Schema Validator** | Performs automated validation of bank-authored fabric, hub, and scenario declarations, checking syntactic completeness and verifying compliance rules. |
| **Catalog Manager** | Governs the publishing, versioning, and distribution of Work Catalogues, allowing banks to roll out new or refined Streams, Loops, and Scenarios. |
| **Workbench Provisioner** | Coordinates the provisioning of new Workbenches and links them to their corresponding product configurations. |

### 2. Workspace Session Infrastructure

Containerized, secure runtime environments where human-agent teams collaborate.

| Capability | What It Delivers |
|---|---|
| **Session Pod Controller** | Dynamically spins up and tears down isolated, Kubernetes-hosted developer workspaces, allocating CPU/GPU quotas. |
| **Agent-IDE Connector** | Exposes a secure visual interface (Web IDE and workspaces panels) letting human developers inspect running agent loops, view task queues, and edit code. |
| **Network Gatekeeper** | Enforces hard egress/ingress boundaries on active sessions, preventing data leakage while allowing secure proxying to authorized APIs. |

### 3. Work Order Runtime

The execution engine that handles in-session task orchestration, context compilation, and multi-agent execution.

| Capability | What It Delivers |
|---|---|
| **Context Compiler** | Dynamically gathers the relevant file segments, repository states, and chat threads to build a unified context vector before spawning an agent. |
| **In-Session Spawner** | Spawns specialized "think" or "do" agents bound to specific tasks, injecting their scoped SPIFFE credentials and Tool Contracts. |
| **Task State Ledger** | Tracks the real-time execution of task items, managing retries, timeouts, and compensatory rollbacks when a tool call fails. |

### 4. Foundry Orchestrator

The coordination plane that manages the lifecycle of Product Intent and enforces verification gates.

| Capability | What It Delivers |
|---|---|
| **Intent Router** | Manages the movement of Product Intent (specifications, assets, code, tests) across functional workspaces (Specification, UX, Dev, QA, Release). |
| **Governance Scenario Engine** | Automatically invokes verification and compliance checks when a Work Order transitions, gathering and logging immutable evidence. |

---

## Boundaries and Adjacencies

| Adjacent Fabric / Hub | Consumed Interface / Relationship |
|---|---|
| **Agent Fabric** | *Fabric Consumed*. Foundry Fabric consumes Agent Fabric to govern the lifecycle, registry, and quota limits of agents spawned inside workspaces. |
| **Evolution Fabric** | *Fabric Consumed*. Foundry Fabric deploys compiled Workbenches and Hubs natively onto the Evolution Fabric, executing their active Scenarios. |
| **Cloud Fabric** | *Adjacent Fabric*. Exposes K8s cluster telemetry, resource metrics, and pod usage metrics to the Session Pod Controller. |
| **Trust Fabric** | *Adjacent Fabric*. Validates user and developer SSO tokens, federates workspace IAM, and manages identity-binding for external tool-calling. |

---

## References

- [Agent Fabric](./06-agent-fabric.md) — Multi-agent registration and control
- [Evolution Fabric](./04-evolution-fabric.md) — Bounded runtime and orchestration
- [Quark — Domain Hubs for Banking](../04-product-lines/05-quark.md) — Open, modular hubs extensible via Foundry Fabric
