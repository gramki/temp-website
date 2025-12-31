# Solution Approach: Features as ETSL Data Products

## A Directional Guide for Architects and Product Managers

---

## TL;DR

The semantic infrastructure for features doesn't need to be invented from scratch. **ETSL (Enterprise Truth & Semantics Layer)** already provides the foundation:

- **Entity definitions** → ETSL Semantic Artifacts
- **Feature metadata** → ETSL Data Products
- **Relationships and composites** → ETSL relationship modeling
- **Governance and lineage** → ETSL authority and assertion patterns

The approach: **Build Feature Data Products as a specialized class of ETSL Data Products**, inheriting ETSL's semantic rigor while adding feature-specific concerns (freshness, serving, ML consumption).

---

## Why ETSL?

The [problem document](./features-as-data-products.md) identifies what's missing from current feature stores:

| Gap | What's Needed |
|-----|---------------|
| Entity semantics | Defined entities with relationships, not just row keys |
| Composite entities | Formal definitions for Customer × Merchant, etc. |
| Business-language metadata | Descriptions, ownership, governance |
| Discoverability | Self-service browsing by entity, domain, concept |
| Lineage | Structural traceability from feature to source |

ETSL already addresses these for enterprise data. The insight: **features are a type of enterprise truth**, and should be modeled as such.

---

## ETSL Primer (For This Context)

For those unfamiliar with ETSL, a minimal orientation:

| ETSL Concept | What It Means | Feature Analog |
|--------------|---------------|----------------|
| **Semantic Artifact** | A definition of meaning — entity types, relationships, constraints | Entity Registry entries |
| **Data Artifact** | A governed dataset that implements a semantic artifact | Feature tables/views |
| **Data Product** | A consumable, governed, discoverable data asset | A feature set with catalog entry |
| **Authority** | Who has the right to assert truth about something | Feature ownership |
| **Assertion** | A statement of fact with provenance | A feature value with lineage |

ETSL distinguishes **schema-level** (what things mean) from **instance-level** (actual values). This maps directly to the [entity type vs. instance distinction](./entity-type-vs-instance-analysis.md) that feature stores conflate.

For full ETSL documentation, see [ETSL Documentation Index](../etsl/README.md).

---

## The Approach

### 1. Entity Registry = ETSL Semantic Artifacts

Define entities (Customer, Account, Merchant, CardBIN, etc.) as **ETSL Semantic Artifacts**:

```yaml
# Example: Entity definition as ETSL Semantic Artifact
semantic_artifact:
  type: entity
  name: Customer
  description: "An individual or business with an account relationship"
  authority: customer-mdm-team
  key:
    field: customer_id
    type: string
  relationships:
    - target: Account
      type: one-to-many
    - target: Device
      type: many-to-many
  governance:
    pii: true
    retention: 7-years
```

**Why this works:**
- ETSL already has patterns for entity definition, authority, and governance
- Relationships are first-class
- The semantic artifact is queryable, versionable, and governed

---

### 2. Composite Entities = ETSL Relationship Artifacts

Define composite entities (Customer × Merchant, etc.) as **ETSL relationship semantic artifacts**:

```yaml
# Example: Composite entity as ETSL Semantic Artifact
semantic_artifact:
  type: composite_entity
  name: CustomerMerchantRelationship
  description: "A customer's transactional relationship with a specific merchant"
  authority: fraud-features-team
  constituents:
    - entity: Customer
      role: subject
    - entity: Merchant
      role: object
  key_schema:
    - customer_id: string
    - merchant_id: string
  materialization: explicit  # or virtual
```

**Why this works:**
- Composites are now formal definitions, not ad-hoc key concatenations
- The key schema is explicit and discoverable
- Authority is assigned

---

### 3. Feature Catalog = ETSL Data Products

Define features as **ETSL Data Products** with feature-specific metadata:

```yaml
# Example: Feature as ETSL Data Product
data_product:
  name: customer_merchant_spend_velocity_30d
  type: feature
  entity: CustomerMerchantRelationship
  description: "Average daily spend by this customer at this merchant over 30 days"
  
  # Standard ETSL metadata
  authority: fraud-features-team
  lineage:
    source: transactions
    transform: aggregate by (customer_id, merchant_id, day) → avg
  governance:
    pii_derived: true
    approved_uses: [fraud-detection, risk-scoring]
  
  # Feature-specific metadata
  feature_metadata:
    freshness: T+1
    granularity: daily
    serving:
      online: true
      offline: true
    quality:
      coverage: 0.95
      drift_threshold: 0.1
```

**Why this works:**
- Features inherit ETSL's governance, lineage, and authority patterns
- Feature-specific concerns (freshness, serving, quality) are added as extensions
- The feature is discoverable in the ETSL catalog

---

### 4. Feature Store = ETSL Data Artifact (Execution Layer)

The physical feature store (Feast, DynamoDB, Redis, etc.) remains the **execution substrate**. It's an ETSL Data Artifact that implements the Data Product:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           LAYERED ARCHITECTURE                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    ETSL Semantic Layer                              │   │
│   │   • Entity definitions (Semantic Artifacts)                         │   │
│   │   • Composite entity definitions                                    │   │
│   │   • Relationship models                                             │   │
│   │   • Governance constraints                                          │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│                                    ▼                                        │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    Feature Catalog (Data Products)                  │   │
│   │   • Feature definitions with business descriptions                  │   │
│   │   • Ownership and authority                                         │   │
│   │   • Lineage and approved uses                                       │   │
│   │   • Feature-specific metadata (freshness, quality)                  │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│                                    ▼                                        │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                    Feature Store (Data Artifacts)                   │   │
│   │   • Physical storage (S3, DynamoDB, Redis)                          │   │
│   │   • Materialization pipelines                                       │   │
│   │   • Online/offline serving                                          │   │
│   │   • Existing feature store infrastructure                           │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**The feature store doesn't change.** The semantic and catalog layers are added on top.

---

## What This Enables

| Capability | How ETSL Enables It |
|------------|---------------------|
| **Entity browsing** | Query ETSL semantic artifacts by type, domain, relationship |
| **Feature discovery** | Search ETSL data products with business-language metadata |
| **Composite discoverability** | Composites are first-class semantic artifacts, not hidden keys |
| **Lineage** | ETSL assertion patterns provide structural lineage |
| **Governance** | Authority, approved uses, PII tracking are native to ETSL |
| **Self-service** | ETSL catalog is browsable by non-engineers |
| **Agent-readiness** | Agents can query ETSL for entities and features before creating |

---

## Implementation Direction

### Phase 1: Entity Registry on ETSL

1. Define core entities (Customer, Account, Transaction, Merchant, etc.) as ETSL Semantic Artifacts
2. Define key composite entities (Customer × Merchant, etc.)
3. Establish authority assignments
4. Validate with one domain (e.g., Fraud)

### Phase 2: Feature Catalog on ETSL

1. Define feature metadata schema as ETSL Data Product extension
2. Register existing features with business descriptions
3. Enable catalog browsing for non-engineers
4. Validate discoverability with product managers

### Phase 3: Integration with Feature Store

1. Connect ETSL catalog to existing feature store(s)
2. Ensure feature writes update catalog metadata
3. Enable lineage from feature to source data
4. Validate with end-to-end feature lifecycle

### Phase 4: Self-Service Decisions (Future)

1. Rule authoring layer that consumes ETSL-registered features
2. Testing infrastructure with historical replay
3. Governance workflows for rule approval
4. Decision execution with audit logging

---

## What This Is NOT

This document is **directional**, not comprehensive. It does not cover:

- Detailed schema designs for ETSL artifacts
- API specifications for catalog access
- Migration plan for existing features
- Integration architecture with specific feature stores
- UI/UX for self-service discovery
- Rule language design for decision authoring

These require dedicated architecture and product documents.

---

## Open Questions

| Question | Owner |
|----------|-------|
| Which ETSL patterns apply directly vs. need extension for features? | Architecture |
| How do feature-specific concerns (freshness, serving) integrate with ETSL metadata? | Architecture |
| What's the migration path for existing features without ETSL metadata? | Engineering |
| How does the ETSL catalog integrate with existing data catalogs (if any)? | Architecture |
| What's the UI for self-service discovery? | Product |

---

## Related Documents

- [Features as Data Products](./features-as-data-products.md) — The problem statement
- [ETSL Documentation Index](../etsl/README.md) — Full ETSL guidance
- [ETSL Purpose and Story](../etsl/introduction/etsl-purpose-and-story.md) — Why ETSL exists
- [Building Data Products using ETSL](../etsl/building-data-products/building-data-products-using-etsl-data-artifacts.md) — ETSL data product patterns
- [Questions on Features and Decisions](./questions-on-features-and-decisions.md) — Open deliberation points

