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

### Skill Registry Service

Two-tier registry for skill packages:

| Registry | Scope | Contents |
|----------|-------|----------|
| **Global** | Cross-Foundry (public) | Community skills, vendor-provided skills |
| **Foundry** | Org-scoped (private) | Internal skills, forked/modified skills |

Skills are published following the [Agent Skills specification](https://agentic.ai/) (SKILL.md + supporting files).

→ [skill-registry.md](skill-registry.md)

### Skill CLI Tooling

GitHub CLI extensions for skill lifecycle:

| Command | Purpose |
|---------|---------|
| `gh foundry-skill init` | Scaffold new skill |
| `gh foundry-skill build` | Validate and build |
| `gh foundry-skill test` | Run evaluation harness |
| `gh foundry-skill publish` | Publish to registry |
| `gh foundry-skill install` | Install to workspace |
| `gh foundry-skill search` | Search registries |

→ [skill-registry.md](skill-registry.md)

### Capable Agent Registry

Manage whitelisted agent systems at Foundry / Workbench levels:

- Enable/disable agents with cascade rules
- Configure supported models per agent
- Credential management (references to secure storage)
- Auto-fallback configuration

→ [capable-agents.md](capable-agents.md)

### Quota Management

Configurable quotas at multiple levels:

| Level | Scope | Example |
|-------|-------|---------|
| Foundry | Global org limit | $50K/month total |
| Workbench | Product limit | $2K/month for Checkout |
| (Foundry, User) | User's global limit | Alice: $500/month |
| (Workbench, User) | User's product limit | Alice on Checkout: $200/month |

Effective quota = minimum of all applicable limits.

### Gateway Policy

Configuration for an OSS LLM gateway (not built-in). Recommended gateways:

| Gateway | License | Strengths |
|---------|---------|-----------|
| **LiteLLM Proxy** | MIT | 100+ providers, spend tracking, caching |
| **Portkey** | Apache 2.0 | Enterprise features, load balancing |
| **Helicone** | Apache 2.0 | Observability, cost tracking |

The module provides:
- Quota policy configuration for the gateway
- Delegation token validation hooks
- Credential injection from Capable Agent registry
- Audit log aggregation

→ [gateway-policy.md](gateway-policy.md)

### Usage Analytics

Metrics for skill and agent utilization:

| Metric | Description |
|--------|-------------|
| Invocation count | Per skill, per Skilled Agent |
| Cost attribution | By Foundry / Workbench / User / Skill |
| Automation coverage | Scenarios with vs without Skilled Agents |
| Failure rates | By skill, by capable agent |

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

## Module Documents

| Document | Content |
|----------|---------|
| [requirements.md](requirements.md) | Implementation requirements (APIs, database, observability) |
| [agent-lifecycle-journey.md](agent-lifecycle-journey.md) | End-to-end agent lifecycle walkthrough |
| [skill-registry.md](skill-registry.md) | Skill distribution, packaging, and CLI tooling |
| [capable-agents.md](capable-agents.md) | Capable Agent registry, fallback, credentials |
| [skilled-agents.md](skilled-agents.md) | Skilled Agent manifest structure and guardrails |
| [employed-agents.md](employed-agents.md) | Runtime instantiation and delegation model |
| [gateway-policy.md](gateway-policy.md) | OSS gateway configuration and quota enforcement |

## Read Next

- [../work-order-runtime/README.md](../work-order-runtime/README.md) — How agents execute Work Orders
- [../orchestrator/README.md](../orchestrator/README.md) — WO creation and routing
- [../management/README.md](../management/README.md) — Workbench provisioning
- [../../ace/concepts.md](../../ace/concepts.md) — Agent, Skill definitions
