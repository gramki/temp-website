# Chapter 02.03: Account Products and Core Banking — Opportunity Analysis

*Prepared for Zeta's executive team and board. March 2026.*

---

## Executive Summary

The account products and core banking technology market is a **$25–40 billion opportunity** growing at 9–14% CAGR, with Tier 2–3 vendor-addressable TAM of approximately $15–20 billion. The market is shaped by seven structural shifts: (1) progressive core replacement displacing big-bang migration after TSB's £614 million failure; (2) cloud-native infrastructure becoming the default selection criterion with 84.5% cloud adoption across tracked transformations; (3) composable banking reaching production at 15+ named banks — though only alongside monolithic cores, not replacing them entirely; (4) business banking digitization creating a separate $8–12 billion modernization wave; (5) open banking mandates exposing legacy limitations without forcing core replacement; (6) deposit competition from neobanks capturing 40% of new US account openings; and (7) embedded banking requiring modern core infrastructure after the Synapse collapse.

The most underserved segment is **mid-market banks ($10–100 billion in assets)** — too large for community bank solutions, too small to build in-house. Legacy incumbents (FIS, Fiserv, Jack Henry) are over-engineered and expensive; cloud-native challengers (Thought Machine, Mambu, 10x) are designed for digital subsidiaries and fintechs. No vendor delivers genuinely integrated, affordable, cloud-native account infrastructure for this segment.

**Zeta's position is grounded in production evidence.** Tachyon Credit Cards powers three credit card programs in the USA. Tachyon DDA powers multiple demand deposit account programs in the USA, including health benefits accounts (Optum) and loyalty/rewards programs. All programs run on Photon for payment rail processing. The Evolution Fabric + Tachyon combination (operational model + account platform) is a positioning no competitor occupies — and unlike prior assessments, this is now backed by US production deployments. The gap is not product readiness but market visibility: Zeta lacks analyst coverage (Celent, Datos Insights, CB RADAR) and the production evidence has not been translated into publicly referenceable case studies.

**Recommended actions:** (1) Convert existing US production deployments into referenceable case studies — three credit card programs and multiple DDA programs represent a credible production track record that must be visible to mid-market buyers. (2) Engage Celent and Datos Insights for analyst coverage — production evidence makes this engagement substantive rather than aspirational. (3) Pursue India bank deployments for Tachyon DDA in retail/business banking to expand the reference base beyond purpose-specific programs. (4) Target US Tier 2 banks ($10–100B assets) with the Tachyon + Photon + Evolution Fabric combination, leading with credit card and DDA production evidence.

---

# PART I — THE OPPORTUNITY

---

## 1. The Account Products Technology Market

### What banks spend on account technology

The account products and core banking technology market — what banks pay external vendors for core processing, digital banking platforms, deposit operations, origination, and related services — is a **$25–40 billion market** depending on definitional scope, growing at **9–21% CAGR** across sub-segments. The narrowest cut — core banking software alone — ranges from $12.4 billion ([Grand View Research](https://www.grandviewresearch.com/industry-analysis/core-banking-software-market)) to $18.1 billion ([360iResearch via GII](https://www.giiresearch.com/report/ires1589147-core-banking-software-market-by-solution-deposits.html)), with a working mid-range of **$15–17 billion** growing at 9–14% CAGR ([Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/core-banking-market)). The broadest adjacent category — digital banking platforms encompassing mobile, web, and self-service channels — is **$37–46 billion** growing at 17–21% CAGR ([Grand View Research](https://www.grandviewresearch.com/industry-analysis/digital-banking-platforms-market-report); [Kings Research](https://www.kingsresearch.com/digital-banking-platforms-market-2608)).

| Sub-Segment | 2025 Estimate | CAGR | Notes |
|---|---|---|---|
| Core banking platforms | $12–18B | 9–14% | Tier 1 largely in-house; vendor TAM skews Tier 2–3 |
| Digital banking platforms | $37–46B | 17–21% | Broadest definition; includes channel layers |
| Cash management / treasury (BFSI) | $2.8–5.4B | 7–10% | 27% of $20B total market is bank-specific ([Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/cash-management-system-market)) |
| Business banking technology | $8–12B (inferred) | 6–7% | Derived from McKinsey's $1.18T MSME revenue pool |
| Account origination / onboarding | $2.7–6.1B | 15–17% | Cross-industry; banking-specific portion smaller |
| Deposit operations / servicing | $5.8B | 13% | Narrower segment ([Growth Market Reports](https://growthmarketreports.com/report/deposit-product-innovation-platforms-market)) |

*Sources: [Grand View Research](https://www.grandviewresearch.com/industry-analysis/core-banking-software-market), [Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/core-banking-market), [360iResearch](https://www.giiresearch.com/report/ires1589147-core-banking-software-market-by-solution-deposits.html), [Kings Research](https://www.kingsresearch.com/digital-banking-platforms-market-2608) (2025)*

### The vendor-addressable distinction

Not all of this spending reaches external vendors. Tier 1 banks — JPMorgan, Goldman Sachs, and other G-SIBs — are increasingly building core capabilities in-house, "hollowing out" legacy platforms rather than purchasing new ones. JPMorgan selected Thought Machine for its US retail core and runs 70% of its data on cloud infrastructure ([Finextra](https://www.finextra.com/blogposting/28538/deep-dive-how-jpmorgan-is-reengineering-banking-at-scale)). Goldman Sachs engineered its own deposit platform for the Marcus consumer offering. The vendor-addressable TAM for **Tier 2–3 banks is approximately $15–20 billion** ([Levera Partners](https://leverapartners.com/blog/credit-union-banking-software-ma/)).

Vendor concentration is extreme. FIS Banking Solutions generates **$7.3 billion** in revenue ([FIS 10-K](https://www.stocktitan.net/sec-filings/FIS/10-k-fidelity-national-information-services-inc-files-annual-report-faa6cf780c27.html)). Fiserv's total revenue is **$21.2 billion** ([Fiserv](https://investors.fiserv.com)). Jack Henry generates **~$2.4 billion** ([Jack Henry IR](https://ir.jackhenry.com/news-releases/news-release-details/jack-henry-associates-inc-reports-second-quarter-fiscal-2025)). Temenos: **$1.1 billion** ([Temenos](https://www.temenos.com/press_release/temenos-announces-q4-2025-results-22tw4tk10/)). These four vendors together exceed the total revenue of all cloud-native challengers combined.

### The intent-to-action gap

The demand signals are strong but misleading at face value. Only **53% of banks** are satisfied with their core platform provider ([ABA 2025](https://aba.com/about-us/press-room/press-releases/core-platform-survey-2025)). **98% of community banks** planned core system modernization ([Jupid/Cornerstone](https://jupid.com/blog/state-of-community-banking-2025)). UK banks spend **£3.3 billion annually** on legacy core maintenance — 24% of IT budgets, with over half of banking leaders describing their core systems as a "bottomless pit" of wasted resources ([EY/The Banker](https://www.thebanker.com/content/f3b2afa4-2c79-4d26-9cc4-00c5b9b970b1); [Business Money](https://www.business-money.com/announcements/uk-banks-to-pour-3-3bn-into-bottomless-pit-of-core-banking-technology-in-2026/)). Yet Cornerstone Advisors consistently finds that "planned core banking system replacements continue to fall well short of actual deployments" ([Cornerstone WGOB 2026](https://www.crnrstone.com/gritty-insights/research/whats-going-on-in-banking-2026)). The gap between stated intent and executed transformation is the defining feature of this market.

---

## 2. How We Got Here

Three eras of account technology investment shaped the current landscape.

**The monolithic core era (1970s–2005).** Banks deployed integrated core banking systems — FIS, Fiserv, and Jack Henry in the United States; Temenos, Infosys Finacle, TCS BaNCS, and Oracle FLEXCUBE globally. A single vendor provided a single platform with tightly coupled account processing, deposit management, and lending. These systems worked. They processed trillions in transactions, supported regulatory compliance, and scaled with growing customer bases. They also created the 15–25 year replacement cycles that still define the market. The architecture was batch-oriented, mainframe-hosted, and deeply embedded in every operational process the bank ran.

**The channel overlay era (2005–2020).** Rather than replace cores, banks layered digital capabilities on top. Online banking arrived first, then mobile banking, then digital onboarding — each added as a separate system wrapping the legacy core. Integration complexity grew with every layer. The core remained unchanged. Banks spent billions on Backbase, Q2, Alkami, and custom-built digital channels, all communicating with 30-year-old account processing engines through middleware and file-based integrations. The strategy was rational: avoid the risk of core replacement while delivering the digital experiences customers demanded.

**The composable platform pressure (2020–present).** Cloud-native challengers — Thought Machine, Mambu, 10x Banking, Finxact — demonstrated that modern account platforms could be deployed in months, not years. Neobanks launched deposit products in weeks on these platforms. Chime captured 12.8% of all new US checking accounts — more than Chase or Wells Fargo individually ([American Banker/J.D. Power](https://www.americanbanker.com/news/chime-leads-in-new-checking-accounts-opened)). Revolut accumulated £30.2 billion in deposits ([Revolut 2024 Annual Report](https://www.revolut.com/financial-statements/)). Banks that had deferred core modernization for two decades could no longer layer.

The defining cautionary event: TSB's big-bang migration failure — £318 million in direct costs, £247 million in remediation, £48.65 million in regulatory fines, 1.9 million customers locked out, and the CEO's resignation. Total cost: approximately **£614 million** ([UK Parliament Treasury Committee](https://www.parliament.uk/business/committees/committees-a-z/commons-select/treasury-committee/news-parliament-2017/tsb-failure-report-published-19-20/)). The result was lasting industry aversion to full core replacement. Progressive, product-by-product migration became the dominant strategy — though few banks have completed the journey.

---

## 3. Structural Shifts Creating Opportunity

### Shift 1: Progressive Core Replacement Displacing Big-Bang Migration

The industry has abandoned big-bang core replacement in favor of phased, product-by-product migration — a strategic shift driven by catastrophic failure cases, consulting firm endorsement, and a growing evidence base of multi-year successes.

**Evidence:**

- **TSB's £614 million failure** created lasting aversion to big-bang approaches across the global banking industry. The combination of customer harm (1.9 million locked out), regulatory penalties (£48.65 million in fines), executive casualties (CEO resignation), and reputational damage established big-bang migration as an unacceptable risk for board-level decision-makers ([IceDQ/Celent](https://icedq.com/resources/case-studies/tsb-bank-data-migration-failure)).
- **BancoEstado**, Chile's largest bank by customers, migrated **14 million customers** to Mambu over five years (July 2020–June 2025), running parallel processing with zero customer disruption. The program won the **Celent 2025 Model Bank Award** and targets 90% mainframe reduction by 2027 ([Mambu](https://mambu.com/customer-stories/bancoestado); [Celent](https://celent.com/en/insights/banco-estado-moving-from-mainframe-to-next-gen-core)).
- **Oliver Wyman** explicitly recommends phased co-existence approaches over big-bang cutover, with active/active configurations mirroring requests on both cores until stability is achieved ([Oliver Wyman, May 2025](https://oliverwyman.com/our-expertise/insights/2025/may/next-gen-core-banking-modernization.html)).
- **CB RADAR** tracks **113 global core banking transformation projects** (2021–2025), with 72.5% reported complete or live and 84.5% choosing cloud deployment ([Core System Partners](https://coresystempartners.com/resources/core-banking-market-intelligence-report-2025/)).
- **Marginalen Bank** (Sweden) completed full migration to Mambu in 13 months on Azure Cloud ([Mambu](https://mambu.com/insights/press/mambu-and-avenga-marginalen-bank-cloud-migration)), demonstrating that smaller banks can execute faster full replacements where scale permits.

**Qualification:** Few banks have fully completed a progressive migration. BancoEstado is the most documented success — and it took five years. CB RADAR's 72.5% "complete/live" figure likely includes significant remaining scope. "Progressive migration" may function as a euphemism for indefinite coexistence: banks running new and old cores in parallel without ever fully decommissioning legacy systems.

**Opportunity by segment:**

- **Tier 1 banks:** Progressive migration is the only viable strategy — scale prohibits big-bang. Lloyds, BancoEstado, and Deutsche Bank exemplify multi-year phased approaches.
- **Tier 2 banks:** Mixed — some still attempt accelerated replacements, but TSB's failure is the cautionary reference point. The trend is strongly toward phased deployment.
- **Tier 3 banks:** Faster full replacements remain feasible due to smaller scale. Marginalen Bank completed in 13 months; Shawbrook went live on Thought Machine Vault Core in under nine months ([Thought Machine](https://www.thoughtmachine.net/press-releases/shawbrook)).

### Shift 2: Cloud-Native Core Infrastructure Becoming Table Stakes

Cloud-native deployment is moving from architectural aspiration to default selection criterion, with regulatory frameworks across all major markets now explicitly permitting cloud-hosted core banking.

**Evidence:**

- **84.5% cloud adoption** across 113 tracked core banking transformation projects ([CB RADAR/Core System Partners](https://coresystempartners.com/resources/core-banking-market-intelligence-report-2025/)).
- **SaaS core banking** is growing from **$12.12 billion to $50.62 billion** by 2033 at 19.6% CAGR ([SNS Insider/GlobeNewsWire](https://www.globenewswire.com/news-release/2026/01/07/3214621/0/en/SaaS-Based-Core-Banking-Software-Market-to-Reach-USD-50-62-Billion-by-2033-Owing-to-Banking-Digital-Transformation-and-Cloud-Based-Modernization-SNS-Insider.html)).
- **92% of UK financial institutions** have commenced modernization journeys; **83% plan second-generation cores**; 50% aim to complete within three to five years ([EY UK, October 2025](https://www.ey.com/content/dam/ey-unified-site/ey-com/en-uk/industries/banking-capital-markets/documents/ey-uk-core-banking-technology-modernisation-10-2025.pdf)).
- **Deutsche Bank** migrated 260 applications to Google Cloud, consolidated 12 million Postbank customers onto Google Spanner ([Google Cloud](https://cloud.google.com/blog/products/databases/deutsche-bank-scales-online-banking-platform-with-spanner)).
- Regulatory clearances are documented across major markets: **OCC** permits cloud with full bank accountability; **PRA** recognizes 40–90% of bank workloads could move to cloud within a decade ([TechUK](https://www.techuk.org/resource/banking-on-resilience-how-to-meet-the-pra-regulations-when-outsourcing-it.html)); **RBI** mandates India data residency but is launching its own cloud pilot ([Economic Times](https://economictimes.indiatimes.com/tech/technology/rbi-plans-2025-launch-of-cloud-services-countering-dominance-of-global-firms/articleshow/115405872.cms)).

**Opportunity by segment:**

- **Tier 1 banks:** Cloud-native is already the strategic direction — JPMorgan runs 70% of data on cloud, Deutsche Bank is migrating to Google Cloud. These banks build cloud-first but migration takes years.
- **Tier 2 banks:** Active cloud migration; building societies and specialist banks increasingly select cloud-native as the default criterion. Shawbrook, Leeds Building Society, and West Brom Building Society are all deploying cloud-native cores.
- **Tier 3 banks:** Dependent on vendor cloud readiness. Community banks exploring (Mascoma Bank on Thought Machine) but OCC's 2025 RFI signals regulatory concern about core provider concentration in cloud environments.

### Shift 3: Composable Banking Architecture Reaching Production

Composable banking — modular, API-first platforms with independently deployable components — has moved from Gartner thesis to production reality at fifteen or more named banks. The evidence base is strong but comes with a critical qualification.

**Evidence:**

- **Thought Machine Vault Core** is in production at Lloyds Banking Group, Standard Chartered (Mox), Intesa Sanpaolo (isybank), ING Bank Śląski, Shawbrook, and Judo Bank ([Thought Machine](https://www.thoughtmachine.net/case-studies)).
- **10x Banking** powers Chase UK (2.5 million customers, £15 billion+ deposits), Westpac's institutional platform, West Brom Building Society, and Co-operative Bank New Zealand ([10x Banking](https://www.10xbanking.com/success-stories/10x-banking-teams-up-with-chase-to-create-next-generation-digital-banking-platform)).
- **Mambu** runs at BancoEstado (14 million customers), Leeds Building Society (£30 billion AUM), Marginalen Bank, and Chetwood Bank, with 200+ clients globally and 60+ new customers in 2025 alone ([Mambu](https://mambu.com/en/customer/leeds-building-society)).
- **Judo Bank** completed full core migration to Thought Machine and reported a **50% reduction in product development time** and 4x faster system performance ([Thought Machine](https://www.thoughtmachine.net/case-studies/judo-bank)).
- The market remains highly fragmented: the top three vendors control only **30.1%** of transformation deal share ([CB RADAR/Core System Partners](https://coresystempartners.com/resources/core-banking-market-intelligence-report-2025/)).

**Qualification:** No Tier 1 bank has fully replaced its monolithic core with a composable platform. All major deployments are either digital subsidiaries (isybank, Mox, Chase UK), specific product lines (Shawbrook commercial SME lending, Leeds savings), or progressive migrations still in progress (Lloyds, BancoEstado). Composable banking is production-proven *alongside* monolithic cores — not *replacing* them entirely. Gartner's composable banking thesis describes the architectural direction; the market reality is coexistence, not displacement.

**Opportunity by segment:**

- **Tier 1 banks:** Deploying composable for new product lines and digital subsidiaries while maintaining legacy cores. Full replacement remains aspirational.
- **Tier 2 banks:** The sweet spot. Shawbrook, ING Bank Śląski, Leeds Building Society, and Judo Bank demonstrate that mid-market banks can execute composable deployments within 9–18 months.
- **Tier 3 banks:** Community banks are beginning to enter — Mascoma Bank signed Thought Machine for cloud-native migration — but adoption is early-stage.

### Shift 4: Business Banking Digitization Creating a Separate Modernization Wave

Business banking has structurally different requirements from retail account products — different competitive sets, different buyers, different revenue pools, and an independent modernization cycle. It is not a sub-topic of retail core modernization; it is a distinct wave.

**Evidence:**

- **MSMEs account for 21% of global banking revenue pools** (~$1.18 trillion in 2024), growing at **7% annually** — faster than either retail or corporate banking ([McKinsey](https://www.mckinsey.com/industries/financial-services/our-insights/digital-led-with-a-human-touch-the-next-era-in-small-business-banking)).
- **Mercury:** $650 million annualized revenue, $20 billion in deposits, GAAP profitable for three consecutive years, applied for a national bank charter ([Fortune](https://fortune.com/2025/11/07/exclusive-mercury-fintech-valuation-650-million-2025-annualized-revenue-immad-akhund-interview/)).
- **Tide:** 1.8 million global members, **14% UK SME market share**, expanded to India (surpassed 1 million members within three years) and France ([Tide](https://www.tide.co/blog/tide-update/major-milestones-in-2025-and-a-look-ahead-to-2026-a-letter-from-our-ceo/)).
- **Virtual accounts:** 86% of banks have invested or are planning to invest in virtual account management ([Datos Insights via CashFac](https://cashfac.com/resource/news-blog/why-banks-are-adopting-virtual-account-management/)). JPMorgan, Bank of America, Citi, and Wells Fargo have all launched VAM systems.
- **UK digital-first banks** captured approximately one-third of MSME customers in five years ([McKinsey](https://www.mckinsey.com/industries/financial-services/our-insights/digital-led-with-a-human-touch-the-next-era-in-small-business-banking)).
- **Brex** was acquired by Capital One for $5.15 billion (January 2026), validating the strategic value of business banking fintech capabilities and demonstrating that standalone business banking fintechs eventually consolidate with banks ([Sacra/CBInsights](https://sacra.com/c/brex)).

**Opportunity by segment:**

- **Tier 1 banks:** Investing in virtual accounts and digital SME platforms as overlays on legacy cores. JPMorgan, BofA, Citi, and Wells Fargo have deployed proprietary VAM solutions.
- **Tier 2 banks:** Most exposed to fintech disruption. Need modern product engines for cash management, virtual accounts, and multi-entity structures to compete with Mercury and Tide.
- **Tier 3 banks:** Community banks are traditionally strong in SME relationships but lack digital tooling. The relationship advantage erodes as digital-native expectations become baseline.

### Shift 5: Open Banking Mandates Exposing Account Infrastructure Limitations

Open banking regulations are scaling across all major markets but — critically — most mandates do not force core replacement. Their value is in exposing legacy limitations and accelerating the strategic case for modernization, not in mandating specific infrastructure changes.

**Evidence:**

- **UK OBIE:** 15.1 million monthly active users (one in three UK adults), **22 billion annual API calls**, growing 36% year-over-year. Payment initiation services growing 66% YoY. One million account switches in 2025 via CASS ([OBIE](https://www.openbanking.org.uk/insights/2-billion-api-calls-and-15-million-users-a-landmark-month-for-open-banking-in-the-uk/); [CASS](https://www.currentaccountswitch.co.uk/news-insights/switching-data/current-account-switch-service-records-over-one-million-switches-in-2025/)).
- **India Account Aggregator:** **390.9 million cumulative consents**, **2.1 billion linked accounts** (60%+ of India's total financial accounts), 913 FIUs, 177 FIPs. MSME loan processing reduced from weeks to 48 hours ([Sahamati](https://sahamati.org.in/aa-dashboard/); [Business Standard](https://www.business-standard.com/finance/news/aa-ecosystem-consent-processing-up-78-in-fy25-shows-sahamati-data-125031301053_1.html)).
- **USA Section 1033:** Finalized October 2024 with an April 2026 deadline for the largest institutions, but enforcement is blocked by federal court injunction. The rule remains on the books; banks are building API infrastructure regardless ([PYMNTS](https://www.pymnts.com/bank-regulation/2026/data-aggregators-push-secure-access-as-rule-1033-rewrite-looms/); [KPMG](https://kpmg.com/us/en/articles/2024/1033-open-banking-cfpb-final-rule-reg-alert.html)).
- **EU PSD3/PSR:** Provisional agreement reached November 2025. Transition to the Payment Services Regulation (directly applicable) and PSD3 directive (18-month national transposition) expected H2 2027–early 2028 ([Norton Rose Fulbright](https://www.nortonrosefulbright.com/en/knowledge/publications/cedd39c6/psd3-and-psr-from-provisional-agreement-to-2026-readiness)).

**Nuance:** Most open banking mandates are wrappable via API gateways and middleware — they do not force core replacement. PSD2/PSD3 and Section 1033 can be satisfied by layering an API gateway on top of the existing core. The value of open banking as a core modernization driver is indirect: it exposes the limitations of legacy architectures (real-time data access, consent management, granular product APIs) and strengthens the strategic case for deeper investment. Only in India, where the Account Aggregator framework has scaled to 2.1 billion linked accounts, has open banking created infrastructure-level demand that tests the limits of legacy cores.

**Opportunity by segment:**

- **All tiers:** Open banking compliance is universal. The primary buying event is API infrastructure for Section 1033, PSD2/PSD3, and Account Aggregator — not core replacement.
- **Tier 2 banks:** Most impacted operationally. Lack the engineering teams to build custom API layers; need vendor-delivered open banking compliance platforms.

### Shift 6: Deposit Competition Forcing Product Agility

Neobanks are winning the battle for new deposit relationships — not by offering marginally better products, but by operating on fundamentally different infrastructure that enables a 10:1 time-to-market advantage over legacy platforms.

**Evidence:**

- **40% of new US account openings** now go to neobanks, surpassing large nationwide banks at 38% ([Simon-Kucher 2025](https://www.simon-kucher.com/en/insights/neobanking-united-states-acceleration-amid-uneven-ground)).
- **Chime** captures **12.8% of new checking accounts** — more than Chase (8.4%) or Wells Fargo (7.1%) individually. Active members: 9.5 million ([American Banker/J.D. Power](https://www.americanbanker.com/news/chime-leads-in-new-checking-accounts-opened)).
- **SoFi:** $37.5 billion in deposits, growing $4.6 billion in a single quarter. Net interest margin: 5.72%. First billion-dollar revenue quarter in Q4 2025 ([SoFi Q4 2025 Earnings](https://investors.sofi.com/financials/quarterly-results/default.aspx)).
- **UK neobanks** hold material deposit volumes: Revolut £30.2 billion ([Revolut](https://www.revolut.com/financial-statements/)), Monzo £16.6 billion ([Monzo](https://monzo.com/annual-report/2025)), Starling £12.1 billion ([Starling](https://www.starlingbank.com/investors/2025/annual-report-2025/)). Combined, the top UK neobanks hold over £59 billion in deposits.
- **Time-to-market gap:** Legacy cores require 9–18 months for a new deposit product; modern platforms can deliver equivalent capability in weeks ([DUNNIXER](https://www.dunnixer.com/insights/information/banking/us/how-long-does-core-banking-modernization-take); [Celent/BancoEstado](https://celent.com/en/insights/banco-estado-moving-from-mainframe-to-next-gen-core)). BancoEstado reduced product launches from six months to weeks after migrating to Mambu ([Celent](https://celent.com/en/insights/banco-estado-moving-from-mainframe-to-next-gen-core)).
- **The "soft switching" pattern** dominates: 52% of new checking accounts are additions, not replacements. Consumers are multi-banking — opening fintech accounts while retaining traditional bank relationships. Banks should worry less about switching and more about losing primary deposit status ([J.D. Power/American Banker](https://www.americanbanker.com/news/chime-leads-in-new-checking-accounts-opened)).

**The overlay alternative:** Product pricing overlay tools (Zafin, SunTec) can address deposit pricing agility without core replacement. A Tier 1 US bank achieved a **>50% increase in CD approved volumes** in eight weeks via a Zafin deployment — no core change required ([Zafin](https://zafin.com/insights/banking-blueprints/modernize/deposit-modernization-single-product-case-study/)). Overlays solve the most acute pricing problem but cannot address deeper product structure limitations: goal-based savings vaults, group accounts, conditional interest, and savings circles all require flexible product engines that legacy cores cannot easily provide.

**Opportunity by segment:**

- **Tier 1 banks:** Losing checking account acquisition share to Chime and SoFi. Responding with digital feature parity, high-yield savings offers, and pricing overlays.
- **Tier 2 banks:** Most vulnerable — lack both the brand strength of Tier 1 and the agility of neobanks. This is the segment where deposit competition creates the most urgent modernization pressure.
- **Tier 3 banks:** Community banks compete on relationships, but digital expectations are rising. Community bank NIM reached 3.77% in Q4 2025 — the highest since 2018 ([FDIC QBP](https://www.fdic.gov/news/speeches/2026/fdic-quarterly-banking-profile-fourth-quarter-2025)) — providing financial capacity to invest.

### Shift 7: Embedded Banking Requiring Modern Account Infrastructure

The banking-as-a-service model is growing — $21.4 billion to an estimated $105.8 billion by 2035 ([Grand View Research](https://grandviewresearch.com/industry-analysis/banking-as-a-service-market-report)) — but the Synapse collapse fundamentally restructured what infrastructure BaaS demands. The middleware model is dead. Banks pursuing embedded banking must own the ledger on a modern, real-time platform.

**Evidence:**

- **Synapse collapse** (April 2024): **$265 million in deposits frozen**, 100,000+ consumers affected. Partner banks were unable to retrieve accurate customer-level balance records because Synapse operated as middleware between fintechs and banks, maintaining its own ledger that diverged from the banks' systems ([Yale Journal of International Affairs](https://www.yalejournal.org/publications/the-synapse-collapse)).
- **FDIC proposed the "Synapse Rule"** (October 2024): banks must ensure custodial deposit account balances are accurate and reconciled daily, with the ability to calculate per-depositor insurance coverage within 24 hours ([FDIC](https://www.fdic.gov/news/press-releases/2024/fdic-proposes-deposit-insurance-recordkeeping-rule-banks-third-party)).
- **Federal Reserve issued a cease-and-desist** against Evolve Bank (June 2024) for deficiencies in AML, risk management, and consumer compliance across its fintech partnerships. Evolve cannot establish new fintech partners without Federal Reserve approval ([Federal Reserve](https://www.federalreserve.gov/newsevents/pressreleases/enforcement20240614a.htm)).
- **Westpac** launched a BaaS platform in 18 months using 10x Banking and AWS — the Tier 1 model for bank-owned modern core enabling embedded distribution ([10x Banking](https://www.10xbanking.com/banking-as-a-service)).

**Post-Synapse architectural implications:** Banks pursuing embedded banking must maintain real-time customer-level deposit visibility through fintech intermediaries. Legacy cores — designed for branch-mediated, single-institution deposit management — are structurally inadequate for multi-tenant, partner-mediated deposit relationships. The shift is from "BaaS through middleware" to "BaaS through modern core."

**AI in account operations** is an adjacent development worth noting. CIBC launched CRTeX, an AI-enabled personalization engine for omni-channel engagement ([CIBC](https://www.newswire.ca/news-releases/cibc-launches-cibc-crtex-tm-an-ai-enabled-client-personalization-amp-engagement-engine-to-further-its-industry-leading-digital-capabilities-and-enhance-client-experiences-890473929.html)). Wells Fargo is deploying AI agents company-wide via Google Agentspace ([Fast Company](https://www.fastcompany.com/91380316/wells-fargo-is-rolling-out-companywide-ai-it-says-everyone-from-branch-tellers-to-investment-bankers-will-benefit)). Synthetic identity fraud reached $3.3 billion in exposure during H1 2025 ([Federal Reserve Bank of Boston](https://www.bostonfed.org/news-and-events/news/2025/04/synthetic-identity-fraud-financial-fraud-expanding-because-of-generative-artificial-intelligence.aspx)). AI in account lifecycle operations is real but analyst coverage remains thin; the evidence base is vendor-driven rather than independently validated.

**Opportunity by segment:**

- **Tier 1 banks:** Selectively entering BaaS — Westpac and Goldman Sachs (Marcus platform) demonstrate the model. Modern core is a prerequisite.
- **Tier 2 banks:** The primary BaaS provider segment. Banks like Cross River are positioned as BaaS-enabling institutions, but post-Synapse regulatory scrutiny is rising.
- **Tier 3 banks:** Most exposed. Small banks that entered BaaS partnerships (Evolve Bank, Synapse partner banks) without adequate infrastructure face existential regulatory risk.

---

## 4. The Engagement Landscape

These structural shifts produce specific buying events — projects that banks commission technology vendors to deliver.

### Progressive Core Migration
**Shifts:** 1, 2, 3. **Primary buyer:** Tier 1–2 banks. The multi-year, product-by-product migration from legacy monolithic cores to cloud-native composable platforms. **Named examples:** BancoEstado (14 million customers migrated to Mambu over five years, Celent 2025 Model Bank Award), Lloyds Banking Group (Thought Machine license extended to 2029, Vault Core in production), Leeds Building Society (Mambu partnership, pilot digital savings launched in under one year).

### Digital Account Platform
**Shifts:** 2, 6. **Primary buyer:** Tier 2–3 banks. Wrapping the legacy core with a modern digital account experience — mobile onboarding, real-time balance visibility, self-service product management — without replacing the underlying account processing engine. This is the "augment the core" path. Digital banking platform vendors (Alkami at $444 million revenue with 33% growth, Q2 at $795 million with 14% growth, Backbase at ~$365 million) serve this engagement type. The buyer seeks consumer-grade digital experience on legacy infrastructure.

### Business Banking Build
**Shift:** 4. **Primary buyer:** Tier 2 banks. Cash management modernization, virtual account management, multi-entity treasury structures, and SME digital banking platforms. This engagement has a distinct buyer (commercial banking head or CFO), distinct vendors (iGTB, Finastra, Kyriba, Bottomline, CashFac), and an independent budget from retail core modernization. 86% of banks have invested or plan to invest in virtual accounts ([Datos Insights](https://cashfac.com/resource/news-blog/why-banks-are-adopting-virtual-account-management/)).

### BaaS Enablement
**Shift:** 7. **Primary buyer:** Tier 2 banks. Modern account infrastructure for fintech partnerships and embedded banking distribution. Post-Synapse, the requirement is real-time customer-level deposit visibility through fintech intermediaries. The FDIC's proposed Synapse Rule and Federal Reserve enforcement actions against Evolve Bank create a compliance floor that legacy cores cannot easily satisfy.

### Deposit Innovation Platform
**Shift:** 6. **Primary buyer:** Tier 2–3 banks. Product configuration agility for competitive deposit products — high-yield savings, goal-based vaults, conditional interest, subscription banking. Buyers face a strategic choice: product pricing overlays (Zafin, SunTec) for immediate wins in weeks, or core replacement for structural product flexibility in months-to-years. Many banks pursue both on parallel tracks.

### Open Banking Compliance
**Shift:** 5. **Primary buyer:** All tiers. API infrastructure for Section 1033 (US), PSD2/PSD3 (Europe), and Account Aggregator (India). The buying event is compliance-driven, typically satisfied with API gateways and middleware layers rather than core replacement. India's Account Aggregator ecosystem — 2.1 billion linked accounts, 913 FIUs — creates the most demanding infrastructure requirements.

---

## 5. Competitive Landscape

### Legacy incumbents

| Vendor | Revenue | Position | Vulnerability |
|---|---|---|---|
| FIS | $10.7B total; $7.3B Banking Solutions ([FIS 10-K](https://www.stocktitan.net/sec-filings/FIS/10-k-fidelity-national-information-services-inc-files-annual-report-faa6cf780c27.html)) | Dominant US core + issuer processor. Acquired TSYS for $13.5B (Jan 2026). Finxact cloud-native core in portfolio | Integration complexity; mid-market finds it over-engineered; Finxact still early in customer traction |
| Fiserv | $21.2B total ([Fiserv](https://investors.fiserv.com)) | #1 US core account processing (DNA, Signature, Premier). Dominant community bank/CU position (25.9% share, 1,155 CU clients) | Core banking revenue buried in larger total; Signature/Premier architecturally aging; DNA modernization slow |
| Jack Henry | ~$2.4B ([Jack Henry IR](https://ir.jackhenry.com)) | >99% core retention rate; 46 core renewals in H1 FY2025; winning larger FIs | US-only; no cloud-native core; dependent on community bank segment facing consolidation |
| Temenos | $1.1B; ARR $860M ([Temenos](https://www.temenos.com/press_release/temenos-announces-q4-2025-results-22tw4tk10/)) | #1 IBS Intelligence Sales League Table for 20 consecutive years; 950+ clients across 150+ countries | SaaS transition incomplete; 2024 short-seller attack damaged credibility; margins under pressure |
| Infosys Finacle | Est. $500–700M (not separately disclosed) | SBI (flagship), 100+ banks globally; 29.8% of customers in India | Cloud-native story weaker than pure-play challengers; parent priorities may not align |
| TCS BaNCS | Est. $400–600M (not separately disclosed) | Gartner MQ Leader (Europe 2025); 200+ customers globally | SaaS traction slower than cloud-native challengers |
| Oracle FLEXCUBE | Est. $300–500M (not separately disclosed) | 130+ countries; Access Bank (60M customers) completed modernization Sep 2025 | Aging architecture; lowest Gartner Peer rating (3.9/5) among major vendors |
| Finastra | ~$1.85B total (private) | Treasury & Capital Markets serves 48 of top 50 banks. ME/Asia core banking unit being explored for sale | Highly leveraged (Vista Equity); strategic uncertainty; TCM division being sold to Apax for ~$2B |

### Modern challengers

| Vendor | Revenue / Funding | Position | Limitation |
|---|---|---|---|
| Thought Machine | £47.6M revenue; $570M total funding; $2.7B valuation ([CityAM](https://www.cityam.com/thought-machine-lands-45m-funding-round-after-losses-widen/)) | Cloud-native core at Lloyds, Standard Chartered, Intesa, Judo Bank, Shawbrook. Dominant Tier 1 next-gen vendor | Revenue declining slightly; losses widening (£71.2M); valuation cut ~40% by Molten Ventures |
| Mambu | Est. ~$160M revenue; €4.9B valuation ([Acton Capital](https://www.actoncapital.com/news/mambu-closes-eu235m-seriese-at-a-eu4-9b-valuation)) | SaaS-only cloud-native core; 200+ clients; 60+ new in 2025; BancoEstado, Leeds, Marginalen | Profitability unproven; limited Tier 1 traction; valuation may be stretched |
| 10x Banking | $187M total funding (private) | Chase UK (2.5M customers, £15B+ deposits), Westpac, West Brom, Co-op Bank NZ ([10x Banking](https://www.10xbanking.com)) | Concentrated customer base; profitability unknown; limited geographic scale |
| Finxact (FIS) | Integrated into FIS Banking Solutions | Cloud-native core within FIS portfolio; 13 implementations per CB RADAR | Still early in production; internal competition with FIS legacy products |
| Pismo (Visa) | Acquired by Visa for $1B (Jan 2024) ([Visa](https://investor.visa.com/news/news-details/2024/Visa-Completes-Acquisition-of-Pismo/)) | Cloud-native core + issuer processing; Citigroup DDA, European expansion accelerating | Visa ownership may create conflicts with non-Visa banks; scale still limited outside Brazil |

### Digital banking and product specialists

| Vendor | Revenue | Position |
|---|---|---|
| Alkami | $444M (+33% YoY); ARR $480M ([Alkami](https://investors.alkami.com/2026-02-25-Alkami-Announces-Fourth-Quarter-2025-Financial-Results)) | Cloud-native digital banking for US community banks/CUs; 22.4M registered users |
| Q2 Holdings | $795M (+14%); subscription ARR $780M ([Q2](https://www.nasdaq.com/press-release/q2-holdings-inc-announces-fourth-quarter-and-full-year-2025-financial-results-2026-02)) | Digital banking platform; completed AWS migration Jan 2026; 8 Enterprise/Tier 1 wins in Q4 2025 |
| Backbase | Est. ~$365M; €2.5B valuation | Engagement banking platform; 150+ clients globally; consistent >30% ARR growth |
| Zafin | Est. $50–100M (private) | Product pricing overlay; Tier 1 US bank references; CNBC Top Fintech 2025 |
| SunTec | Est. $80–120M (private) | Pricing, billing, revenue management; 150–170 clients across 45+ countries |

### Business banking specialists

| Vendor | Revenue / Scale | Position |
|---|---|---|
| Finastra (TCM) | ~$400M (being sold to Apax for ~$2B) | Treasury and cash management; 48 of top 50 banks; Celent leader |
| Bottomline (Thoma Bravo) | ~$530M+ annualized | Corporate payments and cash management; $16T annual payments; 90 Fortune 100 clients |
| Kyriba | Est. $200–300M (private) | Treasury management; 3,400 clients; 9,900+ banks connected; Euromoney Best TMS 2025 |
| Intellect iGTB | ~$380M annualized (multi-segment) | Transaction banking; handles 23% of cross-border MNC sweeping flows; 100+ banking groups |

### The defining competitive question

Is the market moving to "replace the core" or "augment the core"? The evidence supports both narratives simultaneously:

- **For replacement:** 92% of UK FIs have commenced modernization (EY). Temenos has 950+ core clients. Access Bank completed a full Oracle FLEXCUBE modernization for 60 million customers. Chase UK built entirely on 10x's cloud-native core and reached 2.5 million customers.
- **For augmentation:** The legacy Big 3 (FIS/Fiserv/Jack Henry) control the vast majority of US banking relationships. Digital banking platforms (Alkami, Q2, Backbase) are growing 14–33% by wrapping legacy cores. Zafin and SunTec prove pricing can be externalized without core replacement. Wells Fargo integrated 65 fragmented systems into its Vantage platform without replacing the core.

The market is bifurcating by tier. Tier 1 banks with resources and strategic urgency pursue multi-year core transformation. The vast majority of Tier 2–4 banks augment — wrapping legacy cores with modern digital layers, externalizing pricing and origination, and extending core life by a decade or more. The critical competitive gap is in the **mid-market**: no vendor delivers genuinely integrated, affordable, cloud-native account infrastructure for banks between $10 billion and $100 billion in assets. Legacy incumbents are over-engineered and expensive. Modern challengers are designed for fintechs and digital subsidiaries. The mid-market bank that wants to modernize its core — not build a digital subsidiary alongside it — has limited options.

---

## 6. Target Universe

Institutions with publicly signaled account products or core banking modernization activity, organized by geography, tier, and horizon.

### United States

| Institution | Tier | Signal | Horizon | Source |
|---|---|---|---|---|
| JPMorgan Chase | 1 | Selected Thought Machine for US retail core; Chase UK on 10x (2.5M customers, £15B+ deposits); 70% of data on cloud | Near-term (0–2yr) | [Finextra](https://www.finextra.com/newsarticle/38943/chase-taps-10x-for-uk-digital-bank); [10x Banking](https://www.10xbanking.com/success-stories/10x-banking-teams-up-with-chase-to-create-next-generation-digital-banking-platform) |
| Wells Fargo | 1 | $900M+ incremental tech spend; Vantage digital banking platform (integrated 65 systems); AI agents via Google Agentspace | Near-term (0–2yr) | [InfotechLead](https://infotechlead.com/cio/wells-fargo-says-digital-transformation-and-technology-investments-support-customer-growth-efficiency-and-operational-performance-in-q4-2025-93120); [Fast Company](https://www.fastcompany.com/91380316/wells-fargo-is-rolling-out-companywide-ai-it-says-everyone-from-branch-tellers-to-investment-bankers-will-benefit) |
| Citi | 1 | Actively recruiting "Head of Core Banking Transformation" (Mar 2026); building future-state digital banking platform; initial focus LATAM, then global rollout | Near-term (0–2yr) | [Citi Careers](https://jobs.citi.com/job/jersey-city/head-of-core-banking-transformation/287/92309329792) |
| Mascoma Bank | 3 | Signed Thought Machine for cloud-native core migration; $2.6B mutual savings bank | Near-term (0–2yr) | [Thought Machine](https://www.thoughtmachine.net/press-releases/thought-machine-signs-mascoma-bank-to-take-community-banking-into-the-cloud) |
| Hanover Bank | 3 | Completed core banking system conversion (Feb 2025) | Completed | [GlobeNewsWire](https://www.globenewswire.com/news-release/2025/04/22/3065416/0/en/) |

### India

| Institution | Tier | Signal | Horizon | Source |
|---|---|---|---|---|
| SBI | 1 | Two-year core banking modernization: Unix→Linux migration, microservices, private cloud, 300 APIs via sandbox; "modernising as we run the ship" | Near-term (0–2yr) | [BW Businessworld](https://www.businessworld.in/article/sbi-targets-two-year-timeline-to-modernise-core-banking-system-md-579751) |
| HDFC Bank | 1 | Core banking system migration to new engineered platform; multi-cloud active-active architecture; 97% digital transactions | Near-term (0–2yr) | [HDFC Bank](https://www.hdfcbank.com/personal/about-us/news-room/press-release/2024/q2/hdfc-bank-plans-migration-of-core-banking-system-to-new-engineered-platform-to-enhance-robustness-a) |
| Axis Bank | 1 | Launched "open" by Axis Bank (digital entity); 15M+ MAU mobile; DevSecOps and cloud infrastructure | Medium-term (2–5yr) | [Axis Bank Annual Report 2025](https://www.axisbank.com/annual-reports/2024-2025/pdf/s2.pdf) |

### UK / Europe

| Institution | Tier | Signal | Horizon | Source |
|---|---|---|---|---|
| Lloyds Banking Group | 1 | Acquired additional £10M stake in Thought Machine (Mar 2025); Vault Core in production; core transformation is "key part of three-year strategic plan"; license extended to 2029 | Near-term (0–2yr) | [Thought Machine](https://www.thoughtmachine.net/case-studies/lloyds-bank) |
| HSBC | 1 | $1.8B technology cost reallocation; decommissioned 1,165 legacy apps in 2025; plans to retire 1/3 of app portfolio by 2028 | Near-term (0–2yr) | [Kingy AI/HSBC](https://kingy.ai/news/hsbc-ai-transformation-digital-banking/) |
| Standard Chartered | 1 | Mox Bank on Thought Machine since 2020; "Fit for Growth" $754M run-rate savings; targeting $1.3B total savings | Near-term (0–2yr) | [InfotechLead](https://infotechlead.com/networking/standard-chartered-steps-up-digital-transformation-and-ai-strategy-in-2025-under-fit-for-growth-program-93884) |
| Deutsche Bank | 1 | 260 apps migrated to Google Cloud; 12M Postbank customers on Google Spanner; Project Magellan (€1B) | Near-term (0–2yr) | [Google Cloud](https://cloud.google.com/blog/products/databases/deutsche-bank-scales-online-banking-platform-with-spanner) |
| Intesa Sanpaolo | 1 | isybank launched Jun 2023 on Thought Machine + Google Cloud; 300K migrated customers; targeting €800M annual savings from 2026 | Near-term (0–2yr) | [Thought Machine](https://www.thoughtmachine.net/case-studies/intesa-sanpaolo) |
| ING Bank Śląski | 2 | Live on Thought Machine Vault Core since Dec 2021; first Polish bank on cloud-native core; expanding via NextGen Architecture | Near-term (0–2yr) | [Thought Machine](https://www.thoughtmachine.net/press-releases/ing-bank-slaski-selects-thought-machine-and-goes-live-with-vault-to-further-enhance-customer-experience) |
| Leeds Building Society | 2 | Mambu partnership for multi-year core modernization; pilot digital savings launched in <1 year; £30B AUM | Near-term (0–2yr) | [Mambu](https://mambu.com/en/customer/leeds-building-society) |
| West Brom Building Society | 2 | 10x Banking + Deloitte for multi-phase cloud-native core transformation (May 2025); 400K+ members | Near-term (0–2yr) | [10x Banking](https://www.10xbanking.com/news/west-brom-building-society-announces-major-digital-transformation-with-deloitte-and-10x-banking) |
| Shawbrook | 2 | Live on Thought Machine Vault Core (Aug 2025); deployed in <9 months; commercial SME lending | Completed | [Thought Machine](https://www.thoughtmachine.net/press-releases/shawbrook) |
| Judo Bank | 2 | Full core migration to Thought Machine completed Apr 2025; 50% reduction in product dev time | Completed | [Thought Machine](https://www.thoughtmachine.net/case-studies/judo-bank) |

### Rest of World

| Institution | Tier | Signal | Horizon | Source |
|---|---|---|---|---|
| BancoEstado (Chile) | 1 | Celent 2025 Model Bank: 14M customers migrated to Mambu; targets 90% mainframe reduction by 2027 | Near-term (0–2yr) | [Celent](https://celent.com/en/insights/banco-estado-moving-from-mainframe-to-next-gen-core); [Mambu](https://mambu.com/customer-stories/bancoestado) |
| Westpac (Australia) | 1 | 10x Banking partnership for institutional platform + BaaS; technology simplification through 2028 | Near-term (0–2yr) | [10x Banking](https://www.10xbanking.com/success-stories/10x-and-westpac-partner-to-launch-a-robust-scalable-and-flexible-transaction-banking-platform) |
| Access Bank (Nigeria) | 1 | Completed Oracle FLEXCUBE core modernization Sep 2025; 60M customers; 35M+ txns/day across 24 markets | Completed | [Oracle](https://www.oracle.com/news/announcement/access-bank-completes-major-core-banking-modernization-with-oracle-2025-09-16/) |
| Co-operative Bank (NZ) | 2 | 10x Banking selected for full-platform migration (Aug 2025); 180K+ customers; multi-year phased approach | Near-term (0–2yr) | [10x Banking](https://www.10xbanking.com/news/the-co-operative-bank-selects-10x-banking) |
| Burgan Bank (Kuwait) | 2 | Selected TCS BaNCS May 2024; consolidating legacy into universal banking; 160+ branches | Near-term (0–2yr) | [TCS](https://www.tcs.com/content/tcs/global/en/who-we-are/newsroom/press-release/burgan-bank-selects-tcs-bancs-transform-core-banking) |
| NS&I (UK, Government) | Govt | Replacing legacy core with SBS cloud-native SBP Digital Core; partnering with Atos, IBM, Sopra Steria | Near-term (0–2yr) | [BusinessWire](https://www.businesswire.com/news/home/20250724610197/en/) |

**Geographic distribution:** UK dominates the active transformation pipeline (10 institutions), followed by the US (5), India (3), and Australia (2). The UK's concentration reflects both regulatory pressure (PRA operational resilience, EY finding that 92% of UK FIs have commenced modernization) and the competitive intensity of a market where Revolut, Monzo, and Starling collectively hold £59 billion in neobank deposits.

**Tier distribution:** Tier 1 banks (15 institutions) represent the largest transformation programs but are also the most likely to build in-house. Tier 2 banks (7 institutions) are the sweet spot for vendor-delivered solutions — large enough to justify platform investment, not large enough to build proprietary cores. The evidence base for Tier 3 community bank adoption (Mascoma, Hanover) is growing but early-stage.

---

# PART II — THE ADVISORY

---

## 7. Zeta's Position

Zeta's account products assets (Tachyon product lines) and operational infrastructure (Evolution Fabric, Quark domain hubs) map to the structural shifts identified in Part I — with the critical advantage that Tachyon is production-validated in the US market.

**Tachyon's production footprint.** Tachyon Credit Cards powers three credit card programs in the USA. Tachyon DDA powers multiple demand deposit account programs — including health benefits (Optum) and loyalty/rewards programs — all using Photon for payment rail processing. This establishes Tachyon as a production-grade account platform with US market evidence. The remaining gap is not product readiness but market visibility and breadth: existing deployments are purpose-specific programs (credit cards, benefits, rewards) rather than full-service retail or business banking core replacements. Competitors have named Tier 1 core banking references — Thought Machine has Lloyds, Standard Chartered, Intesa Sanpaolo, and Judo Bank; Mambu has BancoEstado (14 million customers); 10x has Chase UK. Tachyon's production evidence must be packaged into referenceable case studies and extended into broader banking use cases.

| Structural Shift | Zeta Asset | Readiness |
|---|---|---|
| Progressive core replacement | Tachyon Kernel + DDA | **Production-validated for purpose-specific programs** — three credit card programs and multiple DDA programs (health benefits, loyalty/rewards) in US production. Extension to full-service retail/business core replacement requires broader account product coverage |
| Cloud-native core infrastructure | Tachyon (all product lines) | **Validated** — US production deployments confirm cloud-native architecture in operation. No CB RADAR entries or analyst coverage yet — a visibility gap, not a capability gap |
| Composable banking architecture | Tachyon + Quark domain hubs | **Strong** — Quark's pre-modeled operational domains are a genuinely differentiated concept. No competitor ships pre-built domain hubs with operational models. Tachyon's production deployments validate the underlying account infrastructure |
| Business banking digitization | Tachyon Loans + DDA (business) | **Weak** — no evidence of virtual account management, cash management, multi-entity structures, or any business banking capability. Competing against Finastra, iGTB, Kyriba, Bottomline |
| Open banking mandates | Trust Fabric + Tachyon APIs | **Partial** — Trust Fabric's consent and identity capabilities are relevant for KYC/onboarding and Account Aggregator compliance. But open banking is wrappable — not a core replacement driver |
| Deposit competition / product agility | Tachyon DDA | **Medium** — Tachyon DDA is in production for purpose-specific deposit programs (health benefits, rewards). Extension to configurable retail deposit products (goal-based savings, conditional interest, subscription banking) is a product roadmap question, not a platform readiness question |
| Embedded banking / BaaS | Tachyon + Cloud Fabric | **Architectural advantage** — cloud-native, multi-tenant by design intent. Post-Synapse BaaS requires real-time customer-level deposit visibility, which modern architecture enables. But: no BaaS-specific packaging or regulatory wrapper |
| AI in account operations | Evolution Fabric (Hub) + Agent Fabric | **Differentiated** — the structural differentiator. No competitor combines account infrastructure with an explicit operational model and AI agent governance |

### The differentiator hypothesis

The Evolution Fabric + Tachyon combination — an operational model (Hub + Agent Fabric) paired with an account platform (Tachyon) — is a positioning no competitor occupies. Thought Machine delivers account infrastructure. Mambu delivers account infrastructure. Neither delivers an operational substrate that makes account operations explicit, governed, and AI-ready. Evolution Fabric is the most fully articulated product in Zeta's portfolio: the thesis that banks need not just an account platform but an operational layer for their account domains is genuinely differentiated.

But state this honestly: the hypothesis is untested in the market. No bank has adopted this combination. "Differentiated positioning" and "winning deals" are different things. The narrative must connect to concrete bank outcomes — reduced operational cost, faster product launches, governed AI deployment — not thesis articulation alone.

### The Photon/Electron adjacency

Tachyon accounts are the ledger endpoints for Photon payment flows. Cross-sell from payments to accounts is architecturally natural — a bank running Photon for card issuance and payments has a logical path to Tachyon for account infrastructure. But core banking is a different buying center (CTO/CIO vs. payments head). FIS's experience cross-selling Finxact alongside legacy core products shows that intra-company cannibalization and organizational resistance are real barriers. The adjacency is real; the conversion is not automatic.

---

## 8. Where to Play — Right to Play / Right to Win Assessment

| Segment | Right to Play | Right to Win | Recommendation |
|---|---|---|---|
| **Progressive core migration (Tier 2 US)** | **Strong.** $15–20B vendor-addressable TAM. 53% bank dissatisfaction with core providers. Mid-market gap is clear — no vendor delivers genuinely integrated, affordable, cloud-native account infrastructure for banks between $10B and $100B in assets | **Medium-Strong.** Tachyon is production-validated in the US — three credit card programs and multiple DDA programs (health benefits, loyalty/rewards). Cloud-native challengers entered this market with <$100M revenue and now serve Tier 1 banks. Market is fragmented (top 3 hold only 30.1% deal share). Tachyon's gap is breadth (purpose-specific programs, not full-service core) and visibility (no analyst coverage, no public case studies) | **Pursue.** Target Tier 2 US banks ($10–100B assets) actively evaluating alternatives post-FIS-TSYS consolidation. Lead with credit card and DDA production evidence. Convert existing deployments into referenceable case studies as the immediate priority |
| **Progressive core migration (India)** | **Strong.** SBI, HDFC Bank, and Axis Bank are all actively modernizing. India is Zeta's home market with existing bank relationships | **Medium-Strong.** Home market advantage, existing relationships, regulatory familiarity. Infosys Finacle (29.8% India share) and TCS BaNCS are the incumbents — but both have weaker cloud-native narratives than a purpose-built challenger | **Pursue.** Lead with Tachyon DDA in India. Expand Tachyon's reference base beyond purpose-specific programs into retail/business banking. India references complement existing US production evidence and strengthen analyst engagement |
| **Digital account platform / deposit innovation (Tier 2 US)** | **Strong.** $37–46B digital banking market growing 17–21% CAGR. 40% of new US accounts go to neobanks | **Weak.** Competing against Alkami ($444M revenue, 33% growth, 22.4M registered users), Q2 ($795M, 14% growth), and Backbase (~$365M). These vendors have hundreds of client relationships and deep mid-market distribution. Zeta has none | **Do not pursue as standalone.** This is the "augment" market, not the "replace" market. The digital banking layer wraps legacy cores — it does not replace them. Not Tachyon's natural positioning |
| **Business banking (all tiers)** | **Strong.** $8–12B market growing 7%. 86% of banks investing in virtual accounts. Mercury at $650M revenue validates the category | **Weak.** No evidence of Tachyon business banking capabilities — virtual accounts, cash management, multi-entity treasury structures, commercial lending workflows. Competing against Finastra ($400M TCM unit being sold for ~$2B), iGTB (23% of cross-border MNC sweeping), Kyriba (3,400 clients), Bottomline ($530M+) | **Defer.** Do not enter with incomplete capability. Build business banking features into Tachyon roadmap. Revisit when virtual account management and cash management capabilities exist |
| **BaaS enablement (Tier 2)** | **Strong.** Post-Synapse market restructuring ($21B→$106B by 2035). FDIC proposed Synapse Rule demands real-time customer-level deposit visibility. Legacy cores structurally inadequate for multi-tenant, partner-mediated deposits | **Medium.** Tachyon's US production evidence (credit cards, DDA) validates cloud-native multi-tenant architecture. Westpac launched BaaS on 10x in 18 months — the model is proven. Tachyon's gap is BaaS-specific packaging, not platform readiness | **Build toward.** Develop BaaS packaging after establishing core banking references. BaaS is an expansion play, not an entry play — banks require core banking credibility (which Tachyon's US deployments now provide) before extending to partner-mediated deposits |
| **AI in account operations** | **Strong.** CIBC CRTeX, Wells Fargo AI agents via Google Agentspace. Synthetic identity fraud at $3.3B H1 2025 exposure. Banks need governed AI in account lifecycle | **Strong.** Evolution Fabric + Agent Fabric is the structural differentiator. No competitor combines account infrastructure with an explicit operational model and AI agent governance. This is unique | **Pursue as long-term differentiator.** This is the expansion sale after establishing the platform relationship — not the entry sale. A bank must first trust Tachyon as its account platform before it will adopt Evolution Fabric as its operational model |

### What to defer or avoid

Do not pursue **Tier 1 US banks** as the primary entry segment. JPMorgan selected Thought Machine. Wells Fargo built Vantage internally. Citi is recruiting a Head of Core Banking Transformation. These banks build strategically, require 18–36 month sales cycles, and will not adopt from a vendor without Tier 1 references.

Do not pursue **digital banking platform** competition head-on. Alkami, Q2, and Backbase serve the "augment the core" market. Tachyon's thesis is "replace the core." These are different buyers, different budgets, and different competitive dynamics.

Do not invest in **business banking** until Tachyon has virtual account management, cash management, and multi-entity capabilities. Entering with incomplete capability against vendors like Finastra and iGTB — who serve 48 of the top 50 banks in treasury alone — would damage credibility.

---

## 9. Risks and Gaps

### What must be true for the account products opportunity to work

1. **Tachyon's production evidence must be converted into public references.** Three credit card programs and multiple DDA programs (Optum health benefits, loyalty/rewards) in the US establish production readiness. The gap is visibility: these deployments must become referenceable case studies that buyers and analysts can evaluate. Without public references, production capability remains invisible to the market.
2. **Tachyon's scope must expand beyond purpose-specific programs.** Current US production deployments are credit cards and purpose-specific DDA (benefits, rewards). Extension to full-service retail and business banking DDA is the product roadmap question that determines how broadly Tachyon can compete against Thought Machine, Mambu, and 10x in core banking replacement.
3. **The Evolution Fabric thesis must translate to measurable bank outcomes.** "Making work explicit and governed" is compelling conceptually. Banks buy measurable outcomes: reduced operational cost, faster product launches, lower compliance risk, governed AI deployment. Quantify the thesis.
4. **Pricing must be demonstrably lower than incumbents for comparable capability.** The mid-market gap exists because FIS, Fiserv, and Temenos are over-engineered and expensive for Tier 2 banks. Zeta must be affordable, not just modern.
5. **Analyst coverage must be established.** Mid-market banks rely on Celent, Datos Insights (Aite-Novarica), and Gartner for vendor shortlisting. Without analyst coverage, Zeta is invisible to the buyer.

### Honest gaps in Zeta's position

- **Production evidence is not publicly referenceable.** Tachyon powers three credit card programs and multiple DDA programs in the US, but these deployments are not packaged as public case studies. Analyst firms and mid-market buyers cannot discover or evaluate this evidence.
- **Documentation lags production reality.** Tachyon Credit Cards and DDA are in production, but product line documentation remains thin. Technical documentation, API references, and architecture guides must match the level competitors publish (Thought Machine's Vault Core docs, Mambu's public API references).
- **No analyst coverage.** Thought Machine, Mambu, and 10x appear in CB RADAR, Celent reports, and Gartner evaluations. Tachyon appears in none.
- **No business banking capabilities.** Virtual accounts, cash management, multi-entity — the $8–12B business banking opportunity is inaccessible without these features.
- **Different buying center from payments.** Cross-sell from Photon to Tachyon requires navigating from the payments head to the CTO/CIO. This is a sales motion change, not an incremental conversation.

### Competitive retaliation risk

- **FIS post-TSYS ($13.5B acquisition, Jan 2026)** will aggressively defend and expand its core banking and issuer processor base. FIS has Finxact (cloud-native) in its portfolio and 13 implementations tracked by CB RADAR. The integration may take 18–24 months — this is the window for challengers.
- **Mambu (200+ clients, 60+ new in 2025)** is rapidly building Tier 2 distribution. If Mambu establishes dominance in the mid-market segment Zeta targets, the entry window closes.
- **Thought Machine** is cutting costs and extending into community banking (Mascoma Bank). If Thought Machine successfully moves downmarket while retaining Tier 1 credibility, it compresses the space for new entrants.

### The overlay delay effect

If Zafin and SunTec solve banks' immediate deposit pricing problems in 8 weeks — as demonstrated by a Tier 1 US bank achieving >50% increase in CD approved volumes via Zafin — the business case for a 3-year Tachyon deployment weakens. Overlays remove the most acute pain without forcing the deeper architectural decision. Zeta must articulate why Evolution Fabric creates urgency that overlays cannot satisfy: overlays fix pricing but cannot fix the operational model, cannot enable governed AI participation, and cannot compound investments across domains.

---

## 10. Recommended Actions

### Near-term (0–2 years)

| Action | Rationale | Priority |
|---|---|---|
| **Convert US deployments into referenceable case studies** | Tachyon powers three credit card programs and multiple DDA programs (Optum health benefits, loyalty/rewards) in the US. These deployments are production evidence that must become publicly visible — structured case studies with deployment scope, scale metrics, and architecture details | **Immediate** |
| **Secure 1–2 Indian bank pilots for Tachyon DDA** | India is the home market with existing relationships. India bank deployments for retail/business DDA would expand Tachyon's reference base beyond purpose-specific programs into general-purpose banking — strengthening the core banking replacement narrative. SBI, HDFC, and Axis are all modernizing — but start with a smaller institution where deployment risk is manageable | **Immediate** |
| **Document Tachyon product lines fully** | "To be expanded" is not acceptable for a product family that must compete against Thought Machine's Vault Core documentation and Mambu's public API references. Complete technical documentation for Kernel, DDA, Credit Cards, CLM, and Loans | **Q2 2026** |
| **Engage Celent and Datos Insights for analyst coverage** | Mid-market banks rely on analyst recommendations for vendor shortlisting. Without coverage, Tachyon is invisible. Target CB RADAR inclusion and Celent ABCD evaluation | **Q2 2026** |
| **Develop Evolution Fabric outcome metrics** | Translate "making work explicit and governed" into measurable outcomes: X% reduction in operational cost, Y% faster product launch, Z% reduction in compliance incidents. Use Quark domain hubs to package these outcomes by banking domain | **2026** |
| **Package Tachyon + Photon cross-sell for existing payments clients** | Existing Photon bank relationships provide warm introductions. Develop a cross-sell motion from payments head to CTO/CIO — not as an upsell, but as an architectural integration that makes the payments investment more valuable | **2026–2027** |

### Medium-term (2–5 years)

| Action | Rationale | Priority |
|---|---|---|
| **Expand into US Tier 2 core banking market** with full-service retail/business DDA | The mid-market gap ($10–100B banks) is real. FIS-TSYS integration creates a window. Tachyon's existing US credit card and DDA production evidence provides the entry credential. Combine with analyst coverage and demonstrable pricing advantage | **2027–2028** |
| **Launch Evolution Fabric positioning for account domains** | The "integrated account platform + operational model" hypothesis is the long-term differentiator. Introduce after the core banking platform relationship is established — as an expansion, not the entry sale | **2027–2028** |
| **Develop BaaS-specific packaging** | Post-Synapse BaaS requires real-time customer-level deposit visibility on modern cores. Package Tachyon for multi-tenant, partner-mediated deposit management. Target banks evaluating BaaS after Evolve Bank's cease-and-desist | **2028** |
| **Build business banking capabilities** | Virtual account management, cash management, multi-entity structures. The $8–12B market is growing 7% annually. Do not enter until capability is complete | **2028–2029** |

### What to defer or avoid

| Decision | Rationale |
|---|---|
| **Do not pursue Tier 1 US banks** as primary segment | Relationship-intensive, 18–36 month sales cycles. JPMorgan, Wells Fargo, and Citi have made their core banking decisions. Zeta lacks the brand, references, and sales infrastructure |
| **Do not pursue digital banking platform** competition | Alkami ($444M), Q2 ($795M), and Backbase (~$365M) own the "augment the core" market. Tachyon's value is "replace the core" — do not compete in someone else's category |
| **Do not enter business banking** without virtual accounts and cash management | Finastra (48 of top 50 banks in treasury), iGTB, Kyriba, and Bottomline are deeply entrenched. Entering with incomplete capability damages credibility for the broader account products story |
| **Do not position Evolution Fabric as the entry sale** | Banks buy platforms, then adopt operational models. Leading with the operational thesis before establishing platform credibility inverts the sales motion |

---

## 11. Key Differences: Account Products vs. Other Engagement Areas

| Dimension | Account Products & Core Banking | Payments | Digital Identity & Trust | Cloud & Platform Ops | Agentic Banking | Banking Operations |
|---|---|---|---|---|---|---|
| Market structure | Oligopoly (FIS, Fiserv, Jack Henry) + fragmented cloud-native challengers | Oligopoly (FIS, Fiserv, GP) + fragmented challengers | Fragmented IAM vendors | Hyperscalers + observability tools | Nascent; no dominant vendor | Fragmented across 7 vendor categories; no unified operations vendor |
| Competitive intensity | Very high — incumbents hold 15–25 year relationships with deep switching costs | Very high | Medium | High (hyperscaler adjacency) | Low (new category) | High (entrenched incumbents per sub-domain) |
| Regulatory forcing | Moderate — only 5 of 19 regulations force core replacement; most are wrappable | Very strong (multiple concurrent mandates) | Strong (GDPR, PSD2/3, DPDP) | Medium | Weak | Strong (BSA/AML enforcement, EU AML Package, RBI mandates) |
| Geographic concentration | UK leads active transformation pipeline (10 institutions); US is primary vendor TAM | USA 30–40% of global spend | Distributed | Distributed | USA-first | USA 33–42%; Asia-Pacific fastest-growing |
| Central strategic argument | Banks must eventually replace 30-year-old cores — but most will defer as long as overlays and wrappers can extend core life. The question is when, not whether | Banks must replace infrastructure they have been layering for 20 years. The technology debt is structural | Identity is fragmenting across human/AI/partner boundaries | Cloud operations lack customer-centric observability | AI agents need an operational model to participate in banking | Operations volume, regulatory intensity, and knowledge fragility demand explicit, governed, AI-augmented operations models |
| Vendor-addressable TAM | $15–20B (Tier 2–3 vendor-addressable); $25–40B (broad composite) | $60–85B (narrow); $150–200B (broad) | $15–25B (IAM/IGA) | $10–15B | <$5B (nascent) | $19–27B |

---

## Research Sources

This analysis draws on data from 50+ sources across six research streams. All cited URLs were verified as of March 2026. Detailed research files are retained in `_research/account-products-and-banking/`.

**Primary institutional sources:** [ABA](https://aba.com/); [FDIC](https://www.fdic.gov/); [Federal Reserve](https://www.federalreserve.gov/); [OCC](https://www.occ.gov/); [EY](https://www.ey.com/); [RBI](https://rbi.org.in/); [PRA](https://www.bankofengland.co.uk/prudential-regulation); [UK OBIE](https://www.openbanking.org.uk/)

**Industry reports (may be paywalled):** [Celent](https://celent.com/); [CB RADAR / Core System Partners](https://coresystempartners.com/); [Cornerstone Advisors](https://www.crnrstone.com/); [Datos Insights](https://datos-insights.com/); Oliver Wyman; McKinsey; Gartner; EY UK Core Banking Modernisation Report (October 2025)

**Market research:** [Grand View Research](https://grandviewresearch.com/); [Mordor Intelligence](https://www.mordorintelligence.com/); [360iResearch](https://www.giiresearch.com/); [Kings Research](https://www.kingsresearch.com/); [SNS Insider](https://www.globenewswire.com/); [Growth Market Reports](https://growthmarketreports.com/)

**Vendor financials and case studies:** [FIS](https://www.fisglobal.com/); [Fiserv](https://investors.fiserv.com/); [Jack Henry](https://ir.jackhenry.com/); [Temenos](https://www.temenos.com/); [Thought Machine](https://www.thoughtmachine.net/); [Mambu](https://mambu.com/); [10x Banking](https://www.10xbanking.com/); [Pismo/Visa](https://investor.visa.com/); [Alkami](https://investors.alkami.com/); [Q2](https://www.nasdaq.com/); [Zafin](https://zafin.com/)

**Industry media:** [Finextra](https://www.finextra.com/); [American Banker](https://www.americanbanker.com/); [PYMNTS](https://www.pymnts.com/); [The Banker](https://www.thebanker.com/); [Business Money](https://www.business-money.com/)
