# Entity Type vs. Instance in Feature Store Systems

## A Detailed Analysis of Current Approaches

---

## 1. The Problem in Detail

### 1.1 Two Levels, One Word

The word "entity" in feature store contexts conflates two distinct concepts:

| Level | Formal Term | What It Represents | Example |
|-------|-------------|-------------------|---------|
| **Type / Schema** | Entity Type, Entity Class, Entity Definition | The abstract concept — what kind of thing exists | "Customer" as a category with properties and relationships |
| **Instance / Data** | Entity Instance, Entity Record | A specific occurrence | Customer ID 12345, "John Smith", Premium segment |

This conflation isn't just semantic imprecision — it reflects a structural gap in how feature stores are designed.

---

### 1.2 Concrete Example: Customer

**At the Type Level (Schema):**
```yaml
entity_type:
  name: Customer
  description: "An individual or business with a banking relationship"
  primary_key: customer_id
  key_type: string
  attributes:
    - name: segment
      type: enum[Retail, Premium, Business]
    - name: tenure_months
      type: integer
  relationships:
    - target: Account
      cardinality: one-to-many
    - target: Device
      cardinality: many-to-many
  constraints:
    - pii: true
    - retention: 7_years
```

**At the Instance Level (Data):**
```json
{
  "customer_id": "12345",
  "segment": "Premium",
  "tenure_months": 36,
  "avg_spend_30d": 450.00,
  "churn_risk": 0.23
}
```

**What feature stores capture:** The instance-level data (feature values keyed by customer_id).

**What feature stores miss:** The type-level definition (what Customer means, its relationships, constraints).

---

### 1.3 Why This Matters

| Capability | Requires Type-Level | Requires Instance-Level |
|------------|---------------------|------------------------|
| "What is a Customer?" | ✓ | |
| "What features exist for Customer?" | ✓ | |
| "What's the avg_spend_30d for customer 12345?" | | ✓ |
| "How does Customer relate to Account?" | ✓ | |
| "Which Customer features are PII-derived?" | ✓ | |
| "Give me all features for customer 12345" | | ✓ |

Feature stores excel at instance-level queries. They cannot answer type-level questions.

---

## 2. How Current Feature Stores Handle This

### 2.0 Important Clarification

All feature stores discussed below **do** have "Entity" as a first-class concept, and this **is** the entity type/class definition — not an instance. The stores are not confused about type vs. instance at the API level.

**The problem is that these entity type definitions are impoverished.** They capture:
- ✓ Name
- ✓ Key schema
- Sometimes: Description, ownership
- ✗ Relationships to other entities
- ✗ Non-feature attributes
- ✗ Constraints (PII, cardinality, validity)
- ✗ Composite entity formalization

The "Entity" in feature stores is a **key resolution mechanism**, not a **rich semantic type**. The stores know "Customer is identified by customer_id" but not "Customer owns Accounts, may have Devices, is subject to PII constraints."

---

### 2.1 Feast (Open Source)

**Entity Definition in Feast:**
```python
from feast import Entity, ValueType

customer = Entity(
    name="customer",
    value_type=ValueType.STRING,
    description="A customer of the bank",
    join_keys=["customer_id"]
)
```

This **is** an entity type definition. Feast's Entity is a schema-level concept.

**What Feast's Entity Type Captures:**

| Aspect | Captured? | How |
|--------|-----------|-----|
| Entity name | ✓ | `name="customer"` |
| Key schema | ✓ | `join_keys=["customer_id"]` |
| Key type | ✓ | `value_type=ValueType.STRING` |
| Description | ✓ | Free-text description field |
| Relationships | ✗ | Not modeled |
| Attributes (non-feature) | ✗ | Not modeled (only features) |
| Constraints (PII, retention) | ✗ | Not modeled |
| Composite entities | ✗ | Manual key concatenation |

**Feature View in Feast:**
```python
customer_features = FeatureView(
    name="customer_features",
    entities=[customer],  # References the entity type
    schema=[
        Field(name="avg_spend_30d", dtype=Float32),
        Field(name="churn_risk", dtype=Float32),
    ],
    source=customer_source,
    ttl=timedelta(days=1),
)
```

**Pros:**
- Open source, widely adopted
- Entity definition exists (even if minimal)
- Feature Views explicitly reference entities

**Cons:**
- Entity is just a key schema, not a semantic concept
- No relationships between entities
- No entity attributes (only features)
- Composite entities require manual key construction
- No governance metadata (ownership, PII, lineage)

**Gap Summary:**
Feast handles instance-level data well. Type-level semantics are minimal — entities are key schemas, not rich definitions.

---

### 2.2 Tecton (Commercial)

**Entity Definition in Tecton:**
```python
from tecton import Entity

customer = Entity(
    name="customer",
    join_keys=["customer_id"],
    description="A banking customer",
    owner="risk-team@company.com",
    tags={"pii": "true", "domain": "customer"}
)
```

**What Tecton Captures:**

| Aspect | Captured? | How |
|--------|-----------|-----|
| Entity name | ✓ | `name="customer"` |
| Key schema | ✓ | `join_keys=["customer_id"]` |
| Description | ✓ | Free-text description |
| Owner | ✓ | `owner` field |
| Tags/metadata | ✓ | `tags` dictionary |
| Relationships | ✗ | Not directly modeled |
| Composite entities | ✓ | Multiple entities in Feature View |

**Feature View with Multiple Entities (Composite):**
```python
@batch_feature_view(
    entities=[customer, merchant],  # Composite: Customer × Merchant
    sources=[transactions],
    ...
)
def customer_merchant_features(transactions):
    return transactions.groupby("customer_id", "merchant_id").agg(...)
```

**Pros:**
- Richer entity metadata (owner, tags)
- Native composite entity support (multiple entities per feature view)
- Strong feature management (versioning, environments)
- Good observability and monitoring

**Cons:**
- Proprietary, expensive
- Relationships between entities still implicit (no graph)
- Tags are unstructured (no schema enforcement)
- No formal entity type registry separate from feature definitions

**Gap Summary:**
Tecton is more mature than Feast on entity semantics. Composite entities are supported. But entity types are still embedded in code, not a queryable registry. Relationships are implicit.

---

### 2.3 AWS SageMaker Feature Store

**Feature Group Definition:**
```python
from sagemaker.feature_store.feature_group import FeatureGroup

customer_fg = FeatureGroup(
    name="customer-features",
    sagemaker_session=session,
    feature_definitions=[
        FeatureDefinition(feature_name="customer_id", feature_type=FeatureTypeEnum.STRING),
        FeatureDefinition(feature_name="avg_spend_30d", feature_type=FeatureTypeEnum.FRACTIONAL),
        FeatureDefinition(feature_name="churn_risk", feature_type=FeatureTypeEnum.FRACTIONAL),
    ],
    record_identifier_feature_name="customer_id",
    event_time_feature_name="event_time",
)
```

**What SageMaker Feature Store Captures:**

| Aspect | Captured? | How |
|--------|-----------|-----|
| Feature Group name | ✓ | `name` |
| Record identifier | ✓ | `record_identifier_feature_name` |
| Feature definitions | ✓ | `feature_definitions` list |
| Entity concept | ✗ | No explicit entity abstraction |
| Relationships | ✗ | Not modeled |
| Composite entities | ✗ | Manual; no native support |
| Ownership/tags | Partial | Via AWS resource tags |

**Pros:**
- Fully managed, scales well
- Integrates with AWS ecosystem (Glue, Athena, SageMaker)
- Online and offline store built-in
- Resource tagging for metadata

**Cons:**
- No explicit entity abstraction — only "Feature Groups"
- Entity is just the record identifier
- No relationships, no composites
- Governance relies on AWS IAM and tagging (not semantic)
- Tightly coupled to AWS

**Gap Summary:**
SageMaker Feature Store is infrastructure-focused. It has no entity concept — only Feature Groups with record identifiers. Type-level semantics are absent.

---

### 2.4 Databricks Feature Store (Unity Catalog)

**Feature Table Definition:**
```python
from databricks.feature_store import FeatureStoreClient

fs = FeatureStoreClient()

fs.create_table(
    name="risk.customer_features",
    primary_keys=["customer_id"],
    df=customer_features_df,
    description="Customer risk features",
)
```

**Unity Catalog Integration:**
```sql
-- Feature table registered in Unity Catalog
-- Inherits catalog/schema/table governance

COMMENT ON TABLE risk.customer_features IS 'Customer risk features for fraud models';
ALTER TABLE risk.customer_features SET OWNER TO `risk-team`;
```

**What Databricks Captures:**

| Aspect | Captured? | How |
|--------|-----------|-----|
| Table name | ✓ | Catalog.schema.table naming |
| Primary keys | ✓ | `primary_keys` |
| Description | ✓ | Comments |
| Ownership | ✓ | Unity Catalog ownership |
| Lineage | ✓ | Unity Catalog lineage tracking |
| Relationships | ✗ | Not modeled (tables are independent) |
| Composite entities | Partial | Multiple primary keys |
| Entity as concept | ✗ | Tables, not entities |

**Pros:**
- Strong governance via Unity Catalog
- Lineage tracking built-in
- Ownership and access control
- Integrates with Delta Lake, Spark

**Cons:**
- Entity is still just a table with primary keys
- No explicit entity type registry
- Relationships not modeled (would require foreign keys, which aren't enforced)
- Composite entities are just multi-column primary keys
- Tightly coupled to Databricks

**Gap Summary:**
Databricks has better governance than most (via Unity Catalog) but no semantic entity model. Tables are the abstraction, not entities. Relationships are not captured.

---

### 2.5 Hopsworks Feature Store

**Entity and Feature Group:**
```python
from hsfs import feature_store

fs = feature_store.get_feature_store()

customer_fg = fs.create_feature_group(
    name="customer_features",
    version=1,
    primary_key=["customer_id"],
    description="Customer features for risk models",
    online_enabled=True,
    statistics_config={"enabled": True},
)
```

**What Hopsworks Captures:**

| Aspect | Captured? | How |
|--------|-----------|-----|
| Feature Group name | ✓ | `name` |
| Primary keys | ✓ | `primary_key` |
| Description | ✓ | `description` |
| Versioning | ✓ | `version` |
| Statistics | ✓ | Built-in feature statistics |
| Lineage | ✓ | Provenance tracking |
| Relationships | Partial | Feature Group joins, but not entity relationships |
| Composite entities | ✓ | Multiple primary keys |

**Pros:**
- Strong versioning and lineage
- Built-in feature statistics and validation
- Composite keys supported
- Feature Group joins modeled
- Open-core (Hopsworks.ai or self-hosted)

**Cons:**
- Entity is still implicit in Feature Group keys
- No explicit entity type registry
- Relationships are at Feature Group level, not entity level
- Less ecosystem adoption than Feast/Databricks

**Gap Summary:**
Hopsworks is more mature on lineage and validation. But entity types are still implicit — there's no registry for "Customer as a concept" separate from feature groups.

---

## 3. Alternative Approaches

### 3.1 DataHub + Feast (Integration Pattern)

**Approach:**
Use Feast for feature storage/serving, DataHub for metadata and entity modeling.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       DATAHUB + FEAST PATTERN                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   DataHub (Type-Level):                                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  - Entity type definitions (as custom aspects)                      │   │
│   │  - Relationships between entities                                   │   │
│   │  - Feature definitions with metadata                                │   │
│   │  - Lineage (feature → source)                                       │   │
│   │  - Ownership, tags, glossary terms                                  │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│                                    │ metadata sync                          │
│                                    ▼                                        │
│   Feast (Instance-Level):                                                   │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  - Feature values keyed by entity instance                          │   │
│   │  - Online/offline serving                                           │   │
│   │  - Materialization                                                  │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Pros:**
- Clear separation: DataHub for semantics, Feast for data
- DataHub has rich entity modeling (entities, aspects, relationships)
- Both are open source
- Lineage visualization in DataHub

**Cons:**
- Integration requires custom work
- Two systems to maintain
- Sync between DataHub metadata and Feast definitions
- DataHub's entity model is generic, not ML-feature-native

**Gap Summary:**
This pattern addresses the type/instance separation but requires glue code. DataHub isn't designed for ML features specifically, so some concepts don't map cleanly.

---

### 3.2 dbt + Feature Store (Semantic Layer Pattern)

**Approach:**
Use dbt's semantic layer for entity/metric definitions, feature store for serving.

```python
# dbt semantic layer (metrics.yml)
semantic_models:
  - name: customers
    entities:
      - name: customer
        type: primary
        expr: customer_id
    dimensions:
      - name: segment
        type: categorical
    measures:
      - name: avg_spend
        agg: average
        expr: transaction_amount
```

**Pros:**
- dbt semantic layer has entity concept
- Metrics are well-defined
- Integrates with BI tools

**Cons:**
- dbt semantic layer is BI-focused, not ML-focused
- No online serving
- Metrics ≠ ML features (different compute patterns)
- Doesn't address composite entities well

**Gap Summary:**
dbt's semantic layer is closer to what's needed for type-level definitions, but it's designed for BI metrics, not ML features. The two have different requirements.

---

### 3.3 Custom Entity Registry + Feature Store (Enterprise Pattern)

**Approach:**
Build a custom Entity Registry that sits above the feature store.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       CUSTOM ENTITY REGISTRY PATTERN                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Entity Registry (Custom):                                                 │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  - Entity type definitions (YAML/JSON/DB)                           │   │
│   │  - Relationships (stored in graph or relational)                    │   │
│   │  - Composite entity definitions                                     │   │
│   │  - Feature definitions with entity anchoring                        │   │
│   │  - Governance metadata (ownership, PII, lineage)                    │   │
│   │  - API for discovery and validation                                 │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│                                    │ references / validates                 │
│                                    ▼                                        │
│   Feature Store (Feast/Tecton/Custom):                                      │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  - Feature values keyed by entity instance                          │   │
│   │  - Online/offline serving                                           │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Known Implementations:**
- Uber (Michelangelo) — custom entity and feature catalog
- Airbnb (Zipline) — feature registry with entity concepts
- Stripe — internal feature platform with entity modeling
- LinkedIn — custom feature marketplace

**Pros:**
- Full control over entity model
- Can be tailored to domain (banking, payments, etc.)
- Clear separation of type and instance
- Can enforce governance at registration time

**Cons:**
- Significant build effort
- Maintenance burden
- Not reusable across companies
- Risk of becoming stale if not integrated into workflows

**Gap Summary:**
This is the most complete solution but requires significant investment. It's what large tech companies have built internally.

---

### 3.4 Knowledge Graph + Feature Store (Ontology Pattern)

**Approach:**
Use a knowledge graph (Neo4j, AWS Neptune, or RDF-based) for entity ontology.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     KNOWLEDGE GRAPH + FEATURE STORE                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Knowledge Graph (Neo4j / Neptune):                                        │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  Schema Level (Type):                                               │   │
│   │    (Customer)-[:OWNS]->(Account)                                    │   │
│   │    (Account)-[:HAS]->(Transaction)                                  │   │
│   │    (Transaction)-[:AT]->(Merchant)                                  │   │
│   │                                                                     │   │
│   │  Optionally Instance Level:                                         │   │
│   │    (Customer:12345)-[:OWNS]->(Account:67890)                        │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│                                    │ entity type lookup                     │
│                                    ▼                                        │
│   Feature Store:                                                            │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │  - Feature values keyed by entity instance                          │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Pros:**
- Native graph modeling for relationships
- Can express complex entity hierarchies
- Query relationships (Cypher, SPARQL)
- Industry-standard ontology languages available (OWL, SHACL)

**Cons:**
- Additional infrastructure to manage
- May be overkill if only schema-level is needed
- Performance concerns if instance-level data is large
- Learning curve for graph query languages
- Integration with feature store is custom

**Gap Summary:**
Powerful for relationship modeling but adds complexity. Best suited when entity relationships are first-class (e.g., fraud rings, network analysis).

---

## 4. Comparative Summary

| System | Type-Level Entity | Relationships | Composites | Governance | Open Source |
|--------|-------------------|---------------|------------|------------|-------------|
| **Feast** | Minimal (key schema) | ✗ | Manual | ✗ | ✓ |
| **Tecton** | Moderate (owner, tags) | ✗ | ✓ Native | Partial | ✗ |
| **SageMaker FS** | None | ✗ | ✗ | AWS tags only | ✗ |
| **Databricks FS** | Table-level | ✗ | Multi-key | Unity Catalog | ✗ |
| **Hopsworks** | Moderate | Partial (joins) | ✓ | ✓ Lineage | Open-core |
| **DataHub + Feast** | ✓ (via DataHub) | ✓ | Manual | ✓ | ✓ |
| **Custom Registry** | ✓ Full control | ✓ | ✓ | ✓ | N/A (custom) |
| **Knowledge Graph + FS** | ✓ | ✓ Native | ✓ | Custom | Varies |

---

## 5. Recommendations

### 5.1 If Starting Fresh

**Recommended:** DataHub + Feast (or Hopsworks)

- Use DataHub as the entity/feature registry (type-level)
- Use Feast or Hopsworks for feature storage/serving (instance-level)
- Build integration layer for sync and validation

### 5.2 If Budget Allows

**Recommended:** Tecton + DataHub

- Tecton for mature feature management
- DataHub for broader entity and lineage modeling
- Tecton's entity model is better than Feast, but still benefits from DataHub's relationship modeling

### 5.3 If Building for Differentiation

**Recommended:** Custom Entity Registry

- Build a lightweight entity registry tailored to your domain
- Define entity types, relationships, and composites formally
- Integrate with existing feature store
- This is the path to "Features as Data Products"

### 5.4 If Relationship-Heavy Use Case

**Recommended:** Knowledge Graph + Feature Store

- If fraud rings, customer networks, or entity relationships are core to the use case
- Neo4j or Neptune for entity graph
- Feature store for feature values

---

## 6. Gap Summary

| Gap | Current State | What's Needed |
|-----|---------------|---------------|
| **Entity Type Richness** | Entity types exist, but are just key schemas | Rich types with relationships, attributes, constraints |
| **Entity Relationships** | Not modeled | Explicit relationship definitions (Customer owns Account) |
| **Composite Entities** | Manual key concatenation | First-class composite definitions (Customer × Merchant) |
| **Non-Feature Attributes** | Not captured (only features) | Entity attributes from master data |
| **Governance Metadata** | Spreadsheets, wikis, or tags | Structured ownership, PII tracking, lineage |
| **Discovery** | Tribal knowledge | Self-service, browsable, business-language catalog |

**The core gap:** Feature stores have entity type definitions — but those definitions are thin (key schemas only). Rich type-level semantics (relationships, constraints, attributes) require additional infrastructure that doesn't exist as a unified, ML-native solution.

---

## 7. Conclusion

Current feature stores are **not confused** about entity type vs. instance — they have explicit Entity definitions at the type level and store feature values at the instance level. The API distinction is clear.

**The problem is that entity type definitions are impoverished:**

| What Entity Types Have | What Entity Types Lack |
|------------------------|------------------------|
| Name | Relationships to other entities |
| Key schema | Non-feature attributes |
| Sometimes: description, owner | Constraints (PII, cardinality) |
| | Composite entity formalization |
| | Queryable registry |

Feature stores treat Entity as a **key resolution mechanism**, not a **semantic concept**. This limits:
- Discoverability ("What entities exist? How do they relate?")
- Governance ("Which entities have PII constraints?")
- Composability ("What is Customer × Merchant as a formal concept?")
- User accessibility ("What does Customer mean in business terms?")

The path forward requires:

1. **Richer Entity Type Definitions** — beyond key schemas
2. **Explicit Relationships** — between entity types
3. **Composite Entity Formalization** — as first-class types
4. **Queryable Entity Registry** — separate from feature store code
5. **Integration** with existing feature stores for instance-level data

This is the foundation for treating features as data products — and for bridging builders and users.

---

