# Kong for MCP (Heracles) — Gateway Design & Guidance

## Table of Contents
1. [Purpose & Scope](#purpose--scope)  
2. [Primer: MCP & Streamable HTTP](#primer-mcp--streamable-http)  
3. [Technical Specifications & References](#technical-specifications--references)  
4. [Desired Architecture](#desired-architecture)  
5. [Responsibilities: Heracles vs Orchestrators](#responsibilities-heracles-vs-orchestrators)  
6. [Session Management](#session-management)  
7. [Standard Headers & Trailers Contract](#standard-headers--trailers-contract)  
8. [Tuning Heracles for MCP](#tuning-heracles-for-mcp)  
9. [Authentication & Access Control](#authentication--access-control)  
10. [Application Identity Between Heracles and Backend](#application-identity-between-heracles-and-backend)  
11. [Observability](#observability)  
    - [Access Logs](#access-logs)  
    - [Tracing](#tracing)  
    - [Metrics](#metrics)  
12. [DoS Prevention](#dos-prevention)  
13. [Resource Routing](#resource-routing)  
14. [Plugin Guidance](#plugin-guidance)  
15. [Configuration Examples](#configuration-examples)  
16. [Operations Playbook](#operations-playbook)  
17. [Roadmap & Open Questions](#roadmap--open-questions)  

---

## Purpose & Scope

This document defines how **Heracles (our fork of Kong OSS)** should be configured and extended to act as a **gateway for MCP (Model Context Protocol)** traffic.

- **Scope:** Gateway responsibilities for MCP transports and sessions.  
- **Not in scope:** The design of **mcp-orch** (orchestration layer) and **mcp-resources** (resource service). These will be covered separately.  
- **Audience:** Developers and maintainers familiar with Kong internals, JWT-based auth, and OTel tracing.  

---

## Primer: MCP & Streamable HTTP

### MCP Concepts
- **Tools:** callable actions (functions).  
- **Prompts:** templates for model input.  
- **Resources:** retrievable entities like tickets, configs, PDFs.  

### Why MCP is Different
- Multi-turn, conversational interactions.  
- Long-lived sessions rather than single request/response.  
- One client session may involve multiple backends (through an orchestrator).  

### Streamable HTTP
- **JSON-RPC 2.0** over HTTP with **chunked transfer encoding**.  
- Each chunk = one JSON-RPC frame (request, response, notification, progress).  
- Works with standard HTTP infra (ALB, Kong, Cloudflare).  
- Proxy-friendly, debuggable, minimal complexity.  

---

## Technical Specifications & References

### Streamable HTTP
- **RFC 7230** - HTTP/1.1 Message Syntax and Routing
- **RFC 7231** - HTTP/1.1 Semantics and Content
- **RFC 7232** - HTTP/1.1 Conditional Requests
- **RFC 7233** - HTTP/1.1 Range Requests
- **RFC 7234** - HTTP/1.1 Caching
- **RFC 7235** - HTTP/1.1 Authentication
- **RFC 7540** - HTTP/2 (for future consideration)
- **RFC 9113** - HTTP/2 (obsoletes RFC 7540)
- **RFC 9114** - HTTP/3

### JSON-RPC 2.0
- **JSON-RPC 2.0 Specification** - [jsonrpc.org](https://www.jsonrpc.org/specification)
- **RFC 7159** - The JavaScript Object Notation (JSON) Data Interchange Format
- **RFC 8259** - The JavaScript Object Notation (JSON) Data Interchange Format (obsoletes RFC 7159)

### Model Context Protocol (MCP)
- **MCP Specification** - [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- **MCP GitHub Repository** - [github.com/modelcontextprotocol](https://github.com/modelcontextprotocol)
- **MCP Transport Specifications** - Including Streamable HTTP transport details
- **MCP Tool Definitions** - Standard tool interfaces and schemas
- **MCP Resource Management** - Resource discovery and access patterns

### HTTP Chunked Transfer Encoding
- **RFC 7230 Section 4.1** - Chunked Transfer Coding
- **RFC 2616 Section 3.6.1** - Chunked Transfer Coding (historical reference)

### Related Standards
- **RFC 7519** - JSON Web Token (JWT)
- **RFC 7517** - JSON Web Key (JWK)
- **RFC 7518** - JSON Web Algorithms (JWA)
- **OpenTelemetry Specification** - Distributed tracing and observability
- **W3C Trace Context** - Distributed tracing context propagation

---

## Desired Architecture

```
Client
  |
  v
Heracles (Kong-based Gateway)
  |
  ├── /mcp/<mcp-server-name>  →  mcp-orch (per MCP app)
  |
  └── /resources/<mcp-server-name>/… → mcp-resources (optional)
```

- **Multi-server entrypoints:** Each MCP app is exposed at `/mcp/<mcp-server-name>`.  
- **mcp-orch:** Handles JSON-RPC orchestration, backend fan-out, and result merging.  
- **mcp-resources:** Dedicated service for resources scoped under `<mcp-server-name>`.  

---

## Responsibilities: Heracles vs Orchestrators

### What Heracles Does
- Generates **transport session ID** for every new MCP connection.  
- Routes `/mcp/<mcp-server-name>` → corresponding **mcp-orch**.  
- Routes `/resources/<mcp-server-name>` → corresponding **mcp-resources**.  
- Validates JWTs and enforces claims.  
- Ensures transport hygiene: no buffering, proper timeouts, header preservation.  
- Provides observability: logs, traces, metrics.  
- Enforces quotas and rate limits at the edge.  

### What Heracles Does **Not** Do
- ❌ No JSON-RPC parsing or per-frame routing.  
- ❌ No mid-stream fan-out.  
- ❌ No tool/method-level policy enforcement.  
- ❌ No aggregation of partial responses.  

Those belong in **mcp-orch**.  

---

## Session Management

- Every new MCP client connection begins with a **transport handshake**.  
- Heracles plugin generates a **unique session ID** (UUID or ULID).  
- Session ID is added to all proxied requests as header:  
  ```
  X-MCP-Transport-Session: <session-id>
  ```  
- This ID ensures all activity in a session can be correlated across Heracles, mcp-orch, and backends.  
- Access logs, traces, and metrics must always include this session ID.  

---

## Standard Headers & Trailers Contract

### Headers (Heracles → mcp-orch / mcp-resources)
- `X-MCP-Transport-Session` — Unique transport session ID.  
- `X-Client-Id` — From JWT `sub`.  
- `X-Client-App` — From JWT claim (application).  
- `traceparent`, `baggage` — OTel context propagation.  

### Trailers (mcp-orch → Heracles → client)
- `X-MCP-Result-Summary` — `{method,id,status,duration_ms}`.  
- `X-MCP-Backend` — Name of backend service that handled the call.  
- `X-MCP-Error` — Error code or reason, if any.  

This contract ensures **end-to-end observability** without Heracles needing to parse JSON-RPC frames.  

---

## Tuning Heracles for MCP

- Disable proxy buffering to allow streaming.  
- Increase timeouts:  
  - Read/Write: 20–30 minutes.  
  - Connect: 10 seconds.  
- Align ALB idle timeouts with MCP session durations.  
- Preserve headers and trailers.  
- Ensure Cloudflare rules allow for long-lived connections.  

---

## Authentication & Access Control

- JWT validation with JWKS.  
- Claims enforced: `aud`, `sub`, `exp`.  
- Client identity mapped to Kong consumer.  
- Identity passed to mcp-orch / mcp-resources via headers.  

---

## Application Identity Between Heracles and Backend

### Application Identity Header Forwarding

Heracles acts as a gateway that forwards application identity information to backend services to enable proper authentication and authorization:

- **Header Forwarding**: Heracles passes the application's SPIFFE identity to backend services via the `X-Application-Identity` header:
  ```
  X-Application-Identity: <SPIFFE-JWT-SVID>
  ```
- **Backend Authentication**: Backend services can extract and validate the SPIFFE JWT-SVID to authenticate the calling application.
- **Authorization Context**: Backend services use the application identity for authorization decisions and audit logging.

### mTLS for Zone-Local Communications

For all interactions within the local 'zone' (internal service-to-service communication), Heracles uses mutual TLS (mTLS) with X.509-SVID:

- **Zone-Local mTLS**: All communications between Heracles and backend services within the same zone use mTLS with X.509-SVID certificates.
- **Application Identity Verification**: The X.509-SVID provides cryptographically verifiable application identity during the TLS handshake.
- **Enhanced Security**: mTLS ensures both parties can verify each other's identities, providing stronger security for internal communications.
- **Performance Optimization**: mTLS is used for zone-local traffic where the overhead is acceptable, while JWT-SVID headers are used for cross-zone or external communications.

### Implementation Details

- **Dual Authentication**: Backend services receive both the forwarded `X-Application-Identity` header and can verify the mTLS certificate for comprehensive identity validation.
- **Identity Correlation**: The SPIFFE ID from both the JWT-SVID header and X.509-SVID certificate should match for consistency.
- **Fallback Handling**: Backend services should gracefully handle cases where only one form of identity is available (e.g., external clients without mTLS).

---

## Observability

### Access Logs
Include at minimum:  
- `client_id`, `client_app`.  
- `mcp-server-name`.  
- `transport_session_id`.  
- `backend_app` (from trailers).  
- HTTP status, response size, duration.  

### Tracing
- Root span created at Heracles per session.  
- OTel context propagated downstream.  
- Support for **sampling directives**: target by client, subject, backend, or method, with percentage + duration.  

### Metrics
- Active sessions, concurrency.  
- Session duration histograms.  
- Throughput (bytes in/out).  
- Tool call latency and success rates (from trailers).  
- Quota consumption (per client/app).  

---

## DoS Prevention

- Per-client session caps (e.g., max 10 concurrent).  
- Rate limiting: requests/sec, bytes/sec.  
- Daily/monthly quota enforcement.  
- Detection of abnormal session patterns (too long, excessive progress chatter).  

---

## Resource Routing

- Resources are **scoped under each MCP app**.  
- Convention: `/resources/<mcp-server-name>/…`.  
- Routed directly from Heracles to **mcp-resources service**.  
- Authentication and access logs still enforced at Heracles.  
- Caching may be applied for static artifacts.  

---

## Plugin Guidance

### What to Implement
- **Session ID generator**.  
- **JWT validator**.  
- **Access-log enricher**.  
- **OTel injector** with sampling rules.  
- **Quota / rate limiter**.  

### What NOT to Implement
- JSON-RPC parsing.  
- Mid-stream routing or fan-out.  
- Tool/method-level policies.  

Keep plugins **thin** and **stream-safe**.  

---

## Configuration Examples

### Route Setup
```yaml
routes:
- name: mcp-booking
  paths: ["/mcp/booking"]
  service: booking-orch
- name: booking-resources
  paths: ["/resources/booking"]
  service: booking-resources
```

### Plugin Snippets
- **Session ID Plugin:** inject `X-MCP-Transport-Session`.  
- **JWT Plugin:** validate + forward claims.  
- **Rate Limiter:** Redis-backed, per-client.  

### ALB Idle Timeout
```
aws_lb_idle_timeout: 1200s
```

---

## Operations Playbook

- **Debugging:**  
  - Session drops: check ALB/Kong timeouts.  
  - Auth failures: verify JWKS rotation.  
  - Stalled streams: check buffering config.  

- **Dashboards:**  
  - Session concurrency.  
  - Latency histograms.  
  - Error rates.  
  - Quota usage.  

- **Incident Triage:**  
  - Edge issue (Heracles) vs Orchestrator vs Backend.  

---

## Roadmap & Open Questions

- Standardize header/trailer contract in MCP community.  
- Agree on quota semantics (per tool vs per session).  
- Support for dynamic sampling rules in Kong config.  
- Multi-region scaling of `/mcp/<name>` endpoints.  
- Potential for lightweight MCP-aware analytics at edge (without deep parsing).  

---
