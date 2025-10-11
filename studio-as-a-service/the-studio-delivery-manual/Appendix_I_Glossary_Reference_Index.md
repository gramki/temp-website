# Appendix I — Glossary & Reference Index

Use this appendix to align on terminology and to quickly look up where concepts are defined, owned, and measured. For role definitions and org placement, see `studio-as-a-service/roles_reference.md`.

---

## I.1 Glossary (curated)

- Acceptance Criteria (AC)
  - Clear, testable conditions for acceptance of a Feature/Story; aligned to subsystem boundaries. See Sections 5.4, 7.
- Amortization Reserve (Debt)
  - Capacity set aside (10–20%) for debt paydowns; protects stability and future velocity. See Section 6 and Appendix T.
- Application Programming Interface (API)
  - Programmatic interface/contract; see integration rules. See Sections 5.10, 7.
- Architecture Decision Record (ADR)
  - Lightweight record of significant technical decisions. See Appendix C (examples).
- Capacity Health Score
  - Composite score indicating team capacity readiness under TCM; includes runway, idle time, variance. See Section 8.
- Card‑Not‑Present (CNP)
  - Transactions where card is not physically present; higher risk. See Section 5 examples.
- Change Request (CR)
  - Formal scope/time/cost change artifact; governed in Section 8A.
- Continuous Integration / Continuous Delivery (CI/CD)
  - Automation pipeline for build/test/release. See Section 7 (Allure/Jenkins) and tooling notes.
- Critical Path (Quality)
  - The customer‑visible journeys whose failure blocks value; must meet pass‑rate thresholds at release. See Section 7.
- Decision Paper
  - One‑page options/impacts memo used for Steering or policy changes; includes owner/date and links. See Sections 9, 10, 11.
- Delivery Product Manager (DPM)
  - Decomposes features; supports requirement→feature conversion. See roles_reference and Sections 5, 9.
- Delivery Product Owner (DPO)
  - Product leader in EO org; acts as Solution Architect. Disambiguation: not Data Protection Officer here. See roles_reference and Sections 5, 9.
- Dependency Variance
  - Variance between promised and actual lead‑time on critical dependencies; tracked separately from delivery variance. See Section 8.
- DependencyFunding%
  - Percentage score representing funding + lead‑time commitment readiness across critical dependencies. See Sections 5.10, 8.
- Engineering Manager (EM)
  - Leads engineering execution/capacity/quality. See roles_reference and Sections 9, 10.
- Engagement Owner (EO)
  - Business owner; chairs Steering. See roles_reference and Sections 8, 9, Appendix J.
- Error Budget
  - Allowable failure budget under SLOs; when exhausted, stabilization takes priority over new intake. See Section 7.
- Feature / Epic / Story
  - Feature: subsystem‑scoped, testable slice of value; Epics/Stories: implementation decomposition units. See Section 5.7.
- Flake (Test)
  - Non‑deterministic test outcomes; quarantined and addressed via hardening windows. See Section 7.
- Forum Ownership Labels
  - Steering (EO‑owned); CCB/Operational Reviews (Studio‑owned). Every invite lists owner and chair. See Section 9.
- Funding Visibility Score (FVS)
  - Composite score indicating funding readiness and exposure under SFM; used for Steering readiness. See Section 8.
- JSON Web Key (JWK)
  - JSON key representation used for signing/verification. See Section 5.10.
- Leakage (Defect)
  - Defects escaping to later phases or production; tracked with taxonomy and trends. See Section 7.
- Lighter Control
  - A smaller, faster control that preserves the original intent (e.g., shorter template, time‑boxed review). See Section 10.9.
- Mean Time To Detect (MTTD)
  - Time to detect an incident/defect; tracked on quality dashboards. See Section 7.
- Mean Time To Restore/Resolve (MTTR)
  - Time to restore/resolve incidents; tracked on quality dashboards. See Section 7.
- Minimally Acceptable Requirement (MAR)
  - A requirement that is testable, bounded, and sufficiently clear to begin decomposition. See Section 5.2.
- Mutual TLS (mTLS)
  - Mutual certificate authentication for services. See Section 5.10.
- Non‑Functional Requirements (NFR)
  - Quality/system constraints such as performance, security, availability, operability. See Sections 5, 7.
- One‑Time Password (OTP)
  - Temporary code used for step‑up authentication/verification. See Section 5 examples.
- Process Exception / Concession
  - A time‑boxed relaxation or replacement of a control to meet near‑term goals; labeled, owned, reversible. See Section 10.9.
- Project Management Office (PMO)
  - Customer governance/program office. See Section 11 participants.
- Quality Assurance (QA)
  - Test/quality leadership (QA/Test Lead in this manual). See Section 7.
- Ready Coverage (Backlog)
  - Number of sprints worth of Ready items relative to planned capacity (TCM). See Sections 9, 8B.
- Ready‑for‑Planning (RfP)
  - Gate where a requirement’s Features are defined, AC/NFR drafted, design/impact assessed, dependencies mapped, and Customer sign‑off obtained. See Section 5.3.
- Risk Surfaces
  - Agreed areas where risk is expected or tolerated; defects within them are not automatically grounds for rejection. See Sections 7, 10.9.
- Scope‑Funded Model (SFM)
  - Commercial model where budget is tied to defined scope; changes via CR lifecycle. See Section 8A.
- Service Level Agreement (SLA)
  - Contracted service commitment (e.g., decision turnaround, provider lead‑time). See Sections 7, 8, 9, Appendix J.
- Service Level Indicator (SLI)
  - Measured indicator used to assess SLOs (e.g., pass rate, leakage). See Section 7.
- Service Level Objective (SLO)
  - Target level for a service metric (e.g., pass rate, error budget). See Section 7.
- Shelf‑life (RfP)
  - Time a signed Feature definition remains valid before re‑confirmation is needed. See Section 5.
- Single Sign‑On (SSO)
  - Federated authentication pattern. See Section 5.10.
- Site Reliability Engineering (SRE)
  - Discipline focused on reliability; distinct from product quality metrics in Section 7.
- Statement of Work (SoW)
  - Contract appendix describing scope/governance/commerce. See Appendix J.
- Strong Customer Authentication (SCA)
  - PSD2 authentication requirement in EU. See Section 5 examples.
- Studio Council Member (SCM)
  - Owner of institutional learning and manual versioning; tracks improvement lifecycle discovery→decision→implementation→adoption audit. See Section 11 and roles_reference.
- Team‑Capacity Model (TCM)
  - Commercial model where budget is tied to team capacity; scope evolves iteration by iteration. See Section 8B.
- Three‑Domain Secure (3DS)
  - Card network authentication protocol (e.g., 3DS 2.x). See Section 5 examples.
- Transaction Risk Analysis (TRA)
  - PSD2 risk‑based exemption analysis. See Section 5 examples.
- User Acceptance Testing (UAT)
  - Customer testing stage prior to production. Referenced in environments.


---

## I.2 Reference Index (where to find it)

Concept → Location(s)
- MAR & RfP gates → Section 5.2–5.3; Appendix G (Requirements SOPs)
- Feature/Epic/Story rules → Section 5.7; Appendix G
- Design/Impact addendum → Sections 5, 10; Appendix G
- Integration readiness checklist → Section 5.10; Appendix A (Reqs widgets)
- Quality gates & SLOs → Section 7; Appendix A (Quality dashboard); Appendix E (Quality Council)
- Error budget policy → Section 7; Appendix G (Quality SOPs)
- Debt taxonomy & portfolio → Section 6; Appendix C; Appendix A (Debt dashboard)
- Commercial models (SFM/TCM) → Section 8; Appendix A (Commercial dashboard)
- FVS / Capacity Health → Section 8; Appendix A (widgets); Appendix B (alerts)
- Rituals & facilitation → Section 9; Appendix E templates; Appendix F (flow map)
- Exception policy & concessions → Section 10.9; Appendix G (Operational SOPs)
- Continuous Improvement & SCM → Section 11; Appendix H (audit)
- Thresholds (tunable) → Appendix T

Roles & Forums → Ownership
- Steering Committee → EO‑owned (Chair: Engagement Owner). See Section 9; roles_reference.
- CCB / Commercial Review → Studio‑owned (Chair: Delivery Manager). See Sections 8, 9; roles_reference.
- Operational Review (Monthly) → Studio‑owned (Chair: Delivery Manager). See Section 9.
- Weekly Health & Risk Review → Studio‑owned (Chair: Delivery Manager). See Section 9.
- Quality Council → Studio‑owned (Chair: QA Lead). See Section 7.
- Architecture Roundtable → Studio‑owned (Chair: DPO/Technical Architect). See Section 9.

Labels & Indexing → Usage
- `RfP`, `decomposition/*` → Decomposition & readiness filters (Section 5)
- `process-exception` → Exception indexing and review (Sections 10.9, 11)
- `integration-risk`, `dependency/*` → Integration & dependency readiness (Sections 5.10, 8)
- Debt boards/labels → Portfolio indexing (Section 6, Appendix C)

---

## I.3 Notes on Consistency

- Terminology must match `roles_reference.md` (org placement, forum ownership, decision rights).
- Dashboards and alerts should name the forum and owner to avoid “shadow governance.”
- SCM reviews glossary updates quarterly and proposes manual version bumps when definitions change.
