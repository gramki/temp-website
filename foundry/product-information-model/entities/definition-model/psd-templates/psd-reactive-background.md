# PSD Template: Reactive / Background Module

**Module Archetype:** Reactive / Background (Asynchronous)
**Primary Specification Surfaces:** Technical (Dimension 5), Operational (Dimension 7), Data (Dimension 9)
**Examples:** Kafka event consumers, nightly ETL jobs, email notification dispatchers

> **TODO:** This template covers the Reactive/Background archetype broadly. Specialize into sub-templates by capability type, as each has distinct specification concerns:
> - **Event-Driven Applications** — real-time event consumers/producers (Kafka, SQS, EventBridge). Focus: event schemas, ordering guarantees, consumer group coordination, backpressure.
> - **Batch / File Applications** — file-based processing (CSV/SFTP ingestion, file generation, bulk imports/exports). Focus: file format contracts, parsing/validation rules, partial failure handling, file delivery SLAs.
> - **Scheduled Jobs** — time-triggered processing (cron, ETL pipelines, data applications). Focus: scheduling cadence, dependency chains, SLA windows, rerun/catch-up semantics.
>
> Each sub-type may warrant different depth in Sections 5–8, different acceptance criteria patterns, and different operational monitoring strategies.

---

## Section 0: Header & Traceability [Required]

| Field | Value |
|---|---|
| PSD ID | |
| Version | |
| Status | Draft / In Review / Approved / Superseded / Cancelled |
| PDR Reference | |
| Source Signals | |
| Target Module | |
| Module Archetype | Reactive / Background |
| Product Archetype | |
| Change Type | New Feature(s) / Feature Refinement / Feature Retirement |
| Author | |
| Related PSDs | |

---

## Section 1: Structural Impact — Dimension 8 [Required]

*The "table of contents" of the change. What is being added, modified, or retired?*

**Module:**

**Capabilities Added:**

**Capabilities Modified:**

**Capabilities Retired:**

**Features Added:**
- Feature name: Description

**Features Modified:**
- Feature name: Delta description

**Features Retired:**
- Feature name: Retirement rationale

**Cross-Module Dependencies:**

---

## Section 2: Vendor Value Impact — Dimension 2 [Depth: per product archetype]

*Background modules often affect cost structures (compute, storage) more than pricing directly.*

**Pricing / Packaging Implications:**

**Value Metric Changes:**

**KPI Impact Projections:**
- Cost impact (compute, storage, data transfer)
- Processing volume projections

---

## Section 3: Business Impact — Customer ROI — Dimension 3 [Depth: per product archetype]

**Buyer Persona Implications:**

**Business Outcome Changes:**

**ROI Metric Impact:**

---

## Section 4: User Experience Impact — Dimension 4 [N/A]

*Reactive/Background modules typically have no direct user interaction.*

*State: "No direct UX impact — this module operates asynchronously without user-facing interfaces." If there is an admin/monitoring dashboard, describe it briefly. If this module's outputs surface in a User Journey (e.g., async notification triggers an Email channel journey, or batch results appear in a Web dashboard), reference the affected Jobs, Channels, and Journeys.*

---

## Section 5: Technical & Architectural Impact — Dimension 5 [Deep]

*This is a primary specification surface. Be thorough on processing pipelines, concurrency, and fault tolerance.*

**New / Modified Subsystems:**

**Key Component Specifications:**
- Processing pipeline design (stages, transformations)
- Concurrency model (parallelism, partitioning)
- Fault tolerance strategy (retry, dead-letter, circuit breaker)
- Idempotency guarantees
- Transaction boundaries and consistency model (eventual vs. strong)
- Batch size and windowing strategy (if applicable)

**Architecture Decision Records:**

**Performance Requirements:**
- Processing throughput (events/sec, records/batch)
- End-to-end latency (from trigger to completion)
- Backpressure handling
- Resource bounds (CPU, memory, disk I/O)

---

## Section 6: Ecosystem & Extensibility Impact — Dimension 6 [Medium]

*Event schemas, topic contracts, message formats.*

**New / Modified Event Topics:**
- Topic name, schema, partitioning strategy

**Payload Schema Changes:**
- Event payload schema (with field types, versioning)
- **Breaking change assessment for downstream consumers**

**Backward Compatibility Plan:**
- Schema evolution strategy (Avro, Protobuf, JSON Schema)
- Consumer migration timeline

**Webhook / Notification Changes:**
- Outbound notification contracts

---

## Section 7: Operational Impact — Dimension 7 [Deep]

*This is a primary specification surface. Be thorough on scheduling, scaling, monitoring, and failure recovery.*

**Infrastructure Requirements:**
- Queue/topic provisioning (Kafka, SQS, RabbitMQ)
- Compute provisioning (container sizing, serverless limits)
- Storage provisioning (temporary and persistent)
- Scheduling configuration (cron expressions, trigger rules)

**Security & Compliance Implications:**
- Data encryption (at-rest, in-transit)
- Access controls for queues/topics
- Audit trail requirements
- Data residency constraints

**Deployment Strategy:**
- Rolling deployment with drain strategy
- Feature flag for new processing logic
- Rollback plan (reprocessing, offset reset)

**Monitoring & Alerting:**
- Queue depth / consumer lag SLIs
- Processing error rate SLIs
- End-to-end latency SLIs
- Dead-letter queue monitoring
- Batch completion SLOs
- Alerting thresholds and escalation

---

## Section 8: Data & Information Impact — Dimension 9 [Deep]

*This is a primary specification surface. Be thorough on data schemas, state machines, and migration.*

**New / Modified Data Entities:**
- Entity name, purpose, cardinality

**Attribute / Field Changes:**
- New fields (with types, constraints, defaults)
- Modified fields (migration impact)
- Removed fields (backward compatibility)

**State Lifecycle Changes:**
- New states and transitions (state machine diagram if complex)
- Guard conditions on transitions
- Side effects triggered by state changes

**Data Migration Requirements:**
- Migration scripts and strategy
- Backfill requirements for existing data
- Rollback plan for migration failures
- Estimated migration duration and downtime

**Data Retention & Archival:**
- Retention policy for processed data
- Archival strategy (cold storage, compression)
- Purge schedule and compliance requirements

---

## Section 9: Acceptance Criteria [Required]

**Per-Feature Acceptance Criteria:**
- Feature name: Given... When... Then...

**Cross-Cutting Acceptance Criteria:**
- Throughput:
- Fault tolerance (failure and recovery):
- Data consistency:
- Idempotency:

**Regression Scope:**

---

## Section 10: Epic Decomposition & Sequencing [Required]

**Proposed Epics:**
- Epic name: Description and scope

**Dependencies & Sequencing:**

**Risks & Open Questions:**
