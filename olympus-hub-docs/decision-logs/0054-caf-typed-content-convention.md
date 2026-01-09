# ADR-0054: CAF Typed Content Convention

## Status

**Accepted**

## Date

2026-01-07

## Context

CAF records contain structured data (objects, arrays) that may:
- Evolve over time (need versioning)
- Come from different sources (need schema identification)
- Be consumed by different systems (need format negotiation)
- Require validation (need schema location)

Standard field types (`object`, `array`) don't convey:
- What schema the data conforms to
- What version of the schema
- How to interpret the structure
- Where to find validation rules

## Decision

### Typed Content Pattern

For fields containing structured data, CAF uses a **typed content** pattern:

```yaml
factors: array                    # The actual content
factors_content_type:
  mime: string                    # "application/vnd.olympus.caf.decision-factor.v1+json"
  format: string                  # json (default) | yaml
  schema: string                  # olympus.caf.decision-factor
  schema_version: string          # "1.0.0"
  schema_uri: string              # olympus://schemas/caf/decision-factor/v1.0.0
```

### MIME Type Format (RFC 6838 Compliant)

CAF uses **vendor MIME types** for schema+version encoding:

```
application/vnd.olympus.<namespace>.<type>.v<major>+<format>
```

| Component | Description | Example |
|-----------|-------------|---------|
| `vnd.olympus` | Vendor prefix | Required |
| `<namespace>` | Subsystem namespace | `caf`, `seer`, `hub` |
| `<type>` | Schema type name | `decision-factors` |
| `v<major>` | Major version | `v1`, `v2` |
| `+<format>` | Serialization suffix | `+json`, `+yaml` |

**Examples:**
- `application/vnd.olympus.caf.decision-factors.v1+json`
- `application/vnd.olympus.seer.context-frame.v1+json`
- `application/vnd.zeta.core.account.v3+json`

### Why Both MIME and Structured Form?

Standard MIME types have limitations:

| Limitation | Structured Solution |
|------------|---------------------|
| Only major version in suffix | `schema_version: "1.2.3"` (full semver) |
| No schema resolution | `schema_uri: "olympus://schemas/..."` |
| String parsing required | Direct field access |
| Format coupled to type | Separate `format` field |

### Human-Readable Serialization Requirement

**CAF records MUST use human-readable serialization formats:**

| Format | Status | Use Case |
|--------|--------|----------|
| **JSON** | ✅ **Default** | All CAF records unless specified |
| **YAML** | ✅ Allowed | Configuration-heavy content |
| **XML** | ⚠️ Legacy only | Integration with legacy systems |
| **Binary (CBOR, Protobuf)** | ❌ **Not allowed** | Use only in non-CAF contexts |

**Rationale:** CAF exists for audit, explanation, and learning. Binary formats optimize for machine efficiency at the cost of human legibility—the opposite of CAF's mission.

### When to Use Typed Content

| Field Type | Use Typed Content? |
|------------|-------------------|
| Simple scalars (string, number) | No |
| Enums | No |
| Domain objects | **Yes** |
| Extensible arrays | **Yes** |
| External data | **Yes** |
| Model I/O | **Yes** |

## Alternatives Considered

### Alternative 1: Untyped Content
Store all content as plain JSON without type metadata.

- **Pros**: Simple, no extra fields
- **Cons**: No schema validation, no versioning, interpretation unclear

### Alternative 2: MIME Only (No Structured Form)
Use only MIME string for type identification.

- **Pros**: Standard approach, single field
- **Cons**: Cannot express full semver, no schema URI, parsing required

### Alternative 3: JSON Schema $schema Reference
Use JSON Schema's $schema property.

- **Pros**: Standard JSON Schema approach
- **Cons**: Requires JSON Schema tooling, verbose, doesn't support other formats

## Consequences

### Positive
- **Version Tracking**: Full semver support for all content
- **Schema Resolution**: URI-based schema lookup
- **Format Flexibility**: JSON and YAML supported
- **Interoperability**: MIME types work with standard HTTP tooling
- **Human Legibility**: Binary formats prohibited

### Negative
- **More Fields**: Each content field has companion *_content_type
- **Schema Registry**: Need schema repository (olympus://schemas/...)

### Neutral
- Default to JSON when format not specified
- MIME string is optional if structured form is sufficient

## Related Decisions

- [ADR-0052: CAF Record Type Taxonomy](./0052-caf-record-type-taxonomy.md)
- [ADR-0053: CAF Record ID and Traversal Conventions](./0053-caf-record-id-traversal.md)
- [ADR-0029: CAF as Control Plane](./0029-caf-control-plane.md)

