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

## Machine Signal Emission via Webhook

Machines can emit signals to Hub through Heracles using **webhook endpoints**. Webhooks provide a simple HTTP-based push mechanism for Machines to send signals in real-time.

### Webhook Endpoint Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scoping** | Workbench-scoped endpoints |
| **Endpoint Pattern** | `https://heracles.olympus.tech/api/workbenches/{workbench-id}/signals` |
| **Method** | POST |
| **Protocol** | HTTP/HTTPS |
| **Provisioning** | Provisioned by tenant admin or authorized developers as resources |

### Signal Schema Validation

**Heracles validates webhook payloads against OpenAPI specification** for POST request body. The schema is defined in the Machine Definition or Machine Instance configuration.

**Validation Process:**
1. Machine sends HTTP POST request to webhook endpoint
2. Heracles validates request body against OpenAPI specification
3. If valid, Heracles normalizes to Signal Exchange format
4. If invalid, Heracles returns 400 Bad Request with validation errors

### Authentication Mechanisms

Webhook endpoints support multiple authentication mechanisms:

| Mechanism | Description | Configuration |
|-----------|-------------|---------------|
| **API Key** | Simple API key in header or query parameter | `X-API-Key` header or `?api_key=...` |
| **OAuth 2.0** | Bearer token authentication | `Authorization: Bearer <token>` |
| **mTLS** | Mutual TLS for service-to-service | Client certificate validation |
| **HMAC** | HMAC signature validation | `X-Hub-Signature` header |

### Example Machine Configuration

**Machine Definition (Schema):**
```yaml
machine_definition:
  id: "payment-switch"
  signal_emission:
    signals:
      - type: "payment.authorized"
        push:
          protocols: [webhook]
          schemas:
            webhook:
              openapi_spec:
                type: object
                required: [payment_id, amount, customer_id]
                properties:
                  payment_id:
                    type: string
                    description: "Unique payment identifier"
                  amount:
                    type: number
                    description: "Payment amount"
                  customer_id:
                    type: string
                    description: "Customer identifier"
                  timestamp:
                    type: string
                    format: date-time
                    description: "Payment authorization timestamp"
                  currency:
                    type: string
                    default: "USD"
```

**Machine Instance (Endpoint Configuration):**
```yaml
machine:
  id: "acme-payment-switch"
  definition_id: "payment-switch"
  workbench_id: "payment-operations"
  
  signal_emission:
    push:
      webhook:
        # Workbench-scoped endpoint
        endpoint: "https://heracles.olympus.tech/api/workbenches/payment-operations/signals"
        method: POST
        auth:
          type: api_key
          credentials_ref: "vault://secrets/acme/payment-switch/webhook-key"
```

### Example Webhook Request

**HTTP Request:**
```http
POST /api/workbenches/payment-operations/signals HTTP/1.1
Host: heracles.olympus.tech
Content-Type: application/json
X-API-Key: <api-key-from-vault>

{
  "payment_id": "pay_12345",
  "amount": 100.50,
  "customer_id": "cust_67890",
  "timestamp": "2026-01-15T10:30:00Z",
  "currency": "USD"
}
```

**Response (Success):**
```http
HTTP/1.1 202 Accepted
Content-Type: application/json

{
  "request_id": "req_abc123",
  "status": "ACCEPTED",
  "message": "Signal received and queued for processing"
}
```

**Response (Validation Error):**
```http
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
  "error": "Validation failed",
  "details": [
    {
      "field": "amount",
      "message": "must be a number"
    }
  ]
}
```

### Endpoint Provisioning

Webhook endpoints are provisioned as resources within a subscription and workbench:

1. **Tenant Admin** provisions endpoints for workbenches in their tenant
2. **Authorized Developers** can provision endpoints for accessible workbenches
3. Endpoints are tied to workbench lifecycle
4. Endpoint configuration includes authentication credentials and access policies

**Provisioning Example:**
```yaml
webhook_endpoint:
  id: "payment-ops-signals"
  workbench_id: "payment-operations"
  subscription_id: "prod-subscription"
  tenant_id: "acme-bank"
  
  endpoint: "https://heracles.olympus.tech/api/workbenches/payment-operations/signals"
  
  auth:
    methods: [api_key, oauth2]
    api_key:
      credentials_ref: "vault://secrets/payment-ops/webhook-key"
    oauth2:
      issuer: "https://auth.olympus.tech"
      scopes: ["webhook:send"]
  
  access_policies:
    allowed_machines: ["acme-payment-switch", "acme-gateway"]
    rate_limit: 1000  # requests per minute
```

For detailed configuration, see [Machine Registry](../registry-services/machine-registry.md) and [Machine Signal Emission Guide](../../10-guides/machine-signal-emission-guide.md).

## Related Documentation

- [Olympus Academy - Heracles](https://heracles.olympus.tech/)
- [Heracles Gateway Infrastructure](../../05-infrastructure/heracles-gateway.md) - Detailed Kong/MCP configuration
- [MCP Router](../../05-infrastructure/mcp-orchestrator.md) - MCP tool orchestration
- [Hub Architecture - Signals](../../02-system-design/hub-architecture.md#13-signals)
- [Cipher IAM](../supporting-systems/cipher-iam.md) - Authentication/authorization
- [Machine Registry](../registry-services/machine-registry.md)
- [Machine Signal Emission Guide](../../10-guides/machine-signal-emission-guide.md)
- [Machine Signal Emission Concept](../../02-system-design/implementation-concepts/machine-signal-emission.md) - Implementation concept

---

*Status: 🟡 WIP - Definition phase*

