# DevOps Workbench Reference

> **Status:** 🟡 Draft
> **Category:** Implementation Concepts / DevOps and Lifecycle

---

## Definition

A **DevOps Workbench Reference** (`devops_ref`) is an optional configuration on a Business Workbench that associates it with a DevOps Workbench for automated development operations. The reference enables routing of development lifecycle signals (ideation, CI/CD, feedback) from the business workbench to the DevOps workbench via Atropos.

---

## Purpose

| Purpose | Description |
|---------|-------------|
| **Cross-Workbench Association** | Link business workbench to DevOps workbench |
| **Signal Routing** | Route development events to DevOps for automation |
| **Cross-Subscription Support** | Enable DevOps workbench in different subscription |
| **Credential Management** | Secure cross-workbench communication |

---

## Configuration Schema

### In Business Workbench Specification

```yaml
apiVersion: hub.olympus.io/v1
kind: Workbench
metadata:
  name: dispute-ops-dev
  namespace: acme-bank
spec:
  # ... standard workbench config ...
  
  # DevOps Workbench Association (optional)
  devops:
    # Reference to target DevOps Workbench
    reference:
      workbench_id: string           # Required: Target workbench ID
      namespace: string              # Required: Target namespace
      subscription_id: string        # Optional: If cross-subscription
      tenant_id: string              # Optional: If cross-tenant
    
    # Signal routing configuration
    signal_routing:
      enabled: boolean               # Default: true
      sources:                       # List of subsystem event sources
        - subsystem: string          # e.g., "automation-ideation"
          events: [string]           # e.g., ["idea.submitted", "idea.promoted"]
      filters:                       # Optional event filters
        - source: string
          condition: string          # CEL expression
      rate_limit:                    # Optional rate limiting
        max_signals_per_minute: integer
        burst: integer
      batching:                      # Optional signal batching
        enabled: boolean
        max_batch_size: integer
        max_delay: duration
    
    # Cross-subscription credentials (required if different subscription)
    credentials:
      secret_ref:
        name: string                 # Secret name
        namespace: string            # Secret namespace
      auth_type: string              # "bot_token" | "service_account" | "mtls"
```

### DevOps Workbench Type

```yaml
apiVersion: hub.olympus.io/v1
kind: Workbench
metadata:
  name: dispute-devops
  namespace: acme-devops
spec:
  # Explicit workbench type marker
  workbench_type: devops    # "business" (default) | "devops"
  
  # Accept signals from authorized workbenches
  signals:
    inbound:
      - type: devops_event
        source_filter:
          authorized_workbenches:
            - workbench_id: string
              subscription_id: string
```

---

## Signal Routing

### Event Sources

| Subsystem | Events | Description |
|-----------|--------|-------------|
| `automation-ideation` | `idea.submitted`, `idea.promoted`, `intent.completed`, `charter.created` | Ideation lifecycle events |
| `ci-subsystem` | `test.passed`, `test.failed`, `build.passed`, `build.failed` | CI/CD events |
| `artifact-registry` | `artifact.published`, `promotion.requested`, `promotion.completed` | Artifact lifecycle events |
| `feedback-services` | `feedback.promoted`, `problem.promoted`, `feedback.resolved` | Production feedback events |

### Routing via Atropos

Signals are routed through **Atropos** (outbound signal gateway):

```
Business Workbench (A)          Atropos          DevOps Workbench (D)
        │                          │                       │
        │  1. Event emitted        │                       │
        ├─────────────────────────▶│                       │
        │                          │  2. Authenticate     │
        │                          │  3. Transform        │
        │                          │  4. Deliver          │
        │                          ├──────────────────────▶│
        │                          │                       │  5. Route to SX
        │                          │                       │  6. Trigger Scenario
```

### Signal Envelope

Routed signals include source context:

```json
{
  "signal_type": "devops_event",
  "event": {
    "type": "idea.submitted",
    "timestamp": "2026-01-09T15:30:00Z",
    "payload": { ... }
  },
  "source": {
    "workbench_id": "dispute-ops-dev",
    "subscription_id": "acme-bank",
    "tenant_id": "acme-corp",
    "subsystem": "automation-ideation"
  },
  "routing": {
    "via": "atropos",
    "correlation_id": "uuid",
    "routed_at": "timestamp"
  }
}
```

---

## Topology Models

### Default DevOps Workbench

Every subscription has a platform-provided default DevOps workbench:

```
Subscription: acme-bank
├── default-devops (D)        ← Platform-provided
├── dispute-ops-dev (A)       ← No devops config → uses default
├── payments-ops-dev (A)      ← No devops config → uses default
└── onboard-ops-dev (A)       ← No devops config → uses default
```

### Explicit Reference (Same Subscription)

```yaml
# Business workbench
devops:
  reference:
    workbench_id: dispute-devops
    namespace: acme-bank
```

### Cross-Subscription Reference

```yaml
# Business workbench in acme-bank subscription
devops:
  reference:
    workbench_id: central-devops
    namespace: devops-platform
    subscription_id: acme-devops-central    # Different subscription
  credentials:
    secret_ref:
      name: central-devops-creds
      namespace: acme-bank
    auth_type: bot_token
```

---

## Credential Types

| Type | Use Case | Secret Contents |
|------|----------|-----------------|
| `bot_token` | Same-tenant, cross-subscription | `bot_token`, `atropos_endpoint` |
| `service_account` | Platform-managed accounts | `service_account_token`, `atropos_endpoint` |
| `mtls` | Cross-tenant, high-security | `client_cert`, `client_key`, `ca_cert`, `atropos_endpoint` |

---

## Platform Provision

Hub Platform provides:

| Asset | Description |
|-------|-------------|
| **Default DevOps Workbench** | One per subscription, auto-provisioned |
| **DevOps Blueprint** | Template for custom DevOps workbenches |
| **Standard Scenarios** | Platform-provided DevOps scenarios |
| **AI Agent Templates** | Pre-configured assistant agents |

---

## Validation Rules

| Rule | Error |
|------|-------|
| `reference.workbench_id` must exist | "DevOps workbench not found" |
| Target must have `workbench_type: devops` | "Target is not a DevOps workbench" |
| Cross-subscription requires `credentials` | "Credentials required for cross-subscription reference" |
| Secret must exist and contain required fields | "Invalid credentials secret" |
| Business WB must be authorized in DevOps WB | "Workbench not authorized to send signals" |

---

## Related Documentation

- [DevOps Workbench Pattern](../../09-composite-systems-and-patterns/devops-workbench/README.md)
- [DevOps Workbench Reference (Detailed)](../../09-composite-systems-and-patterns/devops-workbench/devops-workbench-reference.md)
- [Atropos (Outbound Gateway)](../../04-subsystems/io-gateways/atropos.md)
- [Signal Exchange](../../04-subsystems/signal-exchange/README.md)
- [Workbench Management](../../04-subsystems/workbench-management/README.md)

