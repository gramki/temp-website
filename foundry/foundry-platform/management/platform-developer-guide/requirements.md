# Management Module Requirements

This document specifies detailed implementation requirements for the Foundry Management module.

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
    default_capable_agents: string[]
    default_integrations: Integration[]
  created_at: timestamp
  updated_at: timestamp
```

#### Creation Process

1. Validate workshop name and code uniqueness within Foundry
2. Create Workshop record in database
3. Create Workshop Definition Repository (Git repo)
4. Initialize repository with scaffold structure
5. Return Workshop ID

---

### Workbench Service

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
    capable_agents: string[]
    jira_project_key: string
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

##### Jira Integration

```yaml
JiraIntegration:
  type: jira
  site_url: string
  project_keys:
    work_orders: string
    operations: string
    feedback: string
  oauth_token: string (encrypted)
  status: active | disconnected
```

Setup process:
1. User authorizes Jira OAuth
2. User selects/creates projects
3. Management configures custom fields for Foundry attributes
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

| Operation | Retry Count | Backoff |
|-----------|-------------|---------|
| GitHub API | 3 | Exponential (1s, 2s, 4s) |
| Jira API | 3 | Exponential (1s, 2s, 4s) |
| Database | 2 | Fixed (100ms) |
| Webhook delivery | 5 | Exponential (1m, 2m, 4m, 8m, 16m) |

---

## Scalability

### Multi-Tenancy

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

- API requests authenticated via JWT tokens
- Service accounts for inter-service communication
- OAuth tokens for external integrations (encrypted at rest)

### Authorization

- Role-based access control (RBAC)
- Foundry Admin → Workshop Admin → Workbench Admin hierarchy
- API endpoints enforce authorization based on user's highest role in scope

### Secrets Management

- Integration credentials stored encrypted (AES-256)
- Encryption key in secrets manager (e.g., HashiCorp Vault, AWS Secrets Manager)
- Credentials never logged or exposed in API responses

---

## Open Implementation Questions

- Workbench deletion vs archival — hard delete or soft delete with TTL?
- GitHub org sharing model — one org per Workbench or shared orgs?
- Jira project naming convention
- User identity provider integration (SAML, OIDC)
- Webhook signature verification across integrations

## Read Next

- [workbench-architecture.md](workbench-architecture.md) — Workbench repository storage model
- [workshop-repository.md](workshop-repository.md) — Workshop Definition Repository structure
- [../orchestrator/orchestrator-requirements.md](../orchestrator/orchestrator-requirements.md) — Orchestrator requirements
