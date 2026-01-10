# 8.4 Cost Integration

The Model Gateway is tightly integrated with Seer's cost governance. Every token is tracked, attributed, and subject to budget enforcement.

## Token Tracking

### Per-Request Tracking

Every request records token usage:

```yaml
usage_record:
  request_id: req-abc123
  timestamp: 2026-01-10T14:30:00Z
  
  tokens:
    prompt: 1234
    completion: 567
    total: 1801
    
  cost:
    prompt_cost: 0.0037
    completion_cost: 0.0085
    total_cost: 0.0122
    currency: USD
    
  attribution:
    tenant: acme
    workbench: dispute-ops-prod
    agent: dispute-analyst-tier1
    request_type: decision
    case_id: case-12345
```

### Cost Calculation

Costs calculated using current pricing:

```yaml
pricing_config:
  claude-3.5-sonnet:
    input_per_1k: 0.003
    output_per_1k: 0.015
    effective_from: 2025-01-01
    
  gpt-4o:
    input_per_1k: 0.005
    output_per_1k: 0.015
    effective_from: 2025-01-01
    
  gpt-4o-mini:
    input_per_1k: 0.00015
    output_per_1k: 0.0006
    effective_from: 2025-01-01
```

## Budget Enforcement

### Pre-Request Check

Before routing, verify budget:

```python
def check_budget(request, agent):
    estimated_cost = estimate_cost(request)
    
    # Check agent budget
    if agent.spent_today + estimated_cost > agent.daily_budget:
        return BudgetExceeded("Agent daily budget exceeded")
        
    # Check workbench budget
    if workbench.spent_today + estimated_cost > workbench.daily_budget:
        return BudgetExceeded("Workbench daily budget exceeded")
        
    return BudgetOK()
```

### Budget Hierarchy

```yaml
budget_hierarchy:
  tenant:
    daily: 10000
    monthly: 200000
    
  workbench:
    daily: 1000
    monthly: 20000
    
  agent:
    daily: 100
    per_request: 10
```

### Budget Actions

When budget is exceeded:

```yaml
budget_actions:
  soft_limit:
    threshold: 80%
    action: alert
    
  hard_limit:
    threshold: 100%
    action: block_new_requests
    fallback: cheaper_model (if configured)
    
  emergency:
    threshold: 150%  # Exceeded due to in-flight
    action: alert_critical
```

## Cost Attribution

### Granular Attribution

Costs attributed at multiple levels:

```yaml
attribution_dimensions:
  organizational:
    - tenant
    - business_unit
    - cost_center
    
  technical:
    - workbench
    - agent
    - model
    
  operational:
    - request_type
    - case_id
    - scenario
```

### Attribution Report

```yaml
cost_report:
  period: 2026-01-10
  
  by_tenant:
    acme:
      total: 1234.56
      workbenches:
        dispute-ops: 567.89
        fraud-detection: 666.67
        
  by_model:
    claude-3.5-sonnet: 890.12
    gpt-4o: 234.56
    gpt-4o-mini: 109.88
    
  by_agent:
    dispute-analyst-tier1: 234.56
    fraud-detector-v2: 456.78
```

## Cost Observability

### Real-Time Metrics

```yaml
cost_metrics:
  real_time:
    - cost_per_minute
    - cost_per_hour_projected
    - budget_utilization
    
  alerts:
    - budget_80_percent
    - budget_exceeded
    - cost_spike (anomaly)
```

### Cost Dashboard

```yaml
cost_dashboard:
  panels:
    - name: Cost Trend
      metrics: [hourly_cost, daily_cost, monthly_projection]
      
    - name: Budget Status
      metrics: [budget_by_level, utilization_percentage]
      
    - name: Cost by Model
      metrics: [model_cost_breakdown, model_efficiency]
      
    - name: Cost by Agent
      metrics: [agent_cost_breakdown, cost_per_decision]
      
    - name: Anomalies
      metrics: [cost_spikes, unusual_patterns]
```

## Cost Optimization

### Recommendations

Gateway provides optimization suggestions:

```yaml
optimization_recommendations:
  - agent: dispute-analyst-tier1
    current_model: claude-3.5-sonnet
    recommendation: gpt-4o-mini for classification tasks
    estimated_savings: 40%
    quality_impact: minimal for this task type
    
  - agent: fraud-detector-v2
    issue: excessive_retries
    recommendation: improve prompt to reduce retries
    estimated_savings: 25%
```

### Automatic Optimization

Optional automatic cost optimization:

```yaml
auto_optimization:
  enabled: true
  
  strategies:
    - name: downgrade_simple_tasks
      condition: task_type == "classification"
      action: use_cheaper_model
      
    - name: cache_common_responses
      condition: response_cacheable
      action: use_cached
```

---

**References:**
*   `olympus-seer-docs/seer-design/subsystems/model-gateway.md`
*   `olympus-seer-docs/why-seer/part-2-how-seer-solves/09-cost-governance-in-seer/_section-overview.md`

