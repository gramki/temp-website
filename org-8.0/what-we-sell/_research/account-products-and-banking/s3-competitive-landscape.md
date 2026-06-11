# S3: Competitive Landscape

**Research date:** March 2026
**Engagement area:** Account Products and Core Banking
**Cross-reference:** `org-8.0/what-we-sell/_research/payments/s3-competitive-landscape.md` (FIS/Fiserv data overlap)

---

## Competitor Profiles Table

### A. Legacy Core Banking Incumbents

| Vendor | Product(s) | Revenue (Total / Banking) | Bank Customers | Tier Focus | Geography | Architecture | Deployment | Recent Wins | Vulnerabilities | Source | URL | Verified |
|--------|-----------|---------------------------|---------------|------------|-----------|-------------|------------|-------------|-----------------|--------|-----|----------|
| FIS | HORIZON, IBS, PROFILE, Modern Banking Platform (Finxact) | $10.7B total / $7.285B Banking Solutions (FY2025) | Thousands (legacy); Finxact early-stage cloud-native | Tier 1–3 (legacy); Tier 1–2 (Modern Banking Platform) | US-dominant, global | Legacy monolithic (IBS/PROFILE); cloud-native (Finxact) | On-prem (legacy); public cloud (Finxact) | Named Leader in Gartner MQ North America 2025; acquired Global Payments Issuer Solutions (TSYS) Jan 2026 for $13.5B | Finxact still early in customer traction post-acquisition; legacy platforms aging; integration complexity across acquired portfolio | FIS 10-K FY2025; FIS press releases | https://www.fisglobal.com | No — revenue from 10-K, wins from press releases |
| Fiserv | DNA, Signature, Premier, Cleartouch | $21.2B total (FY2025); core banking segment not separately disclosed | #1 market position in US core account processing (self-reported) | Tier 2–4 (community banks, credit unions) | US-dominant | Monolithic (Signature, Premier); modular (DNA) | On-prem; private cloud (some DNA deployments) | Dominant US community bank/CU position maintained | Core banking revenue buried in larger fintech revenue; DNA modernization slow relative to cloud-native challengers; Signature/Premier architecturally aging | Fiserv 10-K FY2025 | https://investors.fiserv.com | No — total revenue verified, segment breakdown unverified |
| Jack Henry | SilverLake, CIF 20/20, Core Director | ~$2.4B total revenue (FY2025, ended Jun 2025); guided $2.475–2.504B FY2026 | ~800+ community banks and credit unions (estimated) | Tier 3–4 (community banks, credit unions; winning some larger FIs) | US-only | Modular; hybrid architecture | On-prem; private cloud; some hosted | Winning "larger financial institutions" per CEO; strong Q4 FY2025 sales wins | US-only geography limits TAM; no cloud-native core; dependent on community bank segment facing consolidation | Jack Henry 10-K FY2025; IR releases | https://ir.jackhenry.com | No — revenue from IR release, customer count estimated |
| Temenos | Transact (core), Infinity (digital) | $1.091B total revenue (FY2025); ARR $860M | 950+ core banking clients across 150+ countries | Tier 1–3 | Global (strong in EMEA, growing in US) | Modular; API-first; cloud-deployable | On-prem; private cloud; SaaS (Temenos SaaS) | #1 IBS Intelligence Sales League Table for 20 consecutive years; MIDBANK Egypt full replacement; strong US Tier 1 wins in 2025 | Revenue growth re-accelerating but margins under pressure; SaaS transition incomplete; 2024 short-seller attack damaged credibility | Temenos FY2025 results; IBS Intelligence SLT 2025 | https://www.temenos.com/press_release/temenos-announces-q4-2025-results-22tw4tk10/ | No — revenue from press release |
| Infosys | Finacle (core, digital, payments) | Not separately disclosed (Infosys total ~$19B); Finacle est. $500–700M [unverified — needs manual confirmation] | 100+ banks globally; ~30% in India | Tier 1–2 | India-dominant (29.8% of customers); global presence | Modular; API-enabled | On-prem; private cloud; some cloud-native modules | Bharat Co-op Bank upgrade to v10.2.25 (Jan 2025); Global Banking & Finance Awards 2025 | Perceived as India-centric; cloud-native story weaker than Thought Machine/Mambu; parent company (Infosys) priorities may not align with product investment needs | Finacle website; ANI News | https://www.finacle.com | No — revenue estimated |
| TCS | BaNCS (core, digital, payments, compliance) | Not separately disclosed (TCS total ~$29B); BaNCS est. $400–600M [unverified — needs manual confirmation] | 200+ customers; 450+ installations globally | Tier 1–3 | Global (strong in Middle East, Europe, US growing) | Modular; open architecture; cloud-ready | On-prem; private cloud; SaaS (BaNCS Cloud) | Leader in Gartner MQ Europe 2025; Central Bank (US); Burgan Bank (Kuwait) May 2024; PostFinance (Switzerland) live | SaaS traction slower than cloud-native challengers; large-bank deal cycles long; pricing competitive but margins uncertain | TCS press releases; Gartner MQ | https://www.tcs.com | No — customer count from press releases |
| Oracle | FLEXCUBE (Universal Banking, Retail) | Not separately disclosed (Oracle total ~$56B); FLEXCUBE est. $300–500M [unverified — needs manual confirmation] | 130+ countries; hundreds of banks | Tier 1–2 | Global (strong in Africa, Middle East, Asia) | Monolithic moving to modular; Oracle Cloud compatible | On-prem; Oracle Cloud | Access Bank (Nigeria) core modernization Sep 2025 — 60M customers, 24 markets; Gartner Peer rating 3.9/5 | Aging architecture vs cloud-native; Oracle sales model friction; lower Gartner Peer rating than competitors; strategic priority unclear within Oracle's broader cloud push | Oracle press release Sep 2025 | https://www.oracle.com/financial-services/banking/ | No — revenue estimated |
| Finastra | Fusion Essence, Midas, Equation, Fusion Corporate Channels, Fusion Cash Management | ~$1.85B total revenue; TCM division ~$400M (being sold to Apax for ~$2B); ME/Asia core banking unit $100M EBITDA (exploring sale >$1B) | Thousands across lending, treasury, core banking | Tier 1–3 | Global (strong in EMEA, Asia, Middle East) | Mixed (legacy + modern); Fusion Essence more modular | On-prem; private cloud; some SaaS | TCM division serves 48 of top 50 banks globally | Highly leveraged (9.97x EBITDA in 2023, targeting 6.3x post-sales); Vista Equity actively divesting pieces; strategic uncertainty; three failed exit attempts since 2019; $4.8B outstanding debt | Finastra press release; Reuters; CorpDev.Org | https://www.finastra.com | No — revenue from analyst estimates |

### B. Modern Cloud-Native Challengers

| Vendor | Product(s) | Revenue / Funding | Bank Customers | Tier Focus | Geography | Architecture | Deployment | Recent Wins | Vulnerabilities | Source | URL | Verified |
|--------|-----------|-------------------|---------------|------------|-----------|-------------|------------|-------------|-----------------|--------|-----|----------|
| Thought Machine | Vault Core, Vault Payments | £47.6M revenue (FY2024, slight decline); losses widened to £71.2M; raised £45M Jul 2024 | ~20–25 (estimated); Lloyds, ING, SEB, Intesa Sanpaolo, Standard Chartered, Atom Bank, Curve, Shawbrook | Tier 1–2 | UK-centric; expanding globally | Cloud-native; microservices; smart contracts | Public cloud (AWS, GCP) | Shawbrook go-live Aug 2025; Lloyds extended license to 2029 | Revenue declining slightly; losses widening; valuation cut ~40% by Molten Ventures Dec 2024; headcount reduced 12.4% in 2024; pre-revenue at scale; IPO timeline uncertain | CityAM Oct 2025; Tech.eu | https://www.thoughtmachine.net | No — revenue from Companies House filing |
| Mambu | Mambu Cloud Banking Platform | Est. ~$160M revenue (2025); valued at €4.9B (Series E, Dec 2021; current est. $5.5B) | 200+ (estimated; 60+ new in 2025 alone) | Tier 2–4; fintechs | Global (65+ countries) | Cloud-native; SaaS; composable; low-code | Public cloud (SaaS-only) | 60+ new customers in 2025; entered US credit union market; Payments hub launched; 20+ European VOP customers | Revenue still modest relative to valuation; profitability unproven; limited Tier 1 traction; valuation may be stretched post-2021 peak | Mambu website; CompWorth; Acton Capital | https://www.mambu.com | No — revenue estimated |
| 10x Banking | SuperCore | Not disclosed (private); raised $187M total funding | ~10–15 (estimated); Chase UK (flagship), Standard Chartered (Audax), Old Mutual, West Brom, Co-operative Bank NZ | Tier 1–2 | UK-centric; expanding APAC, Africa | Cloud-native; microservices; AWS-based | Public cloud | Chase UK: 2.5M+ customers Feb 2025, £15B+ deposits; named Celent Luminary for mid-large banks; 10-year anniversary Jan 2026 | Concentrated customer base (Chase UK dominant); profitability unknown; limited geographic scale; dependent on marquee client retention | 10x Banking website; Celent report; Open Banking Expo | https://www.10xbanking.com | No — customer data from press releases |
| Finxact (FIS) | Finxact Core | Integrated into FIS Banking Solutions ($7.285B segment) | Early-stage; pre-acquisition ~12–15 banks [unverified — needs manual confirmation] | Tier 1–2 (target) | US primarily | Cloud-native; AWS-based; API-first | Public cloud (SaaS) | Acquired by FIS 2022; now branded as FIS Modern Banking Platform | Still early in production deployments; integration into FIS sales motion uncertain; competing with FIS's own legacy products for internal attention | FIS 10-K; press releases | https://www.fisglobal.com | No — customer count unverified |
| Pismo (Visa) | Pismo Core Banking & Issuer Processing | Acquired by Visa Jan 2024 for $1B; revenue not separately disclosed | ~30–40 (estimated); Itaú (flagship), Citigroup (DDA), 1 major European bank live, 3 implementing | Tier 1–2 | Brazil (origin); expanding Europe, US, India, Australia | Cloud-native; API-first; multi-product (core + payments) | Public cloud (SaaS) | Citigroup corporate DDA contract; European expansion from 0 to multiple customers post-Visa; 15–20 US conversations underway | Visa ownership may create conflicts with non-Visa banks; scale still limited outside Brazil; revenue contribution to Visa immaterial currently | Visa investor relations; Payments Dive | https://corporate.visa.com/en/sites/visa-perspectives/innovation/transform-with-visa-and-pismo-next-gen-processing-and-core-banking.html | No — deal data from press releases |

### C. Digital Banking Platform Specialists

| Vendor | Product(s) | Revenue | Bank Customers | Tier Focus | Geography | Architecture | Deployment | Recent Wins | Vulnerabilities | Source | URL | Verified |
|--------|-----------|---------|---------------|------------|-----------|-------------|------------|-------------|-----------------|--------|-----|----------|
| Backbase | Engagement Banking Platform | Est. ~$365M revenue (2025); valued at €2.5B; raised €120M from Motive Partners (2022) | 150+ globally | Tier 1–3 | Global (HQ Netherlands) | Modular; API-first; microservices | On-prem; private cloud; SaaS | Consistent >30% ARR growth; strong Tier 1/2 traction | Private company — limited financial transparency; not a core banking system (engagement layer only); competition from Temenos Infinity, Q2, Alkami | Backbase website; Growjo; Owler | https://www.backbase.com | No — revenue estimated |
| Alkami Technology | Alkami Digital Banking Platform | $443.6M revenue (FY2025, +33%); ARR $480.3M (+35%); adj. EBITDA $59.1M | 22.4M registered users; 39 new logos in 2025 (11 banks) | Tier 3–4 (community banks, credit unions) | US-only | Cloud-native; SaaS | Public cloud (SaaS-only) | Best new logo year in 4 years; guided $525–530M revenue FY2026 | US community bank/CU only — limited TAM expansion path; not a core — digital channel layer; profitability still early-stage | Alkami Q4 2025 earnings Feb 2026 | https://investors.alkami.com | Yes — public company SEC filings |
| Q2 Holdings | Q2 Digital Banking Platform | $794.8M revenue (FY2025, +14%); subscription ARR $780.1M (+14%); backlog $2.7B (+21%) | 8 Enterprise/Tier 1 wins in Q4 2025 alone | Tier 1–4 | US-dominant; some international | Cloud-native (completed AWS migration Jan 2026) | Public cloud (SaaS) | Second-strongest bookings quarter ever in Q4 2025; targeting 65%+ non-GAAP gross margin by 2030 | Margins still improving; GAAP net income only $52M on $795M revenue; commercial digital banking competing with Backbase, Temenos | Q2 Holdings Q4 2025 earnings Feb 2026 | https://www.nasdaq.com/press-release/q2-holdings-inc-announces-fourth-quarter-and-full-year-2025-financial-results-2026-02 | Yes — public company SEC filings |
| NCR Voyix (Digital Banking — now Veritas Capital) | NCR Digital Banking Platform (incl. Terafina) | Sold to Veritas Capital Sep 2024 for $2.45B + $100M contingent | 1,300+ FIs; 20M+ active users (at time of sale) | Tier 3–4 | US-only | Modular | Private cloud; hosted | N/A (under new PE ownership; strategic direction unclear) | New PE ownership may prioritize cash extraction over investment; separated from NCR's broader ecosystem; Terafina account origination integration uncertain | NCR Voyix IR; Financial IT | https://investor.ncrvoyix.com | Yes — sale price from SEC filings |
| Temenos | Infinity (digital front-end) | Included in Temenos $1.091B total revenue | Part of 950+ client base | Tier 1–3 | Global | Modular; API-enabled; integrates with Transact | On-prem; cloud; SaaS | Bundled wins with Transact core | Competes with best-of-breed digital platforms (Backbase, Q2); bundled positioning limits standalone appeal | Temenos FY2025 results | https://www.temenos.com | No |

### D. Business Banking and Cash Management

| Vendor | Product(s) | Revenue | Bank Customers | Tier Focus | Geography | Architecture | Deployment | Recent Wins | Vulnerabilities | Source | URL | Verified |
|--------|-----------|---------|---------------|------------|-----------|-------------|------------|-------------|-----------------|--------|-----|----------|
| Finastra | Fusion Corporate Channels, Fusion Cash Management | Part of ~$1.85B total; TCM division ~$400M (being sold) | 340+ FIs for TCM (incl. 48 of top 50 banks) | Tier 1–2 | Global | Mixed legacy + modern | On-prem; private cloud | TCM sale to Apax at ~5x revenue; strong Tier 1 penetration | Under divestiture — strategic uncertainty; buyer Apax may not invest in innovation; leveraged parent entity | CorpDev.Org; Finastra press release | https://www.finastra.com | No |
| Bottomline Technologies (Thoma Bravo) | Paymode-X, Digital Banking, Cash Management | ~$530M+ revenue (annualized from last public quarter at ~$132M/qtr); acquired for $2.6B May 2022 | Thousands of corporates and banks | Tier 1–3 (corporate treasury focus) | US-dominant; global | SaaS; cloud-based | Cloud; SaaS | U.S. Bank partnership; strong payment automation traction | PE-owned — limited public visibility; innovation pace under Thoma Bravo unclear; competing with Kyriba, FIS, Fiserv | Reuters; Bottomline press release | https://www.bottomline.com | No — revenue annualized from last public quarter |
| Kyriba | Kyriba Liquidity Performance Platform | Not disclosed (private); est. $200–300M [unverified — needs manual confirmation] | 2,500+ corporate clients; connects to 9,900+ banks | Corporate treasury (not banks directly) | Global | Cloud-native; SaaS | SaaS-only | U.S. Bank partnership Nov 2025 (Liquidity Manager); 82% YTD new business bookings growth Q3 2025; launched TAI (Agentic AI) | Corporate treasury focus — not a banking vendor directly; competes with bank-owned treasury platforms; revenue not publicly disclosed | Kyriba website; press releases | https://www.kyriba.com | No — revenue estimated |
| ION Group | Openlink, Wallstreet Suite | Not disclosed (PE-owned; ION Group est. $2B+ total across all divisions) [unverified — needs manual confirmation] | Major banks and corporates | Tier 1 (capital markets, treasury) | Global (European roots) | Legacy + modernizing | On-prem; hosted | Openlink V25 launch for treasury/commodity management | PE-owned (opaque); complex multi-acquisition structure; limited innovation visibility; treasury/capital markets niche | ION Group website | https://iongroup.com | No — revenue highly estimated |
| ACI Worldwide | ACI Enterprise Payments Platform (incl. cash management modules) | $1.76B total revenue (FY2025, +10%); Payment Software segment grew 9% | 94 of top 100 banks; 9 of top 10 | Tier 1–2 | Global | Mixed (legacy UP platform + modern modules) | On-prem; cloud | Double-digit revenue growth; guided 7–9% for 2026 | Cash management is a secondary product line vs payments; architecture is hybrid not cloud-native; competing with pure-play treasury platforms | ACI FY2025 earnings Feb 2026 | https://www.businesswire.com/news/home/20260226452626/en/ | Yes — public company |

### E. Account Origination Specialists

| Vendor | Product(s) | Revenue | Bank Customers | Tier Focus | Geography | Architecture | Deployment | Recent Wins | Vulnerabilities | Source | URL | Verified |
|--------|-----------|---------|---------------|------------|-----------|-------------|------------|-------------|-----------------|--------|-----|----------|
| Newgen Software | NewgenONE (Loan Origination, Account Opening) | ₹1,487 crore (~$178M) revenue FY2025 (+20% YoY); PAT ₹315 crore (+25%) | 500+ customers across 57 countries; 62 new logos in FY25 | Tier 2–4 | India-origin; global (EMEA, US expanding) | Low-code; cloud-native; API-enabled | On-prem; cloud; SaaS | US banking client digital account opening ($1.8M deal); Aye Finance loan origination (INR 24Cr); EMEA digital lending ($2M) | Modest revenue scale; not a household name in US/EU Tier 1 banking; competes with Pega, Temenos JM for mindshare | Newgen Q2 FY26 press release | https://newgensoft.com | Yes — public company (India) |
| Pegasystems | Pega Platform (Financial Services) | $1.746B total revenue (FY2025, +17%); Pega Cloud ACV +33% | Financial services is a top vertical but segment revenue not disclosed | Tier 1–2 | Global | Low-code; cloud-native; AI-powered decisioning | Public cloud; on-prem | Strong ACV growth; 45% operating cash flow growth | Financial services is one of many verticals — not banking-specialized; expensive; complex implementation; losing some ground to lower-code alternatives | Pega Q4 2025 earnings Feb 2026 | https://www.nasdaq.com/press-release/innovation-accelerates-pegas-q4-2025-growth-2026-02-10 | Yes — public company |
| Temenos | Journey Manager, Temenos Origination | Included in Temenos $1.091B total | Part of 950+ client base | Tier 1–3 | Global | Cloud-deployable; API-integrated; omnichannel | Cloud; on-prem | MidWestOne Bank: <2 min account opening, 63% completion rate (vs 50% industry avg) | Competes with standalone origination platforms; cross-sell dependent on Transact core presence | Temenos website | https://temenos.com/products/journey-manager | No |
| Salesforce | Financial Services Cloud (Agentforce Financial Services) | Not separately disclosed (Salesforce total ~$38B); FSC is one of many industry clouds | Not disclosed; customers incl. RBC Wealth Management, PenFed, Holmes Murphy, Pacific Life | Tier 1–3 | Global | Cloud-native; CRM-based; Agentforce AI | SaaS-only | Summer 2025: launched Agentforce for Financial Services with banking, wealth, insurance assistants | Not a core banking or account origination system — CRM overlay; requires integration with actual core; pricing premium; implementation complexity | Salesforce Financial Services Cloud releases | https://www.salesforce.com/financial-services/cloud/ | No |

### F. Product and Pricing Engines

| Vendor | Product(s) | Revenue | Bank Customers | Tier Focus | Geography | Architecture | Deployment | Recent Wins | Vulnerabilities | Source | URL | Verified |
|--------|-----------|---------|---------------|------------|-----------|-------------|------------|-------------|-----------------|--------|-----|----------|
| Zafin | Zafin Product & Pricing Platform, Product & Pricing Index | Not disclosed (private); est. $50–100M [unverified — needs manual confirmation] | ~20–40 banks (estimated; primarily Tier 1 US/Canada) | Tier 1–2 | North America primarily | Cloud-native; microservices; API-first | Cloud; SaaS | CNBC World's Top Fintech 2025; Tier 1 US bank recaptured $10M/yr; leading bank saved $20M/qtr via rate management | Narrow product scope (pricing/billing only); small revenue base; dependent on core augmentation narrative winning over core replacement | Zafin website; CNBC | https://zafin.com | No — revenue estimated |
| Moxo | Moxo Service Orchestration Platform | Not disclosed (private) | 40+ named orgs; Citibank, BNP Paribas, Standard Chartered, Scotiabank, Emirates Bank | Tier 1–2 (wealth management, private banking) | Global | Cloud-native; AI orchestration | Cloud; SaaS | Won 2 categories at Global Private Banker WealthTech Awards 2025; BNP Paribas MyWealth platform | Not a pricing engine per se — service orchestration/collaboration platform; niche use case; limited to relationship management workflows | Moxo website; PR Newswire | https://www.moxo.com | No |
| SunTec | Xelerate (pricing, billing, revenue management) | Not disclosed (private); est. $80–120M [unverified — needs manual confirmation] | 150–170 clients across 45+ countries; 400M+ end-customers served | Tier 1–3 | Global (India-origin; strong in Middle East, Asia, Europe) | Cloud-native; microservices; AI-augmented | On-prem; private cloud; SaaS | UAE pre-approved e-invoicing provider; launched AI-augmented deal management for global banks; Celent recognized | "Core augmentation" positioning attractive but niche; competes with core vendors bundling pricing; modest brand recognition in US | SunTec website; Celent | https://www.suntecgroup.com | No — revenue estimated |

### G. India-Specific Core Banking

| Vendor | Product(s) | Revenue | Bank Customers | Tier Focus | Geography | Architecture | Deployment | Recent Wins | Vulnerabilities | Source | URL | Verified |
|--------|-----------|---------|---------------|------------|-----------|-------------|------------|-------------|-----------------|--------|-----|----------|
| Infosys Finacle | Finacle Core, Finacle Digital, Finacle Payments | Est. $500–700M [unverified — needs manual confirmation] | SBI (flagship — largest bank in India), ICICI, and 100+ banks globally | Tier 1–2 (India); Tier 2–3 (global) | India dominant (29.8% customer base); global presence | Modular; API-enabled; 5-stage modernization framework | On-prem; private cloud; cloud-native modules available | SBI modernization (2-year timeline); Bharat Co-op Bank upgrade Jan 2025 | Cloud-native story incomplete; modernization framework competes with Temenos, TCS narratives; Infosys parent priorities may deprioritize product investment | Finacle website; BW Businessworld | https://www.finacle.com | No — revenue estimated |
| TCS BaNCS | BaNCS Core, BaNCS Cloud | Est. $400–600M [unverified — needs manual confirmation] | 200+ globally; strong India presence | Tier 1–3 | India; Middle East; Europe; US growing | Modular; open architecture; SaaS variant | On-prem; private cloud; SaaS | Gartner MQ Leader Europe 2025; Central Bank US; Burgan Bank Kuwait | SaaS model still early; competes with Finacle domestically; parent TCS services revenue may overshadow product investment | TCS press releases; Gartner | https://www.tcs.com | No — revenue estimated |
| Oracle FLEXCUBE | FLEXCUBE Universal Banking, FLEXCUBE Retail | Est. $300–500M [unverified — needs manual confirmation] | Hundreds of banks; 130+ countries | Tier 1–2 (India, Africa, Middle East) | India; Africa; Middle East; Asia | Monolithic moving to modular | On-prem; Oracle Cloud | Access Bank Nigeria Sep 2025 (60M customers) | Gartner Peer rating 3.9 (lowest among major vendors); aging architecture; Oracle's strategic focus on cloud may deprioritize FLEXCUBE; lower Tier 1 wins vs Temenos, Finacle | Oracle press release | https://www.oracle.com/financial-services/ | No — revenue estimated |
| Intellect Design Arena | iGTB (corporate banking), iGCB (consumer banking), IntellectAI | ₹789 crore Q2 FY26 (~$95M/qtr); ARR ₹1,080 crore (~$130M); license revenue +69% YoY | 500+ customers across 57 countries; 117 banking customers via Central Bank acquisition | Tier 1–3 (corporate banking); Tier 2–4 (retail) | India-origin; global (57 countries) | eMACH.ai (event-driven, microservices, APIs, cloud, headless AI) | On-prem; cloud; SaaS | 43 new customer wins FY25; 35 deal wins H1 FY26; 15 strategic eMACH.ai-led deals incl. 10 multi-million-dollar; deal funnel >₹12,000 crore | Corporate banking niche — not a full-spectrum retail core; brand recognition limited outside India/Middle East; scale modest relative to Finacle/BaNCS | Intellect Design Arena Q2 FY26 results | https://www.intellectdesign.com | Yes — public company (India) |

---

## Bank Modernization Signals Table

| Bank | Tier | Geography | Signal | Source | URL |
|------|------|-----------|--------|--------|-----|
| Citi | Tier 1 | US / Global | Actively recruiting "Head of Core Banking Transformation" (Mar 2026); building future-state digital banking platform; initial focus LATAM, then global rollout; historical migration to FIS Systematics ~2010 | Citi careers; American Banker; Celent | https://jobs.citi.com/job/jersey-city/head-of-core-banking-transformation/287/92309329792 |
| SBI (State Bank of India) | Tier 1 | India | 2-year core banking modernization program: migrating Unix→Linux, deploying microservices, building private cloud, externalizing functions; "modernising as we run the ship"; 300 APIs open via sandbox | BW Businessworld; Business Standard (Nov 2025) | https://www.businessworld.in/article/sbi-targets-two-year-timeline-to-modernise-core-banking-system-md-579751 |
| HDFC Bank | Tier 1 | India | Plans migration of Core Banking System to new engineered platform for enhanced robustness and scalability | HDFC Bank press release (2024) | https://www.hdfcbank.com/personal/about-us/news-room/press-release/2024/q2/hdfc-bank-plans-migration-of-core-banking-system-to-new-engineered-platform-to-enhance-robustness-a |
| HSBC | Tier 1 | UK / Global | $1.8B technology cost reallocation; decommissioned 1,165 legacy applications in 2025; plans to retire 1/3 of application portfolio by 2028; hired 1,800 net new tech employees; GenAI is biggest tech investment priority | Kingy AI / HSBC reporting | https://kingy.ai/news/hsbc-ai-transformation-digital-banking/ |
| Standard Chartered | Tier 1 | UK / Global | "Fit for Growth" program: $754M run-rate savings in 2025 across 300+ initiatives; 18% of initiatives on simplifying tech stack; targeting $1.3B total savings through 2026; achieved 2024–2026 targets a year early | InfotechLead (2025) | https://infotechlead.com/networking/standard-chartered-steps-up-digital-transformation-and-ai-strategy-in-2025-under-fit-for-growth-program-93884 |
| Deutsche Bank | Tier 1 | Germany / Global | Modernizing Corporate Bank payment rails; building real-time cash visibility; exposing APIs for client integration; strategy to operate "like a platform company with standardized core systems and cloud-ready infrastructure" | Ad-Hoc News | https://www.ad-hoc-news.de/boerse/news/ueberblick/deutsche-bank-ag-s-high-stakes-rebuild-can-its-universal-banking/68530612 |
| Wells Fargo | Tier 1 | US | Launched Vantage® next-gen digital banking platform for corporate clients; integrated 65 fragmented systems; won 2025 Celent Model Bank Award for corporate digital banking; uses micro-frontends, APIs, AI/ML, GraphQL | Celent (2025) | [unverified — needs manual confirmation] |
| Access Bank | Tier 1 | Nigeria / 24 markets | Completed core banking modernization with Oracle FLEXCUBE Sep 2025; supports 60M customers; handles 35M+ transactions/day; deployed Oracle Exadata + Private Cloud Appliance | Oracle press release Sep 2025 | https://www.oracle.com/news/announcement/access-bank-completes-major-core-banking-modernization-with-oracle-2025-09-16/ |
| NS&I | Government | UK | Replacing legacy core banking with SBS's cloud-native SBP Digital Core platform; partnering with Atos, IBM, Sopra Steria; announced Jul 2025 | BusinessWire Jul 2025 | https://www.businesswire.com/news/home/20250724610197/en/ |
| MIDBANK | Tier 3 | Egypt | Completed full legacy system replacement with Temenos (big-bang approach); deployed Temenos Core, Payments Hub, Financial Crime Mitigation, Data Hub | Temenos press release Jul 2025 | https://temenos.com/press_release/egypt-midbank-core-banking-modernization-temenos |
| Hanover Bank | Tier 4 | US (New York) | Completed core banking system conversion Feb 2025; upgrading for digital capabilities, enhanced security, streamlined operations | GlobeNewsWire Apr 2025 | https://www.globenewswire.com/news-release/2025/04/22/3065416/0/en/ |
| Chase UK (JPMorgan) | Tier 1 | UK | Operating on 10x Banking's cloud-native core; 2.5M+ customers by Feb 2025; £15B+ deposits; voted Best British Bank 2023 & 2024; on track for profitability by 2025 | 10x Banking website | https://www.10xbanking.com/success-stories/10x-banking-teams-up-with-chase-to-create-next-generation-digital-banking-platform |
| Shawbrook | Tier 3 | UK | Went live on Thought Machine Vault Core Aug 2025; first product: buy-to-let mortgage launched May 2025 | Thought Machine press release | https://www.thoughtmachine.net/press-releases/shawbrook |
| Burgan Bank | Tier 2 | Kuwait / Regional | Selected TCS BaNCS May 2024; consolidating legacy applications into universal banking solution; 160+ branches, 360 ATMs | TCS press release | https://www.tcs.com/content/tcs/global/en/who-we-are/newsroom/press-release/burgan-bank-selects-tcs-bancs-transform-core-banking |

---

## Key Claims Table

| # | Claim | Value | Source | URL | Verified |
|---|-------|-------|--------|-----|----------|
| 1 | FIS total revenue FY2025 | $10.7B (+5%) | FIS 10-K 2025 | https://www.stocktitan.net/sec-filings/FIS/10-k | No |
| 2 | FIS Banking Solutions revenue FY2025 | $7.285B (+6% adjusted) | FIS 10-K 2025 | — | No |
| 3 | FIS acquired Global Payments Issuer Solutions | $13.5B, closed Jan 2026 | Cross-ref: payments S3 | — | No |
| 4 | Fiserv total revenue FY2025 | $21.2B (+4%) | Cross-ref: payments S3; Fiserv 10-K | — | No |
| 5 | Jack Henry revenue FY2025 | +7.2% GAAP; guided $2.475–2.504B FY2026 | Jack Henry IR release | https://ir.jackhenry.com | No |
| 6 | Temenos total revenue FY2025 | $1.091B (+10% CC) | Temenos FY25 results | https://www.temenos.com/press_release/temenos-announces-q4-2025-results-22tw4tk10/ | No |
| 7 | Temenos ARR | $860M (+12% YoY) | Temenos FY25 results | — | No |
| 8 | Temenos #1 IBS SLT for 20 consecutive years | Core banking sales leader | IBS Intelligence SLT 2025 | https://ibsintelligence.com/ibs-intelligence-unveils-the-results-of-its-prestigious-sales-league-table-2025/ | No |
| 9 | Thought Machine revenue FY2024 | £47.6M (−0.4% YoY) | CityAM Oct 2025 | https://www.cityam.com/thought-machine-lands-45m-funding-round-after-losses-widen/ | No |
| 10 | Thought Machine losses FY2024 | £71.2M (+20.6%) | CityAM Oct 2025 | — | No |
| 11 | Thought Machine valuation cut | ~40% cut by Molten Ventures Dec 2024 | CityAM Oct 2025 | — | No |
| 12 | Mambu estimated revenue | ~$160M | CompWorth 2026 | https://compworth.com/company/mambu | No |
| 13 | Mambu valuation | €4.9B (Series E, Dec 2021) | Acton Capital | https://www.actoncapital.com/news/mambu-closes-eu235m-seriese-at-a-eu4-9b-valuation | No |
| 14 | 10x Banking: Chase UK customers | 2.5M+ (Feb 2025) | 10x Banking website | https://www.10xbanking.com | No |
| 15 | Pismo acquired by Visa | $1B, closed Jan 2024 | Visa IR | https://investor.visa.com/news/news-details/2024/Visa-Completes-Acquisition-of-Pismo/ | Yes |
| 16 | Alkami revenue FY2025 | $443.6M (+33%); ARR $480.3M (+35%) | Alkami Q4 2025 earnings | https://investors.alkami.com/2026-02-25-Alkami-Announces-Fourth-Quarter-2025-Financial-Results | Yes |
| 17 | Q2 Holdings revenue FY2025 | $794.8M (+14%); subscription ARR $780.1M | Q2 Q4 2025 earnings | https://www.nasdaq.com/press-release/q2-holdings-inc-announces-fourth-quarter-and-full-year-2025-financial-results-2026-02 | Yes |
| 18 | NCR Digital Banking sold to Veritas | $2.45B + $100M contingent, Sep 2024 | NCR Voyix IR | https://investor.ncrvoyix.com | Yes |
| 19 | Backbase estimated revenue | ~$365M; valued at €2.5B | Growjo; Backbase website | — | No |
| 20 | nCino revenue FY2025 | $540.7M (+13%) | nCino earnings Apr 2025 | https://www.ncino.com/news/ncino-reports-fourth-quarter-fiscal-2025-results | Yes |
| 21 | Finastra total revenue | ~$1.85B | CorpDev.Org | https://www.corpdev.org/2025/05/05/apax-partners-emerges-as-frontrunner-in-2-billion-finastra-tcm-unit-acquisition/ | No |
| 22 | Finastra TCM sale to Apax | ~$2B (5x revenue) | CorpDev.Org; Finastra PR | https://finastra.com/press-media/finastra-sell-treasury-and-capital-markets-division-apax | No |
| 23 | Finastra ME/Asia core banking unit sale explored | >$1B; $100M EBITDA | Reuters/MA Insights | https://www.mainsights.io/ma-news/vista-equity-partners-considering-sale-of-finastra039s-middle-eastern-and-asian-core-banking-unit-for-over-1-billion | No |
| 24 | Bottomline acquired by Thoma Bravo | $2.6B, May 2022 | Reuters; Bottomline PR | https://www.bottomline.com/newsroom/press-releases/thoma-bravo-completes-acquisition-bottomline | Yes |
| 25 | ACI Worldwide revenue FY2025 | $1.76B (+10%) | Cross-ref: payments S3; ACI earnings | https://www.businesswire.com/news/home/20260226452626/en/ | Yes |
| 26 | Pegasystems revenue FY2025 | $1.746B (+17%) | Pega Q4 2025 earnings | https://www.nasdaq.com/press-release/innovation-accelerates-pegas-q4-2025-growth-2026-02-10 | Yes |
| 27 | Newgen Software revenue FY2025 | ₹1,487 crore (~$178M, +20%) | Newgen press release | https://newgensoft.com | Yes |
| 28 | Intellect Design Arena ARR | ₹1,080 crore (~$130M) | Intellect Q2 FY26 results | https://www.intellectdesign.com | Yes |
| 29 | Kyriba new business bookings growth | +82% YTD (Q3 2025) | Kyriba press release | https://www.kyriba.com/news/kyriba-closes-q3-with-82-percent-growth-in-ytd-new-business-bookings/ | No |
| 30 | 92% of FIs commenced core modernization | Industry survey | EY UK Core Banking Technology Modernisation report Oct 2025 | https://www.ey.com/content/dam/ey-unified-site/ey-com/en-uk/industries/banking-capital-markets/documents/ey-uk-core-banking-technology-modernisation-10-2025.pdf | No |
| 31 | 83% of banks plan 2nd-gen cores; 50% within 3–5 years | Industry survey | EY UK report Oct 2025 | — | No |
| 32 | Legacy systems cost banks $57B annually by 2028 | Industry projection | MobileLive | https://www.mobilelive.ai/blog/the-core-banking-modernization-dilemma-incremental-vs-full-system-upgrade | No |
| 33 | Core banking market size 2025 | $19.12B (one estimate) | Expert Market Research | https://www.expertmarketresearch.com/reports/core-banking-solutions-market | No |
| 34 | SBI core banking modernization timeline | 2 years | BW Businessworld Nov 2025 | https://www.businessworld.in/article/sbi-targets-two-year-timeline-to-modernise-core-banking-system-md-579751 | No |
| 35 | HSBC decommissioned legacy apps in 2025 | 1,165 applications | Kingy AI / HSBC | https://kingy.ai/news/hsbc-ai-transformation-digital-banking/ | No |

---

## Key Findings

### Market Structure

- **The legacy Big 3 (FIS, Fiserv, Jack Henry) control the US market.** FIS Banking Solutions alone is $7.3B — larger than the entire revenue of all cloud-native challengers combined. Fiserv is #1 in US core account processing. Jack Henry owns the community bank/CU tier. Displacing them requires breaking switching costs, not just better technology.

- **Cloud-native challengers are real but small.** Thought Machine (~£48M revenue, widening losses, valuation cut 40%), Mambu (~$160M, valuation potentially stretched at €4.9B), 10x (~$187M total funding, concentrated on Chase UK), and Pismo ($1B acquisition, still early outside Brazil). None has achieved escape velocity to Tier 1 scale production across geographies.

- **The Indian core banking market is a distinct competitive theater.** Finacle (SBI, ICICI), TCS BaNCS (200+ global installs), FLEXCUBE (Access Bank, 130+ countries), and Intellect Design Arena (iGTB for corporate banking) dominate. Indian vendors have global aspirations but remain geography-weighted.

### Competitive Dynamics

- **FIS is making the boldest portfolio bet.** Banking Solutions ($7.3B) + Finxact (cloud-native core) + TSYS/Issuer Solutions ($13.5B acquisition) = end-to-end "money lifecycle" positioning. If they execute the integration, FIS becomes the only vendor spanning core banking + payments processing + card issuing at scale.

- **Finastra is being dismantled.** Vista Equity selling TCM to Apax (~$2B), exploring ME/Asia core banking unit sale (>$1B), trying to deleverage from 9.97x EBITDA. This creates acquisition opportunities and customer uncertainty simultaneously.

- **Digital banking platforms are the fastest-growing pure-play segment.** Alkami (+33% to $444M), Q2 (+14% to $795M), and Backbase (~$365M, 30%+ ARR growth) are all outpacing the core banking market. These are the "augment the core" wedge — they wrap legacy cores with modern digital experiences.

- **Product/pricing engines (Zafin, SunTec) are the sleeper category.** They enable "core augmentation" — externalizing pricing, billing, and product management from the core without replacing it. SunTec (150–170 clients, 45+ countries) and Zafin (Tier 1 US banks) are proving that you can modernize around the core rather than through it.

### M&A and Ownership Reshuffling

- **Visa acquiring Pismo ($1B, Jan 2024)**: Network player entering core banking; Pismo now has Visa's sales force accelerating global expansion (0 European customers pre-acquisition → multiple now)
- **FIS acquiring Finxact (2022)**: Legacy incumbent buying cloud-native core; integration and cannibalization risk
- **FIS acquiring TSYS/Issuer Solutions ($13.5B, Jan 2026)**: Consolidating banking + payments + issuing
- **NCR spinning off (Oct 2023)**: Digital banking sold to Veritas Capital ($2.45B, Sep 2024); 1,300 FIs now under PE ownership
- **Thoma Bravo acquiring Bottomline ($2.6B, May 2022)**: Cash management/payments under PE
- **Vista Equity divesting Finastra pieces**: TCM to Apax (~$2B); ME/Asia core banking (>$1B explored)

---

## The Defining Competitive Question

### Is the market moving to "replace the core" or "augment the core"?

**Evidence for "replace the core":**
- 92% of FIs have commenced core modernization journeys (EY UK Oct 2025)
- 83% plan to choose second-generation cores (EY UK Oct 2025)
- Temenos: 950+ core banking clients, #1 IBS SLT for 20 years — demand for replacement engines is persistent
- Access Bank (60M customers) completed full Oracle FLEXCUBE replacement (Sep 2025)
- MIDBANK Egypt completed big-bang Temenos replacement (Jul 2025)
- NS&I replacing legacy core with SBS cloud-native platform (Jul 2025)
- Chase UK built entirely on 10x's cloud-native core — reached 2.5M customers in ~3 years
- SBI targeting 2-year modernization with microservices, private cloud, platform decoupling
- Citi actively hiring "Head of Core Banking Transformation" for global modernization (Mar 2026)
- Thought Machine Vault live at Lloyds, ING, SEB, Intesa Sanpaolo — Tier 1 adoption is real

**Evidence for "augment the core":**
- Legacy Big 3 (FIS/Fiserv/Jack Henry) control the vast majority of US banking relationships — switching costs are enormous
- Digital banking platforms (Alkami, Q2, Backbase) growing 14–33% by wrapping legacy cores, not replacing them
- Zafin and SunTec proving pricing/billing can be externalized without core replacement
- Wells Fargo Vantage integrated 65 fragmented systems without replacing the core
- Progressive/layered modernization now favored over big-bang by majority of analysts (Everest Group, Finastra, Oliver Wyman)
- "Core augmentation" is the dominant actual behavior — 50% of banks aim to complete modernization within 3–5 years, but "modernization" increasingly means wrapping, not replacing
- Standard Chartered's $1.3B savings program focuses on simplifying tech stack, not core replacement
- SBI explicitly says "modernising as we run the ship" — microservices externalization, not core swap
- Legacy systems cost $57B/yr by 2028 (industry est.) — but replacing them costs more upfront

**Synthesis:** The market is bifurcating. Tier 1 banks with resources and strategic urgency (Citi, HSBC, Deutsche Bank) will pursue multi-year core transformation programs. The vast majority of Tier 2–4 banks will augment — wrapping legacy cores with modern digital layers, externalizing pricing/payments/origination, and extending core life by 10+ years. The vendors winning are those that serve both motions: offering cloud-native cores for replacement AND modular capabilities (digital banking, pricing, origination) for augmentation.

---

## Gaps and Unresolved Questions

1. **FIS Banking Solutions breakdown**: $7.285B revenue not decomposed into core banking vs. lending vs. wealth vs. other — need 10-K segment detail
2. **Fiserv core banking customer count**: #1 self-reported position but actual DNA/Signature/Premier customer counts not publicly available
3. **Jack Henry core revenue**: Total company revenue available but core banking vs. payments vs. complementary not separately disclosed
4. **Temenos US Tier 1 wins**: Mentioned in earnings call but no specific bank names disclosed — need to verify
5. **Thought Machine customer pipeline**: ~20–25 estimated customers but exact production-live count unclear; revenue declining despite new wins
6. **Mambu profitability**: ~$160M revenue at €4.9B valuation — path to profitability not demonstrated
7. **10x Banking financials**: Entirely private; revenue, losses, runway unknown
8. **Finacle, BaNCS, FLEXCUBE revenues**: None report segment-level revenue — all estimates are rough ranges
9. **Finastra post-divestiture strategy**: What remains after TCM and ME/Asia core banking are sold? Is Finastra viable as a standalone?
10. **Zafin and SunTec revenues**: Both private; revenue estimates are triangulated from employee count and customer base
11. **ION Group treasury revenue**: PE-owned, multi-acquisition conglomerate — financial data not publicly available
12. **Gartner MQ details**: Only vendor announcement summaries available — full MQ positioning (Leaders, Challengers, Visionaries, Niche) not accessible without subscription
13. **Celent xCelent Awards**: Full vendor-by-vendor rankings not publicly available — only vendor-announced awards captured
14. **IDC MarketScape for Core Banking**: No 2025/2026 edition found in public domain
15. **HDFC Bank core migration vendor selection**: Announced platform migration but vendor/technology choice not disclosed
16. **Citi core banking transformation vendor**: Actively hiring but vendor selection (if any) not publicly disclosed
17. **EY "92% commenced modernization" claim**: Source is EY UK report (Oct 2025 PDF) — survey methodology and sample size not verified
18. **Core banking market size**: Estimates range wildly from $10B to $19B depending on scope definition — need to align to consistent methodology

---

## Raw Notes and Excerpts

### Analyst/Industry Quotes

> "Banking CIOs are prioritizing core modernization to deliver decentralized applications, with core banking systems evolving to enhance composability and cloud usage."
> — Gartner MQ for Retail Core Banking Systems, Europe 2025

> "The core banking sector has shifted from early adopter to early majority phase, with next-gen cores now mainstream consideration."
> — Celent, Retail Banking Core Systems: Next-Generation Core Banking Edition (Dec 2024)

> "92% of financial institutions have commenced core modernisation journeys. About 83% plan to choose second-generation cores, with 50% aiming to complete modernization within three to five years."
> — EY UK Core Banking Technology Modernisation report, Oct 2025

> "A risky 'big-bang' replacement isn't the answer."
> — Finastra, Solving Banking's Toughest Challenges: Practical Paths to Rapid Core Modernization (2026)

> "By 2028, legacy systems are projected to cost banks over $57 billion annually."
> — MobileLive analysis

> "FIS now has the most comprehensive financial dataset in the industry — spanning the entire money lifecycle."
> — FIS Q4 2025 earnings commentary, Feb 2026

> "We are modernising as we run the ship."
> — SBI Managing Director on core banking modernization, Nov 2025

> "Visa's acquisition of Pismo has been transformative... We had zero European customers before Visa. Now we're live with one major bank, implementing three others, with tens of conversations going on."
> — Pismo/Visa commentary to Payments Dive, 2025

### Revenue Comparison (Ranked by Banking-Specific Revenue, FY2025)

| Rank | Vendor | Banking/Total Revenue | Type |
|------|--------|-----------------------|------|
| 1 | FIS | $7.285B / $10.7B | Public |
| 2 | Fiserv | Not disclosed / $21.2B | Public |
| 3 | Jack Henry | Not disclosed / ~$2.4B | Public |
| 4 | ACI Worldwide | Not disclosed / $1.76B | Public |
| 5 | Finastra | ~$1.85B total (private) | Private (Vista) |
| 6 | Temenos | $1.091B (all banking) | Public |
| 7 | Q2 Holdings | $794.8M (all banking) | Public |
| 8 | Pegasystems | FS segment not disclosed / $1.746B | Public |
| 9 | nCino | $540.7M (all banking) | Public |
| 10 | Alkami | $443.6M (all banking) | Public |
| 11 | Backbase | ~$365M (estimated, all banking) | Private |
| 12 | Newgen | ~$178M (multi-industry) | Public (India) |
| 13 | Mambu | ~$160M (estimated, all banking) | Private |
| 14 | Intellect Design Arena | ~$380M annualized (multi-segment) | Public (India) |
| 15 | SunTec | ~$80–120M (estimated) | Private |
| 16 | Zafin | ~$50–100M (estimated) | Private |
| 17 | Thought Machine | ~$60M (~£47.6M) | Private |

### Architecture Model Comparison

| Vendor | Monolithic | Modular | Cloud-Native | SaaS-Only |
|--------|-----------|---------|-------------|-----------|
| FIS (legacy) | ✓ | | | |
| FIS (Finxact) | | | ✓ | ✓ |
| Fiserv (Signature/Premier) | ✓ | | | |
| Fiserv (DNA) | | ✓ | | |
| Jack Henry | | ✓ | | |
| Temenos Transact | | ✓ | | |
| Oracle FLEXCUBE | ✓ → ✓ | | | |
| Infosys Finacle | | ✓ | | |
| TCS BaNCS | | ✓ | | |
| Finastra (mixed) | ✓ | ✓ | | |
| Thought Machine | | | ✓ | |
| Mambu | | | ✓ | ✓ |
| 10x Banking | | | ✓ | |
| Pismo | | | ✓ | ✓ |
| Alkami | | | ✓ | ✓ |
| Q2 Holdings | | | ✓ | ✓ |
| Backbase | | ✓ | | |

### Gartner MQ Positioning (2025, Partial — from vendor announcements only)

| Region | Leaders | Other Recognized Vendors |
|--------|---------|------------------------|
| North America | FIS (HORIZON, IBS) | [Full quadrant not publicly available] |
| Europe | TCS BaNCS | [Full quadrant not publicly available] |
| Next-Gen (Celent) | 10x Banking (Luminary — mid-large banks) | [Full report not publicly available] |

### IBS Intelligence Sales League Table 2025 (Core Banking Category)

| Rank | Vendor | Note |
|------|--------|------|
| 1 | Temenos | 20th consecutive year; topped 13 categories total |
| 2+ | [Not publicly disclosed] | Full rankings behind paywall |

### M&A Activity Summary (2022–2026)

| Date | Acquirer | Target | Value | Rationale |
|------|----------|--------|-------|-----------|
| 2022 | FIS | Finxact | ~$650M [unverified — needs manual confirmation] | Cloud-native core banking acquisition |
| May 2022 | Thoma Bravo | Bottomline Technologies | $2.6B | Cash management / payments PE take-private |
| Jun 2023 (closed Jan 2024) | Visa | Pismo | $1B | Cloud-native core + issuer processing |
| Oct 2023 | N/A | NCR spin-off | N/A | NCR Voyix (commerce) vs NCR Atleos (ATM) |
| Sep 2024 | Veritas Capital | NCR Voyix Digital Banking | $2.45B + $100M contingent | Digital banking platform PE take-private |
| Jan 2026 | FIS | Global Payments Issuer Solutions (TSYS) | $13.5B | End-to-end money lifecycle |
| H1 2026 (expected) | Apax Partners | Finastra TCM division | ~$2B | Treasury & capital markets carve-out |
| TBD | TBD | Finastra ME/Asia core banking | >$1B (explored) | Core banking unit divestiture |

---

*All unverified claims require Stream 8 verification pass. Revenue estimates for private companies are triangulated from Owler, Growjo, CompWorth, Tracxn, and public filings of parent companies where applicable. Gartner MQ and Celent xCelent full reports are behind paywalls — only vendor-announced positioning captured.*
