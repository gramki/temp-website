# Scenario Management

**Module scope:** Subsystem of Management — scenario schema, validation, and agent recommendations.

## Purpose

Scenarios are the bridge between "what needs to happen" (orchestration) and "how it gets done" (execution). Without a consistent way to define and validate scenarios, each Workspace would invent its own format, making cross-Workspace coordination impossible and agent recommendations unreliable.

Scenario Management ensures that every scenario in the platform follows a standard structure. When a Workshop admin creates a scenario, this subsystem validates that it's well-formed, that referenced skills exist, and that the scenario can actually be executed. When WO Runtime needs to spawn an agent, this subsystem recommends which Skilled Agent is best suited for the job.

Primary beneficiaries are Workshop/Workbench Admins (who define scenarios with confidence), WO Runtime (which gets validated scenarios and recommendations), and Orchestrator (which relies on consistent trigger definitions to create Work Orders).

## What this module does

- **Schema Definition** — define and version the canonical YAML schema for scenario definitions
- **Validation Logic** — validate scenario content against schema and cross-references
- **Agent Recommendations** — match scenarios to suitable Skilled Agents based on skill requirements
- **Effective Resolution** — compute merged scenario (Workshop base + Workbench override)

## What this module does NOT do

| Boundary | Owned By |
|----------|----------|
| Execute scenarios | WO Runtime |
| Store scenario files | Workshop Definition Repo (Git) |
| Trigger scenario execution | Orchestrator |
| Manage skills | Agent Fabric |
| Store validated scenarios | Metadata Service |
| Define scenario templates | Scenario Catalogue (content folder) |

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        Scenario Management                                   │
│                                                                             │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐             │
│  │  Schema Service │  │   Validation    │  │     Agent       │             │
│  │                 │  │    Service      │  │  Recommender    │             │
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘             │
│           │                    │                    │                       │
│           └────────────────────┴────────────────────┘                       │
│                                │                                            │
└────────────────────────────────┼────────────────────────────────────────────┘
                                 │
           ┌─────────────────────┼─────────────────────┐
           │                     │                     │
           ▼                     ▼                     ▼
┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐
│    Workshop     │   │    Metadata     │   │   WO Runtime    │
│   Validation    │   │    Service      │   │ (recommendations)│
└─────────────────┘   └─────────────────┘   └─────────────────┘
```

## Key Services / Components

### Schema Service

Provides the canonical schema for scenario definitions. Manages schema versions for evolution.

→ [scenario-schema.md](scenario-schema.md) for the full YAML schema specification

### Validation Service

Called by Workshop Validation Service to validate scenario files in PRs:

```
POST /api/v1/scenarios/validate
Body: { scenario_yaml: "..." }
Response: { "valid": true, "warnings": [], "errors": [] }
```

| Validation Rule | Description |
|-----------------|-------------|
| Schema conformance | YAML matches current schema |
| Task structure | Tasks have valid types and fields |
| Skill references | Referenced skills exist in registry |
| Trigger validity | Triggers are recognized types |
| Output completeness | Declared outputs have producers |

### Agent Recommender

Suggests Skilled Agents for scenario execution based on required skills:

```
GET /api/v1/scenarios/{id}/recommendations
Response: {
  "recommendations": [
    { "skilled_agent_id": "sa-code-impl", "score": 0.95, "reason": "Has required skills" }
  ]
}
```

| Factor | Weight | Description |
|--------|--------|-------------|
| Skill match | High | Agent has skills scenario requires |
| Workspace fit | Medium | Agent configured for this Workspace |
| Success history | Low | Past success rate on similar scenarios |

## Effective Scenario Resolution

Scenarios can be defined at Workshop level (defaults) and overridden at Workbench level:

```
Workshop: workspaces/development/scenarios/create-feature.yaml
Workbench: workbenches/checkout/workspaces/development/scenarios/create-feature.yaml
```

Resolution rules:
1. If Workbench defines scenario, use Workbench version
2. Otherwise, use Workshop version
3. `catalog.yaml` files are **merged** (both Workshop and Workbench scenarios available)

## ACE Concepts Realized

| Concept | How this subsystem realizes it |
|---------|--------------------------------|
| **Scenario** | Defines the standard schema; validates all scenario definitions |
| **Skill** | Validates skill references; uses skills for agent matching |
| **Workspace** | Scenario schema scopes scenarios to Workspace types |
| **Task** | Schema defines task types (agent, human) and structure |
| **Skilled Agent** | Recommends Skilled Agents based on scenario requirements |

## Key Design Decisions

- **Scenario Management is a subsystem, not a standalone module.** Tightly coupled to Metadata Service (storage), Workshop Validation (PR checks), and Workshop Sync (parsing) — separating it would create artificial integration boundaries.
- **Schema is versioned.** Breaking changes increment `apiVersion`; non-breaking additions don't. Enables evolution without disrupting existing scenarios.
- **Validation is synchronous.** PR validation must block on scenario validation results — async would create race conditions with merge.
- **Recommendations are advisory, not prescriptive.** WO Runtime can override recommendations; this keeps humans in control of agent selection.
- **Effective resolution merges, not replaces.** Workbench-specific scenarios add to Workshop defaults rather than hiding them — prevents accidental scenario loss.

## Open Questions

- Scenario versioning — how to track changes over time for audit?
- A/B testing scenarios — multiple versions for experimentation?
- Scenario templates — reusable patterns across Workspaces?
- Recommendation learning — should success history influence future recommendations?

## Module Documents

| Document | Content |
|----------|---------|
| [requirements.md](requirements.md) | Implementation requirements (APIs, database, observability) |
| [scenario-execution-journey.md](scenario-execution-journey.md) | End-to-end scenario lifecycle walkthrough |
| [scenario-schema.md](scenario-schema.md) | Full YAML schema with examples |

## Read Next

- [../services/metadata-service.md](../services/metadata-service.md) — Where validated scenarios are stored
- [../services/workshop-validation.md](../services/workshop-validation.md) — How scenarios are validated in PRs
- [../services/workshop-sync.md](../services/workshop-sync.md) — How scenarios are synced to Metadata Service
- [../../scenario-catalogue/README.md](../../scenario-catalogue/README.md) — Reference scenario templates
- [../../agent-fabric/skilled-agents.md](../../agent-fabric/skilled-agents.md) — Skilled Agent definitions
- [../../orchestrator/README.md](../../orchestrator/README.md) — How orchestrator triggers scenarios
