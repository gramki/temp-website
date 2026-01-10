# 8.3 Intelligent Routing

Bifrost can route requests to different models based on task characteristics, cost constraints, latency requirements, and other factors. This enables optimization without changing agent code.

## Routing Dimensions

| Dimension | Optimization | Example |
|-----------|--------------|---------|
| **Task type** | Capability matching | Complex reasoning → large model |
| **Cost** | Cost optimization | Simple query → cheaper model |
| **Latency** | Speed optimization | Interactive → faster model |
| **Load** | Availability | Overloaded → alternative |

## Task-Based Routing

Route based on task complexity:

```yaml
task_routing:
  rules:
    - name: complex_reasoning
      condition:
        task_type: decision
        complexity: high
      route_to: claude-3.5-sonnet
      
    - name: simple_classification
      condition:
        task_type: classification
      route_to: gpt-4o-mini
      
    - name: summarization
      condition:
        task_type: summarization
      route_to: claude-3-haiku
      
    - name: default
      route_to: gpt-4o
```

### Task Detection

Tasks can be explicitly labeled or inferred:

```python
# Explicit task labeling
response = await gateway.chat_completion(
    model="auto",
    messages=[...],
    metadata={"task_type": "decision", "complexity": "high"}
)

# Inferred from context
# Gateway analyzes prompt to determine task
```

## Cost-Aware Routing

Route to minimize costs while meeting requirements:

```yaml
cost_routing:
  strategy: minimize_cost
  
  constraints:
    quality_floor: 0.9  # Don't sacrifice too much quality
    latency_ceiling: 5s
    
  model_costs:
    claude-3.5-sonnet:
      input: 0.003  # per 1K tokens
      output: 0.015
      quality: 0.95
      
    gpt-4o-mini:
      input: 0.00015
      output: 0.0006
      quality: 0.85
      
    claude-3-haiku:
      input: 0.00025
      output: 0.00125
      quality: 0.80
```

### Cost Optimization Algorithm

```
For each request:
1. Estimate token count
2. Calculate cost per model
3. Filter models meeting quality floor
4. Filter models meeting latency ceiling
5. Select lowest cost model
6. Route request
```

## Latency-Aware Routing

Route for speed when needed:

```yaml
latency_routing:
  interactive_mode:
    condition: metadata.interactive == true
    preference:
      - model: gpt-4o-mini
        max_latency: 1s
      - model: claude-3-haiku
        max_latency: 1.5s
        
  batch_mode:
    condition: metadata.batch == true
    preference:
      - model: claude-3.5-sonnet  # Best quality, latency acceptable
```

## Load-Aware Routing

Route around overloaded providers:

```yaml
load_routing:
  health_checks:
    interval: 10s
    threshold:
      error_rate: 0.1
      latency_p95: 3s
      
  routing:
    - if: provider.health < 0.8
      action: reduce_traffic_50%
      
    - if: provider.health < 0.5
      action: route_to_fallback
```

## A/B Testing

Route for experimentation:

```yaml
ab_test:
  name: new_model_evaluation
  
  traffic_split:
    control:
      model: claude-3.5-sonnet
      percent: 80
    treatment:
      model: gpt-4o
      percent: 20
      
  metrics:
    - quality_score
    - latency
    - cost
    - user_satisfaction
```

## Routing Audit

All routing decisions are logged:

```yaml
routing_decision:
  request_id: req-abc123
  timestamp: 2026-01-10T14:30:00Z
  
  request:
    agent: dispute-analyst-tier1
    task_type: decision
    estimated_tokens: 2500
    
  routing:
    strategy: cost_aware
    candidates:
      - model: claude-3.5-sonnet
        estimated_cost: 0.05
        meets_quality: true
        meets_latency: true
      - model: gpt-4o-mini
        estimated_cost: 0.01
        meets_quality: false  # Below quality floor
        
    selected: claude-3.5-sonnet
    reason: "Cheapest meeting all constraints"
```

---

**References:**
*   `olympus-seer-docs/seer-design/subsystems/model-gateway.md`

