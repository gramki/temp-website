# ADR-0008: Persona-Channel-UseCase Meta Approach

## Status

Accepted

## Date

2026-01-06

## Context

Hub's UX architecture needed organizing principles to guide how applications, interfaces, and services are structured. Without clear principles, there was risk of:

- Inconsistent experiences across different user types
- Duplication of functionality across channels
- Difficulty adding new channels or personas
- Unclear ownership of capabilities

Key questions:
1. How should we organize applications? By function? By technology? By user type?
2. How should we handle multiple delivery channels (Web, Mobile, Teams, AI)?
3. How should we structure interfaces within applications?

## Decision

**Adopt three organizing principles for UX architecture: Persona-Focused, Channel-Agnostic, Use-Case Driven.**

### 1. Persona-Focused
- Each persona has dedicated applications optimized for their work
- Common capabilities are shared across personas
- Specialized views and tools per role
- Examples: Agent Desk, Supervisor Desk, Hub Control Center

### 2. Channel-Agnostic
- Headless access services provide core functionality
- Channel adapters render for specific platforms
- Same capabilities available through multiple delivery mechanisms
- Examples: Web, Mobile, MS Teams, Email, AI Assistants all access same backend services

### 3. Use-Case Driven
- Interfaces organized by what users need to accomplish
- Focus on workflows, not just screens
- Task completion, not feature lists

## Consequences

### Positive
- **Consistent experience**: Users get same capabilities regardless of channel
- **Clear ownership**: Each persona's app has clear responsibility
- **Extensible**: New channels added without changing core services
- **User-centered**: Design focused on user goals, not technology

### Negative
- **More artifacts**: Separate applications per persona to maintain
- **Coordination required**: Changes may affect multiple persona apps
- **Complexity**: Headless + adapter pattern adds architectural layers

### Neutral
- Requires clear persona definitions (see Personas and Journeys documentation)

## Related

- [UX Architecture Overview](../06-ux-architecture/README.md)
- [Personas and Journeys](../08-personas-and-journeys/README.md)
- [MCP Channels](../06-ux-architecture/tenant-domain/mcp-channels.md)
- [REST Channels](../06-ux-architecture/tenant-domain/rest-channels.md)

