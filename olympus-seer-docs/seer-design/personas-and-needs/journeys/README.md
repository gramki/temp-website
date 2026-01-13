# Seer Journeys

This folder contains journeys specific to agentic automation — the Seer extension to Hub's conventional automation journeys.

## Critical Journeys

The following 8 journeys are critical for Seer Agent Development, Administration, and Evolution:

| Priority | Journey | Primary Personas | Frequency |
|----------|---------|------------------|-----------|
| 1 | [New Agent Development](./new-agent-development.md) | APO, CSA, AE, ARE, ARAO | High |
| 2 | [Production Deployment](./production-deployment.md) | AE, ARE, CSA | High |
| 3 | [Agent Incident Response](./agent-incident-response.md) | ARE, COS, AE, APO | Medium |
| 4 | [Agent Evolution from Feedback](./agent-evolution-from-feedback.md) | COS, APO, CSA, AE, KMO | Ongoing |
| 5 | [Autonomy Level Upgrade](./autonomy-level-upgrade.md) | APO, ARAO, ARE, COS | Medium |
| 6 | [Behavioral Drift Investigation](./behavioral-drift-investigation.md) | COS, AE, CSA, KMO | Medium |
| 7 | [Enterprise Learning Promotion](./enterprise-learning-promotion.md) | COS, KMO, APO | Medium |
| 8 | [Compliance Audit](./compliance-audit.md) | ARAO, APO, ARE, COS, AE | Low (scheduled) |

## Journey Categories

### Development Journeys

| Journey | Description |
|---------|-------------|
| [New Agent Development](./new-agent-development.md) | End-to-end agent creation from charter to production |
| [Production Deployment](./production-deployment.md) | Deploying agent versions to production |

### Operations Journeys

| Journey | Description |
|---------|-------------|
| [Agent Incident Response](./agent-incident-response.md) | Responding to operational and cognitive incidents |
| [Behavioral Drift Investigation](./behavioral-drift-investigation.md) | Investigating and resolving behavioral drift |

### Evolution Journeys

| Journey | Description |
|---------|-------------|
| [Agent Evolution from Feedback](./agent-evolution-from-feedback.md) | Continuous improvement from operational feedback |
| [Enterprise Learning Promotion](./enterprise-learning-promotion.md) | Promoting learnings through memory hierarchy |

### Governance Journeys

| Journey | Description |
|---------|-------------|
| [Autonomy Level Upgrade](./autonomy-level-upgrade.md) | Upgrading agent autonomy levels |
| [Compliance Audit](./compliance-audit.md) | Auditing agent compliance |

## Existing Journeys

| Journey | Description |
|---------|-------------|
| [Agentic Automation Lifecycle](./agentic-automation-lifecycle.md) | Complete lifecycle for AI agents, extending Hub's [Automation Lifecycle](../../../../olympus-hub-docs/08-personas-and-journeys/journeys/automation-lifecycle.md) |

## Relationship to Hub Journeys

Seer journeys **extend** Hub journeys rather than replace them. The base flow is defined in Hub, and Seer adds agentic-specific activities and personas.

```
Hub Journeys (Conventional)          Seer Journeys (Agentic)
┌─────────────────────────┐         ┌─────────────────────────┐
│ Automation Lifecycle    │ ◀─────▶ │ Agentic Automation      │
│ (conventional)          │ extends │ Lifecycle               │
├─────────────────────────┤         ├─────────────────────────┤
│ Scenario Development    │         │ New Agent Development   │
│ Workbench Configuration │         │ Production Deployment   │
│ Request Lifecycle       │         │ Incident Response       │
│                         │         │ ... and more            │
└─────────────────────────┘         └─────────────────────────┘
```

## Fork Point

The decision between conventional and agentic automation happens during Stage 2 (Design) of the Automation Lifecycle:

1. **APO** proposes automation approach
2. **Process Architect** validates feasibility
3. If agentic: **CSA** validates cognitive suitability, **ARAO** approves autonomy
4. Scenario transitions to appropriate lifecycle

See: [Automation Approach Decision](../../../../olympus-hub-docs/08-personas-and-journeys/journeys/automation-lifecycle.md#automation-approach-decision)

## Journey Coverage by Persona

| Persona | Journeys |
|---------|----------|
| **APO** | New Agent Development, Autonomy Level Upgrade, Agent Evolution from Feedback, Compliance Audit |
| **CSA** | New Agent Development, Behavioral Drift Investigation, Agent Evolution from Feedback |
| **AE** | New Agent Development, Production Deployment, Agent Incident Response, Behavioral Drift Investigation, Agent Evolution from Feedback, Compliance Audit |
| **KMO** | Enterprise Learning Promotion, Behavioral Drift Investigation, Agent Evolution from Feedback |
| **ARE** | New Agent Development, Production Deployment, Agent Incident Response, Autonomy Level Upgrade, Compliance Audit |
| **COS** | Agent Incident Response, Behavioral Drift Investigation, Enterprise Learning Promotion, Autonomy Level Upgrade, Agent Evolution from Feedback, Compliance Audit |
| **ARAO** | New Agent Development, Autonomy Level Upgrade, Compliance Audit |

## OPDA Alignment

All journeys support the OPDA framework:

| Journey | O | P | D | A |
|---------|---|---|---|---|
| New Agent Development | ✅ | ✅ | ✅ | ✅ |
| Production Deployment | ✅ | ✅ | ✅ | — |
| Agent Incident Response | ✅ | ✅ | ✅ | — |
| Agent Evolution from Feedback | ✅ | ✅ | ✅ | ✅ |
| Autonomy Level Upgrade | ✅ | ✅ | ✅ | ✅ |
| Behavioral Drift Investigation | ✅ | ✅ | ✅ | — |
| Enterprise Learning Promotion | ✅ | ✅ | ✅ | ✅ |
| Compliance Audit | ✅ | ✅ | ✅ | ✅ |

O = Observable, P = Predictable, D = Directable, A = Authority Enforceable