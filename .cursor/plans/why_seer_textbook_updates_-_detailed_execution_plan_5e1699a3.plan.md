---
name: Why Seer Textbook Updates - Detailed Execution Plan
overview: Execute the writing plan to add 3 critical gaps (Request-Scoped Delegation, Agent Identity Model, MCP Server CRD) and 5 enhancements to the Why Seer? textbook, plus update front matter and appendices. All work follows the 7-part structural contract and textbook writing methodology.
todos:
  - id: task-1-2
    content: Update Agent Identity (Section 8.1) - Expand to explain two-layer identity model (Deployment Identity vs Agent Persona), SPIFFE ID as OAuth Client analogy, token structure
    status: completed
  - id: task-1-3
    content: Update Delegation Chains (Section 8.2) - Update to reflect persona-based delegation, clarify delegation chains track Agent Persona not SPIFFE ID
    status: completed
    dependencies:
      - task-1-2
  - id: task-1-1
    content: Create Request-Scoped Authority Delegation (Section 8.6) - New section explaining business user delegation model, OAuth 2.0-inspired flows, Delegation Templates/Certificates/Tokens
    status: completed
    dependencies:
      - task-1-2
      - task-1-3
  - id: task-1-4
    content: Add Sub-Persona Note to Hub Composite Applications (Section 22.1) - Explain that each agent in composite gets its own sub-persona
    status: completed
    dependencies:
      - task-1-2
  - id: task-1-5
    content: Create MCP Server CRD Design (Section 23.4) - New section explaining multiple MCP Servers per workbench, template-based persona inference, OPA access control
    status: completed
  - id: task-2-1
    content: Enhance Composite Routing (Section 22.3) - Add routing table schema details, OPA filter compilation, backward compatibility explanation
    status: completed
  - id: task-2-2
    content: Add Composite Application Requirement (Section 5.9) - Add note about composite application requirements with cross-reference to Section 22
    status: completed
  - id: task-2-3
    content: Cross-Reference Validation - Review all cross-references in updated sections, verify Section 8.6 and 23.4 references resolve, update outline document
    status: completed
    dependencies:
      - task-1-1
      - task-1-2
      - task-1-3
      - task-1-4
      - task-1-5
      - task-2-1
      - task-2-2
  - id: task-3-1
    content: Enhance Request Sentinel Details (Section 19.1) - Add enrollment mechanism, scenario filters, child request creation flow, webhook notifications
    status: completed
  - id: task-3-2
    content: Enhance COGW Details (Section 19.5) - Add COGW architecture, signal forwarding mechanism, read-only sync process, operator responsibilities
    status: completed
  - id: task-3-3
    content: Enhance Persona Twin Blueprint Details (Section 21.2) - Add blueprint structure details, signal/filter/schedule suggestions, extension model explanation
    status: completed
  - id: task-4-1
    content: Update Table of Contents - Add Section 3.6, Sections 19-24, Section 23.4
    status: completed
    dependencies:
      - task-1-1
      - task-1-5
      - task-2-3
  - id: task-4-2
    content: Update How to Use This Book - Update Part 2 table with Section 3.6 and Sections 19-24
    status: completed
    dependencies:
      - task-1-1
      - task-1-5
  - id: task-4-3
    content: Update Glossary - Add 15+ new terms (Request-Scoped Delegation, Agent Persona, MCP Server, COGW, Persona Twin Blueprint, etc.)
    status: completed
    dependencies:
      - task-1-1
      - task-1-2
      - task-1-5
      - task-3-2
      - task-3-3
  - id: task-4-4
    content: Review Appendix B - Verify responsibility matrix for new capabilities (MCP Server, Request-Scoped Delegation, COGW, Persona Twins)
    status: completed
  - id: task-4-5
    content: Review Appendix D - Add new ADR references (0127, 0129, 0130, 0131, 0132, 0134, 0126, 0125)
    status: completed
  - id: task-5-1
    content: Comprehensive Editorial Review - Review entire textbook for consistency, quality, terminology, cross-references, and structural adherence
    status: completed
    dependencies:
      - task-1-1
      - task-1-2
      - task-1-3
      - task-1-4
      - task-1-5
      - task-2-1
      - task-2-2
      - task-2-3
      - task-3-1
      - task-3-2
      - task-3-3
      - task-4-1
      - task-4-2
      - task-4-3
      - task-4-4
      - task-4-5
---

# Why Seer? Textbook Updates - Detailed Execution Plan

## Overview

This plan executes the writing tasks identified in `writing-plan-2026-01-17.md` to address 3 critical gaps and 5 enhancement opportunities in the Why Seer? textbook, plus updates to front matter and appendices. All writing follows the 7-part structural contract and textbook methodology defined in `why-seer-textbook-prompt.md`.

**Phases:**

- **Phase 1:** Critical gaps (5 tasks) — COMPLETED
- **Phase 2:** Enhancements (3 tasks) — COMPLETED
- **Phase 3:** Optional enhancements (3 tasks) — COMPLETED
- **Phase 4:** Front matter & appendices (5 tasks) — PENDING
- **Phase 5:** Comprehensive editorial review (1 task) — PENDING

## Phase 1: Critical Gaps (High Priority)

### Task 1.1: Request-Scoped Authority Delegation (Section 8.6)

**File to Create:** `olympus-seer-docs/why-seer/part-2-how-seer-solves/03-identity-authority-in-seer/03-6-request-scoped-delegation.md`

**Context Rehydration:**

- Read `olympus-hub-docs/decision-logs/0127-request-scoped-authority-delegation.md`
- Read `olympus-seer-docs/seer-design/implementation-concepts/request-scoped-delegation.md`
- Review existing Section 8.1-8.5 for terminology consistency
- Review Section 8.2 (Delegation Chains) to understand enterprise delegation context

**7-Part Structure:**

1. **Purpose:** Explain how business users (customers, end-users) delegate authority to agents, distinct from enterprise delegation
2. **Core Concepts:** Two identity domains (Enterprise vs Request-Scoped), OAuth 2.0-inspired model, Delegation Template, Delegation Certificate, Delegation Access Token
3. **Conceptual Models:** OAuth 2.0 mapping table, delegation flow diagrams (Proactive, Reactive, Implicit, Cascading), policy composition model
4. **Enterprise Considerations:** Channel dependency, business user identity federation, consent capture, token lifecycle, policy composition (AND logic)
5. **Misconceptions:** Confusing with enterprise delegation, assuming Channels and Signal Providers are equivalent, thinking tokens are long-lived
6. **Practical Implications:** When to use request-scoped vs enterprise delegation, channel requirements, reactive delegation latency trade-offs
7. **Cross-References:** Section 8.2 (Delegation Chains), Section 8.5 (Cipher IAM), Section 23 (Collaboration Channels)

**Key Content:**

- Two orthogonal identity domains explanation
- OAuth 2.0 analogy (Client=Employed Agent, Resource Owner=Business User, etc.)
- Four delegation flows with examples
- Policy composition requiring ALL policies to ALLOW
- Channel-only facilitation (not Signal Providers)

**References to Include:**

- `olympus-hub-docs/decision-logs/0127-request-scoped-authority-delegation.md`
- `olympus-seer-docs/seer-design/implementation-concepts/request-scoped-delegation.md`
- OAuth 2.0 RFC 6749 (external reference)

**Editor Mode Checklist:**

- [ ] Terminology matches Section 8.1-8.5
- [ ] Clear distinction from enterprise delegation
- [ ] All cross-references resolve
- [ ] No marketing language

---

### Task 1.2: Update Agent Identity (Section 8.1)

**File to Update:** `olympus-seer-docs/why-seer/part-2-how-seer-solves/03-identity-authority-in-seer/03-1-agent-identity.md`

**Context Rehydration:**

- Read `olympus-hub-docs/decision-logs/0129-agent-identity-model.md`
- Read `olympus-hub-docs/decision-logs/0130-unified-delegation-model.md`
- Review current Section 8.1 content
- Review Section 8.2 for delegation context

**Enhancement Needed:**

- Expand to explain two-layer identity model
- Add SPIFFE ID as OAuth Client analogy
- Explain Deployment Identity (infrastructure layer) vs Agent Persona (business layer)
- Add token structure explanation
- Explain one deployment/multiple personas and one persona/multiple deployments

**Key Additions:**

- Two-layer identity model diagram
- SPIFFE ID = OAuth Client explanation
- Agent Persona = Business Identity explanation
- Token structure with both identities
- Use case table (mTLS uses Deployment Identity, Access Tokens use Agent Persona, etc.)

**Editor Mode Checklist:**

- [ ] Two-layer model clearly explained
- [ ] Terminology consistent with Section 8.6 (when written)
- [ ] OAuth analogy accurate
- [ ] Use cases clear

---

### Task 1.3: Update Delegation Chains (Section 8.2)

**File to Update:** `olympus-seer-docs/why-seer/part-2-how-seer-solves/03-identity-authority-in-seer/03-2-delegation-chains.md`

**Context Rehydration:**

- Read `olympus-hub-docs/decision-logs/0129-agent-identity-model.md`
- Review current Section 8.2 content
- Review Section 8.1 (after update) for identity context

**Enhancement Needed:**

- Update to reflect persona-based delegation (not just deployment identity)
- Clarify that delegation chains track Agent Persona, not SPIFFE ID
- Add note about composite application sub-personas

**Key Updates:**

- Delegation chains use Agent Persona (business identity)
- Audit logs attribute to personas
- Composite applications create sub-personas

**Editor Mode Checklist:**

- [ ] Consistent with Section 8.1 updates
- [ ] Clear persona vs deployment distinction
- [ ] Cross-references to Section 8.6 accurate

---

### Task 1.4: Add Sub-Persona Note to Hub Composite Applications (Section 22.1)

**File to Update:** `olympus-seer-docs/why-seer/part-2-how-seer-solves/22-multi-agent-topologies-in-hub/22-1-hub-composite-applications.md`

**Context Rehydration:**

- Read `olympus-hub-docs/decision-logs/0129-agent-identity-model.md` (composite section)
- Review current Section 22.1 content

**Enhancement Needed:**

- Add subsection or paragraph explaining that each agent in a composite gets its own sub-persona
- Explain sub-personas derive from same base Agent Persona but have distinct identity

**Key Addition:**

- Sub-persona concept for composite applications
- Example showing multiple sub-personas from one scenario

**Editor Mode Checklist:**

- [ ] Consistent with Section 8.1 identity model
- [ ] Clear and concise addition

---

### Task 1.5: MCP Server CRD Design (Section 23.4)

**File to Create:** `olympus-seer-docs/why-seer/part-2-how-seer-solves/23-collaboration-channels-in-hub/23-4-mcp-server-crd.md`

**Context Rehydration:**

- Read `olympus-hub-docs/decision-logs/0131-mcp-server-crd-design.md`
- Read `olympus-hub-docs/decision-logs/0132-mcp-template-kinds.md`
- Read `olympus-hub-docs/decision-logs/0134-mcp-directory-service.md`
- Read `olympus-hub-docs/04-subsystems/mcp-channel/mcp-server-crd.md`
- Review Section 23.3 (Multi-Channel Access) for context
- Review Section 6.9 (Persona-Specific Desks) for persona context

**7-Part Structure:**

1. **Purpose:** Explain how MCP Servers enable multiple collaboration endpoints per workbench with persona-based access control
2. **Core Concepts:** MCP Server CRD, template kind, persona inference, OPA access control, MCP Directory Service
3. **Conceptual Models:** CRD structure, template kind → persona mapping, access control flow
4. **Enterprise Considerations:** Multiple servers for functional/privilege boundaries, OPA policy management, discovery via directory service
5. **Misconceptions:** Thinking one server per workbench, confusing template kind with explicit persona field, assuming all scenarios exposed
6. **Practical Implications:** When to create multiple servers, template kind selection, OPA policy design
7. **Cross-References:** Section 23.3 (Multi-Channel Access), Section 6.9 (Persona-Specific Desks), Section 8 (Identity & Authority)

**Key Content:**

- Multiple MCP Servers per workbench capability
- Template kind implies persona (no explicit persona field)
- Scenarios automatically include requests
- OPA-based access control structure
- MCP Directory Service for discovery

**References to Include:**

- `olympus-hub-docs/decision-logs/0131-mcp-server-crd-design.md`
- `olympus-hub-docs/decision-logs/0132-mcp-template-kinds.md`
- `olympus-hub-docs/decision-logs/0134-mcp-directory-service.md`
- `olympus-hub-docs/04-subsystems/mcp-channel/mcp-server-crd.md`

**Editor Mode Checklist:**

- [ ] Template kind concept clearly explained
- [ ] OPA access control structure clear
- [ ] Consistent with Section 23.3
- [ ] No marketing language

---

## Phase 2: Enhancements (Medium Priority)

### Task 2.1: Enhance Composite Routing (Section 22.3)

**File to Update:** `olympus-seer-docs/why-seer/part-2-how-seer-solves/22-multi-agent-topologies-in-hub/22-3-deployment-model.md`

**Context Rehydration:**

- Read `olympus-hub-docs/decision-logs/0126-composite-routing-table-schema.md`
- Read `olympus-hub-docs/04-subsystems/signal-exchange/application-router.md`
- Review current Section 22.3 content

**Enhancement Needed:**

- Add subsection on routing table schema
- Explain OPA filter compilation and caching
- Emphasize backward compatibility with single-app scenarios
- Explain routing logic (applications array vs application field)

**Key Addition:**

- Routing table schema explanation
- OPA filter storage and compilation
- Backward compatibility guarantee

**Editor Mode Checklist:**

- [ ] Technical detail appropriate for audience
- [ ] Consistent with Section 22.1 and 22.2
- [ ] Backward compatibility clear

---

### Task 2.2: Add Composite Application Requirement (Section 5.9)

**File to Update:** `olympus-seer-docs/why-seer/part-2-how-seer-solves/part-1-background/05-building-enterprise-agent/05-9-multi-agent-coordination.md`

**Context Rehydration:**

- Read `olympus-hub-docs/decision-logs/0125-hub-composite-applications.md`
- Review current Section 5.9 content
- Review Section 5.14 (Multi-Agent Topology Requirements) for context

**Enhancement Needed:**

- Add note about composite application requirements
- Reference Section 22 for solution coverage
- Distinguish from coordination mechanisms (Section 5.9) vs topology patterns (Section 5.14)

**Key Addition:**

- Composite application as enterprise requirement
- Cross-reference to Section 22

**Editor Mode Checklist:**

- [ ] Clear distinction from coordination mechanisms
- [ ] Consistent with Section 5.14
- [ ] Cross-reference accurate

---

### Task 2.3: Cross-Reference Validation

**Files to Review:** All files in `olympus-seer-docs/why-seer/`

**Context Rehydration:**

- Review all cross-references in updated sections
- Verify Section 8.6 references resolve
- Verify Section 23.4 references resolve
- Check Section 8.1, 8.2 updates don't break existing references

**Validation Tasks:**

- [ ] All Section 8.6 cross-references resolve
- [ ] All Section 23.4 cross-references resolve
- [ ] Section 8.1, 8.2 updates don't break existing references
- [ ] Outline document updated if structure changes

**Editor Mode Checklist:**

- [ ] All internal links work
- [ ] All section numbers accurate
- [ ] Outline document reflects changes

---

## Phase 3: Optional Enhancements (Low Priority)

### Task 3.1: Enhance Request Sentinel Details (Section 19.1)

**File to Update:** `olympus-seer-docs/why-seer/part-2-how-seer-solves/19-agent-oversight-monitoring-in-seer/19-1-seer-sentinels.md`

**Context Rehydration:**

- Read `olympus-hub-docs/decision-logs/0116-request-sentinel-type.md`
- Read `olympus-hub-docs/decision-logs/0117-sentinel-scenario-spec-crds.md`
- Review current Section 19.1 content

**Enhancement Needed:**

- Add subsection on Request Sentinel enrollment mechanism
- Explain scenario whitelist/blacklist filters
- Explain OPA filter-based enrollment
- Detail child request creation flow
- Explain webhook notification mechanism

**Key Addition:**

- Enrollment flow diagram
- Filter configuration examples
- Child request creation process

**Editor Mode Checklist:**

- [ ] Enrollment mechanism clearly explained
- [ ] Consistent with existing sentinel content
- [ ] Technical detail appropriate

---

### Task 3.2: Enhance COGW Details (Section 19.5)

**File to Update:** `olympus-seer-docs/why-seer/part-2-how-seer-solves/19-agent-oversight-monitoring-in-seer/19-5-cogw.md`

**Context Rehydration:**

- Read `olympus-hub-docs/decision-logs/0118-cognitive-operations-governance-workbench-type.md`
- Read `olympus-hub-docs/decision-logs/0119-cog-sentinel-cross-workbench-enrollment.md`
- Read `olympus-hub-docs/decision-logs/0120-cogw-operator-subscription-scope.md`
- Review current Section 19.5 content

**Enhancement Needed:**

- Add subsection on COGW architecture
- Explain signal forwarding from target workbenches
- Explain read-only sync of Sentinel specs
- Detail COGW Operator responsibilities

**Key Addition:**

- Signal forwarding mechanism
- Read-only sync process
- Operator responsibilities

**Editor Mode Checklist:**

- [ ] Architecture clearly explained
- [ ] Consistent with existing COGW content
- [ ] Cross-workbench model clear

---

### Task 3.3: Enhance Persona Twin Blueprint Details (Section 21.2)

**File to Update:** `olympus-seer-docs/why-seer/part-2-how-seer-solves/21-persona-twins-in-seer/21-2-persona-twin-lifecycle.md`

**Context Rehydration:**

- Read `olympus-hub-docs/decision-logs/0121-persona-twin-blueprint-structure.md`
- Read `olympus-seer-docs/seer-design/implementation-concepts/persona-twin-blueprint.md`
- Review current Section 21.2 content

**Enhancement Needed:**

- Add subsection on blueprint structure
- Explain signal suggestions, filter suggestions, schedule suggestions
- Explain blueprint as extension to Trained Agent Blueprints (not separate CRD)
- Detail Hub Platform subscription blueprints

**Key Addition:**

- Blueprint structure details
- Extension model explanation
- Platform-provided blueprints

**Editor Mode Checklist:**

- [ ] Blueprint structure clearly explained
- [ ] Extension model clear
- [ ] Consistent with existing Persona Twin content

---

## Execution Methodology

### For Each Task:

1. **Context Rehydration** (Before Writing):

- Read all referenced ADRs and design documents
- Review related sections for terminology consistency
- Identify cross-reference targets

2. **Writing** (Follow 7-Part Structure):

- Purpose of the Chapter
- Core Concepts & Definitions
- Conceptual Models / Frameworks
- Systemic and Enterprise Considerations
- Common Misconceptions & Failure Modes
- Practical Implications
- Cross-References

3. **Editor Mode** (After Writing):

- Conceptual clarity check
- Terminology consistency check
- Structural adherence check
- Redundancy check
- Cross-reference validation
- Update writing plan status

4. **Quality Standards**:

- Long-form prose (not bullet dumps)
- No marketing language
- First-principles reasoning
- Explicit assumptions
- Distinguish facts, design choices, opinions

---

## Dependencies

- Task 1.1 (Section 8.6) depends on Task 1.2 (Section 8.1 update) and Task 1.3 (Section 8.2 update) being completed first
- Task 1.4 (Section 22.1) depends on Task 1.2 (Section 8.1 update)
- Task 2.3 (Cross-Reference Validation) depends on all Phase 1 and Phase 2 tasks
- Task 4.1 (Table of Contents) depends on Task 1.1, Task 1.5, and Task 2.3 (to ensure all sections are complete)
- Task 4.2 (How to Use This Book) depends on Task 1.1 and Task 1.5 (to know what sections exist)
- Task 4.3 (Glossary) depends on all content tasks (Task 1.1, 1.2, 1.5, 3.2, 3.3) to capture all new terms
- Task 4.4 (Appendix B) can be done independently but benefits from content completion
- Task 4.5 (Appendix D) can be done independently but benefits from content completion
- Task 5.1 (Editorial Review) depends on ALL previous tasks being completed

---

## Success Criteria

- All critical gaps filled (3 new sections/updates)
- All enhancements completed (5 updates)
- All cross-references resolve
- Terminology consistent throughout
- 7-part structural contract followed
- No marketing language
- Outline document updated
- Table of Contents complete and accurate
- Glossary includes all new terms
- Front matter reflects current structure
- Appendices include all new ADR references
- Comprehensive editorial review completed
- All quality standards met
- Textbook ready for publication

---

## Phase 4: Front Matter & Appendices Updates (High Priority)

### Task 4.1: Update Table of Contents

**File to Update:** `olympus-seer-docs/why-seer/00-front-matter/00-3-table-of-contents.md`

**Context Rehydration:**

- Review current TOC structure
- List all files in `part-2-how-seer-solves/` to identify missing sections
- Verify section numbering matches actual file structure

**Updates Needed:**

- Add Section 3.6 (Request-Scoped Authority Delegation) under Section 3 (Identity & Authority)
- Add complete Section 19 (Agent Oversight & Monitoring in Seer) with all subsections
- Add complete Section 20 (Developer Experience in Seer) with all subsections
- Add complete Section 21 (Persona Twins in Seer) with all subsections
- Add complete Section 22 (Multi-Agent Topologies in Hub) with all subsections
- Add complete Section 23 (Collaboration Channels in Hub) including new 23.4
- Add complete Section 24 (Task Management in Hub) with all subsections

**Key Additions:**

- Section 3.6 entry: [3.6 Request-Scoped Authority Delegation](../part-2-how-seer-solves/03-identity-authority-in-seer/03-6-request-scoped-delegation.md)
- All Section 19-24 entries with proper file paths
- Verify all existing entries still resolve

**Editor Mode Checklist:**

- [ ] All section numbers match file structure
- [ ] All file paths are correct
- [ ] No duplicate entries
- [ ] Consistent formatting

---

### Task 4.2: Update How to Use This Book

**File to Update:** `olympus-seer-docs/why-seer/00-front-matter/00-2-how-to-use-this-book.md`

**Context Rehydration:**

- Review current Part 2 table (lines 27-42)
- Review terminology table (lines 108-120)
- Check if structure changes require reading path updates

**Updates Needed:**

- Update Part 2 table to include Section 3.6 under Section 3 (Identity & Authority)
- Add Sections 19-24 to Part 2 overview table
- Update terminology table if new key terms introduced
- Verify reading paths by role still make sense

**Key Changes:**

- Part 2 table: Add Section 3.6, Sections 19-24
- Terminology table: Add key new terms if they're foundational concepts
- Reading paths: Verify no changes needed based on new content

**Editor Mode Checklist:**

- [ ] Part 2 table complete and accurate
- [ ] Terminology table includes foundational terms
- [ ] Reading paths still valid
- [ ] Consistent with TOC structure

---

### Task 4.3: Update Glossary

**File to Update:** `olympus-seer-docs/why-seer/appendices/appendix-a-glossary.md`

**Context Rehydration:**

- Review all new sections for defined terms
- Check existing glossary structure
- Identify which terms are first defined where

**New Terms to Add:**

**Identity & Authority Section:**

- **Request-Scoped Authority Delegation**: Delegation model enabling business users to grant temporary authority to agents for specific tasks, distinct from enterprise delegation
- **Delegation Template**: Defines a package of authority that can be delegated to agents
- **Delegation Certificate**: Represents a user's consent to delegate authority per a template
- **Delegation Access Token**: Request-scoped JWT that an agent uses to perform actions on behalf of the delegator
- **Agent Persona**: Scenario-derived business identity representing "who is accountable" in business terms
- **Deployment Identity**: SPIFFE-based infrastructure identity used for mTLS and service mesh authentication
- **Sub-Persona**: Distinct identity for each agent in a composite application, derived from base Agent Persona

**Collaboration Channels Section:**

- **MCP Server**: Workbench-scoped CRD that exposes Hub capabilities via Model Context Protocol
- **Template Kind**: CRD kind (e.g., `business-user-template`) that implies persona and capabilities without explicit persona field

**Governance Section:**

- **COGW**: Cognitive Operations Governance Workbench — subscription-wide governance workbench type enabling cross-workbench oversight
- **COG Sentinel**: Request Sentinel with cross-workbench targeting via pattern-based matching

**Persona Twins Section:**

- **Persona Twin Blueprint**: Extension to Trained Agent Blueprints providing signal suggestions, filter templates, and schedule suggestions for non-developer twin creation
- **Signal Suggestions**: Common signals suggested by Persona Twin Blueprints (task assignment, platform notifications, schedules)
- **Filter Suggestions**: OPA filter templates provided by Persona Twin Blueprints for signal filtering
- **Schedule Suggestions**: Common schedules suggested by Persona Twin Blueprints (daily summaries, weekly reviews)

**Key Additions:**

- Add terms to appropriate existing sections (Identity & Authority, Platform Components, etc.)
- Create new sections if needed (e.g., Persona Twins)
- Ensure definitions match usage in main text
- Cross-reference first definition locations

**Editor Mode Checklist:**

- [ ] All new terms added
- [ ] Definitions match main text usage
- [ ] Terms organized logically
- [ ] Cross-references accurate

---

### Task 4.4: Review Appendix B (Seer + Hub Division)

**File to Review:** `olympus-seer-docs/why-seer/appendices/appendix-b-seer-hub-division.md`

**Context Rehydration:**

- Review responsibility matrix
- Check new capabilities against existing matrix
- Verify ownership is clear

**Review Tasks:**

- Verify MCP Server responsibility (likely Hub — collaboration channel)
- Verify Request-Scoped Delegation responsibility (likely Seer via Cipher IAM Extensions, but Hub Channels facilitate)
- Verify COGW responsibility (likely Hub — workbench type)
- Verify Persona Twin responsibility (likely Seer lifecycle, Hub operations)
- Verify Agent Identity Model (Deployment Identity vs Persona) — both Seer concepts

**Updates Needed:**

- Update responsibility matrix if clarifications needed
- Add new capabilities to appropriate sections
- Ensure consistency with main text

**Editor Mode Checklist:**

- [ ] Responsibility matrix accurate
- [ ] New capabilities properly categorized
- [ ] Consistent with main text

---

### Task 4.5: Review Appendix D (Further Reading)

**File to Review:** `olympus-seer-docs/why-seer/appendices/appendix-d-further-reading.md`

**Context Rehydration:**

- Review current ADR listing
- Check Decision Records section structure
- Verify all new ADRs are included

**New ADRs to Add:**

**Identity & Authority:**

- `olympus-hub-docs/decision-logs/0127-request-scoped-authority-delegation.md` — Request-Scoped Authority Delegation
- `olympus-hub-docs/decision-logs/0129-agent-identity-model.md` — Agent Identity Model (Deployment vs Persona)
- `olympus-hub-docs/decision-logs/0130-unified-delegation-model.md` — Unified Delegation Model

**Collaboration Channels:**

- `olympus-hub-docs/decision-logs/0131-mcp-server-crd-design.md` — MCP Server CRD Design
- `olympus-hub-docs/decision-logs/0132-mcp-template-kinds.md` — MCP Template Kinds
- `olympus-hub-docs/decision-logs/0134-mcp-directory-service.md` — MCP Directory Service

**Composite Patterns:**

- `olympus-hub-docs/decision-logs/0125-hub-composite-applications.md` — Hub Composite Applications
- `olympus-hub-docs/decision-logs/0126-composite-routing-table-schema.md` — Composite Routing Table Schema

**Updates Needed:**

- Add new ADRs to appropriate Decision Records subsections
- Organize by category (Identity, Collaboration, Composite Patterns)
- Verify all ADR paths are correct
- Add brief descriptions if helpful

**Editor Mode Checklist:**

- [ ] All new ADRs included
- [ ] Properly categorized
- [ ] Paths verified correct
- [ ] Consistent formatting

---

## Phase 5: Comprehensive Editorial Review (High Priority)

### Task 5.1: Comprehensive Editorial Review

**Scope:** Entire textbook — all sections, front matter, and appendices

**Context Rehydration:**

- Review textbook writing methodology from `why-seer-textbook-prompt.md`
- Review 7-part structural contract requirements
- Review terminology consistency guidelines
- Review cross-reference standards

**Review Areas:**

**1. Structural Consistency**

- [ ] All sections follow 7-part structural contract where applicable
- [ ] Purpose statements are clear and consistent
- [ ] Core concepts are formally defined
- [ ] Conceptual models are present where needed
- [ ] Enterprise considerations are addressed
- [ ] Misconceptions are identified
- [ ] Practical implications are clear
- [ ] Cross-references are complete

**2. Terminology Consistency**

- [ ] Key terms defined on first use (bolded)
- [ ] Terms used consistently throughout
- [ ] No conflicting definitions
- [ ] Glossary matches main text usage
- [ ] Acronyms expanded on first use
- [ ] Technical terms explained appropriately

**3. Cross-Reference Accuracy**

- [ ] All section references resolve correctly
- [ ] Cross-references are relevant and helpful
- [ ] No broken internal links
- [ ] Table of Contents matches actual structure
- [ ] Outline document matches content

**4. Content Quality**

- [ ] No marketing language
- [ ] First-principles reasoning present
- [ ] Explicit assumptions stated
- [ ] Facts, design choices, and opinions distinguished
- [ ] Long-form prose (not bullet dumps)
- [ ] Examples are clear and relevant
- [ ] Diagrams/examples support text

**5. Completeness**

- [ ] All ADRs referenced in plan are covered
- [ ] All gaps identified are addressed
- [ ] All enhancements completed
- [ ] Front matter is current
- [ ] Appendices are complete
- [ ] No placeholder content remains

**6. Writing Quality**

- [ ] Clear, professional prose
- [ ] Appropriate technical depth
- [ ] Consistent tone and voice
- [ ] Proper grammar and spelling
- [ ] Consistent formatting
- [ ] Tables are well-formatted
- [ ] Code examples are accurate

**7. Navigation & Usability**

- [ ] Table of Contents is complete
- [ ] "How to Use This Book" is accurate
- [ ] Reading paths are valid
- [ ] Glossary is comprehensive
- [ ] Appendices are useful
- [ ] Cross-references aid navigation

**Review Process:**

1. **Structural Pass:** Review each section for structural adherence
2. **Terminology Pass:** Create terminology map, verify consistency
3. **Cross-Reference Pass:** Verify all references resolve
4. **Quality Pass:** Review prose, examples, clarity
5. **Completeness Pass:** Verify all planned content exists
6. **Navigation Pass:** Verify all navigation aids work

**Deliverables:**

- Editorial review checklist (completed)
- List of issues found (if any)
- Recommendations for improvements (if any)
- Sign-off that textbook is ready for publication

**Editor Mode Checklist:**

- [ ] All review areas covered
- [ ] Issues documented and addressed
- [ ] Quality standards met
- [ ] Ready for final publication

---

## Estimated Effort

- **Phase 1 (Critical):** 5 tasks × ~2-3 hours each = 10-15 hours
- **Phase 2 (Enhancements):** 3 tasks × ~1-2 hours each = 3-6 hours
- **Phase 3 (Optional):** 3 tasks × ~1-2 hours each = 3-6 hours
- **Phase 4 (Front Matter & Appendices):** 5 tasks × ~1-2 hours each = 5-10 hours
- **Phase 5 (Editorial Review):** 1 task × ~8-12 hours = 8-12 hours (comprehensive review)
- **Total:** 29-49 hours