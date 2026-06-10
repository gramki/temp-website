# Swarms

## Purpose

This guide explains what Swarms are, how they organize Trained Agents, and when Foundry Admins or Workbench Managers create and manage them.

## Audience

| Role | When to use this guide |
|------|------------------------|
| Foundry Admin | Managing Foundry-level Swarms |
| Workshop Manager | Creating Workshop Swarms or extending platform Swarms |
| Workbench Manager | Creating Workbench Swarms for product-specific agents |
| Workspace Owner | Creating Workspace Swarms for personal agent organization |

## What is a Swarm?

A **Swarm** is an organizational unit (OU) for Trained Agents — a named grouping that organizes agents by function, team, or purpose.

Think of Swarms like teams for agents:

| Human Organization | Agent Organization |
|-------------------|-------------------|
| Engineering Team | Build Swarm |
| QA Team | Test Swarm |
| Security Team | Review Swarm |

Swarms are not running processes. They are static groupings that:
- Organize agents by function
- Provide scope-based visibility
- Apply policies and quotas
- Are referenced by Scenarios

## Platform-Shipped Swarms

Foundry provides standard Swarms available to all organizations:

| Swarm | Purpose | When to Use |
|-------|---------|-------------|
| **Build Swarm** | Feature implementation | Implementing features, refactoring, writing tests |
| **Review Swarm** | Code review | Code reviews, security analysis, style checking |
| **Test Swarm** | Test execution | Running tests, analyzing coverage, reporting |
| **Documentation Swarm** | Documentation | Writing docs, changelogs, API documentation |
| **Release Swarm** | Release preparation | Release prep, deployment validation |
| **Governance Swarm** | Policy compliance | Policy reviews, compliance checking |

You can use these Swarms as-is or extend them with your own Trained Agents.

## Swarm Scopes

Swarms exist at four levels, each with different visibility:

```
Foundry Swarms (visible everywhere)
└── Workshop Swarms (visible to Workshop + children)
    └── Workbench Swarms (visible to Workbench + children)
        └── Workspace Swarms (visible to that Workspace only)
```

| Scope | Visible To | Managed By | Use Case |
|-------|------------|------------|----------|
| **Foundry** | All | Foundry Admin | Org-wide agent organization |
| **Workshop** | Workshop + Workbenches | Workshop Manager | Team-specific agents |
| **Workbench** | Workbench + Workspaces | Workbench Manager | Product-specific agents |
| **Workspace** | That Workspace | Workspace Owner | Personal agent organization |

## Creating a Swarm

### 1. Choose the Right Scope

Ask yourself: Who needs access to this Swarm?

| If... | Create at... |
|-------|-------------|
| Everyone in the org | Foundry scope |
| Just my team | Workshop scope |
| Just this product | Workbench scope |
| Just me | Workspace scope |

### 2. Create the Swarm Folder

Create a folder in your repository's `swarms/` directory:

```
workbench-{id}/
└── swarms/
    └── my-swarm/
        └── swarm.yaml
```

### 3. Define the Swarm

Create `swarm.yaml`:

```yaml
apiVersion: foundry.io/v1
kind: Swarm
metadata:
  name: my-swarm
spec:
  description: Agents for my specific workflow
  charter: |
    This Swarm contains agents specialized for our internal processes.
    Members should follow our coding standards and use approved tools.
  policies:
    - require-code-review
  quota:
    max-concurrent-employed: 5
```

### 4. Add Trained Agents

Create Trained Agent manifests in the `trained-agents/` subfolder:

```
swarms/my-swarm/
├── swarm.yaml
└── trained-agents/
    ├── agent-a.yaml
    └── agent-b.yaml
```

Each Trained Agent declares its Swarm membership:

```yaml
# trained-agents/agent-a.yaml
apiVersion: foundry.io/v1
kind: TrainedAgent
metadata:
  name: agent-a
  swarm: my-swarm
spec:
  raw-agent-ref: registry.foundry.io/raw-agents/codex:v2.4.1
  skills:
    - name: code-generator
      version: ^2.1.0
  guardrails:
    - no-force-push
```

## Extending Platform Swarms

You can add your own Trained Agents to platform-shipped Swarms without creating new Swarms.

### Why Extend?

- Use the same Swarm reference across Scenarios
- Mix platform and custom agents in one Swarm
- Inherit platform Swarm policies

### How to Extend

1. Create a folder for the platform Swarm in your `swarms/` directory:

```
workbench-{id}/
└── swarms/
    └── build-swarm/              # Same name as platform Swarm
        └── trained-agents/
            └── my-implementer.yaml
```

2. Create your Trained Agent referencing the platform Swarm:

```yaml
# my-implementer.yaml
apiVersion: foundry.io/v1
kind: TrainedAgent
metadata:
  name: my-implementer
  swarm: build-swarm    # References platform Swarm
spec:
  raw-agent-ref: registry.acme.foundry.io/raw-agents/custom-agent:v1.0.0
  skills:
    - name: internal-code-generator
      version: ^1.0.0
```

Now when Scenarios reference `build-swarm`, they can use both platform agents and your custom agent.

## Single Membership Rule

**Each Trained Agent belongs to exactly one Swarm.**

This constraint ensures:
- Clear ownership and governance
- Unambiguous quota accounting
- Simple reference semantics

If you need an agent available in multiple contexts, consider:
- Creating it at a higher scope (so it's inherited)
- Creating separate Trained Agents with different names

## Swarm Promotion

If a Swarm proves useful beyond its original scope, you can promote it:

| Promotion Path | Who Can Promote |
|----------------|-----------------|
| Workspace → Workbench | Workbench Manager |
| Workbench → Workshop | Workshop Manager |
| Workshop → Foundry | Foundry Admin |

### How to Promote

1. Copy the Swarm folder to the higher scope:

```bash
# Promote from Workbench to Workshop
cp -r workbench-123/swarms/my-swarm/ workshop-456/swarms/my-swarm/
```

2. Update the scope metadata in `swarm.yaml`

3. The Swarm is now visible to all children of the new scope

## Using Swarms in Scenarios

Scenarios reference Swarms to specify which agents can execute them:

```yaml
name: implement-feature
description: Implement a feature based on specification
swarms:
  - build-swarm
  - review-swarm
coordinator-agent: build-swarm/feature-implementer
```

The `coordinator-agent` specifies which agent leads the work, using `{swarm}/{agent}` notation.

## Best Practices

### Naming

- Use lowercase with hyphens: `build-swarm`, `my-custom-swarm`
- Be descriptive: `frontend-build-swarm` not `swarm-1`
- Avoid shadowing platform Swarms unless intentional

### Organization

| Pattern | Recommendation |
|---------|----------------|
| **By function** | build-swarm, review-swarm, test-swarm |
| **By team** | frontend-swarm, backend-swarm, infra-swarm |
| **By workflow** | feature-swarm, bugfix-swarm, release-swarm |

### Scope Selection

- Start at the lowest necessary scope
- Promote when usage expands
- Don't create Foundry Swarms for single-product needs

### Extension vs Creation

| Scenario | Approach |
|----------|----------|
| Adding an agent to platform Build Swarm | Extend `build-swarm` |
| Creating entirely new function | Create new Swarm |
| Team-specific variant of platform Swarm | Create new Swarm at Workshop scope |

## Quotas

Swarms can have quotas that limit resource usage:

| Quota | What It Limits |
|-------|----------------|
| `max-concurrent-employed` | How many agents from this Swarm can run simultaneously |
| `max-daily-invocations` | How many tasks can be assigned per day |
| `max-daily-tokens` | How many tokens can be consumed per day |

When quotas are exceeded:
- New tasks are queued (not rejected)
- Admins receive alerts
- Usage reports show quota utilization

## Related

- [Trained Agents](trained-agents.md) — Agents that belong to Swarms
- [Raw Agents](raw-agents.md) — Agent systems that Trained Agents reference
- [Employed Agents](employed-agents.md) — Running instances of Trained Agents
- [Agent Fabric concepts](../README.md) — Module overview
- [Platform developer guide: Swarm Registry](../platform-developer-guide/swarm-registry.md) — API and schema details
