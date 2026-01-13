# ADR-0108: Seer UX Architecture Detailed Design

**Status**: Accepted  
**Date**: 2026-01-13  
**Category**: ux-architecture

---

## Context

Seer's UX architecture documentation existed as an overview with directional guidance, but lacked the detailed specifications needed for implementation. Key gaps included:

1. **Incomplete desk documentation** — Desks were identified but console specifications were missing
2. **Unclear REST channel architecture** — No definition of how Seer channels relate to Hub channels
3. **Inconsistent autonomy terminology** — Different naming schemes used across documents
4. **Missing journey documentation** — No end-to-end workflows showing how personas accomplish their goals
5. **Persona needs gaps** — Complex needs not adequately documented for new developers/PMs

Additionally, Seer needed to:
- Align with Hub's desk-based UX organization pattern
- Ensure OPDA (Observable, Predictable, Directable, Authority Enforceable) capabilities are integrated throughout
- Support full lifecycle coverage for Agent Engineers (AE) and Cognitive Systems Architects (CSA)
- Enable all personas to accomplish their needs via their desks

---

## Decision

We established a comprehensive UX architecture for Seer with the following architectural decisions:

### 1. Desk-Based Organization with Common Consoles

**Seer follows Hub's desk-based organization pattern:**

- **7 persona desks**, each with 3 specialized consoles
- **Common consoles** for shared functionality across multiple personas
- **Desk structure**: `desks/{desk-name}/` with README + console specifications

| Desk | Persona | Consoles |
|------|---------|----------|
| Agent Portfolio Desk | APO | Portfolio, Outcomes, Autonomy |
| Agent Design Desk | CSA | Design, Topology, Validation |
| Agent Development Desk | AE | Development, Test, Release |
| Knowledge Governance Desk | KMO | Knowledge, Memory, Learning |
| Agent Operations Desk | ARE | Health, Control, Incident |
| Cognitive Health Desk | COS | Behavior, Patterns, Issues |
| Agent Compliance Desk | ARAO | Autonomy, Compliance, Security |

**Common Consoles:**
- Agent Behavior Console (shared by COS, ARE, AE with persona-specific views)
- Additional common consoles identified as needed (Agent Catalog, Alert Console)

**Rationale:**
- Consistency with Hub UX architecture (ADR-0082)
- Clear persona ownership and responsibility
- Reusable components reduce duplication
- Permission model supports persona-specific views

### 2. Hybrid REST Channel Architecture

**Seer uses a hybrid approach for REST channels:**

| Channel Type | Personas | Pattern |
|--------------|----------|---------|
| **Hub-Extended** | APO, KMO, ARE | Extend existing Hub channels (e.g., `/api/creator/v1` with Seer extensions) |
| **Seer-Native** | CSA, AE, COS, ARAO | New Seer-specific channels (e.g., `/api/seer/csa/v1`) |

**Key Principles:**
- All console capabilities available via REST APIs
- Same APIs exposed via MCP channels for AI assistant access
- Persona-scoped channels (not function-scoped)
- Authentication and authorization via Heracles Gateway

**Rationale:**
- Leverages existing Hub infrastructure where appropriate
- New channels only where Seer-specific needs exist
- Consistent API access model (REST + MCP)
- Aligns with ADR-0011 (persona-scoped API channels)

### 3. Autonomy Level Standardization

**Seer standardizes on 5-level autonomy scale (L0-L4):**

| Level | Name | Description | Human Role |
|-------|------|-------------|------------|
| L0 | Manual | Human executes, AI advises | Executor |
| L1 | Assisted | AI proposes, human decides | Decision-maker |
| L2 | Supervised | AI executes, human reviews | Reviewer |
| L3 | Bounded Autonomous | AI autonomous within rules | Exception Handler |
| L4 | Fully Autonomous | AI autonomous, audit only | Auditor |

**Rationale:**
- Clear progression from manual to fully autonomous
- Consistent terminology across all desks and consoles
- Supports autonomy level upgrade journey
- Enables ARAO approval workflows

### 4. Common Consoles Pattern

**Shared consoles documented in `common-consoles/` folder:**

- **Agent Behavior Console** — Primary shared console for behavioral observation
  - Persona-specific views: COS (cognitive health), ARE (operational health), AE (development debugging)
  - Detail-level filtering (summary → detailed → trace)
  - Permission-based access control

**Rationale:**
- Reduces duplication across desks
- Ensures consistent behavioral observation capabilities
- Supports multiple personas viewing same data with different lenses
- Permission model enables appropriate access control

### 5. Critical Journeys Documentation

**8 critical journeys documented covering Development, Administration, and Evolution:**

1. New Agent Development
2. Production Deployment
3. Agent Incident Response
4. Agent Evolution from Feedback
5. Autonomy Level Upgrade
6. Behavioral Drift Investigation
7. Enterprise Learning Promotion
8. Compliance Audit

**Each journey includes:**
- Step-by-step workflow with persona responsibilities
- Desks and consoles used at each step
- Decision points and gates
- OPDA checkpoints
- Integration with Hub journeys where applicable

**Rationale:**
- Demonstrates how desks enable end-to-end workflows
- Covers full lifecycle (development → operations → evolution)
- Shows cross-persona collaboration
- Provides implementation guidance

### 6. Persona Needs Documentation Structure

**Dedicated need pages for complex requirements:**

- Created when needs require explanation for new developers/PMs
- Linked from persona reference files
- Inline documentation for self-explanatory needs

**Rationale:**
- Supports onboarding of new team members
- Provides detailed context for complex needs
- Maintains clean persona reference files
- Enables focused documentation

### 7. OPDA Integration Throughout

**Every desk and console includes OPDA contribution:**

- **Observable** — Metrics, logs, traces, dashboards
- **Predictable** — Forecasting, trend analysis, behavior baselines
- **Directable** — Control levers, configuration changes, interventions
- **Authority Enforceable** — Approval workflows, policy enforcement, audit trails

**Rationale:**
- Ensures Seer agents meet enterprise requirements
- Enables stakeholders to action, assess, and evidence OPDA properties
- Supports governance and compliance needs
- Provides foundation for trust and safety

---

## Consequences

### Positive

1. **Comprehensive documentation** — 53 files created covering all aspects of UX architecture
2. **Consistency with Hub** — Aligns with established Hub patterns (ADR-0082, ADR-0085)
3. **Clear implementation path** — Detailed specifications enable development teams to build
4. **Full lifecycle coverage** — AE and CSA desks cover feedback → design → implementation → evolution
5. **OPDA foundation** — Every desk demonstrates how it supports Observable, Predictable, Directable, Authority Enforceable
6. **Journey-driven design** — 8 critical journeys show how personas accomplish their goals
7. **Reusable components** — Common consoles reduce duplication and ensure consistency

### Negative

1. **Documentation maintenance** — Large documentation set requires ongoing updates
2. **Initial learning curve** — New team members need to understand desk/console structure
3. **REST channel complexity** — Hybrid approach requires understanding both Hub and Seer channels
4. **Journey documentation** — Must be kept in sync with desk capabilities as they evolve

### Neutral

1. **Structure mirrors Hub** — Familiar to Hub users, but requires Hub knowledge
2. **Common consoles** — Additional abstraction layer, but reduces duplication
3. **Autonomy levels** — Standardization may need refinement based on real-world usage

---

## Alternatives Considered

### 1. Function-Based Organization

Organize by function (development, operations, compliance) rather than persona.

**Rejected because:**
- Personas have overlapping needs across functions
- Hub uses persona-based organization (ADR-0082)
- Persona ownership is clearer with desk-based approach

### 2. All Seer-Native REST Channels

Create new REST channels for all personas, even those that could extend Hub.

**Rejected because:**
- Unnecessary duplication of Hub infrastructure
- Inconsistent with Hub's channel architecture
- More maintenance overhead

### 3. Autonomy Levels as Named Categories

Use descriptive names (Full, Suggest, Ask, Watch) instead of L0-L4.

**Rejected because:**
- L0-L4 provides clear progression and ordering
- Easier to reference in documentation and code
- Supports autonomy level upgrade journey more clearly

### 4. No Common Consoles

Duplicate console functionality in each desk that needs it.

**Rejected because:**
- Significant duplication across desks
- Inconsistent implementations likely
- Harder to maintain and evolve

---

## Documents Created

### Desk Documentation (28 files)
- 7 desk README files
- 21 console specification files

### Common Consoles (2 files)
- `common-consoles/README.md`
- `common-consoles/agent-behavior-console.md`

### REST Channels (8 files)
- `rest-channels/README.md`
- 7 persona-specific channel documents

### Critical Journeys (8 files)
- 8 journey documents in `personas-and-needs/journeys/`

### Persona Needs (7 files)
- 7 dedicated need pages in `personas-and-needs/needs/`

**Total: 53 new files, 9,427 lines added**

---

## Related

- [ADR-0082: Hub Desk Restructuring](./0082-hub-desk-restructuring.md)
- [ADR-0085: Seer Desk Naming Convention](./0085-seer-desk-naming-convention.md)
- [ADR-0011: Persona-Scoped API Channels](./0011-persona-scoped-api-channels.md)
- [Seer UX Architecture README](../../olympus-seer-docs/seer-design/ux-architecture/README.md)
- [Seer Desk Requirements](../../olympus-seer-docs/seer-design/ux-architecture/desk-requirements.md)
- [Hub UX Architecture](../../olympus-hub-docs/06-ux-architecture/README.md)
