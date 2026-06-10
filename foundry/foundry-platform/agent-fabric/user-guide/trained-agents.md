# Trained Agents

## Purpose

This guide explains what Trained Agents are, how they relate to Swarms and Scenarios, and when Foundry Admins or Workbench Managers configure them.

## Audience

| Role | When to use this guide |
|------|------------------------|
| Foundry Admin | Configuring agent behavior across Swarms |
| Workbench Manager | Customizing agent capabilities for a product |

## What is a Trained Agent?

A **Trained Agent** is a manifest that combines a [Raw Agent](raw-agents.md) with Skills, Guardrails, and identity for a specific function within a [Swarm](swarms.md).

Think of it as a job description: it specifies which agent system to use (Raw Agent), what skills to equip, what constraints to enforce, and which Swarm the agent belongs to — all defining what this agent is configured to do.

Each Trained Agent has a **Service Principal identity** using Jabber JID notation:

```
{agent}@{swarm}.agents.{tenant}.foundry.io
```

## Swarm Membership

Every Trained Agent belongs to exactly one Swarm. Swarms are organizational units (like OUs for agents) that group Trained Agents by function:

| Swarm | Example Trained Agents |
|-------|------------------------|
| Build Swarm | feature-implementer, code-refactorer, test-writer |
| Review Swarm | code-reviewer, security-reviewer |
| Test Swarm | test-executor, test-analyzer |

Scenarios reference Swarms rather than individual Trained Agents. The coordinator agent is always explicitly specified in the Scenario definition.

## Scenario vs Trained Agent

| Concept | Defines | Analogy |
|---------|---------|---------|
| **Scenario** | **WHAT** — the work contract a Workspace accepts | Interface / API contract |
| **Trained Agent** | **HOW** — the implementation that fulfills the contract | Implementation class |
| **Swarm** | **WHERE** — the organizational group agents belong to | Department / OU |

A Scenario is the ingress contract: it specifies inputs, expected outcomes, and scope. The Scenario references Swarms and a coordinator agent. The Trained Agent within the Swarm is the implementation: it specifies which Raw Agent, skills, and guardrails execute that work.

## Manifests vs Packages

| Concept | What It Is | Where It Lives |
|---------|------------|----------------|
| **Skill** | Reusable capability package | [Skill Registry](skill-registry.md) (published) |
| **Trained Agent** | Manifest referencing skills + Raw Agent | `swarms/{swarm}/trained-agents/` (in repo) |

**Skills are packages; Trained Agents are manifests.** This is analogous to:

- Skills = npm packages (published, versioned)
- Trained Agent = `package.json` (declares which packages to use)

## What a Trained Agent Manifest Specifies

A Trained Agent manifest declares:

- **Raw Agent reference** — Which OCI-packaged agent system and version to use
- **Swarm membership** — Which Swarm this agent belongs to
- **Identity** — JID for Service Principal addressing
- **Skills** — References to published skill packages (name + version)
- **Guardrails** — Constraints on agent behavior
- **Evaluation** — Metrics for assessing agent performance

```yaml
name: feature-implementer
swarm: build-swarm
raw-agent-ref: registry.foundry.io/raw-agents/codex:v2.4.1
identity:
  jid: feature-implementer@build-swarm.agents.acme.foundry.io
skills:
  - name: code-generator
    version: ^2.1.0
guardrails:
  - no-force-push
  - require-tests-for-new-code
```

## When to Configure Trained Agents

Trained Agents are defined per Swarm. Configure them when you need to:

- Add an agent with specific skills to a Swarm
- Assign a specific Raw Agent to a type of work
- Equip an agent with particular skills from the registry
- Enforce guardrails for safety or compliance
- Extend a platform-shipped Swarm with tenant-specific agents

## Scenarios Without Trained Agents

If a Scenario does not reference any Swarms:

- Tasks are queued for human completion
- Tasks appear in the Workspace Console and IDE Work Orders Panel
- The session owner picks up and completes the task manually

## Related

- [Swarms](swarms.md) — organizational units where Trained Agents live
- [Raw Agents](raw-agents.md) — agent systems available for assignment
- [Skill Registry](skill-registry.md) — where skills are published and fetched
- [Employed Agents](employed-agents.md) — how Trained Agents become running instances
- [Agent Fabric concepts](../README.md) — module boundaries and architecture
- [Platform developer guide: Trained Agents](../platform-developer-guide/trained-agents.md) — manifest schema, identity model, and Swarm structure
