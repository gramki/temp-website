---
name: Lending & Credit Opportunity Analysis
overview: "McKinsey-grade two-part opportunity analysis (Part I: independent analyst assessment, Part II: Zeta strategic advisory) for the Lending and Credit engagement area. Replaces the current CIO-facing capability catalogue."
todos:
  - id: p1b1
    content: Phase 1 Batch 1 — Research Streams 1–4 (market sizing, regulatory landscape, competitive landscape, structural shifts). Raw output saved to _research/lending-and-credit/s1–s4 files.
    status: pending
  - id: p1b2
    content: Phase 1 Batch 2 — Research Streams 5–7 (embedded credit & BNPL disruption, AI in credit decisioning & servicing, commercial lending technology gap). Raw output saved to _research/lending-and-credit/s5–s7 files.
    status: pending
  - id: p2-synthesis
    content: "Phase 2 — Synthesis & gap-fill: cross-reference streams, rate evidence quality, verify URLs, assemble target universe, map Right to Play / Right to Win. Save synthesis-notes.md and unverified-claims.md."
    status: pending
  - id: p3-market
    content: Phase 3 Part I §1 — Market section. Vendor-addressable TAM across lending technology sub-segments.
    status: pending
  - id: p3-history
    content: Phase 3 Part I §2 — How We Got Here. Three eras of lending technology.
    status: pending
  - id: p3-shifts
    content: Phase 3 Part I §3 — Structural Shifts. 7–8 shifts evidenced with data, regulatory citations, bank-tier and geographic analysis.
    status: pending
  - id: p3-engagements
    content: Phase 3 Part I §4 — Engagement Landscape. Program types mapped to bank tier and structural shift.
    status: pending
  - id: p3-competitive
    content: Phase 3 Part I §5 — Competitive Landscape. Incumbents, modern challengers, specialists profiled.
    status: pending
  - id: p3-targets
    content: Phase 3 Part I §6 — Target Universe. Named institutions across USA/India/UK with cited evidence.
    status: pending
  - id: p3-position
    content: Phase 3 Part II §7 — Zeta's Position. Tachyon Loans, Quark Lending, Evolution Fabric mapped. Gaps identified honestly.
    status: pending
  - id: p3-wheretoplay
    content: Phase 3 Part II §8 — Where to Play. Segments, geographies, tiers prioritized with explicit deferrals.
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
    content: "Phase 4 — Part I review: all citations verified, no Zeta references, no commercial voice, segment/geographic specificity confirmed, all target universe entries evidenced."
    status: pending
  - id: p4-partII
    content: "Phase 4 — Part II review: all recommendations trace to Part I evidence, gaps stated honestly, product references verified against repo product-line files."
    status: pending
  - id: p4-editorial
    content: "Phase 4 — Editorial rigor review (Part I only): all 8 tests from editorial-rigor-review skill."
    status: pending
isProject: true
---

# Lending and Credit — Opportunity Analysis & Strategic Advisory Plan

**Engagement Area:** Lending and Credit
**Output:** `org-8.0/what-we-sell/strategy/engagement-areas/lending-and-credit.md`
**Target length:** 5,500–8,000 words (two-part structure)
**Current state:** 116-line CIO-facing capability catalogue. Explicitly marked as placeholder. Must be fully replaced.

---

## 1. Model Recommendation

**Orchestration:** Default model. The orchestrator must manage seven parallel research streams across two batches, run synthesis and cross-referencing, enforce the analyst/advisor voice boundary, and apply the eight editorial rigor tests. Lending and credit spans multiple distinct sub-markets (consumer, mortgage, commercial, embedded) — each with its own competitive landscape, regulatory regime, and technology stack — requiring sustained reasoning across a complex multi-segment analysis.

**Research sub-agents:** Default model for all seven streams. Rationale:

- **Streams 1–4** (market sizing, regulatory landscape, competitive landscape, structural shifts) have **strong analyst coverage**. Lending technology infrastructure is a well-studied category: Celent publishes annual vendor evaluations for loan origination, servicing, and commercial lending platforms. Forrester covers digital lending. IDC, Gartner, Grand View Research, and Mordor Intelligence publish market sizing reports. The competitive landscape is well-documented through SEC filings (nCino, Blend, ICE/Black Knight, Jack Henry, Finastra) and analyst reports. The default model can synthesize these effectively.
- **Stream 5** (embedded credit and BNPL disruption) has **strong coverage** from multiple perspectives — fintech analyst reports (CB Insights, PitchBook), regulatory scrutiny (CFPB BNPL reports, RBI Digital Lending Guidelines), and public company disclosures (Affirm, Klarna, Afterpay/Block). This is a high-profile category with dense evidence.
- **Stream 6** (AI in credit decisioning and servicing) has **moderate to strong coverage**. AI/ML model risk management is heavily regulated (SR 11-7, OCC guidance, EU AI Act high-risk classification for credit scoring). Analyst coverage exists for AI in lending (McKinsey, BCG, Deloitte surveys). Vendor activity is strong (Upstart, Zest AI, Pagaya). However, **AI in loan servicing and collections** has thinner coverage — research must emphasize primary evidence (vendor product launches, bank earnings call mentions, patent activity).
- **Stream 7** (commercial lending technology gap) has **moderate coverage**. Commercial lending technology is a recognized but less thoroughly sized sub-category. Key vendors (nCino, Finastra, Temenos) have public data. However, the **mid-market commercial lending gap** — the specific underservice of Tier 2–3 banks in commercial lending technology — requires synthesis across multiple partial sources rather than a single market report.

**Impact on research approach:** Lending has broader analyst coverage than emerging areas like agentic operations, but the market is fragmented across sub-segments (consumer origination, mortgage, commercial, servicing, collections, embedded credit). No single market report covers the full vendor-addressable opportunity. Market sizing must be constructed by aggregating sub-segment estimates — similar to the digital identity analysis but with better-sourced component parts.

---

## 2. Phase 1: Parallel Research (7 Streams)

### Stream 1: Market Sizing and Revenue Pools

**What to gather:**

- Vendor-addressable TAM for each sub-segment of lending technology infrastructure — what banks spend on platforms, not total loan volume:
  - Loan origination systems (LOS) — consumer, mortgage, commercial
  - Loan management / servicing systems (LMS) — repayment, interest accrual, modification, forbearance
  - Credit decisioning and underwriting platforms — traditional scorecards, AI/ML-based decisioning, alternative data platforms
  - Collections and recovery systems
  - Commercial lending platforms — working capital, revolving credit, trade finance, covenant monitoring
  - Embedded lending / lending-as-a-service infrastructure — BNPL, POS credit, API-driven lending
- Revenue breakdown by geography (USA, India, UK)
- Revenue breakdown by bank tier where available (Tier 1, Tier 2, Tier 3)
- Growth rates (CAGR) by sub-segment
- Build vs. buy patterns by bank tier — which tiers build in-house vs. buy from vendors
- Lending technology spend as a percentage of total bank IT spend

**Sources to target:**

- Celent (annual lending technology reports — LOS rankings, vendor evaluations)
- Forrester (Digital Lending wave reports)
- Gartner (Market Guide for Lending Platforms)
- Grand View Research, Mordor Intelligence, MarketsandMarkets, Allied Market Research (lending technology market reports)
- IDC (financial services IT spending breakdowns)
- Cornerstone Advisors ("What's Going On in Banking" annual survey — technology adoption data by bank tier)
- SEC filings for public lending technology vendors: nCino (10-K), Blend Labs (10-K), ICE (Encompass/Black Knight segment), Jack Henry (10-K), Finastra (parent Detica/Vista reports)
- BCG/McKinsey/Bain financial services technology reports that include lending segments
- Federal Reserve Bank surveys on bank technology adoption

**Geographic scope:** Global with USA, India, UK breakdowns.

**How data will be used:** Part I, Section 1 (Market). Establishes the prize. Sub-segment breakdowns reveal where spend is concentrated (origination vs. servicing vs. commercial) and where growth is accelerating (embedded lending, AI decisioning).

**Citation requirement:** Every data point must include a navigable URL or full bibliographic detail per the Citation Standard. Flag as `[unverified — needs manual confirmation]` if the source cannot be linked.

---

### Stream 2: Regulatory Landscape and Lending Mandates

**What to gather:**

- Specific regulations that force banks to invest in lending infrastructure — with compliance requirements, penalty regimes, and infrastructure implications
- For each regulation: what capability it demands, what the compliance status is, and what infrastructure investment it forces
- Regulatory pressure on AI/ML in credit decisioning — explainability, fairness, model risk management

**Regulations to cover by geography:**

**USA:**

- Equal Credit Opportunity Act (ECOA) / Regulation B — adverse action notice requirements, prohibited basis for credit decisions, implications for AI/ML model fairness and explainability
- Fair Housing Act and Home Mortgage Disclosure Act (HMDA) — fair lending data collection and reporting, disparate impact analysis
- Community Reinvestment Act (CRA) — final 2023 rule update modernizing assessment areas and metrics, implications for lending in underserved communities
- Truth in Lending Act (TILA) / Regulation Z — disclosure requirements, implications for embedded lending and BNPL
- Real Estate Settlement Procedures Act (RESPA) — mortgage servicing rules, loss mitigation requirements
- CFPB oversight — BNPL interpretive rule (treating BNPL as credit under TILA), rulemaking on AI in lending, Section 1071 small business lending data collection rule
- OCC/Fed/FDIC interagency guidance on model risk management (SR 11-7 / OCC 2011-12) — implications for AI/ML credit models
- OCC/FDIC/Fed joint statement on AI — specific to lending and credit decisions
- Dodd-Frank Section 1033 (open banking data access) — implications for alternative credit data and consumer-permissioned data in underwriting

**India:**

- RBI Digital Lending Guidelines (September 2022) — first-loss default guarantee (FLDG) norms, mandatory bank intermediation, restrictions on fintech lending models
- RBI Master Direction on NBFC — Systemically Important Non-Deposit taking Company and Deposit taking Company — prudential norms for lending
- RBI Fair Practices Code for NBFCs and digital lenders
- Account Aggregator framework — consent-based credit data sharing, implications for alternative data underwriting
- RBI guidelines on co-lending / co-origination — bank-NBFC partnerships
- Priority sector lending norms — mandatory lending to agriculture, MSMEs, weaker sections
- Credit Information Companies (Regulation) Act — credit bureau framework

**UK:**

- FCA Consumer Duty (effective July 2023) — fair value assessments, vulnerable customer obligations, implications for lending product design and servicing
- MCOB (Mortgages and Home Finance: Conduct of Business) — mortgage lending and servicing standards
- FCA authorized push payment (APP) fraud rules — implications for disbursement
- PRA supervisory expectations on model risk management (SS1/23)
- FCA and PRA guidance on AI/ML in financial services
- Open Banking / Smart Data Bill — consumer credit data portability, implications for alternative underwriting

**Sources to target:**

- Official regulatory texts (CFPB, OCC, Fed, FDIC, FCA, PRA, RBI)
- CFPB rulemaking activity and enforcement actions (CFPB.gov)
- RBI circulars and master directions (RBI.org.in)
- Law firm analyses (Davis Polk, Sullivan & Cromwell, Mayer Brown — for readable summaries with compliance timelines)
- Regulatory compliance trackers (PwC, Deloitte financial services regulatory outlook)
- Cross-reference with `org-8.0/what-we-sell/strategy/_research/payments/s2-regulatory-landscape.md` for any overlapping regulatory content (Dodd-Frank 1033, India RBI digital payments regulations)

**Geographic scope:** USA (primary — heaviest fair lending regulation), India (RBI digital lending), UK (FCA Consumer Duty, open banking credit).

**How data will be used:** Part I, Sections 2 (How We Got Here) and 3 (Structural Shifts). Fair lending regulations and AI/ML governance requirements are the primary forcing functions for lending infrastructure investment. The regulatory burden on AI in credit decisioning is a structural shift unto itself.

**Citation requirement:** Every regulation cited must link to the official text or a specific regulatory guidance document.

---

### Stream 3: Competitive Landscape

**What to gather:**

For each competitor category, identify the key players and for each: positioning, target market (bank tier, geography), revenue model, product scope (origination, servicing, commercial, embedded), strengths, weaknesses, and vulnerabilities.

**Categories and key players to map:**


| Category                                    | Players to Research                                                                                                                                                                |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Legacy core lending (incumbents)**        | FIS (lending modules), Fiserv (LoanServ, Mortgage Director), Jack Henry (lending solutions), Temenos (Infinity lending), Finastra (Fusion Mortgagebot, Fusion Loan IQ, Fusion CML) |
| **Modern cloud-native origination**         | nCino (Bank Operating System — lending), Blend Labs (mortgage + consumer origination), MeridianLink (consumer lending, mortgage), Tavant (mortgage technology)                     |
| **Mortgage-specific platforms**             | ICE Mortgage Technology (Encompass, formerly Ellie Mae), Black Knight (now ICE — MSP servicing platform), Optimal Blue (pricing/secondary), CoreLogic                              |
| **Commercial lending specialists**          | nCino (commercial), Finastra Fusion CML, Moody's Analytics (CreditLens), Baker Hill, Abrigo, Numerated                                                                             |
| **AI-native credit decisioning**            | Upstart, Zest AI, Pagaya, Scienaptic AI, Provenir                                                                                                                                  |
| **Embedded lending / lending-as-a-service** | Amount (formerly Avant), Blend Labs (embedded), Mambu (lending core), Thought Machine (lending capabilities), Finzly                                                               |
| **BNPL / point-of-sale credit**             | Affirm, Klarna, Afterpay (Block), Sezzle, Splitit                                                                                                                                  |
| **Servicing and collections**               | FICO (Debt Manager), Fiserv (LoanServ), Black Knight/ICE (MSP), Aculocity, TrueAccord (AI collections)                                                                             |
| **India lending technology**                | Nucleus Software, Newgen Software, Perfios (credit data), Jocata, LendingKart platform, nCino India operations                                                                     |


**For each player, capture:**

- Annual revenue or ARR (where public or estimable) — for the lending segment specifically
- Banking-specific customer count and notable bank logos
- Geographic focus and bank tier focus
- Product scope: which lending lifecycle stages they cover (origination, decisioning, servicing, collections, commercial)
- Whether they serve as point solution or end-to-end platform
- Recent M&A activity and partnership announcements
- Vulnerabilities: which lifecycle stages they do NOT cover, which bank tiers they do NOT serve, where their architecture limits composability or AI integration

**Sub-task — bank modernization signals:**

> Identify specific banks that have publicly signaled lending modernization activity — through earnings calls, press releases, RFP announcements, vendor partnership disclosures, or analyst commentary. For each: bank name, tier, geography, the signal (which lending capability is being modernized), the source, and a navigable URL.

**Sources to target:**

- SEC filings (10-K/10-Q) for public competitors: nCino, Blend, ICE, Jack Henry, FICO
- Celent vendor evaluations (LOS, mortgage, commercial lending)
- Forrester Wave: Digital Lending (latest)
- Gartner Market Guide for Lending Platforms
- Earnings call transcripts (Seeking Alpha, Motley Fool Transcripts)
- Vendor press releases (partnership announcements with banks)
- Crunchbase / PitchBook (funding rounds, M&A)
- American Banker / National Mortgage News (vendor deal announcements)

**Geographic scope:** Global, with emphasis on USA, India, UK vendors.

**How data will be used:** Part I, Section 5 (Competitive Landscape) and Part II, Section 7 (Zeta's Position — relative to competitors).

**Citation requirement:** Every competitive claim must be sourced. Revenue figures from SEC filings or credible analyst estimates. Product scope claims from vendor documentation.

---

### Stream 4: Structural Shifts and Bank Modernization Activity

**What to gather:**

Evidence for 7–8 structural shifts reshaping the lending technology infrastructure market. Each shift must be evidenced with data, regulatory citations, competitive activity, and bank-tier analysis.

**Candidate structural shifts to investigate:**

1. **Legacy origination systems cannot meet speed expectations.** Fintech lenders and digital banks have compressed application-to-disbursement from weeks to minutes for consumer loans. Banks with batch-driven origination lose volume. Evidence: origination speed benchmarks by channel (branch vs. digital vs. fintech), consumer expectation surveys, bank digital lending adoption rates by tier, fintech market share gains in personal lending.
2. **AI/ML credit decisioning is shifting from experimental to regulated operational requirement.** Banks adopting AI for credit scoring face simultaneous pressure to modernize (competitive urgency) and to govern (regulatory mandate). SR 11-7, ECOA adverse action, and EU AI Act high-risk classification create a regulatory framework that legacy credit engines cannot satisfy. Evidence: AI adoption in credit decisioning surveys, regulatory enforcement actions, model risk management investment data, vendor deployment counts.
3. **Post-pandemic servicing infrastructure proved inadequate.** COVID-era forbearance programs exposed the brittleness of legacy servicing systems — banks that managed millions of loan modifications on inflexible platforms understand the operational constraint. The structural argument: servicing systems designed for steady-state operations cannot handle mass modification, dynamic restructuring, or real-time policy changes. Evidence: forbearance volume data (CFPB, MBA), bank earnings commentary on servicing challenges, vendor servicing modernization deals.
4. **Embedded credit is reshaping the point of origination.** BNPL, POS credit, and micro-lending are moving lending into non-banking channels. Banks that cannot offer lending as an embeddable API-first service lose origination volume. Evidence: BNPL market size and growth, CFPB regulatory actions, bank-fintech BNPL partnerships, embedded lending platform adoption.
5. **Commercial lending remains operationally primitive.** Working capital, revolving credit, trade finance, and covenant monitoring in mid-market banks still run on spreadsheets, manual workflows, and legacy systems. The technology gap between commercial and consumer lending is wide and growing. Evidence: commercial lending technology adoption surveys, vendor revenue data, bank earnings commentary on commercial lending investments.
6. **Open banking and alternative data are reshaping credit assessment.** Consumer-permissioned data (Account Aggregator in India, Dodd-Frank 1033 in USA, Open Banking in UK) enables thinner-file borrowers to access credit and allows lenders to underwrite with richer, real-time data. Evidence: Account Aggregator adoption data, CFPB 1033 rulemaking, open banking credit products launched, alternative data underwriting outcomes.
7. **Fair lending scrutiny is intensifying — and AI amplifies the risk.** CFPB and DOJ are increasing fair lending enforcement. AI/ML models that outperform traditional scorecards on accuracy may introduce or amplify disparate impact. Banks face a dual bind: legacy scorecards limit inclusion; AI models create explainability and fairness challenges. Evidence: CFPB enforcement actions, ECOA settlements, fair lending audit data, model fairness research.
8. **(Candidate — include if evidence supports)** **Collections is becoming an AI-first domain.** AI-powered collections triage, communication optimization, and workout strategy are showing measurable results. Evidence: TrueAccord and similar vendor outcomes, bank collections modernization announcements, regulatory guidance on AI in collections.

**For each shift, gather:**

- 3–5 data points with sources and URLs
- Regulatory citations that create or accelerate the shift
- Competitive activity (vendors capitalizing on the shift)
- Analysis by bank tier (how does this shift affect Tier 1 vs. Tier 2 vs. Tier 3 differently?)
- Geographic variation (USA vs. India vs. UK)

**Sub-task — bank modernization signals:**

> Identify specific banks that have publicly signaled lending modernization activity — through earnings calls, press releases, RFP announcements, analyst commentary, or vendor partnership disclosures. For each: bank name, tier, geography, the signal, the source, and a navigable URL.

**Sources to target:**

- Federal Reserve Senior Loan Officer Opinion Survey (SLOOS) — lending conditions and technology investment signals
- CFPB consumer complaint data (lending categories)
- MBA (Mortgage Bankers Association) technology surveys and reports
- American Banker, National Mortgage News (bank technology announcements)
- Bank earnings call transcripts (search for "origination," "lending platform," "loan servicing," "commercial lending," "AI in credit," "digital lending," "BNPL," "embedded lending")
- Vendor partnership press releases
- Celent/Forrester/IDC banking technology surveys

**Geographic scope:** USA, India, UK.

**How data will be used:** Part I, Sections 2 (How We Got Here), 3 (Structural Shifts), 4 (Engagement Landscape), and 6 (Target Universe).

**Citation requirement:** Every structural shift claim must be grounded in at least three independent data points with navigable URLs.

---

### Stream 5: Embedded Credit and BNPL Disruption

**Why a separate stream:** Embedded credit and BNPL represent a structural disruption to bank lending origination — not just a new product category, but a shift in who controls the customer relationship and where credit decisions happen. This has regulatory, competitive, and infrastructure implications distinct from traditional lending modernization.

**What to gather:**

- BNPL market size, volume, and growth (global, USA, India, UK)
- CFPB BNPL interpretive rule and enforcement activity — treating BNPL as credit under TILA, adverse action and dispute resolution requirements
- RBI Digital Lending Guidelines impact on BNPL and fintech lending models in India
- FCA Consumer Duty implications for BNPL in UK
- Bank responses: which banks have launched BNPL / embedded lending products, which have partnered with BNPL providers, which are building their own embedded lending infrastructure
- Embedded lending as a platform play — lending-as-a-service infrastructure (Amount, Mambu, Blend, Thought Machine) enabling banks to offer lending through non-banking channels
- Consumer credit data: BNPL's impact on credit bureau reporting, credit visibility, and consumer debt levels
- Vendor product launches addressing bank-offered BNPL / embedded credit
- Return rates, loss rates, and credit performance of BNPL vs. traditional credit products

**Sources to target:**

- CFPB BNPL report (2022, 2024 updates)
- CFPB enforcement actions on BNPL providers
- RBI Digital Lending Guidelines (September 2022) and subsequent circulars
- FCA Consumer Duty and BNPL regulation proposals
- SEC filings: Affirm (10-K), Block/Afterpay (segment data), Sezzle (10-K)
- CB Insights / PitchBook (BNPL market data and funding)
- TransUnion / Experian / Equifax credit data studies on BNPL impact
- Bank press releases and earnings calls mentioning BNPL or embedded lending launches
- BCG/McKinsey/Bain reports on embedded finance and lending disruption

**Geographic scope:** USA (CFPB regulation), India (RBI guidelines), UK (FCA regulation).

**How data will be used:** Part I, Section 3 (Structural Shift 4 — embedded credit reshaping origination) and Part I, Section 5 (Competitive Landscape — BNPL and embedded lending providers). Part II, Sections 8–10 (Zeta's embedded lending positioning via Tachyon Loans + Photon).

**Citation requirement:** Regulatory sources must link to official texts. Market data must cite the issuing firm. BNPL provider data from SEC filings preferred.

---

### Stream 6: AI in Credit Decisioning and Loan Servicing

**Why a separate stream:** AI in lending is at the intersection of massive competitive opportunity and intense regulatory scrutiny. It spans credit underwriting, servicing triage, collections optimization, and portfolio monitoring — each with distinct regulatory and technology requirements. The regulatory dimension (SR 11-7, ECOA, EU AI Act) makes this a uniquely complex area where technology capability and governance capability are inseparable.

**What to gather:**

- AI/ML adoption rates in credit decisioning — by bank tier, by geography
- Regulatory framework for AI/ML in credit: SR 11-7 model risk management, OCC guidance, ECOA adverse action requirements for AI-generated decisions, EU AI Act Annex III high-risk classification for creditworthiness assessment
- Performance data: AI/ML underwriting vs. traditional scorecards (approval rates, loss rates, default prediction accuracy, disparate impact metrics)
- Vendor landscape: AI-native credit decisioning vendors (Upstart, Zest AI, Pagaya, Scienaptic) — revenues, bank deployments, regulatory track record
- Alternative data in underwriting: cash flow underwriting, bank transaction data, Account Aggregator data (India), open banking data (UK) — adoption rates, regulatory acceptance
- AI in loan servicing: automated loan modification, forbearance management, customer communication optimization — vendor capabilities, bank deployment evidence
- AI in collections: intelligent triage, communication channel optimization, workout strategy optimization — TrueAccord, FICO, vendor evidence
- AI in portfolio analytics and early warning: vintage analysis, concentration risk, predictive default modeling
- Model governance infrastructure: MLOps for lending, model validation, bias testing, explainability tools

**Sources to target:**

- OCC/Fed/FDIC SR 11-7 and related model risk management guidance
- CFPB rulemaking and statements on AI in lending
- EU AI Act (Annex III, high-risk AI systems — credit scoring explicitly listed)
- Upstart SEC filings (10-K — bank partner counts, loan volumes, model performance data)
- Zest AI case studies and publications
- McKinsey/BCG/Deloitte AI in banking surveys (lending-specific sections)
- Federal Reserve AI in lending research papers
- Brookings Institution / Urban Institute research on AI in credit and fair lending
- Bank earnings call transcripts mentioning AI in credit, ML models, alternative data underwriting

**Geographic scope:** USA (primary — heaviest regulatory scrutiny), India (Account Aggregator + RBI), UK (PRA SS1/23 model risk).

**How data will be used:** Part I, Section 3 (Structural Shifts 2 and 7 — AI in decisioning, fair lending scrutiny). Part II, Sections 7–10 (Zeta's position via Evolution Fabric/Seer for AI governance, Cognitive Audit Fabric for decision auditability, Tachyon Loans for integrated AI decisioning).

**Citation requirement:** Regulatory guidance must be sourced to official texts. Performance claims from vendors must identify the vendor as source. Academic/research claims from named institutions with URLs.

---

### Stream 7: Commercial Lending Technology Gap

**Why a separate stream:** Commercial lending is a distinct sub-market with fundamentally different dynamics from consumer lending. The technology gap is wider, the operational complexity is greater, and the competitive landscape is sparser. Mid-market commercial lending — working capital, revolving credit, trade finance for SMEs and mid-cap corporates — is arguably the most underserved segment in all of lending technology.

**What to gather:**

- Commercial lending technology market size and growth — distinct from consumer/mortgage
- Technology adoption by bank tier: what do Tier 1, Tier 2, and Tier 3 banks use for commercial lending? What percentage still rely on spreadsheets and manual workflows?
- Commercial lending lifecycle complexity: covenant monitoring, collateral management, relationship-level exposure, multi-facility structures, draw/repayment management, financial spreading, credit review cycles
- Vendor landscape: nCino (commercial lending), Finastra Fusion CML, Moody's CreditLens, Baker Hill, Abrigo, Numerated — depth of coverage, bank tier focus, deployment model
- Trade finance technology: distinct sub-segment with its own vendor landscape (Finastra, Surecomp, China Systems, Bolero) — include only to the extent that banks bundle trade finance with commercial lending modernization
- SBA and government-guaranteed lending technology — PPP experience exposed infrastructure gaps in community and regional banks
- India commercial lending: MSME lending, SIDBI programs, TReDS (Trade Receivables Discounting System), India digital lending guidelines for business lending
- UK commercial lending: British Business Bank programs, FCA oversight of SME lending, open banking for business credit assessment

**Sources to target:**

- nCino SEC filings (10-K — commercial lending segment, bank customer counts, revenue by segment)
- Celent commercial lending technology reports
- ABA (American Bankers Association) commercial lending surveys
- Federal Reserve SLOOS (Senior Loan Officer Opinion Survey) — commercial lending conditions
- SBA lending data (PPP program data, ongoing SBA lending volumes)
- RBI MSME lending data and priority sector compliance reports
- Vendor partnership press releases with banks for commercial lending
- Bank earnings call transcripts (search for "commercial lending platform," "commercial real estate," "C&I lending," "treasury management," "working capital")

**Geographic scope:** USA (primary — largest commercial lending market, SBA/PPP infrastructure gap), India (MSME lending), UK (SME lending, British Business Bank).

**How data will be used:** Part I, Section 3 (Structural Shift 5 — commercial lending remains operationally primitive). Part I, Section 4 (Engagement Landscape — commercial lending-led engagements). Part II, Sections 8–10 (Zeta's position in commercial lending via Tachyon Loans + Quark Lending).

**Citation requirement:** Commercial lending market data is sparser than consumer — use SEC filings and industry surveys as primary sources. Flag estimates with wider uncertainty bands. Vendor marketing claims must be distinguished from verified deployments.

---

## 3. Phase 2: Synthesis and Gap-Fill

### Cross-referencing

- **Market sizing consistency:** Compare TAM estimates across Stream 1 sources. Lending technology market is fragmented across sub-segments — origination, servicing, commercial, embedded. Reconcile where analyst firms define market boundaries differently. Produce a consolidated vendor-addressable TAM with explicit notes on definitional differences. Distinguish between "lending technology" (platforms) and "lending-as-a-service" (BaaS/embedded).
- **Regulatory-competitive alignment:** Map each regulation (Stream 2) to the vendors positioned to benefit (Stream 3) and the structural shift it accelerates (Stream 4). Identify regulations where vendor coverage is thin — particularly AI governance in credit decisioning (SR 11-7 + ECOA intersection) and embedded lending compliance (CFPB BNPL regulation).
- **Embedded credit market data reconciliation:** Cross-reference Stream 5 (BNPL/embedded credit) with Stream 1 (market sizing) to avoid double-counting. Embedded credit platforms are both competitors to banks and potential infrastructure customers — the analysis must distinguish.
- **AI regulatory framework coherence:** Cross-reference Stream 6 (AI in credit) with Stream 2 (regulatory landscape) to produce a unified view of the AI governance requirements in lending. SR 11-7, ECOA, EU AI Act, and RBI guidelines create an overlapping regulatory framework that the document must present coherently.
- **Commercial lending evidence quality:** Stream 7 data is expected to be sparser than consumer/mortgage. Assess whether evidence supports a dedicated structural shift section or whether commercial lending is better treated as an aspect of other shifts.
- **Bank signal aggregation:** Consolidate bank modernization signals from Streams 3, 4, 5, 6, and 7 into a single target universe. De-duplicate. Verify each bank's tier classification and geography. Confirm each signal source URL resolves.

### Evidence quality assessment

For each structural shift, rate evidence quality:

- **Strong:** 3+ independent data points with navigable URLs, confirmed by both analyst and primary sources
- **Moderate:** 2 data points or analyst-only without primary confirmation
- **Thin:** Single source or vendor-provided only
- **Hypothesis:** No external evidence found — flag as hypothesis and state explicitly in the document

Shifts with "thin" or "hypothesis" evidence quality must be either dropped from Part I or explicitly flagged. The analyst voice does not assert without evidence.

### URL and citation verification

- Verify every URL resolves to the cited content (not a homepage, not a 404, not a paywall with no preview)
- For paywalled sources, confirm full bibliographic detail (publication, author, date, title, issue)
- Flag unverifiable claims in `unverified-claims.md`

### Targeted gap-fill research

Based on synthesis, conduct targeted follow-up for:

- Any structural shift with fewer than 3 data points
- Commercial lending technology market sizing if Stream 7 evidence is thin
- Bank-specific modernization signals in India and UK if Streams 3/4 produce mostly US-centric signals
- AI in servicing/collections if Stream 6 evidence skews heavily toward origination/decisioning
- Mortgage technology market — if evidence shows significant overlap with the lending opportunity, may warrant additional research; if it is a separate ecosystem dominated by ICE/Black Knight, the analysis should acknowledge it but not make it central

### Right to Play / Right to Win mapping

Map findings to the distillation framework:

**Right to Play questions to answer:**

- Is the vendor-addressable TAM large enough to justify entry across consumer, commercial, and embedded lending?
- Are banks actively replacing lending infrastructure (not just patching)? Or is the modernization cycle still early?
- Which lending sub-segments have the strongest replacement signals — origination, servicing, commercial, embedded?
- Can Zeta enter given Tachyon Loans, Quark Lending, and Evolution Fabric assets? What lifecycle stages are production-ready vs. conceptual?
- What is the regulatory runway — are AI/ML governance and fair lending deadlines creating urgency for infrastructure replacement?

**Right to Win questions to answer:**

- Does Zeta's combination of lending infrastructure (Tachyon Loans) + operational model (Quark Lending on Evolution Fabric) + decision auditability (Cognitive Audit Fabric) represent a genuine architectural advantage over competitors?
- Can Zeta compete with nCino in commercial lending, Blend in consumer origination, or ICE in mortgage? Or should the strategy be segment-avoidance?
- Is the Evolution Fabric / Seer combination — AI agents participating in lending operations with governed identity and auditable decisions — a positioning no competitor occupies?
- Where is Zeta's position genuinely weak? (Mortgage: likely no position. Commercial lending: Quark Lending is a placeholder. AI decisioning: no production track record. Servicing depth: unclear.)
- Does Tachyon Loans have production-grade capabilities in origination, servicing, and commercial lending? Or is the product line still early?

### Assembling the target universe

From bank signals collected across Streams 3, 4, 5, 6, and 7:

- Organize by geography (USA, India, UK)
- Classify by tier (Tier 1 / $100B+ assets, Tier 2 / $10B–$100B, Tier 3 / $1B–$10B)
- Classify by horizon (Near-term 0–2 years: active modernization signals; Medium-term 2–5 years: structural pressure building)
- For each bank, record: name, tier, geography, signal type (origination, servicing, commercial, embedded, AI decisioning), source, URL
- Minimum 15 named institutions across tiers and geographies

### Grounding the Zeta advisory

Cross-reference competitive landscape (Stream 3) with Zeta's product-line files:

- **Tachyon Loans** — primary lending product line. Map against consumer origination (Blend, nCino), commercial lending (nCino, Finastra), servicing (ICE/Black Knight, Fiserv). Assess production readiness honestly — product-line file says "To be expanded."
- **Tachyon Kernel** — core ledger and limit management. Map against core banking platforms that include lending modules (FIS, Temenos, Thought Machine).
- **Quark Lending** — domain hub for lending operations. Map against nCino's "Bank Operating System" positioning. Assess whether Quark Lending exists beyond placeholder status.
- **Quark Origination** — prospecting, sourcing, applications. Map against origination specialists (Blend, MeridianLink).
- **Evolution Fabric / Seer** — AI agent governance for lending. Map against the AI governance gap identified in Stream 6. This is potentially the strongest differentiator — no lending technology vendor offers governed AI operations as an integral platform capability.
- **Cognitive Audit Fabric** — decision auditability for credit decisions. Map against SR 11-7, ECOA adverse action, EU AI Act requirements. The ability to reconstruct and explain credit decisions is a regulatory imperative that most lending platforms do not address natively.
- **Trust Fabric** — borrower identity, authentication, consent. Map against KYC/identity verification in lending onboarding.
- **Photon** — disbursement and repayment flows. Integration point between lending and payments — not a differentiator in lending itself, but a structural advantage for end-to-end lending lifecycle.

Identify gaps honestly:

- Does Tachyon Loans have production-grade loan origination? Or is the product early-stage?
- Does Quark Lending have pre-modeled Streams and Loops for lending? The product-line file says "To be expanded" — this may be conceptual.
- Does Zeta have mortgage capabilities? The current engagement area file mentions mortgage/secured lending, but the competitive landscape (ICE/Encompass dominance) suggests this may be a "do not pursue" category.
- Does Zeta have commercial lending depth? Covenant monitoring, financial spreading, relationship-level exposure — these are complex capabilities that nCino has invested a decade in building.
- What is Zeta's AI in credit decisioning capability? Evolution Fabric/Seer provides governance, but does Zeta have credit scoring models, alternative data integration, or underwriting engines?

---

## 4. Phase 3: Document Writing

Section-by-section writing order. Target word counts are guidelines, not hard limits.

### PART I — THE OPPORTUNITY (Analyst voice, no Zeta references)

**Section 1: Market (~600 words)**

- Vendor-addressable TAM across lending technology sub-segments, aggregated and broken out
- Revenue by geography (USA, India, UK)
- Revenue by bank tier
- Growth rates by sub-segment
- Build vs. buy patterns — Tier 1 banks build or buy best-of-breed; Tier 2–3 banks buy platforms
- Fastest-growing segments (embedded lending, AI decisioning, commercial lending platforms)
- Framing: the lending technology market is entering a replacement cycle driven by regulatory mandates, AI requirements, and competitive pressure from fintechs

**Section 2: How We Got Here (~400 words)**

- Three eras of lending technology:
  - Era 1 (pre-2010): Monolithic origination — large-vendor LOS platforms (FIS, Fiserv), batch processing, paper-heavy workflows, branch-centric origination. Systems deployed in this era are still in production at most banks.
  - Era 2 (2010–2019): Digital channel overlay — online applications and mobile interfaces layered on top of legacy origination engines. Fintech lending emergence (LendingClub, SoFi, Kabbage). Banks added digital front-ends without replacing back-end processing.
  - Era 3 (2020–present): Platform pressure — COVID-era forbearance exposed servicing fragility. BNPL and embedded credit shifted origination to non-banking channels. AI/ML entered credit decisioning under intense regulatory scrutiny. Banks that deferred infrastructure replacement now face a multi-front modernization mandate.
- What was deferred: through all three eras, most banks avoided replacing core lending infrastructure. The technology debt overhang now forces concurrent modernization of origination, servicing, decisioning, and commercial lending.

**Section 3: Structural Shifts (7–8 shifts, ~2,500 words — the core)**

Each shift follows the evidence → segment opportunity → geographic dynamics pattern:

1. Legacy origination cannot meet speed expectations
2. AI/ML credit decisioning is shifting from experimental to regulated operational requirement
3. Post-pandemic servicing infrastructure proved inadequate
4. Embedded credit is reshaping the point of origination
5. Commercial lending remains operationally primitive
6. Open banking and alternative data are reshaping credit assessment
7. Fair lending scrutiny is intensifying — and AI amplifies the risk
8. (If evidence supports) Collections is becoming an AI-first domain

**Section 4: The Engagement Landscape (~500 words)**

Concrete engagement types banks are commissioning:

- Consumer origination modernization (replacing legacy LOS with real-time, digital-first origination)
- Lending servicing platform replacement (flexible servicing for modification, forbearance, and dynamic restructuring)
- Commercial lending platform build (working capital, revolving credit, covenant monitoring — replacing spreadsheets)
- Embedded lending infrastructure (API-first lending for BNPL, POS credit, partner channel distribution)
- AI-integrated credit decisioning (ML models + governance + explainability as a unified platform)
- Full lending lifecycle modernization (origination through collections on a single platform)

Map each engagement type to bank tier and structural shift.

**Section 5: Competitive Landscape (~600 words)**

- By category: legacy incumbents, cloud-native origination, mortgage specialists, commercial lending specialists, AI-native decisioning, embedded lending/LaaS, BNPL providers, servicing/collections
- Platform convergence: which vendors are expanding toward end-to-end lending vs. deepening point-solution excellence
- Gaps and vulnerabilities: where no vendor covers the full lending lifecycle from origination through collections with integrated AI governance; where commercial lending for Tier 2–3 banks is underserved; where AI decisioning and explainability are treated as separate from the lending platform
- The nCino gap: nCino dominates cloud lending for mid-market banks but is origination-heavy, Salesforce-dependent, and lacks servicing depth. What does this leave open?

**Section 6: Target Universe (~500 words)**

Named institutions organized by:

- Geography (USA, India, UK)
- Bank tier (Tier 1 / Tier 2 / Tier 3)
- Horizon (Near-term / Medium-term)
- For each: the observable evidence with navigable URL
- Framed as analytical observation, not sales targeting

---

### PART II — THE ADVISORY (Advisor voice, Zeta-specific)

**Section 7: Zeta's Position (~500 words)**

- Tachyon Loans capability domains mapped to the opportunity: what's production-ready, what's partial, what's architectural vision
- Quark Lending mapped to operational domain model for lending — pre-modeled Streams and Loops
- Evolution Fabric / Seer mapped to AI governance in lending operations — the structural differentiator
- Cognitive Audit Fabric mapped to credit decision auditability — SR 11-7, ECOA adverse action, EU AI Act
- Trust Fabric mapped to borrower identity, KYC, consent
- Photon mapped to disbursement/repayment flows
- Honest gap assessment: mortgage (likely no meaningful position — ICE/Encompass dominance), commercial lending depth (covenant monitoring, financial spreading — unverified capability), AI credit models (governance yes, models unclear), servicing depth (mass modification, forbearance — capability status unknown), US market presence (no installed base, no brand in lending)

**Section 8: Where to Play (~500 words)**

- Which sub-segments to pursue (consumer origination for Tier 2–3, AI-governed lending for AI-forward banks, commercial lending for mid-market)
- Which sub-segments to defer (mortgage — dominated by ICE, insufficient differentiation; standalone BNPL — fintech-dominated with margin compression)
- Which geographies to prioritize (India for proof and references, USA for revenue, UK for regulatory alignment)
- Which bank tiers to target (Tier 2 most likely; Tier 3 through partners; Tier 1 only for specific components like AI governance)
- Explicit "do not pursue" calls where evidence is thin or competitive position is weak

**Section 9: Risks and Gaps (~400 words)**

- What must be true: Tachyon Loans must be production-grade for consumer origination; Quark Lending must move beyond placeholder; AI governance (Evolution Fabric + Cognitive Audit Fabric) must be demonstrable
- Window risks: nCino could expand into servicing and collections (completing their lifecycle); legacy vendors could modernize faster than expected; embedded lending platforms (Mambu, Thought Machine) could capture the Tier 2–3 segment
- Capability gaps: mortgage (build vs. partner), commercial lending depth, AI credit models (build vs. partner), servicing flexibility (mass modification capability)
- Go-to-market risk: lending is a different buying center from payments and cards — Zeta's existing relationships may not transfer to the lending technology buyer

**Section 10: Recommended Actions (~400 words)**

- Near-term (0–2 years): specific actions, specific capability investments, specific bank targets
- Medium-term (2–5 years): platform positioning, geographic expansion, ecosystem plays
- Priority order: what to do first, second, third
- Which banks to approach first, and why (based on Target Universe evidence)

**Section 11: Executive Summary (~400 words)**

- Written last
- Covers both Part I and Part II
- A board member who reads only this section should understand: the lending technology market opportunity, the structural shifts creating it, Zeta's position, the honest gaps, and the recommended action

---

## 5. Phase 4: Review

### Part I Checks

- Every data point has a source citation with a navigable, verified URL — or full bibliographic detail for paywalled sources
- No broken links — every URL confirmed to resolve to cited content
- No "according to [authority]" citations without a traceable reference
- All unverifiable claims flagged as `[unverified — needs manual confirmation]`
- No structural shift relies on assertion without evidence
- Segment analysis (Tier 1/2/3) grounded in research, not generic
- Geographic analysis specific to USA, India, UK — not generic "global" claims
- No Zeta references, product names, or commercial voice anywhere in Part I
- Every bank named in the Target Universe has a citable evidence basis with navigable source link
- Document reads as external strategic analysis, not internal marketing
- The AI governance in lending thesis is supported by regulatory evidence, not technology aspiration

### Part II Checks

- Every recommendation traces back to evidence presented in Part I
- Gaps and weaknesses stated honestly, not minimized
- Recommendations specific and prioritized, not a generic list
- "Do not pursue" and "delay" recommendations included where warranted (mortgage, standalone BNPL)
- Product and asset references accurate against repo's product-line files (Tachyon Loans, Quark Lending, Evolution Fabric, Cognitive Audit Fabric, Trust Fabric, Photon)
- Go-to-market challenges acknowledged (lending is a different buying center)
- Capability readiness assessed honestly — product lines marked "To be expanded" in the repo are not presented as production-ready

### Editorial Rigor (Part I only) — Eight Tests

1. **Does every sentence earn its place?** No dead weight. Every sentence advances the argument.
2. **Tonal consistency.** Board-grade prose throughout. No drops to filing-cabinet language.
3. **Commercial voice.** Zero first-person plural. Zero market opportunity language. Zero buyer-readiness framing. Zero competitive positioning.
4. **Meta-narration.** No "this section will explore..." The structure speaks for itself.
5. **Vocabulary discipline.** Consistent terms throughout. "Lending platform" not alternating with "LOS system" and "credit infrastructure" without discipline.
6. **Shelf life.** No time-fragile language. Structural arguments survive without timestamps. "After successive rounds of fintech lending competition" not "since 2020."
7. **Specificity vs. thesis level.** No performance claims without evidence. No implementation details.
8. **Audience neutrality.** Consumable by bank CIOs, bank CEOs, Zeta's board. Not a sales document.

---

## 6. Key Differences from Other Engagement Areas


| Dimension                      | Payments                                                                                                 | Digital Identity & Trust                                                                                    | Lending and Credit                                                                                                                                                                                                                                                                                               |
| ------------------------------ | -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Market structure**           | Single well-defined category. Analyst firms size it consistently.                                        | Fragmented across 5+ adjacent categories. TAM must be constructed by aggregation.                           | Fragmented across lifecycle stages (origination, servicing, commercial, embedded) with distinct vendor ecosystems per stage. Mortgage is its own market.                                                                                                                                                         |
| **Competitive landscape**      | Dominated by incumbents (FIS, Fiserv) with clear challengers (Marqeta, Stripe). Relatively consolidated. | Highly fragmented, point-solution-dominated, M&A consolidating.                                             | Fragmented by sub-segment. nCino dominates cloud origination. ICE dominates mortgage. Legacy vendors dominate servicing. AI-native decisioning is a new category. No vendor covers the full lifecycle with integrated AI governance.                                                                             |
| **Primary driver**             | Real-time payments mandates + technology debt forcing infrastructure replacement.                        | Regulatory convergence making per-regulation compliance unsustainable + AI agent identity as new category.  | Fintech speed pressure on origination + AI/ML regulatory governance requirements (SR 11-7, ECOA, EU AI Act) + post-pandemic servicing fragility + embedded credit reshaping origination. Multiple concurrent forcing functions.                                                                                  |
| **Regulatory intensity**       | Moderate — real-time payment mandates, tokenization requirements.                                        | High — privacy, authentication, AI governance converging.                                                   | **Very high** — fair lending (ECOA, CRA, HMDA), AI model governance (SR 11-7), consumer protection (TILA, RESPA), BNPL regulation (CFPB), anti-discrimination enforcement. Lending is the most regulated domain in banking technology.                                                                           |
| **Geographic concentration**   | USA 30–40% of global payments tech spend. India (UPI). UK/EU. Brazil.                                    | USA primary (IAM spend). EU strongest regulatory driver. India (Aadhaar/DPDP).                              | USA dominant (largest consumer and commercial lending market, heaviest regulation). India (digital lending explosion, Account Aggregator). UK (open banking credit, FCA Consumer Duty).                                                                                                                          |
| **Central strategic argument** | Banks must replace aging payment infrastructure because they can no longer layer.                        | Banks must converge fragmented identity point solutions because per-regulation management is unsustainable. | Banks must modernize lending infrastructure because AI-powered credit decisioning, embedded distribution, and regulatory scrutiny demand platform capabilities that legacy origination and servicing systems cannot provide — and the AI governance requirement is inseparable from the lending platform itself. |
| **AI governance relevance**    | Moderate — AI in fraud/reconciliation.                                                                   | High — AI agent identity is a new category.                                                                 | **Critical** — credit decisioning is explicitly classified as high-risk AI by the EU AI Act. SR 11-7 model risk management is mandatory. ECOA requires adverse action explanations. AI governance is not an add-on — it is a prerequisite for AI adoption in lending.                                            |
| **Zeta's position**            | Strong — Photon product lines directly address card issuance, tokenization, processing.                  | Architectural — Trust Fabric defines converged vision but production depth uncertain.                       | **Uncertain** — Tachyon Loans and Quark Lending exist as product-line definitions but production depth is unclear. The differentiation thesis (lending + Evolution Fabric + Cognitive Audit Fabric = governed AI lending) is architecturally strong but commercially untested.                                   |
| **Analyst coverage**           | Strong. Multiple market sizing reports, Magic Quadrants, Forrester Waves.                                | Moderate to strong for components; thin for converged category.                                             | Strong for origination and mortgage. Moderate for commercial lending technology. Growing for AI in credit. Thin for "governed lending platform" as a unified category.                                                                                                                                           |


---

## 7. Execution Approach

### Sub-agent batching strategy

Seven research streams, max 4 concurrent sub-agents:

**Batch 1 (4 concurrent):**

- Stream 1: Market sizing and revenue pools
- Stream 2: Regulatory landscape and lending mandates
- Stream 3: Competitive landscape
- Stream 4: Structural shifts and bank modernization activity

**Batch 2 (3 concurrent):**

- Stream 5: Embedded credit and BNPL disruption
- Stream 6: AI in credit decisioning and loan servicing
- Stream 7: Commercial lending technology gap

### Estimated turns


| Phase                               | Estimated Turns   |
| ----------------------------------- | ----------------- |
| Phase 1, Batch 1 (Streams 1–4)      | 1 turn (parallel) |
| Phase 1, Batch 2 (Streams 5–7)      | 1 turn (parallel) |
| Phase 2: Synthesis and gap-fill     | 2 turns           |
| Phase 3: Document writing (Part I)  | 2–3 turns         |
| Phase 3: Document writing (Part II) | 1–2 turns         |
| Phase 4: Review and editorial rigor | 1–2 turns         |
| **Total**                           | **8–11 turns**    |


### Output file path

`org-8.0/what-we-sell/strategy/engagement-areas/lending-and-credit.md`

---

## 8. Output Files

### Primary document

`org-8.0/what-we-sell/strategy/engagement-areas/lending-and-credit.md` — replaces the current CIO-facing capability catalogue with the two-part opportunity analysis and advisory.

### Research retention

**Location:** `org-8.0/what-we-sell/strategy/_research/lending-and-credit/`

**Files to create:**


| File                           | Contents                                                                                                                                                                                                     |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `s1-market-sizing.md`          | Lending technology TAM by sub-segment (origination, servicing, commercial, embedded, AI decisioning). Claim/Value/Source/URL/Verified table.                                                                 |
| `s2-regulatory-landscape.md`   | USA (ECOA, CRA, TILA, SR 11-7, CFPB BNPL), India (RBI Digital Lending, Account Aggregator), UK (FCA Consumer Duty, PRA model risk) regulations with compliance requirements and infrastructure implications. |
| `s3-competitive-landscape.md`  | By-category competitor profiles. Revenue, positioning, strengths, weaknesses, vulnerabilities. Bank modernization signals.                                                                                   |
| `s4-structural-shifts.md`      | Evidence for each structural shift. Data points, regulatory citations, bank-tier analysis. Bank modernization signals.                                                                                       |
| `s5-embedded-credit-bnpl.md`   | BNPL market data, regulatory actions, bank embedded lending launches, lending-as-a-service platforms.                                                                                                        |
| `s6-ai-credit-decisioning.md`  | AI/ML adoption in credit, regulatory framework (SR 11-7, ECOA, EU AI Act), vendor landscape (Upstart, Zest AI), AI in servicing and collections.                                                             |
| `s7-commercial-lending-gap.md` | Commercial lending technology adoption, vendor landscape, mid-market bank signals, MSME lending (India).                                                                                                     |
| `synthesis-notes.md`           | Cross-references, contradictions, evidence quality ratings, Right to Play / Right to Win mapping, editorial decisions, target universe assembly notes.                                                       |
| `unverified-claims.md`         | Every claim flagged as `[unverified — needs manual confirmation]` with context.                                                                                                                              |


**Format for stream files:**

- Research date and engagement area
- Data table: Claim | Value | Source | URL | Verified (Yes/No)
- Key findings as structured bullets
- Gaps and unresolved questions
- Raw notes and excerpts

**Cross-references to existing research:**

- `org-8.0/what-we-sell/strategy/_research/payments/s2-regulatory-landscape.md` — Dodd-Frank 1033 (open banking) and India RBI regulatory content overlaps with lending data access and alternative credit data. Reference rather than re-research.
- `org-8.0/what-we-sell/strategy/_research/digital-identity-and-trust/s2-regulatory-landscape.md` — ECOA and fair lending overlap with identity verification and KYC in lending. Reference for cross-domain regulatory coherence.
- `org-8.0/what-we-sell/strategy/_research/digital-identity-and-trust/s5-ai-agent-identity.md` — EU AI Act and AI governance framework overlaps with AI in credit decisioning. Reference for regulatory consistency.
- `market-study/` — Multiple market study files reference lending tangentially in core modernization context. Cross-reference `market-study/bank-decision-makers/cio/core-modernization/` for lending-adjacent CIO investment data.
- Note all cross-references in `synthesis-notes.md`.

---

## 9. What This Plan Does NOT Do

- Does not write the opportunity analysis itself.
- Does not produce generic research streams applicable to any engagement area. Every stream, competitor, regulation, and structural shift is specific to lending and credit.
- Does not include more than 3 geographic markets (USA, India, UK). UK is included because FCA Consumer Duty, PRA model risk management guidance (SS1/23), and open banking credit data sharing create a regulatory environment with specific infrastructure investment implications for lending — and UK banks are active modernizers.
- Does not plan for a document shorter than 5,500 words or longer than 8,000 words.
- Does not blend the analyst and advisor voices. Part I and Part II are structurally separated.
- Does not include banks in the Target Universe without specifying evidence sources.
- Does not cite sources without navigable URLs or full bibliographic detail.
- Does not discard research output. Every stream's raw findings are saved to `_research/lending-and-credit/`.
- Does not treat Zeta product lines marked "To be expanded" in the repo as production-ready. The advisory must be honest about maturity status.

