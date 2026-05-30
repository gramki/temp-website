# Foundry Management — Foundry Platform developer guide

This guide contains implementation specifications for engineers building the **Foundry Management** components of the Foundry Platform.

## Implementation overview

Foundry Management is the admin plane — configuration services, provisioning, Work Catalog Management, team and knowledge management, validation, and external tool integrations. Configuration flows through the Metadata Service; consumers query Management rather than reading git directly.

## ACE alignment

| ACE concept | How this module realizes it |
|-------------|----------------------------|
| [Workshop](../../ace/concepts.md) | Provisions divisions/units in a Foundry |
| [Workbench](../../ace/concepts.md) | Provisions Product containers with all integrations |
| [Repositories](../../ace/repositories.md) | Provisions and connects the 15 canonical repositories |
| [Scenario](../../ace/concepts.md) | Schema, validation, storage via Work Catalog Management |

## Specification index

| Document | Scope |
|----------|-------|
| [requirements.md](requirements.md) | Module-level functional and non-functional requirements |
| [services/README.md](services/README.md) | Configuration services overview |
| [validation/README.md](validation/README.md) | Validation module (pre-publish gate) |
| [services/workshop-sync.md](services/workshop-sync.md) | Webhook processing and sync |
| [services/metadata-service.md](services/metadata-service.md) | Central config store |
| [services/workshop-validation.md](services/workshop-validation.md) | GitHub integration appendix |
| [foundry-management/README.md](foundry-management/README.md) | Foundry lifecycle, tenancy, settings |
| [team-management/README.md](team-management/README.md) | Users, teams, roles, permissions |
| [team-management/platform-developer-guide/requirements.md](team-management/platform-developer-guide/requirements.md) | Team management implementation requirements |
| [work-catalog-management/README.md](work-catalog-management/README.md) | Work Catalog Management subsystem |
| [work-catalog-management/scenario-schema.md](work-catalog-management/scenario-schema.md) | Scenario YAML schema |
| [work-catalog-management/oi-workflow-schema.md](work-catalog-management/oi-workflow-schema.md) | OI Workflow YAML schema |
| [work-catalog-management/resolution-algorithm.md](work-catalog-management/resolution-algorithm.md) | Hierarchy resolution implementation |
| [knowledge-management/README.md](knowledge-management/README.md) | Knowledge Management subsystem |
| [knowledge-management/knowledge-hierarchy.md](knowledge-management/knowledge-hierarchy.md) | Inheritance model and resolution rules |
| [knowledge-management/knowledge-apis.md](knowledge-management/knowledge-apis.md) | REST API specifications |
| [foundry-definition-repository.md](foundry-definition-repository.md) | Foundry repository structure |
| [workshop-repository.md](workshop-repository.md) | Workshop Definition Repository structure |
| [git-infrastructure.md](git-infrastructure.md) | Git repositories — provisioning, access, webhooks |
| [workbench-architecture.md](workbench-architecture.md) | Workbench internal architecture — storage model, integrations, services |

## Dependencies

| Module / foundation | Integration |
|---------------------|-------------|
| [Orchestrator](..//orchestrator/platform-developer-guide/) | Queries Metadata Service for configuration |
| [Work Order Runtime](..//work-order-runtime/platform-developer-guide/) | Queries Metadata Service; resolves Scenarios |
| [Work Catalogues](..//work-catalogues/) | Conceptual docs and platform defaults; engine specs here |

## Related documentation

- [Module concepts](../README.md) — scope, boundaries, and documentation index
- [Foundry Management user guide](../user-guide/) — admin and provisioning tasks
- [Foundry Platform README](../../README.md) — platform-wide module map and spec authoring rules
