# 20.2 SDK Capabilities

Seer Agent SDK provides comprehensive capabilities for agent development through five API groups: Employment Spec APIs, Prompt APIs, Context Compiler APIs, Observability APIs, and Hub Integration APIs. Each API group provides specific functionality while working together to enable comprehensive agent development.

This subsection describes each API group in detail, explaining how they address the core SDK capabilities required in Section 5.13.2. It also describes framework builders that provide convenience layers for popular Python frameworks.

## Purpose of this Subsection

This subsection describes the specific SDK capabilities provided by Seer Agent SDK. It explains each API group (Employment Spec, Prompts, Context Compiler, Observability, Hub Integration), describes framework builders, and explains how these capabilities enable comprehensive agent development.

## Core Concepts & Definitions

### Employment Spec APIs

**Employment Spec APIs** provide SDK interfaces for Raw Agents to retrieve, cache, and access their Employment Specifications. Employment Specs contain authority delegation, work scope, resource quotas, tool bindings, and operational environment configuration.

Employment Spec APIs provide:
*   **Spec retrieval**: Retrieve Employment Spec for current agent instance
*   **Caching**: Cache Employment Specs locally for performance
*   **Versioning**: Handle Employment Spec versioning and updates
*   **Automatic refresh**: Refresh cached specs when updates occur

Employment Spec APIs enable agents to understand their delegated authority and operational constraints at runtime.

### Prompt APIs

**Prompt APIs** provide SDK interfaces for Raw Agents to retrieve prompts from Training Specs with support for A/B testing, authority enforcement awareness, and autonomy level-based selection. Prompts are tagged with autonomy levels (Full, Suggest, Ask, Watch) and are selected based on the current agent's autonomy level.

Prompt APIs provide:
*   **A/B testing awareness**: Automatically select A/B testing variants based on configured experiments
*   **Authority enforcement awareness**: Prompts respect authority constraints and guardrails
*   **Autonomy level-based selection**: Prompts tagged with autonomy levels are selected based on current agent autonomy level
*   **Prompt versioning**: Handle prompt versioning and updates

Prompt APIs enable agents to use appropriate prompts for their autonomy level and participate in A/B testing.

### Context Compiler APIs

**Context Compiler APIs** provide SDK wrappers for the context compilation service, enabling agents to compile reasoning context from Enterprise Knowledge, Enterprise Memory, Agent Memory, and Hub Request Context.

Context Compiler APIs provide:
*   **Four-source model**: Compile context from Enterprise Knowledge, Enterprise Memory, Agent Memory, and Hub Request Context
*   **SDK wrappers**: SDK wrappers for context compilation service that abstract away service complexity
*   **Caching**: Cache compiled context for performance when appropriate
*   **Versioning**: Handle knowledge and memory versioning

Context Compiler APIs enable agents to assemble the information they need for reasoning and decision-making.

### Observability APIs

**Observability APIs** provide SDK interfaces for instrumenting agents with metrics, tracing, structured logging, and auto-instrumentation for LLM calls, tool invocations, and memory operations.

Observability APIs provide:
*   **Metrics**: Custom business metrics in Prometheus format
*   **Tracing**: Distributed tracing via OpenTelemetry
*   **Structured logging**: Structured JSON logging with PII redaction
*   **Auto-instrumentation**: Automatic instrumentation for LLM calls, tool invocations, memory operations

Observability APIs enable developers and operators to understand agent behavior during development and production.

### Hub Integration APIs

**Hub Integration APIs** provide SDK interfaces for interacting with Hub services for tools, memory, knowledge, and events. Hub Integration APIs enable agents to use tools, access memory and knowledge, and publish events through Hub's governed services.

Hub Integration APIs provide:
*   **Tool discovery/calling**: Discover and call tools via Hub Tool Gateway
*   **Stores access**: Access Hub Stores (Workbench Data Store, etc.)
*   **Knowledge Services**: Access Enterprise Knowledge via Knowledge Services
*   **Memory Services**: Access Enterprise Memory and Agent Memory via Memory Services
*   **Events**: Publish events via Signal Exchange

Hub Integration APIs enable agents to use tools, access memory or knowledge, and publish events.

### Framework Builders

**Framework builders** are optional convenience layers that provide framework-specific builders for popular Python frameworks:
*   **LangGraph Builder**: LangGraph agent builder with Seer integration
*   **Strands Builder**: Strands agent builder with Seer integration
*   **OpenAPI Builder**: OpenAPI agent builder with Seer integration

Framework builders simplify common patterns for popular frameworks while maintaining framework independence through core APIs.

## Conceptual Models / Frameworks

### The API Group Model

SDK capabilities are organized into API groups:

```
Seer Agent SDK
    ├── Employment Spec APIs
    ├── Prompt APIs
    ├── Context Compiler APIs
    ├── Observability APIs
    └── Hub Integration APIs
            ├── Tool APIs
            ├── Store APIs
            ├── Knowledge APIs
            ├── Memory APIs
            └── Event APIs
```

Each API group provides specific functionality while working together to enable comprehensive agent development.

### The Framework Builder Model

Framework builders provide convenience layers:

```
Framework Builder (LangGraph, Strands, OpenAPI)
    ↓
Core SDK APIs (Framework-Agnostic)
    ↓
Seer & Hub Services
```

Framework builders simplify framework-specific patterns while core APIs remain framework-agnostic.

## Systemic and Enterprise Considerations

### Performance Requirements

SDK APIs must be performant:
*   **Caching**: Employment Specs and prompts must be cached to avoid repeated service calls
*   **Efficient compilation**: Context compilation must be efficient, avoiding unnecessary data retrieval
*   **Minimal overhead**: Observability instrumentation must add minimal overhead to agent execution
*   **Connection pooling**: Hub integration must use connection pooling for efficient service access

Performance directly impacts agent responsiveness and resource utilization.

### Security and Governance

SDK APIs must maintain security and governance:
*   **Authentication**: All service access must be authenticated
*   **Authorization**: Access must respect authority constraints and guardrails
*   **PII redaction**: Observability must redact PII according to workbench policies
*   **Audit trail**: All service access must be auditable

Security and governance are non-negotiable for enterprise deployments.

### Versioning and Compatibility

SDK APIs must handle versioning:
*   **Spec versioning**: Employment Specs and Training Specs are versioned
*   **API versioning**: SDK APIs must handle service API versioning
*   **Backward compatibility**: SDK updates must maintain backward compatibility when possible
*   **Migration support**: SDK must support migration when breaking changes occur

Versioning enables safe updates and rollbacks.

## Common Misconceptions & Failure Modes

### Misconception: Direct Service Access Is Sufficient

Some developers assume that direct service access (REST APIs, gRPC) is sufficient without SDKs. However, direct access requires developers to handle authentication, caching, versioning, observability instrumentation, and error handling—complexity that SDKs abstract away.

**Failure mode**: Developers access services directly, increasing development complexity and reducing productivity.

### Misconception: Observability Is Optional

Some developers assume that observability is optional during development. However, observability is essential for understanding agent behavior, debugging issues, and validating agent correctness.

**Failure mode**: Developers skip observability, making debugging and validation difficult or impossible.

### Misconception: Context Compilation Is Simple

Some developers assume that context compilation is simply retrieving data from various sources. However, context compilation requires understanding the four-source model, handling versioning, managing caching, and assembling context efficiently.

**Failure mode**: Developers implement ad-hoc context assembly, leading to incomplete context, performance problems, or incorrect reasoning.

## Practical Implications

### SDK Design Principles

SDKs should be designed with:
*   **Simplicity**: APIs should be simple and intuitive
*   **Consistency**: APIs should be consistent across capabilities and languages
*   **Performance**: APIs should be performant with appropriate caching
*   **Error handling**: APIs should provide clear error messages and handling
*   **Documentation**: APIs should be well-documented with examples

SDK design directly impacts developer productivity and satisfaction.

### Capability Integration

SDK capabilities must work together:
*   **Employment Spec informs prompts**: Employment Spec determines autonomy level, which informs prompt selection
*   **Context compilation uses knowledge/memory**: Context compilation retrieves data from Knowledge Services and Memory Services
*   **Observability tracks all operations**: Observability instruments all SDK operations
*   **Hub integration enables tools**: Hub integration enables tool discovery and calling

Capability integration enables comprehensive agent functionality.

## Cross-References

*   **Section 5.13.2 (Core SDK Capabilities Required)**: Establishes the SDK capabilities that Seer Agent SDK implements
*   **Section 20.1 (Seer Agent SDK)**: Describes the SDK architecture and design principles
*   **Section 20.3 (Development Workflow)**: Describes how SDK capabilities support development workflows

---

**References:**

*   `seer-design/subsystems/seer-agent-sdk/README.md` — Seer Agent SDK design
*   `seer-design/subsystems/seer-agent-sdk/python-sdk/employment-spec-apis.md` — Employment Spec APIs
*   `seer-design/subsystems/seer-agent-sdk/python-sdk/prompt-apis.md` — Prompt APIs
*   `seer-design/subsystems/seer-agent-sdk/python-sdk/context-compiler-apis.md` — Context Compiler APIs
*   `seer-design/subsystems/seer-agent-sdk/python-sdk/observability-apis.md` — Observability APIs
*   `seer-design/subsystems/seer-agent-sdk/python-sdk/hub-integration-apis.md` — Hub Integration APIs
*   `seer-design/subsystems/seer-agent-sdk/python-sdk/framework-apis.md` — Framework APIs
