# Foundry Management

**Module scope:** Admin plane — Workshops, Workbenches, repositories, teams, configuration services, scenario management, and external tool integrations.

## Purpose

Foundry Management is the administrative foundation that makes everything else possible. Before any Work Order can execute, before any agent can be spawned, before any code can be committed — someone must provision the Workbench, configure the repositories, set up the team, and integrate the tools.

The module treats infrastructure as configuration. A Workbench is not just a database entry — it's a GitHub org, a Jira project, a TestRail instance, a Figma workspace, all wired together. Management handles this complexity by providing declarative provisioning: admins describe what they want, and the module creates and connects all the pieces.

## What this module does / does NOT do

| Does | Does NOT |
|------|----------|
| Workshop & Workbench provisioning | Execute Work Orders (WO Runtime) |
| Repository management | Orchestrate work / route items (Orchestrator) |
| Configuration services (validate, sync, serve) | Manage agent runtime (Agent Fabric, WO Runtime) |
| Work Catalog Management (schemas, resolution) | Store product artifacts (Repositories) |
| Team management (roles, permissions) | Define scenario templates (work-catalogues module) |
| External tool integrations (GitHub, Jira, etc.) | |

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              Foundry Management                                  │
│                                                                                  │
│  ┌────────────────────────────────────────────────────────────────────────────┐ │
│  │                        Configuration Services                               │ │
│  │   Validation Module ──► Workshop Sync ──► Metadata Service                 │ │
│  └────────────────────────────────────────────────────────────────────────────┘ │
│                                                                                  │
│  ┌────────────────────────────────────────────────────────────────────────────┐ │
│  │                        Provisioning Services                                │ │
│  │   Workshop │ Workbench │ Repository │ Foundry provisioning                  │ │
│  └────────────────────────────────────────────────────────────────────────────┘ │
│                                                                                  │
│  ┌────────────────────────────────────────────────────────────────────────────┐ │
│  │                          Subsystems                                         │ │
│  │   Foundry Mgmt │ Team Mgmt │ Work Catalog Mgmt │ Validation │ Knowledge    │ │
│  └────────────────────────────────────────────────────────────────────────────┘ │
│                                                                                  │
│  ┌────────────────────────────────────────────────────────────────────────────┐ │
│  │                       External Integrations                                 │ │
│  │   GitHub App │ Jira OAuth │ TestRail │ Figma │ Olympus Weave               │ │
│  └────────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────────┘
           │ webhooks                     ▲ queries
           ▼                              │
    Workshop Definition Repo      Orchestrator │ WO Runtime │ Web App
```

## ACE alignment

| ACE concept | How Management realizes it |
|-------------|---------------------------|
| **Workshop** | Provisions divisions/units in a Foundry |
| **Workbench** | Provisions Product containers with all integrations |
| **Repositories** | Provisions and connects the 15 canonical repositories |
| **Workforce** | Manages teams, roles, permissions |
| **Scenario** | Schema, validation, storage via Work Catalog Management |
| **Raw Agent** | Stores registry configuration (Agent Fabric uses it) |

## Key Design Decisions

- **Repositories are services, not stores.** Each repository provides interfaces to inject and access contents.
- **Configuration flows through Metadata Service.** Consumers never read from git directly.
- **Validation module gates definition-repo merges.** Invalid config cannot reach main on Foundry or Workshop repos; user catalogs validate on push but allow direct push.
- **Single check name.** All Foundry-scope validation reports as `foundry-validation`.
- **Declarative provisioning** — admins describe desired state; module creates and connects components.
- **Work Catalog Management is a subsystem** — not a separate module; tightly integrated with config services.

## Open Questions

- Workbench lifecycle — creation, archival, deletion
- Repository import workflow for existing GitHub orgs
- Scenario versioning and A/B testing
- Cross-Foundry collaboration patterns

## Key Concepts

### Platform-wide concepts

These concepts are defined centrally and used across Foundry modules:

| Concept | What Management does with it |
|---------|------------------------------|
| [Containment Hierarchy](../concepts/containment-hierarchy.md) | Provisions Foundry → Workshop → Workbench → Workspace |
| [Repositories](../concepts/repositories.md) | Provisions and connects the 15 canonical repositories |
| [Knowledge Hierarchy](../concepts/knowledge-hierarchy.md) | Manages inheritance for domain, practices, and ontology |
| [Metadata Service](../concepts/metadata-service.md) | Serves configuration to platform consumers |
| [Work Catalog](../concepts/work-catalog.md) | Manages schemas, validation, and resolution |
| [Scenario](../concepts/scenario.md) | Schema validation and storage via Work Catalog Management |

### Module-specific concepts

These concepts describe Management internals:

| Concept | Definition |
|---------|------------|
| [Declarative Provisioning](concepts/declarative-provisioning.md) | Admins describe desired state; module creates and connects components |
| [Validation Module](concepts/validation-module.md) | Gates definition-repo merges with config validation |
| [Workshop Sync](concepts/workshop-sync.md) | Syncs Workshop Definition Repo to Metadata Service |
| [Integration Service](concepts/integration-service.md) | Connects GitHub, Jira, TestRail, Figma, Olympus Weave |
| [Work Catalog Resolution](concepts/work-catalog-resolution.md) | Resolves OI Workflows and Scenarios from hierarchy |
| [Agent Recommender](concepts/agent-recommender.md) | Suggests agents based on task context |

→ [concepts/README.md](concepts/README.md) — Full module concept index

## Documentation

| Guide | Audience | Path |
|-------|----------|------|
| Concepts | Anyone | This README, [concepts/](concepts/) |
| User guide | Admins, builders | [user-guide/](user-guide/) |
| Platform developer guide | Platform engineers | [platform-developer-guide/](platform-developer-guide/) |

### Platform developer guide index

| Subsystem | Documentation |
|-----------|---------------|
| Requirements | [requirements.md](platform-developer-guide/requirements.md) |
| Services (Validation, Sync, Metadata) | [services/README.md](platform-developer-guide/services/README.md) |
| Foundry Management | [foundry-management/README.md](platform-developer-guide/foundry-management/README.md) |
| Team Management | [team-management/README.md](platform-developer-guide/team-management/README.md) |
| Work Catalog Management | [work-catalog-management/README.md](platform-developer-guide/work-catalog-management/README.md) |
| Validation | [validation/README.md](platform-developer-guide/validation/README.md) |
| Knowledge Management | [knowledge-management/README.md](platform-developer-guide/knowledge-management/README.md) |
| Git Infrastructure | [git-infrastructure.md](platform-developer-guide/git-infrastructure.md) |

## Read Next

- [../orchestrator/README.md](../orchestrator/README.md) — WO creation and routing
- [../work-order-runtime/README.md](../work-order-runtime/README.md) — WO Runtime execution engine
- [../agent-fabric/README.md](../agent-fabric/README.md) — Agent infrastructure
- [../work-catalogues/README.md](../work-catalogues/README.md) — Work Catalog overview and platform defaults
- [../../ace/repositories.md](../../ace/repositories.md) — the repository taxonomy
