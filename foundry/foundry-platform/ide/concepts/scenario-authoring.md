# Scenario Authoring

Scenario Authoring is the IDE journey for scaffolding new Scenario definitions in the builder's **user work catalog** — including ingress and internal trigger types, optional parent/override relationships, and starter files for the skilled agent.

## What it is

Scenarios define what work a Workspace accepts. Most catalog Scenarios are maintained in Foundry, Workshop, or Workbench tiers. **Scenario Authoring** targets the **User** tier: personal definitions that live in `user-work-catalog/` within the workspace folder (backed by the `user-work-catalog-{userId}/` Git repository).

This journey is **not tied to a Work Order**. It creates a folder structure the builder can edit and later publish.

### Trigger types

| Type | `scope` value | Meaning |
|------|---------------|---------|
| **Ingress** | `workspace-ingress` | Orchestrator may invoke via Work Orders; external systems (Jira, webhooks) route through Orchestrator |
| **Internal** | `workspace-internal` | Builder-initiated only; not offered as an Orchestrator ingress contract |

Ingress Scenarios are the contracts the Orchestrator uses when creating Work Orders. Internal Scenarios support ad-hoc or exploratory flows inside the Workspace.

### Parent / override model

When creating a Scenario, the builder may select a **parent Scenario** (template or catalog entry to extend). The scaffold:

- Copies structural defaults from the parent where applicable
- Records override metadata in `scenario.yaml` (e.g. `extends:` reference)
- Does not modify the parent file

Overrides apply only within the user's catalog path until published upstream via PR.

### Scaffold output

The **Create Scenario** command creates a directory under:

```
user-work-catalog/work-catalog/{track}/{oi-type}/{workspace}/scenarios/{scenario-name}/
├── scenario.yaml        # Scenario definition (ingress or internal)
├── skilled-agent.yaml   # Skilled Agent manifest draft
└── agent-skill.md       # Agent skill instructions draft
```

After scaffold, the IDE opens `scenario.yaml` in the [Scenario Editor](scenario-editor.md) for schema-aware editing.

Example `scenario.yaml` stub (ingress):

```yaml
apiVersion: scenario/v1
name: my-feature-flow
description: Builder-authored ingress scenario
workspace: development
scope: workspace-ingress
extends: implement-feature   # optional parent reference

inputs: []
outputs: []
required-skills: []
tasks: []
```

## Where it lives in Foundry

| Module | Responsibility |
|--------|----------------|
| **IDE** | Create Scenario dialog, scaffold files, open editor |
| **WO Runtime** | Optional validation hook; does not own catalog Git writes |
| **Work Catalogues** | Schema, validation, publish workflow |
| **Management** | User catalog repo provisioning (`user-work-catalog-{userId}/`) |

Publishing from the user catalog uses the standard Work Catalog publish path (direct push to user repo or PR to team tier). See [authoring-scenarios](../../work-catalogues/user-guide/authoring-scenarios.md).

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Scenario](../../concepts/scenario.md) | Artifact produced by this journey |
| [Work Catalog](../../concepts/work-catalog.md) | User tier storage and resolution |
| [Skill](../../concepts/skill.md) | Referenced in `required-skills` and `agent-skill.md` |

From ACE: "Scenarios are the ingress contracts for Workspaces." Scenario Authoring lets builders experiment at the User layer without changing team catalogs.

## Related concepts

- [Scenario Editor](scenario-editor.md) — Editing scaffolded YAML
- [Workspace Folder Structure](workspace-folder-structure.md) — `user-work-catalog/` location
- [Foundry Workspace Panel](foundry-workspace-panel.md) — Workspace context while authoring
- [Builder](builder.md) — Who runs the journey

## Further reading

- [../platform-developer-guide/ux-requirements.md](../platform-developer-guide/ux-requirements.md) — IDE-UX-091 to IDE-UX-098
- [../../work-catalogues/user-guide/authoring-scenarios.md](../../work-catalogues/user-guide/authoring-scenarios.md) — Full authoring guide
- [../../work-order-runtime/platform-developer-guide/ide-integration.md](../../work-order-runtime/platform-developer-guide/ide-integration.md) — Create Scenario API
