# Chapter 02.02: Commercial Cards — Opportunity Analysis

*Prepared for Zeta's executive team and board. March 2026.*

---

## Executive Summary

The commercial card technology market — what banks and corporates spend on card issuance platforms, corporate card program management, and expense management software — is a **$28–30 billion market** growing to **$75–90 billion by the early 2030s**. Commercial card spend itself crossed $4 trillion globally in 2023 ([Datos Insights](https://datos-insights.com/press-release/commercial-card-spending-reaches-us4-trillion/)), but only $3 trillion of an $80 trillion B2B payments addressable market currently flows through card rails — less than 4% penetration ([Mastercard](https://www.investing.com/news/transcripts/mastercard-at-morgan-stanley-tmt-navigating-a-100-trillion-opportunity-93CH-4541736)).

Seven structural shifts are creating the largest wave of commercial card infrastructure investment in the category's history. Virtual cards are displacing checks in B2B payments ($3.95T → $14.6T by 2029). Card issuance and spend management are converging — confirmed by three acquisitions in twelve months (Capital One–Brex $5.15B, Amex–Center, Paylocity–Airbase $325M). Benefits cards are expanding through regulatory tailwinds in India and the $159B US HSA market. AI is moving spend management from after-the-fact audit to authorization-time policy enforcement.

The central structural finding: **the commercial card market is bifurcated between card issuance (bank domain) and spend management (software domain)**. Only five platforms credibly span both sides. Banks are closing the gap through acquisition rather than internal build.

The most underserved buyer segment is **mid-size banks** that need commercial card capabilities for corporate clients but find legacy processors (FIS, Fiserv) over-engineered and expensive, and modern challengers (Brex, Ramp) designed for direct-to-corporate sales rather than bank infrastructure.

**For Zeta:** Electron Benefits is production-proven at scale — powering Pluxee India (11,000+ corporates, 3.5M+ consumers) and holding direct bank partnerships (IDFC FIRST, RBL). The proposed 4x increase in India's meal card tax exemption, if enacted, would significantly expand the addressable market. Electron Expense and Purchase Cards remain placeholders — the gap between proven benefits capability and unvalidated expense/purchase capability is the single most important internal question.

**Recommended actions:** Expand India benefits card partnerships (3–5 new banks), validate Electron Expense Cards through a pilot, build GST ITC reconciliation as a defensible differentiator, and develop the Quark Commercial Cards operational domain. Defer US enterprise T&E (SAP Concur and Ramp are entrenched) and do not pursue fleet cards (vertically integrated, poor fit).

---

# PART I — THE OPPORTUNITY

---

## 1. The Commercial Card Technology Market

### What flows through the rails

Commercial card spending crossed $4 trillion globally for the first time in 2023, growing 8% year-over-year, and is projected to exceed $6 trillion by 2029 ([Datos Insights, January 2025](https://datos-insights.com/press-release/commercial-card-spending-reaches-us4-trillion/)). In the United States alone, commercial card purchase volume reached $2.23 trillion in 2024, representing 20.7% of total US card purchase volume ([Nilson Report, Issue 1298, December 2025](https://nilsonreport.com/articles/us-commercial-cards-amex-mastercard-and-visa-in-2024/)).

### What banks and corporates spend on technology

The vendor-addressable technology market is orders of magnitude smaller than card spend but growing faster:

| Segment | Current Size | Projected | CAGR | Source |
|---------|-------------|-----------|------|--------|
| Card issuance platforms | $1.8B (2025) | $4.2B (2030) | ~19% | [Juniper Research](https://www.juniperresearch.com/press/modern-card-issuing-platforms-market-to-surpass-42-billion-by-2030-as-juniper-research-reveals-global-leaders-driving-fintech-innovation/) |
| Corporate card platforms | $21.4B (2024) | $51.3B (2033) | 10.2% | [Dataintelo](https://dataintelo.com/report/corporate-card-platform-market) |
| SaaS expense management | $5.5B (2024) | $21.9B (2034) | 15% | [Allied Market Research](https://www.prnewswire.com/news-releases/saas-based-expense-management-market-to-reach-usd-21-9-billion-globally-by-2034-at-15-cagr-allied-market-research-302707902.html) |

Combined vendor-addressable technology TAM: approximately **$28–30 billion today**, growing to **$75–90 billion** by the early 2030s.

Mastercard sizes the total commercial payments serviceable addressable market at $80 trillion, of which only $3 trillion currently flows through card rails — less than 4% penetration ([Mastercard at Morgan Stanley TMT Conference](https://www.investing.com/news/transcripts/mastercard-at-morgan-stanley-tmt-navigating-a-100-trillion-opportunity-93CH-4541736)). The United States accounts for approximately 75% of global B2B card spending ([Datos Insights](https://datos-insights.com/press-release/commercial-card-spending-reaches-us4-trillion/)).

### Spend by bank tier

| Tier | Commercial Card Role | Technology Approach | Opportunity Character |
|------|---------------------|--------------------|-----------------------|
| Tier 1 (top 50 global) | Issue commercial cards directly; operate proprietary programs; hold GSA SmartPay contracts | Build or buy best-of-breed; internal card management teams | Platform replacement and virtual card expansion. Long sales cycles, deep customization |
| Tier 2 (mid-size, $10B–$100B) | Need commercial card capability for corporate clients but cannot build internally | Buy/outsource; dependent on FIS or Fiserv, increasingly evaluating fintech alternatives | The primary growth market. Legacy processors are expensive and inflexible; modern challengers (Brex Embedded, Marqeta) are creating switching opportunities |
| Tier 3 (regional, $1B–$10B) | Offer commercial cards through agent-bank arrangements or do not offer them at all | Entirely outsourced via core provider or agent-bank partner | Benefits card programs through fintech partnerships; limited direct platform procurement |

Mid-size banks are the most underserved segment — and the segment where platform switching is actively occurring. Fifth Third Bank transitioned its entire $5.6B annual commercial card volume to Brex Embedded ([BusinessWire, December 2025](https://www.businesswire.com/news/home/20251209555474/en/Fifth-Third-and-Brex-Partner-to-Bring-AI-Powered-Finance-to-Businesses-Unlocking-$5.6B-in-Commercial-Card-Volume)). First Horizon Bank publicly migrated from Fiserv to DXC ([First Horizon](https://www.firsthorizon.com/Fiserv-DXC-Commercial-Card-Conversion)).

### By program type

- **Travel and entertainment (T&E) cards** are the fastest-growing segment, up 16% globally in 2023. India saw T&E spending more than double ([Datos Insights](https://datos-insights.com/press-release/commercial-card-spending-reaches-us4-trillion/)).
- **Virtual cards** are the transformational sub-segment. B2B virtual card transaction value is projected to grow from $3.95 trillion (2025) to $14.6 trillion by 2029, representing 83% of total virtual card volume ([Juniper Research, May 2025](https://www.juniperresearch.com/press/b2b-spending-to-dominate-global-virtual-cards-market/)).
- **Purchase cards** hold approximately 30–36% of commercial card market share, growing at 7–8% CAGR, increasingly embedded in procurement automation ([Business Research Insights](https://www.businessresearchinsights.com/market-reports/commercial-and-corporate-card-market-125229)).
- **Fleet cards** constitute a $1 trillion global market projected to reach $4.8 trillion by 2034 at 16.5% CAGR ([Allied Market Research](https://www.prnewswire.com/news-releases/fleet-card-market-was-valued-at-1-trillion-in-2024-in-the-short-term-and-to-reach-4-8-trillion-by-2034-globally-at-16-5-cagr-allied-market-research-302613431.html)), though this segment is heavily vertically integrated.

### By geography

- **United States**: dominant, with ~45% of the global corporate card market and ~75% of B2B card spending. Modern spend platforms (Ramp, Brex, BILL) are US-born and US-concentrated.
- **India**: the fastest-growth story. The prepaid card market is growing at 28–30% CAGR, with the corporate vertical representing 36% of total prepaid issuance ([IMARC Group](https://www.imarcgroup.com/india-prepaid-cards-market)). Employee benefits cards (meal, fuel, gift) constitute a distinctive, regulation-driven sub-market.
- **UK/Europe**: stable, compliance-driven growth. Commercial card interchange exemptions create distinct economics. PSD3, VAT reclaim automation, and CSRD ESG spend tracking are driving infrastructure investment.

---

## 2. How We Got Here

Commercial card programs were, for most of their history, consumer card platforms with corporate overlays. A bank issued a corporate credit card using the same infrastructure it used for consumer cards — same card management system, same processing pipeline, same lifecycle. Corporate-specific requirements — spending limits by department, merchant category restrictions, purchase order matching, expense reconciliation — were handled through customization or through separate systems that bolted on to the card platform.

This produced a structural separation. The **card issuance and processing layer** was the bank's domain — managed by processors like FIS/TSYS, Fiserv/First Data, or internal systems. The **spend management and policy enforcement layer** was the corporate's domain — managed by expense management platforms like SAP Concur, which integrated with the bank's card feeds but operated independently. The two layers communicated through batch file transfers, not real-time integration.

The model worked when commercial card programs were simple: one card per employee, monthly expense reports, quarterly reconciliation. It began to fail when program complexity increased: multiple card types per organization, real-time policy enforcement, virtual cards for ad-hoc spending, benefits card programs with tax compliance, and corporate hierarchies that drove authorization logic.

Starting around 2019, a new generation of platforms — Brex, Ramp, BILL/Divvy — demonstrated that unifying card issuance and spend management on a single platform created superior economics and user experience. Ramp reached $1 billion in annualized revenue by August 2025 ([Ramp, September 2025](https://www.prnewswire.com/news-releases/ramp-reaches-1-billion-in-annualized-revenue-302550637.html)). These platforms issue the card, enforce policy at authorization time, capture receipts, automate categorization, and reconcile to the general ledger — all in a single flow. The separation that defined the prior generation became the liability.

In parallel, India developed a distinct commercial card sub-market driven by tax regulation rather than corporate expense management. The Income Tax Act provisions for meal cards (Section 17(2)), fuel cards (Rule 3(2)), and gift cards (Rule 3(7)(iv)) created a benefits card ecosystem — with Zaggle, Pluxee (formerly Sodexo BRS), and Edenred as the primary platforms — that evolved independently of the US T&E-centric model.

---

## 3. Structural Shifts Creating Opportunity

### Shift 1: Virtual card explosion and AP automation

Virtual cards are the highest-growth segment in commercial payments. B2B virtual card transaction value is projected to grow from $3.95 trillion in 2025 to $14.6 trillion by 2029 ([Juniper Research](https://www.juniperresearch.com/press/b2b-spending-to-dominate-global-virtual-cards-market/)). The economics are compelling: buyers earn 0.5–1.5% rebates on virtual card payments, converting accounts payable from a cost center to a revenue source, while saving approximately $25 per transaction versus check-based payments ([AFP 2025 Electronic Payments Survey](https://www.afponline.org/publications-data-tools/reports/survey-research-reports/2025-electronic-payments-survey-report)).

The shift is structural, not cyclical. Check usage in B2B payments hit an all-time low of 33% in 2025, down from 42% in 2019 ([AFP](https://www.afponline.org/publications-data-tools/reports/survey-research-reports/2025-electronic-payments-survey-report)), and 25% of organizations plan to eliminate checks entirely by 2026. Mastercard estimates 96% whitespace remains — only $3 trillion of an $80 trillion addressable B2B AP/AR market currently runs on card rails.

However, an adoption gap persists: while 88% of financial leaders consider virtual cards, only 48% have implemented them. Supplier enablement remains the primary bottleneck — 89% of suppliers struggle to balance card acceptance fees with the business benefits of faster settlement ([Mastercard, 2025](https://www.mastercard.com/news/press/2025/march/mastercard-is-modernizing-commercial-payments-with-embedded-virtual-card-technology/)).

**By tier.** Tier 1 banks are launching virtual card programs (BNP Paribas Fortis, HSBC Hong Kong, J.P. Morgan via Conferma). Tier 2 banks are the acute opportunity — they need virtual card capability to serve corporate clients but lack the infrastructure to build it. Tier 3 banks do not currently offer virtual card programs.

### Shift 2: Convergence of card issuance and spend management

The legacy commercial card model separates two functions: the bank issues and processes the card; a separate platform (SAP Concur, Emburse, Coupa) manages corporate spending. SAP Concur, with approximately 49.6% of the T&E management software market and 45,000+ organizational customers ([SAP Concur Blog](https://www.concur.com/blog/article/sap-retains-1-2023-market-share-in-travel-and-expense-management-software)), does not issue cards. It depends entirely on bank-issued card feeds, forfeiting interchange economics and real-time spend controls.

Modern platforms have collapsed this separation. Ramp issues Visa-branded cards (via Sutton Bank), enforces policy at authorization, and automates expense management — reaching $1 billion ARR and $100 billion in annualized purchase volume ([Ramp, September 2025](https://www.prnewswire.com/news-releases/ramp-reaches-1-billion-in-annualized-revenue-302550637.html)). Brex issues corporate cards as program manager and manages expense workflows for 30,000+ companies including Anthropic, Arm, and Robinhood ([Brex, 2025](https://brex.com/journal/press/brex-grows-enterprise-business-80-percent)).

Three acquisitions in twelve months confirm the convergence thesis as structural, not speculative. Capital One is acquiring Brex for $5.15 billion ([Capital One, January 2026](https://www.capitalone.com/about/newsroom/capital-one-to-acquire-brex/)). American Express acquired Center, an expense management platform ([Amex IR, March 2025](https://ir.americanexpress.com/news/investor-relations-news/investor-relations-news-details/2025/American-Express-to-Acquire-Expense-Management-Software-Company-Center/default.aspx)). Paylocity acquired Airbase for $325 million ([TechCrunch, September 2024](https://techcrunch.com/2024/09/04/paylocity-acquiring-corporate-spend-startup-airbase-for-325m)). Fifth Third Bank transitioned its entire $5.6 billion annual corporate card volume to Brex Embedded ([BusinessWire, December 2025](https://www.businesswire.com/news/home/20251209555474/en/Fifth-Third-and-Brex-Partner-to-Bring-AI-Powered-Finance-to-Businesses-Unlocking-$5.6B-in-Commercial-Card-Volume)).

**By tier.** Tier 1 banks are acquiring (Capital One → Brex, Amex → Center). Tier 2 banks are the primary switching market — adopting fintech-embedded solutions (Fifth Third → Brex Embedded) or migrating commercial card platforms (First Horizon from Fiserv to DXC). Tier 3 banks lack scale to justify platform investment.

### Shift 3: Real-time policy enforcement replacing after-the-fact audit

The traditional expense management model is submit-review-audit: the employee spends, submits an expense report, and compliance is assessed after the fact. Violations are discovered days or weeks later, if at all.

Modern platforms enforce policy at the point of transaction. Ramp's AI agents made 26.1 million automated decisions across $10 billion in spend in a single month, blocking 511,000 out-of-policy transactions worth $290.9 million in potential savings ([Ramp, November 2025](https://prnewswire.com/news-releases/ramp-reaches-32-billion-valuation-doubling-revenue-and-customers-in-past-year-302616510.html)). This is authorization-time control, not after-the-fact auditing.

The shift is enabled by architectural convergence: because modern platforms both issue the card and enforce policy, they can intercept the transaction at the authorization moment rather than reviewing it post-settlement. This capability is structurally unavailable to platforms that only receive card feeds after the transaction is complete.

Regulatory requirements amplify this shift. IRS accountable plan rules (Treas. Reg. 1.62-2) require substantiation of each expense with date, amount, merchant, and business purpose — real-time capture eliminates the substantiation gap ([eCFR § 1.62-2](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/subject-group-ECFR064ad1fa7d3cb20/section-1.62-2)). SOX Section 404 requires documented internal controls over purchase card spending, including separation of duties and audit trails ([GAO-04-87G](https://www.gao.gov/assets/gao-04-87g.pdf)).

### Shift 4: Benefits cards as a platform play

Employee benefits card programs — meal cards, fuel cards, health spending accounts, gift cards, lifestyle spending accounts — constitute a distinctive sub-market within commercial cards. Unlike T&E or purchase card programs, benefits cards are driven primarily by **tax regulation** rather than corporate expense management.

**India** is the most developed benefits card market. The Income Tax Act provides specific exemptions: meal cards exempt up to ₹50 per meal under Section 17(2)/Rule 3(7)(iii), fuel cards governed by engine-capacity slabs under Rule 3(2), and gift cards exempt up to ₹5,000 annually under Rule 3(7)(iv) ([Income Tax Act provisions](https://eztax.in/income-tax-act-2025/section-17)). Draft Income-tax Rules 2026 propose quadrupling the meal card exemption from ₹50 to ₹200 per meal, enabling approximately ₹1,05,600 per year in tax-free benefits per employee ([Moneycontrol, 2026](https://www.moneycontrol.com/news/business/personal-finance/draft-income-tax-rules-2026-seek-to-increase-tax-free-meal-benefit-for-employees-to-rs-200-per-meal-13819450.html)). The gift card limit is also proposed to increase from ₹5,000 to ₹15,000 ([Outlook Money](https://www.outlookmoney.com/tax/new-tax-regime-push-spurs-rise-in-wallet-based-employee-benefits)).

Zaggle, the largest listed pure-play in this space, reported quarterly revenue of ₹498 crore (Q3 FY26, +48% YoY) with 45M+ cards issued across 3,500+ corporates ([Zaggle IR](https://ir.zaggle.in/zaggle-overview/)). Pluxee India (formerly Sodexo BRS) serves 11,000+ corporate clients with 3.5M+ consumers across 100,000+ merchant acceptance points ([Pluxee India](https://www.pluxee.in/)).

**In the United States**, the HSA market has reached $159 billion in assets across 40 million accounts, with HSA investments growing 30% year-over-year to $73 billion ([Devenir, Midyear 2025](https://www.devenir.com/hsa-assets-surge-to-159-billion-as-invested-assets-jump-30-year-over-year-to-reach-73-billion/)). HealthEquity dominates with $34.4 billion in HSA assets, 10.1 million accounts, and $1.2 billion in revenue — including $176 million in interchange from benefits card transactions ([HealthEquity FY25](https://www.globenewswire.com/news-release/2025/03/18/3044962/0/en/HealthEquity-Reports-Fiscal-Year-and-Fourth-Quarter-Ended-January-31-2025-Financial-Results.html)). Lifestyle Spending Accounts (LSAs) are the fastest-growing category, with dedicated caregiving and family-formation accounts growing 50%+ year-over-year ([Forma, 2025](https://www.joinforma.com/resources/2025-lifestyle-spending-accounts-lsas-benchmarking-insights)).

**By tier.** In India, mid-tier private banks (Yes Bank, IndusInd, IDFC FIRST, RBL) are launching benefits card programs through fintech partnerships. Large banks (HDFC, Axis) offer proprietary benefits cards but with limited platform depth. In the US, benefits cards are issued primarily through health plan administrators and specialist platforms (HealthEquity, Lively, Forma), not through traditional bank card infrastructure.

### Shift 5: Embedded commercial card programs

Commercial card issuance is moving from being a standalone banking product to an embedded capability within corporate software platforms. Coupa launched virtual cards in November 2025 by partnering with Brex for card provisioning on approved purchase orders ([Coupa Products](https://www.coupa.com/products/ap-automation/virtual-cards/)). Mastercard launched Commercial Connect API, providing single-API access to its issuer ecosystem and virtual card platform to reduce integration time by 18–24 months ([Finextra, October 2025](https://www.finextra.com/pressarticle/107538/mastercard-launches-commercial-connect-api)). Visa launched Commercial Integrated Partners to enable fintechs to embed Visa commercial products ([Visa IR, May 2025](https://investor.visa.com/news/news-details/2025/Visa-Launches-Commercial-Integrated-Partners-to-Turbo-Charge-the-Fintech-Ecosystem/default.aspx)).

Both networks are explicitly lowering the barriers to embedded commercial card issuance. This creates opportunity for platforms that can serve as the issuance-and-processing infrastructure beneath these embedded programs.

### Shift 6: AI-native expense intelligence

The shift from "tool that records expenses" to "system that manages spending" is being driven by AI capabilities. Ramp's AI agents made 26.1 million automated decisions in a single month, including blocking a $49,000 fraudulent invoice and preventing 511,000 out-of-policy transactions ([Ramp, November 2025](https://prnewswire.com/news-releases/ramp-reaches-32-billion-valuation-doubling-revenue-and-customers-in-past-year-302616510.html)). SAP Concur was named Leader across all four 2025 IDC MarketScape reports for AI-enabled T&E ([SAP Concur Blog](https://www.concur.com/blog/article/idc-marketscape-te-software-leader-2025)), indicating that even incumbents are repositioning around AI capabilities.

In India, the GST ITC reconciliation requirement — matching every corporate expense against supplier-filed GSTR-2B data with provisional claims now blocked ([CGST Act Section 16, Rule 36(4)](https://perfectaccounting.in/itc-reconciliation-gst-gstr-2b-vs-purchase-register-practical-guide/)) — creates a compliance automation opportunity that AI-driven card platforms can address through transaction-level tax data capture and automated vendor matching.

### Shift 7: Regulatory forcing functions

Across all three focus markets, regulations are creating non-discretionary investment mandates:

| Market | Mandate | Status / Deadline | Infrastructure Investment Forced |
|--------|---------|-------------------|----------------------------------|
| India | Draft Income-tax Rules 2026: meal card exemption ₹50 → ₹200 | Draft; expected FY2026-27 | Benefits card platform expansion; multi-benefit tax rule engines |
| India | RBI Master Direction on PPIs (updated Dec 2024) | Active | KYC verification, real-time balance enforcement, MCC-restricted acceptance, 10-year log retention |
| India | GST ITC reconciliation (Rule 36(4) — no provisional claims) | Active | Transaction-level GST data capture, automated GSTR-2B matching |
| USA | IRS HSA/FSA card substantiation (IIAS/MCC enforcement) | Active since 2008 | MCC filtering, IIAS auto-substantiation, SIGIS certification |
| USA | GSA SmartPay 3 monthly consolidation reporting | From August 2025 | 16-element data feeds, card count reporting, spend reduction tracking |
| EU | Commercial card interchange exemption (IFR 2015/751) | Active | BIN-level commercial card identification, interchange table differentiation |
| EU | CSRD ESG spend categorization | Phased 2025–2028 | MCC-to-ESG mapping engines, XBRL-tagged reporting, third-party assurance |
| EU | PSD3/PSR Corporate Seal authentication | Expected H2 2027 | Corporate authentication infrastructure, payment factory compliance |

Each mandate creates a buying event. India is the most active — three concurrent mandates (tax rule expansion, PPI framework compliance, GST reconciliation) affecting benefits card programs directly.

---

## 4. The Engagement Landscape

Banks and corporates are commissioning commercial card engagements along five principal patterns:

**Virtual card / AP automation-led.** *Shifts: 1, 5. Primary buyer: Tier 1–2 banks.* Banks launching virtual card programs for corporate clients to capture B2B payment volume currently flowing through checks and ACH. **Named examples:** BNP Paribas Fortis launched in-house corporate virtual cards (May 2025). HSBC launched Hong Kong's first mobile virtual corporate card (June 2025). J.P. Morgan expanded virtual card capabilities across Europe via Conferma (June 2025).

**Expense modernization-led.** *Shifts: 2, 3, 6. Primary buyer: Tier 2 banks and mid-market corporates.* Banks and corporates replacing legacy T&E systems with integrated card-and-spend platforms. **Named examples:** Fifth Third Bank transitioned $5.6B annual commercial card volume to Brex Embedded (December 2025). First Horizon Bank migrated commercial card platform from Fiserv to DXC (October 2025).

**Benefits-led.** *Shifts: 4, 7. Primary buyer: India Tier 2–3 banks; US health plan administrators.* Banks launching or expanding employee benefits card programs. Regulation-driven in India; HSA/FSA-driven in the US. **Named examples:** IDFC FIRST Bank launched digital employee benefits with fintech partner. Yes Bank partnered with Zaggle for co-branded corporate credit card. UMB Bank converted HSA card processing to TSYS Healthcare platform (April 2025).

**Platform-led.** *Shifts: 2, 5, 7. Primary buyer: Tier 2 banks.* Banks building multi-program commercial card platforms supporting benefits, expense, purchase, and virtual cards from common infrastructure. Most relevant for mid-size banks seeking to serve corporate clients across program types without maintaining separate systems.

**Purchase card modernization.** *Shifts: 3, 7. Primary buyer: Tier 1 banks with government contracts.* Banks serving government procurement (GSA SmartPay: $39.7B FY2024 spend, ~13M accounts — [GSA SmartPay](https://smartpay.gsa.gov/about/master-contract/)) or large corporate procurement. Requires Level 2/3 data capture, purchase order matching, and budget enforcement. Concentrated among banks holding government contracts (Citibank, US Bank through 2031).

---

## 5. Competitive Landscape

The commercial card competitive map is **two-sided** — a structural feature that distinguishes it from most other banking technology markets.

### Card issuance and processing

| Vendor | Revenue | Position | Vulnerability |
|--------|---------|----------|---------------|
| FIS (post-TSYS) | $10.7B (guided $13.8B for 2026) | Dominant issuer processor; TS2 serves JPMorgan, U.S. Bank, Santander; 40B+ txns/year | Integration risk; mid-market finds it over-engineered; mainframe-era TS2 architecture |
| Fiserv | $21.2B | Broadest stack: card manufacturing (Output Solutions) → processing (Credit Select) → corporate card mgmt | First Horizon migrated away; Payeezy-to-Clover migration causing attrition |
| Marqeta | $625M; $383B TPV | Powers Ramp and Divvy; API-first, JIT funding, virtual cards | Customer concentration; fintech-oriented; bank-direct wins unproven |
| i2c | Est. $100–200M | Most complete modern commercial card platform; Level 2/3 data, department purses, AI credit decisioning | Low brand awareness; no named commercial card bank clients |
| Zaggle (India) | ₹498Cr quarterly (+48% YoY) | 50M+ prepaid cards; dominant India corporate card issuer | Primarily prepaid, not credit; India-only |
| M2P Fintech (India) | Est. $50–100M | Infrastructure layer for 200+ banks; card issuance APIs | Corporate credit capabilities earlier-stage |

*Sources: [FIS](https://www.fisglobal.com/about-us/media-room/press-release/2026/fis-completes-strategic-acquisition-of-global-payments-issuer-solutions-business), [Marqeta FY2025](https://www.businesswire.com/news/home/20260224239542/en/Marqeta-Reports-Fourth-Quarter-and-Full-Year-2025-Financial-Results), [Zaggle IR](https://ir.zaggle.in/zaggle-overview/), [Finastra-i2c](https://financialit.net/news/e-wallets/finastra-and-i2c-inc-announce-strategic-partnership-offer-debit-card-issuance-and)*

### Expense management and corporate spend

| Vendor | Revenue | Position | Vulnerability |
|--------|---------|----------|---------------|
| SAP Concur | ~$1.4B (est.) | 49.6% of T&E market; 45,000+ organizations; does NOT issue cards | Widely criticized UX; losing mid-market to Ramp/Brex; no interchange revenue |
| Ramp | $1B+ ARR | $32B valuation; 50,000+ customers; issues cards + manages spend | Interchange-dependent; US-concentrated; private (IPO execution risk) |
| Brex | ~$700M | Being acquired by Capital One ($5.15B); 30,000+ companies | Acquisition creates bank-competitor dynamic; enterprise customers on rival banks may defect |
| BILL/Divvy | $1.5B | ~500,000 SMBs; AP + corporate card unified | SMB-focused; slower growth (13% vs. Ramp's 100%+); Divvy integration evolving |
| Navan | $613M TTM | Travel + card + expense unified; IPO'd Oct 2025 at $25/share | Travel-dependent (92% usage revenue); card via partner bank (Celtic) |
| HealthEquity (USA) | $1.2B | 10.1M HSAs, $34.4B AUM, $176M interchange; dominant benefits | Benefits-only; no expense management; interest-rate sensitive |
| Zaggle (India) | ₹498Cr quarterly | Spans issuance AND spend management in India; 50M+ cards | SaaS only 4% of revenue; primarily prepaid-based economics |

*Sources: [SAP Concur](https://www.concur.com/blog/article/sap-retains-1-2023-market-share-in-travel-and-expense-management-software), [Ramp](https://prnewswire.com/news-releases/ramp-reaches-32-billion-valuation-doubling-revenue-and-customers-in-past-year-302616510.html), [Capital One-Brex](https://www.capitalone.com/about/newsroom/capital-one-to-acquire-brex/), [BILL Q4 FY25](https://s202.q4cdn.com/561055838/files/doc_financials/2025/q4/BILL-Q4-25-Press-Release-8-27-25.pdf), [Navan Q3 FY26](https://www.businesswire.com/news/home/20251213266660/en/Navan-Announces-Third-Quarter-Fiscal-Year-2026-Results), [HealthEquity FY25](https://www.globenewswire.com/news-release/2025/03/18/3044962/0/en/HealthEquity-Reports-Fiscal-Year-and-Fourth-Quarter-Ended-January-31-2025-Financial-Results.html)*

### The critical competitive gap

**Legacy expense platforms do not issue cards, and legacy card processors do not manage spending.** An issuance-vs-spend gap analysis of 17 players reveals that only 5 credibly span both sides: Brex, Ramp, BILL/Divvy, Mesh Payments, and Zaggle. SAP Concur, Emburse, Coupa, and the benefits specialists (HealthEquity, Pluxee, Edenred, Forma, Benepass, Lively) all operate on only one side.

Banks are closing this gap through acquisition and partnership rather than internal build — three deals in twelve months confirm this. Mid-size banks that cannot afford acquisitions and find legacy processors inflexible are the underserved segment. A platform that unifies commercial card issuance, policy governance, and spend intelligence — and sells to banks rather than corporates — occupies a position no current competitor holds.

---

## 6. Target Universe

### United States

| Institution | Tier | Horizon | Signal | Source |
|-------------|------|---------|--------|--------|
| Capital One | Large | Near-term (0-2y) | Acquiring Brex for $5.15B; targets $2T in business payments via integrated bank + Discover network + Brex software | [Capital One PR](https://www.capitalone.com/about/newsroom/capital-one-to-acquire-brex/) |
| Fifth Third Bank | Mid-size | Near-term | Transitioned entire $5.6B annual corporate card volume to Brex Embedded platform | [BusinessWire](https://www.businesswire.com/news/home/20251209555474/en/Fifth-Third-and-Brex-Partner-to-Bring-AI-Powered-Finance-to-Businesses-Unlocking-$5.6B-in-Commercial-Card-Volume) |
| First Horizon Bank | Mid-size | Near-term | Publicly migrated commercial card platform from Fiserv to DXC (October 2025) | [First Horizon](https://www.firsthorizon.com/Fiserv-DXC-Commercial-Card-Conversion) |
| UMB Bank | Regional | Near-term | HSA card processor conversion to TSYS Healthcare (April 2025); stacked card/multi-purse HSA offering | [UMB Bank](https://more.umb.com/hcscardconversion/) |
| JPMorgan Chase | Large | Medium-term (2-5y) | Top commercial card issuer; credit card spending growth >7% in Q2 2025; expanding into small-business cards | [WSJ](https://www.wsj.com/finance/banking/jpmorgan-credit-card-spending-growth-064e1d52) |
| U.S. Bank | Large | Medium-term | GSA SmartPay 3 contractor (through 2031); 25+ year TSYS/FIS client; Elan-Fiserv integration underway | [GSA SmartPay](https://smartpay.gsa.gov/about/master-contract/) |
| Bank of America | Large | Medium-term | Active virtual travel card program; commercial card solutions for corporate clients | [Bank of America](https://www.bankofamerica.com/vanity/redirect.go?src=%2Fcardsolutions) |
| Coastal Community Bank | Regional | Medium-term | Banking partner for InComm Benefits' new HSA/FSA platform (launched July 2024) | [PRNewswire](https://www2.prnewswire.com/news-releases/incomm-payments-offers-a-new-way-to-hsa-with-launch-of-incomm-benefits-302197228.html) |

### India

| Institution | Tier | Horizon | Signal | Source |
|-------------|------|---------|--------|--------|
| Yes Bank | Mid-size | Near-term | Multiple Zaggle partnerships: co-branded corporate credit card, prepaid cards, Zakey RuPay key fob | [Indian Startup News](https://indianstartupnews.com/news/yes-bank-announces-partnership-with-zaggle-to-launch-next-gen-corporate-credit-card) |
| IDFC FIRST Bank | Mid-size | Near-term | Launched digital employee benefits solution with fintech partner — end-to-end meal, fuel, health, and LTA card program | [Express Computer](https://expresscomputer.in/news/idfc-bank-partners-with-zeta-to-launch-idfc-bank-benefits-an-employee-benefits-solution-for-corporates/22149) |
| RBL Bank | Mid-size | Near-term | Issues co-branded benefits cards on RuPay; partners with multiple fintechs for prepaid card programs | [Economic Times](https://economictimes.indiatimes.com/industry/banking/finance/banking/zeta-ties-up-with-rupay-for-broader-acceptance-network/articleshow/58128834.cms) |
| AU Small Finance Bank | Regional | Near-term | New Zaggle banking partner (FY26); entering corporate prepaid card segment | [Zaggle IR](https://ir.zaggle.in/zaggle-overview/) |
| Standard Chartered (India) | Large (foreign) | Near-term | New Zaggle banking partner for corporate spend management with prepaid card solutions | [ANI News](https://www.aninews.in/news/business/zaggle-partners-with-standard-chartered-bank-to-redefine-corporate-spend-management-with-its-prepaid-card-solutions20250903172805) |
| IndusInd Bank | Mid-size | Near-term | Banking partner for M2P Fintech digital-first card products; part of Zaggle 16-bank partner ecosystem | [IndusInd-M2P](https://www.indusind.bank.in/in/en/about-us/mediabrand/FY/2022-2023/August/IndusInd-Bank-partners-with-M2P-to-offer-digital-first-and-digital-only-products.html) |
| HDFC Bank | Large | Medium-term | Top credit card issuer (22% market share); offers FoodPlus meal card and MoneyPlus prepaid for corporate benefits | [Economic Times BFSI](https://www.bfsi.economictimes.indiatimes.com/articles/hdfc-bank-tops-credit-card-market-union-banks-share-slips-sbi-leads-in-debit-cards-as-of-jan-26/128779420) |
| Axis Bank | Large | Medium-term | Offers FoodPlus meal card and prepaid card programs for corporates | [Axis Bank](https://axisbank.com/business-banking/cards/prepaid-cards/meal-card/features-benefits/1000) |

### UK / Europe

| Institution | Tier | Horizon | Signal | Source |
|-------------|------|---------|--------|--------|
| BNP Paribas Fortis | Large | Near-term | First Belgian bank to launch in-house corporate virtual cards (May 2025) | [BNP Paribas Fortis](https://www.bnpparibasfortis.com/newsroom/press-release/virtual-card) |
| HSBC | Large | Near-term | Virtual card programs in UK and Hong Kong; first mobile virtual corporate card in Hong Kong (June 2025) | [HSBC HK](https://www.about.hsbc.com.hk/news-and-media/mastercard-and-hsbc-unveil-first-mobile-virtual-corporate-card-in-hong-kong) |
| NatWest | Large | Near-term | Virtual Pay (B2B VCN), onecard Virtual Travel, Lodge Travel programs active | [NatWest](https://www.natwest.com/business/cards/virtual-card-solution.html) |
| Barclays | Large | Medium-term | Precisionpay Go virtual card program via mobile app | [Barclaycard](https://barclaycard.co.uk/business/help/precisionpay-go-app/pp-go-how-to-create-virtual-card) |

---

# PART II — THE ADVISORY

---

## 7. Zeta's Position

| Structural Shift | Zeta Asset | Readiness |
|------------------|-----------|-----------|
| Virtual card explosion (1) | Electron Virtual Cards + Photon authorization | **Partial** — virtual card issuance capability exists; production evidence at scale for commercial-specific virtual card programs not confirmed |
| Issuance-spend convergence (2) | Electron (issuance) + Quark (program governance) | **Partial** — Electron Benefits is production-proven; Electron Expense/Purchase are placeholder. Convergence requires both sides |
| Real-time policy enforcement (3) | Trust Fabric (hierarchy auth) + Truth Fabric (policy definitions) | **Architectural advantage** — declarative policy enforcement is a thesis-level differentiator if implemented |
| Benefits cards as platform (4) | Electron Benefits | **Strong** — production-proven via Pluxee India (11,000+ corporates, 3.5M+ consumers); IDFC FIRST and RBL bank partnerships |
| Embedded card programs (5) | Electron + Cloud Fabric (multi-tenant) | **Medium** — cloud-native architecture supports embedded model; no BaaS-specific packaging for commercial cards |
| AI-native expense intelligence (6) | Cognitive Audit Fabric + Evolution Fabric (Seer) | **Differentiated** — no competitor combines card infrastructure with explicit operational AI governance |
| Regulatory forcing functions (7) | Across Electron + Truth Fabric | **Strong in India** — five separate tax rule engines, RBI PPI compliance, GST ITC reconciliation. **Weak in US/EU** — HSA/FSA IIAS compliance and CSRD mapping not built |

**Honest gaps.** Electron Benefits is production-proven. Electron Expense Cards and Purchase Cards are described in product-line files but marked "to be expanded" — no production deployment exists. Quark Commercial Cards is a placeholder. The gap between "production-proven benefits" and "unvalidated expense/purchase" is the single most important internal question for commercial card strategy.

---

## 8. Where to Play — Right to Play / Right to Win

| Segment | Right to Play | Right to Win | Recommendation |
|---------|--------------|-------------|----------------|
| **India benefits cards (Tier 2–3 banks)** | **Strong.** Market growing 28–30% CAGR. Proposed 4x meal card exemption. Regulation-driven demand. 10+ banks actively launching programs | **Strong.** Production-proven via Pluxee (11,000+ corporates). Bank partnerships (IDFC FIRST, RBL). Five-regulation compliance engine is a moat. Zaggle is primary competitor but runs a different model (direct-to-corporate vs. bank-infrastructure) | **Pursue immediately** |
| **Multi-program commercial card platform (India + US Tier 2 banks)** | **Strong.** $28–30B technology TAM. Mid-size banks underserved — FIS/Fiserv over-engineered, Brex/Ramp are direct-to-corporate. Platform switching actively occurring (Fifth Third, First Horizon) | **Partial.** Electron Benefits proven; Electron Expense/Purchase unvalidated. Tachyon Credit Cards production-validated in US (three programs). Architecture supports multi-program — product evidence does not yet | **Pursue with investment.** Validate Electron Expense Cards through India pilot first |
| **US HSA/FSA benefits cards** | **Medium.** $159B HSA market, 16% growth. Stacked-card innovation aligns with Electron multi-benefit architecture | **Weak.** Top 5 control 75% of assets. HealthEquity has $34.4B AUM and $1.2B revenue. IIAS/SIGIS compliance not built. No US distribution partner | **Selective.** Medium-term; contingent on finding distribution partner |
| **US enterprise T&E expense management** | **Strong.** Large market; SAP Concur losing mid-market | **Very weak.** SAP Concur has 49.6% share and 45,000+ customers. Ramp has $1B ARR and $32B valuation. No brand, references, or sales infrastructure | **Defer.** Revisit only if Electron Expense reaches production maturity and a bank distribution partner provides channel access |
| **Fleet cards** | **Weak.** Vertically integrated; ~4% of US commercial card spend | **Very weak.** WEX ($2.66B) and Corpay ($4.5B) dominate with proprietary networks, RFID infrastructure, telematics | **Do not pursue.** Partnership/white-label only if opportunity emerges |

---

## 9. Risks and Gaps

### What must be true for this opportunity to work

1. **Electron Expense Cards must reach production quality.** The "multi-program commercial card platform" positioning — which is the most compelling play for mid-size banks — requires expense and purchase card capabilities alongside benefits. Without this, Zeta is a benefits-only platform with limited TAM.
2. **India's meal card tax exemption increase must be enacted (or similar regulatory expansion).** The proposed 4x increase (₹50 → ₹200/meal) is the most powerful near-term demand catalyst. If it stalls, growth depends on existing limits.
3. **Banks must prefer bank-infrastructure platforms over direct-to-corporate platforms.** If mid-size banks adopt Brex Embedded (direct-to-corporate), Ramp, or SAP Concur rather than bank-infrastructure solutions, the platform-led engagement model does not gain traction.
4. **Quark Commercial Cards must be built.** The operational domain model — pre-modeled streams, loops, scenarios for commercial card programs — is the thesis-differentiated asset. Without it, Zeta competes on infrastructure alone, where Marqeta and i2c are already positioned.

### Competitive threats

**Capital One–Brex integration.** Creates a vertically integrated competitor with bank balance sheet, Discover network, and Brex software. If this integration succeeds, it sets a new standard that standalone platforms cannot match in the US. Amex–Center signals a similar move. The window for independent platform partnerships may narrow.

**Zaggle scaling in India.** Growing at 48% YoY with 50M+ cards. Expanding into credit cards, forex, and Mastercard partnerships. Already partners with banks (Yes Bank, Standard Chartered, IndusInd). If Zaggle reaches production-quality corporate credit card capabilities, it challenges Zeta's bank-partnership model from the direct-to-corporate side.

**Regulatory execution risk.** India's benefits card compliance requires five or more separate tax rule engines in a single card program (meal, fuel, gift, health, LTA). The complexity is the opportunity; it is also the execution risk.

---

## 10. Recommended Actions

### Near-term (0-2 years)

| Action | Rationale | Priority |
|--------|-----------|----------|
| **Expand India benefits card partnerships** | Target 3–5 additional mid-tier banks (IndusInd, AU Small Finance Bank, Suryoday, Axis or Kotak). Pluxee proof point + proposed meal card exemption = commercial argument | **Immediate** |
| **Validate Electron Expense Cards** | Identify one Indian bank willing to pilot combined benefits + expense card program. This is the critical capability validation for multi-program positioning | **Immediate** |
| **Build GST ITC reconciliation** | Unique Indian compliance challenge (GSTR-2B matching) with no global parallel. AI-driven reconciliation integrated into card platform = defensible differentiator against Zaggle and SAP Concur | **Q3 2026** |
| **Develop Quark Commercial Cards** | Operational domain model — pre-modeled streams, loops, scenarios for benefits card operations first, then expense and purchase card. Thesis-differentiated asset | **2026–2027** |

### Medium-term (2-5 years)

| Action | Rationale | Priority |
|--------|-----------|----------|
| **Evaluate US mid-size bank entry** | If Electron Expense/Purchase reach production maturity. First Horizon and Fifth Third signal segment is in motion. Entry should be platform-led (multi-program), not program-type-led | **2028** |
| **Explore US HSA/FSA benefits cards** | If distribution partner identified. Build IIAS/MCC compliance + SIGIS certification. Stacked-card innovation maps to Electron's multi-benefit architecture | **2028–2029** |
| **Monitor Capital One–Brex integration** | If integration falters or competing banks seek alternatives to avoid Capital One–owned platform, the window for independent bank-focused platform widens | **Ongoing** |

### What to defer or avoid

| Decision | Rationale |
|----------|-----------|
| **Do not pursue US enterprise T&E** | SAP Concur (49.6% share) and Ramp ($1B ARR, $32B valuation) are entrenched. Capital and brand requirements prohibitive |
| **Do not pursue fleet cards** | WEX and Corpay dominate through proprietary networks. ~4% of commercial card spend. Specialized requirements (RFID, telematics, EV charging) are poor fit |
| **Do not pursue Tier 1 US banks** as primary segment | Relationship-intensive, 18–36 month sales cycles, deep customization. Zeta lacks brand and references in US commercial cards |

---

## Key Differences: Commercial Cards vs. Payments

| Dimension | Payments | Commercial Cards |
|-----------|----------|------------------|
| **Market structure** | Single domain (payment infrastructure) | Two-sided: card issuance + spend management |
| **Competitive landscape** | Mostly payment processors | Split: card processors AND expense management vendors — the gap between them is the opportunity |
| **Regulatory drivers** | Rail mandates (FedNow, PSD3, UPI) | Tax/benefits compliance (GST, HSA/FSA), corporate governance (SOX), procurement rules |
| **India angle** | UPI dominance, real-time payments scale | Benefits cards (meal, fuel, health) — regulation-driven, tax-advantaged, high-retention |
| **UK/Europe angle** | PSD3, instant payments regulation | Commercial card interchange exemption economics, VAT reclaim automation, CSRD spend tracking |
| **Zeta product center** | Photon (payments hub) | Electron (commercial cards) + Tachyon (accounts) |
| **Central strategic argument** | Composable payments platform vs. rail-specific integrations | Unified program platform vs. bifurcated issuance + spend management |
| **Key competitive threat** | Legacy processors (FIS, Fiserv) defending installed base | Brex/Ramp consolidating both sides; SAP Concur modernizing from spend side |
| **Vendor-addressable TAM** | $60–85B (narrow); $150–200B (broad) | $28–30B (narrow); $75–90B (broad) |

---

## Research Sources and Citation Index

This analysis draws on data from 60+ sources across six research streams. All cited URLs were verified as of March 2026. Detailed research files with full data tables are retained in `_research/commercial-cards/`.

**Primary institutional sources:** [IRS](https://www.irs.gov/); [RBI](https://rbi.org.in/); [SEBI](https://www.sebi.gov.in/); [GSA SmartPay](https://smartpay.gsa.gov/); [European Commission](https://finance.ec.europa.eu/); [ECB](https://www.ecb.europa.eu/); [FCA/PSR](https://www.psr.org.uk/)

**Industry reports (may be paywalled):** Nilson Report 2025–2026; Datos Insights Global Commercial Cards 2025; Juniper Research; Mercator Advisory Group; IDC MarketScape for AI-enabled T&E 2025; Devenir HSA Research

**Market research:** [Grand View Research](https://grandviewresearch.com/); [Allied Market Research](https://www.alliedmarketresearch.com/); [IMARC Group](https://www.imarcgroup.com/); [Business Research Insights](https://www.businessresearchinsights.com/)

**Vendor financials:** [FIS](https://www.fisglobal.com/); [Fiserv](https://investors.fiserv.com/); [Marqeta](https://www.businesswire.com/news/home/20260224239542/en/Marqeta-Reports-Fourth-Quarter-and-Full-Year-2025-Financial-Results); [BILL Holdings](https://s202.q4cdn.com/561055838/files/doc_financials/2025/q4/BILL-Q4-25-Press-Release-8-27-25.pdf); [HealthEquity](https://www.globenewswire.com/news-release/2025/03/18/3044962/0/en/HealthEquity-Reports-Fiscal-Year-and-Fourth-Quarter-Ended-January-31-2025-Financial-Results.html); [Zaggle IR](https://ir.zaggle.in/zaggle-overview/); [Navan S-1](https://www.cnbc.com/2025/09/19/navan-files-for-ipo-public-offering.html)

**Industry media:** [PYMNTS](https://www.pymnts.com/); [Finextra](https://www.finextra.com/); [Payments Dive](https://www.paymentsdive.com/); [Inc42](https://inc42.com/)

**Cross-references:** [_research/payments/](../../_research/payments/) — FIS, Fiserv, Marqeta, i2c, Galileo competitive profiles overlap; [market-study/tokenization-card-issuance-digital-instruments.md](../../../../market-study/tokenization-card-issuance-digital-instruments.md) — virtual card issuance and tokenization data overlap
