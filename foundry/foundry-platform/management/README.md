# Foundry Management

**Module scope:** Admin plane — Workshops, Workbenches, repositories (as services), teams, agents, knowledge, tenancy, and external tool integrations.

## What this module does

Foundry Management is the administrative layer of the platform. It provides:

- **Workshop provisioning** — create and configure Workshops (divisions/units)
- **Workbench provisioning** — create and configure Workbenches for Products
- **Repository management** — repositories as services with injection/access interfaces
- **Team management** — teams, roles, permissions
- **Agent management** — Capable Agent registry, Skilled Agent definitions, credential hierarchy
- **Knowledge management** — knowledge ingestion, organization (integral to each repository)
- **Tenancy** — tenant provisioning, isolation, configuration, quotas
- **External tool integrations** — GitHub, Figma, TestRail, Jira, Olympus Weave

## Key Services

### Metadata Service

A single service per Workbench that provides identity, tracking, and reference management.

#### ID Generation

The Metadata Service generates unique identifiers for orchestration items and work artifacts.

**API Endpoint:**
```
POST /metadata/ids/{type}
Response: { "id": "<type-prefix>-<sequence>" }
```

**Supported Types:**

| Type | Prefix | Example | Consumers |
|------|--------|---------|-----------|
| `product-intent` | `PI` | `PI-456` | IDE extensions, Orchestrator |
| `release-intent` | `RI` | `RI-78` | Web console, Orchestrator |
| `work-order` | `WO` | `WO-1234` | Orchestrator |
| `discovery-case` | `DC` | `DC-89` | IDE extensions, Orchestrator |
| `run-case` | `RC` | `RC-45` | IDE extensions, Orchestrator |

**Sequence Management:**
- Sequences are scoped per Workbench
- Monotonically increasing integers
- Gap-free sequence is not guaranteed (failed transactions may consume IDs)
- IDs are unique within a Workbench (not globally unique)

**Usage Flow:**

```
1. User initiates "Create Product Intent" in IDE
2. IDE extension calls Metadata Service: POST /metadata/ids/product-intent
3. Metadata Service returns: { "id": "PI-456" }
4. IDE creates PI folder in Intent Repository: intent-repo/PI-456/
5. PI ID is used in Jira item and all subsequent references
```

#### Commit Tracking

| Function | Behavior |
|----------|----------|
| **Intent commits** | Tracks all commits to Intent Repository |
| **Design commits** | Tracks all commits to Design Repository |
| **Code commits** | Tracks all commits to all Code Repositories |

Commit tracking enables:
- Traceability from PI to code changes
- Audit trail for compliance
- Change impact analysis

#### Code Repository References

Manages references to all source code repositories in the Workbench:

| Operation | API |
|-----------|-----|
| List repos | `GET /metadata/code-repos` |
| Add repo | `POST /metadata/code-repos` |
| Remove repo | `DELETE /metadata/code-repos/{id}` |
| Get repo | `GET /metadata/code-repos/{id}` |

### Ontology Service

- **Independent** of Metadata Service
- Auto-provisioned when Workbench is created
- Manages product structure, capabilities, features

## GitHub Integration

Workbench acts as a **GitHub App** with org management capabilities:

| Aspect | Detail |
|--------|--------|
| Integration type | GitHub App (not OAuth) |
| Org sharing | Multiple Workbenches can share one GitHub Org |
| Repo tagging | FoundryID, Workshop, Workbench, Product Code |
| Repo creation | All repos created through Workbench interfaces |
| Access model | Workbench = org manager; team members = repo-level access only |

## External Tool Integrations (Phase 1)

| Tool | Integration Type | Purpose |
|------|------------------|---------|
| **GitHub** | GitHub App | Org management, repo creation, commit tracking |
| **Figma** | OAuth | Design asset linking |
| **TestRail** | OAuth | Test case management (Quality repo SoT) |
| **Jira** | OAuth | Operations (JSM), Feedback, Work repositories |
| **Olympus Weave** | OAuth | Publish, deploy, track versions, EoS |
| **Others** | URL reference | External resource linking |

**Workbench ID** is used as the OAuth client ID for all integrations.

### Olympus Weave

Workbench acts as **Publisher** to Olympus Weave (deployment platform):
- Product Code assigned by Weave on Workbench creation
- Olympus Product Module code assigned per System
- Deployment tracking via webhook (Weave → Foundry) + polling
- EoS/deprecation metadata owned by Weave, surfaced in Foundry

## Repository Architecture

See [workbench-architecture.md](workbench-architecture.md) for detailed repository storage model.

| Repository | Storage | Service Role |
|------------|---------|--------------|
| **Intent** | Git repo (GitHub Org) | Metadata Service: PI ID generation, commit tracking |
| **Design** | Git repo (GitHub Org) | Metadata Service: commit tracking |
| **Code** | Multiple git repos (GitHub Org) | Metadata Service: reference management, commit tracking |
| **Ontology** | Native service | Independent (auto-provisioned) |
| **Quality** | TestRail + Git | Quality Service: unified access wrapper |
| **Operations** | Jira (JSM) | Label-filtered; linked at setup |
| **Feedback** | Jira | Label-filtered; linked at setup |
| **Work** | Jira | Label-filtered; linked at setup |
| **Evolution** | TBD | Deferred (not Phase 1) |

## ACE concepts realized

- **Workshop** — division/unit in a Foundry
- **Workbench** — corresponds to a Product in UPIM; where Product is evolved
- **Repositories** — the 15 canonical repositories defined in [../../ace/repositories.md](../../ace/repositories.md)
- **Workforce** — agents and humans, managed here
- **Capable Agent** — whitelisted frontier model/agent system (Cursor, Copilot, Claude Code)
- **Skilled Agent** — Capable Agent + Skills + Guardrails for a (Workspace, Scenario)

## UPIM entities involved

- Definition Model entities (stored in repositories)
- Work Model entities (stored in repositories)
- Operating Model entities (teams, roles)

## Key design decisions

- **Repositories are services, not stores.** Each repository provides interfaces to inject and access contents, and manages its own organization, layout, and knowledge management.
- **Content evolves via Work Order execution** (or independently for Domain, Practices repositories).
- **Single Metadata Service per Workbench** handles PI IDs, commit tracking, and code repo references.
- **Workbench as GitHub org manager** — team members don't have direct org management access.

## Open questions

- Workbench lifecycle — creation, archival, deletion
- Repository import workflow for existing GitHub orgs
- Team/agent management UX
- Tenant onboarding flow

## Read Next

- [workbench-architecture.md](workbench-architecture.md) — detailed Workbench architecture
- [workshop-repository.md](workshop-repository.md) — Workshop/Workbench definition repository structure
- [../orchestrator/pi-journey.md](../orchestrator/pi-journey.md) — End-to-end PI walkthrough showing Metadata Service usage
- [../agent-fabric/README.md](../agent-fabric/README.md) — Agent Fabric (Capable, Skilled, Employed Agents)
- [../work-order-runtime/README.md](../work-order-runtime/README.md) — WO Runtime execution engine
- [../../ace/repositories.md](../../ace/repositories.md) — the repository taxonomy
- [../../tldr-faq.md](../../tldr-faq.md) — module design decisions
