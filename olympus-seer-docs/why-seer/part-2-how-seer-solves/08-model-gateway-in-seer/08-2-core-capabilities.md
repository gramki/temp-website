# 8.2 Core Capabilities

The Bifrost Model Gateway provides essential capabilities for enterprise AI operations: a unified interface, provider abstraction, automatic fallback, and comprehensive observability.

## Unified Interface

### OpenAI-Compatible API

Agents use a standard OpenAI-compatible interface:

```python
# Chat completion
response = await gateway.chat_completion(
    model="agent-model",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ],
    max_tokens=1000,
    temperature=0.7
)

# Embeddings
embeddings = await gateway.embeddings(
    model="embedding-model",
    input=["text to embed"]
)
```

### Streaming Support

Full streaming support for real-time responses:

```python
async for chunk in gateway.chat_completion_stream(
    model="agent-model",
    messages=[...],
    stream=True
):
    yield chunk.content
```

## Provider Abstraction

### Transparent Provider Switching

Agents don't know which provider is serving:

```yaml
# Before: Using OpenAI
model_config:
  agent-model:
    provider: openai
    model: gpt-4o
    
# After: Switched to Anthropic
model_config:
  agent-model:
    provider: anthropic
    model: claude-3.5-sonnet
    
# Agent code: unchanged
```

### Provider-Specific Features

Some features require provider-specific handling:

```yaml
feature_mapping:
  function_calling:
    openai: native
    anthropic: tool_use
    bedrock: native_or_tool_use
    
  vision:
    openai: supported
    anthropic: supported
    bedrock: model_dependent
```

## Automatic Fallback

### Fallback Chain

When primary provider fails, automatically try alternatives:

```yaml
fallback_config:
  primary: claude-3.5-sonnet
  
  fallback_chain:
    - model: gpt-4o
      trigger:
        - error_code: 503
        - latency: "> 10s"
        
    - model: claude-3-haiku
      trigger:
        - all_above_failed
      limitations:
        - complex_reasoning: degraded
        
  fallback_notification:
    operator: true
    user: configurable
```

### Fallback Triggers

```yaml
fallback_triggers:
  error_based:
    - 429: rate_limit_exceeded
    - 500: internal_error
    - 503: service_unavailable
    - timeout: configurable
    
  performance_based:
    - latency: "> threshold"
    - error_rate: "> threshold"
    
  circuit_breaker:
    - failures: 5 in 1m
    - recovery: 30s
```

### Fallback Audit

All fallbacks are logged:

```yaml
fallback_event:
  timestamp: 2026-01-10T14:30:00Z
  original_model: claude-3.5-sonnet
  fallback_model: gpt-4o
  trigger: error_503
  request_id: req-abc123
  agent: dispute-analyst-tier1
```

## Response Normalization

Responses are normalized across providers:

```yaml
normalized_response:
  id: "chat-xyz123"
  model: "agent-model"  # Logical name
  
  choices:
    - message:
        role: assistant
        content: "..."
      finish_reason: stop
      
  usage:
    prompt_tokens: 1234
    completion_tokens: 567
    total_tokens: 1801
    
  metadata:
    provider: anthropic  # Actual provider
    provider_model: claude-3.5-sonnet
    latency_ms: 450
    cost_usd: 0.05
```

## Observability

### Per-Request Metrics

Every request is instrumented:

```yaml
request_metrics:
  - request_id
  - model (logical)
  - provider
  - provider_model
  - prompt_tokens
  - completion_tokens
  - latency_ms
  - status (success/error)
  - fallback_used
  - cost_usd
```

### Aggregated Metrics

```yaml
aggregated_metrics:
  by_model:
    - requests_per_minute
    - average_latency
    - error_rate
    - fallback_rate
    
  by_provider:
    - availability
    - average_latency
    - cost_per_token
    
  by_agent:
    - token_usage
    - cost_total
    - model_distribution
```

## Rate Limiting

Protect against abuse and control costs:

```yaml
rate_limits:
  per_agent:
    requests_per_minute: 100
    tokens_per_minute: 100000
    
  per_workbench:
    requests_per_minute: 1000
    tokens_per_hour: 10000000
    
  per_tenant:
    tokens_per_day: 100000000
```

---

**References:**
*   `olympus-seer-docs/seer-design/subsystems/model-gateway.md`
*   `olympus-seer-docs/why-seer/part-1-background/05-building-enterprise-agent/05-7-model-provider-independence.md`
