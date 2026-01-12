# Resource Quota Service

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-12  
> **Design Level**: C2 (Container)

---

## Overview

The Resource Quota Service tracks and enforces resource consumption limits for agents. It monitors resources consumed **by the agent itself** (not usage of the agent by users/customers — see [Fair Usage Budget Service](./fair-usage-budget-service.md) for that).

**Key Principle**: The sidecar can track request-level and API call metrics, while compute resources (CPU, memory, tokens) are tracked by external systems (Kubernetes, Model Gateway).

---

## Resource Tracking Scope

### What Sidecar Can Track

| Resource | Tracking Method |
|----------|-----------------|
| ✅ Inbound request count | Count from `/dispatch` traffic |
| ✅ Inbound request size | Bytes from `/dispatch` traffic |
| ✅ Inbound request rate | Requests per time window |
| ✅ Outbound call count | Count from Hub API calls |
| ✅ Outbound call size | Bytes from Hub API calls |
| ✅ Outbound call rate | Calls per time window |
| ✅ API rate limits | Rate limiting on outbound calls |

### What Sidecar Cannot Track (Tracked Elsewhere)

| Resource | Tracked By | Sidecar Visibility |
|----------|------------|-------------------|
| ❌ CPU usage | Kubernetes | Cannot access |
| ❌ Memory usage | Kubernetes | Cannot access |
| ❌ Token consumption | Model Gateway | Can see API calls, not tokens |
| ❌ Storage usage | Memory Service | Cannot access |

---

## Quota Configuration

### Training Spec Quotas

```yaml
# In TrainingSpec
spec:
  quotas:
    # Request-level quotas (sidecar-enforceable)
    requests:
      maxRequestsPerHour: 1000
      maxRequestSizeBytes: 1048576  # 1MB
      maxConcurrentRequests: 10
    
    # Outbound call quotas (sidecar-enforceable)
    outbound:
      maxCallsPerMinute: 100
      maxCallSizeBytes: 524288  # 512KB
    
    # Compute quotas (Kubernetes-enforced)
    compute:
      cpu: "2"
      memory: "4Gi"
    
    # Token quotas (Model Gateway-enforced)
    tokens:
      maxTokensPerDay: 100000
      maxTokensPerRequest: 4096
    
    # Storage quotas (Memory Service-enforced)
    storage:
      maxSessionStorageBytes: 10485760  # 10MB
      maxPersistentStorageBytes: 104857600  # 100MB
```

### Employment Spec Quotas (Narrower Only)

```yaml
# In EmploymentSpec (stricter only)
spec:
  quotas:
    requests:
      maxRequestsPerHour: 500  # ✅ Narrower than 1000
    
    outbound:
      maxCallsPerMinute: 50  # ✅ Narrower than 100
```

---

## Quota Tracking Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    QUOTA TRACKING FLOW                                       │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                        SIDECAR                                      │  │
│   │                                                                      │  │
│   │   ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐    │  │
│   │   │ Inbound Tracker │  │ Outbound Tracker│  │ Rate Limiter    │    │  │
│   │   │ • Request count │  │ • Call count    │  │ • Per-endpoint  │    │  │
│   │   │ • Request size  │  │ • Call size     │  │ • Per-window    │    │  │
│   │   │ • Request rate  │  │ • Call rate     │  │                 │    │  │
│   │   └─────────────────┘  └─────────────────┘  └─────────────────┘    │  │
│   │                                                                      │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                   EXTERNAL SYSTEMS                                  │  │
│   │                                                                      │  │
│   │   ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐    │  │
│   │   │   Kubernetes    │  │  Model Gateway  │  │ Memory Service  │    │  │
│   │   │ • CPU/Memory    │  │ • Token usage   │  │ • Storage usage │    │  │
│   │   │ • Pod limits    │  │ • Token limits  │  │ • Storage limits│    │  │
│   │   └─────────────────┘  └─────────────────┘  └─────────────────┘    │  │
│   │                                                                      │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Quota Enforcement

### Early Enforcement

Sidecar provides early enforcement on outbound calls:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    QUOTA ENFORCEMENT                                         │
│                                                                              │
│   Agent API Call                                                            │
│       │                                                                     │
│       ▼                                                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │              1. SIDECAR QUOTA CHECK (Early)                         │  │
│   │              • Rate limit check                                     │  │
│   │              • Call count check                                     │  │
│   │              • Reject if quota exceeded                             │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│       │                                                                     │
│       ▼                                                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │         2. GATEWAY QUOTA CHECK (Authoritative)                      │  │
│   │         • Token limits (Model Gateway)                              │  │
│   │         • Tool limits (Tool Gateway)                                │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│       │                                                                     │
│       ▼                                                                     │
│   API Call Proceeds or Rejected                                             │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Quota Exhaustion Handling

| Behavior | Description |
|----------|-------------|
| **Reject** | Block operation when quota exceeded |
| **Escalate** | Notify supervisor, allow operation with alert |
| **Graceful Degradation** | Throttle rate, reduce capabilities |

```yaml
# Quota exhaustion policy
spec:
  quotas:
    exhaustionPolicy:
      requests:
        action: reject
        notification: true
      
      outbound:
        action: reject
        notification: true
      
      tokens:
        action: escalate
        notification: true
```

---

## Rate Limiting

### Sliding Window Rate Limiter

```yaml
# Rate limit configuration
spec:
  quotas:
    rateLimits:
      # Per-endpoint rate limits
      endpoints:
        - pattern: "/api/agent/v1/decisions"
          maxPerMinute: 20
        
        - pattern: "/api/agent/v1/requests/*/updates"
          maxPerMinute: 60
        
        - pattern: "*"
          maxPerMinute: 100  # Default for all endpoints
      
      # Sliding window configuration
      window:
        type: sliding
        duration: 60s
        buckets: 6  # 10-second buckets
```

---

## Integration Points

### Agent Lifecycle Manager
- Quota configuration from Employment Spec → Quota limits
- Quota changes trigger configuration reload

### Kubernetes
- CPU/memory quotas → Pod resource limits
- Sidecar cannot access, but correlates with request metrics

### Model Gateway
- Token consumption → Authoritative tracking
- Sidecar can see API calls but not token counts

### Tool Gateway
- Tool invocation quotas → Authoritative enforcement
- Sidecar provides early rate limiting

### Agent Health Monitor
- Quota exhaustion events → Health alerts
- Quota utilization → Health metrics

---

## Observability

### Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `seer_quota_utilization_ratio` | Current utilization (0-1) | `quota_type` |
| `seer_quota_exhaustion_total` | Exhaustion events | `quota_type` |
| `seer_quota_rejection_total` | Rejections due to quota | `quota_type` |
| `seer_rate_limit_remaining` | Remaining quota in window | `endpoint_pattern` |

### Quota Status

```json
{
  "agent_id": "fraud-analyst-001",
  "quotas": {
    "requests": {
      "limit": 1000,
      "used": 450,
      "remaining": 550,
      "window": "hour",
      "resets_at": "2026-01-12T15:00:00Z"
    },
    "outbound_calls": {
      "limit": 100,
      "used": 45,
      "remaining": 55,
      "window": "minute",
      "resets_at": "2026-01-12T14:31:00Z"
    }
  }
}
```

---

## Related Documentation

- [Fair Usage Budget Service](./fair-usage-budget-service.md) — User/customer usage tracking
- [Agent Lifecycle Manager](../agent-lifecycle-manager/README.md) — Quota configuration
- [Metrics Service](./metrics-service.md) — Metrics collection

---

*Resource Quota Service tracks and enforces resource consumption limits for agents, with early enforcement at the sidecar for request-level and API call quotas, and integration with external systems for compute and token quotas.*
