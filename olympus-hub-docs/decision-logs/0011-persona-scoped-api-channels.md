# ADR-0011: Persona-Scoped API Channels

## Status

Accepted

## Date

2026-01-06

## Context

Hub exposes APIs via both MCP (for AI assistants) and REST (for web/mobile/integrations). These APIs need to be organized for discoverability, security, and usability.

Options considered:
1. **Function-based organization**: `/api/tasks/*`, `/api/requests/*`, `/api/queues/*`
2. **Persona-based organization**: `/api/agent/*`, `/api/supervisor/*`, `/api/admin/*`
3. **Hybrid approach**: Mix of both

Function-based organization:
- Pros: Intuitive for developers, RESTful
- Cons: Authorization complex (who can access which endpoints?), discovery overwhelming

Persona-based organization:
- Pros: Clear authorization boundary, curated experience per role
- Cons: Some duplication across personas

## Decision

**Organize both MCP and REST APIs by persona, providing curated tool/endpoint sets per role.**

### API Channels by Persona

| Channel | Base Path | Persona | Purpose |
|---------|-----------|---------|---------|
| Tenant Admin | `/api/admin/v1` | Administrator | Subscription management |
| Creator | `/api/creator/v1` | Process Architect, Developer | Design and development |
| Agent | `/api/agent/v1` | Agent (Human/AI) | Task processing |
| Supervisor | `/api/supervisor/v1` | Supervisor | Operations management |
| Business User | `/api/business/v1` | Customer, Employee, System | Request initiation |
| Auditor | `/api/auditor/v1` | Auditor | Compliance review |

### Principles
1. Each persona gets exactly the APIs they need
2. Authorization is simpler (role = channel access)
3. API discovery returns only relevant capabilities
4. Same pattern for both MCP and REST

### Handling Overlap
When multiple personas need similar functionality (e.g., both Agent and Supervisor can view tasks):
- Include in both channels
- Implementation delegates to shared service
- May have persona-specific variations (Supervisor sees all tasks, Agent sees assigned tasks)

## Consequences

### Positive
- **Clear authorization**: Channel access = role check
- **Curated experience**: Each persona sees relevant APIs only
- **Simpler clients**: No need to filter by permission
- **Consistent pattern**: Same for MCP and REST

### Negative
- **Some duplication**: Similar endpoints across personas
- **Documentation overhead**: Document per persona
- **Discovery by role**: Must know your role first

### Neutral
- Internal implementation can share logic across channels

## Related

- [REST Channels](../06-ux-architecture/tenant-domain/rest-channels.md)
- [MCP Channels](../06-ux-architecture/tenant-domain/mcp-channels.md)
- [Personas and Journeys](../08-personas-and-journeys/README.md)

