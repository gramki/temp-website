# 10. Data & Memory Architecture
FFOS relies on governed data domains and multi-tier memories (core memory, graph memory, feature store) to provide deterministic state to agents. Data models enforce lineage, consent tagging, and jurisdictional boundaries. Storage patterns balance append-only audit needs with low-latency access for advisory and execution flows, while lifecycle controls ensure regulatory compliance.

## 10.1 Logical Data Model

### 10.1.1 Family, Member, and Role Entities
Family entity tables capture identifiers, lifecycle status, jurisdiction, and segmentation tags, including links to regulatory KYC master data. Member entities include demographic attributes, identity proofs, role bindings with temporal validity, and references to consent artifacts. Role entities map to permission sets, channel policies, and delegation hierarchies, enabling graph memory to represent historical changes accurately.

### 10.1.2 Accounts, Products, and Obligations
Relational structures link family entities to product holdings (accounts, loans, cards) with ownership fractions, servicing details, integration metadata, and consent tags (view/initiate/approve). Obligation records tie detected commitments to responsible members, schedules, guardrail states, and workflow references for escalations.

### 10.1.3 Events, Documents, and Consents
Event schemas capture source system, normalized type, payload references, correlation IDs, and channel metadata for audit replay. Document entities store metadata, retention rules, and evidence pointers with hash values. Consent tables maintain subject, scope, policy versions, revocation lineage, and linkages to agent invocations that rely on each consent.

## 10.2 Storage, Indexing & Retrieval

### 10.2.1 Transaction & Event Stores
Hybrid storage pattern: append-only event store (e.g., Kafka + immutable datastore) for timelines, paired with query-optimized warehouses for analytics. Indexing ensures low-latency retrieval by household, member, product, obligation, consent event, or workflow ID. Event stores replicate across regions with strict ordering guarantees for compliance replay.

### 10.2.2 Graph Stores for Family Relationships
Native graph database or graph layer within existing data platform stores nodes/edges with versioning and effective dating. Supports traversal queries for oversight mapping, delegation checks, consent propagation, and simulation of future role changes before they go live. Graph memory snapshots feed agent sandboxes for what-if testing.

### 10.2.3 Feature Store Infrastructure
Feature pipelines compute signals using streaming and batch jobs. Registry enforces schema governance, lineage, ownership, refresh cadence, and model explainability. Features are cached close to agents via low-latency stores with consent-aware filtering; stale features are flagged so orchestrators can request recomputation or fallback heuristics.

## 10.3 Data Lifecycle & Retention

### 10.3.1 Retention Policies and Archival
Policies align with regulatory retention (e.g., 7+ years) and bank-specific obligations. Cold data migrates to encrypted archives with recall SLAs for audit and regulator inquiries. Automated classification determines when data can be anonymized vs destroyed, and governance agents must approve exceptions.

### 10.3.2 PII Handling and Minimization
PII tagging at column level drives masking, tokenization, differential access logging, and dynamic redaction. View-layer services expose minimum required attributes per agent and channel, enforcing purpose limitation and just-in-time access tokens.

### 10.3.3 Data Residency and Sovereignty
Deployments honour jurisdictional mandates via segmented storage, encryption keys per region, localized processing pipelines, and cross-border data transfer approvals managed through governance workflows. Telemetry ensures no data plane breaches residency policies.
