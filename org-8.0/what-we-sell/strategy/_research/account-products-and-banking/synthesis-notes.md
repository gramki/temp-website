# Synthesis Notes — Account Products and Core Banking

**Date:** March 2026
**Streams synthesized:** S1 (Market Sizing), S2 (Regulatory Landscape), S3 (Competitive Landscape), S4 (Structural Shifts), S5 (Business Banking / Cash Management), S6 (Deposit Innovation / Open Banking)

---

## 1. Market Sizing Reconciliation

### Core Banking Platforms: $12–18B

Three analyst houses size this market differently:

| Source | 2024–2025 Estimate | 2030–2031 Forecast | CAGR | Definition |
|---|---|---|---|---|
| Grand View Research | $12.37B (2024) | $21.61B (2030) | 10.2% | Core banking *software* — narrower scope |
| Mordor Intelligence | $17.19B (2025) | $29.01B (2031) | 9.12% | Core banking *market* — includes services |
| 360iResearch | $18.10B (2024) | $40.94B (2030) | 14.50% | Core banking software — broadest definition |

The range is wide ($12.37B to $18.10B) because of definitional scope differences: GVR uses a tighter "software-only" boundary; Mordor includes services; 360iResearch appears to include adjacent modules (digital banking, origination) that GVR excludes. **Working estimate: $15–17B (mid-range) with definitional caveats.** The CAGR consensus is 9–14%.

### Digital Banking Platforms: $37–46B

| Source | 2025 Estimate | CAGR |
|---|---|---|
| Grand View Research | $37.49B | 19.8% (2026–2033) |
| Kings Research | $46.03B | 20.90% (2025–2032) |

This is broader than account products alone — includes mobile banking, web banking, self-service portals, and digital engagement layers. Not all of this is vendor-addressable for a core banking play; it includes Alkami, Q2, Backbase revenue that wraps legacy cores rather than replacing them.

### Cash Management / Treasury: $10–20B total, ~$2.8–5.4B BFSI vendor TAM

The total cash management systems market is $20.35B (Mordor Intelligence, 2025), but only 27% of this is BFSI-specific (Mordor). Treasury management systems are $5.85–6.53B (Business Research Insights). The bank-addressable vendor TAM for cash management and treasury technology platforms is approximately $2.8–5.4B, depending on how much of the broader cash management market is counted. S5 notes that the $20B figure includes non-banking deployments (retail, telecom) and suggests the bank-specific portion is likely $12–15B.

### Business Banking Technology: $8–12B estimated vendor-addressable

No analyst cleanly isolates the business banking technology platform market. S5 infers from McKinsey's $1.18T MSME revenue pool (2024, growing 7% annually). Applying a 1–2% technology-to-revenue ratio (common in banking) yields $12–24B. Cross-referenced with Celent corporate banking IT spending data (+5.6% in 2025, +6.1% in 2026) and vendor revenue estimates (iGTB, Finastra TCM, Kyriba, Bottomline combined ~$2–3B disclosed), a reasonable vendor-addressable estimate is $8–12B, but this is inferred, not analyst-verified.

### Account Origination / Onboarding: $2.7–6.1B

Wide range reflects definitional scope. Business Research Company ($2.69B, 2025) counts a narrower digital onboarding segment; Growth Market Reports ($6.1B, 2024) uses a broader digital onboarding platform definition. CAGR 15–17%.

### Composite Vendor-Addressable TAM

| Sub-Segment | 2025 Estimate | CAGR | Notes |
|---|---|---|---|
| Core banking platforms | $12–18B | 9–14% | Tier 1 largely in-house; vendor TAM skews Tier 2–3 |
| Digital banking platforms | $37–46B | 17–21% | Broader than core; includes channel layers |
| Cash management / treasury | $2.8–5.4B (BFSI) | 7–10% | 27% of total $20B market is BFSI |
| Business banking technology | $8–12B (inferred) | 6–7% | McKinsey revenue pool inference |
| Account origination | $2.7–6.1B | 15–17% | Cross-industry; banking portion smaller |
| Deposit operations | $5.8B | 13% | Narrower segment |

**Composite vendor-addressable TAM for account products and core banking: $25–40B.** Narrow definition (core + digital banking) yields ~$25B. Broad definition (including cash management, origination, business banking) reaches ~$40B.

**Critical caveat:** Tier 1 banks account for significant in-house spend. JPMorgan, Goldman Sachs, and other G-SIBs are building/hollowing cores internally. The vendor-addressable TAM for Tier 2–3 banks is approximately **$15–20B** (Levera Partners estimate for community/regional bank technology TAM aligns with S1's community banking data showing Fiserv 25.9% share with 1,155 CU clients, Jack Henry 12.0% with 535 clients).

---

## 2. Evidence Quality Assessment

| Shift | S4 Rating | Synthesis Assessment | Cross-Stream Validation |
|---|---|---|---|
| **1. Progressive core replacement** | Strong | **Confirmed** — S3 validates with named bank examples (BancoEstado 14M customers migrated to Mambu over 5 years, Lloyds extended Thought Machine license, Access Bank completed Oracle FLEXCUBE modernization). S4's critical assessment is honest: the strategy is dominant but few completions confirmed. CB RADAR tracks 113 projects with 72.5% reported complete/live, but S4 notes "executive optimism often masks overruns and compromises." | S3 confirms named deals; S5 notes overlay vs. replacement question |
| **2. Composable banking** | Strong | **Confirmed with caveat** — production-proven at 15+ named banks (Lloyds, Standard Chartered, Intesa Sanpaolo, JPMorgan, Westpac on Thought Machine/10x; BancoEstado, Leeds, Marginalen on Mambu). But only alongside/within monolithic cores — no Tier 1 has fully replaced its core with a composable platform. S3 confirms cloud-native challengers are "real but small" (Thought Machine £47.6M revenue, Mambu ~$160M, 10x undisclosed). | S3 confirms revenue/scale data; S4 critical assessment is key |
| **3. Cloud-native core** | Strong | **Confirmed** — 84.5% cloud adoption rate across 113 tracked transformations (S4/CB RADAR). Regulatory clearances documented across US, UK, India (S2: OCC permits cloud with accountability, PRA recognizes 40–90% cloud migration potential, RBI launching own cloud pilot). Vendor cloud launches documented (S3: Temenos SaaS, TCS BaNCS Cloud, FIS Finxact). SaaS core banking growing from $12.12B to $50.62B by 2033 at 19.6% CAGR. | S1 (cloud CAGR 16.7%), S2 (regulatory frameworks), S3 (vendor launches), S4 (adoption data) all align |
| **4. Business banking digitization** | Strong | **Confirmed** — $1.18T MSME revenue pool growing 7% annually (S5/McKinsey). Mercury $650M annualized revenue, Tide 1.8M members with 14% UK SMB share (S5). Virtual accounts: 86% of banks invested or planning to invest (S5/Datos Insights). UK digital-first banks captured ~one-third of SMEs in 5 years (S5/McKinsey). This is a separate modernization wave from retail core replacement. | S5 is primary; S4 provides macro evidence on business banking as distinct wave |
| **5. Open banking mandates** | Strong | **Confirmed with nuance** — Section 1033 enjoined but market-moving; banks building APIs regardless (S2). UK OBIE: 15.1M users, 22B annual API calls, 36% YoY growth (S6). India AA: 390.9M cumulative consents, 2.1B linked accounts (S6). **However, S2 finds most open banking regulations do NOT force core replacement — they are wrappable via API gateway/middleware.** This weakens open banking as a core replacement driver; its value is in exposing legacy limitations, not mandating replacement. | S2 weakens forcing function argument; S6 confirms adoption scale |
| **6. Deposit competition** | Strong | **Confirmed** — 40% of new US account openings to neobanks, surpassing large banks at 38% (S4/Simon-Kucher). SoFi $37.5B deposits growing $4.6B in a single quarter (S6). Chime 9.5M active members, 12.8% of new checking accounts — more than Chase or Wells Fargo individually (S6). UK neobanks: Revolut £30.2B, Monzo £16.6B, Starling £12.1B (S6). S6 finds overlay tools (Zafin/SunTec) can address product agility for deposit pricing without core replacement — Tier 1 US bank achieved >50% increase in CD approved volumes in 8 weeks via Zafin overlay. | S6 primary; S4 confirms market share data |
| **7. Embedded banking (BaaS)** | Strong | **Confirmed with restructuring** — Synapse collapse documented with $265M deposits frozen, 100K+ affected (S2, S4). FDIC proposed Synapse Rule for daily reconciliation. Fed cease-and-desist against Evolve Bank (S4). S2 identifies BaaS/third-party guidance as a strong core-level forcing function — banks pursuing embedded banking must maintain real-time visibility into every deposit relationship. Market growing ($21.4B → $105.8B by 2035) but on different architectural foundations post-Synapse. | S2 validates core-level requirement; S4 confirms regulatory enforcement |
| **8. AI in account operations** | Moderate-to-Strong | **Confirmed as emerging** — CIBC CRTeX AI-enabled personalization engine (Oct 2025) and Wells Fargo deploying AI agents company-wide via Google Agentspace are the strongest Tier 1 signals (S4). Vendor-driven category: Cotribute Agentic AI Growth Agents, Kasisto KAIgentic, FlowX.AI Dormant-to-Active Monitor. Federal Reserve research on synthetic identity fraud ($3.3B H1 2025 exposure) provides institutional backing. Analyst coverage is thin — McKinsey/Gartner/Celent have limited published research on AI in account lifecycle specifically. | S4 primary; limited cross-stream validation |

---

## 3. Regulatory Forcing Assessment

From S2: **only 5 of 19 regulations reviewed force core replacement.** The rest can be satisfied by wrapping the legacy core.

### Strong Forcing Functions (require core-level changes)

1. **FDIC Part 370** (USA) — 24-hour deposit insurance calculation by ownership category requires deep integration into core ledger. Post-SVB/Synapse, heightened supervisory priority. Legacy cores organized by account number rather than beneficial owner face structural remediation.

2. **EU Instant Payments Regulation** (EU) — 10-second settlement, 24/7/365 availability, equal pricing. Batch-oriented cores cannot comply. The most direct core banking mandate in Europe.

3. **Basel III/IV (CRR3/CRD6)** (EU) — Output floor parallel calculations, new exposure classes, granular regulatory reporting. Requires changes deep within ledger, risk engine, and reporting infrastructure.

4. **RBI Current Account/CC/OD Direction** (India) — Exposure-based account opening rules require tight integration between lending and deposit systems. Siloed legacy modules for deposits and loans create structural compliance gaps.

5. **Interagency Third-Party Guidance + BaaS model** (USA) — Post-Synapse, banks pursuing embedded banking must maintain real-time customer-level deposit visibility through fintech intermediaries. Legacy cores not designed for multi-tenant partner-mediated deposit management are structurally inadequate.

### Wrappable Regulations (middleware/API layer sufficient)

Section 1033, FinCEN CDD/KYC, BSA/AML monitoring, Regulation E, PSD2/PSD3 open banking, UK Open Banking + CASS, FCA Consumer Duty, RBI Account Aggregator, RBI Digital Lending Guidelines, DPDP Act, CRA — all satisfiable by wrapping the core with middleware, API gateways, or analytics layers.

### Partial/Conditional Forcing Functions

DORA, RBI KYC (account restriction enforcement), RBI BSBDA (product configuration complexity) — do not mandate replacement but test core flexibility and may trigger replacement if the vendor cannot satisfy requirements.

### Comparison to Payments

This is critical for opportunity sizing. **Regulatory forcing pressure in account products is weaker than in payments.** Payments has hard deadlines (FedNow launch, ISO 20022 SWIFT deadline Nov 2025, tokenization mandates) that created genuine urgency. In core banking, only the EU IPR has a comparable hard deadline. The other 4 forcing functions are structural pressures, not time-bounded mandates. This tempers the urgency narrative — banks feel regulatory pressure, but most can defer core replacement by wrapping.

---

## 4. Cross-Stream Contradictions

### Replace vs. Augment

- **S3 finds** "the market is bifurcating" — Tier 1 banks with resources pursue transformation, the vast majority of Tier 2–4 banks augment. The legacy Big 3 (FIS $7.3B, Fiserv $21.2B total, Jack Henry ~$2.4B) control US relationships; switching costs are enormous.
- **S4 finds** progressive migration is the dominant *strategy* (supported by TSB's £614M failure, BancoEstado's Celent award, Oliver Wyman recommendation) — but few completions confirmed. "Progressive migration" may be euphemism for indefinite coexistence.
- **S6 finds** overlay tools (Zafin/SunTec) can address deposit pricing innovation without core replacement. A Tier 1 US bank achieved >50% increase in CD approved volumes in 8 weeks via Zafin — no core change needed.

**These are not contradictions — they describe different segments and timescales.** The synthesis: **the core replacement opportunity is real but concentrated in Tier 1 and select Tier 2 banks. For the majority of Tier 2–3 banks, augmentation (digital banking layers, product/pricing overlays, API wrappers) is the dominant behavior.** Full core replacement is a multi-year, high-risk decision that most banks defer as long as possible.

### Market Sizing Consistency

S1 core banking platforms ($12–18B) and S5 business banking technology ($8–12B estimated) have partial overlap. Cash management features are embedded in both core banking TAM estimates and business banking platform estimates. The composite $25–40B figure risks double-counting ~$2–3B in overlapping cash management/treasury capabilities bundled into core banking platforms.

### Intent vs. Action Gap

- **S1** Cornerstone finding: "planned replacements fall short of deployments"
- **S4** evidence: 1,429 IBS deals in 2025 (up from 1,368 in 2024), accelerating deal velocity; 113 CB RADAR projects with 84.5% cloud adoption
- **S3** 92% of UK FIs have commenced modernization (EY); 83% plan Gen 2 cores

Both narratives are true simultaneously. Deal flow is increasing, but most deals are augmentation/digital banking layer deployments, not full core replacement. EY's "92% commenced modernization" likely includes API layers, digital banking wrappers, and progressive migration pilots — not just core swaps. The intent-to-action gap remains wide for *full core replacement*, even as modernization *activity* accelerates.

### Overlay Delay Effect

S6 raises an underappreciated dynamic: overlay tools (Zafin, SunTec) may *delay* core replacement by removing the most acute pain (deposit pricing inflexibility) without forcing the deeper architectural decision. If a bank solves its immediate deposit competition problem with an 8-week Zafin deployment, the business case for a 3-year core replacement weakens. This benefits overlay vendors and harms core replacement vendors.

---

## 5. Right to Play / Right to Win Mapping

### Right to Play

| Criterion | Assessment | Evidence |
|---|---|---|
| **Market attractive** | Yes | $25–40B composite TAM; growing 9–14% for core banking, 17–21% for digital banking (S1) |
| **Problem real** | Yes | 53% bank dissatisfaction with core providers (ABA, S1); £3.3B UK legacy maintenance annually (S1); 64% of IT budgets on legacy maintenance (S6 vendor estimates); 40% of new accounts going to neobanks (S4) |
| **Entry feasible** | Yes | Tachyon is production-validated in the US — three credit card programs and multiple DDA programs (health benefits/Optum, loyalty/rewards) running on Tachyon with Photon for payment processing. Cloud-native entry path is proven by others (Thought Machine, Mambu, 10x each entered with <$100M revenue and now serve Tier 1 banks). Market is fragmented (top 3 vendors hold only 30.1% of transformation deal share per CB RADAR). |
| **Strategically aligned** | Yes | Account products are the ledger endpoints for Photon payments. Core banking + payments processing is the combination FIS is pursuing ($7.3B Banking + $13.5B TSYS). Product synergy is strong. |
| **Regulatory runway** | Moderate | 5 strong forcing functions, but most regulations wrappable. Weaker urgency than payments. |

### Right to Win

| Criterion | Assessment | Evidence |
|---|---|---|
| **Differentiated value** | Partially validated | Evolution Fabric + Tachyon combination (operational model + account platform). No competitor offers an integrated thesis for *how banks should operate differently*, not just *what technology to use*. Tachyon's US production (3 credit card programs, multiple DDA programs) validates the account platform layer. The operational model thesis (Evolution Fabric) remains unproven as a standalone value proposition with bank buyers. |
| **Competitive advantage** | Medium-Strong for purpose-specific programs | Tachyon has US production evidence: 3 credit card programs and multiple DDA programs (health benefits/Optum, loyalty/rewards). Thought Machine has Tier 1 core banking deployments (Lloyds, Standard Chartered, Intesa). Mambu has 200+ clients. Pismo has Visa's distribution. 10x has Chase UK. Tachyon's gap is scope breadth (purpose-specific vs. full-service core) and visibility (no analyst coverage, no public case studies). |
| **Execution ability** | Validated for purpose-specific programs | Tachyon is in US production for credit cards (3 programs) and DDA (health benefits, loyalty/rewards). Extension to full-service retail/business core banking is a scope expansion question, not a platform maturity question. |
| **Route to market** | Medium | Existing US bank relationships from Tachyon credit card and DDA deployments provide direct expansion paths. Photon/Electron relationships provide additional warm introductions. But full-service core banking is a DIFFERENT buying center (CTO/CIO, not payments head or program sponsor). Cross-selling from purpose-specific programs to core is possible but requires navigating organizational boundaries. |
| **Defensibility** | Conditional | IF Evolution Fabric thesis proves out, switching costs compound (banks that adopt the operational model become deeply integrated). But this is hypothetical. |

**Overall assessment: Strong Right to Play, Medium-Strong Right to Win for purpose-specific account programs, conditional for full-service core banking.**

Tachyon's US production evidence (credit cards, DDA programs) closes the product readiness question for account infrastructure. The remaining gap is between "we can deliver purpose-specific account programs" and "we can win full-service core banking replacement deals against Thought Machine, Mambu, and Temenos." The first is demonstrated by production evidence; the second requires scope expansion, public references, and analyst coverage.

---

## 6. Target Universe Assembly

Named banks with active modernization signals, consolidated from S3 and S4.

| Bank | Tier | Geography | Signal | Horizon | Source Stream |
|---|---|---|---|---|---|
| **Citi** | 1 | US / Global | Recruiting "Head of Core Banking Transformation" (Mar 2026); building future-state digital banking platform; initial focus LATAM, then global rollout | Near-term (0–2yr) | S3 |
| **Lloyds Banking Group** | 1 | UK | Acquired additional £10M stake in Thought Machine (Mar 2025); Vault Core in production; core transformation is "key part of three-year strategic plan"; license extended to 2029 | Near-term (0–2yr) | S4 |
| **JPMorgan Chase** | 1 | USA / UK | Selected Thought Machine for US retail core (2021); Chase UK on 10x Banking (2.5M+ customers, £15B+ deposits); 70% of data on cloud | Near-term (0–2yr) | S3, S4 |
| **HSBC** | 1 | UK / Global | $1.8B technology cost reallocation; decommissioned 1,165 legacy apps in 2025; plans to retire 1/3 of app portfolio by 2028 | Near-term (0–2yr) | S3 |
| **Standard Chartered** | 1 | HK / Asia | Mox Bank on Thought Machine since 2020; "Fit for Growth" $754M run-rate savings across 300+ initiatives; targeting $1.3B total savings through 2026 | Near-term (0–2yr) | S3, S4 |
| **SBI** | 1 | India | 2-year core banking modernization: Unix→Linux migration, microservices, private cloud, 300 APIs via sandbox; "modernising as we run the ship" | Near-term (0–2yr) | S3, S4 |
| **HDFC Bank** | 1 | India | Plans migration to new engineered platform for enhanced robustness and scalability; multi-cloud active-active architecture; 97% digital transactions | Near-term (0–2yr) | S3, S4 |
| **Wells Fargo** | 1 | USA | $900M+ incremental tech spend (2025); Vantage digital banking platform integrated 65 fragmented systems; AI agents via Google Agentspace | Near-term (0–2yr) | S3, S4 |
| **Deutsche Bank** | 1 | Germany / Global | 260 apps migrated to Google Cloud; 12M Postbank customers onto Google Spanner; Project Magellan (€1B); operating "like a platform company" | Near-term (0–2yr) | S3, S4 |
| **BancoEstado** | 1 | Chile | Celent 2025 Model Bank: migrated 14M customers to Mambu (Jul 2020–Jun 2025); targets 90% mainframe reduction by 2027 | Near-term (0–2yr) | S4 |
| **Intesa Sanpaolo** | 1 | Italy | isybank launched Jun 2023 on Thought Machine + Google Cloud; 300K migrated customers; targeting €800M annual savings from 2026 | Near-term (0–2yr) | S4 |
| **Westpac** | 1 | Australia | 10x Banking partnership for institutional platform + BaaS; technology simplification through 2028 | Near-term (0–2yr) | S4 |
| **CIBC** | 1 | Canada | Launched CIBC CRTeX AI-enabled personalization engine (Oct 2025); omni-channel engagement | Medium-term (2–5yr) | S4 |
| **Axis Bank** | 1 | India | Launched "open" by Axis Bank (digital entity); 15M+ MAU mobile; DevSecOps and cloud infrastructure | Medium-term (2–5yr) | S4 |
| **Access Bank** | 1 | Nigeria / 24 markets | Completed Oracle FLEXCUBE core modernization Sep 2025; 60M customers; 35M+ txns/day | Completed | S3 |
| **ING Bank Śląski** | 2 | Poland | Live on Thought Machine Vault Core since Dec 2021; first Polish bank on cloud-native core; expanding via NextGen Architecture program | Near-term (0–2yr) | S4 |
| **Shawbrook** | 2 | UK | Live on Thought Machine Vault Core (Aug 2025); deployed in <9 months; commercial SME lending focus | Completed | S4 |
| **Leeds Building Society** | 2 | UK | Mambu partnership for multi-year core modernization; pilot digital savings launched in <1 year; £30B AUM | Near-term (0–2yr) | S4 |
| **West Brom Building Society** | 2 | UK | 10x Banking + Deloitte for multi-phase cloud-native core transformation (May 2025); 400K+ members | Near-term (0–2yr) | S4 |
| **Judo Bank** | 2 | Australia | Full core migration to Thought Machine completed Apr 2025; 50% reduction in product dev time; 4x faster performance | Completed | S4 |
| **Burgan Bank** | 2 | Kuwait | Selected TCS BaNCS May 2024; consolidating legacy into universal banking; 160+ branches | Near-term (0–2yr) | S3 |
| **Co-operative Bank** | 2 | New Zealand | 10x Banking selected for full-platform migration (Aug 2025); 180K+ customers; multi-year phased approach | Near-term (0–2yr) | S4 |
| **NS&I** | Govt | UK | Replacing legacy core with SBS cloud-native SBP Digital Core; partnering with Atos, IBM, Sopra Steria (Jul 2025) | Near-term (0–2yr) | S3 |
| **MIDBANK** | 3 | Egypt | Completed full legacy replacement with Temenos (big-bang); core, payments hub, FCM, data hub | Completed | S3 |
| **Marginalen Bank** | 3 | Sweden | Completed migration to Mambu in 13 months on Azure Cloud (Jun 2025) | Completed | S4 |
| **Mascoma Bank** | 3 | USA | Signed Thought Machine for cloud-native core migration (Jan 2022); $2.6B mutual savings bank | Near-term (0–2yr) | S4 |
| **Chetwood Bank** | 3 | UK | Live on Mambu; launched savings products in 8 months; Hargreaves Lansdown integration (2025) | Completed | S4 |
| **BPER Bank Luxembourg** | 3 | Luxembourg | Selected OLYMPIC Banking System as new core platform | Near-term (0–2yr) | S4 |
| **Hanover Bank** | 4 | USA | Completed core banking system conversion Feb 2025 | Completed | S3 |

**Geographic distribution:** UK dominates (10 banks), followed by USA (5), India (4), Australia (2). LATAM, Middle East, Africa, and Continental Europe each have 1–3 signals.

**Tier distribution:** Tier 1 (15 banks) — these are the largest transformation programs but also the most likely to build in-house. Tier 2 (7 banks) — the sweet spot for vendor-delivered solutions. Tier 3–4 (5 banks) — faster deployments, smaller deal sizes.

---

## 7. Cross-References to Other Engagement Areas

### Payments

- **FIS/Fiserv data overlap:** FIS Banking Solutions ($7.3B) includes payments processing alongside core banking. Fiserv ($21.2B total) spans payments and core. Market sizing for core banking cannot cleanly separate the payments component within these vendors.
- **PSD2/PSD3:** Drives API infrastructure investment at the account level (AISP/PISP), but S2 confirms this is wrappable — does not force core replacement. The payments research covers PSD3/PSR structure, APP fraud, and timeline.
- **BaaS and payments:** The Synapse collapse is documented in both payments and account products research. The BaaS model requires modern core banking AND modern payments rails — the two are architecturally interdependent.
- **ISO 20022 / SWIFT:** S5 documents new camt.052/053/054 reporting messages from Q2 2026 that improve corporate treasury reconciliation. This intersects with payments infrastructure modernization.

### Digital Identity & Trust

- **KYC regulations:** FinCEN CDD/KYC (S2) directly intersects with identity verification. S2's analysis of the Feb 2026 exceptive relief (streamlined BO verification) supplements the identity research.
- **RBI KYC Master Direction:** Account restriction enforcement (credit-only → freeze) based on KYC status requires core-level product rules integration. Covered in both identity and account products research.
- **India Account Aggregator:** 2.1B linked accounts, 913 FIUs — covered in both identity and account products research streams.
- **DPDP Act 2023:** Consent management for account data intersects with the broader identity/privacy framework.

### Commercial Cards

- **Tachyon account infrastructure:** If Tachyon provides the account ledger, commercial card programs (corporate cards, virtual cards, expense management) depend on the same underlying account platform. The account/card boundary is architecturally porous.
- **Brex acquisition by Capital One ($5.15B, Jan 2026):** S5 documents this as validation that business banking fintechs consolidate with banks — the card/account convergence is a strategic theme.

---

## 8. Editorial Decisions

### For Part I (Opportunity Framing)

1. **The "composable banking replaces monolithic cores" framing must be tempered.** S4's critical assessment is clear: composable is production-proven but only alongside/within monolithic cores, not replacing them entirely. No Tier 1 bank has fully replaced its core with a composable platform. The honest framing: composable is the direction, replacement is the aspiration, augmentation is the reality for most banks.

2. **The regulatory forcing argument is weaker than payments — acknowledge this explicitly.** Only 5 of 19 regulations force core replacement (S2). Payments had FedNow, ISO 20022 SWIFT deadline, tokenization mandates — hard deadlines that created genuine urgency. Core banking has the EU IPR (10-second settlement) as the only comparable hard deadline. The rest are structural pressures, not time-bounded mandates.

3. **Business banking should be treated as a distinct opportunity, not a sub-topic of retail core.** S5 establishes that business banking has different competitive sets (iGTB, Finastra, Kyriba vs. Temenos, TCS), different buyers (commercial banking head / CFO / treasurer vs. retail technology), different revenue pools ($1.18T MSME, growing 7%), and an independent modernization cycle. The overlay market (iGTB, Finastra, CashFac) is the most immediately addressable opportunity.

4. **The intent-vs-action gap must be front and center.** 92% of FIs have "commenced" modernization (EY), 98% of community banks are "planning" modernization (S1/Jupid), but Cornerstone consistently finds planned replacements fall short of deployments. The gap between stated intent and executed transformation is the defining feature of this market.

### For Part II (Zeta's Position)

5. **Tachyon's production evidence must be properly positioned.** Tachyon powers three credit card programs and multiple DDA programs (health benefits/Optum, loyalty/rewards) in the US, with Photon handling payment processing. This is real production evidence — but it is purpose-specific programs, not full-service core banking replacement. Every competitor cited in S3 has named *core banking* references: Thought Machine has Lloyds, Standard Chartered, Intesa Sanpaolo. Mambu has BancoEstado (14M customers). 10x has Chase UK. The honest framing: Tachyon is production-proven for account infrastructure, but the extension to full-service retail/business banking core replacement is the remaining question.

6. **The Evolution Fabric narrative is differentiated but must be grounded.** No other vendor offers an integrated thesis for how banks should operate differently. But "differentiated positioning" and "winning deals" are different things. The narrative must connect to concrete bank outcomes, not just thesis articulation.

7. **The cross-sell from payments is real but not automatic.** Existing Photon/Electron relationships provide warm introductions, but core banking is a different buying center (CTO/CIO, not payments head). The experience of FIS (trying to cross-sell Finxact alongside legacy core products) shows that intra-company cannibalization and organizational resistance are real barriers.

8. **The overlay delay effect should be acknowledged as a competitive risk.** If Zafin and SunTec solve banks' immediate deposit pricing problems in 8 weeks, the business case for a 3-year Tachyon deployment weakens. Part II should address how the Evolution Fabric thesis creates urgency that overlays cannot satisfy.
