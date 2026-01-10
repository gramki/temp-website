# 8.1 The Bifrost Model Gateway

Bifrost is Seer's Model Gateway—a unified access layer for Large Language Models (LLMs) and Small Language Models (SLMs) across multiple providers. It abstracts away provider differences while adding enterprise capabilities like routing, fallback, and governance.

## Why Bifrost

| Challenge | Without Gateway | With Bifrost |
|-----------|-----------------|--------------|
| **Provider lock-in** | Tied to one vendor | Switch freely |
| **API differences** | Code changes per provider | Unified interface |
| **Credentials** | Scattered, hard to manage | Centralized |
| **Cost tracking** | Manual aggregation | Automatic attribution |
| **Fallback** | Custom implementation | Built-in |

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   BIFROST MODEL GATEWAY                      │
│                                                              │
│   ┌───────────────────────────────────────────────────┐    │
│   │                  UNIFIED API                       │    │
│   │   OpenAI-compatible interface                      │    │
│   │   • /v1/chat/completions                           │    │
│   │   • /v1/embeddings                                 │    │
│   └────────────────────────┬──────────────────────────┘    │
│                            │                                │
│   ┌────────────────────────▼──────────────────────────┐    │
│   │               REQUEST PROCESSING                   │    │
│   │                                                    │    │
│   │   Auth → Policy → Route → Transform → Execute      │    │
│   └────────────────────────┬──────────────────────────┘    │
│                            │                                │
│   ┌────────────────────────▼──────────────────────────┐    │
│   │                  PROVIDER LAYER                    │    │
│   │                                                    │    │
│   │   ┌──────────┐ ┌──────────┐ ┌──────────┐         │    │
│   │   │ OpenAI   │ │Anthropic │ │ Bedrock  │ ...     │    │
│   │   └──────────┘ └──────────┘ └──────────┘         │    │
│   │   ┌──────────┐ ┌──────────┐ ┌──────────┐         │    │
│   │   │  Azure   │ │  Google  │ │ Custom   │ ...     │    │
│   │   └──────────┘ └──────────┘ └──────────┘         │    │
│   └───────────────────────────────────────────────────┘    │
│                                                              │
│   ┌───────────────────────────────────────────────────┐    │
│   │                  OBSERVABILITY                     │    │
│   │   Metrics • Logs • Traces • Cost Tracking          │    │
│   └───────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## Key Components

### Unified API

Agents interact with a single OpenAI-compatible API:

```python
# Agent code - same regardless of underlying provider
response = await model_client.chat_completion(
    model="dispute-analyst-primary",  # Logical model name
    messages=[...],
    max_tokens=1000
)
```

### Model Registry

Logical model names map to physical providers:

```yaml
model_registry:
  dispute-analyst-primary:
    provider: anthropic
    model: claude-3.5-sonnet
    fallback: dispute-analyst-fallback
    
  dispute-analyst-fallback:
    provider: openai
    model: gpt-4o
    fallback: dispute-analyst-minimal
    
  dispute-analyst-minimal:
    provider: bedrock
    model: claude-3-haiku
```

### Request Pipeline

Every request flows through:

1. **Authentication**: Verify agent identity
2. **Authorization**: Check model access policy
3. **Budget check**: Verify cost ceiling not exceeded
4. **Routing**: Select target model
5. **Transformation**: Adapt to provider API
6. **Execution**: Call provider
7. **Logging**: Record metrics and costs

### Provider Adapters

Adapters normalize provider differences:

```yaml
providers:
  anthropic:
    adapter: anthropic-claude
    auth: api_key
    endpoint: https://api.anthropic.com
    
  bedrock:
    adapter: aws-bedrock
    auth: iam_role
    region: us-east-1
    
  azure_openai:
    adapter: azure-openai
    auth: azure_ad
    endpoint: ${AZURE_ENDPOINT}
```

## Credential Management

Credentials are managed centrally:

```yaml
credential_management:
  storage: kubernetes_secrets
  rotation: automatic
  access:
    - agents: via_gateway_only
    - operators: via_admin_console
    
  isolation:
    - per_tenant
    - per_workbench (optional)
```

Agents never see raw credentials:

```yaml
agent_access:
  model_gateway: internal-gateway.seer.svc
  auth: agent_identity (SPIFFE)
  # No API keys in agent config
```

## High Availability

Bifrost is designed for production reliability:

```yaml
high_availability:
  replicas: 3
  load_balancing: round_robin
  health_checks:
    - liveness: /health
    - readiness: /ready
    
  provider_health:
    - monitor: response_time
    - monitor: error_rate
    - action: automatic_failover
```

---

**References:**
*   `olympus-seer-docs/seer-design/subsystems/model-gateway.md`
*   `olympus-hub-docs/decision-logs/0075-seer-model-gateway-bifrost.md`
