# Skilled Agents

## Purpose

This guide explains what Skilled Agents are, how they differ from Scenarios and Skills, and when Foundry Admins or Workbench Managers configure them.

## Audience

| Role | When to use this guide |
|------|------------------------|
| Foundry Admin | Configuring agent behavior across workspaces |
| Workbench Manager | Customizing agent capabilities for a product |

## What is a Skilled Agent?

A **Skilled Agent** is a local manifest that combines a [Capable Agent](capable-agents.md) with Skills and Guardrails for a specific (Workspace Type, Scenario) context.

Think of it as a job description: it specifies which agent system to use, what skills to equip, and what constraints to enforce—all tailored to a particular type of work.

## Scenario vs Skilled Agent

| Concept | Defines | Analogy |
|---------|---------|---------|
| **Scenario** | **WHAT** — the work contract a Workspace accepts | Interface / API contract |
| **Skilled Agent** | **HOW** — the implementation that fulfills the contract | Implementation class |

A Scenario is the ingress contract: it specifies inputs, expected outcomes, and scope (`workspace-ingress` or `workspace-internal`). The Skilled Agent is the implementation: it specifies which agent, skills, and guardrails execute that Scenario. One defines the obligation; the other fulfills it.

## Manifests vs Packages

| Concept | What It Is | Where It Lives |
|---------|------------|----------------|
| **Skill** | Reusable capability package | [Skill Registry](skill-registry.md) (published) |
| **Skilled Agent** | Manifest referencing skills | Workshop/Workbench repo (local) |

**Skills are packages; Skilled Agents are manifests.** This is analogous to:

- Skills = npm packages (published, versioned)
- Skilled Agent = `package.json` (declares which packages to use)

## What a Skilled Agent Specifies

A Skilled Agent manifest declares:

- **Compatible Capable Agents** — Which agent systems and models can execute
- **Skills** — References to published skill packages (name + version)
- **Guardrails** — Constraints on agent behavior
- **Evaluation** — Metrics for assessing agent performance

## When to Configure Skilled Agents

Skilled Agents are defined per Workspace Type and Scenario. Configure them when you need to:

- Assign a specific Capable Agent to a type of work
- Equip an agent with particular skills from the registry
- Enforce guardrails for safety or compliance
- Set up evaluation metrics for agent performance

## Scenarios Without Skilled Agents

If a Scenario does not have a Skilled Agent configured:

- Tasks are queued for human completion
- Tasks appear in the Workspace Console and IDE Work Orders Panel
- The session owner picks up and completes the task manually

## Related

- [Capable Agents](capable-agents.md) — agent systems available for assignment
- [Skill Registry](skill-registry.md) — where skills are published and fetched
- [Employed Agents](employed-agents.md) — how Skilled Agents become running instances
- [Agent Fabric concepts](../README.md) — module boundaries and architecture
- [Platform developer guide: Skilled Agents](../platform-developer-guide/skilled-agents.md) — folder structure, YAML schema, and inheritance model
