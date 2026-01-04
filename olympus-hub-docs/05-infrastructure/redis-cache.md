# Redis — Caching and Rate Limiting

> **Status:** 🔴 Stub — Placeholder for expansion

## Overview

**Redis** provides high-performance caching, rate limiting, and ephemeral data storage for Olympus Hub services.

---

## Purpose in Olympus Hub

Redis provides:

- **Rate Limiting** — Per-client and per-endpoint rate limiting
- **Session Cache** — Short-lived session data
- **Token Cache** — JWT and SVID caching
- **Distributed Locks** — Coordination primitives
- **Pub/Sub** — Real-time event distribution

---

## Use Cases

### Rate Limiting (Heracles Gateway)

Redis backs the rate limiter plugin in Heracles:

```yaml
plugins:
  - name: rate-limiting
    config:
      policy: redis
      redis:
        host: redis.hub-infra.svc
        port: 6379
        database: 0
      limit: 100
      window_size: 60
```

### Session State

Temporary session data for:

- MCP transport session metadata
- In-flight request state
- Authentication session cache

### Distributed Caching

- JWKS public key cache
- Service discovery cache
- Configuration cache

---

## Cluster Architecture

```
┌─────────────────────────────────────────────────────┐
│                  Redis Cluster                       │
│  ┌─────────┐   ┌─────────┐   ┌─────────┐           │
│  │ Master  │   │ Master  │   │ Master  │           │
│  │  Shard  │   │  Shard  │   │  Shard  │           │
│  │   1     │   │   2     │   │   3     │           │
│  └────┬────┘   └────┬────┘   └────┬────┘           │
│       │             │             │                 │
│  ┌────▼────┐   ┌────▼────┐   ┌────▼────┐           │
│  │ Replica │   │ Replica │   │ Replica │           │
│  └─────────┘   └─────────┘   └─────────┘           │
└─────────────────────────────────────────────────────┘
```

---

## Data Isolation

| Use Case | Database | TTL |
|----------|----------|-----|
| Rate Limiting | 0 | Per window |
| Session Cache | 1 | Session duration |
| Token Cache | 2 | Token expiry |
| Locks | 3 | Lock timeout |

---

## High Availability

- **Cluster Mode** — Automatic sharding and failover
- **Sentinel** — Master monitoring and promotion
- **Persistence** — RDB snapshots for recovery
- **Replication** — Synchronous replica writes

---

## Performance Tuning

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| `maxmemory-policy` | `volatile-lru` | Evict expired keys first |
| `tcp-keepalive` | `300` | Connection health |
| `timeout` | `0` | Persistent connections |

---

## Security

- **TLS** — Encrypted connections
- **ACL** — Per-service access control
- **Network Isolation** — VPC-only access

---

## Integration Points

| Service | Usage |
|---------|-------|
| **Heracles Gateway** | Rate limiting, session cache |
| **Signal Exchange** | Flow control counters |
| **MCP Orchestrator** | Session state cache |
| **Subscription Management** | Quota tracking |

---

## Monitoring

Metrics exported to Olympus Watch:

- `redis_connected_clients`
- `redis_used_memory_bytes`
- `redis_commands_processed_total`
- `redis_keyspace_hits_total`
- `redis_keyspace_misses_total`

---

## Related Documentation

- [Heracles Gateway](./heracles-gateway.md) — Rate limiting integration
- [Signal Exchange](../04-subsystems/signal-exchange/flow-controller.md) — Flow control
- [Olympus Watch](./olympus-watch.md) — Metrics collection

---

*Expand this document with operational runbooks, scaling procedures, and disaster recovery.*

