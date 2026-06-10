# Swarm

A Swarm is an organizational unit (OU) for Trained Agents — a named grouping that organizes agents by function, team, or purpose. Unlike Employed Agents, Swarms have no lifecycle states; they simply contain members.

## What it is

Swarms represent the organizational layer of Foundry's agent model. They are containers for Trained Agents that provide:

- **Grouping** — Agents organized by function (Build, Review, Test, Documentation)
- **Visibility** — Scoped access at Foundry, Workshop, Workbench, or Workspace level
- **Governance** — Policies and quotas applied at the Swarm level
- **Reference** — Scenarios reference Swarms rather than individual agents

Think of Swarms as OUs (Organizational Units) for agents. Just as human users belong to teams and departments, Trained Agents belong to Swarms. A Swarm is not a running process — it's an organizational construct.

```
Organization
├── Human OUs
│   ├── Engineering Team
│   ├── QA Team
│   └── DevOps Team
└── Agent Swarms
    ├── Build Swarm (feature-implementer, code-refactorer, test-writer)
    ├── Review Swarm (code-reviewer, security-reviewer)
    └── Test Swarm (test-executor, test-analyzer)
```

## Key Constraints

| Constraint | Description |
|------------|-------------|
| **Single membership** | Each Trained Agent belongs to exactly one Swarm |
| **No lifecycle states** | Swarms are static groupings, not running entities |
| **Platform extension** | Tenants can add Trained Agents to platform-shipped Swarms |

## Swarm Scopes

Swarms exist at four scopes, forming a visibility hierarchy:

```
Foundry Swarms
└── Workshop Swarms
    └── Workbench Swarms
        └── Workspace Swarms
```

| Scope | Visible To | Managed By |
|-------|------------|------------|
| **Foundry Swarm** | All Workshops, Workbenches, Workspaces | Foundry Admin |
| **Workshop Swarm** | Workshop and its Workbenches/Workspaces | Workshop Manager |
| **Workbench Swarm** | That Workbench and its Workspaces | Workbench Manager |
| **Workspace Swarm** | That Workspace only | Workspace Owner |

### Visibility Rules

- Lower scopes inherit visibility of higher-scope Swarms
- A Workspace can see: Workspace Swarms + Workbench Swarms + Workshop Swarms + Foundry Swarms
- Swarms at the same scope are peers (no inheritance between them)

## Platform-Shipped Swarms

Foundry provides standard Swarms that all tenants can use:

| Swarm | Purpose | Example Trained Agents |
|-------|---------|------------------------|
| **Build Swarm** | Feature implementation | feature-implementer, code-refactorer, test-writer |
| **Review Swarm** | Code review and analysis | code-reviewer, security-reviewer, style-checker |
| **Test Swarm** | Test execution and analysis | test-executor, test-analyzer, coverage-reporter |
| **Documentation Swarm** | Documentation generation | doc-writer, changelog-generator, api-documenter |
| **Release Swarm** | Release preparation | release-preparer, deployment-validator |
| **Governance Swarm** | Policy and compliance | policy-reviewer, compliance-checker |

### Extending Platform Swarms

Tenants can add their own Trained Agents to platform-shipped Swarms. This allows customization without creating duplicate Swarms:

```yaml
# In tenant's swarms/build-swarm/trained-agents/
# Extends the platform-shipped Build Swarm
name: custom-implementer
swarm: build-swarm  # References platform Swarm
raw-agent-ref: registry.acme.foundry.io/raw-agents/custom-agent:v1.0.0
skills:
  - name: internal-code-generator
    version: ^1.0.0
```

## Swarm Promotion

Moving a Swarm manifest to a higher scope promotes its visibility:

| Action | Effect |
|--------|--------|
| Workbench → Workshop | Swarm visible to all Workbenches in Workshop |
| Workshop → Foundry | Swarm visible to all Workshops in Foundry |

Promotion is a manual operation — copy the Swarm folder to the higher scope's `swarms/` directory.

## Scenario Reference

Scenarios reference Swarms rather than individual agents:

```yaml
name: implement-feature
description: Implement a feature based on specification
swarms:
  - build-swarm
  - review-swarm
coordinator-agent: build-swarm/feature-implementer
```

The coordinator agent is always explicitly specified using the `{swarm}/{agent}` notation.

## Where it lives in Foundry

| Component | Responsibility |
|-----------|----------------|
| **Swarm Registry** (Agent Fabric) | Stores Swarm definitions and metadata |
| **Repository `swarms/` folder** | Source of truth for Swarm manifests |
| **Metadata Service** | Indexes Swarms for discovery |
| **WO Runtime** | Resolves Swarms when executing Scenarios |

### Repository Structure

Swarms live in a dedicated `swarms/` folder at each scope, separate from the Work Catalog:

```
# Foundry-level
foundry-{id}/
├── work-catalog/          # Scenarios, OI Workflows
└── swarms/                # Swarm definitions
    ├── build-swarm/
    │   ├── swarm.yaml
    │   └── trained-agents/
    │       └── custom-implementer.yaml
    └── custom-swarm/
        ├── swarm.yaml
        └── trained-agents/

# Workshop-level
workshop-{id}/
├── work-catalog/
└── swarms/

# Workbench-level
workbench-{id}/
├── work-catalog/
└── swarms/

# Workspace-level (within Workbench repo)
workbench-{id}/
└── workspaces/
    └── {workspace-type}/
        └── swarms/
```

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Agent](../../../ace/concepts.md) | Swarms organize agents into functional groups |
| Team | Swarms are analogous to human teams for agents |
| Workforce Repository | Swarm Registry stores organizational structure |

Swarms operationalize the ACE concept of agent organization. ACE describes agents as participants in human-agent teams; Swarms provide the organizational structure for agent teams.

## Related concepts

- [Agent Model](../../concepts/agent-model.md) — Three-tier hierarchy (Raw, Trained, Employed)
- [Raw Agent](raw-agent.md) — OCI containers that Trained Agents reference
- [Trained Agent](trained-agent.md) — Agents that belong to Swarms
- [Employed Agent](employed-agent.md) — Runtime instances with delegation
- [Scenario](../../concepts/scenario.md) — Work contracts that reference Swarms

## Further reading

- [../platform-developer-guide/swarm-registry.md](../platform-developer-guide/swarm-registry.md) — Registry API, schema, and hierarchy enforcement
- [../user-guide/swarms.md](../user-guide/swarms.md) — How to create and manage Swarms
- [../platform-developer-guide/trained-agents.md](../platform-developer-guide/trained-agents.md) — Trained Agent manifests with Swarm membership
