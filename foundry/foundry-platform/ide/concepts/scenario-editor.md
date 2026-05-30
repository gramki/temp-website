# Scenario Editor

The Scenario Editor is a schema-aware YAML editing extension in the Foundry IDE for authoring, validating, and publishing Work Catalog Scenarios.

## What it is

Scenarios define what work a Workspace accepts — they are ingress contracts that specify inputs, outputs, required skills, and task structures. The Scenario Editor provides purpose-built tooling for creating and maintaining these definitions.

Core capabilities:

| Feature | Description |
|---------|-------------|
| **Schema-aware editing** | Autocomplete, type validation, and hover documentation for Scenario YAML |
| **Skill browser** | Browse available skills from registries; insert references |
| **Real-time validation** | Immediate feedback on schema conformance and reference validity |
| **Dry-run execution** | Test Scenarios with mock inputs before publishing |
| **Catalog publishing** | Publish to User catalog or create PRs to team catalogs |

The editor understands Scenario structure:

```yaml
apiVersion: scenario/v1
name: implement-feature
workspace: development
scope: workspace-ingress

inputs:
  - name: specification_id
    type: string
    required: true

outputs:
  - name: implementation_pr_url
    type: string

required-skills:
  - code-generation
  - test-writing

tasks:
  - id: analyze
    type: agent
  - id: implement
    type: agent
    depends-on: [analyze]
```

For each field, the editor provides:

- **Autocomplete** — Valid field names and enumerated values
- **Type checking** — Flags mismatches immediately
- **Hover docs** — Explains field purpose and constraints
- **Quick fixes** — One-click corrections for common errors
- **Skill reference validation** — Verifies skills exist in effective catalog

The Scenario Editor integrates with the Foundry CLI for operations that affect repositories:

| Action | CLI Command | Behavior |
|--------|-------------|----------|
| Validate | `foundry catalog validate` | Schema + reference checks |
| Dry-run | `foundry catalog dry-run` | Execute with mocks, report path |
| Publish (user) | `foundry catalog publish` | Direct push to local catalog |
| Publish (team) | `foundry catalog publish --target <tier>` | Create PR to repository |

## Where it lives in Foundry

| Module | Responsibility |
|--------|----------------|
| **IDE** | Provides the Scenario Editor extension |
| **Work Catalogues** | Stores Scenarios published via the editor |
| **Agent Fabric** | Provides Skill Registry for reference validation |
| **Management** | Owns validation rules enforced by the editor |

Publishing targets follow the [Work Catalog](../../concepts/work-catalog.md) tier structure:

| Target | Repository | Catalog Path | Required Role |
|--------|------------|--------------|---------------|
| User | Local storage | `~/.foundry/catalogs/user/` | Any builder |
| Workbench | Workshop repo | `catalogs/workbench/<id>/` | Workbench Member |
| Workshop | Workshop repo | `catalogs/workshop/` | Workshop Member |
| Foundry | Foundry repo | `catalogs/foundry/` | Foundry Member |

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Scenario](../../concepts/scenario.md) | The artifact the editor creates |
| Work Catalog | Where edited Scenarios are published |
| [Skill](../../concepts/skill.md) | Referenced in `required-skills` field |

From ACE: "Scenarios are the ingress contracts for Workspaces — they define what work a Workspace accepts."

The Scenario Editor operationalizes Scenario authoring, bridging the conceptual definition in ACE to the practical act of creating and maintaining Scenarios in Foundry.

## Related concepts

- [Scenario](../../concepts/scenario.md) — The artifact being edited
- [Work Catalog](../../concepts/work-catalog.md) — Where Scenarios are stored
- [Skill](../../concepts/skill.md) — Referenced by Scenarios, browsable in editor
- [Builder](builder.md) — Who uses the Scenario Editor

## Further reading

- [../user-guide/workspace-sessions.md#scenario-editor](../user-guide/workspace-sessions.md#scenario-editor) — Builder-facing usage guide
- [../platform-developer-guide/extensions.md](../platform-developer-guide/extensions.md) — Extension implementation
- [../../work-catalogues/user-guide/authoring-scenarios.md](../../work-catalogues/user-guide/authoring-scenarios.md) — Complete authoring guide
