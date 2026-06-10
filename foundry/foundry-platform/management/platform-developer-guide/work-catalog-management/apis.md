# Work Catalog Management APIs

This document specifies the REST APIs provided by the Work Catalog Management subsystem.

## Base URL

```
/api/v1/work-catalog
```

## Authentication

All endpoints require authentication via service account or user token. See [Authorization](#authorization) for permission requirements.

---

## Validation APIs

### Validate Artifact

Validates an OI Workflow or Scenario YAML against the schema and cross-references.

```http
POST /api/v1/work-catalog/validate
Content-Type: application/json

{
  "type": "oi-workflow" | "scenario",
  "yaml": "<yaml-content>",
  "context": {
    "foundry_id": "acme",
    "workshop_id": "ecommerce",      // Required for scenario validation
    "workbench_id": "checkout"       // Optional, for workbench-level validation
  }
}
```

**Response (Success):**

```json
{
  "valid": true,
  "warnings": [
    "Optional field 'guardrails' not specified - using workspace defaults"
  ],
  "errors": []
}
```

**Response (Failure):**

```json
{
  "valid": false,
  "warnings": [],
  "errors": [
    {
      "code": "SCHEMA_VALIDATION_FAILED",
      "message": "Missing required field: metadata.scope",
      "path": "$.metadata.scope",
      "line": 5
    },
    {
      "code": "REFERENCE_NOT_FOUND",
      "message": "Referenced scenario 'implement-feature' not found in effective catalog",
      "path": "$.spec.stages[2].handlers[0].then[0].params.scenario"
    }
  ]
}
```

### Validate File (Multipart)

```http
POST /api/v1/work-catalog/validate-file
Content-Type: multipart/form-data

file: <artifact.yaml>
type: oi-workflow | scenario
context: {"foundry_id": "acme", ...}
```

---

## Resolution APIs

### Get Effective Catalog

Returns the complete effective Work Catalog for a given scope.

```http
GET /api/v1/work-catalog/effective
  ?foundry_id=acme
  &workshop_id=ecommerce
  &workbench_id=checkout
  &user_id=alice              // Optional
  &include_sources=true       // Optional, default: false
  &filter_workspace=development  // Optional, filter by workspace
  &filter_scope=workspace-ingress // Optional, filter by scope
```

**Response:**

```json
{
  "oi_workflows": [
    {
      "name": "product-intent-workflow",
      "orchestration_item": "product-intent",
      "spec": { "stages": [...] },
      "source": {
        "level": "foundry",
        "id": "acme",
        "repository": "acme/foundry-acme",
        "path": "work-catalog/build/product-intent/workflow.yaml",
        "commit_sha": "abc123"
      }
    }
  ],
  "scenarios": [
    {
      "name": "implement-feature",
      "workspace": "development",
      "scope": "workspace-ingress",
      "spec": { "tasks": [...] },
      "source": {
        "level": "user",
        "id": "alice",
        "repository": "acme/user-work-catalog-alice",
        "path": "work-catalog/build/product-intent/development/scenarios/implement-feature.yaml",
        "commit_sha": "def456"
      }
    }
  ],
  "resolved_at": "2026-05-28T10:30:00Z",
  "cache_hit": true
}
```

### Resolve Single Artifact

Resolves a specific OI Workflow or Scenario by name.

```http
GET /api/v1/work-catalog/resolve
  ?type=scenario
  &name=implement-feature
  &foundry_id=acme
  &workshop_id=ecommerce
  &workbench_id=checkout
  &user_id=alice              // Optional
```

**Response:**

```json
{
  "artifact": {
    "name": "implement-feature",
    "kind": "Scenario",
    "metadata": {
      "workspace": "development",
      "scope": "workspace-ingress"
    },
    "spec": { ... }
  },
  "source": {
    "level": "user",
    "id": "alice",
    "repository": "acme/user-work-catalog-alice",
    "path": "work-catalog/build/product-intent/development/scenarios/implement-feature.yaml",
    "commit_sha": "def456"
  },
  "resolved_at": "2026-05-28T10:30:00Z"
}
```

**Response (Not Found):**

```json
{
  "error": "ARTIFACT_NOT_FOUND",
  "message": "Scenario 'implement-feature' not found in effective catalog",
  "searched_levels": ["user", "workbench", "workshop", "foundry", "platform"]
}
```

### Get Catalog Sources

Returns the source information for all artifacts in the effective catalog.

```http
GET /api/v1/work-catalog/sources
  ?foundry_id=acme
  &workshop_id=ecommerce
  &workbench_id=checkout
  &user_id=alice
```

**Response:**

```json
{
  "sources": {
    "oi-workflow:product-intent-workflow": {
      "level": "foundry",
      "id": "acme"
    },
    "scenario:development:implement-feature": {
      "level": "user",
      "id": "alice"
    },
    "scenario:development:run-tests": {
      "level": "workshop",
      "id": "ecommerce"
    },
    "scenario:qa:execute-test-suite": {
      "level": "platform",
      "id": "default"
    }
  }
}
```

---

## Schema APIs

### Get Current Schema

```http
GET /api/v1/work-catalog/schemas/current
  ?type=oi-workflow | scenario   // Optional, returns both if omitted
```

**Response:**

```json
{
  "schemas": {
    "oi-workflow": {
      "api_version": "foundry/v1",
      "kind": "OIWorkflow",
      "schema": { ... },  // JSON Schema
      "published_at": "2026-05-01T00:00:00Z"
    },
    "scenario": {
      "api_version": "foundry/v1",
      "kind": "Scenario",
      "schema": { ... },
      "published_at": "2026-05-01T00:00:00Z"
    }
  }
}
```

### Get Specific Schema Version

```http
GET /api/v1/work-catalog/schemas/{api_version}
  ?type=scenario
```

**Response:**

```json
{
  "api_version": "foundry/v1",
  "kind": "Scenario",
  "schema": { ... },
  "published_at": "2026-05-01T00:00:00Z",
  "deprecated": false
}
```

### List Schema Versions

```http
GET /api/v1/work-catalog/schemas
  ?type=scenario
```

**Response:**

```json
{
  "versions": [
    {
      "api_version": "foundry/v1",
      "kind": "Scenario",
      "published_at": "2026-05-01T00:00:00Z",
      "deprecated": false
    }
  ]
}
```

---

## Agent Recommendation APIs

### Get Recommendations for Scenario

```http
GET /api/v1/scenarios/{scenario_id}/recommendations
  ?workspace_id=checkout-dev
  &limit=5                    // Optional, default: 10
```

**Response:**

```json
{
  "recommendations": [
    {
      "trained_agent_id": "sa-full-stack-dev",
      "score": 0.95,
      "reasons": [
        "Skill coverage: 100%",
        "Configured for development workspace",
        "Historical success rate: 92%"
      ],
      "skills_matched": ["code-implementation", "test-writing", "pr-authoring"],
      "skills_missing": []
    },
    {
      "trained_agent_id": "sa-backend-dev",
      "score": 0.72,
      "reasons": [
        "Skill coverage: 67%",
        "Configured for development workspace"
      ],
      "skills_matched": ["code-implementation", "test-writing"],
      "skills_missing": ["pr-authoring"]
    }
  ],
  "scenario": {
    "name": "implement-feature",
    "required_skills": ["code-implementation", "test-writing", "pr-authoring"]
  }
}
```

### Get Recommendations by Scenario Name

```http
POST /api/v1/recommendations/lookup
Content-Type: application/json

{
  "scenario_name": "implement-feature",
  "workspace_type": "development",
  "workbench_id": "checkout",
  "user_id": "alice"          // Optional
}
```

**Response:** Same as above.

---

## User Catalog APIs

### Activate User Catalog for Session

```http
POST /api/v1/sessions/{session_id}/user-catalog
Content-Type: application/json

{
  "action": "activate"
}
```

**Response:**

```json
{
  "active": true,
  "session_id": "session-123",
  "user_id": "alice",
  "expires_at": "2026-05-28T18:00:00Z"
}
```

### Deactivate User Catalog for Session

```http
POST /api/v1/sessions/{session_id}/user-catalog
Content-Type: application/json

{
  "action": "deactivate"
}
```

### Get User Catalog Status

```http
GET /api/v1/sessions/{session_id}/user-catalog
```

**Response:**

```json
{
  "active": true,
  "source": "session",        // "session" | "profile"
  "expires_at": "2026-05-28T18:00:00Z"
}
```

### Update User Profile Setting

```http
PUT /api/v1/users/{user_id}/settings/user-catalog
Content-Type: application/json

{
  "active": true
}
```

---

## Effective Scenario API (Legacy Compatibility)

For backward compatibility with existing WO Runtime integration:

```http
GET /api/v1/scenarios/effective
  ?name=implement-feature
  &workspace=development
  &workbench=checkout
  &user_id=alice
```

**Response:**

```json
{
  "scenario": {
    "name": "implement-feature",
    "spec": { ... },
    "trained_agent": { "ref": "sa-full-stack-dev", "fallback": "auto" }
  },
  "source": "user",
  "source_id": "alice"
}
```

---

## Error Responses

### Standard Error Format

```json
{
  "error": "<ERROR_CODE>",
  "message": "<Human-readable message>",
  "details": { ... }         // Optional additional context
}
```

### Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `INVALID_YAML` | 400 | YAML syntax error |
| `UNKNOWN_API_VERSION` | 400 | Unrecognized apiVersion |
| `SCHEMA_VALIDATION_FAILED` | 422 | Schema validation errors |
| `REFERENCE_NOT_FOUND` | 422 | Referenced artifact not found |
| `ARTIFACT_NOT_FOUND` | 404 | Requested artifact not found |
| `SESSION_NOT_FOUND` | 404 | Session not found |
| `UNAUTHORIZED` | 401 | Missing or invalid authentication |
| `FORBIDDEN` | 403 | Insufficient permissions |
| `INTERNAL_ERROR` | 500 | Internal server error |

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

| Role | Permission |
|------|------------|
| Foundry Admin | Create/update schema versions |
| Workshop Admin | Read schemas |
| Developer | Read schemas |

### User Catalog

| Role | Permission |
|------|------------|
| User | Activate/deactivate own catalog |
| Workbench Manager | View user catalog status for team members |

---

## Rate Limits

| Endpoint | Limit |
|----------|-------|
| Validation | 100 req/min per service |
| Resolution | 1000 req/min per service |
| Schema | 100 req/min per user |
| Recommendations | 500 req/min per service |

---

## Read Next

- [README.md](README.md) — Work Catalog Management overview
- [resolution-algorithm.md](resolution-algorithm.md) — Resolution algorithm details
- [validation-rules.md](validation-rules.md) — Validation specification
- [events-and-caching.md](events-and-caching.md) — Caching strategy
