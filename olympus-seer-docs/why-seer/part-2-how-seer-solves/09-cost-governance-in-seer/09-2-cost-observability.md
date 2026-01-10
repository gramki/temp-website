# 9.2 Cost Observability

Seer provides comprehensive visibility into agent costs—where money is spent, by whom, and why. This enables optimization, accountability, and anomaly detection.

## What's Tracked

### Per-Request Costs

Every agent request records:

```yaml
request_cost:
  request_id: req-abc123
  timestamp: 2026-01-10T14:30:00Z
  
  model_costs:
    - call: 1
      model: claude-3.5-sonnet
      prompt_tokens: 1234
      completion_tokens: 567
      cost: 0.0122
      
    - call: 2
      model: claude-3.5-sonnet
      prompt_tokens: 890
      completion_tokens: 234
      cost: 0.0062
      
  tool_costs:
    - tool: get_transaction_details
      cost: 0.001
      
    - tool: check_fraud_score
      cost: 0.01
      
  total_cost: 0.0294
```

### Attribution

Costs attributed across dimensions:

```yaml
attribution:
  organizational:
    tenant: acme
    business_unit: operations
    cost_center: CC-12345
    
  technical:
    workbench: dispute-ops-prod
    agent: dispute-analyst-tier1
    agent_version: 2.1.0
    
  operational:
    scenario: dispute_resolution
    case_id: case-12345
    request_type: decision
```

## Cost Metrics

### Real-Time Metrics

```yaml
real_time_metrics:
  current:
    - cost_per_minute
    - cost_per_hour_projected
    - requests_per_minute
    - average_cost_per_request
    
  trending:
    - cost_vs_yesterday
    - cost_vs_last_week
    - cost_vs_baseline
    
  budgets:
    - utilization_by_agent
    - utilization_by_workbench
    - utilization_by_tenant
```

### Aggregated Metrics

```yaml
aggregated_metrics:
  daily:
    - total_cost
    - cost_by_model
    - cost_by_agent
    - cost_by_workbench
    - cost_per_decision
    - cost_per_successful_outcome
    
  monthly:
    - total_cost
    - cost_trend
    - efficiency_trend
    - budget_performance
```

## Cost Dashboard

### Operator View

```yaml
operator_dashboard:
  panels:
    - name: Current Spend
      type: gauge
      metrics: [hourly_cost, daily_cost, monthly_projection]
      thresholds: [warning, critical]
      
    - name: Budget Status
      type: bar_chart
      metrics: [budget_by_level, remaining_by_level]
      
    - name: Cost Trend
      type: line_chart
      metrics: [cost_per_hour, 7_day_trend]
      
    - name: Top Consumers
      type: table
      metrics: [agent_cost_ranking, workbench_cost_ranking]
      
    - name: Anomalies
      type: alert_list
      metrics: [cost_spikes, budget_warnings]
```

### Business View

```yaml
business_dashboard:
  panels:
    - name: Monthly Cost Summary
      type: summary
      metrics: [total_cost, vs_budget, vs_last_month]
      
    - name: Cost by Business Unit
      type: pie_chart
      metrics: [cost_by_cost_center]
      
    - name: Cost per Transaction
      type: metric
      metrics: [average_cost_per_decision, trend]
      
    - name: ROI Indicators
      type: table
      metrics: [cost_per_outcome, value_generated]
```

## Cost Reports

### Automated Reports

```yaml
automated_reports:
  daily:
    recipients: [agent_operators]
    content: [summary, anomalies, top_consumers]
    
  weekly:
    recipients: [are_team, business_owners]
    content: [trends, budget_status, optimization_recommendations]
    
  monthly:
    recipients: [finance, business_owners]
    content: [full_breakdown, chargeback, projections]
```

### On-Demand Analysis

```yaml
analysis_queries:
  - "Cost by agent for last 7 days"
  - "Cost breakdown for case-12345"
  - "Highest cost requests today"
  - "Cost trend for dispute-analyst agents"
  - "Token efficiency by model"
```

## Anomaly Detection

### Baseline Learning

```yaml
baseline:
  learning_period: 14_days
  metrics:
    - cost_per_request_by_agent
    - cost_per_hour_by_workbench
    - token_per_request_by_task_type
    
  update: daily_rolling
```

### Anomaly Identification

```yaml
anomaly_detection:
  methods:
    - z_score: threshold > 3
    - percent_change: threshold > 100%
    - rate_change: threshold > 5x
    
  alert_on:
    - single_request_anomaly
    - agent_hourly_anomaly
    - workbench_daily_anomaly
```

---

**References:**
*   `olympus-seer-docs/seer-design/subsystems/model-gateway.md`
*   `olympus-seer-docs/why-seer/part-2-how-seer-solves/07-runtime-observability-in-seer/07-3-observability.md`

