# Knowledge APIs

This document specifies the REST APIs for querying resolved knowledge from the Metadata Service.

## Overview

Knowledge APIs serve resolved Domain, Practices, and Ontology content to platform consumers (primarily WO Runtime and agents). The APIs apply the knowledge hierarchy and workspace scope resolution automatically.

## Base URL

```
https://api.foundry.{domain}/v1/knowledge
```

## Authentication

All endpoints require a valid Foundry access token:

```
Authorization: Bearer {access_token}
```

## Endpoints

### List Resolved Knowledge

List all knowledge files available for a specific context, with resolution applied.

```
GET /workbenches/{workbench_id}/workspaces/{workspace_type}/{knowledge_type}
```

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `workbench_id` | string | Workbench identifier (e.g., `wb-checkout`) |
| `workspace_type` | string | Workspace type (e.g., `development`, `qa`) |
| `knowledge_type` | string | One of: `domain`, `practices`, `ontology` |

**Query Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `include_source` | boolean | `true` | Include source level and location |
| `recursive` | boolean | `true` | Include files in subdirectories |

**Response:**

```json
{
  "workbench_id": "wb-checkout",
  "workspace_type": "development",
  "knowledge_type": "domain",
  "files": [
    {
      "path": "glossary.md",
      "source": {
        "level": "workshop",
        "scope": "universal",
        "location": "workshop-payments/domain/universal/glossary.md"
      }
    },
    {
      "path": "api-conventions.md",
      "source": {
        "level": "workbench",
        "scope": "development",
        "location": "checkout/domain/development/api-conventions.md"
      }
    },
    {
      "path": "business-rules/payment-validation.md",
      "source": {
        "level": "foundry",
        "scope": "universal",
        "location": "foundry-zeta/domain/universal/business-rules/payment-validation.md"
      }
    }
  ]
}
```

**Example:**

```bash
curl -H "Authorization: Bearer $TOKEN" \
  "https://api.foundry.example.com/v1/knowledge/workbenches/wb-checkout/workspaces/development/domain"
```

---

### Get Knowledge File

Retrieve the content of a specific knowledge file, with resolution applied.

```
GET /workbenches/{workbench_id}/workspaces/{workspace_type}/{knowledge_type}/{path}
```

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `workbench_id` | string | Workbench identifier |
| `workspace_type` | string | Workspace type |
| `knowledge_type` | string | One of: `domain`, `practices`, `ontology` |
| `path` | string | File path within the knowledge type (URL-encoded) |

**Response Headers:**

| Header | Description |
|--------|-------------|
| `X-Knowledge-Source-Level` | Resolution source: `foundry`, `workshop`, or `workbench` |
| `X-Knowledge-Source-Scope` | Resolution scope: `universal` or the workspace type |
| `X-Knowledge-Source-Location` | Full path to the source file |
| `Content-Type` | `text/markdown` or `application/yaml` |

**Response Body:**

The raw content of the knowledge file.

**Example:**

```bash
curl -H "Authorization: Bearer $TOKEN" \
  "https://api.foundry.example.com/v1/knowledge/workbenches/wb-checkout/workspaces/development/practices/coding-standards.md"
```

**Response:**

```markdown
# Coding Standards

## General Principles

1. Readability over cleverness
2. Single responsibility
...
```

---

### Get Ontology

Retrieve the product ontology for a Workbench.

```
GET /workbenches/{workbench_id}/ontology
```

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `workbench_id` | string | Workbench identifier |

**Query Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `format` | string | `json` | Response format: `json` or `yaml` |
| `include` | string[] | all | Sections to include: `capabilities`, `features`, `modules`, `maturity` |

**Response:**

```json
{
  "workbench_id": "wb-checkout",
  "product": {
    "name": "Checkout Service",
    "code": "CHKOUT-001"
  },
  "capabilities": [
    {
      "id": "cap-payment-processing",
      "name": "Payment Processing",
      "description": "Process customer payments",
      "maturity": "ga",
      "features": [
        {
          "id": "feat-card-payments",
          "name": "Card Payments",
          "maturity": "ga"
        },
        {
          "id": "feat-digital-wallets",
          "name": "Digital Wallets",
          "maturity": "beta"
        }
      ]
    }
  ],
  "modules": [
    {
      "id": "mod-checkout-api",
      "name": "Checkout API",
      "type": "service",
      "capabilities": ["cap-payment-processing"]
    }
  ]
}
```

---

### List Knowledge at Level

List knowledge available at a specific hierarchy level (for administrative purposes).

```
GET /{level}/{level_id}/{knowledge_type}
```

**Path Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `level` | string | One of: `foundries`, `workshops`, `workbenches` |
| `level_id` | string | ID at that level |
| `knowledge_type` | string | One of: `domain`, `practices` |

**Query Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `scope` | string | all | Filter by scope: `universal`, `{workspace-type}`, or omit for all |

**Response:**

```json
{
  "level": "workshop",
  "level_id": "workshop-payments",
  "knowledge_type": "practices",
  "scope_filter": null,
  "files": [
    {
      "path": "coding-standards.md",
      "scope": "development"
    },
    {
      "path": "review-policy.md",
      "scope": "universal"
    }
  ]
}
```

---

### Resolve Knowledge File

Determine which source would be used for a knowledge file without fetching content.

```
GET /resolve
```

**Query Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `workbench_id` | string | Yes | Workbench identifier |
| `workspace_type` | string | Yes | Workspace type |
| `knowledge_type` | string | Yes | `domain` or `practices` |
| `path` | string | Yes | File path |

**Response:**

```json
{
  "resolved": true,
  "source": {
    "level": "workshop",
    "scope": "development",
    "location": "workshop-payments/practices/development/coding-standards.md"
  },
  "resolution_chain": [
    {
      "level": "workbench",
      "scope": "development",
      "exists": false
    },
    {
      "level": "workbench",
      "scope": "universal",
      "exists": false
    },
    {
      "level": "workshop",
      "scope": "development",
      "exists": true,
      "location": "workshop-payments/practices/development/coding-standards.md"
    }
  ]
}
```

If not found:

```json
{
  "resolved": false,
  "source": null,
  "resolution_chain": [
    { "level": "workbench", "scope": "development", "exists": false },
    { "level": "workbench", "scope": "universal", "exists": false },
    { "level": "workshop", "scope": "development", "exists": false },
    { "level": "workshop", "scope": "universal", "exists": false },
    { "level": "foundry", "scope": "development", "exists": false },
    { "level": "foundry", "scope": "universal", "exists": false }
  ]
}
```

---

### Bulk Resolve

Resolve multiple knowledge files in a single request.

```
POST /resolve/bulk
```

**Request Body:**

```json
{
  "workbench_id": "wb-checkout",
  "workspace_type": "development",
  "files": [
    { "knowledge_type": "domain", "path": "glossary.md" },
    { "knowledge_type": "practices", "path": "coding-standards.md" },
    { "knowledge_type": "practices", "path": "pr-conventions.md" }
  ]
}
```

**Response:**

```json
{
  "results": [
    {
      "knowledge_type": "domain",
      "path": "glossary.md",
      "resolved": true,
      "source": {
        "level": "workshop",
        "scope": "universal",
        "location": "workshop-payments/domain/universal/glossary.md"
      }
    },
    {
      "knowledge_type": "practices",
      "path": "coding-standards.md",
      "resolved": true,
      "source": {
        "level": "workbench",
        "scope": "development",
        "location": "checkout/practices/development/coding-standards.md"
      }
    },
    {
      "knowledge_type": "practices",
      "path": "pr-conventions.md",
      "resolved": false,
      "source": null
    }
  ]
}
```

---

## Error Responses

### Standard Error Format

```json
{
  "error": {
    "code": "KNOWLEDGE_NOT_FOUND",
    "message": "Knowledge file not found",
    "details": {
      "path": "practices/nonexistent.md",
      "workbench_id": "wb-checkout",
      "workspace_type": "development"
    }
  }
}
```

### Error Codes

| Code | HTTP Status | Description |
|------|-------------|-------------|
| `WORKBENCH_NOT_FOUND` | 404 | Workbench does not exist |
| `INVALID_WORKSPACE_TYPE` | 400 | Invalid workspace type |
| `INVALID_KNOWLEDGE_TYPE` | 400 | Invalid knowledge type |
| `KNOWLEDGE_NOT_FOUND` | 404 | Requested knowledge file not found at any level |
| `ONTOLOGY_NOT_FOUND` | 404 | Workbench has no ontology defined |
| `UNAUTHORIZED` | 401 | Invalid or missing access token |
| `FORBIDDEN` | 403 | User lacks permission to access this knowledge |

---

## Usage by WO Runtime

WO Runtime uses these APIs to assemble agent context:

```python
# Pseudocode for context assembly

def assemble_context(workbench_id, workspace_type, scenario):
    context = {}
    
    # Get all domain knowledge
    domain_files = api.list_knowledge(
        workbench_id, workspace_type, "domain"
    )
    context["domain"] = {
        f["path"]: api.get_knowledge(workbench_id, workspace_type, "domain", f["path"])
        for f in domain_files["files"]
    }
    
    # Get relevant practices
    practices_files = api.list_knowledge(
        workbench_id, workspace_type, "practices"
    )
    context["practices"] = {
        f["path"]: api.get_knowledge(workbench_id, workspace_type, "practices", f["path"])
        for f in practices_files["files"]
    }
    
    # Get ontology if needed
    if scenario.needs_ontology:
        context["ontology"] = api.get_ontology(workbench_id)
    
    return context
```

---

## Caching

### Client-Side Caching

Responses include standard HTTP caching headers:

| Header | Value |
|--------|-------|
| `Cache-Control` | `private, max-age=300` |
| `ETag` | Hash of content |

Clients should use conditional requests:

```
If-None-Match: "abc123"
```

### Server-Side Caching

Metadata Service caches resolved knowledge:
- Cache key: `(workbench_id, workspace_type, knowledge_type, path)`
- Invalidation: On Workshop Sync after Git push

---

## Rate Limits

| Endpoint | Limit |
|----------|-------|
| List knowledge | 100 requests/minute |
| Get file | 500 requests/minute |
| Bulk resolve | 50 requests/minute |

Rate limit headers:
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1622548800
```

---

## OpenAPI Specification

The full OpenAPI spec is available at:
```
GET /openapi.yaml
```

## Read Next

- [knowledge-hierarchy.md](knowledge-hierarchy.md) — Resolution rules
- [README.md](README.md) — Knowledge Management overview
- [../services/metadata-service.md](../services/metadata-service.md) — Metadata Service details
