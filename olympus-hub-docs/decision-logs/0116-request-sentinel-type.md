# ADR-0116: Request Sentinel Type

**Status**: Accepted  
**Date**: 2026-01-14  
**Category**: seer

---

## Context

The Seer Sentinels subsystem provides sentinel oversight for agent sessions via two types:

1. **Realtime Sentinel**: Observes Signal Exchange events, evaluates OPA policies, generates Observations/Exceptions via Cronus
2. **Analytical Sentinel**: Runs templated SQL on analytics data mart, generates Observations/Exceptions via Cronus

Both types share a common limitation: **they generate Observations but cannot participate in requests**. They operate outside the request lifecycle — observing and alerting, but not taking action within the request context.

### The Gap

Several oversight scenarios require more than observation:

| Scenario | Need | Realtime/Analytical Capability |
|----------|------|-------------------------------|
| Token Usage Governance | Monitor and intervene when budgets exceeded | Observe ✅, Intervene ❌ |
| Compliance Sampling | Review decisions and create remediation tasks | Observe ✅, Create tasks ❌ |
| Quality Assurance | Score outputs and create training tickets | Observe ✅, Create tickets ❌ |
| Fraud Pattern Detection | Correlate across requests and escalate | Limited ⚠️, Escalate ❌ |

These scenarios require an AI agent that can:
- Observe other agents' work in real-time
- Access full request context
- Take actions (create tasks, add memos, escalate)
- Work within the standard Hub Request model

### AI Agents Monitoring AI Agents

As AI agent adoption scales, human supervisors cannot review every decision. We need AI agents that can:
- Continuously monitor other AI agents
- Apply governance rules in real-time
- Take corrective action when needed
- Maintain full audit trail

---

## Decision

We introduce a third Sentinel type: **Request Sentinel**.

Request Sentinels operate as **Employed Agents** within a Workbench, observing and/or participating in requests by:
1. Automatically enrolling in requests based on configurable filters
2. Creating child requests using the sentinel's own scenario
3. Receiving webhook notifications for REQUEST_UPDATE events
4. Taking actions within their child request scope

### Key Characteristics

| Aspect | Request Sentinel |
|--------|------------------|
| **Operation Model** | Employed Agent in Workbench |
| **Specification** | SentinelScenarioSpec CRDs (extends Hub ScenarioSpec) |
| **Enrollment** | Automatic based on filters (scenario whitelist/blacklist, OPA policy) |
| **Output** | Child requests, agent actions (not Cronus Observations) |
| **Integration** | Hub Request model via Hub Operators |

### Comparison with Existing Types

| Capability | Realtime | Analytical | Request |
|------------|----------|------------|---------|
| Observe events | ✅ SX events | ✅ Analytics | ✅ Request updates |
| Evaluate policies | ✅ OPA | ✅ SQL | ✅ OPA |
| Generate Observations | ✅ Cronus | ✅ Cronus | ❌ |
| Participate in requests | ❌ | ❌ | ✅ |
| Access request context | Limited | Via SQL | ✅ Full |
| Create follow-up work | ❌ | ❌ | ✅ |

---

## Consequences

### Positive

1. **Enables AI-to-AI Oversight**: AI agents can now monitor and govern other AI agents
2. **Fills Observation Gap**: Request sentinels can take action, not just alert
3. **Leverages Existing Models**: Uses Hub Request model (child requests, context inheritance)
4. **Audit Trail**: All sentinel actions recorded in request history
5. **Flexible Enrollment**: Scenario filters and OPA policies enable precise targeting

### Negative

1. **Complexity**: Third sentinel type adds conceptual complexity
2. **Hub Integration**: Requires coordination with Hub Operators, Signal Exchange
3. **Resource Usage**: Each enrolled sentinel creates a child request and runs as Employed Agent
4. **Potential Loops**: Must prevent sentinels from enrolling in their own child requests

### Neutral

1. **Different Output Model**: Request sentinels don't generate Cronus Observations (different purpose)
2. **New CRD Types**: Requires three new SentinelScenarioSpec CRD types

---

## Alternatives Considered

### 1. Extend Realtime Sentinel to Take Actions

Allow Realtime Sentinels to take actions on requests in addition to generating Observations.

**Rejected because:**
- Realtime Sentinels operate outside request context
- Would require fundamental redesign of the observation model
- Breaks the "generate Observations" contract
- No clear scope for actions (which request? which authority?)

### 2. Use Regular Scenario Enrollment

Deploy governance agents as regular scenarios that receive signals.

**Rejected because:**
- No cross-request filtering capability
- Cannot observe all requests meeting criteria
- Would need explicit invocation (not automatic)
- Doesn't fit the "sentinel" mental model (passive observer)

### 3. Extend Signal Exchange Observer Pattern

Allow observers to take actions, not just receive notifications.

**Rejected because:**
- Observers are modules, not agents
- No authority/delegation model for observers
- Would conflate notification with action
- Breaks the observer pattern contract

### 4. Add "Action" Phase to Observation Service

After generating Observation, optionally execute configured actions.

**Rejected because:**
- Actions need request context (Observation Service doesn't have it)
- Would couple observation to action incorrectly
- No delegated authority for actions
- Actions should be traceable to an agent, not a service

---

## Implementation

### Specification Structure

Request Sentinels use a SentinelSpec with `type: request` and reference SentinelScenarioSpec CRDs:

```yaml
apiVersion: seer.olympus.io/v1
kind: SentinelSpec
metadata:
  name: token-usage-governance-sentinel
spec:
  type: request  # realtime | analytical | request
  
  target:
    workbench_ids: ["acme-disputes"]
  
  sentinel_scenario_specs:
    normative_ref:
      name: token-usage-governance-normative
      version: "1.0.0"
    automation_ref:
      name: token-usage-governance-automation
      version: "1.0.0"
    deployment_ref:
      name: token-usage-governance-deployment
      version: "1.0.0"
```

### Enrollment Flow

1. Request created in Workbench
2. Signal Exchange queries active Request Sentinels
3. Apply scenario whitelist/blacklist filters
4. If match: Create child request, notify sentinel via webhook
5. Sentinel processes via Employed Agent

---

## Related

- [ADR-0117: SentinelScenarioSpec CRD Structure](./0117-sentinel-scenario-spec-crds.md) — CRD structure decision
- [Seer Sentinels README](../../olympus-seer-docs/seer-design/subsystems/seer-sentinels/README.md) — Subsystem overview
- [Sentinel Scenario Processing](../../olympus-seer-docs/seer-design/hub-integration/sentinel-scenario-processing.md) — Hub integration
- [Request Hierarchy](../04-subsystems/request-management/request-hierarchy.md) — Child request model
