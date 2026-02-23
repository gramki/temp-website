# PSD (Product Specification Document)

**Model:** Definition Model
**Dimension:** Dimension 1: The Strategy Dimension
**Owner:** Product Management

## Definition

The validated, approved specification that acts as the contract between Product and Engineering. A PSD is **scoped to a single module** and specifies the advancement of that module's capabilities through new features, feature refinements, or feature retirements. A single validated Idea (via its PDR) may produce multiple PSDs — one per substantially affected module.

A PSD is a **cross-dimensional impact assessment** anchored to a structural change (Dimension 8). While the primary specification surface varies by module archetype, every PSD must acknowledge implications across all 9 dimensions — even if some sections state "No impact."

## Purpose

The PSD is the exit artifact of the Strategy Dimension and the entry point for the Build Track. It translates a validated decision (PDR) into a buildable specification with scope, acceptance criteria, and decomposition into Epics. PSD authoring involves scoping modules, writing acceptance criteria, coordinating with engineering, and decomposing into shippable increments — represented by Specification Tasks in the Discovery Track (see FAQ Q5).

**Terminology note:** The UPIM uses "Product Specification Document" (PSD) rather than the more common "Product Requirements Document" (PRD). See FAQ Q8 for the rationale.

**Scoping rule:** A PSD is scoped to one module. If a validated Idea affects multiple modules substantially, each gets its own PSD. Minor ripple effects on adjacent modules may be documented as cross-module dependencies within the primary PSD rather than warranting a standalone PSD. The threshold: does the module change require its own acceptance criteria and Epic decomposition? If yes, it gets its own PSD. See FAQ Q9.

**Templates:** PSD templates are provided per module archetype (Human-Interactive, Programmatic-Interactive, Reactive/Background). The module archetype determines which dimensional sections are deep vs. light. See `psd-templates/` directory.

## Fields

### Section 0: Header & Traceability

| Field | Type | Description |
|---|---|---|
| PSD ID | String | Unique identifier (e.g., PSD-042) |
| Version | Semver | Document revision (e.g., 1.0, 1.1) |
| Status | Enum | Current document status (see Statuses below) |
| PDR Reference | Reference | The Product Decision Record that justifies this PSD |
| Source Signals | List of References | The Signal(s) — Problem(s), Need(s), or Opportunity(ies) — that originated this work |
| Target Module | Reference (Dim 8) | The Module being changed |
| Module Archetype | Enum | Human-Interactive / Programmatic-Interactive / Reactive-Background |
| Product Archetype | String | e.g., B2B + SaaS + SLG |
| Change Type | Enum | New Feature(s) / Feature Refinement / Feature Retirement |
| Author | Reference | The PM or team authoring the PSD |
| Related PSDs | List of References | Sibling PSDs from the same PDR (for cross-module coordination) |

### Section 1: Structural Impact (Dimension 8 — Bridge)

Always required. The "table of contents" of the change.

| Field | Type | Description |
|---|---|---|
| Module | Reference (Dim 8) | The Module being changed |
| Capabilities Added | List | New Capabilities introduced |
| Capabilities Modified | List | Existing Capabilities being refined |
| Capabilities Retired | List | Capabilities being removed |
| Features Added | List | New Features introduced, each with a brief description |
| Features Modified | List | Existing Features being refined, with delta description |
| Features Retired | List | Features being removed, with retirement rationale |
| Cross-Module Dependencies | List of References | Other Modules affected, with nature of dependency |

### Section 2: Vendor Value Impact (Dimension 2)

| Field | Type | Description |
|---|---|---|
| Win Outcome Implications | Text | Which Win Outcomes (per AAARRR stage, per segment) does this change affect? Does it enable a new Win Outcome or strengthen an existing one? |
| Win Stakeholder Impact | Text | Which Win Stakeholders are affected? Does this change their workflow, tools, or concerns? (e.g., Pre-Sales Engineer gets new demo capability; Implementation Consultant gets self-service onboarding) |
| Delivery Friction Impact | Text | Does this change mitigate any known Delivery Frictions? Which Win Stakeholders benefit? |
| Pricing / Packaging Implications | Text | Which Pricing Tiers include the new features? Is a new tier needed? Does the Value Metric change? |
| Business KPI Impact | Text | Expected effect on vendor Business KPIs — Revenue, Cost, and Activity. Include AAARRR stage context. |
| Win Barrier Impact | Text | Does this change mitigate any known Win Barriers? |

*Depth by product archetype: Deep for Enterprise SaaS (complex pricing, multi-stakeholder AAARRR), Deep for Developer Platform (usage-based, self-serve activation), Medium for Consumer App.*

### Section 3: Customer Value Impact (Dimension 3)

| Field | Type | Description |
|---|---|---|
| Pain Implications | Text | Which user Pains (Dim 3) does this change address or relieve? Reference specific Pains and the User Personas (Dim 4) who endure them. Pain is the visceral urgency that motivates purchase — lead with it. |
| Buying Persona Implications | Text | Does this change which roles care about the product? Consider all role types: Economic Buyer, Technical Buyer, User Buyer, Coach/Champion. |
| Business Outcome Changes | Text | New or strengthened buyer outcomes |
| Customer Promise Implications | Text | New or changed Value Propositions, Service Commitments, or Compliance Posture? |
| Customer Value Metric Impact | Text | Changes to metric targets or SLA thresholds (ROI, Service Level, Compliance) |
| Adoption Barrier Impact | Text | Does this change mitigate any known Adoption Barriers? |

*Depth by product archetype: Deep for Enterprise SaaS (ROI justification is the sales engine), Lighter for Developer Platform and Consumer App.*

### Section 4: User Experience Impact (Dimension 4)

| Field | Type | Description |
|---|---|---|
| Affected User Personas | List of References (Dim 4) | Personas impacted by the change |
| New / Modified User Journeys | List with flow descriptions | End-to-end paths added or changed |
| Touchpoint Specifications | Attachments / descriptions | Wireframes, interaction flows, UI copy |
| Accessibility Considerations | Text | WCAG compliance, assistive technology impact |

*Depth by module archetype: **Deep** for Human-Interactive, Light for Programmatic-Interactive, N/A for Reactive/Background.*

### Section 5: Technical & Architectural Impact (Dimension 5)

| Field | Type | Description |
|---|---|---|
| New / Modified Systems | List of References (Dim 5) | Systems added or changed (see `dim5-system.md`) |
| Key Component Specifications | Text | Behavioral contracts for critical components |
| Architecture Decision Records | List of References | ADRs for significant technical choices |
| Performance Requirements | Text | Latency, throughput, resource bounds |

*Depth by module archetype: Medium for Human-Interactive, **Deep** for Programmatic-Interactive, **Deep** for Reactive/Background.*

### Section 6: Ecosystem & Extensibility Impact (Dimension 6)

| Field | Type | Description |
|---|---|---|
| New / Modified API Operations | List of References (Dim 6) | API Operations (Command, Query, Event, Callback, Batch) added or changed; SLO targets |
| API Contract Changes | Text | Contract diffs (request/response semantics, SLO changes), breaking-change assessment. Payload schema details are Build Track artifacts. |
| Backward Compatibility Plan | Text | Versioning strategy, deprecation timeline |
| Webhook / Event Contract Changes | Text | New events, modified payloads, removed events |

*Depth by module archetype: Light for Human-Interactive, **Deep** for Programmatic-Interactive, Medium for Reactive/Background.*

### Section 7: Operational Impact (Dimension 7)

| Field | Type | Description |
|---|---|---|
| Infrastructure Requirements | Text | New services, scaling needs, resource estimates |
| Security & Compliance Implications | Text | PCI, SOC2, GDPR, data residency |
| Deployment Strategy | Text | Feature flags, canary, blue-green |
| Monitoring & Alerting | Text | New SLIs/SLOs, dashboards, alert rules |
| Operations Decision Records | List of References | ODRs for significant operational choices (see `dim7-odr.md`) |

*Depth by module archetype: Light for Human-Interactive, Medium for Programmatic-Interactive, **Deep** for Reactive/Background.*

### Section 8: Data & Information Impact (Dimension 9)

| Field | Type | Description |
|---|---|---|
| New / Modified Data Entities | List of References (Dim 9) | Entities added or changed |
| Attribute / Field Changes | Text | New fields, modified types, removed fields |
| State Lifecycle Changes | Text | New states, new transitions |
| Data Migration Requirements | Text | Migration scripts, backfill strategy |
| Data Retention & Archival | Text | Retention policy, archival implications |

*Depth by module archetype: Medium for Human-Interactive, Medium for Programmatic-Interactive, **Deep** for Reactive/Background.*

### Section 9: Acceptance Criteria

| Field | Type | Description |
|---|---|---|
| Per-Feature Acceptance Criteria | List | Tied to each Feature in Section 1 |
| Cross-Cutting Acceptance Criteria | List | Performance, security, compatibility requirements |
| Regression Scope | Text | Existing behavior that must not break |

### Section 10: Epic Decomposition & Sequencing

| Field | Type | Description |
|---|---|---|
| Proposed Epics | List of References (Track 2) | The Build Track entry points |
| Dependencies & Sequencing | Text | Order constraints, blocking dependencies |
| Risks & Open Questions | List | Unresolved items to address during Build |

## Statuses

| Status | Description |
|---|---|
| Draft | PSD is being authored (Specification Tasks in progress) |
| In Review | PSD is under review by Engineering and stakeholders |
| Approved | PSD is accepted as the contract — ready for Build Track |
| Superseded | PSD has been replaced by a newer version |
| Cancelled | PSD has been abandoned (e.g., PDR was revised to Kill) |

## Relationships

| Direction | Related Entity | Relationship |
|---|---|---|
| Upstream | Product Decision Record (Dim 1) | PSD references PDR as its justification |
| Scoped to | Module / Domain (Dim 8) | PSD is scoped to a single Module |
| Specifies | Capability (Dim 8) | PSD adds, modifies, or retires Capabilities |
| Specifies | Feature (Dim 8) | PSD adds, modifies, or retires Features |
| Downstream | Epic (Track 2) | PSD decomposes into Epics in the Build Track |
| Sibling | PSD (Dim 1) | Related PSDs from the same PDR (cross-module coordination) |
| Work Model | Specification Task (Track 1) | Specification Tasks represent the work of authoring this PSD |

## Change Type Behavior

| Section | New Feature | Refinement | Retirement |
|---|---|---|---|
| Structural (Dim 8) | Full spec of new M/C/F | Delta description | Removal plan + timeline |
| Business (Dims 2–3) | Full pricing/ROI analysis | Impact delta | Revenue impact, customer notification |
| UX (Dim 4) | Full journey/touchpoint design | Modified flows only | Migration UX, sunset communication |
| Technical (Dim 5) | Full architecture spec | Targeted changes | Deprecation plan, dead code removal |
| Extensibility (Dim 6) | Full API contract | Versioning strategy | Sunset schedule, migration guide |
| Operational (Dim 7) | Full infra requirements | Delta requirements | Decommissioning plan |
| Data (Dim 9) | Full entity/schema design | Migration plan | Data archival/deletion policy |

## Example

PSD-042: "Real-Time FX Rate Lock — Invoice & Payout Processing Module" (Human-Interactive, Feature Addition). Sibling PSD: PSD-043 covering the FX Microservice module (Programmatic-Interactive).
