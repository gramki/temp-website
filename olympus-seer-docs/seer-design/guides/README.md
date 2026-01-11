# Seer Design Guides

> **Audience**: Agent Developers, Domain Stewards, Tenant Admins  
> **Purpose**: Practical guidance for building and operating Seer agents

---

## Available Guides

| Guide | Audience | Description |
|-------|----------|-------------|
| [Agent Development Lifecycle](./agent-development-lifecycle.md) | Engineers, Architects, Stewards | Complete guide to conceiving, training, evaluating, and employing agents |
| [Agent Lifecycle FAQ](./agent-lifecycle-faq.md) | Architects, Developers | Common questions about agent development, CRDs, and naming conventions |
| [Guardrails Best Practices](./guardrails-best-practices.md) | Developers, Stewards, Admins | Effective guardrail design, configuration, and governance |

---

## Quick Reference

### Key Concepts

- **Deploy = Employ**: In Seer, deploying an agent means employing it to a Workbench Instance
- **seerTrainingRef**: Canonical way to reference TrainingSpec from HubApplicationSpec
- **Lifecycle Stages**: dev → build → staging → production (via labels)

### CRD Chain

```
ScenarioNormativeSpec → ScenarioAutomationSpec → ScenarioDeploymentSpec
                              │
                              ▼
                        HubApplicationSpec ──► TrainingSpec
                              │
                              ▼ (generated)
                        HubApplicationDeployment
                              │
                              ▼ (generated)
                        EmploymentSpec
```

See [Agent Lifecycle FAQ](./agent-lifecycle-faq.md) for detailed explanations.

---

## Coming Soon

- Context Assembly Patterns
- Testing and Evaluation Deep Dive
- Multi-Agent Orchestration Patterns

---

*See [Seer Design](../README.md) for technical specifications and subsystem documentation.*

