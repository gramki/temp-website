# ADR-0012: Control Plane vs Data Plane Channel Separation

## Status

Accepted

## Date

2026-01-06

## Context

Hub serves two fundamentally different types of operations:

1. **Hub Administration**: Managing workbenches, scenarios, agents, queues, configurations
2. **Business Operations**: Initiating requests, processing tasks, completing work

These have different characteristics:
- Administration: Lower volume, higher privilege, internal users
- Business operations: Higher volume, external users, public-facing

Mixing these creates challenges:
- Security boundaries become complex
- Scaling requirements differ
- Rate limiting needs differ

## Decision

**Separate API channels into Control Plane (Hub administration) and Data Plane (business operations).**

### Control Plane Channels
| Channel | Persona | Purpose |
|---------|---------|---------|
| Tenant Admin | Administrator | Subscription management |
| Creator | Process Architect, Developer | Design and development |
| Agent | Agent | Task processing |
| Supervisor | Supervisor | Operations management |
| Auditor | Auditor | Compliance review |

### Data Plane Channel
| Channel | Persona | Purpose |
|---------|---------|---------|
| Business User | Customer, Employee, System | Request initiation |

### Key Differences

| Aspect | Control Plane | Data Plane |
|--------|---------------|------------|
| Users | Internal Hub users | Business domain actors |
| Volume | Lower | Higher |
| Access | Authenticated Hub users | Customer/Employee/System identity |
| Operations | Hub administration | Business operations |
| Scaling | Standard | High-throughput |

### Implications
- Different routing paths in gateway
- Different rate limiting policies
- Different security policies
- Can be scaled independently

## Consequences

### Positive
- **Clear security boundaries**: Business users can't access admin APIs
- **Independent scaling**: Data plane can scale for high volume
- **Simpler policies**: Different rules per plane
- **Performance isolation**: Admin operations don't affect business operations

### Negative
- **Two patterns to understand**: Developers must understand plane distinction
- **Routing complexity**: Gateway must route to correct plane

### Neutral
- Agent channel is Control Plane (agents are Hub users, not business domain actors)

## Related

- [REST Channels](../06-ux-architecture/tenant-domain/rest-channels.md)
- [MCP Channels](../06-ux-architecture/tenant-domain/mcp-channels.md)
- [Heracles Gateway](../05-infrastructure/heracles-gateway.md)

