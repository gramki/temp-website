# Olympus Seer Design

This folder contains the design documents for **Olympus Seer** (Seer) — Zeta's enterprise agentic AI platform.

> *Seer is the Agent Lifecycle & Runtime Engine — the control plane and runtime for enterprise AI agents.*

## Design Documents

- [Introduction](./introduction.md) — Seer & Hub in the Enterprise Agent Platform; subsystem overview

## Subsystems

- [Subsystems Overview](./subsystems/README.md)
- [Agent Definition & Lifecycle Service](./subsystems/agent-lifecycle-service.md)
- [Agent Lifecycle API](./subsystems/agent-lifecycle-api.md) — REST API, kill switch, webhooks
- [Guardrails](./subsystems/guardrails.md) — Behavioral guidelines, sidecar enforcement, Python contract
- [Authority Enforcement](./subsystems/authority-enforcement.md) — OPA policies, Tool Gateway, Signal Exchange
- [Agent Identity & Authority Framework](./subsystems/agent-identity-authority.md)
- [Context Assembly Engine](./subsystems/context-assembly-engine.md) — Compile API, retrievers, token budgeting
- [Runtime & Deployment Abstraction](./subsystems/runtime-deployment.md)
- [Observability & Evaluation Service](./subsystems/observability-evaluation.md)
- [Model Gateway](./subsystems/model-gateway.md)

## Hub Integration

How Seer agents operate within the Hub ecosystem:

- [Hub Integration Overview](./hub-integration/README.md) — Seer as Hub Application Runtime
- [Raw Agent in Hub Context](./hub-integration/raw-agent.md) — Container requirements, framework flexibility
- [Trained Agent as Hub Application](./hub-integration/trained-agent.md) — HubApplicationSpec ↔ TrainingSpec
- [Employed Agent as Deployed Application](./hub-integration/employed-agent.md) — ScenarioDeployment ↔ EmploymentSpec
- [Request Dispatch](./hub-integration/request-dispatch.md) — Signal Exchange → Runtime → Agent flow
- [Memory Integration](./hub-integration/memory-integration.md) — Agent Memory Services in Seer context
- [Context Assembly](./hub-integration/context-assembly.md) — CAE invocation patterns

### CRD Specifications

- [Training Spec CRD](./hub-integration/training-spec-crd.md) — Full TrainingSpec schema
- [Employment Spec CRD](./hub-integration/employment-spec-crd.md) — Full EmploymentSpec schema

## Guides

Practical guidance for building and operating Seer agents:

- [Guides Overview](./guides/README.md)
- [Guardrails Best Practices](./guides/guardrails-best-practices.md) — Effective guardrail design, configuration, governance

## Background

- [Requirements: Enterprise Agentic Platform](../requirements-enterprise-agentic-platform/README.md)
- [AOSM Meta-Model](../../aosm-meta-model/agent-oriented-system.md)
- [Raw, Trained, Employed Agents](../../aosm-meta-model/raw-trained-employed-agents.md)
- [Agentic AI Concepts](../agentic-ai-concepts/)
