# ADR-0109: Seer Raw Agent Subsystems Design

**Status**: Accepted  
**Date**: 2026-01-12  
**Category**: seer

---

## Context

Three subsystems collectively define a Raw Agent: **Context Compiler**, **Seer Agent SDK**, and **Raw Agent Lifecycle Manager**. These subsystems needed comprehensive C2-level (Container) design documentation following the Seer Sidecar pattern.

Key design questions that needed resolution:

1. **Context Compilation**: How should context be compiled from multiple sources? How should agent code interact with Training Specs? How should tools influence context compilation?
2. **SDK Design**: Should the SDK support multiple languages? How should prompts be selected based on autonomy levels? Should framework-specific APIs be provided?
3. **Raw Agent Lifecycle**: Are Raw Agents directly deployable? What capabilities should be structured? How should identity be managed?

---

## Decision

We completed the detailed design for three Raw Agent subsystems with the following architectural decisions:

### Context Compilation Architecture

#### Request-Update-Based Retriever Configuration

| Decision | Rationale |
|----------|-----------|
| **Training Specs declaratively define retriever configurations** | Agent code precedes Training Spec; agent code cannot be training-aware |
| **Selectors match request update metadata** | Enables automatic configuration selection based on update type, task type, context keys, etc. |
| **Context Compiler automatically selects and merges matching configurations** | Decouples agent code from Training Spec details; enables flexible context strategies |

**Example Selector Pattern**:
```yaml
retrieverConfigs:
  - selector:
      updateType: "task_created"
      taskType: "fraud_investigation"
    retrievers:
      - type: memory.precedent
        query: "fraud investigation cases"
      - type: knowledge.search
        knowledgeBase: "fraud-policies"
```

#### Hub Request Context with Ancestry Topology

| Decision | Rationale |
|----------|-----------|
| **Agents can access context from all requestors in ancestry** | Enables agents to leverage parent/ancestor request context (extends ADR-0066) |
| **Filtered by agent goal and role** | Ensures agents only access relevant context from ancestry |
| **Full request hierarchy topology included** | Provides complete context lineage for agent reasoning |

#### Tool-Aware Context Compilation

| Decision | Rationale |
|----------|-----------|
| **Available tools incorporated into context constraints** | Tools define what actions are possible, influencing what context is relevant |
| **Tools influence retrieval/ranking** | Context retrieval prioritizes information relevant to available tool capabilities |
| **Tool capabilities from Training/Employment Specs** | Tool availability is known at context compilation time |

#### Four-Source Context Model

| Source | Description |
|--------|-------------|
| **Enterprise Knowledge** | Policies, procedures, documentation (via Knowledge Services) |
| **Enterprise Memory** | Precedents, case history, organizational memory (via CAF) |
| **Agent Memory** | Session-scoped conversation, KV, documents (via Agent Memory Services) |
| **Hub Request Context** | Current request state, ancestry topology, request history |

### SDK Design

#### Dual Language Variants

| Decision | Rationale |
|----------|-----------|
| **Python SDK and Java SDK** | Supports developers using different language ecosystems |
| **Both SDKs for Raw Agent developers** | Consistent API surface across languages |
| **Language-appropriate implementation patterns** | Respects language idioms and conventions |

#### Autonomy Level-Based Prompt Selection

| Decision | Rationale |
|----------|-----------|
| **Prompts tagged with autonomy level in Training Specs** | Full, Suggest, Ask, Watch (from `apo.md`) |
| **Prompts used at tagged level or lower** | Higher autonomy levels can use lower-level prompts |
| **Exclusive prompts can be tagged for specific levels** | Some prompts only applicable at specific autonomy levels |

**Autonomy Levels**:
- **Full**: Agent acts without human review
- **Suggest**: Agent recommends, human decides
- **Ask**: Agent must get approval before acting
- **Watch**: Human acts, agent observes only

#### Framework Convenience APIs

| Language | Framework Support | Rationale |
|----------|-------------------|-----------|
| **Python** | LangGraph, Strands, OpenAPI builders | Popular Python agent frameworks |
| **Java** | Framework-agnostic patterns | Java ecosystem has diverse frameworks; avoid framework lock-in |

### Raw Agent Lifecycle

#### Raw Agents Are Not Deployable

| Decision | Rationale |
|----------|-----------|
| **Only Employed Agents are deployable** | Raw Agents lack organizational knowledge and operational authority |
| **Raw Agents are containers referenced by Employed Agents** | Raw Agents define technical capabilities only |
| **Referenced through Training Specs** | Training Specs bind Raw Agents with organizational knowledge |

#### Structured Capabilities

| Capability Type | Description |
|----------------|-------------|
| **Tool calling** | Tools the agent can invoke |
| **Orchestration** | Ability to coordinate other agents/tools |
| **Archetype roles** | Thinker, Doer, Orchestrator, Governor |
| **Prompt tags** | Tags for Authority Enforcement |
| **Documentation references** | Links to agent documentation |

#### Identity Structure

| Identity Section | Contents |
|-----------------|----------|
| **Raw Agent Identity** | Name, version, container image reference, capabilities summary |
| **Trained Agent Identity** | Training spec name, version, training spec reference |
| **Employed Agent Profile** | Contains explicit sections for both Raw Agent and Trained Agent identities |

---

## Consequences

### Positive

- **Decoupled agent code from Training Specs** — Request-update-based retriever configuration enables flexible context strategies without agent code changes
- **Comprehensive context model** — Four-source model provides rich context for agent reasoning
- **Tool-aware compilation** — Context relevance improved by considering available tool capabilities
- **Language flexibility** — Dual SDK variants support diverse developer ecosystems
- **Clear lifecycle boundaries** — Raw/Trained/Employed distinction clarifies responsibilities and deployability
- **Structured capabilities** — Typed capabilities enable better discovery, validation, and composition

### Negative

- **Additional complexity** — Request-update-based configuration requires selector matching logic
- **SDK maintenance overhead** — Two language variants require parallel maintenance
- **Context compilation latency** — Four-source compilation may increase latency (mitigated by caching and parallel retrieval)

### Neutral

- **Implementation details deferred** — Specific ranking algorithms, token budget strategies, caching policies left to implementation
- **Framework support** — Python framework builders may create lock-in; Java framework-agnostic approach avoids this

---

## Documents Created

### Context Compiler (3 files)
| Document | Description |
|----------|-------------|
| `compilation-service.md` | Core Context Compilation Service design with four-source model, request hierarchy, tool-aware compilation, retriever configuration |
| `SCOPE.md` | Subsystem scope and coverage |
| `README.md` | Overview, architecture, design documents table, key decisions |

### Seer Agent SDK (14 files)
| Document | Description |
|----------|-------------|
| `python-sdk/` (6 files) | Employment Spec, Prompt, Context Compiler, Observability, Hub Integration, Framework APIs |
| `java-sdk/` (6 files) | Same API coverage as Python SDK |
| `SCOPE.md` | Subsystem scope and coverage |
| `README.md` | Overview, architecture, design documents table (organized by language), key decisions |

### Raw Agent Lifecycle Manager (6 files)
| Document | Description |
|----------|-------------|
| `raw-agent-spec-manager.md` | Raw Agent CRD structure, capabilities, identity |
| `raw-agent-directory.md` | Registry, capability discovery, versioning |
| `raw-agent-operators.md` | Lifecycle management, registration, validation |
| `raw-agent-levers.md` | Capability toggles, deprecation, emergency controls |
| `SCOPE.md` | Subsystem scope and coverage |
| `README.md` | Overview, architecture, design documents table, key decisions |

---

## Related

- [ADR-0066](./0066-request-hierarchy-context-inheritance.md) — Request hierarchy and context inheritance (extended by Hub Request Context with ancestry topology)
- [ADR-0074](./0074-seer-runtime-atlantis-based.md) — Seer runtime on Atlantis
- [ADR-0104](./0104-seer-agent-runtime-detailed-design.md) — Agent Runtime detailed design
- [Context Compiler Subsystem](../../olympus-seer-docs/seer-design/subsystems/context-compiler/README.md)
- [Seer Agent SDK Subsystem](../../olympus-seer-docs/seer-design/subsystems/seer-agent-sdk/README.md)
- [Raw Agent Lifecycle Manager Subsystem](../../olympus-seer-docs/seer-design/subsystems/raw-agent-lifecycle-manager/README.md)
- [Autonomy Levels](../../olympus-hub-docs/01-concepts/apo.md)
