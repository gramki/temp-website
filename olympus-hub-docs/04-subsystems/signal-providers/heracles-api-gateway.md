# Heracles - API Gateway

Heracles is the I/O Gateway for **HTTP/REST signals**—API calls from external systems, user interfaces, and integration partners. As Olympus's Traffic Management as a Service, Heracles offers resilient, flexible, and observable traffic management encompassing Ingress, Egress, and Service Mesh components.

> **Olympus Academy:** [Heracles Documentation](https://heracles.olympus.tech/)

## Overview

| Attribute | Value |
|-----------|-------|
| **Signal Type** | HTTP/REST messages |
| **Protocol** | HTTP/1.1, HTTP/2, WebSocket, MCP |
| **Direction** | Inbound (requests) and Outbound (responses) |
| **Role** | Senses API calls, executes Triggers, creates Requests |

## Key Components (from Olympus Academy)

| Component | Description |
|-----------|-------------|
| **Ingress** | Manages inbound traffic from external sources |
| **Egress** | Controls outbound traffic to external services |
| **Service Mesh** | Manages inter-service communication within the cluster |
| **Hygieia** | Manages Kong native ingress objects with custom resources for Zeta-specific routing |

## Architectural Context

Heracles serves as the HTTP entry point for Hub, translating API calls into standardized Requests:

```
┌─────────────────────────────────────────────────────────┐
│                    EXTERNAL CLIENTS                      │
│   (Web Apps, Mobile Apps, Partner Systems, Agents)      │
└────────────────────────┬────────────────────────────────┘
                         │ HTTP/REST
                         ▼
┌─────────────────────────────────────────────────────────┐
│                      HERACLES                            │
│                                                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │ Protocol    │  │ Trigger     │  │ Request     │      │
│  │ Handler     │→ │ Executor    │→ │ Router      │      │
│  └─────────────┘  └─────────────┘  └─────────────┘      │
│                                                          │
│  Protocols: HTTP/REST, WebSocket, MCP (Streamable HTTP) │
└────────────────────────┬────────────────────────────────┘
                         │ Request
                         ▼
                   OPERATIONS CENTER
```

## Request Types Handled

| Request Type | Originator | Use Case |
|--------------|------------|----------|
| **Service Request** | End users, Customers | Self-service portals, mobile apps |
| **Business Request** | Operations teams | Admin portals, internal tools |
| **System Request** | Machines, Integrations | API integrations, webhooks |

## Trigger Configuration

Heracles executes Triggers to bind HTTP requests to Hub Requests:

```yaml
# Example: Workbench Trigger for REST API
trigger:
  name: "customer-dispute-api"
  gateway: heracles
  
  # HTTP matching
  filter:
    method: POST
    path: "/api/v1/disputes"
    content_type: "application/json"
  
  # Authentication
  access:
    auth_required: true
    auth_methods: ["JWT", "API_KEY"]
    scopes: ["disputes:create"]
  
  # Transformation
  transform:
    request_type: "DisputeFilingRequest"
    mapping:
      customer_id: "$.body.customer_id"
      transaction_id: "$.body.transaction_id"
      reason: "$.body.reason"
      amount: "$.body.amount"
      # Headers to Request context
      correlation_id: "$.headers.X-Correlation-ID"
      tenant_id: "$.headers.X-Tenant-ID"
  
  # Target
  target:
    workbench: "dispute-operations"
    scenario: "dispute-filing"
  
  # Response mapping
  response:
    success:
      status: 202
      body:
        request_id: "$.request.id"
        status: "ACCEPTED"
    error:
      status: 400
      body:
        error: "$.error.message"
```

## Capabilities

### Protocol Support
- **HTTP/1.1 & HTTP/2**: Standard REST APIs
- **WebSocket**: Real-time bidirectional communication
- **MCP (Streamable HTTP)**: Model Context Protocol for AI agents
- **GraphQL**: (Future) GraphQL endpoint support

### Authentication & Authorization
- JWT validation (Bearer tokens)
- API Key authentication
- OAuth 2.0 / OIDC integration
- mTLS for service-to-service
- SPIFFE/SPIRE for workload identity

### Rate Limiting & Quotas
- Per-client rate limiting
- Quota enforcement
- Burst handling
- Graceful degradation

### Request Routing
- Path-based routing to Workbenches
- Header-based routing
- Content-based routing

### Response Handling
- Transform Operation responses to HTTP
- Status code mapping
- Error response formatting
- CORS handling

## MCP Support

Heracles provides special support for Model Context Protocol (MCP) for AI agent interactions:

| MCP Feature | Heracles Support |
|-------------|------------------|
| **Streamable HTTP** | Chunked transfer encoding for long-running sessions |
| **Session Management** | Transport session ID generation and tracking |
| **Tool Discovery** | Route tool/resource discovery requests |
| **Progress Reporting** | Stream progress frames to clients |

See [Heracles Gateway Infrastructure](../../05-infrastructure/heracles-gateway.md) for detailed MCP configuration.

## Kong Plugin Architecture

Heracles operates as a Kong plugin ecosystem:

| Plugin Type | Purpose |
|-------------|---------|
| **Authentication** | JWT, API Key, OAuth validation |
| **Authorization** | Policy enforcement, scope checking |
| **Rate Limiting** | Request throttling and quotas |
| **Transformation** | Request/response modification |
| **Logging** | Request tracing and observability |

## Integration with Kubernetes

Heracles uses Kubernetes Custom Resources for configuration:

| CRD Version | Purpose |
|-------------|---------|
| **V1 CRDs** | Legacy ingress configuration |
| **V2 Zone Ingress** | Modern zone-level ingress management |

## Integration Points

| System | Integration |
|--------|-------------|
| **Kong** | Core traffic management engine |
| **Cipher IAM** | JWT validation, SPIFFE identity |
| **Olympus Atlantis** | Deployed via "Olympus Atlantis Traffic" parent chart |
| **Watch** | Observability and monitoring integration |

## Observability

| Metric | Description |
|--------|-------------|
| `heracles.requests.received` | Total HTTP requests |
| `heracles.requests.authenticated` | Authenticated requests |
| `heracles.requests.authorized` | Authorized requests |
| `heracles.hub_requests.created` | Hub Requests created |
| `heracles.latency.p99` | 99th percentile latency |

## Related Documentation

- [Olympus Academy - Heracles](https://heracles.olympus.tech/)
- [Heracles Gateway Infrastructure](../../05-infrastructure/heracles-gateway.md) - Detailed Kong/MCP configuration
- [MCP Router](../../05-infrastructure/mcp-orchestrator.md) - MCP tool orchestration
- [Hub Architecture - Signals](../../02-system-design/hub-architecture.md#13-signals)
- [Cipher IAM](../supporting-systems/cipher-iam.md) - Authentication/authorization

---

*Status: 🟡 WIP - Definition phase*

