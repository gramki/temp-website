# Guardrail Hot-reload Service

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-12  
> **Design Level**: C2 (Container)

---

## Overview

The Guardrail Hot-reload Service enables updating sidecar configurations without restarting agent pods. It watches for configuration changes in Employment Spec and GuardrailProcessor CRDs, validates new configurations, and distributes updates to running sidecars.

**Key Principle**: Configuration changes should be immediate and seamless, without disrupting agent operations or losing in-flight requests.

---

## Configuration Change Detection

### Watched Resources

| Resource | Changes Detected |
|----------|------------------|
| **Employment Spec** | Guardrail configuration, policy changes, quota changes |
| **GuardrailProcessor CRD** | Processor image updates, configuration schema changes |
| **Training Spec** | Not watched (immutable once published) |

### Change Detection Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CONFIGURATION CHANGE FLOW                                 │
│                                                                              │
│   ┌─────────────────┐                                                       │
│   │ Kubernetes API  │                                                       │
│   │    (Watches)    │                                                       │
│   └────────┬────────┘                                                       │
│            │                                                                 │
│            ▼                                                                 │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                  HOT-RELOAD SERVICE                                 │  │
│   │                                                                      │  │
│   │   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                │  │
│   │   │   Detect    │  │  Validate   │  │ Distribute  │                │  │
│   │   │   Change    │──▶│   Config    │──▶│  to Pods    │                │  │
│   │   └─────────────┘  └─────────────┘  └─────────────┘                │  │
│   │                                                                      │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│            │                                                                 │
│            ▼                                                                 │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                  SIDECAR CONTAINERS                                 │  │
│   │                                                                      │  │
│   │   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                │  │
│   │   │   Pod 1     │  │   Pod 2     │  │   Pod 3     │                │  │
│   │   │  (Reload)   │  │  (Reload)   │  │  (Reload)   │                │  │
│   │   └─────────────┘  └─────────────┘  └─────────────┘                │  │
│   │                                                                      │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Hot-reload Mechanism

### Reload Process

1. **Change Detected** — Kubernetes watch event received
2. **Configuration Fetched** — New configuration retrieved
3. **Validation** — New configuration validated before applying
4. **Distribution** — Configuration pushed to all sidecar instances
5. **Reload** — Sidecars reload with new configuration
6. **Verification** — Health checks confirm successful reload

### Reload Without Restart

```yaml
# Sidecar reload mechanism
spec:
  hotReload:
    enabled: true
    
    # Reload strategy
    strategy: graceful  # graceful | immediate
    
    # Graceful reload settings
    graceful:
      drainTimeout: 30s   # Wait for in-flight requests
      rolloutDelay: 5s    # Delay between pod reloads
```

---

## Configuration Validation

### Pre-apply Validation

Before applying configuration changes, the service validates:

| Validation | Description |
|------------|-------------|
| **Schema Validation** | Configuration matches expected schema |
| **Guardrail References** | Referenced guardrail processors exist |
| **Policy Syntax** | OPA policies are syntactically valid |
| **Quota Consistency** | Employment quotas don't exceed Training maximums |
| **Immutability Rules** | Training constraints are not relaxed |

### Validation Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    VALIDATION FLOW                                           │
│                                                                              │
│   New Configuration                                                         │
│       │                                                                     │
│       ▼                                                                     │
│   ┌─────────────────┐                                                       │
│   │ Schema Check    │ ← JSON Schema validation                              │
│   └────────┬────────┘                                                       │
│            │                                                                 │
│            ▼                                                                 │
│   ┌─────────────────┐                                                       │
│   │ Reference Check │ ← Guardrail processors exist                          │
│   └────────┬────────┘                                                       │
│            │                                                                 │
│            ▼                                                                 │
│   ┌─────────────────┐                                                       │
│   │ Policy Syntax   │ ← OPA policy compilation                              │
│   └────────┬────────┘                                                       │
│            │                                                                 │
│            ▼                                                                 │
│   ┌─────────────────┐                                                       │
│   │ Immutability    │ ← Training constraints preserved                      │
│   └────────┬────────┘                                                       │
│            │                                                                 │
│            ▼                                                                 │
│   Valid Configuration → Apply                                               │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Rollback Capability

### Automatic Rollback

If configuration reload fails, the service automatically rolls back:

```yaml
# Rollback configuration
spec:
  hotReload:
    rollback:
      enabled: true
      retainVersions: 5  # Keep last 5 configurations
      
      # Rollback triggers
      triggers:
        - type: health_check_failure
          threshold: 3  # Consecutive failures
        - type: error_rate_spike
          threshold: 0.1  # 10% error rate increase
```

### Manual Rollback

```yaml
# Rollback to specific version
kubectl annotate employment fraud-analyst-emp-001 \
  seer.olympus.io/config-rollback-to=v3
```

---

## Configuration Versioning

### Version Tracking

```yaml
# Configuration version metadata
status:
  configVersion: v5
  previousVersion: v4
  lastUpdated: "2026-01-12T14:30:00Z"
  history:
    - version: v5
      timestamp: "2026-01-12T14:30:00Z"
      changedBy: admin@tenant.com
      changes: ["guardrail.pii-detector.config.sensitivity"]
    - version: v4
      timestamp: "2026-01-11T10:00:00Z"
      changedBy: admin@tenant.com
      changes: ["guardrail.decision-validator added"]
```

---

## Configuration Distribution

### Distribution Strategy

| Strategy | Description |
|----------|-------------|
| **Immediate** | All pods reload simultaneously |
| **Rolling** | Pods reload one at a time |
| **Canary** | One pod reloads first, others follow if healthy |

```yaml
# Distribution configuration
spec:
  hotReload:
    distribution:
      strategy: rolling
      
      rolling:
        maxUnavailable: 1
        maxSurge: 0
        delayBetweenPods: 5s
      
      canary:
        initialPods: 1
        evaluationPeriod: 60s
        successThreshold: 0.95  # 95% success rate to proceed
```

---

## Configuration Consistency

### Consistency Guarantees

| Guarantee | Description |
|-----------|-------------|
| **Eventual Consistency** | All sidecars eventually have same configuration |
| **Version Ordering** | Newer versions always supersede older |
| **Atomic Reload** | Configuration applied atomically per pod |

### Consistency Verification

```yaml
# Consistency check
status:
  consistency:
    expected: 5  # Total pods
    synchronized: 5  # Pods with current config
    version: v5
    lastSync: "2026-01-12T14:31:00Z"
```

---

## Integration Points

### Agent Lifecycle Manager
- Employment Spec changes → Configuration update triggers
- Configuration validation → Pre-apply checks

### Guardrail Service
- Configuration updates → Guardrail processor reload
- New guardrail patterns → Pattern registry update

### Agent Runtime
- Configuration updates → Sidecar configuration sync
- Pod discovery → Distribution targets

### Kubernetes API
- CRD watches → Change detection
- ConfigMap updates → Configuration distribution

---

## Observability

### Metrics

| Metric | Description |
|--------|-------------|
| `seer_config_reload_total` | Total configuration reloads |
| `seer_config_reload_duration_seconds` | Reload duration |
| `seer_config_validation_failures_total` | Validation failures |
| `seer_config_rollback_total` | Rollback events |
| `seer_config_version` | Current configuration version (gauge) |

### Events

```json
{
  "event_type": "config_reload",
  "agent_id": "fraud-analyst-001",
  "config_version": "v5",
  "previous_version": "v4",
  "status": "success",
  "duration_ms": 250,
  "pods_updated": 3,
  "timestamp": "2026-01-12T14:30:00Z"
}
```

---

## Related Documentation

- [Guardrail Service](./guardrail-service.md) — Guardrail configuration
- [Agent Lifecycle Manager](../agent-lifecycle-manager/README.md) — Employment Spec management
- [Agent Runtime](../agent-runtime/README.md) — Pod deployment

---

*Guardrail Hot-reload Service enables seamless configuration updates without pod restarts, with validation, rollback capability, and consistent distribution to all sidecar instances.*
