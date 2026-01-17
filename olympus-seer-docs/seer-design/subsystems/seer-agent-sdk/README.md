# Seer Agent SDK

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-12

---

## Overview

Seer Agent SDK provides the SDK for Raw Agents to interact with Seer and Hub services. The SDK is available in two language variants (Python and Java), both providing the same logical API groups with language-appropriate idioms. The SDK provides APIs for employment spec access, prompt access, context compilation, metrics reporting, tracing, tool discovery/calling, memory services, knowledge services, and events.

**Key Design Point**: The SDK provides framework-agnostic core APIs that work with any agentic framework, with optional framework-specific builders for popular Python frameworks (LangGraph, Strands, OpenAPI).

---

## Design Documents

### Python SDK

| Document | Status | Description |
|----------|--------|-------------|
| [Employment Spec APIs](python-sdk/employment-spec-apis.md) | 🟢 Complete | Employment spec retrieval, caching, versioning |
| [Prompt APIs](python-sdk/prompt-apis.md) | 🟢 Complete | A/B testing aware, authority enforcement aware, autonomy level-based prompt retrieval |
| [Context Compiler APIs](python-sdk/context-compiler-apis.md) | 🟢 Complete | SDK wrappers for context compilation service |
| [Observability APIs](python-sdk/observability-apis.md) | 🟢 Complete | Metrics, tracing, structured logging, auto-instrumentation |
| [Hub Integration APIs](python-sdk/hub-integration-apis.md) | 🟢 Complete | Tool discovery/calling, Stores, Knowledge Services, Memory Services, Events APIs |
| [Delegation APIs](python-sdk/delegation-apis.md) | 🟢 Complete | Request authority, get tokens, delegate to children |
| [Framework APIs](python-sdk/framework-apis.md) | 🟢 Complete | LangGraph, Strands, OpenAPI agent builders |

### Java SDK

| Document | Status | Description |
|----------|--------|-------------|
| [Employment Spec APIs](java-sdk/employment-spec-apis.md) | 🟢 Complete | Employment spec retrieval, caching, versioning |
| [Prompt APIs](java-sdk/prompt-apis.md) | 🟢 Complete | A/B testing aware, authority enforcement aware, autonomy level-based prompt retrieval |
| [Context Compiler APIs](java-sdk/context-compiler-apis.md) | 🟢 Complete | SDK wrappers for context compilation service |
| [Observability APIs](java-sdk/observability-apis.md) | 🟢 Complete | Metrics, tracing, structured logging, auto-instrumentation |
| [Hub Integration APIs](java-sdk/hub-integration-apis.md) | 🟢 Complete | Tool discovery/calling, Stores, Knowledge Services, Memory Services, Events APIs |
| [Delegation APIs](java-sdk/delegation-apis.md) | 🟢 Complete | Request authority, get tokens, delegate to children |
| [Framework APIs](java-sdk/framework-apis.md) | 🟢 Complete | Framework-agnostic patterns and adapters |

### Scope and Coverage

| Document | Status | Description |
|----------|--------|-------------|
| [SCOPE](SCOPE.md) | 🟢 Complete | Coverage summary, design status, intended depth, implementation details deferred |

---

## Key Design Decisions

### Two Language Variants

**Decision**: SDK is provided in two language variants: Python SDK and Java SDK.

**Rationale**:
- Python is dominant in agentic AI ecosystem (LangChain, LangGraph, Strands)
- Java is required for enterprise Java applications
- Both SDKs provide equivalent functionality with language-appropriate idioms

### API Consistency

**Decision**: Both SDKs provide the same logical API groups with language-appropriate implementations.

**Rationale**:
- Consistent developer experience across languages
- Same capabilities available in both languages
- Language-specific idioms for better developer experience

### Framework-Agnostic Core

**Decision**: Core SDK APIs are framework-agnostic; framework builders are optional convenience layers.

**Rationale**:
- Developers can use core APIs with any framework
- No framework lock-in
- Framework builders are optional convenience

### Prompt Access with Autonomy Level Support

**Decision**: Prompts in Training Spec are tagged with autonomy level (Full, Suggest, Ask, Watch); prompts are used at the tagged level or lower levels of autonomy.

**Rationale**:
- Different autonomy levels require different prompt styles
- Full autonomy needs different instructions than supervised autonomy
- Ensures prompts match the agent's authority level

**Selection Logic**:
- Prompts tagged at a level can be used at that level or lower
- Exclusive tags restrict usage to specific levels
- Current autonomy level determined from Employment Spec

---

## Related Documentation

### Seer Design
- [Context Compiler](../context-compiler/README.md) — Context compilation service
- [Agent Lifecycle Manager](../agent-lifecycle-manager/README.md) — Training/Employment Spec management
- [Agent Observability](../agent-observability.md) — Observability concepts

### Hub Documentation
- [Hub Tool Gateway](../../../olympus-hub-docs/04-subsystems/hub-native-utilities/direct-tool-dispatcher.md)
- [Hub Stores](../../../olympus-hub-docs/04-subsystems/stores/README.md)
- [Knowledge Services](../../../olympus-hub-docs/04-subsystems/knowledge-services/README.md)
- [Memory Services](../../../olympus-hub-docs/04-subsystems/memory-services/README.md)
- [Signal Exchange](../../../olympus-hub-docs/04-subsystems/signal-exchange/README.md)
- [Olympus Watch](../../../olympus-hub-docs/05-infrastructure/olympus-watch.md)

---

*Seer Agent SDK provides framework-agnostic APIs for Raw Agents to interact with Seer and Hub services, with Python and Java language variants.*
