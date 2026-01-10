# 7.6 Directability: Rejection-Based Steering

Directability in enterprise agents works through rejection rather than direct command. Humans steer agent behavior by rejecting proposals, providing feedback, and setting boundaries—not by micromanaging every decision.

## Why Rejection-Based

| Approach | Problem | Alternative |
|----------|---------|-------------|
| **Direct command** | Defeats purpose of agent | Rejection-based |
| **No steering** | Loss of control | Human-in-loop |
| **Constant approval** | Bottleneck | Exception-based |

Rejection-based steering enables:
- Agents operate autonomously within bounds
- Humans intervene when needed
- Control without micromanagement

## Rejection Mechanisms

### Policy Rejection

System rejects actions that violate policy:

```yaml
policy_rejection:
  agent_proposes:
    action: approve_refund
    amount: 750
    
  policy_rejects:
    reason: "Exceeds authority ceiling ($500)"
    
  agent_responds:
    - acknowledge_rejection
    - options:
        - escalate_to_human
        - propose_partial_refund (450)
        - explain_limitation_to_user
```

### Human Rejection

Human rejects agent proposal:

```yaml
human_rejection:
  agent_proposes:
    action: approve_refund
    amount: 450
    rationale: "Merchant error confirmed"
    
  human_rejects:
    reason: "Customer has pending chargeback"
    instruction: "Deny refund, explain chargeback process"
    
  agent_responds:
    - acknowledge_rejection
    - follow_instruction
    - record_override
```

### Guardrail Rejection

Guardrail blocks output:

```yaml
guardrail_rejection:
  agent_produces:
    response: "Your SSN 123-45-6789 is on file..."
    
  guardrail_rejects:
    reason: "PII detected in response"
    
  agent_responds:
    - regenerate_response
    - without_pii
    - log_guardrail_trigger
```

## Steering Through Feedback

### Explicit Feedback

Human provides direct feedback:

```yaml
explicit_feedback:
  on_decision: dr-abc123
  
  feedback:
    type: correction
    content: "Decision was correct, but explanation was too technical"
    
  agent_learning:
    - adjust_explanation_style
    - for_similar_contexts
    - within_session (immediate)
    - promotion_candidate (if pattern)
```

### Implicit Feedback

System detects signals:

```yaml
implicit_feedback:
  signals:
    - human_override_rate: high
    - escalation_rate: increasing
    - retry_after_rejection: frequent
    
  interpretation:
    - agent_proposals_misaligned
    - possible_causes: [policy_gap, context_insufficient, model_drift]
    
  action:
    - alert_operators
    - trigger_review
```

## Escalation as Steering

Escalation is a form of directability:

```yaml
escalation_steering:
  agent_recognizes:
    - low_confidence
    - complex_situation
    - policy_ambiguity
    
  agent_escalates:
    reason: "Multiple valid interpretations"
    options_presented: [A, B, C]
    recommendation: B
    
  human_directs:
    selection: C
    additional_guidance: "Always prefer customer benefit when ambiguous"
    
  agent_incorporates:
    - follow_selection
    - record_guidance
    - apply_to_similar (within session)
```

## Preference Tuning

Users can tune agent behavior:

```yaml
preference_tuning:
  user_prefers:
    communication_style: concise
    response_format: bullet_points
    escalation_threshold: conservative
    
  agent_adapts:
    - shorter_responses
    - structured_format
    - escalate_earlier
    
  boundaries:
    - preferences_cannot_override_policy
    - preferences_cannot_relax_guardrails
    - preferences_scoped_to_session
```

## Directability Audit

All steering events are logged:

```yaml
steering_audit:
  event: human_rejection
  timestamp: 2026-01-10T14:30:00Z
  
  proposal:
    action: approve_refund
    amount: 450
    
  rejection:
    by: manager@acme.com
    reason: "Customer has pending chargeback"
    instruction: "Deny refund"
    
  agent_response:
    action: deny_refund
    followed_instruction: true
    
  learning:
    - recorded_override
    - pattern: "chargeback → deny refund"
    - promotion_candidate: yes
```

## Directability Metrics

```yaml
directability_metrics:
  steering_effectiveness:
    - rejection_followed_rate
    - instruction_compliance_rate
    - preference_application_rate
    
  steering_patterns:
    - common_rejection_reasons
    - common_escalation_triggers
    - preference_distribution
    
  learning_velocity:
    - override_reduction_over_time
    - same_mistake_repeat_rate
```

---

**References:**
*   `olympus-seer-docs/why-seer/part-2-how-seer-solves/06-governance-override-in-seer/06-3-human-override.md`
*   `aosm-meta-model/human-ai-team.md`
