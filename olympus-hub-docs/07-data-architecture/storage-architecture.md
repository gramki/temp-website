# Storage Architecture

Hub data is organized into **four categories**, each with distinct scope, lifecycle, ownership, and access patterns. This architecture clearly separates platform-managed data from application-managed data, and cognitive data (memory/knowledge) from operational/business data.

---

## Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         STORAGE ARCHITECTURE                                 │
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │ LAYER 1: SYSTEM DATA                                                    │ │
│  │ Scope: Platform-wide, shared across all tenants                        │ │
│  │ Owner: Platform Operators (Zeta)                                       │ │
│  │ Examples: Blueprints, Command Registries, Industry KB                  │ │
│  └────────────────────────────────────────────────────────────────────────┘ │
│                                  │                                           │
│                                  ▼                                           │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │ LAYER 2: TENANT SPEC / METADATA                                        │ │
│  │ Scope: Tenant-specific configuration and definitions                   │ │
│  │ Owner: Tenant Administrators                                            │ │
│  │ Examples: Workbench Definitions, IAM, Triggers, Tenant KB              │ │
│  └────────────────────────────────────────────────────────────────────────┘ │
│                                  │                                           │
│                                  ▼                                           │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │ LAYER 3: WORKBENCH-SCOPED DATA                                          │ │
│  │                                                                          │ │
│  │  ┌────────────────────────────┐  ┌────────────────────────────────────┐ │ │
│  │  │     OPERATIONS DATA        │  │    APPLICATION DATA STORES        │ │ │
│  │  │    (Hub-Managed)           │  │     (Application-Managed)          │ │ │
│  │  │                            │  │                                     │ │ │
│  │  │  • Requests, Tasks         │  │  • Ganymede (Relational)           │ │ │
│  │  │  • Activities, Actions     │  │  • Callisto (Key-Value)            │ │ │
│  │  │  • Signals, Sessions       │  │  • Europa (Search/Analytics)       │ │ │
│  │  └────────────────────────────┘  └────────────────────────────────────┘ │ │
│  └────────────────────────────────────────────────────────────────────────┘ │
│                                                                              │
│  ┌────────────────────────────────────────────────────────────────────────┐ │
│  │ COGNITIVE SERVICES (Hub-Managed with Specific Semantics)               │ │
│  │                                                                          │ │
│  │  ┌──────────────────────────────────┐  ┌──────────────────────────────┐ │ │
│  │  │         Memory Services          │  │      Knowledge Services      │ │ │
│  │  │      (Control Plane: CAF)        │  │                              │ │ │
│  │  │                                  │  │ • Knowledge Bank             │ │ │
│  │  │ • Enterprise Memory              │  │ • RAG Retrieval              │ │ │
│  │  │   (Semantic, Episodic, Proced.)  │  │                              │ │ │
│  │  │ • Agent Memory (Session-scoped)  │  │                              │ │ │
│  │  │ • User Memory                    │  │                              │ │ │
│  │  └──────────────────────────────────┘  └──────────────────────────────┘ │ │
│  │                                                                          │ │
│  │  Traditional Audit: Cipher Audit Service (not a cognitive store)       │ │
│  └────────────────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Layer 1: System Data

**Scope:** Platform-wide data shared across all tenants. Managed by Hub platform operators.

**Characteristics:**
- Read-only for tenants (consume, not modify)
- Versioned with controlled release cycles
- High availability, low change frequency

### Data Categories

| Category | Description | Examples |
|----------|-------------|----------|
| **Workbench Blueprints** | Reusable templates/patterns that tenants can instantiate | Dispute Resolution Blueprint, KYC Blueprint, Reconciliation Blueprint |
| **Command Registries** | Catalog of Commands/Actuators available platform-wide | Payment Commands, Account Commands, Notification Commands |
| **Domain/Industry Knowledge Base** | Pre-built knowledge for specific industries | Banking regulations, Insurance claim patterns, Healthcare compliance |
| **I/O Gateway Discovery** | Available I/O Gateways and their capabilities | Atropos endpoints, Heracles routes, Dia storage locations |
| **Ontology Definitions** | Core ontology concepts and relationships | Signal types, Request types, Operation patterns |

### Access Patterns

| Actor | Access |
|-------|--------|
| Platform Operators | Read/Write |
| Tenant Admins | Read (reference in Tenant Spec) |
| Agents | Read (runtime reference) |

---

## Layer 2: Tenant Spec / Metadata

**Scope:** Tenant-specific configuration and definitions. Managed by tenant administrators.

**Characteristics:**
- Tenant-isolated (strict multi-tenancy)
- Versioned with migration support
- Configuration-time data (not runtime)

### Data Categories

| Category | Description | Examples |
|----------|-------------|----------|
| **Workbench Definitions** | Instantiated workbenches with tenant-specific configuration | Tenant's Dispute Workbench, Tenant's KYC Workbench |
| **Machines** | Registered machines in the tenant's environment | Core Banking System, Payment Gateway, CRM |
| **Environments** | Sandboxes and deployment contexts | Production, Staging, UAT |
| **IAM Configuration** | Identity and access management settings | Roles, Groups, Permissions, Agent enrollments |
| **User Management** | Tenant's human users and their assignments | Operators, Analysts, Supervisors |
| **I/O Gateway Configuration** | Tenant-specific gateway configurations | API routes, Event subscriptions, File endpoints |
| **Triggers** | Signal-to-Request binding definitions | Event triggers, Exception triggers, Scheduled triggers |
| **Tenant Knowledge Base** | Tenant-specific knowledge and policies | Product policies, SOPs, Business rules, Compliance requirements |
| **Notification Templates** | Message templates for subject communication | Email templates, SMS templates, Push notification templates |
| **Request Definitions** | Domain-specific request type specifications | Dispute Filing Request schema, Account Closure Request schema |
| **Application Data Store Definitions** | DDL and configurations for application data stores | Ganymede schemas, Callisto collections, Europa indices |

### Versioning

Tenant Spec data is versioned to support:
- **Change tracking** — Who changed what and when
- **Rollback** — Revert to previous configuration
- **Migration** — Controlled transition between versions (e.g., Workbench Definition v1 → v2)
- **DDL Evolution** — Schema migrations for Application Data Stores

### Access Patterns

| Actor | Access |
|-------|--------|
| Tenant Admins | Read/Write (via Workbench Studio, Control Center) |
| Agents | Read (runtime reference) |
| Platform Operators | Read (support/debugging) |

---

## Layer 3: Workbench-Scoped Data

Layer 3 contains two distinct categories of data, both scoped to a workbench but with different ownership and access patterns.

### 3A. Operations Data (Hub-Managed)

**Scope:** Runtime and transactional data for active and completed operations. Generated and managed by Hub during operation execution.

**Characteristics:**
- High volume, high velocity
- Tenant and workbench isolated
- Lifecycle-managed (active → completed → archived)
- **Hub Applications do NOT directly access these stores**

**Who writes Operations Data:**
- **Signal Exchange** — signals, requests, request updates
- **Request Lifecycle** — request state transitions
- **I/O Gateways** — incoming signals
- **Hub native subsystems** — tasks, activities, actions, sessions

**Hub Applications contribute to Operations Data only through Request updates** (async or inline via Signal Exchange). They do not write directly to Operations Data stores.

#### Data Categories

| Category | Description | Examples |
|----------|-------------|----------|
| **Signals** | Incoming signals from I/O Gateways | Events, Exceptions, Observations, HTTP-Requests, Batch-Requests |
| **Requests** | Standardized requests created from signals | Service Requests, Business Requests, System Requests |
| **Operations** | Running and completed operation instances | Procedures, Workflows, Cases |
| **Activities** | Observable steps within operations | "Verify Identity", "Review Transaction", "Approve Refund" |
| **Tasks** | Agent-assigned work items | Pending tasks, Completed tasks, Reassigned tasks |
| **Actions** | Atomic execution steps | Command invocations, Decisions, Data operations |
| **Agent Sessions** | Agent interaction sessions | Human sessions, AI agent sessions, MCP sessions |
| **Notifications** | Sent notifications and delivery status | Email sent, SMS delivered, Push failed |

#### Retention Policies

| State | Storage Tier | Retention | Access Pattern |
|-------|--------------|-----------|----------------|
| **Active** | Hot storage | Until completion | Frequent read/write |
| **Completed** | Warm storage | Configurable (e.g., 90 days) | Occasional read |
| **Archived** | Cold storage | Configurable (e.g., 7 years) | Rare read (compliance) |

---

### 3B. Application Data Stores (Application-Managed)

**Scope:** Business domain data that Hub Applications need to persist for their specific use cases. Provisioned by tenant admins per workbench.

**Characteristics:**
- Workbench-scoped lifecycle
- Tenant-isolated
- Application-owned (Hub Applications directly access these)
- DDL integrated into Workbench Definition lifecycle
- Schema evolution managed through Workbench Management

#### Available Services

| Service | Type | Description | Use Cases |
|---------|------|-------------|-----------|
| **Ganymede** | Relational DBaaS | PostgreSQL-compatible relational database with DDL execution, lifecycle management | Business entities with complex relationships, transactional integrity, complex queries |
| **Callisto** | Key-Value Store | Flexible key-value storage (optional — use based on application needs) | Entity state, session data, fast lookups, caching |
| **Europa** | Search/Analytics (OpenSearch) | Full-text search, log aggregation, analytics | Search across entities, audit logs, metrics, analytics dashboards |

**Note:** Dia (File Store) is used as an **I/O Gateway** for file-based signal ingestion, not as an Application Data Store. If explicit durable file I/O becomes a requirement for Hub Applications in the future, Dia could be exposed as a file storage service.

#### Provisioning

Application Data Stores are:
1. **Defined** in Workbench Definitions by Process Architects/Developers
2. **Provisioned** by Tenant Admins as part of workbench activation
3. **Schema-managed** through DDL files in the Workbench Definition
4. **Evolved** through versioned DDL migrations tied to workbench lifecycle

```yaml
# Example: Application Data Store definition in Workbench
workbench:
  id: "dispute-resolution"
  
  application_data_stores:
    - name: "dispute_entities"
      type: "ganymede"
      ddl_path: "./ddl/dispute-entities.sql"
      
    - name: "dispute_state_cache"
      type: "callisto"
      collection: "dispute-states"
      
    - name: "dispute_search"
      type: "europa"
      index_template: "./indices/dispute-index.json"
      retention_days: 90
```

---

## Cognitive Services (Hub-Managed)

Cognitive Services are Hub-managed services with **specific semantics** that applications access through Hub-specified interfaces. They are distinct from Application Data Stores because Hub enforces their structure, lifecycle, and integration with request processing.

### Memory Services

Memory Services manage **what the organization and agents remember over time**. CAF manages the lifecycle, contracts, catalog, and access to these memory stores.

| Memory Type | Definition | Scope | Sharing |
|-------------|------------|-------|---------|
| **Enterprise Memory** | Organizational lived cognition — decisions (Semantic), events (Episodic), skills (Procedural) | Workbench lifecycle | Admin-configurable: can expose to other workbenches |
| **Agent Memory** | Session-scoped memory for agent continuity | Session (= Request) | Session Memory shared in session; Session Private scoped to agent |
| **User Memory** | Preferences and learned behaviors for users/subjects | Workbench lifecycle | Admin-configurable: can expose to other workbenches; never cross-tenant |

**Session = Request:** One Request constitutes one Session. All updates to a Request are part of the same Session. A Hub Session can last many days (e.g., long-running case resolution).

**Key characteristics:**
- Hub-specified interfaces with specific semantics
- Integrated into request update semantics
- Applications **read** for context assembly; **write** via structured request updates
- Decay, eviction, and governance handled by Hub via CAF
- Agents do not retain memory beyond Session/Request unless promoted to Enterprise Memory or User Memory

**Memory Store Sharing:**
- Sharing is **admin-configured** — no automatic visibility
- No copy/sync — shared access to the same store
- Service validates access requests for required privileges before granting access

**Important:** Decisions are recorded in **both**:
1. **Enterprise Memory** — cognitive record with rationale, evidence, explanation (long retention, governed by CAF)
2. **Operations Data** — operational log for triaging and issue resolution (operational retention)

### Knowledge Services

Knowledge Services manage **what the enterprise believes to be true** — authoritative, curated information.

**Knowledge Bank** is the service that provides:

| Capability | Description |
|------------|-------------|
| **Ingestion Pipelines** | Ingest documents, policies, and structured content |
| **Transformation** | Process and structure content for retrieval |
| **Storage** | Store knowledge with underlying stores abstracted from clients |
| **Retrieval** | RAG-enabled retrieval for agents and applications |

**Knowledge Stores within Knowledge Bank:**

| Store | Scope | Examples |
|-------|-------|----------|
| **Industry Knowledge Base** | System (Layer 1) | Banking regulations, compliance patterns |
| **Tenant Knowledge Base** | Tenant (Layer 2) | Product policies, SOPs, business rules |

**Key characteristics:**
- Predominantly **retrieve-only** for Hub Applications
- Insert/update managed by authorized personas (Developers, Supervisors, Process Architects)
- Underlying storage is abstracted — clients interact with Knowledge Bank service
- A "Tenant KB" is one store within Knowledge Bank; tenants may have multiple stores

### Cognitive Audit Fabric (CAF)

CAF is the **control plane for Memory Services** — it is **not a storage layer**. CAF provides:

| Function | Description |
|----------|-------------|
| **Lifecycle Management** | Manages lifecycle of memory stores |
| **Contracts** | Informs and guides the contracts for memory operations |
| **Catalog** | Provides a catalog of memory stores |
| **Access Enablement** | Enables access to memory stores |
| **Decision Records Schema** | Defines structure for decision capture in Enterprise Memory |
| **Evidence Bundles** | Packaging and linking of evidence to decisions |
| **Explanation Service** | Narrative generation from Enterprise Memory for audit and transparency |

**Key distinction:** Memory is *stored* in Memory Services (Enterprise, Agent, User). CAF *controls* how memory stores are managed, structured, and accessed.

---

### Audit Service (Traditional Audit)

Hub uses **Cipher's Audit Service** for traditional audit records (who does what, when). This is distinct from cognitive memory:

| Aspect | Audit Service | Memory Services |
|--------|---------------|-----------------|
| **Purpose** | Traditional audit trail | Cognitive learning and recall |
| **Content** | Who, what, when | Why, how, with what evidence |
| **Semantics** | Operational logging | Cognitive semantics |
| **Retention** | Compliance-driven | Learning and governance-driven |

Every cognitive action may have a reflection in both:
- **Audit Service** — operational record of the action
- **Enterprise Memory** — cognitive record with rationale and context

The storage layer for Audit Service is not in scope of this document; it is managed by Cipher.

---

### Application Observability (Hub Application APM)

Hub Applications report **logs, traces, and metrics** to **Olympus Watch** — the unified observability platform. This is distinct from both cognitive memory and traditional audit.

| Signal | Description | Platform |
|--------|-------------|----------|
| **Logs** | Application logs, debug output, error messages | Watch |
| **Traces** | Distributed traces across services | Watch |
| **Metrics** | Application and business metrics | Watch |

**Key points:**
- Application observability is **not storage** — it's operational telemetry
- Hub provides integration with Watch for all Hub Applications
- Watch provides: CS Navigator, User Diagnostics Navigator, Zone Navigator, Signals Navigator
- Storage layer is managed by Watch (not in scope of this document)

**Reference:** [Olympus Watch](https://watch.olympus.tech/)

---

## Storage Selection Guide

This guide helps determine where to store different types of data, based on the cognitive and operational classification from the Seer documentation.

### The Four Questions

| Question | Answer Points To |
|----------|------------------|
| *"What does the enterprise believe to be true?"* | **Knowledge Services** |
| *"What happened and why?"* | **Enterprise Memory** (managed via CAF) |
| *"How should I act now?"* | **Context** (assembled from Memory + Knowledge) |
| *"What business entities does my application manage?"* | **Application Data Stores** |

---

### Decision Matrix

| Data Characteristic | Storage | Reason |
|---------------------|---------|--------|
| **Authoritative enterprise facts** (policies, SOPs, rules) | Knowledge Services | Asserted, governed truth |
| **Decisions, outcomes, precedents** | Enterprise Memory (via CAF) | Institutional learning and audit |
| **Agent learning and preferences** | Agent Memory | Operational continuity |
| **User preferences and personalization** | User Memory | Subject-specific adaptation |
| **Hub operational data** (requests, tasks, signals) | Operations Data | Hub-managed lifecycle |
| **Business domain entities** (disputes, claims, orders) | Application Data Stores | Application-specific, domain logic |
| **Entity state for fast access** | Callisto | Key-value lookup |
| **Complex entity relationships** | Ganymede | Relational queries, transactions |
| **Full-text search, analytics** | Europa | Search, aggregation, logs |

---

### What Goes Where: Detailed Guidance

#### Use **Knowledge Services** when:
- Data is **curated and approved** by humans
- Data represents **policies, rules, SOPs, or reference data**
- Data is **shared across scenarios and applications**
- Applications need to **retrieve** but not **modify** during execution
- Data requires **governance and version control**

**Examples:**
- Product policies and fee structures
- Regulatory compliance requirements
- Standard operating procedures
- Reference data (country codes, currency mappings)

---

#### Use **Memory Services** when:
- Data captures **what happened and why**
- Data evolves **from experience** (not assertion)
- Data has **temporal significance** (when did we learn this?)
- Data needs **decay and eviction** semantics
- Data is used for **context assembly** in future decisions

| Memory Type | Use When |
|-------------|----------|
| **Enterprise Memory** | Capturing decisions, exceptions, overrides, precedents that benefit the organization |
| **Agent Memory** | Maintaining continuity within an agent's operational context |
| **User Memory** | Learning user preferences, behaviors, and personalization data |

**Examples:**
- "Customer X prefers email over SMS" → User Memory
- "Exception granted for policy P-123 with rationale R" → Enterprise Memory
- "Last 5 interactions with this customer" → Agent Memory (session-scoped)

---

#### Use **Enterprise Memory (via CAF)** for decisions when:
- Data must be **immutable and auditable**
- Data explains **why a decision was made**
- Data packages **evidence available at decision time**
- Data supports **regulatory compliance and explainability**

**Note:** CAF is the control plane that governs how these records are structured and accessed in Enterprise Memory.

**Examples:**
- Decision records with rationale → stored in Enterprise Memory, governed by CAF
- Evidence bundles (what the agent "saw" when deciding) → linked in Enterprise Memory
- Explanation narratives → generated by CAF's Explanation Service from Enterprise Memory

---

#### Use **Operations Data** when:
- Data is **Hub-managed operational state**
- Data represents **requests, tasks, activities, actions**
- Applications interact with this data **through Hub APIs** (not direct access)

**Note:** Hub Applications do NOT directly access Operations Data stores. They interact through Hub's Request, Task, and Activity APIs.

---

#### Use **Application Data Stores** when:
- Data is **business domain entities** specific to your application
- Data has its own **state machine and lifecycle** independent of Hub's operational model
- Data requires **domain-specific queries** (SQL, key-value, full-text search)
- Data is **not cognitive** (not about learning, memory, or knowledge)

| Store | Use When |
|-------|----------|
| **Ganymede** | Complex relationships, transactions, SQL queries, joins |
| **Callisto** | Fast lookups, entity state, caching, flexible schemas |
| **Europa** | Full-text search, log aggregation, time-series, analytics |

**Examples:**
- Transaction Dispute entity with state machine → Ganymede
- Dispute status cache for fast lookup → Callisto
- Searchable dispute history and audit logs → Europa

---

### Anti-Patterns to Avoid

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **Storing decisions in Application Data Stores** | Bypasses Enterprise Memory, loses auditability | Use Enterprise Memory (via CAF) |
| **Using Application Data Stores for preferences** | Loses decay/governance semantics | Use User Memory |
| **Treating Knowledge as Memory** | Policies become exceptions | Separate curated knowledge from learned experience |
| **Treating Memory as Knowledge** | One-off decisions become policy | Require explicit promotion path |
| **Direct access to Operations Data** | Bypasses Hub lifecycle management | Use Hub APIs for requests/tasks |
| **Stuffing everything into Europa** | No structure, no relationships | Use Ganymede for entities, Europa for search |

---

### Example: Dispute Resolution Application

| Data | Store | Reason |
|------|-------|--------|
| Dispute policies and rules | Knowledge Services | Curated, governed truth |
| Dispute resolution precedents | Enterprise Memory | Institutional learning |
| Agent's recent interactions | Agent Memory | Session continuity |
| Customer communication preferences | User Memory | Personalization |
| Dispute Request lifecycle | Operations Data (Hub-managed) | Hub controls request flow |
| Transaction Dispute entity | Ganymede | Business entity with state machine |
| Dispute status for UI | Callisto | Fast key-value lookup |
| Dispute search and analytics | Europa | Full-text search, dashboards |
| Decision: "Refund approved" | Enterprise Memory (via CAF) | Immutable audit trail |

---

## Subsystem Conformance

All Hub subsystems are expected to:

| Expectation | Description |
|-------------|-------------|
| **Layer Separation** | Clearly distinguish System, Tenant Spec, Operations, and Application data |
| **Tenant Isolation** | Enforce strict tenant isolation for Layer 2 and Layer 3 data (nothing shared across tenants except publisher-scoped data) |
| **Versioning** | Support versioning for Layer 2 (Tenant Spec) data including DDL |
| **Retention** | Implement configurable retention policies for Layer 3 (Operations) data |
| **Audit Integration** | Emit audit events to Cipher Audit Service |
| **Cognitive Integration** | Write cognitive records (decisions, evidence) to Memory Services via CAF |
| **Schema Evolution** | Support backward-compatible schema changes |
| **Cognitive Separation** | Use Memory/Knowledge services for cognitive data, not Application Data Stores |

---

## Related Documentation

- [Hub Architecture](../02-system-design/hub-architecture.md) — System context
- [Memory Services](../04-subsystems/memory-services/README.md) — Agent and Enterprise Memory
- [Knowledge Services](../04-subsystems/knowledge-services/README.md) — Knowledge Bank and RAG
- [Cognitive Audit Fabric](../04-subsystems/cognitive-audit-fabric/README.md) — Decision records and evidence
- [Workbench Management](../04-subsystems/workbench-management/README.md) — Workbench and DDL lifecycle
- [Cipher IAM](../04-subsystems/supporting-systems/cipher-iam.md) — Identity and access management
- [Ontology Reference](../01-concepts/ontology-reference.md) — Core concepts

### Olympus Platform References

- [Ganymede](https://jupiter.olympus.tech/ganymede/) — Relational DBaaS
- [Callisto](https://jupiter.olympus.tech/callisto/) — Key-Value Store
- [Europa](https://academy.olympus.tech/) — Search and Analytics (OpenSearch)

---

*Status: 🟡 WIP - Architecture established with storage selection guide. To be enriched with specific data models, technology choices, and subsystem conformance details.*
