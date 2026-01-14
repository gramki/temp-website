# 20.1 Seer Agent SDK

Seer Agent SDK provides the SDK for Raw Agents to interact with Seer and Hub services. The SDK is available in two language variants (Python and Java), both providing the same logical API groups with language-appropriate idioms. The SDK provides framework-agnostic core APIs that work with any agentic framework, with optional framework-specific builders for popular Python frameworks (LangGraph, Strands, OpenAPI).

Seer Agent SDK addresses the framework-agnostic and multi-language requirements established in Section 5.13.1, enabling developers to choose their preferred frameworks and languages while maintaining consistent access to Seer and Hub capabilities.

## Purpose of this Subsection

This subsection describes the architecture and design principles of Seer Agent SDK. It explains the framework-agnostic design, multi-language support, API groups, and framework builders. It also describes how the SDK enables developers to work with any agentic framework while providing convenience layers for popular frameworks.

## Core Concepts & Definitions

### Framework-Agnostic Core APIs

**Framework-agnostic core APIs** are SDK APIs that work with any agentic framework (LangGraph, Strands, OpenAPI, custom frameworks) without requiring framework-specific implementations. Framework-agnostic APIs enable developers to:
*   Choose their preferred framework without lock-in
*   Use core APIs with any framework or build custom integrations
*   Switch frameworks as needs evolve without rewriting agent code

Framework-agnostic APIs provide core capabilities (Employment Spec access, prompt management, context compilation, observability, Hub integration) that work independently of frameworks.

### Multi-Language Support

**Multi-language support** is the provision of SDKs in multiple programming languages (Python, Java) with consistent logical APIs and language-appropriate idioms. Multi-language support enables:
*   **Language flexibility**: Organizations can develop agents in their preferred languages
*   **API consistency**: Same logical API groups across languages
*   **Language idioms**: Language-appropriate idioms for better developer experience
*   **Feature parity**: Equivalent functionality across languages

Multi-language support is essential because different organizations prefer different languages, and some agentic frameworks are language-specific.

### API Groups

Seer Agent SDK organizes capabilities into logical API groups:
*   **Employment Spec APIs**: Retrieve, cache, and access Employment Specifications
*   **Prompt APIs**: Retrieve prompts with A/B testing, authority enforcement, and autonomy level support
*   **Context Compiler APIs**: Compile context from Enterprise Knowledge, Enterprise Memory, Agent Memory, and Hub Request Context
*   **Observability APIs**: Metrics, tracing, structured logging, auto-instrumentation
*   **Hub Integration APIs**: Tool discovery/calling, Stores, Knowledge Services, Memory Services, Events APIs

These API groups provide comprehensive capabilities for agent development while maintaining clear organization and consistency.

### Framework Builders

**Framework builders** are optional convenience layers that provide framework-specific builders for popular Python frameworks (LangGraph, Strands, OpenAPI). Framework builders:
*   Simplify common patterns for popular frameworks
*   Provide framework-specific idioms and patterns
*   Are optional—developers can use core APIs directly
*   Do not create framework lock-in—core APIs remain framework-agnostic

Framework builders enable developers to use popular frameworks more easily while maintaining the flexibility to use core APIs with any framework.

## Conceptual Models / Frameworks

### The SDK Architecture Model

Seer Agent SDK provides a layered architecture:

```
Agent Application (LangGraph, Strands, OpenAPI, Custom)
    ↑
Framework Builders (Optional: LangGraph, Strands, OpenAPI)
    ↑
Core SDK APIs (Framework-Agnostic)
    ├── Employment Spec APIs
    ├── Prompt APIs
    ├── Context Compiler APIs
    ├── Observability APIs
    └── Hub Integration APIs
    ↑
Seer & Hub Services
```

This layered architecture enables framework flexibility while providing convenience for popular frameworks.

### The Multi-Language Consistency Model

Multi-language SDKs maintain consistency through:
*   **Logical API groups**: Same API groups across languages
*   **Capability parity**: Equivalent functionality across languages
*   **Language idioms**: Language-appropriate idioms while maintaining logical consistency

This model enables developers to switch languages or work across languages while maintaining familiarity with SDK capabilities.

## Systemic and Enterprise Considerations

### Framework Ecosystem Support

Seer Agent SDK must support diverse framework ecosystems:
*   **Python frameworks**: LangGraph, LangChain, Strands, AutoGen, CrewAI
*   **Java frameworks**: Custom frameworks, Spring-based agents
*   **OpenAPI frameworks**: Framework-agnostic OpenAPI-based agents

Framework-agnostic core APIs enable support for this diversity without requiring framework-specific implementations for every framework.

### Language Preferences

Different organizations prefer different languages:
*   **Python**: Dominant in AI/ML ecosystem, preferred for data science teams
*   **Java**: Required for enterprise Java applications, preferred for backend services

SDKs must support multiple languages to enable broad adoption across organizations with different language preferences.

### Developer Productivity

SDK design directly impacts developer productivity:
*   **API simplicity**: Simple, intuitive APIs reduce learning curve
*   **Consistency**: Consistent APIs across capabilities and languages reduce cognitive load
*   **Documentation**: Well-documented APIs with examples improve developer experience
*   **Error handling**: Clear error messages and handling improve debugging efficiency

Developer productivity directly impacts agent development efficiency and adoption.

## Common Misconceptions & Failure Modes

### Misconception: Framework-Specific SDKs Are Better

Some developers assume that framework-specific SDKs (e.g., LangGraph-only SDK) are better than framework-agnostic SDKs. However, framework-specific SDKs create lock-in and prevent organizations from using multiple frameworks or switching frameworks as needs evolve.

**Failure mode**: Organizations adopt framework-specific SDKs, creating lock-in that prevents framework flexibility and limits future options.

### Misconception: Single-Language SDKs Are Sufficient

Some organizations assume that single-language SDKs (typically Python-only) are sufficient. However, enterprise organizations often require multiple languages, and some frameworks are language-specific.

**Failure mode**: Organizations adopt single-language SDKs, forcing teams to use languages they don't prefer or preventing adoption in language-specific environments.

### Misconception: Framework Builders Create Lock-In

Some developers assume that framework builders create framework lock-in. However, framework builders are optional convenience layers; core APIs remain framework-agnostic, enabling developers to switch frameworks or use core APIs directly.

**Failure mode**: Developers avoid framework builders, missing convenience benefits, or assume lock-in, avoiding framework builders unnecessarily.

## Practical Implications

### SDK Selection

Organizations should select SDKs based on:
*   **Framework support**: Does the SDK support the frameworks the organization uses?
*   **Language support**: Does the SDK support the languages the organization prefers?
*   **API consistency**: Are APIs consistent across languages and frameworks?
*   **Developer experience**: Does the SDK provide good developer experience?

SDK selection directly impacts developer productivity and agent development efficiency.

### Framework Strategy

Organizations should develop a framework strategy that:
*   **Supports multiple frameworks**: Enables teams to choose frameworks that fit their needs
*   **Avoids lock-in**: Uses framework-agnostic APIs to prevent framework lock-in
*   **Leverages convenience**: Uses framework builders when they provide value without creating lock-in

Framework strategy directly impacts long-term flexibility and developer satisfaction.

## Cross-References

*   **Section 5.13.1 (SDK Needs for Agent Development)**: Establishes the framework-agnostic and multi-language requirements that Seer Agent SDK addresses
*   **Section 20.2 (SDK Capabilities)**: Describes the specific SDK capabilities
*   **Section 20.3 (Development Workflow)**: Describes how the SDK supports development workflows

---

**References:**

*   `seer-design/subsystems/seer-agent-sdk/README.md` — Seer Agent SDK design
*   `seer-design/implementation-concepts/sdk-development-experience.md` — SDK development experience concept
