# Payments — Opportunity Analysis

*Prepared for Zeta's executive team and board. March 2026.*

---

## Executive Summary

The payments technology infrastructure market — what banks spend on platforms, processing, and related services from external vendors — is a **$60–85 billion market** (narrow scope) growing at **12–15% CAGR**, projected to exceed $130 billion by 2030. The broader market including fraud, tokenization, orchestration, and value-added services is **$150–200 billion** and growing faster ([McKinsey Global Payments Report 2025](https://www.mckinsey.com/industries/financial-services/our-insights/global-payments-report); [BCG Global Payments 2025](https://www.bcg.com/publications/2025/global-payments-transformation-amid-instability); [Grand View Research](https://grandviewresearch.com/industry-analysis/payment-processing-solutions-market)).

Eight structural shifts are creating the largest wave of payments infrastructure replacement in a generation. Real-time payments are becoming the default rail. Tokenization is moving from optional to mandated. Acquiring is diversifying into software-embedded channels. AI is entering payments operations. Regulators in all four focus markets are issuing mandates with hard deadlines. The regulatory calendar through 2028 is the densest in the industry's history.

The most underserved buyer segment is **mid-size and regional banks (Tier 2–3)**. Legacy incumbents are over-engineered and expensive. Modern challengers are designed for fintechs and platforms. No vendor delivers genuinely integrated, affordable, cloud-native payments infrastructure for mid-market banks.

**For Zeta:** Photon product lines align strongly with card issuance modernization, tokenization, acquiring diversification, and private payment networks. The combination of payments infrastructure with Evolution Fabric's operational substrate — making payments domains explicit, governed, and AI-ready — is a positioning no competitor occupies. The primary opportunity is Tier 2 US banks, with India as an accessible home market and UK/Europe and Brazil as regulatory-driven expansion markets.

**Recommended actions:** Lead with card issuance and tokenization (regulatory forcing functions create urgency), build acquiring presence through the mid-market gap, and use Evolution Fabric's operational model as the long-term differentiator. Defer payment hub orchestration (Volante and ACI are established), avoid cross-border as a primary play (specialist domain), and do not pursue Tier 1 banks as the primary segment.

---

# PART I — THE OPPORTUNITY

---

## 1. The Payments Technology Market

### What banks spend on payments technology

Global payments revenue is approximately **$2.5 trillion** ([McKinsey Global Payments Report 2025](https://www.mckinsey.com/industries/financial-services/our-insights/global-payments-report)) or **$1.9 trillion** using BCG's narrower fee-based definition ([BCG 2025](https://www.bcg.com/publications/2025/global-payments-transformation-amid-instability)). The vendor-addressable market — what banks pay for payments technology platforms and services — is a fraction of that total.

| Scope | 2025 Estimate | 2030 Projection | CAGR |
|---|---|---|---|
| Core processing, issuing/acquiring engines, payment hubs | $60–85B | $130–160B | 12–15% |
| Broad (including fraud, tokenization, orchestration, VAS) | $150–200B | $350–450B | 15–18% |

*Sources: [Grand View Research](https://grandviewresearch.com/industry-analysis/payment-processing-solutions-market), [Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/payment-processing-solutions-market), Juniper Research, vendor revenue proxies (2025)*

The technology layer is growing **3–4x faster** than payments revenue (4% CAGR for total payments revenue vs. 14–18% for the technology layer). Payments-focused fintech revenue alone reached $176 billion in 2024 ([BCG 2025](https://www.bcg.com/publications/2025/global-payments-transformation-amid-instability)). SaaS-enabled payments companies have delivered **37% annual total shareholder returns** vs. **2% for traditional acquirers** — a structural performance gap that is accelerating investment into the category ([BCG 2025](https://www.bcg.com/publications/2025/global-payments-transformation-amid-instability)).

### Fastest-growing segments

| Segment | 2025 Size | 2030 Projection | CAGR | Source |
|---|---|---|---|---|
| Payment orchestration | $1.7–2.1B | $6.1B | 24% | [ResearchAndMarkets/GlobeNewswire](https://www.globenewswire.com/news-release/2026/01/20/3221577/28124/en/Payment-Orchestration-Platform-Business-Analysis-Report-2025-Market-to-Reach-6-1-Billion-by-2030.html) |
| Modern card issuance platforms | $1.8B | $4.2B | 19% | [Juniper Research](https://www.juniperresearch.com/press/modern-card-issuing-platforms-market-to-surpass-42-billion-by-2030-as-juniper-research-reveals-global-leaders-driving-fintech-innovation) |
| Payment tokenization | $3.5B | $10B+ | 18–20% | [MarketIntelo](https://marketintelo.com/report/payment-tokenization-market) |
| Fraud detection (payments) | $33.1B | $55B+ | 10–19% | [Grand View Research](https://grandviewresearch.com/industry-analysis/fraud-detection-prevention-market) |
| Merchant acquiring | $25–28B | $46–53B | 12–14% | Allied Market Research, Grand View Research (2025) |

### Spend by bank tier

| Tier | Share of Bank IT | Payments Tech Spend (est.) | Build vs. Buy |
|---|---|---|---|
| Tier 1 (top 50 global) | 50–60% | $33–66B | Mix; increasingly in-house for strategic capabilities |
| Tier 2 (mid-size, 200–500) | 25–30% | $16–22B | Primarily buy/outsource |
| Tier 3 (community/small, thousands) | 10–20% | $6–15B | Almost entirely outsourced |

Tier 2–3 banks are heavily vendor-dependent for payments technology and represent the primary growth market for platform vendors. JPMorgan's 2026 technology budget alone is approximately $20 billion ([PYMNTS](https://www.pymnts.com/news/banking/2026/jpmorgans-20-billion-tech-bet-could-shrink-fintechs-innovation-edge/)), illustrating the scale at which Tier 1 banks operate — and why mid-market banks need fundamentally different vendor relationships.

### Spend by market

| Market | Payments Tech Vendor Revenue (est.) | Share of Global |
|---|---|---|
| USA | $25–40B | 30–40% |
| UK/Europe | $15–25B | 18–25% |
| India | $5–10B | 6–10% |
| Brazil | $3–6B | 3–6% |

*Sources: [Grand View Research (US)](https://www.grandviewresearch.com/horizon/outlook/payment-processing-solutions-market/united-states), [UniVDatos (Brazil)](https://univdatos.com/reports/brazil-digital-payments-market) (2025). India and Brazil estimates are analyst synthesis — most public reports conflate technology spend with transaction values.*

---

## 2. How We Got Here

Three waves of payments technology investment over the past two decades shaped the current landscape.

**Wave 1 (2005–2015): Core modernization.** Banks invested in card management centralization, SWIFT upgrades, and first-generation payment hubs. The dominant vendors — FIS, First Data (now Fiserv), TSYS (now back with FIS) — built their franchises during this period. Most systems deployed in this wave are still in production.

**Wave 2 (2015–2020): Digital payments explosion.** Mobile wallets, real-time payments (UPI launched 2016, UK Faster Payments scaled, SEPA Instant launched 2017), PSD2 open banking, and fintech disruption drove investment. But most bank spending went to regulatory compliance and channel overlay, not infrastructure replacement. The underlying payment hubs remained unchanged.

**Wave 3 (2020–2025): Platform era.** Embedded payments, BNPL, tokenization mandates, payment orchestration, and acquiring diversification created demand for modern, API-first, multi-rail infrastructure. COVID accelerated digital payments adoption by 3–5 years. FedNow launched (2023). PIX scaled to universal adoption in Brazil. UPI became the world's largest real-time payments system.

**What was deferred.** Through all three waves, most banks avoided replacing core payment processing infrastructure. They layered new capabilities on top of aging platforms. The result is the technology debt overhang that now drives the structural shifts described below: banks that can no longer layer and must replace.

---

## 3. Structural Shifts Creating Opportunity

### Shift 1: Real-Time Payments Becoming the Default Rail

Real-time payments are moving from premium alternative to primary rail. In three of the four focus markets, this shift is already decisive.

**Evidence:**

- **India (UPI):** 185.9 billion transactions in FY25, approximately 84% of all retail digital payments. 700 million daily transactions in January 2026. Debit card transactions fell 29.5% YoY as UPI displaced them ([MediaNama/RBI](https://www.medianama.com/2025/05/223-upi-84-india-fy25-retail-payment-volume-rbi/)).
- **Brazil (PIX):** 79.8 billion transactions in 2025 (R$35.4 trillion). PIX now represents **50.9% of all electronic payment volume** — surpassing cards. Single-day record: 297.4 million transactions ([G1/BCB](https://g1.globo.com/economia/noticia/2026/02/07/pix-movimenta-r-354-trilhoes-em-2025-com-quase-80-bilhoes-de-transacoes-e-bate-recorde.ghtml)).
- **USA:** FedNow reached **1,600+ institutions** with 459% volume growth in 2025 ([Digital Transactions](https://www.digitaltransactions.net/fednow-tallies-more-than-1600-fis-in-its-real-time-payments-service/); [FRB Services](https://www.frbservices.org/resources/financial-services/fednow/volume-value-stats)). RTP (The Clearing House) carries 98% of US instant payment volume, with 1,130+ participating FIs ([TCH](https://www.theclearinghouse.org/payment-systems/rtp)). The US has a unique dual-network challenge requiring orchestration.
- **EU:** SEPA Instant grew to **24.7%** of all credit transfers (Q1 2025). The EU Instant Payments Regulation (effective October 2025) mandates all PSPs offer instant payments at standard pricing, 24/7 ([ECB](https://www.ecb.europa.eu/paym/integration/retail/instant_payments/html/instant_payments_regulation.en.html); [European Commission](https://finance.ec.europa.eu/news/new-eu-rules-make-instant-euro-payments-faster-and-safer-2025-10-10_en)).
- **UK:** Faster Payments processed 5.088 billion transactions in 2024 ([Pay.UK QSR](https://www.wearepay.uk/wp-content/uploads/2025/03/Q4-2024-QSR.pdf)).

**Opportunity by segment:**

- **Tier 1 banks:** Already on real-time rails but face orchestration complexity — routing across FedNow, RTP, ACH, wires, SEPA Instant, and card networks from a single decisioning layer.
- **Tier 2 banks:** The acute gap. Large banks are **6x more likely** to have deployed real-time payments (74% vs. 44% for smaller institutions) ([PYMNTS](https://pymnts.com/news/digital-banking/2025/60percent-banks-embrace-payment-hubs-modernize-digital-experiences)). Cost, integration complexity, and 24/7 operational demands are the barriers. These banks need managed real-time connectivity at predictable cost.
- **Tier 3 banks:** Increasingly join FedNow as receive-only (only ~40% of FedNow participants can send). They consume through their core banking provider.

### Shift 2: Tokenization as Platform Infrastructure

Network tokenization is moving from optional optimization to mandated infrastructure — driven by network requirements, fraud economics, and regulatory directives.

**Evidence:**

- Visa has issued **over 10 billion tokens**, with approximately 29% of its transactions now tokenized. Visa estimates tokenization prevents **$650 million in fraud annually** and has generated **$40 billion in incremental e-commerce** ([Visa Acceptance Solutions](https://usa.visa.com/products/visa-token-service.html), 2025).
- Mastercard processes **4 billion tokenized transactions per month** (50% YoY growth). Mastercard targets **100% of e-commerce transactions tokenized by 2030**, beginning with phased mandates in APAC (Singapore, Malaysia, Vietnam) ([Mastercard](https://www.mastercard.com/news/press/2024/mastercard-tokenization/), 2024–2025).
- Tokenized transactions show **40–60% lower fraud rates** and **+5–15 percentage point** approval rate improvements ([Visa](https://usa.visa.com/products/visa-token-service.html); [Payments Dive](https://www.paymentsdive.com/), 2025).
- Global card fraud reached **$33.4 billion** in 2024 with card-not-present (CNP) accounting for 71–73% of losses. The US bears 42% of global fraud on 26% of volume (Nilson Report, "Global Card Fraud Report," Issue 1248, Feb 2026 — paywalled).
- India's RBI mandated card-on-file tokenization (in effect since 2022), with updated authentication mechanisms compliance by April 2026 ([RBI Circular](https://www.pdicai.org/Docs/RBI-2025-26-79_299202514919530.pdf)).

**Opportunity by segment:**

- **Tier 1 banks:** Largely compliant. Now extending tokenization into B2B virtual cards and multi-credential management.
- **Tier 2 banks:** Need tokenization platform infrastructure. Network mandates have deadlines; non-compliance risks fines or loss of processing privileges. Many mid-size issuers lack dedicated tokenization infrastructure and rely on network-level solutions that limit flexibility.
- **Tier 3 banks:** Consume tokenization through their card processor.

### Shift 3: Acquiring Diversification and Embedded Acceptance

Merchant acquiring is fragmenting from POS-terminal-based processing into an omnichannel, software-embedded, platform-distributed model.

**Evidence:**

- SaaS-embedded providers now capture **36% of SME acquiring revenues**, projected to reach 45% by 2028 ([BCG 2025](https://www.bcg.com/publications/2025/global-payments-transformation-amid-instability)).
- Over 50% of relevant ISVs in North America now offer embedded payments ([BCG 2025](https://www.bcg.com/publications/2025/global-payments-transformation-amid-instability)).
- The embedded payments market is **$24 billion** (2024), projected to reach **$99.7 billion by 2030** (26.8% CAGR) (ResearchAndMarkets, "Embedded Payments Market," 2025 — paywalled).
- In Brazil, PIX QR drives 41% of all PIX transactions — at zero merchant fees vs. ~2% for cards.
- Bank onboarding costs **$496 over 7 days** vs. PayTech onboarding at **$214 in under 1 hour** (Capgemini, *World Payments Report 2026* — paywalled).

**Opportunity by segment:**

- **Tier 1 banks:** Already in acquiring. The opportunity is infrastructure for the long tail of merchants they cannot serve directly.
- **Tier 2 banks:** The primary growth opportunity. Mid-size banks entering or modernizing acquiring need multi-channel capability (POS, QR, online, payment facilitation) without building from scratch.
- **Tier 3 banks:** Participate through BaaS models — providing settlement infrastructure to platforms and fintechs.

### Shift 4: Private and Proprietary Payment Networks

Banks, corporates, and platforms are building closed-loop and hybrid payment networks — bypassing card network interchange and capturing customer data directly.

**Evidence:**

- **45% of US retailers** now offer branded closed-loop cards. US private-label credit card market exceeds **$300 billion** (Global Growth Insights, Bankhawk, 2025).
- The Visa/Mastercard US interchange settlement (through 2030) is capping fees, accelerating interest in interchange-free alternatives.
- Structural motivations: bypass interchange (1–3% per-transaction savings), own customer data, build loyalty moats, create new revenue streams from float and premium services.

**Opportunity by segment:**

- **Tier 1 banks:** Operate as issuers for retailer private-label programs. The infrastructure opportunity is in the platform powering these programs.
- **Tier 2 banks:** Can offer private payment network infrastructure to regional retailers and corporates — a differentiator against larger banks.
- **Corporates and platforms:** The emerging buyer. Large employers, retail chains, and platforms want branded payment instruments with ledger, settlement, issuance, loyalty, and compliance infrastructure.

### Shift 5: AI in Payments Operations

AI is entering payments operations — not as analytics dashboards but as operational actors in fraud, reconciliation, dispute resolution, and compliance.

**Evidence:**

- **98% of organizations** use AI in fraud and AML processes ([McKinsey](https://www.mckinsey.com/industries/financial-services/our-insights/), 2025).
- SWIFT's AI-based fraud detection pilot with 13 banks analyzed 10 million transactions and demonstrated detection rates above conventional rules ([SWIFT](https://www.swift.com/news-events/news/swift-expands-ai-fraud-detection), 2025).
- Finastra's OperatorAssist reduces manual payment investigation time by **20–30%**; its Intelligent Routing achieves **95%+ straight-through processing** ([Finastra](https://www.finastra.com/financial-services-state-nation-survey-2026), 2025).
- **60% of PayTechs** vs. **41% of banks** have deployed GenAI in payments operations — banks are behind (Capgemini, *World Payments Report 2026* — paywalled).
- ClearBank achieved **80% reduction in payment recovery time** using AI-based exception handling (ClearBank case study, 2025).
- Organizations lose an average of **$98.5 million annually** from money movement disruptions and inefficiencies ([PYMNTS](https://pymnts.com/news/digital-banking/2025/60percent-banks-embrace-payment-hubs-modernize-digital-experiences), 2025).

**Opportunity by segment:**

- **All tiers:** AI for fraud detection and reconciliation is universally relevant. Tier 1 banks build or buy best-of-breed (NICE Actimize, Featurespace). Tier 2–3 banks need AI integrated into their payments platform as a core layer, not a separate system.
- **Competitive gap:** No payments platform vendor offers deeply integrated, AI-native operations as a core layer of the payments hub — it is always an add-on or separate procurement.

### Shift 6: Cross-Border Modernization

Cross-border payments infrastructure is being forced into modernization by ISO 20022 deadlines, fintech competition, and persistent cost pressure.

**Evidence:**

- SWIFT's MX-only era took effect November 22, 2025. Nearly half of banks were behind on readiness before the deadline. Address data remediation deadline: November 2026. Exceptions & Investigations modernization: November 2027 ([SWIFT](https://www.swift.com/news-events/press-releases/global-financial-community-completes-switch-iso-20022-paving-way-new-levels-cross-border-payment-speed-and-innovation-around-world)).
- Cross-border payment flows reached **$194.6 trillion** in 2024, projected to reach $320 trillion by 2032 (FXC Intelligence, 2025).
- The global average cost of sending remittances remains at **6.49%** of principal — more than double the G20's 3% target. Banks charge 12.5% on average vs. 4.9% for digital channels (World Bank, *Remittance Prices Worldwide,* 2025).
- India received **$129.1 billion** in cross-border remittances in 2024 — the world's largest recipient (World Bank, *Migration and Development Brief,* 2025).

**Opportunity by segment:**

- **Tier 1 banks:** Must complete ISO 20022 migration and defend against fintech corridor competition. They buy specialized tools (Volante, ACI).
- **Tier 2 banks:** Most impacted by ISO 20022 remediation — mid-tier and regional banks with legacy correspondent infrastructure face the most work. They need affordable, managed migration paths.

### Shift 7: Regulatory-Driven Infrastructure Replacement

Across all four markets, regulators are issuing mandates with specific deadlines that force payments infrastructure investment. Compliance is not optional.

| Market | Mandate | Deadline | Investment Required |
|---|---|---|---|
| USA | FedNow adoption | Ongoing (competitive) | Real-time rails, 24/7 ops, liquidity |
| USA | GENIUS Act (stablecoins) | Regulations by July 2026 | Tokenization, reserve management |
| India | RBI card tokenization | April 2026 | Token vaults, checkout flows |
| EU | Instant Payments Regulation (send) | October 2025 | 24/7 processing, VoP, liquidity |
| EU | ISO 20022 address remediation | November 2026 | Data remediation, E&I modernization |
| EU | PSD3/PSR | H2 2027 | Fraud, APIs, licensing |
| Brazil | PIX Automático / Parcelado | 2025 | Recurring payments, credit origination |
| Brazil | MED 2.0 (fraud disputes) | February 2026 | Fraud detection, dispute resolution |

*Sources: [FedNow](https://www.frbservices.org/financial-services/fednow); [Venable (GENIUS Act)](https://www.venable.com/insights/publications/2025/07/congress-passes-the-genius-act-key-impacts-for-the); [RBI](https://www.pdicai.org/Docs/RBI-2025-26-79_299202514919530.pdf); [ECB](https://www.ecb.europa.eu/paym/integration/retail/instant_payments/html/instant_payments_regulation.en.html); [SWIFT](https://www.swift.com/news-events/press-releases/global-financial-community-completes-switch-iso-20022-paving-way-new-levels-cross-border-payment-speed-and-innovation-around-world); [SZA PSD3](https://www.sza.de/en/thinktank/psd3-psr-eu-payment-services-regulation)*

Each mandate creates a buying event. The regulatory calendar through 2028 is the densest in the industry's history — and all four markets are simultaneously active.

### Shift 8: Banks as Embedded Payments Infrastructure Providers

Banks are being asked to offer their payments capabilities as embeddable services. But the infrastructure most banks run was never designed for this.

**Evidence:**

- Embedded finance TAM (North America + Europe): **$185 billion**, of which only ~$32 billion is currently penetrated — over 80% remains available ([BCG 2025](https://www.bcg.com/publications/2025/global-payments-transformation-amid-instability)).
- BaaS market growing at 17–21% CAGR, but facing regulatory tightening: the Synapse collapse ($85 million customer deposit shortfall) and Federal Reserve cease-and-desist against Evolve Bank signal stricter oversight ([ABA Banking Journal](https://bankingjournal.aba.com/), 2024–2025).
- Regulatory tightening is pushing fintechs toward more regulated bank partners — creating an opening for well-prepared mid-size banks.

---

## 4. The Engagement Landscape

These structural shifts produce specific buying events — projects that banks commission technology vendors to deliver.

### Payment Hub Modernization
**Shifts:** 1, 6, 7. **Primary buyer:** Tier 2 banks. ~60% of banks have implemented or are implementing payment hubs ([PYMNTS](https://pymnts.com/news/digital-banking/2025/60percent-banks-embrace-payment-hubs-modernize-digital-experiences)). 87% of FIs plan modernization investment in 2026 ([Finastra](https://www.finastra.com/financial-services-state-nation-survey-2026)). **Named examples:** Nationwide Building Society migrated 91.5% of Faster Payments to new infrastructure (Form3 + Accenture). NatWest adopted ISO 20022 and launched Bankline Direct APIs. Deutsche Bank reported 97% ISO 20022 readiness. In the US, Metropolitan Commercial Bank and Vantage Bank went live with Finzly.

### Card Issuance Platform Replacement
**Shifts:** 2, 7. **Primary buyer:** Tier 2 banks. Over 80% of European banks are modernizing card platforms. Banks take 18 months and £1M to launch a card product on legacy vs. 4–6 weeks on modern platforms. The FIS-TSYS consolidation forces banks to evaluate alternatives.

### Merchant Acquiring Stack Build-Out
**Shifts:** 3, 8. **Primary buyer:** Tier 2 banks entering or modernizing acquiring. 40% of SMB merchants considering switching to PayTechs; only 15% of small merchants satisfied with bank acquiring services (Capgemini, *World Payments Report 2026*).

### Tokenization Infrastructure
**Shifts:** 2. **Primary buyer:** All card issuers. Visa AFT mandate in effect (US). Mastercard AFT mandate March 2026 (UK, EEA, MENA). Enhanced merchant data requirements January 2027. RBI tokenization compliance April 2026.

### Private Payment Network Launch
**Shifts:** 4. **Primary buyer:** Tier 2 banks and corporates/retailers. 45% of US retailers now offer closed-loop cards. Interchange caps through 2030 accelerate interest.

### Embedded Payments / BaaS Enablement
**Shifts:** 8. **Primary buyer:** Tier 2 banks seeking platform revenue. Over 80% of $185B TAM remains unpenetrated. Regulatory tightening creates an opening for well-capitalized bank partners.

### Payments Reconciliation and Operations Transformation
**Shifts:** 5. **Primary buyer:** All tiers. $98.5M average annual losses from payment inefficiencies. 60% PayTech vs. 41% bank GenAI adoption gap widening.

### Cross-Border Payments Modernization
**Shifts:** 6, 7. **Primary buyer:** Tier 2 banks with legacy correspondent infrastructure. ISO 20022 address remediation deadline: November 2026. E&I modernization: November 2027.

---

## 5. Competitive Landscape

### The defining event: FIS-TSYS / Global Payments-Worldpay swap

FIS acquired Global Payments' Issuer Solutions (formerly TSYS) for **$13.5 billion**, closed January 2026 ([FIS](https://www.fisglobal.com/about-us/media-room/press-release/2026/fis-completes-strategic-acquisition-of-global-payments-issuer-solutions-business)). Global Payments acquired Worldpay from FIS. FIS is now the dominant issuer processor (40B+ transactions/year, 150+ FIs). Global Payments is now the dominant pure-play acquirer. Banks are being forced to pick sides.

### Legacy incumbents

| Vendor | Revenue | Position | Vulnerability |
|---|---|---|---|
| FIS | $10.7B (guided $13.8B for 2026 with TSYS) ([FIS 10-K](https://www.stocktitan.net/sec-filings/FIS/10-k-fidelity-national-information-services-inc-files-annual-report-faa6cf780c27.html)) | Dominant issuer processor + banking | Integration risk; mid-market finds it over-engineered |
| Fiserv | $21.2B ([Fiserv Earnings](https://investors.fiserv.com/news-releases/news-release-details/fiserv-reports-fourth-quarter-and-full-year-2025-results)) | Full-stack bank + merchant (largest by revenue) | Legacy architecture; inflexibility for mid-market |
| Global Payments | $9.3B adjusted (Global Payments 10-K, Feb 2026) | Pure-play acquiring post-restructuring | No bank infrastructure (divested issuing) |
| ACI Worldwide | $1.76B (ACI Earnings, Feb 2026) | Payments hub + real-time (Connetic) | Competing with Volante and Form3 for hub deals |

### Modern challengers

| Vendor | Revenue | Position | Limitation |
|---|---|---|---|
| Marqeta | $625M ([Nasdaq](https://www.nasdaq.com/press-release/marqeta-reports-fourth-quarter-and-full-year-2025-financial-results-2026-02-24)) | Modern card issuing for fintechs | Customer concentration (Block >50%); fintech-oriented |
| Galileo/SoFi | ~$450M (estimated; [SoFi IR](https://investors.sofi.com/financials/quarterly-results/default.aspx)) | Payments + banking infrastructure | SoFi parent creates channel conflict with banks |
| Stripe | ~$5.1B (estimated; private company — [PYMNTS](https://www.pymnts.com/), Sacra) | Platform payments + BaaS | Not bank infrastructure; BaaS regulatory risk |
| Adyen | €2.36B ([Adyen H2 2025](https://www.adyen.com/press-and-media/adyen-publishes-h2-2025-financial-results-3pgu2)) | End-to-end money movement (merchant) | Enterprise merchant focus |

### Specialists

| Vendor | Position | Relevance |
|---|---|---|
| Volante | Cloud-native payments hub (Gartner Leader) | Strongest competitor in payment hub orchestration |
| Form3 | Cloud-native account-to-account payments (UK/EU) | Growing from UK base; Nationwide deployment is proof point |
| Finzly | FedNow + real-time for US community banks | Small but positioned at the FedNow adoption wave |

### India and Brazil vendors

| Vendor | Revenue | Position |
|---|---|---|
| Razorpay (India) | ~$490M FY25 (Entrackr, 2025 — estimated) | Dominant SME payment gateway; expanding into banking |
| Pine Labs (India) | ~$259M FY25 (estimated, private) | Merchant acquiring + POS; acquired by Fiserv (2025) |
| StoneCo (Brazil) | R$14.15B FY2025 ([Valor Econômico](https://valor.globo.com/financas/noticia/2026/03/02/stone-tem-lucro-de-r-2477-bilhes-em-2025-com-expanso-de-175-pontos-percentuais.ghtml)) | Leading financial technology + acquiring |
| PagBank (Brazil) | R$3.5B Q4 2025 (PagBank Earnings, Q4 2025) | Consumer banking + payments platform |

### The critical competitive gap

Mid-size and regional banks are the most underserved segment:

- Large FIs are 6x more likely to deploy real-time payments (74% vs. 44%)
- 37% of credit union leaders say payment offerings don't meet member needs
- 73% of banking professionals identify fintechs as top competitive threats
- 60% of credit unions self-identify as "fast followers" — wanting to adopt but lacking viable vendor options

*Source: [PYMNTS](https://pymnts.com/news/digital-banking/2025/60percent-banks-embrace-payment-hubs-modernize-digital-experiences) (2025)*

No vendor delivers genuinely integrated, affordable, cloud-native payments infrastructure combined with operational governance for mid-market banks.

---

## 6. Target Universe

The following institutions have publicly signaled payments infrastructure modernization activity. They are organized by geography, tier, and the nature of the signal.

### United States

| Institution | Tier | Signal | Source |
|---|---|---|---|
| JPMorgan Chase | 1 | FedNow participant; $20B tech budget 2026 | [FRB Services](https://www.frbservices.org/financial-services/fednow/organizations); [PYMNTS](https://www.pymnts.com/news/banking/2026/jpmorgans-20-billion-tech-bet-could-shrink-fintechs-innovation-edge/) |
| U.S. Bank | 1 | FedNow instant payments strategy | [FRB Services](https://www.frbservices.org/financial-services/fednow/organizations) |
| PNC Bank | 1 | FedNow real-time payments expansion | [FRB Services](https://www.frbservices.org/financial-services/fednow/organizations) |
| Wells Fargo | 1 | FedNow Industry Voices participant | [FRB Services](https://www.frbservices.org/financial-services/fednow/organizations) |
| KeyBank | 2 | KeyVAM virtual accounts, payments modernization | KeyBank press releases, 2025 |
| Regions Financial | 2 | CashFlowIQ real-time treasury, Visa Commercial Pay, Koxa partnership | Regions Financial press releases, 2025 |
| M&T Bank | 2 | RTP adoption, digital wallet integration | M&T Bank investor presentations, 2025 |
| Citizens Financial | 2 | Payee Select payments platform, RTP adoption | Citizens Financial press releases, 2025 |
| Cross River | 2 | FedNow Industry Voices — BaaS payments | [FRB Services](https://www.frbservices.org/financial-services/fednow/organizations) |
| 1st Source Bank | 3 | FedNow early adopter | [FRB Services](https://www.frbservices.org/financial-services/fednow/organizations) |
| Metropolitan Commercial Bank | 3 | Payment hub go-live (Finzly) | Finzly press release, 2024 |
| Vantage Bank | 3 | Payment hub go-live (Finzly) | Finzly press release, 2024 |
| Berkshire Bank | 3 | Payment hub modernization (Finastra) | Finastra press release, 2024 |

### India

| Institution | Tier | Signal | Source |
|---|---|---|---|
| Axis Bank | 1 | No. 1 UPI Payer PSP (30.87%), largest merchant acquirer | NPCI reports, Oct 2024 |
| Kotak Mahindra Bank | 1 | Rebuilt real-time stack on AWS for UPI scale; p95 latency 600ms→30ms | [AWS Case Study](https://aws.amazon.com/solutions/case-studies/kotak-mahindra-bank/) |
| SBI Card | 1 | RuPay Credit Card on UPI with NPCI | [SBI Card](https://www.sbicard.com/en/personal/rupay-credit-card-on-upi.page) |
| IndusInd Bank | 2 | RuPay Credit Card on UPI go-live | IndusInd Bank, Nov 2023 |
| Federal Bank | 2 | RuPay Wave Credit Card (UPI-enabled) launch | Federal Bank, Jun 2024 |
| Yes Bank | 2 | Paytm PSP partnership, 55.3% Payee PSP share | NPCI/Yes Bank, Mar 2024 |

### UK / Europe

| Institution | Tier | Signal | Source |
|---|---|---|---|
| Nationwide | 1 | 91.5% of Faster Payments migrated to new infrastructure (Form3 + Accenture) | Form3/Nationwide, 2025 |
| NatWest | 1 | ISO 20022 adoption, Bankline Direct APIs for payments | NatWest, 2025 |
| Deutsche Bank | 1 | 97% ISO 20022 readiness | Deutsche Bank, 2025 |
| ING | 1 | Wero/EPI instant payments participant | EPI/ING, 2025 |
| Commerzbank | 1 | Instant payments volume doubling | Commerzbank, 2025 |

### Brazil

| Institution | Tier | Signal | Source |
|---|---|---|---|
| Banco do Brasil | 1 | 25% of PIX volume, 93% digital; first PIX API commercial deals | [Banco do Brasil IR](https://ri.bb.com.br/en/), 2024 |
| Itaú Unibanco | 1 | Open Finance APIs via developer portal | [Itaú Developer](https://developer.itau.com.br/), 2024 |
| Santander Brasil | 1 | Open Finance and PIX APIs via developer portal | [Santander Developer](https://developer.santander.com.br/), 2024 |

---

# PART II — THE ADVISORY

---

## 7. Zeta's Position

Zeta's existing payments assets (Photon product lines) map to the structural shifts identified in Part I — but not equally to all.

| Structural Shift | Zeta Asset | Readiness |
|---|---|---|
| Real-time payments | Photon Payments Hub | **Partial** — covers UPI, IMPS, NEFT, RTGS, card networks. FedNow and RTP connectivity not confirmed. Multi-rail orchestration capability needs validation against Volante and ACI |
| Tokenization | Photon Tokenization | **Strong** — dedicated product line for token lifecycle, provisioning, de-tokenization |
| Card issuance modernization | Photon Card Management | **Strong** — card lifecycle, PIN management, card-level controls. Direct competitor to Marqeta, i2c for mid-market |
| Acquiring diversification | Photon Acquiring | **Strong** — POS, QR, online, payment facilitation, merchant management, terminal management |
| Private payment networks | Photon Payment Network | **Strong** — private-labeled instruments, proprietary rails, clearing, settlement, disputes |
| AI in payments operations | Evolution Fabric (Hub + Seer) | **Differentiated** — no competitor combines payments infrastructure with an explicit operational model and AI agent governance. This is the unique positioning |
| Cross-border | Photon Payments Hub | **Weak** — limited rail coverage for cross-border. No ISO 20022 migration tooling. No FX-as-a-service |
| Regulatory infrastructure | Across Photon | **Varies by market** — India regulatory compliance is strong. US and EU regulatory readiness needs assessment |
| Embedded payments/BaaS | Photon + Cloud Fabric | **Architectural advantage** — cloud-native, multi-tenant by design. But no BaaS-specific product packaging or regulatory wrapper |

### The differentiator hypothesis

If Zeta can deliver **integrated payments + operational model** — where card programs, acquiring, tokenization, and payment operations are governed through explicit domain models (Hubs, Streams, Loops, Scenarios) with AI agent participation (Seer) — this is a positioning that no competitor occupies.

- Legacy vendors (FIS, Fiserv) offer payments processing. They do not offer an operational substrate.
- Modern challengers (Marqeta, Stripe) offer APIs. They do not offer domain modeling or AI governance.
- Hub specialists (Volante, ACI) offer payment orchestration. They do not offer card issuance, acquiring, or an integrated operational model.

The bet: that banks need not just a payments platform, but an **operational layer for their payments domain** — making work explicit, governed, and AI-ready. Evolution Fabric is that layer.

This hypothesis is untested in the market. No bank has validated this positioning. It is a product thesis, not a market proof point.

---

## 8. Where to Play — Right to Play / Right to Win Assessment

Using the [Right to Play / Right to Win framework](../distillation/how-to.md):

| Segment | Right to Play | Right to Win | Recommendation |
|---|---|---|---|
| **Card issuance + tokenization (Tier 2 US)** | **Strong.** $6B market, 19% CAGR. Network mandates create non-discretionary buying events. Mid-market gap is clear | **Medium.** Photon Card Management and Tokenization are strong product lines. But: no US bank references, no brand recognition in the US market. Must prove capability against Marqeta and i2c | **Pursue.** Lead with tokenization mandates as urgency driver. Card issuance as the platform sale |
| **Card issuance + tokenization (India)** | **Strong.** RBI tokenization mandate April 2026. Card-on-file tokenization already drove 50% fraud reduction | **Strong.** Established bank relationships. Existing regulatory compliance. Home market advantage | **Pursue aggressively.** This is Zeta's strongest combined position |
| **Acquiring (Tier 2 US)** | **Medium.** $25-28B market, but highly competitive. ISV-embedded channel growing fast but complex | **Weak.** No US acquiring references. No merchant onboarding track record. Competing against Fiserv (Clover), Stripe, Square, Adyen | **Delay.** Build capability and references in India first. Enter US when product is proven and differentiated |
| **Private payment networks** | **Medium.** Emerging category. 45% of US retailers have closed-loop cards. Interchange caps through 2030 accelerating interest | **Medium.** Photon Payment Network is a differentiated product line. But: market demand is nascent, sales cycles are enterprise-grade | **Selective pursuit.** Target opportunities where the customer brings the use case. Do not invest in demand generation for this category yet |
| **Payment hub orchestration (Tier 1)** | **Strong.** Large market. 87% of FIs plan modernization | **Weak.** Volante is the Gartner Leader. ACI has incumbency. Tier 1 banks will not adopt from an unproven vendor. No reference customers | **Do not pursue as primary.** Consider partnership with hub vendors rather than head-on competition |
| **Cross-border / ISO 20022** | **Weak.** Specialist domain. Limited Photon rail coverage. No FX capability | **Weak.** Volante, ACI, Finastra own this space. SWIFT connectivity is table stakes. No corridor advantage | **Do not pursue.** This is a distraction from stronger opportunities |
| **AI in payments operations** | **Strong.** 98% of orgs use AI in fraud/AML. $98.5M average annual losses from payment inefficiencies. Banks trailing PayTechs in GenAI adoption | **Strong.** Evolution Fabric + Seer is a structural differentiator. No competitor combines payments infrastructure with operational AI governance | **Pursue as long-term differentiator.** This is not the entry sale — it is the expansion sale after establishing the payments platform relationship |
| **Embedded payments / BaaS (Tier 2 US)** | **Strong.** 80%+ of $185B TAM unpenetrated. Regulatory tightening favors bank partners | **Medium.** Cloud-native, multi-tenant architecture is an advantage. But: no BaaS product packaging, no regulatory wrapper, no US bank references | **Build toward.** Develop BaaS-specific packaging. Position after establishing card issuance and acquiring references |

---

## 9. Risks and Gaps

### What must be true for the US payments opportunity to work

1. **Photon must have verified FedNow and RTP connectivity** or a credible roadmap. Without real-time rail connectivity, Zeta cannot participate in the dominant structural shift in US payments.
2. **Zeta must acquire 2-3 US bank reference customers** within 18 months. No mid-market bank will adopt payments infrastructure from a vendor without US references. India references do not transfer.
3. **Pricing must be demonstrably lower than FIS/Fiserv** for comparable capability. The mid-market gap exists because incumbents are too expensive. Zeta must be affordable, not just modern.
4. **US regulatory compliance must be validated.** Card network certifications, PCI-DSS, FedNow certification, state-level money transmitter requirements — each has timelines and costs.

### Honest gaps in Zeta's position

- **No US bank customers.** This is the most significant gap. Every other assessment is conditional on closing this.
- **Brand recognition: zero** in the US payments market. Building brand awareness will require analyst engagement (Celent, Aite-Novarica/Datos Insights), conference presence, and thought leadership.
- **Cross-border is not a viable play.** Photon's rail coverage is insufficient. Do not present it as a capability in early sales engagements.
- **Payment hub orchestration: Zeta is not competitive** against Volante (Gartner Leader) or ACI (Connetic) for pure payment hub modernization. Position as integrated payments platform, not as a hub alternative.

### Competitive retaliation risk

- FIS post-TSYS will aggressively defend its mid-market issuer processor base. The integration may take 18-24 months — this is the window.
- Fiserv's Clover is expanding from SMB into mid-market acquiring. Fiserv has existing bank relationships that create switching cost barriers.
- Marqeta is pivoting from fintech-only to bank-direct sales. If Marqeta successfully establishes bank references, it narrows the competitive gap.

---

## 10. Recommended Actions

### Near-term (0-2 years)

| Action | Rationale | Priority |
|---|---|---|
| **Lead with card issuance + tokenization in India** | Strongest R2P + R2W. RBI tokenization mandate creates urgency. Existing relationships. Fastest path to revenue | **Immediate** |
| **Secure 2-3 US Tier 2 bank pilots for card issuance** | US market entry requires references. Target banks actively evaluating post-FIS-TSYS: banks that need alternatives to the consolidated FIS issuer processor | **Immediate** |
| **Engage Celent and Datos Insights for analyst coverage** | Mid-market banks rely on analyst recommendations. Without coverage, Zeta is invisible to the buyer | **Q2 2026** |
| **Validate FedNow and RTP connectivity** | Real-time payments is the dominant structural shift. Without this, half the opportunity is inaccessible | **Q2 2026** |
| **Package Photon Acquiring for India mid-market** | ISV-embedded acquiring growing 36% YoY. India's acquiring market is less competitive than the US. Build reference base here first | **2026-2027** |
| **Develop US regulatory compliance roadmap** | Card network certifications, PCI-DSS, FedNow certification. Map requirements, timelines, and costs | **2026** |

### Medium-term (2-5 years)

| Action | Rationale | Priority |
|---|---|---|
| **Enter US acquiring for Tier 2 banks** once India references are established | Acquiring diversification is a $25-28B market. Mid-market banks need affordable multi-channel capability. But Zeta must arrive with proven product and references | **2028** |
| **Launch Evolution Fabric positioning for payments domains** | The "integrated payments + operational model" hypothesis is the long-term differentiator. Introduce after the payments platform relationship is established — as an expansion, not the entry sale | **2027-2028** |
| **Evaluate UK/Europe entry** if regulatory licensing is feasible | 80% of European banks modernizing card platforms. PSD3 and EU instant payments mandates create demand. But entry requires regulatory licensing and local presence | **2028-2029** |
| **Evaluate Brazil market entry** | Fastest-growing major payments market. PIX dominance creates opportunities in credit-on-PIX, acquiring diversification, and private networks. Requires understanding of BCB regulatory framework | **2029+** |

### What to defer or avoid

| Decision | Rationale |
|---|---|
| **Do not pursue Tier 1 US banks** as primary segment | Relationship-intensive, 18-36 month sales cycles, deep customization, and these banks build strategically. Zeta lacks the brand, references, and sales infrastructure |
| **Do not pursue cross-border / ISO 20022** as a product area | Specialist domain. Volante, ACI, Finastra are entrenched. Photon's rail coverage is insufficient. This is a distraction |
| **Do not pursue payment hub orchestration** head-on | Volante is the Gartner Leader. ACI has incumbency. Compete on integrated payments platform — issuing + acquiring + tokenization + private networks — not on orchestration alone |
| **Do not invest in demand generation for private payment networks** | The category is emerging. Let the market come to Zeta through enterprise inquiry. Invest when 3+ inbound opportunities demonstrate real demand |

---

## Key Differences: Payments vs. Other Engagement Areas

| Dimension | Payments | Digital Identity & Trust | Cloud & Platform Ops | Agentic Banking | Agentic Operations |
|---|---|---|---|---|---|
| Market structure | Oligopoly (FIS, Fiserv, GP) + fragmented challengers | Fragmented IAM vendors | Hyperscalers + observability tools | Nascent; no dominant vendor | Emerging; workflow + AI vendors |
| Competitive intensity | Very high | Medium | High (hyperscaler adjacency) | Low (new category) | Medium |
| Regulatory forcing | Very strong (multiple concurrent mandates) | Strong (GDPR, PSD2/3, DPDP) | Medium | Weak | Medium (audit/compliance) |
| Geographic concentration | USA 30-40% of global spend | Distributed | Distributed | USA-first | Distributed |
| Central strategic argument | Banks must replace infrastructure they have been layering for 20 years. The technology debt is structural. | Identity is fragmenting across human/AI/partner boundaries | Cloud operations lack customer-centric observability | AI agents need an operational model to participate in banking | Back-office operations need AI-native modernization |
| Vendor-addressable TAM | $60-85B (narrow); $150-200B (broad) | $15-25B (IAM/IGA) | $10-15B | <$5B (nascent) | $5-10B |

---

## Research Sources and Citation Index

This analysis draws on data from 50+ sources. All cited URLs were verified as of March 2026. Detailed research files with full data tables are retained in `_research/payments/`.

**Primary institutional sources:** [Federal Reserve FedNow](https://www.frbservices.org/financial-services/fednow); [RBI](https://rbi.org.in/); [ECB](https://www.ecb.europa.eu/); [SWIFT](https://www.swift.com/); [Banco Central do Brasil](https://www.bcb.gov.br/); [The Clearing House](https://www.theclearinghouse.org/); [NPCI](https://www.npci.org.in/); [Pay.UK](https://www.wearepay.uk/)

**Industry reports (may be paywalled):** McKinsey Global Payments Report 2025; BCG Global Payments 2025; Capgemini World Payments Report 2026; Nilson Report 2025-2026; Juniper Research; Gartner

**Market research:** [Grand View Research](https://grandviewresearch.com/); [Mordor Intelligence](https://www.mordorintelligence.com/); [ResearchAndMarkets](https://www.researchandmarkets.com/); [MarketIntelo](https://marketintelo.com/)

**Vendor financials:** [FIS](https://www.fisglobal.com/); [Fiserv](https://investors.fiserv.com/); [Marqeta](https://www.nasdaq.com/press-release/marqeta-reports-fourth-quarter-and-full-year-2025-financial-results-2026-02-24); [Adyen](https://www.adyen.com/press-and-media/adyen-publishes-h2-2025-financial-results-3pgu2); [SoFi](https://investors.sofi.com/)

**Industry media:** [PYMNTS](https://www.pymnts.com/); [Digital Transactions](https://www.digitaltransactions.net/); Payments Dive; [G1 Economia](https://g1.globo.com/economia/); [MediaNama](https://www.medianama.com/)
