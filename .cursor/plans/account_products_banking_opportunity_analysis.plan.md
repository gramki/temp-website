---
name: Account Products and Core Banking Opportunity Analysis
overview: "McKinsey-grade two-part opportunity analysis (Part I: independent analyst assessment, Part II: Zeta strategic advisory) for the Account Products and Core Banking engagement area. Replaces the current CIO-facing capability catalogue."
todos:
  - id: p1b1
    content: Phase 1 Batch 1 — Research Streams 1–4 (market sizing, regulatory landscape, competitive landscape, structural shifts). Raw output saved to _research/account-products-and-banking/s1–s4 files.
    status: pending
  - id: p1b2
    content: Phase 1 Batch 2 — Research Streams 5–6 (business banking and cash management, deposit innovation and account portability). Raw output saved to _research/account-products-and-banking/s5–s6 files.
    status: pending
  - id: p2-synthesis
    content: "Phase 2 — Synthesis & gap-fill: cross-reference streams, rate evidence quality, verify URLs, assemble target universe, map Right to Play / Right to Win. Save synthesis-notes.md and unverified-claims.md."
    status: pending
  - id: p2-gapfill
    content: Phase 2 — Targeted gap-fill research for any structural shift with fewer than 3 data points or any competitive category where banking-specific positioning is unclear.
    status: pending
  - id: p3-market
    content: Phase 3 Part I §1 — Market section. Vendor-addressable TAM for core banking technology, segmented by sub-domain and geography.
    status: pending
  - id: p3-history
    content: "Phase 3 Part I §2 — How We Got Here. Three eras: monolithic core, channel overlay, composable platform."
    status: pending
  - id: p3-shifts
    content: Phase 3 Part I §3 — Structural Shifts. 6–8 shifts evidenced with data, regulatory citations, bank-tier and geographic analysis.
    status: pending
  - id: p3-engagements
    content: Phase 3 Part I §4 — Engagement Landscape. Concrete engagement types mapped to bank tier and structural shift.
    status: pending
  - id: p3-competitive
    content: Phase 3 Part I §5 — Competitive Landscape. Legacy incumbents, modern challengers, specialists profiled with vulnerabilities.
    status: pending
  - id: p3-targets
    content: Phase 3 Part I §6 — Target Universe. Named institutions across USA, India, UK with cited evidence of core modernization activity.
    status: pending
  - id: p3-position
    content: Phase 3 Part II §7 — Zeta's Position. Tachyon, Quark, Evolution Fabric mapped to opportunity. Gaps identified honestly.
    status: pending
  - id: p3-wheretoplay
    content: Phase 3 Part II §8 — Where to Play. Segments, geographies, bank tiers to pursue, defer, or avoid.
    status: pending
  - id: p3-risks
    content: Phase 3 Part II §9 — Risks and Gaps. Prerequisites, window risks, capability gaps.
    status: pending
  - id: p3-actions
    content: Phase 3 Part II §10 — Recommended Actions. Prioritized near-term and medium-term actions.
    status: pending
  - id: p3-execsummary
    content: Phase 3 §11 — Executive Summary. Written last, covers both Part I and Part II.
    status: pending
  - id: p4-partI
    content: "Phase 4 — Part I review: all citations verified with URLs, no Zeta references, no commercial voice, segment/geographic specificity confirmed."
    status: pending
  - id: p4-partII
    content: "Phase 4 — Part II review: all recommendations trace to Part I evidence, gaps stated honestly, product references verified against repo product-line files."
    status: pending
  - id: p4-editorial
    content: "Phase 4 — Editorial rigor review (Part I only): all 8 tests from editorial-rigor-review skill."
    status: pending
isProject: true
---

# Account Products and Core Banking — Opportunity Analysis & Strategic Advisory Plan

**Engagement Area:** Account Products and Core Banking
**Output:** `org-8.0/what-we-sell/strategy/engagement-areas/account-products-and-banking.md`
**Target length:** 5,500–7,500 words (two-part structure)
**Current state:** 109-line CIO-facing capability catalogue with explicit placeholder note: *"The deep opportunity analysis will follow the same two-part structure (Analyst / Advisor) as Payments."* Must be fully replaced.

---

## 1. Model Recommendation

**Orchestration:** Default model. Core banking modernization involves the longest replacement cycles in banking technology (15–25 years per platform), the broadest competitive landscape (six legacy incumbents, a growing modern challenger cohort, and dozens of specialists), and deeply geography-specific regulatory drivers. The orchestrator must manage six parallel research streams, enforce the analyst/advisor voice boundary across a domain where the temptation to sell is high (Tachyon is Zeta's most directly competitive asset), and apply the eight editorial rigor tests.

**Research sub-agents:** Default model for all six streams. Rationale:

- **Streams 1–3** (market sizing, regulatory landscape, competitive landscape) have **strong analyst coverage**. Gartner publishes a Magic Quadrant for Global Retail Core Banking. Celent produces extensive core banking research (Dimensions reports, vendor analyses). IDC, Forrester, and Datos Insights cover digital banking platforms. Multiple market sizing reports exist from MarketsandMarkets, Grand View Research, and Mordor Intelligence. The default model can synthesize these effectively.
- **Stream 4** (structural shifts) has **moderate to strong coverage** for most shifts. Progressive core replacement and composable banking are well-documented by Gartner and Celent. Cloud-native core is covered extensively. However, "AI in account operations" (beyond origination) is **thinner** — most analyst coverage focuses on AI in lending decisioning, not AI in deposit account lifecycle or cash management operations. This shift will require primary evidence sources.
- **Streams 5–6** (business banking/cash management, deposit innovation/account portability) have **moderate coverage**. Business banking is covered by Celent, McKinsey, and Accenture but the technology vendor landscape is less well-documented than retail core. Deposit innovation and open banking account portability are covered by regulator publications and challenger bank data more than by traditional analyst firms.

**Impact of coverage gaps on research approach:** The core banking technology market is well-sized at the macro level but fragmented in definition. Some analysts include digital banking platforms (front-end) in their TAM; others focus narrowly on account processing engines. The market sizing stream must construct a consistent vendor-addressable TAM by disaggregating the commonly cited figures. The "composable banking" thesis — that monolithic cores will be replaced by component-based architectures — is well-articulated by Gartner but has limited empirical evidence of production deployment at scale beyond a handful of challenger banks. The synthesis phase must assess whether this architectural thesis has enough real-world evidence to sustain a structural shift claim or whether it remains partially aspirational.

---

## 2. Phase 1: Parallel Research (6 Streams)

### Stream 1: Market Sizing and Revenue Pools

**What to gather:**

- Vendor-addressable TAM for core banking technology infrastructure — what banks spend on platforms, not total banking IT:
  - Core banking platforms (account processing, ledger, product configuration) — retail and business
  - Digital banking platforms (digital account opening, self-service, mobile/web banking layers)
  - Cash management and treasury technology platforms
  - Account origination and onboarding platforms
  - Deposit operations and servicing platforms
  - Limit management and cross-product exposure systems
- Revenue breakdown by geography (USA, India, UK/Europe, global)
- Revenue breakdown by bank tier where available (Tier 1 $100B+ assets, Tier 2 $10B–$100B, Tier 3 $1B–$10B)
- Growth rates (CAGR) by sub-segment
- Build vs. buy patterns by bank tier — Tier 1 banks increasingly building in-house (JPMorgan, Goldman); Tier 2–3 heavily vendor-dependent
- Core banking replacement deal flow — number and size of core replacement projects announced or completed in the past 3 years, by vendor and geography
- Average deal size and implementation timeline for core banking replacements by bank tier

**Sources to target:**

- Gartner (Magic Quadrant for Global Retail Core Banking; Market Guide for Digital Banking Platforms)
- Celent (Dimensions reports on core banking; "It's Time" series on core modernization)
- IDC (Financial Insights reports on banking technology spending)
- Forrester (Wave for Digital Banking Engagement Platforms)
- MarketsandMarkets, Grand View Research, Mordor Intelligence (core banking market reports)
- Datos Insights / Aite-Novarica (digital banking platform research)
- Bank IT spending surveys: Cornerstone Advisors ("What's Going On in Banking" annual survey), Gartner CIO surveys
- Vendor revenue disclosures: Temenos (public), FIS (public), Fiserv (public), Infosys Finacle (segment reporting), TCS BaNCS (segment reporting)
- IBS Intelligence annual sales league table (core banking deal tracking)

**Geographic scope:** Global with USA, India, UK/Europe breakdowns.

**How data will be used:** Part I, Section 1 (Market). Establishes the vendor-addressable prize. The distinction between "total core banking market" and "vendor-addressable TAM" is critical — much Tier 1 spending is in-house. The Tier 2–3 segment is the primary vendor-addressable opportunity.

**Citation requirement:** Every data point must include a navigable URL or full bibliographic detail per the Citation Standard. Flag as `[unverified — needs manual confirmation]` if the source cannot be linked.

---

### Stream 2: Regulatory Landscape and Account Mandates

**What to gather:**

Specific regulations that force banks to invest in account infrastructure — with compliance deadlines, penalty regimes, and infrastructure implications. The focus is on regulations that create **technology buying events**, not general banking regulation.

**Regulations to cover by geography:**

**USA:**

- CFPB Section 1033 (Personal Financial Data Rights) — open banking rule requiring banks to make consumer financial data available through standardized APIs. Compliance deadlines phased by bank size. Infrastructure implications: API development, data standardization, consent management for account data sharing
- FDIC Part 370 (Recordkeeping for Timely Deposit Insurance Determination) — requires covered institutions to maintain complete records for rapid deposit insurance calculation. Infrastructure implications: real-time deposit aggregation across account types
- FinCEN CDD/KYC rules — Customer Due Diligence requirements for account opening, beneficial ownership
- BSA/AML requirements for account monitoring — Suspicious Activity Reports, Currency Transaction Reports
- Federal Reserve Regulation E (Electronic Fund Transfers) — consumer protection for deposit accounts
- FDIC/OCC/Fed guidance on third-party relationships (2023) — implications for BaaS and embedded banking partnerships
- Community Reinvestment Act modernization (OCC 2024 updates) — digital banking and deposit access requirements

**India:**

- RBI Master Direction on Opening of Current Accounts and CC/OD (2020, as amended) — restrictions on multiple current accounts, impact on business banking
- RBI Account Aggregator framework — consent-based financial data sharing across deposit, investment, and insurance accounts
- RBI Digital Lending Guidelines (2022) — requirements for digital loan account management and disclosure
- RBI Master Direction on KYC (2016, as amended) — eKYC, Video KYC, periodic KYC updates for deposit accounts
- RBI guidelines on Basic Savings Bank Deposit Accounts (BSBDA) — financial inclusion mandates
- Digital Personal Data Protection (DPDP) Act 2023 — consent and data governance for account holder data

**UK/Europe:**

- PSD2 / PSD3 (proposed) — Account Information Services (AISP), Payment Initiation Services (PISP), Strong Customer Authentication for account access
- UK Open Banking (CMA Order) and Current Account Switch Service (CASS) — the most mature open banking regime driving account portability
- UK FCA Consumer Duty — product governance requirements for deposit accounts, fair value assessments
- EU Instant Payments Regulation — implications for deposit account infrastructure (24/7 availability)
- DORA (Digital Operational Resilience Act) — ICT risk management requirements for core banking systems
- Basel III/IV implementation — capital and liquidity requirements that drive ledger and reporting infrastructure

**Sources to target:**

- Official regulatory texts (Federal Register, CFPB, FDIC, RBI circulars, EUR-Lex, FCA)
- Law firm analyses (Davis Polk, Sullivan & Cromwell, Cleary Gottlieb) for compliance timeline summaries
- PwC, Deloitte, EY regulatory outlook reports
- Cross-reference with `_research/payments/s2-regulatory-landscape.md` for PSD2 and India regulatory content that overlaps
- Cross-reference with `_research/digital-identity-and-trust/s2-regulatory-landscape.md` for KYC/identity regulatory content that overlaps

**Geographic scope:** USA, India, UK/Europe.

**How data will be used:** Part I, Sections 2 (How We Got Here) and 3 (Structural Shifts). Regulations are a secondary forcing function for core banking — less direct than in payments (where mandates like FedNow create hard deadlines), but Section 1033, open banking mandates, and FDIC Part 370 create specific technology investment requirements. The regulatory stream must distinguish between regulations that force core replacement vs. those that can be satisfied by wrapping the existing core.

**Citation requirement:** Every regulation cited must link to the official text or a specific regulatory guidance document. Law firm summaries are acceptable as secondary sources but must reference the underlying regulation.

---

### Stream 3: Competitive Landscape

**What to gather:**

For each competitor category, identify the key players and for each: positioning, target market (bank tier, geography), revenue model (license, SaaS, processing), product scope, strengths, weaknesses, and vulnerabilities.

**Categories and key players to map:**


| Category                             | Players to Research                                                                                                                                                                                                                                                    |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Legacy core banking incumbents       | FIS (Modern Banking Platform + legacy IBS/PROFILE), Fiserv (DNA, Signature, Premier, Cleartouch), Jack Henry (SilverLake, CIF 20/20, Core Director), Oracle (FLEXCUBE), Temenos (Transact), Infosys (Finacle), TCS (BaNCS), Finastra (Fusion Essence, Midas, Equation) |
| Modern cloud-native challengers      | Thought Machine (Vault), Mambu, 10x Banking, Finxact (now FIS), nCino (primarily lending but expanding), Pismo (acquired by Visa)                                                                                                                                      |
| Digital banking platform specialists | Backbase, Alkami Technology, Q2 Holdings, NCR Voyix (now MiTek/Terafina), Temenos Infinity                                                                                                                                                                             |
| Business banking and cash management | Finastra (Fusion Corporate Channels, Fusion Cash Management), Bottomline Technologies (acquired by Thoma Bravo), Kyriba, ION Group (Openlink, Wallstreet Suite), ACI Worldwide (cash management modules)                                                               |
| Account origination specialists      | Newgen Software, Pegasystems, Temenos Journey Manager, Salesforce Financial Services Cloud                                                                                                                                                                             |
| Product and pricing engines          | Zafin, Moxo, SunTec Business Solutions                                                                                                                                                                                                                                 |
| India-specific core banking          | Infosys Finacle (dominant in India), TCS BaNCS, Oracle FLEXCUBE (significant India presence), Intellect Design Arena (iGTB for corporate banking)                                                                                                                      |


**For each player, capture:**

- Annual revenue or ARR (where public or estimable)
- Banking-specific revenue or customer count — number of banks live on the platform
- Geographic concentration (which markets they dominate)
- Bank tier focus (Tier 1, Tier 2, Tier 3)
- Architecture model (monolithic, modular, cloud-native, SaaS)
- Deployment model (on-premise, private cloud, public cloud, BaaS)
- Recent wins and losses — core banking deals announced in the past 2 years
- Recent M&A activity (Visa acquiring Pismo, FIS acquiring Finxact, NCR splitting, Thoma Bravo acquiring Bottomline)
- Vulnerabilities: where their architecture limits flexibility, which bank tiers they underserve, where modernization threats are strongest, contract renewal cycles that create switching windows

**Sub-task — bank modernization signals:**

> Identify specific banks that have publicly signaled core banking modernization activity — through earnings calls, press releases, RFP announcements, analyst commentary, or vendor partnership disclosures. Capture the bank name, tier, geography, the signal, the source, and a navigable URL to the source.

**Sources to target:**

- Gartner Magic Quadrant for Global Retail Core Banking (latest)
- Celent XCelent Awards and Dimensions reports (core banking vendor evaluations)
- IDC MarketScape for Core Banking (if available)
- IBS Intelligence annual sales league table (core banking deal flow)
- SEC filings (10-K/10-Q) for public competitors: Temenos, Alkami, Q2, Jack Henry, Fiserv, FIS
- Earnings call transcripts (Seeking Alpha, Motley Fool Transcripts)
- Vendor press releases (partnership/deployment announcements with banks)
- Crunchbase / PitchBook (funding rounds, M&A, valuations for private players)

**Geographic scope:** Global, with emphasis on USA, India, UK vendors and their bank customer bases.

**How data will be used:** Part I, Section 5 (Competitive Landscape) and Part II, Section 7 (Zeta's Position — relative to competitors).

**Citation requirement:** Every competitive claim must be sourced. Revenue figures from SEC filings or credible analyst estimates. Product scope claims from vendor documentation. M&A from press releases or regulatory filings.

---

### Stream 4: Structural Shifts and Core Modernization Activity

**What to gather:**

Evidence for 6–8 structural shifts reshaping the account products and core banking infrastructure market. Each shift must be evidenced with data, regulatory citations, competitive activity, and bank-tier analysis.

**Candidate structural shifts to investigate:**

1. **Progressive core replacement displacing big-bang migration** — Banks are migrating account products one at a time (e.g., starting with DDA, then savings, then time deposits) rather than attempting full core replacement. The strangler pattern — running modern and legacy cores in parallel — is becoming the dominant migration strategy. Evidence: number of progressive vs. big-bang migrations by bank tier, failure rates of big-bang replacements, vendor support for coexistence/migration models, specific bank migration announcements. Key question: how many banks have successfully completed a full progressive core migration vs. how many are still in early stages?
2. **Composable banking architecture replacing monolithic cores** — The shift from vendor-defined product catalogs (where the core determines what products a bank can offer) to bank-defined product assembly (where products are configured from modular capabilities). Gartner's "composable banking" thesis. Evidence: Gartner analyst positions, vendor product architecture changes, bank adoption data for component-based cores, specific deployments of composable platforms (Thought Machine Vault, Mambu, Finxact). Key question: is composable banking production-proven at scale in established banks, or only in neobanks and challengers?
3. **Cloud-native core infrastructure becoming table stakes** — Core banking platforms moving from on-premise and private cloud to public cloud (AWS, Azure, GCP). Cloud-native is becoming a selection criterion rather than a differentiator. Evidence: cloud deployment data for core banking by bank tier, regulatory clearances for cloud-hosted core systems (OCC, RBI, PRA), specific bank announcements of cloud core deployments, vendor cloud-native product launches. Key question: at what bank tier does cloud-native core become the default selection criterion vs. an optional preference?
4. **Business banking digitization creating a separate modernization wave** — Business banking (SME and commercial) is being modernized independently of retail core. The requirements are structurally different: multi-entity account structures, cash pooling, virtual accounts, liquidity management, real-time treasury visibility. Evidence: McKinsey/BCG business banking market sizing, bank earnings commentary on business banking investment, fintech challengers in business banking (Tide, Mercury, Relay Financial, Novo), specific bank platform deployments for business banking, virtual account adoption data.
5. **Open banking mandates driving account infrastructure investment** — Section 1033 (USA), PSD2/PSD3 (EU), Open Banking (UK), Account Aggregator (India) require banks to expose account data through standardized APIs. This creates infrastructure requirements that legacy cores cannot satisfy without middleware. Evidence: compliance deadline data, API readiness by bank tier, account switching data (UK CASS statistics), fintechs leveraging open banking account access, the link between API mandates and core modernization decisions.
6. **Deposit competition from neobanks and fintechs forcing product agility** — High-yield savings accounts, round-up savings, tiered interest, goal-based savings, and crypto-adjacent yield products are capturing deposit share from traditional banks. Banks need modern product configuration engines to respond — legacy cores cannot launch deposit variants quickly enough. Evidence: neobank deposit growth data (Chime, SoFi, Revolut, Monzo, Starling), deposit migration data from traditional banks to fintechs, time-to-market for new deposit products on legacy vs. modern cores, specific bank responses to deposit competition.
7. **Embedded banking (BaaS) requiring modern account infrastructure** — Fintechs and non-financial brands need banking-as-a-service infrastructure to offer deposit accounts. The BaaS compliance tightening (Synapse collapse, Evolve Bank cease-and-desist) is shifting demand from unregulated middleware to properly licensed bank partners with modern account platforms. Evidence: BaaS market sizing, regulatory enforcement actions, bank BaaS partnerships (Column, Cross River, Coastal Community Bank), the shift from "BaaS through middleware" to "BaaS through modern core," specific core platform requirements for BaaS enablement.
8. **AI in account operations beyond origination** — AI entering account lifecycle management: automated KYC refresh, dormancy prediction, fraud detection in account opening (synthetic identity), personalized product recommendations, automated account servicing. This is thinner in analyst coverage than AI in lending or payments. Evidence: vendor AI product launches for account operations, bank pilot announcements, specific use cases with measured outcomes, the distinction between AI in origination (better covered) and AI in ongoing account lifecycle (less covered).

**For each shift, gather:**

- 3–5 data points with sources and URLs
- Regulatory citations that create or accelerate the shift
- Competitive activity (vendors capitalizing on the shift)
- Analysis by bank tier (how does this shift affect Tier 1 vs. Tier 2 vs. Tier 3 differently?)
- Geographic variation (USA vs. India vs. UK)

**Sub-task — bank modernization signals:**

> Identify specific banks that have publicly signaled account products / core banking modernization activity — through earnings calls, press releases, RFP announcements, analyst commentary, or vendor partnership disclosures. For each: bank name, tier, geography, the signal, the source, and a navigable URL.

**Sources to target:**

- Gartner research notes on core banking modernization, composable banking
- Celent reports on core banking replacement activity, progressive migration
- IBS Intelligence core banking deal tracker
- Bank earnings call transcripts (search for "core modernization," "core replacement," "core banking transformation," "digital banking platform," "deposit platform," "composable," "progressive migration")
- Vendor partnership announcements (Thought Machine, Mambu, 10x, Finxact deployments at named banks)
- McKinsey / BCG / Accenture banking technology publications
- Regulatory guidance on cloud hosting of core banking (OCC, RBI, PRA, EBA)
- Cross-reference with `_research/payments/s4-realtime-payments-hubs.md` for any overlapping core infrastructure modernization signals

**Geographic scope:** USA, India, UK.

**How data will be used:** Part I, Sections 2 (How We Got Here), 3 (Structural Shifts — the core of the document), 4 (Engagement Landscape), and 6 (Target Universe).

**Citation requirement:** Every structural shift claim must be grounded in at least three independent data points with navigable URLs. Assertions without evidence are flagged or dropped.

---

### Stream 5: Business Banking, Cash Management, and Treasury Modernization

**Why a separate stream:** Business banking has structurally different requirements from retail account products. The competitive set is different (Finastra, Bottomline, Kyriba, Intellect iGTB vs. the retail core vendors). The buyer is different (commercial banking head, not retail technology). The revenue pools are distinct. And the modernization cycle is often independent of retail core replacement. Treating business banking as a sub-topic of retail core would understate the opportunity.

**What to gather:**

- Market sizing for business banking technology infrastructure — cash management platforms, virtual account platforms, liquidity management systems, trade finance platforms, treasury management systems
- Virtual accounts as a structural innovation: what they are, adoption by bank tier, vendor capabilities, regulatory status across geographies
- Cash pooling and sweep arrangements: technology requirements, multi-entity visibility, real-time treasury
- SME digital banking: separate from enterprise commercial banking. Neobank challengers (Tide, Mercury, Relay, Novo, Brex for business accounts). The gap between what SMEs expect (consumer-grade experience) and what traditional banks deliver
- Multi-entity and group account structures: corporate hierarchy management, consolidated positions, inter-company transfers. Requirements that retail cores were not designed for
- Business banking as a growth priority: bank earnings commentary, investment signals, specific platform deployments
- The link between business banking modernization and core banking modernization — does a bank modernize business banking by replacing the core, by adding a specialized business banking layer, or by deploying a separate core for business?

**Sources to target:**

- McKinsey Global Banking Practice (business banking, commercial banking, SME banking publications)
- BCG (commercial banking technology)
- Celent (corporate banking, cash management, virtual accounts research)
- Accenture (business banking innovation)
- Vendor documentation: Finastra Fusion, Bottomline, Kyriba, Intellect iGTB, Mambu (business banking)
- Fintech company data: Tide, Mercury, Relay Financial, Novo — funding rounds, customer counts, deposit volumes
- Bank press releases on business banking platform investments
- SWIFT gpi and ISO 20022 implications for corporate account structures

**Geographic scope:** USA (primary — largest commercial banking market), UK (strong challenger activity in SME banking), India (MSME digitization drive).

**How data will be used:** Part I, Sections 3 (Structural Shift 4 — business banking digitization), 4 (Engagement Landscape — business banking-led engagements), and 5 (Competitive Landscape — business banking/cash management vendors). Part II will assess Tachyon's business banking capabilities against this competitive set.

**Citation requirement:** Business banking technology market sizing is less precisely documented than retail core or payments. Where market sizing comes from a single analyst source, note this limitation. Cross-reference with McKinsey Global Banking revenue pool data for business banking to ground the vendor-addressable estimate.

---

### Stream 6: Deposit Innovation, Open Banking, and Account Portability

**Why a separate stream:** Deposit competition and open banking are creating a distinct set of pressures on account infrastructure that go beyond core replacement. They affect product configuration agility, API architecture, customer lifecycle management, and the economics of deposit gathering. These pressures exist regardless of whether a bank replaces its core — but they make the case for replacement more compelling.

**What to gather:**

- Neobank and fintech deposit capture data: Chime, SoFi, Revolut, Monzo, Starling, N26 — customer counts, deposit volumes, growth rates, product types offered
- High-yield savings rate competition: current rates offered by fintechs vs. traditional banks, deposit migration evidence, the impact on bank net interest margins
- Time-to-market for new deposit products: legacy core (months) vs. modern platform (days/weeks) — specific examples and vendor claims with evidence
- Open banking adoption data:
  - UK: Open Banking Implementation Entity (OBIE) statistics, CASS switching data, API call volumes, number of regulated providers
  - USA: Section 1033 compliance timeline, CFPB implementation status, early adopters
  - India: Account Aggregator ecosystem data — number of FIUs, FIPs, consent volume, growth trajectory
  - EU: PSD2 AISP/PISP adoption, PSD3 proposals
- Account portability and switching: how easy it is for consumers and businesses to switch accounts, and whether open banking is actually driving switching behavior or primarily being used for aggregation
- Stablecoin and tokenized deposit competition: GENIUS Act implications, bank experiments with tokenized deposits, the competitive threat from regulated stablecoins offering yield on deposits
- Deposit product innovation examples: goal-based savings, round-ups, tiered/milestone interest, subscription banking, family/group accounts, savings vaults — which banks and fintechs offer these, and what infrastructure they require

**Sources to target:**

- OBIE (UK Open Banking statistics)
- CFPB (Section 1033 rulemaking, compliance deadlines)
- RBI (Account Aggregator data, financial inclusion statistics)
- FDIC Quarterly Banking Profile (deposit trends, bank profitability data)
- Neobank financial disclosures: SoFi (public), Revolut (UK filing), Monzo (UK filing), Starling (UK filing), Chime (private — use estimates from CB Insights, Sacra)
- Cornerstone Advisors consumer banking surveys
- J.D. Power Banking Satisfaction Study
- Cross-reference with `_research/payments/s1-market-sizing.md` for embedded banking/BaaS data
- Cross-reference with `market-study/` files for any overlapping deposit or account research

**Geographic scope:** USA, UK (most mature open banking), India (Account Aggregator growth).

**How data will be used:** Part I, Sections 3 (Structural Shifts 5–7 — open banking, deposit competition, embedded banking), 4 (Engagement Landscape — progressive core modernization and BaaS enablement engagements). The deposit innovation data grounds the product agility argument: banks need modern account platforms not because the old ones don't work, but because the old ones cannot respond to competitive pressure fast enough.

**Citation requirement:** Neobank data is often estimated (private companies). Use multiple estimates and triangulate. Distinguish between confirmed public disclosures (SoFi, Revolut Companies House filings) and analyst estimates. Flag estimates as estimates.

---

## 3. Phase 2: Synthesis and Gap-Fill

### Cross-referencing

- **Market sizing consistency:** Compare TAM estimates across Stream 1 sources. Identify where analyst firms define "core banking" differently (some include digital banking platform front-ends; some don't). Produce a reconciled view with explicit definitional notes. Distinguish between the "total core banking technology market" and the "vendor-addressable TAM for account products infrastructure" — the latter excludes in-house builds by Tier 1 banks and includes digital banking platforms only where they are sold as part of an account platform.
- **Regulatory-competitive alignment:** Map each regulation (Stream 2) to the vendors positioned to benefit (Stream 3) and the structural shift it accelerates (Stream 4). Identify regulations where compliance can be achieved by wrapping the legacy core (API gateway for Section 1033) vs. where compliance forces core replacement (FDIC Part 370 for some banks). This distinction matters: if wrapping suffices, the regulation is a weaker forcing function for core replacement.
- **Progressive migration evidence quality:** Cross-reference Stream 4 (structural shifts) claims about progressive core replacement with Stream 3 (competitive landscape) data on actual bank deployments. How many banks have announced progressive migration vs. how many have completed it? What is the success rate? What is the typical timeline? If evidence for successful progressive migration is thin, this weakens the most important structural shift in the analysis.
- **Business banking gap assessment:** Cross-reference Stream 5 (business banking) with Stream 3 (competitive landscape) to identify whether core banking vendors or specialist business banking vendors are winning business banking modernization deals. If business banking is being modernized on separate specialist platforms rather than on modern core banking platforms, this has implications for Zeta's Tachyon positioning.
- **Deposit competition as core replacement driver:** Cross-reference Stream 6 (deposit innovation) with Stream 4 (structural shifts) to assess whether deposit competition is actually driving core replacement decisions, or whether banks are responding to deposit competition with product overlay tools (Zafin, SunTec) without replacing the core. The answer affects the size and urgency of the opportunity.
- **Bank signal aggregation:** Consolidate bank modernization signals from Streams 3 and 4 into a single target universe. De-duplicate. Verify each bank's tier classification and geography. Confirm each signal source URL resolves.

### Evidence quality assessment

For each structural shift, rate evidence quality:

- **Strong:** 3+ independent data points with navigable URLs, confirmed by both analyst and primary sources
- **Moderate:** 2 data points or analyst-only without primary confirmation
- **Thin:** Single source or vendor-provided only
- **Hypothesis:** No external evidence found — flag as hypothesis and state explicitly in the document

Shifts with "thin" or "hypothesis" evidence quality must be either dropped from Part I or explicitly flagged. The analyst voice does not assert without evidence.

**Critical evidence assessment for this area:** The "composable banking" thesis (Shift 2) and the "progressive core replacement" claim (Shift 1) are the two most important structural arguments. Both are well-articulated by analysts but may have limited empirical evidence of production deployment at established banks (vs. neobanks). The synthesis phase must assess honestly whether these are structural shifts with evidence or aspirational industry narratives with analyst support.

### URL and citation verification

- Verify every URL resolves to the cited content (not a homepage, not a 404, not a paywall with no preview)
- For paywalled sources, confirm full bibliographic detail (publication, author, date, title, issue)
- Flag unverifiable claims in `unverified-claims.md`

### Targeted gap-fill research

Based on synthesis, conduct targeted follow-up for:

- Any structural shift with fewer than 3 data points
- The progressive migration success rate question — specifically targeting case studies of banks that have completed product-by-product core migration
- Business banking technology market sizing if Stream 5 evidence is thin
- AI in account operations (Shift 8) — likely the thinnest shift; may need to emphasize primary evidence (vendor product launches, bank pilot announcements)
- Middle East / Gulf greenfield core banking activity — if Streams 3–4 surface evidence that this is a meaningful opportunity concentration, assess whether to include it as a fourth geography

### Right to Play / Right to Win mapping

Map findings to the distillation framework:

**Right to Play questions to answer:**

- Is the vendor-addressable TAM for account products technology large enough and growing fast enough to justify entry?
- Are banks actively replacing core banking systems, or are they wrapping/extending them? (The answer determines whether the opportunity is core replacement or core augmentation — these require different products.)
- Can Zeta enter given Tachyon's current product maturity (product-line docs are placeholder: "To be expanded")?
- What is the competitive density? How many modern challengers have entered in the past 5 years?
- Is the buying cycle realistic for Zeta? (Core banking deals are 2–5 year sales cycles with 3–7 year implementations.)

**Right to Win questions to answer:**

- Does Tachyon's composable account platform architecture (if production-ready) represent a genuine advantage over Thought Machine Vault, Mambu, or Finxact?
- Does the combination of Tachyon (accounts) + Evolution Fabric (operational model) + Trust Fabric (identity) create a differentiated positioning that no core banking competitor offers?
- Does Zeta's existing bank customer base (from payments and commercial cards) provide a credible route to market for account products?
- Where is Zeta's position genuinely weak? (e.g., no Tier 2 US bank reference for account products, uncertain product maturity, no analyst coverage for core banking)
- Is the Tachyon product-line documentation status ("to be expanded") a documentation gap or a product maturity gap? This is the most important internal question.

### Assembling the target universe

From bank signals collected across Streams 3 and 4:

- Organize by geography (USA, India, UK)
- Classify by tier (Tier 1 / $100B+ assets, Tier 2 / $10B–$100B, Tier 3 / $1B–$10B)
- Classify by horizon (Near-term 0–2 years: active signals; Medium-term 2–5 years: structural pressure)
- For each bank, record: name, tier, geography, signal type, source, URL
- Minimum 15 named institutions across all tiers and geographies
- Prioritize banks signaling core replacement or progressive migration over banks signaling digital banking front-end modernization (the latter may not require core replacement)

### Grounding the Zeta advisory

Cross-reference competitive landscape (Stream 3) with Zeta's product-line files:

- **Tachyon** — primary asset. Map its five product lines (Kernel, DDA, Credit Cards, CLM, Loans) against the competitive landscape. Critical question: which product lines are production-deployed vs. described in documentation? The product-line file states: "This is a placeholder brief. Individual product line details to be expanded in subsequent sessions." This must be addressed honestly in Part II.
- **Quark** — domain hubs for banking operations. Quark Origination, Quark Customer Servicing, Quark CLM are the most relevant. Same maturity question as Tachyon — all marked as "To be expanded."
- **Neutrino** — channel infrastructure for account experiences. Not a differentiator; table stakes.
- **Photon** — payment flows that debit/credit Tachyon accounts. Relevant as integration evidence but not the core value proposition for account products.
- **Evolution Fabric** — the potential differentiator. If Tachyon accounts are the ledger and Evolution Fabric is the operational model, the combination delivers something no core banking vendor offers: an explicit, governed domain model for account operations with AI agent participation. This is the thesis-differentiated positioning.
- **Trust Fabric** — customer identity, authentication, consent for account holders. Relevant for account onboarding and lifecycle.
- **Truth Fabric** — semantic definitions for account entities (balances, limits, statuses, product terms). Relevant for multi-product consistency.

Identify gaps honestly:

- Is Tachyon production-deployed at any bank for deposit accounts (DDA/CASA)? If not, the entire "Where to Play" section must be conditioned on product readiness.
- Does Tachyon have business banking capabilities (cash management, multi-entity structures, virtual accounts, treasury)? The current engagement area file describes these as capabilities, but the product-line file is a placeholder.
- How does Tachyon's ledger architecture compare to Thought Machine Vault's universal ledger or Mambu's composable ledger? Is it technically competitive?
- What bank references exist for Tachyon in any account product category (credit cards, DDA, loans)?

---

## 4. Phase 3: Document Writing

Section-by-section writing order. Target word counts are guidelines, not hard limits.

### PART I — THE OPPORTUNITY (Analyst voice, no Zeta references)

**Section 1: Market (~600 words)**

- Vendor-addressable TAM for account products and core banking technology, disaggregated from commonly cited total figures
- Revenue by geography (USA, India, UK/Europe)
- Revenue by bank tier — emphasizing the Tier 2–3 vendor-dependent segment
- Growth rates by sub-segment (core platforms, digital banking, business banking/cash management, origination, BaaS-enabling infrastructure)
- Build vs. buy patterns: Tier 1 increasingly building in-house; Tier 2–3 the primary vendor opportunity
- The fastest-growing sub-segments (cloud-native core, business banking digitization, BaaS-enabling platforms)
- Framing: core banking technology is the largest and slowest-moving category in banking technology. The replacement cycles are measured in decades, not years. But the structural pressures building against legacy cores are now reaching the point where deferral is more expensive than replacement.

**Section 2: How We Got Here (~400 words)**

Three eras of core banking architecture:

- **Era 1: Monolithic core (1970s–2000s).** Banks deployed comprehensive core banking systems — FIS, Fiserv, Temenos, Finacle, FLEXCUBE — that managed all account types, all products, all lifecycle events from a single platform. The core determined what products the bank could offer and how fast it could launch them. These systems were reliable, comprehensive, and deeply customized over decades of deployment.
- **Era 2: Channel overlay (2000s–2015).** Banks added internet banking, mobile banking, and digital account opening as layers on top of the unchanged core. Digital banking platforms (Backbase, Alkami, Q2) provided customer-facing experiences that consumed core APIs. The core remained the system of record; the channels were the system of engagement. The separation of front-end and back-end created an illusion of modernization while the fundamental constraint — the core determining product scope and speed — remained.
- **Era 3: Core pressure (2015–present).** Neobanks launched on cloud-native cores (Monzo on Thought Machine, N26 on Mambu) and demonstrated that modern account platforms could launch products in days, not months. Open banking mandates forced API exposure that legacy cores couldn't provide natively. BaaS demand required multi-tenant, API-first account infrastructure that monolithic cores weren't designed for. Deposit competition from fintechs forced product agility that legacy product configuration engines couldn't deliver. The pressure on the core is now structural, not cosmetic.

What was deferred: through all three eras, most established banks avoided replacing the core. They overlaid, wrapped, extended, and customized — but the underlying account processing engine remained. The result is the technology debt that now drives the structural shifts below.

**Section 3: Structural Shifts (6–8 shifts, ~2,500 words — the core)**

Each shift follows the pattern established in the payments and commercial cards analyses:

- The evidence (data points with citations)
- The opportunity by segment (Tier 1 / Tier 2 / Tier 3)
- Market-specific dynamics (USA / India / UK)

Anticipated shifts (final list determined by evidence quality in Phase 2):

1. Progressive core replacement displacing big-bang migration
2. Composable banking architecture replacing monolithic cores
3. Cloud-native core infrastructure becoming table stakes
4. Business banking digitization creating a separate modernization wave
5. Open banking mandates driving account infrastructure investment
6. Deposit competition from neobanks and fintechs forcing product agility
7. Embedded banking (BaaS) requiring modern account infrastructure
8. AI in account operations beyond origination

**Section 4: The Engagement Landscape (~500 words)**

Concrete engagement types banks are commissioning:

- **Progressive core migration** — product-by-product migration from legacy core. Start with one account type (typically DDA), prove the modern platform, migrate additional products. Run legacy and modern cores in parallel.
- **Digital account platform deployment** — modern digital banking platform for account opening, self-service, and lifecycle management, overlaying the existing core.
- **Business banking platform build** — purpose-built business banking capabilities (cash management, virtual accounts, multi-entity structures) either on a new core or as a specialized layer.
- **BaaS enablement** — modernizing account infrastructure to support fintech and non-bank partnerships. Multi-tenant, API-first, real-time account processing.
- **Deposit product innovation platform** — modern product configuration and pricing engine that enables rapid deposit product launch without core system changes. Can be deployed alongside legacy core.
- **Open banking account access** — API infrastructure for Section 1033, PSD2/3, Account Aggregator compliance. May or may not trigger core modernization depending on whether the bank chooses to wrap or replace.

Map each engagement type to bank tier and structural shift.

**Section 5: Competitive Landscape (~600 words)**

- Legacy incumbents: FIS, Fiserv, Jack Henry, Temenos, Finacle, BaNCS, FLEXCUBE — positioning, market share, vulnerabilities
- Modern challengers: Thought Machine, Mambu, 10x, Finxact (FIS) — scale of deployment, bank customer counts, the proof-point question (how many established banks, not just neobanks?)
- Digital banking platforms: Backbase, Alkami, Q2 — whether they compete with or complement core banking vendors
- Business banking specialists: Finastra, Bottomline, Kyriba, Intellect iGTB
- Product/pricing specialists: Zafin, SunTec — competing on product agility without core replacement
- The defining competitive question: is the market moving to "replace the core" or "augment the core"? The answer determines which competitive set is relevant.

**Section 6: Target Universe (~500 words)**

Named institutions organized by:

- Geography (USA, India, UK)
- Bank tier (Tier 1 / Tier 2 / Tier 3)
- Horizon (Near-term / Medium-term)
- For each: the observable evidence with navigable URL
- Framed as analytical observation, not sales targeting
- Distinguish between banks signaling full core replacement and banks signaling product-level or channel-level modernization — these are different buying events

---

### PART II — THE ADVISORY (Advisor voice, Zeta-specific)

**Section 7: Zeta's Position (~500 words)**

- Tachyon product lines mapped to the opportunity: Kernel (core infrastructure), DDA (demand deposits), Credit Cards, CLM, Loans. For each: what's production-deployed, what's described but unvalidated, what's missing.
- Quark domain hubs for account operations: Quark Origination, Quark Customer Servicing, Quark CLM. Maturity assessment.
- Evolution Fabric as the operational substrate: the thesis-differentiated positioning. If Tachyon is the account platform and Evolution Fabric provides the explicit, governed operational model, the combination addresses a gap that no core banking vendor fills. Core banking vendors deliver systems; they do not deliver the operational model that makes systems function as a coherent banking operation.
- Trust Fabric: customer identity and lifecycle for account holders.
- Honest gap assessment:
  - Product maturity: Are Tachyon product lines production-grade for the segments this analysis targets? The placeholder documentation is a signal.
  - Bank references: Does Zeta have any bank live on Tachyon for deposit accounts?
  - Business banking: Does Tachyon have cash management, virtual accounts, multi-entity capabilities?
  - Analyst coverage: No Gartner or Celent coverage for Tachyon as a core banking platform. Without analyst recognition, mid-market banks will not evaluate.
  - Geography: Is Tachyon certified / deployable in US and UK regulatory environments?

**Section 8: Where to Play (~500 words)**

Using the Right to Play / Right to Win framework:

- Which sub-segments to pursue (DDA/CASA modernization for Tier 2–3, BaaS-enabling infrastructure, business banking if capabilities exist)
- Which sub-segments to defer (full core replacement for Tier 1, treasury management, trade finance)
- Which geographies to prioritize (India for proof-of-concept given existing bank relationships, USA for revenue, UK for open banking-driven opportunity)
- Which bank tiers to target (Tier 2 primary; Tier 3 through partners or BaaS model; Tier 1 not initially)
- Explicit "do not pursue" calls where evidence is thin, competitive position is weak, or Tachyon product readiness is uncertain
- The sequencing question: should Zeta lead with account products (where Tachyon is the direct offering) or lead with payments/cards (where Photon/Electron are production-proven) and expand into accounts?

**Section 9: Risks and Gaps (~400 words)**

- What must be true: Tachyon must be production-ready for DDA/CASA at a bank of sufficient scale to serve as a reference. Without this, the account products opportunity is aspirational.
- Window risks: Thought Machine is winning Tier 2 bank deals (Standard Chartered, Lloyds, JPMorgan for specific products). If Thought Machine establishes 3–5 more Tier 2 references before Tachyon reaches production readiness, the window narrows. Mambu's SaaS model is becoming the default for BaaS-enabling cores. Visa's acquisition of Pismo signals platform consolidation.
- Capability gaps: business banking/cash management maturity, analyst recognition, US and UK regulatory certification
- Sales cycle reality: core banking deals are 2–5 year sales cycles. This is fundamentally different from the payments opportunity where card issuance deals can close in months. The GTM investment required is larger and the payback period is longer.
- Cannibalization risk: if Zeta pursues account products aggressively before Tachyon is production-ready, failed or delayed deployments could damage the brand in markets where payments and card deployments are proceeding successfully.

**Section 10: Recommended Actions (~400 words)**

- Near-term (0–2 years): specific actions conditioned on Tachyon product readiness. Focus on India bank deployments for DDA/CASA to build reference base. Engage Celent and Gartner for analyst coverage. Validate Tachyon against Thought Machine and Mambu architectures.
- Medium-term (2–5 years): US market entry for Tier 2 banks, business banking capability development, BaaS positioning
- Priority order: what to do first, second, third — and what to delay
- Which banks to approach first, and why (based on Target Universe evidence)
- The lead-with-payments-then-expand-to-accounts sequencing strategy: is this the right approach, or should account products be pursued independently?

**Section 11: Executive Summary (~400 words)**

- Written last
- Covers both Part I and Part II
- A board member who reads only this section should understand: the market opportunity for account products technology, the structural shifts creating it, the competitive landscape, Zeta's current position (honestly assessed), the honest gaps, and the recommended action with explicit conditions

---

## 5. Phase 4: Review

### Part I Checks

- Every data point has a source citation with a navigable, verified URL — or full bibliographic detail for paywalled sources
- No broken links — every URL confirmed to resolve to cited content
- No "according to [authority]" citations without a traceable reference
- All unverifiable claims flagged as `[unverified — needs manual confirmation]`
- No structural shift relies on assertion without evidence
- The "composable banking" and "progressive core replacement" theses are grounded in empirical deployment data, not just analyst advocacy
- Segment analysis (Tier 1/2/3) grounded in research, not generic
- Geographic analysis specific to USA, India, UK — not generic "global" claims
- No Zeta references, product names, or commercial voice anywhere in Part I
- Every bank named in the Target Universe has a citable evidence basis with navigable source link
- Document reads as external strategic analysis, not internal marketing
- The distinction between core replacement and core augmentation is consistently maintained

### Part II Checks

- Every recommendation traces back to evidence presented in Part I
- Gaps and weaknesses stated honestly, not minimized — particularly Tachyon product maturity
- Recommendations specific and prioritized, not a generic list
- "Do not pursue" and "delay" recommendations included where warranted — particularly for segments where Tachyon readiness is uncertain
- Product and asset references accurate against repo's product-line files (Tachyon, Quark, Evolution Fabric, Trust Fabric, Neutrino, Photon)
- The advisory does not claim capabilities that the product-line documentation does not support
- Recommendations are conditioned on product readiness where appropriate ("If Tachyon DDA is production-ready, then...")

### Editorial Rigor (Part I only) — Eight Tests

1. **Does every sentence earn its place?** No dead weight. Every sentence advances the argument.
2. **Tonal consistency.** Board-grade prose throughout. No drops to filing-cabinet language.
3. **Commercial voice.** Zero first-person plural. Zero market opportunity language. Zero buyer-readiness framing. Zero competitive positioning.
4. **Meta-narration.** No "this section will explore..." The structure speaks for itself.
5. **Vocabulary discipline.** Consistent terms throughout. "Core banking platform" not alternating with "account processing engine" and "banking system" without consistent definition.
6. **Shelf life.** No time-fragile language. Structural arguments survive without timestamps.
7. **Specificity vs. thesis level.** No performance claims without evidence. No implementation details.
8. **Audience neutrality.** Consumable by bank CIOs, bank CEOs, Zeta's board. Not a sales document.

---

## 6. Key Differences from Other Engagement Areas


| Dimension                      | Payments                                                                                               | Commercial Cards                                                                                           | Account Products & Core Banking                                                                                                                                                                                                                                       |
| ------------------------------ | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Market structure**           | Oligopoly (FIS, Fiserv, GP) + fragmented challengers                                                   | Two-sided: card issuance vs. spend management                                                              | Oligopoly (FIS, Fiserv, Temenos, Finacle, BaNCS) + small modern challenger cohort (Thought Machine, Mambu, 10x). Fewer viable alternatives for buyers than payments.                                                                                                  |
| **Replacement cycle**          | 5–10 years for payment hubs                                                                            | 3–5 years for card platforms                                                                               | **15–25 years for core banking.** The longest replacement cycle in banking technology. This is the most consequential technology decision a bank makes.                                                                                                               |
| **Competitive intensity**      | Very high                                                                                              | High (convergence creating new entrants)                                                                   | High but **different character.** Incumbents have 20+ year contracts. Modern challengers are growing but have limited Tier 2+ deployment evidence. The barrier to entry is deployment proof points, not technology.                                                   |
| **Primary regulatory driver**  | Very strong — multiple concurrent mandates with hard deadlines (FedNow, tokenization, ISO 20022)       | Strong — tax regulation (India), SOX (US), CSRD (EU)                                                       | **Moderate to strong.** Section 1033, open banking, FDIC Part 370, Basel III/IV. But fewer hard "replace by this date" deadlines than payments. Core replacement is driven more by competitive pressure and technology debt than by regulatory mandate.               |
| **Geographic concentration**   | USA 30–40% of payments tech spend                                                                      | USA ~45% of commercial card market                                                                         | USA largest market. India significant (Finacle/BaNCS home market). **UK is a stronger third market** for core banking than for payments — open banking leadership, CASS, challenger banks as proof points.                                                            |
| **Central strategic argument** | Banks must replace infrastructure they have been layering for 20 years. Technology debt is structural. | The commercial card market is bifurcated between issuance and spend management. Convergence is structural. | **The core banking system is the most consequential technology constraint on a bank's ability to evolve.** Progressive, product-by-product replacement is becoming viable. The question is not whether cores will be replaced — it is how, at what pace, and by whom. |
| **Sales cycle**                | 6–18 months for card/payment platform deals                                                            | 6–12 months for card program deals                                                                         | **2–5 years for core banking decisions, 3–7 years for implementation.** This fundamentally changes GTM investment, payback period, and the importance of reference customers.                                                                                         |
| **Analyst coverage**           | Strong — multiple market sizing reports, Magic Quadrants                                               | Moderate — card issuance well-covered, spend management less so                                            | **Strong.** Gartner Magic Quadrant for Global Retail Core Banking. Celent Dimensions. IBS Intelligence. The market is well-analyzed.                                                                                                                                  |
| **Zeta's current position**    | **Strong** — Photon product lines production-deployed for card issuance, tokenization, acquiring       | **Production-proven in India benefits** — Electron Benefits powers Pluxee (11K+ corporates)                | **Uncertain.** Tachyon product-line documentation is placeholder ("to be expanded"). The critical internal question: is this a documentation gap or a product maturity gap?                                                                                           |
| **Vendor-addressable TAM**     | $60–85B (narrow); $150–200B (broad)                                                                    | $28–30B                                                                                                    | **$25–40B** (core banking platforms + digital banking platforms + business banking technology). Narrower than payments but growing faster in the modern platform sub-segment.                                                                                         |


---

## 7. Execution Approach

### Sub-agent batching strategy

Six research streams, max 4 concurrent sub-agents:

**Batch 1 (4 concurrent):**

- Stream 1: Market sizing and revenue pools
- Stream 2: Regulatory landscape and account mandates
- Stream 3: Competitive landscape
- Stream 4: Structural shifts and core modernization activity

**Batch 2 (2 concurrent):**

- Stream 5: Business banking, cash management, and treasury modernization
- Stream 6: Deposit innovation, open banking, and account portability

### Estimated turns


| Phase                               | Estimated Turns   |
| ----------------------------------- | ----------------- |
| Phase 1, Batch 1 (Streams 1–4)      | 1 turn (parallel) |
| Phase 1, Batch 2 (Streams 5–6)      | 1 turn (parallel) |
| Phase 2: Synthesis and gap-fill     | 2 turns           |
| Phase 3: Document writing (Part I)  | 2–3 turns         |
| Phase 3: Document writing (Part II) | 1–2 turns         |
| Phase 4: Review and editorial rigor | 1–2 turns         |
| **Total**                           | **8–11 turns**    |


### Output file path

`org-8.0/what-we-sell/strategy/engagement-areas/account-products-and-banking.md`

---

## 8. Output Files

### Primary document

`org-8.0/what-we-sell/strategy/engagement-areas/account-products-and-banking.md` — replaces the current CIO-facing capability catalogue with the two-part opportunity analysis and advisory.

### Research retention

**Location:** `org-8.0/what-we-sell/strategy/_research/account-products-and-banking/`

**Files to create:**


| File                                     | Contents                                                                                                                                               |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `s1-market-sizing.md`                    | Core banking, digital banking, business banking technology TAM data. Claim/Value/Source/URL/Verified table.                                            |
| `s2-regulatory-landscape.md`             | USA, India, UK/EU regulations with compliance deadlines, penalties, infrastructure implications.                                                       |
| `s3-competitive-landscape.md`            | By-category competitor profiles. Revenue, positioning, bank customers, architecture, strengths, weaknesses, vulnerabilities.                           |
| `s4-structural-shifts.md`                | Evidence for each structural shift. Data points, regulatory citations, bank-tier analysis. Bank modernization signals.                                 |
| `s5-business-banking-cash-management.md` | Business banking technology market sizing, virtual accounts, cash management vendors, SME banking challengers.                                         |
| `s6-deposit-innovation-open-banking.md`  | Neobank deposit data, open banking adoption, account portability evidence, deposit product innovation examples.                                        |
| `synthesis-notes.md`                     | Cross-references, contradictions, evidence quality ratings, Right to Play / Right to Win mapping, editorial decisions, target universe assembly notes. |
| `unverified-claims.md`                   | Every claim flagged as `[unverified — needs manual confirmation]` with context.                                                                        |


**Format for stream files:**

- Research date and engagement area
- Data table: Claim | Value | Source | URL | Verified (Yes/No)
- Key findings as structured bullets
- Gaps and unresolved questions
- Raw notes and excerpts

**Cross-references to existing research:**

- `_research/payments/s3-competitive-landscape.md` — FIS, Fiserv competitive data. Reference rather than re-research. Note overlap in `synthesis-notes.md`.
- `_research/payments/s2-regulatory-landscape.md` — PSD2/PSD3, India regulatory landscape. Reference overlapping regulatory content.
- `_research/digital-identity-and-trust/s2-regulatory-landscape.md` — KYC/identity regulatory content relevant to account opening.
- `_research/digital-identity-and-trust/s3-competitive-landscape.md` — Identity verification vendors relevant to account onboarding.
- `market-study/` files — check for any overlapping deposit, account, or banking infrastructure research.

---

## 9. What This Plan Does NOT Do

- Does not write the opportunity analysis itself.
- Does not produce generic research streams applicable to any engagement area. Every stream, competitor, regulation, and structural shift is specific to account products and core banking.
- Does not include more than 3 geographic markets (USA, India, UK). Middle East/Gulf will be assessed as a potential fourth only if Phase 1 evidence shows meaningful opportunity concentration.
- Does not plan for a document shorter than 5,500 words or longer than 7,500 words.
- Does not blend the analyst and advisor voices. Part I and Part II are structurally separated.
- Does not include banks in the Target Universe without specifying evidence sources.
- Does not cite sources without navigable URLs or full bibliographic detail.
- Does not discard research output. Every stream's raw findings are saved to `_research/account-products-and-banking/`.
- Does not assume Tachyon product maturity. Part II must honestly assess product readiness and condition recommendations on it.

