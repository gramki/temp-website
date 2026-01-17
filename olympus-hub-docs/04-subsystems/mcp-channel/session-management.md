# Session Management

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-17

MCP sessions provide authenticated, stateful connections between MCP clients and MCP Servers. Sessions are managed up to the MCP Gateway and support resource subscriptions for real-time updates.

---

## Overview

| Attribute | Value |
|-----------|-------|
| **Scope** | MCP Client ↔ MCP Gateway (not beyond) |
| **Authentication** | OAuth 2.0 (client handles OAuth flow) |
| **State** | Session-bound resource subscriptions |
| **Lifecycle** | Established on connection, terminated on inactivity or explicit close |
| **Applicability** | Scenario-based templates only (machine-template is stateless) |

---

## Session Scope

**MCP Session is relevant only up to MCP Gateway:**

```
┌─────────────────────────────────────────────────────────────────┐
│                    MCP CLIENT                                   │
│              (ChatGPT, Claude, Gemini)                           │
└────────────────────────────┬────────────────────────────────────┘
                             │ MCP Protocol
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    MCP GATEWAY                                  │
│              (Session Boundary)                                 │
│  - Session established here                                     │
│  - Session terminated here                                     │
│  - Resource subscriptions managed here                         │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
                    MCP Channel / Hub Services
                    (No session concept)
```

---

## Session Establishment

### OAuth Flow

The client handles the OAuth flow and presents an access token to the MCP Gateway:

```
1. Client initiates OAuth flow (out-of-band browser link or client-provided mechanism)
2. User authenticates and grants access
3. Client receives access token
4. Client connects to MCP Gateway with access token
5. MCP Gateway validates token (JWT validation)
6. MCP Gateway establishes session
7. Session ID returned to client
```

**Note:** The mechanisms for how a client might get an access token are left to the client implementation. Hub provides:
- Out-of-band browser link for user authentication (for delegation flows)
- Client-provided certificate mechanism (for alternative auth flows)

---

## Session Termination

### Termination Triggers

| Trigger | Description |
|---------|-------------|
| **Client-initiated** | Client explicitly terminates session |
| **Server-initiated** | Server terminates if client socket is broken |
| **Inactivity timeout** | Session terminated after inactivity period (configurable in CRD) |
| **Token expiration** | Session terminated when access token expires |

### Inactivity Timeout

Configured per MCP Server CRD:

```yaml
spec:
  session:
    inactivity_timeout: 30m  # Session terminated after 30 minutes of inactivity
```

**Behavior:**
- Timer resets on any client activity (tool call, resource subscription, etc.)
- If no activity for `inactivity_timeout` duration, session is terminated
- Client must re-establish session to continue

---

## Session Limits

### Max Subscriptions

Maximum concurrent resource subscriptions per session:

```yaml
spec:
  session:
    max_subscriptions: 50  # Maximum concurrent resource subscriptions
```

**Behavior:**
- Client can subscribe to multiple resources (requests, tasks, queues, etc.)
- Subscription count limited by `max_subscriptions`
- If limit reached, new subscriptions are rejected
- Client must unsubscribe before subscribing to new resources

---

## Session-Bound Resource Subscriptions

**Resource subscriptions are MCP-session bound:**

- Subscriptions cannot persist beyond session
- Client must re-subscribe on reconnection
- Each subscription is tied to a specific session ID
- Session termination automatically unsubscribes all resources

### Subscription Lifecycle

```
1. Client establishes session
2. Client subscribes to resource: resources/subscribe("request://REQ-123")
3. Server confirms subscription
4. Server sends notifications on resource changes
5. Client unsubscribes: resources/unsubscribe("request://REQ-123")
   OR
   Session terminates → all subscriptions automatically removed
```

---

## Session State

Session state includes:

| State Element | Description |
|---------------|-------------|
| **Session ID** | Unique identifier for the session |
| **User Identity** | Extracted from access token (JWT claims) |
| **MCP Server** | Which MCP Server this session is connected to |
| **Resource Subscriptions** | List of subscribed resources |
| **Last Activity** | Timestamp of last client activity |
| **Access Token** | Cached for authorization checks |

---

## Stateless Templates

**Note:** `machine-template` is stateless and does not use session management:

- No session establishment required
- No resource subscriptions
- Each tool call is independent
- Authentication per request (JWT validation)

---

## Related Documentation

- [MCP Server CRD](./mcp-server-crd.md) — Session configuration in CRD
- [Resource Management](./resource-management.md) — Resource subscriptions
- [MCP Router](../../05-infrastructure/mcp-router.md) — Gateway infrastructure

---

*TODO: C3-level details — session persistence, reconnection handling, token refresh*
