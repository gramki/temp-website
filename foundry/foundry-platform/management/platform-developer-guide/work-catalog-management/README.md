# Work Catalog Management

**Module scope:** Subsystem of Management — schema definitions, validation, resolution, and agent recommendations for OI Workflows and Scenarios.

## Purpose

The Work Catalog defines what work a Foundry can execute and how it flows through the system. It consists of two components:

- **OI Workflows** — Define how Orchestration Items (Product Intent, Discovery Case, etc.) transition through stages and create Work Orders
- **Scenarios** — Define what work a Workspace can accept and how it should be executed

Without standardized schemas and consistent validation, each Foundry would invent its own formats, making cross-Workspace coordination impossible and agent recommendations unreliable.

Work Catalog Management ensures that every OI Workflow and Scenario in the platform follows a standard structure. When an admin creates either artifact, this subsystem validates that it's well-formed, that referenced scenarios and skills exist, and that the definition can actually be executed. When WO Runtime needs to spawn an agent, this subsystem recommends which Skilled Agent is best suited for the job.

Primary beneficiaries are:
- **Platform/Foundry Admins** (who define OI Workflows with confidence)
- **Workshop/Workbench Admins** (who define Scenarios with confidence)
- **Orchestrator** (which gets validated OI Workflows and uses them to drive PI execution)
- **WO Runtime** (which gets validated Scenarios and recommendations)
- **Users** (who can customize their personal Work Catalog for experimentation)

## What this module does

- **Schema Definition** — Define and version canonical YAML schemas for OI Workflows and Scenarios
- **Validation Logic** — Validate content against schemas and cross-references (OI→Scenario linkage, skill references)
- **Hierarchy Resolution** — Compute effective Work Catalog at any scope (Platform → Foundry → Workshop → Workbench → User)
- **Agent Recommendations** — Match Scenarios to suitable Skilled Agents based on skill requirements
- **User Catalog Activation** — Manage user-level catalog activation (session flag, user profile setting)
- **Sync Coordination** — Coordinate Git sync to Metadata Service registry

## What this module does NOT do

| Boundary | Owned By |
|----------|----------|
| Execute Scenarios | WO Runtime |
| Execute OI Workflows | Orchestrator |
| Store Work Catalog files | Work Catalog Repos (Git) at each level |
| Trigger Scenario execution | Orchestrator (via OI Workflow) |
| Manage Skills | Agent Fabric |
| Store validated artifacts | Metadata Service |
| Define platform default content | work-catalogues module |

## Work Catalog Hierarchy

```
Platform                    ← Platform defaults (shipped with Foundry)
    └── Foundry             ← Foundry-level overrides/additions
        └── Workshop        ← Workshop-level overrides/additions
            └── Workbench   ← Workbench-level overrides/additions
                └── User    ← User-level customizations (requires activation)
```

**Resolution rule:** Closest definition wins. See [resolution-algorithm.md](resolution-algorithm.md) for full details.

**User catalog activation:** User-level customizations require explicit activation via:
- Session flag (opt-in per session)
- User profile setting (persistent preference)

## Architecture

```
┌────────────────────────────────────────────────────────────────────────────────┐
│                          Work Catalog Management                                │
│                                                                                 │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐             │
│  │  Schema Service  │  │   Validation     │  │      Agent       │             │
│  │                  │  │    Service       │  │   Recommender    │             │
│  │ • OI Workflow    │  │ • Validate PRs   │  │ • Match skills   │             │
│  │ • Scenario       │  │ • Check refs     │  │ • Score agents   │             │
│  │ • Versioning     │  │ • OI→Scenario    │  │                  │             │
│  └────────┬─────────┘  └────────┬─────────┘  └────────┬─────────┘             │
│           │                     │                     │                        │
│           └─────────────────────┴─────────────────────┘                        │
│                                 │                                              │
│  ┌──────────────────────────────┴──────────────────────────────────┐          │
│  │                     Resolution Engine                            │          │
│  │  Platform → Foundry → Workshop → Workbench → User (if active)   │          │
│  └──────────────────────────────────────────────────────────────────┘          │
│                                 │                                              │
│                          ┌──────┴──────┐                                       │
│                          │    Cache    │                                       │
│                          │   (Redis)   │                                       │
│                          └─────────────┘                                       │
└────────────────────────────────────────────────────────────────────────────────┘
         │                        │                        │
         ▼                        ▼                        ▼
┌─────────────────┐   ┌────────────────────┐   ┌────────────────────┐
│   Work Catalog  │   │     Metadata       │   │    Orchestrator    │
│  Repo Validation│   │     Service        │   │    + WO Runtime    │
│    Services     │   │    (storage)       │   │   (consumers)      │
└─────────────────┘   └────────────────────┘   └────────────────────┘
```

## Key Services / Components

### Schema Service

Provides canonical schemas for both OI Workflows and Scenarios. Manages schema versions for evolution.

→ [oi-workflow-schema.md](oi-workflow-schema.md) for OI Workflow YAML schema  
→ [scenario-schema.md](scenario-schema.md) for Scenario YAML schema

### Validation Service

Called by Work Catalog Repo validation services to validate files in PRs:

```
POST /api/v1/work-catalog/validate
Body: { type: "oi-workflow" | "scenario", yaml: "...", context: {...} }
Response: { "valid": true, "warnings": [], "errors": [] }
```

| Validation Rule | Applies To | Description |
|-----------------|------------|-------------|
| Schema conformance | Both | YAML matches current schema |
| OI→Scenario linkage | OI Workflow | Referenced scenarios exist in catalog |
| Skill references | Scenario | Referenced skills exist in registry |
| Trigger validity | Scenario | Triggers are recognized types |
| Scope validity | Scenario | `workspace-ingress` or `workspace-internal` |
| Output completeness | Scenario | Declared outputs have producers |

→ [validation-rules.md](validation-rules.md) for comprehensive validation specification

### Resolution Engine

Computes effective Work Catalog for any scope by walking the hierarchy:

```
GET /api/v1/work-catalog/effective?scope=workbench&scope_id=checkout&user_id=alice
Response: {
  "oi_workflows": [...],
  "scenarios": [...],
  "sources": {
    "product-intent-workflow": { "level": "foundry", "source": "acme-foundry" },
    "implement-feature": { "level": "user", "source": "alice-catalog" }
  }
}
```

→ [resolution-algorithm.md](resolution-algorithm.md) for hierarchy resolution details

### Agent Recommender

Suggests Skilled Agents for Scenario execution based on required skills:

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
| Skill match | High | Agent has skills Scenario requires |
| Workspace fit | Medium | Agent configured for this Workspace |
| Success history | Low | Past success rate on similar Scenarios |

## Scenario Scope

Scenarios have a `scope` field that determines their visibility and invocation contract:

| Scope | Description | Invocable By |
|-------|-------------|--------------|
| `workspace-ingress` | External contract for the Workspace | Orchestrator (via OI Workflow), Manual trigger |
| `workspace-internal` | Internal implementation detail | Tasks within a Work Order only |

**`workspace-ingress`** Scenarios form the public interface of a Workspace — what work it accepts. These are referenced in OI Workflows.

**`workspace-internal`** Scenarios are invoked by Tasks (via Skills using Jira MCP) for sub-work that shouldn't be part of the Workspace's public contract.

## ACE Concepts Realized

| Concept | How this subsystem realizes it |
|---------|--------------------------------|
| **OI Workflow** | Defines canonical schema; validates all workflow definitions |
| **Scenario** | Defines canonical schema; validates all scenario definitions |
| **Skill** | Validates skill references; uses skills for agent matching |
| **Workspace** | Scenario schema scopes scenarios to Workspace types |
| **Task** | Schema defines task types (agent, human) and structure |
| **Skilled Agent** | Recommends Skilled Agents based on Scenario requirements |
| **Work Catalog** | Manages the full hierarchy and resolution algorithm |

## Key Design Decisions

- **Work Catalog Management is a subsystem, not a standalone module.** Tightly coupled to Metadata Service (storage), Work Catalog Repo Validation (PR checks), and Work Catalog Sync (parsing) — separating it would create artificial integration boundaries.

- **Schemas are versioned.** Breaking changes increment `apiVersion`; non-breaking additions don't. Enables evolution without disrupting existing definitions.

- **Validation is synchronous.** PR validation must block on validation results — async would create race conditions with merge.

- **OI→Scenario linkage is validated.** OI Workflows can only reference Scenarios that exist in the effective catalog at that scope.

- **User catalogs require activation.** Prevents accidental production impact from experimental Scenarios.

- **Recommendations are advisory, not prescriptive.** WO Runtime can override recommendations; this keeps humans in control of agent selection.

- **Scenario scope is explicit.** `workspace-ingress` vs `workspace-internal` makes the contract boundary clear.

## Open Questions

- OI Workflow versioning — how to track changes over time for audit?
- Scenario A/B testing — multiple versions for experimentation?
- Scenario templates — reusable patterns across Workspaces?
- Recommendation learning — should success history influence future recommendations?
- User catalog isolation — how to prevent cross-user interference?

## Module Documents

| Document | Content |
|----------|---------|
| [oi-workflow-schema.md](oi-workflow-schema.md) | OI Workflow YAML schema (canonical) |
| [scenario-schema.md](scenario-schema.md) | Scenario YAML schema (canonical) |
| [resolution-algorithm.md](resolution-algorithm.md) | Hierarchy resolution implementation |
| [validation-rules.md](validation-rules.md) | CI validation specification |
| [apis.md](apis.md) | REST API specification |
| [sync-mechanism.md](sync-mechanism.md) | Git sync and registry updates |
| [events-and-caching.md](events-and-caching.md) | Events, caching, metrics |
| [requirements.md](requirements.md) | Implementation requirements |
| [scenario-execution-journey.md](scenario-execution-journey.md) | End-to-end Scenario lifecycle |

## Read Next

- [../../work-catalogues/README.md](../../work-catalogues/README.md) — Conceptual overview of Work Catalogs
- [../services/metadata-service.md](../services/metadata-service.md) — Where validated artifacts are stored
- [../services/workshop-validation.md](../services/workshop-validation.md) — How artifacts are validated in PRs
- [../services/workshop-sync.md](../services/workshop-sync.md) — How artifacts are synced to Metadata Service
- [../../orchestrator/README.md](../../orchestrator/README.md) — How Orchestrator consumes OI Workflows
- [../../work-order-runtime/README.md](../../work-order-runtime/README.md) — How WO Runtime consumes Scenarios
- [../../agent-fabric/skilled-agents.md](../../agent-fabric/skilled-agents.md) — Skilled Agent definitions
