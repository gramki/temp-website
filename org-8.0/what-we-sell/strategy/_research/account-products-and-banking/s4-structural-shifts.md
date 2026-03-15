# S4: Structural Shifts and Core Modernization Activity

**Research date:** March 2026
**Engagement area:** Account Products and Core Banking
**Stream:** 4 — Structural Shifts

---

## Shift 1: Progressive Core Replacement Displacing Big-Bang Migration

### Evidence Table

| # | Data Point | Value | Source | URL | Verified | Bank Tier Impact | Geography |
|---|-----------|-------|--------|-----|----------|-----------------|-----------|
| 1 | BancoEstado phased migration: 14M customers migrated to Mambu over 5 years (Jul 2020–Jun 2025), parallel processing, no customer disruption | 14M customers; 11M accounts by Dec 2024 | Celent 2025 Model Bank Award | https://celent.com/en/insights/banco-estado-moving-from-mainframe-to-next-gen-core | Yes | Tier 1 (largest Chilean bank by customers) | LATAM (Chile) |
| 2 | Oliver Wyman: phased/co-existence approaches "typically optimal over big-bang cutover"; recommends active/active configurations mirroring requests on both cores until stability | Strategy recommendation | Oliver Wyman May 2025 | https://oliverwyman.com/our-expertise/insights/2025/may/next-gen-core-banking-modernization.html | Yes | All tiers | Global |
| 3 | TSB Bank big-bang migration failure: £318M direct costs, £247M remediation, £48.65M regulatory fines, 1.9M customers locked out, 1,300 fraud victims, CEO resignation | ~£614M total cost of failure | Celent, IT Pro, IceDQ case study | https://icedq.com/resources/case-studies/tsb-bank-data-migration-failure | Yes | Tier 2 | UK |
| 4 | CB RADAR: 113 global core banking transformation projects tracked (2021–2025); 72.5% reported complete/live but "executive optimism often masks overruns and compromises" | 113 projects; 72.5% live | Core System Partners CB RADAR 2025 | https://coresystempartners.com/resources/core-banking-market-intelligence-report-2025/ | Yes | All tiers | Global |
| 5 | 98% of banks planning core modernization within 3 years; legacy systems projected to cost global banks $57.1B annually by 2028 | 98% planning; $57.1B/yr by 2028 | mobileLIVE / Accenture | https://www.mobilelive.ai/blog/the-core-banking-modernization-dilemma-incremental-vs-full-system-upgrade | Yes | All tiers | Global |
| 6 | Marginalen Bank (Sweden): completed full migration to Mambu in 13 months on Azure Cloud | 13-month migration | Mambu press release Jun 2025 | https://mambu.com/insights/press/mambu-and-avenga-marginalen-bank-cloud-migration | Yes | Tier 3 | Europe (Sweden) |

### Regulatory Citations
- No direct regulation mandates progressive migration, but regulatory scrutiny of operational risk during migrations (PRA operational resilience, OCC third-party risk guidance) creates strong incentive for phased approaches
- TSB post-mortem led to PRA/FCA enhanced scrutiny of migration governance

### Competitive Activity
- **Mambu**: positioning as progressive migration enabler (BancoEstado, Marginalen Bank)
- **Thought Machine**: parallel-run capability with legacy cores
- **System integrators** (Deloitte, Accenture, Oliver Wyman): building progressive migration methodologies as service offerings

### Bank Tier Analysis
- **Tier 1**: Progressive migration is the only viable strategy (too large for big-bang); BancoEstado, Lloyds exemplify multi-year phased approaches
- **Tier 2**: Mixed — some attempt big-bang (TSB failure is cautionary tale); trend strongly toward phased
- **Tier 3**: Can still do faster full replacements due to smaller scale (Marginalen Bank: 13 months)

### Evidence Quality: **Strong** (6 independent data points, including a well-documented failure case)

---

## Shift 2: Composable Banking Architecture Replacing Monolithic Cores

### Evidence Table

| # | Data Point | Value | Source | URL | Verified | Bank Tier Impact | Geography |
|---|-----------|-------|--------|-----|----------|-----------------|-----------|
| 1 | Gartner identifies 4 composable banking principles: speed, agility through modularity, better orchestration, resilience through automation; advocates API-enabled PBCs over monolithic cores | Framework endorsement | Gartner via ebankit blog | https://blog.ebankit.com/blog-press/adopt-gartner-4-composable-banking-principles-to-innovate-faster | Yes | All tiers | Global |
| 2 | Temenos #1 in IBSi Sales League Table for 20th consecutive year; 950+ core banking clients, 600+ digital clients across 150+ countries | 950+ core clients | IBSi SLT 2025 / Temenos | https://temenos.com/resource/ibs-intelligence-2025 | Yes | All tiers | Global |
| 3 | Thought Machine Vault Core in production at Standard Chartered (Mox), Lloyds, Intesa Sanpaolo (isybank), Shawbrook, ING Bank Śląski, Judo Bank, Mascoma Bank | 7+ named production clients | Thought Machine case studies | https://www.thoughtmachine.net/case-studies | Yes | Tier 1–3 | Global |
| 4 | 10x Banking: Chase UK, Westpac institutional, West Brom Building Society, Co-operative Bank NZ; processes 1B+ real-time transactions annually, 99.99% uptime | 4+ named clients; 1B+ txns/yr | 10x Banking announcements | https://www.10xbanking.com/news/west-brom-building-society-announces-major-digital-transformation-with-deloitte-and-10x-banking | Yes | Tier 1–2 | UK, Australia, NZ |
| 5 | Mambu: Leeds Building Society (£30B AUM), BancoEstado, Marginalen Bank, Chetwood Bank, Innovation Norway | 5+ named established clients | Mambu customer pages | https://mambu.com/en/customer/leeds-building-society | Yes | Tier 2–3 | UK, LATAM, Europe |
| 6 | IBSi 2025: 2,100+ deals submitted by 60+ vendors; 1,429 passed evaluation across 20+ system categories — market is highly fragmented, top 3 vendors hold only 30.1% | Fragmented vendor market | IBS Intelligence SLT 2025 | https://ibsintelligence.com/ibs-intelligence-unveils-the-results-of-its-prestigious-sales-league-table-2025/ | Yes | All tiers | Global |

### Regulatory Citations
- No direct regulatory mandate for composable architecture, but open banking regulations (PSD2/PSD3, Section 1033) create API-first requirements that favor modular architectures
- PRA operational resilience rules reward modular component-level resilience testing

### Competitive Activity
- **Thought Machine**: dominant next-gen vendor for Tier 1 banks (Lloyds, Standard Chartered, JPMorgan)
- **10x Banking**: winning Tier 1 institutional banking (Westpac, Chase UK)
- **Mambu**: strong in Tier 2–3 and building societies
- **Temenos**: incumbent leader defending with SaaS and cloud-native evolution
- **FIS (Finxact)**: leading by deal count (13 implementations per CB RADAR) but limited public detail on Finxact specifically

### Bank Tier Analysis
- **Tier 1**: Composable is production-proven — Lloyds, Standard Chartered, Intesa Sanpaolo, JPMorgan, Westpac all running next-gen cores (though often for specific product lines or digital subsidiaries, NOT full core replacement)
- **Tier 2**: Active adoption — Shawbrook, ING Bank Śląski, Leeds Building Society, West Brom
- **Tier 3**: Community banks entering — Mascoma Bank on Thought Machine; community bank core modernization is emerging but early

### Geographic Variation
- **UK**: Most active market — Lloyds, Shawbrook, Leeds, West Brom, Chase UK
- **Europe**: ING (Poland), Intesa (Italy), Marginalen (Sweden), BPER Luxembourg
- **APAC**: Westpac (Australia), Judo Bank (Australia), Mox/Standard Chartered (Hong Kong), Co-op Bank (NZ)
- **USA**: 48.7% of CB RADAR transformations; Mascoma Bank, JPMorgan (Thought Machine for US retail core)
- **India**: HDFC Bank building new engineered core platform; Axis Bank launched "open" digital entity

### Evidence Quality: **Strong** (6+ independent data points with named bank deployments)

---

## Shift 3: Cloud-Native Core Infrastructure Becoming Table Stakes

### Evidence Table

| # | Data Point | Value | Source | URL | Verified | Bank Tier Impact | Geography |
|---|-----------|-------|--------|-----|----------|-----------------|-----------|
| 1 | SaaS-based core banking software market: $12.12B (2025) → $50.62B (2033), CAGR 19.6%; US market: $4.17B (2025) → $17.26B (2033) | $12.12B → $50.62B | SNS Insider via GlobeNewsWire Jan 2026 | https://www.globenewswire.com/news-release/2026/01/07/3214621/0/en/SaaS-Based-Core-Banking-Software-Market-to-Reach-USD-50-62-Billion-by-2033-Owing-to-Banking-Digital-Transformation-and-Cloud-Based-Modernization-SNS-Insider.html | Yes | All tiers | Global |
| 2 | CB RADAR: 84.5% cloud adoption rate across 113 tracked core banking transformation projects | 84.5% cloud adoption | Core System Partners 2025 | https://coresystempartners.com/resources/core-banking-market-intelligence-report-2025/ | Yes | All tiers | Global |
| 3 | EY UK: 92% of FIs have commenced core banking modernization; 83% choosing Gen 2 cores; 50% aim to complete within 3–5 years | 92% commenced; 83% Gen 2 | EY UK Oct 2025 | https://www.ey.com/content/dam/ey-unified-site/ey-com/en-uk/industries/banking-capital-markets/documents/ey-uk-core-banking-technology-modernisation-10-2025.pdf | Yes | All tiers | UK |
| 4 | Deutsche Bank: migrated 260 applications to Google Cloud; consolidated 12M Postbank customers onto cloud-native platform using Google Spanner | 260 apps; 12M customers | Google Cloud Blog | https://cloud.google.com/blog/products/databases/deutsche-bank-scales-online-banking-platform-with-spanner | Yes | Tier 1 | Europe (Germany) |
| 5 | JPMorgan: runs 70% of data on cloud infrastructure | 70% on cloud | WebProNews / industry reports | https://www.webpronews.com/banks-face-57b-legacy-system-costs-modernize-for-ai-edge/ | Yes | Tier 1 | USA |
| 6 | PRA: recognizes 40–90% of banks' workloads globally could move to public cloud or SaaS within a decade; mandates risk-based data location approach | 40–90% projected cloud | PRA SS2/21 via TechUK | https://www.techuk.org/resource/banking-on-resilience-how-to-meet-the-pra-regulations-when-outsourcing-it.html | Yes | All tiers | UK |

### Regulatory Citations
- **OCC (USA)**: Interagency Third-Party Risk Management Guidance (Jun 2023) + community bank guide (May 2024). RFI on core provider engagement issued 2025. Cloud permitted but banks retain full accountability. URL: https://www.occ.gov/news-issuances/news-releases/2024/nr-ia-2024-46.html
- **RBI (India)**: Master Direction on Outsourcing of IT Services (Apr 2023) mandates India data residency for core banking/payment data. RBI launching own cloud pilot in 2025. Managing Risks in Outsourcing Directions 2025 issued. URL: https://economictimes.indiatimes.com/tech/technology/rbi-plans-2025-launch-of-cloud-services-countering-dominance-of-global-firms/articleshow/115405872.cms
- **PRA (UK)**: SS2/21 (Outsourcing and Third Party Risk Management) operational resilience deadline passed Mar 31, 2025 — firms must now demonstrate continuous resilience, not merely document compliance. URL: https://www.prarulebook.co.uk/guidance/supervisory-statements/ss02-21-outsourcing-and-third-party-risk-management/1-introduction/19-01-2025

### Bank Tier Analysis
- **Tier 1**: Cloud-native is already the strategic direction (JPMorgan, Deutsche Bank, Wells Fargo multi-cloud). These banks are building cloud-first but migration is multi-year
- **Tier 2**: Active cloud migration; building societies and specialist banks increasingly cloud-first (Shawbrook, Leeds, West Brom all deploying cloud-native cores)
- **Tier 3**: Dependent on vendor cloud readiness; community banks exploring (Mascoma Bank) but OCC RFI signals regulatory concern about core provider lock-in

### Evidence Quality: **Strong** (6 independent data points including regulatory frameworks)

---

## Shift 4: Business Banking Digitization Creating a Separate Modernization Wave

### Evidence Table

| # | Data Point | Value | Source | URL | Verified | Bank Tier Impact | Geography |
|---|-----------|-------|--------|-----|----------|-----------------|-----------|
| 1 | MSMEs = 21% of global banking revenue pools, growing 7% annually (faster than retail or corporate); global MSME banking revenues ~$1.18T (2024) | $1.18T; 21% of revenue; 7% CAGR | McKinsey 2025 | https://www.mckinsey.com/industries/financial-services/our-insights/digital-led-with-a-human-touch-the-next-era-in-small-business-banking | Yes | All tiers | Global |
| 2 | Mercury: $3.5B valuation, $650M annualized revenue (2025), 300,000+ small businesses | $650M revenue; 300K customers | Fortune Nov 2025 | https://fortune.com/2025/11/07/exclusive-mercury-fintech-valuation-650-million-2025-annualized-revenue-immad-akhund-interview/ | Yes | Fintech challenger | USA |
| 3 | Tide: $1.5B valuation, 1.8M global members (nearly doubled in 2025), 14%+ UK SME market share, expanded to France, India surpassed 1M members | 1.8M members; 14% UK share | Tide CEO letter Dec 2025 | https://www.tide.co/blog/tide-update/major-milestones-in-2025-and-a-look-ahead-to-2026-a-letter-from-our-ceo/ | Yes | Fintech challenger | UK, India, Europe |
| 4 | Novo: 250,000+ small businesses, $12B+ lifetime transactions, $170M+ equity funding | 250K businesses | Novo website / press releases | https://www.novo.co/blog/novo-raises-90m-to-reimagine-small-businesses-checking-accounts | Yes | Fintech challenger | USA |
| 5 | Virtual account management: 86% of banks invested or planning to invest in VAM by 2025; BofA, JPMorgan, Citi, Wells Fargo have launched VAM systems; Goldman Sachs identifies VAM as pillar of next-gen transaction banking | 86% bank investment | Datos Insights via CashFac | https://cashfac.com/resource/news-blog/why-banks-are-adopting-virtual-account-management/ | Yes | Tier 1–2 | USA, Global |
| 6 | BCG: $5T+ global SMB funding gap; nearly 50% of US small businesses unable to secure desired financing | $5T+ funding gap | BCG / McKinsey | https://www.mckinsey.com/industries/financial-services/our-insights/digital-led-with-a-human-touch-the-next-era-in-small-business-banking | Yes | All tiers | Global |
| 7 | UK: digital attackers captured ~1/3 of MSME customers in just 5 years | ~33% MSME share to digital | McKinsey 2025 | https://www.mckinsey.com/industries/financial-services/our-insights/digital-led-with-a-human-touch-the-next-era-in-small-business-banking | Yes | Disruptors vs incumbents | UK |

### Regulatory Citations
- No direct regulation requiring business banking modernization, but open banking/PSD3 data sharing requirements and lending regulations drive digital SME platforms
- RBI Account Aggregator framework enables SME data-based lending in India

### Competitive Activity
- **Mercury** ($650M revenue): dominant US startup banking platform
- **Tide** (1.8M members): UK/India SME leader; entering France and Germany
- **Novo** (250K businesses): mid-market US SME challenger
- **Relay Financial**: Canada-based SME platform (smaller but growing)
- **Shawbrook on Thought Machine**: specifically deployed Vault Core for commercial SME lending
- **Incumbent response**: JPMorgan, BofA, Citi, Wells Fargo all launching VAM platforms

### Bank Tier Analysis
- **Tier 1**: Investing in VAM and digital SME platforms, but often as overlay on legacy cores
- **Tier 2**: Most exposed to fintech disruption in business banking; need modern product engines to compete
- **Tier 3**: Community banks traditionally strong in SME relationships but lack digital tooling

### Evidence Quality: **Strong** (7 independent data points with market sizing and named competitors)

---

## Shift 5: Open Banking Mandates Driving Account Infrastructure Investment

### Evidence Table

| # | Data Point | Value | Source | URL | Verified | Bank Tier Impact | Geography |
|---|-----------|-------|--------|-----|----------|-----------------|-----------|
| 1 | CFPB Section 1033: finalized Oct 2024, original April 2026 deadline for large banks, but enforcement blocked by federal judge; rule "final on the books" but faces litigation and potential revision | Delayed/uncertain | PYMNTS / National Law Review | https://www.pymnts.com/bank-regulation/2026/data-aggregators-push-secure-access-as-rule-1033-rewrite-looms/ | Yes | Tier 1–2 first | USA |
| 2 | PSD3/PSR: provisional agreement Nov 2025; PSR directly applicable upon 2026 publication; PSD3 requires 18-month national transposition; earliest application H2 2027–early 2028 | H2 2027–2028 enforcement | Norton Rose Fulbright | https://www.nortonrosefulbright.com/en/knowledge/publications/cedd39c6/psd3-and-psr-from-provisional-agreement-to-2026-readiness | Yes | All tiers | Europe |
| 3 | India Account Aggregator: 252.9M user accounts linked; 2.61B financial accounts enabled; 754 FIUs live; RBI updated NBFC-AA Directions 2025 and launched SRO framework | 252.9M users; 2.61B accounts | Dept of Financial Services India | https://financialservices.gov.in/beta/en/account-aggregator-framework | Yes | All tiers | India |
| 4 | UK CASS: 12.4M total switches since 2013; 1M+ switches in 2025; Q4 2025 busiest quarter (350,114 switches); Monzo gained 9,934 net switches in Q3 2025 | 12.4M total; 1M+ in 2025 | CASS / currentaccountswitch.co.uk | https://www.currentaccountswitch.co.uk/news-insights/switching-data/current-account-switch-service-records-over-one-million-switches-in-2025/ | Yes | All tiers | UK |
| 5 | UK switching reasons: digital functionality (47%), interest rates (38%), customer service (32%) — digital capability is #1 reason for switching | 47% digital functionality | CASS Q1 2025 Dashboard | https://www.currentaccountswitch.co.uk/news-insights/switching-data/current-account-switch-service-reports-222-805-switches-in-q1-2025/ | Yes | All tiers | UK |

### Regulatory Citations
- **Section 1033 (USA)**: Finalized Oct 2024; blocked by court; CFPB reconsideration underway. Banks must prepare API infrastructure regardless. URL: https://natlawreview.com/article/cfpb-issues-final-rule-implementing-section-1033-dodd-frank-act
- **PSD3/PSR (Europe)**: Provisional agreement Nov 2025. 2026–2027 critical window for architectural decisions. URL: https://www.nortonrosefulbright.com/en/knowledge/publications/cedd39c6/psd3-and-psr-from-provisional-agreement-to-2026-readiness
- **Account Aggregator (India)**: RBI NBFC-AA Directions 2025, SRO framework launched Mar 2025. URL: https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=59956
- **UK Open Banking**: Ongoing via CMA Order and FCA oversight; CASS infrastructure operational

### Link to Core Modernization
- Open banking API mandates expose legacy core limitations: real-time data access, consent management, and granular product APIs are difficult on monolithic cores
- Banks using progressive migration or composable architecture can satisfy API requirements incrementally
- India's AA framework (252.9M users) creates strongest data-layer demand for modern account infrastructure

### Evidence Quality: **Strong** (5 independent data points across 4 geographies with regulatory citations)

---

## Shift 6: Deposit Competition from Neobanks Forcing Product Agility

### Evidence Table

| # | Data Point | Value | Source | URL | Verified | Bank Tier Impact | Geography |
|---|-----------|-------|--------|-----|----------|-----------------|-----------|
| 1 | Neobanks capture 40% of all new US account openings, surpassing large nationwide banks (38%); US neobank customer base grew from 86M to ~150M accounts in 30 months | 40% new accounts; ~150M total | Simon-Kucher 2025 | https://www.simon-kucher.com/en/insights/neobanking-united-states-acceleration-amid-uneven-ground | Yes | All tiers | USA |
| 2 | 28% of US customers consider a neobank their primary banking relationship; rises to ~33% among ages 30–39 | 28% primary relationship | Simon-Kucher 2025 | https://www.simon-kucher.com/en/insights/neobanking-united-states-acceleration-amid-uneven-ground | Yes | All tiers | USA |
| 3 | Chime: 12.8% of new checking accounts in Q4 2025 (ahead of Chase 8.4%, Wells Fargo 7.1%); 78% checking conversion rate, 85% savings conversion rate | 12.8% new checking share | J.D. Power / American Banker | https://www.americanbanker.com/news/chime-leads-in-new-checking-accounts-opened | Yes | Neobank vs Tier 1 | USA |
| 4 | SoFi: 13.7M members (Q4 2025, +35% YoY); record $1B quarterly revenue; offers 4.00% APY on savings | 13.7M members; $1B quarterly rev | SoFi Q4 2025 earnings | https://www.businesswire.com/news/home/20260130224251/en/ | Yes | Neobank | USA |
| 5 | Revolut: UK banking license secured; 13M UK customers; analysts estimate £10–15B deposit transfer; investing £3B in UK infrastructure | 13M UK customers; £10–15B deposits | AInvest analysis | https://www.ainvest.com/news/revolut-bank-launch-flow-analysis-deposit-capture-crypto-liquidity-shifts-2603/ | Yes | Neobank | UK |
| 6 | Starling Bank: £12.1B customer deposits; 4.6M open accounts; 4.12% net interest margin (Mar 2025) | £12.1B deposits | Starling Bank Annual Report 2025 | https://www.starlingbank.com/docs/annual-reports/Starling-Bank-Annual-Report-2025.pdf | Yes | Neobank | UK |
| 7 | "Soft switching" trend: 49% of new checking and 46% of new savings accounts are secondary accounts; fintechs benefit most among mass-market consumers | 49% soft switching | J.D. Power / CU Today | https://www.cutoday.info/Fresh-Today/Fintechs-Keep-Winning-Soft-Switchers-As-Chime-SoFi-Gain-Ground-In-Key-Account-Categories-J.D.-Power-Finds | Yes | All tiers | USA |

### Time-to-Market Comparison (Legacy vs. Modern Cores)
- Legacy banks: 4–6 months to deploy new product features (per Payara Fish / industry estimates)
- Modern core banks: 2–4 weeks (fintech competitors)
- BancoEstado on Mambu: product launches went from 6 months to weeks
- Source: https://payara.fish/blog/the-57-billion-problem-why-bankings-java-legacy-crisis-demands-immediate-action/

### Bank Tier Analysis
- **Tier 1**: Losing checking account acquisition to Chime (12.8% vs Chase's 8.4%); responding with digital feature parity and high-yield savings offers
- **Tier 2**: Most vulnerable — lack both brand strength of Tier 1 and agility of neobanks
- **Tier 3**: Community banks competing on relationship, but digital expectations rising

### Evidence Quality: **Strong** (7 independent data points with specific market share data)

---

## Shift 7: Embedded Banking (BaaS) Requiring Modern Account Infrastructure

### Evidence Table

| # | Data Point | Value | Source | URL | Verified | Bank Tier Impact | Geography |
|---|-----------|-------|--------|-----|----------|-----------------|-----------|
| 1 | Synapse collapse (Apr 2024): 100,000+ people affected; $265M+ deposits frozen; partner banks unable to retrieve accurate balance records | 100K people; $265M frozen | Yale Journal of International Affairs | https://www.yalejournal.org/publications/the-synapse-collapse | Yes | Tier 2–3 (partner banks) | USA |
| 2 | FDIC proposed "Synapse Rule": banks must ensure custodial deposit account balances are accurate and reconciled daily; proposed Oct 2024 | Daily reconciliation mandate | FDIC press release | https://www.fdic.gov/news/press-releases/2024/fdic-proposes-deposit-insurance-recordkeeping-rule-banks-third-party | Yes | All BaaS banks | USA |
| 3 | Federal Reserve cease-and-desist against Evolve Bank (Jun 2024): cannot establish new fintech partners without Fed approval; deficiencies in AML, risk management, consumer compliance | Cease-and-desist order | Federal Reserve | https://www.federalreserve.gov/newsevents/pressreleases/enforcement20240614a.htm | Yes | Tier 3 (Evolve) | USA |
| 4 | BaaS market size: $21.4B (2025) → $74.55B (2030) → $105.8B (2035), CAGR 14.1–16.4% | $21.4B → $105.8B | Grand View Research / MAK Data Insights | https://grandviewresearch.com/industry-analysis/banking-as-a-service-market-report | Yes | All tiers | Global |
| 5 | Westpac BaaS: launched BaaS platform in 18 months with 10x Banking and AWS | 18-month launch | 10x Banking | https://www.10xbanking.com/banking-as-a-service | Yes | Tier 1 | Australia |

### Regulatory Citations
- **FDIC "Synapse Rule"** (proposed Oct 2024): custodial deposit recordkeeping and daily reconciliation. URL: https://www.federalregister.gov/documents/2024/10/02/2024-22565/recordkeeping-for-custodial-accounts
- **Fed Evolve Bank C&D** (Jun 2024): cease-and-desist for AML and third-party risk management failures. URL: https://www.federalreserve.gov/newsevents/pressreleases/enforcement20240614a.htm
- **OCC Third-Party Risk Management Guide** (May 2024): banks retain full responsibility regardless of third-party arrangements. URL: https://www.occ.gov/news-issuances/news-releases/2024/nr-ia-2024-46.html

### Shift from Middleware to Modern Core
- Synapse operated as middleware between fintechs and banks — collapse proves middleware-only model is fatally flawed
- Post-Synapse: banks demand direct API access to fintech ledgers; fintech partners face enhanced vetting
- Modern BaaS requires banks to own the core ledger on a real-time, cloud-native platform rather than delegating to middleware
- Westpac's 10x-powered BaaS is the Tier 1 model: bank-owned modern core enabling embedded distribution

### Bank Tier Analysis
- **Tier 1**: Selectively entering BaaS (Westpac, Goldman Sachs/Marcus platform); modern core is prerequisite
- **Tier 2**: Some positioned as BaaS providers (Cross River identified as key player); regulatory scrutiny increasing
- **Tier 3**: Most exposed — Evolve Bank and similar small banks face existential regulatory risk from BaaS partnerships without adequate infrastructure

### Evidence Quality: **Strong** (5 independent data points with regulatory enforcement actions)

---

## Shift 8: AI in Account Operations Beyond Origination

### Evidence Table

| # | Data Point | Value | Source | URL | Verified | Bank Tier Impact | Geography |
|---|-----------|-------|--------|-----|----------|-----------------|-----------|
| 1 | Synthetic identity fraud: $3.3B exposure in H1 2025 (US auto loans, credit cards, personal loans); $35B in losses crossed in 2023; new account fraud hit $6.2B in 2024, doubling from a decade ago | $3.3B/H1; $6.2B new account fraud | Bank Info Security / Federal Reserve | https://www.bankinfosecurity.com/ai-tools-synthetic-ids-are-fracturing-kyc-programs-a-30401 | Yes | All tiers | USA |
| 2 | Federal Reserve: GenAI is accelerating synthetic identity fraud; traditional KYC (name/DOB/SSN verification) is fracturing; industry transitioning to "perpetual KYC" (pKYC) using AI for continuous monitoring | pKYC transition underway | Fed Reserve Boston / Projective Group | https://www.bostonfed.org/news-and-events/news/2025/04/synthetic-identity-fraud-financial-fraud-expanding-because-of-generative-artificial-intelligence.aspx | Yes | All tiers | USA |
| 3 | AI fraud detection: reduces false positives by 40–60% (some systems 70%); institutions using AI for synthetic identity detection report 30%+ reduction in fraud losses; agentic AI systems complete investigations in <50ms | 40–60% false positive reduction | FluxForce AI / xLoopDigital | https://www.fluxforce.ai/blog/synthetic-identity-crime-detection-strategy | Yes | All tiers | Global |
| 4 | CIBC CRTeX: AI-enabled client personalization engine launched Oct 2025 combining client preferences with near real-time decision-making for omni-channel engagement | Production launch | CIBC press release | https://www.newswire.ca/news-releases/cibc-launches-cibc-crtex-tm-an-ai-enabled-client-personalization-amp-engagement-engine-to-further-its-industry-leading-digital-capabilities-and-enhance-client-experiences-890473929.html | Yes | Tier 1 | Canada |
| 5 | Cotribute Agentic AI Growth Agents (Jun 2025): AI Acquisition Agent, AI Cross-Sell Agent, AI Relationship Growth Agent — for banks and credit unions | Vendor launch | Cotribute via BusinessWire | https://www.businesswire.com/news/home/20250602072436/en/ | Yes | Tier 2–3 | USA |
| 6 | Kasisto KAIgentic (Aug 2025): agentic AI platform purpose-built for banking account servicing | Vendor launch | Kasisto via BusinessWire | https://www.businesswire.com/news/home/20250820775883/en/ | Yes | All tiers | USA |
| 7 | FlowX.AI Dormant-to-Active Spike Monitor: AI agent detecting accounts shifting from dormancy to high-velocity use inconsistent with customer profiles | Vendor product | FlowX.AI | https://www.flowx.ai/ai-agents/dormant-to-active-spike-monitor | Yes | All tiers | Global |
| 8 | Wells Fargo + Google Cloud: deploying AI agents company-wide via Google Agentspace starting with 2,000 employees; automating credit memos, financial analysis | Production deployment | Fast Company | https://www.fastcompany.com/91380316/wells-fargo-is-rolling-out-companywide-ai-it-says-everyone-from-branch-tellers-to-investment-bankers-will-benefit | Yes | Tier 1 | USA |

### NOTE: Thinner Analyst Coverage
- McKinsey/Gartner/Celent have limited published research specifically on AI in account lifecycle (most AI banking research focuses on lending origination, fraud detection at payment level, or conversational AI)
- Evidence above leans on vendor announcements and specific bank deployments rather than analyst frameworks
- The Federal Reserve synthetic identity fraud research provides the strongest institutional source
- CIBC and Wells Fargo provide Tier 1 production evidence

### Bank Tier Analysis
- **Tier 1**: Leading AI deployment (CIBC CRTeX, Wells Fargo + Google, JPMorgan AI investments); resources for proprietary AI
- **Tier 2**: Adopting vendor AI solutions (Cotribute, Kasisto, Creatio); can buy rather than build
- **Tier 3**: Most dependent on vendor-embedded AI; limited in-house capability

### Evidence Quality: **Moderate-to-Strong** (8 data points, but analyst coverage is thin compared to other shifts; vendor announcements dominate vs. measured bank outcomes)

---

## Bank Modernization Signals Table

| Bank | Tier | Geography | Signal | Source | URL |
|------|------|-----------|--------|--------|-----|
| Lloyds Banking Group | 1 | UK | Acquired additional £10M stake in Thought Machine (Mar 2025); Vault Core in production; core transformation is "key part of three-year strategic plan" | Thought Machine / Trading & Investment News | https://www.thoughtmachine.net/case-studies/lloyds-bank |
| JPMorgan Chase | 1 | USA/UK | Selected Thought Machine for US retail core (2021); Chase UK digital bank on 10x Banking; 70% of data on cloud; technology is primary investment driver | Finextra / multiple | https://www.finextra.com/newsarticle/38943/chase-taps-10x-for-uk-digital-bank |
| Standard Chartered | 1 | HK/Asia | Mox Bank (HK) live on Thought Machine Vault Core since 2020; 300K+ customers; live across CASA, cards, loans | Thought Machine case study | https://www.thoughtmachine.net/case-studies/mox-bank |
| Intesa Sanpaolo | 1 | Italy | isybank launched Jun 2023 on Thought Machine + Google Cloud; 300K customers migrated; targeting €800M annual cost savings from 2026 | Reuters / Thought Machine | https://www.thoughtmachine.net/case-studies/intesa-sanpaolo |
| Westpac | 1 | Australia | 10x Banking partnership for institutional platform + BaaS; technology simplification roadmap through 2028; 9-to-1 network consolidation | 10x Banking / Westpac | https://www.10xbanking.com/success-stories/10x-and-westpac-partner-to-launch-a-robust-scalable-and-flexible-transaction-banking-platform |
| Deutsche Bank | 1 | Germany | 260 apps migrated to Google Cloud; Postbank 12M customer migration to Google Spanner; SAP core banking (Project Magellan, €1B) | Google Cloud Blog | https://cloud.google.com/blog/products/databases/deutsche-bank-scales-online-banking-platform-with-spanner |
| Wells Fargo | 1 | USA | $900M+ incremental technology spend (2025); multi-cloud approach (Azure primary, Google Cloud); AI agents via Google Agentspace; 50% of new checking accounts opened digitally | InfotechLead / Fast Company | https://infotechlead.com/cio/wells-fargo-says-digital-transformation-and-technology-investments-support-customer-growth-efficiency-and-operational-performance-in-q4-2025-93120 |
| HDFC Bank | 1 | India | Core banking system migration to new engineered platform announced; multi-cloud active-active architecture; 97% digital transactions; 9.7Cr customers | HDFC Bank press release | https://www.hdfcbank.com/personal/about-us/news-room/press-release/2024/q2/hdfc-bank-plans-migration-of-core-banking-system-to-new-engineered-platform-to-enhance-robustness-a |
| Axis Bank | 1 | India | Launched "open" by Axis Bank (digital banking entity); 15M+ MAU mobile banking; 47% digital card issuance; DevSecOps and cloud infrastructure | Axis Bank Annual Report 2025 | https://www.axisbank.com/annual-reports/2024-2025/pdf/s2.pdf |
| CIBC | 1 | Canada | Launched CIBC CRTeX AI-enabled personalization engine (Oct 2025) for omni-channel engagement | CIBC press release | https://www.newswire.ca/news-releases/cibc-launches-cibc-crtex-tm-an-ai-enabled-client-personalization-amp-engagement-engine-to-further-its-industry-leading-digital-capabilities-and-enhance-client-experiences-890473929.html |
| BancoEstado | 1 | Chile | Celent 2025 Model Bank Award: migrated 14M customers to Mambu (Jul 2020–Jun 2025); targets 90% mainframe reduction by 2027 | Celent | https://celent.com/en/insights/banco-estado-moving-from-mainframe-to-next-gen-core |
| ING Bank Śląski | 2 | Poland | Live on Thought Machine Vault Core since Dec 2021; first Polish bank on cloud-native core; expanding via NextGen Architecture program | Thought Machine | https://www.thoughtmachine.net/press-releases/ing-bank-slaski-selects-thought-machine-and-goes-live-with-vault-to-further-enhance-customer-experience |
| Shawbrook | 2 | UK | Live on Thought Machine Vault Core (Aug 2025); deployed in <9 months; focused on commercial SME lending | Thought Machine | https://www.thoughtmachine.net/press-releases/shawbrook |
| Leeds Building Society | 2 | UK | Partnered with Mambu for multi-year core modernization; pilot digital savings product launched in <1 year; £30B AUM, 1M+ members | Mambu | https://mambu.com/en/customer/leeds-building-society |
| West Brom Building Society | 2 | UK | 10x Banking + Deloitte for multi-phase cloud-native core transformation (May 2025); 400K+ members | 10x Banking | https://www.10xbanking.com/news/west-brom-building-society-announces-major-digital-transformation-with-deloitte-and-10x-banking |
| Judo Bank | 2 | Australia | Full core migration to Thought Machine completed Apr 2025; 50% reduction in product development time; 4x faster system performance | Thought Machine case study | https://www.thoughtmachine.net/case-studies/judo-bank |
| Co-operative Bank | 2 | New Zealand | 10x Banking selected for full-platform migration (Aug 2025); 180K+ customers; multi-year phased approach | 10x Banking | https://www.10xbanking.com/news/the-co-operative-bank-selects-10x-banking |
| Marginalen Bank | 3 | Sweden | Completed migration to Mambu in 13 months (Jun 2025) on Azure Cloud | Mambu | https://mambu.com/insights/press/mambu-and-avenga-marginalen-bank-cloud-migration |
| Mascoma Bank | 3 | USA | Signed Thought Machine for cloud-native core migration (Jan 2022); $2.6B mutual savings bank; 28 branches | Thought Machine | https://www.thoughtmachine.net/press-releases/thought-machine-signs-mascoma-bank-to-take-community-banking-into-the-cloud |
| BPER Bank Luxembourg | 3 | Luxembourg | Selected OLYMPIC Banking System as new core banking platform for modernization | IBS Intelligence | https://ibsintelligence.com/ibsi-news/bper-bank-luxembourg-selects-olympic-as-core-banking-platform/ |
| Chetwood Bank | 3 | UK | Live on Mambu; launched savings products in 8 months; expanded to fixed-rate savings and Hargreaves Lansdown integration (2025) | Mambu | https://mambu.com/en/customer/chetwood-bank |

---

## Evidence Quality Summary

| Shift | Rating | Justification |
|-------|--------|---------------|
| 1. Progressive core replacement | **Strong** | 6 independent data points; TSB failure case; Celent Model Bank winner; Oliver Wyman methodology endorsement; CB RADAR tracking |
| 2. Composable banking architecture | **Strong** | 6+ data points; 15+ named bank deployments across 3 major vendors; IBSi market data; Gartner framework |
| 3. Cloud-native core infrastructure | **Strong** | 6 data points; market sizing; regulatory frameworks across 3 geographies; CB RADAR adoption rate |
| 4. Business banking digitization | **Strong** | 7 data points; McKinsey market sizing; named fintechs with revenue/customer data; VAM adoption data |
| 5. Open banking mandates | **Strong** | 5 data points across 4 geographies; specific regulatory citations with timelines; India AA scale data |
| 6. Deposit competition from neobanks | **Strong** | 7 data points; market share data from J.D. Power and Simon-Kucher; named neobank deposit/revenue figures |
| 7. Embedded banking (BaaS) | **Strong** | 5 data points; 2 regulatory enforcement actions; market sizing; Westpac production deployment |
| 8. AI in account operations | **Moderate-to-Strong** | 8 data points but analyst coverage is thin; vendor launches dominate; 2 Tier 1 production deployments (CIBC, Wells Fargo); Federal Reserve fraud research is authoritative |

---

## Key Findings

### Structural (high confidence)
- **Progressive migration is now the dominant strategy** for core banking modernization. The TSB failure (£614M total cost) created lasting aversion to big-bang approaches. BancoEstado's Celent Model Bank Award validates the multi-year phased approach. Oliver Wyman explicitly recommends phased/co-existence over big-bang cutover.
- **Cloud-native core is approaching table stakes**: 84.5% cloud adoption rate across 113 tracked projects (CB RADAR); 92% of UK FIs have commenced modernization (EY); market growing from $12B to $51B by 2033.
- **Neobanks are winning account acquisition**: 40% of all new US account openings go to neobanks (surpassing large banks at 38%). Chime alone captures 12.8% of new checking accounts — more than Chase or Wells Fargo individually.
- **Business banking is a distinct modernization wave**: $1.18T global revenue pool growing 7% annually; UK digital challengers captured ~33% of MSME customers in 5 years; Mercury ($650M revenue) and Tide (1.8M members) prove the fintech business banking model.

### Emerging (moderate confidence)
- **Composable banking is production-proven at Tier 1** banks — but mostly for specific product lines or digital subsidiaries (isybank, Mox Bank, Chase UK), NOT full core replacement. The question "has any established Tier 1 bank fully replaced its core with a composable platform?" remains unanswered. Lloyds is the most advanced progressive migration, but completion status is unclear.
- **BaaS is restructuring post-Synapse**: the middleware model is dead; banks must own the ledger. FDIC's proposed Synapse Rule and Fed's Evolve Bank C&D create compliance floor. Market still growing ($21B → $106B by 2035) but on different architectural foundations.
- **AI in account operations is vendor-driven**: CIBC CRTeX and Wells Fargo + Google Agentspace are the strongest Tier 1 signals. Vendor launches (Cotribute, Kasisto, Creatio, FlowX.AI) provide category evidence. Measured bank outcomes beyond fraud reduction statistics are thin.

### Regulatory tailwinds creating urgency
- **USA**: Section 1033 (delayed but directionally certain), FDIC Synapse Rule, OCC third-party RFI
- **Europe**: PSD3/PSR (enforcement begins H2 2027), PRA operational resilience (deadline passed Mar 2025)
- **India**: Account Aggregator (252.9M users), RBI cloud outsourcing directions (compliance by Apr 2026), RBI's own cloud platform pilot
- **UK**: CMA Open Banking, CASS infrastructure, PRA cloud/resilience requirements

---

## Critical Assessment: Shifts 1 and 2

### Shift 1: Progressive Core Replacement — Structural Shift or Aspirational Narrative?

**Assessment: Structural shift with strong empirical evidence, but completion data is weak.**

Evidence FOR structural shift:
- TSB's £614M failure created lasting industry-wide deterrent against big-bang approaches
- BancoEstado (14M customers, Celent-validated) demonstrates that progressive migration works at scale over 5 years
- Oliver Wyman (major consulting firm) explicitly recommends phased over big-bang
- CB RADAR tracks 113 projects — the sheer volume indicates this is a market pattern, not isolated cases

Evidence of LIMITS:
- Very few banks have COMPLETED a full progressive migration. BancoEstado is the most documented success, and it took 5 years. Most banks in CB RADAR's 72.5% "complete/live" category likely have significant scope remaining.
- "Progressive migration" can become a euphemism for indefinite coexistence — banks run new and old cores simultaneously without ever fully decommissioning legacy. This is a real architectural pattern, but it's different from completed migration.
- The strategy recommendation (Oliver Wyman, Celent) is strong, but analyst endorsement is different from field completion data.

**Verdict**: Progressive migration is the empirically dominant STRATEGY (supported by failure cases, analyst recommendations, and award-winning case studies). Whether it is a proven path to COMPLETION is less clear — the industry may be in a prolonged transition state where "progressive" means "ongoing."

### Shift 2: Composable Banking Architecture — Structural Shift or Aspirational Industry Narrative?

**Assessment: Structural shift with production evidence, but the "composable replaces monolithic" framing is partially aspirational.**

Evidence FOR structural shift:
- 15+ named bank deployments across Thought Machine, 10x, and Mambu — including Tier 1 banks (Lloyds, Standard Chartered, JPMorgan, Intesa, Westpac)
- Gartner explicitly advocates composable banking principles
- IBSi SLT 2025 shows market activity (1,429 evaluated deals across 60+ vendors)
- Specific production outcomes: Judo Bank 50% reduction in product development time; BancoEstado product launches from 6 months to weeks

Evidence of LIMITS:
- **No Tier 1 bank has fully replaced its monolithic core with a composable platform.** All major deployments are either (a) digital subsidiaries (isybank, Mox, Chase UK), (b) specific product lines (Shawbrook SME lending, Leeds savings), or (c) progressive migrations still in progress (Lloyds, BancoEstado).
- Temenos (#1 by IBSi for 20 years, 950+ clients) represents the "evolved monolith" — modular and SaaS-capable but architecturally different from the pure composable thesis. Most banks are choosing Gen 2 cores (83% per EY), not greenfield composable platforms.
- The composable thesis works well for greenfield digital banks and specific product launches. Its viability as a FULL core replacement for large, complex, multi-product banks remains unproven at scale.
- Vendor market is highly fragmented (top 3 hold only 30.1%) — this can indicate healthy competition, but also suggests no vendor has achieved the scale required for enterprise-wide Tier 1 replacement.

**Verdict**: Composable banking is a real, production-proven architectural pattern — but the strongest evidence is for *alongside* or *instead of* monolithic cores for specific use cases, not *replacing* them entirely. The narrative that composable will displace monolithic cores is partially aspirational. The more accurate characterization: banks are using composable platforms for new product lines and digital subsidiaries while maintaining (and gradually hollowing) legacy monolithic cores. Full replacement may eventually occur, but the evidence timeline suggests decades, not years.

---

## Gaps and Unresolved Questions

1. **Completion data for progressive migrations**: How many banks have FULLY decommissioned their legacy core after progressive migration? BancoEstado targets 90% mainframe reduction by 2027 — but no bank has been confirmed as 100% migrated from legacy to next-gen core using progressive approach.

2. **Composable at Tier 1 full scale**: No evidence of a Tier 1 bank running ALL account products on a composable platform. Lloyds is the most advanced candidate, but completion status and scope of Vault Core deployment are not publicly documented.

3. **India core banking modernization vendors**: HDFC Bank announced new core platform but vendor/technology not publicly disclosed. Which next-gen core vendors are gaining traction in India's Tier 1 banking market?

4. **Finxact (FIS) deployment specifics**: FIS leads CB RADAR with 13 implementations, but specific Finxact customer names and outcomes are difficult to find in public sources. FIS's overall core banking franchise mixes legacy and next-gen.

5. **Column bank BaaS model**: Column is frequently cited as a "modern BaaS bank" but limited public data on platform architecture and deployment specifics. [unverified — needs manual confirmation]

6. **AI measured outcomes**: Vendor claims (40–60% false positive reduction, <50ms investigation) need independent validation. CIBC CRTeX and Wells Fargo Agentspace are too new for published outcome data.

7. **Chime deposit data**: Despite IPO filing (May 2025), specific deposit totals and member count are not in available search results. Full S-1 review needed. [unverified — needs manual confirmation]

8. **Section 1033 final status**: Rule is "on the books" but enforcement blocked by court and CFPB reconsideration underway. Timeline highly uncertain under current administration.

9. **Cost savings validation**: Intesa claims €800M annual savings from 2026 via isybank. Deutsche Bank's Project Magellan was €1B. Are these targets being met? Independent verification of ROI claims from core modernization projects is scarce.

10. **Geographic blind spot — Middle East/Africa**: Limited research on core banking modernization activity in GCC, Sub-Saharan Africa. These regions may have distinct patterns (e.g., high mobile banking penetration in Africa, sovereign wealth-funded modernization in GCC).

---

## Raw Notes and Excerpts

### Oliver Wyman (May 2025) — 10 Key Areas for Successful Core Banking Modernization
> "Migration Strategy: Phased or co-existence approaches are typically optimal over big-bang cutover, with active/active configurations recommended to mirror requests on both cores until stability is achieved."
Source: https://oliverwyman.com/our-expertise/insights/2025/may/next-gen-core-banking-modernization.html

### Accenture — Reinventing with the Digital Core in Banking
> "73% of banking executives are accelerating innovation spending... 99% of banking executives report technology as the top lever for reinvention, with generative AI viewed as a main driver."
Source: https://www.accenture.com/gb-en/insights/banking/reinventing-digital-core-banking

### McKinsey — Digital-Led with a Human Touch (Small Business Banking)
> "MSMEs account for 21% of total global banking revenue pools and are growing at 7% annually... In the UK, new digital attackers have captured about one-third of MSME customers in just five years."
Source: https://www.mckinsey.com/industries/financial-services/our-insights/digital-led-with-a-human-touch-the-next-era-in-small-business-banking

### IBM — The Voice of the Makers (Core Banking Modernization)
> "Fewer than half of CIOs report substantial improvements in efficiency or customer experience from modernization efforts."
Source: https://www.ibm.com/thought-leadership/institute-business-value/en-us/report/core-banking-modernization-makers

### EY UK — Core Banking Technology Modernisation (Oct 2025)
> "92% of financial institutions have commenced core banking platform modernization journeys... 83% planning to choose Gen 2 cores... 50% aiming to complete modernization within three to five years."
Source: https://www.ey.com/content/dam/ey-unified-site/ey-com/en-uk/industries/banking-capital-markets/documents/ey-uk-core-banking-technology-modernisation-10-2025.pdf

### Simon-Kucher — Neobanking in the United States (2025)
> "Neobanks now account for 40% of all new account openings, surpassing large nationwide banks (38%)... Nearly 28% of US customers consider a neobank their primary banking relationship... The US neobank customer base grew from 86 million to nearly 150 million accounts in 30 months."
Source: https://www.simon-kucher.com/en/insights/neobanking-united-states-acceleration-amid-uneven-ground

### Federal Reserve Bank of Boston — Synthetic Identity Fraud (Apr 2025)
> "Generative AI is significantly accelerating synthetic identity fraud by enabling criminals to create realistic fake identities faster and at greater scale."
Source: https://www.bostonfed.org/news-and-events/news/2025/04/synthetic-identity-fraud-financial-fraud-expanding-because-of-generative-artificial-intelligence.aspx

### Core System Partners CB RADAR 2025
> "113 global core banking transformation projects tracked (2021–2025)... 84.5% cloud adoption rate... top three vendors control only 30.1%... USA accounts for 48.7% of transformations."
Source: https://coresystempartners.com/resources/core-banking-market-intelligence-report-2025/

### Cross-Reference: Payments S4 Research
From `s4-realtime-payments-hubs.md`:
- ~60% of banks have or are implementing payment hubs (overlaps with core modernization)
- 87% of FIs planning modernization investment in 2026 (Finastra State of Nation 2026)
- Metropolitan Commercial Bank, Vantage Bank, Berkshire Bank named as modernizing (limited overlap with account products core modernization signals above)
