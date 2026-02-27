# Governance, Decision-Making, and Escalation

[← Back to Guide](README.md)

---

## Engagement Readiness Council (ERC)

The **Engagement Readiness Council** governs the Engagement pipeline and provides the ingredients of success:

- **Composition:** Engineering leadership, Architecture leadership, Delivery/Program leadership, Account Management leadership; exact membership varies per organizational structure
- **Assignment authority:** ERC assigns all Engagement-level roles: Client Partner, EO, EPM, EA, AVA. See [Engagement Formation](engagement-formation.md) for the full assignment model.
- **Portfolio Program Manager (PPM):** Maintains the cross-Engagement portfolio view; prioritizes across Engagements; **owns capacity coordination** — consolidates staffing demand from all Engagements, presents a unified demand view to Product Line Squad leads, and coordinates supply commitments so that ELs do not independently approach PL Squad leads
- **Provides ingredients of success:** Assigns Engagement-level leadership (Client Partner, EO, EPM, EA, AVA), provides framework guidance and archetype references, and governs the Exploration pipeline
- **Governs EPM activities:** EPM reports to ERC on Engagement progress, risks, and commercial alignment
- **Security reviews:** Shared security team operates under ERC; performs VA/PT and reviews periodic or on-demand

---

## Platform Architecture Council (PAC)

The **PAC** governs architecture and practice across the product line:

- **Practice Mode (monthly):** Knowledge sharing, case reviews, pattern extraction, best-practice development
- **Governance Mode (ad-hoc):** Architectural disputes, standards changes, variability governance

ERC and PAC coexist: **ERC governs delivery readiness and the Engagement pipeline; PAC governs architecture and engineering practice.** They are complementary, not competing.

See [council-charter.md](../product-line-engineering/governance/council-charter.md) for the full PAC charter.

---

## Scope Change Management

- EPM owns scope change management within the Engagement
- EPM ensures Account Management is aware of any scope changes that affect commercial terms
- EPM verifies that delivery scope remains aligned with contract obligations

---

## Commercial and Contract

- **Account Management** owns the commercial relationship and contract
- **EPM** ensures AMs are aware of delivery-impacting changes and verifies alignment between delivery scope and commercial terms
- EPM does not negotiate contracts; EPM ensures delivery and commercial are in sync

---

## Escalation Model

| Disagreement | Default | Escalation Path |
|---|---|---|
| Client Partner vs EO (delivery-impacting client decision) | EO recommends; Client Partner decides | EO escalates to ERC if delivery quality is at risk |
| Client Partner vs EO (client-impacting delivery decision) | EO decides; Client Partner informed | Client Partner escalates to ERC if client relationship is at risk |
| Client Partner vs EPM (customer-facing communication) | EPM prevails on delivery communication; Client Partner prevails on relationship | EO resolves |
| EA vs AVA (architecture) | EA prevails | EPM resolves |
| EA vs AVA (verification/release) | AVA prevails | EPM resolves, then EO |
| EPO vs EA | EA prevails | EPM resolves |
| EPM vs EL | EL prevails | EA, then EO |
| Squad PM vs EPO | — | EPM, then EA, then EO |
| Scrum Master vs EL (process) | — | EPM resolves |

**Principles:**

- Architecture decisions default to EA; release/verification decisions default to AVA
- EPM is the first escalation point for cross-role disputes within the Engagement
- EO is the final escalation endpoint within the Engagement
- ERC is the escalation endpoint for Client Partner ↔ EO disagreements
- PAC may be engaged for architecture-level disputes that affect the product line

---

## Release and Decision-Point Governance

Key decision points during the Engagement lifecycle require sign-off from multiple roles. These are not pre-planned gates — they emerge as outcomes of continuous delivery and increment certification (see [Verification and Certification](verification-and-certification.md)).

### Go-Live Readiness

- **AVA** certifies the assembly — all go-live acceptance criteria are met
- **SRE Lead** confirms operational readiness — monitoring, alerting, runbooks, and capacity are in place
- **EPM** confirms customer alignment — scope, expectations, and commercial terms are satisfied
- **Client Partner** confirms customer-side readiness — relationship and stakeholder alignment for go-live
- **EO** gives the final go-live decision based on the above sign-offs

### Transfer Readiness

- **AVA** confirms verification module handover is complete — test suites, environment definitions, test data tooling, CI orchestration, certification records, and documentation are delivered to the recipient
- **EPM** confirms handover is complete per the operating model (Fully Managed, Co-Managed, or Customer-Operated)
- **SRE Lead** signs off on operational readiness for steady state

### AVA Release-Block Authority

The AVA holds independent authority to block any release when assembly quality criteria are not met. This authority cannot be overridden by EA, EL, or EPM. If a release block is disputed, the escalation path is: EPM mediates → EO decides. An EO override of an AVA release block is a governance event that must be documented in the decision log.

---

[← Previous: Verification and Certification](verification-and-certification.md) | [→ Next: Metrics and Feedback](metrics-and-feedback.md)
