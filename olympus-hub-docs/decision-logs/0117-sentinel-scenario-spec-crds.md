# ADR-0117: SentinelScenarioSpec CRD Structure

**Status**: Accepted  
**Date**: 2026-01-14  
**Category**: seer

---

## Context

With the introduction of Request Sentinels (see [ADR-0116](./0116-request-sentinel-type.md)), we need to define how Request Sentinels reference their scenario specifications.

Request Sentinels operate as Employed Agents in a Workbench, which requires:
- A scenario definition (normative, automation, deployment)
- A Hub Application binding (which references a Trained Agent)
- Sentinel-specific configuration (enrollment filters, participation mode)

### Hub Scenario Specification Pattern

Hub uses three scenario specification types aligned with ontology layers:

| Specification | Layer | Created By | Purpose |
|---------------|-------|------------|---------|
| `ScenarioNormativeSpec` | Normative | Process Architect | Goals, roles, SOPs, decision criteria |
| `ScenarioAutomationSpec` | Automation | Developer | Application binding, triggers, tools |
| `ScenarioDeploymentSpec` | Execution | Supervisor | Task queues, SLAs, agent enrollment |

Request Sentinels need all three, plus sentinel-specific configuration.

---

## Decision

We create three new CRD types that extend Hub's ScenarioSpec types:

| CRD | Extends | Sentinel-Specific Additions |
|-----|---------|----------------------------|
| `SentinelScenarioNormativeSpec` | `ScenarioNormativeSpec` | None (pure extension) |
| `SentinelScenarioAutomationSpec` | `ScenarioAutomationSpec` | `sentinel` section with participation filters |
| `SentinelScenarioDeploymentSpec` | `ScenarioDeploymentSpec` | `sentinel_deployment` section with limits |

### Design Principles

1. **Extension, Not Modification**: Sentinel CRDs extend Hub CRDs without modifying them
2. **Isolated Sentinel Section**: Sentinel-specific config in clearly-separated sections
3. **Preserve Reference Chain**: Standard `application.ref` → `HubApplicationSpec` → `seerTrainingRef` pattern
4. **Hub Operator Processing**: Hub Operators can process these as regular ScenarioSpecs (extract sentinel section separately)

### SentinelScenarioAutomationSpec Structure

The key addition is the `sentinel` section:

```yaml
apiVersion: seer.olympus.io/v1
kind: SentinelScenarioAutomationSpec
spec:
  # Standard ScenarioAutomationSpec fields
  normative_ref: ...
  application:
    ref: token-usage-governance-agent  # HubApplicationSpec with seerTrainingRef
    version: "1.0.0"
    runtime: seer
  tools: [...]
  ai_agent: {...}
  
  # Sentinel-specific section (isolated)
  sentinel:
    participation:
      mode: observe_and_participate  # observe | participate | observe_and_participate
      
      filters:
        scenario_whitelist:
          - standard-dispute
          - high-value-dispute
        scenario_blacklist: []
        on_request_update:
          enabled: true
          update_filter_policy: |
            package seer.sentinel.enrollment
            default allow = false
            allow { input.update_type == "DECISION" }
```

### SentinelScenarioDeploymentSpec Structure

The key addition is the `sentinel_deployment` section:

```yaml
apiVersion: seer.olympus.io/v1
kind: SentinelScenarioDeploymentSpec
spec:
  # Standard ScenarioDeploymentSpec fields
  automation_ref: ...
  activation: ...
  task_queues: [...]
  sla: {...}
  
  # Sentinel-specific deployment section
  sentinel_deployment:
    auto_activate: true
    
    enrollment_limits:
      max_concurrent_requests: 100
      cooldown_after_enrollment_ms: 1000
      max_child_requests_per_parent: 1
    
    notification_delivery:
      method: webhook
      retry_policy: {...}
      timeout_ms: 5000
    
    child_request:
      scenario_ref: token-usage-governance
      inherit_context: true
      cascade_completion: true
```

---

## Consequences

### Positive

1. **Clean Extension**: Sentinel CRDs extend Hub CRDs without modification
2. **Familiar Pattern**: Follows Hub's three-layer specification model
3. **Isolated Configuration**: Sentinel config in clearly-marked sections
4. **Hub Operator Compatibility**: Hub Operators can process as standard ScenarioSpecs
5. **Trained Agent Chain Preserved**: Standard reference pattern works unchanged

### Negative

1. **Three New CRD Types**: Adds three CRD types to the system
2. **Parallel Hierarchies**: Sentinel specs mirror Hub specs (some duplication)
3. **Validation Complexity**: Must validate sentinel section and reference chain

### Neutral

1. **API Versioning**: Uses `seer.olympus.io/v1` API group (not Hub's)
2. **Processing Overhead**: Hub Operators extract and separately register sentinel config

---

## Alternatives Considered

### 1. Single SentinelScenarioSpec CRD

Combine all three layers into a single CRD.

**Rejected because:**
- Breaks the normative/automation/deployment separation
- Different personas update different layers (Process Architect vs Developer vs Supervisor)
- Would not align with Hub's established pattern
- Harder to version and evolve independently

### 2. Modify Existing Hub ScenarioSpec CRDs

Add optional `sentinel` section directly to Hub CRDs.

**Rejected because:**
- Couples Seer concepts into Hub core
- Hub CRDs should remain Seer-agnostic
- Breaks separation between platform layers
- Complicates Hub CRD schema

### 3. Use Annotations/Labels Only

Configure sentinel behavior via annotations on standard ScenarioSpecs.

**Rejected because:**
- Annotations have size limits
- OPA policies don't fit in annotations
- No schema validation for annotation content
- Hard to discover and document

### 4. Separate Sentinel Configuration CRD

Create a single `SentinelConfiguration` CRD that references standard ScenarioSpecs.

**Rejected because:**
- Splits configuration across CRDs (harder to reason about)
- Requires cross-CRD references and validation
- Doesn't follow Hub's extension pattern
- More complex deployment flow

---

## Implementation

### Validation Rules

| CRD | Validation |
|-----|------------|
| `SentinelScenarioNormativeSpec` | Standard ScenarioNormativeSpec validation |
| `SentinelScenarioAutomationSpec` | Standard validation + `sentinel.participation.mode` required + OPA policy syntax |
| `SentinelScenarioDeploymentSpec` | Standard validation + `sentinel_deployment` limits positive |

### Reference Chain Validation

```
SentinelScenarioAutomationSpec.application.ref
       │
       ▼
HubApplicationSpec (must exist)
       │
       │ seerTrainingRef (must be present)
       ▼
TrainingSpec (must exist)
```

### Hub Operator Processing

1. Receive SentinelScenarioSpec CRDs
2. Process as standard ScenarioSpec (all non-sentinel fields)
3. Extract `sentinel` section
4. Register enrollment filters with Signal Exchange
5. Create Employed Agent via standard deployment flow

---

## Related

- [ADR-0116: Request Sentinel Type](./0116-request-sentinel-type.md) — Request Sentinel introduction
- [Sentinel Scenario Automation Spec](../../olympus-seer-docs/seer-design/subsystems/seer-sentinels/sentinel-scenario-automation-spec.md) — Full specification
- [Hub Developer Operators](../04-subsystems/operators/developer-operators.md) — Hub ScenarioSpec patterns
- [Hub Application Spec](../04-subsystems/operators/developer-operators.md#hub-application-operator) — seerTrainingRef pattern
