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
- [Agent Observability](./subsystems/agent-observability.md) — SDK, Watch integration
- [Agent Evaluation Service](./subsystems/agent-evaluation.md) — PARKED (post-MVP)
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

## Personas & Roles

Enterprise roles for building and operating Agent-Oriented Systems:

- [Role Definitions](./personas-and-needs/roles.md) — All 7 enterprise personas
- [Agent Product Owner (APO)](./personas-and-needs/apo.md) — Intent and business accountability
- [Cognitive Systems Architect (CSA)](./personas-and-needs/csa.md) — Cognitive design and patterns
- [Agent Engineer (AE)](./personas-and-needs/ae.md) — Implementation and testing
- [Knowledge & Memory Owner (KMO)](./personas-and-needs/kmo.md) — Knowledge curation and memory governance
- [Agent Reliability Engineer (ARE)](./personas-and-needs/are.md) — Operations and reliability
- [Cognitive Operations Steward (COS)](./personas-and-needs/cos.md) — Cognitive health monitoring
- [AI Risk & Audit Owner (ARAO)](./personas-and-needs/arao.md) — Compliance and audit

### Production Readiness

- [Production Readiness](./personas-and-needs/needs/production-readiness.md) — What it takes to be production-ready
- [Production Readiness Checklist](./personas-and-needs/needs/production-readiness-checklist.md) — Gate checklist
- [AE Deliverables to ARE](./personas-and-needs/ae-deliverables-to-are.md) — Build-operate handoff contract

## UX Architecture

Applications and channels for enterprise personas:

- [UX Architecture Overview](./ux-architecture/README.md) — Desks and channels
- [Desk Requirements](./ux-architecture/desk-requirements.md) — Requirements for all persona desks

## Guides

Practical guidance for building and operating Seer agents:

- [Guides Overview](./guides/README.md)
- [Guardrails Best Practices](./guides/guardrails-best-practices.md) — Effective guardrail design, configuration, governance

## Background

- [Requirements: Enterprise Agentic Platform](../requirements-enterprise-agentic-platform/README.md)
- [AOSM Meta-Model](../../aosm-meta-model/agent-oriented-system.md)
- [Raw, Trained, Employed Agents](../../aosm-meta-model/raw-trained-employed-agents.md)
- [Agentic AI Concepts](../agentic-ai-concepts/)
