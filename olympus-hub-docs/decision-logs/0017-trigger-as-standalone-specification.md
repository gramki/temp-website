# ADR-0017: Trigger as Standalone Specification

## Status

**Accepted**

## Date

2026-01-06

## Context

Triggers define how incoming signals are matched and transformed to create or update Requests within Scenarios. They specify:
- Signal source (I/O Gateway, Signal Provider)
- Matching conditions (field comparisons, operators)
- Context transformation (JavaScript, JSONata, mapping)
- Request creation settings (subject binding, priority calculation)
- Idempotency and correlation rules

Originally, trigger definitions were embedded within Scenario Automation Specifications. However:
1. Triggers can be complex with detailed matching logic and transformations
2. Multiple Scenarios may share similar trigger patterns
3. Trigger changes may need independent versioning from Scenario automation
4. Signal Exchange benefits from a dedicated trigger catalog

## Decision

Define **TriggerSpec as a standalone CRD** that is referenced by Scenario Automation Specifications:

```yaml
apiVersion: hub.olympus.io/v1
kind: TriggerSpec
metadata:
  name: dispute-submitted-trigger
spec:
  trigger:
    id: dispute-submitted
    name: "Dispute Submitted"
    workbench_ref: dispute-operations
  
  signal_source:
    type: io_gateway
    gateway_ref: heracles-api-gateway
    
  conditions:
    match_all:
      - field: "signal_header.signal_type"
        operator: equals
        value: "dispute.submitted"
        
  transformation:
    type: javascript
    script: |
      (signal) => ({
        dispute_id: signal.payload.data.dispute_id,
        customer_id: signal.payload.data.customer_id
      })
```

Referenced from Scenario Automation Specification:

```yaml
kind: ScenarioAutomationSpec
spec:
  triggers:
    - ref: dispute-submitted-trigger
      required: true
    - ref: merchant-response-trigger
      required: false
```

## Alternatives Considered

### Alternative 1: Inline Triggers in Scenario Automation
```yaml
kind: ScenarioAutomationSpec
spec:
  triggers:
    - id: dispute-submitted
      signal_source: ...
      conditions: ...
      transformation: ...
```

- **Pros**: All-in-one specification, simpler reference model
- **Cons**: Large specifications, no reuse across scenarios, harder to maintain

### Alternative 2: Trigger Catalog (Non-CRD)
Store triggers in a configuration database rather than as CRDs.

- **Pros**: Dynamic updates, no Git workflow required
- **Cons**: Loses GitOps benefits, no version control, inconsistent with other resources

## Consequences

### Positive
- **Reusability**: Same trigger can be referenced by multiple Scenarios
- **Independent Versioning**: Trigger changes don't require Scenario version bump
- **Clarity**: Complex trigger logic isolated from Scenario automation
- **Signal Exchange Integration**: Trigger catalog enables SX to load triggers independently

### Negative
- **Additional CRD**: One more resource type to manage
- **Reference Complexity**: Broken references if trigger deleted before scenario
- **Coordination**: Trigger and Scenario versions must be compatible

### Neutral
- TriggerSpec managed by scenario-developer-operator
- Validation ensures referenced triggers exist before Scenario deployment

## Trigger Categories

| Category | Example | Use Case |
|----------|---------|----------|
| **Event-based** | Customer submits dispute | External system events via Atropos |
| **API-based** | REST API call | Direct API invocation via Heracles |
| **Scheduled** | Daily reconciliation | Time-based triggers via Kale |
| **File-based** | Batch file arrival | File upload events via Tyche |
| **Correlation** | Merchant response | Updates to existing requests |

## Related Decisions

- [ADR-0001: Signal Normalization](./0001-signal-normalization.md)
- [ADR-0002: Scenario Specification Types](./0002-scenario-specification-types.md)
- [ADR-0014: GitOps-Based Operator Model](./0014-gitops-operator-model.md)

