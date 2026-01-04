# Model Gateway

> **Status:** Placeholder — Design in progress

## Overview

The Model Gateway provides **unified access to LLMs and SLMs** across providers, enabling model portability, routing, and operational control.

## Scope

| Capability | Description |
|------------|-------------|
| **Unified Model Interface** | Common API for all model providers |
| **Model Registry** | Catalog of available models with capabilities |
| **Model Routing** | Select model based on task, cost, latency |
| **Fallback & Failover** | Switch to backup model on failure |
| **Rate Limiting** | Manage token budgets and API limits |
| **Cost Tracking** | Track inference costs per agent/tenant |
| **Embedding Generation** | Unified embedding API for RAG |

## Key Principles

- Models are implementation details; agents are products
- Model selection is swappable without agent changes
- Agents should work across model providers
- Gateway handles routing, failover, and traffic management

## Supported Providers

| Provider | Status |
|----------|--------|
| AWS Bedrock | Planned |
| Azure OpenAI | Planned |
| Google Vertex AI | Planned |
| Self-hosted (vLLM, Ollama) | Planned |

## Gateway Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                         MODEL GATEWAY                               │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                     Unified Model Interface                   │ │
│  │   - complete(prompt, options) → response                      │ │
│  │   - embed(text) → vector                                      │ │
│  │   - capabilities() → model_info                               │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                │                                    │
│  ┌─────────────────────────────┼─────────────────────────────────┐ │
│  │                      Routing & Control                        │ │
│  │   - Model selection        - Rate limiting                    │ │
│  │   - Failover logic         - Cost tracking                    │ │
│  └─────────────────────────────┼─────────────────────────────────┘ │
│                                │                                    │
│         ┌──────────────────────┼──────────────────────┐            │
│         ▼                      ▼                      ▼            │
│  ┌─────────────┐       ┌─────────────┐       ┌─────────────┐       │
│  │   Bedrock   │       │ Azure OpenAI│       │  Vertex AI  │       │
│  │   Adapter   │       │   Adapter   │       │   Adapter   │       │
│  └─────────────┘       └─────────────┘       └─────────────┘       │
└─────────────────────────────────────────────────────────────────────┘
```

## Related

- [Introduction](../introduction.md)
- [Enterprise Agent Platform Requirements](../../requirements-enterprise-agentic-platform/README.md)

---

*TODO: Detailed design*

