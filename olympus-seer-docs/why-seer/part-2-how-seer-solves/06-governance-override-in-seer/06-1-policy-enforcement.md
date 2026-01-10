# 6.1 Policy Enforcement

Policy enforcement is the mechanism by which Seer ensures agent behavior complies with organizational rules, regulatory requirements, and delegated authority boundaries. Unlike advisory guidance, policy enforcement is binding—actions that violate policy are blocked.

## What Policy Enforcement Covers

| Policy Type | What It Governs | Example |
|-------------|-----------------|---------|
| **Authority policies** | What agent can decide/act on | Max refund amount |
| **Access policies** | What agent can access | Customer data, tools |
| **Content policies** | What agent can say/produce | PII handling, tone |
| **Behavioral policies** | How agent should behave | Escalation triggers |

## Policy Enforcement Architecture

```
┌─────────────────────────────────────────────────────────────┐
│               POLICY ENFORCEMENT ARCHITECTURE                │
│                                                              │
│   ┌───────────────────────────────────────────────────┐    │
│   │                 POLICY ENGINE                      │    │
│   │                                                    │    │
│   │   Policy Store → Policy Evaluation → Decision      │    │
│   │                                                    │    │
│   └────────────────────────┬──────────────────────────┘    │
│                            │                                │
│   ┌────────────────────────▼──────────────────────────┐    │
│   │            POLICY ENFORCEMENT POINTS               │    │
│   │                                                    │    │
│   │   ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐    │    │
│   │   │Context │ │ Tool   │ │ Model  │ │Output  │    │    │
│   │   │Assembly│ │Invoke  │ │Request │ │Delivery│    │    │
│   │   │  PEP   │ │  PEP   │ │  PEP   │ │  PEP   │    │    │
│   │   └────────┘ └────────┘ └────────┘ └────────┘    │    │
│   └───────────────────────────────────────────────────┘    │
│                                                              │
│   ┌───────────────────────────────────────────────────┐    │
│   │                 AUDIT LOGGING                      │    │
│   │   All policy decisions logged to CAF               │    │
│   └───────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## Policy Store

Policies are defined declaratively and stored centrally:

```yaml
policy:
  name: dispute-analyst-authority
  applies_to:
    agent_class: dispute-analyst
    workbench: dispute-ops-prod
    
  rules:
    - name: max-refund-limit
      type: authority_ceiling
      condition: action.type == "refund"
      constraint: action.amount <= 500
      on_violation: deny
      
    - name: require-human-for-complex
      type: escalation
      condition: case.complexity == "high"
      action: require_human_approval
      
    - name: no-pii-in-response
      type: content
      condition: output.contains_pii == true
      action: redact_and_warn
```

## Policy Evaluation

At each enforcement point, policies are evaluated:

```python
def evaluate_policy(action, context, policies):
    applicable = filter_applicable(policies, action, context)
    
    for policy in applicable:
        result = policy.evaluate(action, context)
        
        if result.decision == "deny":
            log_to_caf(policy, action, "denied")
            return PolicyDenied(policy, result.reason)
            
        if result.decision == "require_approval":
            log_to_caf(policy, action, "approval_required")
            return ApprovalRequired(policy, result.approvers)
            
    log_to_caf(policies, action, "allowed")
    return PolicyAllowed()
```

## Policy Enforcement Points (PEPs)

### Context Assembly PEP

Controls what information enters context:

```yaml
context_pep:
  checks:
    - no_unauthorized_data_access
    - no_cross_tenant_data
    - no_pii_in_constraint_sections
    
  on_violation:
    action: exclude_item
    log: caf
    alert: optional
```

### Tool Invocation PEP

Controls which tools can be called:

```yaml
tool_pep:
  checks:
    - tool_in_agent_allowlist
    - parameters_within_limits
    - rate_limits_not_exceeded
    
  on_violation:
    action: block_invocation
    log: caf
    return_error: "Tool access denied"
```

### Model Request PEP

Controls model access:

```yaml
model_pep:
  checks:
    - agent_authorized_for_model
    - budget_not_exceeded
    - prompt_within_length_limits
    
  on_violation:
    action: block_or_downgrade
    log: caf
```

### Output Delivery PEP

Controls what goes to end users:

```yaml
output_pep:
  checks:
    - no_pii_exposed
    - no_prohibited_content
    - required_disclosures_present
    
  on_violation:
    action: redact_or_block
    log: caf
```

## Policy Decision Audit

All policy evaluations are logged:

```yaml
policy_audit:
  timestamp: 2026-01-10T14:30:00Z
  agent: dispute-analyst-tier1
  action: execute-refund
  
  policies_evaluated:
    - policy: max-refund-limit
      result: allow
      reason: "Amount $450 <= limit $500"
      
    - policy: require-human-for-complex
      result: not_applicable
      reason: "Case complexity: normal"
      
  final_decision: allow
  logged_to: caf
```

## Policy Versioning

Policies are versioned for audit reconstruction:

```yaml
policy_version:
  policy: dispute-analyst-authority
  version: 2.3
  effective_from: 2026-01-01
  effective_to: null  # Current
  
  changes_from_previous:
    - rule: max-refund-limit
      old_value: 300
      new_value: 500
      approved_by: policy-committee
      approval_date: 2025-12-15
```

When reconstructing past decisions:

```python
# What policies applied when this decision was made?
applicable_policies = policy_store.get_at(
    decision_timestamp="2025-12-15T10:00:00Z"
)
```

## Policy Conflicts

When policies conflict, precedence rules apply:

```
1. Deny always wins over Allow
2. More specific policy wins over general
3. Newer policy wins when same specificity
4. Training spec wins over employment spec for guardrails
```

---

**References:**
*   `olympus-seer-docs/seer-design/subsystems/authority-enforcement.md`
*   `olympus-seer-docs/why-seer/part-1-background/05-building-enterprise-agent/05-2-immutability-principle.md`
