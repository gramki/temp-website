# DevOps Workbench

> **Status:** 🟡 WIP — Composite pattern for automating automation development
> **Category:** Composite Patterns

---

## Overview

**DevOps Workbench** is a composite pattern where a dedicated Workbench automates the development activities of Automation Product Owner, Process Architect, and Developer personas. This workbench receives signals from business workbenches (development events, CI/CD events, feedback) and processes them through DevOps Scenarios with AI-assisted agents.

---

## The Premise

Building automation is itself an automation problem.

Every Hub Workbench goes through an Idea → Intent → Charter → Scenario → Application lifecycle. This lifecycle involves:
- **Automation Product Owner** triaging ideas, drafting intents, reviewing feedback
- **Process Architect** reviewing intents, drafting scenarios, generating SOPs
- **Developer** scaffolding applications, diagnosing test failures, managing deployments

These activities are **repetitive, pattern-based, and automatable** — exactly the kind of work Hub was designed to handle.

---

## Pattern Definition

A **DevOps Workbench (D)** is a Workbench that:

1. Is optionally associated with one or more **Business Workbenches (A)**
2. Receives development lifecycle signals from those workbenches via **Atropos**
3. Contains **DevOps Scenarios** that automate Automation Product Owner, Process Architect, and Developer activities
4. Enrolls **AI Assistant Agents** alongside human personas in task queues
5. Operates in its own **IAM domain**, separate from business workbenches

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DEVOPS WORKBENCH PATTERN (BIDIRECTIONAL)                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  BUSINESS WORKBENCHES                       DEVOPS WORKBENCH                │
│                                                                              │
│  ┌─────────────────┐                       ┌─────────────────────────────┐ │
│  │ Dispute-Dev (A) │══════════════════════▶│ Dispute-DevOps (D)          │ │
│  │                 │  Signals (Atropos)    │                             │ │
│  │                 │◀──────────────────────│                             │ │
│  │                 │  Resources (Gateway)  │ ┌─────────────────────────┐ │ │
│  └─────────────────┘                       │ │ APO Scenarios           │ │ │
│                                             │ │ • Idea Triage           │ │ │
│  ┌─────────────────┐                       │ │ • Intent Drafting       │ │ │
│  │ Payments-Dev(A) │══════════════════════▶│ │ • Feedback Review       │ │ │
│  │                 │◀──────────────────────│ └─────────────────────────┘ │ │
│  └─────────────────┘                       │                             │ │
│                                             │ ┌─────────────────────────┐ │ │
│  ┌─────────────────┐                       │ │ PA Scenarios            │ │ │
│  │ Onboard-Dev (A) │══════════════════════▶│ │ • Intent Review         │ │ │
│  │                 │◀──────────────────────│ │ • Scenario Drafting     │ │ │
│  └─────────────────┘                       │ │ • SOP Generation        │ │ │
│                                             │ └─────────────────────────┘ │ │
│                                             │                             │ │
│  ════▶ Signals via Atropos (A → D)         │ ┌─────────────────────────┐ │ │
│  ────▶ Resource access via Gateway (D → A) │ │ Developer Scenarios     │ │ │
│                                             │ │ • App Scaffolding       │ │ │
│                                             │ │ • Test Diagnosis        │ │ │
│                                             │ │ • Build Resolution      │ │ │
│                                             │ └─────────────────────────┘ │ │
│                                             │                             │ │
│                                             │ Machines:                   │ │
│                                             │ • dispute-dev-gateway       │ │
│                                             │ • payments-dev-gateway      │ │
│                                             │ • onboard-dev-gateway       │ │
│                                             └─────────────────────────────┘ │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Workbench Type** | Explicitly marked as `workbench_type: devops` |
| **Scope** | Cross-workbench; can span subscriptions with proper credentials |
| **Ownership** | Tenant owns D; multiple A workbenches can reference same D |
| **Signal Flow** | A → D: Development signals routed via Atropos |
| **Resource Access** | D → A: Query knowledge, memory, data via `{workbench-name}-gateway` |
| **IAM Separation** | D has its own IAM domain; AI agents enrolled in D's queues |
| **Customization** | Tenants can customize all DevOps scenarios |

---

## Platform Provision

Hub Platform provides:

| Asset | Description |
|-------|-------------|
| **Default DevOps Workbench** | One per subscription, using standard scenarios |
| **DevOps Blueprint** | Template for creating custom DevOps workbenches |
| **Standard Scenarios** | Platform-provided scenarios for common DevOps activities |
| **AI Agent Templates** | Pre-configured assistant agents for each persona |

---

## Documents

| Document | Description | Status |
|----------|-------------|--------|
| [DevOps Workbench Reference](./devops-workbench-reference.md) | Cross-workbench association and signal routing (A → D) | 🟡 Draft |
| [DevOps Workbench Binding](./devops-workbench-binding.md) | Bidirectional binding CRDs and operators | 🟡 Draft |
| [Signal Routing via Atropos](./signal-routing-via-atropos.md) | Cross-workbench signal transport and event catalog | 🟡 Draft |
| [DevOps Scenarios](./devops-scenarios.md) | Standard scenarios for all personas | 🟡 Draft |
| [AI Agent Specifications](./ai-agent-specifications.md) | Seer Training Specs for persona assistants | 🟡 Draft |
| [DevOps Blueprint](./devops-blueprint.md) | Template for custom DevOps workbenches | 🔴 Planned |

---

## Why This Pattern?

### 1. Automation at Every Level

Hub's promise is to automate operational workflows. DevOps Workbench extends this promise to the development workflow itself, enabling "automation of automation."

### 2. Clean Separation

By using a separate workbench:
- DevOps activities don't pollute business workbench scope
- AI agents operate in their own IAM domain
- Different domains (HR, Risk, Payments) can share DevOps capabilities

### 3. Tenant Control

Tenants can:
- Use the platform-provided default DevOps workbench
- Create custom DevOps workbenches from the blueprint
- Customize scenarios for domain-specific needs
- Tune AI agent autonomy per scenario

### 4. Cross-Subscription Support

DevOps Workbench can be in a different subscription, enabling:
- Centralized DevOps for multiple business subscriptions
- Shared AI agents across organizational boundaries
- Billing isolation for DevOps resources

---

## Comparison with Other Patterns

| Pattern | Focus | Relationship |
|---------|-------|--------------|
| **Workbench as Machine** | Expose workbench tools to other workbenches | DevOps WB can use this to invoke business WB tools |
| **Scenario as Tool** | Expose scenario as callable tool | DevOps scenarios can invoke business scenarios |
| **DevOps Workbench** | Automate development lifecycle | Receives signals, runs DevOps scenarios |

---

## Related Documentation

### Hub
- [Implementation Concept: DevOps Workbench Reference](../../02-system-design/implementation-concepts/devops-workbench-reference.md)
- [Workbench Management](../../04-subsystems/workbench-management/README.md)
- [Automation Ideation](../../04-subsystems/automation-ideation/README.md)
- [Signal Exchange](../../04-subsystems/signal-exchange/README.md)
- [Atropos (Outbound Signal Gateway)](../../04-subsystems/io-gateways/atropos.md)
- [Admin Operators (DevOps Binding)](../../04-subsystems/operators/admin-operators.md)
- [Idea-to-Deployment Guide](../../10-guides/idea-to-deployment-guide.md)

### Seer
- [Training Spec CRD](../../../olympus-seer-docs/seer-design/hub-integration/training-spec-crd.md)
- [Employment Spec CRD](../../../olympus-seer-docs/seer-design/hub-integration/employment-spec-crd.md)
- [Raw Agent](../../../olympus-seer-docs/seer-design/hub-integration/raw-agent.md)

