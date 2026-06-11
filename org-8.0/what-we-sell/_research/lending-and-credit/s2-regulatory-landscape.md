# S2 — Regulatory Landscape and Lending Mandates

**Research date:** March 2026
**Engagement area:** Lending and Credit

---

## Data Table

| # | Regulation | Jurisdiction | Requirement | Infrastructure Impact | Deadline/Status | Penalty | Source URL | Verified |
|---|-----------|-------------|-------------|----------------------|-----------------|---------|------------|----------|
| 1 | ECOA / Regulation B | USA | Specific adverse action notices for AI/ML-based denials; no AI exemption | Explainability layer for ML credit models; reason-code generation from black-box models | Active — ongoing obligation | Up to $10K per violation (individual); $500K–$1M class action; punitive damages unlimited | [CFPB guidance](https://www.consumerfinance.gov/about-us/newsroom/cfpb-issues-guidance-on-credit-denials-by-lenders-using-artificial-intelligence/) | Yes |
| 2 | Fair Housing Act / HMDA | USA | Data collection & reporting on race, ethnicity, sex, income for mortgage lending; disparate impact analysis | HMDA data pipeline, LAR reporting infrastructure, fair-lending analytics | Annual filing; 2026 FIG published | $12M penalty (Bank of America 2023); $200K (Washington Federal) | [CFPB HMDA resources](https://www.cfpb.gov/compliance/compliance-resources/mortgage-resources/hmda-reporting-requirements/) | Yes |
| 3 | CRA (2023 modernization) | USA | Expanded assessment areas for digital/online lending; metrics-based evaluation; emphasis on LMI communities | Geocoding engines, digital-channel activity tracking, CRA-qualified loan tagging, expanded data warehousing | January 1, 2026 (all provisions) | Unsatisfactory rating blocks mergers/acquisitions; reputational damage; restrictions on branch expansion | [OCC CRA final rule overview](https://occ.gov/news-issuances/news-releases/2023/nr-ia-2023-117b.pdf) | Yes |
| 4 | TILA / Regulation Z | USA | APR disclosure, fee transparency, periodic statements; BNPL products treated as credit under CFPB guidance | Disclosure-generation engines; BNPL integration with TILA-compliant statement systems | Active — ongoing obligation | Statutory damages $500–$4K individual; $500K–$1M class; actual damages; attorney fees | [15 U.S.C. § 1640](https://www.law.cornell.edu/uscode/text/15/1640) | Yes (statute) |
| 5 | RESPA / Regulation X | USA | Mortgage servicing rules; loss mitigation procedures; escrow management; error-resolution timelines | Servicing platform compliance modules; loss mitigation workflow engines; escrow accounting systems | Active — ongoing obligation | Statutory damages up to $2K individual; class action damages; actual damages; pattern-or-practice penalties | [12 U.S.C. § 2605](https://www.law.cornell.edu/uscode/text/12/2605) | Yes (statute) |
| 6 | CFPB Section 1071 (small business lending data) | USA | Collect & report race, ethnicity, gender of small-business loan applicants | New data-collection fields in LOS; demographic capture UI; reporting data warehouse | Tier 1: July 1, 2026; Tiers 2–3: 2027–2028; currently stayed by Fifth Circuit | Civil money penalties; consent orders | [CFPB 1071 rule page](https://www.consumerfinance.gov/1071-rule/) | Yes |
| 7 | CFPB AI adverse action guidance | USA | Lenders using AI/ML must provide specific, accurate adverse action reasons — not generic checklist items | Model explainability infrastructure; reason-code mapping for complex ML outputs | Active | Enforcement via ECOA/Reg B penalties | [CFPB newsroom](https://www.consumerfinance.gov/about-us/newsroom/cfpb-issues-guidance-on-credit-denials-by-lenders-using-artificial-intelligence/) | Yes |
| 8 | CFPB Automated Valuation Models rule | USA | Quality control for AI/ML-based home appraisals; nondiscrimination; accuracy testing | AVM validation frameworks; bias-testing infrastructure; random-sample testing pipelines | Effective June 2024 | Enforcement actions; consent orders | [CFPB AVM rule (via consumerfinanceinsights.com)](https://www.consumerfinanceinsights.com/2024/07/11/cfpb-issues-new-rule-on-use-of-artificial-intelligence-models-in-mortgage-lending/) | Yes |
| 9 | SR 11-7 / OCC 2011-12 | USA | Model risk management: governance, validation, monitoring for all quantitative models incl. AI/ML | MRM frameworks; model inventory systems; independent validation teams; bias & fairness testing | Active — ongoing supervisory expectation | Supervisory action; MRA/MRIA findings; consent orders | [Fed SR 11-7](https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm) | Yes |
| 10 | Dodd-Frank Section 1033 (open banking) | USA | Consumer data portability; third-party data access for credit assessment | API infrastructure for data sharing; consent management; alternative credit data ingestion | Enjoined Oct 2025; CFPB rewriting | N/A — rule not enforceable pending rewrite | [Court injunction analysis (MVA Law)](https://www.mvalaw.com/data-points/cfpb-enjoined-from-enforcing-personal-financial-data-rights-rule-1033) | Yes |
| 11 | RBI Digital Lending Directions 2025 | India | Mandatory bank intermediation; no LSP pass-through accounts; DLG caps; KYC & creditworthiness assessment | Direct disbursement/repayment APIs; LSP due-diligence systems; DLA directory; grievance portals | Most provisions active; multi-lender: Nov 1, 2025; DLA directory: Jun 15, 2025 | License revocation; supervisory action; directions under Sec 35A of BR Act | [RBI notification](https://www.rbi.org.in/scripts/FS_Notification.aspx?Id=12382&Mode=0&fn=2) | Yes |
| 12 | RBI Account Aggregator Directions 2025 | India | Consent-based financial data sharing via NBFC-AAs; ₹2Cr minimum NOF; FIP/FIU integration | AA integration APIs; consent-management infrastructure; credit-underwriting data pipelines | Effective Nov 28, 2025 | RBI supervisory action; registration cancellation | [RBI Master Directions](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=10598) | Yes |
| 13 | RBI Co-Lending Arrangements Directions 2025 | India | Expanded co-lending framework beyond PSL; 80:20 risk sharing; Board-approved policies | Co-lending platform infrastructure; real-time loan-booking APIs; shared servicing systems | Effective Jan 1, 2026 | Supervisory action; restrictions on co-lending activity | [RBI Master Directions](https://rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12888) | Yes |
| 14 | RBI Priority Sector Lending norms | India | PSL targets (40% ANBC for commercial banks; 60% for SFBs from FY26); sub-sector allocations | PSL tracking systems; loan classification engines; RIDF deposit management | FY26 targets active; SFB target reduced from 75% to 60% | Shortfall deposited in RIDF/SIDBI at below-market rates | [RBI PSL Master Directions](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12799) | Yes |
| 15 | RBI Credit Information Companies Directions 2025 | India | Fixed-date data submissions (9th, 16th, 23rd, last day); Data Quality Index; free annual credit report | High-frequency bureau reporting pipelines; DQI computation; DAKSH portal integration | Effective Nov 28, 2025; amendment provisions Jul 1, 2026 | Reporting on DAKSH portal; supervisory action | [RBI CIC Directions](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12764) | Yes |
| 16 | FCA Consumer Duty | UK | Fair value assessments; product design for target markets; vulnerable customer protections; outcomes monitoring | Fair-value assessment engines; product-governance systems; outcomes-monitoring dashboards; MI reporting | Live Jul 31, 2023 (open products); Jul 31, 2024 (closed products) | FCA enforcement powers: unlimited fines; product withdrawal orders; s166 reviews | [FCA Consumer Duty review](https://fca.org.uk/publications/good-and-poor-practice/consumer-duty-findings-our-review-fair-value-frameworks) | Yes |
| 17 | FCA MCOB (mortgage conduct) | UK | Affordability assessments; arrears management; disclosure requirements; execution-only standards | Mortgage origination platforms; affordability calculators; arrears workflow engines | Active; Jul 2025 rule review amendments | FCA enforcement: fines; permissions variation; public censure | [FCA Handbook MCOB](https://www.handbook.fca.org.uk/handbook/MCOB.pdf) | Yes |
| 18 | PRA SS1/23 (model risk management) | UK | Five-principle MRM framework; model inventory; independent validation; AI/ML-specific governance | MRM platforms; model inventory systems; validation infrastructure; AI/ML bias testing | Effective May 2024 | PRA supervisory action; s166 skilled-person reviews; capital add-ons | [BoE SS1/23](https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss) | Yes |
| 19 | FCA/PRA FS2/23 (AI/ML feedback) | UK | No binding rules yet; signals direction toward AI governance, bias testing, third-party model oversight | Anticipatory investment in AI governance frameworks; third-party model risk assessment | Feedback stage — no binding deadline | N/A (guidance stage) | [BoE FS2/23](https://www.bankofengland.co.uk/prudential-regulation/publication/2023/october/artificial-intelligence-and-machine-learning) | Yes |
| 20 | Data (Use and Access) Act 2025 / Smart Data | UK | Statutory basis for open banking; framework for credit data portability; Smart Data schemes | Open Finance APIs; credit data sharing infrastructure; consent management for lending data | Royal Assent Jun 19, 2025; secondary legislation pending | Statutory enforcement powers via designated regulators | [Data (Use and Access) Bill factsheet](https://www.gov.uk/government/publications/data-use-and-access-bill-factsheets/data-use-and-access-bill-factsheet-growing-the-economy) | Yes |

---

## USA Regulatory Landscape

### ECOA / Regulation B

**Statute:** Equal Credit Opportunity Act, 15 U.S.C. §§ 1691–1691f; implemented by Regulation B (12 CFR Part 1002).

**What it demands:**
- Prohibits discrimination in any aspect of a credit transaction on the basis of race, color, religion, national origin, sex, marital status, age, receipt of public assistance, or exercise of rights under the Consumer Credit Protection Act.
- **Adverse action notices** must state specific reasons for denial or adverse action. The CFPB has clarified (September 2022 guidance) that lenders using AI/ML models must provide specific and accurate reasons — generic checklist items are insufficient. There is "no special exemption for artificial intelligence."
- A proposed Regulation B amendment (December 2025) addresses whether ECOA authorizes disparate impact claims; the CFPB under current administration has proposed limiting disparate impact liability.

**Infrastructure investment forced:**
- **Model explainability layers:** Banks using ML credit models must generate human-readable reason codes from complex, non-linear algorithms. This requires investment in SHAP/LIME-type explainability tooling or inherently interpretable model architectures.
- **Adverse action notice generation systems** must dynamically map model outputs to ECOA-compliant reason codes rather than relying on static checklists.
- **Fair lending testing infrastructure** for pre-deployment and ongoing bias monitoring.

**Penalty regime:**
- Individual: up to $10,000 in punitive damages per violation.
- Class action: lesser of $500,000 or 1% of net worth.
- Actual damages, attorney fees, and injunctive relief.
- Enforcement consent orders can require multi-million-dollar remediation programs.

**Bank tiers most affected:** All tiers — but AI/ML model explainability requirements disproportionately affect large and mid-tier banks deploying complex credit models. Community banks using traditional scorecards face lower burden.

**Source:** [CFPB ECOA/Reg B guidance on AI credit denials](https://www.consumerfinance.gov/about-us/newsroom/cfpb-issues-guidance-on-credit-denials-by-lenders-using-artificial-intelligence/) | [Skadden analysis](https://www.skadden.com/insights/publications/2024/01/cfpb-applies-adverse-action-notification-requirement) | [CFPB Reg B proposed amendment (Dec 2025)](https://consumerfed.org/wp-content/uploads/2025/12/CFA-ECOA-comment-CFPB-2025-0039-RIN-3170-AB54_.pdf)

---

### Fair Housing Act and HMDA

**Statutes:** Fair Housing Act, 42 U.S.C. §§ 3601–3631; Home Mortgage Disclosure Act, 12 U.S.C. §§ 2801–2810; implemented by Regulation C (12 CFR Part 1003).

**What it demands:**
- HMDA requires financial institutions to collect and report data on mortgage loan applications, including demographic information (race, ethnicity, sex), loan characteristics, property details, and disposition. Data is filed annually via the FFIEC HMDA Platform.
- Fair Housing Act prohibits discrimination in mortgage lending; federal regulators conduct disparate impact analyses using HMDA data.
- In 2025, federal banking agencies revised fair lending examination guidance to clarify the scope of disparate impact scrutiny — currently de-emphasizing facial-neutrality challenges.

**Infrastructure investment forced:**
- **Loan Application Register (LAR) data pipelines:** Automated capture of 110+ data fields per application from origination systems.
- **HMDA quality-control engines:** Institutions must run edit checks (syntactical, validity, quality, macro) before filing.
- **Fair lending analytics platforms:** Statistical testing for disparate treatment and disparate impact across protected classes.
- **Geocoding and census-tract mapping** for property location reporting.

**Penalty regime:**
- Bank of America: $12M civil money penalty (2023) for reporting violations.
- Washington Federal: $200K penalty for 2016–2017 data errors.
- Consent orders require compliance management system overhauls and ongoing annual reporting.

**Bank tiers most affected:** Institutions originating 25+ closed-end mortgage loans or 200+ open-end lines of credit in each of the two preceding calendar years must report.

**Source:** [CFPB HMDA resources](https://www.cfpb.gov/compliance/compliance-resources/mortgage-resources/hmda-reporting-requirements/) | [HMDA data collection timelines](https://ffiec.cfpb.gov/documentation/faq/data-collection-timelines) | [2026 FIG](https://business.cch.com/BFLD/HMDA-2026-Filing-Instructions-Guide-10082025.pdf) | [ComplianceTech 2025 recap](https://compliancetech.com/2025-recap/)

---

### Community Reinvestment Act (CRA) — 2023 Modernization

**Statute:** Community Reinvestment Act of 1977; 2023 final rule jointly issued by Fed, FDIC, OCC (October 24, 2023).

**What it demands:**
- First major update since 1995. Modernizes assessment areas to account for online, mobile, and hybrid banking delivery.
- Introduces metrics-based benchmarks using peer and demographic data for retail lending performance evaluation.
- Tailored standards by bank size: small banks (<$600M assets) may continue under legacy framework or opt in; large banks face expanded data and reporting requirements.
- Greater emphasis on LMI communities, small businesses, small farms, MDIs, and CDFIs.

**Infrastructure investment forced:**
- **Digital-channel activity tracking:** Banks must now demonstrate CRA performance in geographies where they have significant digital lending activity, not just branch footprints.
- **Geocoding and assessment area engines:** Expanded mapping of where digital lending activity occurs.
- **CRA-qualified loan tagging** in origination systems to identify qualifying activities.
- **Data warehousing and reporting** for new metrics-based evaluation framework.
- **Community development activity tracking** platforms.

**Deadline:** All substantive provisions effective **January 1, 2026** (extended from April 2024).

**Penalty regime:**
- No direct fines, but consequences are severe: unsatisfactory CRA ratings can block mergers, acquisitions, and branch openings. Reputational damage. Restrictions on deposit-taking activities.
- Regulatory examination ratings published publicly.

**Bank tiers most affected:** Large banks (>$2B assets) and intermediate small banks ($600M–$2B) face the heaviest new reporting and data requirements. Community banks (<$600M) have opt-in flexibility.

**Source:** [OCC interagency overview](https://occ.gov/news-issuances/news-releases/2023/nr-ia-2023-117b.pdf) | [FDIC FIL-2023-061](https://fdic.gov/news/financial-institution-letters/2023/fil23061.html) | [OCC supplemental final rule](https://occ.gov/news-issuances/bulletins/2024/bulletin-2024-9.html) | [Fed extension notice](https://www.federalreserve.gov/newsevents/pressreleases/bcreg20240321a.htm)

---

### Truth in Lending Act (TILA) / Regulation Z

**Statute:** Truth in Lending Act, 15 U.S.C. §§ 1601–1667f; implemented by Regulation Z (12 CFR Part 1026).

**What it demands:**
- Standardized disclosure of credit terms: APR, finance charges, total of payments, payment schedule.
- Specific disclosure requirements for closed-end credit, open-end (revolving) credit, and mortgage transactions (Loan Estimate and Closing Disclosure forms under TRID).
- **BNPL implications:** The CFPB issued an interpretive rule in May 2022 classifying certain BNPL products (pay-in-four, deferred interest) as "credit cards" under Reg Z, requiring billing statements, dispute resolution rights, and refund protections. Current administration has not formally rescinded this interpretation but enforcement posture is uncertain.

**Infrastructure investment forced:**
- **Disclosure-generation engines** that dynamically calculate and render compliant APR, fee, and payment disclosures across loan products.
- **TRID compliance modules** for mortgage origination systems (Loan Estimate within 3 business days of application; Closing Disclosure 3 business days before closing).
- **BNPL compliance systems** — if interpretive rule stands, BNPL providers must build billing statement generation, dispute resolution workflows, and refund processing infrastructure.

**Penalty regime:**
- Individual statutory damages: $500–$4,000 (depending on violation type).
- Class action: lesser of $500,000 or 1% of net worth.
- Actual damages and attorney fees recoverable.
- Mortgage-specific rescission right for material disclosure failures (up to 3 years).

**Bank tiers most affected:** All creditors. BNPL implications most relevant to fintechs and banks offering point-of-sale financing.

**Source:** [15 U.S.C. § 1640 (TILA penalties)](https://www.law.cornell.edu/uscode/text/15/1640) | [12 CFR Part 1026 (Regulation Z)](https://www.law.cornell.edu/cfr/text/12/part-1026) | CFPB BNPL interpretive rule: [CFPB newsroom, May 2022](https://www.consumerfinance.gov/about-us/newsroom/cfpb-takes-action-to-ensure-consumers-can-dispute-charges-and-demand-refunds-on-buy-now-pay-later-loans/) `[unverified — URL reconstructed from known CFPB announcement; needs manual confirmation]`

---

### RESPA / Regulation X

**Statute:** Real Estate Settlement Procedures Act, 12 U.S.C. §§ 2601–2617; implemented by Regulation X (12 CFR Part 1024).

**What it demands:**
- Mortgage servicing rules: error-resolution procedures (respond within 5 business days of receipt, resolve within 30 days), information-request responses, force-placed insurance limitations.
- **Loss mitigation requirements:** Servicers must evaluate borrowers for all available loss mitigation options within 30 days of receiving a complete application. Must not initiate foreclosure if application received 37+ days before scheduled sale.
- Early intervention requirements for delinquent borrowers (written notice by 45th day; live contact attempts).
- Escrow account management and periodic statement requirements.

**Infrastructure investment forced:**
- **Servicing platform compliance modules** with configurable loss-mitigation workflow engines.
- **Escrow accounting systems** with regulatory-compliant calculation logic.
- **Error-resolution tracking systems** with SLA management and audit trails.
- **Early intervention communication engines** (automated outreach, tracking, and documentation).
- **Document management systems** for loss mitigation applications.

**Penalty regime:**
- Individual statutory damages up to $2,000.
- Class action: actual and statutory damages (no cap specified in statute for pattern-or-practice).
- Actual damages for servicer failures.
- Consent orders and compliance management requirements.

**Bank tiers most affected:** Mortgage servicers of all sizes; largest servicers face greatest operational complexity due to portfolio scale.

**Source:** [12 U.S.C. § 2605 (RESPA servicing)](https://www.law.cornell.edu/uscode/text/12/2605) | [12 CFR Part 1024 (Regulation X)](https://www.law.cornell.edu/cfr/text/12/part-1024)

---

### CFPB Section 1071 — Small Business Lending Data Collection

**Statute:** Dodd-Frank Act Section 1071; Final rule issued March 2023; compliance dates extended October 2025.

**What it demands:**
- Lenders must collect and report data on small-business credit applications, including:
  - Race, ethnicity, and sex of principal owners
  - Revenue, NAICS code, number of workers
  - Application disposition and credit decision
  - Pricing information
- Modeled on HMDA's demographic data collection for mortgage lending, but applied to small business credit.

**Infrastructure investment forced:**
- **New data-collection fields** integrated into small-business loan origination systems.
- **Demographic capture UI** with applicant-facing forms and opt-out mechanisms.
- **Reporting data warehouse** for annual CFPB submission.
- **Quality-control and edit-check engines** (similar to HMDA infrastructure).
- **Data privacy and firewall controls** separating demographic data from credit decisioning.

**Current status:** The Fifth Circuit Court of Appeals granted a stay of the rule in February 2025. The CFPB under the Trump administration declined to defend the rule. Compliance dates extended: Tier 1 (>2,500 originations): **July 1, 2026**; Tier 2 (>500): January 1, 2027; Tier 3 (>100): October 1, 2027. However, the stay means these dates may slip further. In November 2025, the CFPB issued a proposed rule to reconsider certain provisions.

**Penalty regime:** Civil money penalties under CFPB enforcement authority; consent orders. Community groups filed suit in July 2025 to force implementation.

**Bank tiers most affected:** Lenders originating 100+ small-business loans annually. Largest lenders (Tier 1: >2,500 originations) face earliest deadlines.

**Source:** [CFPB 1071 rule page](https://www.consumerfinance.gov/1071-rule/) | [American Banker — Fifth Circuit stay](https://www.americanbanker.com/news/fifth-circuit-halts-cfpb-small-business-data-rule-again) | [ICBA analysis](https://www.icba.org/newsroom/news-and-articles/2025/02/10/cfpb-s-1071-rule-again-paused-by-court-in-icba-case) | [Consumer Finance Monitor — compliance dates](https://www.consumerfinancemonitor.com/2025/10/02/cfpb-adopts-final-rule-extending-compliance-dates-for-the-1071-rule/)

---

### CFPB AI/ML in Lending — Supervisory Highlights and AVM Rule

**Guidance:** CFPB Supervisory Highlights (January 2025); Automated Valuation Models (AVM) rule (June 2024, jointly with OCC, Fed, FDIC, NCUA, FHFA).

**What it demands:**
- **Adverse action notices for AI models:** Lenders must cite specific factors that actually drove denial, even when using opaque ML models. Generic reason codes are non-compliant.
- **AVM rule:** Quality-control standards for AI/ML-based home appraisals including accuracy verification, data manipulation prevention, conflict-of-interest controls, random sample testing, and nondiscrimination compliance.
- **Supervisory findings (Jan 2025):** Auto lenders failed to validate adverse action methodologies for AI/ML models; credit card lenders showed disparate outcomes for Black and Hispanic applicants from certain credit scoring models.

**Infrastructure investment forced:**
- **Model explainability platforms** (SHAP, LIME, or inherently interpretable architectures).
- **Reason-code generation engines** that translate complex model outputs to ECOA/FCRA-compliant adverse action reasons.
- **AVM validation infrastructure:** Bias testing suites, random-sample audit pipelines, accuracy benchmarking.
- **Pre-deployment fairness testing** across protected classes.
- **Ongoing model monitoring** with drift detection and fairness metric tracking.

**Penalty regime:** Enforcement through ECOA, FCRA, and FHA penalty frameworks; consent orders; supervisory MRAs.

**Bank tiers most affected:** Large and mid-tier banks deploying AI/ML credit models; mortgage originators using AVMs.

**Source:** [CFPB AI credit denial guidance](https://www.consumerfinance.gov/about-us/newsroom/cfpb-issues-guidance-on-credit-denials-by-lenders-using-artificial-intelligence/) | [CFPB AVM rule](https://www.consumerfinanceinsights.com/2024/07/11/cfpb-issues-new-rule-on-use-of-artificial-intelligence-models-in-mortgage-lending/) | [CFPB supervisory highlights on AI fair lending](https://www.consumerfinancialserviceslawmonitor.com/2025/01/cfpb-highlights-fair-lending-risks-in-advanced-credit-scoring-models/)

---

### SR 11-7 / OCC 2011-12 — Model Risk Management

**Guidance:** Federal Reserve SR 11-7 (April 2011); OCC Bulletin 2011-12; OCC Model Risk Management Handbook (2021, Bulletin 2021-39); OCC Bulletin 2025-26 (community bank clarification).

**What it demands:**
- All quantitative models used for material decisions — including AI/ML credit models — must be subject to:
  - **Governance:** Board-level oversight, clear policies, defined roles.
  - **Model development standards:** Documentation of methodology, data, assumptions, limitations.
  - **Independent validation:** Challenger models, back-testing, sensitivity analysis, outcomes monitoring.
  - **Ongoing monitoring:** Performance tracking, drift detection, periodic re-validation.
- External vendor models (including credit bureau scores and third-party ML models) must receive the same validation rigor as in-house models.
- 2025 clarification (OCC 2025-26): Community banks have flexibility to tailor validation frequency and scope to risk exposure — annual validation is not required.

**Infrastructure investment forced:**
- **Model inventory management systems** cataloging all models with risk tiers.
- **Model validation platforms** supporting challenger development, back-testing, sensitivity analysis.
- **Model documentation repositories** with version control.
- **Ongoing monitoring dashboards** tracking model performance metrics.
- **Independent validation teams** (in-house or third-party) with appropriate expertise for AI/ML models.
- **Vendor model assessment frameworks** for third-party credit scoring and decisioning tools.

**Penalty regime:** Supervisory findings: Matters Requiring Attention (MRA) or Matters Requiring Immediate Attention (MRIA). Consent orders in severe cases. No direct monetary fines specified in guidance, but regulatory actions can restrict business activities.

**Bank tiers most affected:** All banks, but proportionate to complexity. Large banks with extensive AI/ML model portfolios face heaviest burden. Community banks received explicit relief in 2025 guidance.

**Source:** [Fed SR 11-7](https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm) | [OCC 2025-26 community bank clarification](https://www.occ.treas.gov/news-issuances/bulletins/2025/bulletin-2025-26.html) | [ValidMind OCC 2011-12 guide](https://validmind.com/blog/mrm-teams-and-how-to-comply-with-occ-2011-12/) | [IBM evolution of OCC MRM expectations](https://www.ibm.com/think/insights/the-evolution-of-occ-expectations-for-model-risk-management)

---

### Dodd-Frank Section 1033 — Open Banking / Data Access

**Statute:** Dodd-Frank Act Section 1033; CFPB Personal Financial Data Rights Rule (finalized October 2024; enjoined October 2025).

**What it demands (when enforceable):**
- Financial institutions must share consumers' personal financial data with authorized third parties at no cost upon consumer request.
- Covers transaction data, account balances, and other financial information — enabling alternative credit data for lending decisions.
- Data providers must make information available in standardized, machine-readable formats.

**Current status:** **Enjoined.** On October 29, 2025, the U.S. District Court for the Eastern District of Kentucky issued a preliminary injunction. The CFPB under the Trump administration acknowledged the rule exceeded its statutory authority in May 2025 and announced new rulemaking in July 2025. An ANPRM was published in August 2025.

**Infrastructure investment forced (when implemented):**
- **Consumer data APIs** for standardized data sharing.
- **Consent management platforms** for third-party data access authorization.
- **Alternative credit data ingestion** — lenders could access bank transaction data, cash-flow data, and other non-traditional data to expand credit access.
- **Data security and authentication infrastructure** for third-party access.

**Penalty regime:** Currently unenforceable. When finalized, CFPB enforcement authority would apply.

**Bank tiers most affected:** Largest data providers (depository institutions) face first compliance deadlines; fintechs and alternative lenders benefit from data access.

**Cross-reference:** Payments S2 research (Claim #6) also covers Section 1033 status — noted as "enjoined; CFPB rewriting." Consistent with findings here.

**Source:** [MVA Law injunction analysis](https://www.mvalaw.com/data-points/cfpb-enjoined-from-enforcing-personal-financial-data-rights-rule-1033) | [Consumer Financial Services Law Monitor](https://www.consumerfinancialserviceslawmonitor.com/2025/07/cfpb-section-1033-open-banking-rule-stayed-as-cfpb-initiates-new-rulemaking/) | [Mondaq analysis](https://www.mondaq.com/unitedstates/financial-services/1702282/judge-delays-effective-dates-of-cfpbs-open-banking-rule) | [PYMNTS](https://www.pymnts.com/bank-regulation/2025/court-halts-cfpbs-open-banking-rule-as-banks-fintechs-await-rewrite)

---

### Interagency RFI on AI/ML in Financial Services (2021)

**Guidance:** Joint Request for Information issued March 2021 by Fed, OCC, FDIC, CFPB, and NCUA.

**What it demands:** No binding requirements — information-gathering exercise. Sought comment on governance, risk management, controls, and challenges for AI/ML adoption in financial services. Areas of interest included credit underwriting, fraud prevention, customer personalization.

**Infrastructure implication:** The RFI signals regulatory intent to formalize AI governance requirements. Banks that invested in AI governance frameworks post-RFI are better positioned for future rulemaking.

**Current status:** Comment period closed July 2021. No binding rulemaking has resulted yet, but supervisory expectations (SR 11-7 updates, CFPB AI guidance) reflect themes from the RFI.

**Source:** [OCC RFI](https://occ.gov/news-issuances/news-releases/2021/nr-ia-2021-54a.pdf) | [Federal Register](https://www.federalregister.gov/documents/2021/03/31/2021-06607/request-for-information-and-comment-on-financial-institutions-use-of-artificial-intelligence)

---

## India Regulatory Landscape

### RBI Digital Lending Directions, 2025

**Regulation:** RBI (Digital Lending) Directions, 2025 — issued May 8, 2025; consolidates September 2022 guidelines and June 2023 DLG norms.

**What it demands:**
- **Mandatory bank intermediation:** All loan disbursals and repayments must flow directly between borrower's bank account and the regulated entity (RE). No pass-through via LSPs or third parties.
- **Default Loss Guarantee (DLG/FLDG) caps:** DLG arrangements permitted but capped; LSPs must deposit guarantees as cash or bank guarantee equivalents.
- **LSP due diligence:** REs must assess LSP past conduct, data privacy practices, and technical capabilities.
- **Multi-lender transparency (effective Nov 1, 2025):** When multiple REs offer loans via an LSP, all matching offers must be displayed with lender name, amount, tenor, APR, and penal charges — presented without bias.
- **DLA directory reporting (effective Jun 15, 2025):** All Digital Lending Apps must be listed in a central directory.
- **Creditworthiness assessment** mandatory before disbursement.
- **Mandatory CIC reporting** and integration with RBI's Centralised Information Management System (CIMS).

**Infrastructure investment forced:**
- **Direct disbursement/collection APIs** between REs and borrower bank accounts — eliminates escrow/pool models.
- **LSP integration platforms** with due-diligence, monitoring, and compliance dashboards.
- **Multi-lender offer-comparison UI frameworks** with anti-bias controls.
- **DLA registry and directory systems.**
- **Grievance redressal portals** with prescribed escalation timelines.
- **CIC reporting pipelines** with high-frequency data submission.

**Penalty regime:** RBI enforcement powers under Section 35A of the Banking Regulation Act (for banks) and Chapter V of the RBI Act (for NBFCs). Includes: directions, license cancellation, restrictions on business activity. Specific fine amounts not prescribed in the Directions — RBI exercises discretionary supervisory action. `[unverified — specific penalty quantum needs manual confirmation from RBI master circulars]`

**Bank tiers most affected:** All banks and NBFCs engaged in digital lending. Disproportionate impact on fintechs operating as LSPs and on NBFCs heavily reliant on digital channels.

**Source:** [RBI notification](https://www.rbi.org.in/scripts/FS_Notification.aspx?Id=12382&Mode=0&fn=2) | [TaxGuru analysis](https://taxguru.in/rbi/reserve-bank-india-digital-lending-directions-2025.html) | [Mondaq overview](https://www.mondaq.com/india/financial-services/1632110/reserve-bank-of-india-digital-lending-directions-2025-brief-overview-analysis) | [Key changes analysis](https://taxguru.in/rbi/rbi-digital-lending-directions-2025-key-changes.html)

---

### RBI Account Aggregator Framework

**Regulation:** RBI (Non-Banking Financial Companies – Account Aggregator) Directions, 2025 — effective November 28, 2025.

**What it demands:**
- Only RBI-registered NBFC-Account Aggregators may facilitate consent-based financial data sharing between Financial Information Providers (FIPs, e.g., banks) and Financial Information Users (FIUs, e.g., lenders).
- Minimum Net Owned Funds of ₹2 crore for AA registration.
- AAs must not store, process, or sell customer data — they are consent brokers only.
- FIPs must make data available through AA infrastructure.
- FIUs (lenders) access data only with time-bound, purpose-specific, revocable customer consent.

**Scale:** As of December 2025, 252.9 million users have linked accounts across 754 operational FIUs. Cumulative lending through AA: ₹204 billion (2.1 million loans as of December 2023) with 170% YoY CAGR.

**Infrastructure investment forced:**
- **AA integration APIs** for both FIP (data provider) and FIU (data consumer) sides.
- **Consent management platforms** with granular consent flows (purpose, duration, data types, revocation).
- **Real-time credit underwriting pipelines** ingesting AA data for cash-flow-based lending.
- **Data security infrastructure** meeting AA data-handling standards (encrypted transit, no storage at AA).

**Penalty regime:** Registration cancellation; supervisory action by RBI. AAs permanently classified in Base Layer of NBFC Scale Based Regulation.

**Bank tiers most affected:** All banks (as FIPs must provide data); all NBFCs and banks using digital lending (as FIUs consuming data for credit assessment). Greatest strategic impact on entities building cash-flow-based lending models.

**Source:** [RBI Master Directions on NBFC-AA](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=10598) | [TaxGuru AA Directions 2025](https://taxguru.in/rbi/rbi-non-banking-financial-companies-account-aggregator-directions-2025.html) | [Government of India AA framework](https://financialservices.gov.in/beta/en/account-aggregator-framework) | [Sahamati lending via AA report](https://sahamati.org.in/wp-content/uploads/2024/02/Lending-through-AA-Dec23-Sahamati-Report.pdf)

---

### RBI Co-Lending Arrangements Directions, 2025

**Regulation:** RBI (Co-Lending Arrangements) Directions, 2025 — issued August 6, 2025; effective January 1, 2026.

**What it demands:**
- Expands the 2020 Co-Lending Model (CLM) beyond priority sector lending to all loan categories.
- Banks and NBFCs (including Housing Finance Companies) may jointly originate and hold loans.
- Minimum 20% risk retention by the NBFC on each individual loan until maturity.
- Board-approved co-lending policies required for both institutions.
- Single point of customer interface (typically the NBFC).

**Infrastructure investment forced:**
- **Co-lending platforms** with real-time loan booking and risk-sharing APIs.
- **Shared servicing infrastructure** — single-point customer interface while maintaining dual books of account.
- **Real-time data exchange** between banks and NBFCs for loan origination, servicing, and collections.
- **PSL tagging and reporting systems** — banks can claim PSL credit for their portion of co-lent loans.
- **Risk-sharing accounting modules** maintaining 80:20 (or other agreed) splits across loan lifecycle.

**Penalty regime:** RBI supervisory action; restrictions on co-lending activity for non-compliant entities.

**Bank tiers most affected:** Mid-tier banks seeking to expand reach via NBFC partnerships; NBFCs seeking lower-cost funding from banks. Large banks use co-lending as a channel to underserved segments.

**Source:** [RBI Master Directions on Co-Lending](https://rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12888) | [Mondaq analysis](https://www.mondaq.com/india/financial-services/1688146/the-co-lending-reset-what-rbis-co-lending-arrangements-directions-2025-signal-for-banks-and-nbfcs) | [Original 2020 CLM circular](https://rbi.org.in/Scripts/NotificationUser.aspx?Id=11991&Mode=0) | [TaxGuru features overview](https://taxguru.in/rbi/essential-features-co-lending-model-banks-nbfcs.html)

---

### RBI Priority Sector Lending (PSL) Norms

**Regulation:** RBI (Priority Sector Lending – Targets and Classification) Directions, as amended January 19, 2026.

**What it demands:**
- **Commercial banks:** 40% of Adjusted Net Bank Credit (ANBC) must be directed to priority sectors (agriculture, MSME, education, housing, social infrastructure, renewable energy, others).
- **Small Finance Banks:** Target reduced from 75% to 60% of ANBC effective FY2025-26.
- Sub-sector targets: agriculture (18%), micro enterprises (7.5%), weaker sections (12%), with incremental targets for small and marginal farmers and non-corporate farmers.
- External auditor certification requirements for PSL compliance.
- Caps and safeguards to prevent double-counting.

**Infrastructure investment forced:**
- **PSL classification engines** tagging loans against sector and sub-sector targets at origination.
- **ANBC computation modules** integrated with core banking for real-time target monitoring.
- **Shortfall calculation and RIDF deposit management** — automated identification of gaps and deposit routing.
- **Priority Sector Lending Certificates (PSLC) trading infrastructure** — banks can buy PSLCs from surplus institutions.
- **Reporting systems** aligned with revised population-based district classifications.

**Penalty regime:** Banks failing to meet PSL targets must deposit shortfall amounts with:
- RIDF (maintained by NABARD) at below-market interest rates, or
- Funds maintained by SIDBI, NHB, or MUDRA depending on shortfall category.
This represents an opportunity cost penalty — funds earn lower returns than market lending rates.

**Bank tiers most affected:** All scheduled commercial banks. Small Finance Banks most impacted (60% target, though reduced from 75%). Foreign banks with >20 branches have full targets; <20 branches have partial targets.

**Source:** [RBI PSL Master Directions](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12799) | [2026 PSL amendment](https://taxguru.in/rbi/rbi-priority-sector-lending-targets-classification-amendment-directions-2026.html) | [RBI SFB target reduction notification](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12875&Mode=0)

---

### RBI Credit Information Companies (CIC) Directions, 2025

**Regulation:** RBI (Credit Information Companies) Directions, 2025 — effective November 28, 2025; Amendment Directions effective July 1, 2026.

**What it demands:**
- Credit Institutions must submit data on **fixed reference dates:** 9th, 16th, 23rd, and last day of each month.
- Full-file submissions due by 5th of the following month; incremental submissions within four calendar days.
- CICs must implement uniform data validation rules, encryption standards, and online maintenance formats.
- **Data Quality Index (DQI)** scores required within three calendar days at file level.
- One free full credit report annually to every individual.
- Strengthened grievance redressal with compensation framework for delayed rectifications.
- CICs must report non-compliant credit institutions on **DAKSH portal** at half-yearly intervals.

**Infrastructure investment forced:**
- **High-frequency bureau reporting pipelines** — shift from monthly to near-weekly batch submissions.
- **DQI computation engines** — automated quality scoring at file level within 3-day turnaround.
- **Encryption and data-format standardization** across consumer, commercial, and microfinance segments.
- **DAKSH portal integration** for compliance reporting.
- **Grievance redressal workflow systems** with SLA tracking and compensation calculation.

**Penalty regime:** CICs report non-compliant credit institutions on DAKSH portal (public visibility of compliance failures). RBI supervisory action for persistent non-compliance.

**Bank tiers most affected:** All scheduled commercial banks, NBFCs, and microfinance institutions that are Credit Institutions under CICRA. Larger institutions face greater data-pipeline complexity.

**Source:** [RBI CIC Directions Master page](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12764) | [TaxGuru CIC Directions 2025](https://taxguru.in/rbi/rbi-credit-information-companies-directions-2025.html) | [Amendment Directions Dec 2025](https://taxguru.in/rbi/rbi-credit-information-companies-amendment-directions-2025.html) | [NBFC Compliance analysis](https://www.nbfccompliance.com/post/rbi-credit-information-companies-credit-bureau-amendment-directions-2025)

---

### RBI Fair Practices Code for NBFCs

**Regulation:** RBI Master Direction on Fair Practices Code for NBFCs (initially 2012; updated periodically; now subsumed into consolidated Digital Lending Directions 2025 for digital channel aspects).

**What it demands:**
- Transparent communication of loan terms, interest rates, and charges at the time of sanction.
- Standardized Key Facts Statement (KFS) to be provided to borrowers before contract execution.
- Prohibition on coercive recovery practices; adherence to prescribed recovery agent guidelines.
- Board-approved loan policies publicly available.
- Non-discrimination in lending based on religion, caste, or gender.

**Infrastructure investment forced:**
- **KFS generation engines** integrated with loan origination systems.
- **Recovery management systems** with regulatory-compliant communication templates.
- **Board-approved policy repositories** with website publication.
- **Customer complaint management systems** with prescribed escalation and resolution timelines.

**Penalty regime:** RBI supervisory action; directions; license-condition modifications. `[unverified — specific penalty quantum for Fair Practices Code violations needs manual confirmation]`

**Bank tiers most affected:** All NBFCs, including MFIs and HFCs. Digital lenders face additional layered requirements from Digital Lending Directions 2025.

**Source:** [RBI Master Directions (Fair Practices Code)](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=10598) `[unverified — this URL may point to AA directions; the specific Fair Practices Code Master Direction URL needs manual confirmation]`

---

## UK Regulatory Landscape

### FCA Consumer Duty

**Regulation:** FCA PS22/9: A new Consumer Duty — final rules published July 2022; in force July 31, 2023 (open products), July 31, 2024 (closed products).

**What it demands:**
- **Consumer Principle:** Firms must act to deliver good outcomes for retail customers.
- **Four outcomes:** Products and services, price and value, consumer understanding, consumer support.
- **Fair value assessments:** Firms must demonstrate that price paid is reasonable relative to benefits received — considering nature of product, limitations, total lifetime cost, and market comparators.
- **Target market identification:** Products must be designed with specific customer segments in mind; distribution must ensure products reach the right customers.
- **Vulnerable customers:** Specific protections and outcome monitoring for vulnerable customer groups.
- **Ongoing monitoring:** Firms must use data and MI to verify products continue meeting customer needs.

**Infrastructure investment forced:**
- **Fair-value assessment engines** performing product-level value analysis across fees, charges, and customer outcomes.
- **Product governance systems** with target market definition, distribution strategy monitoring, and ongoing product reviews.
- **Outcomes-monitoring dashboards** tracking customer outcomes data across the four outcome areas.
- **MI and reporting infrastructure** supporting Board-level Consumer Duty reporting.
- **Vulnerable customer identification and support systems.**

**Penalty regime:** FCA enforcement powers are extensive: unlimited fines, product withdrawal orders, s166 skilled-person reviews, requirements to provide redress, public censure, removal of permissions. The FCA has signaled Consumer Duty is a supervision priority.

**Bank tiers most affected:** All FCA-authorized firms offering lending products — banks, building societies, consumer credit firms, mortgage lenders. Smaller firms face proportionality flexibility but must still demonstrate compliance.

**Source:** [FCA fair value review findings](https://fca.org.uk/publications/good-and-poor-practice/consumer-duty-findings-our-review-fair-value-frameworks) | [FCA letter to mainstream consumer credit lenders](https://fca.org.uk/publication/correspondence/consumer-duty-letter-mainstream-consumer-credit-lenders.pdf) | [FCA price and value outcome update](https://www.fca.org.uk/publications/good-and-poor-practice/price-value-outcome-good-poor-practice-update)

---

### FCA MCOB — Mortgage Conduct of Business

**Regulation:** FCA Handbook MCOB; amended by Instrument 2025/34 (Mortgage Rule Review) effective July 22, 2025.

**What it demands:**
- **Affordability assessments:** Standardized methodology for assessing borrower ability to repay.
- **Advising standards:** Advice required during interactive dialogue sales; exceptions for execution-only (expanded in 2025 amendment for non-interactive channels).
- **Arrears management (MCOB 13):** Detailed requirements for servicers handling payment shortfalls, forbearance, and repossession proceedings.
- **Disclosure requirements:** Interest rate change notifications in durable medium; clear product information.
- **Vulnerable customer protections:** Regulated sale-and-rent-back customers and debt consolidation borrowers must receive advice (not eligible for execution-only).

**Infrastructure investment forced:**
- **Mortgage origination platforms** with built-in affordability calculations and compliant advice workflows.
- **Arrears management workflow engines** with regulatory-compliant escalation paths.
- **Execution-only channel infrastructure** (digital mortgage platforms) with appropriate warnings and disclosures.
- **Interest rate notification systems** triggered by rate changes.

**Penalty regime:** FCA enforcement: unlimited fines, permissions variation, public censure. Mortgage lending is a high-priority supervisory area.

**Bank tiers most affected:** All mortgage lenders and administrators authorized by the FCA.

**Source:** [FCA Handbook MCOB](https://www.handbook.fca.org.uk/handbook/MCOB.pdf) | [FCA Instrument 2025/34](https://api-handbook.fca.org.uk/files/instrument/MCOB/FCA%202025/34-2025-07-22.pdf)

---

### PRA SS1/23 — Model Risk Management Principles

**Regulation:** PRA Supervisory Statement SS1/23 — published May 2023; effective May 2024.

**What it demands:**
Five core MRM principles for UK-incorporated banks, building societies, and PRA-designated investment firms:
1. **Model identification and classification:** Comprehensive model inventories with risk-based tiering.
2. **Governance:** Board and senior management accountability (linked to SM&CR Senior Management Function holders).
3. **Model development, implementation, and use:** Standards for data, methodology, documentation, and limitations — explicitly covering AI/ML techniques.
4. **Independent model validation:** Effective challenge by validators independent of model developers.
5. **Model risk mitigants:** Controls, monitoring, and limitations to manage residual risk.

**2025 developments:** In October 2025, the PRA held CRO roundtables with 21 regulated firms specifically discussing AI/ML adoption within the SS1/23 framework — signaling deepening supervisory attention to AI models.

**Infrastructure investment forced:**
- **Enterprise model inventory systems** with risk classification taxonomies.
- **Model validation platforms** supporting both traditional and AI/ML model types.
- **AI/ML-specific governance frameworks** including explainability, bias testing, and drift monitoring.
- **SM&CR accountability mapping** for model risk ownership.
- **Vendor model assessment processes** for third-party AI/ML tools.

**Penalty regime:** PRA supervisory action: s166 skilled-person reviews (firm bears cost), capital add-ons for inadequate MRM, restrictions on model use.

**Bank tiers most affected:** UK-incorporated banks with internal model approval or significant model portfolios. Proportionality applies — smaller firms can demonstrate compliance with simpler frameworks.

**Source:** [BoE SS1/23](https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss) | [BoE PS6/23](https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks) | [PRA AI/ML roundtable Nov 2025](https://www.bankofengland.co.uk/prudential-regulation/publication/2025/november/pra-holds-model-risk-management-roundtable-on-ai)

---

### FCA/PRA FS2/23 — AI and Machine Learning Feedback

**Guidance:** FCA Feedback Statement FS23/6 and PRA FS2/23 — published October 2023, based on Discussion Paper DP5/22.

**What it signals (no binding rules yet):**
- Existing regulatory frameworks (SM&CR, SS1/23) are broadly adequate for AI governance.
- Areas requiring clarification: AI-specific model risk (beyond traditional quant models), third-party model risks, fairness and bias dimensions, data fragmentation.
- Cross-functional coordination needed between data management and model risk teams.
- Consumer outcomes and ethical dimensions should be central to AI governance.

**Infrastructure implication:** Anticipatory — banks investing in AI governance frameworks now are better positioned for forthcoming binding guidance. The PRA's October 2025 CRO roundtables suggest formal rules may follow.

**Bank tiers most affected:** All firms deploying AI/ML in lending decisions; largest banks with the most complex model portfolios face the most scrutiny.

**Source:** [BoE FS2/23](https://www.bankofengland.co.uk/prudential-regulation/publication/2023/october/artificial-intelligence-and-machine-learning) | [FCA FS23/6](https://fca.org.uk/publications/feedback-statements/fs23-6-artifical-intelligence-machine-learning) | [Goodwin analysis](https://www.goodwinlaw.com/en/insights/publications/2023/10/alerts-otherindustries-ftec-ai-and-machine-learning-in-uk-financial-services)

---

### Data (Use and Access) Act 2025 / Smart Data / Open Banking

**Legislation:** Data (Use and Access) Act 2025 — Royal Assent June 19, 2025.

**What it demands:**
- Puts the UK's existing Open Banking regime on a statutory footing (previously operated under CMA order).
- Establishes a Smart Data framework enabling regulators to mandate real-time data sharing across sectors — including financial services (Open Finance).
- Part 1 empowers the Secretary of State and HM Treasury to specify: which parties must provide data, data types, formats, security measures, and fee structures.
- Extends Open Banking beyond current accounts to **mortgages, credit products, and other lending data**.

**Infrastructure investment forced:**
- **Open Finance APIs** extending current Open Banking APIs to cover credit products, mortgages, and savings.
- **Credit data portability infrastructure** enabling consumers to share verified lending history with competing providers.
- **Consent management systems** for expanded data-sharing scope.
- **Real-time data-sharing infrastructure** meeting prescribed security and format standards.
- **Competitive pricing and product comparison** — lenders must prepare for increased transparency when consumers can easily share financial data across providers.

**Implementation timeline:** The Act is an enabling framework — detailed operational rules will come via secondary legislation (SI) during 2026–2027. One in five UK consumers and businesses already use Open Banking (as of May 2025).

**Economic impact:** £10 billion boost to UK economy over 10 years (government estimate).

**Penalty regime:** Statutory enforcement powers via designated regulators (FCA for financial services). Specific penalties to be defined in secondary legislation.

**Bank tiers most affected:** All UK banks and credit providers will need to participate as data providers; challenger banks and fintechs positioned to benefit as data consumers.

**Source:** [Data (Use and Access) Bill factsheet](https://www.gov.uk/government/publications/data-use-and-access-bill-factsheets/data-use-and-access-bill-factsheet-growing-the-economy) | [Lexology analysis](https://www.lexology.com/library/detail.aspx?g=4003efc1-5ae9-467e-be92-48888f8a4d0d) | [Kennedys Law analysis](https://kennedyslaw.com/en/thought-leadership/article/2025/smart-data-schemes-and-digital-services-under-the-data-use-and-access-bill-2025-the-uk-s-new-legal-framework-for-trusted-data-sharing-uk/) | [Open Banking – Open Finance](https://www.openbanking.org.uk/open-finance/)

---

## AI/ML Model Governance Requirements (Cross-Jurisdictional)

### Comparative Framework

| Dimension | USA | India | UK |
|-----------|-----|-------|-----|
| **Primary MRM standard** | SR 11-7 / OCC 2011-12 (2011); OCC Handbook 2021 | No formal MRM standard; embedded in digital lending & NBFC directions | PRA SS1/23 (2023); effective May 2024 |
| **AI/ML-specific guidance** | CFPB adverse action guidance (2022); AVM rule (2024); Supervisory Highlights (Jan 2025); interagency RFI (2021) | RBI Digital Lending Directions 2025 (creditworthiness assessment); no AI-specific guidance | FS2/23 feedback (2023); PRA CRO roundtables on AI (Oct 2025) |
| **Explainability requirement** | Mandatory for adverse action notices (ECOA); no AI exemption | Implicit in Fair Practices Code (KFS, transparent terms) | SS1/23 Principle 3 covers documentation and limitations |
| **Fairness/bias testing** | Required under fair lending laws (ECOA, FHA, HMDA); CFPB supervisory priority | Not explicitly required but implied by Fair Practices Code non-discrimination | FCA Consumer Duty outcomes monitoring; FS2/23 flags fairness as priority |
| **Vendor model oversight** | OCC 2021 Handbook: same rigor as in-house models | Digital Lending Directions: LSP due diligence including technical capabilities | SS1/23 Principle 4: validation applies to vendor/third-party models |
| **Regulatory maturity** | Most mature — decades of fair lending enforcement | Emerging — RBI framework focuses on conduct rules, less on model-level governance | Rapidly maturing — SS1/23 is comprehensive; AI-specific rules anticipated |
| **Penalty enforcement** | Active: consent orders, CMPs, class actions | Supervisory: directions, license conditions | Active: s166 reviews, capital add-ons, fines |

### Key observation

The three jurisdictions are converging on a common set of AI/ML governance expectations for lending:
1. **Explainability** — borrowers must receive understandable reasons for credit decisions.
2. **Fairness testing** — models must be tested for discriminatory outcomes before and during deployment.
3. **Independent validation** — challenger models, back-testing, and ongoing monitoring.
4. **Vendor model accountability** — institutions cannot outsource model risk to third parties.

The USA is furthest along in enforcement (multiple consent orders, specific guidance). The UK is furthest along in codified MRM framework (SS1/23). India is furthest along in operational infrastructure mandates (direct fund flow, LSP due diligence, bureau reporting frequency).

---

## Cross-References to Existing Research

### Overlap with Payments S2 (`org-8.0/what-we-sell/_research/payments/s2-regulatory-landscape.md`)

| Topic | Payments S2 Claim | Lending S2 Finding | Alignment |
|-------|-------------------|-------------------|-----------|
| **CFPB Section 1033** | Claim #6: "Enjoined; CFPB rewriting" | Enjoined Oct 29, 2025 by E.D. Kentucky; CFPB ANPRM Aug 2025 | Consistent; lending S2 adds court reasoning and timeline detail |
| **RBI tokenization** | Claim #10: April 1, 2026 deadline | Not directly relevant to lending S2 scope | N/A — payments-specific |
| **Open Banking (UK)** | Claim #20: 16M+ users, 53% YoY growth | Data (Use and Access) Act 2025; extends to credit/mortgage data | Complementary — lending S2 covers Open Finance extension |

### Overlap with Market Study Research

The following market study files may contain related content:
- `market-study/regulatory-landscape-payments-infrastructure.md` — broader regulatory context
- `market-study/lending-credit-opportunity-analysis.md` `[if exists — unverified]`

---

## Key Findings

1. **Infrastructure-forcing regulations are simultaneously active across all three jurisdictions.** Banks face concurrent compliance deadlines in the USA (CRA Jan 2026, Section 1071 July 2026), India (Co-Lending Jan 2026, CIC Directions Nov 2025/Jul 2026, Digital Lending 2025), and UK (SS1/23 effective May 2024, Consumer Duty ongoing, Smart Data secondary legislation 2026–27).

2. **AI/ML model governance is the single largest cross-jurisdictional infrastructure investment driver.** Every jurisdiction now requires some form of model explainability, fairness testing, or independent validation for credit models. The USA (ECOA adverse action + SR 11-7), UK (SS1/23 + Consumer Duty outcomes), and India (Fair Practices Code + Digital Lending creditworthiness) all demand infrastructure that most banks lack today.

3. **India is the most prescriptive on operational infrastructure.** RBI regulations dictate fund-flow architecture (no LSP pass-through), data submission frequency (near-weekly bureau reporting), co-lending platform specifications, and AA integration requirements. This creates hard infrastructure mandates, not just compliance paperwork.

4. **USA fair lending enforcement has the highest financial penalty exposure.** ECOA/FHA/HMDA violations can trigger multi-million-dollar consent orders (Bank of America: $12M), class action litigation, and reputational damage. The combination of private right of action (class action) and regulatory enforcement creates dual exposure.

5. **Open banking/data portability is structurally stalled in the USA but advancing in UK and India.** Section 1033 is enjoined with no clear timeline for resolution. UK Smart Data Act is law with secondary legislation pending. India's Account Aggregator framework is live with 253M linked accounts. This asymmetry creates different infrastructure investment timelines by geography.

6. **CRA modernization creates a new digital-lending tracking requirement.** For the first time, banks must demonstrate CRA performance in geographies where they have digital lending activity — not just branch footprints. This requires geocoding, digital-channel activity attribution, and expanded data warehousing.

7. **Small business lending data collection (Section 1071) remains in regulatory limbo.** Despite compliance dates being set, the Fifth Circuit stay and CFPB's own proposed reconsideration create significant uncertainty. Banks face a build-now-or-wait dilemma for data collection infrastructure.

8. **Co-lending in India is expanding beyond priority sector.** The 2025 Co-Lending Arrangements Directions broaden the framework to all loan categories effective January 2026, creating infrastructure demand for banks and NBFCs that had only built PSL-focused co-lending systems.

9. **UK PRA is actively tightening AI model oversight.** The October 2025 CRO roundtables with 21 firms signal that binding AI-specific MRM expectations may follow SS1/23. Banks should treat the five SS1/23 principles as minimum baseline, with AI-specific additions likely.

10. **Regulatory calendar density is unprecedented.** Between January 2026 and mid-2027, lending institutions in all three jurisdictions face overlapping compliance deadlines that collectively require investment in: model governance, data pipelines, fair-value assessment, co-lending platforms, bureau reporting, and open-data APIs.

---

## Gaps and Unresolved Questions

1. **CFPB BNPL interpretive rule status:** The May 2022 interpretive rule classifying certain BNPL products as "credit cards" under Reg Z has not been formally rescinded by the current administration, but enforcement posture is unclear. `[unverified — needs manual confirmation of current rule status]`

2. **RBI Fair Practices Code penalty quantum:** Specific fine amounts for Fair Practices Code violations by NBFCs need manual confirmation from RBI master circulars. The research found supervisory action powers but not specific monetary penalties. `[unverified — needs manual confirmation]`

3. **FCA Consumer Duty enforcement track record in lending:** No specific Consumer Duty enforcement actions against lending firms were identified in research. The FCA has published good/poor practice reviews but limited public enforcement data as of March 2026. `[unverified — needs manual confirmation of any formal enforcement actions]`

4. **India NBFC Scale Based Regulation (SBR) interaction with lending regulations:** The four-layer NBFC SBR framework (Base, Middle, Upper, Top) imposes differential prudential requirements that interact with digital lending and co-lending rules. This interaction was not fully researched. `[gap — needs dedicated research]`

5. **Section 1033 timeline uncertainty:** With the CFPB ANPRM published August 2025 and the rule enjoined, there is no reliable estimate for when (or whether) a revised open banking rule will take effect. The payments S2 research flagged the same uncertainty.

6. **CRA modernization — specific data field requirements:** The 2023 CRA final rule introduces new data requirements for large banks, but the specific additional data fields and reporting formats were not fully detailed in this research. `[gap — needs review of interagency implementation guides]`

7. **AI model governance convergence trajectory:** While the three jurisdictions are converging, the speed and form of convergence are uncertain. No jurisdiction has issued binding, prescriptive AI/ML lending model standards (as opposed to principle-based guidance). The first jurisdiction to do so will set the de facto global standard.

8. **EU AI Act implications for UK-based lenders:** The EU AI Act (effective August 2025) classifies credit scoring as "high risk" AI. While the UK is not bound by the EU AI Act post-Brexit, UK-based banks with EU operations may need to comply. This cross-border dimension was not researched. `[gap — needs dedicated research]`

---

## Raw Notes

### USA research notes
- ECOA adverse action + AI: CFPB September 2022 guidance is the anchor document. No AI exemption. Skadden analysis (Jan 2024) provides good legal interpretation.
- CFPB Reg B proposed amendment (Dec 2025): Would limit disparate impact liability under ECOA. CFA comment letter provides details. Political uncertainty high.
- HMDA: 2026 FIG confirms no significant changes from 2025. Reporting remains annual.
- CRA: January 1, 2026 effective date confirmed by Fed/OCC/FDIC joint extension notice (March 2024).
- Section 1071: Highly fluid. Three separate tracks: Fifth Circuit stay, CFPB proposed reconsideration, community group enforcement lawsuit. Compliance date extensions (Oct 2025) may become moot if rule is substantially revised.
- SR 11-7: OCC 2025-26 community bank clarification is notable — signals proportionality, not deregulation.
- Section 1033: Injunction analysis well-documented. Court reasoning focuses on statutory interpretation (consumer vs. third-party access).

### India research notes
- RBI Digital Lending Directions 2025: Comprehensive consolidation. Key dates: multi-lender Nov 1, 2025; DLA directory Jun 15, 2025.
- Account Aggregator: Scale is significant — 253M linked accounts, 754 FIUs. Lending via AA growing at 170% CAGR.
- Co-Lending 2025: Major expansion beyond PSL. January 1, 2026 effective date creates infrastructure urgency.
- CIC Directions: Near-weekly data submission (4 fixed reference dates per month) is a significant pipeline upgrade from prior monthly cadence.
- PSL: SFB target reduction (75% → 60%) is noteworthy but still onerous.

### UK research notes
- Consumer Duty: FCA publishing good/poor practice reviews regularly — firms should treat these as de facto enforcement guidance.
- SS1/23: May 2024 effective date means first full cycle of supervisory review is 2025. CRO roundtables in Oct 2025 are the leading indicator for AI-specific additions.
- Data (Use and Access) Act: Royal Assent achieved but operational impact depends entirely on secondary legislation timeline.
- MCOB 2025 amendments: Execution-only expansion is pro-digital but carves out vulnerable customers.
