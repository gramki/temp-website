# ADR-0009: Headless Access Services with Channel Adapters

## Status

Accepted

## Date

2026-01-06

## Context

Hub needs to support multiple interaction channels:
- Web applications (Agent Desk, Supervisor Desk, Control Center)
- Mobile applications
- MS Teams integration (bots, chat groups)
- Email notifications with CTAs
- AI assistants (ChatGPT, Claude, Gemini)
- Programmatic integrations (REST APIs)

Building separate backends for each channel would result in:
- Duplicated business logic
- Inconsistent behavior across channels
- High maintenance burden
- Slow time-to-market for new channels

## Decision

**Implement Hub capabilities as headless access services with channel adapters for rendering.**

Architecture:
```
Channel Adapters (Web, Mobile, Teams, Email, AI)
                    │
                    ▼
    Headless Access Services (MCP, REST, GraphQL)
                    │
                    ▼
              Hub Services
```

### Headless Access Services
- **MCP Gateway**: For AI agents and assistants
- **REST APIs**: For web, mobile, and system integrations
- **GraphQL**: For flexible data queries (where needed)

### Channel Adapters
- **Web**: Angelos components rendered in browser
- **Mobile**: Native or React Native apps
- **MS Teams**: Bot Framework integration
- **Email**: Hercules Launcher for CTAs
- **AI Assistants**: MCP tool invocation

### Key Principle
Channel adapters handle presentation and interaction patterns; headless services handle business logic.

## Consequences

### Positive
- **Single source of truth**: Business logic in one place
- **Consistent behavior**: All channels execute same logic
- **New channels are easy**: Add adapter, get all capabilities
- **API-first design**: Good for integrations and testing

### Negative
- **Additional layer**: Adapter pattern adds complexity
- **Channel limitations**: Some channels can't express all capabilities
- **Latency**: Additional hop through adapter

### Neutral
- Each channel may expose subset of capabilities based on UX constraints
- Some capabilities may need channel-specific optimizations

## Related

- [UX Architecture Overview](../06-ux-architecture/README.md)
- [MCP Channels](../06-ux-architecture/tenant-domain/mcp-channels.md)
- [REST Channels](../06-ux-architecture/tenant-domain/rest-channels.md)
- [Heracles Gateway](../05-infrastructure/heracles-gateway.md)
- [MCP Router](../05-infrastructure/mcp-router.md)

