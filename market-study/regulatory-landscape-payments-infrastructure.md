# Regulatory Landscape & Mandates: Payments Technology Infrastructure Investment

**Research Date:** March 15, 2026
**Scope:** USA, India, UK/Europe, Brazil

---

## Table of Contents

1. [United States](#1-united-states)
2. [India](#2-india)
3. [UK / Europe](#3-uk--europe)
4. [Brazil](#4-brazil)
5. [Cross-Market Summary Matrix](#5-cross-market-summary-matrix)

---

## 1. United States

### 1.1 FedNow — Real-Time Payments Infrastructure

| Attribute | Detail |
|-----------|--------|
| **Status** | Live since July 2023; rapid scaling phase |
| **Participating institutions** | 1,600+ financial institutions across all 50 states (as of early 2026); community banks and credit unions comprise >95% of participants |
| **Transaction volumes (2025)** | 8.4 million settled payments (459% growth vs. 2024); average daily volume ~23,050 payments |
| **Transaction value (2025)** | $853.4 billion total; average payment $101,435 |
| **Transaction cap** | Raised from $1M to $10M (November 2025) to unlock real estate, corporate payroll, and treasury use cases |

**Planned enhancements (2026):**
- New API suite for streamlined data integration and product development
- Account activity threshold features for customizable fraud velocity/dollar controls
- Exception Resolution Service expanded to cover instant payment transactions (previously ACH-only)
- Continued onboarding acceleration (one institution went live in 5 days in 2025)

**Infrastructure investment implications:** All banks — particularly mid-tier and community institutions — must invest in real-time payment rails connectivity, liquidity management systems, and 24/7/365 operational capabilities. The 95%+ community bank representation signals this is no longer optional for smaller institutions.

> Sources: [FedNow Volume Stats](https://www.frbservices.org/resources/financial-services/fednow/volume-value-stats), [Digital Transactions (Jan 2026)](https://www.digitaltransactions.net/fednow-tallies-more-than-1600-fis-in-its-real-time-payments-service/), [Federal Reserve 2026 Enhancements](https://www.frbservices.org/news/fed360/issues/121625/general-2026-fees-payment-system-enhancements)

---

### 1.2 Durbin Amendment — Debit Interchange & Routing

| Attribute | Detail |
|-----------|--------|
| **Status** | Enacted (2010); fee cap challenged in court (2025) |
| **Current cap** | 21¢ + 0.05% per transaction + optional 1¢ fraud-prevention adjustment |
| **Proposed cap reduction** | Fed proposed reducing base from 21¢ to 14.4¢ (~30% cut) in November 2023 |
| **Court ruling** | August 7, 2025: U.S. District Judge Traynor vacated Regulation II, ruling the Fed exceeded its authority; ruling stayed pending Fed appeal |
| **Routing mandate** | Every debit transaction must be enabled for processing over at least two unaffiliated networks; clarified in July 2023 to extend to online/card-not-present transactions |
| **Exemption threshold** | Banks with <$10B consolidated assets are exempt |

**Infrastructure investment implications:** Large issuers (>$10B assets) face dual-network routing compliance for all channels including digital/card-not-present. If the proposed 14.4¢ cap takes effect, covered issuers face ~30% interchange revenue reduction, pressuring them to invest in processing efficiency. Smaller issuers are exempt but increasingly adopt compliance infrastructure voluntarily for network interoperability.

> Sources: [LegalClarity — Durbin Amendment](https://legalclarity.org/durbin-amendment-debit-card-interchange-fees-and-routing-rules/), [Pay Stream — 2025 Ruling](https://www.mypaystream.com/insights/marginsontheline), [Federal Reserve Regulation II Data](https://www.federalreserve.gov/paymentsystems/RegII_Additional_information_proposed_methodology.htm)

---

### 1.3 CFPB Section 1033 — Open Banking Rule

| Attribute | Detail |
|-----------|--------|
| **Status** | Finalized October 2024; enforcement enjoined by Kentucky federal court (November 2025); CFPB announced intent to "substantially revise" the rule |
| **Scope** | Checking accounts, prepaid cards, credit cards, mobile wallets (Apple Pay, Google Pay, PayPal, Zelle, Venmo) |

**Original compliance timeline (staggered by institution size):**

| Tier | Deadline |
|------|----------|
| Largest institutions | April 1, 2026 (now June 2026 per revised schedule) |
| Tier 2 | April 1, 2027 |
| Tier 3 | April 1, 2028 |
| Tier 4 | April 1, 2029 |
| Smallest institutions | April 1, 2030 |

**Current legal status:** The Trump administration's CFPB leadership declared the rule "unlawful" and filed to dismiss/vacate it. On July 29, 2025, the CFPB committed to initiating a new rulemaking on an "accelerated timeline." The stay was granted with 90-day status report requirements. Fintech trade associations intervened to preserve existing compliance deadlines.

**Infrastructure investment implications:** Despite legal uncertainty, large data providers are proceeding with API infrastructure investments for data-sharing, as the underlying statutory mandate (Dodd-Frank Section 1033) remains law. Banks must build consumer data access APIs, consent management systems, and third-party provider authentication. The rule's ultimate scope — once rewritten — will determine the depth of investment required.

> Sources: [Moody's Open Banking Analysis](https://www.moodys.com/web/en/us/kyc/resources/insights/open-banking-in-the-us-what-the-2026-cfpb-rule-means-for-consumers-banks-and-fintechs.html), [ABA Banking Journal — Court Injunction](https://bankingjournal.aba.com/2025/11/kentucky-federal-court-enjoins-cfpb-from-enforcing-current-1033-final-rule/), [JDSupra — CFPB Rulemaking Reopen](https://www.jdsupra.com/legalnews/cfpb-to-reopen-1033-open-banking-2277269/)

---

### 1.4 GENIUS Act — Stablecoin Regulatory Framework

| Attribute | Detail |
|-----------|--------|
| **Status** | Signed into law July 18, 2025 |
| **Effective date** | Earlier of 18 months after enactment (~January 2027) or 120 days after regulators issue final rules |
| **Permitted issuers** | Three tiers: state-qualified (capped at $10B outstanding issuance), federal-qualified (OCC-supervised), FDIC-insured depository subsidiaries |
| **Regulator mandate** | Fed, FDIC, OCC, NCUA must issue implementing regulations within 1 year of enactment (~July 2026) |

**Infrastructure investment implications:** Banks seeking to issue or custody stablecoins must build tokenization infrastructure, reserve management systems meeting the Act's 1:1 backing requirements, and compliance frameworks. The Act creates a competitive pathway for both banks and non-bank issuers, pressuring traditional payment providers to evaluate stablecoin-based payment rails.

> Sources: [National Law Review — Senate Passes GENIUS Act](https://natlawreview.com/article/senate-passes-genius-act-landmark-federal-stablecoin-bill-advances-house), [KPMG — GENIUS Act Framework](https://kpmg.com/us/en/articles/2025/genius-act-payment-stablecoin-framework-senate-approves.html)

---

### 1.5 Summary: US Investment Drivers

| Mandate | Deadline Pressure | Tier Most Affected | Investment Domain |
|---------|-------------------|---------------------|-------------------|
| FedNow adoption | Ongoing (competitive) | Mid-tier & community banks | Real-time rails, 24/7 ops, liquidity |
| Durbin routing | In effect; cap change pending appeal | Issuers >$10B assets | Multi-network routing, digital channels |
| Section 1033 | June 2026 (largest); legal uncertainty | Largest banks first | Open banking APIs, consent mgmt |
| GENIUS Act | Regulations by July 2026; effective ~Jan 2027 | All tiers (opportunity) | Tokenization, reserve mgmt, compliance |

---

## 2. India

### 2.1 UPI Evolution

| Attribute | Detail |
|-----------|--------|
| **2025 transaction volume** | 228 billion transactions worth ₹300 trillion (33% YoY growth) |
| **Market share** | ~84% of retail digital payment volumes in FY2024-25 |
| **December 2025 record** | 21.6 billion transactions worth ₹30 trillion in a single month |

**Product innovations and their infrastructure requirements:**

| Feature | Status | What It Requires |
|---------|--------|-----------------|
| **UPI Lite** | Live; 57 banks onboarded | On-device wallet integration; reduced core banking load for sub-₹500 txns; single-factor authentication |
| **UPI Credit on RuPay** | Live | Credit line origination systems linked to UPI rails; RuPay network integration |
| **UPI Lite X** | Pilot | Offline transaction capability; NFC-based; requires new device-level payment infrastructure |
| **123PAY** | Live | IVR, feature phone, and missed-call payment infrastructure for non-smartphone users |
| **Tap & Pay** | Scaling | NFC-enabled payment acceptance; POS terminal upgrades |
| **Autopay mandates** | Live | Recurring payment infrastructure; e-mandate management systems |

**Cross-border UPI expansion:**

| Country/Region | Status | Infrastructure Need |
|----------------|--------|---------------------|
| Singapore (PayNow-UPI) | Live (Feb 2023) | Real-time cross-border settlement; FX conversion |
| UAE | Live (direct merchant integration) | Merchant acquiring network; multi-currency processing |
| Japan (NTT Data MoU) | Signed Oct 2025 | Merchant POS integration; settlement layer |
| Malaysia (PayNet-DuitNow) | Signed Feb 2026 | QR interop; bilateral settlement |
| France, Nepal, Bhutan, Mauritius, Sri Lanka, Qatar | Various stages of live | Local acquiring partnerships |
| Oman, Cyprus | In development for 2026 | Network build-out |

**NRI access:** Banks now permit UPI registration using international mobile numbers for NRIs with NRE/NRO accounts in select countries, requiring banks to build international number verification and KYC flows.

> Sources: [Mint — UPI 2025 Records](https://origin-pre-prod.livemint.com/industry/banking/upi-smashes-records-in-2025-what-s-next-for-india-s-payment-giant-11767273727763.html), [NPCI — UPI Lite](https://www.npci.org.in/what-we-do/upi-lite/product-overview), [Rupeeflo — UPI Global](https://www.rupeeflo.com/resources/upi-global-rollout-updates-where-nris-can-use-upi-outside-india-and-regulatory-updates-in-2025), [NPCI International — Malaysia](https://www.prnewswire.co.uk/news-releases/npci-international-signs-agreement-with-payments-network-malaysia-to-enable-upi-and-duitnow-acceptance-in-india-and-malaysia-302686409.html)

---

### 2.2 RBI Tokenization — Card-on-File Mandate

| Attribute | Detail |
|-----------|--------|
| **Status** | Mandatory; phased enforcement since 2022 |
| **Latest deadline** | April 1, 2026 for full compliance with updated Authentication Mechanisms for Digital Payment Transactions Directions, 2025 |
| **Core requirement** | Only card schemes and card-issuing banks may store actual cardholder data; merchants and payment aggregators must use tokenized formats |
| **CoFT enablement** | Since December 2023, banks can enable Card-on-File Tokenization directly through mobile/internet banking channels |

**Infrastructure investment required:**
- Token provisioning and lifecycle management systems
- Merchant-side token vault integration
- Updated checkout flows across all digital channels
- Network-level token routing (card scheme interoperability)

**Impact by tier:** All banks issuing cards are affected. Larger issuers bear the tokenization infrastructure cost; smaller issuers can leverage card network solutions but must still update their systems. Merchants and payment aggregators face the heaviest compliance burden.

> Sources: [The Paypers — RBI Card-on-File Tokenization](https://thepaypers.com/fraud-and-fincrime/interviews/rbis-card-on-file-storage-restrictions-rules-is-tokenization-the-answer), [RBI Notification](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12345&Mode=0)

---

### 2.3 Digital Rupee (e₹) CBDC

| Attribute | Detail |
|-----------|--------|
| **Status** | Pilot phase (wholesale since Nov 2022; retail since Dec 2022); expanding |
| **Wallet providers** | Mobikwik (full-scale, early 2025), CRED (beta, Jan 2025), plus participating banks |
| **Programmability pilot** | Digital food currency pilot launched in Puducherry (Feb 2026); plans to extend to 3-4 additional states |
| **Cross-border** | RBI exploring bilateral/multilateral CBDC settlement pilots |

**Infrastructure investment required:**
- CBDC wallet integration (banks and fintechs)
- Programmable money / smart contract capabilities for targeted subsidies
- UPI QR interoperability with e₹ wallets
- Cross-border CBDC settlement systems

> Sources: [NewsBytesApp — RBI e-Rupee Expansion](https://www.newsbytesapp.com/news/business/rbi-expands-erupee-pilot-to-explore-cross-border-cbdc-use-cases/story), [MediaNama — Digital Food Currency Pilot](https://www.medianama.com/2026/02/223-centre-digital-currency-pilot-food-subsidies-puducherry/)

---

### 2.4 RBI Digital Payments Regulatory Framework (2025-2026)

| Regulation | Effective Date | Key Requirements |
|-----------|---------------|-----------------|
| **Digital Banking Channels Authorisation Directions** | January 1, 2026 | Uniform requirements for internet/mobile banking; enhanced cybersecurity; board-level accountability |
| **Payment Aggregator Master Directions, 2025** | September 2025 (phased compliance through 2026) | Unified PA-O (online), PA-P (physical), PA-CB (cross-border) framework; capital requirements; data localization; escrow structures |
| **Authentication Mechanisms Directions** | April 1, 2026 | Updated digital payment authentication standards for all PSPs |
| **Payments Infrastructure Development Fund (PIDF)** | Extended through Dec 2025 | Target: 30 lakh new touch points/year; 90% subsidy in special focus areas; Aadhaar biometric and soundbox devices eligible |
| **Self-Regulatory Organisation (SRPA)** | Recognized November 2025 | Industry self-governance for payment system operators; compliance monitoring; dispute resolution |

**Tier impact:** All banks operating digital channels must comply with the Digital Banking Channels Directions. Payment aggregators (Razorpay, PhonePe, BillDesk, etc.) face the heaviest new compliance burden under the PA Master Directions. The PIDF subsidies primarily benefit payment infrastructure providers deploying in rural/underserved areas.

> Sources: [ET BFSI — RBI Regulations 2026](https://www.bfsi.economictimes.indiatimes.com/articles/upcoming-rbi-regulations-for-2026-what-to-expect-in-digital-banking-and-financial-oversight/126278663), [RBI — PIDF](https://www.rbi.org.in/scripts/FS_Notification.aspx?Id=12584&Mode=0&fn=9), [ET BFSI — SRPA Recognition](https://bfsi.economictimes.indiatimes.com/articles/rbi-grants-sro-status-to-self-regulated-pso-association-for-payment-system-operators/125245250)

---

### 2.5 NPCI International (NIPL) Expansion

| Attribute | Detail |
|-----------|--------|
| **Partnership network** | ~20 partners across 9+ countries |
| **Merchant reach** | 2+ million international merchants onboarded |
| **UPI One World** | Launched Feb 2026; enables foreign visitors to make UPI payments in India without local bank account/SIM; ₹25,000/txn, ₹50,000/month limits |
| **Global cross-border txns** | 1.48 million in Dec 2024 (2x YoY growth) |

**Infrastructure investment required for participating banks:** Cross-border settlement capabilities, multi-currency treasury management, international KYC/AML compliance, QR interoperability across national payment systems.

> Sources: [NPCI — UPI One World](https://assets.thehansindia.com/technology/tech-news/npci-introduces-upi-one-world-wallet-for-global-delegates-at-india-ai-impact-summit-2026-1049007), [Outlook Business — UPI Japan](https://www.outlookbusiness.com/news/upi-enters-japan-npcis-international-arm-signs-mou-with-ntt-data-to-enable-payments-for-indian-tourists)

---

### 2.6 Summary: India Investment Drivers

| Mandate | Deadline Pressure | Tier Most Affected | Investment Domain |
|---------|-------------------|---------------------|-------------------|
| UPI Lite / Credit / NFC | Ongoing (competitive) | All participating banks | Core banking offload, credit systems, NFC infra |
| Cross-border UPI | Rolling (country-by-country) | Banks with international presence | FX, settlement, compliance |
| Card tokenization | April 1, 2026 | All card issuers & acquirers | Token vaults, checkout flows |
| Digital Rupee (e₹) | Pilot expansion 2026 | Large banks (pilot participants) | CBDC wallets, programmability |
| Digital Banking Directions | January 1, 2026 | All commercial banks | Cybersecurity, auth, governance |
| PA Master Directions | Phased through 2026 | Payment aggregators | Licensing, capital, data localization |

---

## 3. UK / Europe

### 3.1 PSD3 / PSR — Payment Services Regulation Reform

| Attribute | Detail |
|-----------|--------|
| **Status** | Informal trilogue agreement reached November 27, 2025; final text expected in coming weeks |
| **Expected implementation** | H2 2027 at earliest, possibly early 2028 |
| **Transition period** | 2-2.5 years for existing payment/e-money institutions to comply with new prudential requirements |

**Structural change:** PSD2 is replaced by two instruments:
- **PSR** (Regulation): Directly applicable across EU — covers SCA, open banking, user rights, transparency
- **PSD3** (Directive): National transposition required — covers licensing, prudential requirements

**Key changes from PSD2:**

| Area | Change | Investment Required |
|------|--------|---------------------|
| **E-money integration** | EMIs become sub-category of payment institutions; EMD2 repealed | Licensing/structural reorganization for EMIs |
| **APP fraud liability** | Expanded liability for authorized push payment impersonation fraud | Fraud detection systems, liability reserves, customer communication |
| **Open banking** | Stricter dedicated interface requirements; consent dashboards; limited grounds for refusing banking services to TPPs | API infrastructure upgrades, consent management UX |
| **Supervision** | Stronger cross-border supervisory powers; product intervention capabilities | Compliance and reporting systems |
| **Confirmation of Payee** | Mandatory 24 months after entry into force | Name-matching verification systems |

**Tier impact:** All licensed payment institutions and e-money institutions across the EU. Large banks face the broadest investment across fraud, APIs, and compliance. EMIs face potential relicensing.

> Sources: [Norton Rose Fulbright — PSD3/PSR Preparation](https://www.nortonrosefulbright.com/en/inside-fintech/blog/2026/03/eu-payment-services-reform-preparing-for-psd3-and-psr), [Norton Rose Fulbright — PSD3/PSR Readiness](https://www.nortonrosefulbright.com/en/knowledge/publications/cedd39c6/psd3-and-psr-from-provisional-agreement-to-2026-readiness), [SZA — PSD3/PSR Overview](https://www.sza.de/en/thinktank/psd3-psr-eu-payment-services-regulation)

---

### 3.2 EU Instant Payments Regulation (IPR)

| Attribute | Detail |
|-----------|--------|
| **Status** | Adopted March 13, 2024; phased deadlines in force |
| **Core mandate** | All PSPs offering credit transfers must also offer instant credit transfers at equal or lower charges |

**Compliance timeline:**

| Requirement | Euro Area Deadline | Non-Euro Area Deadline |
|------------|-------------------|----------------------|
| **Receive instant payments** | January 9, 2025 ✅ | April 9, 2027 |
| **Send instant payments** | October 9, 2025 | July 9, 2027 (EMIs/PIs); June 9, 2028 (outside business hours) |
| **Verification of Payee** | October 9, 2025 | October 9, 2025 |
| **Equal charges** | January 9, 2025 ✅ | January 9, 2027 |

**Infrastructure investment required:**
- 24/7/365 instant payment processing capability
- Verification of Payee (name-matching) systems — free to consumers
- Sanctions screening within the 10-second execution window
- Liquidity management for continuous settlement

**Tier impact:** All PSPs in the EU. Euro-area institutions face the most immediate deadlines. Non-euro-area banks (e.g., Sweden, Poland, Czech Republic) have until 2027-2028 but must begin infrastructure planning now. EMIs and smaller payment institutions have slightly extended timelines.

> Sources: [ECB — Instant Payments Regulation](https://www.ecb.europa.eu/paym/integration/retail/instant_payments/html/instant_payments_regulation.en.html), [Osborne Clarke — IPR Obligations](https://www.osborneclarke.com/insights/what-are-key-obligations-and-timelines-eu-instant-payments-regulation)

---

### 3.3 ISO 20022 Migration — SWIFT

| Attribute | Detail |
|-----------|--------|
| **Status** | Coexistence period ended November 22, 2025; MX-only era in effect |
| **Bank readiness** | Nearly half of banks were behind on ISO 20022 readiness prior to the deadline |

**Key deadlines:**

| Date | Requirement |
|------|------------|
| **November 22, 2025** ✅ | All cross-border payments must use ISO 20022 MX format via FINplus; legacy MT payment messages (MT102, MT103 REMIT, MT201, MT203) rejected |
| **January 2026** | SWIFT in-flow translation service (MX→MT) becomes chargeable |
| **November 2026** | Unstructured postal addresses forbidden; only structured/hybrid addresses accepted |
| **November 2026** | Exceptions & Investigations (E&I) modernization — banks must receive ISO 20022 E&I messages |
| **November 2027** | Banks must send E&I messages in ISO 20022 format |

**Contingency:** SWIFT provides temporary conversion services for institutions unable to process MX natively, but limited to <15,000 messages/month and subject to fees.

**Infrastructure investment required:**
- Core banking message format migration (MT→MX)
- Address data remediation across customer databases
- Exceptions and investigations workflow modernization (replacing ~40 years of free-text manual processes)
- Compliance system updates for enriched ISO 20022 data fields

**Tier impact:** All banks participating in SWIFT cross-border payments. Largest impact on mid-tier and regional banks with legacy correspondent banking infrastructure. Tier-1 banks largely migrated; Tier-2/3 banks face the most remediation work, particularly on address data and E&I systems.

> Sources: [SWIFT — ISO 20022 Roadmap](https://www.swift.com/standards/iso-20022/iso-20022-programme/cbpr-roadmap), [BNY — End of Coexistence](https://www.bny.com/assets/corporate/documents/pdf/iso-20022-end-of-co-existence_-may-2025-final.pdf), [Red Compass Labs — 2026 Deadlines](https://www.redcompasslabs.com/insights/what-now-iso-20022-deadlines-in-2026-onwards/)

---

### 3.4 Open Banking → Open Finance

#### UK Direction

| Attribute | Detail |
|-----------|--------|
| **Current scale** | 16+ million users; 53% YoY growth in open banking payments |
| **VRP adoption** | Variable Recurring Payments = 16% of all open banking transactions |
| **Phase 1 VRP go-live** | Q1 2026 for utilities, financial services, government payments |
| **Phase 2 VRP** | E-commerce expansion (timeline TBD) |
| **New operator** | UK Payments Initiative (UKPI) established by 31 firms to coordinate VRP delivery |
| **Legislation** | HM Treasury expected to introduce legislation in 2026 granting FCA new open banking rule-setting powers |
| **FCA consultation** | New long-term regulatory framework rules consultation expected before end of 2026 |

#### EU Direction (FIDA — Financial Data Access Regulation)

| Attribute | Detail |
|-----------|--------|
| **Status** | Trilogue negotiations ongoing; Council and Parliament adopted mandates December 2024 |
| **Scope** | Extends beyond payments to mortgages, loans, savings, investments, insurance, pensions, crypto-assets |
| **Compliance period** | 30-32 months after adoption for financial institutions |
| **Key provision** | Large digital platforms designated as DMA gatekeepers may be excluded from becoming financial information service providers |

**Infrastructure investment required:** API infrastructure expansion beyond payment accounts to cover investment, insurance, and pension data. Consent management systems must scale to cover broader financial product sets. UK firms must prepare for VRP infrastructure supporting recurring payment use cases.

> Sources: [FCA — Open Banking Progress](https://www.fca.org.uk/news/news-stories/open-banking-2025-progress), [PSR — Open Banking Next Steps](https://www.psr.org.uk/news-and-updates/latest-news/news/psr-and-fca-set-out-next-steps-for-open-banking/), [The Paypers — FIDA Explainer](https://thepaypers.com/regulations/explainers/explainer-understanding-fida-proposal-and-europes-open-finance-agenda)

---

### 3.5 Digital Euro (ECB CBDC)

| Attribute | Detail |
|-----------|--------|
| **Status** | Preparation phase completed (Nov 2023 – Oct 2025); awaiting legislation |
| **Decisive vote** | 2026 in European Parliament |
| **Political agreement target** | Early 2026 |
| **Launch target** | 2029 (contingent on legislation passing in 2026) |
| **Post-legislation buildout** | 2-3 years needed after legislation passes |

**Progress to date:**
- Draft digital euro scheme rulebook developed (UX, brand, implementation specs, risk management)
- Infrastructure providers selected (private companies + 6 national central banks)
- User research conducted with 70+ market participants
- Offline functionality and accessibility features designed

**Key risk:** European Parliament remains divided; missing legislation is the primary bottleneck.

**Strategic driver:** Concern over European dependence on US payment firms (Visa, Mastercard, PayPal) amid geopolitical tensions is accelerating the political urgency.

**Infrastructure investment required (if approved):** Distribution infrastructure for banks; wallet/app development; offline payment capabilities; merchant acceptance integration; interoperability with existing payment schemes.

> Sources: [Irish Times — Digital Euro 2026 Vote](https://www.irishtimes.com/business/financial-services/2026/01/05/down-to-the-wire-ecbs-digital-euro-project-faces-decisive-vote-in-2026/), [Reuters — ECB Political Deal](https://www.reuters.com/business/finance/ecb-hopes-have-political-deal-digital-euro-by-early-2026-2025-05-15/), [ECB — Third Progress Report](https://www.ecb.europa.eu/euro/digital_euro/progress/html/ecb.deprp202507.en.html)

---

### 3.6 Summary: UK/Europe Investment Drivers

| Mandate | Deadline Pressure | Tier Most Affected | Investment Domain |
|---------|-------------------|---------------------|-------------------|
| EU Instant Payments | Oct 2025 (euro-area send); 2027 (non-euro) | All EU PSPs | 24/7 processing, VoP, liquidity |
| PSD3/PSR | H2 2027 – early 2028 | All PIs, EMIs, banks | Fraud, APIs, licensing, CoP |
| ISO 20022 | Nov 2025 ✅ (MX-only); Nov 2026 (addresses, E&I) | Mid-tier/regional banks | Message migration, data remediation |
| UK VRP / Open Banking | Q1 2026 (Phase 1); legislation 2026 | UK CMA9 banks, PIs | VRP infrastructure, API expansion |
| FIDA (Open Finance) | ~2028-2029 (30-32 months post-adoption) | All EU financial institutions | Multi-product APIs, consent mgmt |
| Digital Euro | 2029 (if legislation passes 2026) | All euro-area banks | Distribution, wallets, offline payments |

---

## 4. Brazil

### 4.1 PIX Evolution

| Attribute | Detail |
|-----------|--------|
| **User base** | ~170 million users (90% of Brazilian adults) |
| **Status** | Dominant national payment infrastructure; continuous feature expansion |

**Feature roadmap:**

| Feature | Status | Launch Date | Description |
|---------|--------|-------------|-------------|
| **Pix Automático** | Live | June 16, 2025 | Standardized recurring payments through Central Bank infrastructure; replaces fragmented automatic debit agreements; expected to serve ~60M Brazilians without credit cards |
| **Pix Parcelado** | Planned | September 2025 (targeted) | Installment payments: receiver gets full payment instantly; payer finances over time; credit risk borne by payer's institution |
| **Pix em Garantia** | Planned | 2026 | Merchants can use future PIX receivables as collateral for credit; reduces borrowing costs |
| **MED 2.0** | Planned | Dec 2025 (launch) / Feb 2026 (mandatory) | Enhanced fraud dispute mechanism via self-service banking apps |
| **Contactless Pix** | Planned | 2026 | Payment by proximity (NFC-like) |
| **Pix Internacional** | Under development | TBD | Cross-border PIX; facing regulatory coordination challenges |

**Infrastructure investment required:**
- Recurring payment engines (Pix Automático)
- Credit origination systems integrated with payment rails (Pix Parcelado)
- Receivables registration and collateral management (Pix em Garantia)
- Fraud detection and automated dispute resolution (MED 2.0)
- NFC/proximity payment terminal upgrades (Contactless Pix)

> Sources: [Estadão — PIX 2026](https://einvestidor.estadao.com.br/educacao-financeira/pix-em-2026-novas-funcionalidades-regras-seguranca-aproximacao-futuro), [Agência Brasil — Pix Parcelado](https://agenciabrasil.ebc.com.br/economia/noticia/2025-04/pix-parcelado-deve-ser-lancado-em-setembro-diz-banco-central), [Valor Internacional — Auto Pix](https://valorinternational.globo.com/markets/news/2025/06/16/after-auto-pix-installments-are-next-step-in-central-bank-agenda.ghtml)

---

### 4.2 Drex (Brazilian CBDC)

| Attribute | Detail |
|-----------|--------|
| **Status** | Phase 2 concluding; original blockchain platform shut down November 2025 |
| **Phase 1** | Completed; 16 bank-led consortiums tested digital real on decentralized networks |
| **Phase 2** | October 2024 – early 2026; 13 use cases including receivables, collateralization, trade finance, FX, carbon credits, real estate |
| **Platform pivot** | Central Bank shut down the original blockchain platform due to high maintenance costs and unresolved privacy issues |
| **Phase 3** | Discussions beginning early 2026 |

**Post-pivot direction:** Banks are exploring privately issued stablecoins as alternatives to the state-backed CBDC approach. The original vision of Drex replacing Brazil's STR settlement system is being reconsidered.

**Infrastructure investment implications:** The pivot introduces uncertainty. Banks that invested heavily in blockchain-based Drex infrastructure may need to redirect toward stablecoin issuance/custody capabilities. The Central Bank's continued exploration signals that some form of tokenized settlement infrastructure will be required, but the technology stack is in flux.

> Sources: [Drex Guide — Pilot Overview](https://drex.guide/docs/pilot-project/overview), [Digital Pound Foundation — Drex Phase 2](https://digitalpoundfoundation.com/brazils-drex-cbdc-pilot-enters-second-phase-with-focus-on-privacy-and-interoperability/), [Valor Internacional — Drex Platform Shutdown](https://valorinternational.globo.com/markets/news/2025/11/05/central-bank-shuts-drex-platform-clearing-path-for-stablecoins.ghtml)

---

### 4.3 Open Finance Brasil

| Attribute | Detail |
|-----------|--------|
| **Status** | Global leader; live and scaling |
| **Active consents** | 128 million data-sharing authorizations (early 2026) — #1 globally |
| **Growth** | 44% increase from 62M consents in January 2025 |
| **Weekly API communications** | 4.4 billion between institutions |
| **Credit released via Open Finance data** | R$31 billion (2021-2025) |
| **Industry investment** | R$2+ billion invested by FEBRABAN-associated banks |

**2026 expansion plans:**

| Feature | Timeline | Description |
|---------|----------|-------------|
| **Digital credit portability** | February 2026 | 100% digital credit portability starting with unsecured personal credit; expanding to payroll-deductible credit |
| **Pix by proximity** | 2026 | Proximity-based Pix payments integrated with Open Finance |
| **Journey Without Redirection (JSR)** | Ongoing improvements | Streamlined user consent flows without bank-app redirections |

> Sources: [Contadores — Open Finance Brasil Global Lead](https://www.contadores.cnt.br/noticias/empresariais/2026/01/28/open-finance-brasil-lidera-ranking-global-com-128-milhoes-de-consentimentos-ativos.html), [Let's Money — Credit Portability 2026](https://www.letsmoney.com.br/open-finance/open-finance-2026-como-a-portabilidade-digital-de-credito-acaba-com-a-inercia-bancaria/), [ANBC — Five Years of Open Finance](https://anbc.org.br/en/five-years-of-open-finance/)

---

### 4.4 Central Bank of Brazil — Regulatory Direction

| Regulation | Status | Key Requirements |
|-----------|--------|-----------------|
| **PIX authorization mandate** | In force; phased | Only authorized FIs/PIs can participate in PIX; unauthorized institutions must obtain authorization by March 2025–May 2026 depending on join date |
| **Minimum capital requirements** | January 1, 2026 | R$5 million minimum share capital and net equity for PIX participants |
| **MED 2.0 (fraud disputes)** | Mandatory February 2026 | Self-service fraud dispute resolution in banking apps |
| **Token applicant regulation** | Under consultation | Rules for tokenized asset participants |
| **Interoperability fees** | Under consultation | Fee structures between registrars in open arrangements |
| **Guarantee fund revision** | Planned | Alignment with international standards |

**Tier impact:** The PIX authorization and capital requirements most heavily affect smaller fintechs and payment institutions that joined PIX early without full BCB authorization. Larger banks face investment pressure from Pix Automático, Parcelado, and Open Finance feature mandates.

> Sources: [Machado Meyer — BCB Regulatory Agenda 2025/2026](https://www.machadomeyer.com.br/en/recent-publications/publications/banking-insurance-and-finance/central-bank-learn-about-the-regulatory-agenda-for-2025-2026), [Demarest — PIX Eligibility](https://www.demarest.com.br/en/bc-publishes-new-guidelines-on-pix-eligibility-through-bcb-resolution-no-429/)

---

### 4.5 Summary: Brazil Investment Drivers

| Mandate | Deadline Pressure | Tier Most Affected | Investment Domain |
|---------|-------------------|---------------------|-------------------|
| Pix Automático / Parcelado | Live / Sep 2025 | All PIX participants | Recurring payments, credit origination |
| MED 2.0 | Mandatory Feb 2026 | All PIX participants | Fraud detection, dispute resolution |
| PIX authorization | March 2025 – May 2026 (phased) | Fintechs, smaller PIs | Licensing, compliance, capital |
| Capital requirements | January 1, 2026 | Smaller PIX participants | Capital adequacy |
| Open Finance credit portability | February 2026 | All participating FIs | Credit systems, API infrastructure |
| Drex / tokenization | Uncertain (pivot underway) | Large banks (pilot participants) | Stablecoin/tokenization infrastructure |
| Contactless Pix | 2026 | Acquirers, merchants | NFC/proximity terminal upgrades |

---

## 5. Cross-Market Summary Matrix

### Regulatory Urgency Heatmap (by deadline proximity)

| Market | Immediate (2025–H1 2026) | Near-term (H2 2026–2027) | Medium-term (2028+) |
|--------|--------------------------|--------------------------|----------------------|
| **USA** | FedNow scaling (ongoing); GENIUS Act regulations (Jul 2026) | Section 1033 (rewrite TBD); Durbin cap (pending appeal) | Section 1033 smaller tiers (2028-2030) |
| **India** | Digital Banking Directions (Jan 2026); Tokenization (Apr 2026); PA Master Directions (phased) | UPI cross-border expansion; e₹ programmability pilots | e₹ full rollout |
| **UK/EU** | EU Instant Payments send (Oct 2025); ISO 20022 address/E&I (Nov 2026); UK VRP Phase 1 (Q1 2026) | PSD3/PSR implementation (H2 2027+); FIDA trilogue | FIDA compliance (2028-29); Digital Euro (2029) |
| **Brazil** | PIX authorization (phased–May 2026); MED 2.0 (Feb 2026); Capital requirements (Jan 2026); Credit portability (Feb 2026) | Pix em Garantia; Contactless Pix; Drex Phase 3 direction | Pix Internacional |

### Infrastructure Investment Themes Across Markets

| Theme | USA | India | UK/EU | Brazil |
|-------|-----|-------|-------|--------|
| **Real-time payments** | FedNow adoption | UPI scaling (228B txns) | EU IPR mandate | PIX feature expansion |
| **Open banking / finance** | Section 1033 (uncertain) | Account Aggregator ecosystem | PSD3 APIs; FIDA | Open Finance Brasil (global #1) |
| **CBDC** | N/A (stablecoin via GENIUS Act) | e₹ pilots expanding | Digital Euro (2029 target) | Drex pivoting from blockchain |
| **Tokenization** | Stablecoin framework | Card-on-file tokenization mandate | — | Drex tokenization use cases |
| **Fraud / security** | FedNow risk controls | RBI authentication directions | PSD3 APP fraud liability | MED 2.0 |
| **Cross-border** | — | UPI international (9+ countries) | ISO 20022 (MX-only) | Pix Internacional (early stage) |
| **ISO 20022** | Domestic adoption ongoing | NPCI alignment discussions | SWIFT MX-only era; address remediation by Nov 2026 | — |

---

*End of regulatory landscape research. All data points sourced from cited references as of March 15, 2026.*
