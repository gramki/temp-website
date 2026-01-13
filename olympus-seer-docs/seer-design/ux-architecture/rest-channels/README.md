# Seer REST Channels

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13

---

## Overview

Seer REST channels provide persona-specific API access for the UX layer. Each desk consumes APIs from its corresponding REST channel, ensuring role-appropriate access and consistent interaction patterns.

---

## Architecture

### Hybrid Channel Structure

Seer uses a **hybrid REST channel architecture**:

1. **Hub-Extended Channels**: Inherit from Hub's REST channels and extend with Seer-specific endpoints
2. **Seer-Native Channels**: Entirely new channels for Seer-specific capabilities

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         SEER REST CHANNELS                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   HUB-EXTENDED CHANNELS              SEER-NATIVE CHANNELS                   │
│   ─────────────────────────          ─────────────────────────              │
│   ┌───────────────────────┐          ┌───────────────────────┐              │
│   │ APO Channel           │          │ CSA Channel           │              │
│   │ /api/seer/apo/v1      │          │ /api/seer/csa/v1      │              │
│   │ (extends Hub APO)     │          │ (Seer-native)         │              │
│   └───────────────────────┘          └───────────────────────┘              │
│   ┌───────────────────────┐          ┌───────────────────────┐              │
│   │ ARE Channel           │          │ COS Channel           │              │
│   │ /api/seer/are/v1      │          │ /api/seer/cos/v1      │              │
│   │ (extends Hub ARE)     │          │ (Seer-native)         │              │
│   └───────────────────────┘          └───────────────────────┘              │
│   ┌───────────────────────┐          ┌───────────────────────┐              │
│   │ KMO Channel           │          │ AE Channel            │              │
│   │ /api/seer/kmo/v1      │          │ /api/seer/ae/v1       │              │
│   │ (extends Hub KMO)     │          │ (Seer-native)         │              │
│   └───────────────────────┘          └───────────────────────┘              │
│                                      ┌───────────────────────┐              │
│                                      │ ARAO Channel          │              │
│                                      │ /api/seer/arao/v1     │              │
│                                      │ (Seer-native)         │              │
│                                      └───────────────────────┘              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### MCP Channel Integration

All REST APIs are also exposed as MCP tools, allowing AI assistants to programmatically interact with Seer capabilities:

```
REST Endpoint                    →  MCP Tool
─────────────────────────────────   ───────────────────────────
GET /api/seer/apo/v1/agents      →  seer_apo_list_agents
GET /api/seer/csa/v1/patterns    →  seer_csa_list_patterns
POST /api/seer/ae/v1/versions    →  seer_ae_create_version
```

---

## Channel Inventory

| Channel | Type | Base Path | Desk Served |
|---------|------|-----------|-------------|
| [APO Channel](./apo-channel.md) | Hub-Extended | `/api/seer/apo/v1` | Agent Portfolio Desk |
| [CSA Channel](./csa-channel.md) | Seer-Native | `/api/seer/csa/v1` | Agent Design Desk |
| [AE Channel](./ae-channel.md) | Seer-Native | `/api/seer/ae/v1` | Agent Development Desk |
| [KMO Channel](./kmo-channel.md) | Hub-Extended | `/api/seer/kmo/v1` | Knowledge Governance Desk |
| [ARE Channel](./are-channel.md) | Hub-Extended | `/api/seer/are/v1` | Agent Operations Desk |
| [COS Channel](./cos-channel.md) | Seer-Native | `/api/seer/cos/v1` | Cognitive Health Desk |
| [ARAO Channel](./arao-channel.md) | Seer-Native | `/api/seer/arao/v1` | Agent Compliance Desk |

---

## Common Patterns

### Authentication

All channels use the same authentication mechanism as Hub:

```http
Authorization: Bearer <token>
X-Tenant-ID: <tenant-id>
```

### Pagination

List endpoints support cursor-based pagination:

```http
GET /api/seer/apo/v1/agents?limit=20&cursor=<cursor>
```

Response includes:
```json
{
  "items": [...],
  "next_cursor": "...",
  "has_more": true
}
```

### Filtering

List endpoints support common filtering patterns:

```http
GET /api/seer/apo/v1/agents?status=active&class=expense-approver
```

### Error Responses

Standard error format across all channels:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid agent ID format",
    "details": {
      "field": "agent_id",
      "reason": "Must be UUID format"
    }
  }
}
```

---

## Hub Channel Extension Pattern

For Hub-Extended channels, the extension pattern is:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   Hub APO Channel (/api/hub/apo/v1)                                         │
│   ─────────────────────────────────────────────────────────────────────     │
│   • Scenario management                                                     │
│   • Hub Application configuration                                           │
│   • General portfolio operations                                            │
│                                                                             │
│          │                                                                  │
│          │ extends                                                          │
│          ▼                                                                  │
│                                                                             │
│   Seer APO Channel (/api/seer/apo/v1)                                       │
│   ─────────────────────────────────────────────────────────────────────     │
│   • All Hub APO capabilities (proxied)                                      │
│   • + Agent portfolio operations                                            │
│   • + Autonomy level management                                             │
│   • + Business outcome tracking                                             │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Security

### Role-Based Access

Each channel enforces role-based access:

| Channel | Required Role |
|---------|--------------|
| APO | `seer:apo` or `hub:apo` |
| CSA | `seer:csa` |
| AE | `seer:ae` |
| KMO | `seer:kmo` or `hub:kmo` |
| ARE | `seer:are` or `hub:are` |
| COS | `seer:cos` |
| ARAO | `seer:arao` |

### Cross-Channel Access

Some consoles access multiple channels. The Agent Behavior Console, for example, accesses:
- COS Channel (behavior data)
- ARE Channel (operational data)
- AE Channel (agent configuration)

Access is granted based on user role combination.

---

## Document Index

- [APO Channel](./apo-channel.md) - Agent portfolio and autonomy APIs
- [CSA Channel](./csa-channel.md) - Design patterns and architecture APIs
- [AE Channel](./ae-channel.md) - Development, testing, and release APIs
- [KMO Channel](./kmo-channel.md) - Knowledge and memory governance APIs
- [ARE Channel](./are-channel.md) - Operations, health, and control APIs
- [COS Channel](./cos-channel.md) - Cognitive health and behavior APIs
- [ARAO Channel](./arao-channel.md) - Compliance, autonomy, and security APIs

---

*Status: 🟡 Draft — Structure defined, individual channel specs in development*
