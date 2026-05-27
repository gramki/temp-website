---
name: Client Partner, EO, ERC, Scaling
overview: Add Client Partner as a core Engagement role, reframe EO as a role playable from three functions, expand ERC to assign all Engagement-level roles with AM representation, create a scaling-patterns document for Stream DLs and Stream Architects, and propagate changes across the guide.
todos:
  - id: roles-client-partner
    content: Add Client Partner role section to roles.md; update hierarchy diagram, execution-axis table, functional-axis table, and EO section
    status: pending
  - id: governance-erc
    content: "Update governance.md: ERC composition (add AM, Architecture), ERC assigns all Engagement-level roles, Client Partner in escalation and go-live"
    status: pending
  - id: staffing-fix
    content: "Update squad-model.md and lifecycle.md: ERC assigns Client Partner, EO, EPM, EA, AVA (not Engineering Leadership assigns EO)"
    status: pending
  - id: scaling-patterns-doc
    content: "Create scaling-patterns.md: Stream Delivery Leads (EPM scaling), Stream Architects (EA scaling), activation criteria, scaled diagram"
    status: pending
  - id: career-paths-updates
    content: "Update career-paths.md: add Client Partner to role assignment table, AM function row, EO heritage matching table"
    status: pending
  - id: readme-updates-v2
    content: "Update README.md: hierarchy diagram, Client Partner in role table and activity table, scaling-patterns.md in guide contents, audience"
    status: pending
  - id: definition-updates
    content: "Update engagement-definition.md: Client Partner and EO rows in role table"
    status: pending
  - id: open-items-updates
    content: "Update open-items.md: Client Partner section, EL dual-axis items, EO heritage criteria"
    status: pending
isProject: false
---

# Client Partner, EO Reframe, ERC Expansion, and Scaling Patterns

## Design Decisions (from discussion)

1. **Client Partner is a core role**, not a scaling pattern. Enterprise clients require dedicated strategic client interface regardless of Engagement size.
2. **Client Partner and EO are peers.** Client Partner faces outward (executive governance, multi-stakeholder alignment, delivery-commercial synthesis); EO faces inward (technical coordination, escalation, role direction). Neither is above the other.
3. **EO is a role, not a function.** EO can be played by someone from Architecture, Delivery, or Engineering heritage. ERC matches EO background to Engagement risk profile.
4. **ERC assigns all Engagement-level roles:** Client Partner, EO, EPM, EA, AVA. Previously Engineering Leadership assigned EO separately.
5. **AM has representation in ERC.** ERC becomes cross-functional: Engineering, Architecture, Delivery, AM leadership, plus PPM.
6. **Scaling patterns** (Stream Delivery Leads for EPM, Stream Architects for EA) activate for large Engagements (6+ squads). These are separate from core roles.
7. **Dual-axis operational mechanics** (EL-functional leader coordination, performance input process) are captured as open items.

---

## 1. Add Client Partner role to `roles.md`

[roles.md](org-8.0/engagement/roles.md) — new section after the Dual-Axis Reporting Model, before Mandatory Architect Consultation (or after EO). The execution-axis hierarchy diagram and table also need updating.

### Hierarchy diagram (lines 18-29)

Replace to show Client Partner and EO as peers:

```
        Client Partner ─── Engagement Owner (EO)
        (outward)          (inward)
                                │
             ┌──────────┬──────┼───────┬──────────┐
             │          │      │       │          │
            EPM        EA    AVA     EPO     SRE Lead
             │                 │
        ┌────┼────┬────┐   Verification
        │    │    │    │     Squad
       CP  Studio PL  Scrum
       EL    EL  ELs  Masters
```

### Execution-axis table (lines 31-36)

Add row: `| Client Partner | Peer to EO (not reporting to EO) |`

Update EO row bullets to include: "Works in partnership with Client Partner"

### Client Partner role section

New section — placed before EO (since Client Partner is the outward-facing peer). Structure:

- **Purpose:** Strategic client interface — owns executive governance, multi-stakeholder alignment, and delivery-commercial synthesis for the Engagement. The Client Partner faces outward to the client organization; the EO faces inward to the delivery organization. They form a peer partnership.
- **Responsibilities:** Executive governance (steering committees), multi-stakeholder management on client side, delivery-commercial negotiation synthesis (AM owns commercial; EPM owns delivery; Client Partner synthesizes for governance), client escalation handling, relationship health across client's organizational layers
- **Authority:** Client-facing authority at the executive/governance level. Does not direct internal Engagement squads or roles.
- **Key relationships:** Peer to EO; works with EPM (delivery status for governance), AM (commercial context, account strategy), EA (technical discussions with client architects); assigned by ERC (AM representation).
- **Functional-axis home:** Account Management / Client leadership
- **Staffing:** One per Engagement. Assigned by ERC (AM leadership representation). For strategic accounts, the Client Partner may serve across multiple Engagements for the same client.
- **Typical challenges:** Navigating client politics; aligning multiple client stakeholders with competing priorities; representing delivery trade-offs in executive governance without having direct delivery authority; balancing client expectations with delivery reality (EO provides the reality; Client Partner communicates it)

### EO section update (lines 73-95)

Rewrite the EO section:

- Add: "The EO is a role, not a function — the EO's functional home remains their origin function (Architecture, Delivery, or Engineering)."
- Update purpose: "overall **internal** accountability for the Engagement's success, in partnership with the Client Partner who owns the strategic client interface"
- Add heritage matching: EO can come from Architecture (technically complex), Delivery (delivery-complex), or Engineering (execution-risk) heritage. ERC matches background to Engagement risk profile.
- Update key relationships: "Peer to Client Partner; reports to ERC (assigned by ERC); directs EPM, EA, AVA, EPO, SRE Lead"
- Remove "Reports to engineering leadership (execution axis)" — EO is assigned by ERC, not by Engineering Leadership

### Functional-axis table (lines 50-56)

Add row: `| Account Management | AM / Client leadership | Client Partner |`

---

## 2. Update `governance.md` — ERC composition and assignment scope

[governance.md](org-8.0/engagement/governance.md) lines 7-15.

### ERC composition (line 11)

Replace: `Senior delivery leaders and engineering leadership; exact membership varies per organizational structure`

With: `Cross-functional body with representation from Engineering leadership, Architecture leadership, Delivery leadership, and Account Management leadership; exact membership varies per organizational structure`

### ERC assignment scope (line 13)

Replace: `Provides ingredients of success: Exploration Leads, EA and AVA assignments, framework guidance, archetype references`

With: `Assigns all Engagement-level roles: Client Partner, EO, EPM, EA, AVA. Provides ingredients of success: Exploration Leads, framework guidance, archetype references`

### Add escalation row

Add Client Partner escalation: `| Client Partner vs EO (client-internal alignment) | — | ERC resolves |`

### Update Go-Live Readiness (line 77)

Add Client Partner: "**Client Partner** confirms client-side governance approval and stakeholder alignment"

---

## 3. Update `squad-model.md` — staffing assignments

[squad-model.md](org-8.0/engagement/squad-model.md) lines 73-77.

Replace:

```
- Engineering Leadership assigns **EO**
- ERC assigns **EPM** and **EA** (ingredients of success)
- EO assigns **ELs**, **AVA**, **EPO**, **SRE Lead**
```

With:

```
- ERC assigns **Client Partner**, **EO**, **EPM**, **EA**, and **AVA**
- EO assigns **ELs**, **EPO**, **SRE Lead**
```

---

## 4. Update `lifecycle.md` — same staffing fix

[lifecycle.md](org-8.0/engagement/lifecycle.md) lines 20-21.

Same replacement as squad-model.md:

Replace `Engineering Leadership assigns **EO**` and `ERC assigns **EPM** and **EA**` with:

`ERC assigns **Client Partner**, **EO**, **EPM**, **EA**, and **AVA**`

---

## 5. Create `scaling-patterns.md` — Stream DLs and Stream Architects

New document: [scaling-patterns.md](org-8.0/engagement/scaling-patterns.md)

Contents:

- **When scaling patterns activate:** 6+ squads across CP, Studio, and Verification. Scaling patterns are independent — you might need Stream DLs but not Stream Architects, or vice versa.
- **Stream Delivery Leads (EPM scaling):** From Program/Delivery function; each owns 2-3 related squads; provides integrated stream view to EPM; EPM remains the single customer-facing contact and owns the Engagement-level integrated view; Stream DLs face inward, not toward the client. Report to EPM on execution axis.
- **Stream Architects (EA scaling):** From Architecture function; each covers a stream's architecture (e.g., CP stream, Studio stream); EA becomes Lead Architect integrating across stream architects; stream architects handle squad-level architecture review within their stream. Report to EA on execution axis.
- Scaled structure diagram showing the full picture with Client Partner, EO, EPM+Stream DLs, EA+Stream Architects
- Note: scaling patterns don't change the core role model — they add intermediate layers within the existing reporting lines

---

## 6. Update `career-paths.md` — role assignment table, EO section, Client Partner

[career-paths.md](org-8.0/engagement/career-paths.md)

### Section 5: Role assignment table (lines 141-151)

Add Client Partner row: `| **Client Partner** | AM / Account Management | Core role for all Engagements |`

Update EO note: `Architecture, Delivery, or Engineering heritage; ERC matches to Engagement risk profile`

### Section 6: Convergence at EO (lines 157-167)

Add: "EO works in partnership with the Client Partner — the Client Partner owns the strategic client interface while the EO owns internal delivery coordination."

Add the heritage-matching table:

- Architecture heritage — best for technically complex Engagements
- Delivery heritage — best for delivery-complex Engagements
- Engineering heritage — best for execution-risk Engagements

### Functional-axis table in Section 7 (line 152)

Add row: `| AM / Account Management | AM / Client leadership | Client Partner |`

---

## 7. Update `README.md`

[README.md](org-8.0/engagement/README.md)

### Role hierarchy diagram (lines 49-60)

Update to show Client Partner-EO peer structure (matching roles.md).

### Role descriptions (lines 62-69)

Add: `- **Client Partner** — strategic client interface; executive governance; peer to EO (assigned by ERC)`

### Role Activity by Stage table (lines 31-43)

Add Client Partner row: primary from Exploration through Complete (Client Partner is active throughout).

### Guide Contents table (line 79)

Update roles.md description to include Client Partner.

Add row for scaling-patterns.md (new document, numbered as item 12; renumber Open Items to 13).

### Audience line (line 15)

Add "Client Partners" to the audience list.

---

## 8. Update `engagement-definition.md` — role table

[engagement-definition.md](org-8.0/engagement/engagement-definition.md) lines 280-291.

Add Client Partner row at the top: `| **Client Partner** | Strategic client interface; executive governance; peer to EO |`

Update EO row: `| **Engagement Owner (EO)** | Internal accountability; final escalation (Architecture, Delivery, or Engineering heritage) |`

---

## 9. Update `open-items.md`

[open-items.md](org-8.0/engagement/open-items.md)

### Add Client Partner section

- **Client Partner-EO partnership operating cadence** — How the Client Partner and EO coordinate: standing touchpoints, information flow, who prepares for governance meetings, how client escalations are triaged.
- **Client Partner-AM boundary** — The distinction between Client Partner (per-Engagement strategic interface) and AM (account-level commercial relationship). Operational detail on how they coordinate and where their mandates differ.

### Add EL dual-axis mechanics items (under ELs section)

- **Performance input process** — How the EL provides performance input to the functional-axis leader for squad members from other functions. The mechanism (written input, frequency, format) is not defined.
- **Assignment contract** — When an engineer is assigned to a squad, the EL, engineer, and functional leader should agree on expected duration, growth opportunity, and return plan. This practice is not documented.

### Update EO section

Add: Heritage matching guidance — how to assess whether an Engagement needs Architecture, Delivery, or Engineering heritage in the EO role. Currently left to ERC judgment without criteria.

### Update navigation

Update footer: scaling-patterns.md comes after career-paths.md.

---

## Files Changed Summary

- `org-8.0/engagement/roles.md` — Major: Client Partner section, EO rewrite, hierarchy diagram, functional-axis table
- `org-8.0/engagement/governance.md` — Moderate: ERC composition, assignment scope, Client Partner in escalation and go-live
- `org-8.0/engagement/squad-model.md` — Minor: staffing assignment fix (ERC assigns EO)
- `org-8.0/engagement/lifecycle.md` — Minor: same staffing fix
- `org-8.0/engagement/scaling-patterns.md` — New: Stream DLs, Stream Architects
- `org-8.0/engagement/career-paths.md` — Moderate: Client Partner in role table, EO heritage matching, AM function row
- `org-8.0/engagement/README.md` — Moderate: hierarchy diagram, role table, guide contents, audience
- `org-8.0/engagement/engagement-definition.md` — Minor: Client Partner and EO rows in role table
- `org-8.0/engagement/open-items.md` — Minor: Client Partner items, EL dual-axis items, EO heritage item

