# Agent Fabric Requirements

This document specifies detailed implementation requirements for the Agent Fabric module.

## Key Concepts

This module implements several platform concepts. For definitions, see:

| Concept | Link |
|---------|------|
| Agent Model | [../../concepts/agent-model.md](../../concepts/agent-model.md) |
| Skill | [../../concepts/skill.md](../../concepts/skill.md) |
| Delegation | [../../concepts/delegation.md](../../concepts/delegation.md) |
| Governance | [../../concepts/governance.md](../../concepts/governance.md) |

Module-specific concepts (internals):

| Concept | Link |
|---------|------|
| Raw Agent | [../concepts/raw-agent.md](../concepts/raw-agent.md) |
| Trained Agent | [../concepts/trained-agent.md](../concepts/trained-agent.md) |
| Employed Agent | [../concepts/employed-agent.md](../concepts/employed-agent.md) |
| Quota Management | [../concepts/quota-management.md](../concepts/quota-management.md) |
| Usage Analytics | [../concepts/usage-analytics.md](../concepts/usage-analytics.md) |

## ACE alignment

| ACE concept | How this module realizes it |
|-------------|---------------------------|
| **Agent** | Manages the three-tier agent model: Raw Agent → Trained Agent → Employed Agent |
| **Skill** | Provides Skill Registry for publishing, versioning, and distributing skill packages |
| **Delegation** | Issues Delegation Tokens via Gateway Policy Layer for scoped authority |
| **Workspace** | Quota and policy enforcement scoped to Workbench and Workspace context |

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                               Agent Fabric                                       │
│                                                                                  │
│  ┌─────────────────────────────────────────────────────────────────────────────┐│
│  │                         Skill Registry Service                               ││
│  │                                                                              ││
│  │  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐        ││
│  │  │  Global Registry │    │ Foundry Registry │    │  CLI (gh ext)   │        ││
│  │  │    (public)      │    │    (private)     │    │                 │        ││
│  │  └────────┬─────────┘    └────────┬─────────┘    └────────┬────────┘        ││
│  │           │                       │                       │                 ││
│  │           └───────────────────────┴───────────────────────┘                 ││
│  └─────────────────────────────────────────────────────────────────────────────┘│
│                                                                                  │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐            │
│  │  Capable    │  │   Quota     │  │   Usage     │  │  Gateway    │            │
│  │   Agent     │  │  Manager    │  │  Analytics  │  │   Policy    │            │
│  │  Registry   │  │             │  │             │  │   Layer     │            │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘            │
│         │                │                │                │                    │
│         └────────────────┴────────────────┴────────────────┘                    │
│                                    │                                            │
└────────────────────────────────────┼────────────────────────────────────────────┘
         │                           │                           │
         ▼                           ▼                           ▼
┌─────────────────┐    ┌─────────────────────┐    ┌─────────────────────┐
│   WO Runtime    │    │   OSS LLM Gateway   │    │    Secrets Store    │
│   (consumer)    │    │  (LiteLLM/Portkey)  │    │ (credentials vault) │
└─────────────────┘    └─────────────────────┘    └─────────────────────┘
```

## Core Components

### Skill Registry Service

**AGF-FR-0001:** The Skill Registry Service SHALL store, version, and serve skill packages.

**AGF-FR-0002:** The Skill Registry Service SHALL support publish requests, search queries, and package downloads.

| Aspect | Detail |
|--------|--------|
| Responsibility | Store, version, and serve skill packages |
| Input | Skill packages (tar.gz), publish requests, search queries |
| Output | Skill metadata, package downloads, search results |
| Dependencies | Object storage (S3/GCS), PostgreSQL for metadata |

### Raw Agent Registry

**AGF-FR-0003:** The Raw Agent Registry SHALL manage the whitelist of agent systems and their credentials.

**AGF-FR-0004:** The Raw Agent Registry SHALL compute effective agent config using Workbench > Workshop > Foundry precedence.

| Aspect | Detail |
|--------|--------|
| Responsibility | Manage whitelist of agent systems and their credentials |
| Input | Agent configuration from Workshop Definition Repo |
| Output | Effective agent config, credential references |
| Dependencies | Secrets store (Vault/KMS), Metadata Service |

### Quota Manager

**AGF-FR-0005:** The Quota Manager SHALL track usage events from the Gateway Policy Layer.

**AGF-FR-0006:** The Quota Manager SHALL enforce usage limits and return quota status.

**AGF-FR-0007:** Effective quota SHALL be the minimum of all applicable quotas (Foundry, Workbench, User).

| Aspect | Detail |
|--------|--------|
| Responsibility | Track and enforce usage limits |
| Input | Usage events from Gateway Policy Layer |
| Output | Quota status, enforcement decisions |
| Dependencies | PostgreSQL for usage tracking, Redis for real-time counters |

### Gateway Policy Layer

**AGF-FR-0008:** The Gateway Policy Layer SHALL validate delegation tokens before processing requests.

**AGF-FR-0009:** The Gateway Policy Layer SHALL enforce quota policy before forwarding requests.

**AGF-FR-0010:** The Gateway Policy Layer SHALL inject credentials and attribution metadata into requests.

| Aspect | Detail |
|--------|--------|
| Responsibility | Validate tokens, enforce policy, inject credentials |
| Input | Model requests with delegation tokens |
| Output | Enriched requests to OSS gateway |
| Dependencies | OSS LLM Gateway, Raw Agent Registry, Quota Manager |

### Usage Analytics Service

| Aspect | Detail |
|--------|--------|
| Responsibility | Aggregate and report on agent/skill usage |
| Input | Usage events from Gateway Policy Layer |
| Output | Reports, dashboards, cost attribution |
| Dependencies | ClickHouse or TimescaleDB for analytics |

---

## Database Schema

### Skill Registry Database

| Table | Purpose |
|-------|---------|
| `skills` | Skill metadata (name, version, author, created_at) |
| `skill_versions` | Version history and package references |
| `skill_dependencies` | Skill dependency graph |
| `skill_downloads` | Download counts and analytics |

**Key columns:**

```sql
CREATE TABLE skills (
    id UUID PRIMARY KEY,
    registry TEXT NOT NULL,  -- 'global' or 'foundry:{id}'
    name TEXT NOT NULL,
    author TEXT NOT NULL,
    description TEXT,
    keywords TEXT[],
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(registry, name)
);

CREATE TABLE skill_versions (
    id UUID PRIMARY KEY,
    skill_id UUID REFERENCES skills(id),
    version TEXT NOT NULL,
    package_url TEXT NOT NULL,
    package_sha256 TEXT NOT NULL,
    dependencies JSONB,
    compatible_agents TEXT[],
    published_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(skill_id, version)
);

CREATE INDEX idx_skills_registry ON skills(registry);
CREATE INDEX idx_skill_versions_skill ON skill_versions(skill_id);
```

### Raw Agent Registry Database

| Table | Purpose |
|-------|---------|
| `raw_agents` | Agent definitions (system-level) |
| `agent_configs` | Per-level configurations (Foundry/Workshop/Workbench) |
| `model_configs` | Per-model settings and credentials |

**Key columns:**

```sql
CREATE TABLE raw_agents (
    id TEXT PRIMARY KEY,  -- e.g., 'cursor-agent'
    type TEXT NOT NULL,   -- 'ide-agent', 'cli-agent'
    provider TEXT NOT NULL,
    supported_models TEXT[],
    spawn_adapter TEXT    -- implementation reference
);

CREATE TABLE agent_configs (
    id UUID PRIMARY KEY,
    agent_id TEXT REFERENCES raw_agents(id),
    scope_type TEXT NOT NULL,  -- 'foundry', 'workshop', 'workbench'
    scope_id TEXT NOT NULL,
    enabled BOOLEAN DEFAULT TRUE,
    config JSONB,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(agent_id, scope_type, scope_id)
);

CREATE TABLE model_configs (
    id UUID PRIMARY KEY,
    agent_config_id UUID REFERENCES agent_configs(id),
    model TEXT NOT NULL,
    enabled BOOLEAN DEFAULT TRUE,
    credential_ref TEXT,  -- reference to secrets store
    UNIQUE(agent_config_id, model)
);
```

### Quota Database

| Table | Purpose |
|-------|---------|
| `quota_policies` | Quota limits per scope |
| `usage_counters` | Real-time usage tracking |
| `usage_history` | Historical usage for reporting |

**Key columns:**

```sql
CREATE TABLE quota_policies (
    id UUID PRIMARY KEY,
    scope_type TEXT NOT NULL,  -- 'foundry', 'workbench', 'user', etc.
    scope_id TEXT NOT NULL,
    monthly_budget_usd DECIMAL(10,2),
    daily_token_limit BIGINT,
    effective_from TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(scope_type, scope_id)
);

CREATE TABLE usage_counters (
    scope_type TEXT NOT NULL,
    scope_id TEXT NOT NULL,
    period TEXT NOT NULL,  -- '2026-05' for monthly, '2026-05-28' for daily
    tokens_used BIGINT DEFAULT 0,
    cost_usd DECIMAL(10,4) DEFAULT 0,
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    PRIMARY KEY(scope_type, scope_id, period)
);

CREATE TABLE usage_history (
    id UUID PRIMARY KEY,
    timestamp TIMESTAMPTZ NOT NULL,
    session_owner TEXT NOT NULL,
    workbench_id TEXT NOT NULL,
    work_order TEXT,
    task TEXT,
    trained_agent TEXT,
    raw_agent TEXT,
    model TEXT NOT NULL,
    input_tokens INT NOT NULL,
    output_tokens INT NOT NULL,
    cost_usd DECIMAL(10,6) NOT NULL,
    latency_ms INT
);

CREATE INDEX idx_usage_history_time ON usage_history(timestamp);
CREATE INDEX idx_usage_history_owner ON usage_history(session_owner, timestamp);
CREATE INDEX idx_usage_history_workbench ON usage_history(workbench_id, timestamp);
```

---

## Integration Details

### Workshop Sync Integration

| Aspect | Detail |
|--------|--------|
| Integration type | Event consumer |
| Direction | Inbound (Workshop Sync → Agent Fabric) |
| Events | `config.updated` with Raw Agent and quota configs |

When Workshop Sync writes config to Metadata Service, Agent Fabric refreshes:
- Raw Agent configurations
- Quota policies
- Trained Agent manifests (for reference validation)

### OSS LLM Gateway Integration

| Aspect | Detail |
|--------|--------|
| Integration type | HTTP middleware / sidecar |
| Direction | Intercept and enrich |
| Authentication | Service account token |

The Gateway Policy Layer runs as middleware before the OSS gateway:

```
Agent Request → Policy Layer → OSS Gateway → Provider
                    │
                    ├── Validate delegation token
                    ├── Check quota
                    ├── Inject credentials
                    └── Tag with attribution metadata
```

### Secrets Store Integration

| Aspect | Detail |
|--------|--------|
| Integration type | REST API |
| Supported stores | HashiCorp Vault, AWS Secrets Manager, GCP Secret Manager |
| Usage | Retrieve credentials for Raw Agents |

```
credential_ref: "vault://foundry/anthropic-api-key"
         ↓
Secrets client resolves to actual API key at request time
```

---

## Processing Logic

### Skill Version Resolution

**AGF-FR-0011:** Skill version resolution SHALL check the Foundry registry first, then fall back to the Global registry.

**AGF-FR-0012:** Skill version resolution SHALL return the highest matching version within the semver constraint.

**AGF-FR-0013:** Skill version resolution SHALL raise `SkillNotFoundError` if no matching version is found in any registry.

```python
def resolve_skill_version(name: str, constraint: str, foundry_id: str) -> SkillVersion:
    # 1. Parse constraint (e.g., "^2.1.0")
    constraint = parse_semver_constraint(constraint)
    
    # 2. Check Foundry registry first
    foundry_versions = get_versions(registry=f"foundry:{foundry_id}", name=name)
    matching = [v for v in foundry_versions if constraint.matches(v.version)]
    if matching:
        return max(matching, key=lambda v: parse_version(v.version))
    
    # 3. Fall back to Global registry
    global_versions = get_versions(registry="global", name=name)
    matching = [v for v in global_versions if constraint.matches(v.version)]
    if matching:
        return max(matching, key=lambda v: parse_version(v.version))
    
    raise SkillNotFoundError(name, constraint)
```

### Effective Quota Calculation

```python
def get_effective_quota(user: str, workbench_id: str) -> Quota:
    # Collect all applicable quotas
    quotas = []
    
    # Foundry-level
    foundry_quota = get_quota(scope_type="foundry", scope_id=foundry_id)
    if foundry_quota:
        quotas.append(foundry_quota)
    
    # Workbench-level
    workbench_quota = get_quota(scope_type="workbench", scope_id=workbench_id)
    if workbench_quota:
        quotas.append(workbench_quota)
    
    # (Foundry, User) level
    foundry_user_quota = get_quota(scope_type="foundry_user", scope_id=f"{foundry_id}:{user}")
    if foundry_user_quota:
        quotas.append(foundry_user_quota)
    
    # (Workbench, User) level
    workbench_user_quota = get_quota(scope_type="workbench_user", scope_id=f"{workbench_id}:{user}")
    if workbench_user_quota:
        quotas.append(workbench_user_quota)
    
    # Effective = minimum of all
    return Quota(
        monthly_budget_usd=min(q.monthly_budget_usd for q in quotas if q.monthly_budget_usd),
        daily_token_limit=min(q.daily_token_limit for q in quotas if q.daily_token_limit)
    )
```

### Credential Resolution

```python
def resolve_credentials(agent_id: str, model: str, workbench_id: str) -> Credentials:
    # Resolution order: Workbench → Workshop → Foundry
    for scope_type, scope_id in [
        ("workbench", workbench_id),
        ("workshop", get_workshop_id(workbench_id)),
        ("foundry", get_foundry_id(workbench_id))
    ]:
        config = get_model_config(agent_id, scope_type, scope_id, model)
        if config and config.credential_ref:
            return secrets_client.get(config.credential_ref)
    
    raise CredentialsNotFoundError(agent_id, model)
```

---

## Error Handling

### Retry Policy

**AGF-NFR-0001:** For secrets store timeouts, Agent Fabric SHALL retry with exponential backoff (100ms, 200ms, 400ms) up to 3 times.

**AGF-NFR-0002:** For registry unavailability, Agent Fabric SHALL retry with exponential backoff (1s, 2s, 4s) up to 5 times.

**AGF-FR-0014:** Gateway policy validation failures SHALL NOT be retried (fail fast).

**AGF-FR-0015:** Quota checks SHALL NOT be retried (authoritative response).

| Failure Type | Strategy |
|--------------|----------|
| Secrets store timeout | Exponential backoff: 100ms, 200ms, 400ms (3 retries) |
| Registry unavailable | Exponential backoff: 1s, 2s, 4s (5 retries) |
| Gateway policy validation | No retry (fail fast) |
| Quota check | No retry (authoritative) |

### Error Responses

**AGF-FR-0016:** For skill not found errors, the API SHALL return HTTP 404 with skill name and constraint.

**AGF-FR-0017:** For quota exceeded errors, the API SHALL return HTTP 429 with reset time and limit.

**AGF-FR-0018:** For invalid delegation token errors, the API SHALL return HTTP 401 with reason.

**AGF-FR-0019:** For agent disabled errors, the API SHALL return HTTP 403 with agent and scope.

**AGF-NFR-0003:** Credentials not found errors SHALL NOT be exposed to clients (internal 500 error).

| Error | HTTP Status | Response |
|-------|-------------|----------|
| Skill not found | 404 | `{ "error": "skill_not_found", "name": "...", "constraint": "..." }` |
| Quota exceeded | 429 | `{ "error": "quota_exceeded", "reset_at": "...", "limit": "..." }` |
| Invalid delegation token | 401 | `{ "error": "invalid_token", "reason": "..." }` |
| Agent disabled | 403 | `{ "error": "agent_disabled", "agent": "...", "scope": "..." }` |
| Credentials not found | 500 | `{ "error": "credentials_not_found" }` (internal, not exposed) |

### Recoverable Failures

Tasks encountering these errors enter recoverable failure state:

| Error | Resume Trigger |
|-------|----------------|
| `quota_exceeded` | Quota refreshes (daily/monthly) or limit increased |
| `agent_disabled` | Agent re-enabled at applicable scope |
| `all_fallbacks_exhausted` | Any fallback option restored |

---

## Authorization

### Skill Registry Permissions

**AGF-FR-0020:** Foundry Admins SHALL be able to publish to the Foundry registry and manage Global registry submissions.

**AGF-FR-0021:** Workshop Admins SHALL be able to read all skills and publish to the Foundry registry.

**AGF-FR-0022:** Workbench Admins SHALL be able to read all skills.

**AGF-FR-0023:** Developers SHALL be able to read all skills and install to their session.

| Role | Scope | Permissions |
|------|-------|-------------|
| Foundry Admin | Foundry | Publish to Foundry registry, manage Global registry submissions |
| Workshop Admin | Workshop | Read all, publish to Foundry registry |
| Workbench Admin | Workbench | Read all |
| Developer | Session | Read all, install to session |

### Raw Agent Permissions

**AGF-FR-0024:** Foundry Admins SHALL be able to enable/disable agents and manage credentials.

**AGF-FR-0025:** Workshop and Workbench Admins SHALL be able to override agent enable/disable and credentials at their scope.

| Role | Scope | Permissions |
|------|-------|-------------|
| Foundry Admin | Foundry | Enable/disable agents, manage credentials |
| Workshop Admin | Workshop | Override enable/disable, override credentials |
| Workbench Admin | Workbench | Override enable/disable, override credentials |

### Quota Permissions

**AGF-FR-0026:** Foundry Admins SHALL be able to set all quotas.

**AGF-FR-0027:** Workshop Admins SHALL be able to set Workshop/Workbench quotas within Foundry limits.

**AGF-FR-0028:** Workbench Admins SHALL be able to view quotas.

| Role | Scope | Permissions |
|------|-------|-------------|
| Foundry Admin | Foundry | Set all quotas |
| Workshop Admin | Workshop | Set Workshop/Workbench quotas (within Foundry limits) |
| Workbench Admin | Workbench | View quotas |

---

## API Specification

### Skill Registry API

```
# Publish skill
POST /api/v1/skills
Content-Type: multipart/form-data
Body: { package: <tar.gz>, registry: "foundry" | "global" }
Response: { skill_id, name, version }

# Get skill metadata
GET /api/v1/skills/{registry}/{name}
Response: { name, description, author, versions: [...] }

# Get specific version
GET /api/v1/skills/{registry}/{name}/{version}
Response: { name, version, package_url, dependencies, compatible_agents }

# Download package
GET /api/v1/skills/{registry}/{name}/{version}/package
Response: <tar.gz binary>

# Search skills
GET /api/v1/skills/search?q={query}&registry={registry}&compatible_agent={agent}
Response: { results: [{ name, description, version, downloads }] }

# Resolve version
POST /api/v1/skills/resolve
Body: { name, constraint, foundry_id }
Response: { name, version, package_url }
```

### Raw Agent API

```
# List agents
GET /api/v1/raw-agents?scope_type={type}&scope_id={id}
Response: { agents: [{ id, type, provider, enabled, models }] }

# Get effective config
GET /api/v1/raw-agents/{agent_id}/effective?workbench_id={id}
Response: { agent_id, enabled, models: [{ model, enabled }] }

# Update config (admin)
PUT /api/v1/raw-agents/{agent_id}/config
Body: { scope_type, scope_id, enabled, models: [...] }
Response: { success: true }
```

### Quota API

```
# Get effective quota
GET /api/v1/quotas/effective?user={user}&workbench_id={id}
Response: { monthly_budget_usd, daily_token_limit, current_usage }

# Get usage
GET /api/v1/usage?user={user}&workbench_id={id}&period={period}
Response: { tokens_used, cost_usd, by_model: {...} }

# Set quota policy (admin)
PUT /api/v1/quotas
Body: { scope_type, scope_id, monthly_budget_usd, daily_token_limit }
Response: { success: true }
```

### Gateway Policy API (Internal)

```
# Validate and enrich request (called by middleware)
POST /api/v1/gateway/validate
Body: { delegation_token, model, estimated_tokens }
Response: { 
  allowed: true, 
  credentials: { api_key: "..." },
  attribution: { session_owner, workbench_id, work_order, task }
}
```

---

## Scalability

### Skill Registry

**AGF-NFR-0004:** Skill package storage SHALL use object storage (S3/GCS) with CDN.

**AGF-NFR-0005:** Skill metadata queries SHALL use PostgreSQL with read replicas.

**AGF-NFR-0006:** High download volume SHALL be supported via CDN caching and signed URLs.

| Concern | Approach |
|---------|----------|
| Package storage | Object storage (S3/GCS) with CDN |
| Metadata queries | PostgreSQL with read replicas |
| High download volume | CDN caching, signed URLs |

### Quota Tracking

**AGF-NFR-0007:** Real-time counters SHALL use Redis with atomic increments.

**AGF-NFR-0008:** Quota checks SHALL use Redis for current period, PostgreSQL for history.

**AGF-NFR-0009:** High throughput SHALL be supported via partitioning by workbench_id.

| Concern | Approach |
|---------|----------|
| Real-time counters | Redis with atomic increments |
| Quota checks | Redis for current period, PostgreSQL for history |
| High throughput | Partitioned by workbench_id |

### Gateway Policy Layer

**AGF-NFR-0010:** Request validation SHALL be stateless and horizontally scalable.

**AGF-NFR-0011:** Token validation SHALL use JWT verification without DB lookup.

**AGF-NFR-0012:** Credential caching SHALL use short TTL cache (5 min) to reduce Vault calls.

| Concern | Approach |
|---------|----------|
| Request validation | Stateless, horizontally scalable |
| Token validation | JWT verification (no DB lookup) |
| Credential caching | Short TTL cache (5 min) to reduce Vault calls |

---

## Observability

### Metrics

| Metric | Type | Description |
|--------|------|-------------|
| `skill_registry_downloads_total` | Counter | Downloads by skill, version, registry |
| `skill_registry_publishes_total` | Counter | Publishes by registry |
| `quota_checks_total` | Counter | Quota checks by result (allowed/denied) |
| `quota_usage_ratio` | Gauge | Current usage / limit by scope |
| `gateway_requests_total` | Counter | Requests by model, agent, result |
| `gateway_latency_seconds` | Histogram | Policy layer processing time |
| `credential_resolution_duration` | Histogram | Time to resolve credentials |
| `model_cost_usd` | Counter | Cost by model, workbench, user |

### Logging

Structured JSON logs with:

| Field | Description |
|-------|-------------|
| `correlation_id` | Request trace ID |
| `operation` | `skill_download`, `quota_check`, `gateway_validate` |
| `result` | `success`, `denied`, `error` |
| `user` | Session owner |
| `workbench_id` | Workbench context |
| `duration_ms` | Operation duration |

### Tracing

OpenTelemetry spans for:
- Skill resolution and download
- Quota check and enforcement
- Credential resolution
- Gateway validation pipeline

---

## External Dependencies

| Dependency | Integration | Failure Mode |
|------------|-------------|--------------|
| PostgreSQL | Primary data store | Retry with backoff, fail if unavailable |
| Redis | Real-time counters | Fall back to PostgreSQL (degraded performance) |
| Object Storage | Skill packages | Return cached URL if available, fail otherwise |
| Secrets Store | Credentials | Retry with backoff, fail task if unavailable |
| OSS LLM Gateway | Request forwarding | Pass through errors to caller |
| Metadata Service | Config sync | Use cached config, log warning |

---

## Open Implementation Questions

- Skill package size limits and storage quotas
- Global registry governance and moderation process
- Skill signing key management and rotation
- Offline/air-gapped deployment (registry mirroring)
- Credential rotation without service interruption
- Cost model updates (new models, pricing changes)
- Analytics retention policy and data archival

## Read Next

- [../user-guide/agent-lifecycle.md](../user-guide/agent-lifecycle.md) — End-to-end agent lifecycle
- [skill-registry.md](skill-registry.md) — Skill distribution details
- [gateway-policy.md](gateway-policy.md) — Gateway configuration
- [raw-agents.md](raw-agents.md) — Agent registry details
