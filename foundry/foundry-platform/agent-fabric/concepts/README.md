# Agent Fabric Concepts

This folder contains module-specific concept definitions for Agent Fabric. These concepts elaborate on platform-wide concepts from [../concepts/](../../concepts/) with Agent Fabric-specific details.

## How to use these concepts

- **Reference platform concepts first.** Core concepts like [Agent Model](../../concepts/agent-model.md), [Skill](../../concepts/skill.md), and [Delegation](../../concepts/delegation.md) are defined at the platform level.
- **Module concepts add depth.** These files provide Agent Fabric-specific implementation details, schemas, and operational behavior.
- **Link, don't duplicate.** Reference platform concepts rather than restating them.

## Concept Index

### Agent Hierarchy

| Concept | Definition |
|---------|------------|
| [Capable Agent](capable-agent.md) | Platform-layer agent system with orchestration capabilities |
| [Skilled Agent](skilled-agent.md) | Declarative manifest binding skills and guardrails to a Capable Agent |
| [Employed Agent](employed-agent.md) | Runtime instance spawned in a Workspace Session with delegated authority |

### Infrastructure

| Concept | Definition |
|---------|------------|
| [Quota Management](quota-management.md) | Multi-level usage limits with effective quota calculation |
| [Usage Analytics](usage-analytics.md) | Skill invocation metrics, cost attribution, and automation coverage |

## Relationship to Platform Concepts

These module concepts elaborate on concepts defined in [../concepts/](../../concepts/):

| Platform Concept | Module Elaborations |
|------------------|---------------------|
| [Agent Model](../../concepts/agent-model.md) | [Capable Agent](capable-agent.md), [Skilled Agent](skilled-agent.md), [Employed Agent](employed-agent.md) |
| [Delegation](../../concepts/delegation.md) | Token handling in [Employed Agent](employed-agent.md) |
| [Skill](../../concepts/skill.md) | Skill references in [Skilled Agent](skilled-agent.md) |

## Read Next

- [../../concepts/README.md](../../concepts/README.md) — Platform-wide concepts
- [../README.md](../README.md) — Agent Fabric module overview
- [../platform-developer-guide/README.md](../platform-developer-guide/README.md) — Implementation specifications
