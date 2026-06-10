# Agent Fabric

**Module scope:** Agent infrastructure — Raw Agent Registry, Swarm Registry, Skill Registry, quota enforcement, gateway policy, usage analytics.

## Purpose

Agent Fabric provides the infrastructure layer that enables AI-powered automation at scale. It answers the questions: which agent systems are available? how are agents organized? what skills do they have? how much can they cost? how do we track what they do?

Without Agent Fabric, each team would need to independently manage agent configurations, handle model access, track costs, and publish capabilities. This creates inconsistency, security risks, and cost overruns. Agent Fabric centralizes these concerns while allowing customization at Workshop and Workbench levels.

The module follows the "provide policy, not operations" principle. It doesn't run LLM gateways — it configures them. It doesn't execute agents — it provides the registries, skills, and configuration that WO Runtime uses to spawn them. This separation keeps the module focused on governance and enablement rather than execution.

## What this module does

- **Raw Agent Registry** — OCI container catalog for agent systems; two-layer model (platform-shipped + tenant-added)
- **Swarm Registry** — Organizational units for Trained Agents; scoped at Foundry, Workshop, Workbench, Workspace
- **Skill Registry** — Global and Foundry-scoped registries for publishable skill packages
- **Skill CLI Tooling** — `gh foundry-skill` extensions for build, package, publish, install
- **Quota Management** — Configurable limits at Foundry, Workbench, and User levels
- **Gateway Policy** — Configuration for OSS LLM gateway (quota enforcement, routing, audit)
- **Usage Analytics** — Skill invocation metrics, cost attribution, automation coverage

## What this module does NOT do

- **Does not spawn agents** — WO Runtime spawns Employed Agents in Workspace Sessions
- **Does not execute tasks** — WO Runtime manages task execution
- **Does not run the LLM gateway** — Module provides policy; ops teams run LiteLLM/Portkey/etc.
- **Does not manage Work Orders** — Orchestrator creates WOs; WO Runtime executes them
- **Does not store artifacts** — Skills are packages in the registry; execution artifacts go to repositories

## Architecture

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                               Agent Fabric                                    │
│                                                                               │
│  ┌──────────────────────────────┐  ┌──────────────────────────────────────┐  │
│  │     Raw Agent Registry       │  │          Swarm Registry              │  │
│  │                              │  │                                      │  │
│  │  Platform-shipped:           │  │  Platform-shipped:                   │  │
│  │  • Codex, Cursor Agent,     │  │  • Build, Review, Test,             │  │
│  │    Claude Code               │  │    Documentation, Release,          │  │
│  │                              │  │    Governance                        │  │
│  │  Tenant-added:              │  │                                      │  │
│  │  • Custom OCI agents        │  │  Tenant-added/extended:             │  │
│  │                              │  │  • Custom Swarms + extensions       │  │
│  └──────────────────────────────┘  └──────────────────────────────────────┘  │
│                                                                               │
│  ┌──────────────────────────────┐  ┌──────────────────────────────────────┐  │
│  │      Skill Registry          │  │         Quota Management             │  │
│  │                              │  │                                      │  │
│  │  Global (public)             │  │  Foundry │ Workbench │ User limits  │  │
│  │  Foundry (private)           │  │  Effective = min(all levels)        │  │
│  │  CLI: gh foundry-skill       │  │                                      │  │
│  └──────────────────────────────┘  └──────────────────────────────────────┘  │
│                                                                               │
│  ┌──────────────────────────────┐  ┌──────────────────────────────────────┐  │
│  │      Usage Analytics         │  │       Gateway Policy Layer           │  │
│  │                              │  │                                      │  │
│  │  Invocations, cost,          │  │  Quota enforcement │ Delegation     │  │
│  │  automation coverage,        │  │  Credential injection │ Audit       │  │
│  │  failure rates               │  │                                      │  │
│  └──────────────────────────────┘  └──────────────────────────────────────┘  │
│                                                                               │
└───────────────────────────────────────────────────────────────────────────────┘
                                     │
                                     ▼
                          ┌─────────────────────┐
                          │   OSS LLM Gateway   │
                          │  (LiteLLM/Portkey/  │
                          │   Helicone)         │
                          └─────────────────────┘
```

## Key Services

| Service | Role | Specification |
|---------|------|---------------|
| **Raw Agent Registry** | OCI container catalog with two-layer distribution (platform + tenant) | [raw-agent-registry.md](platform-developer-guide/raw-agent-registry.md) |
| **Swarm Registry** | Trained Agent organizational units with scope hierarchy | [swarm-registry.md](platform-developer-guide/swarm-registry.md) |
| **Skill Registry** | Global + Foundry-scoped registries for skill packages | [skill-registry.md](platform-developer-guide/skill-registry.md) |
| **Quota Management** | Configurable limits at Foundry, Workbench, and User levels | [gateway-policy.md](platform-developer-guide/gateway-policy.md) |
| **Gateway Policy** | Configuration for OSS LLM gateway (quota, routing, audit) | [gateway-policy.md](platform-developer-guide/gateway-policy.md) |
| **Usage Analytics** | Skill invocation metrics, cost attribution, automation coverage | [requirements.md](platform-developer-guide/requirements.md) |

## Agent Model

The module manages a three-tier agent model:

```
┌─────────────────────────────────────────────────────────────────┐
│  Packaging Layer                                                 │
│  Raw Agent: OCI container (Codex, Cursor Agent, Claude Code)    │
│  URI: registry.foundry.io/raw-agents/{agent}:{version}          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ referenced by
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Configuration Layer                                             │
│  Trained Agent: Manifest with skills, guardrails, Swarm member  │
│  JID: {agent}@{swarm}.agents.{tenant}.foundry.io                │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ instantiated as
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Runtime Layer                                                   │
│  Employed Agent: Trained Agent + Delegation Token               │
│  (Delegated authority, quota-bound, session-scoped)             │
└─────────────────────────────────────────────────────────────────┘
```

| Concept | What It Is | Where It Lives |
|---------|------------|----------------|
| **Raw Agent** | OCI container packaging an agent system | Raw Agent Registry |
| **Trained Agent** | Manifest combining Raw Agent ref + skills + guardrails; belongs to a Swarm | `swarms/{swarm}/trained-agents/` |
| **Employed Agent** | Runtime instance (Trained Agent + Delegation Token) | Workspace Session |
| **Swarm** | Organizational unit for Trained Agents (like an OU) | Swarm Registry |
| **Skill** | Reusable capability package | Skill Registry (published) |

## Swarm Organization

Swarms are organizational units for Trained Agents — analogous to OUs for human users:

```
Organization
├── Human OUs
│   ├── Engineering Team
│   ├── QA Team
│   └── DevOps Team
└── Agent Swarms
    ├── Build Swarm (feature-implementer, code-refactorer, test-writer)
    ├── Review Swarm (code-reviewer, security-reviewer)
    ├── Test Swarm (test-executor, test-analyzer)
    ├── Documentation Swarm (doc-writer, changelog-generator)
    ├── Release Swarm (release-preparer, deployment-validator)
    └── Governance Swarm (policy-reviewer, compliance-checker)
```

Swarm scopes form a visibility hierarchy:

| Scope | Visible To | Managed By |
|-------|------------|------------|
| **Foundry Swarm** | All Workshops, Workbenches, Workspaces | Foundry Admin |
| **Workshop Swarm** | Workshop and its Workbenches/Workspaces | Workshop Manager |
| **Workbench Swarm** | That Workbench and its Workspaces | Workbench Manager |
| **Workspace Swarm** | That Workspace only | Workspace Owner |

## Two-Layer Distribution

Both Raw Agents and Swarms follow a two-layer distribution model:

| Layer | Raw Agents | Swarms |
|-------|------------|--------|
| **Platform-shipped** | `registry.foundry.io/raw-agents/codex:v2.4.1` | Build, Review, Test, Documentation, Release, Governance |
| **Tenant-extended** | N/A | Add Trained Agents to platform Swarms |
| **Tenant-added** | `registry.{tenant}.foundry.io/raw-agents/...` | Organization-specific at Foundry/Workshop/Workbench/Workspace scope |

## ACE Concepts Realized

| Concept | How Agent Fabric realizes it |
|---------|------------------------------|
| **Agent** | Manages Raw Agent, Trained Agent, Employed Agent hierarchy |
| **Skill** | Packages capabilities following Agent Skills spec |
| **Delegation** | Provides delegation token infrastructure for Employed Agents |
| **Scenario** | Scenarios reference Swarms; coordinator explicitly specified |
| **Team** | Swarms organize agents analogously to human OUs |

## Key Design Decisions

- **Three-tier model.** Raw (packaging) → Trained (configuration) → Employed (runtime) separates concerns cleanly.
- **Swarms as OUs.** No lifecycle states — Swarms are static groupings that organize Trained Agents by function.
- **Single Swarm membership.** Each Trained Agent belongs to exactly one Swarm (hard constraint).
- **Two registries.** Raw Agent Registry (OCI catalog) + Swarm Registry (organizational structure) are distinct services.
- **Two-layer distribution.** Platform ships standard agents and Swarms; tenants extend or add their own.
- **JID identity.** Trained Agents use Jabber JID notation: `{agent}@{swarm}.agents.{tenant}.foundry.io`.
- **Skills are packages, Trained Agents are manifests.** Skills are published to registries; Trained Agents are configuration that reference skills.
- **OSS gateway, not built.** Use LiteLLM or similar; module provides policy, not operations.
- **Quota at three levels.** Foundry, Workbench, User intersections. Workshop level deferred.
- **Auto-fallback enabled.** Model/agent fallback when preferred option unavailable.
- **Recoverable failures.** Disabled agent or quota exhaustion pause task; resume when resolved.
- **`gh` CLI tooling.** Skill lifecycle via GitHub CLI extensions (developer familiarity).

## Open Questions

- Skill versioning scheme (semver? calver?)
- Global registry governance (who can publish?)
- Skill signing and verification
- Offline/air-gapped Foundry support (registry mirroring)

## Key Concepts

### Platform-wide concepts

These concepts are defined centrally and used across Foundry modules:

| Concept | What Agent Fabric does with it |
|---------|--------------------------------|
| [Agent Model](../concepts/agent-model.md) | Manages the three-tier hierarchy (Raw → Trained → Employed) |
| [Skill](../concepts/skill.md) | Packages capabilities via Skill Registry |
| [Delegation](../concepts/delegation.md) | Provides delegation token infrastructure |
| [Scenario](../concepts/scenario.md) | Scenarios reference Swarms; coordinator agent explicitly specified |
| [Governance](../concepts/governance.md) | Quota enforcement as governance over agent resources |

### Module-specific concepts

These concepts describe Agent Fabric internals:

| Concept | Definition |
|---------|------------|
| [Raw Agent](concepts/raw-agent.md) | OCI container packaging an agent system (Codex, Cursor Agent, Claude Code) |
| [Trained Agent](concepts/trained-agent.md) | Manifest combining Raw Agent ref + skills + guardrails; belongs to a Swarm |
| [Employed Agent](concepts/employed-agent.md) | Runtime instance (Trained Agent + Delegation Token) in a Workspace Session |
| [Swarm](concepts/swarm.md) | Organizational unit for Trained Agents — scoped at Foundry/Workshop/Workbench/Workspace |
| [Quota Management](concepts/quota-management.md) | Configurable limits at Foundry, Workbench, and User levels |
| [Usage Analytics](concepts/usage-analytics.md) | Skill invocation metrics, cost attribution |

→ [concepts/README.md](concepts/README.md) — Full module concept index

## Documentation

| Guide | Audience | Index |
|-------|----------|-------|
| Concepts | Anyone | This README, [concepts/](concepts/) |
| [User guide](user-guide/) | Admins, builders | Task-oriented usage |
| [Foundry Platform developer guide](platform-developer-guide/) | Platform engineers | Implementation specs |

## Read Next

- [../work-order-runtime/README.md](../work-order-runtime/README.md) — How agents execute Work Orders
- [../orchestrator/README.md](../orchestrator/README.md) — WO creation and routing
- [../management/README.md](../management/README.md) — Workbench provisioning
- [../../ace/concepts.md](../../ace/concepts.md) — Agent, Skill definitions
