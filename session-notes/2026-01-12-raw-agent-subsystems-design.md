# Session Notes: Raw Agent Subsystems Design

**Date**: 2026-01-12  
**Focus**: Creating C2-level (Container) design documentation for Context Compiler, Seer Agent SDK, and Raw Agent Lifecycle Manager subsystems

---

## Objective

Create comprehensive design documentation for three subsystems that collectively define a Raw Agent:
1. **Context Compiler** — Four-source context compilation service
2. **Seer Agent SDK** — Python and Java SDKs for Raw Agent developers
3. **Raw Agent Lifecycle Manager** — Raw Agent specification, directory, operators, and levers

Design follows the Seer Sidecar pattern: C2-level (conceptual) for most components, C3-level detail for critical mechanisms.

---

## Work Completed

### 1. Context Compiler Subsystem

**Created core design document** (`compilation-service.md`):
- **Four-Source Context Model**: Enterprise Knowledge, Enterprise Memory, Agent Memory, Hub Request Context
- **Request Hierarchy Integration**: Agents can access context from all requestors in ancestry topology, filtered by agent goal and role
- **Request-Update-Based Retriever Configuration**: Training Specs define retriever configurations with selectors matching request update metadata; Context Compiler automatically selects and merges matching configurations
- **Tool-Aware Context Compilation**: Incorporates available tools (from Training/Employment Specs) into context constraints and influences retrieval/ranking based on tool capabilities
- **Ranking and Token Budgeting**: Multi-stage ranking, cross-source deduplication, token budget allocation across sources
- **Provenance Tracking**: Full lineage tracking for all context sources

**Key Design Decisions**:
- Decoupled agent code from Training Spec details (agent code precedes training spec)
- Declarative retriever configuration in Training Specs with selector-based matching
- Hub Request Context includes full request ancestry topology
- Tools influence context compilation through constraints and retrieval ranking

### 2. Seer Agent SDK Subsystem

**Created dual-variant SDK design** (Python and Java):

#### Python SDK (6 API documents):
- `employment-spec-apis.md` — Employment Spec retrieval, caching, versioning
- `prompt-apis.md` — A/B testing, authority enforcement, autonomy level-based selection (Full, Suggest, Ask, Watch)
- `context-compiler-apis.md` — SDK wrappers for Context Compilation Service
- `observability-apis.md` — Metrics, tracing, structured logging, auto-instrumentation
- `hub-integration-apis.md` — Tool discovery/calling, Stores, Knowledge Services, Memory Services, Events
- `framework-apis.md` — LangGraph, Strands, OpenAPI agent builders

#### Java SDK (6 API documents):
- Same API coverage as Python SDK
- Framework-agnostic patterns (no framework-specific builders)
- Language-appropriate implementation patterns

**Key Design Decisions**:
- **Autonomy Levels**: Full, Suggest, Ask, Watch (from `apo.md`)
- Prompts tagged with autonomy level in Training Spec; used at that level or lower
- Exclusive prompts can be tagged for specific autonomy levels
- Framework convenience APIs differ by language (Python: LangGraph/Strands/OpenAPI; Java: framework-agnostic)

### 3. Raw Agent Lifecycle Manager Subsystem

**Created 4 component design documents**:

- `raw-agent-spec-manager.md` — Raw Agent CRD structure with:
  - Structured/typed capabilities (tool calling, orchestration, archetype roles: Thinker, Doer, Orchestrator, Governor)
  - Prompt tags for Authority Enforcement
  - Documentation references
  - Container image references
  - Raw Agent Identity (for recognizing derived agents)
  - **Clarification**: Raw Agents are NOT deployable; only Employed Agents are deployable

- `raw-agent-directory.md` — Registry, capability discovery, versioning, search

- `raw-agent-operators.md` — Lifecycle management (registration, validation, versioning)
  - **Clarification**: Operators do not directly deploy Raw Agents

- `raw-agent-levers.md` — Capability toggles, version deprecation, emergency controls

**Key Design Decisions**:
- Raw Agents are containers referenced by Employed Agents through Training Specs
- Raw Agent Identity is for recognizing derived agents
- Employed Agent Profile contains explicit identity sections for Raw Agent and Trained Agent
- Raw Agents define technical capabilities but lack organizational knowledge or operational authority

### 4. Content Migration

**Migrated from `context-assembly-engine.md`**:
- Context compilation architecture and four-source model
- Retrieval orchestration patterns
- Token budgeting and ranking mechanisms

**Migrated from `agent-observability.md`**:
- Observability API patterns
- Metrics, tracing, logging integration
- Auto-instrumentation approaches

**Deleted deprecated file**: `context-assembly-engine.md` (after updating all references)

### 5. Editorial Review and Cleanup

**Performed comprehensive editorial review**:
- Fixed consistency issues across all documents
- Updated all cross-references from `context-assembly-engine.md` to new `context-compiler/compilation-service.md`
- Updated terminology (CAE → Context Compilation Service)
- Removed duplication and ambiguity
- Updated `employed-agent-directory.md` to include explicit Raw Agent and Trained Agent identity sections

**Files updated with reference fixes**:
- `guardrails.md`
- `introduction.md`
- `hub-integration/README.md`
- `hub-integration/context-assembly.md`
- `implementation-concepts/context-assembly.md`
- `implementation-concepts/agent-observability.md`
- `subsystems/README.md`

---

## Artifacts Created

### Context Compiler (3 files)
| File | Description |
|------|-------------|
| `compilation-service.md` | Core Context Compilation Service design with four-source model, request hierarchy, tool-aware compilation, retriever configuration |
| `SCOPE.md` | Subsystem scope and coverage |
| `README.md` | Overview, architecture, design documents table, key decisions |

### Seer Agent SDK (14 files)
| File | Description |
|------|-------------|
| `python-sdk/employment-spec-apis.md` | Employment Spec Access APIs (Python) |
| `python-sdk/prompt-apis.md` | Prompt Access APIs with autonomy levels (Python) |
| `python-sdk/context-compiler-apis.md` | Context Compiler SDK wrappers (Python) |
| `python-sdk/observability-apis.md` | Observability APIs (Python) |
| `python-sdk/hub-integration-apis.md` | Hub Integration APIs (Python) |
| `python-sdk/framework-apis.md` | Framework Convenience APIs (Python) |
| `java-sdk/employment-spec-apis.md` | Employment Spec Access APIs (Java) |
| `java-sdk/prompt-apis.md` | Prompt Access APIs with autonomy levels (Java) |
| `java-sdk/context-compiler-apis.md` | Context Compiler SDK wrappers (Java) |
| `java-sdk/observability-apis.md` | Observability APIs (Java) |
| `java-sdk/hub-integration-apis.md` | Hub Integration APIs (Java) |
| `java-sdk/framework-apis.md` | Framework Convenience APIs (Java) |
| `SCOPE.md` | Subsystem scope and coverage |
| `README.md` | Overview, architecture, design documents table (organized by language), key decisions |

### Raw Agent Lifecycle Manager (6 files)
| File | Description |
|------|-------------|
| `raw-agent-spec-manager.md` | Raw Agent CRD structure, capabilities, identity |
| `raw-agent-directory.md` | Registry, capability discovery, versioning |
| `raw-agent-operators.md` | Lifecycle management, registration, validation |
| `raw-agent-levers.md` | Capability toggles, deprecation, emergency controls |
| `SCOPE.md` | Subsystem scope and coverage |
| `README.md` | Overview, architecture, design documents table, key decisions |

### Editorial Review (1 file)
| File | Description |
|------|-------------|
| `EDITORIAL-REVIEW-RAW-AGENT-SUBSYSTEMS.md` | Comprehensive editorial review documenting issues found and fixes applied |

---

## Files Updated

### Core Documentation Updates
- `subsystems/README.md` — Updated subsystem status and references
- `introduction.md` — Updated Context Compiler reference
- `hub-integration/README.md` — Updated Context Compiler reference
- `hub-integration/context-assembly.md` — Updated terminology and references
- `implementation-concepts/context-assembly.md` — Updated to reference new design documents
- `implementation-concepts/agent-observability.md` — Updated to reference new SDK Observability APIs
- `subsystems/guardrails.md` — Updated Context Compiler reference
- `subsystems/agent-lifecycle-manager/employed-agent-directory.md` — Added explicit Raw Agent and Trained Agent identity sections

### Files Deleted
- `subsystems/context-assembly-engine.md` — Migrated content to new Context Compiler design documents

---

## Key Decisions Made

### Context Compilation Architecture
1. **Request-Update-Based Retriever Configuration**: Training Specs declaratively define retriever configurations with selectors matching request update metadata. Context Compiler automatically selects and merges matching configurations. This decouples agent code from Training Spec details.
2. **Hub Request Context with Ancestry**: Agents can access context from all requestors in the request hierarchy/ancestry topology, filtered by agent goal and role.
3. **Tool-Aware Compilation**: Available tools (from Training/Employment Specs) are incorporated into context constraints and influence retrieval/ranking based on tool capabilities.

### SDK Design
1. **Dual Language Variants**: Python SDK and Java SDK, both for developers building Raw Agents.
2. **Autonomy Level-Based Prompt Selection**: Prompts tagged with autonomy level (Full, Suggest, Ask, Watch) in Training Specs; used at that level or lower. Exclusive prompts can be tagged for specific levels.
3. **Framework Convenience APIs**: Python supports LangGraph, Strands, OpenAPI builders; Java uses framework-agnostic patterns.

### Raw Agent Lifecycle
1. **Raw Agents Are Not Deployable**: Only Employed Agents are deployable. Raw Agents are containers referenced by Employed Agents through Training Specs.
2. **Structured Capabilities**: Raw Agent capabilities include tool calling, orchestration, archetype roles (Thinker, Doer, Orchestrator, Governor), and prompt tags for Authority Enforcement.
3. **Identity Structure**: Employed Agent Profile contains explicit identity sections for Raw Agent (name, version, container image, capabilities) and Trained Agent (training spec name, version, reference).

---

## Technical Highlights

### Context Compiler
- **Four-Source Model**: Enterprise Knowledge, Enterprise Memory, Agent Memory, Hub Request Context
- **Request Hierarchy**: Full ancestry topology support with goal/role-based filtering
- **Retriever Configuration**: Selector-based matching against request update metadata
- **Tool Integration**: Tools influence context constraints and retrieval ranking
- **Token Budgeting**: Per-source allocation with reserve budgets
- **Provenance**: Full lineage tracking for all context sources

### Seer Agent SDK
- **12 API Documents**: 6 for Python, 6 for Java
- **Autonomy Levels**: Full, Suggest, Ask, Watch (from `apo.md`)
- **Framework Support**: Python (LangGraph, Strands, OpenAPI), Java (framework-agnostic)
- **Observability**: Auto-instrumentation, metrics, tracing, structured logging

### Raw Agent Lifecycle Manager
- **4 Components**: Spec Manager, Directory, Operators, Levers
- **CRD Structure**: Structured capabilities, archetype roles, prompt tags
- **Identity Management**: Raw Agent and Trained Agent identity in Employed Agent Profile
- **Non-Deployable**: Raw Agents are containers, not directly deployable

---

## Commits Made

```
[SPE-0000] feat(seer): editorial review fixes and additional design documents
```

**Stats**: Multiple files created and updated across three subsystems

---

## Final Structure

```
olympus-seer-docs/seer-design/subsystems/
├── context-compiler/
│   ├── README.md
│   ├── SCOPE.md
│   └── compilation-service.md
├── seer-agent-sdk/
│   ├── README.md
│   ├── SCOPE.md
│   ├── python-sdk/
│   │   ├── employment-spec-apis.md
│   │   ├── prompt-apis.md
│   │   ├── context-compiler-apis.md
│   │   ├── observability-apis.md
│   │   ├── hub-integration-apis.md
│   │   └── framework-apis.md
│   └── java-sdk/
│       ├── employment-spec-apis.md
│       ├── prompt-apis.md
│       ├── context-compiler-apis.md
│       ├── observability-apis.md
│       ├── hub-integration-apis.md
│       └── framework-apis.md
└── raw-agent-lifecycle-manager/
    ├── README.md
    ├── SCOPE.md
    ├── raw-agent-spec-manager.md
    ├── raw-agent-directory.md
    ├── raw-agent-operators.md
    └── raw-agent-levers.md
```

---

## Next Steps

The three Raw Agent subsystems are now design complete. Potential next work:
1. **Trained Agent Lifecycle Manager** — Training Spec management, capability binding
2. **Agent Test Runner** — Testing framework for Raw and Trained Agents
3. **Seer Sidecar** — Additional guardrails and policy enforcement details
4. **Implementation** — Begin implementation of Context Compilation Service

---

*Session completed successfully with all three subsystems fully documented and editorial review completed.*
