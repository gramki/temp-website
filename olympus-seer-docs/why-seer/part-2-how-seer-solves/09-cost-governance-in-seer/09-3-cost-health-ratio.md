# 9.3 Cost-to-Health Ratio

Cost in isolation is incomplete. An agent that's cheap but wrong is worse than one that's expensive but correct. The Cost-to-Health Ratio (CHR) provides a balanced view of operational efficiency.

## What CHR Measures

```
CHR = Total Operational Cost / Agent Health Score (AHS)
```

Where:
- **Cost**: All operational expenses (model, tools, infrastructure)
- **AHS**: Composite score of accuracy, success rate, compliance, satisfaction

## Agent Health Score (AHS)

AHS is a composite metric (0.0 to 1.0):

```yaml
agent_health_score:
  components:
    accuracy:
      weight: 0.30
      source: outcome_feedback
      definition: "Decisions later validated as correct"
      
    success_rate:
      weight: 0.25
      source: completion_metrics
      definition: "Requests completed without error/escalation"
      
    compliance:
      weight: 0.25
      source: policy_enforcement
      definition: "Actions compliant with policy"
      
    user_satisfaction:
      weight: 0.20
      source: explicit_feedback
      definition: "User ratings and override rate"
```

## Interpreting CHR

| CHR Pattern | Meaning | Action |
|-------------|---------|--------|
| **Low CHR, High AHS** | Efficient and effective | Maintain, replicate |
| **High CHR, High AHS** | Expensive but effective | Optimize cost |
| **Low CHR, Low AHS** | Cheap failures | Fix quality first |
| **High CHR, Low AHS** | Crisis | Immediate intervention |
| **Rising CHR, Stable AHS** | Efficiency declining | Investigate cost drivers |
| **Falling CHR, Stable AHS** | Efficiency improving | Continue optimizing |

## CHR in Practice

### Agent Comparison

```yaml
agent_chr_comparison:
  agent_a:
    daily_cost: 100
    ahs: 0.90
    chr: 111.11
    assessment: "Efficient and effective"
    
  agent_b:
    daily_cost: 50
    ahs: 0.60
    chr: 83.33
    assessment: "Cheap but low quality - misleading efficiency"
    
  agent_c:
    daily_cost: 150
    ahs: 0.95
    chr: 157.89
    assessment: "Higher cost but best quality"
```

### CHR Trend Analysis

```yaml
chr_trend:
  agent: dispute-analyst-tier1
  period: 30_days
  
  data_points:
    - week_1: {cost: 700, ahs: 0.85, chr: 823}
    - week_2: {cost: 750, ahs: 0.87, chr: 862}
    - week_3: {cost: 720, ahs: 0.88, chr: 818}
    - week_4: {cost: 680, ahs: 0.90, chr: 756}
    
  trend: improving (CHR decreasing, AHS increasing)
  
  interpretation: "Quality improvements reducing rework costs"
```

## Using CHR for Decisions

### Model Selection

```yaml
model_selection_by_chr:
  options:
    - model: claude-3.5-sonnet
      estimated_cost: 0.05
      estimated_ahs: 0.92
      estimated_chr: 0.054
      
    - model: gpt-4o-mini
      estimated_cost: 0.01
      estimated_ahs: 0.75
      estimated_chr: 0.013
      
  decision:
    if: task_requires_high_accuracy
    then: claude-3.5-sonnet (lower CHR despite higher cost)
    else: evaluate based on task requirements
```

### Optimization Targets

```yaml
chr_optimization:
  current_chr: 125
  target_chr: 100
  
  strategies:
    reduce_cost:
      - use_cheaper_models_for_simple_tasks
      - improve_prompt_efficiency
      - reduce_retries
      estimated_impact: -15%
      
    improve_health:
      - better_training_data
      - refined_guardrails
      - reduced_error_rate
      estimated_impact: +10%
```

## CHR Dashboard

```yaml
chr_dashboard:
  panels:
    - name: CHR Overview
      type: gauge
      metrics: [current_chr, trend, target]
      
    - name: CHR by Agent
      type: scatter_plot
      x: cost
      y: ahs
      size: request_volume
      
    - name: CHR Trend
      type: line_chart
      metrics: [chr_over_time, cost_over_time, ahs_over_time]
      
    - name: CHR Analysis
      type: table
      metrics: [agents_sorted_by_chr, improvement_recommendations]
```

## Key Insight

> **Minimizing cost without considering health leads to cheap failures. Optimizing CHR leads to efficient quality.**

The goal is not lowest cost—it's lowest cost *per unit of value delivered*.

---

**References:**
*   `olympus-seer-docs/why-seer/part-1-background/05-building-enterprise-agent/05-11-cost-requirements.md`
*   `olympus-seer-docs/why-seer/part-2-how-seer-solves/07-runtime-observability-in-seer/07-3-observability.md`

