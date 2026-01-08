# Seer Subsystems

This folder contains design documents for each Olympus Seer subsystem.

## Subsystems

| Subsystem | Description | Status |
|-----------|-------------|--------|
| [Agent Definition & Lifecycle Service](./agent-lifecycle-service.md) | Agent versioning, Training/Employment Specs, state management, governance definitions | 🟡 Draft |
| [Agent Lifecycle API](./agent-lifecycle-api.md) | REST API for lifecycle management, kill switch, webhooks | 🟡 Draft |
| [Guardrails](./guardrails.md) | Behavioral guidelines + sidecar enforcement, Python contract, execution pipeline | 🟡 Draft |
| [Authority Enforcement](./authority-enforcement.md) | OPA policies at Tool Gateway and Signal Exchange, violation handling | 🟡 Draft |
| [Agent Identity & Authority Framework](./agent-identity-authority.md) | Agent identity, delegation chains, IAM integration (via Cipher) | Placeholder |
| [Context Assembly Engine](./context-assembly-engine.md) | Context compilation from memory, knowledge, session state | 🟡 Draft |
| [Runtime & Deployment](./runtime-deployment.md) | Atlantis, Heracles, pod architecture, request dispatch | 🟡 Draft |
| [Agent Observability](./agent-observability.md) | SDK, Watch integration, metrics, logs, traces, dashboards | 🟡 Draft |
| [Agent Evaluation Service](./agent-evaluation.md) | Development-time testing, benchmarks, CI/CD quality gates | 🔴 PARKED |
| [Model Gateway](./model-gateway.md) | Bifrost-based LLM gateway, routing, fallback, budgets | 🟡 Draft |

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
- [Editorial Review](../EDITORIAL-REVIEW.md) — Documentation review summary

## Related ADRs

- [ADR-0072: Guardrails Two-Layer Model](../../../olympus-hub-docs/decision-logs/0072-seer-guardrails-two-layer-model.md)
- [ADR-0073: Authority Enforcement via OPA](../../../olympus-hub-docs/decision-logs/0073-seer-authority-enforcement-opa.md)
- [ADR-0074: Runtime on Atlantis](../../../olympus-hub-docs/decision-logs/0074-seer-runtime-atlantis-based.md)
- [ADR-0075: Model Gateway (Bifrost)](../../../olympus-hub-docs/decision-logs/0075-seer-model-gateway-bifrost.md)
- [ADR-0076: Observability via Watch](../../../olympus-hub-docs/decision-logs/0076-seer-observability-watch-based.md)
- [ADR-0077: Agent Evaluation Deferred](../../../olympus-hub-docs/decision-logs/0077-seer-evaluation-deferred.md)

