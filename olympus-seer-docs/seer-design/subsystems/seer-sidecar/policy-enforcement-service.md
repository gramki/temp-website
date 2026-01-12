# Policy Enforcement Service

> **Status**: 🟢 Design Complete  
> **Last Updated**: 2026-01-12  
> **Design Level**: C3 (Component) — Detailed API specifications

---

## Overview

The Policy Enforcement Service evaluates OPA policies at runtime for all agent interactions. It provides **early policy enforcement** at the sidecar level, complementing the authoritative enforcement at Tool Gateway and Signal Exchange.

**Key Principle**: Sidecar enforcement provides **defense in depth** — policy violations are caught early before reaching downstream systems.

---

## OPA Policy Evaluation

### Policy Sources

Policies are loaded from multiple sources in precedence order:

| Source | Precedence | Scope |
|--------|------------|-------|
| **Tool Specification** | Base | Per-tool defaults |
| **Training Specification** | Extends | Per-agent type |
| **Employment Specification** | Overrides (narrows only) | Per-deployment |

**Override Rule**: Employment Spec policies can **narrow** but never **expand** Training Spec policies.

### Policy Evaluation Scope

| Traffic Type | Policy Evaluation |
|--------------|-------------------|
| ✅ Inbound `/dispatch` requests | Request content policies |
| ✅ Outbound Hub API calls | Update policies, decision policies |
| ⚠️ Tool invocations | Early enforcement; Tool Gateway enforces authoritatively |
| ⚠️ Model Gateway calls | Early enforcement; Model Gateway enforces authoritatively |

---

## OPA Policy Engine Integration

### Policy Loading

```yaml
# Policy loading from Employment Spec
spec:
  policies:
    # File-based policy references
    files:
      - ref: policies/request-validation.rego
      - ref: policies/decision-limits.rego
    
    # Inline policies
    inline:
      - name: request-scope
        policy: |
          package seer.policy.request
          
          default allow = false
          
          allow {
            input.scenario_id == data.allowed_scenarios[_]
          }
```

### Policy Context Schema

```yaml
# AgentContext (available at all evaluation points)
AgentContext:
  type: object
  required: [agent_id, training_spec, employment_spec]
  properties:
    agent_id:
      type: string
      description: Unique agent identifier
    training_spec:
      type: string
      description: Training spec name
    employment_spec:
      type: string
      description: Employment spec name
    iam_role:
      type: string
      description: Delegated IAM role ARN
    delegated_scopes:
      type: array
      items:
        type: string
      description: Delegated permission scopes
    accountable_user:
      type: string
      description: IAM user/group accountable for this agent

# AccessContext (request-specific context)
AccessContext:
  type: object
  required: [tenant_id, workbench_id, scenario_id, request_id]
  properties:
    tenant_id:
      type: string
    workbench_id:
      type: string
    scenario_id:
      type: string
    request_id:
      type: string

# InboundContext (for /dispatch requests)
InboundContext:
  allOf:
    - $ref: "#/AgentContext"
    - $ref: "#/AccessContext"
    - type: object
      properties:
        payload:
          type: object
          description: Dispatch request payload
        headers:
          type: object
          description: HTTP headers

# OutboundContext (for Hub API calls)
OutboundContext:
  allOf:
    - $ref: "#/AgentContext"
    - $ref: "#/AccessContext"
    - type: object
      properties:
        api_endpoint:
          type: string
          description: Target API endpoint
        api_method:
          type: string
          enum: [GET, POST, PUT, DELETE, PATCH]
        payload:
          type: object
          description: API call payload
```

---

## Policy Decision Types

| Decision | Behavior | Recording |
|----------|----------|-----------|
| **ALLOW** | Action proceeds | Logged for audit |
| **ALERT** | Action proceeds, notification sent | Logged + Observation created |
| **REJECT** | Action blocked | Recorded as violation on Request |

> **Terminology Note**: OPA policies use "REJECT" (uppercase) for blocking operations. Guardrails (in Guardrail Service) use "Deny" for the same concept. Both result in blocking the operation.

### OPA Decision Format

```json
{
  "decision": "REJECT",
  "reason_code": "SCOPE_VIOLATION",
  "reason": "Request targets customer tier not in agent scope",
  "policy_id": "seer.policy.scope",
  "evaluation_context": {
    "agent_id": "fraud-analyst-001",
    "api_endpoint": "/api/agent/v1/requests/req-123/updates",
    "timestamp": "2026-01-12T14:30:00Z"
  }
}
```

---

## Policy Evaluation API

### Internal API

```yaml
# POST /internal/policy/evaluate
PolicyEvaluationRequest:
  type: object
  required: [context, policies]
  properties:
    context:
      oneOf:
        - $ref: "#/InboundContext"
        - $ref: "#/OutboundContext"
    policies:
      type: array
      items:
        type: string
      description: Policy references to evaluate
    evaluation_mode:
      type: string
      enum: [strict, lenient]
      default: strict
      description: strict = fail on any REJECT; lenient = aggregate results

PolicyEvaluationResponse:
  type: object
  required: [decision, evaluations]
  properties:
    decision:
      type: string
      enum: [ALLOW, ALERT, REJECT]
      description: Aggregate decision
    evaluations:
      type: array
      items:
        type: object
        properties:
          policy_id:
            type: string
          decision:
            type: string
            enum: [ALLOW, ALERT, REJECT]
          reason_code:
            type: string
          reason:
            type: string
          duration_ms:
            type: integer
    total_duration_ms:
      type: integer
```

### Example Policy Evaluation

```python
# Policy evaluation request
request = PolicyEvaluationRequest(
    context=OutboundContext(
        agent_id="fraud-analyst-001",
        training_spec="fraud-analyst-v2",
        employment_spec="acme-fraud-emp-001",
        tenant_id="acme",
        workbench_id="acme-disputes",
        scenario_id="fraud-investigation",
        request_id="req-abc123",
        api_endpoint="/api/agent/v1/decisions",
        api_method="POST",
        payload={
            "decision_type": "refund_approved",
            "amount": 7500,
            "case_id": "case-67890"
        }
    ),
    policies=["seer.policy.decision.limits", "seer.policy.scope"]
)

# Policy evaluation response
response = PolicyEvaluationResponse(
    decision="REJECT",
    evaluations=[
        {
            "policy_id": "seer.policy.decision.limits",
            "decision": "REJECT",
            "reason_code": "AMOUNT_EXCEEDED",
            "reason": "Decision amount 7500 exceeds limit of 5000",
            "duration_ms": 5
        },
        {
            "policy_id": "seer.policy.scope",
            "decision": "ALLOW",
            "reason_code": None,
            "reason": None,
            "duration_ms": 2
        }
    ],
    total_duration_ms=7
)
```

---

## Policy Override Rules

Employment Spec can narrow but never expand Training Spec policies:

```yaml
# Training Spec policy
spec:
  policies:
    decision_limits:
      max_refund_amount: 5000
      allowed_decision_types: ["refund_approved", "refund_denied", "escalate"]

# Employment Spec override (narrower)
spec:
  policies:
    decision_limits:
      max_refund_amount: 2500        # ✅ Narrower than 5000
      allowed_decision_types:         # ✅ Subset
        - "refund_approved"
        - "escalate"
```

Invalid overrides are rejected at deployment time:

```yaml
# INVALID Employment Spec override
spec:
  policies:
    decision_limits:
      max_refund_amount: 10000       # ❌ Wider than Training Spec
```

---

## Policy Violation Handling

### Violation Recording

All violations are recorded on the Request:

```json
{
  "request_id": "req-abc123",
  "violations": [
    {
      "id": "vio-001",
      "timestamp": "2026-01-12T14:30:00Z",
      "enforcement_point": "SIDECAR",
      "decision": "REJECT",
      "reason_code": "AMOUNT_EXCEEDED",
      "reason": "Decision amount 7500 exceeds limit of 5000",
      "policy_id": "seer.policy.decision.limits",
      "agent_id": "fraud-analyst-001",
      "action_attempted": {
        "api_endpoint": "/api/agent/v1/decisions",
        "payload": {
          "decision_type": "refund_approved",
          "amount": 7500
        }
      }
    }
  ]
}
```

### Violation Notification Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    VIOLATION NOTIFICATION FLOW                               │
│                                                                              │
│   Policy Violation Detected                                                 │
│           │                                                                  │
│           ▼                                                                  │
│   ┌─────────────────┐                                                       │
│   │ Record on       │ Violation recorded with full context                  │
│   │ Request         │                                                       │
│   └────────┬────────┘                                                       │
│            │                                                                 │
│   ┌────────┼────────┬───────────────┐                                       │
│   ▼        ▼        ▼               ▼                                       │
│ Observers  Accountable  Workbench   Agent Health                            │
│ Notified   Person       Observation Monitor                                 │
│            Notified     Created     Alerted                                 │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Violation Response Types

| Response | Behavior |
|----------|----------|
| **Block** | Operation rejected with error |
| **Allow with Alert** | Operation proceeds, notification sent |
| **Escalate** | Operation blocked, escalation triggered |

---

## Integration Points

### Agent Lifecycle Manager
- OPA policy configuration from Employment Spec → Policy loading
- Policy changes trigger hot-reload

### OPA Policy Engine
- Policy evaluation requests → Policy decisions
- Policy bundle loading → Runtime policies

### Guardrail Service
- Policy violations → Guardrail rejection
- Shared enforcement pipeline

### Tool Gateway (Authoritative)
- Tool invocation policies → Authoritative enforcement
- Sidecar provides early enforcement

### Model Gateway (Authoritative)
- Model invocation policies → Authoritative enforcement
- Sidecar provides early enforcement

### Signal Exchange
- REQUEST_UPDATE policies → Enforced by sidecar on outbound calls

### Agent Health Monitor
- Policy violations → Health alerts
- Violation patterns → Health score impact

---

## Observability

### Metrics

| Metric | Description | Labels |
|--------|-------------|--------|
| `seer_policy_evaluation_total` | Total evaluations | `policy_id`, `decision` |
| `seer_policy_evaluation_duration_seconds` | Evaluation latency | `policy_id` |
| `seer_policy_violation_total` | Violations | `policy_id`, `reason_code` |
| `seer_policy_cache_hit_total` | Policy cache hits | `policy_id` |

### Tracing

```json
{
  "traceId": "trace-abc123",
  "spans": [
    {
      "name": "policy.evaluate.seer.policy.decision.limits",
      "duration": 5,
      "result": "REJECT",
      "tags": {
        "policy_id": "seer.policy.decision.limits",
        "reason_code": "AMOUNT_EXCEEDED"
      }
    },
    {
      "name": "policy.evaluate.seer.policy.scope",
      "duration": 2,
      "result": "ALLOW"
    }
  ]
}
```

### Audit

Policy evaluations are logged to CAF:

```json
{
  "record_type": "policy_evaluation",
  "request_id": "req-abc123",
  "agent_id": "fraud-analyst-001",
  "enforcement_point": "sidecar",
  "api_endpoint": "/api/agent/v1/decisions",
  "policy_id": "seer.policy.decision.limits",
  "decision": "REJECT",
  "reason_code": "AMOUNT_EXCEEDED",
  "timestamp": "2026-01-12T14:30:00Z"
}
```

---

## Related Documentation

- [Authority Enforcement Service](./authority-enforcement-service.md) — Ceiling enforcement
- [Guardrail Service](./guardrail-service.md) — Request/response enforcement
- [Authority Enforcement Concepts](../../implementation-concepts/authority-enforcement.md) — Conceptual overview
- [ADR-0073: Authority Enforcement via OPA](../../../../olympus-hub-docs/decision-logs/0073-seer-authority-enforcement-opa.md)

---

*Policy Enforcement Service provides OPA-based policy evaluation for all agent interactions, with detailed API specifications for policy evaluation, violation handling, and integration with Hub enforcement points.*
