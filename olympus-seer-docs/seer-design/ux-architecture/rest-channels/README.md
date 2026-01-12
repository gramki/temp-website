# Seer REST Channels

> **Status:** 🔴 Planning  
> **Last Updated:** 2026-01-13  
> **Related:** [UX Architecture Overview](../README.md) | [Hub REST Channels](../../../../olympus-hub-docs/06-ux-architecture/tenant-domain/rest-channels.md)

---

## Overview

REST channels provide programmatic access to Seer capabilities. Each persona has a dedicated REST channel scoped to their responsibilities and permissions.

---

## Architecture

### Hybrid Approach

Seer REST channels follow a hybrid approach:

1. **Hub Channel Extensions** — Some channels extend existing Hub channels with Seer-specific endpoints
2. **Seer-Native Channels** — Some channels are entirely Seer-specific

| Channel Type | Example | Base Path |
|--------------|---------|-----------|
| Hub Extension | AE Channel extends Creator | `/api/creator/v1/seer/...` |
| Seer Native | APO Channel | `/api/seer/apo/v1/...` |

### Base URL Structure

```
https://{tenant}.seer.olympus.io/api/{channel}/v1/...
```

| Component | Description |
|-----------|-------------|
| `{tenant}` | Tenant identifier |
| `{channel}` | Persona channel (e.g., `seer/apo`, `seer/are`) |
| `v1` | API version |

---

## Persona Channels

| Persona | Channel Path | Type | Documentation |
|---------|--------------|------|---------------|
| **APO** | `/api/seer/apo/v1` | Seer Native | [APO REST Channel](./apo-rest-channel.md) |
| **CSA** | `/api/seer/csa/v1` | Seer Native | [CSA REST Channel](./csa-rest-channel.md) |
| **AE** | `/api/creator/v1/seer` | Hub Extension | [AE REST Channel](./ae-rest-channel.md) |
| **KMO** | `/api/seer/kmo/v1` | Seer Native | [KMO REST Channel](./kmo-rest-channel.md) |
| **ARE** | `/api/seer/are/v1` | Seer Native | [ARE REST Channel](./are-rest-channel.md) |
| **COS** | `/api/seer/cos/v1` | Seer Native | [COS REST Channel](./cos-rest-channel.md) |
| **ARAO** | `/api/seer/arao/v1` | Seer Native | [ARAO REST Channel](./arao-rest-channel.md) |

---

## Common Capabilities

All REST channels share common capabilities:

### Authentication

```http
Authorization: Bearer {jwt_token}
X-Tenant-ID: {tenant_id}
```

- OAuth 2.0 / OIDC authentication
- JWT tokens with persona claims
- Tenant context required

### Rate Limiting

| Tier | Requests/Second | Burst |
|------|-----------------|-------|
| Standard | 100 | 200 |
| Premium | 500 | 1000 |
| Enterprise | Custom | Custom |

Rate limit headers:
```http
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1704139200
```

### Pagination

Standard pagination for list endpoints:

```http
GET /api/seer/apo/v1/agents?page=1&per_page=20

Response:
{
  "data": [...],
  "pagination": {
    "page": 1,
    "per_page": 20,
    "total": 100,
    "total_pages": 5
  }
}
```

### Error Responses

Standard error format:

```json
{
  "error": {
    "code": "AGENT_NOT_FOUND",
    "message": "Agent with ID 'xyz' not found",
    "details": {
      "agent_id": "xyz"
    },
    "request_id": "req-123"
  }
}
```

---

## Gateway Integration

### Heracles Gateway

All REST channels route through the Heracles API Gateway:

```
Client → Heracles Gateway → Seer API Services
                ↓
        Authentication
        Rate Limiting
        Request Routing
        Audit Logging
```

### Gateway Responsibilities

| Responsibility | Description |
|----------------|-------------|
| Authentication | Validate JWT tokens |
| Authorization | Check persona permissions |
| Rate Limiting | Enforce request limits |
| Routing | Direct to appropriate service |
| Audit | Log all requests |

---

## MCP Channel Equivalence

Every REST API is also available via MCP (Model Context Protocol) for AI assistant integration:

| REST Channel | MCP Server |
|--------------|------------|
| APO REST | `seer-apo-mcp` |
| CSA REST | `seer-csa-mcp` |
| AE REST | `seer-ae-mcp` |
| KMO REST | `seer-kmo-mcp` |
| ARE REST | `seer-are-mcp` |
| COS REST | `seer-cos-mcp` |
| ARAO REST | `seer-arao-mcp` |

### MCP Tool Mapping

Each REST endpoint maps to an MCP tool:

```
REST: GET /api/seer/apo/v1/agents/{id}
MCP:  seer_apo_get_agent(agent_id)

REST: POST /api/seer/apo/v1/autonomy/proposals
MCP:  seer_apo_create_autonomy_proposal(...)
```

---

## Cross-Channel Operations

Some operations span multiple channels:

### Example: Agent Deployment

```
1. AE finalizes agent (AE Channel)
   POST /api/creator/v1/seer/agents/{id}/versions

2. ARE reviews readiness (ARE Channel)
   POST /api/seer/are/v1/production-gates/{id}/review

3. ARE approves deployment (ARE Channel)
   POST /api/seer/are/v1/production-gates/{id}/approve

4. AE triggers deployment (AE Channel)
   POST /api/creator/v1/seer/agents/{id}/deploy
```

---

## Versioning

### Version Strategy

- Major version in URL path (`/v1/`, `/v2/`)
- Minor versions via content negotiation
- Deprecation notices 6 months before removal

### Version Headers

```http
Accept: application/vnd.seer.v1+json
X-API-Version: 1.2.3
```

---

## Documentation Standards

Each REST channel document includes:

1. **Overview** — Channel purpose and scope
2. **Base Path** — API base URL
3. **Authentication** — Auth requirements
4. **Endpoints** — Full endpoint listing
5. **Request/Response Schemas** — JSON schemas
6. **Error Codes** — Channel-specific errors
7. **MCP Equivalence** — MCP tool mapping
8. **Examples** — Usage examples

---

## Hub Integration

### Extending Hub Channels

For Hub extensions, Seer adds endpoints under a `/seer` prefix:

```
Hub Creator Channel: /api/creator/v1/
├── scenarios/
├── components/
└── seer/           ← Seer extension
    ├── agents/
    └── versions/
```

### Shared Endpoints

Some endpoints are shared with Hub:

| Endpoint | Hub | Seer Extension |
|----------|-----|----------------|
| `/scenarios` | Scenario management | Agent binding info |
| `/knowledge` | Knowledge base | Agent knowledge access |
| `/users` | User management | Persona mapping |

---

## Next Steps

Detailed documentation for each REST channel:

- [ ] [APO REST Channel](./apo-rest-channel.md)
- [ ] [CSA REST Channel](./csa-rest-channel.md)
- [ ] [AE REST Channel](./ae-rest-channel.md)
- [ ] [KMO REST Channel](./kmo-rest-channel.md)
- [ ] [ARE REST Channel](./are-rest-channel.md)
- [ ] [COS REST Channel](./cos-rest-channel.md)
- [ ] [ARAO REST Channel](./arao-rest-channel.md)

---

*Status: 🔴 Planning — Structure defined, detailed specs TBD*
