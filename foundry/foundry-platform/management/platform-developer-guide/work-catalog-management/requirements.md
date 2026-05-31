# Work Catalog Management Requirements

This document specifies detailed implementation requirements for the Work Catalog Management subsystem within the Management module.

## ACE alignment

| ACE concept | How this module realizes it |
|-------------|---------------------------|
| **Scenario** | Schema Service defines and validates Scenario YAML; Resolution Engine computes effective Scenarios |
| **Track** | OI Workflows are Track-specific; schema includes `orchestration-item` field for Track binding |
| **Workspace** | Scenarios are scoped to Workspace types; scope attribute (`workspace-ingress`/`workspace-internal`) controls invocability |
| **Agent** | Agent Recommender matches Scenarios to suitable Skilled Agents |

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           Work Catalog Management                                    │
│                                                                                      │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐                 │
│  │  Schema Service │    │ Validation Rules│    │     Agent       │                 │
│  │                 │    │       API       │    │  Recommender    │                 │
│  │  • OI Workflow  │    │  • Schema rules │    │  • Match skills │                 │
│  │  • Scenario     │    │  • Ref checks   │    │  • Score agents │                 │
│  │  • Versioning   │    │  • OI→Scenario  │    │                 │                 │
│  └────────┬────────┘    └────────┬────────┘    └────────┬────────┘                 │
│           │                      │                      │                           │
│           └──────────────────────┴──────────────────────┘                           │
│                                  │                                                  │
│           ┌──────────────────────┴──────────────────────┐                          │
│           │            Resolution Engine                 │                          │
│           │  Platform → Foundry → Workshop → Workbench  │                          │
│           │                    → User (if active)        │                          │
│           └─────────────────────────────────────────────┘                          │
│                                  │                                                  │
│                           ┌──────┴──────┐                                           │
│                           │   Cache     │                                           │
│                           │  (Redis)    │                                           │
│                           └─────────────┘                                           │
└────────────────────────────────────────────────────────────────────────────────────┘
         │                         │                         │
         ▲                         ▼                         ▼
┌─────────────────┐    ┌─────────────────────┐    ┌─────────────────────┐
│  Validation     │    │    Metadata         │    │    Orchestrator     │
│    module       │────│    Service          │    │    + WO Runtime     │
│  (calls WCM)    │    │   (storage)         │    │   (consumers)       │
└─────────────────┘    └─────────────────────┘    └─────────────────────┘
```

## Core Components

### Schema Service

**WCM-FR-0001:** The Schema Service SHALL manage schema versions for OI Workflows and Scenarios.

**WCM-FR-0002:** The Schema Service SHALL provide schemas for validation by the Validation module.

| Aspect | Detail |
|--------|--------|
| Responsibility | Manage schema versions for OI Workflows and Scenarios, provide schemas for validation |
| Input | Schema version requests, schema updates |
| Output | Schema definitions, schema metadata |
| Dependencies | PostgreSQL for schema storage |

### Validation Rules API

**WCM-FR-0003:** The Validation Rules API SHALL validate OI Workflow and Scenario content against schemas.

**WCM-FR-0004:** The Validation Rules API SHALL validate skill references against the Skill Registry.

**WCM-FR-0005:** The Validation Rules API SHALL validate Scenario references in OI Workflows against the effective catalog.

| Aspect | Detail |
|--------|--------|
| Responsibility | Provide validation rules and API for OI Workflow and Scenario content; called by the external Validation module |
| Input | Raw YAML content from Validation module |
| Output | Validation results (errors, warnings) |
| Dependencies | Schema Service, Skill Registry (for skill validation), Metadata Service (for reference resolution) |

### Resolution Engine

**WCM-FR-0006:** The Resolution Engine SHALL compute effective Work Catalog by walking the hierarchy: Platform > Foundry > Workshop > Workbench > User (if active).

**WCM-FR-0007:** The Resolution Engine SHALL track the source of each artifact in the effective catalog.

**WCM-FR-0008:** The Resolution Engine SHALL include User catalog only when user catalog activation is enabled.

| Aspect | Detail |
|--------|--------|
| Responsibility | Compute effective Work Catalog by walking hierarchy |
| Input | Resolution context (foundry, workshop, workbench, user, activation status) |
| Output | Effective catalog with source tracking |
| Dependencies | Metadata Service (catalog storage), Session Service (user activation) |

### Agent Recommender

**WCM-FR-0009:** The Agent Recommender SHALL recommend Skilled Agents for Scenario execution based on skill matching.

**WCM-FR-0010:** The Agent Recommender SHALL return a ranked list of agents with scores, skills matched, and skills missing.

| Aspect | Detail |
|--------|--------|
| Responsibility | Recommend Skilled Agents for Scenario execution |
| Input | Scenario definition, available Skilled Agents |
| Output | Ranked list of recommended agents with scores |
| Dependencies | Metadata Service (Skilled Agent definitions), Usage Analytics |

---

## Database Schema

### Schema Version Store

| Table | Purpose |
|-------|---------|
| `schema_versions` | OI Workflow and Scenario schema versions |
| `schema_migrations` | Migration history between versions |

**Key columns:**

```sql
CREATE TABLE schema_versions (
    api_version TEXT NOT NULL,           -- 'foundry/v1'
    kind TEXT NOT NULL,                  -- 'OIWorkflow' or 'Scenario'
    schema_json JSONB NOT NULL,
    published_at TIMESTAMPTZ DEFAULT NOW(),
    deprecated_at TIMESTAMPTZ,
    migration_from TEXT,
    migration_notes TEXT,
    PRIMARY KEY (api_version, kind)
);

CREATE TABLE schema_migrations (
    id UUID PRIMARY KEY,
    kind TEXT NOT NULL,                  -- 'OIWorkflow' or 'Scenario'
    from_version TEXT NOT NULL,
    to_version TEXT NOT NULL,
    migration_script TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### Work Catalog Registry

| Table | Purpose |
|-------|---------|
| `oi_workflows` | OI Workflow definitions at each hierarchy level |
| `scenarios` | Scenario definitions at each hierarchy level |
| `catalog_sources` | Source tracking for artifacts |

```sql
CREATE TABLE oi_workflows (
    id UUID PRIMARY KEY,
    name TEXT NOT NULL,
    orchestration_item TEXT NOT NULL,    -- 'product-intent', etc.
    api_version TEXT NOT NULL,
    spec JSONB NOT NULL,
    
    -- Hierarchy location
    catalog_level TEXT NOT NULL,         -- 'platform', 'foundry', 'workshop', 'workbench', 'user'
    foundry_id TEXT,
    workshop_id TEXT,
    workbench_id TEXT,
    user_id TEXT,
    
    -- Source tracking
    source_repository TEXT,
    source_path TEXT,
    source_commit_sha TEXT,
    
    synced_at TIMESTAMPTZ DEFAULT NOW(),
    
    UNIQUE (name, catalog_level, foundry_id, workshop_id, workbench_id, user_id)
);

CREATE INDEX idx_oi_workflows_lookup ON oi_workflows(
    name, catalog_level, foundry_id, workshop_id, workbench_id, user_id
);

CREATE TABLE scenarios (
    id UUID PRIMARY KEY,
    name TEXT NOT NULL,
    workspace_type TEXT NOT NULL,        -- 'development', 'qa', etc.
    scope TEXT NOT NULL,                 -- 'workspace-ingress', 'workspace-internal'
    api_version TEXT NOT NULL,
    spec JSONB NOT NULL,
    
    -- Hierarchy location
    catalog_level TEXT NOT NULL,
    foundry_id TEXT,
    workshop_id TEXT,
    workbench_id TEXT,
    user_id TEXT,
    
    -- Source tracking
    source_repository TEXT,
    source_path TEXT,
    source_commit_sha TEXT,
    
    synced_at TIMESTAMPTZ DEFAULT NOW(),
    
    UNIQUE (name, workspace_type, catalog_level, foundry_id, workshop_id, workbench_id, user_id)
);

CREATE INDEX idx_scenarios_lookup ON scenarios(
    name, workspace_type, catalog_level, foundry_id, workshop_id, workbench_id, user_id
);

CREATE INDEX idx_scenarios_by_scope ON scenarios(scope, workspace_type);
```

### Validation Cache

```sql
CREATE TABLE validation_cache (
    content_hash TEXT NOT NULL,          -- SHA256 of content
    kind TEXT NOT NULL,                  -- 'OIWorkflow' or 'Scenario'
    api_version TEXT NOT NULL,
    is_valid BOOLEAN NOT NULL,
    errors JSONB,
    warnings JSONB,
    validated_at TIMESTAMPTZ DEFAULT NOW(),
    expires_at TIMESTAMPTZ,
    PRIMARY KEY (content_hash, kind)
);

CREATE INDEX idx_validation_cache_expires ON validation_cache(expires_at);
```

### User Catalog Activation

```sql
CREATE TABLE user_catalog_settings (
    user_id TEXT NOT NULL,
    foundry_id TEXT NOT NULL,
    active BOOLEAN DEFAULT FALSE,
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    PRIMARY KEY (user_id, foundry_id)
);

CREATE TABLE session_catalog_overrides (
    session_id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    foundry_id TEXT NOT NULL,
    active BOOLEAN NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    expires_at TIMESTAMPTZ
);

CREATE INDEX idx_session_overrides_user ON session_catalog_overrides(user_id, foundry_id);
```

### Agent Recommendation Cache

```sql
CREATE TABLE recommendation_cache (
    scenario_id UUID NOT NULL,
    workspace_id TEXT NOT NULL,
    recommendations JSONB NOT NULL,
    computed_at TIMESTAMPTZ DEFAULT NOW(),
    expires_at TIMESTAMPTZ,
    PRIMARY KEY (scenario_id, workspace_id)
);

CREATE INDEX idx_recommendation_cache_expires ON recommendation_cache(expires_at);
```

---

## Integration Details

### Validation module integration

| Aspect | Detail |
|--------|--------|
| Integration type | Internal REST API call |
| Direction | Validation module → Work Catalog Management |
| Trigger | On PR with OI Workflow or Scenario file changes |

**Flow:**

```
PR opened with work catalog change
    │
    ├── Validation module receives PR check trigger
    │
    ├── Extracts changed OI Workflow and Scenario files
    │
    ├── Calls Work Catalog Management Validation API
    │   POST /api/v1/work-catalog/validate
    │   Body: { type, yaml, context }
    │
    ├── Work Catalog Management validates:
    │   - Schema conformance (OI Workflow or Scenario)
    │   - Skill references exist (Scenarios)
    │   - Scenario references exist (OI Workflows)
    │   - Scope constraints (workspace-ingress vs internal)
    │   - Cross-artifact linkage
    │
    └── Returns validation result
        { valid: true/false, errors: [], warnings: [] }
        (reported as foundry-validation GitHub check)
```

### Orchestrator Integration

| Aspect | Detail |
|--------|--------|
| Integration type | REST API |
| Direction | Orchestrator queries Work Catalog Management |

**Operations:**

| Operation | When |
|-----------|------|
| Get effective OI Workflow | Before processing an Orchestration Item |
| Resolve Scenario for create-work-order | When executing workflow action |

### WO Runtime Integration

| Aspect | Detail |
|--------|--------|
| Integration type | REST API |
| Direction | WO Runtime queries Work Catalog Management |

**Operations:**

| Operation | When |
|-----------|------|
| Get effective Scenario | Before executing a Work Order |
| Get agent recommendations | Before spawning agent for task |
| Check user catalog activation | Before including user catalog in resolution |

### Metadata Service Integration

| Aspect | Detail |
|--------|--------|
| Integration type | Internal service calls |
| Direction | Bidirectional |

**Operations:**

| Operation | Direction | Purpose |
|-----------|-----------|---------|
| Store OI Workflow | → Metadata | After sync |
| Store Scenario | → Metadata | After sync |
| Query Skilled Agents | ← Metadata | For recommendations |
| Query effective catalog | ← Metadata | For resolution |

---

## Processing Logic

### Schema Validation

**WCM-FR-0011:** Schema validation SHALL parse YAML and reject invalid YAML with a clear error.

**WCM-FR-0012:** Schema validation SHALL verify the `kind` field matches the expected artifact type.

**WCM-FR-0013:** Schema validation SHALL reject unknown API versions.

**WCM-FR-0014:** Schema validation SHALL validate artifact structure against the schema before checking cross-references.

```python
def validate_artifact(
    artifact_type: str,      # "oi-workflow" or "scenario"
    yaml_content: str,
    context: ValidationContext
) -> ValidationResult:
    # 1. Parse YAML
    try:
        artifact = yaml.safe_load(yaml_content)
    except yaml.YAMLError as e:
        return ValidationResult(valid=False, errors=[f"Invalid YAML: {e}"])
    
    # 2. Determine API version and kind
    api_version = artifact.get("apiVersion", "foundry/v1")
    kind = artifact.get("kind")
    
    expected_kind = "OIWorkflow" if artifact_type == "oi-workflow" else "Scenario"
    if kind != expected_kind:
        return ValidationResult(valid=False, errors=[f"Expected kind: {expected_kind}, got: {kind}"])
    
    # 3. Get schema
    schema = schema_service.get_schema(api_version, kind)
    if not schema:
        return ValidationResult(valid=False, errors=[f"Unknown API version: {api_version}"])
    
    # 4. Validate structure
    errors = validate_against_schema(artifact, schema)
    if errors:
        return ValidationResult(valid=False, errors=errors)
    
    # 5. Validate cross-references
    if artifact_type == "oi-workflow":
        ref_errors = validate_workflow_references(artifact, context)
    else:
        ref_errors = validate_scenario_references(artifact, context)
    
    if ref_errors:
        return ValidationResult(valid=False, errors=ref_errors)
    
    # 6. Check warnings
    warnings = check_warnings(artifact, artifact_type)
    
    return ValidationResult(valid=True, warnings=warnings)
```

### OI Workflow Reference Validation

**WCM-FR-0015:** OI Workflow validation SHALL verify all referenced Scenarios exist in the effective catalog.

**WCM-FR-0016:** OI Workflow validation SHALL reject references to Scenarios with `workspace-internal` scope (Orchestrator cannot invoke them).

```python
def validate_workflow_references(workflow: dict, context: ValidationContext) -> list[str]:
    errors = []
    
    # Get effective catalog at context scope
    effective_catalog = get_effective_catalog(context)
    
    for stage in workflow.get("spec", {}).get("stages", []):
        for handler in stage.get("handlers", []):
            for action in handler.get("then", []):
                if action.get("action") == "create-work-order":
                    scenario_name = action.get("params", {}).get("scenario")
                    workspace = action.get("params", {}).get("workspace")
                    
                    # Check scenario exists
                    scenario = effective_catalog.get_scenario(scenario_name, workspace)
                    if not scenario:
                        errors.append(f"Scenario not found: {scenario_name}")
                        continue
                    
                    # Check scenario scope is workspace-ingress
                    if scenario.metadata.scope != "workspace-ingress":
                        errors.append(
                            f"Scenario '{scenario_name}' is workspace-internal, "
                            "cannot be invoked by Orchestrator"
                        )
    
    return errors
```

### Scenario Reference Validation

**WCM-FR-0017:** Scenario validation SHALL verify all skill references exist in the Skill Registry.

**WCM-FR-0018:** Scenario validation SHALL verify referenced Skilled Agents exist for the specified workspace type.

**WCM-FR-0019:** Scenario validation SHALL reject Orchestrator triggers for `workspace-internal` scope Scenarios.

**WCM-FR-0020:** Scenario validation SHALL reject task triggers for `workspace-ingress` scope Scenarios.

**WCM-FR-0021:** Scenario validation SHALL detect and reject circular dependencies in task dependencies.

```python
def validate_scenario_references(scenario: dict, context: ValidationContext) -> list[str]:
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
        workspace_type = scenario.get("metadata", {}).get("workspace")
        if not metadata_service.skilled_agent_exists(skilled_agent_ref, workspace_type):
            errors.append(f"Unknown Skilled Agent: {skilled_agent_ref}")
    
    # Validate scope constraints
    scope = scenario.get("metadata", {}).get("scope")
    triggers = scenario.get("spec", {}).get("triggers", [])
    
    for trigger in triggers:
        if isinstance(trigger, dict) and "orchestrator" in trigger:
            if scope == "workspace-internal":
                errors.append("Orchestrator trigger not allowed for workspace-internal scope")
        if isinstance(trigger, dict) and "task" in trigger:
            if scope == "workspace-ingress":
                errors.append("Task trigger not allowed for workspace-ingress scope")
    
    # Validate task dependencies (no cycles)
    if has_dependency_cycle(scenario.get("spec", {}).get("tasks", [])):
        errors.append("Circular dependency detected in task dependencies")
    
    return errors
```

### Effective Catalog Resolution

```python
def get_effective_catalog(context: ResolutionContext) -> EffectiveCatalog:
    """Compute effective Work Catalog at given scope."""
    
    # Start with platform defaults
    catalog = load_platform_defaults()
    
    # Layer Foundry catalog
    if context.foundry_id:
        foundry_catalog = load_foundry_catalog(context.foundry_id)
        catalog = merge_catalogs(catalog, foundry_catalog, "foundry")
    
    # Layer Workshop catalog
    if context.workshop_id:
        workshop_catalog = load_workshop_catalog(context.workshop_id)
        catalog = merge_catalogs(catalog, workshop_catalog, "workshop")
    
    # Layer Workbench catalog
    if context.workbench_id:
        workbench_catalog = load_workbench_catalog(context.workbench_id)
        catalog = merge_catalogs(catalog, workbench_catalog, "workbench")
    
    # Layer User catalog if active
    if context.user_id and is_user_catalog_active(context):
        user_catalog = load_user_catalog(context.user_id, context.foundry_id)
        catalog = merge_catalogs(catalog, user_catalog, "user")
    
    return catalog


**WCM-FR-0022:** User catalog activation SHALL check session override first, then fall back to user profile setting.

def is_user_catalog_active(context: ResolutionContext) -> bool:
    """Check if user catalog should be included in resolution."""
    
    # Check session override first
    session_override = get_session_catalog_override(context.session_id)
    if session_override is not None:
        return session_override
    
    # Fall back to user profile setting
    return get_user_catalog_setting(context.user_id, context.foundry_id)
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
                reasons=reasons,
                skills_matched=list(set(required_skills) & set(agent.skills)),
                skills_missing=list(set(required_skills) - set(agent.skills))
            ))
    
    # 5. Sort by score descending
    recommendations.sort(key=lambda r: r.score, reverse=True)
    
    return recommendations
```

---

## Error Handling

### Validation Errors

| Error | HTTP Status | Response |
|-------|-------------|----------|
| Invalid YAML syntax | 400 | `{ "error": "INVALID_YAML", "details": "..." }` |
| Unknown API version | 400 | `{ "error": "UNKNOWN_API_VERSION", "version": "..." }` |
| Schema validation failed | 422 | `{ "error": "SCHEMA_VALIDATION_FAILED", "errors": [...] }` |
| Reference validation failed | 422 | `{ "error": "REFERENCE_VALIDATION_FAILED", "errors": [...] }` |

### Resolution Errors

| Error | HTTP Status | Response |
|-------|-------------|----------|
| Artifact not found | 404 | `{ "error": "ARTIFACT_NOT_FOUND", "name": "...", "type": "..." }` |
| Invalid scope | 400 | `{ "error": "INVALID_SCOPE", "details": "..." }` |

### Retry Policy

**WCM-NFR-0001:** Skill Registry checks SHALL retry up to 3 times with 100ms backoff.

**WCM-NFR-0002:** Metadata Service queries SHALL retry up to 3 times with 100ms backoff.

**WCM-NFR-0003:** Schema lookup SHALL use cached schema if the service is unavailable.

**WCM-NFR-0004:** Cache operations SHALL skip cache on failure and query directly.

| Operation | Strategy |
|-----------|----------|
| Skill Registry check | Retry 3x with 100ms backoff |
| Metadata Service query | Retry 3x with 100ms backoff |
| Schema lookup | Use cached schema if unavailable |
| Cache operations | Skip cache on failure, query directly |

---

## Authorization

### Validation API

| Caller | Permission |
|--------|------------|
| Validation module | Service account (internal) |
| Admin CLI | Foundry Admin |

### Resolution API

| Caller | Permission |
|--------|------------|
| Orchestrator | Service account (internal) |
| WO Runtime | Service account (internal) |
| Web Console | Authenticated user in workspace |
| IDE Extension | Authenticated user in workspace |

### Schema Management

**WCM-FR-0023:** Foundry Admins SHALL be able to create and update schema versions.

**WCM-FR-0024:** Workshop Admins and Developers SHALL have read-only access to schemas.

| Role | Permission |
|------|------------|
| Foundry Admin | Create/update schema versions |
| Workshop Admin | Read schemas |
| Developer | Read schemas |

### User Catalog Management

**WCM-FR-0025:** Users SHALL be able to activate/deactivate and sync their own catalog.

**WCM-FR-0026:** Workbench Managers SHALL be able to view user catalog status for team members.

| Role | Permission |
|------|------------|
| User | Activate/deactivate own catalog, sync own catalog |
| Workbench Manager | View user catalog status for team members |

---

## Scalability

### Caching Strategy

| Data | Cache | TTL |
|------|-------|-----|
| Schema versions | In-memory | Indefinite (versioned) |
| Validation results | Redis | 1 hour |
| Effective catalog | Redis | 5 minutes |
| Recommendations | Redis | 5 minutes |

### Cache Invalidation

| Event | Invalidation |
|-------|--------------|
| Platform upgrade | All caches |
| Foundry catalog sync | Affected foundry and children |
| Workshop catalog sync | Affected workshop and children |
| Workbench catalog sync | Affected workbench |
| User catalog sync | Affected user's sessions |
| User catalog activation change | Affected user's sessions |
| Schema version published | Validation cache |

### Performance Targets

**WCM-NFR-0005:** Validation of a single artifact SHALL complete in < 200ms.

**WCM-NFR-0006:** Resolution of effective catalog SHALL complete in < 100ms.

**WCM-NFR-0007:** Resolution of a single artifact SHALL complete in < 50ms.

**WCM-NFR-0008:** Recommendation lookup SHALL complete in < 100ms.

| Operation | Target |
|-----------|--------|
| Validation (single artifact) | < 200ms |
| Resolution (effective catalog) | < 100ms |
| Resolution (single artifact) | < 50ms |
| Recommendation lookup | < 100ms |

---

## Observability

### Metrics

| Metric | Type | Description |
|--------|------|-------------|
| `work_catalog_validations_total` | Counter | Validations by type and result |
| `work_catalog_validation_duration_ms` | Histogram | Validation latency |
| `work_catalog_validation_errors_total` | Counter | Errors by rule ID |
| `work_catalog_resolutions_total` | Counter | Resolution requests by scope |
| `work_catalog_resolution_duration_ms` | Histogram | Resolution latency |
| `work_catalog_recommendations_total` | Counter | Recommendation requests |
| `work_catalog_cache_hits_total` | Counter | Cache hits by type |
| `work_catalog_cache_misses_total` | Counter | Cache misses by type |
| `work_catalog_user_activations_total` | Counter | User catalog activations |

### Logging

Structured JSON logs with:

| Field | Description |
|-------|-------------|
| `operation` | `validate`, `resolve`, `recommend`, `activate` |
| `artifact_type` | `oi-workflow`, `scenario` |
| `artifact_name` | Name of artifact being processed |
| `scope` | Resolution scope |
| `result` | `valid`, `invalid`, `found`, `not_found`, `error` |
| `duration_ms` | Operation duration |
| `cache_hit` | Whether result came from cache |
| `user_catalog_active` | Whether user catalog was included |

### Tracing

OpenTelemetry spans for:
- Schema lookup
- YAML parsing
- Schema validation
- Reference validation (OI→Scenario, Skill)
- Hierarchy resolution (each level)
- Agent scoring
- Cache operations

---

## External Dependencies

| Dependency | Integration | Failure Mode |
|------------|-------------|--------------|
| Skill Registry | REST API | Retry with backoff, fail validation if unavailable |
| Metadata Service | Internal service | Retry with backoff, use cache |
| Redis | Caching | Bypass cache, query directly |
| PostgreSQL | Schema/registry storage | Fail if unavailable |
| Atropos | Events | Queue events locally, retry |

---

## Open Implementation Questions

- Schema versioning policy (breaking vs non-breaking changes)
- Validation strictness levels (strict, warn, permissive)
- Recommendation algorithm tuning parameters
- Cache warming strategy on service startup
- Schema migration tooling for existing artifacts
- User catalog isolation (prevent cross-user interference)
- Quota/limits for user catalogs
- A/B testing framework for recommendations

## Read Next

- [README.md](README.md) — Work Catalog Management overview
- [oi-workflow-schema.md](oi-workflow-schema.md) — OI Workflow schema
- [scenario-schema.md](scenario-schema.md) — Scenario schema
- [resolution-algorithm.md](resolution-algorithm.md) — Resolution algorithm
- [validation-rules.md](validation-rules.md) — Validation specification
- [apis.md](apis.md) — API specification
- [sync-mechanism.md](sync-mechanism.md) — Sync mechanism
- [events-and-caching.md](events-and-caching.md) — Events and caching
- [scenario-execution-journey.md](scenario-execution-journey.md) — End-to-end flow
