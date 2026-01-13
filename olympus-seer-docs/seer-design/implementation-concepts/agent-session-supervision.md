# Agent Session Sentinel Oversight

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-14

## Overview

Agent Session Sentinel Oversight provides **sentinel oversight** for agent sessions, managing sentinel policies, observations, and escalations for failed or stuck agents. It also enables AI agents to observe and participate in other agents' requests.

**Key Capabilities:**
- Real-time sentinel oversight via Signal Exchange event observation
- Analytical sentinel oversight via Agent Analytics data mart queries
- Request sentinel oversight via AI agents observing/participating in requests
- OPA policy evaluation for sentinel decisions
- Observation/Exception generation via Cronus Gateway
- Child request creation for cross-request monitoring
- Workbench routing for Ops Center display

---

## Architecture

Agent Session Sentinel operates in three modes:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                  AGENT SESSION SENTINEL ARCHITECTURE                        │
│                                                                              │
│   ┌──────────────────────┐  ┌──────────────────────┐  ┌──────────────────┐  │
│   │  Realtime Sentinel   │  │ Analytical Sentinel  │  │ Request Sentinel │  │
│   │  • SX event observe  │  │ • SQL on analytics   │  │ • Enroll in reqs │  │
│   │  • OPA policy eval   │  │ • Periodic execution │  │ • Employed Agent │  │
│   └──────────┬───────────┘  └──────────┬───────────┘  └────────┬─────────┘  │
│              │                          │                       │            │
│              └────────────┬─────────────┘                       │            │
│                           │                                     │            │
│              ┌────────────▼────────────┐                        │            │
│              │   Observation Service   │                        │            │
│              │   (Cronus Integration)  │                        │            │
│              └────────────┬────────────┘                        │            │
│                           │                                     │            │
│              ┌────────────▼────────────┐          ┌─────────────▼──────────┐│
│              │     Cronus Gateway      │          │   Hub Request Model    ││
│              │   (Observations/        │          │   (Child Requests,     ││
│              │    Exceptions)          │          │    Agent Actions)      ││
│              └─────────────────────────┘          └────────────────────────┘│
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Principles

- **Three Sentinel Types** — Realtime, Analytical, and Request sentinels for different use cases
- **Cronus Integration** — Realtime/Analytical sentinels use Hub's Observation/Exception model via Cronus Gateway
- **Hub Request Integration** — Request sentinels create child requests and operate as Employed Agents
- **Deployment Model** — Sentinels deployed via Deployment CRDs referencing Spec CRDs
- **Lifecycle Pattern** — Follows same pattern as Trained/Employed Agent lifecycle managers
- **No Enforcement** — Sentinels generate observations or take actions within their scope; cross-request enforcement handled externally

---

## Sentinel Types

### Realtime Sentinel

Observes Signal Exchange events in real-time:

| Capability | Description |
|------------|-------------|
| **Event Observation** | Observes SX events for agent sessions |
| **OPA Policy Evaluation** | Evaluates OPA policies on events |
| **Real-time Generation** | Generates Observations/Exceptions immediately |
| **Use Cases** | Stuck agents, failed requests, policy violations |

### Analytical Sentinel

Runs templated SQL queries on Agent Analytics data mart:

| Capability | Description |
|------------|-------------|
| **SQL Execution** | Runs templated SQL queries periodically |
| **Data Mart Queries** | Queries Agent Analytics data mart |
| **Periodic Execution** | Runs on schedule (cron-based) |
| **Use Cases** | Trend analysis, pattern detection, historical issues |

### Request Sentinel

Operates as an Employed Agent that observes and/or participates in other agents' requests:

| Capability | Description |
|------------|-------------|
| **Request Enrollment** | Automatically enrolls in requests based on configurable filters |
| **Employed Agent** | Runs as a full Employed Agent with delegated authority |
| **Child Requests** | Creates child requests using sentinel's own scenario |
| **Webhook Notifications** | Receives REQUEST_UPDATE notifications for monitored requests |
| **Use Cases** | Token governance, compliance monitoring, quality assurance, fraud detection |

---

## Why Request Sentinels

### The Need for Cross-Request Observation

Realtime and Analytical Sentinels are powerful for generating Observations and Exceptions, but they have a fundamental limitation: **they cannot participate in requests**. They observe events and data, evaluate policies, and generate alerts — but they operate outside the request lifecycle.

| Capability | Realtime/Analytical | Request Sentinel |
|------------|---------------------|------------------|
| Observe events/data | ✅ | ✅ |
| Evaluate OPA policies | ✅ | ✅ |
| Generate Observations | ✅ | ❌ (uses child requests) |
| Participate in requests | ❌ | ✅ |
| Take actions on requests | ❌ | ✅ (within child request) |
| Access request context | Limited | Full (via context inheritance) |
| Create follow-up work | ❌ | ✅ |

### Gap in Realtime/Analytical Model

Consider these scenarios that Realtime/Analytical Sentinels cannot address:

1. **Token Usage Governance**: An AI agent needs to monitor token consumption across requests and intervene when budgets are exceeded — not just alert, but actually pause or adjust behavior.

2. **Compliance Sampling**: A compliance sentinel needs to review a sample of AI decisions, verify evidence, and create remediation tasks when issues are found.

3. **Quality Assurance**: A QA sentinel needs to observe agent outputs, score quality, and create retraining tickets for patterns of poor performance.

These scenarios require an AI agent that can:
- Observe other agents' work in real-time
- Access the full request context
- Take actions (create tasks, add memos, escalate)
- Work within the standard Hub Request model

**Request Sentinels fill this gap** by operating as Employed Agents within the Workbench, creating child requests that give them a proper scope for observation and action.

### AI Agents Monitoring AI Agents

Request Sentinels enable a new pattern: **AI agents overseeing other AI agents**. This is essential for:

- **Scalable Governance**: Human supervisors can't review every AI decision; AI sentinels can
- **Real-time Intervention**: Sentinels can act immediately, not just alert
- **Continuous Improvement**: Pattern detection feeds back into training and configuration
- **Audit Trail**: All sentinel actions are recorded as part of the request history

---

## Request Sentinel Use Cases

### Token Usage Governance

**Problem**: AI agents consume tokens unpredictably; need to enforce budgets without manual monitoring.

**Solution**: A Request Sentinel monitors token usage across requests, flags when budgets are approached, and can pause/throttle agents exceeding limits.

```yaml
sentinel_scenario:
  name: token-usage-governance
  participation:
    mode: observe_and_participate
    filters:
      scenario_whitelist: ["*"]  # All scenarios
      on_request_update:
        enabled: true
        update_filter_policy: |
          allow { input.payload.metrics.token_usage != null }
```

### Compliance Monitoring

**Problem**: Regulatory requirements mandate review of AI decisions, but volume is too high for human review.

**Solution**: A Request Sentinel samples decisions, verifies required evidence is present, checks against compliance rules, and creates remediation tasks for violations.

**Monitored Scenarios**: High-value disputes, loan decisions, fraud determinations

### Quality Assurance Sampling

**Problem**: Need to continuously assess AI agent quality without disrupting operations.

**Solution**: A QA Sentinel randomly samples completed requests, evaluates output quality against rubrics, and feeds results into improvement pipelines.

**Actions**: Score quality, flag outliers, create training data tickets

### Fraud Pattern Detection

**Problem**: Individual fraud checks pass, but cross-request patterns indicate coordinated fraud.

**Solution**: A Request Sentinel observes multiple requests, correlates patterns (timing, amounts, entities), and escalates when patterns emerge.

**Monitored Scenarios**: Payment processing, account changes, dispute filings

### Escalation Pattern Analysis

**Problem**: Too many escalations indicate process or training issues; need to identify root causes.

**Solution**: A Request Sentinel monitors escalation events, clusters by cause, and creates improvement tickets when patterns emerge.

**Actions**: Categorize escalations, identify training gaps, propose SOP changes

### Cross-Request Correlation

**Problem**: Related requests need coordinated handling; agents working in isolation miss connections.

**Solution**: A Request Sentinel monitors requests, identifies connections (same customer, related transactions), and ensures appropriate coordination.

**Actions**: Link related requests, notify assigned agents, flag conflicts

---

## COG Sentinels (Cross-Workbench)

### Subscription-Wide Governance

Request Sentinels operate within a single workbench. For subscription-wide governance, **COG Sentinels** (Cognitive Operations Governance Sentinels) extend Request Sentinels to operate across multiple workbenches.

| Capability | Request Sentinel | COG Sentinel |
|------------|------------------|--------------|
| **Scope** | Single workbench | Subscription-wide |
| **Definition** | Any workbench | COGW workbench only |
| **Targeting** | Implicit (same workbench) | Explicit (cogSpec patterns) |
| **Visibility** | Single workbench | Multiple workbenches (read-only) |
| **Local Control** | Full control | Enable/disable only |

### COGW Workbench

COG Sentinels are defined in Cognitive Operations Governance Workbenches (COGWs):

- **Workbench type**: `workbench_type: "cogw"`
- **Default COGW**: Every subscription gets a default COGW at creation
- **Pattern-based targeting**: `cogSpec.workbench_patterns` defines target workbenches
- **Read-only sync**: COG Sentinel specs appear as read-only in target workbenches

### COG Sentinel Use Cases

| Use Case | Description |
|----------|-------------|
| **Enterprise Token Governance** | Enforce token budgets across all workbenches |
| **Cross-Domain Compliance** | Compliance rules spanning multiple domains |
| **Enterprise AI Quality** | Quality patterns compared across workbenches |
| **Unified Security Monitoring** | Security sentinels observing all workbenches |

→ See [Cognitive Operations Governance Workbench](../subsystems/cognitive-operations-governance-workbench/README.md) for details.

---

## Sentinel Spec Structure

Sentinel Specs define sentinel policies:

| Component | Description |
|-----------|-------------|
| **Sentinel Policies** | OPA policies for realtime sentinels |
| **SQL Templates** | Templated SQL queries for analytical sentinels |
| **Observation Rules** | Rules for generating Observations/Exceptions |
| **Workbench Routing** | Routing configuration for observations |

---

## Observation Service

Observation Service generates Observations/Exceptions:

| Capability | Description |
|------------|-------------|
| **Observation Generation** | Generate Observations via Cronus Gateway |
| **Exception Generation** | Generate Exceptions via Cronus Gateway |
| **Workbench Routing** | Route observations to appropriate workbenches |
| **Ops Center Display** | Display observations in Hub Ops Center |

---

## Cronus Integration

Agent Session Sentinel integrates with Cronus Gateway:

| Aspect | Description |
|--------|-------------|
| **Observation Model** | Uses Hub's existing Observation/Exception model |
| **No New Model** | No new model required; leverages existing Hub model |
| **Workbench Routing** | Observations routed to workbenches via Cronus |
| **Ops Center** | Observations displayed in Hub Ops Center |

---

## Deployment Model

Sentinels follow a deployment model:

| Component | Description |
|-----------|-------------|
| **Spec CRD** | Sentinel Spec CRD defines sentinel policies |
| **Deployment CRD** | Deployment CRD references Spec CRD |
| **Clear Separation** | Spec definition separate from deployment configuration |
| **Seer Operator** | Seer Operator reconciles CRDs to Kubernetes state |

---

## Related

### Seer Sentinels Subsystem
- [Seer Sentinels README](../subsystems/seer-sentinels/README.md) — Subsystem overview
- [Sentinel Spec Manager](../subsystems/seer-sentinels/sentinel-spec-manager.md) — Spec structure, validation
- [Realtime Sentinel Service](../subsystems/seer-sentinels/realtime-sentinel-service.md) — SX event observation, OPA evaluation
- [Analytical Sentinel Service](../subsystems/seer-sentinels/analytical-sentinel-service.md) — Templated SQL execution
- [Observation Service](../subsystems/seer-sentinels/observation-service.md) — Cronus Observations/Exceptions generation

### Request Sentinel Documentation
- [Sentinel Scenario Normative Spec](../subsystems/seer-sentinels/sentinel-scenario-normative-spec.md) — Normative requirements
- [Sentinel Scenario Automation Spec](../subsystems/seer-sentinels/sentinel-scenario-automation-spec.md) — Automation with enrollment filters
- [Sentinel Scenario Deployment Spec](../subsystems/seer-sentinels/sentinel-scenario-deployment-spec.md) — Deployment configuration
- [Sentinel Scenario Processing](../hub-integration/sentinel-scenario-processing.md) — Hub integration flow

### Related Systems
- [Agent Health Monitor](../subsystems/agent-health-monitor/README.md) — Can trigger sentinels on SLO deviations
- [Agent Analytics](../subsystems/agent-analytics/README.md) — Uses Agent Analytics data mart for analytical sentinels
- [Signal Exchange](../../../olympus-hub-docs/04-subsystems/signal-exchange/README.md) — SX event source for realtime sentinels, auto-enrollment for request sentinels
- [Cronus Gateway](../../../olympus-hub-docs/04-subsystems/signal-providers/cronus-business-exceptions.md) — Observations/Exceptions publishing
- [Request Hierarchy](../../../olympus-hub-docs/04-subsystems/request-management/request-hierarchy.md) — Child request model for request sentinels

---

*For detailed implementation, see [Seer Sentinels README](../subsystems/seer-sentinels/README.md).*
