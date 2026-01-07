# Cognitive Audit Fabric (CAF)

> **Status:** 🔴 Stub — Placeholder for expansion

The Cognitive Audit Fabric (CAF) is the **Enterprise Memory Control Plane**—the connecting tissue that governs how memory is captured, linked, explained, and audited. CAF provides catalogs, policies, and services but does **not** store the memory itself.

---

## Overview

From the conceptual foundation:

> *"CAF emerges as the connecting tissue: It does not replace knowledge systems. It does not store raw agent memory. It governs how memory is captured, linked, explained, and audited. CAF makes enterprise memory legible and defensible."*

---

## CAF is a Control Plane, Not Storage

| CAF Provides | CAF Does NOT Provide |
|--------------|---------------------|
| **Catalog** of decision records | Storage for decision records |
| **Catalog** of evidence bundles | Storage for evidence bundles |
| **Explanation Service** | Raw data storage |
| Memory capture **policies** | Memory storage itself |
| Linking and indexing **rules** | Operational storage |
| Schema **definitions** | — |

**Where is the actual storage?**
- Decision records and evidence bundles are stored in **Enterprise Memory** (via Memory Services)
- CAF maintains a catalog (metadata, references, indexes) pointing to these records
- CAF enforces policies on how records are structured, linked, and accessed

---

## Subsystem Documents

### Memory Stores (by Memory Class)

| Memory Class | Folder | Description | Status |
|--------------|--------|-------------|--------|
| **Episodic** | [episodic-memory-store/](./episodic-memory-store/) | Event-based, time-ordered, case-bound records | 🟡 Draft |
| **Semantic** | [semantic-memory-store/](./semantic-memory-store/) | Learned beliefs, patterns, probabilistic inferences | 🟡 Draft |
| **Procedural** | [procedural-memory-store/](./procedural-memory-store/) | Learned skills, procedures, action sequences | 🟡 Draft |
| **Preference** | [preference-memory-store/](./preference-memory-store/) | User/agent preferences, behaviors, interaction patterns | 🟡 Draft |

### Episodic Memory Store

> Event-based, time-ordered, case-bound cognitive records. See [episodic-memory-store/README.md](./episodic-memory-store/README.md) for full documentation.

#### Contracts & APIs
| Document | Description | Status |
|----------|-------------|--------|
| [Memory Store Contract](./episodic-memory-store/memory-store-contract.md) | CRD registration, protocols, scope | 🟡 Draft |
| [CAF Store REST API](./episodic-memory-store/caf-store-rest-api.md) | Default write API (order-tolerant, idempotent) | 🟡 Draft |
| [Record Relationships](./episodic-memory-store/record-relationships.md) | How records link and traversal patterns | 🟡 Draft |

#### Record Schemas (9 types)
| Document | Description | Status |
|----------|-------------|--------|
| [Case Records](./episodic-memory-store/case-records.md) | Root anchor, lifecycle, resolution | 🟡 Draft |
| [Decision Records](./episodic-memory-store/decision-records.md) | Decision with rationale | 🟡 Draft |
| [Evidence Bundles](./episodic-memory-store/evidence-bundles.md) | Context at decision time | 🟡 Draft |
| [Context Snapshots](./episodic-memory-store/context-snapshots.md) | Compiled context per turn | 🟡 Draft |
| [Outcome Records](./episodic-memory-store/outcome-records.md) | Post-decision outcomes | 🟡 Draft |
| [Override Records](./episodic-memory-store/override-records.md) | Manual override documentation | 🟡 Draft |
| [Handoff Context](./episodic-memory-store/handoff-context.md) | State transfer between agents | 🟡 Draft |
| [Hypothesis Records](./episodic-memory-store/hypothesis-records.md) | Learned patterns (bridge to Semantic) | 🟡 Draft |
| [Incident Timelines](./episodic-memory-store/incident-timelines.md) | Chronological event sequences | 🟡 Draft |

### Semantic Memory Store

> Learned beliefs, patterns, and probabilistic inferences. Domain-scoped (workbench), not case-bound. See [semantic-memory-store/README.md](./semantic-memory-store/README.md) for full documentation.

#### Contracts & APIs
| Document | Description | Status |
|----------|-------------|--------|
| [Record Relationships](./semantic-memory-store/record-relationships.md) | Entity-anchored traversal patterns | 🟡 Draft |

#### Record Schemas (6 types)
| Document | Description | Status |
|----------|-------------|--------|
| [Hypothesis Records](./semantic-memory-store/hypothesis-records.md) | Patterns pending promotion to knowledge | 🟡 Draft |
| [Pattern Summary](./semantic-memory-store/pattern-summary.md) | Recurring patterns with conditions | 🟡 Draft |
| [Learned Constraints](./semantic-memory-store/learned-constraints.md) | Advisory "avoid X when Y" guidelines | 🟡 Draft |
| [Evaluation Findings](./semantic-memory-store/evaluation-findings.md) | Benchmark and test results | 🟡 Draft |
| [Entity Beliefs](./semantic-memory-store/entity-beliefs.md) | Probabilistic entity attributes | 🟡 Draft |
| [Relationship Beliefs](./semantic-memory-store/relationship-beliefs.md) | Inferred entity connections | 🟡 Draft |

### Procedural Memory Store

> Learned skills, procedures, and action patterns. Skill-anchored, role/workbench-scoped. See [procedural-memory-store/README.md](./procedural-memory-store/README.md) for full documentation.

#### Record Schemas (4 types)
| Document | Description | Status |
|----------|-------------|--------|
| [Learned Skills](./procedural-memory-store/learned-skills.md) | Capabilities learned from successful patterns | 🟡 Draft |
| [Procedures](./procedural-memory-store/procedures.md) | Step-by-step guidance derived from cases | 🟡 Draft |
| [Action Sequences](./procedural-memory-store/action-sequences.md) | Successful tool invocation patterns | 🟡 Draft |
| [Tool Usage Patterns](./procedural-memory-store/tool-usage-patterns.md) | Effective tool combinations and orderings | 🟡 Draft |
| [Record Relationships](./procedural-memory-store/record-relationships.md) | Skill-anchored traversal patterns | 🟡 Draft |

### Preference Memory Store

> Learned preferences and behavioral patterns. Subject-anchored (user/agent), context-sensitive. See [preference-memory-store/README.md](./preference-memory-store/README.md) for full documentation.

#### Record Schemas (4 types)
| Document | Description | Status |
|----------|-------------|--------|
| [User Preferences](./preference-memory-store/user-preferences.md) | Learned preferences for human users | 🟡 Draft |
| [Agent Behaviors](./preference-memory-store/agent-behaviors.md) | Observed agent behavioral patterns | 🟡 Draft |
| [Interaction Patterns](./preference-memory-store/interaction-patterns.md) | How entities prefer to interact | 🟡 Draft |
| [Contextual Preferences](./preference-memory-store/contextual-preferences.md) | Context-dependent preference variations | 🟡 Draft |
| [Record Relationships](./preference-memory-store/record-relationships.md) | Subject-anchored traversal patterns | 🟡 Draft |

### CAF Services
| Document | Description | Status |
|----------|-------------|--------|
| [Memory Store Catalog](./memory-store-catalog.md) | Discovery API for registered memory stores | 🟡 Draft |
| [Record Content Schema Registry](./record-content-schema-registry.md) | Schema discovery, retrieval, and validation | 🟡 Draft |
| [Explanation Service](./explanation-service.md) | Explanation generation using semantic explainers from Schema Registry | 🟡 Draft |
| [Enterprise Learning Services](./enterprise-learning-services.md) | Conceptual design for memory promotion; manual process initially | 🟡 Draft |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                 COGNITIVE AUDIT FABRIC                           │
│                     (Control Plane)                              │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                     POLICIES                             │    │
│  │                                                          │    │
│  │  • Memory capture policies (what to capture, when)       │    │
│  │  • Schema definitions (structure of records)             │    │
│  │  • Linking rules (how records relate)                    │    │
│  │  • Retention policies (how long to keep)                 │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                     CATALOGS                             │    │
│  │                                                          │    │
│  │  Core:          Decision Records | Evidence Bundles      │    │
│  │                 Context Snapshots                         │    │
│  │                                                          │    │
│  │  Lifecycle:     Outcome Records | Override Records       │    │
│  │                 Handoff Context                           │    │
│  │                                                          │    │
│  │  Learning:      Hypothesis Records | Incident Timelines  │    │
│  │                                                          │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                    SERVICES                              │    │
│  │                                                          │    │
│  │  ┌───────────────────────────────────────────────────┐  │    │
│  │  │              Explanation Service                   │  │    │
│  │  │  • Narrative assembly from records                 │  │    │
│  │  │  • Counterfactual generation                       │  │    │
│  │  │  • Multi-audience formatting                       │  │    │
│  │  └───────────────────────────────────────────────────┘  │    │
│  └─────────────────────────────────────────────────────────┘    │
│                            │                                     │
│                            │ references                          │
│                            ▼                                     │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │         ENTERPRISE MEMORY (via Memory Services)          │    │
│  │                                                          │    │
│  │  Actual storage of decision records, evidence bundles   │    │
│  └─────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Record Binding Conventions

### Episodic Record Immutability

All **episodic memory records** are **immutable**. Once written, they cannot be modified or deleted.

```yaml
# Every episodic record includes:
content_hash: string    # sha256:<hex> — cryptographic hash of record content
```

| Principle | Description |
|-----------|-------------|
| **Append-Only** | Records can only be created, never updated or deleted |
| **Hash-Verified** | Content hash ensures integrity and enables de-duplication |
| **Tamper-Evident** | Any modification would change the hash, revealing tampering |
| **Corrections via New Records** | Errors are corrected by creating `override_record` referencing original |

See [CAF Store REST API - Immutability](./episodic-memory-store/caf-store-rest-api.md#immutability) for enforcement details.

### ID Format (UUID v4)

All CAF record identifiers use **UUID v4** format:

```yaml
id: uuid              # e.g., "550e8400-e29b-41d4-a716-446655440000"
content_hash: string  # sha256:<hex> — record content hash
case_id: uuid         # Universal binding anchor
*_id: uuid            # All foreign key references
```

| Principle | Description |
|-----------|-------------|
| **Uniqueness** | UUIDs are globally unique across all systems |
| **Opacity** | No semantic meaning encoded (unlike sequential IDs) |
| **Decentralization** | Can be generated without coordination |
| **Immutability** | IDs never change after creation |

### Case ID (Universal Binding)

All CAF records include a **`case_id`** field as a universal binding identifier:

```yaml
case_id: string  # Universal binding ID (= hub request_id when Hub-originated)
```

| Context | case_id Value |
|---------|---------------|
| **Hub-originated** | Same as `hub_metadata.request_id` |
| **External system** | External case/ticket/reference ID |
| **Standalone agent** | Agent-assigned correlation ID |

This enables:
- **Cross-record correlation** regardless of origin system
- **Mixed-origin cases** (some records from Hub, some from external systems)
- **System-agnostic queries** ("all records for case X")

### Hub Metadata (Optional)

All CAF records include an **optional** `hub_metadata` section that captures the Hub context in which the record was created:

```yaml
hub_metadata:
  tenant_id: string              # Tenant identifier
  subscription_id: string        # Subscription within tenant
  workbench_id: string           # Workbench where event occurred
  scenario_id: string            # Scenario governing this record
  request_id: string             # Hub Request this record belongs to
  parent_request_id: string      # Parent request if nested (optional)
```

| Field | Description | Always Present? |
|-------|-------------|-----------------|
| `tenant_id` | Top-level organizational boundary | Yes |
| `subscription_id` | Subscription within tenant | Yes |
| `workbench_id` | Workbench context for the operation | Yes |
| `scenario_id` | Scenario that governed the behavior | Context-dependent |
| `request_id` | Hub Request ID for traceability | Context-dependent |
| `parent_request_id` | For nested/sub-requests | Only when applicable |

**Why optional?** CAF records may be created outside of Hub context (e.g., by standalone agents or external systems). When present, `hub_metadata` enables:
- Cross-record correlation (all records for a request)
- Workbench-scoped queries and dashboards

### Typed Content Convention

For fields containing structured data (objects, arrays with complex items), CAF uses a **typed content** pattern with content type metadata:

#### Typed Content Wrapper

```yaml
typed_content:
  content: object | array | string   # The actual content
  content_type:
    # MIME-compatible string (for interoperability)
    mime: string                     # e.g., "application/vnd.olympus.caf.decision-factors.v1+json"
    
    # Structured form (for programmatic access)
    format: string                   # Serialization: json (default) | yaml
    schema: string                   # Fully qualified type: olympus.caf.decision-factors
    schema_version: string           # Semantic version: "1.0.0"
    schema_uri: string               # Optional: resolvable schema location
```

#### MIME Type Format

CAF uses **vendor MIME types** (RFC 6838 compliant) for schema+version encoding:

```
application/vnd.olympus.<namespace>.<type>.v<major>+<format>
```

| Component | Description | Example |
|-----------|-------------|---------|
| `vnd.olympus` | Vendor prefix | Required |
| `<namespace>` | Subsystem namespace | `caf`, `seer`, `hub` |
| `<type>` | Schema type name | `decision-factors`, `evidence-bundle` |
| `v<major>` | Major version | `v1`, `v2` |
| `+<format>` | Serialization suffix | `+json`, `+yaml` |

**Examples:**
- `application/vnd.olympus.caf.decision-factors.v1+json`
- `application/vnd.olympus.caf.entity-snapshot.v2+json`
- `application/vnd.olympus.seer.agent-memory.v1+yaml`

#### Serialization Format Requirements

**CAF records MUST use human-readable serialization formats.** This is a design requirement to support:
- Manual inspection during debugging and investigation
- Audit review without specialized tooling
- Log analysis and troubleshooting
- Regulatory examination and discovery

| Format | Status | Use Case |
|--------|--------|----------|
| **JSON** | ✅ **Default** | All CAF records unless specified otherwise |
| **YAML** | ✅ Allowed | Configuration-heavy content, multi-line text |
| **XML** | ⚠️ Legacy only | Integration with legacy systems |
| **Binary (CBOR, Protobuf, etc.)** | ❌ **Not allowed** | Use only in performance-critical non-CAF contexts |

**Default Rule:** When `format` is not specified, assume **JSON**.

```yaml
# Preferred - explicit JSON
content_type:
  mime: "application/vnd.olympus.caf.decision-factors.v1+json"
  format: json
  schema: olympus.caf.decision-factors
  schema_version: "1.0.0"

# Also valid - format defaults to json when omitted
content_type:
  mime: "application/vnd.olympus.caf.decision-factors.v1+json"
  schema: olympus.caf.decision-factors
  schema_version: "1.0.0"
```

**Rationale:** CAF exists for audit, explanation, and institutional learning. Binary formats optimize for machine efficiency at the cost of human legibility—the opposite of CAF's mission. The marginal storage/bandwidth savings do not justify the loss of inspectability.

#### Why Structured Form Too?

Standard MIME types have limitations:
- Cannot express **minor/patch versions** (only major in suffix)
- Cannot include **schema URI** for resolution
- Parsing type components requires string manipulation

The structured form provides:

| Need | MIME Limitation | Structured Solution |
|------|-----------------|---------------------|
| **Full semver** | Only major version | `schema_version: "1.2.3"` |
| **Schema resolution** | No URI support | `schema_uri: "olympus://schemas/..."` |
| **Programmatic access** | String parsing required | Direct field access |
| **Format negotiation** | Coupled with type | Separate `format` field |

#### Schema Registry

Content types reference schemas in the **CAF Schema Registry**:

```
olympus://schemas/<namespace>/<type>/v<version>
```

Example: `olympus://schemas/caf/decision-factors/v1.0.0`

The registry provides:
- Schema definitions (JSON Schema, Avro, Protobuf)
- Version history and compatibility matrix
- Validation endpoints
- Documentation links

#### When to Use Typed Content

| Field Type | Use Typed Content? | Rationale |
|------------|-------------------|-----------|
| Simple scalars | No | String, number, boolean need no typing |
| Enums | No | Type is self-evident |
| Domain objects | **Yes** | May evolve, need version tracking |
| Extensible arrays | **Yes** | Item types may vary |
| External data | **Yes** | Schema unknown at design time |
| Model I/O | **Yes** | Model-specific formats |
- Scenario-level analytics and auditing
- Request-level traceability across systems

---

## Core Capabilities

### Decision Journaling
Capture rationale at decision time:
- What was decided
- What alternatives existed
- What evidence was considered
- What reasoning was applied
- Who is accountable

### Evidence Bundles
Package context for reproducibility:
- State of information at decision time
- Documents and data referenced
- Model inputs and outputs
- Retrieval results

### Explanation Generation
Produce human-readable explanations:
- Narrative assembly from records
- Counterfactual generation
- Compliance-appropriate summaries
- Multi-audience formats

### Replay Capability
Reconstruct decisions with original context:
- Time-travel to decision point
- Same inputs produce same explanation
- Audit and investigation support

---

## The CAF Questions

CAF enables answering the critical questions:

### Decision & Audit Questions
| Question | CAF Component |
|----------|---------------|
| *"What was decided?"* | Decision Records |
| *"Why was it decided?"* | Decision Records + Explanation Service |
| *"What was known at the time?"* | Evidence Bundles + Context Snapshots |
| *"What would have happened otherwise?"* | Counterfactual Generator |
| *"Can we prove this was reasonable?"* | Explanation Service + Evidence Bundles |

### Outcome & Learning Questions
| Question | CAF Component |
|----------|---------------|
| *"Did the decision work?"* | Outcome Records |
| *"Who overrode it and why?"* | Override Records |
| *"What patterns are we seeing?"* | Hypothesis Records |

### Investigation & Continuity Questions
| Question | CAF Component |
|----------|---------------|
| *"What happened in sequence?"* | Incident Timelines |
| *"What context did the agent have?"* | Context Snapshots |
| *"What does the next agent need to know?"* | Handoff Context |

---

## Compliance Use Cases

| Requirement | CAF Support |
|-------------|-------------|
| **Model Explainability** | Explain AI decisions in human terms |
| **Fair Lending** | Document decision factors and outcomes |
| **Right to Explanation** | Generate customer-facing explanations |
| **Audit Response** | Produce evidence packages on demand |
| **Dispute Resolution** | Reconstruct decision context |

---

## Seer Integration

| Integration Point | Description |
|-------------------|-------------|
| **Agent Observability** | Decision traces feed CAF |
| **Context Assembly** | CAF receives context snapshots |
| **Runtime Enforcement** | Policy violations logged |
| **Workbench Integration** | CAF accessed through Hub Workbench |

---

## Workbench as CAF Memory Provider

From the Todo notes:
- Workbench with Enterprise Memory Storage Services
- Enterprise Memory Storage Services as part of Seer
- Workbench Enterprise Memory Stores to CAF Memory mapping
- Workbench serving as CAF Memory Provider

---

## Related Documentation

- [Memory Services](../memory-services/README.md) — Enterprise Memory storage
- [Hub Enterprise Memory](../memory-services/hub-enterprise-memory.md) — Memory layer
- [Seer Agent Observability](../../../olympus-seer-docs/seer-design/subsystems/agent-observability.md)

---

---

## TODO: Concepts to Clarify

The following concepts require detailed specification:

| Concept | Description | Priority | Status |
|---------|-------------|----------|--------|
| **CAF-to-Memory-Store Contract** | Interface contract between CAF control plane and Enterprise Memory stores | P1 | ✅ Done |
| **CAF Store REST API** | Default read/write API for memory stores (order-tolerant, idempotent) | P1 | ✅ Done |
| **CAF Memory Store Catalog** | Registry of available memory stores, capabilities, routing; discovery API | P1 | ✅ Done |
| **CAF Explainer Services** | Explanation generation using semantic explainers; audience formatting; counterfactuals | P1 | ✅ Done |
| **CAF Enterprise Learning Services** | Conceptual design complete; manual initially, automation post-adoption | P1 | ✅ Done |
| **CAF Record Content Schema Repository** | Central registry for content type schemas (olympus://schemas/...); CRD registration, discovery API | P2 | ✅ Done |
| **Procedural Memory Store** | Skill, learned-procedure record types (4 types: LearnedSkill, Procedure, ActionSequence, ToolUsagePattern) | P2 | ✅ Done |
| **Preference Memory Store** | User/agent preference record types (4 types: UserPreference, AgentBehavior, InteractionPattern, ContextualPreference) | P2 | ✅ Done |

### Completed
- Episodic Memory Store — 9 record types, domain contracts, REST API
- Semantic Memory Store — 6 record types, domain-scoped, evidence-grounded
- Record relationships — case_id binding (episodic), workbench_id binding (semantic)
- Typed content convention — MIME + versioned schemas
- Human-readable serialization — JSON default

### Deferred Items
- Schema validation enforcement — depends on Schema Repository
- Compliance mappings — regulatory-specific

