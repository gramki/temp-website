# CAF Record Content Schema Registry

> **Status**: 🟡 Draft  
> **Last Updated**: 2026-01-07  
> **Related**: [CAF README](./README.md) | [Typed Content Convention](./README.md#typed-content-convention)

---

## Overview

The **Record Content Schema Registry** is the CAF service that provides **discovery, retrieval, and validation of content schemas** used in CAF records. It serves as the authoritative source for all `olympus://schemas/...` references.

### Key Principles

| Principle | Description |
|-----------|-------------|
| **Registration via CRD** | Schemas are registered through Kubernetes CRDs, not API calls |
| **Discovery via API** | CAF exposes read-only APIs to discover and retrieve schemas |
| **Versioned** | Schemas are versioned with semantic versioning |
| **Namespace-organized** | Schemas are organized by namespace/domain |
| **Validation-ready** | Schemas can be used for runtime validation |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        KUBERNETES CONTROL PLANE                          │
│                                                                          │
│   ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐   │
│   │  ContentSchema  │     │  ContentSchema  │     │  ContentSchema  │   │
│   │  CRD Instance   │     │  CRD Instance   │     │  CRD Instance   │   │
│   │ (decision-rec)  │     │ (fraud-context) │     │ (custom-type)   │   │
│   └────────┬────────┘     └────────┬────────┘     └────────┬────────┘   │
│            │                       │                       │            │
│            └───────────────────────┼───────────────────────┘            │
│                                    │                                     │
│                                    ▼                                     │
│                     ┌──────────────────────────────┐                     │
│                     │   CAF Schema Registry        │                     │
│                     │        Controller            │                     │
│                     │   (watches CRD changes)      │                     │
│                     └──────────────┬───────────────┘                     │
│                                    │                                     │
└────────────────────────────────────┼─────────────────────────────────────┘
                                     │
                                     ▼
                      ┌──────────────────────────────┐
                      │   Schema Registry API        │
                      │    (Discovery Service)       │
                      │                              │
                      │  GET /schemas                │
                      │  GET /schemas/{uri}          │
                      │  POST /schemas/validate      │
                      └──────────────────────────────┘
```

---

## Semantic Explainers

Every content schema includes a **semantic explainer** section that enables the [Explanation Service](./explanation-service.md) to generate human-readable explanations from record data.

### Explainer Components

| Component | Description |
|-----------|-------------|
| **Templates** | Parameterized narrative templates for different audiences |
| **Field Semantics** | Human-readable meaning of each field |
| **Significance Rules** | What values are notable or concerning |
| **Relationship Descriptions** | How this content relates to other records |
| **Counterfactual Hints** | What alternative scenarios to explain |

### Explainer in Schema

```yaml
semantic_explainer:
  # Narrative templates by audience
  templates:
    executive:
      summary: "A {{decision.action}} was made with {{decision.confidence | percent}} confidence."
      detail: "The decision to {{decision.action}} was based on {{rationale.factors | count}} factors..."
    technical:
      summary: "Decision: {{decision.action}} (confidence: {{decision.confidence}})"
      detail: "Factors: {{rationale.factors | json}}"
    audit:
      summary: "Record {{record_id}}: {{decision.action}} at {{timestamp | datetime}}"
      detail: "Full decision trace with {{evidence_refs | count}} evidence items..."
    customer:
      summary: "We reviewed your case and {{decision.action | customer_friendly}}."
      detail: null  # Not applicable for this record type
  
  # Field-level semantics
  field_semantics:
    decision.action:
      label: "Decision"
      description: "The action taken by the agent"
      display_format: "action_verb"
    decision.confidence:
      label: "Confidence Level"
      description: "How certain the agent was about this decision"
      display_format: "percentage"
      significance:
        low: { below: 0.5, label: "Low confidence", style: "warning" }
        high: { above: 0.9, label: "High confidence", style: "success" }
    rationale.summary:
      label: "Reasoning"
      description: "Why this decision was made"
      display_format: "prose"
  
  # Significance rules (what to highlight)
  significance_rules:
    - condition: "decision.confidence < 0.5"
      level: "warning"
      message: "This decision had low confidence and may warrant review"
    - condition: "alternatives | count > 3"
      level: "info"
      message: "Multiple alternatives were considered"
    - condition: "override_of != null"
      level: "attention"
      message: "This decision overrides a previous decision"
  
  # Relationship context
  relationships:
    evidence_bundle:
      description: "Supporting evidence for this decision"
      traversal: "evidence_refs[]"
      explanation: "This decision was supported by {{evidence_refs | count}} pieces of evidence"
    case:
      description: "Parent case"
      traversal: "case_id"
      explanation: "Part of case {{case_id}}"
  
  # Counterfactual hints
  counterfactuals:
    - scenario: "What if confidence was higher?"
      condition: "decision.confidence < 0.8"
      explanation: "If confidence exceeded 80%, this might have been auto-approved"
    - scenario: "What if this factor was absent?"
      for_each: "rationale.factors"
      explanation: "Without {{factor.name}}, the decision might have been different"
```

---

## Schema URI Format

All schemas use the `olympus://` URI scheme:

```
olympus://schemas/{namespace}/{domain}/{type}/v{major}

Examples:
  olympus://schemas/caf/episodic/decision-record/v1
  olympus://schemas/caf/semantic/hypothesis/v2
  olympus://schemas/hub/fraud/fraud-investigation-context/v1
  olympus://schemas/tenant/acme/custom-evidence/v1
```

### URI Components

| Component | Description | Examples |
|-----------|-------------|----------|
| `namespace` | Top-level namespace | `caf`, `hub`, `tenant`, `vendor` |
| `domain` | Domain/area | `episodic`, `semantic`, `fraud`, `payments` |
| `type` | Schema type name | `decision-record`, `fraud-context` |
| `version` | Major version | `v1`, `v2` |

---

## Discovery API

### List Schemas

```yaml
GET /v1/schemas
  ?namespace={namespace}           # Optional filter
  &domain={domain}                 # Optional filter
  &type={type}                     # Optional filter
  &status={status}                 # Optional: active | deprecated | draft
  &include_deprecated={bool}       # Default: false

Response: 200 OK
{
  "schemas": [
    {
      "uri": "olympus://schemas/caf/episodic/decision-record/v1",
      "namespace": "caf",
      "domain": "episodic",
      "type": "decision-record",
      "version": {
        "major": 1,
        "minor": 3,
        "patch": 0,
        "full": "1.3.0"
      },
      "status": "active",
      "display_name": "Decision Record",
      "description": "Schema for cognitive decision records",
      "mime_type": "application/vnd.olympus.caf.decision-record.v1+json",
      "created_at": "2025-09-01T00:00:00Z",
      "updated_at": "2026-01-05T10:00:00Z",
      "_links": {
        "self": "/v1/schemas/caf/episodic/decision-record/v1",
        "schema": "/v1/schemas/caf/episodic/decision-record/v1/schema",
        "versions": "/v1/schemas/caf/episodic/decision-record/versions"
      }
    },
    ...
  ],
  "pagination": {
    "total": 45,
    "offset": 0,
    "limit": 50
  }
}
```

### Get Schema Metadata

```yaml
GET /v1/schemas/{namespace}/{domain}/{type}/v{major}

Response: 200 OK
{
  "uri": "olympus://schemas/caf/episodic/decision-record/v1",
  "namespace": "caf",
  "domain": "episodic",
  "type": "decision-record",
  
  "version": {
    "major": 1,
    "minor": 3,
    "patch": 0,
    "full": "1.3.0"
  },
  
  "status": "active",
  "display_name": "Decision Record",
  "description": "Schema for capturing agent decisions with rationale, alternatives, and confidence",
  
  "mime_type": "application/vnd.olympus.caf.decision-record.v1+json",
  "supported_formats": ["json", "yaml"],
  
  "metadata": {
    "author": "CAF Team",
    "owner": "platform-team",
    "tags": ["decision", "cognitive", "audit"],
    "memory_class": "episodic",
    "created_at": "2025-09-01T00:00:00Z",
    "updated_at": "2026-01-05T10:00:00Z"
  },
  
  "compatibility": {
    "backwards_compatible_with": ["v1.2.0", "v1.1.0", "v1.0.0"],
    "breaking_changes_from": null
  },
  
  "usage": {
    "record_types_using": ["decision_record"],
    "stores_supporting": ["fraud-ops.enterprise-memory.primary", "..."]
  },
  
  "_links": {
    "self": "/v1/schemas/caf/episodic/decision-record/v1",
    "schema": "/v1/schemas/caf/episodic/decision-record/v1/schema",
    "versions": "/v1/schemas/caf/episodic/decision-record/versions",
    "documentation": "/v1/schemas/caf/episodic/decision-record/v1/docs"
  }
}
```

### Get Schema Definition

```yaml
GET /v1/schemas/{namespace}/{domain}/{type}/v{major}/schema
  ?format={format}                 # Optional: jsonschema (default) | openapi | typescript

Response: 200 OK
Content-Type: application/schema+json

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "olympus://schemas/caf/episodic/decision-record/v1",
  "title": "Decision Record",
  "description": "Schema for capturing agent decisions with rationale",
  "type": "object",
  "required": ["record_id", "case_id", "decision", "rationale", "timestamp"],
  "properties": {
    "record_id": {
      "type": "string",
      "format": "uuid",
      "description": "Unique identifier for this record"
    },
    "case_id": {
      "type": "string",
      "format": "uuid",
      "description": "Case this decision belongs to"
    },
    "decision": {
      "type": "object",
      "properties": {
        "action": { "type": "string" },
        "confidence": { "type": "number", "minimum": 0, "maximum": 1 }
      },
      "required": ["action"]
    },
    "rationale": {
      "type": "object",
      "properties": {
        "summary": { "type": "string" },
        "factors": { "type": "array", "items": { "$ref": "#/$defs/factor" } }
      },
      "required": ["summary"]
    },
    "timestamp": {
      "type": "string",
      "format": "date-time"
    },
    "hub_metadata": {
      "$ref": "olympus://schemas/caf/common/hub-metadata/v1"
    }
  },
  "$defs": {
    "factor": {
      "type": "object",
      "properties": {
        "factor": { "type": "string" },
        "weight": { "type": "number" },
        "value": { "type": "string" }
      }
    }
  }
}
```

### List Schema Versions

```yaml
GET /v1/schemas/{namespace}/{domain}/{type}/versions

Response: 200 OK
{
  "type": "decision-record",
  "namespace": "caf",
  "domain": "episodic",
  
  "versions": [
    {
      "major": 1,
      "full": "1.3.0",
      "status": "active",
      "released_at": "2026-01-05T10:00:00Z",
      "uri": "olympus://schemas/caf/episodic/decision-record/v1",
      "_links": {
        "self": "/v1/schemas/caf/episodic/decision-record/v1"
      }
    },
    {
      "major": 1,
      "full": "1.2.0",
      "status": "superseded",
      "released_at": "2025-11-01T10:00:00Z",
      "uri": "olympus://schemas/caf/episodic/decision-record/v1",
      "_links": {
        "self": "/v1/schemas/caf/episodic/decision-record/v1?version=1.2.0"
      }
    }
  ],
  
  "latest": {
    "major": 1,
    "full": "1.3.0"
  }
}
```

### Validate Content Against Schema

```yaml
POST /v1/schemas/validate

Request:
{
  "schema_uri": "olympus://schemas/caf/episodic/decision-record/v1",
  "content": {
    "record_id": "abc-123",
    "case_id": "case-456",
    "decision": {
      "action": "approve_refund",
      "confidence": 0.85
    },
    "rationale": {
      "summary": "Evidence supports customer claim"
    },
    "timestamp": "2026-01-07T14:30:00Z"
  }
}

Response: 200 OK
{
  "valid": true,
  "schema_uri": "olympus://schemas/caf/episodic/decision-record/v1",
  "schema_version": "1.3.0",
  "errors": [],
  "warnings": [
    {
      "path": "$.hub_metadata",
      "message": "Recommended field 'hub_metadata' is missing"
    }
  ]
}

# If invalid:
Response: 200 OK
{
  "valid": false,
  "schema_uri": "olympus://schemas/caf/episodic/decision-record/v1",
  "schema_version": "1.3.0",
  "errors": [
    {
      "path": "$.rationale.summary",
      "message": "Required property 'summary' is missing",
      "keyword": "required"
    }
  ],
  "warnings": []
}
```

### Resolve Schema by MIME Type

```yaml
GET /v1/schemas/by-mime/{mime_type}

Example:
GET /v1/schemas/by-mime/application%2Fvnd.olympus.caf.decision-record.v1%2Bjson

Response: 200 OK
{
  "mime_type": "application/vnd.olympus.caf.decision-record.v1+json",
  "schema_uri": "olympus://schemas/caf/episodic/decision-record/v1",
  "format": "json",
  "_links": {
    "schema": "/v1/schemas/caf/episodic/decision-record/v1"
  }
}
```

### Get Semantic Explainer

```yaml
GET /v1/schemas/{namespace}/{domain}/{type}/v{major}/explainer

Response: 200 OK
{
  "schema_uri": "olympus://schemas/caf/episodic/decision-record/v1",
  
  "templates": {
    "executive": {
      "summary": "A {{decision.action}} decision was made with {{decision.confidence | percent}} confidence.",
      "detail": "Based on {{rationale.factors | count}} factors, the agent decided to {{decision.action}}."
    },
    "technical": {
      "summary": "Decision: {{decision.action}} (conf: {{decision.confidence}})",
      "detail": "Factors: {{rationale.factors | json}}"
    },
    "audit": {
      "summary": "{{record_id}}: {{decision.action}} @ {{timestamp}}",
      "detail": "Decision record with {{evidence_refs | count}} evidence refs"
    },
    "customer": {
      "summary": "We reviewed your case and decided to {{decision.action | customer_friendly}}.",
      "detail": null
    }
  },
  
  "field_semantics": {
    "decision.action": {
      "label": "Decision",
      "description": "The action taken",
      "display_format": "action_verb"
    },
    "decision.confidence": {
      "label": "Confidence",
      "description": "Certainty level (0-100%)",
      "display_format": "percentage",
      "significance": {
        "low": { "below": 0.5, "label": "Low", "style": "warning" },
        "high": { "above": 0.9, "label": "High", "style": "success" }
      }
    },
    "rationale.summary": {
      "label": "Reasoning",
      "description": "Why this decision was made",
      "display_format": "prose"
    }
  },
  
  "significance_rules": [
    {
      "condition": "decision.confidence < 0.5",
      "level": "warning",
      "message": "Low confidence decision"
    },
    {
      "condition": "alternatives | count > 3",
      "level": "info",
      "message": "Multiple alternatives considered"
    }
  ],
  
  "relationships": {
    "evidence": {
      "traversal": "evidence_refs[]",
      "explanation": "Supported by {{count}} evidence items"
    },
    "case": {
      "traversal": "case_id",
      "explanation": "Part of case {{case_id}}"
    }
  },
  
  "counterfactuals": [
    {
      "scenario": "higher_confidence",
      "condition": "decision.confidence < 0.8",
      "explanation": "With >80% confidence, this could auto-approve"
    }
  ],
  
  "_links": {
    "schema": "/v1/schemas/caf/episodic/decision-record/v1/schema",
    "explain": "/v1/explainer/render"
  }
}
```

### Render Explanation (Convenience API)

This endpoint is a shortcut that combines schema lookup + explainer rendering:

```yaml
POST /v1/schemas/explain

Request:
{
  "schema_uri": "olympus://schemas/caf/episodic/decision-record/v1",
  "audience": "executive",
  "content": {
    "record_id": "dec-12345",
    "decision": {
      "action": "approve_refund",
      "confidence": 0.87
    },
    "rationale": {
      "summary": "Customer claim supported by evidence",
      "factors": [
        { "factor": "purchase_verified", "weight": 0.4 },
        { "factor": "no_prior_disputes", "weight": 0.3 },
        { "factor": "amount_reasonable", "weight": 0.3 }
      ]
    },
    "timestamp": "2026-01-07T14:30:00Z"
  },
  "options": {
    "include_significance": true,
    "include_counterfactuals": false
  }
}

Response: 200 OK
{
  "schema_uri": "olympus://schemas/caf/episodic/decision-record/v1",
  "audience": "executive",
  
  "explanation": {
    "summary": "A approve_refund decision was made with 87% confidence.",
    "detail": "Based on 3 factors, the agent decided to approve_refund.",
    
    "field_explanations": [
      {
        "field": "decision.action",
        "label": "Decision",
        "value": "approve_refund",
        "formatted": "Approve Refund"
      },
      {
        "field": "decision.confidence",
        "label": "Confidence",
        "value": 0.87,
        "formatted": "87%",
        "significance": {
          "level": "normal",
          "message": null
        }
      }
    ],
    
    "significance_alerts": [],
    
    "related_records": [
      {
        "relationship": "case",
        "explanation": "Part of case dec-12345"
      }
    ]
  }
}
```

---

## CRD-Based Registration

Schemas are registered via Kubernetes CRDs:

```yaml
apiVersion: olympus.hub/v1
kind: ContentSchema
metadata:
  name: caf-episodic-decision-record-v1
  namespace: olympus-system
  labels:
    caf.olympus.io/namespace: caf
    caf.olympus.io/domain: episodic
    caf.olympus.io/type: decision-record
    caf.olympus.io/major-version: "1"
spec:
  uri: "olympus://schemas/caf/episodic/decision-record/v1"
  
  identity:
    namespace: caf
    domain: episodic
    type: decision-record
    
  version:
    major: 1
    minor: 3
    patch: 0
    
  status: active    # active | deprecated | draft
  
  display_name: "Decision Record"
  description: "Schema for capturing agent decisions with rationale"
  
  mime_type: "application/vnd.olympus.caf.decision-record.v1+json"
  supported_formats:
    - json
    - yaml
    
  metadata:
    author: "CAF Team"
    owner: "platform-team"
    tags:
      - decision
      - cognitive
      - audit
    memory_class: episodic
    
  schema:
    # Inline JSON Schema or reference to ConfigMap
    inline: |
      {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "olympus://schemas/caf/episodic/decision-record/v1",
        "type": "object",
        ...
      }
    # Or:
    # configMapRef:
    #   name: decision-record-schema
    #   key: schema.json
  
  # Semantic explainer for Explanation Service
  semantic_explainer:
    templates:
      executive:
        summary: "A {{decision.action}} decision was made with {{decision.confidence | percent}} confidence."
        detail: "Based on {{rationale.factors | count}} factors, the agent decided to {{decision.action}}."
      technical:
        summary: "Decision: {{decision.action}} (conf: {{decision.confidence}})"
        detail: "Factors: {{rationale.factors | json}}"
      audit:
        summary: "{{record_id}}: {{decision.action}} @ {{timestamp}}"
        detail: "Decision record with {{evidence_refs | count}} evidence refs"
      customer:
        summary: "We reviewed your case and decided to {{decision.action | customer_friendly}}."
        
    field_semantics:
      decision.action:
        label: "Decision"
        description: "The action taken"
        display_format: "action_verb"
      decision.confidence:
        label: "Confidence"
        description: "Certainty level (0-100%)"
        display_format: "percentage"
        significance:
          low: { below: 0.5, label: "Low", style: "warning" }
          high: { above: 0.9, label: "High", style: "success" }
          
    significance_rules:
      - condition: "decision.confidence < 0.5"
        level: "warning"
        message: "Low confidence decision"
        
    relationships:
      evidence:
        traversal: "evidence_refs[]"
        explanation: "Supported by {{count}} evidence items"
        
    counterfactuals:
      - scenario: "higher_confidence"
        condition: "decision.confidence < 0.8"
        explanation: "With >80% confidence, this could auto-approve"
    
  compatibility:
    backwards_compatible_with:
      - "1.2.0"
      - "1.1.0"
      - "1.0.0"
      
status:
  registered: true
  validated: true
  explainer_validated: true
  last_validated: "2026-01-05T10:00:00Z"
```

---

## Schema Namespaces

| Namespace | Description | Governance |
|-----------|-------------|------------|
| `caf` | Core CAF schemas (decision, evidence, etc.) | CAF team |
| `hub` | Hub subsystem schemas | Hub team |
| `seer` | Seer subsystem schemas | Seer team |
| `tenant` | Tenant-specific custom schemas | Tenant admin |
| `vendor` | Third-party integration schemas | Vendor + platform |

---

## Common Schemas

The registry includes common reusable schemas:

```yaml
olympus://schemas/caf/common/hub-metadata/v1      # Standard hub_metadata section
olympus://schemas/caf/common/typed-content/v1     # content + content_type pattern
olympus://schemas/caf/common/evidence-ref/v1      # Reference to evidence
olympus://schemas/caf/common/actor/v1             # User or agent actor
olympus://schemas/caf/common/outcome/v1           # Outcome structure
```

These can be referenced via `$ref` in other schemas.

---

## Schema Lifecycle

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│    Draft    │───►│   Active    │───►│ Deprecated  │───►│   Retired   │
│  (testing)  │    │  (in use)   │    │ (phase out) │    │  (removed)  │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
                          │
                          │ New minor/patch version
                          ▼
                   ┌─────────────┐
                   │   Active    │
                   │ (1.x+1 or   │
                   │  1.x.y+1)   │
                   └─────────────┘
```

### Versioning Rules

| Change Type | Version Bump | Compatibility |
|-------------|--------------|---------------|
| New optional field | Patch | Backwards compatible |
| New required field with default | Minor | Backwards compatible |
| New required field (no default) | Major | Breaking change |
| Remove field | Major | Breaking change |
| Change field type | Major | Breaking change |

---

## Access Control

| Operation | Required Permission |
|-----------|---------------------|
| List schemas | `caf:schema:read` |
| Get schema | `caf:schema:read` |
| Validate content | `caf:schema:read` |
| Register schema (CRD) | Kubernetes RBAC |

---

## TODO

| Item | Description | Priority |
|------|-------------|----------|
| Define schema evolution policies | Rules for backwards compatibility | P1 |
| Define tenant schema isolation | How tenant schemas are namespaced | P1 |
| Define schema caching strategy | How clients cache schemas | P2 |
| Define schema documentation format | Standardized docs for schemas | P2 |
| Define schema testing/validation tooling | CI/CD for schema changes | P2 |

---

## Related Documents

- [CAF README](./README.md) — Cognitive Audit Fabric overview
- [Typed Content Convention](./README.md#typed-content-convention) — How content types are specified
- [Memory Store Catalog](./memory-store-catalog.md) — Store discovery

