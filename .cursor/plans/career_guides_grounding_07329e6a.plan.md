---
name: Career Guides Grounding
overview: Update the career-guides plan so all Function and Role Coaching documents are grounded in the Engagement Operating Model and its business context, and avoid platitudes and broad generalizations.
todos: []
isProject: false
---

# Career Guides — Grounding in Operating Model and Business Context

This addendum applies to the career-guides structure (function coaching by seniority; role coaching with interactions, escalation, further learning). All coaching documents **must** follow the rules below so they stay specific to this operating model and avoid generic advice.

---

## 1. Grounding in the Engagement Operating Model

Coaching content must reference **concrete constructs** from the guide. Use them by name and tie advice to them.

**Constructs to reference where relevant:**

- **Engagement** — artifact collection (not project/relationship); lifecycle Initiate → Discover → Build → Transfer → Complete; pipeline element; unit of delivery accountability. See [engagement-definition.md](org-8.0/engagement/engagement-definition.md).
- **Formation** — ERC assigns Client Partner, EO, EPM, EA, AVA (and CPA support); EO assigns ELs, EPO, SRE Lead; PPM consolidates demand; designation-to-complexity matching; scaling patterns (Stream DLs, Stream Architects). See [engagement-formation.md](org-8.0/engagement/engagement-formation.md).
- **Dual-axis reporting** — execution axis (EO, EPM, Client Partner) vs functional/career axis; who evaluates performance vs who evaluates career; multi-Engagement track record as seniority signal. See [roles.md](org-8.0/engagement/roles.md#dual-axis-reporting-model).
- **Client Partner → EO** — EO reports to Client Partner; authority boundary (client-facing vs internal delivery); ERC as escalation endpoint for CP ↔ EO. See [roles.md](org-8.0/engagement/roles.md#client-partner--eo-authority-boundary).
- **Squad types** — CP, Studio, Verification (AVA-directed), PL (rotation source). Composition (EL, Squad PM, Scrum Master, engineers); Verification Squad has no EL. See [squad-model.md](org-8.0/engagement/squad-model.md).
- **Three artifact groups** — Customer Product, Studio Component, Verification (handed over at Transfer). See [engagement-engineering-in-practice.md](org-8.0/engagement/engagement-engineering-in-practice.md).
- **Governance** — ERC (composition, assignment authority, PPM, ingredients of success); PAC (Practice Mode, Governance Mode); escalation paths and decision defaults (EA vs AVA, EPM first, EO final, ERC for CP↔EO). See [governance.md](org-8.0/engagement/governance.md).
- **Engagement Success** — EPM-owned; readiness, adoption, value delivery; beyond engineering completion. See [engagement-definition.md](org-8.0/engagement/engagement-definition.md) Section 2.3.
- **Exploration** — pre-commitment; qualification gate; Exploration Lead as preferred CP Squad EL; boundary when commitment triggers Initiate. See [exploration.md](org-8.0/engagement/exploration.md).
- **Inner source** — EA prioritizes; EL plans into squad capacity; consult Product Line Maintainer before building; no fork. See [engagement-engineering-in-practice.md](org-8.0/engagement/engagement-engineering-in-practice.md) and [Inner Source Guidelines](org-8.0/product-line-engineering/governance/inner-source-guidelines.md).
- **Verification and certification** — AVA directs Verification Squad; release-block authority; system-under-test boundary; EA–AVA co-design; handover at Transfer. See [verification-and-certification.md](org-8.0/engagement/verification-and-certification.md).
- **Archetypes** — blueprint, cookbook, playbook; EA selects/adapts; variability documentation; PAC and pattern extraction. See [architecture-and-archetypes.md](org-8.0/engagement/architecture-and-archetypes.md).

**How to use in coaching:**

- In **Function Coaching:** For each level, tie "required craft, skills, competencies" to what the model demands (e.g. Senior Engineer ready for EL: can run a CP or Studio squad, work with EPM on staffing via PPM, meet EA’s mandatory review and DoD, support inner source prioritised by EA).
- In **Role Coaching:** Describe interactions using actual role names and governance (e.g. "When you escalate EA vs AVA on verification, EPM mediates first; if unresolved, EO decides. Do not go straight to EO."). Reference lifecycle phase where the role’s decisions matter (e.g. Discover: gap analysis and inner source plan; Build: variability documentation and certification).

---

## 2. Grounding in the Business Context

Coaching should explain **why this model exists** and **why roles/levels exist within it**, so the reader sees how their behaviour supports the business intent.

**Business context to weave in (from [engagement-definition.md](org-8.0/engagement/engagement-definition.md) and [engagement-engineering-in-practice.md](org-8.0/engagement/engagement-engineering-in-practice.md)):**

- **Product-line-based assembly** — We deliver customer-specific value by **assembling** from Product Lines and studio-built components, not by running bespoke projects. Engagements are artifact collections with a governed lifecycle.
- **Avoiding services drift** — The model keeps delivery repeatable and scalable; it avoids "every customer is a one-off," knowledge in people’s heads, and forking platforms. Engagement Engineering is the discipline that makes assembly repeatable.
- **Extend, don’t fork** — Ownership boundary: Engagement squads own the derived product (Customer Product + Studio + Verification); Product Line Squads own platforms. Inner source is the path for closing gaps; ELs and EAs work within that boundary.
- **Adoption and value delivery** — Engineering completion is not the end state. Engagement Success (EPM-owned) covers readiness, adoption, and value delivery in the customer’s environment.
- **Platforms as accelerators** — Platforms (e.g. Olympus, Tachyon) are accelerators/frameworks; customers need solutioning, implementation, integration. The EA/EPO/EL work exists to close the gap between "what’s in the box" and what the customer needs, in a governed way.

**How to use in coaching:**

- In **Function Coaching:** At each level, briefly state why that level exists in this model (e.g. "Staff Engineer (PE-1) may play EA on smaller Engagements because the model allows Architecture function or senior Engineering to supply EA; your craft must include gap analysis and inner source prioritisation, not only technical design.").
- In **Role Coaching:** Tie role success to business outcomes (e.g. "EPM success in this model means the customer is using what was delivered and realising value — Engagement Success — not only that milestones were reported.").

---

## 3. Avoiding Platitudes and Broad Generalizations

**Avoid:**

- Standalone statements that could apply to any company or role: e.g. "Be a strong communicator," "Build trust with stakeholders," "Think strategically," "Manage your time well," without linking to a specific artifact, decision, or interaction in the model.
- Vague "challenges" (e.g. "You will face difficult conversations") without naming who is involved, what decision is at stake, and which governance or escalation path applies.
- Generic "how to learn" (e.g. "Read widely and seek feedback") without pointing to concrete mechanisms in the model (e.g. execution-axis feedback to functional-axis leader, rotation, multi-Engagement exposure, PAC Practice Mode).

**Do instead:**

- **Tie to artifacts and decisions:** e.g. "When the EPM asks for integrated status, the EL should be able to summarise squad progress against the solution architecture and known gaps (inner source vs custom) so the EPM can report to the Client Partner and customer without chasing multiple threads."
- **Name roles and governance:** e.g. "If the client pushes for an earlier release and AVA has not certified, the Client Partner owns the client conversation; the EO owns the internal decision. Escalation between them goes to ERC. Do not ask the EPM to override AVA."
- **Use lifecycle and formation:** e.g. "At Initiate you are assigned by ERC; at Discover you work with PPM for squad staffing. Your first 90 days as EL should include aligning with EA on mandatory review and DoD, and with EPM on how you will feed integrated status."
- **Quote or paraphrase the guide:** Where a boundary or rule is already stated (e.g. "Client Partner cannot override AVA release-block authority"), the coaching doc can quote or cite it and then give practical "how to behave" guidance (e.g. "When the client pressures for a date, your job as Client Partner is to represent that pressure to EO and ERC, not to instruct AVA or EPM to release.").

---

## 4. Checklist for Authors

Before publishing a Function or Role Coaching doc:

- Every section references at least one concrete construct from the guide (ERC, lifecycle phase, squad type, artifact group, role, escalation path, formation step, etc.).
- The business context (assembly not services, extend don’t fork, Engagement Success, platforms as accelerators) is reflected where it explains why the role or level exists or why a behaviour matters.
- There are no standalone platitudes; every piece of advice is tied to a specific interaction, decision, or artifact in the model.
- Escalation and interaction guidance names the actual roles and governance (EPM, EO, ERC, Client Partner, AVA, etc.) and points to [governance.md](org-8.0/engagement/governance.md) and [roles.md](org-8.0/engagement/roles.md) where appropriate.
- "How to learn" points to mechanisms that exist in the model (dual-axis feedback, rotation, formation, PAC Practice Mode, inner source, multi-Engagement experience).

These rules should be added to the career-guides **README** and to the optional **FUNCTIONS.md** / **ROLES.md** templates so every new or revised coaching doc is written against them.