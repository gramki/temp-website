# Signal Routing via Atropos

> **Status:** 🟡 Draft
> **Category:** Composite Patterns / DevOps Workbench

---

## Overview

This document specifies how development lifecycle signals are routed from a Business Workbench (A) to a DevOps Workbench (D) using **Atropos** (outbound signal gateway). This is the A → D direction of the [DevOps Workbench Binding](./devops-workbench-binding.md).

---

## Signal Flow Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SIGNAL ROUTING: A → D VIA ATROPOS                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  BUSINESS WORKBENCH (A)                                                     │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                         SUBSYSTEMS                                   │   │
│  │                                                                      │   │
│  │  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐            │   │
│  │  │ automation-   │  │ ci-subsystem  │  │ artifact-     │            │   │
│  │  │ ideation      │  │               │  │ registry      │            │   │
│  │  │               │  │ • test.passed │  │               │            │   │
│  │  │ • idea.       │  │ • test.failed │  │ • artifact.   │            │   │
│  │  │   submitted   │  │ • build.      │  │   published   │            │   │
│  │  │ • idea.       │  │   passed      │  │ • promotion.  │            │   │
│  │  │   promoted    │  │ • build.      │  │   requested   │            │   │
│  │  │ • intent.     │  │   failed      │  │ • promotion.  │            │   │
│  │  │   completed   │  │               │  │   completed   │            │   │
│  │  │ • charter.    │  │               │  │               │            │   │
│  │  │   created     │  │               │  │               │            │   │
│  │  └───────┬───────┘  └───────┬───────┘  └───────┬───────┘            │   │
│  │          │                  │                  │                     │   │
│  │  ┌───────────────┐          │                  │                     │   │
│  │  │ feedback-     │          │                  │                     │   │
│  │  │ services      │          │                  │                     │   │
│  │  │               │          │                  │                     │   │
│  │  │ • feedback.   │          │                  │                     │   │
│  │  │   promoted    │          │                  │                     │   │
│  │  │ • problem.    │          │                  │                     │   │
│  │  │   promoted    │          │                  │                     │   │
│  │  │ • feedback.   │          │                  │                     │   │
│  │  │   resolved    │          │                  │                     │   │
│  │  └───────┬───────┘          │                  │                     │   │
│  │          │                  │                  │                     │   │
│  └──────────┼──────────────────┼──────────────────┼─────────────────────┘   │
│             │                  │                  │                         │
│             ▼                  ▼                  ▼                         │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    DEVOPS SIGNAL AGGREGATOR                          │   │
│  │                                                                      │   │
│  │  1. Subscribe to configured subsystem event streams                 │   │
│  │  2. Apply filter conditions (if configured)                         │   │
│  │  3. Enrich with source workbench context                            │   │
│  │  4. Normalize to DevOps Event format                                │   │
│  │  5. Route to Atropos                                                │   │
│  └──────────────────────────────┬───────────────────────────────────────┘   │
│                                 │                                            │
│                                 ▼                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    ATROPOS (Outbound Gateway)                        │   │
│  │                                                                      │   │
│  │  1. Load credentials from DevOpsWorkbenchBinding                    │   │
│  │  2. Authenticate with target subscription                           │   │
│  │  3. Transform to normalized signal format                           │   │
│  │  4. Deliver to target Heracles endpoint                             │   │
│  │  5. Handle retries and dead-letter queue                            │   │
│  └──────────────────────────────┬───────────────────────────────────────┘   │
│                                 │                                            │
│                                 │ HTTPS / mTLS                               │
│                                 │                                            │
└─────────────────────────────────┼────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  DEVOPS WORKBENCH (D)                                                       │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    HERACLES (Inbound Gateway)                        │   │
│  │                                                                      │   │
│  │  1. Validate credentials (bot token / mTLS)                         │   │
│  │  2. Verify source workbench is authorized                           │   │
│  │  3. Parse DevOps Event format                                       │   │
│  │  4. Route to Signal Exchange                                        │   │
│  └──────────────────────────────┬───────────────────────────────────────┘   │
│                                 │                                            │
│                                 ▼                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    SIGNAL EXCHANGE (D)                               │   │
│  │                                                                      │   │
│  │  1. Match event type to Trigger definition                          │   │
│  │  2. Transform signal to Request                                     │   │
│  │  3. Instantiate DevOps Scenario                                     │   │
│  │  4. Create tasks in appropriate queue                               │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Signal Catalog

### Automation Ideation Signals

| Event | Description | Payload |
|-------|-------------|---------|
| `idea.submitted` | New idea submitted | `idea_id`, `title`, `description`, `submitter`, `category` |
| `idea.promoted` | Idea promoted to intent | `idea_id`, `intent_id`, `promoted_by` |
| `idea.parked` | Idea moved to parking lot | `idea_id`, `reason`, `parked_by` |
| `idea.rejected` | Idea rejected | `idea_id`, `reason`, `rejected_by` |
| `intent.created` | Intent created from idea | `intent_id`, `idea_id`, `apo_id` |
| `intent.completed` | Intent fully specified | `intent_id`, `business_case`, `success_criteria` |
| `intent.accepted` | Intent accepted by PA (becomes Charter) | `intent_id`, `charter_id`, `pa_id` |
| `charter.created` | Charter created | `charter_id`, `intent_id`, `scope`, `pa_id` |
| `charter.updated` | Charter modified | `charter_id`, `changes`, `updated_by` |

### CI Subsystem Signals

| Event | Description | Payload |
|-------|-------------|---------|
| `build.started` | Build started | `build_id`, `artifact_id`, `trigger` |
| `build.passed` | Build succeeded | `build_id`, `artifact_id`, `duration`, `outputs` |
| `build.failed` | Build failed | `build_id`, `artifact_id`, `error`, `logs_ref` |
| `test.started` | Test run started | `test_run_id`, `artifact_id`, `test_suite` |
| `test.passed` | All tests passed | `test_run_id`, `artifact_id`, `results_summary` |
| `test.failed` | Tests failed | `test_run_id`, `artifact_id`, `failures`, `logs_ref` |
| `lint.passed` | Lint checks passed | `lint_run_id`, `artifact_id` |
| `lint.failed` | Lint checks failed | `lint_run_id`, `artifact_id`, `issues` |

### Artifact Registry Signals

| Event | Description | Payload |
|-------|-------------|---------|
| `artifact.created` | New artifact registered | `artifact_id`, `type`, `version`, `created_by` |
| `artifact.published` | Artifact marked ready | `artifact_id`, `version`, `published_by` |
| `promotion.requested` | Promotion to next stage requested | `promotion_id`, `artifact_id`, `from_stage`, `to_stage` |
| `promotion.approved` | Promotion approved | `promotion_id`, `approved_by` |
| `promotion.rejected` | Promotion rejected | `promotion_id`, `reason`, `rejected_by` |
| `promotion.completed` | Promotion finished | `promotion_id`, `artifact_id`, `target_workbench` |

### Feedback Services Signals

| Event | Description | Payload |
|-------|-------------|---------|
| `feedback.promoted` | Feedback promoted from production | `feedback_id`, `type`, `source_workbench`, `promoter` |
| `problem.promoted` | Problem promoted from production | `problem_id`, `type`, `severity`, `source_workbench` |
| `feedback.triaged` | Feedback categorized | `feedback_id`, `category`, `priority`, `triaged_by` |
| `feedback.accepted` | Feedback accepted for action | `feedback_id`, `action_plan`, `accepted_by` |
| `feedback.rejected` | Feedback rejected | `feedback_id`, `reason`, `rejected_by` |
| `feedback.resolved` | Feedback addressed | `feedback_id`, `resolution`, `resolved_by` |

---

## DevOps Event Format

All signals are normalized to a standard DevOps Event format before routing:

```json
{
  "schema_version": "1.0",
  "event_id": "evt-12345678-abcd-1234-efgh-567890abcdef",
  "event_type": "devops_event",
  
  "event": {
    "type": "idea.submitted",
    "timestamp": "2026-01-09T15:30:00.123Z",
    "payload": {
      "idea_id": "idea-001",
      "title": "Automate refund eligibility check",
      "description": "Currently manual process taking 15 mins per case...",
      "submitter": {
        "user_id": "agent-supervisor-001",
        "role": "supervisor"
      },
      "category": "process_automation",
      "estimated_value": "high",
      "metadata": {
        "source_request_id": "req-12345",
        "related_scenario": "dispute-resolution"
      }
    }
  },
  
  "source": {
    "workbench_id": "dispute-ops-dev",
    "workbench_name": "Dispute Operations - Development",
    "namespace": "acme-bank",
    "subscription_id": "acme-bank",
    "tenant_id": "acme-corp",
    "subsystem": "automation-ideation",
    "domain": "dispute-resolution"
  },
  
  "routing": {
    "via": "atropos",
    "correlation_id": "corr-98765432-wxyz",
    "binding_id": "dispute-devops-binding",
    "routed_at": "2026-01-09T15:30:00.456Z",
    "attempt": 1
  },
  
  "auth": {
    "token_id": "tok-abc123",
    "service_account": "dispute-devops-binding-sa"
  }
}
```

---

## Signal Routing Configuration

### In DevOpsWorkbenchBinding

```yaml
signal_routing:
  enabled: true
  
  # Which subsystem events to route
  sources:
    - subsystem: automation-ideation
      events:
        - idea.submitted
        - idea.promoted
        - intent.completed
        - charter.created
    
    - subsystem: ci-subsystem
      events:
        - test.failed
        - build.failed
      # Route only failures for CI
    
    - subsystem: artifact-registry
      events:
        - promotion.requested
        - artifact.published
    
    - subsystem: feedback-services
      events:
        - feedback.promoted
        - problem.promoted
  
  # Optional: Filter conditions (CEL expressions)
  filters:
    - source: ci-subsystem
      condition: "event.payload.severity == 'critical' || event.payload.test_suite == 'integration'"
    
    - source: automation-ideation
      condition: "event.payload.category != 'documentation'"
  
  # Rate limiting
  rate_limit:
    max_signals_per_minute: 100
    burst: 20
    overflow_policy: queue    # queue | drop | backpressure
  
  # Batching (for high-volume sources)
  batching:
    enabled: false
    max_batch_size: 50
    max_delay: 5s
  
  # Retry configuration
  retry:
    max_attempts: 3
    initial_delay: 1s
    max_delay: 30s
    backoff_multiplier: 2
  
  # Dead letter queue
  dlq:
    enabled: true
    retention: 7d
    alert_threshold: 100
```

---

## Trigger Mapping in DevOps Workbench

DevOps Workbench defines triggers that map incoming events to scenarios:

```yaml
# In DevOps Workbench specification
triggers:
  # APO Scenarios
  - name: idea-triage-trigger
    signal_type: devops_event
    condition: "event.type == 'idea.submitted'"
    scenario: idea-triage
    transformation:
      idea_id: "$.event.payload.idea_id"
      title: "$.event.payload.title"
      source_workbench: "$.source.workbench_id"
  
  - name: intent-drafting-trigger
    signal_type: devops_event
    condition: "event.type == 'idea.promoted'"
    scenario: intent-drafting
    transformation:
      idea_id: "$.event.payload.idea_id"
      intent_id: "$.event.payload.intent_id"
      source_workbench: "$.source.workbench_id"
  
  - name: feedback-triage-trigger
    signal_type: devops_event
    condition: "event.type in ['feedback.promoted', 'problem.promoted']"
    scenario: feedback-triage
    transformation:
      feedback_id: "$.event.payload.feedback_id || $.event.payload.problem_id"
      type: "$.event.type"
      source_workbench: "$.source.workbench_id"
  
  # PA Scenarios
  - name: intent-review-trigger
    signal_type: devops_event
    condition: "event.type == 'intent.completed'"
    scenario: intent-review
    transformation:
      intent_id: "$.event.payload.intent_id"
      business_case: "$.event.payload.business_case"
      source_workbench: "$.source.workbench_id"
  
  - name: scenario-drafting-trigger
    signal_type: devops_event
    condition: "event.type == 'charter.created'"
    scenario: scenario-drafting
    transformation:
      charter_id: "$.event.payload.charter_id"
      scope: "$.event.payload.scope"
      source_workbench: "$.source.workbench_id"
  
  # Developer Scenarios
  - name: test-diagnosis-trigger
    signal_type: devops_event
    condition: "event.type == 'test.failed'"
    scenario: test-diagnosis
    transformation:
      test_run_id: "$.event.payload.test_run_id"
      failures: "$.event.payload.failures"
      logs_ref: "$.event.payload.logs_ref"
      source_workbench: "$.source.workbench_id"
  
  - name: build-resolution-trigger
    signal_type: devops_event
    condition: "event.type == 'build.failed'"
    scenario: build-resolution
    transformation:
      build_id: "$.event.payload.build_id"
      error: "$.event.payload.error"
      logs_ref: "$.event.payload.logs_ref"
      source_workbench: "$.source.workbench_id"
  
  - name: promotion-review-trigger
    signal_type: devops_event
    condition: "event.type == 'promotion.requested'"
    scenario: promotion-review
    transformation:
      promotion_id: "$.event.payload.promotion_id"
      artifact_id: "$.event.payload.artifact_id"
      from_stage: "$.event.payload.from_stage"
      to_stage: "$.event.payload.to_stage"
      source_workbench: "$.source.workbench_id"
```

---

## Delivery Guarantees

### At-Least-Once Delivery

Atropos provides at-least-once delivery semantics:

| Aspect | Behavior |
|--------|----------|
| **Acknowledgment** | D must acknowledge receipt within timeout |
| **Retry** | Automatic retry on failure (configurable) |
| **Idempotency** | D must handle duplicate events (use `event_id`) |
| **Ordering** | Best-effort ordering within source; no global order |

### Idempotency in DevOps Scenarios

DevOps scenarios must be idempotent:

```python
# In DevOps Scenario Application
async def handle_idea_submitted(event: DevOpsEvent):
    idea_id = event.payload.idea_id
    
    # Check if already processed
    existing = await db.get_triage_record(idea_id)
    if existing:
        logger.info(f"Idea {idea_id} already triaged, skipping")
        return existing.result
    
    # Process the idea
    result = await triage_idea(event.payload)
    
    # Record processing
    await db.save_triage_record(idea_id, result)
    
    return result
```

---

## Monitoring and Observability

### Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `devops_signals_routed_total` | Total signals routed | `source_workbench`, `event_type`, `status` |
| `devops_signal_latency_seconds` | End-to-end routing latency | `source_workbench`, `event_type` |
| `devops_signal_retry_count` | Number of retries | `source_workbench`, `event_type` |
| `devops_dlq_size` | Dead letter queue size | `source_workbench` |

### Alerts

| Alert | Condition | Severity |
|-------|-----------|----------|
| `DevOpsSignalRoutingDown` | No signals routed in 1 hour | Warning |
| `DevOpsSignalHighLatency` | P95 latency > 30s | Warning |
| `DevOpsSignalDLQGrowing` | DLQ size > threshold | Critical |
| `DevOpsBindingCredentialExpiring` | Credential expires in < 7 days | Warning |

### Logging

```json
{
  "level": "info",
  "timestamp": "2026-01-09T15:30:00.500Z",
  "logger": "atropos.devops_router",
  "message": "Signal routed successfully",
  "event_id": "evt-12345678-abcd-1234-efgh-567890abcdef",
  "event_type": "idea.submitted",
  "source_workbench": "dispute-ops-dev",
  "target_workbench": "dispute-devops",
  "latency_ms": 45,
  "attempt": 1
}
```

---

## Error Handling

### Transient Failures

| Error | Handling |
|-------|----------|
| Network timeout | Retry with exponential backoff |
| Target temporarily unavailable | Retry with backoff |
| Rate limited (429) | Respect `Retry-After` header |

### Permanent Failures

| Error | Handling |
|-------|----------|
| Invalid credentials (401) | Stop routing; alert operator |
| Target workbench not found (404) | Move to DLQ; alert operator |
| Validation error (400) | Move to DLQ; log error |
| Authorization denied (403) | Stop routing; alert operator |

### Dead Letter Queue

Failed signals are moved to DLQ:

```json
{
  "dlq_entry_id": "dlq-123",
  "original_event": { ... },
  "failure": {
    "reason": "target_unavailable",
    "error_code": "503",
    "message": "Service temporarily unavailable",
    "attempts": 3,
    "first_attempt": "2026-01-09T15:30:00Z",
    "last_attempt": "2026-01-09T15:31:30Z"
  },
  "retention_expires": "2026-01-16T15:30:00Z"
}
```

---

## Related Documentation

- [DevOps Workbench Overview](./README.md)
- [DevOps Workbench Binding](./devops-workbench-binding.md)
- [Atropos (Outbound Gateway)](../../04-subsystems/io-gateways/atropos.md)
- [Signal Exchange](../../04-subsystems/signal-exchange/README.md)
- [Normalized Signal Format](../../02-system-design/implementation-concepts/normalized-signal-format.md)

