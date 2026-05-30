# Scenario

A Scenario is the ingress contract that defines what work a Workspace accepts — a well-defined situation the Workspace is set up to handle, with inputs, expected outcomes, and the workspace it belongs to.

## What it is

Scenarios are not free-form prompts. They are defined entities that specify:

- **Inputs** — What data the Scenario receives (parent item, artifacts, context)
- **Outputs** — What artifacts and state changes the Scenario produces
- **Triggers** — What events can invoke the Scenario
- **Skilled Agent** — What agent capabilities are required
- **Tasks** — What work structure gets created

When a Scenario triggers, it creates one or more [Tasks](task.md). Tasks are the unit of work completed by the Human–Agent Team. An agent doesn't just "run" — it executes a Scenario that creates Tasks, with clear boundaries on what it can do and produce.

Scenarios have a **scope** attribute that determines visibility:

| Scope | Description | Invocable By |
|-------|-------------|--------------|
| `workspace-ingress` | External contract — part of Workspace's public API | Orchestrator, manual trigger |
| `workspace-internal` | Internal implementation detail | Tasks within a Work Order only |

**`workspace-ingress`** Scenarios form the public interface of a Workspace. These are what OI Workflows reference when they say "create a Work Order for Development."

**`workspace-internal`** Scenarios are invoked by Tasks for sub-work that shouldn't be part of the public contract — for example, a "validate imports" scenario called during code implementation.

Scenarios are defined in YAML and stored in the [Work Catalog](work-catalog.md) at the appropriate level (Platform, Foundry, Workshop, Workbench, or User).

## Where it lives in Foundry

| Module | Responsibility |
|--------|----------------|
| **Work Catalog Management** | Schema definition, validation rules |
| **Validation Module** | Validates Scenario YAMLs in PRs |
| **Metadata Service** | Stores and serves Scenario definitions |
| **Orchestrator** | References Scenarios in OI Workflows |
| **WO Runtime** | Reads Scenarios, spawns agents, creates Tasks |

Scenario files live at: `work-catalog/{track}/{oi}/{workspace}/scenarios/{scenario}.yaml`

Example path: `work-catalog/build/product-intent/development/scenarios/implement-feature.yaml`

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Scenario](../../ace/concepts.md#scenarios-and-tasks) | YAML definitions in Work Catalog |
| Workspace ingress contract | `workspace-ingress` scope attribute |
| Task creation | Scenario execution creates Task tree |

From ACE: "A Scenario is a well-defined situation a Workspace is set up to handle — the ingress contract that defines what work a Workspace accepts."

Scenarios are ACE Workspace definitions. They are not UPIM entities; UPIM supplies the orchestration items, artifacts, and evidence that Scenarios read or write.

## Related concepts

- [Task](task.md) — What Scenarios create when they execute
- [Work Order](work-order.md) — Instantiation of a Scenario for execution
- [Work Catalog](work-catalog.md) — Where Scenarios are stored and resolved
- [Agent Model](agent-model.md) — Skilled Agents referenced in Scenario definitions
- [Skill](skill.md) — Capabilities required by Scenarios

## Further reading

- [../management/platform-developer-guide/work-catalog-management/scenario-schema.md](../management/platform-developer-guide/work-catalog-management/scenario-schema.md) — Canonical Scenario YAML schema
- [../work-catalogues/user-guide/authoring-scenarios.md](../work-catalogues/user-guide/authoring-scenarios.md) — How to create Scenarios
- [../management/platform-developer-guide/work-catalog-management/validation-rules.md](../management/platform-developer-guide/work-catalog-management/validation-rules.md) — Validation rules
- [../../ace/concepts.md#scenarios-and-tasks](../../ace/concepts.md#scenarios-and-tasks) — ACE definition
