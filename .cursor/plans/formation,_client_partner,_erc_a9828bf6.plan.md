---
name: Formation, Client Partner, ERC
overview: Create a new engagement-formation.md document consolidating all team formation, assignment, phase evolution, and scaling patterns into a single authoritative source. Simultaneously add Client Partner as a core role, update ERC composition and assignment authority, and propagate changes across the Engagement guide.
todos:
  - id: formation-doc
    content: "Create engagement-formation.md: three-stage assignment model, designation-to-complexity matching, phase-by-phase team evolution, scaling patterns (Stream DLs, Stream Architects), team release"
    status: completed
  - id: roles-client-partner
    content: Add Client Partner role section to roles.md; update hierarchy diagram, execution-axis table, functional-axis table, and EO section
    status: completed
  - id: governance-erc
    content: "Update governance.md: ERC composition (add AM, Architecture), ERC assigns all Engagement-level roles, Client Partner in escalation and go-live"
    status: completed
  - id: staffing-fix
    content: "Update squad-model.md: fix assignment authority to ERC, slim staffing detail, add cross-reference to engagement-formation.md"
    status: completed
  - id: lifecycle-fix
    content: "Update lifecycle.md: fix Initiate phase role assignment to ERC, add Client Partner to active roles"
    status: completed
  - id: career-paths-updates
    content: "Update career-paths.md: add Client Partner to role assignment table, Account Management function/row, update function-role model section"
    status: completed
  - id: readme-updates
    content: "Update README.md: hierarchy diagram, Client Partner in role table and activity table, engagement-formation.md in guide contents, audience"
    status: completed
  - id: definition-updates
    content: "Update engagement-definition.md: Client Partner and EO rows in role table, fix activation model"
    status: completed
  - id: open-items-updates
    content: "Update open-items.md: Client Partner section, EO heritage criteria, formation-related open items"
    status: completed
isProject: false
---

# Formation, Client Partner, ERC, and Scaling Updates

This plan supersedes the previous `client_partner,_eo,_erc,_scaling` plan by incorporating the new **formation document** and merging scaling patterns into it.

## Key Design Decisions

- **New document:** [engagement-formation.md](org-8.0/engagement/engagement-formation.md) — single source of truth for how an Engagement team is formed, who assigns whom, from which function, at what designation level, how the team evolves through lifecycle phases, and how it scales for large Engagements.
- **No separate scaling-patterns.md** — scaling patterns (Stream Delivery Leads, Stream Architects) are a section within the formation document.
- **Summaries remain** in [squad-model.md](org-8.0/engagement/squad-model.md) and [lifecycle.md](org-8.0/engagement/lifecycle.md) with cross-references to the formation document for detail.
- **Client Partner → EO hierarchy:** Client Partner is the senior-most per-client role. EO reports to Client Partner on the execution axis. Client Partner is scoped per-client (may span multiple Engagements with the same client, bandwidth permitting); EO is scoped per-Engagement. Client Partner owns client-facing decisions; EO retains full internal delivery authority. ERC is the escalation endpoint for CP ↔ EO disagreements. AVA release-block authority remains independent of Client Partner.
- **Client Partner Associate (CPA):** Every Client Partner is supported by at least one CPA — a generalist who handles governance prep, stakeholder coordination, commercial tracking, cross-Engagement alignment, executive briefings, and operational work. CPA is a client-level role (not Engagement-scoped), reports to Client Partner, and can come from either Account Management or Program/Delivery function. For complex multi-Engagement clients, multiple CPAs may be staffed. ERC ensures CPA support is in place as part of Client Partner assignment.
- **ERC assigns all Engagement-level roles** (Client Partner, EO, EPM, EA, AVA) — not Engineering Leadership for EO.
- **ERC composition** expanded: add AM leadership and Architecture leadership.
- **Account Management function** added to career-paths.md.

---

## 1. Create engagement-formation.md

New file: [org-8.0/engagement/engagement-formation.md](org-8.0/engagement/engagement-formation.md)

Structure:

- **Purpose** — This document is the single source of truth for how an Engagement team is formed, how roles are assigned, and how the team evolves through the lifecycle.
- **Formation Philosophy** — ERC provides "ingredients of success"; assignment is function-based; ERC matches designation level to Engagement complexity.
- **Three-Stage Assignment Model**
  - **Stage 1 — ERC assigns Engagement leadership (at Initiate):** Client Partner + CPA(s) (per-client, may already be assigned if client has existing Engagements), EO, EPM, EA, AVA. ERC considers Engagement complexity, risk profile, customer relationship depth, and candidate heritage (for EO). Client Partner is assigned per-client and may span multiple Engagements; EO is per-Engagement and reports to Client Partner. ERC ensures at least one CPA is in place for the Client Partner. Describe heritage matching for EO (Architecture, Delivery, Engineering heritage).
  - **Stage 2 — EO assigns squad-level leadership (at Initiate/early Discover):** ELs, EPO, SRE Lead. EO selects from functional benches with ERC/PPM support. Note: Exploration Lead is the preferred candidate for CP Squad EL.
  - **Stage 3 — Squad staffing through PPM (at Discover):** Engineers, Squad PMs, Scrum Masters. ELs submit staffing requests to PPM; PPM consolidates demand; PL Squad leads commit individuals. Describe the 6-step process (currently in squad-model.md lines 81-86).
- **Designation-to-Complexity Matching** — Table showing which designation levels typically play each role based on Engagement complexity (small, medium, large/complex). Examples:
  - EA: Staff Engineer (small) vs. Architect (medium) vs. Senior Architect (large)
  - AVA: Staff Engineer (small) vs. Architect (medium) vs. Senior Architect (large)
  - EPM: Program Manager (small) vs. Senior Program Manager (medium) vs. Director of Delivery (large)
  - EPO: Product Manager (small) vs. Senior PM (medium) vs. Director of Product (large)
  - EO: Heritage-matched senior leader; complexity drives seniority requirement
- **Phase-by-Phase Team Evolution** — Diagram/table showing which roles activate, scale, or wind down at each lifecycle phase (Initiate, Discover, Build, Transfer, Complete). Reference the existing Role Activity table from README.md but add formation/release actions:
  - Initiate: Stage 1 and Stage 2 assignments happen
  - Discover: Stage 3 staffing; AVA begins; SRE Lead advisory
  - Build: Full team active; Verification Squad activated if warranted
  - Transfer: Squad members begin releasing; handover activities
  - Complete: Progressive release; final close
- **Scaling Patterns for Large Engagements (6+ squads)**
  - **Stream Delivery Leads** — EPM scaling pattern. When the EPM spans 6+ squads, introduce Stream DLs (from Program/Delivery function). Each Stream DL manages 2-4 squads; EPM coordinates across streams. Activation criteria, reporting, and functional-axis home.
  - **Stream Architects** — EA scaling pattern. When the Engagement spans multiple Product Lines or has 6+ squads with significant architecture complexity, introduce Stream Architects (from Architecture function). Each Stream Architect owns a domain slice; EA coordinates across streams. Activation criteria, reporting, and functional-axis home.
  - **Scaled hierarchy diagram** showing EO → EPM → Stream DLs → ELs and EO → EA → Stream Architects.
  - **Activation criteria** — When to activate scaling patterns (squad count, Product Line count, integration complexity).
- **Team Release** — How the team demobilizes at Transfer/Complete. Release sequence, return to functional benches, rotation model connection.
- **References** — Links to roles.md, squad-model.md, lifecycle.md, career-paths.md, governance.md, rotation-model.md.

---

## 2. Add Client Partner role to roles.md

In [roles.md](org-8.0/engagement/roles.md):

- Add **Client Partner** section as the first role (before EO), with: Purpose (senior-most per-client role; owns the strategic client relationship; EO reports to Client Partner), Responsibilities, Authority, Staffing (per-client, not per-Engagement; may span multiple Engagements with the same client), Typical challenges.
- Add **Client Partner Associate (CPA)** section immediately after Client Partner, with: Purpose (generalist support for Client Partner — governance prep, stakeholder coordination, commercial tracking, cross-Engagement alignment, executive briefings), Responsibilities, Reporting (to Client Partner), Staffing (at least one per Client Partner; more for multi-Engagement clients; from AM or Program/Delivery function), Typical challenges. Note: CPA experience across multiple clients is a natural progression toward the Client Partner role, but the role is defined by its operational accountability, not as a training position.
- Update the **execution-axis hierarchy diagram** to show Client Partner above EO:

```
              Client Partner
                │       │
               CPA     EO
                        │
        ┌──────────┬────┼────────┬──────────┐
        │          │    │        │          │
       EPM        EA   AVA     EPO     SRE Lead
```

- Update the **execution-axis table**:
  - Add Client Partner → "Assigned by ERC; reports to AM leadership (functional axis)"
  - Add CPA → "Reports to Client Partner (execution axis)"
  - Change EO → "Reports to Client Partner (execution axis)"
- Add **CP ↔ EO authority boundary** section: Client Partner owns client-facing decisions (stakeholder management, commercial alignment, relationship strategy); EO retains full internal delivery authority (architecture, quality, squad execution). When delivery decisions affect client commitments, EO recommends and Client Partner decides. When client demands affect delivery feasibility, Client Partner brings to EO and EO assesses. Client Partner cannot override AVA release-block authority. ERC is the escalation endpoint for CP ↔ EO disagreements.
- Update the **functional/career-axis table**: add Account Management function row
- Update **EO section**: EO reports to Client Partner (execution axis); EO retains internal delivery authority; add Client Partner to key relationships

---

## 3. Update governance.md — ERC composition and assignment authority

In [governance.md](org-8.0/engagement/governance.md):

- **ERC composition** (line 11): Replace "Senior delivery leaders and engineering leadership" with explicit list: "Engineering leadership, Architecture leadership, Delivery/Program leadership, Account Management leadership"
- **ERC assignment authority**: Add a sentence: "ERC assigns all Engagement-level roles: Client Partner, EO, EPM, EA, AVA. See [Engagement Formation](engagement-formation.md) for the full assignment model."
- Remove "Provides ingredients of success: Exploration Leads, EA and AVA assignments" (line 13) and replace with: "Provides ingredients of success: assigns Engagement-level leadership (Client Partner, EO, EPM, EA, AVA), provides framework guidance and archetype references, and governs the Exploration pipeline"
- **Go-Live Readiness** (lines 74-77): Add Client Partner as confirming customer-side readiness alongside EPM
- **Escalation model**: Add rows for Client Partner ↔ EO disputes:
  - "Client Partner vs EO (delivery-impacting client decision)" → "EO recommends; Client Partner decides" → "EO escalates to ERC if delivery quality is at risk"
  - "Client Partner vs EO (client-impacting delivery decision)" → "EO decides; Client Partner informed" → "Client Partner escalates to ERC if client relationship is at risk"
  - "Client Partner vs EPM (customer-facing communication)" → "EPM prevails on delivery communication; Client Partner prevails on relationship" → "EO resolves"

---

## 4. Update squad-model.md — Staffing section

In [squad-model.md](org-8.0/engagement/squad-model.md):

- **Staffing section** (lines 67-86): Keep the two-stage summary but:
  - Fix "Engineering Leadership assigns EO" → "ERC assigns Client Partner, EO, EPM, EA, AVA"
  - Fix "ERC assigns EPM and EA" → remove (absorbed into above)
  - Slim down the 6-step squad staffing process to a brief summary
  - Add cross-reference: "For the complete formation model — including designation-to-complexity matching, phase-by-phase team evolution, and scaling patterns — see [Engagement Formation](engagement-formation.md)."

---

## 5. Update lifecycle.md — Initiate phase

In [lifecycle.md](org-8.0/engagement/lifecycle.md):

- **Initiate Key activities** (lines 19-22): Fix role assignment bullets:
  - "ERC assigns **Client Partner**, **EO**, **EPM**, **EA**, **AVA** (ingredients of success)"
  - "EO assigns **ELs**, **EPO**, **SRE Lead**"
  - Remove "Engineering Leadership assigns EO"
- Add cross-reference to formation document
- **Roles active** (line 29): Add Client Partner

---

## 6. Update career-paths.md

In [career-paths.md](org-8.0/engagement/career-paths.md):

- **Section 1 (Function-Role Model)**: Add Client Partner as a role. Mention Account Management as the sixth function (or as a subset of Sales/Commercial — to be clarified during implementation based on whether AM warrants its own functional track or is a role within a broader Commercial function).
- **Section 5 (Role Assignment table)**: Add Client Partner row: "Typically supplied by: Account Management / Commercial function". Add CPA row: "Typically supplied by: Account Management or Program/Delivery function"
- **Section 6 (Convergence at EO)**: Already covers EO heritage — no change needed.
- **Section 7 (Dual-Axis Career Tracking)**: Add Account Management row if it's a separate function.

---

## 7. Update README.md

In [README.md](org-8.0/engagement/README.md):

- **Audience** (line 15): Add "Client Partner" and "Account Management"
- **Role Activity table** (lines 31-44): Add Client Partner row (primary at Initiate, Discover; supporting at Build, Transfer, Complete)
- **Hierarchy diagram** (lines 49-60): Update to show Client Partner above EO
- **Role descriptions** (lines 62-69): Add Client Partner description
- **Guide Contents table** (lines 75-88): Add row for `engagement-formation.md` (new document), update `squad-model.md` description to note cross-reference to formation
- **Glossary**: Add Client Partner entry

---

## 8. Update engagement-definition.md

In [engagement-definition.md](org-8.0/engagement/engagement-definition.md):

- **Role table** (Section 9.2, lines 282-291): Add Client Partner row; update EO row to note "assigned by ERC"
- **Section 9.4 (Activation Model)** (lines 331-336): Fix to reflect ERC assigning Client Partner, EO, EPM, EA, AVA

---

## 9. Update open-items.md

In [open-items.md](org-8.0/engagement/open-items.md):

- Add **Client Partner** section with open items: CP-EPM coordination protocol, CP scaling for multi-Engagement clients
- Add items under **EOs**: EO heritage matching criteria, EL functional-axis coordination mechanics
- Add items under **Cross-Cutting**: Designation-to-complexity matching calibration, formation retrospective process
- Remove any items that the formation document now addresses

