# 7.2 Graceful Degradation

Enterprise agents must handle failures without catastrophic outcomes. Graceful degradation ensures that when components fail, agents reduce capability rather than fail completely, maintaining user experience and operational continuity.

## Types of Failures

| Failure Type | Example | Impact |
|--------------|---------|--------|
| **Model unavailable** | LLM provider outage | Cannot reason |
| **Tool failure** | External API error | Cannot act |
| **Memory unavailable** | Hub service down | Cannot remember |
| **Rate limiting** | Exceeded quotas | Throttled |
| **Timeout** | Slow response | Delayed |

## Degradation Strategies

### Strategy 1: Model Fallback

When primary model is unavailable:

```yaml
model_fallback:
  primary: claude-3.5-sonnet
  fallback_chain:
    - model: gpt-4o
      conditions:
        - primary_unavailable
        - primary_latency > 10s
        
    - model: claude-3-haiku
      conditions:
        - all_above_unavailable
      limitations:
        - complex_reasoning: degraded
        - notify_user: true
        
    - model: none
      conditions:
        - all_above_unavailable
      action: escalate_to_human
```

### Strategy 2: Reduced Capability

When tools fail, reduce scope:

```yaml
capability_degradation:
  normal:
    - retrieve_knowledge
    - query_memory
    - invoke_tools
    - execute_actions
    
  degraded_tool_failure:
    - retrieve_knowledge
    - query_memory
    # Tools unavailable
    limitations:
      - cannot_execute_actions
      - provide_guidance_only
    notify_user: true
    
  degraded_memory_failure:
    - retrieve_knowledge
    # Memory unavailable
    limitations:
      - no_precedent_lookup
      - no_personalization
    notify_user: true
```

### Strategy 3: Queue and Retry

For transient failures:

```yaml
retry_strategy:
  model_calls:
    max_retries: 3
    backoff: exponential
    initial_delay: 1s
    max_delay: 30s
    
  tool_calls:
    max_retries: 2
    backoff: linear
    initial_delay: 2s
    
  on_exhausted:
    action: fallback_or_escalate
```

### Strategy 4: Cached Responses

Use cached knowledge when live retrieval fails:

```yaml
cache_fallback:
  knowledge_retrieval:
    on_failure: use_cache_if_fresh
    max_cache_age: 1h
    
  operational_data:
    on_failure: use_cache_with_warning
    max_cache_age: 5m
    warn_user: "Using data from 5 minutes ago"
```

## Degradation Notification

Users and operators are informed of degraded state:

### User Notification

```yaml
user_notification:
  degraded_mode:
    template: |
      I'm currently operating with reduced capabilities due to 
      {reason}. I can still help with {available_capabilities}, 
      but {limitations}. Would you like to proceed or speak 
      with a human agent?
      
  examples:
    tool_failure:
      reason: "a temporary system issue"
      available_capabilities: "answering questions about your account"
      limitations: "I cannot make changes right now"
```

### Operator Alert

```yaml
operator_alert:
  degraded_mode:
    severity: warning
    channels: [pagerduty, slack]
    message: |
      Agent {agent_id} entered degraded mode.
      Reason: {failure_type}
      Impact: {affected_capabilities}
      Duration: {degraded_since}
```

## Degradation Audit

All degradation events are logged:

```yaml
degradation_event:
  timestamp: 2026-01-10T14:30:00Z
  agent: dispute-analyst-tier1
  
  trigger:
    type: model_unavailable
    details: "claude-3.5-sonnet: 503 Service Unavailable"
    
  degradation:
    from: full_capability
    to: fallback_model
    fallback_model: gpt-4o
    
  impact:
    requests_affected: 12
    capabilities_reduced: []  # None with gpt-4o fallback
    
  recovery:
    timestamp: 2026-01-10T14:35:00Z
    duration: 5m
```

## Health States

Agents report their health state:

```yaml
health_states:
  healthy:
    definition: "All capabilities available"
    indicator: green
    
  degraded:
    definition: "Some capabilities reduced"
    indicator: yellow
    details: [which_degraded]
    
  impaired:
    definition: "Critical capabilities unavailable"
    indicator: orange
    action: consider_escalation
    
  unavailable:
    definition: "Cannot serve requests"
    indicator: red
    action: route_to_human
```

## Circuit Breaker

Prevent cascading failures:

```yaml
circuit_breaker:
  tool_calls:
    failure_threshold: 5  # Failures before open
    success_threshold: 3  # Successes before close
    timeout: 30s          # Time before half-open
    
  states:
    closed: "Normal operation"
    open: "Rejecting calls, fast fail"
    half_open: "Testing if recovered"
    
  on_open:
    action: use_fallback
    notify: operators
```

---

**References:**
*   `olympus-seer-docs/seer-design/subsystems/model-gateway.md`
*   `olympus-seer-docs/why-seer/part-1-background/02-enterprise-agents-different/02-3-opd-triad.md`
