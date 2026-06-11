# S2: Regulatory Landscape and Operations Mandates

| Field | Value |
|---|---|
| **Research date** | 15 March 2026 |
| **Engagement area** | Banking Operations |
| **Stream** | S2 — Regulatory Landscape |
| **Analyst scope** | Regulations that force or strongly incentivize banks to invest in run-the-bank business operations infrastructure — reconciliation, compliance/AML, fraud, collections, credit operations, regulatory reporting |
| **Geographies** | USA, India, UK/EU |

---

## 1. Regulation Data Table

### 1.1 United States

| Regulation | Jurisdiction | Operational Capability Demanded | Deadline / Status | Penalty Regime | Source URL | Verified |
|---|---|---|---|---|---|---|
| **BSA/AML — AML Program Requirements (31 USC §5318; 31 CFR Chapter X)** | USA | Written BSA/AML compliance program: internal controls, independent testing, designated BSA officer, employee training, Customer Identification Program (CIP). Transaction monitoring systems to detect and report suspicious activity. SAR filing for transactions ≥$5,000 where suspicion exists. CTR filing for cash transactions >$10,000. | In force (1970; amended continuously). October 2025 FinCEN FAQs clarified SAR filing documentation and structuring activity reviews. | Civil money penalties: up to $1M per violation per day (31 USC §5321). Criminal penalties: up to $500K fine and 10 years imprisonment. Recent benchmark: TD Bank — $3B total penalties (2024) for BSA/AML failures including inadequate transaction monitoring. | https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/04 | Yes |
| **FinCEN Beneficial Ownership / Corporate Transparency Act (CTA)** | USA | Banks must collect and verify beneficial ownership information for legal entity customers at account opening. CTA requires companies to report beneficial ownership to FinCEN — banks would use FinCEN's database for CDD. | **Enforcement suspended** as of March 2026. January 2025: Supreme Court stayed one nationwide injunction; a separate January 7, 2025 injunction remains in effect. FinCEN confirmed no filing obligation while injunction is active. Fifth Circuit oral arguments March 25, 2025. | Penalties under CTA: $500/day for late filing; criminal penalties up to $10K and 2 years. Banks' existing CDD Rule obligations (2018) remain in force regardless. | https://www.fincen.gov/boi | Yes (for CTA status); CDD Rule: https://www.federalregister.gov/documents/2016/05/11/2016-10567/customer-due-diligence-requirements-for-financial-institutions |
| **FinCEN AML Whistleblower Program (AMLA 2020 / AML Whistleblower Improvement Act 2022)** | USA | Banks must maintain effective BSA/AML programs or face whistleblower-driven enforcement. Whistleblowers receive 10–30% of monetary sanctions exceeding $1M. FinCEN launched dedicated whistleblower tip portal February 2026. | Operational as of February 2026. FinCEN has not published final implementing regulations for awards processing. | Creates external enforcement pressure: AML program deficiencies can be reported by insiders for substantial financial reward. Prior $150K cap removed. | https://www.fincen.gov/whistleblower-program | Yes |
| **OFAC Sanctions Screening** | USA | Real-time and continuous screening at multiple touchpoints: customer onboarding, ongoing transactions, periodic re-screening of entire customer base. Transaction-level screening of ACH and wires (all parties — originators and receivers). Fuzzy name-matching and multi-alphabet search capability. Detailed audit trails. | In force; continuous updates. Machine-readable sanctions lists and API-based continuous monitoring replacing static daily imports (2025–2026 developments). | Strict liability regime — no intent required. Civil penalties per violation; no statutory maximum (assessed case-by-case). Criminal penalties up to $20M and 30 years. OFAC penalty for name transliteration failure: £160K. TD Bank ACH screening failure contributed to $3B penalty. | https://ofac.treasury.gov/civil-penalties-and-enforcement-information | Yes |
| **OCC/Fed/FDIC Interagency Third-Party Risk Management Guidance (2023)** | USA | Full lifecycle third-party risk management: planning, due diligence, contract negotiation, ongoing monitoring, termination. Applies to all outsourced operations — reconciliation platforms, AML/compliance vendors, fraud systems, collections servicers. Risk-based approach with heightened oversight for critical activities. | In force (June 6, 2023). Exam-enforced. | Supervisory action: MRAs, consent orders, cease-and-desist. No fixed statutory fine — noncompliance constrains business activities. | https://www.occ.treas.gov/news-issuances/news-releases/2023/nr-ia-2023-53.html | Yes |
| **OCC Heightened Standards (12 CFR 30, Appendix D)** | USA | Three lines of defense for banks ≥$50B: front-line units own risk (operations teams); independent risk management provides oversight; internal audit assures controls. Risk appetite statement with concentration limits. Risk data aggregation and reporting capabilities. | In force (2014; technical amendments through December 2025). | Supervisory action (MRAs, consent orders, C&D). | https://www.law.cornell.edu/cfr/text/12/appendix-D_to_part_30 | Yes |
| **SEC/FINRA Recordkeeping (Rules 17a-3, 17a-4; FINRA Rule 4511)** | USA | Preserve all business communications and records for 3–6 years in non-rewriteable, non-erasable format (WORM). Extends to electronic communications (email, text, messaging apps). Must produce records on demand for examination. | In force. SEC off-channel enforcement sweep ongoing since 2021. August 2024: 26 firms fined $393M combined. January 2025: additional settlements on modified terms. | Civil penalties: $50M per firm (top end of 2024 settlements). $393M combined across 26 firms in August 2024 sweep. Total industry fines in billions since 2021. Collateral consequences: statutory disqualification risk. | https://www.sec.gov/newsroom/press-releases/2024-98 | Yes |
| **CFPB Regulation F — Debt Collection Practices (12 CFR 1006)** | USA | Implements FDCPA for debt collectors. Validation notice requirements. Call frequency limits (7 calls per 7 days per debt). Third-party communication restrictions. Electronic communication opt-out requirements. Prohibition on time-barred debt litigation. | Effective November 30, 2021. In force. | CFPB enforcement actions; UDAAP liability; state AG enforcement. Private right of action under FDCPA: actual damages + up to $1,000 statutory damages + attorney fees. Class actions: up to lesser of $500K or 1% of net worth. | https://www.consumerfinance.gov/rules-policy/final-rules/debt-collection-practices-regulation-f/ | Yes |
| **CFPB Supervision — Fair Lending, Servicing, Collections** | USA | Fair lending analysis on credit decisions and servicing practices. Servicing transfer and payment processing accuracy (Regulation Z / TILA). Loss mitigation evaluation completeness and timeliness. Collections communication compliance. Consumer complaint response and documentation. | In force; continuous supervisory examination. CFPB Supervisory Highlights Issue 38 (January 2025) established "no advanced technology exception." | CFPB enforcement: disgorgement, restitution, civil money penalties (up to $50K/day for knowing violations). ECOA/Reg B adverse action requirements extend to AI-mediated credit decisions. | https://www.consumerfinance.gov/compliance/circulars/circular-2023-03-adverse-action-notification-requirements-and-the-proper-use-of-the-cfpbs-sample-forms-provided-in-regulation-b/ | Yes |
| **Dodd-Frank Section 1033 — Personal Financial Data Rights** | USA | Data providers (banks, card issuers) must make consumer financial data available in standardized electronic formats. Consumer and developer API interfaces. Transaction and balance data for 24 months. Third-party data retention limited to 1 year with reauthorization. | Final rule issued October 2024. **Compliance dates:** April 1, 2026 (largest institutions); April 1, 2027–2030 (phased by size). Institutions ≤$850M assets exempt. Currently facing legal challenge from banking trade associations. | CFPB enforcement authority. No specific penalty schedule in the rule — enforcement through CFPB supervisory and enforcement powers. | https://www.consumerfinance.gov/compliance/compliance-resources/other-applicable-requirements/personal-financial-data-rights/ | Yes |

### 1.2 India

| Regulation | Jurisdiction | Operational Capability Demanded | Deadline / Status | Penalty Regime | Source URL | Verified |
|---|---|---|---|---|---|---|
| **RBI Master Direction — Know Your Customer (KYC) Direction, 2016 (updated August 2025)** | India | Customer identification and due diligence (CDD/EDD). Beneficial ownership identification for legal entities. Video-based Customer Identification Process (V-CIP). Centralized KYC (CKYC) integration. Periodic KYC update processes. Risk-based transaction monitoring. Ongoing due diligence and record retention. | In force (2016; continuously amended). Latest amendments August 2025 cover V-CIP enhancements, CKYC standardization, and beneficial ownership requirements. | RBI penalties under Banking Regulation Act (Section 46/47A): up to ₹1 crore per instance + ₹25,000 per day for continuing violations. Supervisory action including licence restrictions. | https://www.rbi.org.in/Scripts/BS_CircularIndexDisplay.aspx?Id=12089 | Yes |
| **PMLA / FIU-IND — STR, CTR, and Cross-Border Wire Transfer Reporting** | India | Suspicious Transaction Reports (STRs) for identified ML/TF red flags. Cash Transaction Reports (CTRs) for cash transactions >₹10 lakh. Cross-border wire transfer reports for transfers >₹5 lakh. Non-profit organization transaction reports >₹10 lakh. Property transaction reports >₹50 lakh. XML-format submission via FIU-IND portal (FINnet 2.0). | In force (PMLA 2002; rules amended through 2024). CTR/STR filing ongoing. FINnet 2.0 reporting format in use. | PMLA Section 13: imprisonment 3–7 years + fine up to ₹5 lakh. For fraud involving >₹100 crore: imprisonment up to 10 years + fine up to ₹25 lakh. Director's liability for corporate offences. Bank licence risk for persistent non-compliance. | https://fiuindia.gov.in/pdfs/AML_legislation/AMLCFTguidelines04072023.pdf | Yes |
| **RBI Master Directions on Fraud Risk Management (July 2024)** | India | Board-approved fraud risk management policy. Early Warning Signals (EWS) framework integrated with Core Banking Solutions for real-time monitoring. Dedicated Data Analytics-Market Intelligence Unit (mandatory). Central Fraud Registry reporting via CRILC — threshold reduced from ₹50 crore to ₹3 crore. Red-Flagged Account (RFA) reporting to RBI within 7 days. Fraud Monitoring Report (FMR) submission within 14 days (reduced from 21). Show Cause Notice and due process before fraud classification. | Effective July 15, 2024. Supersedes 36 prior circulars. Six-month timeline for EWS system setup/upgrade from effective date. | Fraudulent borrowers debarred from credit for 5 years from full repayment. RBI supervisory penalties. Criminal referral for fraud. Reputational and operational risk from inadequate fraud detection. | https://www.rbi.org.in/scripts/NotificationUser.aspx?Id=12703&Mode=0 | Yes |
| **RBI Statutory Returns and CIMS Migration** | India | Regulatory reporting via Centralised Information Management System (CIMS) — replacing legacy XBRL portal. Form A (fortnightly), Form VIII (monthly), Form IX (annual). Internet Banking and Mobile Banking returns (monthly, from August 2025). Master Direction on Filing of Supervisory Returns (February 2024) consolidates all supervisory return instructions. | CIMS migration phased: Form A from June 2024; Form VIII from May 2024; Form IX from December 2024. Internet/Mobile Banking returns from August 2025. Master Direction in force from February 2024. | RBI supervisory action for late or inaccurate filing. Penalties under Banking Regulation Act. Non-compliance flagged in annual inspection reports. | https://www.rbi.org.in/Scripts/BS_Listofallreturns.aspx?id=14 | Yes |
| **Digital Personal Data Protection Act (DPDP) 2023 and DPDP Rules 2025** | India | Explicit, granular consent for each data processing purpose (no bundling, no pre-ticked boxes). Multilingual consent notices. Data Protection Impact Assessments (DPIA) for Significant Data Fiduciaries (most banks qualify). Annual compliance audits. Mandatory Data Auditor appointment. Tiered data retention: PMLA requires 7-year retention vs. DPDP deletion after purpose fulfilled. Triple breach notification clock: CERT-In (6 hours), Data Protection Board (72 hours), RBI. Payment data must remain in India (RBI localization prevails over DPDP cross-border provisions). | DPDP Act enacted August 2023. DPDP Rules 2025 notified November 13, 2025. Phase 1 (Board setup) immediate. Phase 2 (consent managers) November 2026. Phase 3 (full compliance) May 2027. | Up to ₹250 crore per violation. Children's data violations: separate penalty. Data breach notification failure: separate penalty. Board orders can include processing restrictions. | https://www.meity.gov.in/static/uploads/2024/06/2a5ef610a85e2b05965a5a6bbd7e4c25.pdf | Yes |
| **CERT-In Directions — 6-Hour Incident Reporting (Section 70B, IT Act)** | India | Report cyber incidents within 6 hours. 20 reportable incident types. 180-day log retention across all systems. NTP clock synchronization. Designated CERT-In point of contact. | In force (June 28, 2022). | Imprisonment up to 1 year and/or fine up to ₹1 lakh under IT Act. Most aggressive incident reporting timeline globally. | https://cert-in.org.in/Directions70B.jsp | Yes |

### 1.3 UK / EU

| Regulation | Jurisdiction | Operational Capability Demanded | Deadline / Status | Penalty Regime | Source URL | Verified |
|---|---|---|---|---|---|---|
| **EU AML Package: AMLR (Regulation 2024/1624), 6AMLD (Directive 2024/1640), AMLA** | EU | Unified Customer Due Diligence (CDD) and Enhanced Due Diligence (EDD) with strengthened risk-based approach. Harmonized €10,000 cash payment threshold. Enhanced beneficial ownership transparency and traceability. Broader scope: crypto-asset service providers, sports agents, luxury sector. Harmonized ML offence definitions and minimum sanctions. Enhanced FIU cooperation. | Published June 19, 2024. **Full applicability: July 10, 2027.** AMLA operational launch mid-2025; direct supervision of high-risk entities from 2028. Some technical measures (e.g. property registers) until 2029. | 6AMLD: harmonized criminal sanctions including imprisonment. AMLR: administrative penalties set by member states; AMLA can impose penalties on supervised entities. Increased liability for legal persons. | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A32024L1640 | Yes |
| **AMLD5 (Directive 2018/843) — currently in force** | EU | Enhanced CDD for high-risk third countries. Beneficial ownership registers (public access). Virtual currency exchange and custodian wallet providers brought into scope. Wider access to beneficial ownership information for FIUs. Lower thresholds for anonymous prepaid cards. | In force (transposition deadline January 10, 2020). Will be superseded by AMLR/6AMLD in July 2027. | Member state-determined penalties. Enforcement varies by jurisdiction. | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32018L0843 | Yes |
| **DORA — Digital Operational Resilience Act (Regulation EU 2022/2554)** | EU | ICT risk management framework. Incident reporting. Digital operational resilience testing (TLPT every 3 years for significant institutions). Third-party ICT provider oversight (Register of Information). Information sharing. **Cross-reference:** Covered comprehensively in `_research/cloud-and-platform-operations/s2-regulatory-landscape.md`. For banking operations: DORA mandates that critical business operations (including reconciliation, compliance, and reporting) have documented ICT dependencies, tested recovery capabilities, and incident management protocols. | Fully applicable January 17, 2025. Register of Information first submission April 30, 2025. TLPT notifications expected 2026. | National supervisory penalties. CTPPs: up to €5M. Suspension/termination of services orders. | https://eur-lex.europa.eu/eli/reg/2022/2554 | Yes |
| **EBA Reporting Framework (COREP/FINREP) — Framework 4.2** | EU | Supervisory reporting: own funds (COREP), financial reporting (FINREP), large exposures, leverage ratio, liquidity coverage, net stable funding ratio, resolution planning. New operational risk reporting under CRR3 (Business Indicator Component replacing prior approaches). xBRL-CSV format adoption. DPM 2.0 transition. | Framework 4.2 applies from Q4 2025. **Operational risk COREP: June 2026.** FINREP updates (IFRS 18): March 2026. xBRL-CSV adoption: March 31, 2026. Resolution planning revision: December 2025. | National supervisory penalties for late or inaccurate regulatory reporting. ECB SREP score impact (Pillar 2 capital add-ons). | https://www.eba.europa.eu/risk-and-data-analysis/reporting-frameworks/reporting-framework-42 | Yes |
| **FCA Consumer Duty (PRIN 2A)** | UK | Four outcomes: Products & Services, Price & Value, Consumer Understanding, Consumer Support. 100% monitoring of customer interactions. Must identify when vulnerable customer groups receive poorer outcomes. Applies to collections and servicing operations. Board-level accountability under SM&CR. | Effective July 31, 2023 (new products); July 31, 2024 (existing customers). In force. | FCA enforcement: unlimited fines. SM&CR personal accountability for senior managers. | https://www.handbook.fca.org.uk/handbook/PRIN/2A.htm | Yes |
| **PRA SS1/21 / FCA PS21/3 — Operational Resilience** | UK | Identify important business services (including reconciliation, compliance, fraud operations). Set impact tolerances. Map dependencies. Scenario testing. Resilience investment. **Cross-reference:** Covered in `_research/cloud-and-platform-operations/s2-regulatory-landscape.md`. For banking operations: reconciliation, compliance monitoring, and regulatory reporting are likely "important business services" requiring impact tolerances and tested recovery capabilities. | Rules in force March 31, 2022. **Full compliance: March 31, 2025.** | PRA/FCA supervisory action and enforcement powers under FSMA. FCA: unlimited fines. | https://bankofengland.co.uk/prudential-regulation/publication/2021/march/operational-resilience-impact-tolerances-for-important-business-services-ss | Yes |

---

## 2. Key Findings

### 2.1 AML/Compliance Operations Are Under Unprecedented Regulatory Pressure

- **The BSA/AML enforcement benchmark has been reset.** TD Bank's $3B penalty (2024) — the largest BSA/AML enforcement action in history — established a new ceiling for consequences of inadequate transaction monitoring and AML program failures. The penalty included a $1.3B FinCEN assessment, a $1.8B DOJ plea agreement, and an asset cap. This is not an outlier — it is the signal for what regulators consider proportionate for systemic AML failures at large banks. Every bank's AML operations investment calculus changed in October 2024.

- **The FinCEN whistleblower program creates a new enforcement vector.** With the February 2026 tip portal launch and awards of 10–30% of sanctions exceeding $1M, internal compliance failures now have an external reporting incentive. Banks with weak transaction monitoring, inadequate SAR filing, or deficient compliance operations face exposure from their own staff. This is the first time BSA/AML compliance has had a financial incentive for whistleblowers comparable to the SEC's program.

- **India's fraud reporting framework underwent a structural overhaul in July 2024.** The revised RBI Master Directions on Fraud Risk Management supersede 36 prior circulars and mandate: (a) EWS systems integrated with core banking for real-time monitoring, (b) a dedicated Data Analytics-Market Intelligence Unit, (c) CRILC fraud reporting threshold dropped from ₹50 crore to ₹3 crore, and (d) FMR filing compressed from 21 to 14 days. Banks have six months from effective date to establish or upgrade EWS infrastructure — a direct investment mandate.

- **The EU is building a single AML rulebook.** AMLR + 6AMLD + AMLA replaces the current patchwork of national transpositions with a directly applicable regulation (AMLR), a harmonized criminal directive (6AMLD), and a centralized supervisor (AMLA). Full applicability in July 2027. Banks operating across EU jurisdictions will face a single set of CDD/EDD requirements rather than 27 national variations — simplifying compliance architecture but requiring a one-time alignment effort.

### 2.2 Sanctions Screening Is Shifting from Batch to Continuous

- **OFAC expectations have moved to real-time, multi-touchpoint screening.** Banks must screen at customer onboarding, during ongoing transactions (real-time for payments), and through periodic re-screening of the entire customer base against updated lists. Transaction-level ACH screening — covering all parties (originators and receivers) — is now expected, not just customer-level checks. Batch-only screening architectures are non-compliant.

- **Machine-readable sanctions lists and API-based monitoring** are replacing static daily file imports. This is a technology infrastructure shift: sanctions operations platforms must support continuous list ingestion, fuzzy matching across alphabets and transliterations, and explainable AI for transparent decision-making on potential matches.

### 2.3 Regulatory Reporting Is Being Modernized Across All Jurisdictions

- **India: RBI is migrating from XBRL to CIMS.** The Centralised Information Management System is a next-generation data warehouse replacing legacy XBRL reporting. Statutory returns (Form A, Form VIII, Form IX) are already on CIMS; Internet and Mobile Banking returns followed from August 2025. The February 2024 Master Direction on Filing of Supervisory Returns consolidates all return instructions into a single framework. Banks must invest in data extraction, transformation, and submission infrastructure aligned with CIMS specifications.

- **EU: EBA Reporting Framework 4.2 introduces structural changes.** The shift to xBRL-CSV format (March 2026 deadline), new operational risk reporting under CRR3's Business Indicator Component (June 2026), and FINREP updates for IFRS 18 (March 2026) force banks to upgrade regulatory reporting infrastructure. The DPM 2.0 transition changes the underlying data model.

- **US: SEC/FINRA recordkeeping enforcement has extracted billions in fines.** The off-channel communications enforcement sweep — $393M in August 2024 alone, billions cumulative since 2021 — demonstrates that recordkeeping is not a back-office formality. Banks and broker-dealers must capture, preserve, and produce all business communications in WORM-compliant format. The January 2025 settlements introduced modified terms, but the compliance obligation remains.

### 2.4 Collections and Servicing Operations Face Distinct Regulatory Constraints

- **CFPB Regulation F imposes operational constraints on collections.** Call frequency limits (7 calls per 7 days per debt), electronic communication opt-out requirements, validation notice mandates, and the prohibition on time-barred debt litigation all require collections operations platforms with configurable communication rules, audit trails, and compliance monitoring. Manual collections processes cannot reliably enforce these constraints at scale.

- **FCA Consumer Duty extends to collections and servicing.** The 100% interaction monitoring requirement and vulnerable customer identification obligation apply to collections operations. UK banks must demonstrate that collections practices deliver "good outcomes" for all customer segments, including vulnerable populations.

### 2.5 Data Access and Data Protection Create New Operations Infrastructure Requirements

- **Dodd-Frank 1033 forces operations data architecture investment.** The April 2026 compliance deadline for largest institutions requires standardized API access to transaction and balance data for 24 months. This is not just a technology project — it requires operations infrastructure to extract, format, and serve data from core systems, reconciliation records, and account servicing platforms in standardized formats with performance and security requirements. The rule is facing legal challenge but the April 2026 deadline for largest banks stands as of March 2026.

- **India's DPDP Act creates a triple compliance burden for banking operations.** Banks must manage three concurrent regulatory clocks for data breach notification (CERT-In 6 hours, Data Protection Board 72 hours, RBI incident reporting), reconcile PMLA's 7-year retention requirement with DPDP's purpose-limitation deletion mandate, and implement granular per-purpose consent management across all operations that process personal data.

### 2.6 Cross-Jurisdictional Regulatory Convergence on Operations Investment

Every jurisdiction studied mandates investment in the same operational capability categories, though through different regulatory instruments:

| Capability | USA | India | UK/EU |
|---|---|---|---|
| **Transaction monitoring and SAR/STR filing** | BSA/AML, FinCEN | PMLA, FIU-IND | AMLR/6AMLD, national FIUs |
| **Sanctions screening** | OFAC | RBI KYC Direction, PMLA | EU sanctions regulations, OFSI (UK) |
| **Fraud detection and reporting** | OCC/Fed examination | RBI Master Direction on Fraud (2024) | FCA/PRA supervisory expectations |
| **Regulatory reporting** | SEC/FINRA recordkeeping, Call Reports | RBI CIMS statutory returns | EBA COREP/FINREP, national reporting |
| **Collections compliance** | CFPB Regulation F, FDCPA | RBI Fair Practices Code | FCA Consumer Duty, FCA CONC |
| **Data access / open banking** | Dodd-Frank 1033 | Account Aggregator framework (RBI) | PSD2/PSD3 (EU), UK Open Banking |
| **Incident reporting** | SEC (4 business days) | CERT-In (6 hours) | DORA (hours-to-days), GDPR (72 hours) |
| **Third-party/vendor risk** | Interagency guidance 2023 | RBI IT outsourcing direction | DORA third-party oversight |

---

## 3. Cross-References to Existing Research

| Topic | Existing Coverage | This Document's Focus |
|---|---|---|
| **DORA (five pillars)** | `_research/cloud-and-platform-operations/s2-regulatory-landscape.md` — comprehensive cloud and ICT infrastructure analysis | Banking operations angle: which operations functions (reconciliation, compliance, reporting) are "important business services" requiring DORA-mandated resilience |
| **PRA SS1/21 / FCA PS21/3 operational resilience** | `_research/cloud-and-platform-operations/s2-regulatory-landscape.md` — full coverage including March 2025 deadline | Not duplicated; cross-referenced for banking operations service identification |
| **CERT-In 6-hour reporting** | `_research/cloud-and-platform-operations/s2-regulatory-landscape.md` — full coverage | Referenced for triple-clock data breach notification (CERT-In + DPB + RBI) |
| **SR 11-7 and AI model governance** | `_research/agentic-banking/s2-regulatory-landscape.md` — customer-facing AI focus; `_research/cloud-and-platform-operations/s2-regulatory-landscape.md` — AIOps focus | Not duplicated; relevant to banking operations only where AI is used for transaction monitoring, fraud detection, or reconciliation |
| **EU AI Act** | `_research/agentic-banking/s2-regulatory-landscape.md` — comprehensive high-risk classification analysis | Not duplicated; relevant to banking operations only where AI credit scoring is classified as high-risk |
| **DPDP Act (India)** | `_research/agentic-banking/s2-regulatory-landscape.md` — consent management for AI interactions | This document: data operations compliance — retention conflicts (PMLA vs. DPDP), triple breach notification, SDF obligations for banks |
| **Interagency Third-Party Risk Management 2023** | `_research/cloud-and-platform-operations/s2-regulatory-landscape.md` — cloud vendor focus | This document: operations vendor oversight (AML platforms, reconciliation systems, collections servicers) |

---

## 4. Gaps and Unresolved Questions

### 4.1 Regulatory Gaps

1. **BSA/AML modernization rulemaking status unclear.** FinCEN proposed an AML/CFT program effectiveness rule in 2024 that would require risk-based, reasonably designed programs with specific emphasis on government priorities (FinCEN national priorities). Whether this rule has been finalized, withdrawn, or paused under the current administration requires confirmation. [unverified — needs manual confirmation of FinCEN rulemaking docket]

2. **Corporate Transparency Act enforcement remains judicially blocked.** As of March 2026, the January 7, 2025 nationwide injunction remains in effect. FinCEN has confirmed no filing obligation while the injunction stands. Whether the Fifth Circuit appeal (oral arguments March 25, 2025) has been decided, and whether any executive order has further affected CTA implementation, requires verification. [unverified — needs manual check of Fifth Circuit docket and FinCEN announcements post-March 2025]

3. **CFPB operational status under current administration.** Multiple CFPB enforcement actions and supervisory priorities cited in this document (Regulation F enforcement, Section 1033 implementation, fair lending supervision) were initiated or finalized under the prior administration. The current administration's posture on CFPB enforcement intensity — particularly for collections and servicing supervision — requires confirmation. Section 1033 faces a legal challenge from banking trade associations; whether the CFPB is defending the rule or has signaled willingness to modify it is an open question. [unverified — needs manual confirmation of CFPB enforcement posture and 1033 litigation status]

4. **India PMLA/FIU-IND — FINnet 2.0 reporting format transition completeness.** The transition from fixed-width text format to XML via FINnet 2.0 for CTR/STR filing is ongoing. Whether all banks have completed migration, and whether FIU-IND has sunset the legacy format, requires confirmation from FIU-IND. [unverified — needs manual confirmation from fiuindia.gov.in]

5. **EU AMLA — supervisory scope and timeline for direct supervision.** AMLA is expected to begin direct supervision of high-risk entities in 2028. Which banks will fall under direct AMLA supervision (vs. national supervisors) and the criteria for "high-risk cross-border group" designation are not yet fully specified. [unverified — needs monitoring of AMLA designation criteria publications]

6. **RBI Account Aggregator framework — regulatory reporting implications.** India's Account Aggregator (AA) ecosystem is the operational equivalent of Dodd-Frank 1033 / PSD2. Whether AA participation creates additional regulatory reporting or data-sharing obligations for banks, beyond the existing NBFC-AA licensing framework, requires clarification for the banking operations scope. [needs further research]

### 4.2 Evidence Quality Assessment

| Regulation | Evidence Quality | Notes |
|---|---|---|
| BSA/AML / FinCEN | **Strong** — official regulatory texts, FFIEC examination manual, enforcement actions with public records | |
| OFAC sanctions screening | **Strong** — official OFAC guidance, enforcement data, industry analysis with specific penalties cited | |
| SEC/FINRA recordkeeping | **Strong** — SEC press releases with specific penalty amounts, enforcement orders | |
| CFPB Regulation F | **Strong** — final rule text, FAQ documentation, official CFPB resources | |
| Dodd-Frank 1033 | **Moderate** — final rule published October 2024; litigation status and current administration posture unclear | |
| CTA/Beneficial Ownership | **Moderate** — Supreme Court and district court orders documented; current enforcement status requires monitoring | |
| FinCEN Whistleblower | **Strong** — FinCEN official website, February 2026 portal launch confirmed | |
| RBI KYC Direction | **Strong** — official RBI Master Direction with amendment history | |
| RBI Fraud Management | **Strong** — official RBI notification, KPMG and industry analysis cross-referenced | |
| PMLA/FIU-IND | **Moderate** — FIU-IND guidelines available; operational status of FINnet 2.0 migration requires confirmation | |
| RBI CIMS/Statutory Returns | **Strong** — official RBI circulars and notification with specific form migration dates | |
| DPDP Act | **Strong** — official Act text, DPDP Rules 2025, industry compliance analyses | |
| AMLR/6AMLD/AMLA | **Strong** — EUR-Lex official text, industry analyses with specific timelines | |
| EBA COREP/FINREP 4.2 | **Strong** — EBA official reporting framework page with module-by-module timelines | |

---

## 5. Raw Notes

### 5.1 BSA/AML Operations — Scale and Complexity

> Banks are only required to file SARs when they "know, suspect, or have reason to suspect" that a transaction is designed to evade BSA reporting requirements — not merely because transactions occur at or near the $10,000 CTR threshold. SARs must be filed for transactions involving at least $5,000 when there is suspicion of BSA evasion or other illicit activity.

Source: FinCEN SAR FAQs (October 2025). https://www.fincen.gov/system/files/2025-10/SAR-FAQs-October-2025.pdf

> Banks must establish written BSA/AML compliance programs appropriate to their size, business lines, and risks. Programs must include internal controls for ongoing compliance, independent testing procedures, designated compliance personnel, employee training, and a Customer Identification Program (CIP).

Source: Reuters Practical Law, "Bank Secrecy Act: Compliance Issues" (March 2025). https://www.reuters.com/practical-law-the-journal/transactional/bank-secrecy-act-compliance-issues-2025-03-01/

### 5.2 OFAC Continuous Monitoring Shift

> OFAC expects screening at multiple touchpoints: customer onboarding, ongoing transactions (real-time), and periodic re-screening of entire customer base against updated lists. Transaction-level screening of ACH and wire transfers must cover all parties — originators and receivers.

Source: Hunton Andrews Kurth, "OFAC to Banks: Implement Continuous Sanctions Monitoring." https://www.hunton.com/insights/legal/ofac-to-banks-implement-continuous-sanctions-monitoring

> Key 2025–2026 developments include machine-readable sanctions lists, API-based continuous monitoring replacing static daily imports, and expanded individual identifiers including biometric fields.

Source: CheckLynx, "Sanctions Screening: 2026 Best Practices." https://checklynx.com/en/resources/knowledge-base/sanction-screening

### 5.3 SEC Off-Channel Communications — Penalty Scale

> The SEC charged 26 broker-dealers and investment advisers with widespread recordkeeping failures for failing to maintain off-channel communications. These firms agreed to pay a combined $392.75 million in civil penalties. Major individual penalties: Ameriprise ($50M), Edward Jones ($50M), LPL Financial ($50M), Raymond James ($50M), RBC Capital Markets ($45M), BNY Mellon/Pershing ($40M).

Source: SEC Press Release 2024-98 (August 2024). https://www.sec.gov/newsroom/press-releases/2024-98

### 5.4 FinCEN Whistleblower Program Launch

> On February 13, 2026, FinCEN launched a dedicated webpage to accept confidential whistleblower tips. Whistleblowers can receive awards of 10–30% of monetary sanctions collected in excess of $1 million. The Anti-Money Laundering Act of 2020 significantly expanded FinCEN's whistleblower program, modeled after the SEC's successful model.

Source: Arnold & Porter, "FinCEN Launches New Whistleblower Webpage" (February 2026). https://www.arnoldporter.com/en/perspectives/blogs/enforcement-edge/2026/02/fincen-launches-new-whistleblower-webpage

### 5.5 RBI Fraud Risk Management Overhaul (July 2024)

> The aggregate fund-based and non-fund-based exposure threshold for CRILC reporting has been reduced from INR 50 crore to INR 3 crore for fraud/Red-Flagged Account cases. The timeline to furnish Fraud Monitoring Reports has been reduced from 21 days to 14 days. A dedicated Data Analytics-Market Intelligence Unit is now mandated.

Source: KPMG India, "Boardroom Briefing: RBI's New Guidelines on Strengthening Fraud Risk Management" (September 2024). https://assets.kpmg.com/content/dam/kpmgsites/in/pdf/2024/09/boardroom-briefing-rbis-new-guidelines-on-strengthening-fraud-risk-management.pdf

> The revised Master Directions on Fraud Risk Management, issued July 15, 2024, supersede 36 existing circulars and require compliance with principles of natural justice before classifying accounts as fraudulent — banks must serve Show Cause Notices with a minimum 21-day response period.

Source: IndiaLaw.in, "RBI Issues Revised Master Directions on Fraud." https://www.indialaw.in/blog/banking-and-finance/rbi-issues-revised-master-directions-on-fraud/

### 5.6 India DPDP Act — Triple Compliance Burden

> Financial institutions now face three regulatory clocks: CERT-In (6 hours), the Data Protection Board (72 hours under DPDP), and RBI's incident reporting framework.

> RBI requires 7-year retention for KYC and transaction records under PMLA compliance, while DPDP mandates deletion once processing purpose is fulfilled (1-year minimum). Banks must implement tiered retention policies documenting legal bases for extended retention.

Source: ZCyberSecurity, "DPDP Act Impact on Indian Banking/BFSI Sector." https://zcybersecurity.com/understanding-dpdp-act-for-banks-financial-institutions/

### 5.7 EU AML Package — Single Rulebook

> AMLA will begin operational launch in mid-2025, with direct supervision of high-risk entities (systemic banks, cross-border groups, crypto providers) commencing in 2028. This replaces fragmented national approaches with EU-level coordination.

> The AMLR is a directly applicable regulation — unlike directives (AMLD1-5), it does not require national transposition, creating a genuine single rulebook for AML compliance across the EU.

Source: B4Finance, "AMLA, AMLR, 6AMLD: Key Compliance Reforms for 2026." https://www.b4finance.com/blog/amla-amlr-6amld-major-compliance-reforms-to-anticipate-in-2026

### 5.8 EBA Reporting Framework 4.2 — Structural Changes

> EBA reporting framework 4.2 applies from Q4 2025. Operational risk (COREP): new reporting requirements under CRR3 covering operational risk own funds requirements, expected June 2026. FINREP updates including IFRS 18 adjustments, expected March 2026. xBRL-CSV adoption moved to March 31, 2026, replacing xBRL-XML format.

Source: EBA, "Reporting Framework 4.2." https://www.eba.europa.eu/risk-and-data-analysis/reporting-frameworks/reporting-framework-42

### 5.9 RBI CIMS Migration

> RBI is transitioning statutory returns reporting from the legacy XBRL Portal to its new Centralised Information Management System (CIMS). Form A (fortnightly) submission to CIMS began June 14, 2024. Form VIII (monthly) began May 2024. Form IX (annual) began December 31, 2024. Internet Banking and Mobile Banking returns began from August 2025.

Source: TaxGuru, "RBI CIMS Project: Submission of Statutory Returns." https://taxguru.in/rbi/rbi-cims-project-submission-of-statutory-returns-form-a-viii-ix-cims-portal.html

### 5.10 CFPB Section 1033 — Compliance Phases

> Compliance is phased based on institution size: April 1, 2026 (largest institutions); April 1, 2027, 2028, 2029 (mid-size, staggered); April 1, 2030 (small depository institutions). Depository institutions with $850 million or less in assets are exempt.

> Covered data includes payment initiation information (account numbers), terms and conditions, transaction and account balance information (up to 24 months). Excluded: data collected solely for fraud prevention or regulatory compliance.

Source: Orrick, "The CFPB's Final Rule on Personal Financial Data Rights" (October 2024). https://www.orrick.com/en/Insights/2024/10/The-CFPB-Final-Rule-on-Personal-Financial-Data-Rights-What-Financial-Institutions-Should-Know

### 5.11 Corporate Transparency Act — Legal Limbo

> As of January 24, 2025, FinCEN confirmed that companies are not required to file beneficial ownership information reports while the January 7 injunction remains in force. A January 20 executive order freezing new rule issuances has created uncertainty about whether FinCEN can announce new filing deadlines.

Source: American Bar Association, "The Corporate Transparency Act Is Still on Pause, but Less So" (February 2025). https://www.americanbar.org/groups/business_law/resources/business-law-today/2025-february/corporate-transparency-act-still-on-pause-but-less-so/

---

## 6. Source Index

| # | Source | Type | URL | Verified |
|---|---|---|---|---|
| 1 | FFIEC BSA/AML Examination Manual — SAR Requirements | Official examination manual | https://bsaaml.ffiec.gov/manual/AssessingComplianceWithBSARegulatoryRequirements/04 | Yes |
| 2 | FinCEN SAR FAQs (October 2025) | Official guidance | https://www.fincen.gov/system/files/2025-10/SAR-FAQs-October-2025.pdf | Yes |
| 3 | OCC Bulletin 2025-31 — BSA/AML SAR FAQs | Official bulletin | https://occ.gov/news-issuances/bulletins/2025/bulletin-2025-31.html | Yes |
| 4 | Reuters Practical Law — BSA Compliance Issues (March 2025) | Legal analysis | https://www.reuters.com/practical-law-the-journal/transactional/bank-secrecy-act-compliance-issues-2025-03-01/ | Yes |
| 5 | FinCEN Beneficial Ownership Information | Official regulatory | https://www.fincen.gov/boi | Yes |
| 6 | FinCEN CDD Rule (2016) | Official regulation | https://www.federalregister.gov/documents/2016/05/11/2016-10567/customer-due-diligence-requirements-for-financial-institutions | Yes |
| 7 | FinCEN Whistleblower Program | Official | https://www.fincen.gov/whistleblower-program | Yes |
| 8 | Arnold & Porter — FinCEN Whistleblower Webpage (Feb 2026) | Law firm analysis | https://www.arnoldporter.com/en/perspectives/blogs/enforcement-edge/2026/02/fincen-launches-new-whistleblower-webpage | Yes |
| 9 | OFAC Civil Penalties and Enforcement | Official | https://ofac.treasury.gov/civil-penalties-and-enforcement-information | Yes |
| 10 | Hunton — OFAC Continuous Sanctions Monitoring | Law firm analysis | https://www.hunton.com/insights/legal/ofac-to-banks-implement-continuous-sanctions-monitoring | Yes |
| 11 | CheckLynx — Sanctions Screening 2026 Best Practices | Industry analysis | https://checklynx.com/en/resources/knowledge-base/sanction-screening | Yes |
| 12 | ION Group — Sanctions Screening Compliance 2026 | Industry guide | https://iongroup.com/blog/treasury/sanctions-screening-and-compliance-a-2026-guide/ | Yes |
| 13 | Interagency Third-Party Risk Management Guidance (2023) | Official regulation | https://www.occ.treas.gov/news-issuances/news-releases/2023/nr-ia-2023-53.html | Yes |
| 14 | OCC Heightened Standards (12 CFR 30, Appendix D) | Official regulation | https://www.law.cornell.edu/cfr/text/12/appendix-D_to_part_30 | Yes |
| 15 | SEC Press Release 2024-98 — Off-Channel Communications | Official enforcement | https://www.sec.gov/newsroom/press-releases/2024-98 | Yes |
| 16 | FINRA — Off-Channel Communications SRO Consequences | Official | https://www.finra.org/media-center/blog/sec-off-channel-communications-settlements-sro-collateral-consequences | Yes |
| 17 | CFPB Regulation F — Debt Collection Practices | Official regulation | https://www.consumerfinance.gov/rules-policy/final-rules/debt-collection-practices-regulation-f/ | Yes |
| 18 | CFPB Circular 2023-03 — Adverse Action and AI | Official guidance | https://www.consumerfinance.gov/compliance/circulars/circular-2023-03-adverse-action-notification-requirements-and-the-proper-use-of-the-cfpbs-sample-forms-provided-in-regulation-b/ | Yes |
| 19 | CFPB Section 1033 — Personal Financial Data Rights | Official compliance resource | https://www.consumerfinance.gov/compliance/compliance-resources/other-applicable-requirements/personal-financial-data-rights/ | Yes |
| 20 | CFPB Section 1033 Final Rule (PDF) | Official rule text | https://files.consumerfinance.gov/f/documents/cfpb_personal-financial-data-rights-final-rule_2024-10.pdf | Yes |
| 21 | Orrick — CFPB Final Rule Analysis (Oct 2024) | Law firm analysis | https://www.orrick.com/en/Insights/2024/10/The-CFPB-Final-Rule-on-Personal-Financial-Data-Rights-What-Financial-Institutions-Should-Know | Yes |
| 22 | RBI Master Direction — KYC Direction 2016 | Official regulation | https://www.rbi.org.in/Scripts/BS_CircularIndexDisplay.aspx?Id=12089 | Yes |
| 23 | FIU-IND AML/CFT Guidelines (July 2023) | Official guidelines | https://fiuindia.gov.in/pdfs/AML_legislation/AMLCFTguidelines04072023.pdf | Yes |
| 24 | RBI Master Directions on Fraud Risk Management (July 2024) | Official regulation | https://www.rbi.org.in/scripts/NotificationUser.aspx?Id=12703&Mode=0 | Yes |
| 25 | KPMG — RBI Fraud Risk Management Boardroom Briefing (Sep 2024) | Industry analysis | https://assets.kpmg.com/content/dam/kpmgsites/in/pdf/2024/09/boardroom-briefing-rbis-new-guidelines-on-strengthening-fraud-risk-management.pdf | Yes |
| 26 | IndiaLaw — RBI Revised Fraud Directions | Legal analysis | https://www.indialaw.in/blog/banking-and-finance/rbi-issues-revised-master-directions-on-fraud/ | Yes |
| 27 | RBI — List of All Returns | Official | https://www.rbi.org.in/Scripts/BS_Listofallreturns.aspx?id=14 | Yes |
| 28 | TaxGuru — RBI CIMS Statutory Returns | Industry analysis | https://taxguru.in/rbi/rbi-cims-project-submission-of-statutory-returns-form-a-viii-ix-cims-portal.html | Yes |
| 29 | RBI — CIMS Internet/Mobile Banking Returns (Sep 2025) | Official notification | https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12895 | Yes |
| 30 | RBI Master Direction — Filing of Supervisory Returns | Official regulation | https://www.rbi.org.in/scripts/BS_ViewMasDirections.aspx?id=12613 | Yes |
| 31 | India DPDP Act 2023 | Official legislation | https://www.meity.gov.in/static/uploads/2024/06/2a5ef610a85e2b05965a5a6bbd7e4c25.pdf | Yes |
| 32 | CADP — DPDP Implementation Tracker 2026 | Industry tracker | https://cadp.in/resources/guides/dpdp-implementation-tracker/ | Yes |
| 33 | ZCyberSecurity — DPDP Act Impact on Banking | Industry analysis | https://zcybersecurity.com/understanding-dpdp-act-for-banks-financial-institutions/ | Yes |
| 34 | TCSA — DPDP Compliance for BFSI | Industry analysis | https://www.tcsa.in/resources/dpdp-compliance-bfsi-rbi-guidelines | Yes |
| 35 | CERT-In Directions (Section 70B) | Official regulation | https://cert-in.org.in/Directions70B.jsp | Yes |
| 36 | 6AMLD (Directive EU 2024/1640) | Official legislation | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX%3A32024L1640 | Yes |
| 37 | AMLR (Regulation EU 2024/1624) | Official legislation | https://anti-money-laundering.eu/regulation-eu-2024-1624/ | Yes |
| 38 | B4Finance — AMLA/AMLR/6AMLD Reforms 2026 | Industry analysis | https://www.b4finance.com/blog/amla-amlr-6amld-major-compliance-reforms-to-anticipate-in-2026 | Yes |
| 39 | AMLD5 (Directive 2018/843) | Official legislation | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32018L0843 | Yes |
| 40 | DORA (Regulation EU 2022/2554) | Official legislation | https://eur-lex.europa.eu/eli/reg/2022/2554 | Yes |
| 41 | EBA Reporting Framework 4.2 | Official | https://www.eba.europa.eu/risk-and-data-analysis/reporting-frameworks/reporting-framework-42 | Yes |
| 42 | FCA Consumer Duty (PRIN 2A) | Official handbook | https://www.handbook.fca.org.uk/handbook/PRIN/2A.htm | Yes |
| 43 | PRA SS1/21 — Operational Resilience | Official | https://bankofengland.co.uk/prudential-regulation/publication/2021/march/operational-resilience-impact-tolerances-for-important-business-services-ss | Yes |
| 44 | ABA — Transaction-Level ACH Screening | Industry guidance | https://www.aba.com/-/media/documents/industry-insights/fincom-transaction-level-ach-screening.pdf | Yes |
| 45 | Mayer Brown — CTA Supreme Court Stay (Jan 2025) | Law firm analysis | https://www.mayerbrown.com/en/insights/publications/2025/01/not-quite-yet-supreme-court-stays-cta-injunction-but-filing-requirements-remain-suspended | Yes |
| 46 | ABA — CTA Still on Pause (Feb 2025) | Legal analysis | https://www.americanbar.org/groups/business_law/resources/business-law-today/2025-february/corporate-transparency-act-still-on-pause-but-less-so/ | Yes |

---

*End of S2 regulatory landscape research for Banking Operations. All data points sourced from cited references as of March 15, 2026. Items marked [unverified] require manual confirmation from primary regulatory sources.*
