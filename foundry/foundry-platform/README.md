# Foundry Platform

Engineering documentation for the **Foundry Platform** — the implementation that delivers ACE and UPIM capabilities. Module-level specs grow here as they are produced.

**Audience:** Product and engineering teams building the Foundry Platform. For the model the platform delivers, read [../ace/](../ace/README.md). For the formal information schema, read [../product-information-model/](../product-information-model/README.md).

**Terminology:** "Foundry Platform" = this implementation. Bare "Foundry" = the ACE architectural construct. See [../glossary.md](../glossary.md).

## Platform Modules

| Module | Folder | Scope |
|--------|--------|-------|
| **Foundry Management** | [management/](management/README.md) | Admin plane — Validation, configuration services, Work Catalog Management, Workbenches, repositories, teams, tenancy |
| **Foundry IDE** | [ide/](ide/README.md) | Builder-facing interface — workspace-specific views |
| **Agent Fabric** | [agent-fabric/](agent-fabric/README.md) | Agent infrastructure — Skill Registry, Raw Agents, quota, gateway policy |
| **Work Order Runtime** | [work-order-runtime/](work-order-runtime/README.md) | In-session execution — task management, agent spawning, management-plane agent |
| **Foundry Orchestrator** | [orchestrator/](orchestrator/README.md) | Coordination — route orchestration items per Track, create Workspace Work Orders, invoke Governance Scenarios, enforce gates |
| **Workspace Session Infrastructure** | [workspace-session-infrastructure/](workspace-session-infrastructure/README.md) | Session runtime infra — K8s pod provisioning, container images, Coder integration, networking, multi-tenant isolation |
| **Workspace Session Management** | [workspace-session-management/](workspace-session-management/README.md) | Session control plane — lifecycle, state tracking, session events, URL registry |
| **Release Tools** | [release-tools/](release-tools/README.md) | CI/CD pipelines with embedded agents, CD integrations, distribution stores |
| **Foundry Web App** | [foundry-web-app/](foundry-web-app/README.md) | User-facing web interface for Foundry members and Foundry Admins |
| **Platform Admin Web App** | [foundry-platform-admin-web-app/](foundry-platform-admin-web-app/README.md) | Super-admin interface for foundry-platform-admin users managing the entire platform |

See [../tldr.md](../tldr.md) for the one-page overview and [../tldr-faq.md](../tldr-faq.md) for design decisions.

## Content Folders

| Folder | Content |
|--------|---------|
| **Platform Concepts** | [concepts/](concepts/README.md) | Cross-module definitions — Work Order, Scenario, Personal Work, Workspace Session, Orchestration Item |
| **Work Catalogues** | [work-catalogues/](work-catalogues/README.md) | OI Workflows and Scenarios; see [platform-defaults/](work-catalogues/platform-defaults/README.md) for shipped Build and Discovery workflows |

## Deferred Modules

The `_deferred/` folder contains module stubs outside current scope:

- **Platform Ops** — observability dashboards, standard tooling, infrastructure

## Read next

- [concepts/](concepts/README.md) — platform-wide definitions
- [_templates/STYLE-GUIDE.md](_templates/STYLE-GUIDE.md) — documentation structure and contributor guide
- [../tldr-faq.md](../tldr-faq.md) — design decisions
- [../ace/](../ace/README.md) — the model this platform realizes
- [../product-information-model/](../product-information-model/README.md) — the schema the platform implements
