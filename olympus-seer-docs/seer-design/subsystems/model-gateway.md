# Model Gateway

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-08

---

## Overview

The Seer Model Gateway provides **unified LLM/SLM access** for all agents in the Hub ecosystem. It is based on [Bifrost](https://github.com/maximhq/bifrost), an open-source LLM gateway, adapted for Hub's authentication, governance, and observability requirements.

**Key Capabilities:**
- Unified interface for 8+ providers, 1000+ models
- Provider fallback for high availability
- Budget enforcement at workbench and agent levels
- Virtual key management per Employed Agent
- OpenTelemetry-based observability

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        MODEL GATEWAY ARCHITECTURE                            │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                         AGENT PODS                                   │   │
│   │                                                                       │   │
│   │   ┌───────────┐   ┌───────────┐   ┌───────────┐                     │   │
│   │   │  Agent 1  │   │  Agent 2  │   │  Agent N  │                     │   │
│   │   │           │   │           │   │           │                     │   │
│   │   │ base_url= │   │ base_url= │   │ base_url= │                     │   │
│   │   │ $MODEL_   │   │ $MODEL_   │   │ $MODEL_   │                     │   │
│   │   │ GATEWAY   │   │ GATEWAY   │   │ GATEWAY   │                     │   │
│   │   └─────┬─────┘   └─────┬─────┘   └─────┬─────┘                     │   │
│   │         │               │               │                            │   │
│   └─────────┼───────────────┼───────────────┼────────────────────────────┘   │
│             │               │               │                                │
│             └───────────────┼───────────────┘                                │
│                             │ OpenAI-compatible API                          │
│                             ▼                                                │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    MODEL GATEWAY (Bifrost)                           │   │
│   │                                                                       │   │
│   │   ┌─────────────────────────────────────────────────────────────┐   │   │
│   │   │                    AUTHENTICATION                            │   │   │
│   │   │                    (Cipher IAM Integration)                  │   │   │
│   │   └─────────────────────────────────────────────────────────────┘   │   │
│   │                             │                                        │   │
│   │   ┌─────────────────────────────────────────────────────────────┐   │   │
│   │   │                    OPA POLICIES                              │   │   │
│   │   │                    • Model access control                    │   │   │
│   │   │                    • Rate limiting                           │   │   │
│   │   │                    • Budget enforcement                      │   │   │
│   │   └─────────────────────────────────────────────────────────────┘   │   │
│   │                             │                                        │   │
│   │   ┌─────────────────────────────────────────────────────────────┐   │   │
│   │   │                    ROUTING & FALLBACK                        │   │   │
│   │   │                    (Tenant-configured)                       │   │   │
│   │   └─────────────────────────────────────────────────────────────┘   │   │
│   │                             │                                        │   │
│   │   ┌─────────────────────────────────────────────────────────────┐   │   │
│   │   │                    OBSERVABILITY                             │   │   │
│   │   │                    (Prometheus → Watch)                      │   │   │
│   │   └─────────────────────────────────────────────────────────────┘   │   │
│   │                             │                                        │   │
│   └─────────────────────────────┼───────────────────────────────────────┘   │
│                                 │                                            │
│              ┌──────────────────┼──────────────────┐                        │
│              │                  │                  │                        │
│              ▼                  ▼                  ▼                        │
│   ┌───────────────┐   ┌───────────────┐   ┌───────────────┐                │
│   │    OpenAI     │   │   Anthropic   │   │  AWS Bedrock  │   ...          │
│   └───────────────┘   └───────────────┘   └───────────────┘                │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Deployment Model

Model Gateway is deployed at **platform level** — one instance per Hub installation:

| Scope | Description |
|-------|-------------|
| **Hub Installation** | Single Model Gateway instance |
| **All Tenants** | Share the gateway |
| **Isolation** | Virtual keys, budgets, and policies per tenant/agent |

---

## Bifrost Customizations

The following Hub-specific integrations have been added to Bifrost:

| Integration | Purpose |
|-------------|---------|
| **Cipher IAM** | Authentication and authorization |
| **OPA Policies** | Access control, rate limiting, budget enforcement |
| **Olympus Watch** | Observability (metrics, logs, alerts) |

> **Note**: LLM calls are **not** logged to CAF. They are treated as operational logs, not enterprise auditable events.

---

## Model Catalog

### Provider Configuration

**Tenant admins** configure available providers per Seer Subscription:

```yaml
# Workbench Model Configuration
apiVersion: seer.olympus.io/v1
kind: ModelConfiguration
metadata:
  name: acme-disputes-models
  namespace: acme-disputes
spec:
  subscription: acme-seer-subscription
  
  providers:
    - name: openai
      enabled: true
      credentials:
        secretRef: openai-api-key
      models:
        - gpt-4o
        - gpt-4o-mini
        - o1
        - o1-mini
    
    - name: anthropic
      enabled: true
      credentials:
        secretRef: anthropic-api-key
      models:
        - claude-3-5-sonnet
        - claude-3-5-haiku
    
    - name: bedrock
      enabled: true
      credentials:
        iamRoleArn: arn:aws:iam::123456789:role/bedrock-access
      models:
        - amazon.titan-text-premier-v1:0
        - anthropic.claude-3-5-sonnet-v1
```

### Custom Models

Tenants can add custom deployed models (e.g., fine-tuned models on SageMaker, Bedrock):

```yaml
providers:
  - name: custom-sagemaker
    type: sagemaker
    endpoint: arn:aws:sagemaker:us-west-2:123456789:endpoint/fraud-classifier
    credentials:
      iamRoleArn: arn:aws:iam::123456789:role/sagemaker-invoke
```

> **Note**: Custom model configuration details are out of scope for this document.

---

## Model Selection

### Whitelist Hierarchy

Models are selected through a hierarchy of whitelists:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        MODEL SELECTION HIERARCHY                             │
│                                                                              │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  1. Raw Agent: Declares supported models                             │   │
│   │     models: [gpt-4o, gpt-4o-mini, claude-3-5-sonnet, o1]            │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                 │                                            │
│                                 ▼ subset                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  2. Training Spec: Selects from Raw Agent's list                    │   │
│   │     allowedModels: [gpt-4o, claude-3-5-sonnet]                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                 │                                            │
│                                 ▼ subset                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  3. Employment Spec: Further restricts for deployment               │   │
│   │     allowedModels: [gpt-4o]                                         │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Specification Examples

```yaml
# Training Spec
spec:
  models:
    allowedModels:
      - gpt-4o
      - gpt-4o-mini
      - claude-3-5-sonnet
    preferredModel: gpt-4o

# Employment Spec (can only subset, not expand)
spec:
  models:
    allowedModels:
      - gpt-4o  # Restricted to single model for this deployment
```

---

## Routing and Fallback

### Fallback Configuration

Fallback is **configured by tenant admin** at the workbench level:

```yaml
# Workbench Model Configuration
spec:
  fallback:
    enabled: true
    strategy: priority  # or: round-robin, cost-optimized
    
    chains:
      - name: reasoning-chain
        models:
          - gpt-4o           # Primary
          - claude-3-5-sonnet # Fallback 1
          - o1-mini          # Fallback 2
        
        triggers:
          - type: error
            codes: [429, 500, 502, 503]
          - type: timeout
            thresholdMs: 30000
          - type: circuit-breaker
            errorRate: 0.1
            windowSeconds: 60
```

### Routing Behavior

| Scenario | Behavior |
|----------|----------|
| **Primary available** | Route to primary model |
| **Primary rate-limited (429)** | Fallback to next in chain |
| **Primary timeout** | Fallback to next in chain |
| **Circuit breaker open** | Skip primary, use fallback |
| **All models unavailable** | Return error to agent |

---

## Governance

### Budget Enforcement

Budgets are enforced at two levels:

| Level | Scope | Example |
|-------|-------|---------|
| **Workbench** | All agents in workbench | $10,000/month |
| **Agent** | Per Employed Agent | $500/month |

```yaml
# Workbench Budget
spec:
  budgets:
    workbench:
      monthlyLimit: 10000  # USD
      alertThresholds: [50, 75, 90]  # Percent
      action: alert  # or: throttle, block
    
    perAgent:
      default:
        monthlyLimit: 500
        action: throttle
      
      overrides:
        - agent: fraud-analyst-senior
          monthlyLimit: 2000
```

### Virtual Keys

Each Employed Agent gets a **unique virtual key**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          VIRTUAL KEY MAPPING                                 │
│                                                                              │
│   Employed Agent                    Virtual Key                             │
│   ─────────────────────────────────────────────────────────────────────     │
│   fraud-analyst-acme-retail    →    vk_acme_fraud_analyst_retail_001        │
│   fraud-analyst-acme-commercial →   vk_acme_fraud_analyst_commercial_001    │
│   support-agent-acme           →    vk_acme_support_agent_001               │
│                                                                              │
│   Virtual Key Provides:                                                      │
│   • Usage tracking per agent                                                 │
│   • Budget enforcement per agent                                             │
│   • Audit trail per agent                                                    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Agent Access

### API Compatibility

Model Gateway provides an **OpenAI-compatible API**. Agents use it by setting `base_url`:

```python
# Agent code (any framework)
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ["VIRTUAL_KEY"],  # Injected by Seer
    base_url=os.environ["MODEL_GATEWAY_URL"]  # Injected at deployment
)

response = client.chat.completions.create(
    model="gpt-4o",  # Must be in allowed list
    messages=[
        {"role": "user", "content": "Analyze this transaction..."}
    ]
)
```

### Endpoint Discovery

Model Gateway URL is injected as an **environment variable** at deployment:

```yaml
# Pod specification (created by Seer Operator)
spec:
  containers:
    - name: agent
      env:
        - name: MODEL_GATEWAY_URL
          value: "http://model-gateway.seer-system.svc.cluster.local/v1"
        - name: VIRTUAL_KEY
          valueFrom:
            secretKeyRef:
              name: fraud-analyst-acme-retail-keys
              key: virtual-key
```

---

## Observability

### Metrics

Model Gateway exposes Prometheus-compatible metrics:

```prometheus
# Token usage
seer_model_tokens_total{agent="fraud-analyst", model="gpt-4o", type="input"} 125000
seer_model_tokens_total{agent="fraud-analyst", model="gpt-4o", type="output"} 45000

# Request metrics
seer_model_requests_total{agent="fraud-analyst", model="gpt-4o", status="success"} 1234
seer_model_requests_total{agent="fraud-analyst", model="gpt-4o", status="error"} 12

# Latency
seer_model_latency_seconds_bucket{agent="fraud-analyst", model="gpt-4o", le="1"} 900
seer_model_latency_seconds_bucket{agent="fraud-analyst", model="gpt-4o", le="5"} 1200

# Cost tracking
seer_model_cost_usd{agent="fraud-analyst", model="gpt-4o"} 145.50
seer_model_budget_remaining_usd{agent="fraud-analyst"} 354.50
```

### Watch Integration

Olympus Watch scrapes Model Gateway metrics and provides:

- **Dashboards**: Token usage, cost tracking, latency percentiles
- **Alerts**: Budget thresholds, error rate spikes, latency degradation
- **Analytics**: Usage trends, model comparison, cost optimization

### Logging

LLM calls are logged to **Olympus Watch** as operational logs:

```json
{
  "timestamp": "2026-01-08T14:30:00Z",
  "level": "INFO",
  "service": "model-gateway",
  "event": "llm_request",
  "agent_id": "fraud-analyst-acme-retail",
  "virtual_key": "vk_acme_fraud_analyst_retail_001",
  "model": "gpt-4o",
  "input_tokens": 500,
  "output_tokens": 150,
  "latency_ms": 1250,
  "status": "success",
  "cost_usd": 0.0195
}
```

> **Note**: LLM calls are **not** logged to CAF. Request/response content is not stored for audit (operational log only).

---

## Security

### Authentication

All requests to Model Gateway require valid authentication:

- **Cipher IAM** validates agent identity
- **Virtual Key** identifies the specific Employed Agent
- **mTLS** via Istio service mesh

### Authorization

OPA policies enforce:

```rego
package seer.model_gateway

# Allow if agent is authorized for this model
allow {
    input.agent.allowed_models[_] == input.request.model
    budget_available(input.agent.virtual_key)
}

# Check budget
budget_available(virtual_key) {
    usage := data.budgets[virtual_key].current
    limit := data.budgets[virtual_key].limit
    usage < limit
}
```

---

## Configuration Reference

### Environment Variables (Agent)

| Variable | Description |
|----------|-------------|
| `MODEL_GATEWAY_URL` | Model Gateway endpoint |
| `VIRTUAL_KEY` | Agent's virtual key for authentication |

### CRDs

| CRD | Purpose |
|-----|---------|
| `ModelConfiguration` | Provider and model catalog configuration |
| `ModelBudget` | Budget limits and alerts |
| `FallbackChain` | Fallback routing configuration |

---

## Related Documentation

- [Bifrost GitHub](https://github.com/maximhq/bifrost) — Upstream project
- [Bifrost Documentation](https://docs.getbifrost.ai/) — Feature documentation
- [Runtime Deployment](./runtime-deployment.md) — Agent deployment
- [Authority Enforcement](./authority-enforcement.md) — OPA policies
- [Training Spec CRD](../hub-integration/training-spec-crd.md) — Model whitelist
- [Employment Spec CRD](../hub-integration/employment-spec-crd.md) — Model restrictions
- [Olympus Watch](https://watch.olympus.tech/) — Observability
- [ADR-0075: Model Gateway (Bifrost)](../../../olympus-hub-docs/decision-logs/0075-seer-model-gateway-bifrost.md)

---

*Model Gateway provides unified, governed, and observable LLM access for all Seer agents, based on Bifrost OSS.*
