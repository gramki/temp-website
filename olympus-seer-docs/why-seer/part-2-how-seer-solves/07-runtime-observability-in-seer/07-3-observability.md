# 7.3 Observability

Observability for AI agents extends beyond traditional metrics. Seer provides purpose-built observability that understands agent behavior—reasoning patterns, decision quality, and cognitive health—not just system metrics.

## Observability Pillars

| Pillar | What It Provides | Agent-Specific Aspects |
|--------|------------------|------------------------|
| **Metrics** | Quantitative measurements | Token usage, decision rates, health scores |
| **Logs** | Event records | Reasoning steps, tool calls, policy decisions |
| **Traces** | Request flow | Context assembly, model calls, action execution |

## Metrics

### Agent Health Score (AHS)

Composite metric reflecting overall agent health:

```yaml
agent_health_score:
  components:
    accuracy:
      weight: 0.3
      source: outcome_feedback
      
    success_rate:
      weight: 0.25
      source: completion_rate
      
    compliance:
      weight: 0.25
      source: policy_adherence
      
    user_satisfaction:
      weight: 0.2
      source: explicit_feedback
      
  calculation: weighted_average
  range: 0.0 - 1.0
  
  thresholds:
    healthy: >= 0.8
    warning: 0.6 - 0.8
    critical: < 0.6
```

### Operational Metrics

```yaml
operational_metrics:
  throughput:
    - requests_per_second
    - decisions_per_hour
    - actions_per_day
    
  latency:
    - p50_response_time
    - p95_response_time
    - p99_response_time
    - model_latency
    - tool_latency
    
  errors:
    - error_rate
    - failure_by_type
    - retry_rate
    
  resources:
    - cpu_utilization
    - memory_utilization
    - gpu_utilization (if applicable)
```

### Cognitive Metrics

```yaml
cognitive_metrics:
  reasoning:
    - average_reasoning_turns
    - reasoning_loop_rate
    - stuck_detection_rate
    
  context:
    - average_context_tokens
    - token_budget_utilization
    - retrieval_relevance_score
    
  decisions:
    - decision_confidence_distribution
    - escalation_rate
    - override_rate
    
  learning:
    - feedback_incorporation_rate
    - pattern_detection_rate
```

### Cost Metrics

```yaml
cost_metrics:
  token_usage:
    - input_tokens_per_request
    - output_tokens_per_request
    - total_tokens_per_request
    
  cost:
    - cost_per_request
    - cost_per_decision
    - cost_per_hour
    - cost_per_day
    
  efficiency:
    - cost_to_health_ratio (CHR)
    - cost_per_successful_outcome
```

## Logs

### Structured Logging

All agent events are logged with structure:

```json
{
  "timestamp": "2026-01-10T14:30:00Z",
  "level": "info",
  "agent": "dispute-analyst-tier1",
  "request_id": "req-abc123",
  "trace_id": "trace-xyz789",
  
  "event": "decision_made",
  "decision": {
    "type": "refund_approved",
    "amount": 450,
    "confidence": 0.87
  },
  
  "context": {
    "case_id": "case-12345",
    "reasoning_turns": 3,
    "tools_used": ["get_transaction", "check_policy"],
    "knowledge_retrieved": 4
  },
  
  "policy": {
    "evaluated": ["max-refund-limit", "escalation-rules"],
    "decisions": ["allow", "not_applicable"]
  }
}
```

### Log Categories

```yaml
log_categories:
  reasoning:
    - reasoning_step_started
    - reasoning_step_completed
    - reasoning_loop_detected
    
  context:
    - context_assembly_started
    - source_queried
    - context_assembled
    
  tools:
    - tool_invoked
    - tool_succeeded
    - tool_failed
    
  decisions:
    - decision_made
    - decision_escalated
    - decision_overridden
    
  governance:
    - policy_evaluated
    - guardrail_triggered
    - authority_checked
```

## Traces

### Distributed Tracing

Seer uses OpenTelemetry for distributed tracing:

```yaml
trace_structure:
  root_span: agent_request
  
  child_spans:
    - name: context_assembly
      children:
        - knowledge_retrieval
        - memory_query
        - operational_data_fetch
        - agent_memory_load
        
    - name: reasoning_loop
      children:
        - reasoning_turn_1
        - reasoning_turn_2
        - tool_invocation
        - reasoning_turn_3
        
    - name: decision_making
      children:
        - policy_evaluation
        - authority_check
        - decision_record_creation
        
    - name: action_execution
      children:
        - tool_call
        - result_processing
        - output_delivery
```

### Trace Example

```
agent_request (500ms)
├── context_assembly (150ms)
│   ├── knowledge_retrieval (80ms)
│   ├── memory_query (40ms)
│   └── agent_memory_load (30ms)
├── reasoning_loop (280ms)
│   ├── reasoning_turn_1 (50ms)
│   ├── tool_invocation: get_transaction (30ms)
│   ├── reasoning_turn_2 (60ms)
│   └── reasoning_turn_3 (40ms)
├── decision_making (50ms)
│   ├── policy_evaluation (20ms)
│   └── decision_record (30ms)
└── action_execution (20ms)
    └── tool_call: approve_refund (20ms)
```

## Dashboards

### Operator Dashboard

```yaml
operator_dashboard:
  panels:
    - name: Agent Health Overview
      metrics: [ahs_by_agent, healthy_degraded_impaired_counts]
      
    - name: Request Volume
      metrics: [requests_per_second, by_agent, by_workbench]
      
    - name: Latency
      metrics: [p50, p95, p99, by_component]
      
    - name: Errors
      metrics: [error_rate, errors_by_type, recent_errors]
      
    - name: Cost
      metrics: [cost_per_hour, cost_by_agent, chr_trend]
      
    - name: Governance
      metrics: [escalation_rate, override_rate, policy_denials]
```

### Alerting

```yaml
alerts:
  - name: agent_health_critical
    condition: ahs < 0.6 for 5m
    severity: critical
    channels: [pagerduty]
    
  - name: high_escalation_rate
    condition: escalation_rate > 0.3 for 15m
    severity: warning
    channels: [slack]
    
  - name: cost_anomaly
    condition: cost_per_hour > 2x baseline
    severity: warning
    channels: [slack, email]
```

---

**References:**
*   `olympus-seer-docs/seer-design/subsystems/observability.md`
*   `olympus-seer-docs/why-seer/part-1-background/02-enterprise-agents-different/02-3-opd-triad.md`
