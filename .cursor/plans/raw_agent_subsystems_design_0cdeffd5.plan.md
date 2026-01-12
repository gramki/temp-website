---
name: Raw Agent Subsystems Design
overview: Create C2-level (Container) design documentation for context-compiler, seer-agent-sdk, and raw-agent-lifecycle-manager subsystems, following the seer-sidecar pattern. Design at conceptual level (C2) for most components, with C3-level detail for critical mechanisms. Context Compiler includes four-source compilation (Enterprise Knowledge, Enterprise Memory, Agent Memory, Hub Request Context with request hierarchy/ancestry topology) and tool-aware compilation (incorporating available tools into context constraints and influencing context retrieval/ranking based on tool capabilities). Migrate relevant content from context-assembly-engine.md and agent-observability.md into the new design documents.
todos:
  - id: context-compiler-service
    content: ""
    status: completed
  - id: sdk-employment-spec-apis-python
    content: Create C2-level design for Python SDK Employment Spec Access APIs covering functional scope (employment spec retrieval, caching, versioning) and integration with Agent Lifecycle Manager
    status: in_progress
  - id: sdk-employment-spec-apis-java
    content: Create C2-level design for Java SDK Employment Spec Access APIs covering functional scope (employment spec retrieval, caching, versioning) and integration with Agent Lifecycle Manager
    status: in_progress
  - id: sdk-prompt-apis-python
    content: Create C2-level design for Python SDK Prompt Access APIs covering functional scope (A/B testing aware retrieval, authority enforcement aware prompts, prompt versioning, autonomy level-based prompt selection - prompts tagged with autonomy level in Training Spec are used at that level or lower levels of autonomy) and integration points
    status: completed
  - id: sdk-prompt-apis-java
    content: Create C2-level design for Java SDK Prompt Access APIs covering functional scope (A/B testing aware retrieval, authority enforcement aware prompts, prompt versioning, autonomy level-based prompt selection - prompts tagged with autonomy level in Training Spec are used at that level or lower levels of autonomy) and integration points
    status: completed
  - id: sdk-context-compiler-apis-python
    content: Create C2-level design for Python SDK Context Compiler APIs covering SDK wrappers for context compilation service, integration with Context Compiler service
    status: completed
    dependencies:
      - context-compiler-service
  - id: sdk-context-compiler-apis-java
    content: Create C2-level design for Java SDK Context Compiler APIs covering SDK wrappers for context compilation service, integration with Context Compiler service
    status: completed
    dependencies:
      - context-compiler-service
  - id: sdk-observability-apis-python
    content: Create C2-level design for Python SDK Observability APIs covering metrics reporting, tracing, structured logging, auto-instrumentation, and integration with Watch
    status: completed
  - id: sdk-observability-apis-java
    content: Create C2-level design for Java SDK Observability APIs covering metrics reporting, tracing, structured logging, auto-instrumentation, and integration with Watch
    status: completed
  - id: sdk-hub-integration-apis-python
    content: Create C2-level design for Python SDK Hub Integration APIs covering tool discovery/calling, Stores, Knowledge Services, Memory Services, Events APIs, and integration patterns
    status: completed
  - id: sdk-hub-integration-apis-java
    content: Create C2-level design for Java SDK Hub Integration APIs covering tool discovery/calling, Stores, Knowledge Services, Memory Services, Events APIs, and integration patterns
    status: completed
  - id: sdk-framework-apis-python
    content: Create C2-level design for Python SDK Framework Convenience APIs covering LangGraph, Strands, OpenAPI agent builders, maintaining framework-agnostic design principles
    status: in_progress
    dependencies:
      - sdk-employment-spec-apis-python
      - sdk-prompt-apis-python
      - sdk-context-compiler-apis-python
  - id: sdk-framework-apis-java
    content: Create C2-level design for Java SDK Framework Convenience APIs covering framework-agnostic patterns, maintaining framework-agnostic design principles
    status: in_progress
    dependencies:
      - sdk-employment-spec-apis-java
      - sdk-prompt-apis-java
      - sdk-context-compiler-apis-java
  - id: raw-agent-spec-manager
    content: "Create C2-level design for Raw Agent Spec Manager covering functional scope (Raw Agent CRD structure with structured/typed capabilities specification: tool calling capabilities, orchestration capabilities, archetype roles supported (thinker, doer, orchestrator, governor), tags supported for prompts and their meaning in Authority Enforcement; documentation reference for Trained/Employed Agent developers; container image reference; identity for recognizing derived agents; validation rules; note that Raw Agents are NOT deployable - only Employed Agents are deployable; Raw Agents are containers referenced by Employed Agents through Training Spec) and integration points"
    status: pending
  - id: raw-agent-directory
    content: Create C2-level design for Raw Agent Directory covering functional scope (raw agent registry, capability discovery, versioning, search) and integration points
    status: pending
    dependencies:
      - raw-agent-spec-manager
  - id: raw-agent-operators
    content: Create C2-level design for Raw Agent Operators covering functional scope (Raw Agent lifecycle management operators - note that Raw Agents are NOT directly deployed; they are deployed only as part of Employed Agents with associated configs and environment in workbench instances; operators manage Raw Agent registration, validation, versioning, and discovery) and integration with Agent Runtime (for Employed Agent deployment that references Raw Agent containers)
    status: pending
    dependencies:
      - raw-agent-spec-manager
  - id: raw-agent-levers
    content: Create C2-level design for Raw Agent Levers covering functional scope (kill switches, capability toggles, emergency controls, execution methods) and integration points
    status: pending
    dependencies:
      - raw-agent-operators
  - id: migrate-context-assembly
    content: Migrate runtime enforcement content from subsystems/context-assembly-engine.md to context-compiler/compilation-service.md
    status: pending
    dependencies:
      - context-compiler-service
  - id: migrate-observability
    content: Migrate SDK content from subsystems/agent-observability.md to seer-agent-sdk/python-sdk/observability-apis.md and seer-agent-sdk/java-sdk/observability-apis.md
    status: pending
    dependencies:
      - sdk-observability-apis-python
      - sdk-observability-apis-java
  - id: create-context-compiler-scope
    content: Create SCOPE.md document for context-compiler with coverage summary, design status, intended depth callout, and related documentation references
    status: pending
    dependencies:
      - context-compiler-service
  - id: create-sdk-scope
    content: Create SCOPE.md document for seer-agent-sdk with coverage summary, design status, intended depth callout, and related documentation references
    status: pending
    dependencies:
      - sdk-employment-spec-apis-python
      - sdk-employment-spec-apis-java
      - sdk-prompt-apis-python
      - sdk-prompt-apis-java
      - sdk-context-compiler-apis-python
      - sdk-context-compiler-apis-java
      - sdk-observability-apis-python
      - sdk-observability-apis-java
      - sdk-hub-integration-apis-python
      - sdk-hub-integration-apis-java
      - sdk-framework-apis-python
      - sdk-framework-apis-java
  - id: create-raw-agent-scope
    content: Create SCOPE.md document for raw-agent-lifecycle-manager with coverage summary, design status, intended depth callout, and related documentation references
    status: pending
    dependencies:
      - raw-agent-spec-manager
      - raw-agent-directory
      - raw-agent-operators
      - raw-agent-levers
  - id: update-context-compiler-readme
    content: Update context-compiler/README.md with links to all detailed design documents, remove old content references, update status to reflect design completion, add design documents table, and include Key Design Decisions section
    status: pending
    dependencies:
      - context-compiler-service
      - create-context-compiler-scope
  - id: update-sdk-readme
    content: Update seer-agent-sdk/README.md with links to all detailed design documents (organized by Python SDK and Java SDK folders), remove old content references, update status to reflect design completion, add design documents table, and include Key Design Decisions section
    status: pending
    dependencies:
      - sdk-employment-spec-apis-python
      - sdk-employment-spec-apis-java
      - sdk-prompt-apis-python
      - sdk-prompt-apis-java
      - sdk-context-compiler-apis-python
      - sdk-context-compiler-apis-java
      - sdk-observability-apis-python
      - sdk-observability-apis-java
      - sdk-hub-integration-apis-python
      - sdk-hub-integration-apis-java
      - sdk-framework-apis-python
      - sdk-framework-apis-java
      - create-sdk-scope
  - id: update-raw-agent-readme
    content: Update raw-agent-lifecycle-manager/README.md with links to all detailed design documents, remove old content references, update status to reflect design completion, add design documents table, and include Key Design Decisions section
    status: pending
    dependencies:
      - raw-agent-spec-manager
      - raw-agent-directory
      - raw-agent-operators
      - raw-agent-levers
      - create-raw-agent-scope
  - id: update-concept-docs
    content: Update implementation-concepts/context-assembly.md and implementation-concepts/agent-observability.md to reference new design documents and remove migrated content
    status: pending
    dependencies:
      - migrate-context-assembly
      - migrate-observability
  - id: update-employed-agent-profile
    content: Update agent-lifecycle-manager/employed-agent-directory.md to add explicit identity sections for Raw Agent (raw agent name, version, container image reference, capabilities summary) and Trained Agent (training spec name, version, training spec reference) in the Employed Agent Profile structure
    status: pending
---

# Raw Agent Subsystems Detailed Design

Create comprehensive C2-level design documentation for three subsystems that collectively define a Raw Agent: **Context Compiler**, **Seer Agent SDK**, and **Raw Agent Lifecycle Manager**. Follow the pattern established by the Seer Sidecar detailed design, with C2-level (conceptual) design for most components and C3-level detail for critical mechanisms.

## Subsystem Breakdown

### 1. Context Compiler

Single service with multiple capabilities. Design as one document covering:

- **Compilation Service**: Main context assembly from four sources:
- Enterprise Knowledge (Hub Knowledge Services)
- Enterprise Memory (Hub Memory Services)
- Agent Memory (Hub Memory Services)
- Hub Request Context (current request + all ancestors in request hierarchy)
- **Request Hierarchy Integration**: Ancestry topology traversal, goal and role-based filtering of ancestor contexts
- **Request-Update-Based Retriever Configuration**: Automatic retriever selection based on request update metadata (updateType, taskType, contextKeys, etc.) matching Training Spec selector criteria; Training Spec defines retriever configurations with selectors that match against request update characteristics; when multiple selectors match, all matching configurations are merged; agent code remains framework-agnostic and doesn't need to specify retrievers
- **Tool-Aware Compilation**: Incorporation of available tools (from Training/Employment Specs) into context constraints section; tool capabilities influence context retrieval and ranking (e.g., if tool can query database, reduce redundant context about that data; prioritize context that helps with tool selection)
- **Ranking & Relevance**: Context ranking algorithms and relevance scoring
- **Token Budgeting**: Token allocation strategies and overflow handling
- **Provenance Tracking**: Context source attribution and reproducibility

### 2. Seer Agent SDK

Two language variants for developers building Raw Agents, with separate documentation per variant:

- **Python SDK**: For Python-based Raw Agents (LangChain, LangGraph, Strands, custom Python frameworks)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                - Separate design documents in `seer-agent-sdk/python-sdk/` folder
- **Java SDK**: For Java-based Raw Agents (custom Java frameworks)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                - Separate design documents in `seer-agent-sdk/java-sdk/` folder

Both SDKs provide the same logical API groups (not separate services):

- **Employment Spec Access APIs**: Access to employment specifications
- **Prompt Access APIs**: A/B testing aware, authority enforcement aware prompt retrieval
- **Context Compiler APIs**: SDK wrappers for context compilation service
- **Observability APIs**: Metrics reporting, tracing (migrate from agent-observability.md)
- **Hub Integration APIs**: Tool discovery/calling, Stores, Knowledge Services, Memory Services, Events
- **Framework Convenience APIs**: Framework-specific builders (Python: LangGraph, Strands, OpenAPI; Java: framework-agnostic patterns)

### 3. Raw Agent Lifecycle Manager

Break down into sub-components following agent-lifecycle-manager pattern:

- **Raw Agent Spec Manager**: Raw Agent specification CRD with structured/typed capabilities: tool calling capabilities, orchestration capabilities, archetype roles supported (thinker, doer, orchestrator, governor), tags supported for prompts and their meaning in Authority Enforcement; documentation reference (for Trained/Employed Agent developers); container image reference; identity (for recognizing derived agents); validation rules. Note: Raw Agents are NOT deployable - only Employed Agents are deployable. Raw Agents are containers referenced by Employed Agents through Training Spec.
- **Raw Agent Directory**: Raw Agent registry, capability discovery, versioning, search by capabilities
- **Raw Agent Operators**: Raw Agent lifecycle management (registration, validation, versioning) - note that Raw Agents are NOT directly deployed; they are deployed only as part of Employed Agents with associated configs and environment in workbench instances
- **Raw Agent Levers**: Capability toggles, version deprecation, emergency controls (affects all derived Employed Agents)

## Design Approach

### Design Levels

- **C2 (Container) Level**: Most components - functional scope, integration points, conceptual models, operational flows
- **C3 (Component) Level**: Critical mechanisms only (e.g., context ranking algorithms, SDK authentication)

### Content Migration

- Migrate runtime enforcement content from `context-assembly-engine.md` to `context-compiler/compilation-service.md`
- Migrate SDK content from `agent-observability.md` to `seer-agent-sdk/observability-apis.md`
- Update implementation-concepts documents to reference new design documents

### Documentation Structure

Each subsystem follows the pattern:

- `README.md`: Overview, design documents table, key design decisions
- `SCOPE.md`: Coverage summary, design status, intended depth, implementation details deferred
- Individual component documents: Functional scope, integration points, hand-offs

## Key Design Decisions to Document

### Context Compiler

#### Request-Update-Based Retriever Configuration Model

**Principle**: Agent code (Raw Agent) is framework-agnostic and precedes Training Spec. Agents cannot be Training-aware.

**Approach**: Training Spec defines retriever configurations with selectors that match against request update metadata. Context Compiler automatically selects the matching configuration based on the incoming request update.

**Training Spec Configuration**:

```yaml
spec:
  contextCompilation:
    retrieverConfigs:
      - selector:
          updateType: "task_created"
          taskType: "fraud_investigation"
        retrievers: [...]
        tokenBudget: {...}
        ranking: {...}
      - selector:
          updateType: "context_update"
          contextKeys: ["customer_profile"]
        retrievers: [...]
        tokenBudget: {...}
      - selector: {}  # Default fallback
        retrievers: [...]
```

**Agent Code** (framework-agnostic):

```python
# Agent just invokes compilation - no retriever specification
context = cae.compile(
    request_id=invocation.request.request_id,
    update_id=invocation.update.update_id
)
```

**Context Compiler Behavior**:

1. Receives request update with metadata (updateType, taskType, contextKeys, etc.)
2. Loads Training Spec retriever configurations
3. Matches request update against selector criteria
4. Applies matching retriever configuration (retrievers, token budget, ranking)
5. Falls back to default configuration if no match

**Selector Matching Criteria**: updateType, taskType, contextKeys, scenarioId, workbenchId, custom metadata fields

### Context Compiler

- Service invocation model (explicit agent invocation vs pre-compilation)
- Four-source retrieval orchestration (Enterprise Knowledge, Enterprise Memory, Agent Memory, Hub Request Context)
- Request hierarchy/ancestry topology traversal (accessing all requestors in ancestry chain)
- Goal and role-based filtering of ancestor contexts (agent goal and role determine which ancestor contexts are relevant)
- Request-update-based retriever configuration (Training Spec defines retriever configurations with selectors matching request update metadata; Context Compiler automatically matches and merges all matching configurations; agent code remains framework-agnostic)
- Selector matching criteria (updateType, taskType, contextKeys, scenarioId, workbenchId, custom metadata)
- Selector matching behavior (when multiple selectors match, all matching retriever configurations are merged - retrievers combined, token budgets aggregated, ranking strategies merged)
- Tool-aware context compilation (available tools from Training/Employment Specs included in context constraints; tool capabilities influence context retrieval and ranking)
- Ranking strategy selection (relevance, priority, custom)
- Token budget allocation strategies (per retriever configuration)
- Provenance preservation requirements

### Seer Agent SDK

- **Two Language Variants**: Python SDK and Java SDK for developers building Raw Agents
- **API Consistency**: Both SDKs provide equivalent functionality with language-appropriate idioms
- SDK initialization and authentication model (language-specific implementations)
- Framework-agnostic design principles (both SDKs support any agentic framework)
- Hub service integration patterns (consistent across languages)
- Observability auto-instrumentation approach (language-specific instrumentation libraries)
- Error handling and retry policies (language-appropriate patterns)
- Framework Convenience APIs (Python: LangGraph, Strands, OpenAPI builders; Java: framework-agnostic patterns)
- **Prompt Access with Autonomy Level Support**: Prompts in Training Spec are tagged with autonomy level (Full, Suggest, Ask, Watch as defined in apo.md); prompts are used at the tagged level or lower levels of autonomy (Full > Suggest > Ask > Watch); SDK APIs support autonomy level-based prompt selection

### Raw Agent Lifecycle Manager

- Raw Agent Spec CRD structure with structured/typed capabilities specification: tool calling capabilities, orchestration capabilities, archetype roles supported (thinker, doer, orchestrator, governor), tags supported for prompts and their meaning in Authority Enforcement (for Agent Engineers to evaluate suitability), documentation reference (for Trained/Employed Agent developers), container image reference, identity (for recognizing derived agents)
- Raw Agents are NOT deployable - only Employed Agents are deployable; Raw Agents are containers referenced by Employed Agents through Training Spec
- Raw Agents are deployed only as part of Employed Agents with associated configs and environment in workbench instances
- Directory organization (by capability, framework, version) for Agent Engineers to discover suitable Raw Agents
- Operator reconciliation patterns (registration, validation, versioning - not deployment)
- Lever execution methods (affects all derived Employed Agents - version deprecation, capability toggles)
- Integration with Agent Runtime (for Employed Agent deployment that references Raw Agent containers)

## Integration Points

### Context Compiler

- Hub Memory Services (Enterprise Memory, Agent Memory)
- Hub Knowledge Services (Enterprise Knowledge)
- Hub Request Management (request hierarchy, ancestor context access, request context records)
- Tools Gateway / Tool Registry (tool metadata, capabilities, schemas for tool-aware compilation)
- Agent Lifecycle Manager (Training Spec retriever configurations with selectors; Employment Spec for tool bindings and constraints)
- Model Gateway (token limits)
- Seer Agent SDK (SDK APIs)

### Seer Agent SDK

- Context Compiler (context compilation APIs)
- Agent Lifecycle Manager (employment spec access)
- Hub Tool Gateway (tool discovery/calling)
- Hub Memory Services (memory APIs)
- Hub Knowledge Services (knowledge APIs)
- Hub Signal Exchange (events APIs)
- Model Gateway (model access)
- Watch (observability)

### Raw Agent Lifecycle Manager

- Agent Runtime (Raw Agent containers are deployed only as part of Employed Agents; Agent Runtime deploys Employed Agents which reference Raw Agent containers through Training Spec)
- Cipher IAM Extensions (Raw Agent identity for recognizing derived agents)
- Trained Agent Lifecycle Manager (Training Specs reference Raw Agents; Raw Agent capabilities influence Training Spec creation)
- Agent Lifecycle Manager (Employed Agent Profile includes Raw Agent and Trained Agent identity sections)
- CI/CD pipelines (raw agent container image registration and versioning)

## Implementation Details Deferred

- Detailed CRD schemas
- Complete API specifications (REST/gRPC endpoints)
- Storage backends and indexing strategies
- Performance optimization strategies
- Specific algorithm implementations (beyond conceptual)
- Error code taxonomies
- Wire format details