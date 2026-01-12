# Authority Enforcement

> **Status**: 🟠 Legacy — See new design docs  
> **Last Updated**: 2026-01-08

---

> ⚠️ **Note**: Sidecar enforcement content has been migrated to [Authority Enforcement Service](./seer-sidecar/authority-enforcement-service.md) and [Policy Enforcement Service](./seer-sidecar/policy-enforcement-service.md). This document is retained for reference. See [Seer Sidecar](./seer-sidecar/README.md) for the current design.

---

## Overview

Authority enforcement ensures AI agents operate within their delegated limits. Hub provides **multiple enforcement points** with **OPA-based policies** that validate agent actions against their authorized scope.

**Key Principle**: Enforcement is **layered** — violations are caught at the appropriate point and recorded on the Request for audit and corrective action.

---

## Enforcement Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AUTHORITY ENFORCEMENT FLOW                                │
│                                                                              │
│                         Agent Action                                         │
│                              │                                               │
│                              ▼                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                   1. SIDECAR GUARDRAILS                              │   │
│   │                   (Tenant-defined, custom logic)                     │   │
│   │                   → Transform, Reject, or Pass                       │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                               │
│                              ▼                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                   2. TOOL GATEWAY                                    │   │
│   │                   • OPA policies (Tool Spec + Employment Spec)       │   │
│   │                   • IAM role and scope validation                    │   │
│   │                   → ALLOW / ALERT / REJECT                           │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                               │
│                              ▼                                               │
│                      Tool Execution                                          │
│                              │                                               │
│                              ▼                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                   3. SIGNAL EXCHANGE                                 │   │
│   │                   • OPA policies on REQUEST_UPDATE                   │   │
│   │                   • Any agent update subject to policy               │   │
│   │                   → ALLOW / ALERT / REJECT                           │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                               │
│                              ▼                                               │
│                    Request Updated / Violation Recorded                      │
│                              │                                               │
│              ┌───────────────┼───────────────┐                              │
│              ▼               ▼               ▼                              │
│         Observers       Accountable     Workbench                           │
│         Notified        Person (IAM)   Observation                          │
│                         Notified       Created                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Enforcement Points

### 1. Sidecar Guardrails

Tenant-defined guardrails provide **custom enforcement logic**:

- Deployed as Istio sidecars in agent pods
- Execute before/after agent actions
- Can transform, reject, or pass requests
- See [Guardrails](./guardrails.md) for details

**Use Case**: Domain-specific rules, compliance requirements, custom thresholds.

---

### 2. Tool Gateway

The Tool Gateway is the **primary enforcement point** for tool invocations:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         TOOL GATEWAY ENFORCEMENT                             │
│                                                                              │
│   Agent                Tool Gateway                     Tool                 │
│     │                      │                              │                  │
│     │  invoke(tool, params)│                              │                  │
│     │─────────────────────►│                              │                  │
│     │                      │                              │                  │
│     │                      │ ┌──────────────────────────┐ │                  │
│     │                      │ │ OPA Policy Evaluation    │ │                  │
│     │                      │ │                          │ │                  │
│     │                      │ │ Inputs:                  │ │                  │
│     │                      │ │ • Agent IAM context      │ │                  │
│     │                      │ │ • Tool parameters        │ │                  │
│     │                      │ │ • Request context        │ │                  │
│     │                      │ │                          │ │                  │
│     │                      │ │ Policies from:           │ │                  │
│     │                      │ │ • Tool Specification     │ │                  │
│     │                      │ │ • Employment Spec        │ │                  │
│     │                      │ │ (Employment overrides)   │ │                  │
│     │                      │ └──────────────────────────┘ │                  │
│     │                      │                              │                  │
│     │                      │ Decision: ALLOW/ALERT/REJECT │                  │
│     │                      │──────────────────────────────│                  │
│     │                      │                              │                  │
│     │  If ALLOW:           │         execute()            │                  │
│     │                      │─────────────────────────────►│                  │
│     │                      │                              │                  │
│     │  If REJECT:          │                              │                  │
│     │◄─────────────────────│ Return error + record        │                  │
│     │                      │                              │                  │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Policy Sources

| Source | Scope | Override Behavior |
|--------|-------|-------------------|
| **Tool Specification** | Per-tool defaults | Base policies |
| **Training Specification** | Per-agent type | Extends tool policies |
| **Employment Specification** | Per-deployment | **Overrides** training policies |

**Override Rule**: Employment Spec policies take precedence over Training Spec policies.

#### IAM Integration

Tool Gateway validates against the agent's delegated IAM role:

```yaml
# Employment Spec
spec:
  identity:
    iamRole: arn:olympus:iam::123456789:role/fraud-analyst-agent
    delegatedScopes:
      - read:accounts
      - read:transactions
      - write:case-notes
      # NOT: write:accounts (agent cannot modify accounts)
```

---

### 3. Signal Exchange

Signal Exchange enforces policies on **all agent updates** to the Request:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     SIGNAL EXCHANGE ENFORCEMENT                              │
│                                                                              │
│   Agent                Signal Exchange                  Request Store        │
│     │                      │                                │                │
│     │  REQUEST_UPDATE      │                                │                │
│     │  (decision, context) │                                │                │
│     │─────────────────────►│                                │                │
│     │                      │                                │                │
│     │                      │ ┌──────────────────────────┐   │                │
│     │                      │ │ OPA Policy Evaluation    │   │                │
│     │                      │ │                          │   │                │
│     │                      │ │ Can validate ANY update: │   │                │
│     │                      │ │ • Decision content       │   │                │
│     │                      │ │ • Memory records         │   │                │
│     │                      │ │ • Status changes         │   │                │
│     │                      │ │ • Escalation requests    │   │                │
│     │                      │ └──────────────────────────┘   │                │
│     │                      │                                │                │
│     │                      │ If ALLOW:                      │                │
│     │                      │ ──────────────────────────────►│ Store update   │
│     │                      │                                │                │
│     │                      │ If REJECT:                     │                │
│     │                      │ ──────────────────────────────►│ Store as       │
│     │                      │                                │ 'rejected'     │
│     │◄─────────────────────│ Return decision               │                │
│     │                      │                                │                │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Key Behaviors**:
- Any REQUEST_UPDATE can be subject to policy
- Rejected updates are **recorded** (not discarded) with status `rejected`
- Rejection reason and policy code included in record

---

## OPA Policy Model

### Policy Definition

Policies are defined in Training and Employment Specifications:

```yaml
# Training Specification
spec:
  authority:
    toolPolicies:
      - tool: refund.approve
        policy: |
          package seer.authority
          
          default decision = "REJECT"
          
          decision = "ALLOW" {
            input.parameters.amount <= 5000
            input.agent.scopes[_] == "write:refunds"
          }
          
          decision = "ALERT" {
            input.parameters.amount > 5000
            input.parameters.amount <= 10000
            input.agent.scopes[_] == "write:refunds"
          }
          
          reason = "Amount exceeds threshold" {
            input.parameters.amount > 5000
          }
        
        opaContextSchema:
          type: object
          properties:
            parameters:
              type: object
              properties:
                amount: { type: number }
                case_id: { type: string }
            agent:
              $ref: "#/definitions/AgentContext"
            request:
              $ref: "#/definitions/RequestContext"
```

### Employment Override

```yaml
# Employment Specification (overrides training)
spec:
  authority:
    toolPolicies:
      - tool: refund.approve
        policy: |
          package seer.authority
          
          # Stricter limits for this deployment
          default decision = "REJECT"
          
          decision = "ALLOW" {
            input.parameters.amount <= 2500  # Lower than training spec
            input.agent.scopes[_] == "write:refunds"
          }
```

### OPA Decision Format

```json
{
  "decision": "REJECT",        // ALLOW | ALERT | REJECT
  "reason_code": "THRESHOLD_EXCEEDED",
  "reason": "Refund amount $7,500 exceeds authorized limit of $5,000",
  "policy_id": "refund.approve.threshold",
  "evaluation_context": {
    "agent_id": "fraud-analyst-001",
    "tool": "refund.approve",
    "timestamp": "2026-01-08T14:30:00Z"
  }
}
```

### Decision Types

| Decision | Behavior | Recording |
|----------|----------|-----------|
| **ALLOW** | Action proceeds | Logged for audit |
| **ALERT** | Action proceeds, notification sent | Logged + Observation created |
| **REJECT** | Action blocked | Recorded as violation on Request |

---

## OPA Context Schema

Each enforcement point provides a **standardized context schema** for OPA evaluation:

### Common Context (All Enforcement Points)

```yaml
# Available at all enforcement points
AgentContext:
  type: object
  properties:
    agent_id:
      type: string
    training_spec:
      type: string
    employment_spec:
      type: string
    iam_role:
      type: string
    delegated_scopes:
      type: array
      items:
        type: string
    accountable_user:
      type: string
      description: IAM user or group accountable for this agent

AccessContext:
  type: object
  properties:
    tenant_id:
      type: string
    workbench_id:
      type: string
    scenario_id:
      type: string
    request_id:
      type: string
```

### Tool Gateway Context

```yaml
ToolGatewayContext:
  allOf:
    - $ref: "#/definitions/AgentContext"
    - $ref: "#/definitions/AccessContext"
    - type: object
      properties:
        tool:
          type: object
          properties:
            name:
              type: string
            version:
              type: string
        parameters:
          type: object
          description: Tool-specific parameters (schema from Tool Specification)
        invocation:
          type: object
          properties:
            timestamp:
              type: string
              format: date-time
            request_headers:
              type: object
              description: HTTP headers from invocation
```

### Signal Exchange Context

```yaml
SignalExchangeContext:
  allOf:
    - $ref: "#/definitions/AgentContext"
    - $ref: "#/definitions/AccessContext"
    - type: object
      properties:
        update:
          type: object
          properties:
            type:
              type: string
              enum: [DECISION, CONTEXT, STATUS, MEMORY_RECORD, ESCALATION]
            content:
              type: object
              description: Update-type-specific content
        request:
          type: object
          description: Current request state
```

---

## Violation Handling

### Recording

All violations are recorded on the Request:

```json
{
  "request_id": "req-12345",
  "violations": [
    {
      "id": "vio-001",
      "timestamp": "2026-01-08T14:30:00Z",
      "enforcement_point": "TOOL_GATEWAY",
      "decision": "REJECT",
      "reason_code": "THRESHOLD_EXCEEDED",
      "reason": "Refund amount $7,500 exceeds authorized limit of $5,000",
      "policy_id": "refund.approve.threshold",
      "agent_id": "fraud-analyst-001",
      "action_attempted": {
        "tool": "refund.approve",
        "parameters": {
          "amount": 7500,
          "case_id": "case-67890"
        }
      }
    }
  ]
}
```

### Notification

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      VIOLATION NOTIFICATION FLOW                             │
│                                                                              │
│                        Violation Recorded                                    │
│                              │                                               │
│              ┌───────────────┼───────────────┐                              │
│              ▼               ▼               ▼                              │
│   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐                   │
│   │  Observers   │   │ Accountable  │   │  Workbench   │                   │
│   │  (Agents)    │   │ Person (IAM) │   │ Observation  │                   │
│   │              │   │              │   │              │                   │
│   │ Receive      │   │ Email/Slack  │   │ Dashboard    │                   │
│   │ REQUEST_     │   │ notification │   │ entry with   │                   │
│   │ UPDATE with  │   │ with details │   │ violation    │                   │
│   │ violation    │   │              │   │ details      │                   │
│   └──────────────┘   └──────────────┘   └──────────────┘                   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Corrective Actions

| Context | Available Actions |
|---------|-------------------|
| **Agent on Task Queue** | Escalation, reassignment via task queue specification |
| **Automation Application** | Invoke different scenario, application-specific recourse |
| **Observer Agent** | Intervene, provide guidance, take over task |
| **Human Supervisor** | Manual intervention, policy adjustment |

---

## Compound Agents

For Raw Agents with internal sub-agents (not visible to Hub):

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         COMPOUND AGENT AUTHORITY                             │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    Raw Agent (Hub-visible)                           │   │
│   │                                                                       │   │
│   │   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐               │   │
│   │   │ Sub-Agent A │   │ Sub-Agent B │   │ Sub-Agent C │               │   │
│   │   │ (internal)  │   │ (internal)  │   │ (internal)  │               │   │
│   │   └─────────────┘   └─────────────┘   └─────────────┘               │   │
│   │                                                                       │   │
│   │   ← All sub-agents operate under outer agent's authority →           │   │
│   │                                                                       │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│   Enforcement scoped to outer agent only                                     │
│   Outer agent responsible for sub-agent compliance                           │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Key Points**:
- Hub enforcement points (Tool Gateway, Signal Exchange) see only the outer agent
- All actions from sub-agents are attributed to the outer agent
- Outer agent is responsible for ensuring sub-agent compliance
- Violations are recorded against the outer agent

---

## Integration with IAM

### Role Delegation

```yaml
# Employment Specification
spec:
  identity:
    # IAM role assumed by this agent
    iamRole: arn:olympus:iam::123456789:role/fraud-analyst-agent
    
    # Scopes delegated to this agent
    delegatedScopes:
      - read:accounts
      - read:transactions
      - write:case-notes
      - write:refunds:5000  # Amount limit encoded in scope
    
    # Accountable human (receives violation notifications)
    accountableUser: fraud-team@company.com  # IAM user or group
```

### Scope Validation

Tool Gateway validates delegated scopes:

```rego
# OPA policy for scope validation
package seer.authority.iam

default allow = false

allow {
  required_scope := tool_scope_requirement[input.tool.name]
  input.agent.delegated_scopes[_] == required_scope
}

# Tool-specific scope requirements
tool_scope_requirement["refund.approve"] = "write:refunds"
tool_scope_requirement["account.query"] = "read:accounts"
```

---

## Best Practices

### For Developers

1. **Define clear authority boundaries** in Training Spec
2. **Use ALERT for soft limits** — allows action but notifies
3. **Test policies** with edge cases before deployment
4. **Document policy intent** in human-readable reason messages

### For Tenant Admins

1. **Review Employment overrides** — ensure they don't weaken security
2. **Monitor violation patterns** — frequent violations indicate training issues
3. **Set appropriate accountable users** — ensure notifications reach the right people
4. **Audit OPA policies** — regularly review for completeness

### For Domain Stewards

1. **Align policies with SOPs** — authority limits should reflect business rules
2. **Define escalation thresholds** — when should agents escalate vs. decide?
3. **Review violation reports** — identify systemic issues

---

## Observability

### Metrics

| Metric | Description |
|--------|-------------|
| `authority.evaluations.total` | Total policy evaluations |
| `authority.evaluations.by_decision` | Breakdown by ALLOW/ALERT/REJECT |
| `authority.violations.by_policy` | Violations per policy |
| `authority.violations.by_agent` | Violations per agent |

### Dashboards

Workbench Observations provide:
- Violation timeline
- Top violating agents
- Policy effectiveness (false positive rate)
- Trend analysis

---

## Related Documentation

- [Guardrails](./guardrails.md) — Tenant-defined enforcement
- [Agent Identity & Authority Framework](./agent-identity-authority.md) — IAM integration
- [Hub Registry Services](../../../olympus-hub-docs/04-subsystems/registry-services/README.md) — Tool specifications
- [Employment Spec CRD](../hub-integration/employment-spec-crd.md) — Authority configuration
- [Signal Exchange](../../../olympus-hub-docs/04-subsystems/signal-exchange/README.md) — Update policies
- [ADR-0073: Authority Enforcement via OPA](../../../olympus-hub-docs/decision-logs/0073-seer-authority-enforcement-opa.md)

---

*Authority enforcement provides layered protection with OPA policies at Tool Gateway and Signal Exchange, ensuring agents operate within delegated limits.*

