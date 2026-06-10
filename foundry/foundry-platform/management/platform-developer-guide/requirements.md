# Management Module Requirements

This document specifies detailed implementation requirements for the Foundry Management module.

## Key Concepts

This module implements several platform concepts. For definitions, see:

| Concept | Link |
|---------|------|
| Containment Hierarchy | [../../concepts/containment-hierarchy.md](../../concepts/containment-hierarchy.md) |
| Repositories | [../../concepts/repositories.md](../../concepts/repositories.md) |
| Knowledge Hierarchy | [../../concepts/knowledge-hierarchy.md](../../concepts/knowledge-hierarchy.md) |
| Metadata Service | [../../concepts/metadata-service.md](../../concepts/metadata-service.md) |
| Work Catalog | [../../concepts/work-catalog.md](../../concepts/work-catalog.md) |
| Scenario | [../../concepts/scenario.md](../../concepts/scenario.md) |

Module-specific concepts (internals):

| Concept | Link |
|---------|------|
| Declarative Provisioning | [../concepts/declarative-provisioning.md](../concepts/declarative-provisioning.md) |
| Validation Module | [../concepts/validation-module.md](../concepts/validation-module.md) |
| Workshop Sync | [../concepts/workshop-sync.md](../concepts/workshop-sync.md) |
| Integration Service | [../concepts/integration-service.md](../concepts/integration-service.md) |
| Work Catalog Resolution | [../concepts/work-catalog-resolution.md](../concepts/work-catalog-resolution.md) |

## Phase 1 contract alignment

Management implements entity provisioning and Metadata Service IDs per [../../../foundry-work-plan/phase-1/repository-contracts.md](../../../foundry-work-plan/phase-1/repository-contracts.md). HTTP routes for artifacts vs work items are defined in [../../../foundry-work-plan/phase-1/api-surface.md](../../../foundry-work-plan/phase-1/api-surface.md). Event transport uses Atropos per [../../../foundry-work-plan/phase-1/event-contracts.md](../../../foundry-work-plan/phase-1/event-contracts.md).

Key conventions:

- All entity APIs expose `title` and markdown `description`.
- Work Repository binding uses `workRepoProject`, `workRepoKey`, `workRepoItemKey`, `workRepoStatus` — not Jira-branded field names in contracts.
- Shared Work Repository projects filter by `foundry-workbench-{workbenchId}` labels (see Workshop `integrations.yaml`).

## ACE alignment

| ACE concept | How this module realizes it |
|-------------|---------------------------|
| **Workshop** | Workshop Service provisions and configures Workshops (divisions/units) |
| **Workbench** | Workbench Service provisions Product containers with GitHub, Jira, and other integrations |
| **Repositories** | Repository Service manages the 15 canonical repository types |
| **Workforce** | Team Service manages users, teams, roles, and permissions |
| **Scenario** | Work Catalog Management stores and validates Scenario schemas |

## Architecture Overview

```
┌───────────────────────────────────────────────────────────────────────────┐
│                         Foundry Management API                             │
│                                                                            │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐              │
│  │   REST API     │  │   Admin UI     │  │   CLI Tools    │              │
│  │   Gateway      │  │   (Web App)    │  │   (gh ext)     │              │
│  └───────┬────────┘  └───────┬────────┘  └───────┬────────┘              │
│          │                   │                   │                        │
│          └───────────────────┴───────────────────┘                        │
│                              │                                            │
│                     ┌────────┴────────┐                                  │
│                     │  Service Layer  │                                  │
│                     └────────┬────────┘                                  │
│                              │                                            │
│    ┌──────────────┬──────────┼──────────┬──────────────┐                │
│    │              │          │          │              │                │
│    ▼              ▼          ▼          ▼              ▼                │
│ ┌──────┐    ┌──────┐   ┌──────┐   ┌──────┐    ┌──────────┐            │
│ │Workshop│   │Workbench│  │ Repo │   │ Team │    │Integration│            │
│ │Service│   │ Service │  │Service│  │Service│   │  Service │            │
│ └───┬───┘   └────┬────┘  └───┬───┘  └───┬───┘   └─────┬────┘            │
└─────┼────────────┼───────────┼──────────┼─────────────┼─────────────────┘
      │            │           │          │             │
      └────────────┴───────────┴──────────┴─────────────┘
                               │
                      ┌────────┴────────┐
                      │   Postgres DB   │
                      └─────────────────┘
```

## Core Services

### Workshop Service

**MGT-FR-0001:** The Workshop Service SHALL manage Workshop (division/unit) lifecycle including create, read, update, and archive.

Manages Workshop (division/unit) lifecycle.

#### API Endpoints

```
POST   /api/v1/workshops                    # Create workshop
GET    /api/v1/workshops                    # List workshops
GET    /api/v1/workshops/{id}               # Get workshop
PUT    /api/v1/workshops/{id}               # Update workshop
DELETE /api/v1/workshops/{id}               # Archive workshop
GET    /api/v1/workshops/{id}/workbenches   # List workbenches in workshop
```

#### Workshop Entity

```yaml
Workshop:
  id: string (uuid)
  name: string
  code: string (unique, slug)
  description: string
  foundry_id: string (fk)
  status: active | archived
  config:
    default_raw_agents: string[]
    default_integrations: Integration[]
  created_at: timestamp
  updated_at: timestamp
```

#### Creation Process

**MGT-FR-0002:** Workshop creation SHALL validate name and code uniqueness within the Foundry.

**MGT-FR-0003:** Workshop creation SHALL create a Workshop Definition Repository (Git repo) and initialize it with scaffold structure.

1. Validate workshop name and code uniqueness within Foundry
2. Create Workshop record in database
3. Create Workshop Definition Repository (Git repo)
4. Initialize repository with scaffold structure
5. Return Workshop ID

---

### Workbench Service

**MGT-FR-0004:** The Workbench Service SHALL manage Workbench (Product) lifecycle including create, read, update, archive, and integration management.

Manages Workbench (Product) lifecycle.

#### API Endpoints

```
POST   /api/v1/workbenches                    # Create workbench
GET    /api/v1/workbenches                    # List workbenches
GET    /api/v1/workbenches/{id}               # Get workbench
PUT    /api/v1/workbenches/{id}               # Update workbench
DELETE /api/v1/workbenches/{id}               # Archive workbench
POST   /api/v1/workbenches/{id}/integrations  # Add integration
DELETE /api/v1/workbenches/{id}/integrations/{type}  # Remove integration
```

#### Workbench Entity

```yaml
Workbench:
  id: string (uuid)
  name: string
  product_code: string (unique within workshop)
  description: string
  workshop_id: string (fk)
  status: provisioning | active | archived
  config:
    raw_agents: string[]
    workRepoProjectKey: string   # Canonical work repository project key (Jira-backed in current adapter)
    github_org: string
    github_repos: string[]
  integrations:
    github: GitHubIntegration
    jira: JiraIntegration
    figma: FigmaIntegration
    testrail: TestRailIntegration
    olympus_weave: OlympusWeaveIntegration
  created_at: timestamp
  updated_at: timestamp
```

#### Provisioning Process

**MGT-FR-0005:** Workbench provisioning SHALL validate name and product_code uniqueness within the Workshop.

**MGT-FR-0006:** Workbench provisioning SHALL create an Intent Repository and Design Repository in the GitHub org.

**MGT-FR-0007:** Workbench provisioning SHALL create a Jira project for Work Orders.

**MGT-FR-0008:** Workbench provisioning SHALL provision Metadata Service and Ontology Service instances.

**MGT-FR-0009:** Workbench provisioning SHALL set status to `active` only after all provisioning steps complete successfully.

```
1. Validate workbench name and product_code uniqueness
2. Create Workbench record (status: provisioning)
3. Create/link GitHub organization
   a. If new org: create via GitHub App
   b. If existing: verify permissions, tag repos
4. Create Intent Repository in GitHub org
5. Create Design Repository in GitHub org
6. Create Jira project for Work Orders
7. Link Jira project (Operations, Feedback, Work)
8. Provision Metadata Service instance
9. Provision Ontology Service instance
10. Initialize Workshop Definition Repo scaffold for this Workbench
11. Update status to active
12. Return Workbench ID
```

#### Archival Process

**MGT-FR-0010:** Workbench archival SHALL verify no active Work Orders exist before proceeding.

**MGT-FR-0011:** Workbench archival SHALL preserve GitHub repos and Jira history while disabling access.

**MGT-FR-0012:** Workbench archival SHALL retain all data for audit purposes.

```
1. Verify no active Work Orders
2. Set status to archived
3. Disable GitHub App access (preserve repos)
4. Disable Jira project (preserve history)
5. Stop Metadata and Ontology services
6. Retain all data for audit
```

---

### Metadata Service

**MGT-FR-0013:** The Metadata Service SHALL be provisioned per-Workbench for identity and tracking.

Per-Workbench service for identity and tracking.

#### API Endpoints

```
POST   /api/v1/workbenches/{id}/metadata/ids/{type}     # Generate ID
GET    /api/v1/workbenches/{id}/metadata/commits        # List commits
GET    /api/v1/workbenches/{id}/metadata/commits/{sha}  # Get commit details
GET    /api/v1/workbenches/{id}/metadata/code-repos     # List code repos
POST   /api/v1/workbenches/{id}/metadata/code-repos     # Add code repo
DELETE /api/v1/workbenches/{id}/metadata/code-repos/{repo_id}  # Remove repo
```

#### ID Generation

**MGT-FR-0014:** ID generation SHALL use database sequences per (workbench_id, type) for atomicity.

**MGT-FR-0015:** IDs SHALL be formatted as `{prefix}-{value}` (e.g., `PI-456`).

```yaml
IDSequence:
  workbench_id: string (fk)
  type: product-intent | release-intent | work-order | discovery-case | run-case
  current_value: bigint
  prefix: string (PI, RI, WO, DC, RC)
```

Implementation:
- Use database sequence per (workbench_id, type)
- Atomic increment with `SELECT ... FOR UPDATE` or `RETURNING`
- Format: `{prefix}-{value}` (e.g., `PI-456`)

#### Commit Tracking

```yaml
TrackedCommit:
  id: string (uuid)
  workbench_id: string (fk)
  repository_type: intent | design | code
  repository_name: string
  commit_sha: string
  author: string
  message: string
  timestamp: timestamp
  files_changed: string[]
  orchestration_item_refs: string[]  # PI-123, etc.
```

**MGT-FR-0016:** Commit tracking SHALL use GitHub webhook listener for push events.

**MGT-FR-0017:** Commit tracking SHALL parse commit messages for orchestration item references (e.g., PI-123).

**MGT-FR-0018:** Commit metadata SHALL be stored for traceability queries.

Implementation:
- GitHub webhook listener for push events
- Parse commit messages for orchestration item references
- Store commit metadata for traceability queries

---

### Repository Service

Manages repository lifecycle and configuration.

#### API Endpoints

```
POST   /api/v1/workbenches/{id}/repositories           # Create repository
GET    /api/v1/workbenches/{id}/repositories           # List repositories
GET    /api/v1/workbenches/{id}/repositories/{type}    # Get repository
PUT    /api/v1/workbenches/{id}/repositories/{type}    # Update repository
```

#### Repository Types

| Type | Storage | Management |
|------|---------|------------|
| `intent` | GitHub | Auto-created on Workbench provision |
| `design` | GitHub | Auto-created on Workbench provision |
| `code` | GitHub | Linked manually (1+) |
| `ontology` | Native | Auto-provisioned service |
| `quality` | TestRail + GitHub | Linked on integration setup |
| `operations` | Jira | Linked on integration setup |
| `feedback` | Jira | Linked on integration setup |
| `work` | Jira | Linked on integration setup |

---

### Team Service

**MGT-FR-0019:** The Team Service SHALL manage teams, roles, and permissions within a Workbench.

Manages teams, roles, and permissions.

#### API Endpoints

```
POST   /api/v1/workbenches/{id}/teams                  # Create team
GET    /api/v1/workbenches/{id}/teams                  # List teams
GET    /api/v1/workbenches/{id}/teams/{team_id}        # Get team
PUT    /api/v1/workbenches/{id}/teams/{team_id}        # Update team
DELETE /api/v1/workbenches/{id}/teams/{team_id}        # Delete team
POST   /api/v1/workbenches/{id}/teams/{team_id}/members  # Add member
DELETE /api/v1/workbenches/{id}/teams/{team_id}/members/{user_id}  # Remove member
```

#### Team Entity

```yaml
Team:
  id: string (uuid)
  workbench_id: string (fk)
  name: string
  description: string
  workspace_types: string[]  # Which workspaces this team works in
  members: TeamMember[]

TeamMember:
  user_id: string
  role: admin | member | viewer
  joined_at: timestamp
```

#### Roles and Permissions

**MGT-FR-0020:** Foundry Admins SHALL be able to create workshops and manage foundry settings.

**MGT-FR-0021:** Workshop Admins SHALL be able to create workbenches and manage workshop settings.

**MGT-FR-0022:** Workbench Admins SHALL be able to configure integrations and manage teams.

**MGT-FR-0023:** Team Admins SHALL be able to manage team membership.

**MGT-FR-0024:** Team Members SHALL be able to access workbench resources and execute WOs.

**MGT-FR-0025:** Viewers SHALL have read-only access.

| Role | Capabilities |
|------|--------------|
| **Foundry Admin** | Create workshops, manage foundry settings |
| **Workshop Admin** | Create workbenches, manage workshop settings |
| **Workbench Admin** | Configure integrations, manage teams |
| **Team Admin** | Manage team membership |
| **Team Member** | Access workbench resources, execute WOs |
| **Viewer** | Read-only access |

---

### Integration Service

**MGT-FR-0026:** The Integration Service SHALL manage external tool integrations (GitHub, Jira, TestRail, Figma, Olympus Weave).

**MGT-FR-0027:** Management module events (metadata changes, catalog sync, team lifecycle) SHALL publish to Atropos at paths `/{foundry-id}/foundry.management.{event-semantic-name}` using the canonical envelope defined in [event-contracts.md](../../../foundry-work-plan/phase-1/event-contracts.md).

**MGT-FR-0028:** Foundry provisioning SHALL register Atropos tenant configuration (`integrations.atropos`) and callback authentication for the Foundry.

Manages external tool integrations.

#### Supported Integrations

##### GitHub Integration

```yaml
GitHubIntegration:
  type: github
  org_name: string
  app_installation_id: string
  permissions:
    - repo:admin
    - org:read
  webhook_secret: string (encrypted)
  status: active | disconnected
```

Setup process:
1. User installs Foundry GitHub App on their org
2. OAuth callback stores installation_id
3. Management tags existing repos with Foundry metadata
4. Webhooks configured for push events

##### Work Repository integration (Jira adapter)

```yaml
WorkRepositoryIntegration:
  type: jira                    # adapter identifier; contract fields remain workRepo*
  site_url: string
  project_keys:
    work_orders: string         # maps to workRepoProject for WOs
    operations: string
    feedback: string
    work: string
  label_prefix: foundry-         # canonical label namespace
  custom_fields:                # adapter maps to foundry-* attributes
    foundry-scenario: string
    foundry-workbench: string
    foundry-orchestration-item: string
    foundry-wo-group: string
  oauth_token: string (encrypted)
  status: active | disconnected
```

Setup process:
1. User authorizes Jira OAuth
2. User selects/creates projects
3. Management configures custom fields for `foundry-*` attributes and applies label filters (`foundry-workbench-{workbenchId}`)
4. Webhooks configured for issue events

##### TestRail Integration

```yaml
TestRailIntegration:
  type: testrail
  instance_url: string
  project_id: string
  oauth_token: string (encrypted)
  status: active | disconnected
```

##### Figma Integration

```yaml
FigmaIntegration:
  type: figma
  team_id: string
  oauth_token: string (encrypted)
  status: active | disconnected
```

##### Olympus Weave Integration

```yaml
OlympusWeaveIntegration:
  type: olympus_weave
  product_code: string  # Assigned by Weave
  module_codes: string[]
  webhook_url: string
  api_key: string (encrypted)
  status: active | disconnected
```

---

## Database Schema

### Core Tables

```sql
CREATE TABLE foundries (
  id UUID PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  code VARCHAR(63) UNIQUE NOT NULL,
  config JSONB,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE workshops (
  id UUID PRIMARY KEY,
  foundry_id UUID REFERENCES foundries(id),
  name VARCHAR(255) NOT NULL,
  code VARCHAR(63) NOT NULL,
  status VARCHAR(20) DEFAULT 'active',
  config JSONB,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(foundry_id, code)
);

CREATE TABLE workbenches (
  id UUID PRIMARY KEY,
  workshop_id UUID REFERENCES workshops(id),
  name VARCHAR(255) NOT NULL,
  product_code VARCHAR(63) NOT NULL,
  status VARCHAR(20) DEFAULT 'provisioning',
  config JSONB,
  integrations JSONB,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(workshop_id, product_code)
);

CREATE TABLE id_sequences (
  workbench_id UUID REFERENCES workbenches(id),
  type VARCHAR(20) NOT NULL,
  current_value BIGINT DEFAULT 0,
  prefix VARCHAR(5) NOT NULL,
  PRIMARY KEY (workbench_id, type)
);

CREATE TABLE tracked_commits (
  id UUID PRIMARY KEY,
  workbench_id UUID REFERENCES workbenches(id),
  repository_type VARCHAR(20) NOT NULL,
  repository_name VARCHAR(255) NOT NULL,
  commit_sha VARCHAR(40) NOT NULL,
  author VARCHAR(255),
  message TEXT,
  timestamp TIMESTAMP,
  files_changed JSONB,
  orchestration_item_refs VARCHAR(20)[],
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE teams (
  id UUID PRIMARY KEY,
  workbench_id UUID REFERENCES workbenches(id),
  name VARCHAR(255) NOT NULL,
  description TEXT,
  workspace_types VARCHAR(50)[],
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE team_members (
  team_id UUID REFERENCES teams(id),
  user_id VARCHAR(255) NOT NULL,
  role VARCHAR(20) NOT NULL,
  joined_at TIMESTAMP DEFAULT NOW(),
  PRIMARY KEY (team_id, user_id)
);
```

---

## Error Handling

### Standard Error Response

```json
{
  "error": {
    "code": "WORKBENCH_PROVISIONING_FAILED",
    "message": "Failed to create GitHub organization",
    "details": {
      "step": "github_org_creation",
      "github_error": "Rate limit exceeded"
    }
  }
}
```

### Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `WORKSHOP_NOT_FOUND` | 404 | Workshop ID does not exist |
| `WORKBENCH_NOT_FOUND` | 404 | Workbench ID does not exist |
| `WORKBENCH_PROVISIONING_FAILED` | 500 | Provisioning step failed |
| `INTEGRATION_AUTH_FAILED` | 401 | OAuth token expired or invalid |
| `INTEGRATION_NOT_CONFIGURED` | 400 | Required integration not set up |
| `DUPLICATE_CODE` | 409 | Workshop/Workbench code already exists |
| `QUOTA_EXCEEDED` | 429 | Rate limit or resource quota exceeded |

### Retry Policy

**MGT-NFR-0001:** GitHub API calls SHALL retry up to 3 times with exponential backoff (1s, 2s, 4s).

**MGT-NFR-0002:** Jira API calls SHALL retry up to 3 times with exponential backoff (1s, 2s, 4s).

**MGT-NFR-0003:** Database operations SHALL retry up to 2 times with fixed 100ms backoff.

**MGT-NFR-0004:** Webhook delivery SHALL retry up to 5 times with exponential backoff (1m, 2m, 4m, 8m, 16m).

| Operation | Retry Count | Backoff |
|-----------|-------------|---------|
| GitHub API | 3 | Exponential (1s, 2s, 4s) |
| Jira API | 3 | Exponential (1s, 2s, 4s) |
| Database | 2 | Fixed (100ms) |
| Webhook delivery | 5 | Exponential (1m, 2m, 4m, 8m, 16m) |

---

## Scalability

### Multi-Tenancy

**MGT-NFR-0005:** Each Foundry SHALL be isolated at the database level using row-level security.

**MGT-NFR-0006:** API authentication SHALL include Foundry context.

**MGT-NFR-0007:** Cross-Foundry queries SHALL be prohibited.

- Each Foundry is isolated at the database level (row-level security)
- API authentication includes Foundry context
- Cross-Foundry queries are prohibited

### Service Scaling

| Service | Scaling Model |
|---------|---------------|
| API Gateway | Horizontal (load balanced) |
| Workshop Service | Horizontal (stateless) |
| Workbench Service | Horizontal (stateless) |
| Metadata Service | Per-Workbench instance (can scale horizontally) |
| Ontology Service | Per-Workbench instance |

### Database Scaling

- Primary for writes
- Read replicas for queries
- Partition by Foundry ID for large deployments

---

## Observability

### Metrics

| Metric | Type | Description |
|--------|------|-------------|
| `management.workbenches.provisioned` | Counter | Workbenches successfully provisioned |
| `management.workbenches.provisioning_duration` | Histogram | Time to provision workbench |
| `management.integrations.status` | Gauge | Integration health (1=active, 0=disconnected) |
| `management.metadata.ids_generated` | Counter | IDs generated by type |
| `management.commits.tracked` | Counter | Commits tracked |

### Logging

Structured JSON logs with:
- `request_id` — Correlation ID
- `foundry_id` — Tenant context
- `workshop_id` — Workshop context (if applicable)
- `workbench_id` — Workbench context (if applicable)
- `operation` — API operation name
- `duration_ms` — Operation duration

### Health Checks

```
GET /health          # Liveness probe
GET /health/ready    # Readiness probe (includes DB, GitHub, Jira connectivity)
```

---

## Security

### Authentication

**MGT-NFR-0008:** API requests SHALL be authenticated via JWT tokens.

**MGT-NFR-0009:** Inter-service communication SHALL use service accounts.

**MGT-NFR-0010:** OAuth tokens for external integrations SHALL be encrypted at rest.

- API requests authenticated via JWT tokens
- Service accounts for inter-service communication
- OAuth tokens for external integrations (encrypted at rest)

### Authorization

**MGT-NFR-0011:** Authorization SHALL use role-based access control (RBAC) with Foundry Admin > Workshop Admin > Workbench Admin hierarchy.

**MGT-NFR-0012:** API endpoints SHALL enforce authorization based on user's highest role in scope.

- Role-based access control (RBAC)
- Foundry Admin → Workshop Admin → Workbench Admin hierarchy
- API endpoints enforce authorization based on user's highest role in scope

### Secrets Management

**MGT-NFR-0013:** Integration credentials SHALL be stored encrypted using AES-256.

**MGT-NFR-0014:** Encryption keys SHALL be stored in a secrets manager (HashiCorp Vault, AWS Secrets Manager).

**MGT-NFR-0015:** Credentials SHALL never be logged or exposed in API responses.

- Integration credentials stored encrypted (AES-256)
- Encryption key in secrets manager (e.g., HashiCorp Vault, AWS Secrets Manager)
- Credentials never logged or exposed in API responses

---

## External dependencies

| Dependency | Integration | Failure mode |
|------------|-------------|--------------|
| GitHub | REST API + webhooks | Retry with backoff |
| Jira | REST API + OAuth | Retry with backoff |
| Atropos | HTTP publish + callbacks | Queue locally, retry with backoff |
| PostgreSQL | Connection pool | Retry with backoff |
| Redis | Cache | Bypass cache, query directly |

---

## Open Implementation Questions

- Workbench deletion vs archival — hard delete or soft delete with TTL?
- GitHub org sharing model — one org per Workbench or shared orgs?
- Jira project naming convention
- User identity provider integration (SAML, OIDC)
- Webhook signature verification across integrations

## Read Next

- [../../../foundry-work-plan/phase-1/event-contracts.md](../../../foundry-work-plan/phase-1/event-contracts.md) — Atropos event transport SSOT
- [../../../foundry-work-plan/phase-1/repository-contracts.md](../../../foundry-work-plan/phase-1/repository-contracts.md) — Phase 1 entity and label SSOT
- [workbench-architecture.md](workbench-architecture.md) — Workbench repository storage model
- [workshop-repository.md](workshop-repository.md) — Workshop Definition Repository structure
- [../orchestrator/platform-developer-guide/requirements.md](..//orchestrator/platform-developer-guide/requirements.md) — Orchestrator requirements
