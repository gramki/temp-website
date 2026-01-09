# DevOps Workbench Reference

> **Status:** 🟡 Draft
> **Category:** Composite Patterns / DevOps Workbench

---

## Overview

This document specifies how a **Business Workbench (A)** references a **DevOps Workbench (D)** for automated development operations. The reference includes cross-workbench signal routing configuration, cross-subscription credentials, and Atropos-based transport.

---

## DevOps Workbench Reference Model

### Reference Configuration

A business workbench can optionally include a `devops` block that references a DevOps workbench:

```yaml
apiVersion: hub.olympus.io/v1
kind: Workbench
metadata:
  name: dispute-ops-dev
  namespace: acme-bank
spec:
  domain: dispute-resolution
  description: "Dispute Operations - Development"
  
  dev_lifecycle_stage: DEV
  development_workbench_ref: null    # This IS the dev workbench
  
  # DevOps Workbench Association (optional)
  devops:
    # Reference to DevOps Workbench
    reference:
      # Target DevOps workbench identification
      workbench_id: dispute-devops
      
      # If in same subscription, namespace is sufficient
      namespace: acme-bank
      
      # If in different subscription, full coordinates required
      subscription_id: acme-bank-devops-sub    # Optional: if cross-subscription
      tenant_id: acme-corp                     # Optional: if cross-tenant
      
    # Signal routing configuration
    signal_routing:
      enabled: true
      
      # Which subsystems' events to route
      sources:
        - subsystem: automation-ideation
          events: [idea.submitted, idea.promoted, intent.completed, charter.created]
        
        - subsystem: ci-subsystem
          events: [test.passed, test.failed, build.passed, build.failed]
        
        - subsystem: artifact-registry
          events: [artifact.published, promotion.requested, promotion.completed]
        
        - subsystem: feedback-services
          events: [feedback.promoted, problem.promoted, feedback.resolved]
      
      # Optional: Event filters
      filters:
        - source: ci-subsystem
          condition: "event.type in ['test.failed', 'build.failed']"  # Only failures
    
    # Cross-subscription credentials (required if different subscription)
    credentials:
      # Reference to a Secret containing Atropos channel credentials
      secret_ref:
        name: devops-workbench-credentials
        namespace: acme-bank
      
      # The credential type
      auth_type: bot_token    # bot_token | service_account | mtls
```

### Cross-Subscription Reference

When the DevOps Workbench is in a different subscription:

```yaml
devops:
  reference:
    workbench_id: central-devops
    namespace: devops-platform
    subscription_id: acme-devops-central      # Different subscription
    tenant_id: acme-corp                       # Same or different tenant
  
  credentials:
    secret_ref:
      name: central-devops-credentials
      namespace: acme-bank
    auth_type: bot_token
```

The referenced Secret must contain:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: central-devops-credentials
  namespace: acme-bank
type: hub.olympus.io/atropos-credential
data:
  # Bot token for authenticating with target DevOps Workbench
  bot_token: <base64-encoded-token>
  
  # Atropos endpoint for target subscription
  atropos_endpoint: <base64-encoded-url>
  
  # Optional: mTLS certificate if using certificate auth
  client_cert: <base64-encoded-cert>
  client_key: <base64-encoded-key>
```

---

## Signal Routing via Atropos

### Architecture

Signals from business workbench subsystems are routed to the DevOps workbench via **Atropos** (outbound signal gateway):

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SIGNAL ROUTING VIA ATROPOS                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  BUSINESS WORKBENCH (A)                    DEVOPS WORKBENCH (D)             │
│  Subscription: acme-bank                   Subscription: acme-devops        │
│                                                                              │
│  ┌─────────────────────────────┐                                            │
│  │ Subsystems                  │                                            │
│  │                             │                                            │
│  │ automation-ideation ───────────┐                                         │
│  │ ci-subsystem ──────────────────┤                                         │
│  │ artifact-registry ─────────────┼──▶ DevOps Signal Aggregator            │
│  │ feedback-services ─────────────┤                                         │
│  └─────────────────────────────┘  │                                         │
│                                   │                                         │
│                                   ▼                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    DEVOPS SIGNAL AGGREGATOR                          │   │
│  │                                                                      │   │
│  │  1. Subscribe to configured subsystem events                        │   │
│  │  2. Apply filters (if any)                                          │   │
│  │  3. Enrich with source workbench context                            │   │
│  │  4. Route to Atropos                                                │   │
│  └──────────────────────────┬───────────────────────────────────────────┘   │
│                             │                                               │
│                             ▼                                               │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    ATROPOS (Outbound Gateway)                        │   │
│  │                                                                      │   │
│  │  • Authenticate with target subscription (using credentials)        │   │
│  │  • Transform to normalized signal format                            │   │
│  │  • Deliver to target Heracles endpoint                              │   │
│  └──────────────────────────┬───────────────────────────────────────────┘   │
│                             │                                               │
│                             │ HTTPS / mTLS                                  │
│                             ▼                                               │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    HERACLES (Inbound Gateway) — D                    │   │
│  │                                                                      │   │
│  │  • Validate credentials                                             │   │
│  │  • Route to D's Signal Exchange                                     │   │
│  └──────────────────────────┬───────────────────────────────────────────┘   │
│                             │                                               │
│                             ▼                                               │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    SIGNAL EXCHANGE (D)                               │   │
│  │                                                                      │   │
│  │  • Match event to Trigger                                           │   │
│  │  • Instantiate DevOps Scenario                                      │   │
│  │  • Create Request with source context                               │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Signal Enrichment

Signals routed to DevOps workbench include source context:

```json
{
  "signal_type": "devops_event",
  "event": {
    "type": "idea.submitted",
    "timestamp": "2026-01-09T15:30:00Z",
    "payload": {
      "idea_id": "idea-12345",
      "title": "Automate refund eligibility check",
      "submitter": "agent-001"
    }
  },
  "source": {
    "workbench_id": "dispute-ops-dev",
    "workbench_name": "Dispute Operations - Development",
    "subscription_id": "acme-bank",
    "tenant_id": "acme-corp",
    "subsystem": "automation-ideation"
  },
  "routing": {
    "via": "atropos",
    "correlation_id": "corr-98765",
    "routed_at": "2026-01-09T15:30:01Z"
  }
}
```

---

## DevOps Workbench Specification

### Workbench Type

DevOps workbenches are explicitly marked with `workbench_type: devops`:

```yaml
apiVersion: hub.olympus.io/v1
kind: Workbench
metadata:
  name: dispute-devops
  namespace: acme-devops
spec:
  domain: devops
  description: "DevOps Workbench for Dispute Domain"
  
  # Explicit workbench type
  workbench_type: devops    # "business" (default) | "devops"
  
  # This workbench is in DEV stage (it develops itself traditionally)
  dev_lifecycle_stage: DEV
  
  # DevOps workbenches don't require their own DevOps workbench (no chicken-egg)
  devops: null
  
  # Signal registration for receiving routed events
  signals:
    inbound:
      # Accept DevOps events from linked workbenches
      - type: devops_event
        source_filter:
          # Only accept from authorized workbenches
          authorized_workbenches:
            - workbench_id: dispute-ops-dev
              subscription_id: acme-bank
            - workbench_id: payments-ops-dev
              subscription_id: acme-bank
  
  # DevOps Scenarios
  scenarios:
    # APO Scenarios
    - name: idea-triage
      trigger:
        event_type: devops_event
        filter: "event.type == 'idea.submitted'"
      application:
        type: cognitive
        runtime: seer
        config_ref: idea-triage-app
    
    - name: intent-drafting
      trigger:
        event_type: devops_event
        filter: "event.type == 'idea.promoted'"
      application:
        type: cognitive
        runtime: seer
        config_ref: intent-drafting-app
    
    # PA Scenarios
    - name: intent-review
      trigger:
        event_type: devops_event
        filter: "event.type == 'intent.completed'"
      application:
        type: cognitive
        runtime: seer
        config_ref: intent-review-app
    
    - name: scenario-drafting
      trigger:
        event_type: devops_event
        filter: "event.type == 'charter.created'"
      application:
        type: cognitive
        runtime: seer
        config_ref: scenario-drafting-app
    
    # Developer Scenarios
    - name: test-diagnosis
      trigger:
        event_type: devops_event
        filter: "event.type == 'test.failed'"
      application:
        type: cognitive
        runtime: seer
        config_ref: test-diagnosis-app
    
    - name: build-resolution
      trigger:
        event_type: devops_event
        filter: "event.type == 'build.failed'"
      application:
        type: cognitive
        runtime: seer
        config_ref: build-resolution-app
  
  # Task Queues with AI Agents
  task_queues:
    - name: apo-queue
      description: "APO tasks (AI-assisted)"
      enrolled_agents:
        - type: human
          role: automation_product_owner
        - type: ai
          agent_id: apo-assistant
          autonomy_level: medium
      escalation:
        ai_to_human:
          enabled: true
          timeout: 30m
          conditions:
            - "task.confidence < 0.7"
            - "task.requires_approval == true"
    
    - name: pa-queue
      description: "Process Architect tasks (AI-assisted)"
      enrolled_agents:
        - type: human
          role: process_architect
        - type: ai
          agent_id: pa-assistant
          autonomy_level: medium
      escalation:
        ai_to_human:
          enabled: true
          timeout: 1h
    
    - name: dev-queue
      description: "Developer tasks (AI-assisted)"
      enrolled_agents:
        - type: human
          role: developer
        - type: ai
          agent_id: dev-assistant
          autonomy_level: high    # Developers trust more automation
      escalation:
        ai_to_human:
          enabled: true
          timeout: 2h
```

---

## Workbench Relationship Model

### Topology Options

| Topology | Description | Use Case |
|----------|-------------|----------|
| **N:1** | Multiple business WBs → One DevOps WB | Shared DevOps for domain |
| **1:1** | Each business WB → Own DevOps WB | Isolated DevOps per domain |
| **Default** | WBs without `devops_ref` → Subscription default | Simple tenant setup |

### N:1 Example

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    N:1 TOPOLOGY (Shared DevOps)                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  SUBSCRIPTION: acme-bank                                                    │
│                                                                              │
│  ┌─────────────────┐                                                        │
│  │ Dispute-Dev (A) │────────┐                                               │
│  └─────────────────┘        │                                               │
│                             │                                               │
│  ┌─────────────────┐        │     ┌────────────────────────────────────┐   │
│  │ Payments-Dev(A) │────────┼────▶│ Finance-DevOps (D)                 │   │
│  └─────────────────┘        │     │                                    │   │
│                             │     │ Shared scenarios for all finance   │   │
│  ┌─────────────────┐        │     │ workbenches                        │   │
│  │ Onboard-Dev (A) │────────┘     │                                    │   │
│  └─────────────────┘              └────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Cross-Subscription Example

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CROSS-SUBSCRIPTION TOPOLOGY                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  SUBSCRIPTION: acme-bank            SUBSCRIPTION: acme-devops-central       │
│                                                                              │
│  ┌─────────────────┐                ┌────────────────────────────────────┐ │
│  │ Dispute-Dev     │───────────────▶│ Central-DevOps                     │ │
│  └─────────────────┘    Atropos     │                                    │ │
│                         + creds     │ Enterprise DevOps for all          │ │
│  ┌─────────────────┐                │ business subscriptions             │ │
│  │ Payments-Dev    │───────────────▶│                                    │ │
│  └─────────────────┘                │ Centralized AI agents, shared      │ │
│                                      │ learnings across domains          │ │
│  SUBSCRIPTION: acme-insurance       │                                    │ │
│                                      │                                    │ │
│  ┌─────────────────┐                │                                    │ │
│  │ Claims-Dev      │───────────────▶│                                    │ │
│  └─────────────────┘                └────────────────────────────────────┘ │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Default DevOps Workbench

### Platform Provision

Hub Platform automatically provisions a **Default DevOps Workbench** for each subscription:

```yaml
apiVersion: hub.olympus.io/v1
kind: Workbench
metadata:
  name: default-devops
  namespace: ${subscription_namespace}
  labels:
    hub.olympus.io/platform-managed: "true"
    hub.olympus.io/workbench-type: devops
    hub.olympus.io/default-devops: "true"
spec:
  domain: devops
  description: "Platform-provided Default DevOps Workbench"
  workbench_type: devops
  
  # Uses platform-provided standard scenarios
  scenarios:
    - $ref: platform://devops-scenarios/idea-triage
    - $ref: platform://devops-scenarios/intent-drafting
    - $ref: platform://devops-scenarios/test-diagnosis
    # ... other standard scenarios
  
  # Uses platform-provided AI agent templates
  task_queues:
    - name: apo-queue
      enrolled_agents:
        - $ref: platform://devops-agents/apo-assistant
    - name: pa-queue
      enrolled_agents:
        - $ref: platform://devops-agents/pa-assistant
    - name: dev-queue
      enrolled_agents:
        - $ref: platform://devops-agents/dev-assistant
```

### Fallback Behavior

Business workbenches without explicit `devops` configuration use the subscription's default:

```yaml
# Business workbench without devops config
apiVersion: hub.olympus.io/v1
kind: Workbench
metadata:
  name: dispute-ops-dev
  namespace: acme-bank
spec:
  domain: dispute-resolution
  dev_lifecycle_stage: DEV
  
  # No devops block → Uses default-devops workbench
```

---

## Credential Management

### Bot Token Authentication

For same-tenant, cross-subscription references:

```yaml
# 1. Create service account in DevOps Workbench
apiVersion: hub.olympus.io/v1
kind: ServiceAccount
metadata:
  name: business-wb-signal-sender
  namespace: acme-devops
spec:
  description: "Service account for receiving signals from business workbenches"
  permissions:
    - resource: signal-exchange
      actions: [create]
    - resource: devops-events
      actions: [emit]

# 2. Generate bot token
apiVersion: hub.olympus.io/v1
kind: BotToken
metadata:
  name: signal-sender-token
  namespace: acme-devops
spec:
  service_account_ref:
    name: business-wb-signal-sender
  expires_at: "2027-01-09T00:00:00Z"
  
# 3. Reference token in business workbench
# (Token value stored in Secret referenced by credentials.secret_ref)
```

### mTLS Authentication

For cross-tenant or high-security references:

```yaml
credentials:
  secret_ref:
    name: devops-mtls-credentials
    namespace: acme-bank
  auth_type: mtls

# Secret contains:
# - client_cert: Certificate issued by DevOps workbench's CA
# - client_key: Private key for the certificate
# - ca_cert: DevOps workbench's CA certificate (for verification)
```

---

## Implementation Considerations

### Bootstrap (Chicken-Egg Resolution)

DevOps Workbenches are optional:

| Scenario | Behavior |
|----------|----------|
| **No DevOps WB configured** | Business workbench works normally; no automated DevOps |
| **Default DevOps WB** | Automatic routing to subscription's default |
| **Custom DevOps WB** | Explicit `devops_ref` routing |
| **DevOps WB without DevOps** | DevOps workbenches don't need their own DevOps WB |

### Signal Volume Considerations

For high-volume business workbenches:

```yaml
devops:
  signal_routing:
    # Rate limiting
    rate_limit:
      max_signals_per_minute: 100
      burst: 20
    
    # Batching
    batching:
      enabled: true
      max_batch_size: 50
      max_delay: 5s
    
    # Filtering to reduce noise
    filters:
      - source: ci-subsystem
        condition: "event.type == 'test.failed'"  # Only failures
```

---

## Related Documentation

- [DevOps Workbench Overview](./README.md)
- [Signal Routing via Atropos](./signal-routing-via-atropos.md)
- [Implementation Concept: DevOps Workbench Reference](../../02-system-design/implementation-concepts/devops-workbench-reference.md)
- [Atropos (Outbound Gateway)](../../04-subsystems/io-gateways/atropos.md)
- [Workbench Management](../../04-subsystems/workbench-management/README.md)

