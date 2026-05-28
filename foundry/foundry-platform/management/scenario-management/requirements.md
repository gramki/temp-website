# Scenario Management Requirements

This document specifies detailed implementation requirements for the Scenario Management subsystem within the Management module.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           Scenario Management                                    │
│                                                                                  │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐             │
│  │  Schema Service │    │   Validation    │    │     Agent       │             │
│  │                 │    │    Service      │    │  Recommender    │             │
│  │  • Schema store │    │  • Validate PRs │    │  • Match skills │             │
│  │  • Versioning   │    │  • Check refs   │    │  • Score agents │             │
│  └────────┬────────┘    └────────┬────────┘    └────────┬────────┘             │
│           │                      │                      │                       │
│           └──────────────────────┴──────────────────────┘                       │
│                                  │                                              │
│                           ┌──────┴──────┐                                       │
│                           │  Scenario   │                                       │
│                           │   Cache     │                                       │
│                           │  (Redis)    │                                       │
│                           └─────────────┘                                       │
└────────────────────────────────────────────────────────────────────────────────┘
         │                         │                         │
         ▼                         ▼                         ▼
┌─────────────────┐    ┌─────────────────────┐    ┌─────────────────────┐
│    Workshop     │    │    Metadata         │    │    WO Runtime       │
│   Validation    │    │    Service          │    │ (recommendations)   │
│    Service      │    │   (storage)         │    │                     │
└─────────────────┘    └─────────────────────┘    └─────────────────────┘
```

## Core Components

### Schema Service

| Aspect | Detail |
|--------|--------|
| Responsibility | Manage scenario schema versions and provide schema for validation |
| Input | Schema version requests, schema updates |
| Output | Schema definitions, schema metadata |
| Dependencies | PostgreSQL for schema storage |

### Validation Service

| Aspect | Detail |
|--------|--------|
| Responsibility | Validate scenario YAML against schema and cross-references |
| Input | Raw scenario YAML from PR content |
| Output | Validation results (errors, warnings) |
| Dependencies | Schema Service, Skill Registry (for skill validation) |

### Agent Recommender

| Aspect | Detail |
|--------|--------|
| Responsibility | Recommend Skilled Agents for scenario execution |
| Input | Scenario definition, available Skilled Agents |
| Output | Ranked list of recommended agents with scores |
| Dependencies | Metadata Service (Skilled Agent definitions), Usage Analytics |

---

## Database Schema

### Schema Version Store

| Table | Purpose |
|-------|---------|
| `schema_versions` | Scenario schema versions |
| `schema_migrations` | Migration history between versions |

**Key columns:**

```sql
CREATE TABLE schema_versions (
    api_version TEXT PRIMARY KEY,     -- 'foundry/v1'
    schema_json JSONB NOT NULL,
    published_at TIMESTAMPTZ DEFAULT NOW(),
    deprecated_at TIMESTAMPTZ,
    migration_from TEXT,
    migration_notes TEXT
);

CREATE TABLE schema_migrations (
    id UUID PRIMARY KEY,
    from_version TEXT NOT NULL,
    to_version TEXT NOT NULL,
    migration_script TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### Validation Cache

| Table | Purpose |
|-------|---------|
| `validation_cache` | Cached validation results for unchanged scenarios |

```sql
CREATE TABLE validation_cache (
    scenario_hash TEXT PRIMARY KEY,   -- SHA256 of scenario content
    api_version TEXT NOT NULL,
    is_valid BOOLEAN NOT NULL,
    errors JSONB,
    warnings JSONB,
    validated_at TIMESTAMPTZ DEFAULT NOW(),
    expires_at TIMESTAMPTZ
);

CREATE INDEX idx_validation_cache_expires ON validation_cache(expires_at);
```

### Agent Recommendation Cache

```sql
CREATE TABLE recommendation_cache (
    scenario_id TEXT NOT NULL,
    workspace_id TEXT NOT NULL,
    recommendations JSONB NOT NULL,
    computed_at TIMESTAMPTZ DEFAULT NOW(),
    expires_at TIMESTAMPTZ,
    PRIMARY KEY(scenario_id, workspace_id)
);
```

---

## Integration Details

### Workshop Validation Service Integration

| Aspect | Detail |
|--------|--------|
| Integration type | Internal REST API call |
| Direction | Workshop Validation → Scenario Management |
| Trigger | On PR with scenario file changes |

**Flow:**

```
PR opened with scenario change
    │
    ├── Workshop Validation Service receives PR check trigger
    │
    ├── Extracts changed scenario files
    │
    ├── Calls Scenario Management Validation API
    │   POST /api/v1/scenarios/validate
    │   Body: { scenario_yaml, api_version }
    │
    ├── Scenario Management validates:
    │   - Schema conformance
    │   - Skill references exist
    │   - Trigger validity
    │   - Output completeness
    │
    └── Returns validation result
        { valid: true/false, errors: [], warnings: [] }
```

### Metadata Service Integration

| Aspect | Detail |
|--------|--------|
| Integration type | Internal service calls |
| Direction | Bidirectional |

**Operations:**

| Operation | Direction | Purpose |
|-----------|-----------|---------|
| Store validated scenario | → Metadata | After Workshop Sync |
| Query Skilled Agents | ← Metadata | For recommendations |
| Query Scenario | ← Metadata | For effective resolution |

### WO Runtime Integration

| Aspect | Detail |
|--------|--------|
| Integration type | REST API |
| Direction | WO Runtime queries Scenario Management |

**Operations:**

| Operation | When |
|-----------|------|
| Get agent recommendations | Before spawning agent for task |

---

## Processing Logic

### Schema Validation

```python
def validate_scenario(scenario_yaml: str, api_version: str = None) -> ValidationResult:
    # 1. Parse YAML
    try:
        scenario = yaml.safe_load(scenario_yaml)
    except yaml.YAMLError as e:
        return ValidationResult(valid=False, errors=[f"Invalid YAML: {e}"])
    
    # 2. Determine API version
    api_version = api_version or scenario.get("apiVersion", "foundry/v1")
    
    # 3. Get schema
    schema = schema_service.get_schema(api_version)
    if not schema:
        return ValidationResult(valid=False, errors=[f"Unknown API version: {api_version}"])
    
    # 4. Validate structure
    errors = validate_against_schema(scenario, schema)
    if errors:
        return ValidationResult(valid=False, errors=errors)
    
    # 5. Validate cross-references
    ref_errors = validate_references(scenario)
    if ref_errors:
        return ValidationResult(valid=False, errors=ref_errors)
    
    # 6. Check warnings
    warnings = check_warnings(scenario)
    
    return ValidationResult(valid=True, warnings=warnings)
```

### Reference Validation

```python
def validate_references(scenario: dict) -> list[str]:
    errors = []
    
    # Validate skill references
    for task in scenario.get("spec", {}).get("tasks", []):
        if task.get("type") == "agent":
            for skill_ref in task.get("skills", []):
                if not skill_registry.skill_exists(skill_ref):
                    errors.append(f"Unknown skill reference: {skill_ref}")
    
    # Validate Skilled Agent reference
    skilled_agent_ref = scenario.get("spec", {}).get("skilled_agent", {}).get("ref")
    if skilled_agent_ref:
        workspace_id = scenario.get("metadata", {}).get("workspace")
        if not metadata_service.skilled_agent_exists(skilled_agent_ref, workspace_id):
            errors.append(f"Unknown Skilled Agent: {skilled_agent_ref}")
    
    # Validate task dependencies (no cycles)
    if has_dependency_cycle(scenario.get("spec", {}).get("tasks", [])):
        errors.append("Circular dependency detected in task dependencies")
    
    return errors
```

### Effective Scenario Resolution

```python
def get_effective_scenario(scenario_name: str, workspace_type: str, workbench_id: str) -> Scenario:
    # Resolution order: Workbench → Workshop
    workshop_id = get_workshop_id(workbench_id)
    
    # 1. Check Workbench-level scenario
    workbench_scenario = metadata_service.get_scenario(
        scope="workbench",
        scope_id=workbench_id,
        workspace=workspace_type,
        name=scenario_name
    )
    if workbench_scenario:
        return workbench_scenario
    
    # 2. Fall back to Workshop-level scenario
    workshop_scenario = metadata_service.get_scenario(
        scope="workshop",
        scope_id=workshop_id,
        workspace=workspace_type,
        name=scenario_name
    )
    if workshop_scenario:
        return workshop_scenario
    
    raise ScenarioNotFoundError(scenario_name, workspace_type)
```

### Agent Recommendation

```python
def get_recommendations(scenario_id: str, workspace_id: str) -> list[Recommendation]:
    # 1. Get scenario definition
    scenario = metadata_service.get_scenario_by_id(scenario_id)
    
    # 2. Extract required skills
    required_skills = extract_required_skills(scenario)
    
    # 3. Get available Skilled Agents for this workspace
    skilled_agents = metadata_service.get_skilled_agents(workspace_id)
    
    # 4. Score each agent
    recommendations = []
    for agent in skilled_agents:
        score, reasons = score_agent(agent, required_skills, scenario)
        if score > 0:
            recommendations.append(Recommendation(
                skilled_agent_id=agent.id,
                score=score,
                reasons=reasons
            ))
    
    # 5. Sort by score descending
    recommendations.sort(key=lambda r: r.score, reverse=True)
    
    return recommendations

def score_agent(agent, required_skills: list[str], scenario: dict) -> tuple[float, list[str]]:
    score = 0.0
    reasons = []
    
    # Skill match (high weight)
    agent_skills = set(s["name"] for s in agent.skills)
    matched_skills = set(required_skills) & agent_skills
    skill_coverage = len(matched_skills) / len(required_skills) if required_skills else 1.0
    score += skill_coverage * 0.6
    reasons.append(f"Skill coverage: {skill_coverage:.0%}")
    
    # Workspace fit (medium weight)
    if agent.workspace_type == scenario.get("metadata", {}).get("workspace"):
        score += 0.3
        reasons.append("Configured for this workspace")
    
    # Success history (low weight, optional)
    success_rate = usage_analytics.get_success_rate(agent.id, scenario.get("metadata", {}).get("name"))
    if success_rate is not None:
        score += success_rate * 0.1
        reasons.append(f"Historical success rate: {success_rate:.0%}")
    
    return score, reasons
```

---

## Error Handling

### Validation Errors

| Error | HTTP Status | Response |
|-------|-------------|----------|
| Invalid YAML syntax | 400 | `{ "error": "invalid_yaml", "details": "..." }` |
| Unknown API version | 400 | `{ "error": "unknown_api_version", "version": "..." }` |
| Schema validation failed | 422 | `{ "error": "schema_validation_failed", "errors": [...] }` |
| Unknown skill reference | 422 | `{ "error": "reference_validation_failed", "errors": [...] }` |

### Recommendation Errors

| Error | HTTP Status | Response |
|-------|-------------|----------|
| Scenario not found | 404 | `{ "error": "scenario_not_found", "id": "..." }` |
| No agents available | 200 | `{ "recommendations": [], "message": "No matching agents" }` |

### Retry Policy

| Operation | Strategy |
|-----------|----------|
| Skill Registry check | Retry 3x with 100ms backoff |
| Metadata Service query | Retry 3x with 100ms backoff |
| Schema lookup | Use cached schema if unavailable |

---

## Authorization

### Validation API

| Caller | Permission |
|--------|------------|
| Workshop Validation Service | Service account (internal) |
| Admin CLI | Foundry Admin |

### Recommendation API

| Caller | Permission |
|--------|------------|
| WO Runtime | Service account (internal) |
| Web Console | Authenticated user in workspace |

### Schema Management

| Role | Permission |
|------|------------|
| Foundry Admin | Create/update schema versions |
| Workshop Admin | Read schemas |
| Developer | Read schemas |

---

## API Specification

### Validation API

```
# Validate scenario YAML
POST /api/v1/scenarios/validate
Content-Type: application/json
Body: {
  "scenario_yaml": "apiVersion: foundry/v1\nkind: Scenario\n...",
  "api_version": "foundry/v1"  // optional, auto-detected
}
Response: {
  "valid": true,
  "errors": [],
  "warnings": ["Optional field 'guardrails' not specified"]
}

# Validate scenario file (multipart)
POST /api/v1/scenarios/validate-file
Content-Type: multipart/form-data
Body: { file: <scenario.yaml> }
Response: { "valid": true, "errors": [], "warnings": [] }
```

### Schema API

```
# Get current schema
GET /api/v1/schemas/current
Response: {
  "api_version": "foundry/v1",
  "schema": { ... JSON Schema ... },
  "published_at": "2026-05-01T00:00:00Z"
}

# Get specific schema version
GET /api/v1/schemas/{api_version}
Response: { "api_version": "foundry/v1", "schema": { ... } }

# List schema versions
GET /api/v1/schemas
Response: {
  "versions": [
    { "api_version": "foundry/v1", "published_at": "...", "deprecated": false }
  ]
}
```

### Recommendation API

```
# Get agent recommendations for scenario
GET /api/v1/scenarios/{scenario_id}/recommendations?workspace_id={id}
Response: {
  "recommendations": [
    {
      "skilled_agent_id": "sa-code-impl",
      "score": 0.95,
      "reasons": ["Skill coverage: 100%", "Configured for this workspace"]
    },
    {
      "skilled_agent_id": "sa-general-dev",
      "score": 0.72,
      "reasons": ["Skill coverage: 80%"]
    }
  ]
}

# Get recommendations by scenario name (lookup)
POST /api/v1/recommendations/lookup
Body: {
  "scenario_name": "implement-feature",
  "workspace_type": "development",
  "workbench_id": "checkout"
}
Response: { "recommendations": [...] }
```

### Effective Resolution API

```
# Get effective scenario
GET /api/v1/scenarios/effective?name={name}&workspace={type}&workbench={id}
Response: {
  "scenario": { ... full scenario object ... },
  "source": "workbench",  // or "workshop"
  "source_id": "checkout"
}
```

---

## Scalability

### Caching Strategy

| Data | Cache | TTL |
|------|-------|-----|
| Schema versions | In-memory | Indefinite (versioned) |
| Validation results | Redis | 1 hour |
| Recommendations | Redis | 5 minutes |
| Effective scenarios | Redis | 5 minutes |

### Cache Invalidation

| Event | Invalidation |
|-------|--------------|
| Workshop Sync completes | Clear affected scenarios and recommendations |
| Schema version published | Clear validation cache |
| Skilled Agent updated | Clear recommendation cache |

### Performance Targets

| Operation | Target |
|-----------|--------|
| Validation (single scenario) | < 200ms |
| Recommendation lookup | < 100ms |
| Effective resolution | < 50ms |

---

## Observability

### Metrics

| Metric | Type | Description |
|--------|------|-------------|
| `scenario_validations_total` | Counter | Validations by result (valid/invalid) |
| `scenario_validation_duration_ms` | Histogram | Validation latency |
| `scenario_validation_errors_total` | Counter | Errors by type |
| `scenario_recommendations_total` | Counter | Recommendation requests |
| `scenario_recommendation_duration_ms` | Histogram | Recommendation latency |
| `scenario_cache_hits_total` | Counter | Cache hits by type |
| `scenario_cache_misses_total` | Counter | Cache misses by type |

### Logging

Structured JSON logs with:

| Field | Description |
|-------|-------------|
| `operation` | `validate`, `recommend`, `resolve` |
| `scenario_name` | Scenario being processed |
| `workspace_type` | Workspace context |
| `result` | `valid`, `invalid`, `error` |
| `duration_ms` | Operation duration |
| `cache_hit` | Whether result came from cache |

### Tracing

OpenTelemetry spans for:
- Schema lookup
- YAML parsing
- Schema validation
- Reference validation
- Agent scoring
- Cache operations

---

## External Dependencies

| Dependency | Integration | Failure Mode |
|------------|-------------|--------------|
| Skill Registry | REST API | Retry with backoff, fail validation if unavailable |
| Metadata Service | Internal service | Retry with backoff, use cache |
| Redis | Caching | Bypass cache, query directly |
| PostgreSQL | Schema storage | Fail if unavailable |

---

## Open Implementation Questions

- Schema versioning policy (breaking vs non-breaking changes)
- Validation strictness levels (strict, warn, permissive)
- Recommendation algorithm tuning parameters
- Cache warming strategy on service startup
- Schema migration tooling for existing scenarios
- A/B testing framework for recommendation algorithms

## Read Next

- [README.md](README.md) — Scenario Management overview
- [scenario-schema.md](scenario-schema.md) — Full YAML schema specification
- [scenario-execution-journey.md](scenario-execution-journey.md) — End-to-end flow
- [../services/workshop-validation.md](../services/workshop-validation.md) — How validation is triggered
- [../services/metadata-service.md](../services/metadata-service.md) — Where scenarios are stored
