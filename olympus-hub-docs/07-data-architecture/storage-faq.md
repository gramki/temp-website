# Storage Architecture FAQ

> **Audience:** Architects and Developers building Hub subsystems and Hub Applications  
> **Purpose:** Clarify common questions about where to store data and how the storage layers interact

---

## Table of Contents

1. [Fundamental Concepts](#1-fundamental-concepts)
2. [Memory Services](#2-memory-services)
3. [Knowledge Services](#3-knowledge-services)
4. [Application Data Stores](#4-application-data-stores)
5. [Operations Data](#5-operations-data)
6. [Cognitive Audit Fabric (CAF)](#6-cognitive-audit-fabric-caf)
7. [Audit and Observability](#7-audit-and-observability)
8. [Access Patterns and Permissions](#8-access-patterns-and-permissions)
9. [Lifecycle and Retention](#9-lifecycle-and-retention)
10. [Common Scenarios](#10-common-scenarios)

---

## 1. Fundamental Concepts

### Q: What's the difference between cognitive data and operational data?

**Cognitive data** captures *why* something happened — rationale, evidence, learning, and institutional knowledge. It has semantic meaning and supports future decision-making.

**Operational data** captures *what* happened — the state of requests, tasks, activities, and actions. It supports day-to-day operations and issue triaging.

| Aspect | Cognitive Data | Operational Data |
|--------|---------------|------------------|
| Purpose | Learning, recall, explanation | State tracking, triaging |
| Examples | Decisions with rationale, precedents | Request status, task assignments |
| Retention | Governed by learning needs | Governed by operational needs |
| Storage | Memory Services, Knowledge Services | Operations Data |

---

### Q: What's the difference between Memory and Knowledge?

| Dimension | Memory | Knowledge |
|-----------|--------|-----------|
| **Source** | Learned from experience | Curated and asserted by humans |
| **Mutability** | Evolves over time, can decay | Versioned, governed changes |
| **Question answered** | "What happened and what did we learn?" | "What do we believe to be true?" |
| **Examples** | Decisions, precedents, preferences | Policies, SOPs, business rules |

**Rule of thumb:**
- If an agent *looks it up* as authoritative reference → **Knowledge**
- If an agent *learned it* from past experience → **Memory**

---

### Q: What is a Session in Hub? How does it relate to a Request?

**One Request = One Session.** All updates to a Request are part of the same Session.

- A Session can last many days (e.g., a dispute resolution case)
- Agent Memory is scoped to Session (= Request)
- When the Request completes, the Session ends

---

### Q: What does "workbench-scoped" mean for data?

Data scoped to a workbench:
- Is created when the workbench is activated
- Lives for the lifecycle of the workbench
- Is isolated from other workbenches (unless explicitly shared)
- Is deleted/archived when the workbench is deactivated

Both **Operations Data** and **Application Data Stores** are workbench-scoped.

---

## 2. Memory Services

### Q: What are the three types of memory in Hub?

| Memory Type | Scope | Lifecycle | Purpose |
|-------------|-------|-----------|---------|
| **Enterprise Memory** | Workbench | Workbench lifecycle | Organizational cognition — decisions, precedents, procedures |
| **Agent Memory** | Session (= Request) | Request lifecycle | Agent continuity within a single request |
| **User Memory** | Workbench | Workbench lifecycle | User/subject preferences and learned behaviors |

---

### Q: Can memory be shared across workbenches?

**Yes, but only through explicit admin configuration.**

- No automatic sharing between workbenches
- Admins configure which memory stores are visible to which workbenches
- No copy/sync — it's shared access to the same store
- The service validates access requests for required privileges
- **Nothing can be shared across tenants** (except publisher-scoped System Data)

---

### Q: What happens to Agent Memory when a Request completes?

Agent Memory is **Session-scoped**, where Session = Request. When the Request completes:
- Session Memory is no longer accessible
- Agents do not retain memory beyond the Request

**Exception:** If the agent explicitly promotes learnings to Enterprise Memory or User Memory during the Request, those persist.

---

### Q: What's the difference between Session Memory and Session Private Memory?

| Type | Scope | Visibility |
|------|-------|------------|
| **Session Memory** | Session (Request) | Shared across all agents in the session |
| **Session Private Memory** | Agent within Session | Only visible to the specific agent |

---

### Q: How do Hub Applications write to Memory Services?

Hub Applications **do not write directly** to Memory Services. They contribute via **Request updates**:

1. Application sends an async update (e.g., `MEMORY_UPDATE`, `DECISION`) to Signal Exchange
2. Signal Exchange routes the update to the appropriate memory store
3. CAF governs the structure and validation

This ensures all memory writes go through Hub's semantic contracts.

---

### Q: What types of memory are stored in Enterprise Memory?

Enterprise Memory includes:

| Type | Description | Examples |
|------|-------------|----------|
| **Semantic** | Stable facts learned from experience | "Customer X is high-value" |
| **Episodic** | Records of what happened | "Exception granted on 2024-01-15" |
| **Procedural** | How to do things, learned skills | "When pattern P occurs, apply approach A" |

---

## 3. Knowledge Services

### Q: What is Knowledge Bank?

**Knowledge Bank** is the service that provides enterprise knowledge capabilities:

| Capability | Description |
|------------|-------------|
| **Ingestion Pipelines** | Ingest documents, policies, structured content |
| **Transformation** | Process and structure content for retrieval |
| **Storage** | Store knowledge (underlying stores abstracted) |
| **Retrieval** | RAG-enabled retrieval for agents and applications |

---

### Q: What's the relationship between Knowledge Bank and Tenant Knowledge Base?

- **Knowledge Bank** is the *service*
- **Tenant Knowledge Base** is one *store* within Knowledge Bank

Think of it like:
- Knowledge Bank = Database service
- Tenant KB = One database within that service

A tenant may have multiple knowledge stores within Knowledge Bank.

---

### Q: What's stored in Industry KB vs Tenant KB?

| Store | Scope | Owner | Examples |
|-------|-------|-------|----------|
| **Industry Knowledge Base** | System (Layer 1) | Platform (Zeta) | Banking regulations, compliance patterns, industry best practices |
| **Tenant Knowledge Base** | Tenant (Layer 2) | Tenant | Product policies, SOPs, business rules, tenant-specific compliance |

---

### Q: Can Hub Applications modify Knowledge?

**No.** Knowledge Services are **retrieve-only** for Hub Applications.

Insert/update is managed by authorized personas:
- **Developers** — technical documentation, integration guides
- **Process Architects** — SOPs, workflows, business rules
- **Supervisors** — operational guidelines

---

## 4. Application Data Stores

### Q: What are Application Data Stores?

Application Data Stores are **workbench-scoped databases** that Hub Applications use to persist business domain entities. They are distinct from Operations Data (Hub-managed) and Cognitive Services (Memory/Knowledge).

---

### Q: What services are available for Application Data Stores?

| Service | Type | When to Use |
|---------|------|-------------|
| **Ganymede** | Relational DBaaS | Complex relationships, transactions, SQL queries |
| **Callisto** | Key-Value Store | Fast lookups, caching, flexible schemas (optional) |
| **Europa** | Search/Analytics | Full-text search, log aggregation, analytics |

---

### Q: Is Callisto required for all applications?

**No.** Callisto usage is **optional**. 

Not every application needs key-value storage. Developers choose to use Callisto based on their specific business logic requirements. If your application doesn't need caching or fast key-based lookups, you don't need Callisto.

---

### Q: What about Dia (File Store)?

For Hub, **Dia is used only as an I/O Gateway** for file-based signal ingestion.

Dia is **not** exposed as an Application Data Store. If explicit durable file I/O becomes a requirement for Hub Applications in the future, this could be reconsidered.

---

### Q: How do I choose between Ganymede, Callisto, and Europa?

These are **recommendations**, not requirements. Developers should exercise their discretion based on their specific needs.

| Question | Typical Choice |
|----------|----------------|
| Do I need complex relationships and joins? | Ganymede |
| Do I need transactional integrity (ACID)? | Ganymede |
| Do I need fast lookups by key? | Callisto |
| Do I need caching? | Callisto |
| Do I need full-text search? | Europa |
| Do I need time-series analytics? | Europa |

**Developer discretion applies:**
- You may use only one store, or multiple stores
- You may choose a different store than recommended if it fits your needs better
- You are not required to use all three
- Callisto and Europa are optional — only use if your application needs them

---

### Q: Who provisions Application Data Stores?

1. **Process Architects/Developers** define stores in Workbench Definitions
2. **Tenant Admins** provision stores when activating the workbench
3. **Hub** executes DDL and creates collections/indices
4. **Developers** manage schema evolution through versioned DDL migrations

---

### Q: Can I store decisions in Application Data Stores?

**No.** Decisions must be stored in **Enterprise Memory** (for cognitive audit) and are also reflected in **Operations Data** (for operational triaging).

Storing decisions in Application Data Stores bypasses Hub's cognitive contracts and loses auditability.

---

## 5. Operations Data

### Q: What is Operations Data?

Operations Data is **Hub-managed runtime state** for requests, tasks, activities, and actions. It captures the operational lifecycle of work within Hub.

---

### Q: Can Hub Applications access Operations Data directly?

**No.** Hub Applications do not have direct access to Operations Data stores.

They interact through Hub APIs:
- Request API — read request state, submit updates
- Task API — receive tasks, complete tasks
- Activity API — read activity history

---

### Q: Who writes to Operations Data?

| Writer | What They Write |
|--------|-----------------|
| **Signal Exchange** | Signals, requests, request updates |
| **Request Lifecycle** | Request state transitions |
| **I/O Gateways** | Incoming signals |
| **Hub native subsystems** | Tasks, activities, actions, sessions |

**Hub Applications contribute only through Request updates** (async or inline via Signal Exchange).

---

### Q: Decisions appear in Operations Data AND Enterprise Memory. What's the difference?

| Aspect | Operations Data | Enterprise Memory |
|--------|-----------------|-------------------|
| **Purpose** | Operational triaging, issue resolution | Cognitive record, institutional learning |
| **Content** | Decision occurred, outcome, timestamp | Why decided, evidence, rationale, context |
| **Retention** | Operational (shorter) | Governed (longer) |
| **Governance** | Operational policies | CAF-managed |

Both are written via Request updates — Hub routes to both stores.

---

## 6. Cognitive Audit Fabric (CAF)

### Q: What is CAF?

CAF is the **control plane for Memory Services**. It is **not a storage layer**.

CAF provides:
- Lifecycle management for memory stores
- Contracts and schemas for memory operations
- Catalog of memory stores
- Access enablement and validation
- Decision record schemas
- Evidence bundle packaging
- Explanation generation

---

### Q: Is CAF a database?

**No.** CAF does not store data. It manages how data is stored in Memory Services.

Think of CAF as the "governance layer" for cognitive data — it defines the rules, validates the structure, and provides access control.

---

### Q: How do I record a decision through CAF?

You don't interact with CAF directly. You send a **Decision update** through Signal Exchange:

```json
{
  "update_type": "DECISION",
  "decision_id": "dec-001",
  "outcome": "Approved",
  "rationale": "Policy P-123 criteria met",
  "evidence_bundle_ref": "eb-456"
}
```

Signal Exchange routes this to Enterprise Memory, and CAF validates the structure.

---

## 7. Audit and Observability

### Q: What's the difference between audit and memory?

| Aspect | Cipher Audit Service | Memory Services |
|--------|---------------------|-----------------|
| **Purpose** | Traditional audit trail | Cognitive learning and recall |
| **Question** | Who did what, when? | Why, with what evidence? |
| **Semantics** | Operational logging | Cognitive semantics |
| **Retention** | Compliance-driven | Learning and governance-driven |

Every cognitive action may have a reflection in **both**:
- Audit Service — the action occurred
- Enterprise Memory — the reasoning behind it

---

### Q: Where do application logs go?

Application logs, traces, and metrics go to **Olympus Watch** — the unified observability platform.

This is distinct from:
- Audit Service (who did what)
- Enterprise Memory (why and how)
- Operations Data (request state)

---

### Q: What's the difference between Europa (for analytics) and Watch (for observability)?

| Aspect | Europa | Watch |
|--------|--------|-------|
| **Scope** | Application Data Store | Platform observability |
| **Purpose** | Application-specific search and analytics | Logs, traces, metrics across all services |
| **Owner** | Application (developer chooses to use) | Platform (automatic integration) |
| **Examples** | Search dispute history, entity analytics | Debug logs, request traces, SLO metrics |

---

## 8. Access Patterns and Permissions

### Q: How do Hub Applications read from Memory Services?

Applications read memory for **context assembly**:

1. Request arrives at application
2. Application queries Memory Services for relevant context
3. Memory Service validates access permissions
4. Returns relevant memories for the current context

Applications use Hub-provided SDKs/APIs for memory retrieval.

---

### Q: Can applications read each other's Application Data Stores?

**Not directly.** Application Data Stores are scoped to workbenches.

If cross-workbench data access is needed:
- Use Hub APIs (expose data through a service)
- Use Memory Services (for shared cognitive data)
- Request admin to configure memory store sharing

---

### Q: Who can access what data?

| Data Type | Hub Applications | Developers | Admins | Platform Ops |
|-----------|-----------------|------------|--------|--------------|
| System Data | Read | Read | Read | Read/Write |
| Tenant Spec | Read | Read | Read/Write | Read |
| Operations Data | Via APIs only | Debug | Read | Read |
| Application Data | Read/Write | DDL, Debug | Provision | Support |
| Memory Services | Read, Write via updates | Read | Configure | Support |
| Knowledge Services | Read | Curate | Curate | Support |

---

## 9. Lifecycle and Retention

### Q: What happens when a workbench is deactivated?

1. **Application Data Stores** — data retention policies apply, archives created, resources deallocated
2. **Operations Data** — follows configured retention (active → completed → archived)
3. **Memory Stores** — archived per governance policies
4. **Knowledge Stores** — archived or migrated per admin decision

---

### Q: How long is data retained?

| Data Type | Active | Completed | Archived |
|-----------|--------|-----------|----------|
| **Operations Data** | Until completion | ~90 days (configurable) | ~7 years (configurable) |
| **Application Data** | Workbench lifecycle | Per application policy | Per compliance policy |
| **Enterprise Memory** | Workbench lifecycle | Governed by CAF | Long-term learning |
| **Agent Memory** | Request lifecycle | Discarded | Not archived |

---

### Q: Can I extend retention for specific data?

Yes. Retention is configurable per:
- Tenant
- Workbench
- Data category
- Compliance requirements

Work with your tenant admin to configure appropriate policies.

---

## 10. Common Scenarios

### Q: I need to store a "Transaction Dispute" entity. Where?

**Ganymede** (Application Data Store).

This is a business domain entity with:
- Its own state machine
- Complex attributes
- Relationships to other entities

It's not cognitive data (not a decision or preference), so it doesn't go in Memory Services.

---

### Q: I need to remember that "Customer X prefers email over SMS". Where?

**User Memory** (Memory Services).

This is a learned preference about a user/subject. It should:
- Persist across requests
- Be available for personalization
- Have decay/governance semantics

---

### Q: I decided to approve a refund. Where do I record this?

**Both Enterprise Memory AND Operations Data** — but you don't write directly.

Send a **Decision update** through Signal Exchange:

```json
{
  "update_type": "DECISION",
  "decision_id": "dec-001",
  "outcome": "Refund Approved",
  "rationale": "Customer complaint valid, policy exception granted",
  "evidence_bundle_ref": "eb-456"
}
```

Hub routes this to:
- Enterprise Memory (cognitive record)
- Operations Data (operational log)

---

### Q: I need to cache dispute status for fast UI access. Where?

**Callisto** (Application Data Store).

This is application-specific caching for performance. It's optional — only use if your UI needs sub-millisecond lookups.

---

### Q: I need to search across all disputes by customer name. Where?

**Europa** (Application Data Store).

This is full-text search across business entities. Europa provides:
- Full-text indexing
- Aggregations
- Analytics dashboards

---

### Q: I need to log "Processing started at 10:00". Where?

**Olympus Watch** (Application APM).

This is operational telemetry, not cognitive data or audit. Watch handles:
- Application logs
- Traces
- Metrics

---

### Q: A policy says "Refunds over $500 require manager approval". Where is this stored?

**Knowledge Bank** (Tenant Knowledge Base).

This is curated, authoritative enterprise knowledge. It:
- Is asserted by humans (not learned)
- Applies across scenarios
- Is retrieved (not modified) by applications

---

## Quick Reference

### Where Does It Go?

| Data | Store | Notes |
|------|-------|-------|
| Business entities | Ganymede | *Recommendation — developer discretion* |
| Entity state cache | Callisto | *Recommendation — developer discretion* |
| Search/analytics | Europa | *Recommendation — developer discretion* |
| Policies, SOPs | Knowledge Bank | Required |
| Decisions with rationale | Enterprise Memory | Required |
| User preferences | User Memory | Required |
| Agent session state | Agent Memory | Required |
| Request lifecycle | Operations Data | Hub-managed |
| Logs, traces, metrics | Watch | Required |
| Who did what | Cipher Audit | Hub-managed |

> **Note on Application Data Stores:** The recommendations for Ganymede, Callisto, and Europa are guidelines. Hub Application developers are expected to **exercise their discretion** based on their specific requirements. A developer may choose:
> - To use only Ganymede (no Callisto or Europa)
> - To use Europa for entities instead of Ganymede
> - To skip caching entirely
> - Any combination that fits their application needs
>
> The cognitive stores (Memory Services, Knowledge Services) and Hub-managed stores (Operations Data, Audit) have **required semantics** and must be used as specified.

---

*Last updated: 2026-01-04*

