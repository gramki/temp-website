# Skilled Agent

A Skilled Agent is a declarative manifest that binds a Capable Agent to a specific (Workspace, Scenario) context with configured skills, guardrails, and compatible agent preferences.

## What it is

Skilled Agents represent the definition layer of Foundry's three-tier agent model. They are configuration, not running processes — YAML manifests stored in Workshop or Workbench repositories that define how an agent should behave in a specific context.

A Skilled Agent manifest (`agent.yaml`) specifies:

- **Compatible Capable Agents** — Which agent systems can execute this, in preference order
- **Skills** — References to skill packages from the registry (by name and version)
- **Guardrails** — Behavioral constraints (prohibitions, requirements, limits, scope restrictions)
- **Evaluation criteria** — Metrics and golden datasets for measuring agent performance

```yaml
name: feature-implementation-agent
compatible-capable-agents:
  - agent: cursor-agent
    models: [claude-opus, claude-sonnet]
  - agent: copilot
    models: [gpt-5-thinking]
skills:
  - name: code-generator
    version: ^2.1.0
    registry: foundry
guardrails:
  - no-force-push
  - require-tests-for-new-code
  - max-file-changes: 50
```

Skilled Agents follow the Workshop → Workbench inheritance model. Workbench-level definitions override Workshop-level definitions entirely (no merge). This allows teams to define sensible defaults at the Workshop level while allowing product-specific customization.

Skills are NOT stored in the repository. The manifest references skills by name and version; actual skill packages are fetched from the Skill Registry at session start.

## Where it lives in Foundry

| Component | Responsibility |
|-----------|----------------|
| **Workshop Definition Repo** | Stores Workshop-level Skilled Agent manifests |
| **Workbench section** | Stores Workbench-level overrides |
| **Work Catalog Management** | Validates skill references exist |
| **WO Runtime** | Reads manifest, selects Capable Agent, spawns instance |

Folder structure within Scenarios:

```
workspaces/{workspace}/scenarios/{scenario}/
├── scenario.yaml
└── skilled-agent/
    ├── agent.yaml          # The Skilled Agent manifest
    ├── guardrails/         # Optional guardrail overrides
    └── eval/               # Optional evaluation data
```

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Agent](../../../ace/concepts.md) | Skilled Agent configures how capabilities are applied |
| [Skill](../../../ace/concepts.md) | Skills referenced by name from Skill Registry |
| Guardrail | Behavioral constraints defined per Skilled Agent |

Skilled Agents bridge the gap between generic agent capabilities (Capable Agents) and specific work contexts (Scenarios). They apply ACE's concept of agent configuration to Foundry's operational model.

## Related concepts

- [Agent Model](../../concepts/agent-model.md) — Three-tier hierarchy that includes Skilled Agents
- [Capable Agent](capable-agent.md) — Systems that Skilled Agents reference
- [Employed Agent](employed-agent.md) — Runtime instances spawned from Skilled Agent definitions
- [Skill](../../concepts/skill.md) — Capability packages that Skilled Agents reference
- [Scenario](../../concepts/scenario.md) — Context where Skilled Agents operate

## Further reading

- [../platform-developer-guide/skilled-agents.md](../platform-developer-guide/skilled-agents.md) — Schema reference, guardrails, evaluation
- [../user-guide/skilled-agents.md](../user-guide/skilled-agents.md) — How to create Skilled Agent manifests
- [../platform-developer-guide/skill-registry.md](../platform-developer-guide/skill-registry.md) — Skill packaging and publishing
