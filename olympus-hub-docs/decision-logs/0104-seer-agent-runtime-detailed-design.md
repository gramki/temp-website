# ADR-0104: Seer Agent Runtime Detailed Design

**Status**: Accepted  
**Date**: 2026-01-12  
**Category**: seer

---

## Context

The Agent Runtime subsystem had foundational design in `runtime-deployment.md` (ADR-0074), but lacked detailed design for:

1. IAM profile provisioning and lifecycle
2. Authority change detection and respawning
3. Signal Exchange integration architecture
4. Agent Ingress Gateway integration
5. Ingress path configuration

These gaps needed to be addressed to enable implementation.

---

## Decision

We completed the detailed design for Agent Runtime with the following architectural decisions:

### IAM Profile Provisioning

| Decision | Rationale |
|----------|-----------|
| **Profile created before pod deployment** | Ensures agent has valid identity before execution |
| **Roles/groups inheritance from delegator** | Supports wildcard (`*`) or CSV subset |
| **Bot mode for agents without delegator** | Base identity only, manager is accountable |
| **Kill switch includes IAM revocation** | Immediate authority termination |

### Authority Change Detection Architecture

| Component | Responsibility |
|-----------|----------------|
| **Seer Operator** | Only watches CRD changes (EmploymentSpec, TrainingSpec) |
| **IAM Observer Service** | Listens to Cipher IAM changes, updates CRDs |
| **Agent Ecosystem Integration Services** | Suite of services with tenant-admin authority |

**Flow**:
```
IAM Change → IAM Observer Service → CRD Update → Seer Operator → Respawn
```

### Signal Exchange Integration

| Decision | Rationale |
|----------|-----------|
| **sx-observer as workbench-level observer** | Signal Exchange doesn't support per-scenario subscriptions |
| **Signal Exchange unaware of Agent Ingress Gateway** | Clean separation of concerns |
| **All routing via Atropos** | Consistent messaging, durable delivery |
| **Store-and-forward in sx-observer** | Enables reliable delivery, scale-to-zero |
| **sx-observer triggers scale-up** | Agents can scale to zero when idle |

### Agent Response Handling

| Decision | Rationale |
|----------|-----------|
| **Agents update requests directly via Hub APIs** | Simplified response path; sx-observer does NOT forward responses |
| **Outbound Hub API calls pass through sidecar guardrails** | Enforcement on every Hub API call (request updates, decisions, etc.) |
| **External resources via Workbench Data Store** | URIs instead of inline content for large outputs |
| **DLQ in Atropos for failed dispatches** | Configurable retries, replay capability |

> **Note**: Agents handle responses directly through Hub APIs. The sx-observer only forwards inbound dispatch requests to agents — it does not forward agent responses back to Signal Exchange.

### Ingress Path Configuration

| Decision | Rationale |
|----------|-----------|
| **Cluster-ingress only (not public)** | Internal routing via sx-observer |
| **Per-agent ingress paths** | `/seer/subscription/{subscription_id}/data-plane/workbench/{workbench_id}/agents/{agent_id}/dispatch` |
| **zone-auth for sx-observer verification** | Secure internal communication |

---

## Consequences

### Positive

- **Clear separation of concerns** — Seer Operator only watches CRDs, IAM Observer handles IAM changes
- **Scale-to-zero capability** — sx-observer stores requests, triggers scale-up
- **Simplified response path** — Agents update directly, no reverse routing through sx-observer
- **Reliable message delivery** — Atropos provides durable pub-sub, DLQ for failures
- **Flexible authority model** — Supports user delegation, role delegation, and bot mode

### Negative

- **Additional service (sx-observer)** — One more component to operate
- **IAM Observer adds complexity** — Separate service to monitor IAM changes
- **Atropos dependency** — All message routing depends on Atropos availability

### Neutral

- **Implementation details deferred** — Specific thresholds, algorithms left to implementation
- **Hub API dependency for responses** — Agents must use Hub APIs for request updates

---

## Documents Created

| Document | Description |
|----------|-------------|
| `iam-provisioning.md` | IAM profile creation, lifecycle, inheritance, bot mode |
| `authority-change-respawning.md` | Detection architecture, triggers, respawning process |
| `signal-exchange-integration.md` | sx-observer, store-and-forward, scale-to-zero |
| `agent-ingress-gateway-integration.md` | Request routing, response handling, data store |

---

## Related

- [ADR-0074: Seer Runtime on Atlantis](./0074-seer-runtime-atlantis-based.md)
- [Agent Runtime Subsystem](../../olympus-seer-docs/seer-design/subsystems/agent-runtime/README.md)
- [Signal Exchange](../04-subsystems/signal-exchange/README.md)
- [Atropos Event Bus](../05-infrastructure/atropos.md)
