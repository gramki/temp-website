# Seer Journeys

This folder contains journeys specific to agentic automation — the Seer extension to Hub's conventional automation journeys.

## Journeys

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
│ Scenario Development    │         │ (uses Hub base)         │
│ Workbench Configuration │         │                         │
│ Request Lifecycle       │         │                         │
└─────────────────────────┘         └─────────────────────────┘
```

## Fork Point

The decision between conventional and agentic automation happens during Stage 2 (Design) of the Automation Lifecycle:

1. **APO** proposes automation approach
2. **Process Architect** validates feasibility
3. If agentic: **CSA** validates cognitive suitability, **ARAO** approves autonomy
4. Scenario transitions to appropriate lifecycle

See: [Automation Approach Decision](../../../../olympus-hub-docs/08-personas-and-journeys/journeys/automation-lifecycle.md#automation-approach-decision)

