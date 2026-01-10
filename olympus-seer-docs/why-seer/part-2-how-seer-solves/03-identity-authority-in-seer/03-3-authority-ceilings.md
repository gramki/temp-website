# 3.3 Authority Ceilings

Authority ceilings are hard limits that constrain what an agent can do, regardless of what authority has been delegated. Seer implements layered authority ceilings that are enforced at runtime.

## Why Ceilings, Not Just Permissions

Permissions define what an agent *may* do. Ceilings define what an agent *can never exceed*. The distinction matters:

| Concept | Definition | Enforcement |
|---------|------------|-------------|
| **Permission** | Granted capability | Can be delegated, expanded |
| **Ceiling** | Absolute limit | Cannot be exceeded by any delegation |

An agent may have permission to approve refunds, but a ceiling of $500 per refund. Even if a supervisor delegates unlimited refund authority, the ceiling holds.

## Ceiling Layers

Seer implements ceilings at multiple layers, with each layer constraining those below:

```
Bank/Org Policy (highest authority)
    ↓ constrains
Agent Class Ceiling (Training Spec)
    ↓ constrains
Agent Instance Ceiling (Employment Spec)
    ↓ constrains
Request Context Ceiling (runtime)
```

### Bank/Organization Policy

The highest-level ceilings set by organizational policy:

```yaml
# Organization-wide agent policy
agentPolicy:
  ceilings:
    maxSingleTransaction: 100000
    maxDailyVolume: 1000000
    requiresHumanApproval:
      - action: account-closure
      - action: regulatory-filing
    prohibitedActions:
      - trading-on-own-account
      - customer-data-export
```

No agent can exceed these limits, regardless of training or employment.

### Agent Class Ceiling (Training Spec)

The Training Specification sets ceilings for a class of agents:

```yaml
# Training Spec
spec:
  ceilings:
    maxDecisionValue: 10000
    maxConcurrentCases: 50
    requiresApproval:
      - refund: "> 1000"
```

These ceilings apply to all Employed Agents using this Training Spec.

### Agent Instance Ceiling (Employment Spec)

The Employment Specification can further restrict (never expand):

```yaml
# Employment Spec
spec:
  authority:
    ceilings:
      maxDecisionValue: 5000  # ≤ Training ceiling of 10000
      dailyBudget: 500
```

### Request Context Ceiling

Runtime context can apply additional limits:

- Time-of-day restrictions
- Current risk level adjustments
- Workload-based throttling

## Ceiling Types

### Value Ceilings

Limits on monetary or quantitative values:

```yaml
ceilings:
  value:
    maxSingleTransaction: 5000
    maxDailyTotal: 50000
    maxPerCustomer: 10000
```

### Rate Ceilings

Limits on frequency and volume:

```yaml
ceilings:
  rate:
    maxRequestsPerMinute: 100
    maxDecisionsPerHour: 500
    maxActionsPerDay: 2000
```

### Scope Ceilings

Limits on what the agent can access:

```yaml
ceilings:
  scope:
    customerTiers: [standard, premium]  # not enterprise
    dataClasses: [public, internal]      # not confidential
    regions: [us, eu]                    # not apac
```

### Approval Ceilings

Actions that require human approval above threshold:

```yaml
ceilings:
  approval:
    refund:
      threshold: 500
      approver: supervisor
    accountChange:
      always: true
      approver: compliance
```

## Runtime Enforcement

### Policy Enforcement Points (PEPs)

Ceilings are enforced by PEPs at every action:

```
Agent requests action (refund $750)
    ↓
PEP evaluates ceilings:
  - Org policy: max $100,000 ✓
  - Training: max $10,000 ✓
  - Employment: max $5,000 ✓
  - Employment: approval required > $500 → REQUIRES APPROVAL
    ↓
Action routed to approval queue
```

### OPA Policies

Ceiling enforcement uses Open Policy Agent (OPA):

```rego
package seer.authority

# Deny if exceeds ceiling
deny[msg] {
    input.action == "refund"
    input.amount > data.ceilings.training.maxDecisionValue
    msg := sprintf("Refund amount %v exceeds training ceiling %v", 
                   [input.amount, data.ceilings.training.maxDecisionValue])
}

# Require approval if above threshold
requires_approval {
    input.action == "refund"
    input.amount > data.ceilings.employment.approvalThreshold
}
```

### Audit

All ceiling evaluations are logged:

```json
{
  "event": "ceiling_evaluation",
  "agent": "dispute-analyst-bot",
  "action": "refund",
  "amount": 750,
  "ceilings_checked": [
    {"layer": "org", "limit": 100000, "result": "pass"},
    {"layer": "training", "limit": 10000, "result": "pass"},
    {"layer": "employment", "limit": 5000, "result": "pass"},
    {"layer": "employment_approval", "threshold": 500, "result": "approval_required"}
  ],
  "outcome": "routed_to_approval"
}
```

## Ceiling Governance

### Definition Authority

Different roles define ceilings at different layers:

| Layer | Defined By | Change Process |
|-------|------------|----------------|
| **Organization** | Risk/Compliance | Policy change review |
| **Training** | Domain Lead + Security | Training Spec update |
| **Employment** | Deployer + Manager | Employment Spec update |
| **Runtime** | System (contextual) | Automatic |

### Change Control

Ceiling changes require appropriate approval:

- Org-level: Compliance sign-off
- Training: Security review
- Employment: Manager approval

Ceiling expansions are logged and auditable.

---

**References:**
*   `olympus-seer-docs/seer-design/subsystems/authority-enforcement.md`
*   `aosm-meta-model/raw-trained-employed-agents.md`
