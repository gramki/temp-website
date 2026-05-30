# Management Concepts

This folder contains module-specific concept definitions for Foundry Management. These concepts elaborate on platform-wide concepts from [../concepts/](../../concepts/) with Management-specific details.

## How to use these concepts

- **Reference platform concepts first.** Core concepts like [Work Catalog](../../concepts/work-catalog.md), [Containment Hierarchy](../../concepts/containment-hierarchy.md), and [Repositories](../../concepts/repositories.md) are defined at the platform level.
- **Module concepts add depth.** These files provide Management-specific implementation details, services, and operational behavior.
- **Link, don't duplicate.** Reference platform concepts rather than restating them.

## Concept Index

### Provisioning & Configuration

| Concept | Definition |
|---------|------------|
| [Declarative Provisioning](declarative-provisioning.md) | Infrastructure-as-configuration model for Workshop and Workbench setup |
| [Validation Module](validation-module.md) | Pre-publish gate for all Foundry-scope configuration |
| [Workshop Sync](workshop-sync.md) | Git-to-Metadata Service synchronization pipeline |

### Work Catalog

| Concept | Definition |
|---------|------------|
| [Work Catalog Resolution](work-catalog-resolution.md) | Hierarchy resolution algorithm (Platform → Foundry → Workshop → Workbench → User) |
| [Agent Recommender](agent-recommender.md) | Skilled Agent matching based on Scenario skill requirements |

### Integrations

| Concept | Definition |
|---------|------------|
| [Integration Service](integration-service.md) | External tool connections (GitHub, Jira, TestRail, Figma, Olympus Weave) |

## Relationship to Platform Concepts

These module concepts elaborate on concepts defined in [../concepts/](../../concepts/):

| Platform Concept | Module Elaborations |
|------------------|---------------------|
| [Work Catalog](../../concepts/work-catalog.md) | [Work Catalog Resolution](work-catalog-resolution.md), [Validation Module](validation-module.md) |
| [Containment Hierarchy](../../concepts/containment-hierarchy.md) | [Declarative Provisioning](declarative-provisioning.md) |
| [Repositories](../../concepts/repositories.md) | [Integration Service](integration-service.md) |
| [Scenario](../../concepts/scenario.md) | [Agent Recommender](agent-recommender.md) |

## Read Next

- [../../concepts/README.md](../../concepts/README.md) — Platform-wide concepts
- [../README.md](../README.md) — Management module overview
- [../platform-developer-guide/README.md](../platform-developer-guide/README.md) — Implementation specifications
