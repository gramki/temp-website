# Workbench Architecture — Implementation

This document provides implementation details for the Workbench construct — the technical architecture, integration protocols, and internal service configurations.

For the admin-facing conceptual overview, see [../user-guide/workbench-architecture.md](../user-guide/workbench-architecture.md).

---

## GitHub Integration

### Setup Flow

At Workbench creation:

1. Specify GitHub Organization
2. Workbench installs as **GitHub App** on the org
3. Workbench becomes org manager

### Repo Tagging

All repos created through Workbench are tagged with:

- **FoundryID** — the Foundry this Workbench belongs to
- **Workshop** — the Workshop containing this Workbench
- **Workbench** — this Workbench's ID
- **Product Code** — the UPIM Product code

### Access Model

| Actor | GitHub Access |
|-------|---------------|
| **Workbench** | Org management (create repos, settings, tagging) |
| **Team members** | Repo-level access only (read/write to specific repos) |
| **Direct org management** | Disabled — all org operations via Workbench |

### Existing Repos

When connecting to a GitHub Org with existing repos:

- **Best practice:** Import and tag existing repos
- **Not mandated:** Can coexist with untagged repos

---

## Workbench Metadata Service

Single service per Workbench providing:

### Product Intent ID Generation

```
1. User requests new Intent via Workbench UI
2. Metadata Service generates unique PI ID (e.g., PI-001)
3. User provides short title
4. Intent folder created in Intent repo: /PI-001/
5. Detailed content written as docs under that folder
```

### Commit Tracking

Tracks **all commits** to all linked git repos:

- Intent repo
- Design repo
- Code repos (all of them)

Used for:

- Change history
- Audit trail
- Evolution tracking

### Code Repo Reference Management

Manages references to all source code repos:

- Each System/Component can have its own git repo
- All repos in the same GitHub Org
- Metadata Service stores the reference list

---

## Repository Storage Model

### Intent Repository (Git-based)

```
intent-repo/
├── PI-001/                    # Intent folder (PI ID from Metadata Service after Go/Pivot PDR)
│   ├── README.md              # Intent overview (title + description)
│   ├── pdr.md                 # Authorizing Product Decision Record (artifact-only)
│   ├── psd-overview.md        # Product Specification Document refinement
│   ├── psd-feature-a.md       # PSD refinement can span multiple files
│   └── mockups/               # Mockups (or links to Figma)
│       └── figma-links.md
├── PI-002/
│   └── ...
└── (organized as product team sees fit)
```

Artifact URIs follow Phase 1 containment form — see [../../../foundry-work-plan/phase-1/repository-contracts.md](../../../foundry-work-plan/phase-1/repository-contracts.md).

**Key behaviors:**

- PI ID required before creating Intent folder
- Product Intent is created from a Go/Pivot PDR
- PDR, PSD refinements, Mockups, Visual Design stored under Intent
- High-fidelity designs may link to Figma (URLs in PSDs)

### Design Repository (Git-based)

Similar structure to Intent:

- Folder/file organization
- **No ID required** before creating docs
- Metadata Service tracks changes (for audit/history)

### Code Repositories (Git-based, Multiple)

- Multiple git repos per Workbench
- Each System, Component, or element can have its own repo
- Created through Workbench interfaces (ensures tagging)
- Metadata Service maintains reference list

### Ontology Service (Native)

- **Auto-provisioned** on Workbench creation
- Independent of Metadata Service
- Manages:
  - Product structure
  - Capabilities
  - Features
  - Maturity indicators

### Quality Repository (Hybrid)

| Component | Storage | Notes |
|-----------|---------|-------|
| **Test cases** | TestRail | Source of truth for test case definitions |
| **Automation code** | Git repo (GitHub Org) | Automation scripts linked to TestRail test cases |
| **Quality Service** | Foundry-native | Unified access wrapper over TestRail + Git |

**Key behaviors:**

- TestRail is the source of truth for test case definitions
- Git stores automation code corresponding to test cases
- Quality Service provides unified API regardless of underlying storage

### Work Repository (Jira adapter in Phase 1)

| Repository | Adapter | Scope | Purpose |
|------------|---------|-------|---------|
| **Operations** | JSM | `foundry-workbench-{workbenchId}` label | Problems, incidents requiring on-call |
| **Feedback** | Jira | `foundry-workbench-{workbenchId}` label | FIRs, bug reports |
| **Work** | Jira | `foundry-workbench-{workbenchId}` label | Work Model entities |
| **Work Orders** | Jira | Dedicated `workRepoProject` | WO Runtime execution |

**Work Orders project:**

- Orchestrator creates Work Orders with `title`, `description`, and `foundry-*` labels
- WO Runtime creates Tasks with `agentType` (`human` | `ai-agent`)
- Contract fields: `workRepoKey`, `workRepoItemKey`, `workRepoStatus` — see [../../../foundry-work-plan/phase-1/repository-contracts.md](../../../foundry-work-plan/phase-1/repository-contracts.md)

**JSM specifics (Operations):**

- Tracks problems in JSM
- Subset of problems relevant to Product → also in Feedback
- Incidents requiring Workbench team on-call involvement → tracked

### Evolution Repository

Storage model **deferred** (not Phase 1).

---

## Olympus Weave Integration

Workbench acts as **Publisher** to Olympus Weave (deployment platform).

### Setup

At Workbench creation:

1. Connect to Olympus Weave (OAuth, Workbench ID as client)
2. Weave assigns **Product Code** to the Workbench
3. When Systems are registered in Ontology, Weave assigns **Olympus Product Module code** per System

### Identifiers from Weave

| Identifier | Assigned When | Scope |
|------------|---------------|-------|
| **Product Code** | Workbench creation | One per Workbench/Product |
| **Olympus Product Module code** | System registration | One per System |

### Deployment Tracking

| Aspect | Detail |
|--------|--------|
| **Update mechanism** | Weave → Foundry webhook + Foundry polls Weave |
| **Multi-region** | Tracks which version deployed where |
| **End-of-Support** | Weave owns metadata; Foundry surfaces it |
| **Deprecated versions** | Weave owns metadata; Foundry alerts if in use |

### Operations

Workbench can:

- Publish artifacts to Weave
- Query release/deployment status
- Retrieve Product Code and Olympus Product Module codes
- Track version distribution across regions
- Surface EoS/deprecation warnings

---

## External Tool Integrations

### OAuth-Integrated Tools (Phase 1)

| Tool | Integration | Workbench Role |
|------|-------------|----------------|
| **GitHub** | GitHub App | Org manager, repo creation, commit tracking |
| **Figma** | OAuth | View/link design files |
| **TestRail** | OAuth | Test case management (source of truth) |
| **Jira** | OAuth | Operations (JSM), Feedback, Work repositories |
| **Olympus Weave** | OAuth | Publisher — deploy, track versions, EoS |

When a supported tool is added:

1. Workbench initiates OAuth flow (using Workbench ID as client)
2. User authorizes connection
3. Workbench stores access token
4. Tool resources become accessible from Workbench UI

**Note:** GitHub uses GitHub App (not OAuth). Weave assigns Product Code on connection.

### URL-Only Tools

For unsupported tools:

- Store URL reference
- No deep integration
- Manual navigation required

---

## Capable Agents Configuration

Capable Agents (whitelisted frontier models/agent systems) are managed hierarchically. See [../../agent-fabric/platform-developer-guide/capable-agents.md](../../agent-fabric/platform-developer-guide/capable-agents.md).

### Hierarchy

```
Foundry (org-level defaults)
    │
    └── Workshop (team-level overrides)
            │
            └── Workbench (product-level overrides)
```

### Inheritance Rules

| Rule | Behavior |
|------|----------|
| **Enable/disable** | Disabled at higher level = disabled for all lower levels |
| **Credentials** | Resolved upward: Workbench → Workshop → Foundry (first found) |
| **Models** | Configured per Capable Agent at each level |

### Workbench Configuration

In `workbenches/{product-code}/capable-agents.yaml`:

```yaml
capable-agents:
  cursor-agent:
    models:
      claude-opus:
        credentials:
          api-key: ${PROJECT_ANTHROPIC_API_KEY}
```

### Available Capable Agents (Examples)

| Agent | Type | Provider |
|-------|------|----------|
| Cursor Agent | IDE agent | Cursor |
| GitHub Copilot | IDE agent | GitHub |
| Claude Code | CLI agent | Anthropic |
| Codex CLI | CLI agent | OpenAI |

---

## Shared Repositories

Some repositories are shared at Workshop or Foundry level:

| Repository | Scope | Notes |
|------------|-------|-------|
| **Domain** | Workshop-shared | Domain knowledge, glossaries |
| **Practices** | Workshop-shared | Standards, templates |
| **Workforce** | Foundry-shared | Agents, humans |
| **Stakeholders** | Workshop-shared | External stakeholder registry |

Workbenches reference these shared repositories; they don't own them.

---

## Open Questions

- **Evolution repository** — storage model deferred (not Phase 1)
- Scenario Catalog storage and versioning
- Workbench archival/deletion workflow
- Cross-Workbench repository sharing within a Workshop

---

## Related Documentation

- [../user-guide/workbench-architecture.md](../user-guide/workbench-architecture.md) — Admin-facing conceptual overview
- [../user-guide/workbench-provisioning.md](../user-guide/workbench-provisioning.md) — Provisioning guide
- [workshop-repository.md](workshop-repository.md) — Workshop Definition Repository structure
- [services/metadata-service.md](services/metadata-service.md) — Metadata Service specification
- [../../agent-fabric/platform-developer-guide/capable-agents.md](../../agent-fabric/platform-developer-guide/capable-agents.md) — Capable Agents configuration
