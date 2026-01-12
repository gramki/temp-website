# ADR-0107: Model Gateway Two-Level Budget Enforcement

**Status**: Accepted  
**Date**: 2026-01-12  
**Authors**: Architecture Team

---

## Context

Model Gateway needs to enforce budget limits on LLM usage to control costs. Key requirements:

1. Aggregate cost control at workbench level
2. Individual accountability at agent level
3. Budget tracking with accurate cost attribution
4. Configurable actions when limits are reached

Two approaches were considered:

1. **Single-Level Budget**: Only workbench-level limits
2. **Two-Level Budget**: Both workbench and per-agent limits

---

## Decision

**Model Gateway implements two-level budget enforcement with virtual keys for per-agent tracking.**

### Key Design Elements

1. **Workbench-Level Budget**: Aggregate limit for all agents in workbench
2. **Agent-Level Budget**: Per-Employed Agent limit via virtual key
3. **Pre-Request Check**: Budget verified before sending to provider
4. **Virtual Key Attribution**: All usage attributed via unique virtual key

---

## Rationale

### Why Two-Level Budget

| Level | Purpose |
|-------|---------|
| **Workbench** | Financial control, aggregate cost cap |
| **Agent** | Individual accountability, prevent runaway agents |

### Virtual Key Benefits

| Benefit | Description |
|---------|-------------|
| **Attribution** | Every request attributed to specific agent |
| **Isolation** | Agents cannot impact each other's budgets |
| **Audit** | Complete cost trail per agent |
| **Revocation** | Individual agent can be cut off |

### Budget Actions

| Action | Behavior |
|--------|----------|
| `alert` | Log warning, send notification, continue |
| `throttle` | Reduce request rate, queue excess |
| `block` | Reject requests with 429 status |

---

## Consequences

### Positive

- Granular cost control
- Individual accountability
- Complete audit trail
- Flexible enforcement actions

### Negative

- Additional complexity in budget tracking
- Token estimation required for pre-check
- State management for budget counters

### Neutral

- Redis used for fast budget state
- Monthly reset cycle (configurable)

---

## Implementation Details

### Budget Check Algorithm

```
Request arrives
    │
    ▼
Estimate token cost
    │
    ▼
Check agent budget ──→ Exceeded? ──→ Apply agent action
    │                                    │
    │ OK                                 ▼
    ▼                             (throttle/block/alert)
Check workbench budget ──→ Exceeded? ──→ Apply workbench action
    │
    │ OK
    ▼
Forward to provider
    │
    ▼
Record actual usage
    │
    ▼
Reconcile estimate vs actual
```

### Virtual Key Format

```
vk_{subscription}_{agent_id}_{sequence}
```

### Budget Configuration

```yaml
budgets:
  workbench:
    monthlyLimit: 10000  # USD
    alertThresholds: [50, 75, 90]
    action: alert
  
  perAgent:
    default:
      monthlyLimit: 500
      action: throttle
    
    overrides:
      - agent: fraud-analyst-senior
        monthlyLimit: 2000
```

---

## Relationship to ADR-0075

This ADR extends **ADR-0075: Model Gateway (Bifrost)** with detailed budget enforcement design:

- ADR-0075 established Bifrost as the foundation
- This ADR details the two-level budget model
- Virtual key management is a Hub-specific extension

---

## Related Documentation

- [Model Gateway Governance](../../olympus-seer-docs/seer-design/subsystems/model-gateway/governance.md)
- [ADR-0075: Model Gateway (Bifrost)](./0075-seer-model-gateway-bifrost.md)
- [Cipher IAM Extensions](../../olympus-seer-docs/seer-design/subsystems/cipher-iam-extensions/README.md)
