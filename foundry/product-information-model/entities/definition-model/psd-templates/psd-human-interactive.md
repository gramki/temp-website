# Experience Capability Template

**Type:** Capability Template
**Model:** Definition Model — Dimension 1 (PSD)
**Applies to:** Capabilities whose primary expression is direct human interaction — dashboards, forms, flows, portals, mobile screens, chat interfaces.
**Used by:** Product Manager (PM-authored zone of the PSD — Product Draft phase)

---

## Purpose

This template guides a PM in specifying an **Experience Capability** within a PSD. An Experience Capability is one where the primary outcome is delivered through a human-facing interaction — a user sees, navigates, acts, and receives feedback directly.

The template structures the PM's specification at the Capability level. The Architect maps this Capability to Systems and Components independently (Technical Review phase) — the PM does not prescribe which Systems will realize it.

---

## Capability Specification Fields (PM-authored)

### Capability Identity

| Field | Type | Guidance |
|---|---|---|
| Capability Name | String | What does this capability enable? e.g., "Payment Dashboard — Multi-Currency View" |
| Capability Template | Enum | `Experience` (selected) |
| Maturity (target) | Enum | `Alpha` / `Beta` / `Gamma` — what maturity level is the goal of this PSD? |
| Lifecycle Stage (target) | Enum | `Planned → Available` (for new) or `Available → Deprecated` (for retirement) |

### Experience Specification

| Field | Type | Guidance |
|---|---|---|
| User Persona(s) | References (User Experience) | Who uses this capability? Reference User Experience User Personas directly. |
| Job-to-be-Done | Reference (User Experience) | What job is this capability helping the user accomplish? |
| User Journey | Description / Attachment | End-to-end flow: what does the user do, what does the system show/do at each step? Wireframes, flow diagrams, or textual description. |
| UX Channel | Enum / Reference (User Experience) | Web App / Mobile App / CLI / Chat / Email / Embedded Widget / Other |
| Interaction Model | Text | How does the user interact? (Form-driven, data table + actions, wizard, dashboard, conversational, etc.) |
| Key Screens / Views | List | Name and brief description of key screens or views introduced or changed |
| Accessibility Requirements | Text | WCAG level, screen reader support, keyboard navigation, colour contrast requirements |
| Localisation / Language | Text | Languages required, right-to-left support, currency/date format requirements |

### Capability Acceptance Criteria (PM-authored)

| Criterion | Type | Guidance |
|---|---|---|
| User Journey Completion | Text | The user can complete the specified journey end-to-end without errors |
| Performance (UX) | Text | Page load time, time-to-interactive targets |
| Accessibility | Text | Passes automated accessibility audit at specified WCAG level |
| Error Handling | Text | What happens when the user makes an error or the system fails? Expected user-visible behaviour. |
| Additional Criteria | List | Any domain-specific acceptance criteria |

---

## Notes for the Architect (Technical Review phase)

The Architect maps this Experience Capability to Systems and Components in Section 5 of the PSD. Common System contributions for Experience Capabilities:

- A **Web Application** or **Mobile Application** Component implements the frontend
- A **API Service** Component (BFF — Backend for Frontend) serves the frontend's data needs
- An **Event-Driven Worker** Component may handle async background updates surfaced in the UI

The Architect selects and maps the specific Systems and Components. The PM does not specify this.

---

## Example

**Capability:** "Multi-Currency Payment Dashboard"
**Module:** Customer Portal Module (Engagement)
**Template:** Experience

| Field | Value |
|---|---|
| User Persona(s) | AP Clerk (User Experience) |
| JTBD | "When I manage cross-border payments, I want to see all pending and completed payments across currencies in one view so I can reconcile without switching between screens." |
| UX Channel | Web Application |
| Key Screens | (1) Payment List with currency filter; (2) Payment Detail drawer; (3) FX Rate indicator |
| Accessibility | WCAG 2.1 AA; keyboard navigation required |
| Performance | Page load < 2s at P95; table renders < 500ms for up to 500 rows |
