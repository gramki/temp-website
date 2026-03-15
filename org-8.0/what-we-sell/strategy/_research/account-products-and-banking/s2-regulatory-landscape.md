# Stream 2: Regulatory Landscape and Account Mandates

**Research date:** March 2026
**Engagement area:** Account Products and Core Banking

---

## Data Table

| # | Regulation | Jurisdiction | Deadline | Penalty | Infrastructure Impact | Forces Core Replacement? | Source | URL | Verified |
|---|-----------|-------------|----------|---------|----------------------|-------------------------|--------|-----|----------|
| 1 | CFPB Section 1033 (Personal Financial Data Rights) | USA | April 1, 2026 (largest banks; enjoined — new rulemaking underway) | Supervisory enforcement; statutory penalties under Dodd-Frank § 1055 | API development, data standardization, consent management, developer portals | No — wrappable via API gateway/middleware layer over existing core | CFPB Final Rule; ABA Banking Journal; Moore & Van Allen | [CFPB](https://www.consumerfinance.gov/compliance/compliance-resources/other-applicable-requirements/personal-financial-data-rights/), [MVA Analysis](https://www.mvalaw.com/data-points/cfpb-enjoined-from-enforcing-personal-financial-data-rights-rule-1033) | Partial — rule enjoined Oct 2025 |
| 2 | FDIC Part 370 (Recordkeeping for Timely Deposit Insurance Determination) | USA | In force (April 2020 for original covered institutions; 3 years after becoming covered) | Supervisory enforcement; compliance testing by FDIC | IT systems for 24-hour deposit insurance calculation by ownership category; complete beneficial ownership records; data standardization across all deposit types | Yes — forces deep integration into core ledger and account ownership structures | FDIC 12 CFR Part 370 | [FDIC Part 370](https://www.fdic.gov/banker-resource-center/12-cfr-part-370-recordkeeping-timely-deposit-insurance-determination), [12 CFR § 370.3](https://www.law.cornell.edu/cfr/text/12/370.3) | Yes |
| 3 | FinCEN CDD/KYC Rules (Customer Due Diligence) | USA | In force (May 2018); Feb 2026 exceptive relief streamlined BO verification | Civil money penalties $100K–$1M/violation; criminal penalties for willful violations | KYC/AML platforms, beneficial ownership registries, automated screening, ongoing monitoring, risk-based refresh | No — wrappable; KYC/AML is typically a middleware/orchestration layer | FinCEN CDD Final Rule; Crowell FinTalk | [FinCEN CDD](https://www.fincen.gov/resources/statutes-and-regulations/cdd-final-rule), [Feb 2026 Relief](https://www.fincen.gov/news/news-releases/fincen-issues-exceptive-relief-streamline-customer-due-diligence-requirements) | Yes |
| 4 | BSA/AML (SARs, CTRs, Account Monitoring) | USA | Ongoing; continuous compliance | Record: $1.3B (TD Bank, Oct 2024); $450M OCC penalty + asset cap; civil/criminal penalties | Transaction monitoring systems, SAR/CTR filing, risk-based compliance programs, real-time screening | Partial — monitoring wrappable, but real-time screening at scale may require core-level integration | FinCEN; OCC | [FinCEN TD Bank](https://www.fincen.gov/news/news-releases/fincen-assesses-record-13-billion-penalty-against-td-bank), [OCC TD Bank](https://www.occ.treas.gov/news-issuances/news-releases/2024/nr-occ-2024-116.html) | Yes |
| 5 | Regulation E (Electronic Fund Transfers) | USA | In force (continuous) | Supervisory enforcement; consumer statutory damages ($50–unlimited per unauthorized transfer) | Error resolution systems, periodic statement generation, preauthorized transfer management, overdraft service disclosures, prepaid account compliance | No — wrappable via transaction processing and disclosure layers | CFPB 12 CFR 1005 | [eCFR Reg E](https://ecfr.gov/current/title-12/chapter-X/part-1005), [CFPB Reg E](https://www.consumerfinance.gov/compliance/compliance-resources/deposit-accounts-resources/electronic-fund-transfers/) | Yes |
| 6 | Interagency Third-Party Risk Management Guidance (2023) | USA | In force (June 2023); examination-enforced | Supervisory action; consent orders; asset caps (as seen in BaaS enforcement) | Third-party due diligence, ongoing monitoring, contractual governance, BaaS/embedded banking oversight, deposit recordkeeping for fintech partnerships | Partial — forces core-level visibility into end-customer deposits when BaaS partner is intermediary | OCC/FDIC/Fed Joint Guidance | [OCC NR-2023-53](https://www.occ.treas.gov/news-issuances/news-releases/2023/nr-ia-2023-53.html), [Federal Register](https://www.federalregister.gov/documents/2023/06/09/2023-12340/interagency-guidance-on-third-party-relationships-risk-management) | Yes |
| 7 | Community Reinvestment Act (CRA) Modernization | USA | 2023 final rule rescinded (March 2025); proposed replacement July 2025; reverts to 1995/2021 framework | Supervisory ratings (Outstanding/Satisfactory/Needs Improvement/Substantial Noncompliance); M&A restrictions for poor ratings | Assessment area data, lending analytics, community development tracking, deposit product data reporting | No — reporting/analytics layer; does not touch core ledger | OCC/FDIC/Fed | [OCC Rescission](https://www.occ.gov/news-issuances/bulletins/2025/bulletin-2025-5.html), [Replacement NPRM](https://www.occ.treas.gov/news-issuances/bulletins/2025/bulletin-2025-18.html) | Yes |
| 8 | RBI Master Direction — Opening of Current Accounts and CC/OD (2020, amended) | India | In force; semi-annual monitoring required | RBI supervisory action; restrictions on account operations | Current account opening controls tied to credit exposure; lending bank concentration rules; collection account management; semi-annual compliance monitoring | Yes — requires core-level integration between lending and deposit systems to enforce exposure-based account opening rules | RBI Master Direction | [RBI MD](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=10198), [RBI Notification](https://www.rbi.org.in/scripts/FS_Notification.aspx?Id=12184&fn=2&Mode=0) | Yes |
| 9 | RBI Account Aggregator Framework | India | Live; 580 FIUs, 173 FIPs, 600+ entities | RBI supervisory action | Consent architecture, API-based data sharing (FIP/FIU integration), secure data flow management | No — wrappable via API layer; AA is a consent conduit, not a core replacement | RBI; Sahamati | [Sahamati Dashboard](https://sahamati.org.in/aa-dashboard/) | Yes |
| 10 | RBI Digital Lending Guidelines (September 2022) | India | In force (Sept 2022; existing loans Nov 2022 deadline) | RBI supervisory action; restrictions on lending operations | Direct borrower-account disbursement (no pass-through), KFS disclosure systems, LSP/DLA governance, cooling-off period management, grievance redressal | Partial — disbursement routing requires core integration; disclosure/governance wrappable | RBI | [RBI DL Guidelines](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12848&Mode=0), [K&S Analysis](https://ksandk.com/banking/2022-digital-lending-guidelines-rbi/) | Yes |
| 11 | RBI KYC Master Direction (2016, amended Aug 2025) | India | In force; June 2025 amendments for periodic updation | RBI supervisory action; account restrictions for non-compliance | V-CIP infrastructure, Aadhaar eKYC integration, CKYCR connectivity, periodic KYC updation workflows, BC-facilitated KYC | No — wrappable via identity/onboarding middleware | RBI KYC Directions | [RBI KYC MD](https://www.rbi.org.in/ScriptS/BS_ViewMasDirections.aspx?id=10292), [Signzy Analysis](https://www.signzy.com/blogs/RBI-KYC-Master-Directions-2025-key-changes) | Yes |
| 12 | RBI BSBDA Guidelines (revised, effective April 2026) | India | April 1, 2026 (revised framework) | RBI supervisory action | Zero-balance account management, free ATM/debit card issuance, unlimited digital transactions, free cheque books, withdrawal limit management (4/month excl. digital), multi-channel access | Partial — product configuration and fee engine changes at core level; channel access wrappable | RBI | [Upstox Summary](https://upstox.com/news/personal-finance/latest-updates/rbi-announces-new-bsbd-account-rules-for-2026-zero-balance-accounts-with-expanded-free-services-full-list-here/article-185732/), [ET BFSI](https://bfsi.economictimes.indiatimes.com/articles/rbi-standardises-zero-balance-account-rules-payments-banks-labs-and-rrbs-see-major-additions/125768806) | Yes |
| 13 | Digital Personal Data Protection (DPDP) Act 2023 + Rules 2025 | India | Phased: Nov 2025 (foundation); Nov 2026 (consent managers); May 2027 (full compliance) | Up to ₹250 crore (~$30M) per violation category | Consent management platforms, data principal rights portals, breach notification systems, consent manager integration | No — wrappable via consent/privacy middleware | MeitY; CADP | [CADP Rules 2025](https://www.cadp.in/resources/guides/dpdp-rules-2025/), [CADP Tracker](https://cadp.in/resources/guides/dpdp-implementation-tracker/) | Yes |
| 14 | PSD2 / PSD3+PSR (proposed) | EU | PSD2 in force; PSD3/PSR trilogue agreed Nov 2025; implementation H2 2027–2028 | National supervisory penalties; PSD3 adds APP fraud liability | AISP/PISP API infrastructure, SCA, consent dashboards, Confirmation of Payee, real-time TPP authorization verification | No — wrappable via API/access layer; core ledger unaffected | Norton Rose Fulbright; Konsentus | [NRF PSD3](https://www.nortonrosefulbright.com/en/knowledge/publications/cedd39c6/psd3-and-psr-from-provisional-agreement-to-2026-readiness), [Konsentus](https://www.konsentus.com/qa-psd2-to-psd3-aspsp-and-account-data-access/) | Yes |
| 15 | UK Open Banking (CMA Order) + CASS | UK | In force; CASS compliance monitored annually by PSR | PSR enforcement; FCA supervisory action | Open banking APIs, CASS integration (7-day switch guarantee, 36-month payment redirection), TPP permission management | No — wrappable via API/switching service layer | PSR; FCA; Pay.UK | [PSR CASS Monitoring 2025](https://www.psr.org.uk/news-and-updates/latest-news/news/psrs-annual-monitoring-2025-casss-compliance-with-the-payment-account-regulations-2015/) | Yes |
| 16 | FCA Consumer Duty — Deposit Accounts | UK | In force (Jul 2023 new products; Jul 2024 closed books) | FCA unlimited fines; supervisory action | Fair value assessment frameworks for savings/deposit products, consumer outcomes monitoring, inclusive onboarding, interest rate pass-through monitoring | No — wrappable via product governance and pricing analytics layers | FCA | [FCA Cash Savings](https://fca.org.uk/news/statements/fca-publishes-update-cash-savings-market-and-fair-value), [FCA Consumer Duty](https://fca.org.uk/firms/consumer-duty-information-firms) | Yes |
| 17 | EU Instant Payments Regulation (IPR) | EU | Jan 2025 (receive, euro area); Oct 2025 (send, euro area); Jan/Jul 2027 (non-euro) | National supervisory penalties | Instant payment send/receive capability for all deposit accounts, verification of payee, equal pricing with standard transfers, daily sanctions screening | Yes — requires real-time processing capability in core ledger; batch-oriented cores cannot satisfy 10-second settlement requirement | ECB; Finextra; Osborne Clarke | [Finextra IPR](https://www.finextra.com/the-long-read/1471/europes-instant-payments-regulation-and-the-9-october-deadline-explained), [Osborne Clarke](https://www.osborneclarke.com/insights/what-are-key-obligations-and-timelines-eu-instant-payments-regulation) | Yes |
| 18 | DORA (Digital Operational Resilience Act) | EU | Effective Jan 17, 2025 | National supervisory penalties; proportionate sanctions | ICT risk management framework, incident reporting, resilience testing (including TLPT), third-party ICT provider registers, concentration risk monitoring for core banking vendors | Partial — forces visibility into core banking vendor resilience; may force core replacement if vendor cannot satisfy resilience testing requirements | EBA; EC | [EBA DORA](https://www.eba.europa.eu/activities/direct-supervision-and-oversight/digital-operational-resilience-act), [DORA Guide](https://www.compliancehub.wiki/digital-operational-resilience-act-dora-a-comprehensive-guide-to-compliance/) | Yes |
| 19 | Basel III/IV (CRR3/CRD6) | EU (global standards) | CRR3 effective Jan 1, 2025; first reporting June 30, 2025; output floor transition to 2030 | National supervisory penalties; capital surcharges | Ledger-level capital calculation, output floor (72.5%) parallel calculation, operational risk (SA-OR) engine, credit risk reclassification, FRTB market risk, ESG disclosure, granular regulatory reporting | Yes — forces deep changes to ledger, risk engines, and reporting infrastructure; batch-oriented legacy systems struggle with real-time capital adequacy | EBA; Suade; Deloitte | [Suade CRR3](https://suade.org/crr3-compliance-and-challenges-for-banks-in-2025), [Deloitte CRR3](https://www.deloitte.com/pl/pl/services/risk-advisory/perspectives/CRR3-what-to-expect-in-2025.html) | Yes |

---

## United States

### CFPB Section 1033 — Personal Financial Data Rights

**Official citation:** 12 CFR Part 1033; Personal Financial Data Rights Rule (October 22, 2024)

**Status as of March 2026:** Enjoined. The U.S. District Court for the Eastern District of Kentucky issued a preliminary injunction on October 29, 2025, preventing enforcement pending new rulemaking. The CFPB reversed course in May 2025 (post-administration change), asked the court to vacate the rule, and published an advance notice of proposed rulemaking in August 2025. The rule's original compliance schedule is suspended indefinitely.

**Original compliance schedule (now suspended):**
- April 1, 2026 — Largest depository institutions (>$850M assets)
- April 1, 2028 — Mid-sized institutions
- April 1, 2030 — Smaller depository institutions

**What the rule required:**
- Banks must make consumer financial data available to consumers and authorized third parties through standardized, machine-readable APIs
- Data categories: transaction data, account balances, account terms, upcoming bill information, basic account verification
- Third-party access governed by consumer authorization with revocation rights
- Prohibition on screen scraping once compliant APIs are available
- Data providers prohibited from charging consumers or authorized third parties for access

**Infrastructure implications:**
- Developer-facing API infrastructure (REST/JSON) exposing deposit account data
- Consumer consent management and authorization workflows
- Third-party credential management (replacing screen scraping)
- Data standardization across legacy account systems
- Rate limiting, security, and audit infrastructure

**Core replacement assessment:** Does NOT force core replacement. The API layer can wrap existing core systems via middleware. The data already exists in the core; the regulation forces standardized access, not restructuring.

**Strategic note:** Despite being enjoined, the regulation signals the direction. Large banks (JPMorgan, Wells Fargo) have already built or are building compliant APIs. The market is moving regardless of the regulatory timeline.

> Sources: [CFPB Compliance Resources](https://www.consumerfinance.gov/compliance/compliance-resources/other-applicable-requirements/personal-financial-data-rights/), [Moore & Van Allen — Injunction Analysis](https://www.mvalaw.com/data-points/cfpb-enjoined-from-enforcing-personal-financial-data-rights-rule-1033), [ABA Banking Journal — Injunction](https://bankingjournal.aba.com/2025/11/kentucky-federal-court-enjoins-cfpb-from-enforcing-current-1033-final-rule/), [KPMG 1033 Analysis](https://kpmg.com/us/en/articles/2024/1033-open-banking-cfpb-final-rule-reg-alert.html)

---

### FDIC Part 370 — Recordkeeping for Timely Deposit Insurance Determination

**Official citation:** 12 CFR Part 370

**Covered institutions:** Insured depository institutions with 2 million or more deposit accounts

**Compliance timeline:** Original deadline April 1, 2020 (for institutions covered as of April 2017); three years after becoming a covered institution for new entrants.

**Core requirements:**
1. **IT system capability:** Calculate insured and uninsured deposit amounts by ownership right and capacity within 24 hours of FDIC receivership appointment
2. **Record completeness:** Maintain unique identifiers for every account holder and beneficial owner, grantor/beneficiary information for trust accounts, and ownership category codes for every deposit
3. **Annual testing:** Covered institutions must demonstrate capability through compliance testing and certify results to the FDIC

**Penalty regime:** Supervisory enforcement through FDIC examination; no specific statutory penalty, but noncompliance invites formal enforcement action (C&D orders, civil money penalties under FDI Act § 8).

**Infrastructure implications — this is a core-level requirement:**
- Requires the core banking system to maintain structured ownership data for every deposit account (individual, joint, revocable trust, irrevocable trust, employee benefit plan, etc.)
- Must be able to aggregate deposits across all account types per beneficial owner per ownership category
- 24-hour processing deadline means no manual reconciliation is possible at scale
- Trust account structures (POD/ITF) require complete beneficiary records linked to the deposit ledger

**Core replacement assessment:** **Strong forcing function for core modernization.** Legacy systems that maintain accounts by account number rather than by beneficial owner across ownership categories often cannot satisfy Part 370 without significant re-architecture. The Synapse/BaaS failures (2024) have intensified FDIC focus on deposit recordkeeping, particularly for institutions with complex ownership structures through fintech partnerships.

**Post-SVB/Synapse context:** The 2023 bank failures (SVB, Signature, First Republic) and the 2024 Synapse BaaS collapse ($65–96M shortfall between Synapse records and bank records, 100,000+ consumers locked out) have made Part 370 compliance a heightened supervisory priority. The FDIC proposed new rules in late 2024 to strengthen recordkeeping for deposits received through third parties (fintechs), broadening the definition of brokered deposits.

> Sources: [FDIC Part 370](https://www.fdic.gov/banker-resource-center/12-cfr-part-370-recordkeeping-timely-deposit-insurance-determination), [12 CFR § 370.3 — IT Systems](https://www.law.cornell.edu/cfr/text/12/370.3), [12 CFR § 370.4 — Recordkeeping](https://www.law.cornell.edu/cfr/text/12/370.4), [Synapse/FDIC Response](https://www.bclplaw.com/en-US/events-insights-news/synapse-failure-spurs-fdic-to-specify-record-keeping-for-bank-sponsored-fintechs.html)

---

### FinCEN CDD / KYC Rules

**Official citation:** 31 CFR 1010, 1020, 1023, 1024, 1026 (CDD Final Rule, effective May 2018)

**February 2026 update:** FinCEN issued exceptive relief on February 13, 2026, eliminating the requirement to identify and verify beneficial owners at every new account opening. Now required only at: (1) first account opening, (2) when red flags arise, or (3) per risk-based ongoing due diligence.

**Cross-reference:** Covered in detail in `digital-identity-and-trust/s2-regulatory-landscape.md` — FinCEN CDD section. That document covers the four core CDD requirements and BOI registry status. This document adds the February 2026 streamlining and account-opening-specific implications.

**Account-opening-specific infrastructure implications:**
- Real-time beneficial ownership verification at first account opening
- Risk-scoring engine to determine when re-verification is warranted
- Integration with FinCEN BOI registry (when operational — status remains in flux as of March 2026)
- Customer certification workflows for subsequent account openings

**Core replacement assessment:** Does NOT force core replacement. CDD/KYC is an onboarding and monitoring function that wraps around the core.

> Sources: [FinCEN CDD Final Rule](https://www.fincen.gov/resources/statutes-and-regulations/cdd-final-rule), [FinCEN Feb 2026 Exceptive Relief](https://www.fincen.gov/news/news-releases/fincen-issues-exceptive-relief-streamline-customer-due-diligence-requirements), [Crowell FinTalk Analysis](https://www.crowellfintalk.com/2026/03/fincen-grants-exceptive-relief-to-streamline-beneficial-ownership-verification-requirements-for-financial-institutions/)

---

### BSA/AML — Account Monitoring (SARs, CTRs)

**Official citation:** Bank Secrecy Act (31 USC 5311 et seq.); implementing regulations at 31 CFR Chapter X

**Status:** In force; continuous compliance. FinCEN/OCC/FDIC/Fed issued updated SAR FAQs in October 2025 to clarify requirements and help institutions focus on highest-value suspicious activity detection.

**Scale of the compliance obligation:**
- FY 2024: 4.7 million SARs and 20.5 million CTRs filed across ~324,000 registered financial institutions
- SARs required when institution knows, suspects, or has reason to suspect suspicious activity
- CTRs mandatory for cash transactions >$10,000 per business day
- Structuring detection (multiple transactions designed to evade CTR thresholds)

**Penalty regime — escalating dramatically:**
- **TD Bank (October 2024):** $1.3B FinCEN penalty (largest ever against a depository institution) + $450M OCC penalty + asset cap + 4-year monitorship. Violations spanned 2012–2024 including inadequate peer-to-peer monitoring (Venmo, Zelle), human trafficking transaction failures, and employee-facilitated money laundering.
- Civil money penalties: $100K–$1M per violation
- Criminal penalties for willful violations (fines + imprisonment)

**Infrastructure implications:**
- Transaction monitoring systems capable of real-time screening across all account activity
- Automated SAR/CTR filing workflows
- Risk-based compliance programs with independent testing
- Customer identification programs (CIP)
- Enhanced due diligence for high-risk accounts
- Sanctions screening (OFAC) integrated with account operations

**Core replacement assessment:** Partial. Transaction monitoring and filing are wrappable middleware functions. However, the TD Bank enforcement demonstrates that truly effective BSA/AML requires deep visibility into all transaction flows at the core level — surface-level monitoring of aggregated data is insufficient. Real-time peer-to-peer transaction monitoring, in particular, may require core-level integration.

> Sources: [FinCEN — TD Bank Penalty](https://www.fincen.gov/news/news-releases/fincen-assesses-record-13-billion-penalty-against-td-bank), [OCC — TD Bank C&D](https://www.occ.treas.gov/news-issuances/news-releases/2024/nr-occ-2024-116.html), [OCC SAR FAQs Bulletin 2025-31](https://occ.gov/news-issuances/bulletins/2025/bulletin-2025-31.html)

---

### Regulation E — Electronic Fund Transfers

**Official citation:** 12 CFR Part 1005 (CFPB); Electronic Fund Transfer Act (15 USC 1693)

**Status:** In force; continuous compliance for all institutions offering deposit accounts with electronic access.

**Key requirements for deposit accounts:**
- **Liability limits:** Consumer liability capped at $50 (if reported within 2 business days), $500 (2–60 days), potentially unlimited (>60 days) for unauthorized transfers
- **Error resolution:** Institutions must investigate and resolve errors within 10 business days (45 days for new accounts), provisionally credit consumers during investigation
- **Periodic statements:** Required for all accounts with electronic access
- **Preauthorized transfers:** Stop-payment rights, notification of varying amounts
- **Overdraft services:** Opt-in requirement for ATM and one-time debit card overdraft
- **Prepaid account protections:** Error resolution, fee disclosures, limited liability

**Penalty regime:** Supervisory enforcement; consumer private right of action for statutory damages ($50–unlimited per unauthorized transfer depending on notification timing).

**Infrastructure implications:**
- Dispute management and error resolution workflows with regulatory timelines
- Provisional credit processing
- Electronic statement generation and delivery
- Preauthorized transfer management (stop payment, variable amount notification)
- Overdraft opt-in tracking and enforcement
- Prepaid account compliance systems

**Core replacement assessment:** Does NOT force core replacement. Reg E compliance is a product rules and workflow layer that wraps the core. However, institutions with archaic dispute management workflows may need to modernize their operational systems.

> Sources: [eCFR — Reg E Full Text](https://ecfr.gov/current/title-12/chapter-X/part-1005), [CFPB — Reg E Resources](https://www.consumerfinance.gov/compliance/compliance-resources/deposit-accounts-resources/electronic-fund-transfers/), [12 CFR § 1005.6 — Liability](https://www.consumerfinance.gov/rules-policy/regulations/1005/6)

---

### Interagency Third-Party Risk Management Guidance (June 2023) + BaaS Enforcement

**Official citation:** Interagency Guidance on Third-Party Relationships: Risk Management (OCC/FDIC/Fed, June 6, 2023); 88 Fed. Reg. 37920

**Status:** In force. Examination-enforced. Post-Synapse, the regulatory posture has hardened significantly.

**Key requirements:**
- Full lifecycle management: planning → due diligence → contract negotiation → ongoing monitoring → termination
- No materiality threshold — all third-party relationships in scope regardless of size
- "Same risks, same rules" principle applied to fintech partnerships
- Specific attention to arrangements where fintechs serve as intermediaries providing banking services to end customers (BaaS)
- Banks remain fully responsible for all activities conducted through third parties

**Synapse collapse context (April 2024):**
- $65–96M shortfall between Synapse middleware records and bank records
- 100,000+ consumers locked out of accounts; $265M in deposits frozen
- FDIC responded with: (1) direct monitoring of fintech partners, (2) proposed new recordkeeping rules for third-party deposits, (3) proposed broadening of brokered deposit definitions

**Infrastructure implications for BaaS/embedded banking:**
- End-to-end visibility into deposits held through fintech intermediaries
- Real-time reconciliation between middleware records and core ledger
- Customer-level deposit ownership records maintained at the bank level (not delegated to fintech partner)
- Contractual and technical controls ensuring data integrity across the partnership

**Core replacement assessment:** **Strong forcing function.** Banks pursuing BaaS or embedded banking strategies must ensure their core banking system can maintain direct, real-time visibility into every deposit relationship, even when the customer-facing interface is operated by a fintech partner. Legacy cores that were not designed for multi-tenant, partner-mediated deposit management are structurally inadequate for this model.

> Sources: [OCC NR-2023-53](https://www.occ.treas.gov/news-issuances/news-releases/2023/nr-ia-2023-53.html), [Federal Register — Final Guidance](https://www.federalregister.gov/documents/2023/06/09/2023-12340/interagency-guidance-on-third-party-relationships-risk-management), [BCLP — Synapse/FDIC Response](https://www.bclplaw.com/en-US/events-insights-news/synapse-failure-spurs-fdic-to-specify-record-keeping-for-bank-sponsored-fintechs.html), [CNBC — Synapse](https://www.cnbc.com/2024/07/02/synapse-fintech-fdic-false-promise.html)

---

### Community Reinvestment Act (CRA) Modernization

**Official citation:** 12 CFR Parts 25, 228, 345 (joint OCC/Fed/FDIC rulemaking)

**Status:** The October 2023 interagency final rule was challenged in court and subsequently rescinded by the agencies in March 2025. A proposed replacement rule (July 2025) reverts to the 1995/2021 CRA framework. Regulatory certainty restored to pre-2023 status quo.

**What the 2023 rule would have required (now rescinded):**
- Metrics-based evaluation of retail lending and community development financing
- Expanded assessment areas to capture online/mobile banking activity
- New data reporting (effective January 2027)
- Tailored standards by bank size and business model

**Current framework (1995/2021 rules, in force):**
- Assessment area-based evaluation
- Lending, investment, and service tests
- CRA ratings (Outstanding/Satisfactory/Needs Improvement/Substantial Noncompliance)
- Poor ratings restrict M&A activity

**Infrastructure implications (under current framework):**
- Assessment area data management and reporting
- Lending analytics for LMI community evaluation
- Community development activity tracking
- Branch/deposit product data reporting

**Core replacement assessment:** Does NOT force core replacement. CRA compliance is an analytics and reporting function.

**Strategic note:** The rescission and reversion to the 1995 framework eliminates CRA as a near-term technology buying event. However, future modernization attempts remain likely given the bipartisan recognition that CRA's geographic assessment areas don't reflect digital banking realities.

> Sources: [Fed — 2023 Final Rule](https://www.federalreserve.gov/newsevents/pressreleases/bcreg20231024a.htm), [OCC — Rescission](https://www.occ.gov/news-issuances/bulletins/2025/bulletin-2025-5.html), [OCC — Replacement NPRM](https://www.occ.treas.gov/news-issuances/bulletins/2025/bulletin-2025-18.html)

---

## India

### RBI Master Direction — Opening of Current Accounts and CC/OD (2020, amended)

**Official citation:** RBI/DOR/2020-21/68; Master Direction — Opening of Current Accounts, Cash Credit (CC) and Overdraft (OD) Accounts

**Status:** In force; semi-annual monitoring required.

**Key requirements:**

| Borrower Exposure | Current Account Rules |
|---|---|
| Below ₹5 crore | Banks may open current accounts/CC/OD without restrictions (undertaking required) |
| ₹5 crore and above | Current account permitted only with bank holding ≥10% of total banking exposure; other lenders limited to collection accounts (funds swept within 2 working days) |
| No single bank at 10%+ | Bank with highest exposure may open current accounts |
| Non-lending banks | Cannot open current accounts for borrowers with ≥₹5 crore exposure |

**Exemptions:** Real estate project accounts (RERA), payment aggregator accounts, IPO/NFO settlement accounts, FEMA-permitted accounts, court-ordered accounts.

**Infrastructure implications — this is a core-level regulation:**
- Real-time credit exposure lookup across the banking system (requires inter-bank data sharing or consortium-level visibility)
- Account opening workflows that enforce exposure-based eligibility rules before account creation
- Automated collection account sweeping (2 working-day fund transfer)
- Semi-annual compliance monitoring and reporting
- Integration between lending system (exposure data) and deposit system (account opening)

**Core replacement assessment:** **Strong forcing function.** This regulation requires the deposit/account system and the lending/credit system to be tightly integrated. Legacy banks running siloed core banking modules for deposits and loans face structural compliance gaps. Modern core systems with unified customer views across deposit and credit relationships are significantly better positioned.

> Sources: [RBI Master Direction](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=10198), [RBI Notification on Amendments](https://www.rbi.org.in/scripts/FS_Notification.aspx?Id=12184&fn=2&Mode=0)

---

### RBI Account Aggregator Framework

**Cross-reference:** Covered extensively in `digital-identity-and-trust/s2-regulatory-landscape.md` — Account Aggregator Framework section, including scale data (2.84 lakh daily consents, 4.77 crore users, ₹887 billion loan disbursements via AA in FY25, 580 FIUs, 173 FIPs).

**Account products-specific implications:**
- Banks must function as Financial Information Providers (FIPs), sharing deposit account data upon consumer consent
- Account balance, transaction history, and account metadata must be available through AA APIs
- Consent-based data sharing infrastructure required for all deposit account types
- Integration with registered Account Aggregators for outbound data sharing

**Core replacement assessment:** Does NOT force core replacement. AA integration is an API/middleware function wrapping the core. The account data already exists; the regulation forces consent-governed API access.

> Sources: [Sahamati Dashboard](https://sahamati.org.in/aa-dashboard/), [Business Standard — AA FY25](https://www.business-standard.com/finance/news/aa-ecosystem-consent-processing-up-78-in-fy25-shows-sahamati-data-125031301053_1.html)

---

### RBI Digital Lending Guidelines (September 2022)

**Official citation:** RBI/2022-23/111 DOR.CRE.REC.66/21.07.001/2022-23 (September 2, 2022)

**Status:** In force. Applies to all commercial banks, cooperative banks, and NBFCs (including HFCs).

**Key requirements affecting account infrastructure:**
- **All loan disbursals must go directly to the borrower's bank account** — no third-party pass-through (except statutory mandates, co-lending, or specific end-use disbursals)
- **All repayments must flow between RE's and borrower's accounts directly** — no LSP/DLA intermediary handling of funds
- **Key Fact Statement (KFS)** must be provided before contract execution with APR, fees, recovery details
- **Cooling-off period** for borrowers to exit loans
- **LSP/DLA governance:** REs remain fully responsible; LSPs cannot charge borrowers directly

**Infrastructure implications:**
- Loan management system must enforce direct-to-borrower-account disbursement routing
- Account verification (ensure disbursement goes to the right borrower account)
- KFS generation and delivery systems (digital documents to verified email/SMS)
- Cooling-off period management workflows
- LSP/DLA oversight and audit trail systems

**Core replacement assessment:** Partial. The direct disbursement routing requirement forces integration between the lending system and the deposit/account system. If these are separate legacy systems, the routing logic adds complexity. The governance and disclosure requirements are wrappable.

> Sources: [RBI Digital Lending Guidelines](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12848&Mode=0), [K&S Analysis](https://ksandk.com/banking/2022-digital-lending-guidelines-rbi/)

---

### RBI KYC Master Direction (2016, amended August 2025)

**Cross-reference:** Covered extensively in `digital-identity-and-trust/s2-regulatory-landscape.md` — RBI KYC Master Direction section, including V-CIP, eKYC, periodic updation, CKYCR integration, and June 2025 amendments.

**Account products-specific additions:**
- KYC updation directly affects account operations — accounts can be restricted (credit-only, then frozen) for non-compliant KYC
- Aadhaar OTP-based e-KYC accounts have operational limits until full CDD is completed (within 1 year)
- Non-face-to-face onboarded accounts require strict monitoring
- BC-facilitated KYC updation (June 2025 amendment) creates a field-level account servicing requirement

**Core replacement assessment:** Does NOT force core replacement. KYC is an identity/onboarding middleware function. However, the account restriction enforcement (credit-only → freeze) based on KYC status requires core-level product rules integration.

> Sources: [RBI KYC Directions](https://www.rbi.org.in/ScriptS/BS_ViewMasDirections.aspx?id=10292), [Signzy — KYC Directions 2025](https://www.signzy.com/blogs/RBI-KYC-Master-Directions-2025-key-changes)

---

### RBI BSBDA Guidelines (revised, effective April 1, 2026)

**Official citation:** RBI Master Direction on Basic Savings Bank Deposit (BSBD) Accounts (revised 2026)

**Status:** Revised framework effective April 1, 2026. Standardized across all bank categories (commercial banks, SFBs, payments banks, LABs, RRBs, cooperative banks).

**Key requirements:**
- Zero minimum balance — no balance requirements whatsoever
- Free ATM/debit card with zero annual charges (upon request only)
- At least 25 free cheque leaves per year (upon request)
- Free internet and mobile banking
- Free passbooks or monthly statements
- Minimum 4 free withdrawals per month (including ATM + transfers)
- **Digital transactions (UPI, NEFT, RTGS, IMPS, PoS) do NOT count against withdrawal limit** — unlimited
- Banks cannot mandate customers to opt for ATM cards, cheque books, or digital banking
- One BSBDA per customer across all banks

**Infrastructure implications:**
- Product configuration engine must support zero-fee product with complex conditional fee/limit logic
- Withdrawal counting logic that distinguishes digital channels from cash/transfer channels
- Multi-channel access provisioning (internet banking, mobile banking, UPI, NEFT, RTGS, IMPS) — all free
- Cross-bank uniqueness enforcement (one BSBDA per customer across the system)
- Passbook/statement generation at zero cost

**Core replacement assessment:** Partial. The product configuration requirements (zero-fee with channel-specific withdrawal counting, unlimited digital transactions) test the flexibility of core banking product engines. Rigid legacy cores with hardcoded fee structures or channel-agnostic transaction limits may struggle. Modern cores with configurable product rules engines handle this natively.

> Sources: [Upstox — BSBD 2026 Rules](https://upstox.com/news/personal-finance/latest-updates/rbi-announces-new-bsbd-account-rules-for-2026-zero-balance-accounts-with-expanded-free-services-full-list-here/article-185732/), [ET BFSI — Standardization](https://bfsi.economictimes.indiatimes.com/articles/rbi-standardises-zero-balance-account-rules-payments-banks-labs-and-rrbs-see-major-additions/125768806)

---

### Digital Personal Data Protection (DPDP) Act 2023

**Cross-reference:** Covered extensively in `digital-identity-and-trust/s2-regulatory-landscape.md` — DPDP Act 2023 section, including phased timeline (Nov 2025/Nov 2026/May 2027), penalty regime (up to ₹250 crore), Consent Manager concept, and data principal rights.

**Account products-specific implications:**
- Deposit account data (balances, transactions, account holder information) is personal data under the Act
- Banks must obtain verifiable consent for processing deposit account data beyond regulatory requirements
- Data principal rights (access, correction, erasure) apply to account records
- Breach notification obligations cover account data breaches
- Consent Manager integration required for data sharing through the AA framework

**Core replacement assessment:** Does NOT force core replacement. DPDP compliance is a consent and privacy middleware function.

> Sources: [CADP Rules 2025](https://www.cadp.in/resources/guides/dpdp-rules-2025/), [CADP Implementation Tracker](https://cadp.in/resources/guides/dpdp-implementation-tracker/)

---

## UK / Europe

### PSD2 / PSD3+PSR

**Cross-reference:** Covered in both `payments/s2-regulatory-landscape.md` (PSD3/PSR structure, APP fraud, open banking, Confirmation of Payee, timeline) and `digital-identity-and-trust/s2-regulatory-landscape.md` (SCA, dynamic linking, authentication mandates).

**Account products-specific implications:**
- AISP (Account Information Service Provider) access: Banks must provide third-party read access to deposit account data (balances, transactions) through standardized APIs
- PISP (Payment Initiation Service Provider) access: Banks must enable third-party payment initiation from deposit accounts
- SCA (Strong Customer Authentication): Two-factor authentication required for account access and transactions
- PSD3/PSR adds: Consent dashboards for account holders; real-time TPP authorization verification; role/permission-aware access controls; prohibition on arbitrary barriers

**Timeline:** PSD2 in force; PSD3/PSR trilogue agreed November 2025; implementation expected H2 2027–early 2028.

**Core replacement assessment:** Does NOT force core replacement. Open banking APIs wrap the core. However, institutions with cores that lack API-compatible data access layers face higher middleware complexity.

> Sources: [Norton Rose — PSD3/PSR](https://www.nortonrosefulbright.com/en/knowledge/publications/cedd39c6/psd3-and-psr-from-provisional-agreement-to-2026-readiness), [Konsentus — PSD2 to PSD3 Changes](https://www.konsentus.com/qa-psd2-to-psd3-aspsp-and-account-data-access/)

---

### UK Open Banking (CMA Order) + Current Account Switch Service (CASS)

**Official citation:** CMA Retail Banking Market Investigation Order 2017; Payment Accounts Regulations 2015 (PAR)

**Status:** In force. CASS compliance monitored annually by the PSR; confirmed compliant for 2024 and 2025.

**Key requirements:**
- **CMA Order:** Nine largest banks/building societies required to maintain open banking APIs for account data and payment initiation (aligned with PSD2/Open Banking Standard)
- **CASS:** Free 7-working-day current account switch guarantee; 36-month automatic payment redirection; backed by 40+ UK banks via Pay.UK
- **PSR designation criteria:** Switching must complete within 12 working days; no additional consumer burden; clearly in consumer interest

**CASS operational note:** TPP (open banking) permissions do NOT transfer during a CASS switch. Customers must re-establish third-party access with their new provider — this is a known friction point.

**Infrastructure implications:**
- Open banking API infrastructure (read + write) per CMA Order
- CASS integration for inbound/outbound switching (payment redirection, direct debit transfer, standing order migration)
- Account portability data management
- TPP permission management dashboard for consumers

**Core replacement assessment:** Does NOT force core replacement. APIs and switching services are middleware functions. However, the CASS 7-day switch guarantee requires efficient account setup and payment redirection capabilities that challenge highly manual legacy account opening processes.

> Sources: [PSR CASS Monitoring 2025](https://www.psr.org.uk/news-and-updates/latest-news/news/psrs-annual-monitoring-2025-casss-compliance-with-the-payment-account-regulations-2015/)

---

### FCA Consumer Duty — Deposit Accounts

**Official citation:** FCA PS22/9 — A new Consumer Duty (July 2022); in force from July 2023 (new products), July 2024 (closed books)

**Status:** In force; active supervisory focus on cash savings.

**Deposit account-specific requirements:**
- **Fair value assessments:** Banks must demonstrate that savings/deposit product pricing delivers fair value (price ≈ reasonable relative to benefits)
- **Interest rate pass-through:** FCA actively monitors how banks adjust savings rates as base rate changes — expects clear explanations for significant discrepancies
- **Cash savings market improvements:** Average easy access savings rates rose from 1.66% (Jul 2023) to 2.11% (Jun 2024); estimated £4 billion/year consumer benefit
- **Remaining concerns:** Largest firms still paying below market average for easy access; closed-book products under scrutiny

**Penalty regime:** FCA unlimited fines; supervisory action; s.166 skilled person reviews.

**Infrastructure implications:**
- Fair value assessment frameworks (comparing product pricing against market benchmarks, costs, and benefits)
- Consumer outcome monitoring dashboards
- Interest rate analytics and competitive benchmarking
- Closed-book product review and remediation workflows
- Product governance documentation and audit trails

**Core replacement assessment:** Does NOT force core replacement. Consumer Duty compliance is a product governance and analytics function.

> Sources: [FCA — Cash Savings Update](https://fca.org.uk/news/statements/fca-publishes-update-cash-savings-market-and-fair-value), [FCA — Consumer Duty](https://fca.org.uk/firms/consumer-duty-information-firms), [PwC — Fair Value](https://www.pwc.co.uk/industries/financial-services/understanding-regulatory-developments/fca-shares-findings-of-fair-value-supervisory-work.html)

---

### EU Instant Payments Regulation (IPR)

**Official citation:** Regulation (EU) 2024/886 (amending SEPA Regulation, PSD2, Settlement Finality Directive)

**Status:** In force (April 8, 2024); phased compliance.

**Compliance deadlines:**

| Date | Obligation | Scope |
|------|-----------|-------|
| January 9, 2025 | Receive instant payments; equal charges | Euro area PSPs |
| October 9, 2025 | Send instant payments; verification of payee | Euro area PSPs |
| January 9, 2027 | Receive instant payments; equal charges | Non-euro area PSPs |
| July 9, 2027 | Send instant payments; verification of payee | Non-euro area PSPs |
| — | Send/receive capability | E-money and payment institutions (April 2027) |

**Key requirements:**
- Every PSP offering standard credit transfers must also offer instant credit transfers
- Instant transfers must be priced equal to or lower than standard transfers
- Settlement within 10 seconds, 24/7/365
- Verification of Payee (VoP) — free payee name matching service for all credit transfers
- Daily sanctions screening of payment service user base (replacing per-transaction screening)

**Infrastructure implications — this is a core-level regulation:**
- **Real-time processing:** Core banking system must support 10-second end-to-end settlement. Batch-oriented cores cannot satisfy this.
- **24/7/365 availability:** No maintenance windows. Ledger must support continuous operation.
- **Equal pricing:** Fee engines must ensure instant ≤ standard pricing
- **Verification of Payee:** Pre-transaction payee name matching integrated into payment flow
- **Daily sanctions screening:** Shift from per-transaction to daily batch screening of entire customer base
- **SEPA Instant Credit Transfer Scheme:** Compliance with updated 2025 rulebook

**Core replacement assessment:** **Strong forcing function for core replacement.** This is the most direct account infrastructure mandate in Europe. Banks with batch-oriented legacy cores that process overnight cannot satisfy the 10-second settlement and 24/7/365 availability requirements. The equal-pricing mandate eliminates the ability to price instant as a premium service, making it the default. Banks must either replace their core or implement a parallel real-time processing layer — and maintaining two parallel ledgers creates its own complexity.

**Cross-reference:** The payments research (`payments/s2-regulatory-landscape.md`) covers IPR deadlines and SEPA Instant share metrics (24.74% of credit transfers in Q1 2025).

> Sources: [Finextra — IPR Explained](https://www.finextra.com/the-long-read/1471/europes-instant-payments-regulation-and-the-9-october-deadline-explained), [Osborne Clarke — IPR Obligations](https://www.osborneclarke.com/insights/what-are-key-obligations-and-timelines-eu-instant-payments-regulation), [EC — IPR Clarification](https://finance.ec.europa.eu/publications/clarification-requirements-instant-payments-regulation_en)

---

### DORA (Digital Operational Resilience Act)

**Cross-reference:** Covered in `digital-identity-and-trust/s2-regulatory-landscape.md` — DORA section, including five pillars, ICT third-party risk management, and operational resilience testing requirements.

**Account products / core banking-specific implications:**
- Core banking systems are ICT infrastructure within DORA's scope — subject to risk management, incident reporting, and resilience testing requirements
- **ICT third-party registers:** Banks must maintain registers of all ICT providers, including core banking vendors — with concentration risk assessment
- **Resilience testing:** Core banking systems (as critical ICT) must undergo advanced threat-led penetration testing (TLPT)
- **Critical Third-Party Provider (CTPP) designation:** ESAs designated critical ICT TPPs in November 2025; major core banking vendors likely subject to direct oversight
- **Incident reporting:** Major incidents affecting core banking (outages, data corruption, availability failures) must be reported to supervisory authorities within prescribed timeframes

**Core replacement assessment:** Partial forcing function. DORA does not mandate core replacement directly, but it forces banks to assess whether their core banking vendor can satisfy resilience testing, incident reporting, and operational continuity requirements. If the vendor cannot — or if the bank identifies concentration risk from a single core vendor — DORA creates regulatory pressure for architectural change.

> Sources: [EBA — DORA](https://www.eba.europa.eu/activities/direct-supervision-and-oversight/digital-operational-resilience-act), [DORA Guide](https://www.compliancehub.wiki/digital-operational-resilience-act-dora-a-comprehensive-guide-to-compliance/)

---

### Basel III/IV Implementation (CRR3/CRD6)

**Official citation:** Regulation (EU) 2024/1623 (CRR3); Directive (EU) 2024/1619 (CRD6)

**Status:** CRR3 effective January 1, 2025; first reporting submission June 30, 2025; output floor transition extends to 2030.

**Key requirements affecting core banking infrastructure:**

| Requirement | Infrastructure Impact |
|---|---|
| **Output floor (72.5%)** | Banks using internal models must run standardized approaches in parallel — requires dual calculation capability in the ledger/risk engine |
| **Credit risk (SA-CR / IRB)** | New exposure classes (subordinated debt), revised risk weights, stricter collateral treatment — loan/account classification changes at ledger level |
| **Operational risk (SA-OR)** | Single Business Indicator Component replaces multiple methodologies — new data collection and calculation engine |
| **Market risk (FRTB)** | Parallel FRTB calculation alongside CRR2 methodologies — preparation for transition |
| **ESG disclosure** | Qualitative and quantitative ESG risk reporting from 2025 — new data fields at account/exposure level |
| **Regulatory reporting** | ITS on supervisory reporting (effective June 2025) — increased data granularity for solvency, leverage, output floor |

**Penalty regime:** National supervisory penalties; capital surcharges for noncompliance; restrictions on distributions (dividends, bonuses).

**Infrastructure implications — this is a core-level regulation:**
- **Ledger-level changes:** Account classification, risk weight assignment, and exposure categorization must be updated in the core ledger
- **Parallel calculation engines:** Output floor requires running both internal model and standardized approach simultaneously
- **Real-time capital adequacy:** Regulators increasingly expect near-real-time capital ratio calculations, not just quarterly reporting
- **Data granularity:** CRR3 reporting requires more granular exposure-level data than many legacy systems can produce
- **ESG data integration:** New data fields at the account/loan level for ESG risk categorization

**Core replacement assessment:** **Strong forcing function.** CRR3 requires changes deep within the ledger, risk engine, and reporting infrastructure. Banks with legacy cores that cannot support parallel calculation, new exposure classes, or granular regulatory data extraction face significant re-architecture or replacement pressure. The Deloitte/KPMG consensus is that at least 6 months of parallel calculation runs are recommended before go-live — indicating the complexity of the transition.

> Sources: [Suade — CRR3 Compliance](https://suade.org/crr3-compliance-and-challenges-for-banks-in-2025), [Deloitte — CRR3 2025](https://www.deloitte.com/pl/pl/services/risk-advisory/perspectives/CRR3-what-to-expect-in-2025.html), [EBA — CRR3 Reporting ITS](https://www.eba.europa.eu/activities/single-rulebook/regulatory-activities/supervisory-reporting/implementing-technical-standards-supervisory-reporting-changes-related-crr3crd6-step-1), [KPMG — Basel IV](https://kpmg.com/de/en/home/insights/2023/04/basel-4.html)

---

## Cross-References to Existing Research

| Topic | Existing Research File | What's Covered There | What This Document Adds |
|-------|----------------------|---------------------|------------------------|
| **FinCEN CDD/KYC** | `digital-identity-and-trust/s2-regulatory-landscape.md` | Four CDD requirements, BOI registry status, penalty structure | Feb 2026 exceptive relief; account-opening-specific workflow implications |
| **DPDP Act 2023** | `digital-identity-and-trust/s2-regulatory-landscape.md` | Phased timeline, penalties, Consent Manager concept | Account data as personal data; deposit-specific consent requirements |
| **RBI KYC Master Direction** | `digital-identity-and-trust/s2-regulatory-landscape.md` | V-CIP, eKYC, periodic updation, CKYCR, June 2025 amendments | Account restriction enforcement (credit-only → freeze) based on KYC status |
| **Account Aggregator** | `digital-identity-and-trust/s2-regulatory-landscape.md` | Scale data (FY25), consent architecture, FIP/FIU structure | Bank-as-FIP obligations for deposit account data sharing |
| **PSD2/PSD3** | Both `payments/s2` and `digital-identity/s2` | PSD3/PSR structure, APP fraud, SCA, dynamic linking, timeline | AISP/PISP account access implications; consent dashboards |
| **DORA** | `digital-identity-and-trust/s2-regulatory-landscape.md` | Five pillars, ICT TPP risk management, TLPT | Core banking vendor as ICT third party; concentration risk; resilience testing for core systems |
| **CFPB 1033 status** | `payments/s2-regulatory-landscape.md` | Noted as enjoined; CFPB rewriting (Claim #6) | Full legal challenge analysis; new rulemaking context; infrastructure requirements |
| **EU IPR deadlines** | `payments/s2-regulatory-landscape.md` | Jan/Oct 2025 deadlines; SEPA Instant share metrics | Core banking infrastructure implications; 10-second settlement forcing function |

---

## Key Findings

### Regulations That Force Core Replacement (Strong Forcing Functions)

1. **FDIC Part 370** — Deposit insurance recordkeeping within 24 hours requires deep integration into the core ledger's account ownership structures. Post-SVB/Synapse, this is a heightened supervisory priority. Banks with legacy cores that organize data by account number rather than by beneficial owner across ownership categories face structural remediation.

2. **EU Instant Payments Regulation** — 10-second settlement and 24/7/365 availability is the most direct core banking mandate in Europe. Batch-oriented cores cannot comply. Equal pricing eliminates instant-as-premium, making real-time the default path.

3. **Basel III/IV (CRR3)** — Output floor parallel calculations, new exposure classes, and granular regulatory reporting requirements force changes deep within the ledger and risk engine. Legacy cores struggle with real-time capital adequacy and dual-methodology calculation.

4. **RBI Current Account/CC/OD Direction** — Exposure-based account opening rules require tight integration between lending and deposit systems. Siloed legacy modules for deposits and loans create structural compliance gaps.

5. **Interagency Third-Party Guidance + BaaS model** — For banks pursuing embedded banking, the Synapse failure created a regulatory expectation of real-time, customer-level deposit visibility through fintech intermediaries. Legacy cores not designed for multi-tenant partner-mediated deposit management are structurally inadequate.

### Regulations Satisfiable by Wrapping the Core (Weak Forcing Functions)

6. **CFPB Section 1033** — API gateway/middleware over existing core; data already exists, regulation forces standardized access. (Currently enjoined, adding further relief.)

7. **FinCEN CDD/KYC** — Onboarding and monitoring middleware; wraps the core rather than replacing it.

8. **BSA/AML monitoring** — Transaction monitoring is largely wrappable, though TD Bank enforcement suggests surface-level monitoring is insufficient for truly effective compliance.

9. **Regulation E** — Product rules and workflow layer; does not touch core ledger structure.

10. **PSD2/PSD3 open banking** — API layer wrapping account data; core ledger unaffected.

11. **UK Open Banking + CASS** — API and switching service middleware.

12. **FCA Consumer Duty** — Product governance and analytics layer.

13. **RBI Account Aggregator** — API middleware for consent-based data sharing.

14. **RBI Digital Lending Guidelines** — Disbursement routing requires some integration, but governance and disclosure requirements are wrappable.

15. **DPDP Act** — Consent and privacy middleware.

16. **CRA** — Analytics and reporting function; 2023 modernization rescinded, removing near-term buying event.

### Regulations With Partial/Conditional Core Impact

17. **DORA** — Does not mandate replacement but forces resilience assessment of core banking vendor; may trigger replacement if vendor cannot satisfy testing requirements.

18. **RBI KYC** — Account restriction enforcement (freeze on KYC non-compliance) requires core-level product rules integration.

19. **RBI BSBDA** — Product configuration requirements (zero-fee, channel-specific withdrawal counting) test core flexibility.

### The Regulatory Calendar Creates Compound Pressure

The density of regulatory deadlines across 2025–2027 creates compound investment pressure:

| Period | Key Deadlines |
|--------|--------------|
| **2025** | CRR3 effective (Jan); DORA effective (Jan); EU IPR receive (Jan); EU IPR send (Oct); DPDP Phase 1 (Nov) |
| **2026** | CFPB 1033 (enjoined but market-moving); RBI BSBDA (Apr); EU AI Act high-risk (Aug); DPDP Phase 2 (Nov) |
| **2027** | EU IPR non-euro (Jan/Jul); PSD3/PSR implementation (H2); eIDAS 2.0 bank acceptance (Dec); DPDP Phase 3 (May) |

Banks facing multiple concurrent compliance deadlines across jurisdictions cannot address them with point solutions — the compound pressure creates a structural case for core modernization.

---

## Gaps and Unresolved Questions

1. **CFPB 1033 final disposition:** The rule is enjoined and undergoing new rulemaking. The ultimate compliance requirements and timeline are unknown. However, large banks are building APIs regardless, making this a market-driven standard even without regulatory certainty. [Needs monitoring — ANPR comment period may yield new rule in 2026–2027]

2. **FinCEN BOI registry operational status:** The Corporate Transparency Act BOI reporting requirements have faced multiple injunctions (2024–2025). Whether banks can rely on the FinCEN BOI registry for CDD verification at account opening remains unresolved. [unverified — needs manual confirmation of current status]

3. **FDIC proposed rules on fintech deposit recordkeeping:** Following Synapse, the FDIC proposed new recordkeeping rules for third-party deposits and broadening of brokered deposit definitions. Final rule status and timeline unknown. [Needs monitoring — final rule expected 2026]

4. **CRA modernization next iteration:** The 2023 rule was rescinded and a replacement NPRM issued (July 2025). Whether the replacement meaningfully updates the 1995 framework or simply restores it remains unclear. [Needs monitoring — comment period outcome]

5. **DORA secondary legislation completeness:** Not all delegated and implementing regulations are finalized as of the January 2025 effective date. Banks face compliance uncertainty on specific reporting timelines and testing requirements. [unverified — needs manual check of ESA publications]

6. **Basel III/IV output floor transition mechanics:** The 72.5% output floor is being phased in through 2030. Specific transitional percentages by year, and national discretion on implementation pace, require verification from CRR3 text. [unverified — needs manual confirmation from regulatory text]

7. **RBI Current Account Direction — inter-bank exposure data sharing mechanism:** How banks verify a borrower's total banking system exposure in real-time (to enforce the ₹5 crore threshold and 10% concentration rule) is unclear. Whether this relies on CRILC (Central Repository of Information on Large Credits), bilateral checks, or borrower self-declaration affects the infrastructure requirement. [Needs manual verification from RBI operational guidelines]

8. **FCA Consumer Duty — enforcement trajectory for savings accounts:** The FCA has identified ongoing concerns about largest firms paying below-market rates. Whether this leads to formal enforcement actions (fines, requirements) or remains supervisory guidance will determine whether Consumer Duty is a genuine buying event for deposit infrastructure. [Needs monitoring — FCA 2026 supervisory priorities]

9. **India DPDP cross-border transfer restrictions:** 14 of 40 DPDP obligations remain unnotified, including cross-border restrictions and Significant Data Fiduciary designations. Banks with India operations cannot finalize data architecture. [unverified — pending MeitY notification]

10. **EU PSD3/PSR final text:** Trilogue agreed November 2025 but final text not published. Exact consent dashboard specifications, TPP access requirements, and APP fraud liability mechanics remain subject to change. [Needs monitoring — formal adoption expected 2026]

---

## Raw Notes and Excerpts

### USA Research Notes

- **CFPB 1033 political context:** The rule's injunction and new rulemaking reflect the change in presidential administration. The May 2025 CFPB request to vacate its own rule is unprecedented. Market participants (large banks, data aggregators like Plaid/MX/Finicity) are building to the October 2024 rule's specifications regardless, suggesting the standard will persist even if the regulatory mandate shifts.

- **FDIC Part 370 and Synapse:** The $65–96M recordkeeping shortfall in the Synapse bankruptcy is the most compelling recent evidence that deposit recordkeeping is a systemic risk. Former FDIC Chair McWilliams as bankruptcy trustee adds institutional weight. The FDIC's proposed response (direct fintech monitoring, broadened brokered deposit definitions) signals that Part 370-style requirements may be extended to all institutions with third-party deposit relationships, not just those with 2M+ accounts.

- **TD Bank BSA/AML enforcement ($1.75B total):** This is the defining enforcement action of the decade for account monitoring. The OCC asset cap — restricting growth to September 2024 levels with potential 7% annual reduction — is more punitive than any fine. It demonstrates that BSA/AML failures can constrain an institution's entire business strategy, not just impose financial penalties.

- **Regulation E and fraud liability:** The $50/$500/unlimited liability tiers haven't been updated since 1978. As unauthorized electronic transfers evolve (P2P fraud, account takeover), the gap between Reg E's framework and current fraud patterns creates compliance ambiguity. The CFPB has been active in enforcement — expect examination focus on error resolution timelines.

- **BaaS regulatory model under stress:** The combination of (a) interagency third-party guidance, (b) Synapse failure, (c) FDIC proposed rules on fintech deposits, and (d) multiple consent orders against BaaS banks (Evolve, Blue Ridge, others) creates a regulatory environment where the BaaS model only works if the core banking system maintains complete, real-time visibility into all deposits. This is a structural requirement that didn't exist three years ago.

### India Research Notes

- **RBI Current Account Direction is unique:** No other jurisdiction has a comparable regulation that ties deposit account opening eligibility to credit exposure across the banking system. This reflects India's credit discipline challenges (multiple banking, fund diversion) but creates a genuinely novel infrastructure requirement — the deposit system must query the credit system before opening an account.

- **BSBDA revised guidelines — channel-specific logic:** The distinction between "free" and "counted" transactions based on channel (digital = free/unlimited, cash/transfer = counted against 4/month limit) is a product configuration challenge. Legacy cores that apply uniform transaction limits regardless of channel need re-engineering. This is a relatively low-profile regulation but tests core flexibility in a practical way.

- **RBI Digital Lending — direct disbursement routing:** The prohibition on third-party pass-through for loan disbursement is specifically designed to prevent the "loan stacking" and "digital lending app abuse" patterns that characterized India's fintech lending crisis (2022). It forces the lending system and the deposit/account system to have direct integration for fund flow routing.

- **Account Aggregator as infrastructure standard:** With 580 FIUs, 173 FIPs, and ₹887B in AA-mediated loan disbursements, the AA framework is no longer a pilot — it's critical financial infrastructure. Every bank operating in India must function as an FIP (data provider) for deposit accounts. This is functionally equivalent to open banking mandates in the US/UK/EU but achieved through a different regulatory architecture (licensed intermediaries vs. direct APIs).

### EU/UK Research Notes

- **EU IPR is the strongest core banking forcing function globally.** The 10-second settlement mandate with 24/7/365 availability and equal pricing is unambiguous: if your core can't process in real time, you can't comply. No amount of middleware wrapping solves this — the ledger itself must support real-time posting. The SEPA Instant share is still only ~25% of credit transfers (Q1 2025), indicating massive adoption headroom.

- **CRR3 parallel calculation requirement:** Running both internal models and standardized approaches simultaneously is computationally expensive and data-intensive. Banks that relied on internal models to optimize capital requirements now face higher floor requirements AND the computational burden of maintaining two parallel calculation engines. This compounds the core infrastructure challenge.

- **DORA's third-party oversight and core banking vendors:** When ESAs designated critical ICT third-party providers in November 2025, major core banking vendors (e.g., Temenos, FIS, Finastra) likely fell within scope. Banks using these vendors must now maintain detailed registers of the vendor relationship, assess concentration risk, and demonstrate that the vendor's operational resilience satisfies DORA requirements. For banks unhappy with their core vendor's resilience posture, DORA provides regulatory justification for vendor change.

- **FCA Consumer Duty and savings inertia:** The £4B/year consumer benefit from higher savings rates post-Consumer Duty demonstrates the regulation's effectiveness. But the FCA's ongoing concern about largest firms paying below-market rates on easy access products suggests further supervisory action. For deposit infrastructure vendors, this creates demand for real-time competitive benchmarking and dynamic pricing capabilities.

- **PSD3 consent dashboards:** The requirement for consent dashboards where account holders can see and manage all third-party access to their accounts creates a new UI/UX requirement for every institution offering deposit accounts in the EU. This is a middleware function but requires integration with the core's account access control layer.

---

*End of regulatory landscape research for account products and core banking. All data points sourced from cited references as of March 15, 2026. Items marked [unverified] require manual confirmation from primary regulatory sources.*
