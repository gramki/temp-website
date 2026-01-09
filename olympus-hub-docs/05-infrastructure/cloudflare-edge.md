# Cloudflare Edge

> **Status:** 🔴 Stub — Placeholder for expansion

## Overview

**Cloudflare** provides the edge layer for Olympus Hub, handling DNS, CDN, DDoS protection, and edge security for all external traffic entering the Hub platform.

---

## Purpose in Olympus Hub

Cloudflare provides:

- **DDoS Protection** — Layer 3/4/7 attack mitigation
- **WAF** — Web Application Firewall rules
- **CDN** — Static asset caching and delivery
- **DNS** — Authoritative DNS with global anycast
- **SSL/TLS** — Edge termination and origin certificates

---

## Traffic Flow

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│    Client    │────►│  Cloudflare  │────►│   Heracles   │
│              │     │    Edge      │     │   Gateway    │
└──────────────┘     └──────────────┘     └──────────────┘
                            │
                            ▼
                    ┌──────────────┐
                    │   Origin     │
                    │   Servers    │
                    └──────────────┘
```

---

## MCP Session Support

For long-lived MCP sessions, Cloudflare is configured to:

- **Extended Timeouts** — Support 30+ minute sessions
- **No Buffering** — Stream-through for chunked responses
- **Session Affinity** — Route to same origin when possible
- **Keep-Alive** — Maintain persistent connections

---

## Security Configurations

### WAF Rules

- Block common attack patterns (SQLi, XSS)
- Custom rules for Hub-specific endpoints
- Rate limiting per IP/client

### Bot Management

- Challenge suspicious traffic
- Allow known good bots
- Block malicious automation

### Access Policies

- IP allowlists for admin endpoints
- Geo-blocking where required
- mTLS for origin connections

---

## Performance Optimizations

| Feature | Configuration |
|---------|---------------|
| **Caching** | Static assets, API responses where applicable |
| **Compression** | Brotli/gzip for text responses |
| **HTTP/3** | Enabled for supported clients |
| **Early Hints** | Preload critical resources |

---

## Integration with Hub

### DNS Records

- `hub.olympus.tech` — Main Hub endpoint
- `api.hub.olympus.tech` — API gateway
- `mcp.hub.olympus.tech` — MCP endpoints

### SSL Certificates

- Cloudflare-managed edge certificates
- Origin certificates for Heracles
- Full (strict) SSL mode

---

## Observability

Cloudflare provides:

- **Access Logs** — Request logs to Olympus Watch
- **Analytics** — Traffic and performance metrics
- **Security Events** — Attack detection and mitigation logs

---

## Related Documentation

- [Heracles Gateway](./heracles-gateway.md) — Origin gateway
- [Traffic Management](./traffic-management.md) — Internal traffic routing

---

*Expand this document with specific rule configurations, worker scripts, and failover procedures.*

