# SDK & Development Experience

> **Status**: 🟡 Draft — Concept  
> **Last Updated**: 2026-01-13

## Overview

SDK & Development Experience provides the **Seer Agent SDK** for Raw Agents to interact with Seer and Hub services. The SDK is available in two language variants (Python and Java), both providing the same logical API groups with language-appropriate idioms.

**Key Design Point**: The SDK provides framework-agnostic core APIs that work with any agentic framework, with optional framework-specific builders for popular Python frameworks (LangGraph, Strands, OpenAPI).

---

## Architecture

Seer Agent SDK provides unified APIs:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SEER AGENT SDK ARCHITECTURE                              │
│                                                                              │
│   Raw Agent Application                                                     │
│        │                                                                     │
│        ├── Employment Spec APIs                                             │
│        ├── Prompt APIs                                                      │
│        ├── Context Compiler APIs                                           │
│        ├── Observability APIs                                               │
│        ├── Hub Integration APIs (Tools, Memory, Knowledge, Events)            │
│        └── Framework APIs (optional: LangGraph, Strands, OpenAPI)           │
│                                                                              │
│   → Seer Services (Agent Lifecycle Manager, Context Compiler, etc.)          │
│   → Hub Services (Tool Gateway, Memory Services, Knowledge Services, etc.)  │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Principles

- **Two Language Variants** — Python SDK and Java SDK with equivalent functionality
- **API Consistency** — Both SDKs provide the same logical API groups
- **Framework-Agnostic Core** — Core SDK APIs are framework-agnostic
- **Framework Builders** — Optional framework-specific builders for convenience
- **Prompt Access with Autonomy Level** — Prompts tagged with autonomy level (Full, Suggest, Ask, Watch)

---

## API Groups

### Employment Spec APIs

| Capability | Description |
|------------|-------------|
| **Spec Retrieval** | Retrieve Employment Spec for current agent |
| **Caching** | Cache Employment Spec for performance |
| **Versioning** | Handle Employment Spec versioning |

### Prompt APIs

| Capability | Description |
|------------|-------------|
| **A/B Testing Aware** | Prompts support A/B testing |
| **Authority Enforcement Aware** | Prompts respect authority constraints |
| **Autonomy Level-Based** | Prompts tagged with autonomy level (Full, Suggest, Ask, Watch) |
| **Selection Logic** | Prompts used at tagged level or lower levels |

### Context Compiler APIs

| Capability | Description |
|------------|-------------|
| **Context Compilation** | Compile context from memory, knowledge, session state |
| **SDK Wrappers** | SDK wrappers for context compilation service |
| **Four-Source Model** | Enterprise Knowledge, Enterprise Memory, Agent Memory, Hub Request Context |

### Observability APIs

| Capability | Description |
|------------|-------------|
| **Metrics** | Custom business metrics (Prometheus format) |
| **Tracing** | Distributed tracing via OpenTelemetry |
| **Structured Logging** | Structured JSON logging with PII redaction |
| **Auto-Instrumentation** | Auto-instrumentation for LLM calls, tool invocations, memory operations |

### Hub Integration APIs

| Capability | Description |
|------------|-------------|
| **Tool Discovery/Calling** | Discover and call tools via Hub Tool Gateway |
| **Stores** | Access Hub Stores (Workbench Data Store, etc.) |
| **Knowledge Services** | Access Enterprise Knowledge via Knowledge Services |
| **Memory Services** | Access Enterprise Memory and Agent Memory via Memory Services |
| **Events** | Publish events via Signal Exchange |

### Framework APIs

| Framework | Description |
|-----------|-------------|
| **LangGraph** | LangGraph agent builder (Python) |
| **Strands** | Strands agent builder (Python) |
| **OpenAPI** | OpenAPI agent builder (Python) |
| **Framework-Agnostic** | Framework-agnostic patterns and adapters (Java) |

---

## Prompt Access with Autonomy Level

Prompts in Training Spec are tagged with autonomy level:

| Autonomy Level | Description |
|----------------|-------------|
| **Full** | Full autonomy (agent makes decisions independently) |
| **Suggest** | Suggest mode (agent suggests, human approves) |
| **Ask** | Ask mode (agent asks before acting) |
| **Watch** | Watch mode (agent observes, human acts) |

**Selection Logic:**
- Prompts tagged at a level can be used at that level or lower levels
- Exclusive tags restrict usage to specific levels
- Current autonomy level determined from Employment Spec

---

## Language Variants

### Python SDK

| Aspect | Description |
|--------|-------------|
| **Target** | Python agentic AI ecosystem (LangChain, LangGraph, Strands) |
| **Frameworks** | LangGraph, Strands, OpenAPI builders |
| **Idioms** | Python-appropriate idioms and patterns |

### Java SDK

| Aspect | Description |
|--------|-------------|
| **Target** | Enterprise Java applications |
| **Frameworks** | Framework-agnostic patterns and adapters |
| **Idioms** | Java-appropriate idioms and patterns |

---

## Framework-Agnostic Core

Core SDK APIs are framework-agnostic:

| Aspect | Description |
|--------|-------------|
| **No Framework Lock-In** | Developers can use core APIs with any framework |
| **Optional Builders** | Framework builders are optional convenience layers |
| **Flexibility** | Maximum flexibility for developers |

---

## Related

### Seer Agent SDK Subsystem
- [Seer Agent SDK README](../subsystems/seer-agent-sdk/README.md) — SDK overview
- [Python SDK: Employment Spec APIs](../subsystems/seer-agent-sdk/python-sdk/employment-spec-apis.md) — Employment spec retrieval, caching
- [Python SDK: Prompt APIs](../subsystems/seer-agent-sdk/python-sdk/prompt-apis.md) — A/B testing aware, autonomy level-based prompts
- [Python SDK: Context Compiler APIs](../subsystems/seer-agent-sdk/python-sdk/context-compiler-apis.md) — Context compilation SDK wrappers
- [Python SDK: Observability APIs](../subsystems/seer-agent-sdk/python-sdk/observability-apis.md) — Metrics, tracing, logging
- [Python SDK: Hub Integration APIs](../subsystems/seer-agent-sdk/python-sdk/hub-integration-apis.md) — Tools, Memory, Knowledge, Events
- [Python SDK: Framework APIs](../subsystems/seer-agent-sdk/python-sdk/framework-apis.md) — LangGraph, Strands, OpenAPI builders
- [Java SDK: Employment Spec APIs](../subsystems/seer-agent-sdk/java-sdk/employment-spec-apis.md) — Employment spec retrieval, caching
- [Java SDK: Prompt APIs](../subsystems/seer-agent-sdk/java-sdk/prompt-apis.md) — A/B testing aware, autonomy level-based prompts
- [Java SDK: Context Compiler APIs](../subsystems/seer-agent-sdk/java-sdk/context-compiler-apis.md) — Context compilation SDK wrappers
- [Java SDK: Observability APIs](../subsystems/seer-agent-sdk/java-sdk/observability-apis.md) — Metrics, tracing, logging
- [Java SDK: Hub Integration APIs](../subsystems/seer-agent-sdk/java-sdk/hub-integration-apis.md) — Tools, Memory, Knowledge, Events
- [Java SDK: Framework APIs](../subsystems/seer-agent-sdk/java-sdk/framework-apis.md) — Framework-agnostic patterns

### Related Systems
- [Context Compiler](../subsystems/context-compiler/README.md) — Context compilation service
- [Agent Lifecycle Manager](../subsystems/agent-lifecycle-manager/README.md) — Training/Employment Spec management
- [Agent Observability](../implementation-concepts/agent-observability.md) — Observability concepts
- [Hub Tool Gateway](../../../olympus-hub-docs/04-subsystems/hub-native-utilities/direct-tool-dispatcher.md) — Tool Gateway
- [Hub Stores](../../../olympus-hub-docs/04-subsystems/stores/README.md) — Stores
- [Knowledge Services](../../../olympus-hub-docs/04-subsystems/knowledge-services/README.md) — Knowledge Services
- [Memory Services](../../../olympus-hub-docs/04-subsystems/memory-services/README.md) — Memory Services
- [Signal Exchange](../../../olympus-hub-docs/04-subsystems/signal-exchange/README.md) — Signal Exchange

---

*For detailed implementation, see [Seer Agent SDK README](../subsystems/seer-agent-sdk/README.md).*
