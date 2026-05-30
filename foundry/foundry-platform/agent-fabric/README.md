# Agent Fabric

**Module scope:** Agent infrastructure — Skill Registry, Capable Agent management, quota enforcement, gateway policy, usage analytics.

## Purpose

Agent Fabric provides the infrastructure layer that enables AI-powered automation at scale. It answers the questions: which agents are allowed? what skills do they have? how much can they cost? how do we track what they do?

Without Agent Fabric, each team would need to independently manage agent configurations, handle model access, track costs, and publish capabilities. This creates inconsistency, security risks, and cost overruns. Agent Fabric centralizes these concerns while allowing customization at Workshop and Workbench levels.

The module follows the "provide policy, not operations" principle. It doesn't run LLM gateways — it configures them. It doesn't execute agents — it provides the Skills and configuration that WO Runtime uses to spawn them. This separation keeps the module focused on governance and enablement rather than execution.

## What this module does

- **Skill Registry** — Global and Foundry-scoped registries for publishable skill packages
- **Skill CLI Tooling** — `gh foundry-skill` extensions for build, package, publish, install
- **Capable Agent Registry** — Whitelist and configure agent systems (Cursor, Copilot, Claude Code)
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
┌─────────────────────────────────────────────────────────────────────────────┐
│                              Agent Fabric                                    │
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │                        Skill Registry Service                          │ │
│  │                                                                         │ │
│  │   ┌─────────────────┐              ┌─────────────────┐                │ │
│  │   │  Global Registry │              │ Foundry Registry │                │ │
│  │   │    (public)      │              │   (private)      │                │ │
│  │   └────────┬─────────┘              └────────┬─────────┘                │ │
│  │            │                                 │                          │ │
│  │            └────────────────┬────────────────┘                          │ │
│  │                             │                                           │ │
│  │                    ┌────────┴────────┐                                 │ │
│  │                    │  gh foundry-skill │  ◀── CLI Tooling              │ │
│  │                    │  (init/build/     │                                │ │
│  │                    │   publish/install)│                                │ │
│  │                    └─────────────────┘                                 │ │
│  └────────────────────────────────────────────────────────────────────────┘ │
│                                                                              │
│  ┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────┐ │
│  │  Capable Agent      │  │  Quota Management   │  │   Usage Analytics   │ │
│  │     Registry        │  │                     │  │                     │ │
│  │                     │  │  Foundry │ Workbench│  │  Invocations        │ │
│  │  • Cursor Agent     │  │  ────────┼──────────│  │  Cost attribution   │ │
│  │  • Copilot          │  │  User limits        │  │  Automation coverage│ │
│  │  • Claude Code      │  │  Effective = min()  │  │  Failure rates      │ │
│  │  • Codex CLI        │  │                     │  │                     │ │
│  └─────────────────────┘  └─────────────────────┘  └─────────────────────┘ │
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │                       Gateway Policy Layer                              │ │
│  │                                                                         │ │
│  │    Quota enforcement │ Delegation tokens │ Credential injection │ Audit│ │
│  │                                 │                                       │ │
│  └─────────────────────────────────┼───────────────────────────────────────┘ │
└────────────────────────────────────┼────────────────────────────────────────┘
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
| **Skill Registry** | Global + Foundry-scoped registries for skill packages | [skill-registry.md](platform-developer-guide/skill-registry.md) |
| **Capable Agent Registry** | Whitelist and configure agent systems (Cursor, Copilot, Claude Code) | [capable-agents.md](platform-developer-guide/capable-agents.md) |
| **Quota Management** | Configurable limits at Foundry, Workbench, and User levels | [gateway-policy.md](platform-developer-guide/gateway-policy.md) |
| **Gateway Policy** | Configuration for OSS LLM gateway (quota, routing, audit) | [gateway-policy.md](platform-developer-guide/gateway-policy.md) |
| **Usage Analytics** | Skill invocation metrics, cost attribution, automation coverage | [requirements.md](platform-developer-guide/requirements.md) |

## Agent Model

The module manages a three-tier agent model:

```
┌─────────────────────────────────────────────────────────────────┐
│  Platform Layer                                                  │
│  Capable Agent: Cursor Agent, Copilot, Claude Code, Codex CLI   │
│  (Whitelisted agent systems with orchestration capabilities)    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ configured in
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Definition Layer                                                │
│  Skilled Agent: Local manifest in Workshop/Workbench repo       │
│  (References skills, guardrails, compatible capable agents)     │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │ instantiated as
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Runtime Layer                                                   │
│  Employed Agent: Running in Workspace Session                   │
│  (Delegated authority, quota-bound, session-scoped)             │
└─────────────────────────────────────────────────────────────────┘
```

| Concept | What It Is | Where It Lives |
|---------|------------|----------------|
| **Skill** | Reusable capability package | Skill Registry (published) |
| **Capable Agent** | Whitelisted agent system | Agent Fabric registry |
| **Skilled Agent** | Manifest combining skills + guardrails | Workshop/Workbench repo |
| **Employed Agent** | Runtime instance | Workspace Session |

## ACE Concepts Realized

| Concept | How Agent Fabric realizes it |
|---------|------------------------------|
| **Agent** | Manages Capable Agent, Skilled Agent, Employed Agent hierarchy |
| **Skill** | Packages capabilities following Agent Skills spec |
| **Delegation** | Provides delegation token infrastructure for Employed Agents |
| **Scenario** | Skilled Agents are defined per (Workspace, Scenario) |

## Key Design Decisions

- **Skills are packages, Skilled Agents are manifests.** Skills are published to registries; Skilled Agents are local configuration that reference skills.
- **Two-tier registry.** Global (public) + Foundry (private) mirrors npm/private registry pattern.
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
| [Agent Model](../concepts/agent-model.md) | Manages the three-tier hierarchy (Capable → Skilled → Employed) |
| [Skill](../concepts/skill.md) | Packages capabilities via Skill Registry |
| [Delegation](../concepts/delegation.md) | Provides delegation token infrastructure |
| [Scenario](../concepts/scenario.md) | Skilled Agents are defined per (Workspace, Scenario) |
| [Governance](../concepts/governance.md) | Quota enforcement as governance over agent resources |

### Module-specific concepts

These concepts describe Agent Fabric internals:

| Concept | Definition |
|---------|------------|
| [Capable Agent](concepts/capable-agent.md) | Whitelisted agent system (Cursor, Copilot, Claude Code) |
| [Skilled Agent](concepts/skilled-agent.md) | Local manifest combining skills + guardrails |
| [Employed Agent](concepts/employed-agent.md) | Runtime instance within a Workspace Session |
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
