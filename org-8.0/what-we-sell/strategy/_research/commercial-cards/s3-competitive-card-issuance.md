# Stream 3: Competitive Landscape — Card Issuance and Processing

**Research date:** March 2026
**Engagement area:** Commercial Cards

---

## Cross-References from Existing Research

### Extracted from `payments-technology-competitive-landscape.md`

- **FIS**: Revenue $10.7B (FY2025); acquired TSYS for $13.5B (Jan 2026); 40B+ txns/year across 75+ countries for 150+ FIs; $500M incremental FCF Year 1, $700M by 2028; vulnerability to modern card issuers (Marqeta, i2c)
- **Fiserv**: Revenue $21.2B (FY2025); scale across both issuing and acquiring; First Data integration; Clover SMB platform; Payeezy-to-Clover migration issues
- **Global Payments / TSYS**: Divested TSYS Issuer Solutions to FIS for $13.5B; now pure-play merchant ($9.3B adjusted net revenue); no longer in issuing business
- **ACI Worldwide**: Revenue $1.76B (+10%); ACI Connetic cloud-native payments hub; limited issuer processing capabilities (pre-2026); SaaS revenue +15% Q4 2025
- **Marqeta**: Revenue $625M (+23%); TPV $383B (+31%); API-first card issuing with JIT funding; Block/Cash App historically >50% revenue; expanding to banks
- **i2c**: Revenue est. $100–200M; unified platform; 99.999% uptime; 300+ APIs; Finastra partnership (Mar 2025) for NA bank debit issuance; Mastercard One Credential integration
- **Galileo/SoFi**: Revenue est. $430–460M; 157.9M enabled accounts; U.S. Treasury Direct Express win; SoFi parent creates channel conflict with banks
- **Thredd**: 100+ fintech clients; 47 countries; cloud-native issuer processing; credit capabilities launched 2026; BNPL volumes +48%; U.S. market launch

### Extracted from `tokenization-card-issuance-digital-instruments.md`

- **Virtual card market**: $5.2–5.4T (2025) → $17.4T by 2029; B2B share 76% (→ 83% by 2029); small business virtual card txn growth +48% YoY
- **Legacy platform replacement wave**: >80% of European banks engaged in core system modernization; banks migrating away from FIS VisionPLUS, TSYS TS2; modern replacements include Marqeta, Fiserv Optis, i2c, BPC SmartVista
- **Card launch time gap**: UK banks average 18 months / £1M on legacy vs. 4–6 weeks for fintechs
- **Digital wallet impact**: 74% of consumers prioritize instant card issuance; cards projected to decline from 69% to 47% of transactions by 2029
- **Virtual card platform requirements**: Real-time API issuance, granular per-card controls, multi-form-factor support, PCI DSS Level 1, webhook-driven eventing

---

## Legacy Incumbents

### FIS (post-TSYS acquisition)

| Dimension | Detail | Source | URL |
|-----------|--------|--------|-----|
| Revenue | $10.7B total (FY2025); Banking Solutions $7.3B. Guided $13.8B for 2026 (+30%) after absorbing TSYS | FIS 10-K (Feb 2026) | [FIS Press Release](https://www.fisglobal.com/about-us/media-room/press-release/2026/fis-completes-strategic-acquisition-of-global-payments-issuer-solutions-business) |
| Target segment | Tier 1–2 banks globally; 150+ FI and corporate clients | FIS Press Release (Jan 2026) | [FIS Press Release](https://www.fisglobal.com/about-us/media-room/press-release/2026/fis-completes-strategic-acquisition-of-global-payments-issuer-solutions-business) |
| Revenue model | Long-term processing contracts with FIs; per-transaction + platform licensing; $500M incremental FCF in 2026, $700M by 2028 from TSYS | FIS 10-K, Press Release | [FIS Press Release](https://www.fisglobal.com/about-us/media-room/press-release/2026/fis-completes-strategic-acquisition-of-global-payments-issuer-solutions-business) |
| Commercial card capabilities | **FIS Total Issuing Solutions** (rebranded TSYS TS2): corporate cards, purchase cards, One Card, virtual cards, executive and fleet cards; 24/7 program admin support; fraud management; expense management integration; mobile app access; processes commercial card portfolios across 75+ countries in 17+ European languages/currencies | TSYS.com, FIS Press Releases | [TSYS FI Platform](https://www.tsys.com/financial-institutions) |
| AI/innovation | Industry-first agentic commerce platform (Jan 2026): AI agents can initiate and complete card transactions with "Know Your Agent" (KYA) data; developed with Visa and Mastercard; fraud protection, fewer false declines | FIS Press Release (Jan 2026) | [FIS Agentic Commerce](https://www.fisglobal.com/about-us/media-room/press-release/2026/fis-launches-industry-first-ai-transaction-platform-to-help-banks-lead) |
| Strengths | World's largest issuing business; 40B+ txns/year; massive bank relationships; TS2 is proven at Tier 1 scale (JPMorgan Chase, U.S. Bank historically); acquisition creates end-to-end banking + issuing stack | FIS 10-K, TSYS history | [Forbes](https://www.forbes.com/sites/nicolecasperson/2026/01/15/fis-closes-135-billion-fintech-deal-launches-agentic-commerce/) |
| Weaknesses | Integration risk absorbing $13.5B acquisition; TS2 is mainframe-era architecture despite cloud branding; slow innovation velocity vs. modern challengers; lost direct merchant capabilities (sold Worldpay) | Analyst commentary, existing research | [The Fintech Times](https://thefintechtimes.com/fis-seals-13-5bn-tsys-deal-and-launches-ai-agentic-commerce-for-banks) |
| Vulnerability | Cloud-native issuers (Marqeta, i2c) attacking next-gen card programs; mid-market banks may find FIS over-engineered and expensive; legacy architecture limits time-to-market for new card products | Existing research analysis | [Payments Technology Competitive Landscape — internal] |

---

### Fiserv / First Data

| Dimension | Detail | Source | URL |
|-----------|--------|--------|-----|
| Revenue | $21.2B total GAAP (FY2025, +4%); Merchant Solutions 6% organic growth; adjusted operating margin 37.4%; $4.6B FCF (22% margin) | Fiserv 10-K (2025) | [Fiserv Corporate Cards](https://www.fiserv.com/en-emea/who-we-serve/financial-institutions/issuing-solutions/corporate-cards.html) |
| Target segment | Tier 1–3 banks, credit unions, merchants; broad mid-market bank presence for core + payments + card services | Fiserv investor materials | [Fiserv Processing](https://merchants.fiserv.com/en-us/products/financial-institutions/payment-processing/) |
| Revenue model | Long-term processing contracts; Output Solutions manufacturing fees; per-account and per-transaction fees; bundled core + payments pricing | Fiserv product pages | [Fiserv Output Solutions](https://www.fiserv.com/en/solutions/output-solutions) |
| Commercial card capabilities | **Full commercial card stack**: purchasing cards (PCard), T&E cards, virtual cards, fleet cards; Travel Expense Management (TEM) integrated with TMCs; Invoice-to-Pay AP automation; card & expense management on single platform; spending controls (limits, authorization rules, MCC restrictions); **Credit Select** full-service credit platform; **Output Solutions** for card manufacturing (EMV, contactless, eco-friendly), central issuance, instant issue | Fiserv.com product pages | [Fiserv Commercial Processing](https://merchants.fiserv.com/en-us/products/financial-institutions/commercial-solutions/) |
| Strengths | End-to-end issuing + acquiring + manufacturing stack; best-in-class margins; integrated corporate card + expense + billing management; Output Solutions provides physical card production at scale; Credit Select gives flexibility for issuers of all sizes | Fiserv investor materials | [Fiserv Credit Select](https://www.fiserv.com/en/solutions/card-services/credit-select.html) |
| Weaknesses | Payeezy-to-Clover migration causing merchant attrition and lawsuits; legacy First Data integration complexity; innovation pace behind cloud-native competitors; monolithic architecture in card processing | Existing research, analyst commentary | [Payments Technology Competitive Landscape — internal] |
| Vulnerability | Cloud-native card issuers eroding next-gen programs; regional banks may find bundled approach inflexible; First Horizon Bank publicly migrated commercial card FROM Fiserv to DXC (Oct 2025) — signals competitive displacement | First Horizon Bank conversion page | [First Horizon Fiserv-to-DXC Migration](https://www.firsthorizon.com/Fiserv-DXC-Commercial-Card-Conversion) |

---

### Global Payments / TSYS (pre-acquisition commercial card position)

| Dimension | Detail | Source | URL |
|-----------|--------|--------|-----|
| Revenue (pre-divestiture) | TSYS Issuer Solutions divested to FIS for $13.5B enterprise value (Jan 2026); Global Payments now $9.3B adjusted net revenue as pure-play merchant | Global Payments 10-K (Feb 2026) | [Payments Technology Competitive Landscape — internal] |
| Historical commercial card position | TSYS TS2 was the dominant U.S. commercial card processing platform: corporate cards, purchase cards, One Card, virtual cards; processing in 17 European countries; served JPMorgan Chase (~87M cardmembers), U.S. Bank (25+ year relationship), Santander (migrated to TS2 in 2022) | TSYS press releases, BusinessWire | [TSYS-US Bank Extension](https://www.securetechalliance.org/tsys-extends-relationship-with-u-s-bank/) |
| Post-divestiture status | **No longer in card issuing**. Global Payments is now a pure-play merchant solutions company after divesting TSYS to FIS and acquiring Worldpay. Commercial card issuing and processing capabilities transferred entirely to FIS | Global Payments 10-K | [Payments Technology Competitive Landscape — internal] |
| Relevance to landscape | TSYS TS2 continues as the dominant legacy commercial card platform — now under FIS Total Issuing Solutions branding. Banks on TS2 now have FIS as their processing partner | FIS press releases | [FIS Acquisition Completion](https://www.fisglobal.com/about-us/media-room/press-release/2026/fis-completes-strategic-acquisition-of-global-payments-issuer-solutions-business) |

---

### ACI Worldwide

| Dimension | Detail | Source | URL |
|-----------|--------|--------|-----|
| Revenue | $1.76B total (FY2025, +10%); recurring revenue $1.21B (+11%); guided $1.88–1.91B for 2026 (+7–9%) | ACI Worldwide earnings (Feb 2026) | [ACI Earnings](https://investor.aciworldwide.com/news-releases/news-release-details/payments-leaders-unprepared-2026-disruption-warns-aci-worldwide) |
| Target segment | Tier 1–2 banks, billers, intermediaries; expanding to commercial card processors with Connetic for Cards | ACI Worldwide press releases | [ACI Connetic for Cards](https://www.helpnetsecurity.com/2026/03/04/aci-worldwide-aci-connetic-for-cards/) |
| Revenue model | SaaS subscriptions (growing 15% in Q4 2025), term licenses, recurring maintenance; 50–60% of operating cash flow committed to shareholder returns | ACI earnings release | [ACI Earnings](https://investor.aciworldwide.com/news-releases/news-release-details/payments-leaders-unprepared-2026-disruption-warns-aci-worldwide) |
| Commercial card capabilities | **ACI Connetic for Cards** (launched March 2026): cloud-native card payments suite unifying issuing, acquiring, and ATM capabilities; processes full transaction lifecycle (capture, authentication, routing, authorization, clearing, settlement); integrates with A2A payments and AI-driven fraud prevention on single platform; processes 300B+ card transactions annually globally | ACI Press Release (Mar 2026) | [ACI Connetic for Cards Launch](https://finance.yahoo.com/news/aci-worldwide-launches-card-payments-070000902.html) |
| Fraud capabilities | Real-time ML + rules-based fraud screening; support for third-party and customer-built models; global fraud intelligence network; APP fraud protection; deployed via cloud including Azure Marketplace | ACI Worldwide product pages | [ACI Real-Time Payments Fraud](https://www.aciworldwide.com/solutions/real-time-payments-fraud-prevention) |
| Strengths | Deep payments domain expertise; genuine cloud-native architecture (Connetic); unified card + A2A + fraud on single platform; massive processing scale (300B+ card txns); first UK bank win for Connetic validates platform | ACI press releases | [ACI UK Bank Win](https://investor.aciworldwide.com/news-releases/news-release-details/aci-connetic-accelerates-global-adoption-uk-banks-can-now-unite) |
| Weaknesses | Card processing is brand-new capability (March 2026 launch) — unproven at scale in production; historically limited issuer processing; Connetic for Cards still early in pipeline conversion; smaller scale vs. FIS/Fiserv | Analyst commentary | [Simply Wall St Analysis](https://simplywall.st/stocks/us/software/nasdaq-aciw/aci-worldwide/news/aci-worldwides-first-uk-connetic-bank-win-tests-cloud-paymen) |
| Vulnerability | FIS/TSYS deeply entrenched in bank card processing; Marqeta and i2c dominate modern card issuing; Connetic for Cards must prove production reliability before winning card-processing mandates at scale | Market analysis | [ACI Connetic for Cards](https://www.helpnetsecurity.com/2026/03/04/aci-worldwide-aci-connetic-for-cards/) |

---

## Modern Card Issuers / Processors

### Marqeta

| Dimension | Detail | Source | URL |
|-----------|--------|--------|-----|
| Revenue | $625M net revenue (FY2025, +23%); gross profit $437M (+24%); TPV $383B (+31%); guided $700–715M for 2026 (+12–14%) | Marqeta Q4 2025 earnings (Feb 2026) | [Marqeta Earnings](https://www.businesswire.com/news/home/20260224239542/en/Marqeta-Reports-Fourth-Quarter-and-Full-Year-2025-Financial-Results) |
| Target segment | Fintechs and expense management platforms (Ramp, Divvy); neobanks; BNPL providers; gig-economy platforms; expanding to traditional banks via portfolio migration services | Marqeta product pages, earnings | [Marqeta Expense Management](https://marqeta.com/payment-solutions/expense-management) |
| Revenue model | Per-transaction interchange sharing + platform fees; economics driven by TPV scale; margin pressure from large-customer deals | Marqeta 10-K | [Marqeta Earnings](https://www.businesswire.com/news/home/20260224239542/en/Marqeta-Reports-Fourth-Quarter-and-Full-Year-2025-Financial-Results) |
| Commercial card capabilities | **Virtual card issuance** via API for corporate expense programs; **JIT Funding** for real-time cash flow optimization; dynamic spend controls (MCC, velocity, amount, time, geo); single-use virtual cards for AP automation; real-time transaction data and visibility; AI/ML Real-Time Decisioning (first customer live 2025); **Portfolio Migration Service** for banks switching from legacy processors; **UX Toolkit** with pre-built card management interfaces (network-approved) | Marqeta product pages | [Marqeta Virtual Cards](https://marqeta.com/platform/virtual-cards) |
| Key commercial clients | Block (Cash App), Uber, DoorDash, Klarna; **Expense management**: Ramp, Divvy (Bill.com); Bold.org and Finfare as early UX Toolkit adopters | Marqeta earnings, product pages | [Marqeta Controlling Business Spend](https://marqeta.com/embedded-finance/controlling-business-spend) |
| Strengths | Proven at massive scale ($383B TPV); best-in-class APIs for card issuance; JIT Funding differentiator; powers leading expense management platforms (Ramp: $1B ARR, $22.5B valuation); portfolio migration tools signal serious bank-market intent; multinational expansion (UK, Europe via TransactPay acquisition) | Marqeta earnings, Ramp revenue data | [Marqeta Portfolio Migration](https://marqeta.com/blog/simplifying-the-process-of-card-portfolio-migration) |
| Weaknesses | Revenue concentration — Block historically >50% (diversifying); not a full payments hub — card-centric only; margin pressure from large-customer economics; limited direct commercial card product (relies on fintech partners like Ramp to build the user-facing experience) | Marqeta 10-K, existing research | [Payments Technology Competitive Landscape — internal] |
| Vulnerability | i2c competing with broader platform (commercial credit, banking); FIS/TSYS adding modern APIs to defend franchise; Galileo bundling card issuing with banking infra; Lithic offering lower-cost alternative for developer-focused programs | Market analysis | [Payments Technology Competitive Landscape — internal] |

---

### i2c Inc.

| Dimension | Detail | Source | URL |
|-----------|--------|--------|-----|
| Revenue | Private — estimated $100–200M based on scale indicators | Industry estimates | [Payments Technology Competitive Landscape — internal] |
| Target segment | Banks, credit unions, fintechs, program managers; expanding to enterprise commercial card programs; **Finastra partnership** brings NA bank distribution | i2c press releases | [Finastra-i2c Partnership](https://financialit.net/news/e-wallets/finastra-and-i2c-inc-announce-strategic-partnership-offer-debit-card-issuance-and) |
| Revenue model | Per-transaction processing fees + platform licensing; private company economics not disclosed | Industry estimates | [i2c Commercial Credit](https://www.i2cinc.com/solutions/commercial-credit/) |
| Commercial card capabilities | **Dedicated commercial credit solution**: department-level purses and configurable account hierarchies; Level 2 & 3 data capture for enhanced commercial reporting; flexible spend controls per department/card; automated payables and reconciliation; corporate portal for program management; AI-powered decisioning for credit line setting and approvals; supports consumer credit, commercial credit, secured cards, co-brand, private-label, BNPL, debit, and prepaid on single platform; product launches in days; Mastercard One Credential integration (Feb 2025) | i2c product pages | [i2c Commercial Credit](https://www.i2cinc.com/solutions/commercial-credit/) |
| Strengths | Unified platform covering all card types on single codebase; 99.999% uptime; 100K+ pre-coded building blocks; 300+ APIs; 216+ countries; Level 2/3 data native for commercial programs; Finastra distribution partnership opens NA bank channel; program management advisory services | i2c product pages | [i2c Issuer Processing](https://www.i2cinc.com/what-we-do/issuer-processing/) |
| Weaknesses | Limited brand awareness vs. Marqeta; private company — less transparency, potentially limited capital for rapid expansion; smaller engineering and GTM footprint | Market analysis | [Payments Technology Competitive Landscape — internal] |
| Vulnerability | Marqeta has stronger brand; FIS/TSYS have deeper bank relationships; could be acquisition target; Finastra partnership is nascent and unproven at scale | Market analysis | [Payments Technology Competitive Landscape — internal] |

---

### Galileo / SoFi Technologies

| Dimension | Detail | Source | URL |
|-----------|--------|--------|-----|
| Revenue | ~$430–460M estimated (FY2025); Q3 2025 $114.6M (+12% YoY); Technology Platform segment: $395.2M (FY2024, +12%); 168M enabled accounts (Q4 2024) | SoFi quarterly earnings | [Galileo Partnerships](https://www.galileo-ft.com/news/galileo-partnerships-help-drive-sofi-record-growth/) |
| Target segment | Fintechs (historically); expanding to banks (major U.S. FI debit portfolio transitioning early 2026) and government programs (U.S. Treasury Direct Express) | SoFi/Galileo press releases | [Galileo Partnerships](https://www.galileo-ft.com/news/galileo-partnerships-help-drive-sofi-record-growth/) |
| Revenue model | Per-account and per-transaction processing fees; higher average deal sizes driving revenue mix improvement | SoFi earnings | [Galileo Partnerships](https://www.galileo-ft.com/news/galileo-partnerships-help-drive-sofi-record-growth/) |
| Commercial card capabilities | **Cyberbank Core** for commercial payment services: debit, prepaid, ACH, and wire transactions for commercial clients; cloud-based real-time transaction processing; ML-based fraud detection (35% average fraud reduction for clients); co-branded debit programs (Wyndham, Southwest Airlines); government-grade compliance (Treasury Direct Express for 3.4M beneficiaries) | SoFi/Galileo press releases | [SoFi Commercial Payments](https://www.sofi.com/press/sofi-technologies-adopt-galileos-cyberbank-core-new-commercial-payment-services-sponsor-banking-program/) |
| Strengths | Full-stack payments + banking infrastructure; massive account base (168M+); government program wins validate reliability; major U.S. FI transitioning to Galileo in early 2026 (top-10 client); expanding into co-branded card programs | SoFi/Galileo press releases | [Galileo Partnerships](https://www.galileo-ft.com/news/galileo-partnerships-help-drive-sofi-record-growth/) |
| Weaknesses | SoFi parent is a competing bank — creates channel conflict with bank prospects; limited dedicated commercial card product (focus remains debit/prepaid); transaction volume dipped (157.9M in Q3 vs. 168M Q4 2024); dependence on fintech clients whose growth may be slowing | SoFi earnings, market analysis | [Payments Technology Competitive Landscape — internal] |
| Vulnerability | Banks may resist platform owned by competing bank/fintech; i2c and Marqeta compete without this conflict; FIS/TSYS offer incumbency advantages; commercial card capabilities less mature than Marqeta or i2c | Market analysis | [Payments Technology Competitive Landscape — internal] |

---

### Thredd

| Dimension | Detail | Source | URL |
|-----------|--------|--------|-----|
| Revenue | Private — not disclosed; estimated mid-market scale based on 100+ fintech clients, 47 countries, billions of transactions annually | Thredd press releases | [Thredd Homepage](https://www.thredd.com/) |
| Target segment | Fintechs, digital banks, embedded finance providers, corporate card platforms; expanding to U.S. market | Thredd product pages | [Thredd Homepage](https://www.thredd.com/) |
| Revenue model | Per-transaction processing fees; platform services fees; compliance and in-market support services | Thredd product pages | [Thredd Products UK/Europe](https://docs.thredd.com/More_Information/Regions-Europe.htm) |
| Commercial card capabilities | Cloud-native issuer processing for corporate card programs: physical and virtual cards (single/multi-use); real-time spend controls and card freezing; multi-currency capabilities; automated expense management; fraud transaction monitoring; BIN management and tokenization (Apple Pay, Google Pay); end-to-end credit capabilities (launched 2026); **OFX corporate card expansion** across Australia, Canada, Europe, U.S., and APAC (Sep 2025); **PhotonPay** card processing partnership (Oct 2025) | Thredd press releases | [Thredd-OFX Partnership](https://www.businesswire.com/news/home/20250925917356/en/Thredd-Powers-OFX-Corporate-Card-Expansion-Across-Key-Global-Markets) |
| Key clients | OFX (corporate cards), PhotonPay (card infrastructure), Zilch, Curve, Pockit, Treezor | Thredd press releases, existing research | [Thredd-PhotonPay](https://www.thredd.com/about-us/newsroom/company-news/photonpay-partners-with-thredd-to-enhance-card-infrastructure) |
| Strengths | Strong European commercial card processing pedigree; proven multi-geography corporate card programs (OFX across 5+ regions); AI-first positioning; BNPL volumes +48% across UK/Europe/APAC; single-partner model for multi-region expansion; 99.99% availability | Thredd press releases | [Thredd-OFX Partnership](https://www.businesswire.com/news/home/20250925917356/en/Thredd-Powers-OFX-Corporate-Card-Expansion-Across-Key-Global-Markets) |
| Weaknesses | Smaller scale than Marqeta or i2c; U.S. presence just launching; revenue not at critical mass for Tier 1 bank deals; limited credit processing history (just launched 2026) | Market analysis | [Payments Technology Competitive Landscape — internal] |
| Vulnerability | Marqeta's multinational expansion encroaching on European turf; Adyen adding issuing capabilities; legacy processors' digital subsidiaries; late U.S. entry into crowded market | Market analysis | [Payments Technology Competitive Landscape — internal] |

---

### Lithic

| Dimension | Detail | Source | URL |
|-----------|--------|--------|-----|
| Revenue | Private — not disclosed; $1B+ monthly TPV reached Nov 2024; $121M total funding raised; $800M valuation (Jul 2021 Series C) | Lithic blog, Tracxn, Financial Post | [Lithic $1B TPV](https://www.lithic.com/blog/1-billion-monthly-tpv) |
| Target segment | Fintech developers building commercial card programs; expense management platforms; vertical SaaS companies needing embedded card issuance | Lithic product pages | [Lithic Homepage](https://www.lithic.com/) |
| Revenue model | Per-transaction processing fees; platform access fees; BIN sponsorship fees | Lithic documentation | [Lithic Card Issuing](https://www.lithic.com/card-issuing) |
| Commercial card capabilities | **Commercial Charge Card** (launched Oct 2023): full-stack credit solution with programmable limits, statement generation API, automated ACH repayment; **Commercial Revolving Credit** (launched Dec 2024): carry-balance programs, configurable APRs, custom billing cycles; virtual, digital, and physical card issuance in a single API call; granular Auth Rules (MCC, amount, velocity, time-of-day); enhanced commercial data capabilities; settlement APIs with virtual and routable accounts; mobile/web provisioning with digital wallet support | Lithic product pages, blog | [Lithic Charge Card](https://docs.lithic.com/docs/commercial-charge-card-overview) |
| Strengths | Developer-first API experience (TypeScript, Python SDKs); 100+ high-growth clients; 99.99%+ uptime; SOC 1/2, PCI DSS, ISO 27001 compliant; direct Visa and Mastercard connections; low-friction onboarding for fintech developers; both charge and revolving credit for commercial programs; formerly Privacy.com — proven virtual card heritage | Lithic product pages | [Lithic Card Issuing API](https://www.lithic.com/card-issuing-api) |
| Weaknesses | Smaller scale than Marqeta; $800M valuation dates to 2021 — no recent public funding round; limited brand awareness outside developer community; not a full banking/payments platform; no direct bank relationships | Tracxn, market analysis | [Lithic Funding](https://tracxn.com/d/companies/lithic/__28Ezra3aDJaO2QPtnWdzSQalhBSITkIwCow927YZrHI/funding-and-investors) |
| Vulnerability | Marqeta dominates the fintech card-issuing market at larger scale; i2c offers broader platform; niche developer-focused positioning may limit TAM; could be acquisition target | Market analysis | [Lithic Revolving Credit Blog](https://lithic.com/blog/revolving-credit) |

---

## India-Specific Players

### M2P Fintech

| Dimension | Detail | Source | URL |
|-----------|--------|--------|-----|
| Revenue | Private — not disclosed; valued at ~$790M (Sep 2024 Series D); total funding ~$184–215M | Entrackr, Inc42, Tracxn | [M2P Funding (Inc42)](https://inc42.com/company/m2p-fintech/funding/) |
| Target segment | Banks and fintechs in India, MENA, APAC, Oceania; 200+ banks and 300+ lenders served across 30+ markets | M2P press releases | [M2P Fintech Homepage](https://m2pfintech.com/) |
| Revenue model | API infrastructure licensing; per-transaction processing fees; card issuance platform fees | M2P product pages | [M2P Credit Cards](https://m2pfintech.com/credit-cards/) |
| Commercial card capabilities | **Corporate credit card** issuance on unified platform: unsecured, secured, and corporate credit cards; credit lines on UPI; 3M+ debit cards issued; 30M+ transactions processed; 10+ banks served; 100% API coverage; rapid deployment (weeks not months); AI-powered personalization; fraud prevention; physical, virtual, and disposable card formats; **Intelligent Debit Card Stack** (2025) with AI-driven engagement | M2P product pages | [M2P Credit Cards](https://m2pfintech.com/credit-cards/) |
| Bank partnerships | IndusInd Bank (digital-first products), Federal Bank (first biometric auth for e-commerce card txns in India), Visa + CTBC Bank (Philippines debit issuance for rural banks), Karbon (corporate card, 30% txn volume increase) | M2P press releases, bank announcements | [IndusInd-M2P Partnership](https://www.indusind.bank.in/in/en/about-us/mediabrand/FY/2022-2023/August/IndusInd-Bank-partners-with-M2P-to-offer-digital-first-and-digital-only-products.html) |
| Strengths | Largest Indian card infrastructure provider; modular multi-product platform (credit, debit, BNPL, prepaid); expanding beyond India to MENA and APAC; compliance-ready for RBI mandates; 99.95% uptime; strong fintech ecosystem presence | M2P product pages, press releases | [M2P Debit Cards](https://m2pfintech.com/debit-cards/) |
| Weaknesses | Sub-unicorn valuation (~$790M) limits capital firepower; India-centric despite international expansion; commercial card capabilities less mature than consumer card stack; limited brand awareness outside India/MENA | Market analysis | [M2P Funding (Entrackr)](https://entrackr.com/2024/09/m2p-fintech-raises-over-100-mn-in-primary-and-secondary-funding/) |
| Vulnerability | Zaggle dominates corporate prepaid card space in India; global players (Marqeta, i2c) entering India; Razorpay's Banking Stack competes for bank infrastructure; CARD91 emerging as alternative | Market analysis | [M2P Fintech Homepage](https://m2pfintech.com/) |

---

### Zaggle

| Dimension | Detail | Source | URL |
|-----------|--------|--------|-----|
| Revenue | Q3 FY26: ₹4,976 crore revenue (+47.9% YoY); ₹360 crore PAT (+77.7% YoY); 9-month TTM: ~₹1,510 crore; FY26 guidance: 40–45% growth | Zaggle Q3 FY26 results | [Zaggle Q3 FY26](https://eduinvesting.in/zaggle-prepaid-20260217/) |
| Target segment | Indian corporates (3,700+ clients); public companies; listed on NSE/BSE; serves enterprises across benefits, expenses, travel, and vendor payments | Zaggle product pages, investor reports | [Zaggle Q3 FY26](https://eduinvesting.in/zaggle-prepaid-20260217/) |
| Revenue model | Program fees (42%), Propel Platform (54%), Software fees (4%); earns from card commissions, merchant interchange, and corporate SaaS subscriptions | Zaggle investor presentations | [Zaggle Q2 FY26](https://eduinvesting.in/zaggle-prepaid-20251111/) |
| Commercial card capabilities | **India's #1 prepaid card issuer**: 50M+ cards issued; corporate expense cards with dynamic spending controls and real-time visibility; employee benefits management; travel allowance cards; vendor payment solutions (Zoyer platform); forex cards; fleet management; ZatiX analytics platform for spend intelligence; co-branded corporate credit card with Yes Bank for T&E | Zaggle product pages, press releases | [Zaggle Cards](https://zagglecards.com/) |
| Bank partnerships | Yes Bank (corporate credit card), Standard Chartered Bank (prepaid card solutions, Sep 2025), IndusInd Bank, NSDL Payments Bank, AU Small Finance Bank (Mar 2026); 16 banking partners total; 45M+ co-branded prepaid cards issued | Zaggle press releases | [Zaggle-Standard Chartered](https://www.aninews.in/news/business/zaggle-partners-with-standard-chartered-bank-to-redefine-corporate-spend-management-with-its-prepaid-card-solutions20250903172805) |
| Enterprise clients | Tata Power, DTDC, Blue Star, Kotak Mahindra Bank, Apollo Clinic, Chennai Super Kings, Pirelli | Zaggle press releases, CBInsights | [Zaggle-CSK Partnership](https://www.ndtvprofit.com/business/zaggle-expands-corporate-card-footprint-through-chennai-super-kings-partnership-11143067) |
| Strengths | Dominant Indian corporate prepaid card franchise (50M+ cards); strong revenue growth trajectory (+48% YoY); publicly listed (transparency + capital access); integrated benefits + expense + travel management; deep banking partner network (16 banks) | Zaggle investor reports | [Zaggle Q3 FY26](https://eduinvesting.in/zaggle-prepaid-20260217/) |
| Weaknesses | Primarily prepaid card model — limited credit card capabilities (one co-brand with Yes Bank); India-only; dependent on interchange revenue model; Propel Platform (54% of revenue) less transparent in value delivery; tax-benefit-driven demand may shift with regulatory changes | Zaggle investor presentations | [Zaggle Q3 FY26](https://eduinvesting.in/zaggle-prepaid-20260217/) |
| Vulnerability | EnKash launching unified corporate card ecosystem (credit + prepaid + UPI); global expense platforms (Ramp, Brex) potentially entering India; M2P and CARD91 competing on infrastructure layer; credit card capabilities underdeveloped vs. competitors | Market analysis | [Zaggle Q2 FY26](https://eduinvesting.in/zaggle-prepaid-20251111/) |

---

### EnKash

| Dimension | Detail | Source | URL |
|-----------|--------|--------|-----|
| Revenue | FY25: ₹71 crore operating revenue (down 77% from FY24's ₹308 crore — driven by service income decline); loss reduced 54% to ₹17 crore; $23.5M total funding raised (Series B, Apr 2022) | Entrackr, Inc42, CBInsights | [EnKash Revenue (Entrackr)](https://entrackr.com/fintrackr/enkashs-revenue-nosedives-77-in-fy25-halves-losses-10590754) |
| Target segment | Indian SMEs and enterprises; 5,000+ businesses served; 1M+ corporate cards issued; RBI-licensed PPI issuer | EnKash press releases | [EnKash PPI License](https://www.prnewswire.com/in/news-releases/enkash-secures-prestigious-ppi-license-strengthening-its-leadership-in-corporate-cards-and-spend-management-302424099.html) |
| Revenue model | Corporate card interchange + platform SaaS fees; transactional revenue from spend management; AP automation fees | EnKash product pages | [EnKash Products](https://www.enkash.com/products) |
| Commercial card capabilities | **India's first unified corporate card ecosystem** (Oct 2025): integrates travel cards, employee cards, fleet cards, fuel cards, benefit cards with expense management and UPI wallets on single platform; virtual cards (single/multi-use); purchase cards and T&E cards; AI-powered expense management (receipt scanning, auto-reconciliation, policy-aligned approvals); digital petty cash; budget tracking; real-time spend analytics; RBI PPI license (Apr 2025) | EnKash press releases | [EnKash Unified Ecosystem](https://www.prnewswire.com/in/news-releases/enkash-unveils-indias-first-unified-corporate-card-ecosystem-for-businesses-302582732.html) |
| Enterprise clients | Starbucks, Reliance, Pristyn Care, DTDC, McDonald's, Adidas, Mahindra Finance, PNB Housing, Tata AIG, British Airways, Vijay Sales, Rakuten | EnKash website | [EnKash Corporate Cards](https://www.enkash.com/products/corporate-cards/) |
| Strengths | Unified corporate card ecosystem (unique in India — credit + prepaid + UPI on one platform); strong enterprise client roster; RBI PPI license; AI-first expense automation; comprehensive product suite (cards + AP + reimbursements + petty cash) | EnKash press releases | [EnKash Unified Ecosystem](https://www.prnewswire.com/in/news-releases/enkash-unveils-indias-first-unified-corporate-card-ecosystem-for-businesses-302582732.html) |
| Weaknesses | Dramatic revenue decline (FY25: -77% YoY) raises sustainability questions; small funding base ($23.5M total); still loss-making; limited scale compared to Zaggle (50M cards vs. 1M); 166 employees limits execution capacity | Entrackr, market analysis | [EnKash Revenue (Entrackr)](https://entrackr.com/fintrackr/enkashs-revenue-nosedives-77-in-fy25-halves-losses-10590754) |
| Vulnerability | Zaggle has 50x card issuance scale and growing profitability; revenue collapse may signal business model pivot or customer loss; underfunded relative to competitors; global platforms (Ramp, SAP Concur) competing for enterprise expense management | Market analysis | [EnKash Revenue (Entrackr)](https://entrackr.com/fintrackr/enkashs-revenue-nosedives-77-in-fy25-halves-losses-10590754) |

---

### YAP

| Dimension | Detail | Source | URL |
|-----------|--------|--------|-----|
| Status | **Insufficient public data available** — web searches returned no results for "YAP" as a standalone Indian card issuance API platform. The brand may have been absorbed, rebranded, or is operating at a scale below public research visibility. CARD91 and CardForge (Toucan OS) appear to occupy the space YAP is described as filling | Web search results | [unverified — needs manual confirmation] |
| Alternative players in segment | **CARD91**: end-to-end payment infrastructure; credit card management (Optimus), PPI, credit line management; LinkedIn Top Startups 2025; full-stack UPI acquiring; 99.99% uptime, ~2,000 TPS. **CardForge (Toucan OS)**: modular API-first card issuing; RBI/NPCI/PCI DSS v4.0 compliant; 1M+ daily txns; 99.95% uptime | CARD91 and CardForge websites | [CARD91](https://card91.io/) |

---

## Bank Signals

| Bank | Tier | Geography | Vendor | Signal | Source URL |
|------|------|-----------|--------|--------|-----------|
| JPMorgan Chase | Large ($100B+) | U.S. | FIS/TSYS (TS2) | Long-standing card processing relationship; selected TSYS for ~87M cardmember portfolio (2004); now under FIS Total Issuing Solutions | [JPMorgan-TSYS](https://jpmorganchaseco.gcs-web.com/news-releases/news-release-details/jpmorgan-chase-selects-tsysr-credit-card-processing) |
| U.S. Bank | Large ($100B+) | U.S., Europe, Canada | FIS/TSYS (TS2) | 25+ year TSYS client; extended long-term renewal for commercial card payment services across U.S., Europe, and Canada | [TSYS-US Bank](https://www.securetechalliance.org/tsys-extends-relationship-with-u-s-bank/) |
| Santander | Large ($100B+) | Europe | FIS/TSYS (TS2) | Migrated to TS2 platform in 2022 for commercial card processing | [Santander-TSYS Migration](https://www.santanderbank.com/documents/330001/2140033/Card-Migration-Frequently-Asked-Questions+%281%29.pdf/38d13193-c410-59cd-aeda-d9891fa474f8) |
| U.S. Bank (Elan) + Fiserv | Large ($100B+) | U.S. | Fiserv | U.S. Bank integrating Elan Financial Services credit card capabilities into Fiserv Credit Choice; full portfolio conversion expected end-2025; integrated digital tech available H1 2026 | [U.S. Bank-Fiserv](https://www.nasdaq.com/press-release/us-bank-and-fiserv-create-market-leading-integrated-agent-card-issuance-2025-06-12) |
| First Horizon Bank | Mid-size ($10B–$100B) | U.S. | DXC (migrating FROM Fiserv) | Commercial card platform migration from Fiserv to DXC; new cards issued Oct 2025; old cards deactivated Nov 2025 | [First Horizon Migration](https://www.firsthorizon.com/Fiserv-DXC-Commercial-Card-Conversion) |
| UK Retail Bank (unnamed) | Large ($100B+) | UK | ACI Worldwide (Connetic) | First UK retail bank to consolidate SWIFT, CHAPS, Faster Payments on single cloud-native SaaS platform (Feb 2026) | [ACI UK Bank Win](https://investor.aciworldwide.com/news-releases/news-release-details/aci-connetic-accelerates-global-adoption-uk-banks-can-now-unite) |
| Major U.S. FI (unnamed) | Large ($100B+) | U.S. | Galileo/SoFi | Major U.S. financial services provider with active debit card portfolio transitioning to Galileo; top-10 revenue client; full transition early 2026 | [Galileo Partnerships](https://www.galileo-ft.com/news/galileo-partnerships-help-drive-sofi-record-growth/) |
| U.S. Treasury (Direct Express) | Government | U.S. | Galileo/SoFi | U.S. Department of Treasury selected Galileo for Direct Express prepaid debit processing (3.4M beneficiaries); integration 2025, financial impact 2026 | [Galileo Partnerships](https://www.galileo-ft.com/news/galileo-partnerships-help-drive-sofi-record-growth/) |
| Finastra NA bank clients | Mid-size / Regional | U.S. / Canada | i2c | Finastra-i2c strategic partnership (Mar 2025) for debit card issuance and digital wallet solutions across NA banks and credit unions via Phoenix core | [Finastra-i2c](https://financialit.net/news/e-wallets/finastra-and-i2c-inc-announce-strategic-partnership-offer-debit-card-issuance-and) |
| OFX | Fintech | Australia, Canada, Europe, U.S., APAC | Thredd | Corporate card expansion across multiple global markets; physical and virtual cards with real-time spend controls (Sep 2025) | [Thredd-OFX](https://www.businesswire.com/news/home/20250925917356/en/Thredd-Powers-OFX-Corporate-Card-Expansion-Across-Key-Global-Markets) |
| PhotonPay | Fintech | Global (230+ countries) | Thredd | Card processing partnership for enhanced issuer processing, settlement routing, tokenization (Oct 2025) | [Thredd-PhotonPay](https://www.thredd.com/about-us/newsroom/company-news/photonpay-partners-with-thredd-to-enhance-card-infrastructure) |
| Capital One | Large ($100B+) | U.S. | Brex (acquiring) | Capital One acquiring Brex for $5.15B (Jan 2026); integrating corporate card + spend management into bank platform; expected close mid-2026 | [Capital One-Brex](https://www.capitalone.com/about/newsroom/capital-one-to-acquire-brex/) |
| IndusInd Bank | Mid-size ($10B–$100B) | India | M2P Fintech | Partnership for digital-first and digital-only card products | [IndusInd-M2P](https://www.indusind.bank.in/in/en/about-us/mediabrand/FY/2022-2023/August/IndusInd-Bank-partners-with-M2P-to-offer-digital-first-and-digital-only-products.html) |
| Federal Bank | Mid-size ($10B–$100B) | India | M2P Fintech | India's first biometric authentication for e-commerce card transactions | [Federal Bank-M2P](https://federalbank.co.in/federal-bank-launches-first-ever-biometric-authentication-for-ecom-card-transactions-in-india) |
| Yes Bank | Mid-size ($10B–$100B) | India | Zaggle | Co-branded corporate credit card for T&E expenses; integrated with ZatiX analytics | [Yes Bank-Zaggle](https://indianstartupnews.com/news/yes-bank-announces-partnership-with-zaggle-to-launch-next-gen-corporate-credit-card) |
| Standard Chartered | Large ($100B+) | India | Zaggle | Prepaid card solutions for corporate expense management, travel, vendor payments (Sep 2025) | [StanChart-Zaggle](https://www.aninews.in/news/business/zaggle-partners-with-standard-chartered-bank-to-redefine-corporate-spend-management-with-its-prepaid-card-solutions20250903172805) |
| AU Small Finance Bank | Regional ($1B–$10B) | India | Zaggle | Partnership initiated March 2026 | [unverified — needs manual confirmation via CBInsights] |

---

## Key Findings

### Market structure

1. **FIS/TSYS is now the undisputed legacy commercial card processing incumbent** — the $13.5B TSYS acquisition (Jan 2026) consolidates TS2 commercial card processing (JPMorgan Chase, U.S. Bank, Santander) under FIS, creating a dominant franchise with 40B+ transactions/year. Banks on TS2 now deal with FIS.

2. **Fiserv holds the broadest integrated commercial card stack** — from card manufacturing (Output Solutions) through issuer processing (Credit Select) to corporate card management (PCard, T&E, virtual, fleet). However, First Horizon's public migration away from Fiserv signals competitive vulnerability in commercial card processing.

3. **ACI Worldwide is making a late but aggressive entry** — ACI Connetic for Cards (March 2026) brings cloud-native card issuing/acquiring capabilities that unify with A2A payments and fraud on a single platform. The first UK bank win validates the thesis, but card processing is genuinely new territory for ACI.

### Modern challengers

4. **Marqeta is the commercial card platform of choice for expense management fintechs** — it powers Ramp ($1B ARR, $22.5B valuation) and Divvy, making it the indirect infrastructure behind a significant share of U.S. commercial card volume. Portfolio migration services and UX Toolkit signal intent to win bank-direct business.

5. **i2c has the most complete modern commercial card platform** — dedicated commercial credit solution with Level 2/3 data, department-level purses, configurable hierarchies, and AI-powered credit decisioning. The Finastra partnership opens the NA bank distribution channel. However, brand awareness remains a barrier.

6. **Lithic is the developer-first alternative** — Commercial Charge Card (2023) and Commercial Revolving Credit (2024) provide a low-friction path for fintech developers to build commercial card programs. Smaller scale than Marqeta but differentiated by developer experience and both charge + revolving credit models.

7. **Thredd is the European commercial card processing leader for fintechs** — the OFX corporate card expansion across 5+ regions and PhotonPay partnership demonstrate multi-geography commercial card capability. U.S. market entry creates growth optionality but increases competitive exposure.

### India

8. **Zaggle dominates Indian corporate card issuance by volume** (50M+ cards, 3,700+ clients) with strong revenue growth (+48% YoY) and improving profitability — but is primarily a prepaid card player with limited credit card capabilities.

9. **EnKash has the most ambitious product vision** (India's first unified corporate card ecosystem) but faces severe financial headwinds — FY25 revenue declined 77% YoY, raising questions about execution capacity despite an impressive enterprise client roster.

10. **M2P Fintech is the infrastructure layer** — serving 200+ banks and 300+ lenders with card issuance APIs, but corporate credit card capabilities remain less mature than consumer/debit products.

### Strategic signals

11. **Capital One acquiring Brex for $5.15B** signals that major banks view corporate card + spend management as a strategic growth vector worth paying 5x+ revenue multiples.

12. **Card transactions are growing, not shrinking** — ACI projects global card transactions to grow from 776B (2024) to 1.1T by 2029 (+43%), driven by contactless, e-commerce, and critically, **B2B digitization**. Commercial cards are a growth segment within this trend.

13. **Virtual card capabilities are table stakes** — every modern player (Marqeta, i2c, Lithic, Thredd, EnKash, Zaggle, M2P) offers virtual card issuance via API with granular spend controls. Differentiation has shifted from "can you issue virtual cards?" to "how deep are your commercial data, hierarchy, and reconciliation capabilities?"

---

## Gaps and Unresolved Questions

1. **FIS Total Issuing Solutions commercial card roadmap**: No public detail on how FIS will modernize the TS2 commercial card platform post-acquisition. Will they add modern APIs, virtual card capabilities, and JIT funding to compete with Marqeta/i2c, or rely on incumbency?

2. **Marqeta direct bank commercial card wins**: Evidence of Marqeta powering fintech expense platforms is strong, but specific traditional bank wins for commercial card programs remain unconfirmed. Portfolio migration tools are new — adoption data not yet available.

3. **i2c commercial card client names**: Despite having the most complete commercial card platform among modern challengers, no specific commercial card bank client names were publicly available.

4. **Galileo commercial card depth**: Galileo's Cyberbank Core supports commercial payment services, but specific commercial card program details (purchase cards, T&E, virtual card for AP) were not publicly documented. Commercial capabilities appear earlier-stage than debit/prepaid.

5. **YAP**: No verifiable public data found for "YAP" as an Indian card issuance API platform. CARD91 and CardForge (Toucan OS) appear to serve this market segment and may be relevant substitutes.

6. **Lithic recent funding and valuation**: Last public round was July 2021 ($800M valuation). Current financial position unclear — no public update in 4+ years despite reaching $1B monthly TPV.

7. **EnKash revenue decline root cause**: The 77% FY25 revenue decline is dramatic and unexplained in public sources. Could indicate business model pivot, major client loss, or accounting reclassification. Needs manual investigation.

8. **ACI Connetic for Cards production deployments**: Launched March 2026 — no production card processing clients publicly announced yet. The UK bank win was for payments hub (SWIFT/CHAPS/Faster Payments), not card processing specifically.

9. **Global Payments TSYS TS2 commercial card client migration status**: How are TSYS commercial card clients (JPMorgan Chase, U.S. Bank, Santander) responding to the ownership change to FIS? Any migrations away?

10. **Level 2/3 commercial data capabilities**: Only i2c explicitly positions Level 2/3 data capture for commercial card programs. Degree of support from FIS/TSYS, Fiserv, and Marqeta for enhanced commercial data is not well-documented publicly.

---

*Document compiled March 2026. Sources cited inline with navigable URLs. Data points drawn from public earnings reports, press releases, product documentation, SEC filings, and financial media. Points marked [unverified — needs manual confirmation] could not be linked to a navigable source.*
