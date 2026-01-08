# Seer Subsystems

This folder contains design documents for each Olympus Seer subsystem.

## Subsystems

| Subsystem | Description | Status |
|-----------|-------------|--------|
| [Agent Definition & Lifecycle Service](./agent-lifecycle-service.md) | Agent versioning, Training/Employment Specs, state management, governance definitions | 🟡 Draft |
| [Agent Lifecycle API](./agent-lifecycle-api.md) | REST API for lifecycle management, kill switch, webhooks | 🟡 Draft |
| [Guardrails](./guardrails.md) | System prompt + sidecar guardrails, Python contract, enforcement pipeline | 🟡 Draft |
| [Agent Identity & Authority Framework](./agent-identity-authority.md) | Agent identity, delegation chains, authority enforcement (via Cipher) | Placeholder |
| [Context Assembly Engine](./context-assembly-engine.md) | Context compilation from memory, knowledge, session state | 🟡 Draft |
| [Runtime & Deployment Abstraction](./runtime-deployment.md) | Agent execution, policy enforcement, graceful degradation | Placeholder |
| [Agent Observability Service](./agent-observability.md) | Runtime metrics, decision traces, health monitoring | Placeholder |
| [Agent Evaluation Service](./agent-evaluation.md) | Development-time testing, benchmarks, CI/CD quality gates | Placeholder |
| [Model Gateway](./model-gateway.md) | Unified LLM/SLM access, model routing, fallback | Placeholder |

## Governance Distribution

Governance, Policy & Override functions are distributed between subsystems:

| Function | Subsystem | Role |
|----------|-----------|------|
| Policy/Guardrail **Definitions** | Lifecycle Service | Control plane |
| Policy/Guardrail **Enforcement** | Runtime Service | Data plane |
| Authority **Grants** | Lifecycle Service | Control plane |
| Authority **Checks** | Runtime Service | Data plane |
| Kill Switch **Commands** | Lifecycle Service | Control plane |
| Kill Switch **Execution** | Runtime Service | Data plane |

## Related

- [Introduction](../introduction.md) — Seer overview
- [Raw, Trained, Employed Agents](../../../aosm-meta-model/raw-trained-employed-agents.md) — Agent lifecycle model

