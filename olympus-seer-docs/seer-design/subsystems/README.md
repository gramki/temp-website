# Seer Subsystems

This folder contains design documents for each Olympus Seer subsystem.

## Subsystems

| Subsystem | Description | Status |
|-----------|-------------|--------|
| [Cipher IAM Extensions](./cipher-iam-extensions/README.md) | Agent identity, authority delegation, IAM integration | 🟡 Draft |
| [Agent Runtime](./agent-runtime/README.md) | Runtime environment, deployment, scaling operators | 🟢 Complete |
| [Seer Sidecar](./seer-sidecar/README.md) | Guardrails, metrics, policy enforcement, authority enforcement | 🟢 Complete |
| [Agent Lifecycle Manager](./agent-lifecycle-manager/README.md) | Employment spec management, delegation chain sync, agent levers, ecosystem integration, directory | 🟢 Complete |
| [Agent Ingress Gateway](./agent-ingress-gateway/README.md) | Subscription lifecycle, subscription-scoped policies, Signal Exchange integration | 🟡 Draft |
| [Model Gateway](./model-gateway/README.md) | Bifrost-based LLM gateway, routing, fallback, budgets | 🟡 Draft |
| [Agent Health Monitor](./agent-health-monitor/README.md) | Cost SLOs, behavior SLOs, feedback SLOs, human feedback service | 🟢 Complete |
| [Agent Session Supervisor](./agent-session-supervisor/README.md) | Supervisory policies, observations, escalations | 🟢 Complete |
| [Context Compiler](./context-compiler/README.md) | Context compilation from memory, knowledge, session state | 🟡 Draft |
| [Seer Agent SDK](./seer-agent-sdk/README.md) | SDK for Raw Agents (employment spec, prompts, context, metrics, tools, memory, knowledge) | 🟡 Draft |
| [Raw Agent Lifecycle Manager](./raw-agent-lifecycle-manager/README.md) | Raw agent spec, validation, directory, operators, levers | 🟡 Draft |
| [Trained Agent Lifecycle Manager](./trained-agent-lifecycle-manager/README.md) | Training spec, validation, directory, employed agent discovery, feedback services | 🟢 Complete |
| [Agent Analytics](./agent-analytics/README.md) | Agent operational data mart, ETSL integration, report integration | 🟢 Complete |
| [Observability Extensions to Watch](./observability-extensions-to-watch/README.md) | Watch extensions, persona dashboards, alert templates, operational tools | 🟢 Complete |
| [Agent Test Runner](./agent-test-runner/README.md) | Agent testing, behavior validation, health and safety checks | 🟢 Complete |

## Legacy Files (To Be Migrated)

The following files contain detailed content that will be migrated to the appropriate subsystem folders:

- `agent-lifecycle-service.md` — Legacy, superseded by `agent-lifecycle-manager/` detailed design
- `agent-lifecycle-api.md` — Legacy, superseded by `agent-lifecycle-manager/` detailed design
- `guardrails.md` → `seer-sidecar/`
- `authority-enforcement.md` → `seer-sidecar/` and `agent-ingress-gateway/`
- `context-assembly-engine.md` → `context-compiler/` and `seer-agent-sdk/`
- `runtime-deployment.md` → `agent-runtime/runtime-deployment.md` ✅ Migrated
- `agent-observability.md` → `agent-analytics/` and `seer-agent-sdk/`
- `observability-extensions-to-watch.md` → `observability-extensions-to-watch/` ✅ Migrated
- `model-gateway.md` → `model-gateway/`
- `agent-evaluation.md` → `agent-test-runner/` (MVP validations implemented; advanced evaluations in `parked-capabilities.md`)
- `agent-identity-authority.md` → `cipher-iam-extensions/` (placeholder)

## Governance Distribution

Governance, Policy & Override functions are distributed between subsystems:

| Function | Subsystem | Role |
|----------|-----------|------|
| Policy/Guardrail **Definitions** | Agent Lifecycle Manager | Control plane |
| Policy/Guardrail **Enforcement** | Seer Sidecar | Data plane |
| Authority **Grants** | Agent Lifecycle Manager | Control plane |
| Authority **Checks** | Agent Ingress Gateway, Seer Sidecar | Data plane |
| Kill Switch **Commands** | Agent Lifecycle Manager | Control plane |
| Kill Switch **Execution** | Agent Runtime | Data plane |

## Related

- [Introduction](../introduction.md) — Seer overview
- [Implementation Concepts](../implementation-concepts/) — Conceptual documentation
- [Raw, Trained, Employed Agents](../../../aosm-meta-model/raw-trained-employed-agents.md) — Agent lifecycle model
- [Editorial Review](../EDITORIAL-REVIEW.md) — Documentation review summary

## Related ADRs

- [ADR-0072: Guardrails Two-Layer Model](../../../olympus-hub-docs/decision-logs/0072-seer-guardrails-two-layer-model.md)
- [ADR-0073: Authority Enforcement via OPA](../../../olympus-hub-docs/decision-logs/0073-seer-authority-enforcement-opa.md)
- [ADR-0074: Runtime on Atlantis](../../../olympus-hub-docs/decision-logs/0074-seer-runtime-atlantis-based.md)
- [ADR-0075: Model Gateway (Bifrost)](../../../olympus-hub-docs/decision-logs/0075-seer-model-gateway-bifrost.md)
- [ADR-0076: Observability via Watch](../../../olympus-hub-docs/decision-logs/0076-seer-observability-watch-based.md)
- [ADR-0077: Agent Evaluation Deferred](../../../olympus-hub-docs/decision-logs/0077-seer-evaluation-deferred.md)
