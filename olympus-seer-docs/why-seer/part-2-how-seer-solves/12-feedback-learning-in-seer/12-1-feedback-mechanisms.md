# 12.1 Feedback Mechanisms

Seer captures feedback through multiple channels: explicit signals from users, implicit signals from behavior, and outcome signals from results. This feedback forms the raw material for learning.

## Feedback Types

| Type | Source | Signal Quality | Examples |
|------|--------|----------------|----------|
| **Explicit** | Direct human input | High | Ratings, corrections, approvals |
| **Implicit** | Observed behavior | Medium | Override rate, escalation patterns |
| **Outcome** | Business results | High | Decision accuracy, case outcomes |

## Explicit Feedback

Direct feedback from humans:

### Ratings

```yaml
rating_feedback:
  request_id: req-abc123
  timestamp: 2026-01-10T15:00:00Z
  
  from:
    principal: analyst@acme.com
    role: dispute_analyst
    
  rating:
    type: quality
    value: 4  # out of 5
    
  context:
    agent: dispute-analyst-tier1
    task: refund_decision
```

### Corrections

```yaml
correction_feedback:
  request_id: req-abc123
  timestamp: 2026-01-10T15:00:00Z
  
  from:
    principal: analyst@acme.com
    
  correction:
    type: decision_override
    original: approve_refund_$450
    corrected: approve_refund_$300
    reason: "Partial refund per policy section 4.3"
    
  learning_signal:
    pattern: "When condition X, use partial refund"
    confidence: high
```

### Textual Feedback

```yaml
textual_feedback:
  request_id: req-abc123
  timestamp: 2026-01-10T15:00:00Z
  
  from:
    principal: analyst@acme.com
    
  comment: "Good analysis, but explanation was too technical for customer"
  
  tags: [explanation_style, customer_communication]
```

## Implicit Feedback

Signals derived from observed behavior:

### Override Patterns

```yaml
implicit_signal:
  type: override_pattern
  
  observation:
    agent: dispute-analyst-tier1
    period: last_7_days
    
  pattern:
    - 15% of decisions were overridden
    - 80% of overrides were for "high_value_customer" cases
    
  interpretation:
    - agent_may_underweight_customer_tier
    - potential_knowledge_gap: high_value_customer_handling
```

### Escalation Patterns

```yaml
implicit_signal:
  type: escalation_pattern
  
  observation:
    agent: fraud-detector-v2
    period: last_30_days
    
  pattern:
    - escalation_rate: 25%
    - common_trigger: "multiple_geographic_locations"
    
  interpretation:
    - agent_may_be_over_cautious_on_travel_patterns
```

### Retry Patterns

```yaml
implicit_signal:
  type: retry_pattern
  
  observation:
    agent: dispute-analyst-tier1
    
  pattern:
    - tool: "get_merchant_details"
    - retry_rate: 40%
    - common_error: "timeout"
    
  interpretation:
    - tool_reliability_issue
    - or: agent_calling_with_invalid_parameters
```

## Outcome Feedback

Signals from business results:

### Decision Accuracy

```yaml
outcome_signal:
  type: decision_accuracy
  
  measurement:
    period: last_30_days
    agent: dispute-analyst-tier1
    
  outcomes:
    - decisions_made: 1247
    - subsequently_reversed: 23
    - customer_appealed: 45
    - appeal_successful: 12
    
  accuracy_rate: 98.2%
```

### Business Metrics

```yaml
outcome_signal:
  type: business_metrics
  
  measurement:
    agent: dispute-analyst-tier1
    
  metrics:
    - customer_satisfaction: 4.2/5.0
    - resolution_time: 2.3 hours (avg)
    - cost_per_case: $12.50
    - escalation_rate: 15%
```

## Feedback Aggregation

Feedback is aggregated for pattern detection:

```yaml
feedback_aggregation:
  agent: dispute-analyst-tier1
  period: last_30_days
  
  explicit:
    ratings: 4.1/5.0 (n=234)
    corrections: 47
    comments: 89
    
  implicit:
    override_rate: 12%
    escalation_rate: 15%
    retry_rate: 8%
    
  outcome:
    accuracy: 98.2%
    satisfaction: 4.2/5.0
    
  synthesis:
    - strength: high_accuracy
    - improvement_area: explanation_style
    - watch: override_rate_on_premium_customers
```

---

**References:**
*   `olympus-seer-docs/why-seer/part-1-background/05-building-enterprise-agent/05-10-feedback-learning-requirements.md`
*   `olympus-hub-docs/04-subsystems/cognitive-audit-fabric/enterprise-learning-services.md`

