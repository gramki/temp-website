# PSD Template: Human-Interactive Module

**Module Archetype:** Human-Interactive (Synchronous UI)
**Primary Specification Surfaces:** UX (Dimension 4), Structural (Dimension 8)
**Examples:** Web Dashboards, Mobile App Frontends, CLIs

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
| Module Archetype | Human-Interactive |
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

*Adjust depth based on product archetype: Deep for Enterprise SaaS, Deep for Developer Platform, Medium for Consumer App.*

**Pricing / Packaging Implications:**

**Value Metric Changes:**

**KPI Impact Projections:**

---

## Section 3: Business Impact — Customer ROI — Dimension 3 [Depth: per product archetype]

*Adjust depth based on product archetype: Deep for Enterprise SaaS (B2B+SLG), Lighter for others.*

**Buyer Persona Implications:**

**Business Outcome Changes:**

**ROI Metric Impact:**

---

## Section 4: User Experience Impact — Dimension 4 [Deep]

*This is the primary specification surface for Human-Interactive modules. Be thorough.*

**Affected User Personas:**

**Affected Jobs (JTBD):**
- Which Jobs are accomplished, modified, or newly enabled by this change

**Affected UX Channels:**
- Which Channels are impacted (specify Interaction Modality × Engagement Mode)
- If a new Channel is being introduced, reference the governing PDR

**New / Modified User Journeys:**
- Journey name: End-to-end flow description
- Job(s) accomplished by each journey
- Channel each journey is experienced through
- Capabilities engaged (list the Dim 8 Capabilities each journey step requires)
- Cross-channel references: equivalent journeys in other channels, continuity handoff points

**Touchpoint Specifications (Build Track work artifacts):**
- Wireframes / mockups (attach or link)
- Interaction flows (step-by-step)
- UI copy and microcopy
- Error states and edge cases

> *Note: Touchpoints are Build Track work artifacts, not Definition Model entities (see DR-020). The Definition Model captures down to User Journey; screen-level detail is specified here and implemented in the Build Track.*

**Experience Attributes (encouraged for HI Module features):**
- For each feature, consider documenting: simplicity, ease, delight, control, speed, discoverability, error tolerance

**Accessibility Considerations:**
- WCAG compliance level (should align with UX Channel's Accessibility Standard field)
- Screen reader behavior
- Keyboard navigation
- Color contrast and visual accessibility

---

## Section 5: Technical & Architectural Impact — Dimension 5 [Medium]

*Frontend architecture, state management, component structure.*

**New / Modified Subsystems:**

**Key Component Specifications:**

**Architecture Decision Records:**

**Performance Requirements:**
- Time-to-interactive targets
- Bundle size constraints
- Rendering performance

---

## Section 6: Ecosystem & Extensibility Impact — Dimension 6 [Light]

*Only relevant if the UI exposes embeddable components, widgets, or SDKs.*

**New / Modified Endpoints:**

**Payload Schema Changes:**

**Backward Compatibility Plan:**

*If no extensibility impact, state: "No impact — this module does not expose programmatic interfaces."*

---

## Section 7: Operational Impact — Dimension 7 [Light]

*CDN, static hosting, edge caching.*

**Infrastructure Requirements:**

**Security & Compliance Implications:**
- CSP headers, XSS prevention
- Authentication/authorization changes

**Deployment Strategy:**

**Monitoring & Alerting:**
- Client-side error tracking
- Performance monitoring (Core Web Vitals)

---

## Section 8: Data & Information Impact — Dimension 9 [Medium]

*Form data, user preferences, client-side state, API data contracts.*

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
- Performance:
- Accessibility:
- Browser/device compatibility:

**Regression Scope:**

---

## Section 10: Epic Decomposition & Sequencing [Required]

**Proposed Epics:**
- Epic name: Description and scope

**Dependencies & Sequencing:**

**Risks & Open Questions:**
