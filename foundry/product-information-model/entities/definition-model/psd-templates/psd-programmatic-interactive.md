# PSD Template: Programmatic-Interactive Module

**Module Archetype:** Programmatic-Interactive (Synchronous M2M)
**Primary Specification Surfaces:** Extensibility (Dimension 6), Technical (Dimension 5)
**Examples:** REST APIs, GraphQL servers, gRPC endpoints

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
| Module Archetype | Programmatic-Interactive |
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

*Adjust depth based on product archetype: Deep for Developer Platform (usage-based metering), Deep for Enterprise SaaS, Medium for Consumer App.*

**Pricing / Packaging Implications:**

**Value Metric Changes:**
- API call metering changes
- Rate limit tier adjustments

**KPI Impact Projections:**

---

## Section 3: Business Impact — Customer ROI — Dimension 3 [Depth: per product archetype]

*Adjust depth based on product archetype: Deep for Enterprise SaaS (B2B+SLG), Lighter for others.*

**Buyer Persona Implications:**

**Business Outcome Changes:**

**ROI Metric Impact:**

---

## Section 4: User Experience Impact — Dimension 4 [Light]

*Only relevant if this module has an admin console, developer portal, or configuration UI.*

**Affected User Personas:**

**Affected Jobs (JTBD):**
- Which Jobs are accomplished, modified, or newly enabled (if applicable — e.g., developer portal, admin console)

**Affected UX Channels:**
- Which Channels are impacted (if applicable — e.g., Embedded widgets powered by this API, CLI tools, developer portal)

**New / Modified User Journeys:**

**Touchpoint Specifications (Build Track work artifacts):**

*If no UX impact, state: "No impact — this module is a headless API service." Note: if this module powers an Embedded channel (widget/plugin), specify the affected UX Channel and Journeys above.*

---

## Section 5: Technical & Architectural Impact — Dimension 5 [Deep]

*This is a primary specification surface. Be thorough on service architecture, processing logic, and behavioral contracts.*

**New / Modified Subsystems:**

**Key Component Specifications:**
- Service contracts (input/output/error behavior)
- Idempotency guarantees
- Transaction boundaries
- Concurrency handling

**Architecture Decision Records:**

**Performance Requirements:**
- Latency targets (p50, p95, p99)
- Throughput targets (requests/sec)
- Resource bounds (CPU, memory)
- Connection pool sizing

---

## Section 6: Ecosystem & Extensibility Impact — Dimension 6 [Deep]

*This is the primary specification surface for Programmatic-Interactive modules. Be thorough. This section captures the deliberate extensibility surface — the named operations, personas, and contracts that external consumers depend on. Only applicable when this module carries Dim 6 concerns (external-facing extensibility). If this module is purely internal, state: "No Dim 6 impact — this module is not part of the product's external extensibility surface."*

**Affected Developer Personas:**
- Which Developer Personas use this module's API surface
- Impact on their integration workflow (new capabilities, breaking changes, migration effort)

**Affected Programmatic User Personas:**
- Which applications/systems consume this API at runtime
- Impact on their runtime behavior (new integration paths, SLO changes, volume implications)

**New / Modified API Operations:**

*For each operation, specify:*
- Operation name and interaction pattern (Command / Query / Event / Callback / Batch)
- Description of what the operation does
- SLO targets (pattern-appropriate):
  - Command/Query: availability, latency (p50/p95/p99), throughput
  - Event/Callback: delivery guarantee, delivery latency, ordering
  - Batch: processing window, throughput, completeness
- Idempotency: yes/no and mechanism
- Authentication/authorization requirements

**Payload Schema Details (Build Track artifacts):**
- Request schema (field types, required/optional, validation rules)
- Response schema (field types, envelope structure)
- Error response schema (error codes, messages)

*Note: Payload schemas are Build Track work artifacts. Include them here for implementation specification but they are not Definition Model entities.*

**API Compatibility Contract Impact:**
- **Breaking change assessment:** Does this change break existing consumers?
- Versioning strategy (URL path, header, query param)
- Deprecation timeline for affected operations
- Migration guide for consumers
- Performance stability: do SLO targets change from previous version?

**SDK / Integration Module Impact:**
- Which SDK/Library Modules need updates
- Which Integration Modules are affected
- Auto-generation feasibility for SDK changes

---

## Section 7: Operational Impact — Dimension 7 [Medium]

*Load balancing, rate limiting, autoscaling, API gateway configuration.*

**Infrastructure Requirements:**
- New service instances
- API gateway route changes
- Rate limiting configuration

**Security & Compliance Implications:**
- Authentication changes (OAuth, API keys, mTLS)
- Data encryption (in-transit, at-rest)
- Audit logging requirements

**Deployment Strategy:**
- Blue-green / canary for API changes
- Feature flag strategy for gradual rollout

**Monitoring & Alerting:**
- Latency and error rate SLIs
- API availability SLOs
- Consumer-facing status page updates

---

## Section 8: Data & Information Impact — Dimension 9 [Medium]

*Entity mutations, request/response logging, data consistency guarantees.*

**New / Modified Data Entities:**

**Attribute / Field Changes:**

**State Lifecycle Changes:**

**Data Migration Requirements:**

**Data Retention & Archival:**

---

## Section 9: Acceptance Criteria [Required]

**Per-Feature Acceptance Criteria:**
- Feature name: Given... When... Then...

**Cross-Cutting Acceptance Criteria:**
- Performance (latency/throughput):
- Security (auth/authz):
- Backward compatibility:
- Error handling:

**Regression Scope:**

---

## Section 10: Epic Decomposition & Sequencing [Required]

**Proposed Epics:**
- Epic name: Description and scope

**Dependencies & Sequencing:**

**Risks & Open Questions:**
