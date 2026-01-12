# 1.1 The Two-System Architecture: Seer + Hub

The Seer platform does not operate in isolation. It exists in a carefully designed partnership with Olympus Hub, where each system owns distinct responsibilities. Understanding this division is essential for architects evaluating the platform and for engineers implementing agents.

## The Fundamental Division

The relationship between Seer and Hub can be summarized in a single statement:

> *Seer governs the agents; Hub governs the operations they perform.*

| Dimension | Olympus Seer | Olympus Hub |
|-----------|--------------|-------------|
| **Focus** | The Agent | The Work |
| **Owns** | Agent lifecycle, identity, runtime, AI models | Operations, memory, knowledge, tools, audit |
| **Metaphor** | The engine that runs agents | The factory floor where work happens |
| **Question** | *How do we manage agents?* | *What do agents work with?* |

## What Seer Provides

Seer is the **agent control plane and runtime**. It answers the question: *How do we build, deploy, govern, and run AI agents at enterprise scale?*

### Core Capabilities

| Capability | Description |
|------------|-------------|
| **Agent Lifecycle Management** | Agents as versioned products with Training Specs, Employment Specs, state management, and rollback |
| **Identity & Authority** | Agent identity distinct from users; explicit delegation; authority ceilings; kill switches |
| **Context Assembly** | Reproducible, auditable context compilation from memory, knowledge, and session state |
| **Runtime Execution** | Policy enforcement on every request; graceful degradation; multi-cloud portability |
| **Observability** | Runtime traces, metrics, health monitoring |
| **Evaluation** | Development-time testing, benchmarks, CI/CD quality gates |
| **Model Gateway** | Unified access to LLMs across providers; model routing and failover |

### Seer Subsystems

| Subsystem | Function |
|-----------|----------|
| **Agent Definition & Lifecycle Service** | Versioning, Training/Employment Specs, state management |
| **Agent Identity & Authority Framework** | Agent identity, delegation chains, authority enforcement |
| **Context Assembly Engine** | Context compilation from memory, knowledge, session state |
| **Runtime & Deployment Abstraction** | Agent execution, policy enforcement, graceful degradation |
| **Agent Observability Service** | Runtime metrics, logs, traces |
| **Agent Test Runner** | Testing, behavior/health/safety validations, quality gates |
| **Model Gateway** | Unified LLM access, routing, fallback |

## What Hub Provides

Hub is the **operational substrate**. It provides the infrastructure that agents operate within—the knowledge they consult, the memory they access, the tools they invoke, and the audit fabric that records their decisions.

### Hub Subsystems Used by Seer Agents

| Hub Subsystem | What Agents Use It For |
|---------------|------------------------|
| **Memory Services** | Episodic, Semantic, Preference, Procedural memory storage and access |
| **Knowledge Integration (RAG)** | Authoritative information retrieval with provenance |
| **Tool & Action Framework** | Tool registry, permissions, execution sandbox |
| **Cognitive Audit Fabric (CAF)** | Decision records, explanations, evidence packaging |
| **Secrets & Credentials** | Secure access to external systems |

## Why Two Systems?

The separation between Seer and Hub is not arbitrary. It reflects fundamental differences in concern:

### Separation of Concerns

**Seer's concerns** are agent-centric:
- How is an agent defined, trained, and deployed?
- Who is this agent, and what authority does it have?
- Is the agent healthy, and how is it performing?
- Which models can this agent use?

**Hub's concerns** are operation-centric:
- What knowledge does the organization have?
- What happened, and why (memory)?
- What tools are available, and who can use them?
- How do we audit and explain decisions?

### Independent Evolution

Seer and Hub can evolve independently:
- New agent capabilities (reasoning patterns, coordination protocols) can be added to Seer without changing Hub.
- New operational capabilities (tool types, memory patterns, audit requirements) can be added to Hub without changing Seer.

### Clear Accountability

When issues arise, the division helps identify the responsible system:
- Agent behaving incorrectly? Seer (training, guardrails, runtime).
- Wrong information provided? Hub (knowledge, memory).
- Tool failure? Hub (tool registry, execution).
- Authorization issue? Seer (identity, authority) + Hub (tool permissions).

## The Integration Surface

Seer and Hub integrate through well-defined interfaces:

### Seer → Hub

- **Memory access:** Agents read and write memory through Hub Memory Services.
- **Knowledge retrieval:** Agents query knowledge through Hub's RAG infrastructure.
- **Tool invocation:** Agents call tools registered in Hub's Tool Registry.
- **Audit recording:** Agent decisions are recorded in Hub's Cognitive Audit Fabric.

### Hub → Seer

- **Agent enrollment:** Hub Workbenches enroll Seer agents as participants.
- **Task assignment:** Hub's task management can assign work to Seer agents.
- **Signals:** Business signals routed through Hub can trigger Seer agent activity.

---

**References:**
*   `olympus-seer-docs/seer-design/introduction.md`
*   `olympus-seer-docs/seer-design/premise.md`
