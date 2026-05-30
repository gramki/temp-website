# Skill

A Skill is a reusable capability package for agents — a published bundle of tools, prompts, and behaviors that can be installed into Workspace Sessions and referenced by Skilled Agent definitions.

## What it is

Skills are how agents gain capabilities beyond their base model. Instead of every Scenario defining how to "write tests" or "review code" from scratch, Skills package these capabilities for reuse:

- **Tools** — MCP servers, CLI commands, APIs the agent can invoke
- **Prompts** — Templates and guidance for agent behavior
- **Resources** — Documentation, examples, reference materials
- **Configuration** — Model preferences, guardrails, limits

Skills follow the Agent Skills specification (similar to Cursor/Claude skills). They are:

- **Packaged** — Bundled for distribution and installation
- **Versioned** — Semver for compatibility management
- **Publishable** — Uploaded to registries for discovery
- **Installable** — Added to Sessions at startup

Skills exist in a two-tier registry:

| Registry | Scope | Contents |
|----------|-------|----------|
| **Global Registry** | Public, platform-wide | Community and vendor skills |
| **Foundry Registry** | Private, Foundry-scoped | Organization-specific skills |

This mirrors the npm public/private registry pattern. Teams can use public skills while developing proprietary capabilities internally.

Skills are **not** Skilled Agents. The distinction:

| Concept | What It Is | Where It Lives |
|---------|------------|----------------|
| **Skill** | Reusable capability package | Skill Registry (published) |
| **Skilled Agent** | Manifest combining skills + guardrails | Workshop/Workbench repo |

A Skilled Agent definition references skills: "This agent needs the `code-review`, `test-writing`, and `jira-integration` skills."

## Where it lives in Foundry

| Component | Responsibility |
|-----------|----------------|
| **Skill Registry** (Agent Fabric) | Stores and serves skill packages |
| **`gh foundry-skill` CLI** | Build, package, publish, install skills |
| **Work Catalog Management** | Validates skill references in Scenarios |
| **WO Runtime** | Installs skills at session start |
| **Workspace Session** | Loaded skills available to agents |

Skill lifecycle:

```
Author Skills → gh foundry-skill build → gh foundry-skill publish → Registry
                                                                       │
Session Start ← gh foundry-skill install ← WO Runtime reads Scenario ←─┘
```

Version resolution happens once at session launch. Pinned versions are recorded for reproducibility — the same Session spec produces the same skill versions.

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Skill](../../ace/concepts.md) | Published packages in Skill Registry |
| Skill Repository (ACE) | Skill Registry service |
| Practitioner Repository | May contain skill guidance and templates |

From ACE/UPIM: The Skill Repository is one of the 15 canonical repository types. Agent Fabric's Skill Registry is the platform service that operationalizes this repository.

Skills are not UPIM entities — they are platform artifacts that enable agents to work effectively within the UPIM-defined work model.

## Related concepts

- [Agent Model](agent-model.md) — Skilled Agents reference Skills
- [Scenario](scenario.md) — Defines required Skills
- [Workspace Session](workspace-session.md) — Where Skills are installed
- [Repositories](repositories.md) — Skill Repository in the taxonomy

## Further reading

- [../agent-fabric/README.md](../agent-fabric/README.md) — Skill Registry overview
- [../agent-fabric/platform-developer-guide/skill-registry.md](../agent-fabric/platform-developer-guide/skill-registry.md) — Registry implementation
- [../agent-fabric/user-guide/authoring-skills.md](../agent-fabric/user-guide/authoring-skills.md) — How to create Skills
- [../../ace/repositories.md](../../ace/repositories.md) — Skill Repository definition
